# Proof-of-concept scope screening

- Document: `scope` (form, tax year 2025)
- Note: Stage 4 screening answers are explicit declarations, not automatic determinations of eligibility. Stage 5 wires these gates into the whole-return outcome.

## (helper) — `scope.schedule1`

- **Authored helper label:** Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately, including any of the following?

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
- **Encoded (Bool):** Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately, including any of the following?

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
- Expr: `{"op":"input","source":"Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately, including any of the following?\n\nIncome:\n- statutory-employee wages or income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner\n- church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)\n- a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund, for example:\n  - a refund of general sales tax, real estate tax or personal property tax\n  - a refund of mortgage interest in box 4 of Form 1098\n  - a reimbursement of medical expenses\n  - a payment on a bad debt you deducted\n- sales of business property (Form 4797)\n- a net operating loss deduction\n- rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1)\n- rental of personal property\n- farm income (Schedule F)\n- an exclusion of Medicaid waiver payments (Schedule 1 line 8s)\n\nAdjustments:\n- other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan)\n- an adjustment on Schedule 1 line 12, 14 or 23\n\nThe ones this tool asks about separately:\n- business income or loss from Schedule C\n- a taxable state or local income tax refund\n- alimony under an agreement made before 2019\n- unemployment compensation\n- the line 8 items asked one by one\n- educator expenses\n- the HSA deduction\n- the deductible part of self-employment tax\n- self-employed SEP and SIMPLE contributions\n- the self-employed health insurance deduction\n- the penalty on early withdrawal of savings\n- the IRA deduction\n- student loan interest\n- jury duty pay you gave your employer\n\nSchedule 1-A deductions are asked separately."}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; i1040gi p. 43, Clergy, "The following instructions apply to ministers, members of religious orders who have not taken a vow of poverty, and Christian Science practitioners."; i1040sse p. 1, Employees of Churches and Church Organizations, "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes." (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.credits`

- **Authored helper label:** Do you want to claim any credit other than the following, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

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
- **Encoded (Bool):** Input — Do you want to claim any credit other than the following, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

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
- Expr: `{"op":"input","source":"Do you want to claim any credit other than the following, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?\n\n- the foreign tax credit claimed without Form 1116\n- the excess social security credit\n- the child tax credit\n- the credit for other dependents\n- the additional child tax credit\n- the earned income credit\n- the credit for child and dependent care expenses (Form 2441)\n- the retirement savings contributions credit (Form 8880)\n- the residential energy credits (Form 5695)\n- the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9)\n- the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits)"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.other_income`

- **Authored helper label:** Any nonresident alien status, or other income or return treatment outside the kinds listed below?

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
- **Encoded (Bool):** Input — Any nonresident alien status, or other income or return treatment outside the kinds listed below?

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
- Expr: `{"op":"input","source":"Any nonresident alien status, or other income or return treatment outside the kinds listed below?\n\nKinds this question is not about:\n- wages\n- interest\n- dividends\n- supported securities sales\n- Form 1099-R distributions\n- social security benefits\n\nNonresident alien status:\n- you or your spouse, for any part of 2025\n\nOther income or return treatment, including:\n- wages or tips not on a Form W-2\n- Medicaid waiver payments (whether or not in Form W-2 box 1)\n- adoption benefits\n- dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan)\n- other earned income (Form 1040 lines 1b to 1d and 1f to 1h)\n- income or loss from a passive activity (including gain on selling an interest in one)\n- the 2025 part of a qualified disaster recovery distribution you received in 2023 or 2024, or a 2025 repayment of one (Form 8915-F)\n- a repayment to an IRA of a qualified reservist distribution (Form 8606 line 1)"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; p575 p. 35, "if you received a $18,000 qualified disaster recovery distribution in 2023, you can include $6,000 in your income in 2023, 2024, and 2025"; i8606 p. 9, Line 1, "Include on line 1 any repayment of a qualified reservist distribution." (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.other_line16`

- **Authored helper label:** Any additional Form 1040 line 16 tax or filing, including any of the following?

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
- **Encoded (Bool):** Input — Any additional Form 1040 line 16 tax or filing, including any of the following?

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
- Expr: `{"op":"input","source":"Any additional Form 1040 line 16 tax or filing, including any of the following?\n\nA child's unearned income:\n- filing Form 8814 (even with no tax)\n- Form 8615, required if all of these apply:\n  - you had more than $2,700 of unearned income\n  - you are required to file\n  - you do not file jointly\n  - you have a parent who was alive at the end of 2025\n  - you were under 18 at the end of 2025, or 18 with earned income of not more than half your support, or a full-time student 19 to 23 with earned income of not more than half your support\n\nForeign corporations:\n- a section 962 election\n- Form 8621\n- stock you own, directly or indirectly, in a controlled foreign corporation (CFC) or a passive foreign investment company (PFIC), even with nothing to include in income for 2025 (its distributions, dispositions and related adjustments can make the modified AGI of Form 8960 line 13 differ from AGI)\n\nOther:\n- Form 4972\n- a Form 8978 amount\n- recapture of an education credit\n- income averaging of farming or fishing income on Schedule J (if you choose it)"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; i1040gi p. 36, "You must file Form 8615 if you meet all of the following conditions." and "If you had income from farming or fishing, your tax may be less if you choose to figure it using income averaging on Schedule J."; i8960 p. 22, Line 13—Modified Adjusted Gross Income (MAGI), "If you exclude amounts under section 911 or own certain CFCs or PFICs, your MAGI is your AGI as modified by certain rules described in Regulations section 1.1411-10(e)(1).", "Increase AGI by the amount of any distributions described in section 959(d) or 1293(c) included in your NII as a dividend." and "Increase AGI by the amount of any excess distributions derived from a PFIC that are dividends included in MAGI but not included in gross income for regular income tax purposes." (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready`

- **Authored helper label:** All declared scope screens passed
- **Encoded (Bool):** true = true
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1. Schedule 1 income and adjustments other than the ones this tool computes (Schedule C business income, a taxable state or local income tax refund, alimony under an agreement made before 2019, unemployment compensation, the supported line 8 items, educator expenses, the HSA deduction, the deductible part of self-employment tax, self-employed SEP and SIMPLE contributions, the self-employed health insurance deduction, the early withdrawal penalty, the IRA deduction, student loan interest and jury duty pay given to your employer) are outside this tool. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.credits is true, cannot complete Other credit forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31). Credits other than the foreign tax credit by election, the excess social security credit, the Schedule 8812 credits, the earned income credit, the child and dependent care credit, the saver's credit, the residential energy credits, the net premium tax credit figured on Form 8962 and the education credits (Form 8863) require forms outside this proof of concept. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_income is true, cannot complete Form 1040 additional income/return forms. Prepare the required unsupported income or return treatment. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_line16 is true, cannot complete Form 1040 line 16 additional tax forms. Prepare the applicable additional tax or alternative worksheet. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when s3.mfs is true, cannot complete Married filing separately. The rules for a married filing separately return (among them a spouse who itemizes, the Social Security base for spouses who lived together and the credits a separate return cannot take) are outside this tool. Married filing jointly is supported. Cite: [i1040gi] p. 14, Married Filing Separately (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)
