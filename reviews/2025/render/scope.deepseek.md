# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 46afc7c5c5dd556cbb0a410bb953944f3adf0e75a9e06908ba4df3ad6235bcb4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a6f16dd3f7d2c8979e080362c9f88caf03b68f5c1cc069f454bf92eeb17b6dbb |
| lines judged | 5 |
| match / mismatch / unclear / missing | 0 / 0 / 5 / 0 |
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

Model: The IRS text provided does not include Schedule 1 or its instructions, so the list of Schedule 1 income and adjustment items and the lines 12, 14, and 23 references cannot be verified.

Ruling: open

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695) and the net premium tax credit you enter from Form 8962 (Schedule 3 line 9), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The IRS text provided does not include Schedule 3 Part I or the credit instructions, so the Schedule 3 line references and the list of excluded credits cannot be verified.

Ruling: open

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), adoption benefits, dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan), other earned income (Form 1040 lines 1b to 1d and 1f to 1h), or income or loss from a passive activity (including gain on selling an interest in one)?

Model: The IRS text provided does not define the supported categories or the passive-activity and nonresident-alien return-treatment items, so the scope screen cannot be fully judged from the given text.

Ruling: open

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **UNCLEAR**

Restated: Input — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?

Model: Form 1040 line 16 shows only checkboxes for Forms 8814 and 4972 plus a blank; the provided text does not include the line 16 instructions needed to verify the additional forms and education-credit recapture.

Ruling: open

### ready — All declared scope screens passed
Status: **UNCLEAR**

Restated: true = true

Model: This is a program scope gate rather than an IRS form line, and the provided text does not define the declared scope screens or the other gate conditions used by the helper.

Ruling: open

## Raw response

```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "The IRS text provided does not include Schedule 1 or its instructions, so the list of Schedule 1 income and adjustment items and the lines 12, 14, and 23 references cannot be verified."
  - key: "credits"
    status: UNCLEAR
    reason: "The IRS text provided does not include Schedule 3 Part I or the credit instructions, so the Schedule 3 line references and the list of excluded credits cannot be verified."
  - key: "other_income"
    status: UNCLEAR
    reason: "The IRS text provided does not define the supported categories or the passive-activity and nonresident-alien return-treatment items, so the scope screen cannot be fully judged from the given text."
  - key: "other_line16"
    status: UNCLEAR
    reason: "Form 1040 line 16 shows only checkboxes for Forms 8814 and 4972 plus a blank; the provided text does not include the line 16 instructions needed to verify the additional forms and education-credit recapture."
  - key: "ready"
    status: UNCLEAR
    reason: "This is a program scope gate rather than an IRS form line, and the provided text does not define the declared scope screens or the other gate conditions used by the helper."
```
