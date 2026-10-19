# Data-level properties

Properties of spec 6.3 checked over 400 generated returns (fast-check, seed 7, every filing status). "Applicable" counts the cases where the property's premise held and its values were computed; a refusal or an unknown makes a case inapplicable. A failure is reported with the smallest counterexample fast-check found.

| Property | Statement | Cases | Applicable | Result |
| --- | --- | --- | --- | --- |
| sdtw_skip_rule | Computing lines 23–43 of the Schedule D Tax Worksheet unconditionally gives the same lines 45, 47 and Form 1040 line 16 as skipping them, and every skipped component of line 41 and line 45 is zero when computed anyway. | 400 | 157 | holds |
| tax_bounds | Form 1040 line 16 is non-negative, at most the top rate (37/100) on taxable income plus one Tax Table band ($50), and at most the tax on all taxable income from the Tax Table or Tax Computation Worksheet. | 400 | 157 | holds |
| deduction_choice | With no election to itemize and no spouse itemizing, Form 1040 line 16 under the project's standard-or-itemized choice is at most line 16 under either deduction forced. | 400 | 157 | holds |
| refusal_propagates | No line computes a value from an operand that is a refusal; every line evaluated from a refused operand is a refusal. | 400 | 297 | holds |
| tax_monotone | Raising W-2 box 1 of the first employer, all else fixed, never lowers Form 1040 line 16. | 400 | 157 | holds |
| tax_monotone_by_method | Raising W-2 box 1 of the first employer, all else fixed, never lowers the Qualified Dividends and Capital Gain Tax Worksheet line 25 or the Schedule D Tax Worksheet line 47, each where it is computed on both returns. | 400 | 157 | holds |

## sdtw_skip_rule

- Rewritten lines (skip rule removed in the variant): 21 — 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43.
- Cases where Form 1040 line 16 came from this worksheet: 157. Cases with lines 1 and 16 equal (lines 23–43 skipped): 82; lines 1 and 32 equal with lines 1 and 16 different (lines 33–43 skipped): 7; Schedule D line 19 zero after line 32 (lines 35–40 skipped): 62; lines 41–43 skipped after line 32: 2.

## deduction_choice

- Cases where total tax (line 24) under the project's choice exceeded the better alternative: 0.

## tax_monotone

- Cases where total tax (line 24) fell as wages rose: 0.

## tax_monotone_by_method

- Cases compared: QDCG worksheet line 25 157, Schedule D Tax Worksheet line 47 157.

## Branch coverage of the generated corpus

1082 of 1117 branches (choose guards, Bool lines both ways, floor and positive sides of subtract_floor0, left and right of smaller_of and larger_of) reached by the 400 generated returns. Unreached:

- carloan.requirements:false
- div.amt:true
- eic.step1_foreign:false
- eic.step1_resident:false
- eic.step2_other:false
- eic.clergy:true
- f1040.line6d:true
- f1040.line27b:true
- f8889.bad_months:true
- f8889.line13_figured:right
- f8959.line12:positive
- f8959.line16:positive
- f8960.bad_allocation:true
- household.roster_ok:false
- household.roster_bad:true
- otjob.figured#4
- otjob.figured#5
- person.itin_applied:true
- person.hsa_repeated:true
- qdcg.line25:right
- s1a.line4c_one:right
- s1a.line18_over:true
- s1a.line18_pos:positive
- s1a.line21_amount#1
- s1a.line24_calc:right
- s1a.spouse_died_before_65:true
- s1a.spouse_senior_decedent:true
- s8812.few_children:false
- s8812.line27#1
- sa.standard#0
- sales.special:true
- scope.ready:false
- sd.screen:true
- sdtw.line47:right
- tipjob.col_d:right
