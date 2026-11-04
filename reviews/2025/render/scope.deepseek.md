# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5e735001c1608662a8cbbee87dd33ceb151e1cd9d0919b4eb053769866368d75 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f6cd527e2ad6b29f35be673c35a7f8fd5621c88f6e48db75ac01c4a4efb247cf |
| lines judged | 5 |
| match / mismatch / unclear / missing | 0 / 0 / 5 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p575 | None | 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **UNCLEAR**

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner; church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)

Model: The IRS text only references Form 1040 lines 8 and 10 as coming from Schedule 1; it does not include Schedule 1 line 10/26 or the listed income and adjustment items, so the restatement cannot be verified.

Ruling: interface gap; The reviewer says the pages given cite only Form 1040 lines 8 and 10 from Schedule 1, so it cannot verify the listed items; the deciding text (Schedule 1 and its instructions) is not among the pages: a coverage gap of the review. The prior scope ruling on the listed clergy, church and statutory-employee items stands (i1040sse p. 1; the question names them, so the filer answers Yes and is refused). Project stands.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695), the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9) and the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The IRS text does not include Schedule 3 Part I or the instructions for the listed credits (Form 2441, Form 8880, Form 5695, Form 8962, Form 8863, etc.), so the scope question cannot be compared.

Ruling: interface gap; f1040s3 p. 1 (Part I lines 1 to 8, line 3 from Form 8863; Part II line 9, Form 8962). The pages given lack Schedule 3 and the listed credits' instructions: a coverage gap of the review. As the prior ruling. Project stands.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), adoption benefits, dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan), other earned income (Form 1040 lines 1b to 1d and 1f to 1h), income or loss from a passive activity (including gain on selling an interest in one), or the 2025 part of a qualified disaster recovery distribution you received in 2023 or 2024, or a 2025 repayment of one (Form 8915-F)?

Model: The IRS text gives only Form 1040 lines 1b–1h and a P575 excerpt on qualified disaster distributions; it does not cover most listed items such as passive activity, adoption benefits, dependent care benefits, or the full Form 8915-F treatment.

Ruling: interface gap; f1040 (2025) lines 1b to 1h; p575 p. 35, "you can include $6,000 in your income in 2023, 2024, and 2025". The pages given cover Form 1040 and the p575 disaster-distribution excerpt only; the other listed items are not decided there: a coverage gap. Checked the refresh change (BUG-0393): the clause names the 2025 part of a qualified disaster recovery distribution received in 2023 or 2024, or a 2025 repayment (Form 8915-F); a 2025 distribution is refused at retirement.special, so the narrowing to 2023 and 2024 leaves no case unscreened. No error introduced. Project stands.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **UNCLEAR**

Restated: Input — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615 (required if you had more than $2,700 of unearned income, are required to file, do not file jointly, have a parent who was alive at the end of 2025, and were under 18 at the end of 2025, or 18 with earned income of not more than half your support, or a full-time student 19 to 23 with earned income of not more than half your support), a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?

Model: The Form 8615 conditions on page 36 largely match, but the IRS text does not cover the other listed line 16 items (Form 8814, Form 4972, section 962, Form 8621, Form 8978, or education credit recapture), so the full restatement cannot be verified.

Ruling: interface gap; f1040 (2025) line 16. The reviewer confirms the Form 8615 conditions; the pages given lack the other listed items (Form 8814, Form 4972, section 962, Form 8621, Form 8978, education credit recapture): a coverage gap. As the prior ruling. Project stands.

### ready — All declared scope screens passed
Status: **UNCLEAR**

Restated: true = true

Model: No IRS line corresponds to the program's 'all declared scope screens passed' helper; the MFS refusal is a support gate, and the IRS text does not define the helper or the 'Social Security base' reference.

Ruling: interface gap; The MFS refusal matches i1040gi p. 14, Married Filing Separately; the other screens are filer-answered declarations whose items are cited on the lines that read them, and the pages given lack the deciding text. As the prior ruling. Project stands.

## Raw response

```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "The IRS text only references Form 1040 lines 8 and 10 as coming from Schedule 1; it does not include Schedule 1 line 10/26 or the listed income and adjustment items, so the restatement cannot be verified."
  - key: "credits"
    status: UNCLEAR
    reason: "The IRS text does not include Schedule 3 Part I or the instructions for the listed credits (Form 2441, Form 8880, Form 5695, Form 8962, Form 8863, etc.), so the scope question cannot be compared."
  - key: "other_income"
    status: UNCLEAR
    reason: "The IRS text gives only Form 1040 lines 1b–1h and a P575 excerpt on qualified disaster distributions; it does not cover most listed items such as passive activity, adoption benefits, dependent care benefits, or the full Form 8915-F treatment."
  - key: "other_line16"
    status: UNCLEAR
    reason: "The Form 8615 conditions on page 36 largely match, but the IRS text does not cover the other listed line 16 items (Form 8814, Form 4972, section 962, Form 8621, Form 8978, or education credit recapture), so the full restatement cannot be verified."
  - key: "ready"
    status: UNCLEAR
    reason: "No IRS line corresponds to the program's 'all declared scope screens passed' helper; the MFS refusal is a support gate, and the IRS text does not define the helper or the 'Social Security base' reference."
```
