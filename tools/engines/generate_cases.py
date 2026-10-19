#!/usr/bin/env python3
"""Generate random returns inside the supported scope: single and head of household returns, then
married filing jointly returns built on the same draws with a spouse added.

Deterministic for a given seed. Every amount is integer cents. The economic
facts an external engine needs (net gains, totals) are derived here from the
same raw facts the project receives, independently of the project's own
Form 8949 and Schedule D logic.

Output: a JSON array of { id, inputs, facts, features } where `inputs` is the
project's interview input map, `facts` the engine-facing economic summary and
`features` the flags the comparison uses for exclusion rules.
"""
import argparse, json, random

TAXPAYER = "person[taxpayer]"
HSA = f"{TAXPAYER}.f8889[hsa]"

WAGE_BASE = 17_610_000        # 2025 Social Security wage base, cents
SS_RATE = (62, 1000)
MEDICARE_RATE = (145, 10000)
ADDL_MEDICARE_RATE = (9, 1000)
ADDL_MEDICARE_START = 20_000_000


def half_up(n, d):
    return (2 * n + d) // (2 * d)


def rate(amount, r):
    return half_up(amount * r[0], r[1])


def log_uniform(rng, lo, hi):
    import math
    return int(round(math.exp(rng.uniform(math.log(lo), math.log(hi)))))


def gen_case(rng, i):
    inputs = {
        "f1040.status": "single", "$person": ["taxpayer"], "person[taxpayer].role": "taxpayer", "person[taxpayer].rrta": False,
        "sb.unsupported": False, "sb.line7a": False, "sb.fbar_required": False, "sb.form8938": False, "sb.line8": False,
        "div.box2c": 0, "div.box2e": 0, "div.box2f": 0, "div.box3": 0,
        "div.box9": 0, "div.box10": 0, "div.box13": 0, "div.basis_reconciled": True,
        "sd.other_forms": False, "sd.carryover": False,
        "qbi.unsupported": False,
        "f4952.line4g": 0, "f4952.carryover": False, "f4952.unsupported": False, "f4952.alternative_allocation": False,
        "f8959.unsupported": False, "f8960.unsupported": False, "f8960.refund": False, "f8960.allocated_taxes": 0,
        "ftc.all_passive": True, "ftc.statements": True, "ftc.eligible": True, "ftc.elect": True,
        "s3.line9": 0, "s3.line10": 0, "s3.line12": 0, "s3.line14": 0,
        "sa.unsupported": False, "sa.charity_limited": False, "sa.excluded_income": False, "sa.dependent": False,
        "sa.spouse_extra": False, "person[taxpayer].age65": False, "person[taxpayer].blind": False, "sa.spouse_itemizes": False, "sa.elect_itemize": False,
        "sa.line5c": 0,
        "scope.schedule1": False, "scope.credits": False, "scope.other_income": False,
        "scope.other_line16": False, "s2.amt": False, "s2.other": False,
        "f1040.line25b": 0, "f1040.line25c": 0, "f1040.line26": 0, "f1040.line35a": 0, "f1040.line36": 0,
        # Earned income credit questions: an adult aged 25 to 64 living in the United States who is
        # nobody's qualifying child, with no tax-exempt interest.
        "f1040.tax_exempt_interest": 0, "div.box12": 0, "eic.qc_of_another": False, "person[taxpayer].born_before_2001": True, "person[taxpayer].born_after_1960": True, "eic.us_home": True, "eic.married": False,
        "$retirement": [],
    }
    facts = {}
    features = set()

    # Wages: one or two employers; sometimes high enough for excess Social Security
    # withholding, Additional Medicare Tax and the net investment income tax.
    n_emp = 1 if rng.random() < 0.5 else 2
    tier = rng.random()
    hi = 40_000_000 if tier < 0.15 else (25_000_000 if tier < 0.4 else 15_000_000)
    employers, wages, withheld, ss_withheld, medicare_wages = [], 0, 0, 0, 0
    for k in range(n_emp):
        w = log_uniform(rng, 500_000, hi)
        box3 = min(w, WAGE_BASE)
        e = {"box1": w, "box2": rate(w, (rng.randint(8, 25), 100)), "box3": box3, "box4": rate(box3, SS_RATE),
             "box5": w, "box6": rate(w, MEDICARE_RATE) + (rate(w - ADDL_MEDICARE_START, ADDL_MEDICARE_RATE) if w > ADDL_MEDICARE_START else 0),
             "box7": 0}
        employers.append(e); wages += w; withheld += e["box2"]; ss_withheld += e["box4"]; medicare_wages += w
    inputs["$w2@person[taxpayer]"] = [f"emp_{chr(97 + k)}" for k in range(n_emp)]
    for k, e in enumerate(employers):
        for box, v in e.items():
            inputs[f"person[taxpayer].w2[emp_{chr(97 + k)}].{box}"] = v
    facts.update(wages=wages, withheld=withheld, medicare_wages=medicare_wages)
    if n_emp == 2 and sum(e["box3"] for e in employers) > WAGE_BASE:
        features.add("excess_social_security")

    # Interest
    n_int = rng.choice([0, 1, 1, 2])
    inputs["$interest"] = [f"bank_{chr(97 + k)}" for k in range(n_int)]
    interest = 0
    for k in range(n_int):
        a = log_uniform(rng, 1_000, 5_000_000); inputs[f"interest[bank_{chr(97 + k)}].amount"] = a; interest += a
    facts["interest"] = interest

    # Dividends: ordinary includes qualified; section 199A dividends are a separate subset.
    ordinary = 0 if rng.random() < 0.4 else log_uniform(rng, 1_000, 8_000_000)
    qualified = rate(ordinary, (rng.randint(0, 100), 100)) if ordinary else 0
    qbi_div = rate(ordinary, (rng.randint(0, 20), 100)) if ordinary and rng.random() < 0.3 else 0
    inputs["sb.ordinary_dividends"] = ordinary; inputs["f1040.line3a"] = qualified; inputs["qbi.dividends"] = qbi_div
    facts.update(ordinary_dividends=ordinary, qualified_dividends=qualified, section_199a_dividends=qbi_div)
    if qbi_div: features.add("qbi_dividends")
    distributions = 0 if rng.random() < 0.5 else log_uniform(rng, 1_000, 2_000_000)
    inputs["sd.distributions"] = distributions; facts["capital_gain_distributions"] = distributions
    # Special-rate gains reported on Form 1099-DIV (boxes 2b and 2d) select the Schedule D Tax Worksheet.
    box2b = box2d = 0
    if distributions and rng.random() < 0.15:
        box2b = rate(distributions, (rng.randint(0, 50), 100)); features.add("special_gains")
    if distributions and rng.random() < 0.1:
        box2d = rate(distributions - box2b, (rng.randint(0, 50), 100)); features.add("special_gains")
    inputs["div.box2b"] = box2b; inputs["div.box2d"] = box2d
    facts.update(unrecaptured_1250=box2b, gain_28pct=box2d)

    # Sales: Form 8949 boxes A/B (short) and D/E (long), detail route, code none or W.
    n_sales = rng.choice([0, 0, 1, 2, 3])
    inputs["$sales"] = [f"s{k + 1}" for k in range(n_sales)]
    st_gain = lt_gain = 0
    for k in range(n_sales):
        key = f"sales[s{k + 1}]"
        box = rng.choice(["A", "B", "D", "E"])
        proceeds = log_uniform(rng, 100_000, 10_000_000)
        basis = int(proceeds * rng.uniform(0.5, 1.5))
        code = "none"; wash = 0
        if proceeds < basis and rng.random() < 0.25:
            code = "W"; wash = rng.randint(1, basis - proceeds); features.add("wash_sale")
        inputs.update({f"{key}.box": box, f"{key}.route": "detail", f"{key}.code": code, f"{key}.special": False,
                       f"{key}.aggregate_eligible": False, f"{key}.proceeds": proceeds,
                       f"{key}.reported_basis": basis, f"{key}.correct_basis": basis, f"{key}.wash_loss": wash})
        gain = proceeds - basis + wash
        if box in ("A", "B"): st_gain += gain
        else: lt_gain += gain
    facts.update(short_term_gain=st_gain, long_term_gain=lt_gain)
    if n_sales: features.add("sales")

    # Itemized deductions, offered on about half the cases. Gifts stay well under the
    # income limits so the project's limitation screen does not fire.
    itemize = rng.random() < 0.5
    medical = log_uniform(rng, 10_000, 3_000_000) if itemize and rng.random() < 0.5 else 0
    salt_income = min(log_uniform(rng, 50_000, 6_000_000), wages // 10) if itemize else 0
    salt_re = log_uniform(rng, 50_000, 2_000_000) if itemize and rng.random() < 0.6 else 0
    mortgage = log_uniform(rng, 100_000, 4_000_000) if itemize and rng.random() < 0.6 else 0
    cash_gifts = min(log_uniform(rng, 10_000, 2_000_000), wages // 8) if itemize and rng.random() < 0.6 else 0
    noncash = min(log_uniform(rng, 10_000, 500_000), wages // 20) if itemize and rng.random() < 0.3 else 0
    inv_interest = log_uniform(rng, 10_000, 1_000_000) if itemize and rng.random() < 0.3 else 0
    inputs.update({"sa.line1": medical, "sa.line5a": salt_income, "sa.line5b": salt_re, "sa.line8a": mortgage,
                   "sa.line11": cash_gifts, "f4952.line1": inv_interest})
    inputs["$gift"] = ["items"] if noncash else []
    if noncash:
        inputs.update({"gift[items].deduction": noncash, "gift[items].public_securities": False, "gift[items].special": False})
    facts.update(medical=medical, salt_income_tax=salt_income, salt_real_estate=salt_re, mortgage_interest=mortgage,
                 cash_gifts=cash_gifts, noncash_gifts=noncash, investment_interest=inv_interest)
    if itemize: features.add("itemized_items")
    if distributions: features.add("capital_gain_distributions")
    if inv_interest: features.add("investment_interest")

    # Dependents: children who qualify in full (citizen, SSN, lived all year, supported),
    # under 17 for the child tax credit or 17-23 full-time students for the credit for
    # other dependents; head of household when a child qualifies, on half of those cases.
    n_children = rng.choice([0, 0, 0, 1, 1, 2, 3])
    ages = [rng.randint(0, 16) if rng.random() < 0.75 else rng.randint(17, 23) for _ in range(n_children)]
    inputs["$dependent"] = [f"child_{k + 1}" for k in range(n_children)]
    for k, age in enumerate(ages):
        key = f"dependent[child_{k + 1}]"
        inputs.update({f"{key}.relationship": "child", f"{key}.age": age, f"{key}.younger": True, f"{key}.student": age >= 17, f"{key}.disabled": False,
                       f"{key}.months": 12, f"{key}.self_support": False, f"{key}.joint_return": False, f"{key}.citizen": True,
                       f"{key}.canada_mexico": False, f"{key}.married": False, f"{key}.tin": True, f"{key}.work_ssn": True,
                       f"{key}.gross_income": 0, f"{key}.supported": True, f"{key}.other_claimant": False,
                       f"{key}.divorced_rule": False, f"{key}.multiple_support": False, f"{key}.parent_home_paid": False,
                       f"{key}.us_half": True, f"{key}.eic_ssn": True})
    hoh = n_children > 0 and rng.random() < 0.5
    inputs["f1040.status"] = "hoh" if hoh else "single"
    inputs.update({"person[taxpayer].tin": True, "person[taxpayer].work_ssn": True,
                   "household.home_cost": True, "household.unmarried": True, "s8812.combat_pay": False, "s8812.puerto_rico": False})
    # Every generated child is a qualifying child for the EIC (under 19, or a full-time student under 24,
    # living with the filer in the United States all year, with an SSN).
    facts.update(children=ages, n24=sum(1 for a in ages if a < 17), hoh=hoh, eic_children=min(3, n_children))
    if n_children:
        features.add("dependents")
    if any(a >= 17 for a in ages):
        features.add("other_dependents")
    if hoh:
        features.add("head_of_household")
    if facts["n24"] >= 3:
        features.add("three_or_more_children")

    # Social security benefits on a third of returns (no Form 1099-R distributions: engines take
    # taxable pensions as an input, so only the benefits worksheet is compared).
    ss = log_uniform(rng, 100_000, 4_500_000) if rng.random() < 0.33 else 0
    inputs.update({"ssb.benefits": ss, "ssb.pub915": False, "ssb.lump_sum": False, "ssb.terror_disability": False})
    facts["ss_benefits"] = ss
    if ss: features.add("social_security")

    # Schedule 1 items. Unemployment compensation and educator expenses on some returns; an HSA with
    # one coverage type all year, so the deduction is the smaller of the contributions and the limit
    # less employer contributions (Form 8889 lines 3, 12 and 13); student loan interest, whose phase-out
    # PolicyEngine-US computes from the interest paid.
    uc = log_uniform(rng, 100_000, 2_500_000) if rng.random() < 0.2 else 0
    inputs.update({"s1.uc_paid": uc, "s1.uc_repaid": 0, "s1.uc_unsupported": False}); facts["unemployment"] = uc
    if uc: features.add("unemployment")
    edu = rng.randint(1_000, 60_000) if rng.random() < 0.1 else 0
    inputs.update({"person[taxpayer].educator_expenses": edu, "person[taxpayer].eligible_educator": True})
    facts.update(educator_expenses=edu, educator_deduction=min(edu, 30_000))
    if edu: features.add("educator_expenses")
    contrib = employer = hsa_deduction = 0
    if rng.random() < 0.15:
        family = rng.random() < 0.4; age55 = rng.random() < 0.2
        limit = (855_000 if family else 430_000) + (100_000 if age55 else 0)
        employer = rng.randint(0, limit // 2) if rng.random() < 0.5 else 0
        contrib = rng.randint(0, limit - employer)
        hsa_deduction = min(contrib, limit - employer)
        inputs.update({f"{HSA}.months_eligible": 12, f"{HSA}.months_family": 12 if family else 0, f"{HSA}.age55": age55,
                       f"{HSA}.dec_coverage": "family" if family else "self_only", f"{HSA}.last_month": False, f"{HSA}.unsupported": False})
        features.add("hsa")
    inputs.update({f"$f8889@{TAXPAYER}": ["hsa"], f"{HSA}.line2": contrib, f"{HSA}.line9": employer}); facts["hsa_deduction"] = hsa_deduction
    sli = rng.randint(1_000, 300_000) if rng.random() < 0.15 else 0
    inputs.update({"sli.interest": sli, "sli.claimed": False}); facts["student_loan_interest"] = sli
    if sli: features.add("student_loan_interest")

    # Foreign tax within the simple-path limit.
    ftc = rng.randint(100, 30_000) if rng.random() < 0.25 else 0
    inputs["ftc.taxes"] = ftc; facts["foreign_tax"] = ftc
    if ftc: features.add("foreign_tax")

    # Schedule 1-A. A separate generator per case leaves every earlier draw, and so the case ids
    # recorded in engine_investigations.json, unchanged. Seniors are 66 or older (born before
    # January 2, 1961, with no question about a final return); tips, the FLSA overtime premium and
    # car loan interest come from one employer or one new qualifying loan, below the wages.
    r = random.Random(f"s1a:{i}")
    inputs.update({"s1a.tips": False, "s1a.overtime": False, "s1a.carloan": False})
    age = 40
    if r.random() < 0.15:
        age = r.randint(66, 85)
        inputs.update({"person[taxpayer].age65": True, "person[taxpayer].died_before_65": False, "person[taxpayer].born_after_1960": False})
        features.add("senior")
    tips = r.randint(10_000, min(4_000_000, wages)) if r.random() < 0.12 else 0
    if tips:
        inputs.update({"s1a.tips": True, "$tipjob@person[taxpayer]": ["t"], "person[taxpayer].tipjob[t].qualified": True, "person[taxpayer].tipjob[t].amount": tips})
        features.add("tips")
    overtime = r.randint(10_000, min(2_000_000, wages // 3)) if r.random() < 0.12 and wages >= 30_000 else 0
    if overtime:
        inputs.update({"s1a.overtime": True, "$otjob@person[taxpayer]": ["o"], "person[taxpayer].otjob[o].flsa": True, "person[taxpayer].otjob[o].special_rule": False,
                       "person[taxpayer].otjob[o].method": "premium", "person[taxpayer].otjob[o].statement": overtime})
        features.add("overtime")
    car = r.randint(5_000, 1_500_000) if r.random() < 0.1 else 0
    if car:
        inputs.update({"s1a.carloan": True, "$carloan": ["v"], "carloan[v].kind": "original", "carloan[v].requirements": True,
                       "carloan[v].vehicle": True, "carloan[v].mixed": False, "carloan[v].interest": car})
        features.add("car_loan_interest")
    facts.update(age=age, tips=tips, overtime=overtime, car_loan_interest=car)
    return {"id": f"gen-{i:05d}", "inputs": inputs, "facts": facts, "features": sorted(features)}


SPOUSE = "person[spouse]"


def make_joint(case, j):
    """A married filing jointly return: the generated return, with a spouse who may have wages
    (one or two employers) and may be 66 or older. A separate generator keeps every single-filer
    case unchanged."""
    r = random.Random(f"mfj:{j}")
    inputs, facts, features = case["inputs"], case["facts"], set(case["features"]) - {"head_of_household"}
    inputs["f1040.status"] = "mfj"; inputs["$person"] = ["taxpayer", "spouse"]
    inputs["household.unmarried"] = False
    age = r.randint(66, 85) if r.random() < 0.15 else r.randint(25, 64)
    inputs.update({f"{SPOUSE}.role": "spouse", f"{SPOUSE}.rrta": False, f"{SPOUSE}.tin": True, f"{SPOUSE}.work_ssn": True,
                   f"{SPOUSE}.age65": age >= 66, f"{SPOUSE}.blind": False, f"{SPOUSE}.born_before_2001": True,
                   f"{SPOUSE}.born_after_1960": age < 66, f"{SPOUSE}.educator_expenses": 0,
                   f"$tipjob@{SPOUSE}": [], f"$otjob@{SPOUSE}": [], f"$f8889@{SPOUSE}": []})
    if age >= 66:
        inputs[f"{SPOUSE}.died_before_65"] = False; features.add("spouse_senior")
    n_emp = 0 if r.random() < 0.3 else (1 if r.random() < 0.6 else 2)
    keys = [f"emp_{chr(97 + k)}" for k in range(n_emp)]
    inputs[f"$w2@{SPOUSE}"] = keys
    wages = medicare = withheld = 0; box3s = []
    for k in keys:
        w = log_uniform(r, 500_000, 25_000_000)
        box3 = min(w, WAGE_BASE)
        e = {"box1": w, "box2": rate(w, (r.randint(8, 25), 100)), "box3": box3, "box4": rate(box3, SS_RATE), "box5": w,
             "box6": rate(w, MEDICARE_RATE) + (rate(w - ADDL_MEDICARE_START, ADDL_MEDICARE_RATE) if w > ADDL_MEDICARE_START else 0), "box7": 0}
        for box, v in e.items(): inputs[f"{SPOUSE}.w2[{k}].{box}"] = v
        wages += w; medicare += w; withheld += e["box2"]; box3s.append(box3)
    if n_emp == 2 and sum(box3s) > WAGE_BASE:
        features.add("excess_social_security")
    facts.update(joint=True, hoh=False, spouse_age=age, spouse_wages=wages, withheld=facts["withheld"] + withheld,
                 medicare_wages=facts["medicare_wages"] + medicare)
    features.add("joint")
    return {"id": f"mfj-{j:05d}", "inputs": inputs, "facts": facts, "features": sorted(features)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=1000)
    ap.add_argument("--joint", type=int, default=400)
    ap.add_argument("--seed", type=int, default=20260101)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    cases = [gen_case(rng, i) for i in range(a.count)]
    cases += [make_joint(gen_case(random.Random(f"mfj-base:{a.seed}:{j}"), 100_000 + j), j) for j in range(a.joint)]
    with open(a.out, "w") as f:
        json.dump(cases, f)
    print(f"generated {len(cases)} cases (seed {a.seed}) -> {a.out}")


if __name__ == "__main__":
    main()
