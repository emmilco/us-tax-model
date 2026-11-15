# Walk: ny05_investor_nyc

The investor of persona 06 (one job, interest, dividends and stock sales, a capital loss carried over), living in Manhattan all of 2025.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/ny05_investor_nyc.yaml` (extending `06_investor_loss_carryover`): the built interview (profile `ny`, the federal questions, then the New York ones, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

## The walk

### 1. `$person`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`)

> Who is this tax return for?

- Offered: “Just me” / “Me and my husband or wife, together on one return”
- Answer: “Just me” (persona)
- Words: prompt 6, help 51. Help begins: “Choose “together” if you are married and the two of you are filing one return, even if only one of you had income.”

### 2. `f1040.status`

**⟶ topic switch**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), Filing Status

> Which of these fits you on December 31, 2025?

- Offered: “Married, and filing apart from my husband or wife (married filing separately)” / “Widowed in 2023 or 2024, not remarried, and my child lived with me all of 2025 (qualifying surviving spouse)” / “I paid over half the cost of the home of my child, or of a relative I support (head of household)” / “None of these: I was not married (single)”
- Answer: “None of these: I was not married (single)” (`single`) (persona)
- Words: prompt 9, help 115. Help begins: “Take the first line that is true for you, with one exception: if you are married but lived apart from your husband or wife for the last six months of 2025 and your child lived with you, look at the line about paying for a home before the first line.”

### 3. `household.ever_married`

**⟶ topic switch**

Topic: Household facts for dependents and head of household (`household`)

> Have you ever been married?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 5, help 21. Help begins: “Count a marriage that has ended, and a common-law marriage.”

### 4. `household.community_property`

Topic: Household facts for dependents and head of household (`household`)

> At any time in 2025, did you live in Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 20, help 31. Help begins: “In these nine states a married couple's income belongs to both of them by law (community property), which matters for a married person or registered partner who does not file jointly.”

### 5. `person[taxpayer].birth_year`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> In what year were you born?

- Offered: a whole number
- Answer: 1980 (persona)
- Words: prompt 6, help 0

### 6. `sa.dependent`

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Can a parent or anyone else claim you as a dependent on their 2025 return?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 15, help 36. Help begins: “It is whether they can, not whether they do.”

### 7. `person[taxpayer].blind`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Were you blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 41. Help begins: “The statement must say that your better eye sees no better than 20/200 with glasses or contact lenses, or that your field of vision is 20 degrees or less, or that your sight is not likely to improve beyond those limits.”

### 8–12. Tick-boxes `about_you`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Schedule A — supported itemized deductions and standard comparison (`sa`)

> Is any of these true of you?
>
> - [ ] Not a U.S. citizen at some time in 2025  (`scope.noncitizen`)
> - [ ] Under 24 at the end of 2025  (`scope.under24`)
> - [ ] In the U.S. armed forces, reserves or National Guard since January 2022  (`scope.armed_forces`)
> - [ ] Leaving out income earned abroad, in Puerto Rico or in American Samoa  (`sa.excluded_income`)
> - [ ] In a chapter 11 bankruptcy case at some time in 2025  (`scope.chapter11`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 51. Behind each box, optional to read: the question's own prompt (11, 9, 19, 26, 13 words) and help (0, 0, 0, 36, 25)

### 13. `s3.disability_retired`

**⟶ topic switch**

Topic: Schedule 3 — selected lines (`s3`)

> Have you retired on permanent and total disability?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 8, help 23. Help begins: “Yes if a person under 65 had to stop working because of a condition a doctor expects to last at least a year.”

### 14. `$dependent`

**⟶ topic switch**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`)

> In 2025, did children live with you, or did you support anyone else, such as a parent, another relative or a partner? List each one, or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 30, help 42. Help begins: “Any label you will recognize will do, such as “Child 1”; a name is not needed.”

### 15–16. Tick-boxes `child_extras`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`); Proof-of-concept scope screening (`scope`)

> Does either of these apply to you?
>
> - [ ] Adopted a child, or paid adoption costs, since the start of 2024  (`s3.adoption_any`)
> - [ ] Reporting a child's 2025 interest or dividends on your own return  (`scope.f8814`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 23. Behind each box, optional to read: the question's own prompt (16, 21 words) and help (18, 28)

### 17–19. Tick-boxes `own_income`: 3 questions on one screen

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you have any of these?
>
> - [ ] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [ ] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 29. Behind each box, optional to read: the question's own prompt (27, 27, 11 words) and help (6, 6, 25)

### 20–21. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did either of these describe your work in 2025?
>
> - [ ] Worked for a railroad  (`person[taxpayer].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[taxpayer].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 15. Behind each box, optional to read: the question's own prompt (8, 30 words) and help (27, 0)

### 22. `$w2@person[taxpayer]`

**⟶ topic switch**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: You

> Which employers gave you a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: the list `software_co` (persona)
- Words: prompt 8, help 32. Help begins: “Name each employer once.”

### 23. `person[taxpayer].w2[software_co].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 software_co

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $118,000.00 (persona)
- Words: prompt 6, help 0

### 24. `person[taxpayer].w2[software_co].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 software_co

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $18,900.00 (persona)
- Words: prompt 6, help 0

### 25. `person[taxpayer].w2[software_co].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 software_co

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $7,316.00 (persona)
- Words: prompt 6, help 0

### 26. `person[taxpayer].w2[software_co].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 software_co

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $118,000.00 (persona)
- Words: prompt 6, help 0

### 27. `person[taxpayer].w2[software_co].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 software_co

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $1,711.00 (persona)
- Words: prompt 5, help 0

### 28–32. Tick-boxes `w2_jobs`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`); Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Do your W-2s, or the jobs on them, show any of these?
>
> - [ ] An amount in box 8, or box 12 code A/B/K/M/N/Z  (`s2.w2_marks`)
> - [ ] In box 11, money paid to you from a deferred pay plan  (`s1.nqdc_pension`)
> - [ ] Box 12 code H, or box 13 “Statutory employee” ticked  (`scope.w2_marks`)
> - [ ] Work as a performing artist, or as an official paid from fees  (`scope.artist_official`)
> - [ ] More pay put into retirement plans at work than the yearly limit  (`scope.excess_deferral`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 12, labels 56. Behind each box, optional to read: the question's own prompt (25, 17, 22, 22, 22 words) and help (27, 18, 6, 0, 34)

### 33–37. Tick-boxes `other_pay`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Form 8959 — Additional Medicare Tax on wages and self-employment income (`f8959`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you have any of these kinds of work or pay?
>
> - [ ] Wages, tips or strike benefits that are not on a W-2  (`scope.pay_no_w2`)
> - [ ] Medicaid pay for caring for someone who lives in your home  (`scope.medicaid_waiver`)
> - [ ] Pay for work for a church or religious body, or as clergy  (`scope.religious_work`)
> - [ ] A wage statement from Puerto Rico or another U.S. territory  (`f8959.territory_w2`)
> - [ ] Employer stock options used to buy shares, or such shares sold  (`s2.options_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 13, labels 55. Behind each box, optional to read: the question's own prompt (16, 18, 25, 16, 19 words) and help (38, 17, 17, 13, 21)

### 38–39. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 3. Behind each box, optional to read: the question's own prompt (9, 9 words) and help (33, 21)

### 40–42. Tick-boxes `care_help`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you have any of these?
>
> - [ ] Care for a child or a dependent, so that you could work  (`f2441.care`)
> - [ ] An employer's help with care costs, such as a dependent care account  (`f2441.benefits`)
> - [ ] Someone you paid to work in your home: a nanny, housekeeper, gardener  (`s2.household_help`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 36. Behind each box, optional to read: the question's own prompt (35, 28, 24 words) and help (33, 42, 24)

### 43–48. Tick-boxes `money_a`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> In 2025, did you get any of these?
>
> - [x] Unemployment benefits  (`s1.uc_any`)
> - [ ] Gambling or lottery winnings, or a prize or award  (`s1.winnings_any`)
> - [ ] A scholarship, a fellowship or a grant for study  (`s1.scholarship_any`)
> - [ ] Pay for serving on a jury  (`s1.jury_any`)
> - [ ] An Alaska Permanent Fund dividend  (`s1.alaska_any`)
> - [ ] Money from a hobby or pastime not run as a business  (`s1.hobby_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Unemployment benefits”; the others recorded No (background)
- Words: heading 8, labels 42. Behind each box, optional to read: the question's own prompt (7, 20, 14, 10, 10, 18 words) and help (7, 17, 14, 0, 0, 0)

### 49. `s1.uc_paid`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> How much unemployment did you get in 2025? Add up box 1 of each Form 1099-G.

- Offered: a dollar amount, zero or more
- Answer: $50,000.00 (background)
- Words: prompt 16, help 10. Help begins: “If box 1 is wrong, give the amount actually paid.”

### 50. `s1.uc_repaid`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> How much of that did you pay back in 2025 because you were overpaid?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 14, help 19. Help begins: “Give 0 if you paid none back.”

### 51. `s1.uc_unsupported`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Did you ever pay into a state unemployment fund yourself, or pay back in 2025 unemployment benefits of an earlier year?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 45. Help begins: “Paying in means money taken from your wages for the fund, as a few states require, or payments for coverage you chose as a self-employed person.”

### 52–57. Tick-boxes `money_b`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Did any of these happen to you?
>
> - [ ] Alimony paid or received since the start of 2023  (`s1.alimony_any`)
> - [ ] A debt canceled or forgiven by a lender or card company  (`s1.cod_any`)
> - [ ] A long-term care insurance payout, or life insurance paid early, in 2025  (`s1.ltc_payout`)
> - [ ] Pay in 2025 for work done while in a jail or prison  (`s1.inmate_wages`)
> - [ ] Crypto received as pay, as a reward, or from mining or staking  (`s1.digital_income`)
> - [ ] A deducted amount paid back to you (not a state tax refund)  (`scope.recovery`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 68. Behind each box, optional to read: the question's own prompt (23, 15, 21, 14, 20, 23 words) and help (22, 18, 11, 6, 21, 35)

### 58. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 59. `$retirement@person[taxpayer]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 31, help 21. Help begins: “List a Form RRB-1099-R too.”

### 60–63. Tick-boxes `accounts`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Do you have any of these accounts?
>
> - [ ] An IRA of any kind (traditional, Roth, SEP or SIMPLE)  (`person[taxpayer].ira_owner`)
> - [ ] An IRA or workplace retirement account inherited from someone who died  (`person[taxpayer].inherited_account`)
> - [ ] A 529 plan, Coverdell or ABLE account (yours or held for you)  (`person[taxpayer].x_edu_account`)
> - [ ] An Archer MSA still holding money put in above its limit  (`person[taxpayer].x_archer_excess`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 44. Behind each box, optional to read: the question's own prompt (12, 18, 26, 28 words) and help (40, 11, 25, 16)

### 64. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 0

### 65. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 15, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 66–69. Tick-boxes `rare_accounts`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did any of these apply to you?
>
> - [ ] Have a 2023 or 2024 disaster withdrawal still being taxed or repaid  (`scope.disaster_distribution`)
> - [ ] Put money into an Archer MSA (an older medical savings account)  (`scope.archer_msa`)
> - [ ] Over-contributed to an HSA for 2024, with no HSA in 2025  (`s2.hsa_testing`)
> - [ ] Got tuition refunded for a year an education credit was claimed  (`scope.education_recapture`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 45. Behind each box, optional to read: the question's own prompt (31, 22, 29, 22 words) and help (23, 14, 42, 14)

### 70. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 21, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 71–76. Tick-boxes `paid_2025`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> In 2025, did you do any of these?
>
> - [ ] Owned a home, condo or land at any time in the year  (`sa.home_owner`)
> - [ ] Had state or local income tax taken out of pay  (`sa.state_tax_any`)
> - [ ] Paid other state or local income tax, or a state disability fund  (`sa.state_tax_other_any`)
> - [ ] Paid a yearly tax on a car or boat, based on value  (`sa.personal_property_tax_any`)
> - [ ] Gave money or things to charity, or paid costs of volunteering  (`sa.gifts`)
> - [ ] Paid medical bills, after insurance, above 7.5% of your income  (`sa.medical_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 67. Behind each box, optional to read: the question's own prompt (14, 23, 34, 28, 21, 21 words) and help (31, 0, 39, 24, 39, 32)

### 77–80. Tick-boxes `paid_more`: 4 questions on one screen

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`); Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Do any of these apply to you for 2025?
>
> - [ ] Paid interest on a boat or camper loan or another person's mortgage  (`sa.home_other`)
> - [ ] Have a gift to charity from an earlier year still being deducted  (`sa.gift_carryover`)
> - [ ] Paid for your own health insurance, not through a job (Medicare, COBRA)  (`sa.medical_premiums`)
> - [ ] Had property damaged, destroyed or stolen (a loss, or an insurance gain)  (`sd.casualty`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 48. Behind each box, optional to read: the question's own prompt (33, 28, 24, 26 words) and help (34, 39, 39, 43)

### 81–85. Tick-boxes `rare_deductions`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do any of these uncommon things apply to you?
>
> - [ ] Reported inherited income on which federal estate tax was paid  (`sa.estate_tax_income`)
> - [ ] Have premium left to deduct on a bond bought above face value  (`sa.bond_premium`)
> - [ ] Lost money on an inflation-protected or contingent-payment bond held directly  (`sa.debt_instrument_loss`)
> - [ ] This return is for someone who died with unrecovered pension contributions  (`sa.pension_unrecovered`)
> - [ ] Have a disability and pay for help or equipment needed to work  (`sa.impairment_work`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 55. Behind each box, optional to read: the question's own prompt (27, 32, 31, 27, 27 words) and help (36, 24, 31, 37, 27)

### 86–87. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 88–93. Tick-boxes `home_school`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`); Schedule 3 — selected lines (`s3`); Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`); Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits) (`f8863`); Student Loan Interest Deduction Worksheet—Schedule 1, Line 21 (`sli`)

> And in 2025, did you do any of these?
>
> - [ ] Paid interest on a loan for a car bought new in 2025  (`s1a.carloan`)
> - [ ] Got an electric or plug-in vehicle, or installed a home charger  (`s3.ev`)
> - [ ] Used kerosene at home for heat, light or cooking  (`s3.kerosene`)
> - [ ] Had solar, insulation, windows, doors or heating equipment installed at home  (`f5695.any`)
> - [ ] Had college or trade school tuition paid, for you or a dependent  (`f8863.paid`)
> - [ ] Paid interest on a student loan  (`sli.any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 61. Behind each box, optional to read: the question's own prompt (19, 22, 13, 27, 20, 10 words) and help (37, 19, 0, 34, 32, 18)

### 94. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 34, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 95. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 0

### 96. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 97. `f1040.tax_exempt_interest`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> How much tax-exempt interest did you get in 2025, for example from a city or state bond? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 38. Help begins: “Box 8 of Form 1099-INT, and tax-exempt amounts on Form 1099-OID (boxes 2 and 11), less any bond premium.”

### 98. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 21, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 99. `sb.ordinary_dividends`

**⟶ topic switch**

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> Add up box 1a (total ordinary dividends) of all your Forms 1099-DIV for 2025. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $1,840.00 (persona)
- Words: prompt 17, help 49. Help begins: “A broker's combined statement counts as a Form 1099-DIV.”

### 100. `f1040.line3a`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 3a

> Add up box 1b (qualified dividends) of the same forms. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $1,520.00 (persona)
- Words: prompt 13, help 39. Help begins: “Box 1b is a part of box 1a.”

### 101. `sd.distributions`

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Capital gain distributions, generally Form 1099-DIV box 2a

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 8, help 30. Help begins: “The total of box 2a of every Form 1099-DIV and substitute statement in your or your spouse's name, including amounts reinvested, plus any capital gain distributions received without a form.”

### 102. `qbi.dividends`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Add up box 5 (section 199A dividends) of the same forms. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 14, help 27. Help begins: “Box 5 is a part of box 1a, usually from real estate funds (REITs).”

### 103. `div.box12`

**⟶ topic switch (returns)**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> Exempt-interest dividends, box 12 (total of all your Forms 1099-DIV; box 13 amounts are already included)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 12. Help begins: “Enter the amounts of all your and your spouse's Forms 1099-DIV combined.”

### 104. `div.other_boxes`

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> Look at your Forms 1099-DIV for 2025. Does any of them show an amount in box 2b, 2c, 2d, 2e, 2f, 3, 9, 10 or 13?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 26, help 22. Help begins: “Most forms show amounts only in boxes 1a, 1b, 2a, 5, 7 and 12.”

### 105. `sd.f2439`

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Did a mutual fund or a real estate investment trust (REIT) send you a Form 2439 for 2025, a notice of gains it kept and paid tax on?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 28, help 16. Help begins: “A return with this is outside what this tool prepares; a Yes ends the interview here.”

### 106. `sb.nominee`

**⟶ topic switch (returns)**

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> Does any of the interest or dividends you received in 2025 belong to someone else, for example to the other owner of a joint account who is not your spouse?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 30, help 34. Help begins: “Interest and dividends on an account you own with your spouse are all yours on a joint return.”

### 107. `sb.bonds_any`

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> In 2025, did you own bonds or notes directly (not through a fund), cash in U.S. savings bonds, or receive interest on money you lent or on a property you sold?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 31, help 25. Help begins: “Interest from a bank account, a certificate of deposit or a fund is not what this asks about.”

### 108. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: the list `stock_a`, `stock_b` (persona)
- Words: prompt 38, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 109. `sd.route_each`

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Do you want to choose, sale by sale, between listing a sale on Form 8949 and adding it to a total on Schedule D? The tax is the same either way; with a No, every sale is listed.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 38, help 35. Help begins: “A sale whose basis the broker reported to the IRS, and that needs no adjustment, may be added to a total on Schedule D instead of being listed on Form 8949.”

### 110. `sales[stock_a].box`

**⟶ topic switch (returns)**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_a

> Under which heading does your broker's statement (Form 1099-B) list this sale?

- Offered: “Short-term, basis reported to the IRS (box A)” / “Long-term, basis reported to the IRS (box D)” / “Short-term, basis not reported to the IRS (box B)” / “Long-term, basis not reported to the IRS (box E)” / “Not on a Form 1099-B, and owned for one year or less (box C)” / “Not on a Form 1099-B, and owned for more than one year (box F)” / “Crypto or another digital asset on a Form 1099-DA, short-term, basis reported to the IRS (box G)” / “Crypto or another digital asset on a Form 1099-DA, short-term, basis not reported to the IRS (box H)” / “Crypto or another digital asset on no form, owned for one year or less (box I)” / “Crypto or another digital asset on a Form 1099-DA, long-term, basis reported to the IRS (box J)” / “Crypto or another digital asset on a Form 1099-DA, long-term, basis not reported to the IRS (box K)” / “Crypto or another digital asset on no form, owned for more than one year (box L)”
- Answer: “Short-term, basis reported to the IRS (box A)” (`A`) (persona)
- Words: prompt 12, help 53. Help begins: “With no statement, count from the day after you got the property through the day you sold it; more than one year is long-term, and inherited property is always long-term.”

### 111. `sales[stock_a].special`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_a

> Is this sale any of these?
>
> - a collectible (art, antiques, coins, stamps, gems, gold or silver), or shares of a fund that holds gold, silver or other metals
> - small business stock on which you exclude part of the gain (section 1202)
> - real estate you once rented out or took a home office deduction for
> - your share of a partnership, an S corporation or a trust that owns collectibles or depreciated buildings
> - an investment in an opportunity zone fund, or a gain you put off by investing in one

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 88, help 38. Help begins: “A broker's statement marks a collectible or an opportunity zone fund (QOF) with a checkbox in box 3.”

### 112. `sales[stock_a].proceeds`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_a

> Proceeds of this sale (box 1d of Form 1099-B). With no statement, the sale price less commissions and fees.

- Offered: a dollar amount, zero or more
- Answer: $12,400.00 (persona)
- Words: prompt 19, help 28. Help begins: “If you received more than the statement shows, enter what you received.”

### 113. `sales[stock_a].reported_basis`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_a

> Cost or other basis the statement shows for this sale (box 1e of Form 1099-B).

- Offered: a dollar amount, zero or more
- Answer: $14,900.00 (persona)
- Words: prompt 15, help 0

### 114. `sales[stock_a].code`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_a

> Does anything need adjusting for this sale?

- Offered: “No, the figures are right and there is no wash sale” / “A wash sale, where part of the loss is not allowed (box 1g of Form 1099-B, or a rebuy within 30 days)” / “The basis on the statement is wrong” / “Both, the basis is wrong and there is a wash sale” / “Something else, such as selling costs the statement leaves out, accrued market discount (box 1f) or the Ordinary box checked”
- Answer: “No, the figures are right and there is no wash sale” (`none`) (persona)
- Words: prompt 7, help 0

### 115. `sales[stock_b].box`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_b

> Under which heading does your broker's statement (Form 1099-B) list this sale?

- Offered: “Short-term, basis reported to the IRS (box A)” / “Long-term, basis reported to the IRS (box D)” / “Short-term, basis not reported to the IRS (box B)” / “Long-term, basis not reported to the IRS (box E)” / “Not on a Form 1099-B, and owned for one year or less (box C)” / “Not on a Form 1099-B, and owned for more than one year (box F)” / “Crypto or another digital asset on a Form 1099-DA, short-term, basis reported to the IRS (box G)” / “Crypto or another digital asset on a Form 1099-DA, short-term, basis not reported to the IRS (box H)” / “Crypto or another digital asset on no form, owned for one year or less (box I)” / “Crypto or another digital asset on a Form 1099-DA, long-term, basis reported to the IRS (box J)” / “Crypto or another digital asset on a Form 1099-DA, long-term, basis not reported to the IRS (box K)” / “Crypto or another digital asset on no form, owned for more than one year (box L)”
- Answer: “Long-term, basis reported to the IRS (box D)” (`D`) (persona)
- Words: prompt 12, help 53. Help begins: “With no statement, count from the day after you got the property through the day you sold it; more than one year is long-term, and inherited property is always long-term.”

### 116. `sales[stock_b].special`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_b

> Is this sale any of these?
>
> - a collectible (art, antiques, coins, stamps, gems, gold or silver), or shares of a fund that holds gold, silver or other metals
> - small business stock on which you exclude part of the gain (section 1202)
> - real estate you once rented out or took a home office deduction for
> - your share of a partnership, an S corporation or a trust that owns collectibles or depreciated buildings
> - an investment in an opportunity zone fund, or a gain you put off by investing in one

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 88, help 38. Help begins: “A broker's statement marks a collectible or an opportunity zone fund (QOF) with a checkbox in box 3.”

### 117. `sales[stock_b].proceeds`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_b

> Proceeds of this sale (box 1d of Form 1099-B). With no statement, the sale price less commissions and fees.

- Offered: a dollar amount, zero or more
- Answer: $31,000.00 (persona)
- Words: prompt 19, help 28. Help begins: “If you received more than the statement shows, enter what you received.”

### 118. `sales[stock_b].reported_basis`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_b

> Cost or other basis the statement shows for this sale (box 1e of Form 1099-B).

- Offered: a dollar amount, zero or more
- Answer: $22,500.00 (persona)
- Words: prompt 15, help 0

### 119. `sales[stock_b].code`

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`). About: sales stock_b

> Does anything need adjusting for this sale?

- Offered: “No, the figures are right and there is no wash sale” / “A wash sale, where part of the loss is not allowed (box 1g of Form 1099-B, or a rebuy within 30 days)” / “The basis on the statement is wrong” / “Both, the basis is wrong and there is a wash sale” / “Something else, such as selling costs the statement leaves out, accrued market discount (box 1f) or the Ordinary box checked”
- Answer: “No, the figures are right and there is no wash sale” (`none`) (persona)
- Words: prompt 7, help 0

### 120–124. Tick-boxes `sales_rare`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> In 2025, did you have any of these less common sales or trades?
>
> - [ ] Sold real estate or business property, or got installments from any sale  (`sd.sold_other`)
> - [ ] Traded futures, foreign currency contracts or index options, or held a straddle  (`sd.sec1256`)
> - [ ] Had business or investment property taken by a government  (`sd.condemned`)
> - [ ] Lost money on small-company stock and claim it as an ordinary loss  (`sd.small_business_stock`)
> - [ ] Trade securities as a business under a mark-to-market election  (`sd.trader_election`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 13, labels 54. Behind each box, optional to read: the question's own prompt (33, 36, 20, 34, 18 words) and help (29, 34, 28, 37, 39)

### 125–126. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your investments?
>
> - [x] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “A loss from selling investments in 2024, or one carried into 2024”; the other recorded No (persona; background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (23, 24 words) and help (34, 37)

### 127. `clcw.spouse_screen`

**⟶ topic switch**

Topic: Capital Loss Carryover Worksheet—Lines 6 and 14 (`clcw`)

> Is either of these true: the 2024 return these figures come from was a joint return, and for 2025 you are not filing a joint return with the same spouse (for example after a divorce, a separation or the death of your spouse in 2024); or, on this 2025 joint return, you and your spouse each filed a separate 2024 return whose Schedule D line 21 showed a loss?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 69, help 32. Help begins: “If, on a 2025 joint return, only one of you filed a separate 2024 return with a loss on Schedule D line 21, answer No and enter the figures from that return.”

### 128. `clcw.prior_sd7`

Topic: Capital Loss Carryover Worksheet—Lines 6 and 14 (`clcw`)

> The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss), negative if it was a loss

- Offered: a dollar amount, which may be negative
- Answer: -$2,000.00 (persona)
- Words: prompt 22, help 18. Help begins: “Line 7 of your 2024 Schedule D; a loss (printed in parentheses) is entered as a negative amount.”

### 129. `clcw.prior_sd15`

Topic: Capital Loss Carryover Worksheet—Lines 6 and 14 (`clcw`)

> The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss), negative if it was a loss

- Offered: a dollar amount, which may be negative
- Answer: -$9,500.00 (persona)
- Words: prompt 22, help 18. Help begins: “Line 15 of your 2024 Schedule D; a loss (printed in parentheses) is entered as a negative amount.”

### 130. `clcw.prior_sd21`

Topic: Capital Loss Carryover Worksheet—Lines 6 and 14 (`clcw`)

> The loss on line 21 of your 2024 Schedule D, entered as a positive amount (line 21 is printed in parentheses)

- Offered: a dollar amount, zero or more
- Answer: $3,000.00 (persona)
- Words: prompt 21, help 21. Help begins: “The loss printed in parentheses on line 21 of your 2024 Schedule D (at most $3,000), entered as a positive amount.”

### 131. `clcw.prior_11`

Topic: Capital Loss Carryover Worksheet—Lines 6 and 14 (`clcw`)

> The amount on line 11 of your 2024 Form 1040 or 1040-SR (your adjusted gross income for 2024), negative if it was a loss

- Offered: a dollar amount, which may be negative
- Answer: $104,000.00 (persona)
- Words: prompt 24, help 61. Help begins: “The amount printed on line 11 of the Form 1040 or 1040-SR you filed for 2024; a loss is entered as a negative amount.”

### 132. `clcw.prior_14`

Topic: Capital Loss Carryover Worksheet—Lines 6 and 14 (`clcw`)

> The amount on line 14 of your 2024 Form 1040 or 1040-SR (your standard or itemized deduction plus the qualified business income deduction)

- Offered: a dollar amount, zero or more
- Answer: $14,600.00 (persona)
- Words: prompt 23, help 16. Help begins: “The amount printed on line 14 of the Form 1040 or 1040-SR you filed for 2024.”

### 133. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 134. `ftc.taxes`

**⟶ topic switch**

Topic: Foreign tax credit — election without Form 1116 (`ftc`)

> How much foreign tax did you pay in 2025? Add up box 7 of your Forms 1099-DIV, box 6 of your Forms 1099-INT, and any income tax you paid to another country yourself. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 36, help 13. Help begins: “Count only income taxes, after any reduction the foreign tax credit rules require.”

### 135–140. Tick-boxes `outside_us`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule B — supported interest and ordinary dividends (`sb`); Proof-of-concept scope screening (`scope`)

> At any time in 2025, did you have any of these outside the United States?
>
> - [ ] An account in another country, or the power to sign for one  (`sb.account_any`)
> - [ ] Other property abroad, or money owed to you by someone abroad  (`sb.asset_any`)
> - [ ] A tie to a trust or family foundation abroad  (`sb.trust_any`)
> - [ ] A foreign company you help run, or own 10% or more of  (`sb.company_any`)
> - [ ] An account, investment, company or trust in a U.S. territory  (`sb.territory_any`)
> - [ ] Shares of a foreign company or fund, held outside a U.S. fund  (`scope.foreign_shares`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 15, labels 66. Behind each box, optional to read: the question's own prompt (28, 24, 38, 32, 25, 27 words) and help (35, 42, 30, 26, 23, 15)

### 141–143. Tick-boxes `rare_credits`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you do any of these?
>
> - [ ] Got a federal tax credit from a bond or a fund  (`s3.credit_bond`)
> - [ ] Sold farmland  (`s3.farmland`)
> - [ ] Paid back more than $3,000 of income from an earlier year  (`s3.repaid_income`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (16, 6, 19 words) and help (17, 9, 35)

### 144. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 145–147. Tick-boxes `other_taxes`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> Do you owe any of these for 2025?
>
> - [ ] A tax credit from an earlier year that must be paid back  (`s2.credit_recapture`)
> - [ ] Alternative minimum tax  (`s2.amt_owed`)
> - [ ] Another federal tax you have not been asked about  (`s2.other_tax`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (16, 8, 16 words) and help (37, 38, 43)

### 148. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 149. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 150. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 151. `qbi.prior_form`

**⟶ topic switch (returns)**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 152. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 153–154. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 18, labels 21. Behind each box, optional to read: the question's own prompt (26, 20 words) and help (39, 22)

### 155. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

### 156. `ny_it201.ask.city_resident`

**⟶ topic switch**

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you live in New York City (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 19, help 43. Help begins: “Count time away on vacation, for work or at school if your home stayed in the city.”

### 157–159. Tick-boxes `ny_where`: 3 questions on one screen

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did any of these apply to you?
>
> - [ ] Lived, worked or kept a home in Yonkers in 2025  (`ny_it201.ask.yonkers`)
> - [ ] Moved into New York City on January 1, 2025  (`ny_it201.ask.moved_in`)
> - [ ] Moved out of New York City on January 1, 2026  (`ny_it201.ask.moved_out`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 29. Behind each box, optional to read: the question's own prompt (17, 11, 12 words) and help (20, 22, 20)

### 160. `ny_it201.ask.decedent`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Is this return for someone who has died?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 8, help 31. Help begins: “Answer Yes if you are filing for a person who died in 2025 or since, including a husband or wife on this joint return.”

### 161. `ny_it201.ask.item_c`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> You said no one can claim you as a dependent. Could a parent or someone else claim you if they filed a return, even one they do not have to file?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 31, help 36. Help begins: “New York counts you as someone's dependent even when that person does not file or did not claim you.”

### 162. `ny_it201.ask.public_job`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> In 2025, did you work for the government in New York, including a public school or college or the MTA?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 20, help 29. Help begins: “Count the State, a city, county, town or village, a school district, SUNY or CUNY, and public authorities such as the MTA.”

### 163–164. Tick-boxes `ny_interest`: 2 questions on one screen

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did any of your interest or dividends come from these?
>
> - [ ] U.S. Treasury or savings bonds, or a fund holding them  (`ny_it201.ask.us_obligation_interest`)
> - [ ] Build America Bonds  (`ny_it201.ask.bab`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 10, labels 13. Behind each box, optional to read: the question's own prompt (23, 11 words) and help (39, 33)

### 165. `ny_it201.ask.it225`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does any item on New York's list of less common income changes (Form IT-225) apply to you? Most people have none.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 29. Help begins: “The list covers, for example, a disability income exclusion, a trust's accumulation distribution, and payments such as Holocaust reparations or a wrongful-conviction award.”

### 166. `ny_it201.ask.itemize`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Do you want to itemize deductions on your New York return instead of taking the New York standard deduction?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 58. Help begins: “New York lets you choose either, whatever you did on your federal return.”

### 167. `ny_it201.ask.resident_credit`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> In 2025, did you pay income tax to another state, or to a city or Canadian province outside New York?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 20, help 40. Help begins: “For example tax taken out of pay for New Jersey or Connecticut (another state in box 15 of a Form W-2), or tax paid to Washington, D.C.”

### 168. `ny_it201.ask.noncustodial`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you pay child support in 2025 through New York's child support program (a Support Collection Unit)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 17, help 17. Help begins: “Such a parent may get a New York credit (Form IT-209), which this tool does not compute.”

### 169. `ny_it201.ask.other_credits`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Are you claiming any other New York State tax credit, such as for long-term care insurance, home solar equipment or a business?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 26. Help begins: “These credits are claimed on their own forms and Form IT-201-ATT.”

### 170. `ny_it201.ask.other_taxes`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Do you owe any other New York tax, such as a tax on a lump-sum retirement payment or the payback of a New York credit taken earlier?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 15. Help begins: “Other New York taxes are reported on Form IT-201-ATT, which this tool does not prepare.”

### 171. `ny_it201.ask.owes_use_tax`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> In 2025, did you buy anything taxable in New York without paying New York sales tax on it (for example online, by mail, or in another state)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 27. Help begins: “The return must state the tax owed on such purchases (use tax), or 0.”

### 172. `ny_it201.ask.other_withholding`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Was New York income tax taken out of any retirement, unemployment or other payment to you (not pay on a Form W-2)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 24. Help begins: “Look at the state and local boxes of your Forms 1099-R, 1099-G and W-2G.”

### 173. `$ny_it2`

**⟶ topic switch**

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`)

> List your Forms W-2 again, one entry per form, so their New York boxes can be entered; include a W-2 that shows no New York tax.

- Offered: a list the filer builds, naming each entry
- Answer: the list `software_co` (persona)
- Words: prompt 26, help 27. Help begins: “New York needs a record for each Form W-2 you received (Form IT-2).”

### 174. `ny_it2[software_co].state_withheld`

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`), line 17a. About: ny_it2 software_co

> For this Form W-2 (Form IT-2, W-2 record) — New York State income tax withheld on this Form W-2 (box 17 for New York State; 0 if none)

- Offered: a dollar amount, zero or more
- Answer: $7,000.00 (persona)
- Words: prompt 27, help 20. Help begins: “Box 17 of the Form W-2, the state income tax withheld, where box 15 shows NY.”

### 175. `ny_it2[software_co].city_withheld`

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`), line 19. About: ny_it2 software_co

> For this Form W-2 (Form IT-2, W-2 record) — Form W-2 box 19, local income tax withheld for New York City (0 if none)

- Offered: a dollar amount, zero or more
- Answer: $4,500.00 (persona)
- Words: prompt 23, help 23. Help begins: “Box 19 of the Form W-2, the local income tax withheld, where box 20 shows New York City (NYC).”

### 176. `ny_it2[software_co].yonkers_withheld`

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`), line 19 (Yonkers). About: ny_it2 software_co

> For this Form W-2 (Form IT-2, W-2 record) — Form W-2 box 19, local income tax withheld for Yonkers (0 if none)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 21, help 21. Help begins: “Box 19 of the Form W-2 where box 20 shows Yonkers.”

### 177. `ny_it201.ask.est_any`

**⟶ topic switch (returns)**

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Apart from tax taken out of your pay, did you pay New York income tax for 2025 ahead of time, or have a 2024 New York refund applied to it?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 30, help 37. Help begins: “Count estimated tax payments (the last one may be paid in January 2026), a 2024 New York refund you asked to have applied to 2025, and a payment made with a request for more time to file.”

### 178–180. Tick-boxes `ny_filing`: 3 questions on one screen

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Do any of these apply to you?
>
> - [ ] Outside the U.S. on April 15, 2026, and filing later  (`ny_it201.ask.abroad`)
> - [ ] Will ask to pay what you owe in installments  (`ny_it201.ask.installment`)
> - [ ] Giving to a New York State charity fund on this return  (`ny_it201.ask.contributions`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 30. Behind each box, optional to read: the question's own prompt (25, 14, 17 words) and help (22, 17, 15)

### 181. `ny_it201.ask.prior_full_year`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you file a New York return for 2024 that covered all 12 months?

- Offered: Yes / No
- Answer: Yes (background)
- Words: prompt 14, help 46. Help begins: “You owe more than was paid in.”

### 182. `ny_it201.ask.prior_agi_high`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Was the New York adjusted gross income on your 2024 return more than $150,000?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 14, help 22. Help begins: “Above $150,000 ($75,000 married filing separately), what you paid during 2025 must reach 110% of your 2024 tax to avoid the penalty.”

### 183. `ny_it201.ask.prior_year_tax`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> What was the total New York State and City income tax on your 2024 New York return?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 17, help 14. Help begins: “Used only to check for the penalty for paying too little during the year.”

### 184. `ny_it201.ask.late_penalty`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Will you pay the New York tax you owe after April 15, 2026, or file this return after its due date?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 12. Help begins: “Late filing and late payment penalties and interest are outside this tool.”

## The end reached

**Complete.** The return is completed after 184 questions.

## Totals

| | |
|---|---|
| Questions asked | 184 |
| Steps (screens; a tick-box group shown together is one) | 111 |
| Answered by the persona / by the background / opened and unanswered | 52 / 132 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 3057 |
| Help words (optional to read) | 4668 |
| Words of the answers offered (Yes and No not counted) | 575 |
| Questions answered no, zero or none | 150 |
| Topics met | 34 |
| New York stretch (questions of New York forms): questions / steps / prompt words / help words | 29 / 24 / 542 / 785 |
| Topic switches | 73 |
| of them, returns to a topic already left | 40 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 111 | `sales[stock_a].special` | 88 | No |
| 116 | `sales[stock_b].special` | 88 | No |
| 127 | `clcw.spouse_screen` | 69 | No |
| 108 | `$sales` | 38 | the list `stock_a`, `stock_b` |
| 109 | `sd.route_each` | 38 | No |
| 137 | `sb.trust_any` (its own prompt, behind a tick-box) | 38 | No |
| 121 | `sd.sec1256` (its own prompt, behind a tick-box) | 36 | No |
| 134 | `ftc.taxes` | 36 | $0.00 |
| 40 | `f2441.care` (its own prompt, behind a tick-box) | 35 | No |
| 73 | `sa.state_tax_other_any` (its own prompt, behind a tick-box) | 34 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                  6w  ["taxpayer"]                  [person]
> *  2  f1040.status                             9w  "single"                      [f1040]
>    3  household.ever_married                   5w  false                         [household]
     4  household.community_property            20w  false
>>*  5  person[taxpayer].birth_year              6w  1980                          [person]
>    6  sa.dependent                            15w  false                         [sa]
>>   7  person[taxpayer].blind                  25w  false                         [person]
>    8  scope.noncitizen                        16w+ false                         [scope]  (screen 8, about_you)
     9  scope.under24                            7w+ false                         (screen 8, about_you)
    10  scope.armed_forces                      12w+ false                         (screen 8, about_you)
>>  11  sa.excluded_income                      12w+ false                         [sa]  (screen 8, about_you)
>>  12  scope.chapter11                         11w+ false                         [scope]  (screen 8, about_you)
>   13  s3.disability_retired                    8w  false                         [s3]
>   14  $dependent                              30w  []                            [dependent]
>>  15  s3.adoption_any                         19w+ false                         [s3]  (screen 11, child_extras)
>>  16  scope.f8814                             11w+ false                         [scope]  (screen 11, child_extras)
    17  scope.rental                            19w+ false                         (screen 12, own_income)
    18  scope.k1                                12w+ false                         (screen 12, own_income)
    19  scope.farm                               6w+ false                         (screen 12, own_income)
>>  20  person[taxpayer].rrta                   13w+ false                         [person]  (screen 13, work_kind)
    21  person[taxpayer].eligible_educator      11w+ false                         (screen 13, work_kind)
> * 22  $w2@person[taxpayer]                     8w  ["software_co"]               [w2]
  * 23  person[taxpayer].w2[software_co].box1    6w  11800000
  * 24  person[taxpayer].w2[software_co].box2    6w  1890000
  * 25  person[taxpayer].w2[software_co].box4    6w  731600
  * 26  person[taxpayer].w2[software_co].box5    6w  11800000
  * 27  person[taxpayer].w2[software_co].box6    5w  171100
> * 28  s2.w2_marks                             22w+ false                         [s2]  (screen 20, w2_jobs)
> * 29  s1.nqdc_pension                         12w+ false                         [s1]  (screen 20, w2_jobs)
>>* 30  scope.w2_marks                          10w+ false                         [scope]  (screen 20, w2_jobs)
  * 31  scope.artist_official                   12w+ false                         (screen 20, w2_jobs)
  * 32  scope.excess_deferral                   12w+ false                         (screen 20, w2_jobs)
    33  scope.pay_no_w2                         24w+ false                         (screen 21, other_pay)
    34  scope.medicaid_waiver                   11w+ false                         (screen 21, other_pay)
    35  scope.religious_work                    12w+ false                         (screen 21, other_pay)
>   36  f8959.territory_w2                      10w+ false                         [f8959]  (screen 21, other_pay)
>>  37  s2.options_any                          11w+ false                         [s2]  (screen 21, other_pay)
>   38  s1a.tips                                12w+ false                         [s1a]  (screen 22, tips_overtime)
    39  s1a.overtime                             2w+ false                         (screen 22, tips_overtime)
>   40  f2441.care                              20w+ false                         [f2441]  (screen 23, care_help)
    41  f2441.benefits                          12w+ false                         (screen 23, care_help)
>>  42  s2.household_help                       12w+ false                         [s2]  (screen 23, care_help)
>>  43  s1.uc_any                               10w+ true                          [s1]  (screen 24, money_a)
    44  s1.winnings_any                          9w+ false                         (screen 24, money_a)
    45  s1.scholarship_any                       9w+ false                         (screen 24, money_a)
    46  s1.jury_any                              6w+ false                         (screen 24, money_a)
    47  s1.alaska_any                            5w+ false                         (screen 24, money_a)
    48  s1.hobby_any                            11w+ false                         (screen 24, money_a)
    49  s1.uc_paid                              16w  5000000
    50  s1.uc_repaid                            14w  0
    51  s1.uc_unsupported                       21w  false
    52  s1.alimony_any                          16w+ false                         (screen 28, money_b)
    53  s1.cod_any                              11w+ false                         (screen 28, money_b)
    54  s1.ltc_payout                           12w+ false                         (screen 28, money_b)
    55  s1.inmate_wages                         12w+ false                         (screen 28, money_b)
    56  s1.digital_income                       12w+ false                         (screen 28, money_b)
>>  57  scope.recovery                          12w+ false                         [scope]  (screen 28, money_b)
>   58  refund.any                              13w  false                         [refund]
>   59  $retirement@person[taxpayer]            31w  []                            [retirement]
>>  60  person[taxpayer].ira_owner              17w+ false                         [person]  (screen 31, accounts)
    61  person[taxpayer].inherited_account      11w+ false                         (screen 31, accounts)
    62  person[taxpayer].x_edu_account          12w+ false                         (screen 31, accounts)
    63  person[taxpayer].x_archer_excess        11w+ false                         (screen 31, accounts)
>   64  ssb.any                                 23w  false                         [ssb]
>   65  $f8889@person[taxpayer]                 15w  []                            [f8889]
>>  66  scope.disaster_distribution             21w+ false                         [scope]  (screen 34, rare_accounts)
    67  scope.archer_msa                        11w+ false                         (screen 34, rare_accounts)
>>  68  s2.hsa_testing                          11w+ false                         [s2]  (screen 34, rare_accounts)
>>  69  scope.education_recapture               11w+ false                         [scope]  (screen 34, rare_accounts)
>   70  $f1095a                                 21w  []                            [f1095a]
>>  71  sa.home_owner                           20w+ false                         [sa]  (screen 36, paid_2025)
    72  sa.state_tax_any                        10w+ false                         (screen 36, paid_2025)
    73  sa.state_tax_other_any                  12w+ false                         (screen 36, paid_2025)
    74  sa.personal_property_tax_any            12w+ false                         (screen 36, paid_2025)
    75  sa.gifts                                11w+ false                         (screen 36, paid_2025)
    76  sa.medical_any                          10w+ false                         (screen 36, paid_2025)
    77  sa.home_other                           21w+ false                         (screen 37, paid_more)
    78  sa.gift_carryover                       12w+ false                         (screen 37, paid_more)
    79  sa.medical_premiums                     12w+ false                         (screen 37, paid_more)
>   80  sd.casualty                             12w+ false                         [sd]  (screen 37, paid_more)
>>  81  sa.estate_tax_income                    19w+ false                         [sa]  (screen 38, rare_deductions)
    82  sa.bond_premium                         12w+ false                         (screen 38, rare_deductions)
    83  sa.debt_instrument_loss                 10w+ false                         (screen 38, rare_deductions)
    84  sa.pension_unrecovered                  11w+ false                         (screen 38, rare_deductions)
    85  sa.impairment_work                      12w+ false                         (screen 38, rare_deductions)
    86  sa.elect_itemize                        16w+ false                         (screen 39, deduction_wishes)
    87  sa.sales_tax_wish                       12w+ false                         (screen 39, deduction_wishes)
>>  88  s1a.carloan                             21w+ false                         [s1a]  (screen 40, home_school)
>>  89  s3.ev                                   11w+ false                         [s3]  (screen 40, home_school)
    90  s3.kerosene                              9w+ false                         (screen 40, home_school)
>   91  f5695.any                               11w+ false                         [f5695]  (screen 40, home_school)
>   92  f8863.paid                              12w+ false                         [f8863]  (screen 40, home_school)
>   93  sli.any                                  6w+ false                         [sli]  (screen 40, home_school)
>   94  $sc@person[taxpayer]                    34w  []                            [sc]
>>  95  scope.business_before                   25w  false                         [scope]
>   96  $interest                               21w  []                            [interest]
>>  97  f1040.tax_exempt_interest               20w  0                             [f1040]
> * 98  div.any                                 21w  true                          [div]
> * 99  sb.ordinary_dividends                   17w  184000                        [sb]
>>*100  f1040.line3a                            13w  152000                        [f1040]
>>*101  sd.distributions                         8w  0                             [sd]
> *102  qbi.dividends                           14w  0                             [qbi]
>>*103  div.box12                               16w  0                             [div]
  *104  div.other_boxes                         26w  false
>>*105  sd.f2439                                28w  false                         [sd]
>>*106  sb.nominee                              30w  false                         [sb]
  *107  sb.bonds_any                            31w  false
> *108  $sales                                  38w  ["stock_a","stock_b"]         [sales]
>>*109  sd.route_each                           38w  false                         [sd]
>>*110  sales[stock_a].box                      12w  "A"                           [sales]
  *111  sales[stock_a].special                  88w  false
  *112  sales[stock_a].proceeds                 19w  1240000
  *113  sales[stock_a].reported_basis           15w  1490000
  *114  sales[stock_a].code                      7w  "none"
  *115  sales[stock_b].box                      12w  "D"
  *116  sales[stock_b].special                  88w  false
  *117  sales[stock_b].proceeds                 19w  3100000
  *118  sales[stock_b].reported_basis           15w  2250000
  *119  sales[stock_b].code                      7w  "none"
>> 120  sd.sold_other                           25w+ false                         [sd]  (screen 67, sales_rare)
   121  sd.sec1256                              12w+ false                         (screen 67, sales_rare)
   122  sd.condemned                             9w+ false                         (screen 67, sales_rare)
   123  sd.small_business_stock                 12w+ false                         (screen 67, sales_rare)
   124  sd.trader_election                       9w+ false                         (screen 67, sales_rare)
  *125  sd.carryover                            20w+ true                          (screen 68, invest_other)
>  126  f4952.has_interest                      12w+ false                         [f4952]  (screen 68, invest_other)
> *127  clcw.spouse_screen                      69w  false                         [clcw]
  *128  clcw.prior_sd7                          22w  -200000
  *129  clcw.prior_sd15                         22w  -950000
  *130  clcw.prior_sd21                         21w  300000
  *131  clcw.prior_11                           24w  10400000
  *132  clcw.prior_14                           23w  1460000
>> 133  s3.foreign_any                          24w  false                         [s3]
> *134  ftc.taxes                               36w  0                             [ftc]
>> 135  sb.account_any                          27w+ false                         [sb]  (screen 77, outside_us)
   136  sb.asset_any                            11w+ false                         (screen 77, outside_us)
   137  sb.trust_any                             9w+ false                         (screen 77, outside_us)
   138  sb.company_any                          12w+ false                         (screen 77, outside_us)
   139  sb.territory_any                        10w+ false                         (screen 77, outside_us)
>> 140  scope.foreign_shares                    12w+ false                         [scope]  (screen 77, outside_us)
>> 141  s3.credit_bond                          19w+ false                         [s3]  (screen 78, rare_credits)
   142  s3.farmland                              2w+ false                         (screen 78, rare_credits)
   143  s3.repaid_income                        11w+ false                         (screen 78, rare_credits)
   144  s3.prior_other_forms                    25w  false
>> 145  s2.credit_recapture                     20w+ false                         [s2]  (screen 80, other_taxes)
   146  s2.amt_owed                              3w+ false                         (screen 80, other_taxes)
   147  s2.other_tax                             9w+ false                         (screen 80, other_taxes)
>  148  $oi8z                                   21w  []                            [oi8z]
>> 149  scope.reforestation                     22w  false                         [scope]
   150  scope.attorney_fees                     21w  false
>> 151  qbi.prior_form                          19w  false                         [qbi]
   152  qbi.coop_patron                         19w  false
>> 153  f1040.withheld_other_any                29w+ false                         [f1040]  (screen 86, paid_already)
   154  f1040.estimated_any                     10w+ false                         (screen 86, paid_already)
>> 155  s3.line10                               20w  0                             [s3]
> *156  ny_it201.ask.city_resident              19w  true                          [ny_it201]
   157  ny_it201.ask.yonkers                    17w+ false                         (screen 89, ny_where)
   158  ny_it201.ask.moved_in                    9w+ false                         (screen 89, ny_where)
   159  ny_it201.ask.moved_out                  10w+ false                         (screen 89, ny_where)
   160  ny_it201.ask.decedent                    8w  false
   161  ny_it201.ask.item_c                     31w  false
  *162  ny_it201.ask.public_job                 20w  false
  *163  ny_it201.ask.us_obligation_interest     20w+ false                         (screen 93, ny_interest)
  *164  ny_it201.ask.bab                         3w+ false                         (screen 93, ny_interest)
   165  ny_it201.ask.it225                      21w  false
   166  ny_it201.ask.itemize                    19w  false
   167  ny_it201.ask.resident_credit            20w  false
   168  ny_it201.ask.noncustodial               17w  false
   169  ny_it201.ask.other_credits              22w  false
   170  ny_it201.ask.other_taxes                27w  false
   171  ny_it201.ask.owes_use_tax               27w  false
   172  ny_it201.ask.other_withholding          22w  false
> *173  $ny_it2                                 26w  ["software_co"]               [ny_it2]
  *174  ny_it2[software_co].state_withheld      27w  700000
  *175  ny_it2[software_co].city_withheld       23w  450000
  *176  ny_it2[software_co].yonkers_withheld    21w  0
>> 177  ny_it201.ask.est_any                    30w  false                         [ny_it201]
   178  ny_it201.ask.abroad                     17w+ false                         (screen 107, ny_filing)
   179  ny_it201.ask.installment                 9w+ false                         (screen 107, ny_filing)
   180  ny_it201.ask.contributions              11w+ false                         (screen 107, ny_filing)
   181  ny_it201.ask.prior_full_year            14w  true
   182  ny_it201.ask.prior_agi_high             14w  false
   183  ny_it201.ask.prior_year_tax             17w  0
   184  ny_it201.ask.late_penalty               21w  false
```
