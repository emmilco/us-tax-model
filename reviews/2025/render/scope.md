# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 46afc7c5c5dd556cbb0a410bb953944f3adf0e75a9e06908ba4df3ad6235bcb4 |
| subject sha256 | a6f16dd3f7d2c8979e080362c9f88caf03b68f5c1cc069f454bf92eeb17b6dbb |
| lines judged | 5 |
| match / mismatch / unclear / missing | 3 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **UNCLEAR**

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or clergy income; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)

Model: This is a filer-answered screening question. The given text shows only Form 1040 line 8 "Additional income from Schedule 1, line 10" and line 10 "Adjustments to income from Schedule 1, line 26". Schedule 1 and its instructions are not provided, so the items it names (line 8s, lines 12, 14 and 23, and the listed income and adjustment types) cannot be checked against IRS text.

Ruling: unclear for want of text; restatement accepted. A filer-answered scope question; the model was given only Form 1040, whose line 8, "Additional income from Schedule 1, line 10", and line 10, "Adjustments to income from Schedule 1, line 26" (f1040 (2025), lines 8 and 10), it found consistent. Checked against Schedule 1 itself (f1040s1 p. 1, line 8s, "Nontaxable amount of Medicaid waiver payments included on Form 1040, line [...] 1a or 1d"; p. 2, line 12, "Certain business expenses of reservists, performing artists, and fee-basis government officials", line 14, "Moving expenses for members of the Armed Forces", line 23, "Archer MSA deduction"): the line numbers it names are right. Its list of items asked separately is the Stage 16 slice (D1 to D3: the state refund, pre-2019 alimony, the line 8 items, the early withdrawal penalty, the IRA deduction, jury duty pay given to the employer, besides the earlier items), each of which has its own Schedule 1 line in forms/2025/s1.yaml, and the refusal shown for a Yes (scope.ready, Form 1040 lines 8 and 10) now names the same items (BUG-0081, T-050). No change.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695) and the net premium tax credit you enter from Form 8962 (Schedule 3 line 9), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The given Form 1040 text shows line 20 "Amount from Schedule 3, line 8" and line 31 "Amount from Schedule 3, line 15", and lines 29 and 30 as the American opportunity and refundable adoption credits. Schedule 3 is not provided, so the listed credits, the Schedule 3 line 9 reference and the Part I amounts cannot be verified.

Ruling: unclear for want of text; restatement accepted (as the prior rulings). A filer-answered scope question; the model could see Form 1040 lines 29 to 31 and found them consistent. Checked against Schedule 3 (f1040s3 p. 1): Part I is lines 1 to 8, line 3 "Education credits from Form 8863, line 19" and lines 6a to 6z the other nonrefundable credits (6l "Amount on Form 8978, line 14"), and line 9 "Net premium tax credit. Attach Form 8962" is in Part II, as the question says. The credits it lists as supported are the Stage 15 slice plus the net premium tax credit (T-050), and its refusal (scope.ready) names what stays refused, Schedule 3 lines 3 and 6a to 6z and Form 1040 lines 29 to 31. No change.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: The question is consistent with Form 1040 page 1, where lines 1b–1d and 1f–1h are household employee wages, unreported tips, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income. Line 1e (dependent care benefits) and nonresident alien status are routed to this screen as the restatement describes.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: Form 1040 line 16 reads "Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3", which agrees with screening out Form 8814 and Form 4972. The other examples come from line 16 instructions that are not given, but they only widen a screen the filer answers and do not change any computed value.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This gate only combines the scope screens, and each refusal names what it excludes. The MFS refusal agrees with the instructions: "You also can't take the standard deduction if your spouse itemizes deductions" and the limits on credits for a separate return. Form 1040 line 6d, which concerns MFS filers who lived apart, supports the Social Security point.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "This is a filer-answered screening question. The given text shows only Form 1040 line 8 \"Additional income from Schedule 1, line 10\" and line 10 \"Adjustments to income from Schedule 1, line 26\". Schedule 1 and its instructions are not provided, so the items it names (line 8s, lines 12, 14 and 23, and the listed income and adjustment types) cannot be checked against IRS text."
  - key: "credits"
    status: UNCLEAR
    reason: "The given Form 1040 text shows line 20 \"Amount from Schedule 3, line 8\" and line 31 \"Amount from Schedule 3, line 15\", and lines 29 and 30 as the American opportunity and refundable adoption credits. Schedule 3 is not provided, so the listed credits, the Schedule 3 line 9 reference and the Part I amounts cannot be verified."
  - key: "other_income"
    status: MATCH
    reason: "The question is consistent with Form 1040 page 1, where lines 1b–1d and 1f–1h are household employee wages, unreported tips, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income. Line 1e (dependent care benefits) and nonresident alien status are routed to this screen as the restatement describes."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads \"Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3\", which agrees with screening out Form 8814 and Form 4972. The other examples come from line 16 instructions that are not given, but they only widen a screen the filer answers and do not change any computed value."
  - key: "ready"
    status: MATCH
    reason: "This gate only combines the scope screens, and each refusal names what it excludes. The MFS refusal agrees with the instructions: \"You also can't take the standard deduction if your spouse itemizes deductions\" and the limits on credits for a separate return. Form 1040 line 6d, which concerns MFS filers who lived apart, supports the Social Security point."
```
```
