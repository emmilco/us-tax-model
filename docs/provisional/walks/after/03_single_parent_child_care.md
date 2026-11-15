# Walk: 03_single_parent_child_care

An unmarried parent, 29, with one child aged 4 who lives with her all year, $26,000 of wages from one job, and day care she pays for so she can work; head of household.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/03_single_parent_child_care.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: “I paid over half the cost of the home of my child, or of a relative I support (head of household)” (`hoh`) (persona)
- Words: prompt 9, help 115. Help begins: “Take the first line that is true for you, with one exception: if you are married but lived apart from your husband or wife for the last six months of 2025 and your child lived with you, look at the line about paying for a home before the first line.”

### 3. `household.ever_married`

**⟶ topic switch**

Topic: Household facts for dependents and head of household (`household`)

> Have you ever been married?

- Offered: Yes / No
- Answer: No (persona)
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
- Answer: 1996 (persona)
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
- Answer: the list `child` (persona)
- Words: prompt 30, help 42. Help begins: “Any label you will recognize will do, such as “Child 1”; a name is not needed.”

### 14. `dependent[child].relationship`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> How is this person related to you?

- Offered: “My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild” / “My brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of my brother, sister, half brother or half sister (a niece or nephew)” / “Another descendant of a brother or sister, such as a grandniece or grandnephew, or a stepbrother's or stepsister's child” / “My father or mother (not a stepparent or foster parent)” / “My grandparent or an earlier ancestor, or a brother or sister of my father or mother (an aunt or uncle)” / “My stepfather or stepmother, or my son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law or sister-in-law, even after a death or divorce” / “Someone else who lived with me all of 2025 as a member of my household, such as a partner, a friend, a cousin or a foster parent” / “Someone else”
- Answer: “My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild” (`child`) (persona)
- Words: prompt 7, help 54. Help begins: “On a joint return, give the relationship to you: your spouse's child is your stepchild, and your spouse's parent, brother or sister is your in-law.”

### 15. `dependent[child].age`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> How old was this person at the end of 2025?

- Offered: a whole number
- Answer: 4 (persona)
- Words: prompt 10, help 8. Help begins: “Enter 0 for a baby born in 2025.”

### 16. `dependent[child].younger`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> Is this person younger than you (or, if you file together, younger than either of you)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 0

### 17–20. Tick-boxes `dependent_facts`: 4 questions on one screen

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> Is any of these true of this person?
>
> - [ ] Lived over half of 2025 with another relative who could claim them  (`dependent[child].other_claimant`)
> - [x] Parents divorced, separated, or apart for the last 6 months of 2025  (`dependent[child].parents_apart`)
> - [ ] Has been married at some time  (`dependent[child].ever_married`)
> - [ ] Had money of their own in 2025, or owned their home  (`dependent[child].own_money`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Parents divorced, separated, or apart for the last 6 months of 2025”; the others recorded No (persona)
- Words: heading 8, labels 41. Behind each box, optional to read: the question's own prompt (36, 20, 6, 27 words) and help (51, 14, 7, 21)

### 21. `dependent[child].lived_all_year`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> Did this person live with you for all of 2025? (For a baby born in 2025, a child adopted or placed with you in 2025, or a person who died in 2025: all of their part of the year.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 39, help 34. Help begins: “Time away at school, on vacation, on business, in hospital, in military service or in juvenile detention counts as living with you.”

### 22. `dependent[child].divorced_rule`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> Has the parent this child lived with for more of 2025 given the right to claim the child to the other parent, by signing Form 8332 or under a divorce decree or separation agreement?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 34, help 34. Help begins: “Answer Yes whichever parent you are.”

### 23. `dependent[child].citizen_ssn`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> Is this person a U.S. citizen with a social security number? (If the card has a restriction printed on it, such as “Not Valid for Employment”, answer No.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 28, help 22. Help begins: “The number must have been issued before the due date of your 2025 return, extensions included; if it was not, answer No.”

### 24. `household.home_cost`

**⟶ topic switch (returns)**

Topic: Household facts for dependents and head of household (`household`)

> Did you pay more than half of what it cost to run your home in 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 59. Help begins: “Count rent or mortgage interest, property tax, home insurance, repairs, utilities and food eaten at home; not clothing, schooling, medical care, vacations, life insurance or transport.”

### 25. `dependent[child].absence_no_return`

**⟶ topic switch (returns)**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> In counting the time this person lived with you, did you count time away that the person, or you, was not expected to come back from, or during which you did not keep up the home?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 36, help 0

### 26–27. Tick-boxes `child_extras`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`); Proof-of-concept scope screening (`scope`)

> Does either of these apply to you?
>
> - [ ] Adopted a child, or paid adoption costs, since the start of 2024  (`s3.adoption_any`)
> - [ ] Reporting a child's 2025 interest or dividends on your own return  (`scope.f8814`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 7, labels 23. Behind each box, optional to read: the question's own prompt (16, 21 words) and help (18, 28)

### 28–30. Tick-boxes `own_income`: 3 questions on one screen

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you have any of these?
>
> - [ ] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [ ] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 29. Behind each box, optional to read: the question's own prompt (27, 27, 11 words) and help (6, 6, 25)

### 31–32. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did either of these describe your work in 2025?
>
> - [ ] Worked for a railroad  (`person[taxpayer].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[taxpayer].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 9, labels 15. Behind each box, optional to read: the question's own prompt (8, 30 words) and help (27, 0)

### 33. `$w2@person[taxpayer]`

**⟶ topic switch**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: You

> Which employers gave you a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: the list `grocer` (persona)
- Words: prompt 8, help 32. Help begins: “Name each employer once.”

### 34. `person[taxpayer].w2[grocer].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 grocer

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $26,000.00 (persona)
- Words: prompt 6, help 0

### 35. `person[taxpayer].w2[grocer].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 grocer

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $900.00 (persona)
- Words: prompt 6, help 0

### 36. `person[taxpayer].w2[grocer].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 grocer

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $1,612.00 (persona)
- Words: prompt 6, help 0

### 37. `person[taxpayer].w2[grocer].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 grocer

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $26,000.00 (persona)
- Words: prompt 6, help 0

### 38. `person[taxpayer].w2[grocer].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 grocer

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $377.00 (persona)
- Words: prompt 5, help 0

### 39–43. Tick-boxes `w2_jobs`: 5 questions on one screen

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

### 44–48. Tick-boxes `other_pay`: 5 questions on one screen

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

### 49–50. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 3. Behind each box, optional to read: the question's own prompt (9, 9 words) and help (33, 21)

### 51. `person[taxpayer].work_ssn`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Do you have a social security number that allows you to work in the United States?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 40. Help begins: “A card that says “Not Valid for Employment” does not.”

### 52–54. Tick-boxes `care_help`: 3 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`); Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you have any of these?
>
> - [x] Care for a child or a dependent, so that you could work  (`f2441.care`)
> - [ ] An employer's help with care costs, such as a dependent care account  (`f2441.benefits`)
> - [ ] Someone you paid to work in your home: a nanny, housekeeper, gardener  (`s2.household_help`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Care for a child or a dependent, so that you could work”; the others recorded No (persona; background)
- Words: heading 8, labels 36. Behind each box, optional to read: the question's own prompt (35, 28, 24 words) and help (33, 42, 24)

### 55–58. Tick-boxes `care_facts`: 4 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`)

> About that care: is any of these true of you?
>
> - [ ] Some care was for someone other than your listed children under 13  (`f2441.care_other`)
> - [ ] Paid a bill in 2025 for care given in 2024  (`f2441.prior_year`)
> - [ ] A full-time student in each of 5 months of 2025  (`f2441.student`)
> - [ ] Unable to care for yourself at some time in 2025  (`f2441.unable`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 10, labels 42. Behind each box, optional to read: the question's own prompt (22, 17, 19, 20 words) and help (42, 6, 6, 23)

### 59. `$dcprov`

**⟶ topic switch**

Topic: Form 2441, Part I — persons or organizations who provided the care, one entry per care provider (`dcprov`)

> Who provided the care in 2025? List each person or organization, one entry each.

- Offered: a list the filer builds, naming each entry
- Answer: the list `bright_start_day_care` (persona)
- Words: prompt 14, help 37. Help begins: “Any name you will recognize will do; the name and address are written on the form itself.”

### 60. `dcprov[bright_start_day_care].paid`

Topic: Form 2441, Part I — persons or organizations who provided the care, one entry per care provider (`dcprov`), line 1(e). About: dcprov bright_start_day_care

> For this care provider — How much did you pay this provider in 2025? Count amounts your employer paid them for you, whichever year the care was given, and do not subtract any money you were paid back. Zero if your employer provided the care itself.

- Offered: a dollar amount, zero or more
- Answer: $6,200.00 (persona)
- Words: prompt 45, help 0

### 61. `dcprov[bright_start_day_care].household`

Topic: Form 2441, Part I — persons or organizations who provided the care, one entry per care provider (`dcprov`), line 1(d). About: dcprov bright_start_day_care

> For this care provider — Was this provider your own employee, working in your home in 2025, as a nanny usually is?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 21, help 36. Help begins: “A person you pay to give care in your home is probably your employee if you decide not only what work is done but how it is done.”

### 62. `dcprov[bright_start_day_care].tin_kind`

Topic: Form 2441, Part I — persons or organizations who provided the care, one entry per care provider (`dcprov`), line 1(c). About: dcprov bright_start_day_care

> For this care provider — Which identifying number did this provider give you?

- Offered: “A social security number, an ITIN or an employer identification number (EIN)” / “None needed: the provider is a tax-exempt organization” / “None: I live abroad, and the provider is foreign and does not need a U.S. number” / “None: I asked, and the provider did not give me the number” / “None needed: my employer provided the care itself, under its dependent care plan”
- Answer: “A social security number, an ITIN or an employer identification number (EIN)” (`tin`) (persona)
- Words: prompt 12, help 31. Help begins: “The number itself is written on the form and is not asked here.”

### 63. `dcprov[bright_start_day_care].related`

Topic: Form 2441, Part I — persons or organizations who provided the care, one entry per care provider (`dcprov`). About: dcprov bright_start_day_care

> For this care provider — Is this provider one of these people?
>
> - a person who was your husband or wife at any time in 2025
> - the other parent of your child under 13 whose care you paid for
> - your child, stepchild or foster child who was under 19 at the end of 2025
> - a person you can claim as a dependent

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 60, help 31. Help begins: “Payments to these people do not count, and a return that lists one of them as a care provider is outside what this tool prepares; a Yes ends the interview here.”

### 64. `dependent[child].dc_paid`

**⟶ topic switch (returns)**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> How much did you pay in 2025 for this person's care in 2025, so that you could work or look for work?
>
> Count day care, a sitter or nanny, preschool, care before and after school and day camp, for the time this person was under 13 or not able to care for themselves.
>
> Count as well:
> - 2025 care that you paid for ahead in 2024
> - your share of the employment taxes on a care provider's wages
> - bills a dependent care account paid back to you, or your employer paid to a provider you chose
> - a housekeeper, cook, maid or cleaner whose work was partly this person's care, with the housekeeper's meals and the extra cost of lodging the housekeeper in your home
> - the care provider's trips with this person to or from the place of care
> - agency fees, application fees and deposits you had to pay to get the care
>
> Leave out:
> - care given in 2024 or 2026, and 2025 care you had not paid for by the end of 2025
> - care your employer provided itself, at your workplace or through a provider it hired
> - school from kindergarten up, summer school, tutoring and overnight camp
> - food, lodging, clothing, schooling and entertainment, unless food or schooling comes with the care and cannot be separated from its cost
> - amounts a state social services agency paid back to you, and expenses you claim as medical expenses
> - payments to your spouse, your child under 19, your dependent, or the parent of your child under 13
> - child support
> - a chauffeur, bartender or gardener, other travel, and a deposit lost for care that was never given
> - care outside your home for anyone but your dependent child under 13, if that person does not regularly spend at least 8 hours a day in your home
> - a care center that does not meet all state and local rules
>
> If you worked or looked for work on only some of the days a bill covers:
> - count only those days (a day with at least 1 hour of work is a day of work)
> - but count the whole bill where you must pay by the week or month whether you work each day or not, and count care paid for during a short break from work, such as a vacation or minor illness (2 weeks or less, or longer in some circumstances)
>
> Volunteer work, or work for a nominal wage, is not work. If a cost was only partly for work, count that part, unless the rest is small. Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $6,200.00 (persona)
- Words: prompt 422, help 0

### 65. `s8812.combat_pay`

**⟶ topic switch**

Topic: Schedule 8812 — Credits for Qualifying Children and Other Dependents (`s8812`)

> In 2025, were you paid for military service in a combat zone? This pay is not taxed; box 12 of the W-2 generally shows it with the letter Q.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 29, help 6. Help begins: “A Yes ends the interview here.”

### 66–71. Tick-boxes `money_a`: 6 questions on one screen

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

### 72–77. Tick-boxes `money_b`: 6 questions on one screen

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

### 78. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 79. `$retirement@person[taxpayer]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 31, help 21. Help begins: “List a Form RRB-1099-R too.”

### 80–83. Tick-boxes `accounts`: 4 questions on one screen

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

### 84. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 0

### 85. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 15, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 86–89. Tick-boxes `rare_accounts`: 4 questions on one screen

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

### 90. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 21, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 91–96. Tick-boxes `paid_2025`: 6 questions on one screen

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

### 97–100. Tick-boxes `paid_more`: 4 questions on one screen

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

### 101–105. Tick-boxes `rare_deductions`: 5 questions on one screen

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

### 106–107. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 108–113. Tick-boxes `home_school`: 6 questions on one screen

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

### 114. `person[taxpayer].tin`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Do you have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 25, help 34. Help begins: “The number must be issued by the date the 2025 return is due, extensions included.”

### 115. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 34, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 116. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 0

### 117. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 118. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 119. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 38, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

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
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 8, labels 24. Behind each box, optional to read: the question's own prompt (23, 24 words) and help (34, 37)

### 127. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 128–133. Tick-boxes `outside_us`: 6 questions on one screen

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

### 134–136. Tick-boxes `rare_credits`: 3 questions on one screen

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

### 137. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 138–140. Tick-boxes `other_taxes`: 3 questions on one screen

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

### 141. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 21, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 142. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 143. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 21, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 144. `qbi.prior_form`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 145. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 146–147. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 18, labels 21. Behind each box, optional to read: the question's own prompt (26, 20 words) and help (39, 22)

### 148. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 20, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

### 149. `household.credit_disallowed`

**⟶ topic switch (returns)**

Topic: Household facts for dependents and head of household (`household`)

> Has the IRS ever reduced or refused a child tax credit, a credit for other dependents or an earned income credit that you claimed, for any reason other than a math or clerical error?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 34, help 39. Help begins: “Count any earlier return, including a joint return with someone else: the earned income credit for 1997 or later, the other credits for 2016 or later.”

### 150. `s8812.puerto_rico`

**⟶ topic switch (returns)**

Topic: Schedule 8812 — Credits for Qualifying Children and Other Dependents (`s8812`)

> In 2025, were you a resident of Puerto Rico (in the tax term, a “bona fide resident”)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 17, help 52. Help begins: “Generally you were one if, during 2025, you met the presence test, had no tax home outside Puerto Rico, and had no closer connection to the United States or to a foreign country than to Puerto Rico (Pub.”

### 151. `dependent[child].us_half`

**⟶ topic switch (returns)**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent child

> Did this person live with you in the United States for more than half of 2025? (For a child born, adopted or placed with you in 2025, or who died in 2025: more than half of their part of the year.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 41, help 47. Help begins: “The United States is the 50 states and the District of Columbia; your home counts as there while you are on extended military duty abroad.”

### 152. `person[taxpayer].eic_ssn`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Do you have a social security number that counts for the earned income credit? Nearly every number does: the help says which do not, if your card says “Not Valid for Employment” or “Valid for Work Only With DHS Authorization”.

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 40, help 52. Help begins: “A card that says “Not Valid for Employment” counts unless the number was issued only to get a federally funded benefit.”

### 153. `f1040.tax_exempt_interest`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> How much tax-exempt interest did you get in 2025, for example from a city or state bond? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 38. Help begins: “Box 8 of Form 1099-INT, and tax-exempt amounts on Form 1099-OID (boxes 2 and 11), less any bond premium.”

### 154. `eic.lived_with_relative`

**⟶ topic switch**

Topic: Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a (`eic`)

> In 2025, did you live for more than half the year in the same home as your parent, grandparent, brother, sister, aunt or uncle, or a foster parent? Count time you were temporarily away, for example at school.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 38, help 18. Help begins: “Stepparents, half brothers and sisters, great-grandparents, great-aunts and great-uncles count too.”

## The end reached

**Complete.** The return is completed after 154 questions.

## Totals

| | |
|---|---|
| Questions asked | 154 |
| Steps (screens; a tick-box group shown together is one) | 81 |
| Answered by the persona / by the background / opened and unanswered | 48 / 106 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 2838 |
| Help words (optional to read) | 3932 |
| Words of the answers offered (Yes and No not counted) | 326 |
| Questions answered no, zero or none | 128 |
| Topics met | 33 |
| Topic switches | 72 |
| of them, returns to a topic already left | 40 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 64 | `dependent[child].dc_paid` | 422 | $6,200.00 |
| 63 | `dcprov[bright_start_day_care].related` | 60 | No |
| 60 | `dcprov[bright_start_day_care].paid` | 45 | $6,200.00 |
| 151 | `dependent[child].us_half` | 41 | Yes |
| 152 | `person[taxpayer].eic_ssn` | 40 | Yes |
| 21 | `dependent[child].lived_all_year` | 39 | Yes |
| 119 | `$sales` | 38 | none (an empty list) |
| 130 | `sb.trust_any` (its own prompt, behind a tick-box) | 38 | No |
| 154 | `eic.lived_with_relative` | 38 | No |
| 17 | `dependent[child].other_claimant` (its own prompt, behind a tick-box) | 36 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                    6w  ["taxpayer"]                  [person]
> *  2  f1040.status                               9w  "hoh"                         [f1040]
> *  3  household.ever_married                     5w  false                         [household]
     4  household.community_property              20w  false
>>*  5  person[taxpayer].birth_year                6w  1996                          [person]
>    6  sa.dependent                              15w  false                         [sa]
>>   7  person[taxpayer].blind                    25w  false                         [person]
>    8  scope.noncitizen                          16w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                        12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                        12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                           11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                      8w  false                         [s3]
> * 13  $dependent                                30w  ["child"]                     [dependent]
  * 14  dependent[child].relationship              7w  "child"
  * 15  dependent[child].age                      10w  4
  * 16  dependent[child].younger                  16w  true
  * 17  dependent[child].other_claimant           20w+ false                         (screen 14, dependent_facts)
  * 18  dependent[child].parents_apart            12w+ true                          (screen 14, dependent_facts)
  * 19  dependent[child].ever_married              6w+ false                         (screen 14, dependent_facts)
  * 20  dependent[child].own_money                11w+ false                         (screen 14, dependent_facts)
  * 21  dependent[child].lived_all_year           39w  true
  * 22  dependent[child].divorced_rule            34w  false
  * 23  dependent[child].citizen_ssn              28w  true
>>* 24  household.home_cost                       16w  true                          [household]
>>* 25  dependent[child].absence_no_return        36w  false                         [dependent]
>>  26  s3.adoption_any                           19w+ false                         [s3]  (screen 20, child_extras)
>>  27  scope.f8814                               11w+ false                         [scope]  (screen 20, child_extras)
    28  scope.rental                              19w+ false                         (screen 21, own_income)
    29  scope.k1                                  12w+ false                         (screen 21, own_income)
    30  scope.farm                                 6w+ false                         (screen 21, own_income)
>>  31  person[taxpayer].rrta                     13w+ false                         [person]  (screen 22, work_kind)
    32  person[taxpayer].eligible_educator        11w+ false                         (screen 22, work_kind)
> * 33  $w2@person[taxpayer]                       8w  ["grocer"]                    [w2]
  * 34  person[taxpayer].w2[grocer].box1           6w  2600000
  * 35  person[taxpayer].w2[grocer].box2           6w  90000
  * 36  person[taxpayer].w2[grocer].box4           6w  161200
  * 37  person[taxpayer].w2[grocer].box5           6w  2600000
  * 38  person[taxpayer].w2[grocer].box6           5w  37700
> * 39  s2.w2_marks                               22w+ false                         [s2]  (screen 29, w2_jobs)
> * 40  s1.nqdc_pension                           12w+ false                         [s1]  (screen 29, w2_jobs)
>>* 41  scope.w2_marks                            10w+ false                         [scope]  (screen 29, w2_jobs)
  * 42  scope.artist_official                     12w+ false                         (screen 29, w2_jobs)
  * 43  scope.excess_deferral                     12w+ false                         (screen 29, w2_jobs)
    44  scope.pay_no_w2                           24w+ false                         (screen 30, other_pay)
    45  scope.medicaid_waiver                     11w+ false                         (screen 30, other_pay)
    46  scope.religious_work                      12w+ false                         (screen 30, other_pay)
>   47  f8959.territory_w2                        10w+ false                         [f8959]  (screen 30, other_pay)
>>  48  s2.options_any                            11w+ false                         [s2]  (screen 30, other_pay)
>   49  s1a.tips                                  12w+ false                         [s1a]  (screen 31, tips_overtime)
    50  s1a.overtime                               2w+ false                         (screen 31, tips_overtime)
>>* 51  person[taxpayer].work_ssn                 16w  true                          [person]
> * 52  f2441.care                                20w+ true                          [f2441]  (screen 33, care_help)
    53  f2441.benefits                            12w+ false                         (screen 33, care_help)
>>  54  s2.household_help                         12w+ false                         [s2]  (screen 33, care_help)
>>* 55  f2441.care_other                          22w+ false                         [f2441]  (screen 34, care_facts)
  * 56  f2441.prior_year                          10w+ false                         (screen 34, care_facts)
  * 57  f2441.student                             10w+ false                         (screen 34, care_facts)
  * 58  f2441.unable                              10w+ false                         (screen 34, care_facts)
> * 59  $dcprov                                   14w  ["bright_start_day_care"]     [dcprov]
  * 60  dcprov[bright_start_day_care].paid        45w  620000
  * 61  dcprov[bright_start_day_care].household   21w  false
  * 62  dcprov[bright_start_day_care].tin_kind    12w  "tin"
  * 63  dcprov[bright_start_day_care].related     60w  false
>>* 64  dependent[child].dc_paid                 422w  620000                        [dependent]
> * 65  s8812.combat_pay                          29w  false                         [s8812]
>>  66  s1.uc_any                                 10w+ false                         [s1]  (screen 42, money_a)
    67  s1.winnings_any                            9w+ false                         (screen 42, money_a)
    68  s1.scholarship_any                         9w+ false                         (screen 42, money_a)
    69  s1.jury_any                                6w+ false                         (screen 42, money_a)
    70  s1.alaska_any                              5w+ false                         (screen 42, money_a)
    71  s1.hobby_any                              11w+ false                         (screen 42, money_a)
    72  s1.alimony_any                            16w+ false                         (screen 43, money_b)
    73  s1.cod_any                                11w+ false                         (screen 43, money_b)
    74  s1.ltc_payout                             12w+ false                         (screen 43, money_b)
    75  s1.inmate_wages                           12w+ false                         (screen 43, money_b)
    76  s1.digital_income                         12w+ false                         (screen 43, money_b)
>>  77  scope.recovery                            12w+ false                         [scope]  (screen 43, money_b)
>   78  refund.any                                13w  false                         [refund]
>   79  $retirement@person[taxpayer]              31w  []                            [retirement]
>>  80  person[taxpayer].ira_owner                17w+ false                         [person]  (screen 46, accounts)
    81  person[taxpayer].inherited_account        11w+ false                         (screen 46, accounts)
    82  person[taxpayer].x_edu_account            12w+ false                         (screen 46, accounts)
    83  person[taxpayer].x_archer_excess          11w+ false                         (screen 46, accounts)
>   84  ssb.any                                   23w  false                         [ssb]
>   85  $f8889@person[taxpayer]                   15w  []                            [f8889]
>>  86  scope.disaster_distribution               21w+ false                         [scope]  (screen 49, rare_accounts)
    87  scope.archer_msa                          11w+ false                         (screen 49, rare_accounts)
>>  88  s2.hsa_testing                            11w+ false                         [s2]  (screen 49, rare_accounts)
>>  89  scope.education_recapture                 11w+ false                         [scope]  (screen 49, rare_accounts)
>   90  $f1095a                                   21w  []                            [f1095a]
>>  91  sa.home_owner                             20w+ false                         [sa]  (screen 51, paid_2025)
    92  sa.state_tax_any                          10w+ false                         (screen 51, paid_2025)
    93  sa.state_tax_other_any                    12w+ false                         (screen 51, paid_2025)
    94  sa.personal_property_tax_any              12w+ false                         (screen 51, paid_2025)
    95  sa.gifts                                  11w+ false                         (screen 51, paid_2025)
    96  sa.medical_any                            10w+ false                         (screen 51, paid_2025)
    97  sa.home_other                             21w+ false                         (screen 52, paid_more)
    98  sa.gift_carryover                         12w+ false                         (screen 52, paid_more)
    99  sa.medical_premiums                       12w+ false                         (screen 52, paid_more)
>  100  sd.casualty                               12w+ false                         [sd]  (screen 52, paid_more)
>> 101  sa.estate_tax_income                      19w+ false                         [sa]  (screen 53, rare_deductions)
   102  sa.bond_premium                           12w+ false                         (screen 53, rare_deductions)
   103  sa.debt_instrument_loss                   10w+ false                         (screen 53, rare_deductions)
   104  sa.pension_unrecovered                    11w+ false                         (screen 53, rare_deductions)
   105  sa.impairment_work                        12w+ false                         (screen 53, rare_deductions)
   106  sa.elect_itemize                          16w+ false                         (screen 54, deduction_wishes)
   107  sa.sales_tax_wish                         12w+ false                         (screen 54, deduction_wishes)
>> 108  s1a.carloan                               21w+ false                         [s1a]  (screen 55, home_school)
>> 109  s3.ev                                     11w+ false                         [s3]  (screen 55, home_school)
   110  s3.kerosene                                9w+ false                         (screen 55, home_school)
>  111  f5695.any                                 11w+ false                         [f5695]  (screen 55, home_school)
>  112  f8863.paid                                12w+ false                         [f8863]  (screen 55, home_school)
>  113  sli.any                                    6w+ false                         [sli]  (screen 55, home_school)
>>*114  person[taxpayer].tin                      25w  true                          [person]
>  115  $sc@person[taxpayer]                      34w  []                            [sc]
>> 116  scope.business_before                     25w  false                         [scope]
>  117  $interest                                 21w  []                            [interest]
>  118  div.any                                   21w  false                         [div]
>  119  $sales                                    38w  []                            [sales]
>> 120  sd.sold_other                             25w+ false                         [sd]  (screen 62, sales_rare)
   121  sd.sec1256                                12w+ false                         (screen 62, sales_rare)
   122  sd.condemned                               9w+ false                         (screen 62, sales_rare)
   123  sd.small_business_stock                   12w+ false                         (screen 62, sales_rare)
   124  sd.trader_election                         9w+ false                         (screen 62, sales_rare)
   125  sd.carryover                              20w+ false                         (screen 63, invest_other)
>  126  f4952.has_interest                        12w+ false                         [f4952]  (screen 63, invest_other)
>> 127  s3.foreign_any                            24w  false                         [s3]
>  128  sb.account_any                            27w+ false                         [sb]  (screen 65, outside_us)
   129  sb.asset_any                              11w+ false                         (screen 65, outside_us)
   130  sb.trust_any                               9w+ false                         (screen 65, outside_us)
   131  sb.company_any                            12w+ false                         (screen 65, outside_us)
   132  sb.territory_any                          10w+ false                         (screen 65, outside_us)
>> 133  scope.foreign_shares                      12w+ false                         [scope]  (screen 65, outside_us)
>> 134  s3.credit_bond                            19w+ false                         [s3]  (screen 66, rare_credits)
   135  s3.farmland                                2w+ false                         (screen 66, rare_credits)
   136  s3.repaid_income                          11w+ false                         (screen 66, rare_credits)
   137  s3.prior_other_forms                      25w  false
>> 138  s2.credit_recapture                       20w+ false                         [s2]  (screen 68, other_taxes)
   139  s2.amt_owed                                3w+ false                         (screen 68, other_taxes)
   140  s2.other_tax                               9w+ false                         (screen 68, other_taxes)
>  141  $oi8z                                     21w  []                            [oi8z]
>> 142  scope.reforestation                       22w  false                         [scope]
   143  scope.attorney_fees                       21w  false
>  144  qbi.prior_form                            19w  false                         [qbi]
   145  qbi.coop_patron                           19w  false
>> 146  f1040.withheld_other_any                  29w+ false                         [f1040]  (screen 74, paid_already)
   147  f1040.estimated_any                       10w+ false                         (screen 74, paid_already)
>> 148  s3.line10                                 20w  0                             [s3]
>>*149  household.credit_disallowed               34w  false                         [household]
>>*150  s8812.puerto_rico                         17w  false                         [s8812]
>>*151  dependent[child].us_half                  41w  true                          [dependent]
>>*152  person[taxpayer].eic_ssn                  40w  true                          [person]
>>*153  f1040.tax_exempt_interest                 20w  0                             [f1040]
> *154  eic.lived_with_relative                   38w  false                         [eic]
```
