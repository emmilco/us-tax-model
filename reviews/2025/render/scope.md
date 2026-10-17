# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 26ee903da5220ab780c6dc71a65ca5b76a6e7e3a92cfea47c1e13a37766ff738 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 5 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?
Status: **MATCH**

Model: Form 1040 line 8 is 'Additional income from Schedule 1, line 10' and line 10 is 'Adjustments to income from Schedule 1, line 26', so a yes/no screen for any Schedule 1 item matches. The refusal names Schedule 1 as excluded. The state/local refund example is not in the given text, but it does not change the gate.

### schedule1a — Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enha
Status: **MATCH**

Model: Form 1040 line 13b reads 'Additional deductions from Schedule 1-A, line 38', so screening for any Schedule 1-A deduction matches. The refusal names Schedule 1-A. The listed examples (tips, overtime, car-loan interest, senior deduction) are not in the given text, but they do not change the gate.

### credits — Any credit outside the simple foreign tax credit, the excess Social Security credit, the c
Status: **UNCLEAR**

Restated: Input — Any credit outside the simple foreign tax credit, the excess Social Security credit, the child tax credit, the credit for other dependents and the additional child tax credit?

Model: Schedule 3 Part I text is not provided, so the refusal's list of Schedule 3 lines (2–4, 5b, 6d, 6f, 6l, 6m) cannot be checked against the excluded credits. Page 117 also shows that 1040 line 31 (Schedule 3 line 15) includes non-credit items such as line 10 'Amount Paid With Request for Extension To File'. A question asking only about 'credits' may not capture those items.

Ruling: representation; project retained. The screen names the credits the slice computes; Schedule 3 Part I (lines 1 to 6m) is encoded in `s3.yaml` and judged in its own render log, where line 1 is the foreign tax credit by election and lines 2 to 4, 5b and 6d to 6m refuse on this screen. Schedule 3 line 10 (amount paid with a request for extension) is a payment the filer supplies as `s3.line10`, not a credit, and is not screened here. No change to the data.

### other_income — Any retirement, Social Security, nonresident or other income/return treatment outside wage
Status: **MATCH**

Model: The screen covers what Form 1040 lines 1b–1h and 4–6 report. Lines 1b–1h are 'Household employee wages not reported on Form(s) W-2', 'Tip income not reported on line 1a', 'Medicaid waiver payments', 'Taxable dependent care benefits', 'Employer-provided adoption benefits', 'Wages from Form 8919' and 'Other earned income'. Lines 4–6 report IRA distributions, pensions and social security. The refusal names these as excluded.

### other_line16 — Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 el
Status: **MATCH**

Model: Form 1040 line 16 reads 'Check if any from Form(s): 1 8814 2 4972 3'. Screening for any such additional tax and refusing it is a valid narrowing. Form 8615 and the section 962 election are not named in the given text; the third box is unlabeled, but including them only broadens the refusal.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This is a constant gate with each excluded case covered by a named refusal. The s3.married refusal relies on the instruction 'Figure this amount separately for you and your spouse', which applies to excess social security for joint filers. Refusing MFS as well is broader than the text requires, but an over-broad refusal is permitted narrowing.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "Form 1040 line 8 is 'Additional income from Schedule 1, line 10' and line 10 is 'Adjustments to income from Schedule 1, line 26', so a yes/no screen for any Schedule 1 item matches. The refusal names Schedule 1 as excluded. The state/local refund example is not in the given text, but it does not change the gate."
  - key: "schedule1a"
    status: MATCH
    reason: "Form 1040 line 13b reads 'Additional deductions from Schedule 1-A, line 38', so screening for any Schedule 1-A deduction matches. The refusal names Schedule 1-A. The listed examples (tips, overtime, car-loan interest, senior deduction) are not in the given text, but they do not change the gate."
  - key: "credits"
    status: UNCLEAR
    reason: "Schedule 3 Part I text is not provided, so the refusal's list of Schedule 3 lines (2–4, 5b, 6d, 6f, 6l, 6m) cannot be checked against the excluded credits. Page 117 also shows that 1040 line 31 (Schedule 3 line 15) includes non-credit items such as line 10 'Amount Paid With Request for Extension To File'. A question asking only about 'credits' may not capture those items."
  - key: "other_income"
    status: MATCH
    reason: "The screen covers what Form 1040 lines 1b–1h and 4–6 report. Lines 1b–1h are 'Household employee wages not reported on Form(s) W-2', 'Tip income not reported on line 1a', 'Medicaid waiver payments', 'Taxable dependent care benefits', 'Employer-provided adoption benefits', 'Wages from Form 8919' and 'Other earned income'. Lines 4–6 report IRA distributions, pensions and social security. The refusal names these as excluded."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads 'Check if any from Form(s): 1 8814 2 4972 3'. Screening for any such additional tax and refusing it is a valid narrowing. Form 8615 and the section 962 election are not named in the given text; the third box is unlabeled, but including them only broadens the refusal."
  - key: "ready"
    status: MATCH
    reason: "This is a constant gate with each excluded case covered by a named refusal. The s3.married refusal relies on the instruction 'Figure this amount separately for you and your spouse', which applies to excess social security for joint filers. Refusing MFS as well is broader than the text requires, but an over-broad refusal is permitted narrowing."
```
```
