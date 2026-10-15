# Proof-of-concept scope screening

- Document: `scope` (form, tax year 2025)
- Note: Stage 4 screening answers are explicit declarations, not automatic determinations of eligibility. Stage 5 wires these gates into the whole-return outcome.

## (helper) — `scope.schedule1`

- **Authored helper label:** Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?
- **Encoded (Bool):** Input — Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?
- Expr: `{"op":"input","source":"Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.schedule1a`

- **Authored helper label:** Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enhanced senior deduction?
- **Encoded (Bool):** Input — Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enhanced senior deduction?
- Expr: `{"op":"input","source":"Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enhanced senior deduction?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.credits`

- **Authored helper label:** Any dependent or other credit outside the simple foreign tax credit and excess Social Security credit?
- **Encoded (Bool):** Input — Any dependent or other credit outside the simple foreign tax credit and excess Social Security credit?
- Expr: `{"op":"input","source":"Any dependent or other credit outside the simple foreign tax credit and excess Social Security credit?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.other_income`

- **Authored helper label:** Any retirement, Social Security, nonresident or other income/return treatment outside wages, interest, dividends and supported securities sales?
- **Encoded (Bool):** Input — Any retirement, Social Security, nonresident or other income/return treatment outside wages, interest, dividends and supported securities sales?
- Expr: `{"op":"input","source":"Any retirement, Social Security, nonresident or other income/return treatment outside wages, interest, dividends and supported securities sales?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.other_line16`

- **Authored helper label:** Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 election?
- **Encoded (Bool):** Input — Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 election?
- Expr: `{"op":"input","source":"Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 election?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready`

- **Authored helper label:** All declared scope screens passed
- **Encoded (Bool):** true = true
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1. Schedule 1 income and adjustments are outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.schedule1a is true, cannot complete Schedule 1-A. Schedule 1-A deductions are outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.credits is true, cannot complete Schedule 8812 / other credit forms. Dependent and other unsupported credits require forms outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_income is true, cannot complete Form 1040 additional income/return forms. Prepare the required unsupported income or return treatment. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_line16 is true, cannot complete Form 1040 line 16 additional tax forms. Prepare the applicable additional tax or alternative worksheet. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when s3.married is true, cannot complete Schedule 3 line 11 (per-spouse computation). The interview currently represents one person. Married filing statuses are unsupported for this per-spouse rule. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
