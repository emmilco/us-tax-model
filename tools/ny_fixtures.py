#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Write fixtures/ny/2025/it201.json: the New York fixtures (decision C6), each expected value predicted from the
source by tools/ny_predict.py before the New York encoding is evaluated.

Each case is a federal return from the federal fixtures (a whole-return case whose federal values are already
asserted there), with its Form W-2 wages varied to place the New York lines where a branch is taken, plus the New
York answers. The federal amounts the New York return copies are taken from the federal encoding's evaluation of
that return (the federal return is the given input of the New York return); the New York values come from the
predictor alone, which reads no New York encoding. Refusal cases assert the refusing line's gate.

The two official tax-table examples (taxable income $38,275, married filing jointly: State tax $1,773, City tax
$1,292) are class A: a married-filing-jointly return whose New York taxable income is $38,275.

    ny_fixtures.py            write the fixtures (runs the federal evaluation through the CLI)
"""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import ny_predict  # noqa: E402
from fixture_inputs import load_cases  # noqa: E402

NODE = ["node", str(ROOT / "engine" / "dist" / "main.js")]
OUT = ROOT / "fixtures" / "ny" / "2025" / "it201.json"
FED_KEYS = ["f1040.status", "f1040.line1z", "f1040.line2b", "f1040.line3b", "s1.line1", "s1.line2a", "s1.line3", "f1040.line7a",
            "f1040.line4b", "f1040.line5b", "s1.line7", "f1040.line6b", "s1.line9", "s1.line26", "f1040.line11a", "f1040.line27a", "eic.limit"]

NO = {"state_resident": True, "city_resident": True, "special_accrual": False, "yonkers": False, "special_code": False,
      "decedent": False, "item_c": False, "inflation_check": False, "out_of_state_bond_interest": False, "414h": False,
      "529_nonqualified": False, "it225": False, "gov_pension": False, "us_obligation_interest": False, "pension_exclusion": False,
      "529_owner": False, "itemize": False, "resident_credit": False, "other_credits": False, "other_taxes": False,
      "city_credits": False, "mctmt": False, "owes_use_tax": False, "use_tax_st141": False, "contributions": False,
      "dependent_care": False, "noncustodial": False, "real_property_credit": False, "college_tuition": False,
      "other_withholding": False, "refund_529": False, "late_penalty": False, "prior_agi_high": False, "spouse_resident": True,
      "abode_part_year": False, "prior_full_year": True, "est_late": False}


_FEDERAL = None


def federal_inputs(case_id):
    """A federal fixture case's inputs as it is evaluated (tools/fixture_inputs.py: parameters and test-data defaults)."""
    global _FEDERAL
    if _FEDERAL is None:
        _FEDERAL = {c["id"]: c["inputs"] for c in load_cases(2025)}
    return copy.deepcopy(_FEDERAL[case_id])


def base(case_id):
    inputs = federal_inputs(case_id)
    if case_id != "stage5.return.owed":
        # Answers the federal full interview asks that this base (written for a narrower federal profile) does not
        # carry: the whole-return base's answers to return-level questions, where the key is missing. None of them is
        # about a person, an entry or an amount that reaches the New York lines.
        whole = federal_inputs("stage5.return.owed")
        for k, v in whole.items():
            if k not in inputs and not k.startswith(("$", "person[", "interest[", "div[", "sales[", "dependent[")):
                inputs[k] = v
    if case_id == "stage5.return.owed":
        # Wages only, so that low taxable incomes are reachable: the base's interest and dividends set to zero.
        inputs["interest[bank_a].amount"] = 0
        inputs["sb.ordinary_dividends"] = 0
        inputs["f1040.line3a"] = 0
        inputs["div.any"] = False  # every amount it gates is now zero
    return inputs


BASES = {  # status: (case id, the W-2 whose wages are varied)
    "single": ("stage5.return.owed", "person[taxpayer].w2[emp_a]"),
    "mfj": ("stage15.f5695.s2", None),
    "hoh": ("stage8.hoh.parent.test1", None),
    "qss": ("stage21.pending1.qss_valid_computes", None),
    "mfs": ("stage4.standard.mfs", None),
}


def federal(inputs):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(inputs, f)
    out = subprocess.run(NODE + ["eval", "--inputs", f.name, "--json"], capture_output=True, text=True, check=True).stdout
    vals = json.loads(out)["values"]
    fed = {}
    for k in FED_KEYS:
        v = vals.get(k, {}).get("value", {})
        if v.get("kind") == "money":
            fed[k] = v["cents"]
        elif v.get("kind") == "enum":
            fed[k] = v["value"]
        elif v.get("kind") == "refusal":
            raise SystemExit(f"federal refusal at {k}: {v.get('gate')}")
    fed["under17"] = sum(1 for k, v in vals.items() if k.endswith(".under_ctc_age") and k.startswith("dependent[") and v.get("value", {}).get("value") is True)
    fed["status"] = fed.pop("f1040.status", inputs.get("f1040.status"))
    return fed, vals


def w2_key(inputs):
    """The first W-2 under the taxpayer."""
    roster = inputs.get("$w2@person[taxpayer]") or []
    return f"person[taxpayer].w2[{roster[0]}]" if roster else None


def set_wages(inputs, wages_cents):
    k = w2_key(inputs)
    for box in ("box1", "box3", "box5"):
        inputs[f"{k}.{box}"] = wages_cents


def ny_inputs(ans, w2s, line75=0, line79=0, prior_tax=0):
    out = {f"ny_it201.ask.{k}": v for k, v in {**NO, **ans}.items()}
    out["ny_it201.ask.prior_year_tax"] = prior_tax
    out["$ny_it2"] = [f"w{i}" for i in range(len(w2s))]
    for i, (s, c) in enumerate(w2s):
        out[f"ny_it2[w{i}].state_withheld"] = s
        out[f"ny_it2[w{i}].city_withheld"] = c
        out[f"ny_it2[w{i}].yonkers_withheld"] = 0
    out["ny_it201.line75"] = line75
    out["ny_it201.line79_amount"] = line79
    return out


ASSERT = ["line1", "line2", "line3", "line17", "line19", "line33", "line34", "line35", "line36", "line37", "line38", "line39",
          "line40", "line44", "line46", "line47", "line47a", "line48", "line49", "line58", "line59", "line61", "line62", "line69",
          "line69a", "line72", "line73", "line76", "line77", "line78", "line78b", "line80"]


_CANON = None


def refusal(line, gate):
    """The refusal value of ny_it201.<line> for <gate>: its recorded form, remedy and citation (canonical build)."""
    global _CANON
    if _CANON is None:
        _CANON = {l["id"]: l for l in json.loads((ROOT / "canonical" / "2025" / "ny_it201.json").read_text())["form"]["lines"]}
    entry = next(r for r in _CANON[f"ny_it201.{line}"]["refuses"] if r["when"] == f"ny_it201.{gate}")
    return {"kind": "refusal", "gate": entry["when"], "form": entry["form"], "remedy": entry["remedy"], "cite": entry["cite"]}


def money(c):
    return {"kind": "money", "cents": c}


def more_parents(inputs, n):
    """Copy the base's qualifying-relative dependent (a parent) n - 1 times, to reach the household credit columns."""
    keys = {k: v for k, v in inputs.items() if k.startswith("dependent[parent].")}
    for i in range(2, n + 1):
        for k, v in keys.items():
            inputs[k.replace("dependent[parent]", f"dependent[parent{i}]")] = v
    inputs["$dependent"] = ["parent"] + [f"parent{i}" for i in range(2, n + 1)]


def fixture_inputs(case_id, keep):
    """The inputs of a federal fixture whose keys pass `keep`."""
    return {k: v for k, v in federal_inputs(case_id).items() if keep(k)}


def gated_federal(gate):
    """For a refusal case whose screen is asked only when a gate's condition holds: (the federal inputs that make the
    condition hold, the New York withholding records, the sentence the evidence note ends with)."""
    pension = (" The federal return carries one Form 1099-R pension (box 1 $12,000, box 5 $1,200; fixture stage10.plan.box5), so "
               "line 10 is above zero and the screen is asked (ny_it201.has_pension_income).")
    if gate in ("gate.line26", "gate.line29"):
        return fixture_inputs("stage10.plan.box5", lambda k: "retirement" in k), None, pension
    if gate == "gate.line28":
        return ({"interest[bank_a].amount": 10000}, None,
                " The interest payer reports $100, so line 2 is not zero and the screen is asked (ny_it201.has_line28_income).")
    if gate == "gate.mctmt":
        fed = fixture_inputs("stage14.f8959.se_above_threshold", lambda k: k.startswith((
            "person[taxpayer].sc[", "$sc@person[taxpayer]", "$scveh@person[taxpayer]", "$asset@person[taxpayer]",
            "$ltc@person[taxpayer]")) or k == "person[taxpayer].se_screen")
        fed["person[taxpayer].sc[big].line1"] = 8000000
        fed["person[taxpayer].plan"] = "none"
        return (fed, None, " The taxpayer has one Schedule C with $80,000 of gross receipts and no expenses (fixture "
                           "stage14.f8959.se_above_threshold's business), so its net profit is over $50,000 and the screen is asked "
                           "(ny_it201.mctmt_possible).")
    if gate == "gate.dependent_care":
        return ({"f2441.care": True, "f2441.nondependent": False, "f2441.prior_year": False, "f2441.student_disabled": False,
                 "$dcprov": ["p0"], "dcprov[p0].household": False, "dcprov[p0].paid": 600000, "dcprov[p0].related": False,
                 "dcprov[p0].tin_kind": "tin"}, None,
                " The federal care question (f2441.care) is answered Yes, so the screen is asked (ny_it201.federal_care); its "
                "other Form 2441 answers (one care provider paid $6,000; fixture classm.f2441.1's answers) complete the "
                "interview; line 64 does not read them.")
    if gate == "gate.refund_529":
        return ({}, ((900000, 500000),),
                " The New York withholding ($9,000 State, $5,000 City) is more than the tax, so line 78 is above zero and the "
                "screen is asked (ny_it201.has_refund).")
    return {}, None, ""


def make_case(cid, status, wages, ans=None, w2s=((0, 0),), line75=0, line79=0, prior_tax=0, note="", refuse=None, evidence=None, covers=None, parents=None,
              fed_inputs=None, note_after=""):
    case_id, _ = BASES[status]
    inputs = base(case_id)
    if parents:
        more_parents(inputs, parents)
    if wages is not None:
        set_wages(inputs, wages)
    inputs.update(ny_inputs(ans or {}, list(w2s), line75, line79, prior_tax))
    inputs.update(fed_inputs or {})
    fed, _ = federal(inputs)
    deps = 0
    if inputs.get("$dependent"):
        deps = sum(1 for k in inputs["$dependent"])  # every listed dependent of these bases is a claimed dependent
    ny = {"item_c": (ans or {}).get("item_c", False), "dependents": deps, "owes_use_tax": (ans or {}).get("owes_use_tax", False),
          "state_withheld": [s for s, _ in w2s], "city_withheld": [c for _, c in w2s], "line75": line75, "line79": line79,
          "prior_year_tax": prior_tax, "prior_agi_high": (ans or {}).get("prior_agi_high", False), "under17": fed.get("under17", 0),
          "prior_full_year": (ans or {}).get("prior_full_year", True), "est_late": (ans or {}).get("est_late", False)}
    case = {"id": f"ny.{cid}", "covers": covers or ["ny_it201"], "inputs": inputs}
    if refuse:
        gate, line = refuse
        case["evidence"] = "synthetic regression (not class B)"
        case["evidence_note"] = (f"Refusal predicted from the source: {note} The New York answers make ny_it201.{gate} true, so "
                                 f"ny_it201.{line} is a refusal carrying that gate; the refusal's form, remedy and citation are the "
                                 f"line's recorded refusal text.{note_after}")
        case["expect"] = {f"ny_it201.{line}": refusal(line, gate)}
        return case
    pred = ny_predict.predict(fed, ny)
    if pred.get("refused") == "eic":
        case["evidence"] = "synthetic regression (not class B)"
        case["evidence_note"] = (f"Refusal predicted from the source: federal AGI {fed['f1040.line11a'] / 100:,.2f} is under the federal "
                                 f"earned income credit's limit {fed['eic.limit'] / 100:,.2f} (or the credit is claimed), so lines 65 and 70 "
                                 f"refuse (decision B9). {note}")
        case["expect"] = {"ny_it201.line65": refusal("line65", "gate.eic"), "ny_it201.line70": refusal("line70", "gate.eic")}
        return case
    if pred.get("refused") == "child_credit":
        case["evidence"] = evidence or "synthetic regression (not class B)"
        case["evidence_note"] = (f"Predicted by tools/ny_predict.py before the New York encoding was evaluated (method for line 39: "
                                 f"{pred['_method']}). A dependent under 17: line 63 refuses (the Empire State child credit, Form IT-213), "
                                 f"so lines 76 to 80 are not asserted. {note}")
        case["expect"] = {f"ny_it201.{k}": money(pred[f"ny_it201.{k}"]) for k in ASSERT if f"ny_it201.{k}" in pred}
        case["expect"]["ny_it201.line63"] = refusal("line63", "gate.child_credit")
        return case
    if pred.get("refused") == "it270":
        case["evidence"] = evidence or "synthetic regression (not class B)"
        case["evidence_note"] = (f"Predicted from the archived IT-201-I and tax tables by tools/ny_predict.py before the New York encoding was "
                                 f"evaluated (method for line 39: {pred['_method']}). A dependent on item H with federal AGI within $5,000 of "
                                 f"the highest IT-270 threshold: line 70a refuses (decision B10), so lines 76 to 80 are not asserted. {note}")
        case["expect"] = {f"ny_it201.{k}": money(pred[f"ny_it201.{k}"]) for k in ASSERT if f"ny_it201.{k}" in pred}
        case["expect"]["ny_it201.line70a"] = refusal("line70a", "gate.it270")
        return case
    if pred.get("refused") == "stc_rr":
        case["evidence"] = evidence or "synthetic regression (not class B)"
        case["evidence_note"] = (f"Predicted from the archived IT-201-I and tax tables by tools/ny_predict.py before the New York encoding was "
                                 f"evaluated (method for line 39: {pred['_method']}). Income over $500,000: line 69a refuses (decision B7), "
                                 f"so lines 76 to 80 are not asserted. {note}")
        case["expect"] = {f"ny_it201.{k}": money(pred[f"ny_it201.{k}"]) for k in ASSERT if f"ny_it201.{k}" in pred}
        case["expect"]["ny_it201.line69a"] = refusal("line69a", "gate.stc_rr_income")
        return case
    if "refused" in pred:
        raise SystemExit(f"{cid}: the predictor refuses ({pred['refused']}); make it a refusal case")
    case["evidence"] = evidence or "synthetic regression (not class B)"
    fedtxt = ", ".join(f"{k} {v / 100:,.2f}" for k, v in fed.items() if k != "status" and isinstance(v, int) and v)
    case["evidence_note"] = (f"Predicted from the archived IT-201-I and tax tables by tools/ny_predict.py before the New York encoding was "
                             f"evaluated (method for line 39: {pred['_method']}). Federal amounts copied (from the federal encoding): "
                             f"status {fed['status']}, {fedtxt}. {note}").strip()
    case["expect"] = {f"ny_it201.{k}": money(pred[f"ny_it201.{k}"]) for k in ASSERT}
    case["evidence_note"] += f" Taxable income reached (line 38): ${pred['ny_it201.line38'] // 100:,}; New York AGI (line 33): ${pred['ny_it201.line33'] // 100:,}."
    return case


def wages_for_taxable(status, target_ti, extra=0):
    """W-2 wages that put New York taxable income (line 38) at target_ti on the base return, found by evaluating the
    federal return once at a probe amount and shifting the wages by the difference (the base returns' other income
    and deductions do not depend on wages in the ranges used)."""
    case_id, _ = BASES[status]
    inputs = base(case_id)
    k = w2_key(inputs)
    probe = 10000000
    set_wages(inputs, probe)
    fed, _ = federal(inputs)
    deps = len(inputs.get("$dependent") or [])
    pred = ny_predict.predict({**fed, "f1040.line27a": 0, "eic.limit": 0}, {"dependents": deps, "state_withheld": [], "city_withheld": []})
    ti = pred["ny_it201.line38"]
    return max(probe + (target_ti * 100 - ti) + extra, 0)


def main():
    cases = []
    # class A: the official tax-table examples ($38,275, married filing jointly)
    w = wages_for_taxable("mfj", 38275)
    cases.append(make_case("official.tax_table_38275", "mfj", w, evidence="A — official New York example",
                           note="Class A: the 2025 tax-tables page's examples, \"Their taxable income on line 38 is $38,275\" ... \"is $1,773\" "
                                "(State) and \"Their taxable income on line 47 is $38,275\" ... \"is $1,292\" (City) (ny_it201_tax_tables). "
                                "Only lines 38, 39, 47 and 47a are the examples' own; the others are the predictor's."))
    # the Tax Table: band edges (single, mfj, hoh)
    for status in ("single", "mfj", "hoh"):
        for ti in (0, 12, 13, 24999, 25000, 38275, 64999):
            if status == "mfj" and ti == 38275:
                continue
            cases.append(make_case(f"table.{status}.{ti}", status, wages_for_taxable(status, ti), note=f"Tax Table (target taxable income ${ti:,})."))
    # the rate schedule ($65,000 or more of taxable income, NY AGI $107,650 or less)
    for status in ("single", "mfj", "hoh"):
        for ti in (65000, 80650, 80651, 95000):
            cases.append(make_case(f"schedule.{status}.{ti}", status, wages_for_taxable(status, ti), note=f"Rate schedule (target taxable income ${ti:,})."))
    # the recapture worksheets
    for status, tis in (("single", (100000, 120000, 150000, 160000, 215400, 215401, 240000, 300000, 1077551, 1200000, 5000001, 26000000)),
                        ("mfj", (100000, 140000, 161550, 161551, 200000, 323201, 400000, 2155351, 5000001)),
                        ("hoh", (110000, 150000, 269301, 300000, 1616451, 5000001))):
        for ti in tis:
            cases.append(make_case(f"worksheet.{status}.{ti}", status, wages_for_taxable(status, ti),
                                   note=f"Tax computation worksheets (target taxable income ${ti:,})."))
    # household credits and the school tax credits at low income
    for status, tis in (("single", (2000, 4000, 12000, 19000, 21000)), ("mfj", (1000, 5000, 12000, 16000)), ("hoh", (500, 3000, 9000, 14000))):
        for ti in tis:
            cases.append(make_case(f"household.{status}.{ti}", status, wages_for_taxable(status, ti),
                                   note=f"Household credits (target taxable income ${ti:,})."))
    # item C (dependent filer): $3,100 deduction, no household or school tax credit
    cases.append(make_case("item_c.single", "single", wages_for_taxable("single", 20000), ans={"item_c": True},
                           note="Item C Yes: the $3,100 standard deduction; no household credit; no school tax credit."))
    # sales and use tax chart
    for ti in (8000, 40000, 180000, 260000):
        cases.append(make_case(f"use_tax.single.{ti}", "single", wages_for_taxable("single", ti), ans={"owes_use_tax": True},
                               note="Use tax owed: the chart amount for federal AGI."))
    # withholding, estimated payments, refund and amount owed, line 79
    cases.append(make_case("payments.refund", "single", wages_for_taxable("single", 70000), w2s=((500000, 300000), (100000, 50000)),
                           line75=20000, line79=10000, note="Two W-2 records, an estimated payment and part of the refund applied to 2026."))
    cases.append(make_case("payments.owe_safe", "single", wages_for_taxable("single", 150000), w2s=((600000, 300000),), prior_tax=800000,
                           note="A balance due with prepayments at least 100% of the prior-year tax: no estimated tax penalty refusal."))
    cases.append(make_case("payments.owe_safe_110", "single", wages_for_taxable("single", 150000), w2s=((600000, 300000),),
                           prior_tax=800000, ans={"prior_agi_high": True},
                           note="Prior-year New York AGI over $150,000: the safe harbor is 110% of $8,000, $8,800, which the $9,000 of prepayments meets."))
    # refusals: every screen
    S = wages_for_taxable("single", 70000)
    for gate, ans, line, why in [
        ("gate.part_year_state", {"state_resident": False}, "line1", "a part-year or nonresident files Form IT-203."),
        ("gate.part_year_city", {"city_resident": False}, "line1", "a part-year City resident files Form IT-360.1."),
        ("gate.special_accrual", {"special_accrual": True}, "line1", "special accruals (IT-225 A-115, S-129)."),
        ("gate.yonkers", {"yonkers": True}, "line1", "Yonkers."),
        ("gate.special_code", {"special_code": True}, "line1", "an item G special condition code."),
        ("gate.decedent", {"decedent": True}, "line1", "a decedent's return."),
        ("gate.line20", {"out_of_state_bond_interest": True}, "line20", "line 20 is not computed (B4)."),
        ("gate.line21", {"414h": True}, "line21", "line 21 is not computed (B4)."),
        ("gate.line22", {"529_nonqualified": True}, "line22", "line 22 is not computed (B4)."),
        ("gate.it225", {"it225": True}, "line23", "Form IT-225."),
        ("gate.line25", {"inflation_check": True}, "line25", "line 25 (B1)."),
        ("gate.line26", {"gov_pension": True}, "line26", "line 26 is not computed (B4)."),
        ("gate.line28", {"us_obligation_interest": True}, "line28", "line 28 is not computed (B4)."),
        ("gate.line29", {"pension_exclusion": True}, "line29", "line 29 is not computed (B4)."),
        ("gate.line30", {"529_owner": True}, "line30", "line 30 is not computed (B4)."),
        ("gate.itemize", {"itemize": True}, "line34", "itemizing (Form IT-196)."),
        ("gate.resident_credit", {"resident_credit": True}, "line41", "the resident credit (Form IT-112-R)."),
        ("gate.other_credits", {"other_credits": True}, "line42", "credits on Form IT-201-ATT."),
        ("gate.other_taxes", {"other_taxes": True}, "line45", "other taxes on Form IT-201-ATT."),
        ("gate.city_credits", {"city_credits": True}, "line53", "City credits on Form IT-201-ATT."),
        ("gate.mctmt", {"mctmt": True}, "line54a", "the MCTMT (B5)."),
        ("gate.use_tax_st141", {"owes_use_tax": True, "use_tax_st141": True}, "line59", "use tax on Form ST-141 (B3)."),
        ("gate.contributions", {"contributions": True}, "line60", "voluntary contributions (B11)."),
        ("gate.dependent_care", {"dependent_care": True}, "line64", "the child and dependent care credit."),
        ("gate.noncustodial", {"noncustodial": True}, "line66", "the noncustodial parent EIC."),
        ("gate.real_property", {"real_property_credit": True}, "line67", "the real property tax credit."),
        ("gate.college_tuition", {"college_tuition": True}, "line68", "the college tuition credit."),
        ("gate.other_withholding", {"other_withholding": True}, "line72", "New York withholding on a form other than a W-2 (B2)."),
        ("gate.refund_529", {"refund_529": True}, "line78a", "a refund deposit into a 529 account (B11)."),
        ("gate.late", {"late_penalty": True}, "line82", "late filing or payment penalties (B11)."),
    ]:
        fed_inputs, w2s, note_after = gated_federal(gate)
        cases.append(make_case(f"refuse.{gate.split('.', 1)[1]}", "single", S, ans=ans, w2s=w2s or ((300000, 200000),), refuse=(gate, line),
                               note=f"the screen's Yes refuses: {why}", fed_inputs=fed_inputs, note_after=note_after))
    cases.append(make_case("refuse.spouse_nonresident", "mfj", wages_for_taxable("mfj", 70000), ans={"spouse_resident": False},
                           refuse=("gate.spouse_nonresident", "line1"), note="a joint return with a nonresident spouse."))
    cases.append(make_case("refuse.estimated_penalty", "single", wages_for_taxable("single", 150000), w2s=((300000, 100000),),
                           prior_tax=800000, refuse=("gate.estimated_penalty", "line81"),
                           note="a balance due with prepayments ($4,000) below the prior-year tax ($8,000) (B6)."))
    cases.append(make_case("refuse.line79_over", "single", wages_for_taxable("single", 70000), w2s=((900000, 500000),), line79=50000000,
                           refuse=("gate.line79_over", "line78"), note="line 79 more than the overpayment."))
    cases.append(make_case("refuse.child_credit", "hoh", wages_for_taxable("hoh", 40000), refuse=("gate.child_credit", "line63"),
                           note="a dependent under 17 (the Empire State child credit, Form IT-213).") if False else None)
    for st, tis in (("qss", (30000, 70000, 140000, 200000)), ("mfs", (40000, 70000, 120000, 300000))):
        for ti in tis:
            cases.append(make_case(f"status.{st}.{ti}", st, wages_for_taxable(st, ti), note=f"Filing status {st} (target taxable income ${ti:,})."
                                   + (" The federal return refuses married filing separately at line 37 (s3.mfs); the New York lines asserted do not read it." if st == "mfs" else "")))
    for n in range(1, 7):
        cases.append(make_case(f"household.hoh.parents{n}", "hoh", wages_for_taxable("hoh", 13800), parents=n,
                               note=f"Head of household with {n} qualifying-relative dependent(s) (parents, not qualifying children for the earned income credit): {n + 1} people for the household credit column."))
    cases.append(make_case("refuse.hh_mfs", "mfs", wages_for_taxable("mfs", 15000), refuse=("gate.hh_state_mfs", "line40"),
                           note="married filing separately with federal AGI within the household credit rows (table 3 needs the spouse's AGI)."))
    cases.append(make_case("refuse.hh_over7", "hoh", wages_for_taxable("hoh", 13800), parents=7, refuse=("gate.hh_state_over7", "line40"),
                           note="eight people (seven dependents) with federal AGI within the household credit rows (Note 3)."))
    # in-session review fixes (step 7), each with its case
    cases.append(make_case("review.it2_whole_dollars", "single", wages_for_taxable("single", 70000), w2s=((300049, 200050), (100050, 49)),
                           note="Each IT-2 record's withholding is rounded to the whole dollar before the totals (IT-2 p. 2, \"drop amounts "
                                "below 50 cents and increase amounts from 50 to 99 cents to the next dollar\"): $3,000.49 and $1,000.50 "
                                "State, $2,000.50 and $0.49 City."))
    cases.append(make_case("review.worksheet_single_rounding", "mfj", wages_for_taxable("mfj", 162820 - 16050),
                           note="Worksheet 2 at New York AGI $162,820 (married filing jointly): 807 x 0.0254 = 20.4978, entered as $20 "
                                "(rounded once; cent-then-dollar rounding gave $21)."))
    cases.append(make_case("refuse.use_tax_abode", "single", S, ans={"owes_use_tax": True, "abode_part_year": True}, w2s=((300000, 200000),),
                           refuse=("gate.use_tax_abode", "line59"), note="use tax owed with a New York abode for only part of the year."))
    cases.append(make_case("refuse.no_prior_full_year", "single", wages_for_taxable("single", 150000), w2s=((600000, 300000),),
                           prior_tax=800000, ans={"prior_full_year": False}, refuse=("gate.estimated_penalty", "line81"),
                           note="a balance due and no full-year 2024 return (no prior-year safe harbor)."))
    cases.append(make_case("refuse.est_late", "single", wages_for_taxable("single", 70000), w2s=((900000, 500000),), line75=100000,
                           ans={"est_late": True}, refuse=("gate.estimated_penalty", "line81"),
                           note="an estimated installment paid late or short, even with a refund."))
    cases = [c for c in cases if c]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"tax_year": 2025, "cases": cases}, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(cases)} cases")


if __name__ == "__main__":
    main()
