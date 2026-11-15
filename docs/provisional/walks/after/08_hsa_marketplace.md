# Walk: 08_hsa_marketplace

A single person, 34, who bought Marketplace health insurance for January to April (a Form 1095-A), then started a job with a high-deductible health plan and a health savings account.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/08_hsa_marketplace.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: 1991 (persona)
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
- Answer: the list `logistics_co` (persona)
- Words: prompt 8, help 32. Help begins: “Name each employer once.”

### 22. `person[taxpayer].w2[logistics_co].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 logistics_co

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $42,000.00 (persona)
- Words: prompt 6, help 0

### 23. `person[taxpayer].w2[logistics_co].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 logistics_co

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $4,600.00 (persona)
- Words: prompt 6, help 0

### 24. `person[taxpayer].w2[logistics_co].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 logistics_co

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $2,604.00 (persona)
- Words: prompt 6, help 0

### 25. `person[taxpayer].w2[logistics_co].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 logistics_co

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $42,000.00 (persona)
- Words: prompt 6, help 0

### 26. `person[taxpayer].w2[logistics_co].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 logistics_co

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $609.00 (persona)
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
- Answer: “Yes” (persona)
- Words: prompt 15, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 62. `person[taxpayer].f8889[hsa].owner_died`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did the owner of this HSA die in 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 9, help 31. Help begins: “The owner is the person these questions are about.”

### 63. `person[taxpayer].f8889[hsa].inherited`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did you get an HSA, or money from one, because its owner died?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 13, help 28. Help begins: “For example, a parent, or a husband or wife who has died, named you as the beneficiary of their HSA.”

### 64. `person[taxpayer].f8889[hsa].archer`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did you or your spouse have an Archer MSA in 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 11, help 56. Help begins: “An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked.”

### 65. `person[taxpayer].f8889[hsa].line9`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`), line 9. About: You › HSA

> How much did your employer put into your HSA for 2025, including money taken out of your pay?

- Offered: a dollar amount, zero or more
- Answer: $1,600.00 (persona)
- Words: prompt 18, help 41. Help begins: “Use the amount in box 12 of your Form W-2 next to the letter W.”

### 66. `person[taxpayer].f8889[hsa].line2`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`), line 2. About: You › HSA

> How much did you put into your HSA for 2025 yourself, not counting money in box 12 of your Form W-2?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 21, help 107. Help begins: “Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone).”

### 67. `person[taxpayer].f8889[hsa].ira_transfer`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was any money moved into your HSA straight from an IRA in 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 13, help 23. Help begins: “The IRA's custodian sends the money directly to the HSA.”

### 68. `person[taxpayer].f8889[hsa].excess_withdrawn`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> In 2025, or in 2026 before filing this return, did you take money back out of your HSA because too much had been put in?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 25, help 33. Help begins: “This is called withdrawing excess contributions.”

### 69. `person[taxpayer].f8889[hsa].coverage_year`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was your health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?

- Offered: “Yes, all 12 months, covering one person only” / “Yes, all 12 months, covering more than one person” / “No: it started, stopped or changed during 2025, or not sure”
- Answer: “No: it started, stopped or changed during 2025, or not sure” (`changed`) (persona)
- Words: prompt 20, help 90. Help begins: “What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”.”

### 70. `person[taxpayer].f8889[hsa].months_eligible`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> On the first day of how many months of 2025 were you covered by an HSA-qualifying plan, with all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills, counting a health FSA or HRA at work that pays ordinary medical bills, yours or your spouse's (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

- Offered: a whole number
- Answer: 8 (persona)
- Words: prompt 74, help 90. Help begins: “Count a month only if everything held on its first day; December counts as one of the months.”

### 71. `person[taxpayer].f8889[hsa].months_family`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> On the first day of how many of those months did your plan cover more than one person, or did your spouse have a high-deductible plan covering more than one person?

- Offered: a whole number
- Answer: 0 (persona)
- Words: prompt 31, help 60. Help begins: “Count a month also if you were covered by someone else's family plan, or had a plan for only you and a family plan at once.”

### 72. `person[taxpayer].f8889[hsa].dec_coverage`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> What did you have on December 1, 2025?

- Offered: “No HSA-qualifying coverage that day” / “An HSA-qualifying plan covering one person only” / “An HSA-qualifying plan covering more than one person”
- Answer: “An HSA-qualifying plan covering one person only” (`self_only`) (persona)
- Words: prompt 8, help 75. Help begins: “Choose the first answer if on December 1 you were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent.”

### 73. `person[taxpayer].f8889[hsa].last_month`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Do you want to be treated as having had your December 1 coverage for all of 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 17, help 75. Help begins: “This is the “last-month rule”.”

### 74. `person[taxpayer].f8889[hsa].ira_prior`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was any money moved into your HSA straight from an IRA during 2024?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 13, help 45. Help begins: “The IRA's custodian sends the money directly to the HSA.”

### 75. `person[taxpayer].f8889[hsa].testing_prior`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> For 2024, was more put into your HSA, by you, your employer or anyone else, than the months you could have an HSA, and the kind of plan you had in each, allowed?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 33, help 175. Help begins: “This is about the “last-month rule”.”

### 76. `person[taxpayer].f8889[hsa].line14a`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`), line 14a. About: You › HSA

> How much came out of your HSA in 2025 in total?

- Offered: a dollar amount, zero or more
- Answer: $450.00 (persona)
- Words: prompt 11, help 56. Help begins: “Add box 1 of your 2025 Forms 1099-SA for HSAs (box 5 marks the kind of account).”

### 77. `person[taxpayer].f8889[hsa].dist_code`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Does box 3 of any of your 2025 Forms 1099-SA for an HSA show a number other than 1 or 3?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 21, help 36. Help begins: “Box 3 is the “distribution code”.”

### 78. `person[taxpayer].f8889[hsa].rollover`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> How much of the money that came out did you put into another HSA of your own within 60 days?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 35. Help begins: “An HSA can take in only one such deposit in any 12 months; do not count a second one, or money the bank moved directly (that is not part of the total).”

### 79. `person[taxpayer].f8889[hsa].mistake_repaid`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was any money paid out of your HSA by mistake and later put back?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 14, help 33. Help begins: “For example, the HSA paid a bill that turned out not to be a medical cost, and you returned the money to the HSA.”

### 80. `person[taxpayer].f8889[hsa].medical_all`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of you, your spouse, or your dependents?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 24, help 66. Help begins: “Answer No if any of it paid for insurance premiums, for someone else (such as an adult child you do not claim), for costs from before you opened the HSA, or for costs that insurance or anyone else paid back to you.”

### 81. `person[taxpayer].f8889[hsa].loan`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> In 2025, did you use your HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it yourself?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 26, help 51. Help begins: “It counts whether you did it yourself or through someone else.”

### 82. `person[taxpayer].x_hsa_prior_excess`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Before 2025, was more put into your HSA than the limit for the year, with some of the extra still in the account at the start of 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 28, help 36. Help begins: “Answer Yes if your 2024 Form 5329 has an amount on line 48, or if you never reported the excess.”

### 83–86. Tick-boxes `rare_accounts`: 4 questions on one screen

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

### 87. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “Yes, with one Form 1095-A” (persona)
- Words: prompt 21, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 88–92. Tick-boxes `mkt_people`: 5 questions on one screen

**⟶ topic switch**

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> About the people on your Marketplace plan in 2025: is any of these true?
>
> - [ ] The plan also covered someone who is not on this return  (`f8962.shared_policy`)
> - [ ] A divorce or legal separation from someone on the same plan  (`f8962.divorced_enrolled`)
> - [ ] Advance payments were made for someone on no one's 2025 return  (`f8962.no_family`)
> - [ ] Someone covered was not lawfully present in the United States  (`f8962.not_lawful`)
> - [ ] Someone covered was in jail or prison (not awaiting trial)  (`f8962.incarcerated`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 14, labels 53. Behind each box, optional to read: the question's own prompt (32, 20, 29, 14, 18 words) and help (58, 16, 44, 16, 16)

### 93. `f8962.medicaid_reversed`

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> Was a Marketplace finding that you, or someone on this return, could not get Medicaid or CHIP later found to rest on wrong information, given on purpose or recklessly?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 29, help 16. Help begins: “A return with this is outside what this tool prepares; a Yes ends the interview here.”

### 94. `f8962.other_coverage`

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> While on Marketplace insurance, could anyone on this return have had other health coverage, such as a job's plan, Medicare, Medicaid, CHIP, TRICARE or veterans' care?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 26, help 24. Help begins: “If you are not sure, answer Yes; the next questions settle it.”

### 95. `f8962.hra`

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> For 2025, did an employer offer you, or anyone on this return, money to pay for health insurance you buy yourself (a 'QSEHRA' or an 'individual coverage HRA')?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 28, help 37. Help begins: “A W-2 shows a QSEHRA in box 12 with the letters FF.”

### 96–99. Tick-boxes `mkt_premiums`: 4 questions on one screen

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> About the premiums for the Marketplace plan: is any of these true?
>
> - [ ] Part of a month's premium was left unpaid  (`f8962.unpaid`)
> - [ ] Form 1095-A shows zero in column A for a month you paid  (`f8962.a_zero_paid`)
> - [ ] A premium for a 2025 month was refunded during 2025  (`f8962.premium_refunded`)
> - [ ] Coverage began mid-month for someone (not a newborn or adopted child)  (`f8962.midmonth_start`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 12, labels 41. Behind each box, optional to read: the question's own prompt (13, 17, 13, 40 words) and help (44, 16, 16, 39)

### 100. `f1095a[form_1].void`

**⟶ topic switch (returns)**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — Is the VOID box at the top of this form ticked, or did the Marketplace later send another form, marked VOID or CORRECTED, for the same plan?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 31, help 28. Help begins: “Use only the form the Marketplace says to use.”

### 101. `f1095a[form_1].same_months`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — Does Part III show the same amount in column A for every month, January to December, and the same amount in column B for every month?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 30, help 16. Help begins: “Answer No if any month is blank in column A.”

### 102. `f1095a[form_1].b_blank`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — Is column B blank or zero in any month that has an amount in column A?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 20, help 0

### 103. `f1095a[form_1].b_changed`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — During 2025, did your address, the people in your household or on this plan, or anyone's access to other health coverage change without the Marketplace being told?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 31, help 57. Help begins: “For example: a move; a birth or a death; someone joining or leaving the plan partway through the year; someone gaining or losing the chance of coverage from a job; or claiming different people on this return than you told the Marketplace you would.”

### 104. `f1095a[form_1].in_c_jan`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — January, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 16, help 0

### 105. `f1095a[form_1].in_c_feb`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — February, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 16, help 0

### 106. `f1095a[form_1].in_c_mar`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — March, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 16, help 0

### 107. `f1095a[form_1].in_c_apr`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — April, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 16, help 0

### 108. `f1095a[form_1].in_c_may`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — May, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 109. `f1095a[form_1].in_c_jun`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — June, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 110. `f1095a[form_1].in_c_jul`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — July, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 111. `f1095a[form_1].in_c_aug`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — August, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 112. `f1095a[form_1].in_c_sep`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — September, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 113. `f1095a[form_1].in_c_oct`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — October, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 114. `f1095a[form_1].in_c_nov`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — November, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 115. `f1095a[form_1].in_c_dec`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — December, column C (the monthly advance payment). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 0

### 116. `f8962.fpl_table`

**⟶ topic switch (returns)**

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> In 2025, did you live in Alaska or Hawaii?

- Offered: “No” / “Yes, in Alaska for all or part of the year” / “Yes, in Hawaii for all or part of the year, and not in Alaska”
- Answer: “No” (`contiguous`) (persona)
- Words: prompt 9, help 0

### 117–122. Tick-boxes `paid_2025`: 6 questions on one screen

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

### 123–126. Tick-boxes `paid_more`: 4 questions on one screen

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

### 127–131. Tick-boxes `rare_deductions`: 5 questions on one screen

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

### 132–133. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 134–139. Tick-boxes `home_school`: 6 questions on one screen

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

### 140. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 34, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 141. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 0

### 142. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 143. `f1040.tax_exempt_interest`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> How much tax-exempt interest did you get in 2025, for example from a city or state bond? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 38. Help begins: “Box 8 of Form 1099-INT, and tax-exempt amounts on Form 1099-OID (boxes 2 and 11), less any bond premium.”

### 144. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 145. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 38, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 146–150. Tick-boxes `sales_rare`: 5 questions on one screen

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

### 151–152. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your investments?
>
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (23, 24 words) and help (34, 37)

### 153. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 154–159. Tick-boxes `outside_us`: 6 questions on one screen

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

### 160–162. Tick-boxes `rare_credits`: 3 questions on one screen

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

### 163. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 164–166. Tick-boxes `other_taxes`: 3 questions on one screen

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

### 167. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 168. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 169. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 170. `f1095a[form_1].in_a_jan`

**⟶ topic switch (returns)**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — January, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 15, help 0

### 171. `f1095a[form_1].in_b_jan`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — January, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for January.

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 172. `f1095a[form_1].in_a_feb`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — February, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 15, help 0

### 173. `f1095a[form_1].in_b_feb`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — February, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for February.

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 174. `f1095a[form_1].in_a_mar`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — March, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 15, help 0

### 175. `f1095a[form_1].in_b_mar`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — March, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for March.

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 176. `f1095a[form_1].in_a_apr`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — April, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 15, help 0

### 177. `f1095a[form_1].in_b_apr`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — April, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for April.

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 178. `f1095a[form_1].in_a_may`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — May, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 179. `f1095a[form_1].in_b_may`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — May, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for May.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 180. `f1095a[form_1].in_a_jun`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — June, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 181. `f1095a[form_1].in_b_jun`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — June, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for June.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 182. `f1095a[form_1].in_a_jul`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — July, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 183. `f1095a[form_1].in_b_jul`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — July, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for July.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 184. `f1095a[form_1].in_a_aug`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — August, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 185. `f1095a[form_1].in_b_aug`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — August, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for August.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 186. `f1095a[form_1].in_a_sep`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — September, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 187. `f1095a[form_1].in_b_sep`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — September, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for September.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 188. `f1095a[form_1].in_a_oct`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — October, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 189. `f1095a[form_1].in_b_oct`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — October, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for October.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 190. `f1095a[form_1].in_a_nov`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — November, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 191. `f1095a[form_1].in_b_nov`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — November, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for November.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 192. `f1095a[form_1].in_a_dec`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — December, column A (the monthly premium). Zero if it is blank.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 193. `f1095a[form_1].in_b_dec`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: Form 1095-A

> On this Form 1095-A — December, column B. If it is blank or wrong, the correct amount from HealthCare.gov/Tax-Tool; zero if column A is blank for December.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 26, help 27. Help begins: “Column B is the monthly premium of the second lowest cost silver plan (SLCSP).”

### 194. `qbi.prior_form`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 195. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 196–197. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 18, labels 21. Behind each box, optional to read: the question's own prompt (26, 20 words) and help (39, 22)

### 198. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

## The end reached

**Complete.** The return is completed after 198 questions.

## Totals

| | |
|---|---|
| Questions asked | 198 |
| Steps (screens; a tick-box group shown together is one) | 124 |
| Answered by the persona / by the background / opened and unanswered | 91 / 107 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 3195 |
| Help words (optional to read) | 5137 |
| Words of the answers offered (Yes and No not counted) | 178 |
| Questions answered no, zero or none | 168 |
| Topics met | 31 |
| Topic switches | 64 |
| of them, returns to a topic already left | 34 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 70 | `person[taxpayer].f8889[hsa].months_eligible` | 74 | 8 |
| 99 | `f8962.midmonth_start` (its own prompt, behind a tick-box) | 40 | No |
| 145 | `$sales` | 38 | none (an empty list) |
| 156 | `sb.trust_any` (its own prompt, behind a tick-box) | 38 | No |
| 147 | `sd.sec1256` (its own prompt, behind a tick-box) | 36 | No |
| 39 | `f2441.care` (its own prompt, behind a tick-box) | 35 | No |
| 119 | `sa.state_tax_other_any` (its own prompt, behind a tick-box) | 34 | No |
| 140 | `$sc@person[taxpayer]` | 34 | none (an empty list) |
| 149 | `sd.small_business_stock` (its own prompt, behind a tick-box) | 34 | No |
| 75 | `person[taxpayer].f8889[hsa].testing_prior` | 33 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                         6w  ["taxpayer"]                  [person]
> *  2  f1040.status                                    9w  "single"                      [f1040]
>    3  household.ever_married                          5w  false                         [household]
     4  household.community_property                   20w  false
>>*  5  person[taxpayer].birth_year                     6w  1991                          [person]
>    6  sa.dependent                                   15w  false                         [sa]
>>   7  person[taxpayer].blind                         25w  false                         [person]
>    8  scope.noncitizen                               16w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                             12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                             12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                                11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                           8w  false                         [s3]
>   13  $dependent                                     30w  []                            [dependent]
>>  14  s3.adoption_any                                19w+ false                         [s3]  (screen 11, child_extras)
>>  15  scope.f8814                                    11w+ false                         [scope]  (screen 11, child_extras)
    16  scope.rental                                   19w+ false                         (screen 12, own_income)
    17  scope.k1                                       12w+ false                         (screen 12, own_income)
    18  scope.farm                                      6w+ false                         (screen 12, own_income)
>>  19  person[taxpayer].rrta                          13w+ false                         [person]  (screen 13, work_kind)
    20  person[taxpayer].eligible_educator             11w+ false                         (screen 13, work_kind)
> * 21  $w2@person[taxpayer]                            8w  ["logistics_co"]              [w2]
  * 22  person[taxpayer].w2[logistics_co].box1          6w  4200000
  * 23  person[taxpayer].w2[logistics_co].box2          6w  460000
  * 24  person[taxpayer].w2[logistics_co].box4          6w  260400
  * 25  person[taxpayer].w2[logistics_co].box5          6w  4200000
  * 26  person[taxpayer].w2[logistics_co].box6          5w  60900
> * 27  s2.w2_marks                                    22w+ false                         [s2]  (screen 20, w2_jobs)
> * 28  s1.nqdc_pension                                12w+ false                         [s1]  (screen 20, w2_jobs)
>>* 29  scope.w2_marks                                 10w+ false                         [scope]  (screen 20, w2_jobs)
  * 30  scope.artist_official                          12w+ false                         (screen 20, w2_jobs)
  * 31  scope.excess_deferral                          12w+ false                         (screen 20, w2_jobs)
    32  scope.pay_no_w2                                24w+ false                         (screen 21, other_pay)
    33  scope.medicaid_waiver                          11w+ false                         (screen 21, other_pay)
    34  scope.religious_work                           12w+ false                         (screen 21, other_pay)
>   35  f8959.territory_w2                             10w+ false                         [f8959]  (screen 21, other_pay)
>>  36  s2.options_any                                 11w+ false                         [s2]  (screen 21, other_pay)
>   37  s1a.tips                                       12w+ false                         [s1a]  (screen 22, tips_overtime)
    38  s1a.overtime                                    2w+ false                         (screen 22, tips_overtime)
>   39  f2441.care                                     20w+ false                         [f2441]  (screen 23, care_help)
    40  f2441.benefits                                 12w+ false                         (screen 23, care_help)
>>  41  s2.household_help                              12w+ false                         [s2]  (screen 23, care_help)
>>  42  s1.uc_any                                      10w+ false                         [s1]  (screen 24, money_a)
    43  s1.winnings_any                                 9w+ false                         (screen 24, money_a)
    44  s1.scholarship_any                              9w+ false                         (screen 24, money_a)
    45  s1.jury_any                                     6w+ false                         (screen 24, money_a)
    46  s1.alaska_any                                   5w+ false                         (screen 24, money_a)
    47  s1.hobby_any                                   11w+ false                         (screen 24, money_a)
    48  s1.alimony_any                                 16w+ false                         (screen 25, money_b)
    49  s1.cod_any                                     11w+ false                         (screen 25, money_b)
    50  s1.ltc_payout                                  12w+ false                         (screen 25, money_b)
    51  s1.inmate_wages                                12w+ false                         (screen 25, money_b)
    52  s1.digital_income                              12w+ false                         (screen 25, money_b)
>>  53  scope.recovery                                 12w+ false                         [scope]  (screen 25, money_b)
>   54  refund.any                                     13w  false                         [refund]
>   55  $retirement@person[taxpayer]                   31w  []                            [retirement]
>>  56  person[taxpayer].ira_owner                     17w+ false                         [person]  (screen 28, accounts)
    57  person[taxpayer].inherited_account             11w+ false                         (screen 28, accounts)
    58  person[taxpayer].x_edu_account                 12w+ false                         (screen 28, accounts)
    59  person[taxpayer].x_archer_excess               11w+ false                         (screen 28, accounts)
>   60  ssb.any                                        23w  false                         [ssb]
> * 61  $f8889@person[taxpayer]                        15w  ["hsa"]                       [f8889]
  * 62  person[taxpayer].f8889[hsa].owner_died          9w  false
  * 63  person[taxpayer].f8889[hsa].inherited          13w  false
  * 64  person[taxpayer].f8889[hsa].archer             11w  false
  * 65  person[taxpayer].f8889[hsa].line9              18w  160000
  * 66  person[taxpayer].f8889[hsa].line2              21w  0
  * 67  person[taxpayer].f8889[hsa].ira_transfer       13w  false
  * 68  person[taxpayer].f8889[hsa].excess_withdrawn   25w  false
  * 69  person[taxpayer].f8889[hsa].coverage_year      20w  "changed"
  * 70  person[taxpayer].f8889[hsa].months_eligible    74w  8
  * 71  person[taxpayer].f8889[hsa].months_family      31w  0
  * 72  person[taxpayer].f8889[hsa].dec_coverage        8w  "self_only"
  * 73  person[taxpayer].f8889[hsa].last_month         17w  false
  * 74  person[taxpayer].f8889[hsa].ira_prior          13w  false
  * 75  person[taxpayer].f8889[hsa].testing_prior      33w  false
  * 76  person[taxpayer].f8889[hsa].line14a            11w  45000
  * 77  person[taxpayer].f8889[hsa].dist_code          21w  false
  * 78  person[taxpayer].f8889[hsa].rollover           20w  0
  * 79  person[taxpayer].f8889[hsa].mistake_repaid     14w  false
  * 80  person[taxpayer].f8889[hsa].medical_all        24w  true
  * 81  person[taxpayer].f8889[hsa].loan               26w  false
>>* 82  person[taxpayer].x_hsa_prior_excess            28w  false                         [person]
>>  83  scope.disaster_distribution                    21w+ false                         [scope]  (screen 52, rare_accounts)
    84  scope.archer_msa                               11w+ false                         (screen 52, rare_accounts)
>>  85  s2.hsa_testing                                 11w+ false                         [s2]  (screen 52, rare_accounts)
>>  86  scope.education_recapture                      11w+ false                         [scope]  (screen 52, rare_accounts)
> * 87  $f1095a                                        21w  ["form_1"]                    [f1095a]
> * 88  f8962.shared_policy                            25w+ false                         [f8962]  (screen 54, mkt_people)
  * 89  f8962.divorced_enrolled                        11w+ false                         (screen 54, mkt_people)
  * 90  f8962.no_family                                11w+ false                         (screen 54, mkt_people)
  * 91  f8962.not_lawful                               10w+ false                         (screen 54, mkt_people)
  * 92  f8962.incarcerated                             10w+ false                         (screen 54, mkt_people)
  * 93  f8962.medicaid_reversed                        29w  false
  * 94  f8962.other_coverage                           26w  false
  * 95  f8962.hra                                      28w  false
  * 96  f8962.unpaid                                   20w+ false                         (screen 58, mkt_premiums)
  * 97  f8962.a_zero_paid                              12w+ false                         (screen 58, mkt_premiums)
  * 98  f8962.premium_refunded                         10w+ false                         (screen 58, mkt_premiums)
  * 99  f8962.midmonth_start                           11w+ false                         (screen 58, mkt_premiums)
>>*100  f1095a[form_1].void                            31w  false                         [f1095a]
  *101  f1095a[form_1].same_months                     30w  false
  *102  f1095a[form_1].b_blank                         20w  false
  *103  f1095a[form_1].b_changed                       31w  false
  *104  f1095a[form_1].in_c_jan                        16w  21000
  *105  f1095a[form_1].in_c_feb                        16w  21000
  *106  f1095a[form_1].in_c_mar                        16w  21000
  *107  f1095a[form_1].in_c_apr                        16w  21000
  *108  f1095a[form_1].in_c_may                        16w  0
  *109  f1095a[form_1].in_c_jun                        16w  0
  *110  f1095a[form_1].in_c_jul                        16w  0
  *111  f1095a[form_1].in_c_aug                        16w  0
  *112  f1095a[form_1].in_c_sep                        16w  0
  *113  f1095a[form_1].in_c_oct                        16w  0
  *114  f1095a[form_1].in_c_nov                        16w  0
  *115  f1095a[form_1].in_c_dec                        16w  0
>>*116  f8962.fpl_table                                 9w  "contiguous"                  [f8962]
>> 117  sa.home_owner                                  20w+ false                         [sa]  (screen 76, paid_2025)
   118  sa.state_tax_any                               10w+ false                         (screen 76, paid_2025)
   119  sa.state_tax_other_any                         12w+ false                         (screen 76, paid_2025)
   120  sa.personal_property_tax_any                   12w+ false                         (screen 76, paid_2025)
   121  sa.gifts                                       11w+ false                         (screen 76, paid_2025)
   122  sa.medical_any                                 10w+ false                         (screen 76, paid_2025)
   123  sa.home_other                                  21w+ false                         (screen 77, paid_more)
   124  sa.gift_carryover                              12w+ false                         (screen 77, paid_more)
   125  sa.medical_premiums                            12w+ false                         (screen 77, paid_more)
>  126  sd.casualty                                    12w+ false                         [sd]  (screen 77, paid_more)
>> 127  sa.estate_tax_income                           19w+ false                         [sa]  (screen 78, rare_deductions)
   128  sa.bond_premium                                12w+ false                         (screen 78, rare_deductions)
   129  sa.debt_instrument_loss                        10w+ false                         (screen 78, rare_deductions)
   130  sa.pension_unrecovered                         11w+ false                         (screen 78, rare_deductions)
   131  sa.impairment_work                             12w+ false                         (screen 78, rare_deductions)
   132  sa.elect_itemize                               16w+ false                         (screen 79, deduction_wishes)
   133  sa.sales_tax_wish                              12w+ false                         (screen 79, deduction_wishes)
>> 134  s1a.carloan                                    21w+ false                         [s1a]  (screen 80, home_school)
>> 135  s3.ev                                          11w+ false                         [s3]  (screen 80, home_school)
   136  s3.kerosene                                     9w+ false                         (screen 80, home_school)
>  137  f5695.any                                      11w+ false                         [f5695]  (screen 80, home_school)
>  138  f8863.paid                                     12w+ false                         [f8863]  (screen 80, home_school)
>  139  sli.any                                         6w+ false                         [sli]  (screen 80, home_school)
>  140  $sc@person[taxpayer]                           34w  []                            [sc]
>> 141  scope.business_before                          25w  false                         [scope]
>  142  $interest                                      21w  []                            [interest]
>>*143  f1040.tax_exempt_interest                      20w  0                             [f1040]
>  144  div.any                                        21w  false                         [div]
>  145  $sales                                         38w  []                            [sales]
>> 146  sd.sold_other                                  25w+ false                         [sd]  (screen 87, sales_rare)
   147  sd.sec1256                                     12w+ false                         (screen 87, sales_rare)
   148  sd.condemned                                    9w+ false                         (screen 87, sales_rare)
   149  sd.small_business_stock                        12w+ false                         (screen 87, sales_rare)
   150  sd.trader_election                              9w+ false                         (screen 87, sales_rare)
   151  sd.carryover                                   20w+ false                         (screen 88, invest_other)
>  152  f4952.has_interest                             12w+ false                         [f4952]  (screen 88, invest_other)
>> 153  s3.foreign_any                                 24w  false                         [s3]
>  154  sb.account_any                                 27w+ false                         [sb]  (screen 90, outside_us)
   155  sb.asset_any                                   11w+ false                         (screen 90, outside_us)
   156  sb.trust_any                                    9w+ false                         (screen 90, outside_us)
   157  sb.company_any                                 12w+ false                         (screen 90, outside_us)
   158  sb.territory_any                               10w+ false                         (screen 90, outside_us)
>> 159  scope.foreign_shares                           12w+ false                         [scope]  (screen 90, outside_us)
>> 160  s3.credit_bond                                 19w+ false                         [s3]  (screen 91, rare_credits)
   161  s3.farmland                                     2w+ false                         (screen 91, rare_credits)
   162  s3.repaid_income                               11w+ false                         (screen 91, rare_credits)
   163  s3.prior_other_forms                           25w  false
>> 164  s2.credit_recapture                            20w+ false                         [s2]  (screen 93, other_taxes)
   165  s2.amt_owed                                     3w+ false                         (screen 93, other_taxes)
   166  s2.other_tax                                    9w+ false                         (screen 93, other_taxes)
>  167  $oi8z                                          21w  []                            [oi8z]
>> 168  scope.reforestation                            22w  false                         [scope]
   169  scope.attorney_fees                            21w  false
>>*170  f1095a[form_1].in_a_jan                        15w  38500                         [f1095a]
  *171  f1095a[form_1].in_b_jan                        26w  41000
  *172  f1095a[form_1].in_a_feb                        15w  38500
  *173  f1095a[form_1].in_b_feb                        26w  41000
  *174  f1095a[form_1].in_a_mar                        15w  38500
  *175  f1095a[form_1].in_b_mar                        26w  41000
  *176  f1095a[form_1].in_a_apr                        15w  38500
  *177  f1095a[form_1].in_b_apr                        26w  41000
  *178  f1095a[form_1].in_a_may                        15w  0
  *179  f1095a[form_1].in_b_may                        26w  0
  *180  f1095a[form_1].in_a_jun                        15w  0
  *181  f1095a[form_1].in_b_jun                        26w  0
  *182  f1095a[form_1].in_a_jul                        15w  0
  *183  f1095a[form_1].in_b_jul                        26w  0
  *184  f1095a[form_1].in_a_aug                        15w  0
  *185  f1095a[form_1].in_b_aug                        26w  0
  *186  f1095a[form_1].in_a_sep                        15w  0
  *187  f1095a[form_1].in_b_sep                        26w  0
  *188  f1095a[form_1].in_a_oct                        15w  0
  *189  f1095a[form_1].in_b_oct                        26w  0
  *190  f1095a[form_1].in_a_nov                        15w  0
  *191  f1095a[form_1].in_b_nov                        26w  0
  *192  f1095a[form_1].in_a_dec                        15w  0
  *193  f1095a[form_1].in_b_dec                        26w  0
>  194  qbi.prior_form                                 19w  false                         [qbi]
   195  qbi.coop_patron                                19w  false
>> 196  f1040.withheld_other_any                       29w+ false                         [f1040]  (screen 123, paid_already)
   197  f1040.estimated_any                            10w+ false                         (screen 123, paid_already)
>> 198  s3.line10                                      20w  0                             [s3]
```
