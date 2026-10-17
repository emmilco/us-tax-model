# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9914d5a7dfc7326a92db2d8a7937c673d1a241f48adb38050823658aa7610d40 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 6 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1, including a taxable state/local tax refund?
Status: **MATCH**

Model: This is a filer-answered scope screen. Form 1040 takes Schedule 1 amounts only on line 8 ("Additional income from Schedule 1, line 10") and line 10 ("Adjustments to income from Schedule 1, line 26"), and the screen refuses any such case. The state/local refund example is not in the text given, but it only narrows the screen.

### schedule1a — Any deduction claimed on Schedule 1-A, including tips, overtime, car-loan interest or enha
Status: **MATCH**

Model: Form 1040 line 13b reads "Additional deductions from Schedule 1-A, line 38", and this screen refuses any Schedule 1-A deduction. The listed examples (tips, overtime, car-loan interest, senior deduction) are not in the text given, but the screen's "any deduction" wording does not depend on them.

### credits — Any credit outside the simple foreign tax credit, the excess Social Security credit, the c
Status: **MATCH**

Model: The supported credits match Form 1040 lines 19, 27a and 28 and the Schedule 3 line 11 excess social security credit described in the instructions; any other credit (for example Form 1040 lines 29–31 or Schedule 3 line 12 fuel credits) triggers the refusal. The Schedule 3 nonrefundable line numbers in the refusal (lines 2–4, 5b, 6d, 6f, 6l, 6m) and the 'simple foreign tax credit' cannot be checked against the pages given. Non-credit Schedule 3 payments (line 10 extension payment, line 13d deferred 965 amount) fall outside this screen's wording.

### other_income — Any retirement, Social Security, nonresident or other income/return treatment outside wage
Status: **MATCH**

Model: The screen covers Form 1040 lines 1b–1h: household wages, tips and Form 8919 wages not on a W-2, "Medicaid waiver payments", dependent care benefits, adoption benefits and "Other earned income". It also covers IRA, pension and Social Security lines 4–6, leaving only lines 1a, 2b, 3b and 7a in scope. The line 1i "Nontaxable combat pay election" is not named explicitly but falls under 'other ... return treatment'.

### other_line16 — Any additional Form 1040 line 16 tax, including Forms 8814, 4972, 8615 or a section 962 el
Status: **MATCH**

Model: Line 16 reads "Check if any from Form(s): 1 8814 2 4972 3". The screen names 8814 and 4972 and covers the open box 3 through 'any additional ... tax'. Forms 8615 and section 962 are not in the text given, but they are offered only as examples.

### ready — All declared scope screens passed
Status: **MATCH**

Model: Ready is a constant true that is gated by the refusals, which properly exclude each unsupported case. The married-status refusal follows the Schedule 3 line 11 instruction "Figure this amount separately for you and your spouse". That rule applies only "if filing a joint return", so also refusing MFS is a permissible over-narrowing.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-answered scope screen. Form 1040 takes Schedule 1 amounts only on line 8 (\"Additional income from Schedule 1, line 10\") and line 10 (\"Adjustments to income from Schedule 1, line 26\"), and the screen refuses any such case. The state/local refund example is not in the text given, but it only narrows the screen."
  - key: "schedule1a"
    status: MATCH
    reason: "Form 1040 line 13b reads \"Additional deductions from Schedule 1-A, line 38\", and this screen refuses any Schedule 1-A deduction. The listed examples (tips, overtime, car-loan interest, senior deduction) are not in the text given, but the screen's \"any deduction\" wording does not depend on them."
  - key: "credits"
    status: MATCH
    reason: "The supported credits match Form 1040 lines 19, 27a and 28 and the Schedule 3 line 11 excess social security credit described in the instructions; any other credit (for example Form 1040 lines 29–31 or Schedule 3 line 12 fuel credits) triggers the refusal. The Schedule 3 nonrefundable line numbers in the refusal (lines 2–4, 5b, 6d, 6f, 6l, 6m) and the 'simple foreign tax credit' cannot be checked against the pages given. Non-credit Schedule 3 payments (line 10 extension payment, line 13d deferred 965 amount) fall outside this screen's wording."
  - key: "other_income"
    status: MATCH
    reason: "The screen covers Form 1040 lines 1b–1h: household wages, tips and Form 8919 wages not on a W-2, \"Medicaid waiver payments\", dependent care benefits, adoption benefits and \"Other earned income\". It also covers IRA, pension and Social Security lines 4–6, leaving only lines 1a, 2b, 3b and 7a in scope. The line 1i \"Nontaxable combat pay election\" is not named explicitly but falls under 'other ... return treatment'."
  - key: "other_line16"
    status: MATCH
    reason: "Line 16 reads \"Check if any from Form(s): 1 8814 2 4972 3\". The screen names 8814 and 4972 and covers the open box 3 through 'any additional ... tax'. Forms 8615 and section 962 are not in the text given, but they are offered only as examples."
  - key: "ready"
    status: MATCH
    reason: "Ready is a constant true that is gated by the refusals, which properly exclude each unsupported case. The married-status refusal follows the Schedule 3 line 11 instruction \"Figure this amount separately for you and your spouse\". That rule applies only \"if filing a joint return\", so also refusing MFS is a permissible over-narrowing."
```
```
