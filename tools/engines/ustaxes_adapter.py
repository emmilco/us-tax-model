#!/usr/bin/env python3
"""UsTaxes as an engine for the differential: the generated returns built as UsTaxes'
`Information` and run through its Form 1040 model, in one Node process, from the clone in
.engines/ustaxes-src/ as shipped.

UsTaxes (https://github.com/ustaxes/UsTaxes, TypeScript, AGPL-3.0) is a browser application
whose tax logic is a set of form classes under src/forms/Y<year>/irsForms/, each line a method
recomputed on every call. tools/engines/ustaxes/run.mjs loads those sources through module hooks
(hooks.mjs: the TypeScript compiler UsTaxes pins, from .engines/ustaxes-deps/), builds each
return with the year's entry point `create1040(info, assets)` (Main.ts) and reads the lines back
by their accessor names. Nothing is attached to the forms after construction, so a form UsTaxes
does not build is not reached: Schedule C is never constructed (F1040.ts declares `scheduleC?`
and no code assigns it), so returns with self-employment income are not run (the `self_employed`
limitation below).

Every amount is a JavaScript double in dollars, never rounded by the engine; the adapter turns
each into integer cents by rounding to the nearest cent. UsTaxes emulates the Tax Table by
applying the rate schedule at the midpoint of the table's band without the table's rounding to
whole dollars (TaxTable.ts `computeTax`); compare.py models that method exactly as the
`table-midpoint` category ("tax_table": "midpoint-unrounded" in the engine record).

Inputs the adapter supplies that the project computes rather than receives are declared in
USTAXES_PASS_THROUGH; project result lines UsTaxes does not compute are listed there with the
reason; every known UsTaxes defect that moves a mapped line is a limitation in `limitations()`,
keyed by the generator feature (or a feature read off the project's values or reported by this
adapter) that triggers it, and names the UsTaxes source location.
"""
import json
import re
import os
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
USTAXES_SRC = ROOT / ".engines" / "ustaxes-src"
USTAXES_DEPS = ROOT / ".engines" / "ustaxes-deps"
RUNNER = Path(__file__).resolve().parent / "ustaxes"
ENGINE_NAME = "UsTaxes"
TAXPAYER = "person[taxpayer]"
SPOUSE = "person[spouse]"
HSA = f"{TAXPAYER}.f8889[hsa]"


def dollars(c):
    return c / 100.0


def cents(x):
    return int(round(float(x) * 100))


# ---------------------------------------------------------------------------------------------
# Package discovery and version


def available(year):
    """Whether the clone, its runtime packages and the tax year's forms are present."""
    return (USTAXES_SRC / "src" / "forms" / f"Y{year}" / "irsForms" / "Main.ts").exists() and all(
        (USTAXES_DEPS / "node_modules" / p / "package.json").exists() for p in ("lodash", "loglevel", "typescript"))


def package_version():
    """The clone's package.json version and its git HEAD commit, read from the files (no git call)."""
    version = json.loads((USTAXES_SRC / "package.json").read_text()).get("version", "unknown")
    git = USTAXES_SRC / ".git"
    head = (git / "HEAD").read_text().strip() if (git / "HEAD").exists() else ""
    commit = head
    if head.startswith("ref: "):
        ref = head[5:]
        if (git / ref).exists():
            commit = (git / ref).read_text().strip()
        elif (git / "packed-refs").exists():
            commit = next((l.split()[0] for l in (git / "packed-refs").read_text().splitlines() if l.endswith(" " + ref)), "unknown")
    return version, commit[:12]


# ---------------------------------------------------------------------------------------------
# Input mapping: the case's facts and interview inputs as UsTaxes' Information


STATUS = {"single": "S", "mfj": "MFJ", "hoh": "HOH", "mfs": "MFS", "qss": "W"}


def birth(year, age):
    """A date of birth giving `age` at the end of the tax year; UsTaxes reads ages from it
    (65 or older: born before January 2, 1961; 55 for the HSA catch-up; children by birth year)."""
    return [year - age, 7, 1]


def person(role, year, age):
    return {"firstName": role.title(), "lastName": "Generated", "ssid": "123456789" if role == "PRIMARY" else "987654321", "role": role,
            "isBlind": False, "dateOfBirth": birth(year, age)}


def w2s(inputs, who, role, box12=None):
    out = []
    for k, key in enumerate(inputs.get(f"$w2@{who}", [])):
        b = lambda n: dollars(inputs[f"{who}.w2[{key}].box{n}"])
        w = {"occupation": "employee", "income": b(1), "fedWithholding": b(2), "ssWages": b(3), "ssWithholding": b(4),
             "medicareIncome": b(5), "medicareWithholding": b(6), "personRole": role, "state": "TX"}
        if k == 0 and box12:
            w["box12"] = box12
        out.append(w)
    return out


def build_info(case, year):
    """UsTaxes' Information and Asset[] for one generated return. Dates are [y, m, d]."""
    f, inputs = case["facts"], case["inputs"]
    status = inputs["f1040.status"]
    joint = bool(f.get("joint"))
    hsa = "hsa" in case["features"]
    age = f.get("age", 40)
    # The HSA catch-up contribution (Form 8889 line 7) follows the date of birth in UsTaxes; the
    # generator answers the age-55 question on its own, so a filer under 55 who answered yes is 56.
    if hsa and inputs.get(f"{HSA}.age55") and age < 55:
        age = 56
    primary = {**person("PRIMARY", year, age), "isTaxpayerDependent": False,
               "address": {"address": "1 Main St", "city": "Austin", "state": "TX", "zip": "78701"}}
    tp = {"filingStatus": STATUS[status], "primaryPerson": primary, "dependents": []}
    if joint:
        tp["spouse"] = {**person("SPOUSE", year, f.get("spouse_age", 40)), "isTaxpayerDependent": False}
    for i, a in enumerate(f.get("children", [])):
        tp["dependents"].append({**person("DEPENDENT", year, a), "firstName": f"Child{i + 1}", "ssid": f"55500{i:04d}",
                                 "relationship": "child", "qualifyingInfo": {"numberOfMonths": 12, "isStudent": a >= 17}})
    box12 = {"W": dollars(inputs.get(f"{HSA}.line9", 0))} if hsa and inputs.get(f"{HSA}.line9", 0) else None
    f1099s = [{"payer": f"Bank {k}", "type": "INT", "personRole": "PRIMARY", "form": {"income": dollars(inputs[f"interest[{k}].amount"])}}
              for k in inputs.get("$interest", [])]
    if f["ordinary_dividends"] or f["capital_gain_distributions"]:
        f1099s.append({"payer": "Fund", "type": "DIV", "personRole": "PRIMARY",
                       "form": {"dividends": dollars(f["ordinary_dividends"]), "qualifiedDividends": dollars(f["qualified_dividends"]),
                                "totalCapitalGainsDistributions": dollars(f["capital_gain_distributions"])}})
    if f.get("ss_benefits"):
        f1099s.append({"payer": "SSA", "type": "SSA", "personRole": "PRIMARY",
                       "form": {"netBenefits": dollars(f["ss_benefits"]), "federalIncomeTaxWithheld": 0}})
    other = {}
    if f.get("unemployment"):
        other["unemploymentCompensation"] = dollars(f["unemployment"])
    if f.get("educator_expenses"):
        other["educatorExpenses"] = dollars(f["educator_expenses"])
    if f.get("ira_contribution"):
        other["iraDeduction"] = dollars(f["ira_contribution"])
    if f.get("foreign_tax"):
        other["foreignTaxCredit"] = dollars(f["foreign_tax"])
    if f.get("investment_interest_carryover"):
        other["priorYearInvestmentInterestCarryover"] = dollars(f["investment_interest_carryover"])
    info = {
        "f1099s": f1099s, "w2s": w2s(inputs, TAXPAYER, "PRIMARY", box12) + (w2s(inputs, SPOUSE, "SPOUSE") if joint else []),
        "realEstate": [], "estimatedTaxes": [], "f3921s": [], "scheduleK1Form1065s": [], "questions": {}, "stateResidencies": [{"state": "TX"}],
        "taxPayer": tp,
        "f1098es": [{"lender": "Lender", "interest": dollars(f["student_loan_interest"])}] if f.get("student_loan_interest") else [],
        "itemizedDeductions": {
            "medicalAndDental": dollars(f["medical"]), "stateAndLocalTaxes": dollars(f["salt_income_tax"]), "isSalesTax": False,
            "stateAndLocalRealEstateTaxes": dollars(f["salt_real_estate"]), "stateAndLocalPropertyTaxes": 0,
            "interest8a": dollars(f["mortgage_interest"]), "interest8b": 0, "interest8c": 0, "interest8d": 0,
            "investmentInterest": dollars(f["investment_interest"]), "charityCashCheck": dollars(f["cash_gifts"]),
            "charityOther": dollars(f["noncash_gifts"])},
        "healthSavingsAccounts": [], "individualRetirementArrangements": [], "credits": [],
        "obbbDeductions": {"qualifiedTips": dollars(f.get("tips", 0)), "qualifiedOvertimePremium": dollars(f.get("overtime", 0)),
                           "carLoanVehicles": [{"vin": "1GENERATED0000000", "interestPaid": dollars(f["car_loan_interest"])}]
                           if f.get("car_loan_interest") else []},
        "otherIncome": other,
    }
    if f.get("marketplace"):
        mk = f["marketplace"]
        adv = [mk["advance"] // 12] * 11 + [mk["advance"] - 11 * (mk["advance"] // 12)]
        info["marketplace1095As"] = [{"monthlyPremiums": [dollars(mk["premium"])] * 12, "monthlySlcsp": [dollars(mk["slcsp"])] * 12,
                                      "monthlyAdvancePtc": [dollars(x) for x in adv]}]
    if f.get("education"):
        # Form 8863: per student the adjusted qualified education expenses and whether the student is an AOC student
        # (UsTaxes' EducationExpenses: aotcQualifiedExpenses with aotcEligible, or llcQualifiedExpenses).
        info["educationExpenses"] = [{"studentName": str(s["who"]), "isDependent": s["who"] not in ("taxpayer", "spouse"),
                                      "aotcEligible": bool(s["aoc"]), "aotcQualifiedExpenses": dollars(s["aoc_expenses"]),
                                      "llcQualifiedExpenses": dollars(s["llc_expenses"])} for s in f["education"]["students"]]
    if f.get("capital_loss_carryover_st") or f.get("capital_loss_carryover_lt"):
        # Entered as positive amounts; UsTaxes puts them on Schedule D lines 4 and 11 (ScheduleD.ts `l4`, `l11`),
        # where the form prints them on lines 6 and 14; lines 7 and 15 are the same either way.
        info["priorYearCapitalLossCarryover"] = {"shortTerm": dollars(f["capital_loss_carryover_st"]),
                                                 "longTerm": dollars(f["capital_loss_carryover_lt"])}
    if hsa:
        family = inputs.get(f"{HSA}.months_family", 0) == 12
        info["healthSavingsAccounts"].append({"label": "HSA", "coverageType": "family" if family else "self-only",
                                              "contributions": dollars(inputs[f"{HSA}.line2"]), "personRole": "PRIMARY",
                                              "startDate": [year, 1, 1], "endDate": [year, 12, 31],
                                              "totalDistributions": 0, "qualifiedDistributions": 0})
    if f.get("ira_contribution") or f.get("roth_contribution"):
        info["individualRetirementArrangements"].append({
            "payer": "IRA", "personRole": "PRIMARY", "grossDistribution": 0, "taxableAmount": 0, "taxableAmountNotDetermined": False,
            "totalDistribution": False, "federalIncomeTaxWithheld": 0, "planType": "IRA",
            "contributions": dollars(f.get("ira_contribution", 0) + f.get("roth_contribution", 0)), "rolloverContributions": 0,
            "rothIraConversion": 0, "recharacterizedContributions": 0, "requiredMinimumDistributions": 0, "lateContributions": 0,
            "repayments": 0})
    if f.get("care_expenses"):
        info["dependentCareExpenses"] = {"qualifyingPersonCount": f["care_persons"], "totalExpenses": dollars(f["care_expenses"])}
    part1 = f.get("energy_part1") or {}
    if part1:
        info["credits"].append({"recipient": "PRIMARY", "type": "CreditType/ResidentialCleanEnergyCost", "amount": dollars(sum(part1.values()))})
    if f.get("energy_part2"):
        # Form 5695 Part II enters UsTaxes as the credit itself (CreditType.EnergyEfficientHomeImprovement:
        # "the computed credit (pre-calculated by taxpayer)"): the generator's amount before the limit.
        part1_credit = (sum(part1.values()) * 30 + 50) // 100 if part1 else 0
        info["credits"].append({"recipient": "PRIMARY", "type": "CreditType/EnergyEfficientHomeImprovement",
                                "amount": dollars(f["energy_credit"] - part1_credit)})
    assets = []
    for s in inputs.get("$sales", []):
        key = f"sales[{s}]"
        long_term = inputs[f"{key}.box"] in ("D", "E")
        a = {"name": s, "positionType": "Security", "openDate": [year - 2, 1, 2] if long_term else [year, 1, 2], "closeDate": [year, 6, 30],
             "openPrice": dollars(inputs[f"{key}.reported_basis"]), "openFee": 0, "closePrice": dollars(inputs[f"{key}.proceeds"]),
             "closeFee": 0, "quantity": 1}
        if inputs[f"{key}.code"] == "W":
            a.update({"adjustmentCode": "W", "adjustmentAmount": dollars(inputs[f"{key}.wash_loss"])})
        assets.append(a)
    return info, assets


# ---------------------------------------------------------------------------------------------
# Line map: project line id <- UsTaxes accessor (tools/engines/ustaxes/run.mjs output names)

F1040_MAP = {
    "f1040.line1a": "f1040.l1a", "f1040.line1z": "f1040.l1z", "f1040.line6b": "f1040.l6b", "f1040.line7a": "f1040.l7a",
    "f1040.line8": "f1040.l8", "f1040.line9": "f1040.l9", "f1040.line10": "f1040.l10", "f1040.line11a": "f1040.l11a",
    "f1040.line11b": "f1040.l11b", "f1040.line12e": "f1040.l12e", "f1040.line13a": "f1040.l13a", "f1040.line13b": "f1040.l13b",
    "f1040.line14": "f1040.l14", "f1040.line15": "f1040.l15", "f1040.line16": "f1040.l16", "f1040.line17": "f1040.l17",
    "f1040.line18": "f1040.l18", "f1040.line19": "f1040.l19", "f1040.line20": "f1040.l20", "f1040.line21": "f1040.l21",
    "f1040.line22": "f1040.l22", "f1040.line23": "f1040.l23", "f1040.line24": "f1040.l24", "f1040.line25a": "f1040.l25a",
    "f1040.line25d": "f1040.l25d", "f1040.line27a": "f1040.l27a", "f1040.line28": "f1040.l28", "f1040.line32": "f1040.l32",
    "f1040.line33": "f1040.l33", "f1040.line34": "f1040.l34", "f1040.line37": "f1040.l37",
    "s1.line10": "s1.l10", "s1.line11": "s1.l11", "s1.line13": "s1.l13", "s1.line21": "s1.l21", "s1.line26": "s1.l26",
    "s2.line21": "s2.l21", "s3.line8": "f1040.l20", "s3.line11": "s3.l11", "s3.line15": "f1040.l31",
    "sa.line3": "sa.l3", "sa.line4": "sa.l4", "sa.line5d": "sa.l5d", "sa.line5e": "sa.l5e", "sa.line7": "sa.l7", "sa.line8e": "sa.l8e",
    "sa.line10": "sa.l10", "sa.line14": "sa.l14", "sa.line17": "sa.l17", "sa.standard": "f1040.standardDeduction",
    "sa.deduction": "f1040.l12e",
    "sb.line2": "sb.l2", "sb.line4": "sb.l4",
    "sd.line7": "sd.l7", "sd.line15": "sd.l15", "sd.line16": "sd.l16", "sd.line21": "sd.l21",
    "f8959.line1": "f8959.l1", "f8959.line4": "f8959.l4", "f8959.line6": "f8959.l6", "f8959.line7": "f8959.l7", "f8959.line18": "f8959.l18",
    "f8959.line19": "f8959.l19", "f8959.line21": "f8959.l21", "f8959.line22": "f8959.l22", "f8959.line24": "f8959.l24",
    "f8959.tax": "f8959.l18",
    "f8960.line8": "f8960.l8", "f8960.line9a": "f8960.l9a", "f8960.line9b": "f8960.l9b", "f8960.line9d": "f8960.l9d",
    "f8960.line11": "f8960.l11", "f8960.line12": "f8960.l12", "f8960.line15": "f8960.l15", "f8960.line16": "f8960.l16",
    "f8960.line17": "f8960.l17", "f8960.tax": "f8960.l17",
    f"{HSA}.line13": "f8889.l13",
}
# Schedule 1-A: the lines UsTaxes has an accessor for. The totals of each part are read on every
# return; a part's working lines only where the part is filled in (the generator feature), because
# the project leaves an unclaimed part's lines at zero where UsTaxes figures them from MAGI anyway.
S1A_MAP = {f"s1a.line{n}": f"s1a.l{n}" for n in ("3", "4c", "6", "7", "13", "14c", "15", "21", "23", "24", "30", "36a", "36b", "37", "38")}
# Lines 10, 18, 27 and 33 (MAGI less the threshold) are not mapped: the project carries the
# negative difference where the form says to skip the phase-out, and UsTaxes floors it at zero.
S1A_PARTS = {"tips": ("8", "12"), "overtime": ("16", "20"), "car_loan_interest": ("25", "29"), "senior": ("31", "34", "35")}
# Lines read only where UsTaxes builds the worksheet or form (the project computes them on every
# return); each block is read when the engine's object exists.
QDCG_MAP = {f"qdcg.line{n}": f"qdcg.l{n}" for n in range(1, 26)}
SSB_MAP = {f"ssb.line{n}": f"ssb.l{n}" for n in range(1, 19)}
SLI_MAP = {f"sli.line{n}": f"sli.l{n}" for n in (1, 2, 3, 4, 8, 9)}
HSA_MAP = {f"{HSA}.line{n}": f"f8889.l{n}" for n in (3, 5, 6, 8, 11, 12)}
S8812_MAP = {"s8812.line3": "s8812.l3", "s8812.line5": "s8812.l5", "s8812.line7": "s8812.l7", "s8812.line8": "s8812.l8",
             "s8812.line10": "s8812.l10", "s8812.line11": "s8812.l11", "s8812.line12": "s8812.l12", "s8812.line14": "s8812.l14",
             "s8812.line16a": "s8812.part2a.l16a", "s8812.line16b": "s8812.part2a.l16b", "s8812.line17": "s8812.part2a.l17",
             "s8812.line18a": "s8812.part2a.l18a", "s8812.line19": "s8812.part2a.l19", "s8812.line20": "s8812.part2a.l20",
             "s8812.line21": "s8812.part2b.l21", "s8812.line23": "s8812.part2b.l23", "s8812.line24": "s8812.part2b.l24",
             "s8812.line25": "s8812.part2b.l25", "s8812.line26": "s8812.part2b.l26", "s8812.line27": "s8812.l27"}

# Form 8962 (UsTaxes' F8962.ts): a flat 8.5% of AGI, no poverty line, Table 2 or Table 5, annual only. Read on every
# return with a Form 1095-A and compared only where that is the form (limitation ustaxes_ptc_stub).
F8962_MAP = {"f8962.line8a": "f8962.contributionAmount", "f8962.line11e": "f8962.allowablePtc", "f8962.line25": "f8962.annualAdvancePtc",
             "f8962.line26": "f8962.credit", "f8962.line29": "f8962.excessRepayment", "s3.line9": "s3.l9"}
# Form 8863 (UsTaxes' F8863.ts): line 1 (`aotcBeforePhaseOut`), the refundable and nonrefundable parts of the American
# opportunity credit after the phase-out (lines 8 and 9), the lifetime learning credit before and after the phase-out
# (lines 12 and 18), line 19 with no Credit Limit Worksheet, Schedule 3 line 3 and Form 1040 line 29. Read on every return
# with education expenses and compared only where its model is the form (the edu_* and ustaxes_edu_* limitations).
F8863_MAP = {"f8863.line1": "f8863.aotcBeforePhaseOut", "f8863.line8": "f8863.l8", "f8863.line9": "f8863.aotcNonrefundable",
             "f8863.line12": "f8863.llcBeforePhaseOut", "f8863.line18": "f8863.llcAfterPhaseOut", "f8863.line19": "f8863.l19",
             "s3.line3": "s3.l3", "f1040.line29": "f1040.l29"}
USTAXES_PRECISION = "float64"


def lines_of(case, values):
    """{project line id: cents} from one UsTaxes run."""
    v = values
    def get(key):
        x = v.get(key)
        return 0 if x is None else x
    out = {pid: cents(get(k)) for pid, k in {**F1040_MAP, **S1A_MAP}.items() if isinstance(get(k), (int, float))}
    out["f1040.tax_before_credits"] = cents(get("f1040.l18")) + cents(get("f1040.l23"))
    for feature, nums in S1A_PARTS.items():
        if feature in case["features"] or (feature == "senior" and "spouse_senior" in case["features"]):
            out.update({f"s1a.line{n}": cents(get(f"s1a.l{n}")) for n in nums})
    if "qdcg.l1" in v:
        out.update({pid: cents(get(k)) for pid, k in QDCG_MAP.items()})
    if "ssb.l1" in v:
        out.update({pid: cents(get(k)) for pid, k in SSB_MAP.items()})
    if "sli.l1" in v:
        out.update({pid: cents(get(k)) for pid, k in SLI_MAP.items()})
    if "hsa" in case["features"]:
        out.update({pid: cents(get(k)) for pid, k in HSA_MAP.items()})
    if case["facts"].get("children"):
        out.update({pid: cents(get(k)) for pid, k in S8812_MAP.items()})
    if case["facts"].get("marketplace"):
        out.update({pid: cents(get(k)) for pid, k in F8962_MAP.items()})
    if case["facts"].get("education"):
        out.update({pid: cents(get(k)) for pid, k in F8863_MAP.items()})
    return out


def run_node(batch, year, work, cache=True, name="ustaxes"):
    """The runner over a batch of {id, info, assets}; returns its per-case results."""
    work = Path(work).resolve()
    inp, outp = work / f"{name}_input.json", work / f"{name}_output.json"
    inp.write_text(json.dumps(batch))
    env = {**os.environ, "USTAXES_SRC": str(USTAXES_SRC), "USTAXES_DEPS": str(USTAXES_DEPS), "USTAXES_NO_CACHE": "" if cache else "1"}
    r = subprocess.run(["node", "--no-experimental-strip-types", "--import", (RUNNER / "hooks.mjs").as_uri(), str(RUNNER / "run.mjs"),
                        str(year), str(inp), str(outp)], env=env, capture_output=True, text=True, cwd=str(work))
    if r.returncode != 0:
        raise RuntimeError(f"UsTaxes runner failed (exit {r.returncode}): {(r.stdout + r.stderr)[-1500:]}")
    return json.loads(outp.read_text())["cases"]


def self_test(cases, year, work_root, n=20):
    """The runner's per-return line cache changes no value: the first `n` returns UsTaxes runs,
    read with and without the cache, give identical values on every accessor. Returns a message;
    raises on a difference."""
    work = Path(work_root)
    work.mkdir(parents=True, exist_ok=True)
    batch = []
    for c in cases:
        if "self_employed" not in c["features"] and len(batch) < n:
            info, assets = build_info(c, year)
            batch.append({"id": c["id"], "info": info, "assets": assets})
    cached = run_node(batch, year, work, cache=True, name="selftest_cached")
    plain = run_node(json.loads(json.dumps(batch)), year, work, cache=False, name="selftest_plain")
    diffs = [(cid, k) for cid in cached for k, v in cached[cid].get("values", {}).items() if plain[cid].get("values", {}).get(k) != v]
    errors = [cid for cid in cached if "error" in cached[cid] or "error" in plain[cid]]
    if diffs or errors or not cached:
        raise RuntimeError(f"UsTaxes line cache self-test failed: {len(diffs)} differing values (e.g. {diffs[:5]}), errors on {errors[:5]}")
    total = sum(len(r["values"]) for r in cached.values())
    return f"UsTaxes line cache self-test: {len(cached)} returns, {total} values identical with and without the cache"


def run_ustaxes(cases, year, work_root):
    """Every case through UsTaxes in one Node process. Returns the engine record for engines.json,
    or None when the clone or its runtime packages are missing."""
    if not available(year):
        return None
    version, commit = package_version()
    work = Path(work_root)
    work.mkdir(parents=True, exist_ok=True)
    batch, skipped = [], []
    for c in cases:
        if "self_employed" in c["features"]:
            skipped.append(c["id"])
            continue
        info, assets = build_info(c, year)
        batch.append({"id": c["id"], "info": info, "assets": assets})
    results = run_node(batch, year, work)
    by_id = {c["id"]: c for c in cases}
    lines, feats, failures = {}, {}, []
    for cid, res in results.items():
        if "error" in res:
            failures.append((cid, res["error"][:300]))
            continue
        vals = res["values"]
        lines[cid] = lines_of(by_id[cid], vals)
        fs = run_features(by_id[cid], vals)
        if fs:
            feats[cid] = sorted(fs)
    # Self-employed returns are not run; every mapped line is excluded under `self_employed`.
    mapped = sorted({**F1040_MAP, **S1A_MAP}) + ["f1040.tax_before_credits"]
    for cid in skipped:
        lines[cid] = {pid: None for pid in mapped}
    if failures:
        print(f"UsTaxes: {len(failures)} cases failed in the engine, e.g. {failures[:3]}")
    return {"version": f"{version} (git {commit}, src/forms/Y{year})", "package_version": version, "precision": USTAXES_PRECISION,
            "tax_table": "midpoint-unrounded", "lines": lines, "features": feats, "limitations": limitations(),
            "pass_through": USTAXES_PASS_THROUGH, "rejected": [cid for cid, _ in failures]}


def run_features(case, vals):
    """Facts about the engine's own run, or about a case input whose UsTaxes handling is a declared
    limitation, that the comparison keys limitations by (engines.json `features`)."""
    fs = set()
    inputs = case["inputs"]
    if (vals.get("f6251.l11") or 0) > 0:
        fs.add("ustaxes_amt")
    if (vals.get("f1040.l27a") or 0) > 0:
        fs.add("ustaxes_eic")
    # UsTaxes' student loan interest phase-out (from $80,000, or $165,000 joint) and the 2025 worksheet's (to $100,000, or
    # $200,000) differ for modified AGI between the two.
    lo, hi = (165_000, 200_000) if inputs["f1040.status"] == "mfj" else (80_000, 100_000)
    if "sli.l4" in vals and lo < (vals["sli.l4"] or 0) < hi:
        fs.add("ustaxes_sli_phaseout")
    if "hsa" in case["features"]:
        if inputs.get(f"{HSA}.months_family", 0) == 12:
            fs.add("hsa_family")
            # The halved limit binds, or (joint return) the spouse's Form 8889, which takes in every family-coverage
            # account (F8889.ts constructor filter), deducts the same contributions a second time.
            if (vals.get("f8889.l2") or 0) > (vals.get("f8889.l12") or 0) or (vals.get("f8889s.l13") or 0) > 0:
                fs.add("hsa_family_limited")
        if inputs.get(f"{HSA}.age55"):
            fs.add("hsa_age55")
        elif case["facts"].get("age", 40) >= 55:
            fs.add("hsa_senior_without_age55")
    if vals.get("f4952.l4h"):
        fs.add("ustaxes_investment_interest_limited")
    return fs


_CREDITS = ("the credit is computed without the tax limit and rounded to whole dollars, and reaches Form 1040 only when Schedule 3 "
            "is needed for another reason (see the limitations); the lines it moves are compared on returns without it")
USTAXES_PASS_THROUGH = {"lines": [], "components": {
    "f1040.line10": "Schedule 1 line 19a (UsTaxes' slot for the IRA deduction, `otherIncome.iraDeduction`) enters as the generator's "
                    "contributions and the educator expenses as paid (the engine applies the $300 limit); lines 13 and 21 are the "
                    "engine's own Form 8889 and student loan interest worksheet",
    "s1.line26": "Schedule 1 line 19a (the IRA deduction) enters as the generator's contributions; the engine computes the other "
                 "adjustments and the sum",
    "f1040.line20": "Schedule 3 line 1 (the foreign tax credit) enters as the foreign tax paid; returns where the tax limits it are excluded",
    "f1040.line24": "Schedule 3 line 1 (the foreign tax credit) enters as the foreign tax paid, and Form 5695 Part II as the generator's "
                    "credit; returns with either limited, or with any Schedule 3 credit, are excluded after the credits",
    "sd.line16": "the sales enter as Form 8949 rows (UsTaxes' Asset list, all on boxes C and F); the engine computes the gains, "
                 "the wash-sale adjustments and Schedule D's totals",
}, "unmapped": {
    "s1.line20": "the IRA deduction is an input (`otherIncome.iraDeduction`); UsTaxes has no IRA Deduction Worksheet",
    "s3.line1": "the foreign tax credit is an input (`otherIncome.foreignTaxCredit`), not limited by the tax",
    "s3.line2": "Form 2441: " + _CREDITS, "f2441.line9c": "Form 2441: UsTaxes exposes only the rounded credit (`credit`), not line 9",
    "f2441.line11": "Form 2441: " + _CREDITS,
    "s3.line4": "Form 8880: " + _CREDITS, "f8880.line10": "Form 8880: the credit before the limit is rounded down to whole dollars (`l4`)",
    "f8880.line12": "Form 8880: " + _CREDITS,
    "s3.line5a": "Form 5695 Part I: " + _CREDITS, "f5695.line13": "Form 5695 Part I: 30% of the costs rounded to whole dollars (`l15`)",
    "f5695.line15": "Form 5695 Part I: " + _CREDITS,
    "s3.line5b": "Form 5695 Part II is an input (the credit amount itself, CreditType.EnergyEfficientHomeImprovement)",
    "f5695.line30": "Form 5695 Part II is an input", "f5695.line32": "Form 5695 Part II is an input",
    "eic.credit": "the EIC is figured from formulas at a misrounded income (ScheduleEIC.ts `roundIncome`); Form 1040 line 27a is mapped "
                  "and excluded on returns with an EIC",
    "eic.earned_income": "UsTaxes exposes earned income only inside its EIC computation (`earnedIncome`), whose eligibility tests are stubs",
    "sdtw.line1": "the Schedule D Tax Worksheet is never reached (the 28% and section 1250 worksheets are stubs)",
    "sd.line18": "the 28% Rate Gain Worksheet is a stub returning undefined (worksheets/SDRateGainWorksheet.ts)",
    "sd.line19": "the Unrecaptured Section 1250 Gain Worksheet is a stub returning undefined (worksheets/SDUnrecaptured1250.ts)",
    "sd.line1b.h": "the Form 8949 rows UsTaxes builds from its Asset list are all box C or F (F8949.ts `part1BoxC`, `part2BoxF`), so "
                   "Schedule D lines 1b, 2, 8b and 9 are empty; lines 7, 15, 16 and 21 are mapped",
    "f8995.line15": "Form 8995 is built only for Schedule K-1 QBI (F1040.ts `totalQbi`); no generated return reaches it",
    "sa.line9": "Form 4952 counts only interest and nonqualified dividends (F4952.ts `l4a`); lines 10 and 17 are mapped and excluded "
                "where either side's limit applies",
    "f4952.line8": "see sa.line9",
    "person.f8889.line7": "UsTaxes enters the age-55 additional contribution on line 7 in every case, the project on line 3 for an "
                          "unmarried filer (limitation hsa_age55); line 8 is mapped",
    "sli.line5": "UsTaxes' phase-out start is the 2024 amount (data/federal.ts `studentLoanInterest`), a parameter, not a computation",
    "sli.line6": "the project carries the negative difference where the worksheet says to skip line 6; UsTaxes floors it at zero",
    "sli.line7": "a ratio, not a money line",
    "s1a.line10": "the project carries the negative difference where the form says to skip the phase-out; UsTaxes floors it at zero "
                  "(likewise lines 18, 27 and 33); the part totals (lines 13, 21, 30, 37) are mapped",
    "s1a.line9": "the phase-out thresholds (lines 9, 17, 26, 32) are parameters",
    "person.se_line12": "UsTaxes never builds Schedule C, so self-employed returns are not run",
}}


def mapped_lines():
    """Every project line id the adapter can report."""
    parts = {f"s1a.line{n}" for nums in S1A_PARTS.values() for n in nums}
    return sorted(set(F1040_MAP) | set(S1A_MAP) | parts | set(QDCG_MAP) | set(SSB_MAP) | set(SLI_MAP) | set(HSA_MAP) | set(S8812_MAP) | set(F8962_MAP) | set(F8863_MAP)
                  | {"f1040.tax_before_credits"})


# Lines figured before adjusted gross income from the income items alone.
INCOME_LINES = {"f1040.line1a", "f1040.line1z", "f1040.line7a", "f1040.line8", "f1040.line25a", "s1.line10", "sb.line2", "sb.line4",
                "sd.line7", "sd.line15", "sd.line16", "sd.line21", "f8960.line8", "s3.line11", "s3.line15", "sa.line5d", "sa.line8e",
                "sa.line14", "sa.standard", "s1.line11", "sli.line1", "s1a.line4c", "s1a.line6", "s1a.line7", "s1a.line14c", "s1a.line15",
                "s1a.line23", "s1a.line24", "s8812.line5", "s8812.line7", "s8812.line8", "s8812.line16b", "s8812.line18a", "s8812.line19",
                "s8812.line20", "s8812.line21", "s8812.line23", "f1040.line25d"} \
               | {f"f8959.line{n}" for n in (1, 4, 6, 7, 18, 19, 21, 22, 24)} | {"f8959.tax"} | {f"ssb.line{n}" for n in range(1, 6)}
# Lines from Form 1040 line 16 on: the tax, the credits and the payments.
TAX_LINES = {f"f1040.line{n}" for n in (16, 17, 18, 19, 20, 21, 22, 24, 28, 32, 33, 34, 37)} \
            | {"f1040.tax_before_credits", "s3.line8", "s8812.line14", "s8812.line16a", "s8812.line17", "s8812.line27"} \
            | {f"qdcg.line{n}" for n in (22, 23, 24, 25)}
# From taxable income on: Form 1040 lines 13a to 15, the worksheet and the tax lines.
TAXABLE_LINES = {"f1040.line13a", "f1040.line13b", "f1040.line14", "f1040.line15"} | set(QDCG_MAP) | TAX_LINES
# The lines the nonrefundable credits move.
AFTER_CREDIT_LINES = {f"f1040.line{n}" for n in (19, 20, 21, 22, 24, 28, 32, 33, 34, 37)} \
                     | {"s3.line8", "s8812.line14", "s8812.line16a", "s8812.line17", "s8812.line27"}
# The lines Schedule A line 9 (the Form 4952 limit) moves.
INVESTMENT_INTEREST_LINES = sorted({"sa.line10", "sa.line17", "sa.deduction", "f1040.line12e"} | TAXABLE_LINES
                                   | {f"f8960.line{n}" for n in ("9a", "9d", "11", "12", "16", "17")}
                                   | {"f8960.tax", "s2.line21", "f1040.line23"})
# The refundable credits and the payment lines.
REFUND_LINES = {f"f1040.line{n}" for n in ("27a", "28", "32", "33", "34", "37")} | {f"s8812.line{n}" for n in (24, 25, 26, 27)}


CAR_LOAN = ("UsTaxes' Schedule 1-A Part IV (irsForms/Schedule1A.ts lines 150-207) reads line 23 from `l22aiii`/`l22biii`, which "
            "return undefined, so lines 23 and 24 are empty and the car loan interest deduction (line 30) is always zero; the entered "
            "interest (`l22iiiTotal`) is never used")
STATE_TAX = ("UsTaxes allocates part of the Schedule A state and local tax deduction to investment income on Form 8960 line 9b by the "
             "ratio of line 8 to AGI (irsForms/F8960.ts `l9b`); the generator enters no allocation (f8960.allocated_taxes is zero), so "
             "itemizers with a state and local tax deduction are not compared from line 9b on")
HSA_FAMILY = ("UsTaxes' Form 8889 line 6 halves the line 5 limit for any family-coverage account (irsForms/F8889.ts "
              "`splitFamilyContributionLimit`: `Math.round(this.l5() / 2)`), where the instructions split it only between spouses with "
              "separate HSAs")


# Lines a Form 1095-A moves: Schedule 3 line 9 and Schedule 2 line 1a, and through Form 1040 lines 17, 18 and 31 the tax,
# every credit the tax limits, the payments and the refund. Engines given no Form 1095-A are not compared on them there.
PTC_MOVED = re.compile(r"^(f1040\.line(1[7-9]|2[0-9]|3[0-9]|35a)|f1040\.tax_before_credits|s3\.line(2|3|4|5a|5b|8|9|15)|s2\.line(1a|1z|3|21)"
                       r"|s8812\.|f2441\.line(9c|10|11)|f8863\.line19|f8880\.line(11|12)|f5695\.line(14|15|31|32)|f8962\.)")
PTC_REASON = ("the engine is given no Form 1095-A, so its tax, credits and payments omit the premium tax credit reconciliation "
              "(Form 8962) the project figures on these returns")

# Lines Form 8863 moves: its own lines, Schedule 3 line 3 and Form 1040 line 29, and through them every credit after the
# education credits, the tax after credits, the payments and the refund.
EDU_MOVED = re.compile(r"^(f1040\.line(19|2[0-2]|24|28|29|3[2-7]|35a)|s3\.line(3|4|5a|5b|8|15)|s8812\.(line(14|16a|17|27)|clw)"
                       r"|f8880\.line(11|12)|f5695\.line(14|15|31|32)|f8863\.)")
EDU_NO_REFUND = ("the engine has no Form 8863 line 7 test: it makes 40% of the American opportunity credit refundable on every return, "
                 "where a filer under 24 who is not filing jointly and meets line 7 conditions 1 and 2 checks the line 7 box and has "
                 "no refundable part (i8863 p. 7, Line 7; 26 U.S.C. 25A(i)(6)); returns with the box checked are not compared on the "
                 "lines it moves")


def limitations():
    """The engine's declared limitations: each names the feature that triggers it, the lines it
    moves and the UsTaxes source (paths under src/forms/Y2025/ of the clone; line numbers at the
    pinned commit)."""
    ALL = mapped_lines()
    AGI_LINES = sorted(set(ALL) - INCOME_LINES - {f"{HSA}.line{n}" for n in (3, 5, 6, 8, 11, 12, 13)} - {"s1.line13"})
    srt = lambda s: sorted(set(s))
    no_s3 = {"feature": "ustaxes_ptc_no_schedule3", "lines": sorted({"s3.line15"} | {l for l in ALL if l in REFUND_LINES or l in {"f1040.line31", "f1040.line32", "f1040.line33", "f1040.line34", "f1040.line37"}}),
             "reason": "UsTaxes attaches Schedule 3 only for the excess social security credit, the foreign tax credit, an extension payment "
                       "or Schedule R (irsForms/Schedule3.ts lines 50-54, `isNeeded`); a net premium tax credit with none of those is dropped "
                       "from Schedule 3 line 15 and Form 1040 line 31 although Schedule3.ts `l9` returns it"}
    stub = {"feature": "ustaxes_ptc_stub", "lines": sorted({l for l in ALL if PTC_MOVED.match(l)}),
            "reason": "UsTaxes' Form 8962 (irsForms/F8962.ts) applies a flat 8.5% of AGI (`applicableContributionRate`) with no federal "
                      "poverty line, Table 2 or Table 5 limitation and no monthly calculation: it is the form only at 400% of the poverty "
                      "line or more, on line 11, with modified AGI equal to AGI; other returns with a Form 1095-A are not compared after line 16"}
    edu = srt(l for l in ALL if EDU_MOVED.match(l))
    edu_lims = [
        {"feature": "edu_no_refund", "lines": edu,
         "reason": EDU_NO_REFUND + " (irsForms/F8863.ts `l8`: 40% of the credit after the phase-out, with no line 7 condition)"},
        {"feature": "edu_phaseout_inexact", "lines": edu,
         "reason": "UsTaxes phases the education credits out by the unrounded fraction 1 - (MAGI - $80,000) / $10,000 ($160,000 and "
                   "$20,000 joint) (irsForms/F8863.ts `phaseOutFraction`); Form 8863 lines 6 and 17 round the ratio to three places "
                   "(the project to three, amb.2025.edu_ratio_places), so returns whose ratio is not exact at three places are not "
                   "compared on the lines it moves"},
        {"feature": "ustaxes_edu_cents", "lines": edu,
         "reason": "UsTaxes rounds the American opportunity credit after the phase-out, its 40% and 60% parts and the lifetime "
                   "learning credit before and after the phase-out to whole dollars (irsForms/F8863.ts `aotcAfterPhaseOut`, `l8`, "
                   "`aotcNonrefundable`, `llcBeforePhaseOut`, `llcAfterPhaseOut`: `Math.round`), where the project carries cents; "
                   "returns on which any of the project's Form 8863 lines 1, 7, 8, 9, 12 and 18 has cents are not compared on the "
                   "lines they move"},
        {"feature": "edu_credit_limited", "lines": srt({"f8863.line19", "s3.line3"} | AFTER_CREDIT_LINES),
         "reason": "UsTaxes has no Form 8863 Credit Limit Worksheet: line 19 (irsForms/F8863.ts `l19`) is lines 9 and 18 added, not "
                   "limited by the tax; returns where the worksheet's line 6 is less than its line 3 are not compared on line 19 and "
                   "the lines after it"},
        {"feature": "ustaxes_edu_no_schedule3", "lines": srt(AFTER_CREDIT_LINES),
         "reason": "UsTaxes attaches Schedule 3 only for the excess social security credit, the foreign tax credit, an extension "
                   "payment or Schedule R (irsForms/Schedule3.ts lines 50-54, `isNeeded`), so a nonrefundable education credit with "
                   "none of those reaches neither Form 1040 line 20 (F1040.ts `l20`) nor Schedule 8812 Credit Limit Worksheet A "
                   "(Schedule8812.ts lines 99-111) although Schedule3.ts `l3` returns it; Schedule 3 line 3 and Form 1040 line 29 "
                   "are compared, the lines after the credits are not"},
    ]
    return [stub, no_s3, *edu_lims,
        {"feature": "self_employed", "lines": ALL,
         "reason": "UsTaxes never builds Schedule C: irsForms/F1040.ts declares `scheduleC?: ScheduleC` and no code assigns it, so "
                   "`selfEmployedIncome` reaches no form (Schedule 1 line 3, Schedule SE, the QBI deduction and earned income are all "
                   "zero); returns with self-employment income are not run"},
        {"feature": "car_loan_interest", "lines": ["s1a.line23", "s1a.line24", "s1a.line30"],
         "reason": CAR_LOAN},
        {"feature": "car_loan_deduction", "lines": srt({"s1a.line38"} | TAXABLE_LINES),
         "reason": CAR_LOAN + "; returns where the project's line 30 is positive are not compared from line 38 on"},
        {"feature": "special_gains", "lines": srt(set(QDCG_MAP) | TAX_LINES),
         "reason": "UsTaxes' 28% Rate Gain Worksheet and Unrecaptured Section 1250 Gain Worksheet are stubs returning undefined "
                   "(irsForms/worksheets/SDRateGainWorksheet.ts, SDUnrecaptured1250.ts) and its Form 1099-DIV has no box 2b or 2d, so "
                   "Schedule D lines 18 and 19 are empty, the Schedule D Tax Worksheet is never reached (ScheduleD.ts "
                   "`computeTaxOnDTaxWorksheet`) and the gain is taxed on the Qualified Dividends and Capital Gain Tax Worksheet"},
        {"feature": "qbi_dividends", "lines": srt(TAXABLE_LINES),
         "reason": "UsTaxes takes qualified business income only from Schedule K-1 (Form 1065) box 20 code Z (irsForms/F1040.ts "
                   "`totalQbi`); its Form 1099-DIV has no box 5, so section 199A dividends give no Form 8995 and no line 13a deduction"},
        {"feature": "negative_agi", "lines": AGI_LINES,
         "reason": "UsTaxes floors adjusted gross income at zero (irsForms/F1040.ts line 472, `l11a = Math.max(0, l9 - l10)`), where "
                   "Form 1040 line 11 is line 9 minus line 10 and may be negative"},
        {"feature": "dependent_care", "lines": srt(AFTER_CREDIT_LINES),
         "reason": "UsTaxes' Form 2441 credit (irsForms/F2441.ts `credit`) is rounded to whole dollars and not limited by the tax "
                   "(no line 10 or 11), and it reaches Form 1040 only when Schedule 3 is needed for another reason: Schedule3.ts "
                   "`isNeeded` tests only excess social security, the foreign tax credit, an extension payment and Schedule R, and "
                   "F1040.ts line 536 takes line 20 only `if schedule3.isNeeded()`; Schedule 8812 Credit Limit Worksheet A drops "
                   "the Schedule 3 lines under the same test (Schedule8812.ts lines 99-111)"},
        {"feature": "savers_credit", "lines": srt(AFTER_CREDIT_LINES),
         "reason": "UsTaxes' Form 8880 (irsForms/F8880.ts `l4`) is the contributions times the rate rounded down to whole dollars, "
                   "with no line 11 limit by the tax, and reaches Form 1040 line 20 only when Schedule 3 is needed for another reason "
                   "(Schedule3.ts `isNeeded`, F1040.ts line 536)"},
        {"feature": "residential_clean_energy", "lines": srt(AFTER_CREDIT_LINES),
         "reason": "UsTaxes' Form 5695 Part I (irsForms/F5695.ts `l15`) is 30% of the costs rounded to whole dollars with no limit by "
                   "the tax; it enters Schedule 3 line 5a only when Schedule 3 is needed for another reason (Schedule3.ts `isNeeded`), "
                   "while Credit Limit Worksheet A subtracts Form 5695 line 30 (Parts I and II together) whether or not it does, and "
                   "twice when Schedule 3 is needed (once as Schedule 3 line 5b, which is `f5695.l30`, and once directly; "
                   "Schedule8812.ts lines 97-124); there is no Credit Limit Worksheet B (`creditLimitWorksheetB` returns undefined)"},
        {"feature": "home_improvement", "lines": srt(AFTER_CREDIT_LINES),
         "reason": "UsTaxes takes the Form 5695 Part II credit as an entered amount (CreditType.EnergyEfficientHomeImprovement, "
                   "irsForms/F5695.ts `l14PartII`), supplied as the generator's credit before the limit; Schedule 3 line 5b is "
                   "`f5695.l30` (Parts I and II, unlimited), it reaches Form 1040 only when Schedule 3 is needed for another reason, "
                   "and Credit Limit Worksheet A subtracts it twice when Schedule 3 is needed (Schedule8812.ts lines 97-124)"},
        {"feature": "eic", "lines": srt(REFUND_LINES),
         "reason": "UsTaxes figures the earned income credit from Rev. Proc. formulas at a rounded income (irsForms/ScheduleEIC.ts "
                   "`roundIncome`: `Math.round(Math.round(income) / 50) * 50 + 25`, which for the upper half of each $50 band reads "
                   "the next band's midpoint), not from the EIC Table, keeps the unrounded formula value, and always takes the smaller "
                   "of the amounts at earned income and at AGI (`credit`), where Worksheet A uses the earned income amount alone when "
                   "AGI is below the phase-out threshold"},
        {"feature": "ustaxes_eic", "lines": srt(REFUND_LINES),
         "reason": "UsTaxes allowed an earned income credit on this return (see the `eic` limitation for its method); its eligibility "
                   "tests are partly stubs (ScheduleEIC.ts: `validSSNs`, `over25Under65`, `qualifyingChildOfAnother` return fixed "
                   "values), so the lines the credit moves are not compared"},
        {"feature": "s8812_line20_below_line17", "lines": srt({"s8812.line27", "f1040.line28", "f1040.line32", "f1040.line33",
                                                               "f1040.line34", "f1040.line37"}),
         "reason": "UsTaxes' Schedule 8812 line 20 test is inverted and uses $4,800 (irsForms/Schedule8812.ts lines 184-194: "
                   "`l20No = l16b >= 4800`), where the form asks whether line 16b is $5,100 or more and, if not, enters the smaller "
                   "of lines 17 and 20 on line 27; so with one or two qualifying children UsTaxes goes to Part II-B, and with three or "
                   "more it skips Part II-B, whenever line 20 is less than line 17"},
        {"feature": "ira_phaseout", "lines": AGI_LINES,
         "reason": "UsTaxes takes the IRA deduction as an entered amount (`otherIncome.iraDeduction`, Schedule 1 line 19a in "
                   "irsForms/Schedule1.ts), supplied as the contributions; it has no IRA Deduction Worksheet, so returns whose "
                   "deduction the worksheet limits are not compared on the lines that follow it"},
        {"feature": "sli_phaseout", "lines": AGI_LINES,
         "reason": "UsTaxes' student loan interest worksheet uses the unrounded line 7 ratio (irsForms/worksheets/"
                   "StudentLoanInterestWorksheet.ts `l7`), where the project rounds it to three places (amb.2025.sli_ratio_places)"},
        {"feature": "ustaxes_sli_phaseout", "lines": AGI_LINES,
         "reason": "UsTaxes' student loan interest phase-out starts at $80,000 ($165,000 married filing jointly) over $15,000 "
                   "($30,000) (data/federal.ts lines 358-364, the 2024 amounts), where the 2025 worksheet uses $85,000 ($170,000) "
                   "to $100,000 ($200,000); returns whose modified AGI (worksheet line 4) lies between UsTaxes' start and the "
                   "worksheet's end are not compared on the lines that follow it"},
        {"feature": "hsa_family", "lines": [f"{HSA}.line{n}" for n in (6, 8, 12)],
         "reason": HSA_FAMILY},
        {"feature": "hsa_family_limited", "lines": srt({f"{HSA}.line13", "s1.line13"} | set(AGI_LINES)),
         "reason": HSA_FAMILY + "; on this return the contributions exceed UsTaxes' halved line 12, or (a joint return) UsTaxes' "
                   "spouse Form 8889, which takes in every family-coverage account (F8889.ts constructor), deducts the same "
                   "contributions again on Schedule 1 line 13, so line 13 and the lines after it differ"},
        {"feature": "hsa_age55", "lines": [f"{HSA}.line{n}" for n in (3, 5, 6)],
         "reason": "UsTaxes enters the $1,000 additional contribution for age 55 on Form 8889 line 7 in every case (irsForms/F8889.ts "
                   "`l7`) and $4,300 on line 3, where the project's Line 3 Limitation Chart includes it on line 3 for an unmarried "
                   "filer; line 8 is the same either way"},
        {"feature": "ustaxes_amt", "lines": srt({"f1040.line17", "f1040.line18", "f1040.tax_before_credits"} | AFTER_CREDIT_LINES),
         "reason": "UsTaxes computed an alternative minimum tax (Form 6251, irsForms/F6251.ts `l11`) on this return; Form 6251 is "
                   "outside the project's scope (the s2.amt screen)"},
        {"feature": "ssb_with_schedule1_income", "lines": srt({f"ssb.line{n}" for n in range(6, 19)} | {"f1040.line6b"} | set(AGI_LINES)),
         "reason": "UsTaxes' Social Security Benefits Worksheet line 6 adds Schedule 1 line 10 (the additional income total) to the "
                   "adjustments (irsForms/worksheets/SocialSecurityBenefits.ts `l6`, first term `schedule1.l10()`), where the "
                   "worksheet's line 6 is Schedule 1 lines 11 through 20, 23 and 25; returns with benefits and unemployment "
                   "compensation are not compared from line 6 on"},
        {"feature": "additional_medicare_tax", "lines": srt({f"s8812.line{n}" for n in (21, 23, 25, 26, 27)}
                                                            | {f"f1040.line{n}" for n in (28, 32, 33, 34, 37)}),
         "reason": "UsTaxes' Schedule 8812 line 21 is the W-2 boxes 4 and 6 total (irsForms/Schedule8812.ts `part2b`, lines 221-229) "
                   "in every case, where the instructions send a filer with Additional Medicare Tax to the Additional Medicare Tax "
                   "and RRTA Tax Worksheet (Form 8959 lines 7 and 24 change the amount)"},
        {"feature": "itemized_state_tax", "lines": [f"f8960.line{n}" for n in ("9b", "9d", "11", "12")],
         "reason": STATE_TAX},
        {"feature": "itemized_state_tax_niit", "lines": srt({"f8960.line16", "f8960.line17", "f8960.tax", "s2.line21", "f1040.line23",
                                                             "f1040.line24", "f1040.tax_before_credits", "f1040.line33", "f1040.line34",
                                                             "f1040.line37"}),
         "reason": STATE_TAX + "; where modified AGI is over the threshold (Form 8960 line 15) the tax lines follow"},
        {"feature": "hsa_senior_without_age55", "lines": srt({f"{HSA}.line{n}" for n in (8, 12, 13)} | {"s1.line13"} | set(AGI_LINES)),
         "reason": "UsTaxes figures the Form 8889 line 7 additional contribution from the date of birth (irsForms/F8889.ts `l7`: "
                   "$1,000 when the filer is 55 by December 31), the same date that gives the senior deduction; the generator answers "
                   "the age-55 question (f8889 age55) independently of the age it gives a senior, so a filer 66 or older who answered "
                   "no cannot be expressed to UsTaxes"},
        {"feature": "investment_interest_limited", "lines": INVESTMENT_INTEREST_LINES,
         "reason": "UsTaxes' Form 4952 counts only taxable interest and nonqualified dividends as investment income (irsForms/"
                   "F4952.ts `l4a`; lines 4b to 4d, the qualified dividends and the net gain from investment property, are left "
                   "undefined), so where the limit applies its Schedule A line 9 differs from the form's"},
        {"feature": "ustaxes_investment_interest_limited", "lines": INVESTMENT_INTEREST_LINES,
         "reason": "UsTaxes' Form 4952 limited the investment interest deduction on this return (its line 4h is positive); it counts "
                   "only taxable interest and nonqualified dividends as investment income (irsForms/F4952.ts `l4a`)"},
        {"feature": "tax_table_band_edge", "lines": srt(TAX_LINES),
         "reason": "UsTaxes emulates the Tax Table by flooring the amount to whole dollars and taking the band midpoint "
                   "(irsForms/TaxTable.ts `computeTax`, `Math.floor(income)`) on a double built by summing the return's lines; when the "
                   "project's amount in integer cents is exactly a band boundary, the double can land a hair below it "
                   "(mfj-00061: line 15 is $85,350.00 and the engine reads the $85,300 band); the Tax Table reads \"At least\" the boundary"},
        {"feature": "foreign_tax_limited", "lines": srt(AFTER_CREDIT_LINES),
         "reason": "UsTaxes takes the foreign tax credit as an entered amount (`otherIncome.foreignTaxCredit`, irsForms/Schedule3.ts "
                   "`l1`), supplied as the foreign tax paid, with no limit by the tax; returns whose credit the tax limits are not "
                   "compared after the credits"},
    ]


if __name__ == "__main__":
    import argparse, sys
    sys.path.insert(0, str(ROOT / "tools"))
    from taxyear import YEAR  # noqa: E402
    ap = argparse.ArgumentParser(description="UsTaxes adapter self-test (the runner's line cache against uncached reads)")
    ap.add_argument("--self-test", action="store_true", required=True)
    ap.add_argument("--cases", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--year", type=int)
    a = ap.parse_args()
    if not available(YEAR):
        print("UsTaxes self-test: SKIPPED - clone or runtime packages missing")
    else:
        print(self_test(json.load(open(a.cases)), YEAR, a.work))
