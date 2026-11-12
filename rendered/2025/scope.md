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
  - you or your spouse being a debtor in a chapter 11 bankruptcy case open at any time in 2025, even if your only income is wages, interest or dividends
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
  - you or your spouse being a debtor in a chapter 11 bankruptcy case open at any time in 2025, even if your only income is wages, interest or dividends
- Expr: `{"op":"input","source":"Any nonresident alien status, or other income or return treatment outside the kinds listed below?\n\nKinds this question is not about:\n- wages\n- interest\n- dividends\n- supported securities sales\n- Form 1099-R distributions\n- social security benefits\n\nNonresident alien status:\n- you or your spouse, for any part of 2025\n\nOther income or return treatment, including:\n- wages or tips not on a Form W-2\n- Medicaid waiver payments (whether or not in Form W-2 box 1)\n- adoption benefits\n- dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan)\n- other earned income (Form 1040 lines 1b to 1d and 1f to 1h)\n- income or loss from a passive activity (including gain on selling an interest in one)\n- the 2025 part of a qualified disaster recovery distribution you received in 2023 or 2024, or a 2025 repayment of one (Form 8915-F)\n- a repayment to an IRA of a qualified reservist distribution (Form 8606 line 1)\n- you or your spouse being a debtor in a chapter 11 bankruptcy case open at any time in 2025, even if your only income is wages, interest or dividends"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; p575 p. 35, "if you received a $18,000 qualified disaster recovery distribution in 2023, you can include $6,000 in your income in 2023, 2024, and 2025"; i8606 p. 9, Line 1, "Include on line 1 any repayment of a qualified reservist distribution."; i1040gi p. 23, Chapter 11 Bankruptcy Cases, "If you are a debtor in a chapter 11 bankruptcy case, income taxable to the bankruptcy estate and reported on the estate’s income tax return includes:" and "Because this income is taxable to the estate, don’t include this income on your own individual income tax return." (2025; created 2025-09-05; sha256 3d31c226)

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
- **Refusal:** when scope.other_income is true, cannot complete Form 1040 additional income/return forms. Prepare the required unsupported income or return treatment. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when scope.other_line16 is true, cannot complete Form 1040 line 16 additional tax forms. Prepare the applicable additional tax or alternative worksheet. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- **Refusal:** when s3.mfs is true, cannot complete Married filing separately. The rules for a married filing separately return (among them a spouse who itemizes, the Social Security base for spouses who lived together and the credits a separate return cannot take) are outside this tool. Married filing jointly is supported. Cite: [i1040gi] p. 14, Married Filing Separately (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.adoption_if_any is true, cannot complete Form 8839 (adoption credit). An adoption that became final in 2025, or adoption costs paid in 2025, can give the adoption credit (Form 8839, with its refundable part on Form 1040 line 30), which this tool does not prepare. Cite: [i8839] p. 1, Purpose of Form, "You may be able to take this credit in 2025 if any of the following statements are true" (2025; sha256 90dd5f4d)
- **Refusal:** when s3.adoption_us_if_earlier is true, cannot complete Form 8839 (adoption credit). Costs paid in 2024 toward adopting a U.S. child, where the adoption was not final at the end of 2024, are credited on the 2025 return (Form 8839), which this tool does not prepare. Cite: [i8839] p. 1, Purpose of Form, "2024 and the adoption wasn’t final at the end of 2024"; p. 3, Domestic Adoption, "the year after the year of the payment" (2025; sha256 90dd5f4d)
- **Refusal:** when s3.credit_bond is true, cannot complete Form 8912 (credit to holders of tax credit bonds). A tax credit from a bond, or one a fund passes on (Form 1097-BTC), is claimed on Form 8912, which this tool does not prepare. Cite: [i8912] p. 1, Who Can Claim the Credits, "can claim the credit by filing Form 8912 for each tax year in which it holds the bond on a credit allowance date"; p. 2, Line 1, "This amount is the total bond credits reported to you on Form(s) 1097-BTC" (December 2024 (continuous-use revision, the current one on irs.gov/pub/irs-pdf when fetched, so in force for 2025); sha256 8d4a48b7)
- **Refusal:** when s3.elderly_credit_if_asked is true, cannot complete Schedule R (credit for the elderly or the disabled). The credit for the elderly or the disabled (Schedule R) is outside this tool. To go on without the credit, answer No to that question. Cite: [i1040sr] p. 1, Qualified Individual, "You are a qualified individual for this credit if you are a U.S. citizen or resident alien" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 7194fa66)
- **Refusal:** when s3.ev_dealer_if_ev is true, cannot complete Form 8936 (clean vehicle credits). A dealer took the clean vehicle credit off the price, so Form 8936 and its Schedule A must be filed with this return; this tool does not prepare them. Cite: [i8936] p. 1, Purpose of Form, "You must file Form 8936 and Schedule A (Form 8936) if you purchased a new or used clean vehicle from a registered dealer and reduced the amount you paid at the time of sale by transferring the credit to the dealer" (2025; sha256 49aa7277)
- **Refusal:** when s3.ev_credit_if_bought is true, cannot complete Form 8936 (clean vehicle credits). This tool does not prepare the clean vehicle credits (Form 8936). To go on without the credit, answer No to that question. Cite: [i8936] p. 1, Purpose of Form, "to figure the following credits for clean vehicles you placed in service during your tax year" (2025; sha256 49aa7277)
- **Refusal:** when s3.ev_equipment_if_ev is true, cannot complete Form 8911 (alternative fuel vehicle refueling property credit). This tool does not prepare the credit for vehicle charging or fueling equipment (Form 8911). To go on without the credit, answer No to that question. Cite: [i8911] p. 1, Purpose of Form, "to figure your credit for alternative fuel vehicle refueling property you placed in service during your tax year" (December 2025 (for tax years beginning in 2025 or later); sha256 a85de224)
- **Refusal:** when s3.farmland_deferral_if_sold is true, cannot complete Form 1062 (Schedule 3 line 13z). The election to pay the tax on a sale of farmland in installments (Form 1062) is reported on Schedule 3 line 13z, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13z, "Use line 13z to report the credit under section 960(c) with respect to an excess limitation account", "Also use line 13z to report the amount of U.S. tax allocable to the U.S. Virgin Islands" and "If you made the election to defer net income tax attributable to the gain on the sale or exchange of qualified farmland property" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ftc.carryover_if_asked is true, cannot complete Form 1116. A foreign tax credit carried from another year is claimed on Form 1116, which this tool does not prepare. Cite: [i1116] p. 19, Line 10, "Enter the unused foreign taxes in the separate category from another tax year that are eligible to be carried forward to or back to 2025" (2025; printed date 2025-12-23; sha256 6998cf8c)
- **Refusal:** when s3.section960c_if_foreign is true, cannot complete Schedule 3 line 13z (section 960(c) credit). The credit under section 960(c) is reported on Schedule 3 line 13z, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13z, "Use line 13z to report the credit under section 960(c) with respect to an excess limitation account", "Also use line 13z to report the amount of U.S. tax allocable to the U.S. Virgin Islands" and "If you made the election to defer net income tax attributable to the gain on the sale or exchange of qualified farmland property" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.section965_if_foreign is true, cannot complete Schedule 3 line 13d (net 965 tax liability). A net 965 tax liability paid in installments is reported on Schedule 3 line 13d, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13d, "If you elected to pay your net 965 tax liability in installments, report the deferred amount on line 13d" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.virgin_islands_if_foreign is true, cannot complete Form 8689 (Schedule 3 line 13z). Tax allocable to the U.S. Virgin Islands (Form 8689) is reported on Schedule 3 line 13z, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13z, "Use line 13z to report the credit under section 960(c) with respect to an excess limitation account", "Also use line 13z to report the amount of U.S. tax allocable to the U.S. Virgin Islands" and "If you made the election to defer net income tax attributable to the gain on the sale or exchange of qualified farmland property" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.kerosene_credit_if_kerosene is true, cannot complete Form 4136 (credit for federal tax paid on fuels). This tool does not prepare the credit for federal tax paid on fuels (Form 4136). To go on without the credit, answer No to that question. Cite: [i4136] p. 2, Part I—Information About Your Business, "If you are claiming a credit for the tax on undyed kerosene you purchased (other than from a blocked pump) and used in your home during the tax period for heating, lighting, or cooking" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 d3d63fc3)
- **Refusal:** when s3.prior_amt_if_forms is true, cannot complete Form 8801 (credit for prior year minimum tax). Alternative minimum tax on your 2024 return can give a credit for 2025 (Form 8801), which this tool does not prepare. Cite: [i8801] p. 1, Who Should File, "An AMT liability and adjustments or preferences other than exclusion items" (2025; sha256 cf99d034)
- **Refusal:** when s3.prior_forms_if_forms is true, cannot complete Credit carried from an earlier year (Form 3800, 8396, 8801, 8834, 8839, 8859 or 8912). A credit carried over from an earlier year is outside this tool. Cite: [i3800] p. 3, Carryback and Carryforward of Unused Credit, "unused general business credits may be carried back 1 year and carried forward 20 years"; f8396 p. 2, Part II—Mortgage Interest Credit Carryforward to 2026, "you may have an unused credit to carry forward to the next 3 tax years"; i8801 p. 1, Who Should File, "A credit carryforward to 2025 (on 2024 Form 8801, line 26)"; f8834 p. 2, Line 1, "Enter the qualified electric vehicle passive activity credits allowed for your current tax year from Form 8582-CR"; i8839 p. 1, Purpose of Form, "You have a carryforward of an adoption credit from 2024"; f8859 p. 1, Purpose of Form, "to claim a carryforward of the District of Columbia first-time homebuyer credit from 2024"; i8912 p. 3, Line 12, "you may carry the unused portion of the credit to the next tax year" (2025; sha256 97e4570d)
- **Refusal:** when s3.repaid_income is true, cannot complete Repayment of income of an earlier year (Schedule 3 line 13b or Schedule A line 16). A repayment of more than $3,000 of income reported in an earlier year gives a choice between a deduction and a credit (Schedule 3 line 13b), which this tool does not figure. Cite: [p525] p. 36, Repayments, "If the amount you repaid was more than $3,000, you can deduct the repayment as an other itemized deduction on Schedule A (Form 1040), line 16, if you included the income under a claim of right" and "However, you can choose to take a credit for the year of repayment"; i1040gi p. 117, Line 13b, "If you are claiming a credit for repayment of amounts you included in your income in an earlier year because it appeared you had a right to the income" (2025; sha256 39b0fa5e)
- **Refusal:** when s3.mcc_if_interest is true, cannot complete Form 8396 (mortgage interest credit). A mortgage credit certificate gives the mortgage interest credit (Form 8396), which also reduces the home mortgage interest deducted on Schedule A; this tool does not prepare it. Cite: [f8396] p. 2, Who Can Claim the Credit, "You can claim the credit only if you were issued a qualified Mortgage Credit Certificate (MCC) by a state or local governmental unit or agency"; p. 2, Line 3, "you must reduce the amount of home mortgage interest you would otherwise deduct on Schedule A by the amount on Form 8396, line 3" (2025; created 2025-08-28; sha256 5c035af7)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)
