# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 636dcbdf671c3a7044ea02f058554316e077e9f76659513b28dc295eb19cffac |
| subject sha256 | 27dfae9e17862c05779bc6b50b1c48dbb643c0785d63f21e8e97cb81d697af2b |
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

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or clergy income; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)

Model: The text given confirms only that Form 1040 line 8 is 'Additional income from Schedule 1, line 10' and line 10 is 'Adjustments to income from Schedule 1, line 26'. Schedule 1 itself is not provided, so the Schedule 1 line numbers named here (8s, 12, 14, 23) and the split between supported and unsupported items cannot be checked.

Ruling: unclear for want of text; restatement accepted. A filer-answered scope question; the model was given only Form 1040, whose line 8, "Additional income from Schedule 1, line 10", and line 10, "Adjustments to income from Schedule 1, line 26" (f1040 (2025), lines 8 and 10), it found consistent. Checked against Schedule 1 itself (f1040s1 p. 1, line 8s, "Nontaxable amount of Medicaid waiver payments included on Form 1040, line [...] 1a or 1d"; p. 2, line 12, "Certain business expenses of reservists, performing artists, and fee-basis government officials", line 14, "Moving expenses for members of the Armed Forces", line 23, "Archer MSA deduction"): the line numbers it names are right. Its list of items asked separately is the Stage 16 slice (D1 to D3: the state refund, pre-2019 alimony, the line 8 items, the early withdrawal penalty, the IRA deduction, jury duty pay given to the employer, besides the earlier items), each of which has its own Schedule 1 line in forms/2025/s1.yaml, and the refusal shown for a Yes (scope.ready, Form 1040 lines 8 and 10) now names the same items (BUG-0081, T-050). No change.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695) and the net premium tax credit you enter from Form 8962 (Schedule 3 line 9), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: Form 1040 lines 29 to 31 are confirmed ('American opportunity credit from Form 8863', 'Refundable adoption credit from Form 8839', 'Amount from Schedule 3, line 15'). Schedule 3 is not provided, so the references to Schedule 3 Part I, line 9 and lines 6a to 6z cannot be checked.

Ruling: unclear for want of text; restatement accepted (as the prior rulings). A filer-answered scope question; the model could see Form 1040 lines 29 to 31 and found them consistent. Checked against Schedule 3 (f1040s3 p. 1): Part I is lines 1 to 8, line 3 "Education credits from Form 8863, line 19" and lines 6a to 6z the other nonrefundable credits (6l "Amount on Form 8978, line 14"), and line 9 "Net premium tax credit. Attach Form 8962" is in Part II, as the question says. The credits it lists as supported are the Stage 15 slice plus the net premium tax credit (T-050), and its refusal (scope.ready) names what stays refused, Schedule 3 lines 3 and 6a to 6z and Form 1040 lines 29 to 31. No change.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: The lines named match Form 1040: 1b household employee wages, 1c tip income, 1d Medicaid waiver payments, 1f adoption benefits, 1g Form 8919 wages and 1h other earned income. Line 1e 'Taxable dependent care benefits from Form 2441' is properly left in scope for W-2 box 10 amounts, and the instructions confirm nonresident alien status affects return treatment.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which matches the screen for Form 8814, Form 4972 and other line 16 items. The other listed items are a reasonable scope narrowing that the refusal names.

### ready — All declared scope screens passed
Status: **MATCH**

Model: The refusals name each excluded case. The MFS reasons agree with the instructions ('you can't take ... the student loan interest deduction, or the education credits', 'can't take the standard deduction if your spouse itemizes deductions') and with Form 1040 line 6d on spouses who lived apart. The s3.mfs gate tests the 'Married filing separately' filing status box.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "The text given confirms only that Form 1040 line 8 is 'Additional income from Schedule 1, line 10' and line 10 is 'Adjustments to income from Schedule 1, line 26'. Schedule 1 itself is not provided, so the Schedule 1 line numbers named here (8s, 12, 14, 23) and the split between supported and unsupported items cannot be checked."
  - key: "credits"
    status: UNCLEAR
    reason: "Form 1040 lines 29 to 31 are confirmed ('American opportunity credit from Form 8863', 'Refundable adoption credit from Form 8839', 'Amount from Schedule 3, line 15'). Schedule 3 is not provided, so the references to Schedule 3 Part I, line 9 and lines 6a to 6z cannot be checked."
  - key: "other_income"
    status: MATCH
    reason: "The lines named match Form 1040: 1b household employee wages, 1c tip income, 1d Medicaid waiver payments, 1f adoption benefits, 1g Form 8919 wages and 1h other earned income. Line 1e 'Taxable dependent care benefits from Form 2441' is properly left in scope for W-2 box 10 amounts, and the instructions confirm nonresident alien status affects return treatment."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which matches the screen for Form 8814, Form 4972 and other line 16 items. The other listed items are a reasonable scope narrowing that the refusal names."
  - key: "ready"
    status: MATCH
    reason: "The refusals name each excluded case. The MFS reasons agree with the instructions ('you can't take ... the student loan interest deduction, or the education credits', 'can't take the standard deduction if your spouse itemizes deductions') and with Form 1040 line 6d on spouses who lived apart. The s3.mfs gate tests the 'Married filing separately' filing status box."
```
```
