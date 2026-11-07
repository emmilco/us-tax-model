# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-06); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5e735001c1608662a8cbbee87dd33ceb151e1cd9d0919b4eb053769866368d75 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f6cd527e2ad6b29f35be673c35a7f8fd5621c88f6e48db75ac01c4a4efb247cf |
| lines judged | 5 |
| match / mismatch / unclear / missing | 1 / 2 / 2 / 0 |
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
Status: **MISMATCH**

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately, including any of the following?

Income:
- statutory-employee wages or income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner
- church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
- a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund, for example:
  - a refund of general sales tax, real estate tax or personal property tax
  - a refund of mortgage interest in box 4 of Form 1098
  - a reimbursement of medical expenses
  - a payment on a bad debt you deducted
- sales of business property (Form 4797)
- a net operating loss deduction
- rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1)
- rental of personal property
- farm income (Schedule F)
- an exclusion of Medicaid waiver payments (Schedule 1 line 8s)

Adjustments:
- other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan)
- an adjustment on Schedule 1 line 12, 14 or 23

The ones this tool asks about separately:
- business income or loss from Schedule C
- a taxable state or local income tax refund
- alimony under an agreement made before 2019
- unemployment compensation
- the line 8 items asked one by one
- educator expenses
- the HSA deduction
- the deductible part of self-employment tax
- self-employed SEP and SIMPLE contributions
- the self-employed health insurance deduction
- the penalty on early withdrawal of savings
- the IRA deduction
- student loan interest
- jury duty pay you gave your employer

Schedule 1-A deductions are asked separately.

Model: The restatement lists statutory-employee, minister, and church-employee income as Schedule 1 items, but the IRS text directs statutory employee social security wages and tips to Schedule SE line 8a ("be sure to include on line 8a statutory employee social security wages and tips from Form W-2") and minister/church-employee income to Schedule SE lines 2/5a, not Schedule 1.

Ruling: model error; i1040sse p. 1. The question lists statutory-employee wages, income as a minister and church employee income so that a filer with them answers Yes and is refused; it does not say their amounts are entered on Schedule 1 (statutory employee income goes on Schedule C, whose net profit Schedule 1 line 3 carries, and clergy and church employee income bring Schedule SE, whose deduction is Schedule 1 line 15). The words are the prior wording's; the prior ruling on these items stands. Project stands.
Reviewed in: pass 14fc9dfc3bd1

### credits — Do you want to claim any credit other than the following, or do you have any other amount
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the following, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

- the foreign tax credit claimed without Form 1116
- the excess social security credit
- the child tax credit
- the credit for other dependents
- the additional child tax credit
- the earned income credit
- the credit for child and dependent care expenses (Form 2441)
- the retirement savings contributions credit (Form 8880)
- the residential energy credits (Form 5695)
- the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9)
- the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits)

Model: The provided IRS text does not include the Schedule 3 or credit instructions for most listed credits (foreign tax, excess Social Security, child tax, etc.), so the completeness of the 'other than' list cannot be verified.

Ruling: interface gap; f1040s3 p. 1 (Part I lines 1 to 8, line 3 from Form 8863; Part II line 9, Form 8962). The pages given lack Schedule 3 and the listed credits' instructions: a coverage gap of the review. As the prior ruling; the list is the prior wording's, item for item. Project stands.
Reviewed in: pass 14fc9dfc3bd1

### other_income — Any nonresident alien status, or other income or return treatment outside the kinds listed
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status, or other income or return treatment outside the kinds listed below?

Kinds this question is not about:
- wages
- interest
- dividends
- supported securities sales
- Form 1099-R distributions
- social security benefits

Nonresident alien status:
- you or your spouse, for any part of 2025

Other income or return treatment, including:
- wages or tips not on a Form W-2
- Medicaid waiver payments (whether or not in Form W-2 box 1)
- adoption benefits
- dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan)
- other earned income (Form 1040 lines 1b to 1d and 1f to 1h)
- income or loss from a passive activity (including gain on selling an interest in one)
- the 2025 part of a qualified disaster recovery distribution you received in 2023 or 2024, or a 2025 repayment of one (Form 8915-F)
- a repayment to an IRA of a qualified reservist distribution (Form 8606 line 1)

Model: The text supports the Form 8915-F disaster-distribution and Form 8606 qualified-reservist repayment items, but it does not cover the nonresident-alien status screen or most other listed income/return treatments, so the full restatement cannot be judged.

Ruling: interface gap; the pages given (f1040 pp. 1 and 2, i1040gi pp. 14, 36 and 43, p575 p. 35, i8606 p. 9) do not hold the nonresident alien rules or most of the listed income items, so the model could not judge them: a coverage gap of the review. Every clause of the prior wording, which this family judged MATCH, is kept (word check: no word lost; the six supported kinds are now a list headed as the kinds the question is not about). Project stands.
Reviewed in: pass 14fc9dfc3bd1

### other_line16 — Any additional Form 1040 line 16 tax or filing, including any of the following?
Status: **MISMATCH**

Restated: Input — Any additional Form 1040 line 16 tax or filing, including any of the following?

A child's unearned income:
- filing Form 8814 (even with no tax)
- Form 8615, required if all of these apply:
  - you had more than $2,700 of unearned income
  - you are required to file
  - you do not file jointly
  - you have a parent who was alive at the end of 2025
  - you were under 18 at the end of 2025, or 18 with earned income of not more than half your support, or a full-time student 19 to 23 with earned income of not more than half your support

Foreign corporations:
- a section 962 election
- Form 8621
- stock you own, directly or indirectly, in a controlled foreign corporation (CFC) or a passive foreign investment company (PFIC), even with nothing to include in income for 2025 (its distributions, dispositions and related adjustments can make the modified AGI of Form 8960 line 13 differ from AGI)

Other:
- Form 4972
- a Form 8978 amount
- recapture of an education credit
- income averaging of farming or fishing income on Schedule J (if you choose it)

Model: The restatement treats CFC/PFIC stock ownership as an additional Form 1040 line 16 tax/filing, but IRS i8960 says CFC/PFIC ownership may require MAGI adjustments on Form 8960 line 13: "If you own, directly or indirectly, stock in a CFC or PFIC ... to calculate your MAGI, you may need to make certain adjustments to your AGI" and "enter your AGI ... on line 13 of Form 8960."

Ruling: model error; i8960 p. 22: "If you exclude amounts under section 911 or own certain CFCs or PFICs, your MAGI is your AGI as modified by certain rules". As the prior ruling: CFC/PFIC ownership is in this refusal screen deliberately, with its reason stated, and the over-refusal of an owner with no NIIT was accepted. No amount is computed from the question. Project stands.
Reviewed in: pass 14fc9dfc3bd1

### ready — All declared scope screens passed
Status: **MATCH**

Model: The refusals name the excluded forms/statuses and the MFS gate matches f1040's 'Married filing separately' filing-status line; within the stated scope the helper is true when no screen triggers.
Reviewed in: pass 14fc9dfc3bd1

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| schedule1 | 177e07f9f761177d8d0d74d5818250a1c77e73f8404f01e9518ee809eba51a79 |
| credits | a2d9bcde875f8e0e3d4e7f8168c8af403162435e40d07d93d7049483ce2820e9 |
| other_income | 4215927dad7e61c1fa8e6d761035d1cd44533e7a65f34742a890462f2bc8cc95 |
| other_line16 | 96db9fa19806453b282fdcc893a7acdde1e978926828bcf82d896542ee4d7f89 |
| ready | 4845f0664f62dfdf1869a2dc192ec117e9941384cf0a2a71c04bb65360f317ac |
| (rest of the document) | 9a25da53ed2fbd2a45701244528c1eac2209891e67bfcf91f6753aa6e83ec08d |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 14fc9dfc3bd1

| field | value |
| --- | --- |
| date | 2026-11-06 |
| review scope | lines schedule1, credits, other_income, other_line16, ready |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 14fc9dfc3bd12eb3c81675b4cf89b3e79580ecfb7a8d1960cb24ee15c5a803b4 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | c22da569405ab86f393956d521b30522322aa02ca930b255d665ff8785e797b9 |
| receipt | .transcription/scope.deepseek.render.lines-3f42ec2e2ecc |
| lines judged | 5 |
| match / mismatch / unclear / missing | 1 / 2 / 2 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| p575 | None | 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| i8606 | 2025 | 9 | pages named by another document's citation | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 9 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| i8960 | 2025; printed date 2026-02-04 | 22 | pages named by another document's citation | fcae098ebc1ad79343de101a66765d3b3597f664dc744de3a7588be123c900a1 | - | d6dc1f475c511790abb02d6d6cfff554a59b40c0da1c56eb2f26af4e3cb7fa51 |

##### Raw response

```yaml
lines:
  - key: "schedule1"
    status: MISMATCH
    reason: "The restatement lists statutory-employee, minister, and church-employee income as Schedule 1 items, but the IRS text directs statutory employee social security wages and tips to Schedule SE line 8a (\"be sure to include on line 8a statutory employee social security wages and tips from Form W-2\") and minister/church-employee income to Schedule SE lines 2/5a, not Schedule 1."
  - key: "credits"
    status: UNCLEAR
    reason: "The provided IRS text does not include the Schedule 3 or credit instructions for most listed credits (foreign tax, excess Social Security, child tax, etc.), so the completeness of the 'other than' list cannot be verified."
  - key: "other_income"
    status: UNCLEAR
    reason: "The text supports the Form 8915-F disaster-distribution and Form 8606 qualified-reservist repayment items, but it does not cover the nonresident-alien status screen or most other listed income/return treatments, so the full restatement cannot be judged."
  - key: "other_line16"
    status: MISMATCH
    reason: "The restatement treats CFC/PFIC stock ownership as an additional Form 1040 line 16 tax/filing, but IRS i8960 says CFC/PFIC ownership may require MAGI adjustments on Form 8960 line 13: \"If you own, directly or indirectly, stock in a CFC or PFIC ... to calculate your MAGI, you may need to make certain adjustments to your AGI\" and \"enter your AGI ... on line 13 of Form 8960.\""
  - key: "ready"
    status: MATCH
    reason: "The refusals name the excluded forms/statuses and the MFS gate matches f1040's 'Married filing separately' filing-status line; within the stated scope the helper is true when no screen triggers."
```

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
