# Walk: 13_self_employed_actual_vehicle_computer

A single self-employed graphic designer, 38, with one business, an office in her home, a van she bought new in 2025 and deducts by its actual costs, and a computer bought new in 2025.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/13_self_employed_actual_vehicle_computer.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: 1987 (persona)
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
- Answer: none (an empty list) (background)
- Words: prompt 8, help 32. Help begins: “Name each employer once.”

### 22–26. Tick-boxes `other_pay`: 5 questions on one screen

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

### 27–28. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 3. Behind each box, optional to read: the question's own prompt (9, 9 words) and help (33, 21)

### 29–31. Tick-boxes `care_help`: 3 questions on one screen

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

### 32–37. Tick-boxes `money_a`: 6 questions on one screen

**⟶ topic switch**

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

### 38–43. Tick-boxes `money_b`: 6 questions on one screen

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

### 44. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 45. `$retirement@person[taxpayer]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 31, help 21. Help begins: “List a Form RRB-1099-R too.”

### 46–49. Tick-boxes `accounts`: 4 questions on one screen

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

### 50. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 0

### 51. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 15, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 52–55. Tick-boxes `rare_accounts`: 4 questions on one screen

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

### 56. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 21, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 57–62. Tick-boxes `paid_2025`: 6 questions on one screen

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

### 63–66. Tick-boxes `paid_more`: 4 questions on one screen

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

### 67–71. Tick-boxes `rare_deductions`: 5 questions on one screen

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

### 72–73. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 74–79. Tick-boxes `home_school`: 6 questions on one screen

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

### 80. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: the list `design_studio` (persona)
- Words: prompt 34, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 81. `person[taxpayer].sc[design_studio].line1`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 1. About: You › sc design_studio

> How much did this business take in during 2025, before any expenses? Count everything customers paid, including amounts on Forms 1099-NEC and 1099-K.

- Offered: a dollar amount, zero or more
- Answer: $88,000.00 (persona)
- Words: prompt 23, help 39. Help begins: “Include sales tax you collected from customers if the tax was charged to you as the seller.”

### 82. `person[taxpayer].sc[design_studio].line2`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 2. About: You › sc design_studio

> How much of that did this business give back to customers in 2025 as refunds or price reductions?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 18, help 0

### 83. `person[taxpayer].sc[design_studio].line6`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 6. About: You › sc design_studio

> How much other income did this business have in 2025, such as interest customers paid on their accounts, old debts recovered, prizes, scrap sales or a fuel tax refund?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 29, help 28. Help begins: “Count here too a fuel tax credit claimed on your 2024 return, sales tax a state let you keep, and amounts on a Form 1099-PATR from a cooperative.”

### 84. `person[taxpayer].sc[design_studio].tips_ot`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> Does the income of this business include tips from customers, or overtime pay reported to you on Form 1099-NEC or 1099-MISC, that you want to deduct as tips or overtime?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 30, help 0

### 85–88. Tick-boxes `biz_refused`: 4 questions on one screen

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Is any of these true of it?
>
> - [ ] Owned jointly by a husband and wife  (`person[taxpayer].sc[design_studio].spouse_owned`)
> - [ ] Its income is from a “statutory employee” W-2 job, or notary fees  (`person[taxpayer].sc[design_studio].statutory`)
> - [ ] It claims a business tax credit, such as for research  (`person[taxpayer].sc[design_studio].business_credit`)
> - [ ] It wants federal fuel tax back for fuel used off the road  (`person[taxpayer].sc[design_studio].fuel_credit`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 10, labels 41. Behind each box, optional to read: the question's own prompt (11, 26, 26, 30 words) and help (32, 13, 36, 22)

### 89. `person[taxpayer].sc[design_studio].passive`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), G. About: You › sc design_studio

> In 2025, did you yourself do all or most of the work of this business, or work in it more than 500 hours? Answer No for a business of renting out property.

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 32, help 53. Help begins: “Yes also if you worked in it more than 100 hours and at least as much as anyone else, or meet another of the tests of “material participation”, or own a working interest in an oil or gas well directly.”

### 90. `person[taxpayer].sc[design_studio].method_other`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), F. About: You › sc design_studio

> Does any of these apply to how this business keeps its books: a method other than cash or accrual; a change of method in 2025; long-term contracts; a tax shelter; or receipts averaging more than $31 million a year?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 39, help 32. Help begins: “Most small businesses use the cash method (income counted when received, expenses when paid) and have none of these.”

### 91. `person[taxpayer].sc[design_studio].special`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> Does any of these apply to this business?
>
> - it mines, drills or cuts timber and deducts depletion
> - it claims the deduction for energy-saving work on a commercial building (Form 7205)
> - it claims a tax credit for employing certain workers or for their benefits (Forms 5884, 8844, 8846, 8932, 8941 or 8994)
> - its interest deduction is limited by Form 8990
> - equipment or a vehicle written off in an earlier year is now used half or less for the business, or leased property has an “inclusion amount”
> - it has export income excluded as extraterritorial income (Form 8873)
> - it reports sales by the installment method
> - you chose to spread research costs over several years
> - it has a capital construction fund (for fishing or shipping vessels)
> - you paid into a dependent care plan for yourself through the business
> - you chose to deduct the costs of producing a sound recording
> - it has losses of earlier years that the passive activity rules held back
> - you do work in it for a business that employed you within the last 3 years, much the same work as when you were its employee
> - it is a hobby, or an occasional activity not run for profit
> - it received a Form 1099-PATR from a cooperative with amounts not reported as qualified
> - it has a license or other cost that must be written off over several years, such as some liquor licenses
> - it paid for travel by cruise ship or ocean liner
> - it is an LLC you own alone that chose to be taxed as a corporation

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 255, help 13. Help begins: “A Yes is outside what this tool prepares and ends the interview here.”

### 92. `person[taxpayer].sc[design_studio].line8`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 8. About: You › sc design_studio

> How much did this business spend on advertising in 2025?

- Offered: a dollar amount, zero or more
- Answer: $1,100.00 (persona)
- Words: prompt 10, help 0

### 93. `person[taxpayer].sc[design_studio].line11`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 11. About: You › sc design_studio

> How much did this business pay in 2025 to freelancers, subcontractors and other people who were not its employees?

- Offered: a dollar amount, zero or more
- Answer: $4,500.00 (persona)
- Words: prompt 19, help 22. Help begins: “Leave out amounts you count under another expense here, such as legal fees, repairs or labor that went into goods you sell.”

### 94. `person[taxpayer].sc[design_studio].line10`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 10. About: You › sc design_studio

> How much did this business pay in commissions and fees in 2025?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 12, help 0

### 95. `person[taxpayer].sc[design_studio].line18`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 18. About: You › sc design_studio

> How much did this business spend on office supplies and postage in 2025?

- Offered: a dollar amount, zero or more
- Answer: $420.00 (persona)
- Words: prompt 13, help 0

### 96. `person[taxpayer].sc[design_studio].line22`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 22. About: You › sc design_studio

> How much did this business spend in 2025 on supplies and small items it used up within a year, such as materials, tools and books?

- Offered: a dollar amount, zero or more
- Answer: $1,300.00 (persona)
- Words: prompt 25, help 27. Help begins: “Leave out things that last well beyond a year (they are entered as equipment) and materials that went into goods you sell (asked about with those goods).”

### 97. `person[taxpayer].sc[design_studio].line20b`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 20b. About: You › sc design_studio

> How much rent did this business pay in 2025 for space, such as an office, a shop or storage?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 19, help 17. Help begins: “Leave out rent for your home; the question on using your home for the business covers it.”

### 98. `person[taxpayer].sc[design_studio].rent_equipment`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> How much rent did this business pay in 2025 for machinery or equipment, or for a vehicle rented for less than 30 days?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 23, help 18. Help begins: “Only the part for business use.”

### 99. `person[taxpayer].sc[design_studio].line25`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 25. About: You › sc design_studio

> How much did this business spend in 2025 on its own utilities, such as electricity, water and phone service?

- Offered: a dollar amount, zero or more
- Answer: $720.00 (persona)
- Words: prompt 19, help 30. Help begins: “Leave out the utilities of your home (the question on using your home for the business covers them) and the basic charge for the first phone line into your home.”

### 100. `person[taxpayer].sc[design_studio].line15`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 15. About: You › sc design_studio

> How much did this business pay in 2025 for business insurance, such as liability or property insurance?

- Offered: a dollar amount, zero or more
- Answer: $600.00 (persona)
- Words: prompt 17, help 30. Help begins: “Leave out health insurance for yourself, insurance against lost earnings, money set aside to insure yourself, insurance on a vehicle you list for this business, and insurance on your home.”

### 101. `person[taxpayer].sc[design_studio].line17`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 17. About: You › sc design_studio

> How much did this business pay accountants and lawyers in 2025 for work on the business, including preparing its tax forms?

- Offered: a dollar amount, zero or more
- Answer: $850.00 (persona)
- Words: prompt 21, help 0

### 102. `person[taxpayer].sc[design_studio].line23`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 23. About: You › sc design_studio

> How much did this business pay in 2025 in business taxes and licenses, such as sales tax charged to you as the seller, property tax on business assets, yearly license fees, and payroll taxes you paid as an employer?

- Offered: a dollar amount, zero or more
- Answer: $150.00 (persona)
- Words: prompt 39, help 39. Help begins: “Leave out income tax, self-employment tax, sales tax on things you bought, property tax on your home, the license plates of a vehicle you list for this business, and a license whose cost must be spread over several years.”

### 103. `person[taxpayer].sc[design_studio].line21`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 21. About: You › sc design_studio

> How much did this business spend in 2025 on repairs and upkeep of its property and equipment?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 17, help 18. Help begins: “Leave out improvements and replacements, your own labor, a vehicle you list for this business, and your home.”

### 104. `person[taxpayer].sc[design_studio].line16a`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 16a. About: You › sc design_studio

> How much mortgage interest did this business pay in 2025 on a building or land it uses, as shown on a Form 1098 sent to you?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 22. Help begins: “Only the business part.”

### 105. `person[taxpayer].sc[design_studio].line16b`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 16b. About: You › sc design_studio

> How much other interest did this business pay in 2025 on its debts, such as a business loan or credit card?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 21, help 38. Help begins: “Only the business part, and only interest that belongs to 2025.”

### 106. `person[taxpayer].sc[design_studio].line48`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 48. About: You › sc design_studio

> How much did this business spend in 2025 on anything else needed to run it that no question here has asked about?

- Offered: a dollar amount, zero or more
- Answer: $2,400.00 (persona)
- Words: prompt 22, help 29. Help begins: “Vehicles, equipment that lasts more than a year, the use of your home, your own health insurance and your own retirement plan are asked about separately; leave them out.”

### 107–111. Tick-boxes `biz_had`: 5 questions on one screen

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Which of these did it have in 2025?
>
> - [x] Overnight travel, or meals, food or drink it paid for  (`person[taxpayer].sc[design_studio].travel_meals`)
> - [ ] Employees paid wages (not freelancers or contractors)  (`person[taxpayer].sc[design_studio].employees`)
> - [ ] Goods it bought or made to sell, or held for sale  (`person[taxpayer].sc[design_studio].goods`)
> - [x] Part of your home used only for it or storing its stock  (`person[taxpayer].sc[design_studio].ho_uses`)
> - [ ] Health insurance for its owner or the owner's family  (`person[taxpayer].sc[design_studio].hi_uses`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Overnight travel, or meals, food or drink it paid for”, “Part of your home used only for it or storing its stock”; the others recorded No (persona)
- Words: heading 11, labels 49. Behind each box, optional to read: the question's own prompt (16, 16, 25, 30, 27 words) and help (38, 25, 30, 0, 43)

### 112. `person[taxpayer].sc[design_studio].line24a`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 24a. About: You › sc design_studio

> How much did this business spend in 2025 on overnight business travel away from home: transport, lodging, and tips to porters and hotel staff?

- Offered: a dollar amount, zero or more
- Answer: $950.00 (persona)
- Words: prompt 24, help 35. Help begins: “Leave out meals (asked next), entertainment, laundry, phone calls, a work assignment away from home of more than a year, and the costs of a companion who is not your employee traveling for the business.”

### 113. `person[taxpayer].sc[design_studio].meals_50`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> How much did business meals cost in 2025: your meals while traveling overnight for this business, and meals with clients or other business contacts? Give the full cost; half of it is deducted.

- Offered: a dollar amount, zero or more
- Answer: $360.00 (persona)
- Words: prompt 33, help 32. Help begins: “Include travel meals of employees that you paid for.”

### 114. `person[taxpayer].sc[design_studio].meals_80`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> How much did meals cost in 2025 that you or your employees ate while on duty under the Department of Transportation’s hours-of-service limits, such as interstate truck drivers and certain air crews? Give the full cost.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 36, help 0

### 115. `person[taxpayer].sc[design_studio].meals_100`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> How much did this business spend in 2025 on food and drink that is deducted in full: a staff party or picnic, food given to the public to promote the business, meals it sells, meals counted as someone’s pay, meals a client paid you back for, or food for the children in your daycare?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 54, help 34. Help begins: “Meals counted as pay are those treated as an employee’s wages or reported on a contractor’s Form 1099-NEC.”

### 116. `person[taxpayer].sc[design_studio].ho_other`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> Does any of these apply to the part of your home used for this business?
>
> - you want to deduct the actual costs of the home (Form 8829) in place of the flat rate for each square foot
> - you used more than one home for this business
> - the home is used as a daycare
> - the space is shared with another person’s business
> - you used the space for only part of 2025, or it changed during the year
> - some of the income of this business was earned at another place of business
> - you sold property of this business at a gain or a loss (Form 8949 or Form 4797)
> - this return is late, or is an amended return

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 116, help 13. Help begins: “A Yes is outside what this tool prepares and ends the interview here.”

### 117. `person[taxpayer].sc[design_studio].ho_sqft`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 30(b). About: You › sc design_studio

> How many square feet of your home did you use that way for this business throughout 2025?

- Offered: a whole number
- Answer: 180 (persona)
- Words: prompt 17, help 0

### 118. `$scveh@person[taxpayer].sc[design_studio]`

**⟶ topic switch**

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio

> For this business — List each car, truck or van you drove for this business in 2025 and want to deduct costs for, one entry per vehicle; leave the list empty if none.

- Offered: a list the filer builds, naming each entry
- Answer: the list `van` (persona)
- Words: prompt 32, help 17. Help begins: “Driving between your home and your regular place of work is commuting, not driving for the business.”

### 119. `person[taxpayer].sc[design_studio].scveh[van].method`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — How do you want to figure what this vehicle cost the business in 2025?

- Offered: “By the mile: $0.70 for each business mile (the standard mileage rate)” / “By what it actually cost: gas, repairs, insurance and the like, with depreciation or lease payments (actual expenses)”
- Answer: “By what it actually cost: gas, repairs, insurance and the like, with depreciation or lease payments (actual expenses)” (`actual`) (persona)
- Words: prompt 17, help 0

### 120. `person[taxpayer].sc[design_studio].scveh[van].miles_business`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`), line 44a. About: You › sc design_studio › scveh van

> For this vehicle — How many miles did you drive it for this business in 2025? Do not count driving between home and your regular workplace.

- Offered: a whole number
- Answer: 8000 (persona)
- Words: prompt 25, help 0

### 121. `person[taxpayer].sc[design_studio].scveh[van].parking`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — How much did you pay for parking and tolls on business trips in 2025? (Zero if none.)

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 20, help 0

### 122. `person[taxpayer].sc[design_studio].scveh[van].miles_commuting`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`), line 44b. About: You › sc design_studio › scveh van

> For this vehicle — How many miles did you drive it in 2025 between home and your regular workplace (commuting)?

- Offered: a whole number
- Answer: 0 (persona)
- Words: prompt 19, help 0

### 123. `person[taxpayer].sc[design_studio].scveh[van].miles_other`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`), line 44c. About: You › sc design_studio › scveh van

> For this vehicle — How many other miles did you drive it in 2025 (personal driving that is not commuting)?

- Offered: a whole number
- Answer: 2000 (persona)
- Words: prompt 19, help 0

### 124. `person[taxpayer].sc[design_studio].scveh[van].operating`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — How much did it cost to run in 2025 (gas, oil, repairs, insurance, license plates and the like)? Leave out depreciation, lease or rent payments, interest, parking and tolls.

- Offered: a dollar amount, zero or more
- Answer: $3,000.00 (persona)
- Words: prompt 32, help 0

### 125. `person[taxpayer].sc[design_studio].scveh[van].employee_use`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Do any of your employees use it for themselves, including driving it to and from work? (Answer No if they drive it only for your business.)

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 29, help 0

### 126. `person[taxpayer].sc[design_studio].scveh[van].owned`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Do you own it? (Answer No if you lease it.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 13, help 0

### 127. `person[taxpayer].sc[design_studio].scveh[van].placed`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — In what year did you start using it in the business?

- Offered: “2025” / “2024” / “2023” / “2022” / “2021” / “2020” / “2019” / “2018” / “2017” / “2016” / “2015” / “2014” / “2013” / “2012” / “2011” / “2010” / “2009” / “2008” / “2007” / “2006” / “2005”
- Answer: “2025” (`y2025`) (persona)
- Words: prompt 14, help 0

### 128. `person[taxpayer].sc[design_studio].scveh[van].records`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Do you have a mileage log or other records that show how much you drove it for the business?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 22, help 0

### 129. `person[taxpayer].sc[design_studio].scveh[van].got_other`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Did you get this vehicle with a trade-in, in an exchange, as a replacement for one that was destroyed, stolen or condemned, or from a relative or a business you control?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 34, help 22. Help begins: “Depreciation of a vehicle got in one of these ways is outside what this tool prepares; a Yes ends the interview here.”

### 130–134. Tick-boxes `veh_history`: 5 questions on one screen

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Is any of these true of its history?
>
> - [ ] Got before September 28, 2017  (`person[taxpayer].sc[design_studio].scveh[van].acquired_before_bonus_date`)
> - [ ] Changed between personal and business use during 2025  (`person[taxpayer].sc[design_studio].scveh[van].converted`)
> - [ ] Sold, traded in, given away or scrapped in 2025  (`person[taxpayer].sc[design_studio].scveh[van].disposed`)
> - [ ] A major improvement, tax credit, deduction or casualty loss changed its cost  (`person[taxpayer].sc[design_studio].scveh[van].basis_changed`)
> - [ ] A tax year of under 12 months since its business use began  (`person[taxpayer].sc[design_studio].scveh[van].short_year`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 11, labels 46. Behind each box, optional to read: the question's own prompt (11, 31, 16, 35, 26 words) and help (0, 0, 0, 0, 17)

### 135–138. Tick-boxes `veh_use`: 4 questions on one screen

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Is any of these true of how it is used or depreciated?
>
> - [ ] Carries people or goods for pay, or is an ambulance or hearse  (`person[taxpayer].sc[design_studio].scveh[van].for_hire`)
> - [ ] Also used in 2025 to earn income outside the business  (`person[taxpayer].sc[design_studio].scveh[van].investment`)
> - [ ] Used by someone else, or for entertainment  (`person[taxpayer].sc[design_studio].scveh[van].others_use`)
> - [ ] Depreciated by straight line, 150% declining balance or the alternative system (ADS)  (`person[taxpayer].sc[design_studio].scveh[van].method_other`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 15, labels 41. Behind each box, optional to read: the question's own prompt (29, 21, 37, 34 words) and help (0, 0, 0, 14)

### 139. `person[taxpayer].sc[design_studio].scveh[van].cost`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — What did it cost, including sales tax, destination charges and dealer preparation? Do not subtract depreciation or any section 179 deduction.

- Offered: a dollar amount, zero or more
- Answer: $30,000.00 (persona)
- Words: prompt 24, help 39. Help begins: “Subtract any gas guzzler tax.”

### 140. `person[taxpayer].sc[design_studio].scveh[van].passenger`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Is this a passenger automobile subject to the depreciation limits: a 4-wheeled vehicle made mainly for public roads rated at 6,000 pounds unloaded gross vehicle weight or less (for a truck or van, 6,000 pounds gross vehicle weight or less), and not a truck or van specially modified as a qualified nonpersonal use vehicle?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 57, help 0

### 141. `person[taxpayer].sc[design_studio].scveh[van].s179_elect`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — How much of its cost do you choose to deduct at once in 2025 under the section 179 election? (Zero if none.)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 25, help 0

### 142. `person[taxpayer].sc[design_studio].scveh[van].bonus_choice`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — For the vehicles, computers and other 5-year property you began using in 2025, do you take the special ("bonus") depreciation allowance?

- Offered: “Yes: the special depreciation allowance” / “The 40% allowance in place of 100% (an election for property acquired after January 19, 2025)” / “No: I elect not to take any special allowance”
- Answer: “Yes: the special depreciation allowance” (`full`) (persona)
- Words: prompt 24, help 0

### 143. `person[taxpayer].sc[design_studio].scveh[van].after_jan19`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Did you acquire this vehicle after January 19, 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 12, help 0

### 144. `person[taxpayer].sc[design_studio].scveh[van].bonus_same`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Is that choice the same for all 5-year property (vehicles, computers and other 5-year property) that you (and your spouse, on a joint return) placed in service in 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 32, help 0

### 145. `person[taxpayer].sc[design_studio].scveh[van].used_before`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Had anyone used this vehicle before you got it?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 12, help 24. Help begins: “A rebuilt or reconditioned vehicle counts as used, unless the cost of its used parts is not more than 20% of its total cost.”

### 146. `person[taxpayer].sc[design_studio].scveh[van].bonus_excluded`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — Is your business a regulated utility (electricity, water, sewage, gas or steam), or one that finances the vehicles or equipment it holds for sale or lease with a loan secured by them?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 35, help 0

### 147. `person[taxpayer].sc[design_studio].scveh[van].quarter`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh van

> For this vehicle — In which part of 2025 did you start using it in the business?

- Offered: “January to March” / “April to June” / “July to September” / “October to December”
- Answer: “April to June” (`q2`) (persona)
- Words: prompt 16, help 0

### 148. `$asset@person[taxpayer].sc[design_studio]`

**⟶ topic switch**

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio

> For this business — List each piece of equipment, furniture or machinery (anything lasting other than a vehicle) whose cost this business deducts over several years or under the section 179 election, one entry per item; leave the list empty if none. Include items first used from 2005 to 2025.

- Offered: a list the filer builds, naming each entry
- Answer: the list `computer` (persona)
- Words: prompt 49, help 19. Help begins: “Things whose cost you deduct in full as supplies, or under a de minimis rule, are not listed here.”

### 149. `person[taxpayer].sc[design_studio].asset[computer].class`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — What kind of property is it? Choose the description that fits the item; if none does, choose the one that fits what your business does.

- Offered: “A computer, printer or similar equipment (00.12 Information Systems)” / “Office furniture and fixtures, such as desks, chairs, files and safes (00.11)” / “A copier, calculator or similar office machine, not a computer (00.13 Data Handling Equipment)” / “00.21 Airplanes (airframes and engines), except those used in commercial or contract carrying of passengers or freight, and all helicopters (airframes and engines)” / “00.22 Automobiles, Taxis” / “00.23 Buses” / “00.241 Light General Purpose Trucks” / “00.242 Heavy General Purpose Trucks” / “00.25 Railroad Cars and Locomotives, except those owned by railroad transportation companies” / “00.26 Tractor Units for Use Over-the-Road” / “00.27 Trailers and Trailer-Mounted Containers” / “00.28 Vessels, Barges, Tugs, and Similar Water Transportation Equipment, except those used in marine construction” / “00.3 Land Improvements” / “00.4 Industrial Steam and Electric Generation and/or Distribution Systems” / “01.1 Agriculture” / “01.11 Cotton Ginning Assets” / “01.21 Cattle, Breeding or Dairy” / “01.221 Any breeding or work horse that is 12 years old or less at the time it is placed in service2” / “01.222 Any breeding or work horse that is more than 12 years old at the time it is placed in service2” / “01.223 Any race horse that is more than 2 years old at the time it is placed in service2” / “01.224 Any horse that is more than 12 years old at the time it is placed in service and that is neither a race horse nor a horse described in class 01.2222” / “01.225 Any horse not described in class 01.221, 01.222, 01.223, or 01.224” / “01.23 Hogs, Breeding” / “01.24 Sheep and Goats, Breeding” / “01.3 Farm buildings except structures included in class 01.4” / “01.4 Single purpose agricultural or horticultural structures (within the meaning of section 168(i)(13) of the Code)” / “10.0 Mining” / “13.0 Offshore Drilling” / “13.1 Drilling of Oil and Gas Wells” / “13.2 Exploration for and Production of Petroleum and Natural Gas Deposits” / “13.3 Petroleum Refining” / “15.0 Construction” / “20.1 Manufacture of Grain and Grain Mill Products” / “20.2 Manufacture of Sugar and Sugar Products” / “20.3 Manufacture of Vegetable Oils and Vegetable Oil Products” / “20.4 Manufacture of Other Food and Kindred Products” / “20.5 Manufacture of Food and Beverages—Special Handling Devices” / “21.0 Manufacture of Tobacco and Tobacco Products” / “22.1 Manufacture of Knitted Goods” / “22.2 Manufacture of Yarn, Thread, and Woven Fabric” / “22.3 Manufacture of Carpets and Dyeing, Finishing, and Packaging of Textile Products and Manufacture of Medical and Dental Supplies” / “22.4 Manufacture of Textile Yarns” / “22.5 Manufacture of Nonwoven Fabrics” / “23.0 Manufacture of Apparel and Other Finished Products” / “24.1 Cutting of Timber” / “24.2 Sawing of Dimensional Stock From Logs” / “24.3 Sawing of Dimensional Stock From Logs” / “24.4 Manufacture of Wood Products, and Furniture” / “26.1 Manufacture of Pulp and Paper” / “26.2 Manufacture of Converted Paper, Paperboard, and Pulp Products” / “27.0 Printing, Publishing, and Allied Industries” / “28.0 Manufacture of Chemicals and Allied Products” / “30.1 Manufacture of Rubber Products” / “30.11 Manufacture of Rubber Products—Special Tools and Devices” / “30.2 Manufacture of Finished Plastic Products” / “30.21 Manufacture of Finished Plastic Products—Special Tools” / “31.0 Manufacture of Leather and Leather Products” / “32.1 Manufacture of Glass Products” / “32.11 Manufacture of Glass Products—Special Tools” / “32.2 Manufacture of Cement” / “32.3 Manufacture of Other Stone and Clay Products” / “33.2 Manufacture of Primary Nonferrous Metals” / “33.21 Manufacture of Primary Nonferrous Metals—Special Tools” / “33.3 Manufacture of Foundry Products” / “33.4 Manufacture of Primary Steel Mill Products” / “34.0 Manufacture of Fabricated Metal Products” / “34.01 Manufacture of Fabricated Metal Products—Special Tools” / “35.0 Manufacture of Electrical and Non-Electrical Machinery and Other Mechanical Products” / “36.0 Manufacture of Electronic Components, Products, and Systems” / “36.1 Any Semiconductor Manufacturing Equipment” / “37.11 Manufacture of Motor Vehicles” / “37.12 Manufacture of Motor Vehicles—Special Tools” / “37.2 Manufacture of Aerospace Products” / “37.31 Ship and Boat Building Machinery and Equipment” / “37.32 Ship and Boat Building Dry Docks and Land Improvements” / “37.33 Ship and Boat Building—Special Tools” / “37.41 Manufacture of Locomotives” / “37.42 Manufacture of Railroad Cars” / “39.0 Manufacture of Athletic, Jewelry, and Other Goods” / “40.1 Railroad Machinery and Equipment” / “40.2 Railroad Structures and Similar Improvements” / “40.3 Railroad Wharves and Docks” / “40.4 Railroad Track” / “40.51 Railroad Hydraulic Electric Generating Equipment” / “40.52 Railroad Nuclear Electric Generating Equipment” / “40.53 Railroad Steam Electric Generating Equipment” / “40.54 Railroad Steam, Compressed Air, and Other Power Plan Equipment” / “41.0 Motor Transport—Passengers” / “42.0 Motor Transport—Freight” / “44.0 Water Transportation” / “45.0 Air Transport” / “45.1 Air Transport (restricted)” / “46.0 Pipeline Transportation” / “48.11 Telephone Central Office Buildings” / “48.12 Telephone Central Office Equipment” / “48.121 Computer-Based Telephone Central Office Switching Equipment” / “48.13 Telephone Station Equipment” / “48.14 Telephone Distribution Plant” / “48.2 Radio and Television Broadcastings” / “48.31 TOCSC—Electric Power Generating and Distribution Systems” / “48.32 TOCSC—High Frequency Radio and Microwave Systems” / “48.33 TOCSC—Cable and Long-Line Systems” / “48.34 TOCSC—Central Office Control Equipment” / “48.35 TOCSC—Computerized Switching, Channeling, and Associated Control Equipment” / “48.36 TOCSC—Satellite Ground Segment Property” / “48.37 TOCSC—Satellite Space Segment Property” / “48.38 TOCSC—Equipment Installed on Customer’s Premises” / “48.39 TOCSC—Support and Service Equipment” / “48.41 CATV—Headend” / “48.42 CATV—Subscriber Connection and Distribution Systems” / “48.43 CATV—Program Origination” / “48.44 CATV—Service and Test” / “48.45 CATV—Microwave Systems” / “49.11 Electric Utility Hydraulic Production Plant” / “49.12 Electric Utility Nuclear Production Plant” / “49.121 Electric Utility Nuclear Fuel Assemblies” / “49.13 Electric Utility Steam Production Plant” / “49.14 Electric Utility Transmission and Distribution Plant” / “49.15 Electric Utility Combustion Turbine Production Plant” / “49.21 Gas Utility Distribution Facilities” / “49.221 Gas Utility Manufactured Gas Production Plants” / “49.222 Gas Utility Substitute Natural Gas (SNG) Production Plant (naphtha or lighter hydrocarbon feedstocks)” / “49.223 Substitute Natural Gas—Coal Gasification” / “49.23 Natural Gas Production Plant” / “49.24 Gas Utility Trunk Pipelines and Related Storage Facilities: Excluding initial clearing and grading land improvements as specified in Rev. Rul. 72-40.” / “49.25 Liquefied Natural Gas Plant” / “49.3 Water Utilities” / “49.4 Central Steam Utility Production and Distribution” / “49.5 Waste Reduction and Resource Recovery Plants” / “50.0 Municipal Wastewater Treatment Plant” / “51.0 Municipal Sewer” / “57.0 Distributive Trades and Services” / “57.1 Distributive Trades and Services—Billboard, Service Station Buildings, and Petroleum Marketing Land Improvements” / “79.0 Recreation” / “80.0 Theme and Amusement Parks” / “Table B-2, Certain Property for Which Recovery Periods Assigned, A. Personal Property With No Class Life” / “Table B-2, A. Section 1245 Real Property With No Class Life” / “Table B-2, B. Qualified Technological Equipment, as defined in section 168(i)(2)” / “Table B-2, C. Property Used in Connection with Research and Experimentation referred to in section 168(e)(3)(B)” / “Table B-2, D, E and F (alternative energy, biomass and energy property)” / “Qualified improvement property placed in service after 2017 (i4562 p. 10; Pub. 946 Table 4-1)”
- Answer: “A computer, printer or similar equipment (00.12 Information Systems)” (`c00_12`) (persona)
- Words: prompt 28, help 46. Help begins: “These are the asset classes of IRS Publication 946, Appendix B.”

### 150. `person[taxpayer].sc[design_studio].asset[computer].placed`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — In what year did you start using it in the business?

- Offered: “2025” / “2024” / “2023” / “2022” / “2021” / “2020” / “2019” / “2018” / “2017” / “2016” / “2015” / “2014” / “2013” / “2012” / “2011” / “2010” / “2009” / “2008” / “2007” / “2006” / “2005”
- Answer: “2025” (`y2025`) (persona)
- Words: prompt 14, help 55. Help begins: “It counts from the year it was ready and available for use, even if not yet used.”

### 151–154. Tick-boxes `asset_kind`: 4 questions on one screen

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Is it any of these?
>
> - [ ] A building, land, a vehicle, an aircraft, a film or a recording  (`person[taxpayer].sc[design_studio].asset[computer].kind_excluded`)
> - [ ] Computer software  (`person[taxpayer].sc[design_studio].asset[computer].software`)
> - [ ] Used in a utility, energy, recycling, rent-to-own, racetrack or loan-financed dealer business  (`person[taxpayer].sc[design_studio].asset[computer].industry`)
> - [ ] Built to order over a long period, or “qualified production property”  (`person[taxpayer].sc[design_studio].asset[computer].long_production`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 8, labels 37. Behind each box, optional to read: the question's own prompt (21, 7, 33, 26 words) and help (32, 0, 0, 0)

### 155. `person[taxpayer].sc[design_studio].asset[computer].cost`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — What did it cost, including sales tax, delivery and installation?

- Offered: a dollar amount, zero or more
- Answer: $2,000.00 (persona)
- Words: prompt 13, help 33. Help begins: “For property you used personally before using it in the business, enter the smaller of its adjusted basis or its fair market value on the date you began using it in the business.”

### 156. `person[taxpayer].sc[design_studio].asset[computer].pct`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — What percentage of its use is for this business, from 1 to 100?

- Offered: a whole number
- Answer: 100 (persona)
- Words: prompt 16, help 59. Help begins: “For listed property, measure the use by the time the property is actually used (rather than merely being available for use).”

### 157. `person[taxpayer].sc[design_studio].asset[computer].listed`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Is it equipment of a kind used for entertainment or recreation (such as a camera, or sound or video recording equipment) that is not used only in your business or at your regular place of business? Also answer Yes for a computer you began using before 2018 that is not used only at your regular place of business.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 61, help 27. Help begins: “A part of your home is your regular business establishment only if that part meets the requirements for deducting expenses for the business use of a home.”

### 158. `person[taxpayer].sc[design_studio].asset[computer].s179`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`), line 6(c). About: You › sc design_studio › asset computer

> For this property — How much of its cost do you choose to deduct at once in 2025 under the section 179 election? (Zero if none; not more than its business cost.)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 31, help 20. Help begins: “Only property you bought for use in your business qualifies.”

### 159. `person[taxpayer].sc[design_studio].asset[computer].got_other`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Did you get it with a trade-in, in an exchange, as a replacement for property that was destroyed, stolen or condemned, from a relative or a business you control, or as a gift or inheritance?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 38, help 19. Help begins: “Property got in one of these ways is outside what this tool prepares; a Yes ends the interview here.”

### 160–163. Tick-boxes `asset_history`: 4 questions on one screen

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Is any of these true of its history?
>
> - [ ] Got before September 28, 2017  (`person[taxpayer].sc[design_studio].asset[computer].acquired_before_bonus_date`)
> - [ ] Sold, given away, scrapped or taken for personal use in 2025  (`person[taxpayer].sc[design_studio].asset[computer].ended_this_year`)
> - [ ] A casualty loss, tax credit or special deduction changed its cost  (`person[taxpayer].sc[design_studio].asset[computer].basis_changed`)
> - [ ] A tax year of under 12 months since its business use began  (`person[taxpayer].sc[design_studio].asset[computer].short_year`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 11, labels 39. Behind each box, optional to read: the question's own prompt (11, 28, 30, 26 words) and help (0, 0, 41, 17)

### 164–166. Tick-boxes `asset_method`: 3 questions on one screen

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Is any of these true of how it is depreciated or used?
>
> - [ ] A special depreciation method was chosen instead of the IRS tables  (`person[taxpayer].sc[design_studio].asset[computer].method_other`)
> - [ ] The alternative depreciation system (ADS) is required for it  (`person[taxpayer].sc[design_studio].asset[computer].ads_required`)
> - [ ] Used mostly abroad; leased to a charity, government or foreigner; or bond-financed  (`person[taxpayer].sc[design_studio].asset[computer].outside_use`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 15, labels 32. Behind each box, optional to read: the question's own prompt (37, 39, 27 words) and help (14, 0, 0)

### 167. `person[taxpayer].sc[design_studio].asset[computer].not179`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Is it a land improvement (such as a fence, paving or a swimming pool), property held for investment, or property you bought and lease to others or that a tax-exempt organization, a government or a foreign person uses?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 41, help 93. Help begins: “Answer No for property you lease to others if you manufactured or produced it, or if the lease term (including options to renew) is less than 50% of its class life and for the first 12 months your business deductions for it (other than rents and reimbursed amounts) are more than 15% of its rental income.”

### 168. `person[taxpayer].sc[design_studio].asset[computer].bonus_choice`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — For property of this kind that you began using in 2025, do you take the special ("bonus") depreciation allowance?

- Offered: “Yes: the special depreciation allowance” / “The 40% allowance in place of 100% (an election for property acquired after January 19, 2025)” / “No: I elect not to take any special allowance”
- Answer: “Yes: the special depreciation allowance” (`full`) (persona)
- Words: prompt 22, help 0

### 169. `person[taxpayer].sc[design_studio].asset[computer].after_jan19`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Did you acquire it after January 19, 2025? (Answer No if you signed a binding written contract for it before January 20, 2025, even if you received it later.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 32, help 0

### 170. `person[taxpayer].sc[design_studio].asset[computer].bonus_same`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Is that choice the same for all property in the same recovery period class that you (and your spouse, on a joint return) placed in service in 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 31, help 0

### 171. `person[taxpayer].sc[design_studio].asset[computer].used_before`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — Had anyone used it before you got it?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 11, help 23. Help begins: “Rebuilt or reconditioned property counts as used, unless the cost of its used parts is not more than 20% of its total cost.”

### 172. `person[taxpayer].sc[design_studio].asset[computer].quarter`

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio › asset computer

> For this property — In which part of 2025 did you start using it in the business?

- Offered: “January to March” / “April to June” / “July to September” / “October to December”
- Answer: “April to June” (`q2`) (persona)
- Words: prompt 16, help 0

### 173. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 0

### 174. `person[taxpayer].plan`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did you put money into a SEP IRA or a SIMPLE IRA for yourself for 2025, as a self-employed person?

- Offered: “No, neither” / “Yes, a SEP IRA” / “Yes, a SIMPLE IRA”
- Answer: “No, neither” (`none`) (persona)
- Words: prompt 20, help 23. Help begins: “Money put in after the end of 2025 counts if it was for 2025 and paid by the due date of this return.”

### 175. `person[taxpayer].se_screen`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Does any of these apply to you: an approved exemption from self-employment tax on religious grounds (Form 4361 or Form 4029); fees as a company director, a fiduciary or a fee-basis government employee that are not in a business listed here; Conservation Reserve Program payments; a choice of the optional method of figuring self-employment earnings; or earnings exempt under a social security agreement with another country or from work for a foreign government?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 73, help 13. Help begins: “A Yes is outside what this tool prepares and ends the interview here.”

### 176. `scope.se_plan_other`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 26, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 177. `scope.income_averaging`

Topic: Proof-of-concept scope screening (`scope`)

> Is your business fishing, and do you choose to figure your tax by averaging its income over three years (Schedule J)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 21, help 17. Help begins: “This is a choice.”

### 178. `s2.lookback`

**⟶ topic switch (returns)**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> Did you finish a contract in 2025 that ran over more than one tax year, with its income reported as the work went on?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 24, help 47. Help begins: “Interest may then be owed or refunded (Form 8697).”

### 179. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 180. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 181. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 38, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 182–186. Tick-boxes `sales_rare`: 5 questions on one screen

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

### 187–188. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your investments?
>
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (23, 24 words) and help (34, 37)

### 189. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 190–195. Tick-boxes `outside_us`: 6 questions on one screen

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

### 196–198. Tick-boxes `rare_credits`: 3 questions on one screen

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

### 199. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 200–202. Tick-boxes `other_taxes`: 3 questions on one screen

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

### 203. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 204. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 205. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 206. `qbi.prior_form`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 207. `qbi.suspended`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, are you deducting a business loss or expense of an earlier year that a tax limit kept you from deducting then?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 23, help 37. Help begins: “Examples are a loss held back by the at-risk rules or by the passive activity rules.”

### 208. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 209–210. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [x] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Estimated tax payments, or a 2024 refund applied to 2025”; the other recorded No (background; persona)
- Words: heading 18, labels 21. Behind each box, optional to read: the question's own prompt (26, 20 words) and help (39, 22)

### 211. `f1040.line26`

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 26

> How much estimated tax did you pay for 2025 in all, counting any 2024 refund applied to 2025?

- Offered: a dollar amount, zero or more
- Answer: $12,000.00 (persona)
- Words: prompt 18, help 15. Help begins: “On a joint return add what each of you paid, even if you paid separately.”

### 212. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

## The end reached

**Complete.** The return is completed after 212 questions.

## Totals

| | |
|---|---|
| Questions asked | 212 |
| Steps (screens; a tick-box group shown together is one) | 127 |
| Answered by the persona / by the background / opened and unanswered | 104 / 108 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 4116 |
| Help words (optional to read) | 4610 |
| Words of the answers offered (Yes and No not counted) | 1295 |
| Questions answered no, zero or none | 165 |
| Topics met | 32 |
| Topic switches | 61 |
| of them, returns to a topic already left | 30 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 91 | `person[taxpayer].sc[design_studio].special` | 255 | No |
| 116 | `person[taxpayer].sc[design_studio].ho_other` | 116 | No |
| 175 | `person[taxpayer].se_screen` | 73 | No |
| 157 | `person[taxpayer].sc[design_studio].asset[computer].listed` | 61 | No |
| 140 | `person[taxpayer].sc[design_studio].scveh[van].passenger` | 57 | Yes |
| 115 | `person[taxpayer].sc[design_studio].meals_100` | 54 | $0.00 |
| 148 | `$asset@person[taxpayer].sc[design_studio]` | 49 | the list `computer` |
| 167 | `person[taxpayer].sc[design_studio].asset[computer].not179` | 41 | No |
| 90 | `person[taxpayer].sc[design_studio].method_other` | 39 | No |
| 102 | `person[taxpayer].sc[design_studio].line23` | 39 | $150.00 |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                                       6w  ["taxpayer"]                  [person]
> *  2  f1040.status                                                  9w  "single"                      [f1040]
>    3  household.ever_married                                        5w  false                         [household]
     4  household.community_property                                 20w  false
>>*  5  person[taxpayer].birth_year                                   6w  1987                          [person]
>    6  sa.dependent                                                 15w  false                         [sa]
>>   7  person[taxpayer].blind                                       25w  false                         [person]
>    8  scope.noncitizen                                             16w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                                           12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                                           12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                                              11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                                         8w  false                         [s3]
>   13  $dependent                                                   30w  []                            [dependent]
>>  14  s3.adoption_any                                              19w+ false                         [s3]  (screen 11, child_extras)
>>  15  scope.f8814                                                  11w+ false                         [scope]  (screen 11, child_extras)
    16  scope.rental                                                 19w+ false                         (screen 12, own_income)
    17  scope.k1                                                     12w+ false                         (screen 12, own_income)
    18  scope.farm                                                    6w+ false                         (screen 12, own_income)
>>  19  person[taxpayer].rrta                                        13w+ false                         [person]  (screen 13, work_kind)
    20  person[taxpayer].eligible_educator                           11w+ false                         (screen 13, work_kind)
>   21  $w2@person[taxpayer]                                          8w  []                            [w2]
>>  22  scope.pay_no_w2                                              24w+ false                         [scope]  (screen 15, other_pay)
    23  scope.medicaid_waiver                                        11w+ false                         (screen 15, other_pay)
    24  scope.religious_work                                         12w+ false                         (screen 15, other_pay)
>   25  f8959.territory_w2                                           10w+ false                         [f8959]  (screen 15, other_pay)
>   26  s2.options_any                                               11w+ false                         [s2]  (screen 15, other_pay)
>   27  s1a.tips                                                     12w+ false                         [s1a]  (screen 16, tips_overtime)
    28  s1a.overtime                                                  2w+ false                         (screen 16, tips_overtime)
>   29  f2441.care                                                   20w+ false                         [f2441]  (screen 17, care_help)
    30  f2441.benefits                                               12w+ false                         (screen 17, care_help)
>>  31  s2.household_help                                            12w+ false                         [s2]  (screen 17, care_help)
>   32  s1.uc_any                                                    10w+ false                         [s1]  (screen 18, money_a)
    33  s1.winnings_any                                               9w+ false                         (screen 18, money_a)
    34  s1.scholarship_any                                            9w+ false                         (screen 18, money_a)
    35  s1.jury_any                                                   6w+ false                         (screen 18, money_a)
    36  s1.alaska_any                                                 5w+ false                         (screen 18, money_a)
    37  s1.hobby_any                                                 11w+ false                         (screen 18, money_a)
    38  s1.alimony_any                                               16w+ false                         (screen 19, money_b)
    39  s1.cod_any                                                   11w+ false                         (screen 19, money_b)
    40  s1.ltc_payout                                                12w+ false                         (screen 19, money_b)
    41  s1.inmate_wages                                              12w+ false                         (screen 19, money_b)
    42  s1.digital_income                                            12w+ false                         (screen 19, money_b)
>>  43  scope.recovery                                               12w+ false                         [scope]  (screen 19, money_b)
>   44  refund.any                                                   13w  false                         [refund]
>   45  $retirement@person[taxpayer]                                 31w  []                            [retirement]
>>  46  person[taxpayer].ira_owner                                   17w+ false                         [person]  (screen 22, accounts)
    47  person[taxpayer].inherited_account                           11w+ false                         (screen 22, accounts)
    48  person[taxpayer].x_edu_account                               12w+ false                         (screen 22, accounts)
    49  person[taxpayer].x_archer_excess                             11w+ false                         (screen 22, accounts)
>   50  ssb.any                                                      23w  false                         [ssb]
>   51  $f8889@person[taxpayer]                                      15w  []                            [f8889]
>>  52  scope.disaster_distribution                                  21w+ false                         [scope]  (screen 25, rare_accounts)
    53  scope.archer_msa                                             11w+ false                         (screen 25, rare_accounts)
>>  54  s2.hsa_testing                                               11w+ false                         [s2]  (screen 25, rare_accounts)
>>  55  scope.education_recapture                                    11w+ false                         [scope]  (screen 25, rare_accounts)
>   56  $f1095a                                                      21w  []                            [f1095a]
>>  57  sa.home_owner                                                20w+ false                         [sa]  (screen 27, paid_2025)
    58  sa.state_tax_any                                             10w+ false                         (screen 27, paid_2025)
    59  sa.state_tax_other_any                                       12w+ false                         (screen 27, paid_2025)
    60  sa.personal_property_tax_any                                 12w+ false                         (screen 27, paid_2025)
    61  sa.gifts                                                     11w+ false                         (screen 27, paid_2025)
    62  sa.medical_any                                               10w+ false                         (screen 27, paid_2025)
    63  sa.home_other                                                21w+ false                         (screen 28, paid_more)
    64  sa.gift_carryover                                            12w+ false                         (screen 28, paid_more)
    65  sa.medical_premiums                                          12w+ false                         (screen 28, paid_more)
>   66  sd.casualty                                                  12w+ false                         [sd]  (screen 28, paid_more)
>>  67  sa.estate_tax_income                                         19w+ false                         [sa]  (screen 29, rare_deductions)
    68  sa.bond_premium                                              12w+ false                         (screen 29, rare_deductions)
    69  sa.debt_instrument_loss                                      10w+ false                         (screen 29, rare_deductions)
    70  sa.pension_unrecovered                                       11w+ false                         (screen 29, rare_deductions)
    71  sa.impairment_work                                           12w+ false                         (screen 29, rare_deductions)
    72  sa.elect_itemize                                             16w+ false                         (screen 30, deduction_wishes)
    73  sa.sales_tax_wish                                            12w+ false                         (screen 30, deduction_wishes)
>>  74  s1a.carloan                                                  21w+ false                         [s1a]  (screen 31, home_school)
>>  75  s3.ev                                                        11w+ false                         [s3]  (screen 31, home_school)
    76  s3.kerosene                                                   9w+ false                         (screen 31, home_school)
>   77  f5695.any                                                    11w+ false                         [f5695]  (screen 31, home_school)
>   78  f8863.paid                                                   12w+ false                         [f8863]  (screen 31, home_school)
>   79  sli.any                                                       6w+ false                         [sli]  (screen 31, home_school)
> * 80  $sc@person[taxpayer]                                         34w  ["design_studio"]             [sc]
  * 81  person[taxpayer].sc[design_studio].line1                     23w  8800000
  * 82  person[taxpayer].sc[design_studio].line2                     18w  0
  * 83  person[taxpayer].sc[design_studio].line6                     29w  0
  * 84  person[taxpayer].sc[design_studio].tips_ot                   30w  false
  * 85  person[taxpayer].sc[design_studio].spouse_owned              17w+ false                         (screen 37, biz_refused)
  * 86  person[taxpayer].sc[design_studio].statutory                 12w+ false                         (screen 37, biz_refused)
  * 87  person[taxpayer].sc[design_studio].business_credit           10w+ false                         (screen 37, biz_refused)
  * 88  person[taxpayer].sc[design_studio].fuel_credit               12w+ false                         (screen 37, biz_refused)
  * 89  person[taxpayer].sc[design_studio].passive                   32w  true
  * 90  person[taxpayer].sc[design_studio].method_other              39w  false
  * 91  person[taxpayer].sc[design_studio].special                  255w  false
  * 92  person[taxpayer].sc[design_studio].line8                     10w  110000
  * 93  person[taxpayer].sc[design_studio].line11                    19w  450000
  * 94  person[taxpayer].sc[design_studio].line10                    12w  0
  * 95  person[taxpayer].sc[design_studio].line18                    13w  42000
  * 96  person[taxpayer].sc[design_studio].line22                    25w  130000
  * 97  person[taxpayer].sc[design_studio].line20b                   19w  0
  * 98  person[taxpayer].sc[design_studio].rent_equipment            23w  0
  * 99  person[taxpayer].sc[design_studio].line25                    19w  72000
  *100  person[taxpayer].sc[design_studio].line15                    17w  60000
  *101  person[taxpayer].sc[design_studio].line17                    21w  85000
  *102  person[taxpayer].sc[design_studio].line23                    39w  15000
  *103  person[taxpayer].sc[design_studio].line21                    17w  0
  *104  person[taxpayer].sc[design_studio].line16a                   26w  0
  *105  person[taxpayer].sc[design_studio].line16b                   21w  0
  *106  person[taxpayer].sc[design_studio].line48                    22w  240000
  *107  person[taxpayer].sc[design_studio].travel_meals              21w+ true                          (screen 56, biz_had)
  *108  person[taxpayer].sc[design_studio].employees                  7w+ false                         (screen 56, biz_had)
  *109  person[taxpayer].sc[design_studio].goods                     11w+ false                         (screen 56, biz_had)
  *110  person[taxpayer].sc[design_studio].ho_uses                   12w+ true                          (screen 56, biz_had)
  *111  person[taxpayer].sc[design_studio].hi_uses                    9w+ false                         (screen 56, biz_had)
  *112  person[taxpayer].sc[design_studio].line24a                   24w  95000
  *113  person[taxpayer].sc[design_studio].meals_50                  33w  36000
  *114  person[taxpayer].sc[design_studio].meals_80                  36w  0
  *115  person[taxpayer].sc[design_studio].meals_100                 54w  0
  *116  person[taxpayer].sc[design_studio].ho_other                 116w  false
  *117  person[taxpayer].sc[design_studio].ho_sqft                   17w  180
> *118  $scveh@person[taxpayer].sc[design_studio]                    32w  ["van"]                       [scveh]
  *119  person[taxpayer].sc[design_studio].scveh[van].method         17w  "actual"
  *120  person[taxpayer].sc[design_studio].scveh[van].miles_business   25w  8000
  *121  person[taxpayer].sc[design_studio].scveh[van].parking        20w  21000
  *122  person[taxpayer].sc[design_studio].scveh[van].miles_commuting   19w  0
  *123  person[taxpayer].sc[design_studio].scveh[van].miles_other    19w  2000
  *124  person[taxpayer].sc[design_studio].scveh[van].operating      32w  300000
  *125  person[taxpayer].sc[design_studio].scveh[van].employee_use   29w  false
  *126  person[taxpayer].sc[design_studio].scveh[van].owned          13w  true
  *127  person[taxpayer].sc[design_studio].scveh[van].placed         14w  "y2025"
  *128  person[taxpayer].sc[design_studio].scveh[van].records        22w  true
  *129  person[taxpayer].sc[design_studio].scveh[van].got_other      34w  false
  *130  person[taxpayer].sc[design_studio].scveh[van].acquired_before_bonus_date   16w+ false                         (screen 75, veh_history)
  *131  person[taxpayer].sc[design_studio].scveh[van].converted       8w+ false                         (screen 75, veh_history)
  *132  person[taxpayer].sc[design_studio].scveh[van].disposed        9w+ false                         (screen 75, veh_history)
  *133  person[taxpayer].sc[design_studio].scveh[van].basis_changed   12w+ false                         (screen 75, veh_history)
  *134  person[taxpayer].sc[design_studio].scveh[van].short_year     12w+ false                         (screen 75, veh_history)
  *135  person[taxpayer].sc[design_studio].scveh[van].for_hire       27w+ false                         (screen 76, veh_use)
  *136  person[taxpayer].sc[design_studio].scveh[van].investment     10w+ false                         (screen 76, veh_use)
  *137  person[taxpayer].sc[design_studio].scveh[van].others_use      7w+ false                         (screen 76, veh_use)
  *138  person[taxpayer].sc[design_studio].scveh[van].method_other   12w+ false                         (screen 76, veh_use)
  *139  person[taxpayer].sc[design_studio].scveh[van].cost           24w  3000000
  *140  person[taxpayer].sc[design_studio].scveh[van].passenger      57w  true
  *141  person[taxpayer].sc[design_studio].scveh[van].s179_elect     25w  0
  *142  person[taxpayer].sc[design_studio].scveh[van].bonus_choice   24w  "full"
  *143  person[taxpayer].sc[design_studio].scveh[van].after_jan19    12w  true
  *144  person[taxpayer].sc[design_studio].scveh[van].bonus_same     32w  true
  *145  person[taxpayer].sc[design_studio].scveh[van].used_before    12w  false
  *146  person[taxpayer].sc[design_studio].scveh[van].bonus_excluded   35w  false
  *147  person[taxpayer].sc[design_studio].scveh[van].quarter        16w  "q2"
> *148  $asset@person[taxpayer].sc[design_studio]                    49w  ["computer"]                  [asset]
  *149  person[taxpayer].sc[design_studio].asset[computer].class     28w  "c00_12"
  *150  person[taxpayer].sc[design_studio].asset[computer].placed    14w  "y2025"
  *151  person[taxpayer].sc[design_studio].asset[computer].kind_excluded   20w+ false                         (screen 89, asset_kind)
  *152  person[taxpayer].sc[design_studio].asset[computer].software    2w+ false                         (screen 89, asset_kind)
  *153  person[taxpayer].sc[design_studio].asset[computer].industry   12w+ false                         (screen 89, asset_kind)
  *154  person[taxpayer].sc[design_studio].asset[computer].long_production   11w+ false                         (screen 89, asset_kind)
  *155  person[taxpayer].sc[design_studio].asset[computer].cost      13w  200000
  *156  person[taxpayer].sc[design_studio].asset[computer].pct       16w  100
  *157  person[taxpayer].sc[design_studio].asset[computer].listed    61w  false
  *158  person[taxpayer].sc[design_studio].asset[computer].s179      31w  0
  *159  person[taxpayer].sc[design_studio].asset[computer].got_other   38w  false
  *160  person[taxpayer].sc[design_studio].asset[computer].acquired_before_bonus_date   16w+ false                         (screen 95, asset_history)
  *161  person[taxpayer].sc[design_studio].asset[computer].ended_this_year   11w+ false                         (screen 95, asset_history)
  *162  person[taxpayer].sc[design_studio].asset[computer].basis_changed   11w+ false                         (screen 95, asset_history)
  *163  person[taxpayer].sc[design_studio].asset[computer].short_year   12w+ false                         (screen 95, asset_history)
  *164  person[taxpayer].sc[design_studio].asset[computer].method_other   26w+ false                         (screen 96, asset_method)
  *165  person[taxpayer].sc[design_studio].asset[computer].ads_required    9w+ false                         (screen 96, asset_method)
  *166  person[taxpayer].sc[design_studio].asset[computer].outside_use   12w+ false                         (screen 96, asset_method)
  *167  person[taxpayer].sc[design_studio].asset[computer].not179    41w  false
  *168  person[taxpayer].sc[design_studio].asset[computer].bonus_choice   22w  "full"
  *169  person[taxpayer].sc[design_studio].asset[computer].after_jan19   32w  true
  *170  person[taxpayer].sc[design_studio].asset[computer].bonus_same   31w  true
  *171  person[taxpayer].sc[design_studio].asset[computer].used_before   11w  false
  *172  person[taxpayer].sc[design_studio].asset[computer].quarter   16w  "q2"
>> 173  scope.business_before                                        25w  false                         [scope]
>>*174  person[taxpayer].plan                                        20w  "none"                        [person]
  *175  person[taxpayer].se_screen                                   73w  false
>>*176  scope.se_plan_other                                          26w  false                         [scope]
  *177  scope.income_averaging                                       21w  false
>>*178  s2.lookback                                                  24w  false                         [s2]
>  179  $interest                                                    21w  []                            [interest]
>  180  div.any                                                      21w  false                         [div]
>  181  $sales                                                       38w  []                            [sales]
>> 182  sd.sold_other                                                25w+ false                         [sd]  (screen 112, sales_rare)
   183  sd.sec1256                                                   12w+ false                         (screen 112, sales_rare)
   184  sd.condemned                                                  9w+ false                         (screen 112, sales_rare)
   185  sd.small_business_stock                                      12w+ false                         (screen 112, sales_rare)
   186  sd.trader_election                                            9w+ false                         (screen 112, sales_rare)
   187  sd.carryover                                                 20w+ false                         (screen 113, invest_other)
>  188  f4952.has_interest                                           12w+ false                         [f4952]  (screen 113, invest_other)
>> 189  s3.foreign_any                                               24w  false                         [s3]
>  190  sb.account_any                                               27w+ false                         [sb]  (screen 115, outside_us)
   191  sb.asset_any                                                 11w+ false                         (screen 115, outside_us)
   192  sb.trust_any                                                  9w+ false                         (screen 115, outside_us)
   193  sb.company_any                                               12w+ false                         (screen 115, outside_us)
   194  sb.territory_any                                             10w+ false                         (screen 115, outside_us)
>> 195  scope.foreign_shares                                         12w+ false                         [scope]  (screen 115, outside_us)
>> 196  s3.credit_bond                                               19w+ false                         [s3]  (screen 116, rare_credits)
   197  s3.farmland                                                   2w+ false                         (screen 116, rare_credits)
   198  s3.repaid_income                                             11w+ false                         (screen 116, rare_credits)
   199  s3.prior_other_forms                                         25w  false
>> 200  s2.credit_recapture                                          20w+ false                         [s2]  (screen 118, other_taxes)
   201  s2.amt_owed                                                   3w+ false                         (screen 118, other_taxes)
   202  s2.other_tax                                                  9w+ false                         (screen 118, other_taxes)
>  203  $oi8z                                                        21w  []                            [oi8z]
>> 204  scope.reforestation                                          22w  false                         [scope]
   205  scope.attorney_fees                                          21w  false
>  206  qbi.prior_form                                               19w  false                         [qbi]
  *207  qbi.suspended                                                23w  false
   208  qbi.coop_patron                                              19w  false
>> 209  f1040.withheld_other_any                                     29w+ false                         [f1040]  (screen 125, paid_already)
  *210  f1040.estimated_any                                          10w+ true                          (screen 125, paid_already)
  *211  f1040.line26                                                 18w  1200000
>> 212  s3.line10                                                    20w  0                             [s3]
```
