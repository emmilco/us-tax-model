#!/usr/bin/env python3
"""Run generated cases through PolicyEngine-US and Tax-Calculator.

Runs under the virtualenv created by tools/engines/setup.sh; nothing else in
the repository imports these engines. Each adapter maps the case's economic
facts (not the project's computed lines) onto the engine's inputs and reads
back the engine's federal lines in integer cents.

Output: { "engines": { name: { "version", "precision", "lines": { case_id: { line: cents } },
          "limitations": [ { feature, lines, reason } ] } } }
The comparison applies the limitations using the case's features, some of which
are derived from the project's own values (for example whether Form 4952 limited
the investment interest deduction).
"""
import argparse, json, warnings
warnings.filterwarnings("ignore")

YEAR = 2025


def cents(x):
    return int(round(float(x) * 100))


def dollars(c):
    return c / 100.0


# Lines of the project compared, and what each engine calls them.
# Values are engine variable names; None means the engine does not expose it.
# PolicyEngine-US variables per project line. Line 24 (total tax) is the sum of
# the pre-refundable-credit income tax (which already includes the net investment
# income tax) and the Additional Medicare Tax, which the engine books as payroll tax.
PE_MAP = {
    # The engine's total includes the capital loss allowance (loss_ald), which Form 1040 takes
    # through Schedule D and line 7a, not through Schedule 1 line 26.
    "f1040.line10": ["above_the_line_deductions", "-loss_ald"],
    "f1040.line11b": ["adjusted_gross_income"],
    "f1040.line13a": ["qualified_business_income_deduction"],
    "f1040.line13b": ["tip_income_deduction", "overtime_income_deduction", "auto_loan_interest_deduction", "additional_senior_deduction"],
    "f1040.line15": ["taxable_income"],
    "f1040.line16": ["regular_tax_before_credits"],
    # The engine's non_refundable_ctc is the credit left after the refundable part, not the
    # amount used against tax; line 19 is the smaller of the credit after phase-out and the
    # limiting tax liability, which is Schedule 8812 line 14.
    "f1040.line19": ["min:ctc,ctc_limiting_tax_liability"],
    "f1040.line28": ["refundable_ctc"],
    "f1040.line27a": ["eitc"],
    "f1040.line6b": ["tax_unit_taxable_social_security"],
    "sa.line17": ["itemized_taxable_income_deductions"],
    "sa.standard": ["standard_deduction"],
    # The engine's total also holds the Schedule 1-A deductions, which Form 1040 takes on line 13b.
    "sa.deduction": ["taxable_income_deductions", "-qualified_business_income_deduction", "-tip_income_deduction",
                     "-overtime_income_deduction", "-auto_loan_interest_deduction", "-additional_senior_deduction"],
    "f8959.tax": ["additional_medicare_tax"],
    "f8960.tax": ["net_investment_income_tax"],
    # The engine's foreign tax credit is the supplied amount, not limited to the tax, so
    # the comparison is made before credits: project line 18 + line 23.
    "f1040.tax_before_credits": ["income_tax_before_credits", "net_investment_income_tax", "additional_medicare_tax"],
}
PE_PRECISION = "float32"
PE_LIMITATIONS = [
    {"feature": "schedule1a_stepped_phaseout", "lines": ['f1040.line13b', 'f1040.line15', 'f1040.line16', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US reduces the tips, overtime and car loan interest deductions by the rate times the exact excess of modified AGI over the threshold; Schedule 1-A lines 11, 19 and 28 count whole $1,000 steps (rounded down, down and up) first"},
    {"feature": "sli_phaseout", "lines": ['f1040.line10', 'f1040.line11b', 'f1040.line13a', 'f1040.line13b', 'f1040.line15', 'f1040.line16', 'f1040.line19', 'f1040.line28', 'f1040.line27a', 'f1040.line6b', 'sa.line17', 'sa.standard', 'sa.deduction', 'f8959.tax', 'f8960.tax', 'f1040.tax_before_credits'],
     "reason": "PolicyEngine-US phases the student loan interest deduction out with the exact ratio; the worksheet's line 7 ratio is rounded to three places in the project (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars"},
    {"feature": "excess_social_security", "lines": ['s3.line11'],
     "reason": "PolicyEngine-US takes excess payroll tax withheld as an input and does not compute it from per-employer withholding"},
    {"feature": "investment_interest_limited", "lines": ['sa.line17', 'sa.deduction', 'f1040.line15', 'f1040.line16', 'f1040.tax_before_credits', 'f8960.tax', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US deducts investment interest expense in full; it does not apply the Form 4952 net-investment-income limit"},
    {"feature": "foreign_tax", "lines": ['f1040.line20', 'f1040.line24', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US takes the foreign tax credit as a supplied amount with a Form 1116-style limit on foreign-source income; the simple no-Form-1116 path is compared before credits instead"},
    {"feature": "section_1250_netted", "lines": ['f1040.line16', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US takes unrecaptured section 1250 gain as an already-netted input; the Unrecaptured Section 1250 Gain Worksheet (Schedule D instructions, lines 14-18) reduces it by the net short-term loss and the 28% worksheet amounts, which the project does"},
    {"feature": "salt_exceeds_agi", "lines": ['sa.line17', 'sa.deduction'],
     "reason": "PolicyEngine-US limits the state and local tax deduction to adjusted gross income; Schedule A line 5e limits it only by the statutory cap"},
    {"feature": "investment_interest_on_8960", "lines": ['f8960.tax', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a"},
]
# Tax-Calculator variables per project line. c09200 is income tax before refundable
# credits and includes both Schedule 2 taxes; `standard` is zero for itemizers, so
# the chosen deduction is standard + c04470.
TC_MAP = {
    "f1040.line10": ["c02900"],
    "f1040.line11b": ["c00100"],
    "f1040.line13a": ["qbided"],
    "f1040.line13b": ["tip_income_deduction", "overtime_income_deduction", "auto_loan_interest_deduction", "senior_deduction"],
    "f1040.line15": ["c04800"],
    "f1040.line16": ["taxbc"],
    "f1040.line19": ["c07220", "odc"],
    "f1040.line28": ["c11070"],
    "f1040.line27a": ["eitc"],
    "f1040.line6b": ["c02500"],
    "f1040.line20": ["c07300"],
    "sa.line17": ["c04470"],
    "sa.deduction": ["standard", "c04470"],
    "f8959.tax": ["ptax_amc"],
    "f8960.tax": ["niit"],
    "f1040.line24": ["c09200"],
    "f1040.tax_before_credits": ["c05800", "niit", "ptax_amc"],
}
TC_PRECISION = "float64"
TC_LIMITATIONS = [
    {"feature": "schedule1a_zero_tax", "lines": ['sa.line17'],
     "reason": "Tax-Calculator takes the standard deduction whenever the tax is the same either way; when the Schedule 1-A deductions leave no tax even with the standard deduction zeroed, its forced pass also takes the standard deduction, so the itemized total is not compared"},
    {"feature": "student_loan_interest", "lines": ['f1040.line10', 'f1040.line11b', 'f1040.line13a', 'f1040.line13b', 'f1040.line15', 'f1040.line16', 'f1040.line19', 'f1040.line28', 'f1040.line27a', 'f1040.line6b', 'f1040.line20', 'sa.line17', 'sa.deduction', 'f8959.tax', 'f8960.tax', 'f1040.line24', 'f1040.tax_before_credits'],
     "reason": "Tax-Calculator takes the student loan interest deduction as a supplied amount (e03210) rather than computing the worksheet's phase-out, so returns with student loan interest are not compared"},
    {"feature": "excess_social_security", "lines": ['s3.line11'],
     "reason": "Tax-Calculator does not compute the excess Social Security withholding credit"},
    {"feature": "qbi_dividends", "lines": ['f1040.line13a', 'sa.deduction', 'f1040.line15', 'f1040.line16', 'f1040.line20', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero"},
    {"feature": "special_gains", "lines": ['f1040.line16', 'f1040.line20', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)"},
    {"feature": "investment_interest_limited", "lines": ['sa.line17', 'sa.deduction', 'f1040.line15', 'f1040.line16', 'f1040.line20', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit"},
    {"feature": "no_tax_either_way", "lines": ['sa.deduction', 'f1040.line15', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass"},
    {"feature": "investment_interest_on_8960", "lines": ['f8960.tax', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a"},
]


def combine(get, spec):
    """Sum of the named variables; a leading "-" subtracts; "min:a,b" takes the smaller of two."""
    total = 0.0
    for v in spec:
        if v.startswith("min:"):
            a, b = v[4:].split(",")
            total += min(get(a), get(b))
        else:
            total += -get(v[1:]) if v.startswith("-") else get(v)
    return total


def run_policyengine(cases):
    from policyengine_us import Simulation
    from importlib.metadata import version as pkg_version
    people, units, fams, spms, hhs = {}, {}, {}, {}, {}
    for c in cases:
        f = c["facts"]; pid = c["id"]
        y = lambda v: {str(YEAR): v}
        people[pid] = {
            "age": y(f.get("age", 40)),
            # Medical expenses are all supplied; without this the engine adds modeled Medicare
            # Part B premiums for a filer 65 or older.
            "medicare_enrolled": y(False),
            # Tips and the FLSA overtime premium are already in wages; these flag the qualified
            # parts. Generated tips are in an occupation on the Treasury list (wait staff, 102).
            "tip_income": y(dollars(f.get("tips", 0))),
            "treasury_tipped_occupation_code": y(102 if f.get("tips") else 0),
            "fsla_overtime_premium": y(dollars(f.get("overtime", 0))),
            "employment_income": y(dollars(f["wages"])),
            "social_security_retirement": y(dollars(f.get("ss_benefits", 0))),
            "taxable_interest_income": y(dollars(f["interest"])),
            "qualified_dividend_income": y(dollars(f["qualified_dividends"])),
            "non_qualified_dividend_income": y(dollars(f["ordinary_dividends"] - f["qualified_dividends"])),
            "qualified_reit_and_ptp_income": y(dollars(f["section_199a_dividends"])),
            "short_term_capital_gains": y(dollars(f["short_term_gain"])),
            # Capital gain distributions enter Schedule D as long-term gain (line 13); the
            # engine's distributions input does not reach income in this version.
            "long_term_capital_gains": y(dollars(f["long_term_gain"] + f["capital_gain_distributions"])),
            "other_medical_expenses": y(dollars(f["medical"])),
            "real_estate_taxes": y(dollars(f["salt_real_estate"])),
            "deductible_mortgage_interest": y(dollars(f["mortgage_interest"])),
            "charitable_cash_donations": y(dollars(f["cash_gifts"])),
            "charitable_non_cash_donations": y(dollars(f["noncash_gifts"])),
            "investment_interest_expense": y(dollars(f["investment_interest"])),
            # Form 1099-DIV box 2d is a collectibles gain before netting; the engine nets it
            # against the net short-term loss on its own, as the 28% Rate Gain Worksheet does.
            "collectibles_gain_or_loss": y(dollars(f["gain_28pct"])),
            "unemployment_compensation": y(dollars(f.get("unemployment", 0))),
            "educator_expense": y(dollars(f.get("educator_expenses", 0))),
            "student_loan_interest": y(dollars(f.get("student_loan_interest", 0))),
            # Roles are supplied so an adult child stays a dependent; by age ordering
            # the engine would make an adult child the filer's spouse.
            "tax_unit_role_input": y("HEAD"),
        }
        members = [pid]
        for k, age in enumerate(f.get("children", [])):
            cid = f"{pid}_c{k + 1}"
            # Children 17 and over are full-time students in the generated cases.
            people[cid] = {"age": y(age), "is_full_time_student": y(age >= 17), "tax_unit_role_input": y("DEPENDENT")}
            members.append(cid)
        units[pid] = {"members": members,
                      "filing_status": y("HEAD_OF_HOUSEHOLD" if f.get("hoh") else "SINGLE"),
                      "state_and_local_sales_or_income_tax": y(dollars(f["salt_income_tax"])),
                      "unrecaptured_section_1250_gain": y(dollars(f["unrecaptured_1250"])),
                      "foreign_tax_credit": y(dollars(f["foreign_tax"])),
                      "health_savings_account_ald": y(dollars(f.get("hsa_deduction", 0)))}
        fams[pid] = {"members": members}; spms[pid] = {"members": members}
        hhs[pid] = {"members": members, "state_code": y("TX"),
                    "qualified_passenger_vehicle_loan_interest": y(dollars(f.get("car_loan_interest", 0)))}
    sim = Simulation(situation={"people": people, "tax_units": units, "families": fams, "spm_units": spms, "households": hhs})
    # Tax-unit ids come back in situation order.
    order = list(units.keys())
    cache = {}
    def var(name):
        if name not in cache:
            cache[name] = sim.calculate(name, YEAR)
        return cache[name]
    lines = {pid: {} for pid in order}
    for line, spec in PE_MAP.items():
        for i, pid in enumerate(order):
            lines[pid][line] = cents(combine(lambda n: float(var(n)[i]), spec))
    return {"version": pkg_version("policyengine-us"), "precision": PE_PRECISION, "lines": lines, "limitations": PE_LIMITATIONS,
            "components": {line: len(spec) for line, spec in PE_MAP.items()}}


def run_taxcalc(cases):
    import taxcalc as tc, pandas as pd
    rows = []
    for i, c in enumerate(cases):
        f = c["facts"]
        ages = f.get("children", [])
        rows.append(dict(
            RECID=i + 1, MARS=4 if f.get("hoh") else 1, age_head=f.get("age", 40), FLPDYR=YEAR,
            XTOT=1 + len(ages), n24=sum(1 for a in ages if a < 17), nu18=sum(1 for a in ages if a < 18),
            n1820=sum(1 for a in ages if 18 <= a <= 20), n21=sum(1 for a in ages if a >= 21), EIC=f.get("eic_children", 0),
            e00200=dollars(f["wages"]), e00200p=dollars(f["wages"]), e02400=dollars(f.get("ss_benefits", 0)),
            e00300=dollars(f["interest"]), e00600=dollars(f["ordinary_dividends"]), e00650=dollars(f["qualified_dividends"]),
            # Distributions enter Schedule D line 13 and net against sales; Tax-Calculator's
            # e01100 is the no-Schedule-D path, so they go into net long-term gain instead.
            p22250=dollars(f["short_term_gain"]), p23250=dollars(f["long_term_gain"] + f["capital_gain_distributions"]), e01100=0.0,
            e17500=dollars(f["medical"]), e18400=dollars(f["salt_income_tax"]), e18500=dollars(f["salt_real_estate"]),
            e19200=dollars(f["mortgage_interest"] + f["investment_interest"]),
            e19800=dollars(f["cash_gifts"]), e20100=dollars(f["noncash_gifts"]), e07300=dollars(f["foreign_tax"]),
            e02300=dollars(f.get("unemployment", 0)), e03220=dollars(f.get("educator_deduction", 0)), e03290=dollars(f.get("hsa_deduction", 0)),
            tip_income=dollars(f.get("tips", 0)), overtime_income=dollars(f.get("overtime", 0)), auto_loan_interest=dollars(f.get("car_loan_interest", 0)),
        ))
    df = pd.DataFrame(rows).astype(float)
    for col in ("RECID", "MARS", "FLPDYR", "XTOT", "n24", "nu18", "n1820", "n21", "EIC"):
        df[col] = df[col].astype(int)
    def run(reform):
        # Exact calculations follow the printed phase-out steps (Schedule 1-A lines 11, 19 and 28,
        # and the other $1,000-step phase-outs) rather than Tax-Calculator's smoothed default.
        recs = tc.Records(data=df.copy(), start_year=YEAR, gfactors=None, weights=None, adjust_ratios=None,
                          exact_calculations=True)
        pol = tc.Policy()
        # Tax-Calculator zeroes the additional child tax credit and the earned income credit by
        # random take-up draws that are not on the form; the documented scale of 9e99 means the
        # credit is always claimed.
        pol.implement_reform({"actc_claim_prob_scale": {YEAR: 9e99}, "eitc_claim_prob_scale": {YEAR: 9e99}, **(reform or {})})
        calc = tc.Calculator(policy=pol, records=recs, verbose=False)
        calc.advance_to_year(YEAR); calc.calc_all()
        return calc
    calc = run(None)
    # Tax-Calculator reports itemized deductions only for units it treats as itemizing
    # (it takes the standard deduction when tax is zero either way). A second pass with
    # the standard deduction (and its addition for age) zeroed exposes its Schedule A total on
    # every return.
    forced = run({"STD": {YEAR: [0, 0, 0, 0, 0]}, "STD_Aged": {YEAR: [0, 0, 0, 0, 0]}})
    lines = {}
    for i, c in enumerate(cases):
        lines[c["id"]] = {line: cents(combine(lambda n: float(calc.array(n)[i]), spec)) for line, spec in TC_MAP.items()}
        lines[c["id"]]["sa.line17"] = cents(forced.array("c04470")[i])
    return {"version": tc.__version__, "precision": TC_PRECISION, "lines": lines, "limitations": TC_LIMITATIONS,
            "components": {line: len(spec) for line, spec in TC_MAP.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    cases = json.load(open(a.cases))
    out = {"engines": {"PolicyEngine-US": run_policyengine(cases), "Tax-Calculator": run_taxcalc(cases)}}
    json.dump(out, open(a.out, "w"))
    print(f"engines ran {len(cases)} cases -> {a.out}")


if __name__ == "__main__":
    main()
