# Walk: ny01_single_nyc_w2

A single person, 31, who lived in Brooklyn all of 2025 with one job (one Form W-2, $52,000 of wages, New York State and City tax withheld) and nothing else to report.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/ny01_single_nyc_w2.yaml` (extending `01_single_w2`): the built interview (profile `ny`, the federal questions, then the New York ones, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: 1994 (persona)
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
- Answer: the list `acme` (persona)
- Words: prompt 8, help 32. Help begins: “Name each employer once.”

### 23. `person[taxpayer].w2[acme].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 acme

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $52,000.00 (persona)
- Words: prompt 6, help 0

### 24. `person[taxpayer].w2[acme].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 acme

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $5,200.00 (persona)
- Words: prompt 6, help 0

### 25. `person[taxpayer].w2[acme].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 acme

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $3,224.00 (persona)
- Words: prompt 6, help 0

### 26. `person[taxpayer].w2[acme].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 acme

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $52,000.00 (persona)
- Words: prompt 6, help 0

### 27. `person[taxpayer].w2[acme].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 acme

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $754.00 (persona)
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

### 97. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 98. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 38, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 99–103. Tick-boxes `sales_rare`: 5 questions on one screen

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

### 104–105. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your investments?
>
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (23, 24 words) and help (34, 37)

### 106. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 107–112. Tick-boxes `outside_us`: 6 questions on one screen

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

### 113–115. Tick-boxes `rare_credits`: 3 questions on one screen

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

### 116. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 117–119. Tick-boxes `other_taxes`: 3 questions on one screen

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

### 120. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 121. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 122. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 123. `qbi.prior_form`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 124. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 125–126. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 18, labels 21. Behind each box, optional to read: the question's own prompt (26, 20 words) and help (39, 22)

### 127. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

### 128. `ny_it201.ask.state_resident`

**⟶ topic switch**

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Were you (and your spouse, on a joint return) a New York State resident for all of 2025: domiciled in New York State, or keeping a permanent place of abode in New York State for substantially all of the year and spending 184 days or more there?
>
> Answer No:
> - if, though domiciled in New York, you kept no permanent place of abode in New York, kept one outside New York all year and spent 30 days or less in New York, or met the 548-day foreign-presence test (Group A or B)
> - if you were in active military service
> - if your only New York residence was undergraduate student housing

- Offered: Yes / No
- Answer: Yes (background)
- Words: prompt 108, help 74. Help begins: “Residency decides which New York return you file.”

### 129. `ny_it201.ask.city_resident`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Were you (and your spouse, on a joint return) a New York City resident (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025, by the same test with New York City in place of New York State?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 40, help 43. Help begins: “The New York City resident tax applies to full-year City residents; the test is the State test with New York City (the five boroughs) in place of New York State.”

### 130. `ny_it201.ask.special_accrual`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does this apply to you: the person was a New York City nonresident on December 31, 2024, or will be a New York State or City nonresident on January 1, 2026, and has income fixed and determinable in one tax year but reported federally in another (accrued income)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 48, help 50. Help begins: “If you moved into or out of New York City or State around the turn of the year, income earned in one period but reported federally in another (for example a bonus fixed in 2025 but paid in 2026) needs the special accrual rules, which this tool does not apply.”

### 131. `ny_it201.ask.yonkers`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you or your spouse maintain living quarters in Yonkers for any part of 2025, or work in Yonkers while not living there (item D2)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 21. Help begins: “Living quarters or wages in Yonkers bring the Yonkers resident surcharge or nonresident earnings tax, which this tool does not compute.”

### 132. `ny_it201.ask.special_code`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does any New York special condition code (item G) apply to you? Examples: A6 Build America Bond interest, C7 combat zone, D9 death of spouse, E3 or E4 an extension, C2 an installment payment agreement, M4 to M9 a military residence election, Y1.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 43, help 31. Help begins: “Special condition codes mark situations such as Build America Bond interest, a combat zone, a filing extension, an installment agreement or a military residence election; this tool does not handle them.”

### 133. `ny_it201.ask.decedent`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Is this return for a taxpayer (or spouse) who died after December 31, 2024?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 14, help 11. Help begins: “A return for a taxpayer who died is outside this tool.”

### 134. `ny_it201.ask.item_c`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Can you be claimed as a dependent on another taxpayer's federal return? Answer Yes even if the other taxpayer did not claim you (item C).

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 35. Help begins: “Answer Yes if another taxpayer could claim you as a dependent on their federal return, even if they did not.”

### 135. `ny_it201.ask.inflation_check`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you receive an inflation refund check from the New York State Tax Department and include it in federal adjusted gross income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 43. Help begins: “New York mailed inflation refund checks in the fall of 2025.”

### 136. `ny_it201.ask.out_of_state_bond_interest`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you have interest or dividends from bonds of states other than New York or their local governments, or from tax-exempt mutual or money market funds that invest in them, that was not included in federal adjusted gross income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 39, help 27. Help begins: “Interest from municipal bonds of other states (or tax-exempt funds holding them) is exempt federally but taxed by New York; this tool does not compute that addition.”

### 137. `ny_it201.ask.414h`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Are you a public employee of New York State or its local governments who is a member of one of the retirement systems below, with 414(h) retirement contributions shown on a Form W-2?
>
> The retirement systems:
> - the New York State and Local Retirement Systems (the Employees' Retirement System or the Police and Fire Retirement System)
> - the New York State Teachers' Retirement System
> - the Optional Retirement Program, as an employee of the State or City University of New York
> - the New York City Employees' Retirement System, Teachers' Retirement System or Board of Education Retirement System, the New York City Police Pension Fund or the NYC Fire Department Pension Fund
> - the Manhattan and Bronx Surface Transit Operating Authority (MABSTOA) Pension Plan
>
> Do not count contributions to a 401(k), 403(b) or 457 plan.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 130, help 23. Help begins: “Members of these New York public retirement systems add back 414(h) contributions shown on Form W-2; this tool does not compute that addition.”

### 138. `ny_it201.ask.529_nonqualified`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you make a withdrawal during 2025 from an account under New York's 529 college savings program that is nonqualified for New York?
>
> A withdrawal is nonqualified for New York unless it was used:
> - for the beneficiary's qualified higher education expenses at an eligible college or other post-secondary institution
> - for the beneficiary's qualified postsecondary credentialing expenses at an eligible educational institution, on or after July 4, 2025
> - to pay principal or interest on a qualified education loan of the beneficiary or the beneficiary's sibling
> - for a rollover to a Roth IRA or to an ABLE account
> - for any purpose, if the withdrawal is the result of the beneficiary's death or disability
>
> Answer Yes for a withdrawal used for elementary or secondary school tuition, or for a transfer to another state's 529 program: New York treats these as nonqualified although they are qualified federally. A transfer between family members' accounts within New York's program, not paid out, is not a withdrawal.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 160, help 45. Help begins: “New York's list of qualified uses is narrower than the federal one, so a withdrawal that is tax-free federally can still be nonqualified for New York.”

### 139. `ny_it201.ask.it225`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does any other New York addition or subtraction on Form IT-225 apply to you, for example modifications passed through from a partnership, S corporation, estate or trust, the disability income exclusion (S-124), combat pay (S-118), a net operating loss (A-215) or an accumulation distribution reported on federal Form 4970?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 49, help 28. Help begins: “Form IT-225 holds the New York modifications not printed on Form IT-201 (many come from a partnership, S corporation, estate or trust); this tool does not compute them.”

### 140. `ny_it201.ask.529_owner`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> During 2025, did you, as an account owner, contribute to or withdraw from a New York 529 college savings account, or, as a beneficiary, receive a withdrawal included in federal adjusted gross income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 33, help 21. Help begins: “Contributions to a New York 529 account are deductible up to $5,000 ($10,000 joint); this tool does not compute the deduction.”

### 141. `ny_it201.ask.itemize`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Is your New York itemized deduction (Form IT-196) larger than your New York standard deduction, or are you married filing separately with a spouse who itemizes on their New York return?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 31, help 28. Help begins: “This tool takes the New York standard deduction.”

### 142. `ny_it201.ask.resident_credit`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you have income from sources outside New York State and pay income tax on it to another state, a local government of another state, the District of Columbia or a province of Canada?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 34, help 23. Help begins: “Tax paid to another state on income from there earns a New York resident credit (Form IT-112-R), which this tool does not compute.”

### 143. `ny_it201.ask.other_credits`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Are you claiming any other New York State nonrefundable or refundable credit on Form IT-201-ATT (for example long-term care insurance, investment, solar energy, farmers' school tax or claim of right)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 30, help 28. Help begins: “Other New York credits are claimed on their own forms and Form IT-201-ATT; this tool computes only the household credits and the New York City school tax credit.”

### 144. `ny_it201.ask.other_taxes`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Do you owe any other New York State or City tax on Form IT-201-ATT, for example the separate tax on a lump-sum distribution (Form IT-230)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 23. Help begins: “Other New York taxes (for example on a lump-sum distribution, Form IT-230) are reported on Form IT-201-ATT; this tool does not compute them.”

### 145. `ny_it201.ask.city_credits`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Can you claim the New York City unincorporated business tax credit, the New York City accumulation distribution credit, or the part-year resident New York City child and dependent care credit?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 30, help 16. Help begins: “These New York City credits are claimed on Form IT-201-ATT; this tool does not compute them.”

### 146. `ny_it201.ask.owes_use_tax`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Do you owe New York sales or use tax on purchases made without paying New York tax (for example online, by catalog, or out of state and brought into New York)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 31, help 38. Help begins: “Line 59 cannot be left blank.”

### 147. `ny_it201.ask.contributions`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Do you want to make voluntary contributions to the funds listed on Form IT-227?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 14, help 12. Help begins: “Voluntary contributions to the funds on Form IT-227 are outside this tool.”

### 148. `ny_it201.ask.noncustodial`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you make child support payments payable through a New York State Support Collection Unit?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 15, help 26. Help begins: “Paying child support through a New York Support Collection Unit may earn the noncustodial parent earned income credit (Form IT-209), which this tool does not compute.”

### 149. `ny_it201.ask.real_property_credit`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Might you qualify for the New York real property tax credit for homeowners and renters (Form IT-214)? It is limited to households with low income that paid real property taxes or rent; if unsure, read the Form IT-214 instructions before answering.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 41, help 22. Help begins: “The real property tax credit (Form IT-214) is for homeowners and renters with low household income; this tool does not compute it.”

### 150. `ny_it201.ask.college_tuition`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you, your spouse or any dependent pay college tuition expenses during 2025?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 20. Help begins: “College tuition paid may earn a New York credit or itemized deduction (Form IT-272); this tool does not compute it.”

### 151. `ny_it201.ask.other_withholding`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Was any New York State, City or Yonkers tax withheld from a pension, annuity or IRA payment (Form 1099-R), unemployment or other government payment (Form 1099-G) or gambling winnings (Form W-2G)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 31, help 10. Help begins: “This tool totals New York withholding from Forms W-2 only.”

### 152. `$ny_it2`

**⟶ topic switch**

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`)

> Which Forms W-2 did you receive? List each Form W-2, one entry per form, even a W-2 that shows no New York wages or tax.

- Offered: a list the filer builds, naming each entry
- Answer: the list `acme` (persona)
- Words: prompt 25, help 33. Help begins: “One record per Form W-2 you received (Form IT-2), even if it shows no New York wages or tax; labelling them as you labelled your federal Forms W-2 makes them easier to match.”

### 153. `ny_it2[acme].state_withheld`

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`), line 17a. About: ny_it2 acme

> For this Form W-2 (Form IT-2, W-2 record) — New York State income tax withheld on this Form W-2 (box 17 for New York State; 0 if none)

- Offered: a dollar amount, zero or more
- Answer: $2,800.00 (persona)
- Words: prompt 27, help 20. Help begins: “Box 17 of the Form W-2, the state income tax withheld, where box 15 shows NY.”

### 154. `ny_it2[acme].yonkers_withheld`

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`), line 19 (Yonkers). About: ny_it2 acme

> For this Form W-2 (Form IT-2, W-2 record) — Form W-2 box 19, local income tax withheld for Yonkers (0 if none)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 21, help 21. Help begins: “Box 19 of the Form W-2 where box 20 shows Yonkers.”

### 155. `ny_it2[acme].city_withheld`

Topic: Form IT-2 (2025), Summary of W-2 Statements — one record per Form W-2 (`ny_it2`), line 19. About: ny_it2 acme

> For this Form W-2 (Form IT-2, W-2 record) — Form W-2 box 19, local income tax withheld for New York City (0 if none)

- Offered: a dollar amount, zero or more
- Answer: $1,900.00 (persona)
- Words: prompt 23, help 23. Help begins: “Box 19 of the Form W-2, the local income tax withheld, where box 20 shows New York City (NYC).”

### 156. `ny_it201.line75`

**⟶ topic switch (returns)**

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`), line 75

> The total of your (and, on a joint return, your spouse's) 2025 New York State, New York City, Yonkers and MCTMT estimated tax payments (including the last installment even if paid in 2026), any 2024 overpayment applied to 2025 estimated tax (as adjusted by the Tax Department), any estimated tax allocated to you by an estate or trust, and any amount paid with Form IT-370; do not include New York City unincorporated business tax payments

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 75, help 34. Help begins: “Include all 2025 New York estimated tax payments (including the last installment paid in 2026), any 2024 overpayment applied to 2025, and any amount paid with an extension (Form IT-370).”

### 157. `ny_it201.ask.prior_agi_high`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Was your 2024 New York adjusted gross income (on your 2024 return) more than $150,000 ($75,000 if you are married filing separately for 2025)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 25. Help begins: “Above $150,000 ($75,000 married filing separately) of 2024 New York adjusted gross income, the safe harbor is 110% of the 2024 tax instead of 100%.”

### 158. `ny_it201.ask.prior_year_tax`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> What was your 2024 New York State and City income tax (the tax shown on your 2024 return, based on a 12-month return)?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 23, help 57. Help begins: “Used only for the estimated tax penalty check: with a balance due, New York charges no penalty if your 2025 withholding and estimated payments were at least 100% of your 2024 New York tax (110% if your 2024 New York AGI was over $150,000).”

### 159. `ny_it201.ask.prior_full_year`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you file a 2024 New York return covering a full 12 months?

- Offered: Yes / No
- Answer: Yes (background)
- Words: prompt 13, help 27. Help begins: “Without a 2024 New York return covering 12 months there is no prior-year safe harbor for the estimated tax penalty, so a balance due is refused here.”

### 160. `ny_it201.ask.late_penalty`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Are you filing late or paying late, so that you owe a late filing or late payment penalty or interest?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 20, help 12. Help begins: “Late filing or late payment penalties and interest are outside this tool.”

## The end reached

**Complete.** The return is completed after 160 questions.

## Totals

| | |
|---|---|
| Questions asked | 160 |
| Steps (screens; a tick-box group shown together is one) | 92 |
| Answered by the persona / by the background / opened and unanswered | 19 / 141 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 3057 |
| Help words (optional to read) | 4089 |
| Words of the answers offered (Yes and No not counted) | 105 |
| Questions answered no, zero or none | 143 |
| Topics met | 32 |
| New York stretch (questions of New York forms): questions / steps / prompt words / help words | 33 / 33 / 1282 / 950 |
| Topic switches | 61 |
| of them, returns to a topic already left | 30 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 138 | `ny_it201.ask.529_nonqualified` | 160 | No |
| 137 | `ny_it201.ask.414h` | 130 | No |
| 128 | `ny_it201.ask.state_resident` | 108 | Yes |
| 156 | `ny_it201.line75` | 75 | $0.00 |
| 139 | `ny_it201.ask.it225` | 49 | No |
| 130 | `ny_it201.ask.special_accrual` | 48 | No |
| 132 | `ny_it201.ask.special_code` | 43 | No |
| 149 | `ny_it201.ask.real_property_credit` | 41 | No |
| 129 | `ny_it201.ask.city_resident` | 40 | Yes |
| 136 | `ny_it201.ask.out_of_state_bond_interest` | 39 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                    6w  ["taxpayer"]                  [person]
> *  2  f1040.status                               9w  "single"                      [f1040]
>    3  household.ever_married                     5w  false                         [household]
     4  household.community_property              20w  false
>>*  5  person[taxpayer].birth_year                6w  1994                          [person]
>    6  sa.dependent                              15w  false                         [sa]
>>   7  person[taxpayer].blind                    25w  false                         [person]
>    8  scope.noncitizen                          16w+ false                         [scope]  (screen 8, about_you)
     9  scope.under24                              7w+ false                         (screen 8, about_you)
    10  scope.armed_forces                        12w+ false                         (screen 8, about_you)
>>  11  sa.excluded_income                        12w+ false                         [sa]  (screen 8, about_you)
>>  12  scope.chapter11                           11w+ false                         [scope]  (screen 8, about_you)
>   13  s3.disability_retired                      8w  false                         [s3]
>   14  $dependent                                30w  []                            [dependent]
>>  15  s3.adoption_any                           19w+ false                         [s3]  (screen 11, child_extras)
>>  16  scope.f8814                               11w+ false                         [scope]  (screen 11, child_extras)
    17  scope.rental                              19w+ false                         (screen 12, own_income)
    18  scope.k1                                  12w+ false                         (screen 12, own_income)
    19  scope.farm                                 6w+ false                         (screen 12, own_income)
>>  20  person[taxpayer].rrta                     13w+ false                         [person]  (screen 13, work_kind)
    21  person[taxpayer].eligible_educator        11w+ false                         (screen 13, work_kind)
> * 22  $w2@person[taxpayer]                       8w  ["acme"]                      [w2]
  * 23  person[taxpayer].w2[acme].box1             6w  5200000
  * 24  person[taxpayer].w2[acme].box2             6w  520000
  * 25  person[taxpayer].w2[acme].box4             6w  322400
  * 26  person[taxpayer].w2[acme].box5             6w  5200000
  * 27  person[taxpayer].w2[acme].box6             5w  75400
> * 28  s2.w2_marks                               22w+ false                         [s2]  (screen 20, w2_jobs)
> * 29  s1.nqdc_pension                           12w+ false                         [s1]  (screen 20, w2_jobs)
>>* 30  scope.w2_marks                            10w+ false                         [scope]  (screen 20, w2_jobs)
  * 31  scope.artist_official                     12w+ false                         (screen 20, w2_jobs)
  * 32  scope.excess_deferral                     12w+ false                         (screen 20, w2_jobs)
    33  scope.pay_no_w2                           24w+ false                         (screen 21, other_pay)
    34  scope.medicaid_waiver                     11w+ false                         (screen 21, other_pay)
    35  scope.religious_work                      12w+ false                         (screen 21, other_pay)
>   36  f8959.territory_w2                        10w+ false                         [f8959]  (screen 21, other_pay)
>>  37  s2.options_any                            11w+ false                         [s2]  (screen 21, other_pay)
>   38  s1a.tips                                  12w+ false                         [s1a]  (screen 22, tips_overtime)
    39  s1a.overtime                               2w+ false                         (screen 22, tips_overtime)
>   40  f2441.care                                20w+ false                         [f2441]  (screen 23, care_help)
    41  f2441.benefits                            12w+ false                         (screen 23, care_help)
>>  42  s2.household_help                         12w+ false                         [s2]  (screen 23, care_help)
>>  43  s1.uc_any                                 10w+ true                          [s1]  (screen 24, money_a)
    44  s1.winnings_any                            9w+ false                         (screen 24, money_a)
    45  s1.scholarship_any                         9w+ false                         (screen 24, money_a)
    46  s1.jury_any                                6w+ false                         (screen 24, money_a)
    47  s1.alaska_any                              5w+ false                         (screen 24, money_a)
    48  s1.hobby_any                              11w+ false                         (screen 24, money_a)
    49  s1.uc_paid                                16w  5000000
    50  s1.uc_repaid                              14w  0
    51  s1.uc_unsupported                         21w  false
    52  s1.alimony_any                            16w+ false                         (screen 28, money_b)
    53  s1.cod_any                                11w+ false                         (screen 28, money_b)
    54  s1.ltc_payout                             12w+ false                         (screen 28, money_b)
    55  s1.inmate_wages                           12w+ false                         (screen 28, money_b)
    56  s1.digital_income                         12w+ false                         (screen 28, money_b)
>>  57  scope.recovery                            12w+ false                         [scope]  (screen 28, money_b)
>   58  refund.any                                13w  false                         [refund]
>   59  $retirement@person[taxpayer]              31w  []                            [retirement]
>>  60  person[taxpayer].ira_owner                17w+ false                         [person]  (screen 31, accounts)
    61  person[taxpayer].inherited_account        11w+ false                         (screen 31, accounts)
    62  person[taxpayer].x_edu_account            12w+ false                         (screen 31, accounts)
    63  person[taxpayer].x_archer_excess          11w+ false                         (screen 31, accounts)
>   64  ssb.any                                   23w  false                         [ssb]
>   65  $f8889@person[taxpayer]                   15w  []                            [f8889]
>>  66  scope.disaster_distribution               21w+ false                         [scope]  (screen 34, rare_accounts)
    67  scope.archer_msa                          11w+ false                         (screen 34, rare_accounts)
>>  68  s2.hsa_testing                            11w+ false                         [s2]  (screen 34, rare_accounts)
>>  69  scope.education_recapture                 11w+ false                         [scope]  (screen 34, rare_accounts)
>   70  $f1095a                                   21w  []                            [f1095a]
>>  71  sa.home_owner                             20w+ false                         [sa]  (screen 36, paid_2025)
    72  sa.state_tax_any                          10w+ false                         (screen 36, paid_2025)
    73  sa.state_tax_other_any                    12w+ false                         (screen 36, paid_2025)
    74  sa.personal_property_tax_any              12w+ false                         (screen 36, paid_2025)
    75  sa.gifts                                  11w+ false                         (screen 36, paid_2025)
    76  sa.medical_any                            10w+ false                         (screen 36, paid_2025)
    77  sa.home_other                             21w+ false                         (screen 37, paid_more)
    78  sa.gift_carryover                         12w+ false                         (screen 37, paid_more)
    79  sa.medical_premiums                       12w+ false                         (screen 37, paid_more)
>   80  sd.casualty                               12w+ false                         [sd]  (screen 37, paid_more)
>>  81  sa.estate_tax_income                      19w+ false                         [sa]  (screen 38, rare_deductions)
    82  sa.bond_premium                           12w+ false                         (screen 38, rare_deductions)
    83  sa.debt_instrument_loss                   10w+ false                         (screen 38, rare_deductions)
    84  sa.pension_unrecovered                    11w+ false                         (screen 38, rare_deductions)
    85  sa.impairment_work                        12w+ false                         (screen 38, rare_deductions)
    86  sa.elect_itemize                          16w+ false                         (screen 39, deduction_wishes)
    87  sa.sales_tax_wish                         12w+ false                         (screen 39, deduction_wishes)
>>  88  s1a.carloan                               21w+ false                         [s1a]  (screen 40, home_school)
>>  89  s3.ev                                     11w+ false                         [s3]  (screen 40, home_school)
    90  s3.kerosene                                9w+ false                         (screen 40, home_school)
>   91  f5695.any                                 11w+ false                         [f5695]  (screen 40, home_school)
>   92  f8863.paid                                12w+ false                         [f8863]  (screen 40, home_school)
>   93  sli.any                                    6w+ false                         [sli]  (screen 40, home_school)
>   94  $sc@person[taxpayer]                      34w  []                            [sc]
>>  95  scope.business_before                     25w  false                         [scope]
>   96  $interest                                 21w  []                            [interest]
>   97  div.any                                   21w  false                         [div]
>   98  $sales                                    38w  []                            [sales]
>>  99  sd.sold_other                             25w+ false                         [sd]  (screen 46, sales_rare)
   100  sd.sec1256                                12w+ false                         (screen 46, sales_rare)
   101  sd.condemned                               9w+ false                         (screen 46, sales_rare)
   102  sd.small_business_stock                   12w+ false                         (screen 46, sales_rare)
   103  sd.trader_election                         9w+ false                         (screen 46, sales_rare)
   104  sd.carryover                              20w+ false                         (screen 47, invest_other)
>  105  f4952.has_interest                        12w+ false                         [f4952]  (screen 47, invest_other)
>> 106  s3.foreign_any                            24w  false                         [s3]
>  107  sb.account_any                            27w+ false                         [sb]  (screen 49, outside_us)
   108  sb.asset_any                              11w+ false                         (screen 49, outside_us)
   109  sb.trust_any                               9w+ false                         (screen 49, outside_us)
   110  sb.company_any                            12w+ false                         (screen 49, outside_us)
   111  sb.territory_any                          10w+ false                         (screen 49, outside_us)
>> 112  scope.foreign_shares                      12w+ false                         [scope]  (screen 49, outside_us)
>> 113  s3.credit_bond                            19w+ false                         [s3]  (screen 50, rare_credits)
   114  s3.farmland                                2w+ false                         (screen 50, rare_credits)
   115  s3.repaid_income                          11w+ false                         (screen 50, rare_credits)
   116  s3.prior_other_forms                      25w  false
>> 117  s2.credit_recapture                       20w+ false                         [s2]  (screen 52, other_taxes)
   118  s2.amt_owed                                3w+ false                         (screen 52, other_taxes)
   119  s2.other_tax                               9w+ false                         (screen 52, other_taxes)
>  120  $oi8z                                     21w  []                            [oi8z]
>> 121  scope.reforestation                       22w  false                         [scope]
   122  scope.attorney_fees                       21w  false
>  123  qbi.prior_form                            19w  false                         [qbi]
   124  qbi.coop_patron                           19w  false
>> 125  f1040.withheld_other_any                  29w+ false                         [f1040]  (screen 58, paid_already)
   126  f1040.estimated_any                       10w+ false                         (screen 58, paid_already)
>> 127  s3.line10                                 20w  0                             [s3]
>  128  ny_it201.ask.state_resident              108w  true                          [ny_it201]
  *129  ny_it201.ask.city_resident                40w  true
   130  ny_it201.ask.special_accrual              48w  false
   131  ny_it201.ask.yonkers                      25w  false
   132  ny_it201.ask.special_code                 43w  false
   133  ny_it201.ask.decedent                     14w  false
   134  ny_it201.ask.item_c                       25w  false
   135  ny_it201.ask.inflation_check              22w  false
   136  ny_it201.ask.out_of_state_bond_interest   39w  false
   137  ny_it201.ask.414h                        130w  false
   138  ny_it201.ask.529_nonqualified            160w  false
   139  ny_it201.ask.it225                        49w  false
   140  ny_it201.ask.529_owner                    33w  false
   141  ny_it201.ask.itemize                      31w  false
   142  ny_it201.ask.resident_credit              34w  false
   143  ny_it201.ask.other_credits                30w  false
   144  ny_it201.ask.other_taxes                  25w  false
   145  ny_it201.ask.city_credits                 30w  false
   146  ny_it201.ask.owes_use_tax                 31w  false
   147  ny_it201.ask.contributions                14w  false
   148  ny_it201.ask.noncustodial                 15w  false
   149  ny_it201.ask.real_property_credit         41w  false
   150  ny_it201.ask.college_tuition              13w  false
   151  ny_it201.ask.other_withholding            31w  false
> *152  $ny_it2                                   25w  ["acme"]                      [ny_it2]
  *153  ny_it2[acme].state_withheld               27w  280000
  *154  ny_it2[acme].yonkers_withheld             21w  0
  *155  ny_it2[acme].city_withheld                23w  190000
>> 156  ny_it201.line75                           75w  0                             [ny_it201]
   157  ny_it201.ask.prior_agi_high               24w  false
   158  ny_it201.ask.prior_year_tax               23w  0
   159  ny_it201.ask.prior_full_year              13w  true
   160  ny_it201.ask.late_penalty                 20w  false
```
