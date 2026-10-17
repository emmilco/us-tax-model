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
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | d0173256c777b69a079b5239cb98fe29d3353314f410cdc88356a94a2182d702 |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?
Status: **MATCH**

Model: Form 1040 line 8 reads 'Additional income from Schedule 1, line 10' and line 10 reads 'Adjustments to income from Schedule 1, line 26', so a yes/no screen for any Schedule 1 item covers both. The state/local refund example is not in the given text, but it only illustrates the screen.

### schedule1a — Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enha
Status: **MATCH**

Model: Form 1040 line 13b reads 'Additional deductions from Schedule 1-A, line 38', and the screen asks whether any such deduction applies. The listed examples (tips, overtime, car-loan interest, senior deduction) are not in the given text, but they only illustrate the screen.

### credits — Any credit outside the simple foreign tax credit, the excess Social Security credit, the c
Status: **UNCLEAR**

Restated: Input — Any credit outside the simple foreign tax credit, the excess Social Security credit, the child tax credit, the credit for other dependents and the additional child tax credit?

Model: Form 1040 shows lines 19, 20, 27a, 28 and 29–31, and the instructions show Schedule 3 Part II lines 9–13z. Schedule 3 Part I lines 1–6m (foreign tax credit, 5b, 6d and so on) are not in the given text, so the exclusions the refusal names cannot be checked. Also, Schedule 3 line 10 ('Amount Paid With Request for Extension') flows to line 31 but is not a credit, so this screen would not catch it.

Ruling: representation; project retained. The screen names the credits the slice computes; Schedule 3 Part I (lines 1 to 6m) is encoded in `s3.yaml` and judged in its own render log, where line 1 is the foreign tax credit by election and lines 2 to 4, 5b and 6d to 6m refuse on this screen. Schedule 3 line 10 (amount paid with a request for extension) is a payment the filer supplies as `s3.line10`, not a credit, and is not screened here. No change to the data.

### other_income — Any retirement, Social Security, nonresident or other income/return treatment outside wage
Status: **MATCH**

Model: The screen matches Form 1040 lines 1b–1h: household employee wages not on W-2, tip income not on line 1a, Medicaid waiver payments, dependent care benefits, adoption benefits, Form 8919 wages and other earned income. It also covers lines 4–6 (IRA, pensions, social security). The refusal names this whole set as unsupported.

### other_line16 — Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 el
Status: **MATCH**

Model: Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', so a screen for any additional line 16 tax fits. Form 8615 and section 962 fall under the unspecified box 3, which the given text does not detail, but they only illustrate the screen.

### ready — All declared scope screens passed
Status: **MATCH**

Model: Each refusal names the excluded form or line, consistent with the Form 1040 references above. The married gate is supported by the Schedule 3 line 11 instruction 'Figure this amount separately for you and your spouse', and the gate tests both married filing statuses shown on Form 1040.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "Form 1040 line 8 reads 'Additional income from Schedule 1, line 10' and line 10 reads 'Adjustments to income from Schedule 1, line 26', so a yes/no screen for any Schedule 1 item covers both. The state/local refund example is not in the given text, but it only illustrates the screen."
  - key: "schedule1a"
    status: MATCH
    reason: "Form 1040 line 13b reads 'Additional deductions from Schedule 1-A, line 38', and the screen asks whether any such deduction applies. The listed examples (tips, overtime, car-loan interest, senior deduction) are not in the given text, but they only illustrate the screen."
  - key: "credits"
    status: UNCLEAR
    reason: "Form 1040 shows lines 19, 20, 27a, 28 and 29–31, and the instructions show Schedule 3 Part II lines 9–13z. Schedule 3 Part I lines 1–6m (foreign tax credit, 5b, 6d and so on) are not in the given text, so the exclusions the refusal names cannot be checked. Also, Schedule 3 line 10 ('Amount Paid With Request for Extension') flows to line 31 but is not a credit, so this screen would not catch it."
  - key: "other_income"
    status: MATCH
    reason: "The screen matches Form 1040 lines 1b–1h: household employee wages not on W-2, tip income not on line 1a, Medicaid waiver payments, dependent care benefits, adoption benefits, Form 8919 wages and other earned income. It also covers lines 4–6 (IRA, pensions, social security). The refusal names this whole set as unsupported."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', so a screen for any additional line 16 tax fits. Form 8615 and section 962 fall under the unspecified box 3, which the given text does not detail, but they only illustrate the screen."
  - key: "ready"
    status: MATCH
    reason: "Each refusal names the excluded form or line, consistent with the Form 1040 references above. The married gate is supported by the Schedule 3 line 11 instruction 'Figure this amount separately for you and your spouse', and the gate tests both married filing statuses shown on Form 1040."
```
```
