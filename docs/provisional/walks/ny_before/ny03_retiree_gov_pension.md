# Walk: ny03_retiree_gov_pension

A retired married couple in Manhattan all of 2025, 71 and 69, filing together, with social security, a New York City pension (a Form 1099-R), bank interest and some fund dividends.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/ny03_retiree_gov_pension.yaml` (extending `04_retired_couple`): the built interview (profile `ny`, the federal questions, then the New York ones, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

## The walk

### 1. `$person`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`)

> Who is this tax return for?

- Offered: “Just me” / “Me and my husband or wife, together on one return”
- Answer: “Me and my husband or wife, together on one return” (persona)
- Words: prompt 6, help 51. Help begins: “Choose “together” if you are married and the two of you are filing one return, even if only one of you had income.”

### 2. `household.married_dec31`

**⟶ topic switch**

Topic: Household facts for dependents and head of household (`household`)

> Were you married on December 31, 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 7, help 49. Help begins: “A divorce that was not yet final on December 31 means you were still married; a final decree of divorce, legal separation or annulment means you were not.”

### 3. `person[spouse].birth_year`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — In what year was your spouse born?

- Offered: a whole number
- Answer: 1956 (persona)
- Words: prompt 10, help 0

### 4. `person[taxpayer].birth_year`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — In what year were you born?

- Offered: a whole number
- Answer: 1954 (persona)
- Words: prompt 8, help 0

### 5. `sa.dependent`

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Can a parent or anyone else claim you or your spouse as a dependent on their 2025 return?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 18, help 36. Help begins: “It is whether they can, not whether they do.”

### 6. `person[spouse].blind`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Was your spouse blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 29, help 44. Help begins: “The statement must say that your spouse's better eye sees no better than 20/200 with glasses or contact lenses, or that your spouse's field of vision is 20 degrees or less, or that your spouse's sight is not likely to improve beyond those limits.”

### 7. `person[taxpayer].blind`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Were you blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 41. Help begins: “The statement must say that your better eye sees no better than 20/200 with glasses or contact lenses, or that your field of vision is 20 degrees or less, or that your sight is not likely to improve beyond those limits.”

### 8–11. Tick-boxes `about_you`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Schedule A — supported itemized deductions and standard comparison (`sa`)

> Is any of these true of you or your spouse?
>
> - [ ] Not a U.S. citizen at some time in 2025  (`scope.noncitizen`)
> - [ ] In the U.S. armed forces, reserves or National Guard since January 2022  (`scope.armed_forces`)
> - [ ] Leaving out income earned abroad, in Puerto Rico or in American Samoa  (`sa.excluded_income`)
> - [ ] In a chapter 11 bankruptcy case at some time in 2025  (`scope.chapter11`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 10, labels 44. Behind each box, optional to read: the question's own prompt (14, 22, 29, 16 words) and help (0, 0, 36, 25)

### 12. `$dependent`

**⟶ topic switch**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`)

> In 2025, did children live with you, or did you or your spouse support anyone else, such as a parent, another relative or a partner? List each one, or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 33, help 42. Help begins: “Any label you will recognize will do, such as “Child 1”; a name is not needed.”

### 13–14. Tick-boxes `child_extras`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`); Proof-of-concept scope screening (`scope`)

> Does either of these apply to you or your spouse?
>
> - [ ] Adopted a child, or paid adoption costs, since the start of 2024  (`s3.adoption_any`)
> - [ ] Reporting a child's 2025 interest or dividends on your own return  (`scope.f8814`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 10, labels 23. Behind each box, optional to read: the question's own prompt (19, 24 words) and help (18, 28)

### 15–17. Tick-boxes `own_income`: 3 questions on one screen

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you or your spouse have any of these?
>
> - [ ] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [ ] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 29. Behind each box, optional to read: the question's own prompt (30, 30, 14 words) and help (6, 6, 25)

### 18–19. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Did either of these describe your spouse's work in 2025?
>
> - [ ] Worked for a railroad  (`person[spouse].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[spouse].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 13, labels 15. Behind each box, optional to read: the question's own prompt (12, 34 words) and help (28, 0)

### 20. `$w2@person[spouse]`

**⟶ topic switch**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: Your spouse

> About your spouse — Which employers gave your spouse a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 12, help 34. Help begins: “Name each employer once.”

### 21–22. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Did either of these describe your work in 2025?
>
> - [ ] Worked for a railroad  (`person[taxpayer].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[taxpayer].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 15. Behind each box, optional to read: the question's own prompt (10, 32 words) and help (27, 0)

### 23. `$w2@person[taxpayer]`

**⟶ topic switch (returns)**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: You

> About you — Which employers gave you a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 10, help 32. Help begins: “Name each employer once.”

### 24–28. Tick-boxes `other_pay`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Form 8959 — Additional Medicare Tax on wages and self-employment income (`f8959`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you or your spouse have any of these kinds of work or pay?
>
> - [ ] Wages, tips or strike benefits that are not on a W-2  (`scope.pay_no_w2`)
> - [ ] Medicaid pay for caring for someone who lives in your home  (`scope.medicaid_waiver`)
> - [ ] Pay for work for a church or religious body, or as clergy  (`scope.religious_work`)
> - [ ] A wage statement from Puerto Rico or another U.S. territory  (`f8959.territory_w2`)
> - [ ] Employer stock options used to buy shares, or such shares sold  (`s2.options_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 16, labels 55. Behind each box, optional to read: the question's own prompt (19, 21, 28, 19, 22 words) and help (38, 17, 17, 13, 21)

### 29–30. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you or your spouse get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 14, labels 3. Behind each box, optional to read: the question's own prompt (12, 12 words) and help (33, 21)

### 31. `person[spouse].work_ssn`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Does your spouse have a social security number that allows your spouse to work in the United States?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 21, help 40. Help begins: “A card that says “Not Valid for Employment” does not.”

### 32. `person[taxpayer].work_ssn`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Do you have a social security number that allows you to work in the United States?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 18, help 40. Help begins: “A card that says “Not Valid for Employment” does not.”

### 33–35. Tick-boxes `care_help`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you or your spouse have any of these?
>
> - [ ] Care for a child or a dependent, so that you could work  (`f2441.care`)
> - [ ] An employer's help with care costs, such as a dependent care account  (`f2441.benefits`)
> - [ ] Someone you paid to work in your home: a nanny, housekeeper, gardener  (`s2.household_help`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 36. Behind each box, optional to read: the question's own prompt (38, 31, 27 words) and help (33, 42, 24)

### 36–41. Tick-boxes `money_a`: 6 questions on one screen

**⟶ topic switch**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> In 2025, did you or your spouse get any of these?
>
> - [x] Unemployment benefits  (`s1.uc_any`)
> - [ ] Gambling or lottery winnings, or a prize or award  (`s1.winnings_any`)
> - [ ] A scholarship, a fellowship or a grant for study  (`s1.scholarship_any`)
> - [ ] Pay for serving on a jury  (`s1.jury_any`)
> - [ ] An Alaska Permanent Fund dividend  (`s1.alaska_any`)
> - [ ] Money from a hobby or pastime not run as a business  (`s1.hobby_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Unemployment benefits”; the others recorded No (background)
- Words: heading 11, labels 42. Behind each box, optional to read: the question's own prompt (10, 23, 17, 13, 13, 21 words) and help (7, 17, 14, 0, 0, 0)

### 42. `s1.uc_paid`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> How much unemployment did you or your spouse get in 2025? Add up box 1 of each Form 1099-G.

- Offered: a dollar amount, zero or more
- Answer: $50,000.00 (background)
- Words: prompt 19, help 10. Help begins: “If box 1 is wrong, give the amount actually paid.”

### 43. `s1.uc_repaid`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> How much of that did you or your spouse pay back in 2025 because you were overpaid?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 17, help 19. Help begins: “Give 0 if you paid none back.”

### 44. `s1.uc_unsupported`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Did you or your spouse ever pay into a state unemployment fund yourself, or pay back in 2025 unemployment benefits of an earlier year?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 45. Help begins: “Paying in means money taken from your wages for the fund, as a few states require, or payments for coverage you chose as a self-employed person.”

### 45–50. Tick-boxes `money_b`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Did any of these happen to you or your spouse?
>
> - [ ] Alimony paid or received since the start of 2023  (`s1.alimony_any`)
> - [ ] A debt canceled or forgiven by a lender or card company  (`s1.cod_any`)
> - [ ] A long-term care insurance payout, or life insurance paid early, in 2025  (`s1.ltc_payout`)
> - [ ] Pay in 2025 for work done while in a jail or prison  (`s1.inmate_wages`)
> - [ ] Crypto received as pay, as a reward, or from mining or staking  (`s1.digital_income`)
> - [ ] A deducted amount paid back to you (not a state tax refund)  (`scope.recovery`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 10, labels 68. Behind each box, optional to read: the question's own prompt (26, 18, 24, 17, 23, 26 words) and help (22, 18, 11, 6, 21, 35)

### 51. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you or your spouse get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 16, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 52. `$retirement@person[spouse]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: Your spouse

> About your spouse — In 2025, did your spouse take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R your spouse received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 36, help 21. Help begins: “List a Form RRB-1099-R too.”

### 53. `$retirement@person[taxpayer]`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> About you — In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: the list `pension` (persona)
- Words: prompt 33, help 21. Help begins: “List a Form RRB-1099-R too.”

### 54. `person[taxpayer].retirement[pension].account`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> What kind of account did this money come from?

- Offered: “A pension, an annuity, or a 401(k), 403(b) or 457(b) plan (the box “IRA/SEP/SIMPLE” is not ticked)” / “A traditional IRA, a SEP IRA or a SIMPLE IRA (the box “IRA/SEP/SIMPLE” is ticked)” / “A Roth IRA”
- Answer: “A pension, an annuity, or a 401(k), 403(b) or 457(b) plan (the box “IRA/SEP/SIMPLE” is not ticked)” (`plan`) (persona)
- Words: prompt 9, help 12. Help begins: “The form has a small box marked “IRA/SEP/SIMPLE” next to box 7.”

### 55. `person[taxpayer].retirement[pension].code`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Which code is in box 7 of this form?

- Offered: “7 (normal distribution)” / “1 (early distribution, no known exception)” / “2 (early distribution, exception applies)” / “3 (disability)” / “4 (death)” / “G (direct rollover)” / “Q (qualified distribution from a Roth IRA)” / “S (early distribution from a SIMPLE IRA in its first 2 years)” / “Any other code, two codes together (such as 7D or 4G), or no code at all (a Form RRB-1099-R has none)”
- Answer: “7 (normal distribution)” (`normal_7`) (persona)
- Words: prompt 9, help 0

### 56. `person[taxpayer].retirement[pension].under59`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Were you under age 59½ when you received any of this money?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 12, help 0

### 57. `person[taxpayer].retirement[pension].rollover_any`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Did any of this money go into a retirement account again (a rollover or a conversion), even if it was paid to you first?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 24, help 16. Help begins: “Money moved into a Roth IRA counts.”

### 58–63. Tick-boxes `plan_payment`: 6 questions on one screen

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Is any of these true of this pension or plan payment?
>
> - [ ] It was taken out, or paid back, because of a declared disaster  (`person[taxpayer].retirement[pension].disaster`)
> - [ ] The form has an amount in box 6  (`person[taxpayer].retirement[pension].box6`)
> - [ ] Part of it is an unpaid plan loan taken off your balance  (`person[taxpayer].retirement[pension].loan_offset`)
> - [ ] You get this pension because you became disabled  (`person[taxpayer].retirement[pension].disability`)
> - [ ] You want a retired public safety officer's exclusion for insurance premiums  (`person[taxpayer].retirement[pension].pso_exclusion`)
> - [ ] The person who earned it was born before January 2, 1936  (`person[taxpayer].retirement[pension].born_1936`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 11, labels 62. Behind each box, optional to read: the question's own prompt (18, 16, 25, 9, 32, 23 words) and help (36, 16, 16, 0, 17, 0)

### 64. `person[taxpayer].retirement[pension].cost_any`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 29, help 7. Help begins: “If you are not sure, answer Yes.”

### 65. `person[taxpayer].retirement[pension].box1`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Gross distribution, Form 1099-R box 1

- Offered: a dollar amount, zero or more
- Answer: $24,000.00 (persona)
- Words: prompt 6, help 0

### 66. `person[taxpayer].retirement[pension].box5`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You › retirement pension

> Employee contributions, designated Roth contributions or insurance premiums, Form 1099-R box 5 (a pension or annuity; zero for an IRA)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 0

### 67–70. Tick-boxes `accounts`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Does your spouse have any of these accounts?
>
> - [ ] An IRA of any kind (traditional, Roth, SEP or SIMPLE)  (`person[spouse].ira_owner`)
> - [ ] An IRA or workplace retirement account inherited from someone who died  (`person[spouse].inherited_account`)
> - [ ] A 529 plan, Coverdell or ABLE account (your spouse's or held for your spouse)  (`person[spouse].x_edu_account`)
> - [ ] An Archer MSA still holding money put in above its limit  (`person[spouse].x_archer_excess`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 46. Behind each box, optional to read: the question's own prompt (16, 22, 31, 32 words) and help (42, 11, 28, 16)

### 71–74. Tick-boxes `accounts`: 4 questions on one screen

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Do you have any of these accounts?
>
> - [ ] An IRA of any kind (traditional, Roth, SEP or SIMPLE)  (`person[taxpayer].ira_owner`)
> - [ ] An IRA or workplace retirement account inherited from someone who died  (`person[taxpayer].inherited_account`)
> - [ ] A 529 plan, Coverdell or ABLE account (yours or held for you)  (`person[taxpayer].x_edu_account`)
> - [ ] An Archer MSA still holding money put in above its limit  (`person[taxpayer].x_archer_excess`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 44. Behind each box, optional to read: the question's own prompt (14, 20, 28, 30 words) and help (40, 11, 25, 16)

### 75. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you or your spouse get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 26, help 0

### 76. `ssb.benefits`

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Total of box 5 (net benefits) of all your or your spouse's Forms SSA-1099 and RRB-1099 for 2025

- Offered: a dollar amount, zero or more
- Answer: $41,000.00 (persona)
- Words: prompt 18, help 0

### 77–79. Tick-boxes `ssb_facts`: 3 questions on one screen

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Is any of these true of the social security benefits?
>
> - [ ] Box 4 of a Form SSA-1099 is more than box 3  (`ssb.repaid_more`)
> - [ ] Put money into a traditional IRA while covered by a work plan  (`ssb.ira_covered`)
> - [ ] They include a payment for an earlier year (box 3 says so)  (`ssb.prior_year_pay`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 10, labels 35. Behind each box, optional to read: the question's own prompt (22, 24, 31 words) and help (16, 16, 0)

### 80. `ssb.terror_disability`

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Are any of these benefits disability payments for injuries from a terrorist attack against the United States or its allies?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 20, help 41. Help begins: “For the September 11 attacks, count any injury eligible for coverage by the September 11 Victim Compensation Fund, whether or not you made a claim.”

### 81. `$f8889@person[spouse]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: Your spouse

> About your spouse — Did your spouse have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 19, help 52. Help begins: “Signs of one: the letter W in box 12 of your spouse's Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 82. `$f8889@person[taxpayer]`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> About you — Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 17, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 83–86. Tick-boxes `rare_accounts`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did any of these apply to you or your spouse?
>
> - [ ] Have a 2023 or 2024 disaster withdrawal still being taxed or repaid  (`scope.disaster_distribution`)
> - [ ] Put money into an Archer MSA (an older medical savings account)  (`scope.archer_msa`)
> - [ ] Over-contributed to an HSA for 2024, with no HSA in 2025  (`s2.hsa_testing`)
> - [ ] Got tuition refunded for a year an education credit was claimed  (`scope.education_recapture`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 12, labels 45. Behind each box, optional to read: the question's own prompt (34, 25, 32, 25 words) and help (23, 14, 42, 14)

### 87. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you or your spouse, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 24, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 88–93. Tick-boxes `paid_2025`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> In 2025, did you or your spouse do any of these?
>
> - [ ] Owned a home, condo or land at any time in the year  (`sa.home_owner`)
> - [ ] Had state or local income tax taken out of pay  (`sa.state_tax_any`)
> - [ ] Paid other state or local income tax, or a state disability fund  (`sa.state_tax_other_any`)
> - [ ] Paid a yearly tax on a car or boat, based on value  (`sa.personal_property_tax_any`)
> - [ ] Gave money or things to charity, or paid costs of volunteering  (`sa.gifts`)
> - [ ] Paid medical bills, after insurance, above 7.5% of your income  (`sa.medical_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 67. Behind each box, optional to read: the question's own prompt (17, 26, 37, 31, 24, 24 words) and help (31, 0, 39, 24, 39, 32)

### 94–97. Tick-boxes `paid_more`: 4 questions on one screen

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`); Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Do any of these apply to you or your spouse for 2025?
>
> - [ ] Paid interest on a boat or camper loan or another person's mortgage  (`sa.home_other`)
> - [ ] Have a gift to charity from an earlier year still being deducted  (`sa.gift_carryover`)
> - [ ] Paid for your own health insurance, not through a job (Medicare, COBRA)  (`sa.medical_premiums`)
> - [ ] Had property damaged, destroyed or stolen (a loss, or an insurance gain)  (`sd.casualty`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 12, labels 48. Behind each box, optional to read: the question's own prompt (36, 31, 27, 29 words) and help (34, 39, 39, 43)

### 98–102. Tick-boxes `rare_deductions`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do any of these uncommon things apply to you or your spouse?
>
> - [ ] Reported inherited income on which federal estate tax was paid  (`sa.estate_tax_income`)
> - [ ] Have premium left to deduct on a bond bought above face value  (`sa.bond_premium`)
> - [ ] Lost money on an inflation-protected or contingent-payment bond held directly  (`sa.debt_instrument_loss`)
> - [ ] This return is for someone who died with unrecovered pension contributions  (`sa.pension_unrecovered`)
> - [ ] Have a disability and pay for help or equipment needed to work  (`sa.impairment_work`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 12, labels 55. Behind each box, optional to read: the question's own prompt (30, 35, 34, 27, 30 words) and help (36, 24, 31, 37, 27)

### 103–104. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 105–110. Tick-boxes `home_school`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`); Schedule 3 — selected lines (`s3`); Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`); Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits) (`f8863`); Student Loan Interest Deduction Worksheet—Schedule 1, Line 21 (`sli`)

> And in 2025, did you or your spouse do any of these?
>
> - [ ] Paid interest on a loan for a car bought new in 2025  (`s1a.carloan`)
> - [ ] Got an electric or plug-in vehicle, or installed a home charger  (`s3.ev`)
> - [ ] Used kerosene at home for heat, light or cooking  (`s3.kerosene`)
> - [ ] Had solar, insulation, windows, doors or heating equipment installed at home  (`f5695.any`)
> - [ ] Had college or trade school tuition paid, for you or a dependent  (`f8863.paid`)
> - [ ] Paid interest on a student loan  (`sli.any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 12, labels 61. Behind each box, optional to read: the question's own prompt (22, 25, 13, 30, 23, 13 words) and help (37, 19, 0, 34, 32, 18)

### 111. `$sc@person[spouse]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: Your spouse

> About your spouse — In 2025, did your spouse work for himself or herself: freelance or gig work, a side business, or a business of your spouse's own? Add one entry for each business; leave the list empty if your spouse did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 42, help 29. Help begins: “Pay reported to your spouse on Form 1099-NEC, 1099-K or 1099-MISC for your spouse's own work is usually such a business.”

### 112. `$sc@person[taxpayer]`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> About you — In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 36, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 113. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you or your spouse own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 28, help 0

### 114. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you or your spouse interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: the list `credit_union` (persona)
- Words: prompt 24, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 115. `interest[credit_union].amount`

Topic: Schedule B — interest payer entries (`interest`). About: interest credit_union

> How much taxable interest did this payer pay in 2025? On a Form 1099-INT it is box 1 plus box 3 (interest on U.S. savings bonds and Treasury securities). Leave out tax-exempt interest (box 8).

- Offered: a dollar amount, zero or more
- Answer: $850.00 (persona)
- Words: prompt 35, help 0

### 116. `interest[credit_union].penalty`

Topic: Schedule B — interest payer entries (`interest`). About: interest credit_union

> Penalty on early withdrawal of savings this payer charged you (box 2 of Form 1099-INT, or the early withdrawal penalty shown on Form 1099-OID); zero if none. Do not subtract it from the interest.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 34, help 17. Help begins: “Enter the full taxable interest as interest; the penalty is deducted separately, on Schedule 1 line 18.”

### 117. `f1040.tax_exempt_interest`

**⟶ topic switch**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> How much tax-exempt interest did you or your spouse get in 2025, for example from a city or state bond? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 23, help 38. Help begins: “Box 8 of Form 1099-INT, and tax-exempt amounts on Form 1099-OID (boxes 2 and 11), less any bond premium.”

### 118. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you or your spouse own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 24, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 119. `sb.ordinary_dividends`

**⟶ topic switch**

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> Add up box 1a (total ordinary dividends) of all your or your spouse's Forms 1099-DIV for 2025. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $2,100.00 (persona)
- Words: prompt 20, help 49. Help begins: “A broker's combined statement counts as a Form 1099-DIV.”

### 120. `f1040.line3a`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 3a

> Add up box 1b (qualified dividends) of the same forms. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $1,600.00 (persona)
- Words: prompt 13, help 39. Help begins: “Box 1b is a part of box 1a.”

### 121. `sd.distributions`

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Capital gain distributions, generally Form 1099-DIV box 2a

- Offered: a dollar amount, zero or more
- Answer: $400.00 (persona)
- Words: prompt 8, help 30. Help begins: “The total of box 2a of every Form 1099-DIV and substitute statement in your or your spouse's name, including amounts reinvested, plus any capital gain distributions received without a form.”

### 122. `qbi.dividends`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Add up box 5 (section 199A dividends) of the same forms. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 14, help 27. Help begins: “Box 5 is a part of box 1a, usually from real estate funds (REITs).”

### 123. `div.box12`

**⟶ topic switch (returns)**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> Exempt-interest dividends, box 12 (total of all your Forms 1099-DIV; box 13 amounts are already included)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 16, help 12. Help begins: “Enter the amounts of all your and your spouse's Forms 1099-DIV combined.”

### 124. `div.other_boxes`

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> Look at your or your spouse's Forms 1099-DIV for 2025. Does any of them show an amount in box 2b, 2c, 2d, 2e, 2f, 3, 9, 10 or 13?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 29, help 22. Help begins: “Most forms show amounts only in boxes 1a, 1b, 2a, 5, 7 and 12.”

### 125. `sd.f2439`

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Did a mutual fund or a real estate investment trust (REIT) send you or your spouse a Form 2439 for 2025, a notice of gains it kept and paid tax on?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 31, help 16. Help begins: “A return with this is outside what this tool prepares; a Yes ends the interview here.”

### 126. `sb.nominee`

**⟶ topic switch (returns)**

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> Does any of the interest or dividends you or your spouse received in 2025 belong to someone else, for example to the other owner of a joint account who is not your spouse?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 33, help 34. Help begins: “Interest and dividends on an account you own with your spouse are all yours on a joint return.”

### 127. `sb.bonds_any`

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> In 2025, did you or your spouse own bonds or notes directly (not through a fund), cash in U.S. savings bonds, or receive interest on money you lent or on a property you sold?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 34, help 25. Help begins: “Interest from a bank account, a certificate of deposit or a fund is not what this asks about.”

### 128. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you or your spouse sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 41, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 129–133. Tick-boxes `sales_rare`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> In 2025, did you or your spouse have any of these less common sales or trades?
>
> - [ ] Sold real estate or business property, or got installments from any sale  (`sd.sold_other`)
> - [ ] Traded futures, foreign currency contracts or index options, or held a straddle  (`sd.sec1256`)
> - [ ] Had business or investment property taken by a government  (`sd.condemned`)
> - [ ] Lost money on small-company stock and claim it as an ordinary loss  (`sd.small_business_stock`)
> - [ ] Trade securities as a business under a mark-to-market election  (`sd.trader_election`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 16, labels 54. Behind each box, optional to read: the question's own prompt (36, 39, 23, 37, 21 words) and help (29, 34, 28, 37, 39)

### 134–135. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your or your spouse's investments?
>
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 24. Behind each box, optional to read: the question's own prompt (26, 27 words) and help (34, 37)

### 136. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you or your spouse ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 137. `ftc.taxes`

**⟶ topic switch**

Topic: Foreign tax credit — election without Form 1116 (`ftc`)

> How much foreign tax did you or your spouse pay in 2025? Add up box 7 of your Forms 1099-DIV, box 6 of your Forms 1099-INT, and any income tax you paid to another country yourself. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 39, help 13. Help begins: “Count only income taxes, after any reduction the foreign tax credit rules require.”

### 138–143. Tick-boxes `outside_us`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule B — supported interest and ordinary dividends (`sb`); Proof-of-concept scope screening (`scope`)

> At any time in 2025, did you or your spouse have any of these outside the United States?
>
> - [ ] An account in another country, or the power to sign for one  (`sb.account_any`)
> - [ ] Other property abroad, or money owed to you by someone abroad  (`sb.asset_any`)
> - [ ] A tie to a trust or family foundation abroad  (`sb.trust_any`)
> - [ ] A foreign company you help run, or own 10% or more of  (`sb.company_any`)
> - [ ] An account, investment, company or trust in a U.S. territory  (`sb.territory_any`)
> - [ ] Shares of a foreign company or fund, held outside a U.S. fund  (`scope.foreign_shares`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 18, labels 66. Behind each box, optional to read: the question's own prompt (31, 27, 41, 35, 28, 30 words) and help (35, 42, 30, 26, 23, 15)

### 144–146. Tick-boxes `rare_credits`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you or your spouse do any of these?
>
> - [ ] Got a federal tax credit from a bond or a fund  (`s3.credit_bond`)
> - [ ] Sold farmland  (`s3.farmland`)
> - [ ] Paid back more than $3,000 of income from an earlier year  (`s3.repaid_income`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 24. Behind each box, optional to read: the question's own prompt (19, 9, 22 words) and help (17, 9, 35)

### 147. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your or your spouse's 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 28, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 148–150. Tick-boxes `other_taxes`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> Do you or your spouse owe any of these for 2025?
>
> - [ ] A tax credit from an earlier year that must be paid back  (`s2.credit_recapture`)
> - [ ] Alternative minimum tax  (`s2.amt_owed`)
> - [ ] Another federal tax you have not been asked about  (`s2.other_tax`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 24. Behind each box, optional to read: the question's own prompt (19, 11, 19 words) and help (37, 38, 43)

### 151. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you or your spouse had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 24, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 152. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you or your spouse own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 153. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you or your spouse pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 154. `qbi.prior_form`

**⟶ topic switch (returns)**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your or your spouse's 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 155. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you or your spouse sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 156–157. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you or your spouse pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 21, labels 21. Behind each box, optional to read: the question's own prompt (29, 23 words) and help (39, 22)

### 158. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you or your spouse pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 23, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

### 159. `s3.elderly_credit`

Topic: Schedule 3 — selected lines (`s3`)

> Do you or your spouse want to claim the credit for the elderly or the disabled (Schedule R)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 18, help 75. Help begins: “Asked because someone on this return is 65 or older, or retired on disability.”

### 160. `ny_it201.ask.state_resident`

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

### 161. `ny_it201.ask.city_resident`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Were you (and your spouse, on a joint return) a New York City resident (the Bronx, Brooklyn, Manhattan, Queens or Staten Island) for all of 2025, by the same test with New York City in place of New York State?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 40, help 43. Help begins: “The New York City resident tax applies to full-year City residents; the test is the State test with New York City (the five boroughs) in place of New York State.”

### 162. `ny_it201.ask.spouse_resident`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> On your joint return, was your spouse also a full-year New York State and New York City resident?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 18, help 38. Help begins: “On a joint federal return, New York requires both spouses to be residents for this return; otherwise you file separate New York returns or a joint return as if both were residents, which this tool does not do.”

### 163. `ny_it201.ask.special_accrual`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does this apply to you or your spouse: the person was a New York City nonresident on December 31, 2024, or will be a New York State or City nonresident on January 1, 2026, and has income fixed and determinable in one tax year but reported federally in another (accrued income)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 51, help 50. Help begins: “If you moved into or out of New York City or State around the turn of the year, income earned in one period but reported federally in another (for example a bonus fixed in 2025 but paid in 2026) needs the special accrual rules, which this tool does not apply.”

### 164. `ny_it201.ask.yonkers`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you or your spouse maintain living quarters in Yonkers for any part of 2025, or work in Yonkers while not living there (item D2)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 21. Help begins: “Living quarters or wages in Yonkers bring the Yonkers resident surcharge or nonresident earnings tax, which this tool does not compute.”

### 165. `ny_it201.ask.special_code`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does any New York special condition code (item G) apply to you or your spouse? Examples: A6 Build America Bond interest, C7 combat zone, D9 death of spouse, E3 or E4 an extension, C2 an installment payment agreement, M4 to M9 a military residence election, Y1.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 46, help 31. Help begins: “Special condition codes mark situations such as Build America Bond interest, a combat zone, a filing extension, an installment agreement or a military residence election; this tool does not handle them.”

### 166. `ny_it201.ask.decedent`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Is this return for a taxpayer (or spouse) who died after December 31, 2024?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 14, help 11. Help begins: “A return for a taxpayer who died is outside this tool.”

### 167. `ny_it201.ask.item_c`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Can you be claimed as a dependent on another taxpayer's federal return? Answer Yes even if the other taxpayer did not claim you (item C).

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 35. Help begins: “Answer Yes if another taxpayer could claim you as a dependent on their federal return, even if they did not.”

### 168. `ny_it201.ask.inflation_check`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you or your spouse receive an inflation refund check from the New York State Tax Department and include it in federal adjusted gross income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 43. Help begins: “New York mailed inflation refund checks in the fall of 2025.”

### 169. `ny_it201.ask.out_of_state_bond_interest`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you or your spouse have interest or dividends from bonds of states other than New York or their local governments, or from tax-exempt mutual or money market funds that invest in them, that was not included in federal adjusted gross income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 42, help 27. Help begins: “Interest from municipal bonds of other states (or tax-exempt funds holding them) is exempt federally but taxed by New York; this tool does not compute that addition.”

### 170. `ny_it201.ask.414h`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Are you or your spouse a public employee of New York State or its local governments who is a member of one of the retirement systems below, with 414(h) retirement contributions shown on a Form W-2?
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
- Words: prompt 133, help 23. Help begins: “Members of these New York public retirement systems add back 414(h) contributions shown on Form W-2; this tool does not compute that addition.”

### 171. `ny_it201.ask.529_nonqualified`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you or your spouse make a withdrawal during 2025 from an account under New York's 529 college savings program that is nonqualified for New York?
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
- Words: prompt 163, help 45. Help begins: “New York's list of qualified uses is narrower than the federal one, so a withdrawal that is tax-free federally can still be nonqualified for New York.”

### 172. `ny_it201.ask.it225`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Does any other New York addition or subtraction on Form IT-225 apply to you or your spouse, for example modifications passed through from a partnership, S corporation, estate or trust, the disability income exclusion (S-124), combat pay (S-118), a net operating loss (A-215) or an accumulation distribution reported on federal Form 4970?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 52, help 28. Help begins: “Form IT-225 holds the New York modifications not printed on Form IT-201 (many come from a partnership, S corporation, estate or trust); this tool does not compute them.”

### 173. `ny_it201.ask.gov_pension`

Topic: Form IT-201 (2025), Resident Income Tax Return — New York State and New York City (`ny_it201`)

> Did you or your spouse receive a pension or other distribution included in federal adjusted gross income from a New York State or local government pension plan or a federal government pension plan, including a return of your own contributions before retirement? Count the military, a U.S. territory or the District of Columbia, the MTA Police 20-Year Retirement Program, MABSTOA, the Long Island Rail Road, and the Optional Retirement Program of SUNY, CUNY or the State Education Department (for example an annuity paid by TIAA), whether received as an employee, as a beneficiary, or as a former spouse under a domestic relations order.

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 103, help 18. Help begins: “New York exempts New York State, local and federal government pensions; this tool does not compute the subtraction.”

## The end reached

**Refused** at the gate `ny_it201.gate.line26`, after 173 questions. The wording shown:

> Form IT-201 line 26
>
> This subtraction is not computed by this tool (decision B4).

## Totals

| | |
|---|---|
| Questions asked | 173 |
| Steps (screens; a tick-box group shown together is one) | 99 |
| Answered by the persona / by the background / opened and unanswered | 45 / 128 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 3498 |
| Help words (optional to read) | 4375 |
| Words of the answers offered (Yes and No not counted) | 143 |
| Questions answered no, zero or none | 149 |
| Topics met | 32 |
| New York stretch (questions of New York forms): questions / steps / prompt words / help words | 14 / 14 / 845 / 487 |
| Topic switches | 67 |
| of them, returns to a topic already left | 36 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 171 | `ny_it201.ask.529_nonqualified` | 163 | No |
| 170 | `ny_it201.ask.414h` | 133 | No |
| 160 | `ny_it201.ask.state_resident` | 108 | Yes |
| 173 | `ny_it201.ask.gov_pension` | 103 | Yes |
| 172 | `ny_it201.ask.it225` | 52 | No |
| 163 | `ny_it201.ask.special_accrual` | 51 | No |
| 165 | `ny_it201.ask.special_code` | 46 | No |
| 111 | `$sc@person[spouse]` | 42 | none (an empty list) |
| 169 | `ny_it201.ask.out_of_state_bond_interest` | 42 | No |
| 128 | `$sales` | 41 | none (an empty list) |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                               6w  ["taxpayer","spouse"]         [person]
> *  2  household.married_dec31                               7w  true                          [household]
>>*  3  person[spouse].birth_year                            10w  1956                          [person]
  *  4  person[taxpayer].birth_year                           8w  1954
>    5  sa.dependent                                         18w  false                         [sa]
>>   6  person[spouse].blind                                 29w  false                         [person]
     7  person[taxpayer].blind                               27w  false
>    8  scope.noncitizen                                     19w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                                   12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                                   12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                                      11w+ false                         [scope]  (screen 8, about_you)
>   12  $dependent                                           33w  []                            [dependent]
>   13  s3.adoption_any                                      22w+ false                         [s3]  (screen 10, child_extras)
>>  14  scope.f8814                                          11w+ false                         [scope]  (screen 10, child_extras)
    15  scope.rental                                         22w+ false                         (screen 11, own_income)
    16  scope.k1                                             12w+ false                         (screen 11, own_income)
    17  scope.farm                                            6w+ false                         (screen 11, own_income)
>>  18  person[spouse].rrta                                  17w+ false                         [person]  (screen 12, work_kind)
    19  person[spouse].eligible_educator                     11w+ false                         (screen 12, work_kind)
>   20  $w2@person[spouse]                                   12w  []                            [w2]
>>  21  person[taxpayer].rrta                                15w+ false                         [person]  (screen 14, work_kind)
    22  person[taxpayer].eligible_educator                   11w+ false                         (screen 14, work_kind)
>>  23  $w2@person[taxpayer]                                 10w  []                            [w2]
>>  24  scope.pay_no_w2                                      27w+ false                         [scope]  (screen 16, other_pay)
    25  scope.medicaid_waiver                                11w+ false                         (screen 16, other_pay)
    26  scope.religious_work                                 12w+ false                         (screen 16, other_pay)
>   27  f8959.territory_w2                                   10w+ false                         [f8959]  (screen 16, other_pay)
>   28  s2.options_any                                       11w+ false                         [s2]  (screen 16, other_pay)
>   29  s1a.tips                                             15w+ false                         [s1a]  (screen 17, tips_overtime)
    30  s1a.overtime                                          2w+ false                         (screen 17, tips_overtime)
>>* 31  person[spouse].work_ssn                              21w  true                          [person]
  * 32  person[taxpayer].work_ssn                            18w  true
>   33  f2441.care                                           23w+ false                         [f2441]  (screen 20, care_help)
    34  f2441.benefits                                       12w+ false                         (screen 20, care_help)
>>  35  s2.household_help                                    12w+ false                         [s2]  (screen 20, care_help)
>   36  s1.uc_any                                            13w+ true                          [s1]  (screen 21, money_a)
    37  s1.winnings_any                                       9w+ false                         (screen 21, money_a)
    38  s1.scholarship_any                                    9w+ false                         (screen 21, money_a)
    39  s1.jury_any                                           6w+ false                         (screen 21, money_a)
    40  s1.alaska_any                                         5w+ false                         (screen 21, money_a)
    41  s1.hobby_any                                         11w+ false                         (screen 21, money_a)
    42  s1.uc_paid                                           19w  5000000
    43  s1.uc_repaid                                         17w  0
    44  s1.uc_unsupported                                    24w  false
    45  s1.alimony_any                                       19w+ false                         (screen 25, money_b)
    46  s1.cod_any                                           11w+ false                         (screen 25, money_b)
    47  s1.ltc_payout                                        12w+ false                         (screen 25, money_b)
    48  s1.inmate_wages                                      12w+ false                         (screen 25, money_b)
    49  s1.digital_income                                    12w+ false                         (screen 25, money_b)
>>  50  scope.recovery                                       12w+ false                         [scope]  (screen 25, money_b)
>   51  refund.any                                           16w  false                         [refund]
>   52  $retirement@person[spouse]                           36w  []                            [retirement]
  * 53  $retirement@person[taxpayer]                         33w  ["pension"]
  * 54  person[taxpayer].retirement[pension].account          9w  "plan"
  * 55  person[taxpayer].retirement[pension].code             9w  "normal_7"
  * 56  person[taxpayer].retirement[pension].under59         12w  false
  * 57  person[taxpayer].retirement[pension].rollover_any    24w  false
  * 58  person[taxpayer].retirement[pension].disaster        23w+ false                         (screen 33, plan_payment)
  * 59  person[taxpayer].retirement[pension].box6             8w+ false                         (screen 33, plan_payment)
  * 60  person[taxpayer].retirement[pension].loan_offset     12w+ false                         (screen 33, plan_payment)
  * 61  person[taxpayer].retirement[pension].disability       8w+ false                         (screen 33, plan_payment)
  * 62  person[taxpayer].retirement[pension].pso_exclusion   11w+ false                         (screen 33, plan_payment)
  * 63  person[taxpayer].retirement[pension].born_1936       11w+ false                         (screen 33, plan_payment)
  * 64  person[taxpayer].retirement[pension].cost_any        29w  false
  * 65  person[taxpayer].retirement[pension].box1             6w  2400000
  * 66  person[taxpayer].retirement[pension].box5            20w  0
>>  67  person[spouse].ira_owner                             21w+ false                         [person]  (screen 37, accounts)
    68  person[spouse].inherited_account                     11w+ false                         (screen 37, accounts)
    69  person[spouse].x_edu_account                         14w+ false                         (screen 37, accounts)
    70  person[spouse].x_archer_excess                       11w+ false                         (screen 37, accounts)
    71  person[taxpayer].ira_owner                           19w+ false                         (screen 38, accounts)
    72  person[taxpayer].inherited_account                   11w+ false                         (screen 38, accounts)
    73  person[taxpayer].x_edu_account                       12w+ false                         (screen 38, accounts)
    74  person[taxpayer].x_archer_excess                     11w+ false                         (screen 38, accounts)
> * 75  ssb.any                                              26w  true                          [ssb]
  * 76  ssb.benefits                                         18w  4100000
  * 77  ssb.repaid_more                                      21w+ false                         (screen 41, ssb_facts)
  * 78  ssb.ira_covered                                      12w+ false                         (screen 41, ssb_facts)
  * 79  ssb.prior_year_pay                                   12w+ false                         (screen 41, ssb_facts)
  * 80  ssb.terror_disability                                20w  false
>   81  $f8889@person[spouse]                                19w  []                            [f8889]
    82  $f8889@person[taxpayer]                              17w  []
>>  83  scope.disaster_distribution                          24w+ false                         [scope]  (screen 45, rare_accounts)
    84  scope.archer_msa                                     11w+ false                         (screen 45, rare_accounts)
>>  85  s2.hsa_testing                                       11w+ false                         [s2]  (screen 45, rare_accounts)
>>  86  scope.education_recapture                            11w+ false                         [scope]  (screen 45, rare_accounts)
>   87  $f1095a                                              24w  []                            [f1095a]
>>  88  sa.home_owner                                        23w+ false                         [sa]  (screen 47, paid_2025)
    89  sa.state_tax_any                                     10w+ false                         (screen 47, paid_2025)
    90  sa.state_tax_other_any                               12w+ false                         (screen 47, paid_2025)
    91  sa.personal_property_tax_any                         12w+ false                         (screen 47, paid_2025)
    92  sa.gifts                                             11w+ false                         (screen 47, paid_2025)
    93  sa.medical_any                                       10w+ false                         (screen 47, paid_2025)
    94  sa.home_other                                        24w+ false                         (screen 48, paid_more)
    95  sa.gift_carryover                                    12w+ false                         (screen 48, paid_more)
    96  sa.medical_premiums                                  12w+ false                         (screen 48, paid_more)
>   97  sd.casualty                                          12w+ false                         [sd]  (screen 48, paid_more)
>>  98  sa.estate_tax_income                                 22w+ false                         [sa]  (screen 49, rare_deductions)
    99  sa.bond_premium                                      12w+ false                         (screen 49, rare_deductions)
   100  sa.debt_instrument_loss                              10w+ false                         (screen 49, rare_deductions)
   101  sa.pension_unrecovered                               11w+ false                         (screen 49, rare_deductions)
   102  sa.impairment_work                                   12w+ false                         (screen 49, rare_deductions)
   103  sa.elect_itemize                                     16w+ false                         (screen 50, deduction_wishes)
   104  sa.sales_tax_wish                                    12w+ false                         (screen 50, deduction_wishes)
>> 105  s1a.carloan                                          24w+ false                         [s1a]  (screen 51, home_school)
>> 106  s3.ev                                                11w+ false                         [s3]  (screen 51, home_school)
   107  s3.kerosene                                           9w+ false                         (screen 51, home_school)
>  108  f5695.any                                            11w+ false                         [f5695]  (screen 51, home_school)
>  109  f8863.paid                                           12w+ false                         [f8863]  (screen 51, home_school)
>  110  sli.any                                               6w+ false                         [sli]  (screen 51, home_school)
>  111  $sc@person[spouse]                                   42w  []                            [sc]
   112  $sc@person[taxpayer]                                 36w  []
>> 113  scope.business_before                                28w  false                         [scope]
> *114  $interest                                            24w  ["credit_union"]              [interest]
  *115  interest[credit_union].amount                        35w  85000
  *116  interest[credit_union].penalty                       34w  0
> *117  f1040.tax_exempt_interest                            23w  0                             [f1040]
> *118  div.any                                              24w  true                          [div]
> *119  sb.ordinary_dividends                                20w  210000                        [sb]
>>*120  f1040.line3a                                         13w  160000                        [f1040]
>>*121  sd.distributions                                      8w  40000                         [sd]
> *122  qbi.dividends                                        14w  0                             [qbi]
>>*123  div.box12                                            16w  0                             [div]
  *124  div.other_boxes                                      29w  false
>>*125  sd.f2439                                             31w  false                         [sd]
>>*126  sb.nominee                                           33w  false                         [sb]
  *127  sb.bonds_any                                         34w  false
>  128  $sales                                               41w  []                            [sales]
>> 129  sd.sold_other                                        28w+ false                         [sd]  (screen 70, sales_rare)
   130  sd.sec1256                                           12w+ false                         (screen 70, sales_rare)
   131  sd.condemned                                          9w+ false                         (screen 70, sales_rare)
   132  sd.small_business_stock                              12w+ false                         (screen 70, sales_rare)
   133  sd.trader_election                                    9w+ false                         (screen 70, sales_rare)
   134  sd.carryover                                         23w+ false                         (screen 71, invest_other)
>  135  f4952.has_interest                                   12w+ false                         [f4952]  (screen 71, invest_other)
>> 136  s3.foreign_any                                       27w  false                         [s3]
> *137  ftc.taxes                                            39w  0                             [ftc]
>> 138  sb.account_any                                       30w+ false                         [sb]  (screen 74, outside_us)
   139  sb.asset_any                                         11w+ false                         (screen 74, outside_us)
   140  sb.trust_any                                          9w+ false                         (screen 74, outside_us)
   141  sb.company_any                                       12w+ false                         (screen 74, outside_us)
   142  sb.territory_any                                     10w+ false                         (screen 74, outside_us)
>> 143  scope.foreign_shares                                 12w+ false                         [scope]  (screen 74, outside_us)
>> 144  s3.credit_bond                                       22w+ false                         [s3]  (screen 75, rare_credits)
   145  s3.farmland                                           2w+ false                         (screen 75, rare_credits)
   146  s3.repaid_income                                     11w+ false                         (screen 75, rare_credits)
   147  s3.prior_other_forms                                 28w  false
>> 148  s2.credit_recapture                                  23w+ false                         [s2]  (screen 77, other_taxes)
   149  s2.amt_owed                                           3w+ false                         (screen 77, other_taxes)
   150  s2.other_tax                                          9w+ false                         (screen 77, other_taxes)
>  151  $oi8z                                                24w  []                            [oi8z]
>> 152  scope.reforestation                                  25w  false                         [scope]
   153  scope.attorney_fees                                  24w  false
>> 154  qbi.prior_form                                       22w  false                         [qbi]
   155  qbi.coop_patron                                      22w  false
>> 156  f1040.withheld_other_any                             32w+ false                         [f1040]  (screen 83, paid_already)
   157  f1040.estimated_any                                  10w+ false                         (screen 83, paid_already)
>> 158  s3.line10                                            23w  0                             [s3]
  *159  s3.elderly_credit                                    18w  false
>  160  ny_it201.ask.state_resident                         108w  true                          [ny_it201]
  *161  ny_it201.ask.city_resident                           40w  true
  *162  ny_it201.ask.spouse_resident                         18w  true
   163  ny_it201.ask.special_accrual                         51w  false
   164  ny_it201.ask.yonkers                                 25w  false
   165  ny_it201.ask.special_code                            46w  false
   166  ny_it201.ask.decedent                                14w  false
   167  ny_it201.ask.item_c                                  25w  false
   168  ny_it201.ask.inflation_check                         25w  false
   169  ny_it201.ask.out_of_state_bond_interest              42w  false
   170  ny_it201.ask.414h                                   133w  false
   171  ny_it201.ask.529_nonqualified                       163w  false
   172  ny_it201.ask.it225                                   52w  false
  *173  ny_it201.ask.gov_pension                            103w  true
```
