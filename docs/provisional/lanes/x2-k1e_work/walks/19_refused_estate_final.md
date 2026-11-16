# Walk: 19_refused_estate_final

A single person, 60, with one job, whose mother's estate closed in 2025; the estate's final Schedule K-1 (Form 1041) shows excess deductions in box 11, which the tool does not prepare.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/19_refused_estate_final.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

## PROBLEMS WITH THIS PERSONA

- persona 19_refused_estate_final: expected a refusal at k1e.box11_any; the walk was refused at person[taxpayer].k1e[mom_estate].box11_any (Schedule K-1 (Form 1041), box 11 (final year deductions)) after 88 answers

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
- Answer: 1965 (persona)
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
- Words: prompt 25, help 53. Help begins: “The statement must say that your better eye sees no better than 20/200 with glasses or contact lenses, or that your field of vision is 20 degrees or less, or that your sight is not likely to improve beyond those limits.”

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
> - [ ] Adoption, or adoption costs paid by you or an employer, since 2024  (`s3.adoption_any`)
> - [ ] Reporting a child's 2025 interest or dividends on your own return  (`scope.f8814`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 23. Behind each box, optional to read: the question's own prompt (21, 21 words) and help (31, 28)

### 16–18. Tick-boxes `own_income`: 3 questions on one screen

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you have any of these?
>
> - [ ] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [x] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Income or a loss from a partnership, S corporation, estate or trust”; the others recorded No (background; persona)
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

### 22–27. Tick-boxes `other_pay`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Form 8959 — Additional Medicare Tax on wages and self-employment income (`f8959`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you have any of these kinds of work or pay?
>
> - [ ] Wages, tips or strike benefits that are not on a W-2  (`scope.pay_no_w2`)
> - [ ] Medicaid pay for caring for someone who lives in your home  (`scope.medicaid_waiver`)
> - [ ] Pay for work for a church or religious body, or as clergy  (`scope.religious_work`)
> - [ ] A wage statement from Puerto Rico or another U.S. territory  (`f8959.territory_w2`)
> - [ ] Employer stock options used to buy shares, or such shares sold  (`s2.options_any`)
> - [ ] Shares bought before 2025 with incentive stock options that vested in 2025  (`s2.iso_vested`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 13, labels 67. Behind each box, optional to read: the question's own prompt (16, 18, 25, 16, 19, 14 words) and help (38, 38, 23, 13, 21, 40)

### 28–29. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 3. Behind each box, optional to read: the question's own prompt (9, 9 words) and help (33, 21)

### 30–32. Tick-boxes `care_help`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you have any of these?
>
> - [ ] Care for a child or disabled adult, during work or job-search hours  (`f2441.care`)
> - [ ] An employer's help with care costs, such as a dependent care account  (`f2441.benefits`)
> - [ ] Someone you paid to work in your home: a nanny, housekeeper, gardener  (`s2.household_help`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 36. Behind each box, optional to read: the question's own prompt (35, 28, 24 words) and help (50, 42, 24)

### 33–38. Tick-boxes `money_a`: 6 questions on one screen

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

### 39–44. Tick-boxes `money_b`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Did any of these happen to you?
>
> - [ ] Alimony paid or received since the start of 2023  (`s1.alimony_any`)
> - [ ] A debt canceled or forgiven by a lender or card company  (`s1.cod_any`)
> - [ ] A long-term care insurance payout, or life insurance paid early, in 2025  (`s1.ltc_payout`)
> - [ ] Pay in 2025 for work done while in a jail or prison  (`s1.inmate_wages`)
> - [ ] Crypto received as pay, a reward, or from mining, staking, a fork  (`s1.digital_income`)
> - [ ] Paid back a deduction or credit that lowered tax (not state/local refund)  (`scope.recovery`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 68. Behind each box, optional to read: the question's own prompt (23, 15, 21, 14, 23, 29 words) and help (22, 37, 11, 6, 38, 73)

### 45. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 46. `$retirement@person[taxpayer]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 31, help 21. Help begins: “List a Form RRB-1099-R too.”

### 47–50. Tick-boxes `accounts`: 4 questions on one screen

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
- Words: heading 7, labels 44. Behind each box, optional to read: the question's own prompt (23, 18, 26, 28 words) and help (40, 11, 25, 16)

### 51. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 0

### 52. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 15, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 53–56. Tick-boxes `rare_accounts`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did any of these apply to you?
>
> - [ ] Have a 2023 or 2024 disaster withdrawal still being taxed or repaid  (`scope.disaster_distribution`)
> - [ ] Money put into or taken from an Archer or Medicare Advantage MSA  (`scope.archer_msa`)
> - [ ] Over-contributed to an HSA for 2024, with no HSA in 2025  (`s2.hsa_testing`)
> - [ ] Tuition refunded, or tax-free aid, for a year an education credit covered  (`scope.education_recapture`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 47. Behind each box, optional to read: the question's own prompt (31, 31, 29, 27 words) and help (23, 14, 42, 36)

### 57. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 21, help 52. Help begins: “Each plan has its own Form 1095-A.”

### 58–63. Tick-boxes `paid_2025`: 6 questions on one screen

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
- Words: heading 8, labels 67. Behind each box, optional to read: the question's own prompt (14, 23, 34, 28, 21, 21 words) and help (31, 0, 54, 30, 39, 32)

### 64–67. Tick-boxes `paid_more`: 4 questions on one screen

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

### 68–72. Tick-boxes `rare_deductions`: 5 questions on one screen

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

### 73–74. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 75–80. Tick-boxes `home_school`: 6 questions on one screen

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
- Words: heading 9, labels 61. Behind each box, optional to read: the question's own prompt (19, 22, 13, 27, 20, 10 words) and help (37, 19, 0, 34, 39, 18)

### 81. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 34, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 82–83. Tick-boxes `before_2025`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Before 2025, did you have either of these?
>
> - [ ] A business, farm, rental, or share in a partnership or S corporation  (`scope.business_before`)
> - [ ] A loss still being carried into 2025 (a 'net operating loss')  (`scope.nol`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 23. Behind each box, optional to read: the question's own prompt (25, 17 words) and help (0, 42)

### 84. `$k1e@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule K-1 (Form 1041), a beneficiary's share of an estate's or trust's income — one entry per Schedule K-1 (`k1e`). About: You

> In 2025, did you get a Schedule K-1 (Form 1041) from an estate or a trust? Add one entry for each; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: the list `mom_estate` (persona)
- Words: prompt 29, help 37. Help begins: “An heir of an estate, or a beneficiary of a trust, gets one for the year the estate or trust paid out or kept income for them.”

### 85–88. Tick-boxes `k1e_refused`: 4 questions on one screen

Topic: Schedule K-1 (Form 1041), a beneficiary's share of an estate's or trust's income — one entry per Schedule K-1 (`k1e`). About: You › k1e mom_estate

> Does any of these boxes of this Schedule K-1 show an amount?
>
> - [ ] Box 9, directly apportioned deductions  (`person[taxpayer].k1e[mom_estate].box9_any`)
> - [ ] Box 10, estate tax deduction  (`person[taxpayer].k1e[mom_estate].box10_any`)
> - [x] Box 11, final year deductions  (`person[taxpayer].k1e[mom_estate].box11_any`)
> - [ ] Box 12, alternative minimum tax adjustment  (`person[taxpayer].k1e[mom_estate].box12_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Box 11, final year deductions”; the others recorded No (persona)
- Words: heading 12, labels 21. Behind each box, optional to read: the question's own prompt (17, 13, 25, 14 words) and help (6, 6, 18, 6)

## The end reached

**Refused** at the gate `person[taxpayer].k1e[mom_estate].box11_any`, after 88 questions. The wording shown:

> Schedule K-1 (Form 1041), box 11 (final year deductions)
>
> This tool prepares the income of an estate or trust reported on Schedule K-1 (Form 1041); final year deductions (excess deductions on termination, and capital loss and net operating loss carryovers) are not prepared.

## Totals

| | |
|---|---|
| Questions asked | 88 |
| Steps (screens; a tick-box group shown together is one) | 35 |
| Answered by the persona / by the background / opened and unanswered | 9 / 79 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 1168 |
| Help words (optional to read) | 2370 |
| Words of the answers offered (Yes and No not counted) | 105 |
| Questions answered no, zero or none | 82 |
| Topics met | 24 |
| Topic switches | 42 |
| of them, returns to a topic already left | 19 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 30 | `f2441.care` (its own prompt, behind a tick-box) | 35 | No |
| 60 | `sa.state_tax_other_any` (its own prompt, behind a tick-box) | 34 | No |
| 81 | `$sc@person[taxpayer]` | 34 | none (an empty list) |
| 64 | `sa.home_other` (its own prompt, behind a tick-box) | 33 | No |
| 69 | `sa.bond_premium` (its own prompt, behind a tick-box) | 32 | No |
| 46 | `$retirement@person[taxpayer]` | 31 | none (an empty list) |
| 53 | `scope.disaster_distribution` (its own prompt, behind a tick-box) | 31 | No |
| 54 | `scope.archer_msa` (its own prompt, behind a tick-box) | 31 | No |
| 70 | `sa.debt_instrument_loss` (its own prompt, behind a tick-box) | 31 | No |
| 13 | `$dependent` | 30 | none (an empty list) |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                       6w  ["taxpayer"]                  [person]
> *  2  f1040.status                                  9w  "single"                      [f1040]
>    3  household.ever_married                        5w  false                         [household]
     4  household.community_property                 20w  false
>>*  5  person[taxpayer].birth_year                   6w  1965                          [person]
>    6  sa.dependent                                 15w  false                         [sa]
>>   7  person[taxpayer].blind                       25w  false                         [person]
>    8  scope.noncitizen                             16w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                           12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                           12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                              11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                         8w  false                         [s3]
>   13  $dependent                                   30w  []                            [dependent]
>>  14  s3.adoption_any                              19w+ false                         [s3]  (screen 11, child_extras)
>>  15  scope.f8814                                  11w+ false                         [scope]  (screen 11, child_extras)
    16  scope.rental                                 19w+ false                         (screen 12, own_income)
  * 17  scope.k1                                     12w+ true                          (screen 12, own_income)
    18  scope.farm                                    6w+ false                         (screen 12, own_income)
>>  19  person[taxpayer].rrta                        13w+ false                         [person]  (screen 13, work_kind)
    20  person[taxpayer].eligible_educator           11w+ false                         (screen 13, work_kind)
>   21  $w2@person[taxpayer]                          8w  []                            [w2]
>>  22  scope.pay_no_w2                              24w+ false                         [scope]  (screen 15, other_pay)
    23  scope.medicaid_waiver                        11w+ false                         (screen 15, other_pay)
    24  scope.religious_work                         12w+ false                         (screen 15, other_pay)
>   25  f8959.territory_w2                           10w+ false                         [f8959]  (screen 15, other_pay)
>   26  s2.options_any                               11w+ false                         [s2]  (screen 15, other_pay)
    27  s2.iso_vested                                12w+ false                         (screen 15, other_pay)
>   28  s1a.tips                                     12w+ false                         [s1a]  (screen 16, tips_overtime)
    29  s1a.overtime                                  2w+ false                         (screen 16, tips_overtime)
>   30  f2441.care                                   20w+ false                         [f2441]  (screen 17, care_help)
    31  f2441.benefits                               12w+ false                         (screen 17, care_help)
>>  32  s2.household_help                            12w+ false                         [s2]  (screen 17, care_help)
>   33  s1.uc_any                                    10w+ false                         [s1]  (screen 18, money_a)
    34  s1.winnings_any                               9w+ false                         (screen 18, money_a)
    35  s1.scholarship_any                            9w+ false                         (screen 18, money_a)
    36  s1.jury_any                                   6w+ false                         (screen 18, money_a)
    37  s1.alaska_any                                 5w+ false                         (screen 18, money_a)
    38  s1.hobby_any                                 11w+ false                         (screen 18, money_a)
    39  s1.alimony_any                               16w+ false                         (screen 19, money_b)
    40  s1.cod_any                                   11w+ false                         (screen 19, money_b)
    41  s1.ltc_payout                                12w+ false                         (screen 19, money_b)
    42  s1.inmate_wages                              12w+ false                         (screen 19, money_b)
    43  s1.digital_income                            12w+ false                         (screen 19, money_b)
>>  44  scope.recovery                               12w+ false                         [scope]  (screen 19, money_b)
>   45  refund.any                                   13w  false                         [refund]
>   46  $retirement@person[taxpayer]                 31w  []                            [retirement]
>>  47  person[taxpayer].ira_owner                   17w+ false                         [person]  (screen 22, accounts)
    48  person[taxpayer].inherited_account           11w+ false                         (screen 22, accounts)
    49  person[taxpayer].x_edu_account               12w+ false                         (screen 22, accounts)
    50  person[taxpayer].x_archer_excess             11w+ false                         (screen 22, accounts)
>   51  ssb.any                                      23w  false                         [ssb]
>   52  $f8889@person[taxpayer]                      15w  []                            [f8889]
>>  53  scope.disaster_distribution                  21w+ false                         [scope]  (screen 25, rare_accounts)
    54  scope.archer_msa                             12w+ false                         (screen 25, rare_accounts)
>>  55  s2.hsa_testing                               11w+ false                         [s2]  (screen 25, rare_accounts)
>>  56  scope.education_recapture                    12w+ false                         [scope]  (screen 25, rare_accounts)
>   57  $f1095a                                      21w  []                            [f1095a]
>>  58  sa.home_owner                                20w+ false                         [sa]  (screen 27, paid_2025)
    59  sa.state_tax_any                             10w+ false                         (screen 27, paid_2025)
    60  sa.state_tax_other_any                       12w+ false                         (screen 27, paid_2025)
    61  sa.personal_property_tax_any                 12w+ false                         (screen 27, paid_2025)
    62  sa.gifts                                     11w+ false                         (screen 27, paid_2025)
    63  sa.medical_any                               10w+ false                         (screen 27, paid_2025)
    64  sa.home_other                                21w+ false                         (screen 28, paid_more)
    65  sa.gift_carryover                            12w+ false                         (screen 28, paid_more)
    66  sa.medical_premiums                          12w+ false                         (screen 28, paid_more)
>   67  sd.casualty                                  12w+ false                         [sd]  (screen 28, paid_more)
>>  68  sa.estate_tax_income                         19w+ false                         [sa]  (screen 29, rare_deductions)
    69  sa.bond_premium                              12w+ false                         (screen 29, rare_deductions)
    70  sa.debt_instrument_loss                      10w+ false                         (screen 29, rare_deductions)
    71  sa.pension_unrecovered                       11w+ false                         (screen 29, rare_deductions)
    72  sa.impairment_work                           12w+ false                         (screen 29, rare_deductions)
    73  sa.elect_itemize                             16w+ false                         (screen 30, deduction_wishes)
    74  sa.sales_tax_wish                            12w+ false                         (screen 30, deduction_wishes)
>>  75  s1a.carloan                                  21w+ false                         [s1a]  (screen 31, home_school)
>>  76  s3.ev                                        11w+ false                         [s3]  (screen 31, home_school)
    77  s3.kerosene                                   9w+ false                         (screen 31, home_school)
>   78  f5695.any                                    11w+ false                         [f5695]  (screen 31, home_school)
>   79  f8863.paid                                   12w+ false                         [f8863]  (screen 31, home_school)
>   80  sli.any                                       6w+ false                         [sli]  (screen 31, home_school)
>   81  $sc@person[taxpayer]                         34w  []                            [sc]
>>  82  scope.business_before                        20w+ false                         [scope]  (screen 33, before_2025)
    83  scope.nol                                    11w+ false                         (screen 33, before_2025)
> * 84  $k1e@person[taxpayer]                        29w  ["mom_estate"]                [k1e]
  * 85  person[taxpayer].k1e[mom_estate].box9_any    17w+ false                         (screen 35, k1e_refused)
  * 86  person[taxpayer].k1e[mom_estate].box10_any    5w+ false                         (screen 35, k1e_refused)
  * 87  person[taxpayer].k1e[mom_estate].box11_any    5w+ true                          (screen 35, k1e_refused)
  * 88  person[taxpayer].k1e[mom_estate].box12_any    6w+ false                         (screen 35, k1e_refused)
```
