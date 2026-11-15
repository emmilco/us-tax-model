# Walk: 10_homeowner_solar_heat_pump

A single homeowner, 52, with wages from one job, who had solar panels and a heat pump installed at her home in 2025.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/10_homeowner_solar_heat_pump.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: 1973 (persona)
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

### 8–11. Tick-boxes `about_you`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Schedule A — supported itemized deductions and standard comparison (`sa`)

> Is any of these true of you?
>
> - [ ] Not a U.S. citizen at some time in 2025  (`scope.noncitizen`)
> - [ ] In the U.S. armed forces, reserves or National Guard since January 2022  (`scope.armed_forces`)
> - [ ] Leaving out income earned abroad, in Puerto Rico or in American Samoa  (`sa.excluded_income`)
> - [ ] In a chapter 11 bankruptcy case at some time in 2025  (`scope.chapter11`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 44. Behind each box, optional to read: the question's own prompt (11, 19, 26, 13 words) and help (0, 0, 36, 25)

### 12. `s3.disability_retired`

**⟶ topic switch**

Topic: Schedule 3 — selected lines (`s3`)

> Have you retired on permanent and total disability?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 8, help 23. Help begins: “Yes if a person under 65 had to stop working because of a condition a doctor expects to last at least a year.”

### 13. `$dependent`

**⟶ topic switch**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`)

> In 2025, did children live with you, or did you support anyone else, such as a parent, another relative or a partner? List each one, or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 30, help 42. Help begins: “Any label you will recognize will do, such as “Child 1”; a name is not needed.”

### 14–15. Tick-boxes `child_extras`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`); Proof-of-concept scope screening (`scope`)

> Does either of these apply to you?
>
> - [ ] Adopted a child, or paid adoption costs, since the start of 2024  (`s3.adoption_any`)
> - [ ] Reporting a child's 2025 interest or dividends on your own return  (`scope.f8814`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 23. Behind each box, optional to read: the question's own prompt (16, 21 words) and help (18, 28)

### 16–18. Tick-boxes `own_income`: 3 questions on one screen

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you have any of these?
>
> - [ ] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [ ] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 29. Behind each box, optional to read: the question's own prompt (27, 27, 11 words) and help (6, 6, 25)

### 19–20. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did either of these describe your work in 2025?
>
> - [ ] Worked for a railroad  (`person[taxpayer].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[taxpayer].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 15. Behind each box, optional to read: the question's own prompt (8, 30 words) and help (27, 0)

### 21. `$w2@person[taxpayer]`

**⟶ topic switch**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: You

> Which employers gave you a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: the list `utility_co` (persona)
- Words: prompt 8, help 32. Help begins: “Name each employer once.”

### 22. `person[taxpayer].w2[utility_co].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 utility_co

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $84,000.00 (persona)
- Words: prompt 6, help 0

### 23. `person[taxpayer].w2[utility_co].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 utility_co

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $11,000.00 (persona)
- Words: prompt 6, help 0

### 24. `person[taxpayer].w2[utility_co].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 utility_co

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $5,208.00 (persona)
- Words: prompt 6, help 0

### 25. `person[taxpayer].w2[utility_co].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 utility_co

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $84,000.00 (persona)
- Words: prompt 6, help 0

### 26. `person[taxpayer].w2[utility_co].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 utility_co

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $1,218.00 (persona)
- Words: prompt 5, help 0

### 27–31. Tick-boxes `w2_jobs`: 5 questions on one screen

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

### 32–36. Tick-boxes `other_pay`: 5 questions on one screen

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

### 37–38. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 3. Behind each box, optional to read: the question's own prompt (9, 9 words) and help (33, 21)

### 39–41. Tick-boxes `care_help`: 3 questions on one screen

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

### 42–47. Tick-boxes `money_a`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> In 2025, did you get any of these?
>
> - [ ] Unemployment benefits  (`s1.uc_any`)
> - [ ] Gambling or lottery winnings, or a prize or award  (`s1.winnings_any`)
> - [ ] A scholarship, a fellowship or a grant for study  (`s1.scholarship_any`)
> - [ ] Pay for serving on a jury  (`s1.jury_any`)
> - [ ] An Alaska Permanent Fund dividend  (`s1.alaska_any`)
> - [ ] Money from a hobby or pastime not run as a business  (`s1.hobby_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 42. Behind each box, optional to read: the question's own prompt (7, 20, 14, 10, 10, 18 words) and help (7, 17, 14, 0, 0, 0)

### 48–53. Tick-boxes `money_b`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Did any of these happen to you?
>
> - [ ] Alimony paid or received since the start of 2023  (`s1.alimony_any`)
> - [ ] A debt canceled or forgiven by a lender or card company  (`s1.cod_any`)
> - [ ] A long-term care insurance payout, or life insurance paid early, in 2025  (`s1.ltc_payout`)
> - [ ] Pay in 2025 for work done while in a jail or prison  (`s1.inmate_wages`)
> - [ ] Crypto received as pay, as a reward, or from mining or staking  (`s1.digital_income`)
> - [ ] Paid back a deduction that lowered your tax (not a state refund)  (`scope.recovery`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 68. Behind each box, optional to read: the question's own prompt (23, 15, 21, 14, 20, 25 words) and help (22, 18, 11, 6, 21, 60)

### 54. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 55. `$retirement@person[taxpayer]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 31, help 21. Help begins: “List a Form RRB-1099-R too.”

### 56–59. Tick-boxes `accounts`: 4 questions on one screen

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

### 60. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 0

### 61. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 15, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 62–65. Tick-boxes `rare_accounts`: 4 questions on one screen

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

### 66. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 21, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 67–72. Tick-boxes `paid_2025`: 6 questions on one screen

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

### 73–76. Tick-boxes `paid_more`: 4 questions on one screen

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

### 77–81. Tick-boxes `rare_deductions`: 5 questions on one screen

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

### 82–83. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 84–89. Tick-boxes `home_school`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`); Schedule 3 — selected lines (`s3`); Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`); Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits) (`f8863`); Student Loan Interest Deduction Worksheet—Schedule 1, Line 21 (`sli`)

> And in 2025, did you do any of these?
>
> - [ ] Paid interest on a loan for a car bought new in 2025  (`s1a.carloan`)
> - [ ] Got an electric or plug-in vehicle, or installed a home charger  (`s3.ev`)
> - [ ] Used kerosene at home for heat, light or cooking  (`s3.kerosene`)
> - [x] Had solar, insulation, windows, doors or heating equipment installed at home  (`f5695.any`)
> - [ ] Had college or trade school tuition paid, for you or a dependent  (`f8863.paid`)
> - [ ] Paid interest on a student loan  (`sli.any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Had solar, insulation, windows, doors or heating equipment installed at home”; the others recorded No (background; persona)
- Words: heading 9, labels 61. Behind each box, optional to read: the question's own prompt (19, 22, 13, 27, 20, 10 words) and help (37, 19, 0, 34, 32, 18)

### 90–95. Tick-boxes `energy_power`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did the work include any of these for making or storing energy?
>
> - [x] Solar panels that make electricity  (`f5695.solar`)
> - [ ] A solar water heater  (`f5695.solar_water`)
> - [ ] A wind turbine  (`f5695.wind`)
> - [ ] A geothermal (ground-source) heat pump  (`f5695.geothermal`)
> - [ ] A battery storing at least 3 kilowatt hours  (`f5695.line5a`)
> - [ ] A fuel cell at your main home  (`f5695.line7a`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Solar panels that make electricity”; the others recorded No (persona)
- Words: heading 12, labels 32. Behind each box, optional to read: the question's own prompt (8, 7, 6, 8, 14, 10 words) and help (6, 0, 0, 0, 10, 27)

### 96–100. Tick-boxes `energy_shell`: 5 questions on one screen

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did the work include any of these?
>
> - [ ] Insulation or air sealing  (`f5695.insulation`)
> - [ ] Exterior doors  (`f5695.doors`)
> - [ ] Exterior windows or skylights  (`f5695.windows`)
> - [ ] A new or upgraded electrical panel, circuits or wiring  (`f5695.panel`)
> - [ ] A home energy audit paid for in 2025  (`f5695.audit`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 7, labels 27. Behind each box, optional to read: the question's own prompt (7, 5, 7, 12, 10 words) and help (0, 0, 0, 0, 0)

### 101–106. Tick-boxes `energy_heating`: 6 questions on one screen

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did the work include any of this heating, cooling or hot-water equipment?
>
> - [x] A heat pump, electric or gas (not geothermal)  (`f5695.heat_pump`)
> - [ ] A heat pump water heater  (`f5695.hp_water_heater`)
> - [ ] A central air conditioner  (`f5695.central_ac`)
> - [ ] A water heater running on natural gas, propane or oil  (`f5695.water_heater`)
> - [ ] A furnace or hot water boiler running on gas, propane or oil  (`f5695.furnace`)
> - [ ] A stove or boiler burning wood, pellets or other plant fuel  (`f5695.biomass`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “A heat pump, electric or gas (not geothermal)”; the others recorded No (persona)
- Words: heading 12, labels 50. Behind each box, optional to read: the question's own prompt (18, 8, 7, 14, 17, 20 words) and help (0, 0, 0, 0, 0, 0)

### 107. `f5695.business_use`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Is any of these items used more than 20% of the time for a business, for renting out or to earn other income?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 23, help 29. Help begins: “An item used 80% or more for personal purposes counts in full; answer No for it.”

### 108. `f5695.joint_occupancy`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did you share a home where this work was done with another occupant who is not your spouse on this return, such as a housemate, a partner or a co-owner living there?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 32, help 64. Help begins: “This is about insulation, doors, windows, heating, cooling, hot-water and panel work and audits, at your main home or another home.”

### 109. `f5695.construction_later`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Was any of the solar, wind, geothermal or battery equipment put in a home being built or rebuilt that you did not begin to live in during 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 28, help 52. Help begins: “Costs of building or rebuilding a home count in the year you first live in it: equipment put in during 2024 in a new home first lived in in 2025 counts for 2025, and the answer is then No.”

### 110. `f5695.line1`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`), line 1

> What did the solar panels cost, with installation labor, after any rebate or utility subsidy?

- Offered: a dollar amount, zero or more
- Answer: $21,500.00 (persona)
- Words: prompt 15, help 63. Help begins: “Leave out roof decking or rafters, and any part that heats a swimming pool or hot tub.”

### 111. `f5695.line21a`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`), line 21a

> Was the heating, cooling, hot-water or electrical equipment installed at a home in the United States that you live in?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 20, help 9. Help begins: “A second home or a home you rent counts.”

### 112. `f5695.line21b`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`), line 21b

> Was it new, not used by anyone before you?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 9, help 0

### 113. `f5695.b_new_home`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Was any of it installed as part of building a new home, rather than in an existing home, an addition or a renovation?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 23, help 13. Help begins: “A Yes is outside what this tool prepares and ends the interview here.”

### 114. `f5695.line29a`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`), line 29a

> What did the heat pump (the most expensive, if more than one) cost, with installation labor, after any rebate or utility subsidy?

- Offered: a dollar amount, zero or more
- Answer: $9,200.00 (persona)
- Words: prompt 22, help 90. Help begins: “It counts only if it meets the highest efficiency tier of the Consortium for Energy Efficiency (CEE) in effect at the start of 2025; the installer or maker can say.”

### 115. `f5695.line29b`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`), line 29b

> What did the other heat pumps cost together?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 8, help 5. Help begins: “Zero if there was one.”

### 116. `f5695.qmid_hp`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Do you have the four-character manufacturer identification number (QMID) of each heat pump, heat pump water heater and biomass stove or boiler?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 22, help 40. Help begins: “The maker gives this code for each product, and a product installed in 2025 counts only with one.”

### 117. `f5695.condo`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Is any of these costs your share of what a condominium association or housing cooperative paid?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 16, help 11. Help begins: “It changes no amount; a box on the form is checked.”

### 118. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 34, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 119. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 0

### 120. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 121. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 122. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 38, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 123–127. Tick-boxes `sales_rare`: 5 questions on one screen

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

### 128–129. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your investments?
>
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (23, 24 words) and help (34, 37)

### 130. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 131–136. Tick-boxes `outside_us`: 6 questions on one screen

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

### 137–139. Tick-boxes `rare_credits`: 3 questions on one screen

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

### 140. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 141–143. Tick-boxes `other_taxes`: 3 questions on one screen

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

### 144. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 145. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 146. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 147. `qbi.prior_form`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 148. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 149–150. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 18, labels 21. Behind each box, optional to read: the question's own prompt (26, 20 words) and help (39, 22)

### 151. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

## The end reached

**Complete.** The return is completed after 151 questions.

## Totals

| | |
|---|---|
| Questions asked | 151 |
| Steps (screens; a tick-box group shown together is one) | 70 |
| Answered by the persona / by the background / opened and unanswered | 43 / 108 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 2075 |
| Help words (optional to read) | 3509 |
| Words of the answers offered (Yes and No not counted) | 105 |
| Questions answered no, zero or none | 134 |
| Topics met | 30 |
| Topic switches | 59 |
| of them, returns to a topic already left | 30 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 122 | `$sales` | 38 | none (an empty list) |
| 133 | `sb.trust_any` (its own prompt, behind a tick-box) | 38 | No |
| 124 | `sd.sec1256` (its own prompt, behind a tick-box) | 36 | No |
| 39 | `f2441.care` (its own prompt, behind a tick-box) | 35 | No |
| 69 | `sa.state_tax_other_any` (its own prompt, behind a tick-box) | 34 | No |
| 118 | `$sc@person[taxpayer]` | 34 | none (an empty list) |
| 126 | `sd.small_business_stock` (its own prompt, behind a tick-box) | 34 | No |
| 73 | `sa.home_other` (its own prompt, behind a tick-box) | 33 | No |
| 123 | `sd.sold_other` (its own prompt, behind a tick-box) | 33 | No |
| 78 | `sa.bond_premium` (its own prompt, behind a tick-box) | 32 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                 6w  ["taxpayer"]                  [person]
> *  2  f1040.status                            9w  "single"                      [f1040]
>    3  household.ever_married                  5w  false                         [household]
     4  household.community_property           20w  false
>>*  5  person[taxpayer].birth_year             6w  1973                          [person]
>    6  sa.dependent                           15w  false                         [sa]
>>   7  person[taxpayer].blind                 25w  false                         [person]
>    8  scope.noncitizen                       16w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                     12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                     12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                        11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                   8w  false                         [s3]
>   13  $dependent                             30w  []                            [dependent]
>>  14  s3.adoption_any                        19w+ false                         [s3]  (screen 11, child_extras)
>>  15  scope.f8814                            11w+ false                         [scope]  (screen 11, child_extras)
    16  scope.rental                           19w+ false                         (screen 12, own_income)
    17  scope.k1                               12w+ false                         (screen 12, own_income)
    18  scope.farm                              6w+ false                         (screen 12, own_income)
>>  19  person[taxpayer].rrta                  13w+ false                         [person]  (screen 13, work_kind)
    20  person[taxpayer].eligible_educator     11w+ false                         (screen 13, work_kind)
> * 21  $w2@person[taxpayer]                    8w  ["utility_co"]                [w2]
  * 22  person[taxpayer].w2[utility_co].box1    6w  8400000
  * 23  person[taxpayer].w2[utility_co].box2    6w  1100000
  * 24  person[taxpayer].w2[utility_co].box4    6w  520800
  * 25  person[taxpayer].w2[utility_co].box5    6w  8400000
  * 26  person[taxpayer].w2[utility_co].box6    5w  121800
> * 27  s2.w2_marks                            22w+ false                         [s2]  (screen 20, w2_jobs)
> * 28  s1.nqdc_pension                        12w+ false                         [s1]  (screen 20, w2_jobs)
>>* 29  scope.w2_marks                         10w+ false                         [scope]  (screen 20, w2_jobs)
  * 30  scope.artist_official                  12w+ false                         (screen 20, w2_jobs)
  * 31  scope.excess_deferral                  12w+ false                         (screen 20, w2_jobs)
    32  scope.pay_no_w2                        24w+ false                         (screen 21, other_pay)
    33  scope.medicaid_waiver                  11w+ false                         (screen 21, other_pay)
    34  scope.religious_work                   12w+ false                         (screen 21, other_pay)
>   35  f8959.territory_w2                     10w+ false                         [f8959]  (screen 21, other_pay)
>>  36  s2.options_any                         11w+ false                         [s2]  (screen 21, other_pay)
>   37  s1a.tips                               12w+ false                         [s1a]  (screen 22, tips_overtime)
    38  s1a.overtime                            2w+ false                         (screen 22, tips_overtime)
>   39  f2441.care                             20w+ false                         [f2441]  (screen 23, care_help)
    40  f2441.benefits                         12w+ false                         (screen 23, care_help)
>>  41  s2.household_help                      12w+ false                         [s2]  (screen 23, care_help)
>>  42  s1.uc_any                              10w+ false                         [s1]  (screen 24, money_a)
    43  s1.winnings_any                         9w+ false                         (screen 24, money_a)
    44  s1.scholarship_any                      9w+ false                         (screen 24, money_a)
    45  s1.jury_any                             6w+ false                         (screen 24, money_a)
    46  s1.alaska_any                           5w+ false                         (screen 24, money_a)
    47  s1.hobby_any                           11w+ false                         (screen 24, money_a)
    48  s1.alimony_any                         16w+ false                         (screen 25, money_b)
    49  s1.cod_any                             11w+ false                         (screen 25, money_b)
    50  s1.ltc_payout                          12w+ false                         (screen 25, money_b)
    51  s1.inmate_wages                        12w+ false                         (screen 25, money_b)
    52  s1.digital_income                      12w+ false                         (screen 25, money_b)
>>  53  scope.recovery                         12w+ false                         [scope]  (screen 25, money_b)
>   54  refund.any                             13w  false                         [refund]
>   55  $retirement@person[taxpayer]           31w  []                            [retirement]
>>  56  person[taxpayer].ira_owner             17w+ false                         [person]  (screen 28, accounts)
    57  person[taxpayer].inherited_account     11w+ false                         (screen 28, accounts)
    58  person[taxpayer].x_edu_account         12w+ false                         (screen 28, accounts)
    59  person[taxpayer].x_archer_excess       11w+ false                         (screen 28, accounts)
>   60  ssb.any                                23w  false                         [ssb]
>   61  $f8889@person[taxpayer]                15w  []                            [f8889]
>>  62  scope.disaster_distribution            21w+ false                         [scope]  (screen 31, rare_accounts)
    63  scope.archer_msa                       11w+ false                         (screen 31, rare_accounts)
>>  64  s2.hsa_testing                         11w+ false                         [s2]  (screen 31, rare_accounts)
>>  65  scope.education_recapture              11w+ false                         [scope]  (screen 31, rare_accounts)
>   66  $f1095a                                21w  []                            [f1095a]
>>  67  sa.home_owner                          20w+ false                         [sa]  (screen 33, paid_2025)
    68  sa.state_tax_any                       10w+ false                         (screen 33, paid_2025)
    69  sa.state_tax_other_any                 12w+ false                         (screen 33, paid_2025)
    70  sa.personal_property_tax_any           12w+ false                         (screen 33, paid_2025)
    71  sa.gifts                               11w+ false                         (screen 33, paid_2025)
    72  sa.medical_any                         10w+ false                         (screen 33, paid_2025)
    73  sa.home_other                          21w+ false                         (screen 34, paid_more)
    74  sa.gift_carryover                      12w+ false                         (screen 34, paid_more)
    75  sa.medical_premiums                    12w+ false                         (screen 34, paid_more)
>   76  sd.casualty                            12w+ false                         [sd]  (screen 34, paid_more)
>>  77  sa.estate_tax_income                   19w+ false                         [sa]  (screen 35, rare_deductions)
    78  sa.bond_premium                        12w+ false                         (screen 35, rare_deductions)
    79  sa.debt_instrument_loss                10w+ false                         (screen 35, rare_deductions)
    80  sa.pension_unrecovered                 11w+ false                         (screen 35, rare_deductions)
    81  sa.impairment_work                     12w+ false                         (screen 35, rare_deductions)
    82  sa.elect_itemize                       16w+ false                         (screen 36, deduction_wishes)
    83  sa.sales_tax_wish                      12w+ false                         (screen 36, deduction_wishes)
>>  84  s1a.carloan                            21w+ false                         [s1a]  (screen 37, home_school)
>>  85  s3.ev                                  11w+ false                         [s3]  (screen 37, home_school)
    86  s3.kerosene                             9w+ false                         (screen 37, home_school)
> * 87  f5695.any                              11w+ true                          [f5695]  (screen 37, home_school)
>   88  f8863.paid                             12w+ false                         [f8863]  (screen 37, home_school)
>   89  sli.any                                 6w+ false                         [sli]  (screen 37, home_school)
>>* 90  f5695.solar                            17w+ true                          [f5695]  (screen 38, energy_power)
  * 91  f5695.solar_water                       4w+ false                         (screen 38, energy_power)
  * 92  f5695.wind                              3w+ false                         (screen 38, energy_power)
  * 93  f5695.geothermal                        5w+ false                         (screen 38, energy_power)
  * 94  f5695.line5a                            8w+ false                         (screen 38, energy_power)
  * 95  f5695.line7a                            7w+ false                         (screen 38, energy_power)
  * 96  f5695.insulation                       11w+ false                         (screen 39, energy_shell)
  * 97  f5695.doors                             2w+ false                         (screen 39, energy_shell)
  * 98  f5695.windows                           4w+ false                         (screen 39, energy_shell)
  * 99  f5695.panel                             9w+ false                         (screen 39, energy_shell)
  *100  f5695.audit                             8w+ false                         (screen 39, energy_shell)
  *101  f5695.heat_pump                        20w+ true                          (screen 40, energy_heating)
  *102  f5695.hp_water_heater                   5w+ false                         (screen 40, energy_heating)
  *103  f5695.central_ac                        4w+ false                         (screen 40, energy_heating)
  *104  f5695.water_heater                     10w+ false                         (screen 40, energy_heating)
  *105  f5695.furnace                          12w+ false                         (screen 40, energy_heating)
  *106  f5695.biomass                          11w+ false                         (screen 40, energy_heating)
  *107  f5695.business_use                     23w  false
  *108  f5695.joint_occupancy                  32w  false
  *109  f5695.construction_later               28w  false
  *110  f5695.line1                            15w  2150000
  *111  f5695.line21a                          20w  true
  *112  f5695.line21b                           9w  true
  *113  f5695.b_new_home                       23w  false
  *114  f5695.line29a                          22w  920000
  *115  f5695.line29b                           8w  0
  *116  f5695.qmid_hp                          22w  true
  *117  f5695.condo                            16w  false
>  118  $sc@person[taxpayer]                   34w  []                            [sc]
>> 119  scope.business_before                  25w  false                         [scope]
>  120  $interest                              21w  []                            [interest]
>  121  div.any                                21w  false                         [div]
>  122  $sales                                 38w  []                            [sales]
>> 123  sd.sold_other                          25w+ false                         [sd]  (screen 57, sales_rare)
   124  sd.sec1256                             12w+ false                         (screen 57, sales_rare)
   125  sd.condemned                            9w+ false                         (screen 57, sales_rare)
   126  sd.small_business_stock                12w+ false                         (screen 57, sales_rare)
   127  sd.trader_election                      9w+ false                         (screen 57, sales_rare)
   128  sd.carryover                           20w+ false                         (screen 58, invest_other)
>  129  f4952.has_interest                     12w+ false                         [f4952]  (screen 58, invest_other)
>> 130  s3.foreign_any                         24w  false                         [s3]
>  131  sb.account_any                         27w+ false                         [sb]  (screen 60, outside_us)
   132  sb.asset_any                           11w+ false                         (screen 60, outside_us)
   133  sb.trust_any                            9w+ false                         (screen 60, outside_us)
   134  sb.company_any                         12w+ false                         (screen 60, outside_us)
   135  sb.territory_any                       10w+ false                         (screen 60, outside_us)
>> 136  scope.foreign_shares                   12w+ false                         [scope]  (screen 60, outside_us)
>> 137  s3.credit_bond                         19w+ false                         [s3]  (screen 61, rare_credits)
   138  s3.farmland                             2w+ false                         (screen 61, rare_credits)
   139  s3.repaid_income                       11w+ false                         (screen 61, rare_credits)
   140  s3.prior_other_forms                   25w  false
>> 141  s2.credit_recapture                    20w+ false                         [s2]  (screen 63, other_taxes)
   142  s2.amt_owed                             3w+ false                         (screen 63, other_taxes)
   143  s2.other_tax                            9w+ false                         (screen 63, other_taxes)
>  144  $oi8z                                  21w  []                            [oi8z]
>> 145  scope.reforestation                    22w  false                         [scope]
   146  scope.attorney_fees                    21w  false
>  147  qbi.prior_form                         19w  false                         [qbi]
   148  qbi.coop_patron                        19w  false
>> 149  f1040.withheld_other_any               29w+ false                         [f1040]  (screen 69, paid_already)
   150  f1040.estimated_any                    10w+ false                         (screen 69, paid_already)
>> 151  s3.line10                              20w  0                             [s3]
```
