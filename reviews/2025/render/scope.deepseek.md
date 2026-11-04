# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b72cbe9671315aa9ccfcaecb5ff3037a401bd380df19fd10eb8975655bb4ef09 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | c0c4f10962168d8e302931bd58e6a8d0aa229a203ae2aa516501c95e6a37af96 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 0 / 1 / 4 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **MISMATCH**

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner; church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)

Model: The restatement treats statutory-employee, minister, and church-employee income as Schedule 1 items, but the IRS text assigns them to Schedule SE: 'If you must pay SE tax, include this income on Schedule SE, line 2' and 'include on line 8a statutory employee social security wages and tips from Form W-2'.

Ruling: scope; i1040sse p. 1, Employees of Churches and Church Organizations; i1040gi p. 43, Clergy. The objection is that statutory-employee, clergy and church-employee income go to Schedule SE rather than Schedule 1. The question lists them expressly ("including ..."), so a filer with any of them answers Yes and the return is refused; the tool supports self-employment tax only for Schedule C income (person.se_screen refuses the same items). Whether each item also reaches Schedule 1 does not change who is refused. The person-dep wording (PENDING-5: "a church or qualified church-controlled organization") matches i1040sse p. 1. render MISMATCH. Project stands.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695), the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9) and the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The provided text lacks Schedule 3 and the credit instructions needed to verify the foreign tax credit, excess Social Security credit, saver's credit, residential energy credits, and related supported-credit list.

Ruling: interface gap; f1040s3 p. 1 (Part I lines 1 to 8, line 9). The pages given (Form 1040, i1040gi pp. 14, 36, 43, i1040sse) omit Schedule 3 and the credit instructions; question unchanged and checked in earlier rounds against s3.line3 and s3.line9. render UNCLEAR. Project stands.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), adoption benefits, dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan), other earned income (Form 1040 lines 1b to 1d and 1f to 1h), or income or loss from a passive activity (including gain on selling an interest in one)?

Model: The text does not provide the instructions for passive activities, nonresident alien treatment, or the full line 1b–1h categories, so the scope Boolean cannot be fully judged.

Ruling: interface gap; f1040 lines 1b-1h; i1040gi p. 115. The defining instructions were not given; question unchanged. render UNCLEAR. Project stands.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **UNCLEAR**

Restated: Input — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615 (required if you had more than $2,700 of unearned income, are required to file, do not file jointly, have a parent who was alive at the end of 2025, and were under 18 at the end of 2025, or 18 with earned income of not more than half your support, or a full-time student 19 to 23 with earned income of not more than half your support), a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?

Model: The Form 8615 conditions match page 36, but the provided line 16 text does not cover the section 962 election, Form 8621, Form 8978 amount, or education-credit recapture, so the full Boolean cannot be judged.

Ruling: interface gap; f1040 line 16; i1040gi p. 36. The reviewer confirms the Form 8615 conditions on p. 36; the other listed forms' text was not given; question unchanged. render UNCLEAR. Project stands.

### ready — All declared scope screens passed
Status: **UNCLEAR**

Restated: true = true

Model: 'ready' is a program-internal gate with no corresponding IRS line; the provided text does not define an 'all declared scope screens passed' Boolean.

Ruling: interface gap; i1040gi p. 14. scope.ready is the whole-return readiness gate (the constant true carrying the scope refusals, each with its own cite), not an IRS line; the reviewer was not given text it could judge it against. render UNCLEAR. Project stands.

## Raw response

```yaml
lines:
  - key: "schedule1"
    status: MISMATCH
    reason: "The restatement treats statutory-employee, minister, and church-employee income as Schedule 1 items, but the IRS text assigns them to Schedule SE: 'If you must pay SE tax, include this income on Schedule SE, line 2' and 'include on line 8a statutory employee social security wages and tips from Form W-2'."
  - key: "credits"
    status: UNCLEAR
    reason: "The provided text lacks Schedule 3 and the credit instructions needed to verify the foreign tax credit, excess Social Security credit, saver's credit, residential energy credits, and related supported-credit list."
  - key: "other_income"
    status: UNCLEAR
    reason: "The text does not provide the instructions for passive activities, nonresident alien treatment, or the full line 1b–1h categories, so the scope Boolean cannot be fully judged."
  - key: "other_line16"
    status: UNCLEAR
    reason: "The Form 8615 conditions match page 36, but the provided line 16 text does not cover the section 962 election, Form 8621, Form 8978 amount, or education-credit recapture, so the full Boolean cannot be judged."
  - key: "ready"
    status: UNCLEAR
    reason: "'ready' is a program-internal gate with no corresponding IRS line; the provided text does not define an 'all declared scope screens passed' Boolean."
```
