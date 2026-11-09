#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Class C differential for New York (decision C6): PolicyEngine-US (the version pinned in requirements.txt, installed
in .engines/venv by tools/engines/setup.sh) against the New York fixtures (fixtures/ny/2025/it201.json).

For the single and married-filing-jointly cases without dependents whose New York lines are asserted, the adapter
gives PolicyEngine a New York City household with the case's federal adjusted gross income as wages (for these
returns New York AGI equals federal AGI: no addition or subtraction applies), and compares, line for line:

    ny_it201.line33   ny_agi                       New York adjusted gross income
    ny_it201.line38   ny_taxable_income
    ny_it201.line39   ny_main_income_tax + ny_supplemental_tax (the tax computation worksheets' recapture)
    ny_it201.line40   ny_household_credit
    ny_it201.line47a  nyc_income_tax_before_credits
    ny_it201.line48   nyc_household_credit
    ny_it201.line69   nyc_school_tax_credit_fixed_amount
    ny_it201.line69a  nyc_school_tax_credit_rate_reduction_amount

PolicyEngine computes in unrounded dollars; New York's entries are whole dollars (decision C4), so a PolicyEngine
value is rounded half-up to the dollar before comparison and that is the only tolerance. Every other difference is
listed for explanation. Writes reports/ny/2025/engine_differential.md.

    .engines/venv/bin/python -I tools/engines/ny_policyengine.py
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import fixture_inputs  # noqa: E402
FIXTURES = ROOT / "fixtures" / "ny" / "2025" / "it201.json"
REPORT = ROOT / "reports" / "ny" / "2025" / "engine_differential.md"
LINES = [("line33", ["ny_agi"]), ("line38", ["ny_taxable_income"]), ("line39", ["ny_main_income_tax", "ny_supplemental_tax"]),
         ("line40", ["ny_household_credit"]), ("line47a", ["nyc_income_tax_before_credits"]), ("line48", ["nyc_household_credit"]),
         ("line69", ["nyc_school_tax_credit_fixed_amount"]), ("line69a", ["nyc_school_tax_credit_rate_reduction_amount"])]


FIRST_LIMIT = {"single": 215400, "mfj": 161550}


def explain(line, e, ours, theirs, status):
    """A cited cause for a difference, or '' (unexplained)."""
    v = lambda k: e[f"ny_it201.{k}"]["cents"] // 100  # noqa: E731
    d = abs(ours - theirs)
    if line == "line39" and v("line33") <= 107650 and v("line38") < 65000 and d <= 3:
        return ("table: PolicyEngine computes from the rate schedule; the return uses the 2025 New York State Tax Table "
                "(IT-201-I p. 12, Line 39)")
    if line == "line47a" and v("line47") < 65000 and d <= 3:
        return "table: PolicyEngine computes from the rate schedule; the return uses the New York City Tax Table (p. 13, Line 47a)"
    if line == "line39" and v("line33") > 107650 and v("line38") <= FIRST_LIMIT[status] and v("line33") > FIRST_LIMIT[status] and d > 3:
        return (f"worksheet selection: taxable income ${v('line38'):,} is within worksheet {7 if status == 'single' else 1}'s "
                f"\"taxable income (line 38) is ${FIRST_LIMIT[status]:,} or less\" while New York AGI is above it; PolicyEngine "
                "selects the recapture by New York AGI alone. The return follows the worksheet conditions, which are the statute's: "
                "Tax Law § 601(d-4), \"the recapture base and incremental benefit shall be determined by New York taxable "
                "income\" (amb.ny.2025.recapture_selection)")
    if line == "line69a" and d <= 1:
        return ("rounded base: the printed rate-reduction base ($21, $37, $25) is 0.171% of the bracket amount rounded "
                "(20.52, 36.94, 24.62); PolicyEngine uses the exact amount")
    if line in ("line39", "line47a") and d <= 2:
        return ("rounded base: the printed schedule bases and recapture amounts are rounded running totals (premise map 4.3, "
                "4.4); PolicyEngine computes them exactly")
    return ""


def dollars_half_up(x):
    f = Fraction(str(x))
    return int((f + Fraction(1, 2)) // 1)


def situation(status, agi):
    people = {"you": {"age": {"2025": 40}, "employment_income": {"2025": agi}}}
    members = ["you"]
    if status == "mfj":
        people["spouse"] = {"age": {"2025": 40}, "employment_income": {"2025": 0}}
        members.append("spouse")
    units = {"members": members}
    return {"people": people, "tax_units": {"tu": dict(units)}, "families": {"f": dict(units)}, "spm_units": {"s": dict(units)},
            "marital_units": {"m": dict(units)},
            "households": {"h": {**units, "state_code": {"2025": "NY"}, "in_nyc": {"2025": True}}}}


def main():
    from policyengine_us import Simulation
    import policyengine_us
    # The inputs each case is evaluated on (parameters and test-data defaults resolved), so an unstated filing status
    # reads as its default rather than as missing.
    stated = json.loads(FIXTURES.read_text())["cases"]
    resolved = fixture_inputs.resolve_cases([{**c, "file": FIXTURES.name} for c in stated], 2025, ny=True)
    cases = [{**c, "inputs": resolved[c["id"]]} for c in stated]
    rows, diffs, compared = [], [], 0
    for c in cases:
        e = c.get("expect", {})
        status = c["inputs"].get("f1040.status")
        if status not in ("single", "mfj") or c["inputs"].get("$dependent") or "ny_it201.line39" not in e \
                or c["inputs"].get("ny_it201.ask.item_c"):
            continue
        if e["ny_it201.line39"].get("kind") != "money":
            continue
        agi = e["ny_it201.line19"]["cents"] // 100 if "ny_it201.line19" in e else e["ny_it201.line33"]["cents"] // 100
        sim = Simulation(situation=situation(status, agi))
        compared += 1
        for line, vars_ in LINES:
            ours = e.get(f"ny_it201.{line}")
            if not ours or ours.get("kind") != "money":
                continue
            theirs = dollars_half_up(sum(float(sim.calculate(v, 2025)[0]) for v in vars_))
            ok = theirs * 100 == ours["cents"]
            cause = "" if ok else explain(line, e, ours["cents"] // 100, theirs, status)
            rows.append(f"| `{c['id']}` | {line} | {ours['cents'] // 100:,} | {theirs:,} | {'agree' if ok else cause or '**unexplained**'} |")
            if not ok:
                diffs.append((c["id"], line, ours["cents"] // 100, theirs, cause))
    out = ["# New York engine differential: PolicyEngine-US", "",
           f"PolicyEngine-US {policyengine_us.__version__ if hasattr(policyengine_us, '__version__') else '(version in tools/engines/requirements.txt)'} "
           f"against the New York fixtures (`tools/engines/ny_policyengine.py`). {compared} cases (single and married filing jointly, no "
           "dependents, New York lines asserted), PolicyEngine values rounded half-up to the dollar. "
           f"Differences: {len(diffs)}, of which unexplained: {sum(1 for d in diffs if not d[4])}. Each difference names its cause.", "", "| Case | Line | Project | PolicyEngine | |", "| --- | --- | --- | --- | --- |"] + rows + [""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(out))
    un = [d for d in diffs if not d[4]]
    print(f"ny differential: {compared} cases, {len(rows)} line comparisons, {len(diffs)} differences, {len(un)} unexplained")
    for d in un[:40]:
        print("  unexplained", d[:4])
    for d in diffs:
        if d[4].startswith("worksheet"):
            print("  worksheet selection", d[:4])
    return 0


if __name__ == "__main__":
    sys.exit(main())
