# Proof-of-concept scope screening

- Document: `scope` (form, tax year 2025)
- Note: Stage 4 screening answers are explicit declarations, not automatic determinations of eligibility. Stage 5 wires these gates into the whole-return outcome.

## (helper) — `scope.schedule1`

- **Authored helper label:** Any income or adjustment requiring Schedule 1, including a taxable state or local tax refund, unemployment compensation, self-employment income or Schedule SE (including clergy and church employee income), Schedule C income including statutory-employee wages, or an exclusion of Medicaid waiver payments (Schedule 1 line 8s)? (Schedule 1-A deductions are asked separately.)
- **Encoded (Bool):** Input — Any income or adjustment requiring Schedule 1, including a taxable state or local tax refund, unemployment compensation, self-employment income or Schedule SE (including clergy and church employee income), Schedule C income including statutory-employee wages, or an exclusion of Medicaid waiver payments (Schedule 1 line 8s)? (Schedule 1-A deductions are asked separately.)
- Expr: `{"op":"input","source":"Any income or adjustment requiring Schedule 1, including a taxable state or local tax refund, unemployment compensation, self-employment income or Schedule SE (including clergy and church employee income), Schedule C income including statutory-employee wages, or an exclusion of Medicaid waiver payments (Schedule 1 line 8s)? (Schedule 1-A deductions are asked separately.)"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.schedule1a`

- **Authored helper label:** Do you qualify for any Schedule 1-A deduction (qualified tips, qualified overtime compensation, qualified passenger vehicle loan interest, or the enhanced deduction for a filer born before January 2, 1961), whether or not you planned to claim it?
- **Encoded (Bool):** Input — Do you qualify for any Schedule 1-A deduction (qualified tips, qualified overtime compensation, qualified passenger vehicle loan interest, or the enhanced deduction for a filer born before January 2, 1961), whether or not you planned to claim it?
- Expr: `{"op":"input","source":"Do you qualify for any Schedule 1-A deduction (qualified tips, qualified overtime compensation, qualified passenger vehicle loan interest, or the enhanced deduction for a filer born before January 2, 1961), whether or not you planned to claim it?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.credits`

- **Authored helper label:** Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit and the earned income credit, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?
- **Encoded (Bool):** Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit and the earned income credit, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?
- Expr: `{"op":"input","source":"Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit and the earned income credit, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.other_income`

- **Authored helper label:** Any retirement, Social Security, nonresident alien (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends and supported securities sales, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), dependent care or adoption benefits, other earned income (Form 1040 lines 1b-1h), or income or loss from a passive activity (including gain on selling an interest in one)?
- **Encoded (Bool):** Input — Any retirement, Social Security, nonresident alien (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends and supported securities sales, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), dependent care or adoption benefits, other earned income (Form 1040 lines 1b-1h), or income or loss from a passive activity (including gain on selling an interest in one)?
- Expr: `{"op":"input","source":"Any retirement, Social Security, nonresident alien (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends and supported securities sales, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), dependent care or adoption benefits, other earned income (Form 1040 lines 1b-1h), or income or loss from a passive activity (including gain on selling an interest in one)?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.other_line16`

- **Authored helper label:** Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?
- **Encoded (Bool):** Input — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?
- Expr: `{"op":"input","source":"Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready`

- **Authored helper label:** All declared scope screens passed
- **Encoded (Bool):** true = true
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1. Schedule 1 income and adjustments are outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.schedule1a is true, cannot complete Schedule 1-A. Schedule 1-A deductions are outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.credits is true, cannot complete Other credit forms (Schedule 3 lines 2 to 4, 5b, 6d, 6f, 6l and 6m; Form 1040 lines 29 to 31). Credits other than the foreign tax credit by election, the excess social security credit, the Schedule 8812 credits and the earned income credit require forms outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_income is true, cannot complete Form 1040 additional income/return forms. Prepare the required unsupported income or return treatment. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_line16 is true, cannot complete Form 1040 line 16 additional tax forms. Prepare the applicable additional tax or alternative worksheet. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when s3.married is true, cannot complete Schedule 3 line 11 (per-spouse computation). The interview currently represents one person. Married filing statuses are unsupported for this per-spouse rule. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
