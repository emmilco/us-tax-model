# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | aeb1093d70c33f816a9820ecad746ef693b7a8040416837294e48b0e253cd30e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c19986791d91c8e0df9e7b353fde8f8bdd8aa3c6b766a45862738d604ee64383 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 3 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **UNCLEAR**

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)

Model: Schedule 1 and its instructions are not in the pages given, so the carved-out items and the references to lines 8s, 12, 14 and 23 cannot be checked. The given text confirms only that Form 1040 lines 8 and 10 draw from Schedule 1 and describes the clergy categories, so the Schedule 1 line list and instructions are what is missing.

Ruling: interface gap; f1040 (2025) line 8, "Additional income from Schedule 1, line 10", and line 10, "Adjustments to income from Schedule 1, line 26". The pages given were Form 1040 pp. 1-2 and i1040gi pp. 14, 36 and 43; Schedule 1 and its instructions, which would decide the carved-out items and the line 8s, 12, 14 and 23 references, are not among them (a coverage gap of the review). The changed text is checked: BUG-0233 replaced "clergy income" with "income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner", which is i1040gi p. 43, Clergy, "The following instructions apply to ministers, members of religious orders who have not taken a vow of poverty, and Christian Science practitioners", word for word, as the model confirms; it widens the screen to the two groups the old word could be read to leave out, so no filer who passed before now passes wrongly. The line numbers were checked against Schedule 1 in the earlier rulings (f1040s1 p. 1, line 8s; p. 2, lines 12, 14 and 23). Restatement accepted.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695), the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9) and the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: Schedule 3 and its instructions are missing, so the claims about Schedule 3 Part I and line 9 cannot be checked, and page 36 only points to Schedule 3 line 6l for a negative Form 8978 line 14 amount. Form 1040 lines 19, 27a, 28 and 29 fit the supported credits, and the refusal keeps the line 30 adoption credit out of scope, but its reference to all of line 31 cannot be reconciled with the supported Schedule 3 line 9 credit without Schedule 3.

Ruling: interface gap; f1040s3 p. 1: Part I is lines 1 to 8, line 3 "Education credits from Form 8863, line 19" and lines 6a to 6z the other nonrefundable credits (6l the Form 8978 line 14 amount); Part II line 9 "Net premium tax credit. Attach Form 8962", which flows with the other Part II lines through line 15 to Form 1040 line 31. Schedule 3 and its instructions were not given (pages: Form 1040 pp. 1-2, i1040gi pp. 14, 36, 43), as the model says. The refusal for a yes names Form 1040 line 31 because an unsupported Part II credit would reach it through Schedule 3 line 15; a yes is an answer that such a credit is claimed, and the supported net premium tax credit is listed in the question as one to leave out of the answer. The question was not changed in the fix round and was checked against Schedule 3 in Stage 19. Restatement accepted.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: The cited lines 1b to 1d and 1f to 1h match Form 1040's household wages, unreported tips, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income, leaving line 1e for separately handled dependent care benefits. The nonresident and passive-activity items only narrow scope through the refusal, and nothing in the text contradicts them.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: The Form 8615 conditions match page 36: over $2,700 of unearned income, required to file, no joint return, a parent alive at the end of 2025, and the same three age and support tests, with 'at least age 19 but under age 24' restated as 19 to 23. Forms 8814 and 4972 appear at Form 1040 line 16 and the Form 8978 amount fits page 36; the remaining items only widen the refusal screen, and nothing in the text contradicts them.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This helper corresponds to no IRS line and is simply true when no refusal fires, with each refusal naming what it excludes. The married filing separately gate matches the Form 1040 filing status box, and page 14 supports the stated limits on a spouse who itemizes and on credits a separate return cannot take.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "Schedule 1 and its instructions are not in the pages given, so the carved-out items and the references to lines 8s, 12, 14 and 23 cannot be checked. The given text confirms only that Form 1040 lines 8 and 10 draw from Schedule 1 and describes the clergy categories, so the Schedule 1 line list and instructions are what is missing."
  - key: "credits"
    status: UNCLEAR
    reason: "Schedule 3 and its instructions are missing, so the claims about Schedule 3 Part I and line 9 cannot be checked, and page 36 only points to Schedule 3 line 6l for a negative Form 8978 line 14 amount. Form 1040 lines 19, 27a, 28 and 29 fit the supported credits, and the refusal keeps the line 30 adoption credit out of scope, but its reference to all of line 31 cannot be reconciled with the supported Schedule 3 line 9 credit without Schedule 3."
  - key: "other_income"
    status: MATCH
    reason: "The cited lines 1b to 1d and 1f to 1h match Form 1040's household wages, unreported tips, Medicaid waiver payments, adoption benefits, Form 8919 wages and other earned income, leaving line 1e for separately handled dependent care benefits. The nonresident and passive-activity items only narrow scope through the refusal, and nothing in the text contradicts them."
  - key: "other_line16"
    status: MATCH
    reason: "The Form 8615 conditions match page 36: over $2,700 of unearned income, required to file, no joint return, a parent alive at the end of 2025, and the same three age and support tests, with 'at least age 19 but under age 24' restated as 19 to 23. Forms 8814 and 4972 appear at Form 1040 line 16 and the Form 8978 amount fits page 36; the remaining items only widen the refusal screen, and nothing in the text contradicts them."
  - key: "ready"
    status: MATCH
    reason: "This helper corresponds to no IRS line and is simply true when no refusal fires, with each refusal naming what it excludes. The married filing separately gate matches the Form 1040 filing status box, and page 14 supports the stated limits on a spouse who itemizes and on credits a separate return cannot take."
```
```
