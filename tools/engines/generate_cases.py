#!/usr/bin/env python3
"""Generate random single-filer returns inside the proof-of-concept scope.

Deterministic for a given seed. Every amount is integer cents. The economic
facts an external engine needs (net gains, totals) are derived here from the
same raw facts the project receives, independently of the project's own
Form 8949 and Schedule D logic.

Output: a JSON array of { id, inputs, facts, features } where `inputs` is the
project's interview input map, `facts` the engine-facing economic summary and
`features` the flags the comparison uses for exclusion rules.
"""
import argparse, json, random

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
        "f1040.status": "single", "$person": ["taxpayer"], "person[taxpayer].rrta": False,
        "sb.unsupported": False, "sb.line7a": False, "sb.fbar_required": False, "sb.form8938": False, "sb.line8": False,
        "div.box2c": 0, "div.box2e": 0, "div.box2f": 0, "div.box3": 0, "div.box4": 0, "div.box6": 0,
        "div.box9": 0, "div.box10": 0, "div.box12": 0, "div.box13": 0, "div.basis_reconciled": True, "div.fatca": False,
        "sd.other_forms": False, "sd.carryover": False,
        "qbi.unsupported": False,
        "f4952.line4g": 0, "f4952.carryover": False, "f4952.unsupported": False, "f4952.alternative_allocation": False,
        "f8959.unsupported": False, "f8960.unsupported": False, "f8960.refund": False, "f8960.allocated_taxes": 0,
        "ftc.all_passive": True, "ftc.statements": True, "ftc.eligible": True, "ftc.elect": True,
        "s3.line9": 0, "s3.line10": 0, "s3.line12": 0, "s3.line14": 0,
        "sa.unsupported": False, "sa.charity_limited": False, "sa.excluded_income": False, "sa.dependent": False,
        "sa.spouse_extra": False, "sa.age65": False, "sa.blind": False, "sa.spouse_itemizes": False, "sa.elect_itemize": False,
        "sa.line5c": 0,
        "scope.schedule1": False, "scope.schedule1a": False, "scope.credits": False, "scope.other_income": False,
        "scope.other_line16": False, "s2.amt": False, "s2.other": False,
        "f1040.line25b": 0, "f1040.line25c": 0, "f1040.line26": 0, "f1040.line35a": 0, "f1040.line36": 0,
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

    # Foreign tax within the simple-path limit.
    ftc = rng.randint(100, 30_000) if rng.random() < 0.25 else 0
    inputs["ftc.taxes"] = ftc; facts["foreign_tax"] = ftc
    if ftc: features.add("foreign_tax")

    return {"id": f"gen-{i:05d}", "inputs": inputs, "facts": facts, "features": sorted(features)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=20260101)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    cases = [gen_case(rng, i) for i in range(a.count)]
    with open(a.out, "w") as f:
        json.dump(cases, f)
    print(f"generated {len(cases)} cases (seed {a.seed}) -> {a.out}")


if __name__ == "__main__":
    main()
