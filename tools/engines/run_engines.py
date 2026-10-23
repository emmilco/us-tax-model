#!/usr/bin/env python3
"""Run generated cases through PolicyEngine-US, Tax-Calculator and OpenTaxSolver.

Runs under the virtualenv created by tools/engines/setup.sh; nothing else in
the repository imports these engines. Each adapter maps the case's economic
facts (not the project's computed lines) onto the engine's inputs and reads
back the engine's federal lines in integer cents. OpenTaxSolver's adapter is
the sibling module ots_adapter.py (text input files through the C programs
built under .engines/opentaxsolver-src/); it is left out, visibly, when that
package is not built.

Output: { "engines": { name: { "version", "precision", "lines": { case_id: { line: cents } },
          "limitations": [ { feature, lines, reason } ],
          "features": { case_id: [feature] } (optional: facts about the engine's own run),
          "pass_through": { "lines": [...], "components": { line: note }, "unmapped": { line: reason } } } } }
The comparison applies the limitations using the case's features, some of which
are derived from the project's own values (for example whether Form 4952 limited
the investment interest deduction) and some reported by the engine's adapter
(for example that OpenTaxSolver computed an alternative minimum tax). `pass_through.lines` names mapped lines the
engine takes whole from the generator's facts instead of computing (none today);
`pass_through.components` names the components of a computed line that enter as
generator facts, so the evidence report can say what the engine did not compute;
`pass_through.unmapped` names project result lines left unmapped, with the reason
(an input the engine does not compute, a value it does not expose, or a line
reached through a copy that is mapped).
"""
import argparse, json, sys, warnings
from pathlib import Path

# tools/ comes off the path again once taxyear is loaded: its coverage/ directory would
# otherwise be imported as the `coverage` module that numba (under Tax-Calculator) probes for.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from taxyear import YEAR  # noqa: E402
sys.path.pop(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ots_adapter  # noqa: E402
sys.path.pop(0)
warnings.filterwarnings("ignore")



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
    # Line 23 includes the self-employment tax of Schedule 2 line 4, which the engine books separately.
    "f1040.tax_before_credits": ["income_tax_before_credits", "net_investment_income_tax", "additional_medicare_tax", "self_employment_tax"],
    "s2.line4": ["self_employment_tax"],
    "s1.line15": ["self_employment_tax_ald"],
    # Schedule SE lines 12 and 13 of the filer (the generated spouse has no self-employment income).
    "person[taxpayer].se_line12": ["head:self_employment_tax"],
    "person[taxpayer].se_line13": ["head:self_employment_tax_ald_person"],
    # Form 2441: the credit before the tax limit (line 9b is zero: no prior-year expenses) and after it;
    # Schedule 3 line 2 carries the credit, or zero when the form is not filed.
    "f2441.line9c": ["cdcc_potential"],
    "f2441.line11": ["cdcc"],
    "s3.line2": ["cdcc"],
    # Form 8880: the credit before the limit (line 10) and the credit (line 12, Schedule 3 line 4).
    "f8880.line10": ["savers_credit_potential"],
    "f8880.line12": ["savers_credit"],
    # Form 5695 Part I (lines 13 and 15, Schedule 3 line 5a) and Part II (lines 30 and 32, Schedule 3 line 5b).
    "f5695.line13": ["residential_clean_energy_credit_potential"],
    "f5695.line15": ["residential_clean_energy_credit"],
    "s3.line5a": ["residential_clean_energy_credit"],
    "f5695.line30": ["energy_efficient_home_improvement_credit_potential"],
    "f5695.line32": ["energy_efficient_home_improvement_credit"],
    "s3.line5b": ["energy_efficient_home_improvement_credit"],
    # Schedule 8812 line 12: the credit after the phase-out, before the tax limit.
    "s8812.line12": ["ctc"],
    # Earned income for the EIC: Step 5 (wages) and Worksheet A/B line 1 (Step 5 plus net earnings from
    # self-employment less half the self-employment tax, not below zero).
    "eic.earned_income": ["eitc_earned_income"],
    "eic.line1": ["eitc_earned_income"],
    # Schedule 1 line 20, the IRA deduction after the IRA Deduction Worksheet.
    "s1.line20": ["traditional_ira_deduction"],
    # Schedule 1-A parts: tips (line 13), overtime (line 21), car loan interest (line 30), seniors (line 37).
    "s1a.line13": ["tip_income_deduction"],
    "s1a.line21": ["overtime_income_deduction"],
    "s1a.line30": ["auto_loan_interest_deduction"],
    "s1a.line37": ["additional_senior_deduction"],
}
PE_PRECISION = "float32"
# Lines the engine takes whole from the generator's facts (none), components of computed lines
# that enter as generator facts rather than the engine's own form arithmetic, and project result
# lines the engine has no computed variable for.
PE_PASS_THROUGH = {"lines": [], "components": {
    "f1040.line10": "the HSA deduction (Form 8889 line 13) enters as the generator's health_savings_account_ald; "
                    "the engine computes the educator, half-of-self-employment-tax, IRA and student loan interest "
                    "components and the sum",
}, "unmapped": {
    "person[taxpayer].f8889[hsa].line13": "health_savings_account_ald is an input with no formula; the engine does not compute Form 8889",
    "ssb.line18": "reached through Form 1040 line 6b, a copy of it",
    "s1a.line38": "reached through Form 1040 line 13b, a copy of it",
    "s8812.line14": "reached through Form 1040 line 19, a copy of it",
    "s8812.line27": "reached through Form 1040 line 28, a copy of it",
    "eic.credit": "reached through Form 1040 line 27a, a copy of it",
}}
# Lines that move with adjusted gross income, for limitations on an engine's AGI.
PE_AGI_LINES = [l for l in PE_MAP if l not in ("eic.earned_income", "eic.line1", "person[taxpayer].se_line12", "person[taxpayer].se_line13", "s2.line4", "s1.line15")]
PE_LIMITATIONS = [
    {"feature": "schedule1a_stepped_phaseout", "lines": ['f1040.line13b', 'f1040.line15', 'f1040.line16', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28', 's1a.line13', 's1a.line21', 's1a.line30'],
     "reason": "PolicyEngine-US reduces the tips, overtime and car loan interest deductions by the rate times the exact excess of modified AGI over the threshold; Schedule 1-A lines 11, 19 and 28 count whole $1,000 steps (rounded down, down and up) first"},
    {"feature": "sli_phaseout", "lines": PE_AGI_LINES,
     "reason": "PolicyEngine-US phases the student loan interest deduction out with the exact ratio; the worksheet's line 7 ratio is rounded to three places in the project (amb.2025.sli_ratio_places), which moves the deduction by up to a few dollars"},
    {"feature": "self_employed", "lines": ['eic.earned_income'],
     "reason": "PolicyEngine-US's eitc_earned_income includes net earnings from self-employment less half the self-employment tax; Step 5 earned income (Form 1040 instructions, line 27) holds wages only and Worksheet B adds the self-employment amounts, so Worksheet B line 6 (eic.line1) is compared instead on self-employed returns"},
    {"feature": "furnace", "lines": ['f5695.line30', 'f5695.line32', 's3.line5b', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US lists capped_qualified_furnace_or_hot_water_boiler_credit twice in gov.irs.credits.energy_efficient_home_improvement.qualified_expenditures.credits, so it counts the furnace credit twice in Form 5695 line 27"},
    {"feature": "heat_pump_with_improvements", "lines": ['f5695.line30', 'f5695.line32', 's3.line5b', 'f1040.line19', 'f1040.line28'],
     "reason": "PolicyEngine-US's energy_efficient_home_improvement_credit_potential takes the larger of the $1,200-capped total and the heat pump credit; Form 5695 line 30 adds line 28 and line 29h"},
    {"feature": "negative_agi", "lines": ['f8880.line10', 'f8880.line12'],
     "reason": "PolicyEngine-US's saver's credit rate (gov.irs.credits.retirement_saving.rate.joint, a bracket scale whose first threshold is $0) is zero for an adjusted gross income below zero; the Form 8880 line 9 table's first row has no lower bound (\"---\" to $23,750, $35,625 or $47,500: 0.5)"},
    {"feature": "excess_social_security", "lines": ['s3.line11'],
     "reason": "PolicyEngine-US takes excess payroll tax withheld as an input and does not compute it from per-employer withholding"},
    {"feature": "investment_interest_limited", "lines": ['sa.line17', 'sa.deduction', 'f1040.line13a', 'f1040.line15', 'f1040.line16', 'f1040.tax_before_credits', 'f8960.tax', 'f1040.line19', 'f1040.line28'],
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
    "f1040.tax_before_credits": ["c05800", "niit", "ptax_amc", "setax"],
    "s2.line4": ["setax"],
    "s1.line15": ["c03260"],
    # Schedule SE lines 12 and 13 (the unit's, which is the filer's: the generated spouse has no self-employment income).
    "person[taxpayer].se_line12": ["setax"],
    "person[taxpayer].se_line13": ["c03260"],
    # Form 2441 line 11 (F2441 computes lines 2 to 11; line 9a is not exposed); Schedule 3 line 2.
    "f2441.line11": ["c07180"],
    "s3.line2": ["c07180"],
    # Earned income for the EIC (`earned`: wages plus self-employment earnings less half the self-employment tax).
    "eic.earned_income": ["earned"],
    "eic.line1": ["earned"],
    "s1a.line13": ["tip_income_deduction"],
    "s1a.line21": ["overtime_income_deduction"],
    "s1a.line30": ["auto_loan_interest_deduction"],
    "s1a.line37": ["senior_deduction"],
}
TC_PRECISION = "float64"
TC_PASS_THROUGH = {"lines": [], "components": {
    "f1040.line10": "the HSA deduction (e03290), the educator expenses deduction (e03220) and the IRA contributions (e03150) "
                    "enter as the generator's amounts; the engine computes the half-of-self-employment-tax component and "
                    "the sum (returns with student loan interest, or an IRA deduction phased out by modified AGI, are excluded)",
    "f1040.line20": "the foreign tax paid (e07300) is a supplied amount; the engine computes the credit limit",
    "f1040.line19": "the Form 5695 credits before their limits (e07260) enter as the generator's amounts figured from the costs; "
                    "the engine subtracts them in Credit Limit Worksheet A",
    "f1040.line24": "the Form 5695 credits before their limits (e07260) enter as the generator's amounts figured from the costs; "
                    "the engine applies the tax limit; returns with a saver's credit are excluded",
}, "unmapped": {
    "person[taxpayer].f8889[hsa].line13": "e03290 is an input; the engine does not compute Form 8889",
    "s1.line20": "e03150 (deductible IRA contributions) is an input; the engine does not compute the IRA Deduction Worksheet",
    "f8880.line10": "e07240 (the Form 8880 credit) is an input; the engine computes only its tax limit (c07240)",
    "f8880.line12": "e07240 (the Form 8880 credit) is an input; the engine computes only its tax limit (c07240)",
    "f5695.line13": "e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts",
    "f5695.line15": "e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts",
    "f5695.line30": "e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts",
    "f5695.line32": "e07260 (the Form 5695 credits) is an input; the engine computes only its tax limit (c07260), after the child tax credit for both parts",
    "f2441.line9c": "F2441 computes line 9a but does not expose it; only c07180 (line 11) is an output",
    "s8812.line12": "ChildDepTaxCredit computes line 12 but does not expose it; c07220 and odc are line 14 split",
    "ssb.line18": "reached through Form 1040 line 6b, a copy of it",
    "s1a.line38": "reached through Form 1040 line 13b, a copy of it",
    "s8812.line14": "reached through Form 1040 line 19, a copy of it",
    "s8812.line27": "reached through Form 1040 line 28, a copy of it",
    "eic.credit": "reached through Form 1040 line 27a, a copy of it",
}}
TC_AGI_LINES = [l for l in TC_MAP if l not in ("eic.earned_income", "eic.line1", "person[taxpayer].se_line12", "person[taxpayer].se_line13", "s2.line4", "s1.line15")]
TC_LIMITATIONS = [
    {"feature": "ira_phaseout", "lines": TC_AGI_LINES,
     "reason": "Tax-Calculator takes the deductible IRA contributions as a supplied amount (e03150) rather than computing the IRA Deduction Worksheet's phase-out by modified AGI, so returns whose deduction is less than the contributions are not compared"},
    {"feature": "savers_credit", "lines": ['f1040.line24'],
     "reason": "Tax-Calculator takes the Form 8880 credit as a supplied amount (e07240) and has no input for retirement contributions, so the total tax of a return with a saver's credit is not compared"},
    {"feature": "savers_displaces_ctc", "lines": ['f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator has no saver's credit to subtract in Schedule 8812 Credit Limit Worksheet A line 2, which moves line 14 where the child tax credit does not fit under the worksheet's limit"},
    {"feature": "rce_displaces_ctc", "lines": ['f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator subtracts the whole Form 5695 amount (e07260) in Credit Limit Worksheet A line 2, which lists Schedule 3 line 5b (Part II) but not line 5a; the residential clean energy credit (Part I) follows the child tax credit, through Credit Limit Worksheet B when there is a qualifying child, which moves line 14 where the child tax credit does not fit under the engine's limit"},
    {"feature": "self_employed", "lines": ['eic.earned_income'],
     "reason": "Tax-Calculator's earned includes self-employment earnings less half the self-employment tax; Step 5 earned income (Form 1040 instructions, line 27) holds wages only and Worksheet B adds the self-employment amounts, so Worksheet B line 6 (eic.line1) is compared instead on self-employed returns"},
    {"feature": "schedule1a_zero_tax", "lines": ['sa.line17'],
     "reason": "Tax-Calculator takes the standard deduction whenever the tax is the same either way; when the Schedule 1-A deductions leave no tax even with the standard deduction zeroed, its forced pass also takes the standard deduction, so the itemized total is not compared"},
    {"feature": "student_loan_interest", "lines": TC_AGI_LINES,
     "reason": "Tax-Calculator takes the student loan interest deduction as a supplied amount (e03210) rather than computing the worksheet's phase-out, so returns with student loan interest are not compared"},
    {"feature": "excess_social_security", "lines": ['s3.line11'],
     "reason": "Tax-Calculator does not compute the excess Social Security withholding credit"},
    {"feature": "qbi_dividends", "lines": ['f1040.line13a', 'sa.deduction', 'f1040.line15', 'f1040.line16', 'f1040.line20', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator has no input for section 199A dividends (Form 1099-DIV box 5), so its QBI deduction is zero"},
    {"feature": "special_gains", "lines": ['f1040.line16', 'f1040.line20', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator has no inputs for unrecaptured section 1250 gain or 28% rate gain (Form 1099-DIV boxes 2b, 2d)"},
    {"feature": "investment_interest_limited", "lines": ['sa.line17', 'sa.deduction', 'f1040.line13a', 'f1040.line15', 'f1040.line16', 'f1040.line20', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator deducts investment interest in full within itemizable interest paid; it does not apply the Form 4952 net-investment-income limit"},
    {"feature": "no_tax_either_way", "lines": ['sa.deduction', 'f1040.line15', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator treats a unit owing no tax under either deduction as taking the standard deduction; the project itemizes whenever itemized deductions exceed the standard deduction. The itemized total itself is compared on every return through a forced-itemize pass"},
    {"feature": "investment_interest_on_8960", "lines": ['f8960.tax', 'f1040.line24', 'f1040.tax_before_credits', 'f1040.line19', 'f1040.line28'],
     "reason": "Tax-Calculator does not deduct investment interest expense (Form 4952 line 8) on Form 8960 line 9a"},
]
# The credits limited by the tax (Form 2441 line 10, Form 8880 line 11, Form 5695 lines 14 and 31) move with
# Form 1040 line 16, so every limitation that sets line 16 aside sets them aside too.
TAX_LIMITED_CREDIT_LINES = ["f2441.line11", "s3.line2", "f8880.line12", "f5695.line15", "s3.line5a", "f5695.line32", "s3.line5b"]
for _mapping, _limitations in ((PE_MAP, PE_LIMITATIONS), (TC_MAP, TC_LIMITATIONS)):
    for _lim in _limitations:
        if "f1040.line16" in _lim["lines"]:
            _lim["lines"] = list(_lim["lines"]) + [l for l in TAX_LIMITED_CREDIT_LINES if l in _mapping and l not in _lim["lines"]]


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
            "self_employment_income": y(dollars(f.get("self_employment_income", 0))),
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
            # IRA contributions within the limit; an employer plan phases the deduction out.
            "traditional_ira_contributions": y(dollars(f.get("ira_contribution", 0))),
            "roth_ira_contributions": y(dollars(f.get("roth_contribution", 0))),
            "ira_active_participant": y(bool(f.get("ira_work_plan", False))),
            # Roles are supplied so an adult child stays a dependent; by age ordering
            # the engine would make an adult child the filer's spouse.
            "tax_unit_role_input": y("HEAD"),
        }
        p1, p2 = f.get("energy_part1") or {}, f.get("energy_part2") or {}
        energy = {"solar_electric_property_expenditures": p1.get("solar_electric", 0),
                  "solar_water_heating_property_expenditures": p1.get("solar_water", 0),
                  "qualified_battery_storage_technology_expenditures": p1.get("battery", 0),
                  "energy_efficient_insulation_expenditures": p2.get("insulation", 0),
                  "energy_efficient_door_expenditures": p2.get("door1", 0) + p2.get("door2", 0),
                  "energy_efficient_window_expenditures": p2.get("windows", 0),
                  "energy_efficient_central_air_conditioner_expenditures": p2.get("central_ac", 0),
                  "qualified_furnace_or_hot_water_boiler_expenditures": p2.get("furnace", 0),
                  "home_energy_audit_expenditures": p2.get("audit", 0),
                  "heat_pump_expenditures": p2.get("heat_pump", 0)}
        members = [pid]
        if f.get("joint"):
            sid = f"{pid}_s"
            people[sid] = {"age": y(f["spouse_age"]), "medicare_enrolled": y(False),
                           "employment_income": y(dollars(f["spouse_wages"])), "tax_unit_role_input": y("SPOUSE")}
            members.append(sid)
        for k, age in enumerate(f.get("children", [])):
            cid = f"{pid}_c{k + 1}"
            # Children 17 and over are full-time students in the generated cases.
            people[cid] = {"age": y(age), "is_full_time_student": y(age >= 17), "tax_unit_role_input": y("DEPENDENT")}
            members.append(cid)
        units[pid] = {"members": members,
                      "filing_status": y("JOINT" if f.get("joint") else "HEAD_OF_HOUSEHOLD" if f.get("hoh") else "SINGLE"),
                      "state_and_local_sales_or_income_tax": y(dollars(f["salt_income_tax"])),
                      "unrecaptured_section_1250_gain": y(dollars(f["unrecaptured_1250"])),
                      "foreign_tax_credit": y(dollars(f["foreign_tax"])),
                      "health_savings_account_ald": y(dollars(f.get("hsa_deduction", 0))),
                      # Form 5695 takes costs net of subsidies and rebates, which the generated costs are; the
                      # engine would otherwise net a modeled Department of Energy home electrification rebate
                      # (by income against the area median) out of the insulation and heat pump costs.
                      "high_efficiency_electric_home_rebate_percent_covered": y(0.0),
                      **{k: y(dollars(v)) for k, v in energy.items()}}
        fams[pid] = {"members": members}
        # Care expenses are an SPM-unit input the engine prorates over the unit's children.
        spms[pid] = {"members": members, "spm_unit_pre_subsidy_childcare_expenses": y(dollars(f.get("care_expenses", 0)))}
        hhs[pid] = {"members": members, "state_code": y("TX"),
                    "qualified_passenger_vehicle_loan_interest": y(dollars(f.get("car_loan_interest", 0)))}
    sim = Simulation(situation={"people": people, "tax_units": units, "families": fams, "spm_units": spms, "households": hhs})
    # Tax-unit ids come back in situation order, as do persons; the filer is the unit's first member.
    order = list(units.keys())
    head_index = {pid: k for k, pid in enumerate(people)}
    cache = {}
    def var(name):
        if name not in cache:
            # A person-level variable (such as self_employment_tax) is summed into its tax unit,
            # so that it is indexed like the tax-unit variables; "head:" reads the filer's own value.
            if name.startswith("head:"):
                cache[name] = sim.calculate(name[5:], YEAR)
            else:
                entity = sim.tax_benefit_system.variables[name].entity.key
                cache[name] = sim.calculate(name, YEAR, map_to="tax_unit") if entity == "person" else sim.calculate(name, YEAR)
        return cache[name]
    lines = {pid: {} for pid in order}
    for line, spec in PE_MAP.items():
        for i, pid in enumerate(order):
            lines[pid][line] = cents(combine(lambda n: float(var(n)[head_index[pid] if n.startswith("head:") else i]), spec))
    return {"version": pkg_version("policyengine-us"), "precision": PE_PRECISION, "lines": lines, "limitations": PE_LIMITATIONS,
            "pass_through": PE_PASS_THROUGH, "components": {line: len(spec) for line, spec in PE_MAP.items()}}


def run_taxcalc(cases):
    import taxcalc as tc, pandas as pd
    rows = []
    for i, c in enumerate(cases):
        f = c["facts"]
        ages = f.get("children", [])
        rows.append(dict(
            RECID=i + 1, MARS=2 if f.get("joint") else 4 if f.get("hoh") else 1, age_head=f.get("age", 40),
            age_spouse=f.get("spouse_age", 0), FLPDYR=YEAR,
            XTOT=(2 if f.get("joint") else 1) + len(ages), n24=sum(1 for a in ages if a < 17), nu18=sum(1 for a in ages if a < 18),
            n1820=sum(1 for a in ages if 18 <= a <= 20), n21=sum(1 for a in ages if a >= 21), EIC=f.get("eic_children", 0),
            e00900=dollars(f.get("self_employment_income", 0)), e00900p=dollars(f.get("self_employment_income", 0)),
            e00200=dollars(f["wages"] + f.get("spouse_wages", 0)), e00200p=dollars(f["wages"]), e00200s=dollars(f.get("spouse_wages", 0)), e02400=dollars(f.get("ss_benefits", 0)),
            e00300=dollars(f["interest"]), e00600=dollars(f["ordinary_dividends"]), e00650=dollars(f["qualified_dividends"]),
            # Distributions enter Schedule D line 13 and net against sales; Tax-Calculator's
            # e01100 is the no-Schedule-D path, so they go into net long-term gain instead.
            p22250=dollars(f["short_term_gain"]), p23250=dollars(f["long_term_gain"] + f["capital_gain_distributions"]), e01100=0.0,
            e17500=dollars(f["medical"]), e18400=dollars(f["salt_income_tax"]), e18500=dollars(f["salt_real_estate"]),
            e19200=dollars(f["mortgage_interest"] + f["investment_interest"]),
            e19800=dollars(f["cash_gifts"]), e20100=dollars(f["noncash_gifts"]), e07300=dollars(f["foreign_tax"]),
            e02300=dollars(f.get("unemployment", 0)), e03220=dollars(f.get("educator_deduction", 0)), e03290=dollars(f.get("hsa_deduction", 0)),
            tip_income=dollars(f.get("tips", 0)), overtime_income=dollars(f.get("overtime", 0)), auto_loan_interest=dollars(f.get("car_loan_interest", 0)),
            # Form 2441: the care expenses and the count of qualifying persons (children under 13).
            e32800=dollars(f.get("care_expenses", 0)), f2441=f.get("care_persons", 0), nu13=sum(1 for a in ages if a < 13),
            # The IRA contributions enter as the deduction (the phase-out is not computed), and the Form 5695
            # credits before their limits as one amount figured from the costs; the engine applies the tax limits.
            e03150=dollars(f.get("ira_contribution", 0)), e07260=dollars(f.get("energy_credit", 0)),
        ))
    df = pd.DataFrame(rows).astype(float)
    for col in ("RECID", "MARS", "FLPDYR", "XTOT", "n24", "nu18", "n1820", "n21", "EIC", "f2441", "nu13"):
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
            "pass_through": TC_PASS_THROUGH, "components": {line: len(spec) for line, spec in TC_MAP.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    cases = json.load(open(a.cases))
    out = {"engines": {"PolicyEngine-US": run_policyengine(cases), "Tax-Calculator": run_taxcalc(cases)}}
    ots = ots_adapter.run_ots(cases, YEAR, Path(a.out).resolve().parent / "ots")
    if ots is None:
        print("OpenTaxSolver: SKIPPED - package not built under .engines/opentaxsolver-src/ (see tools/engines/README.md)")
    else:
        out["engines"][ots_adapter.ENGINE_NAME] = ots
    json.dump(out, open(a.out, "w"))
    print(f"engines ran {len(cases)} cases -> {a.out}")


if __name__ == "__main__":
    main()
