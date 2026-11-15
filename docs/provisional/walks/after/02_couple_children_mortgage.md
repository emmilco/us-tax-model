# Walk: 02_couple_children_mortgage

A married couple filing together, each with one job (two Forms W-2, $95,000 and $68,000), two children aged 3 and 6, and a mortgaged home; they itemize.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/02_couple_children_mortgage.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: 1980 (background)
- Words: prompt 10, help 0

### 4. `person[taxpayer].birth_year`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — In what year were you born?

- Offered: a whole number
- Answer: 1980 (background)
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

### 12. `s3.disability_retired`

**⟶ topic switch**

Topic: Schedule 3 — selected lines (`s3`)

> Have you or your spouse retired on permanent and total disability?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 11, help 23. Help begins: “Yes if a person under 65 had to stop working because of a condition a doctor expects to last at least a year.”

### 13. `$dependent`

**⟶ topic switch**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`)

> In 2025, did children live with you, or did you or your spouse support anyone else, such as a parent, another relative or a partner? List each one, or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: the list `older_child`, `younger_child` (persona)
- Words: prompt 33, help 42. Help begins: “Any label you will recognize will do, such as “Child 1”; a name is not needed.”

### 14. `dependent[older_child].relationship`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> How is this person related to you?

- Offered: “My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild” / “My brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of my brother, sister, half brother or half sister (a niece or nephew)” / “Another descendant of a brother or sister, such as a grandniece or grandnephew, or a stepbrother's or stepsister's child” / “My father or mother (not a stepparent or foster parent)” / “My grandparent or an earlier ancestor, or a brother or sister of my father or mother (an aunt or uncle)” / “My stepfather or stepmother, or my son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law or sister-in-law, even after a death or divorce” / “Someone else who lived with me all of 2025 as a member of my household, such as a partner, a friend, a cousin or a foster parent” / “Someone else”
- Answer: “My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild” (`child`) (persona)
- Words: prompt 7, help 54. Help begins: “On a joint return, give the relationship to you: your spouse's child is your stepchild, and your spouse's parent, brother or sister is your in-law.”

### 15. `dependent[older_child].age`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> How old was this person at the end of 2025?

- Offered: a whole number
- Answer: 6 (persona)
- Words: prompt 10, help 8. Help begins: “Enter 0 for a baby born in 2025.”

### 16. `dependent[older_child].younger`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> Is this person younger than you (or, if you file together, younger than either of you)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 0

### 17–20. Tick-boxes `dependent_facts`: 4 questions on one screen

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> Is any of these true of this person?
>
> - [ ] Lived over half of 2025 with another relative who could claim them  (`dependent[older_child].other_claimant`)
> - [ ] Parents divorced, separated, or apart for the last 6 months of 2025  (`dependent[older_child].parents_apart`)
> - [ ] Has been married at some time  (`dependent[older_child].ever_married`)
> - [ ] Had money of their own in 2025, or owned their home  (`dependent[older_child].own_money`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 8, labels 41. Behind each box, optional to read: the question's own prompt (36, 20, 6, 27 words) and help (51, 14, 7, 21)

### 21. `dependent[older_child].lived_all_year`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> Did this person live with you for all of 2025? (For a baby born in 2025, a child adopted or placed with you in 2025, or a person who died in 2025: all of their part of the year.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 39, help 34. Help begins: “Time away at school, on vacation, on business, in hospital, in military service or in juvenile detention counts as living with you.”

### 22. `dependent[older_child].citizen_ssn`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> Is this person a U.S. citizen with a social security number? (If the card has a restriction printed on it, such as “Not Valid for Employment”, answer No.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 28, help 22. Help begins: “The number must have been issued before the due date of your 2025 return, extensions included; if it was not, answer No.”

### 23. `dependent[younger_child].relationship`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> How is this person related to you?

- Offered: “My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild” / “My brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of my brother, sister, half brother or half sister (a niece or nephew)” / “Another descendant of a brother or sister, such as a grandniece or grandnephew, or a stepbrother's or stepsister's child” / “My father or mother (not a stepparent or foster parent)” / “My grandparent or an earlier ancestor, or a brother or sister of my father or mother (an aunt or uncle)” / “My stepfather or stepmother, or my son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law or sister-in-law, even after a death or divorce” / “Someone else who lived with me all of 2025 as a member of my household, such as a partner, a friend, a cousin or a foster parent” / “Someone else”
- Answer: “My son or daughter (adopted or placed for adoption included), my stepchild, a foster child placed with me by an agency or a court, or a descendant of one of them, such as a grandchild” (`child`) (persona)
- Words: prompt 7, help 54. Help begins: “On a joint return, give the relationship to you: your spouse's child is your stepchild, and your spouse's parent, brother or sister is your in-law.”

### 24. `dependent[younger_child].age`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> How old was this person at the end of 2025?

- Offered: a whole number
- Answer: 3 (persona)
- Words: prompt 10, help 8. Help begins: “Enter 0 for a baby born in 2025.”

### 25. `dependent[younger_child].younger`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Is this person younger than you (or, if you file together, younger than either of you)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 0

### 26–29. Tick-boxes `dependent_facts`: 4 questions on one screen

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Is any of these true of this person?
>
> - [ ] Lived over half of 2025 with another relative who could claim them  (`dependent[younger_child].other_claimant`)
> - [ ] Parents divorced, separated, or apart for the last 6 months of 2025  (`dependent[younger_child].parents_apart`)
> - [ ] Has been married at some time  (`dependent[younger_child].ever_married`)
> - [ ] Had money of their own in 2025, or owned their home  (`dependent[younger_child].own_money`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 8, labels 41. Behind each box, optional to read: the question's own prompt (36, 20, 6, 27 words) and help (51, 14, 7, 21)

### 30. `dependent[younger_child].lived_all_year`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Did this person live with you for all of 2025? (For a baby born in 2025, a child adopted or placed with you in 2025, or a person who died in 2025: all of their part of the year.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 39, help 34. Help begins: “Time away at school, on vacation, on business, in hospital, in military service or in juvenile detention counts as living with you.”

### 31. `dependent[younger_child].citizen_ssn`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Is this person a U.S. citizen with a social security number? (If the card has a restriction printed on it, such as “Not Valid for Employment”, answer No.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 28, help 22. Help begins: “The number must have been issued before the due date of your 2025 return, extensions included; if it was not, answer No.”

### 32–33. Tick-boxes `child_extras`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`); Proof-of-concept scope screening (`scope`)

> Does either of these apply to you or your spouse?
>
> - [ ] Adopted a child, or paid adoption costs, since the start of 2024  (`s3.adoption_any`)
> - [ ] Reporting a child's 2025 interest or dividends on your own return  (`scope.f8814`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 10, labels 23. Behind each box, optional to read: the question's own prompt (19, 24 words) and help (18, 28)

### 34–36. Tick-boxes `own_income`: 3 questions on one screen

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you or your spouse have any of these?
>
> - [ ] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [ ] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 29. Behind each box, optional to read: the question's own prompt (30, 30, 14 words) and help (6, 6, 25)

### 37–38. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Did either of these describe your spouse's work in 2025?
>
> - [ ] Worked for a railroad  (`person[spouse].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[spouse].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 13, labels 15. Behind each box, optional to read: the question's own prompt (12, 34 words) and help (28, 0)

### 39. `$w2@person[spouse]`

**⟶ topic switch**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: Your spouse

> About your spouse — Which employers gave your spouse a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: the list `city_schools` (persona)
- Words: prompt 12, help 34. Help begins: “Name each employer once.”

### 40. `person[spouse].w2[city_schools].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: Your spouse › w2 city_schools

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $68,000.00 (persona)
- Words: prompt 6, help 0

### 41. `person[spouse].w2[city_schools].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: Your spouse › w2 city_schools

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $7,200.00 (persona)
- Words: prompt 6, help 0

### 42. `person[spouse].w2[city_schools].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: Your spouse › w2 city_schools

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $4,216.00 (persona)
- Words: prompt 6, help 0

### 43. `person[spouse].w2[city_schools].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: Your spouse › w2 city_schools

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $68,000.00 (persona)
- Words: prompt 6, help 0

### 44. `person[spouse].w2[city_schools].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: Your spouse › w2 city_schools

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $986.00 (persona)
- Words: prompt 5, help 0

### 45–46. Tick-boxes `work_kind`: 2 questions on one screen

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Did either of these describe your work in 2025?
>
> - [ ] Worked for a railroad  (`person[taxpayer].rrta`)
> - [ ] K–12 teacher, counselor, principal or aide for 900 hours or more  (`person[taxpayer].eligible_educator`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 15. Behind each box, optional to read: the question's own prompt (10, 32 words) and help (27, 0)

### 47. `$w2@person[taxpayer]`

**⟶ topic switch (returns)**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: You

> About you — Which employers gave you a W-2 for 2025?

- Offered: a list the filer builds, naming each entry
- Answer: the list `northside_hospital` (persona)
- Words: prompt 10, help 32. Help begins: “Name each employer once.”

### 48. `person[taxpayer].w2[northside_hospital].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 northside_hospital

> Box 1, wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $95,000.00 (persona)
- Words: prompt 6, help 0

### 49. `person[taxpayer].w2[northside_hospital].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 northside_hospital

> Box 2, federal income tax withheld

- Offered: a dollar amount, zero or more
- Answer: $10,500.00 (persona)
- Words: prompt 6, help 0

### 50. `person[taxpayer].w2[northside_hospital].box4`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 northside_hospital

> Box 4, social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $5,890.00 (persona)
- Words: prompt 6, help 0

### 51. `person[taxpayer].w2[northside_hospital].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 northside_hospital

> Box 5, Medicare wages and tips

- Offered: a dollar amount, zero or more
- Answer: $95,000.00 (persona)
- Words: prompt 6, help 0

### 52. `person[taxpayer].w2[northside_hospital].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 northside_hospital

> Box 6, Medicare tax withheld

- Offered: a dollar amount, zero or more
- Answer: $1,377.50 (persona)
- Words: prompt 5, help 0

### 53–57. Tick-boxes `w2_jobs`: 5 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`); Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Do your or your spouse's W-2s, or the jobs on them, show any of these?
>
> - [ ] An amount in box 8, or box 12 code A/B/K/M/N/Z  (`s2.w2_marks`)
> - [ ] In box 11, money paid to you from a deferred pay plan  (`s1.nqdc_pension`)
> - [ ] Box 12 code H, or box 13 “Statutory employee” ticked  (`scope.w2_marks`)
> - [ ] Work as a performing artist, or as an official paid from fees  (`scope.artist_official`)
> - [ ] More pay put into retirement plans at work than the yearly limit  (`scope.excess_deferral`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (persona)
- Words: heading 15, labels 56. Behind each box, optional to read: the question's own prompt (28, 20, 22, 25, 25 words) and help (27, 18, 6, 0, 34)

### 58–62. Tick-boxes `other_pay`: 5 questions on one screen

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

### 63–64. Tick-boxes `tips_overtime`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> In 2025, did you or your spouse get either of these at a job?
>
> - [ ] Tips  (`s1a.tips`)
> - [ ] Overtime pay  (`s1a.overtime`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 14, labels 3. Behind each box, optional to read: the question's own prompt (12, 12 words) and help (33, 21)

### 65. `person[spouse].work_ssn`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Does your spouse have a social security number that allows your spouse to work in the United States?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 21, help 40. Help begins: “A card that says “Not Valid for Employment” does not.”

### 66. `person[taxpayer].work_ssn`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Do you have a social security number that allows you to work in the United States?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 18, help 40. Help begins: “A card that says “Not Valid for Employment” does not.”

### 67–69. Tick-boxes `care_help`: 3 questions on one screen

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

### 70–75. Tick-boxes `money_a`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> In 2025, did you or your spouse get any of these?
>
> - [ ] Unemployment benefits  (`s1.uc_any`)
> - [ ] Gambling or lottery winnings, or a prize or award  (`s1.winnings_any`)
> - [ ] A scholarship, a fellowship or a grant for study  (`s1.scholarship_any`)
> - [ ] Pay for serving on a jury  (`s1.jury_any`)
> - [ ] An Alaska Permanent Fund dividend  (`s1.alaska_any`)
> - [ ] Money from a hobby or pastime not run as a business  (`s1.hobby_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 42. Behind each box, optional to read: the question's own prompt (10, 23, 17, 13, 13, 21 words) and help (7, 17, 14, 0, 0, 0)

### 76–81. Tick-boxes `money_b`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`); Proof-of-concept scope screening (`scope`)

> Did any of these happen to you or your spouse?
>
> - [ ] Alimony paid or received since the start of 2023  (`s1.alimony_any`)
> - [ ] A debt canceled or forgiven by a lender or card company  (`s1.cod_any`)
> - [ ] A long-term care insurance payout, or life insurance paid early, in 2025  (`s1.ltc_payout`)
> - [ ] Pay in 2025 for work done while in a jail or prison  (`s1.inmate_wages`)
> - [ ] Crypto received as pay, as a reward, or from mining or staking  (`s1.digital_income`)
> - [ ] Paid back a deduction that lowered your tax (not a state refund)  (`scope.recovery`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 10, labels 68. Behind each box, optional to read: the question's own prompt (26, 18, 24, 17, 23, 28 words) and help (22, 18, 11, 6, 21, 60)

### 82. `refund.any`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> In 2025, did you or your spouse get a refund of state or local income tax?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 16, help 36. Help begins: “Count a refund you had applied to your 2025 state tax, or that was taken to pay a debt.”

### 83. `$retirement@person[spouse]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: Your spouse

> About your spouse — In 2025, did your spouse take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R your spouse received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 36, help 21. Help begins: “List a Form RRB-1099-R too.”

### 84. `$retirement@person[taxpayer]`

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> About you — In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 33, help 21. Help begins: “List a Form RRB-1099-R too.”

### 85–88. Tick-boxes `accounts`: 4 questions on one screen

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

### 89–92. Tick-boxes `accounts`: 4 questions on one screen

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

### 93. `ssb.any`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Did you or your spouse get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 26, help 0

### 94. `$f8889@person[spouse]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: Your spouse

> About your spouse — Did your spouse have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 19, help 52. Help begins: “Signs of one: the letter W in box 12 of your spouse's Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 95. `$f8889@person[taxpayer]`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> About you — Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 17, help 51. Help begins: “Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank.”

### 96–99. Tick-boxes `rare_accounts`: 4 questions on one screen

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

### 100. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> In 2025, did you or your spouse, or anyone you claim as a dependent, have health insurance bought through HealthCare.gov or a state Marketplace?

- Offered: “No” / “Yes, with one Form 1095-A” / “Yes, with two Forms 1095-A” / “Yes, with three Forms 1095-A” / “Yes, with four Forms 1095-A” / “Yes, with five Forms 1095-A” / “Yes, with six Forms 1095-A”
- Answer: “No” (background)
- Words: prompt 24, help 43. Help begins: “Each plan has its own Form 1095-A, sent by the Marketplace and kept in your online account there.”

### 101–106. Tick-boxes `paid_2025`: 6 questions on one screen

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> In 2025, did you or your spouse do any of these?
>
> - [x] Owned a home, condo or land at any time in the year  (`sa.home_owner`)
> - [x] Had state or local income tax taken out of pay  (`sa.state_tax_any`)
> - [ ] Paid other state or local income tax, or a state disability fund  (`sa.state_tax_other_any`)
> - [ ] Paid a yearly tax on a car or boat, based on value  (`sa.personal_property_tax_any`)
> - [x] Gave money or things to charity, or paid costs of volunteering  (`sa.gifts`)
> - [ ] Paid medical bills, after insurance, above 7.5% of your income  (`sa.medical_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Owned a home, condo or land at any time in the year”, “Had state or local income tax taken out of pay”, “Gave money or things to charity, or paid costs of volunteering”; the others recorded No (persona; background)
- Words: heading 11, labels 67. Behind each box, optional to read: the question's own prompt (17, 26, 37, 31, 24, 24 words) and help (31, 0, 39, 24, 39, 32)

### 107–108. Tick-boxes `paid_more`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`); Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Do any of these apply to you or your spouse for 2025?
>
> - [ ] Paid for your own health insurance, not through a job (Medicare, COBRA)  (`sa.medical_premiums`)
> - [ ] Had property damaged, destroyed or stolen (a loss, or an insurance gain)  (`sd.casualty`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 12, labels 24. Behind each box, optional to read: the question's own prompt (27, 29 words) and help (39, 43)

### 109. `sa.mortgage_interest`

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> How much home mortgage interest did you or your spouse pay in 2025? Add boxes 1 and 6 of each Form 1098 from your lender.

- Offered: a dollar amount, zero or more
- Answer: $18,900.00 (persona)
- Words: prompt 25, help 37. Help begins: “Form 1098 is the statement a mortgage lender sends in January.”

### 110. `sa.mortgage_unreported`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Did you or your spouse pay mortgage interest or points in 2025 that no Form 1098 shows, for example to a person who sold you the home?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 27, help 29. Help begins: “Interest paid to a bank or a mortgage company is on Form 1098.”

### 111. `sa.mortgage_over_limit`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Did the loans on your home add up to more than $750,000 at any time in 2025, or to more than the home is worth?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 25, help 35. Help begins: “If all of it was borrowed on or before December 15, 2017, the limit is $1,000,000.”

### 112. `sa.mortgage_other_use`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Was any of the money borrowed against your home used for something other than buying, building or improving it, such as paying off other debts?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 25, help 46. Help begins: “A loan used only to buy or build the home, or a refinancing for no more than was still owed on such a loan, is a No.”

### 113. `s3.mcc`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Do you or your spouse have a “mortgage credit certificate” from a state or local housing agency for your home loan?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 21, help 40. Help begins: “It is a paper issued when the loan was made, usually to first-time buyers, and it is not the yearly Form 1098 from the lender.”

### 114. `s2.mortgage_subsidy`

**⟶ topic switch (returns)**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> In 2025, did you or your spouse sell or give away a home bought with a subsidized loan from a state or local housing agency?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 25, help 45. Help begins: “These are first-time buyer loans paid for with mortgage bonds, and loans with a mortgage credit certificate.”

### 115. `sa.line5b`

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> How much property tax did you or your spouse pay in 2025 on your home and on any other real estate you own that is not used for business?

- Offered: a dollar amount, zero or more
- Answer: $5,200.00 (persona)
- Words: prompt 29, help 29. Help begins: “If your lender pays the tax for you, box 10 of Form 1098 or the lender's year-end statement shows what it paid in 2025.”

### 116. `sa.property_tax_other_any`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Does that amount include any of these?
>
> - a charge for a service, such as trash collection or water
> - a charge for an improvement, such as a new sidewalk
> - tax on real estate outside the United States
> - tax a buyer was charged when you sold, or 2025 tax that was refunded to you
> - 2026 tax paid before it was billed
> - a special tax charged only on some properties

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 67, help 43. Help begins: “For most homeowners the answer is No.”

### 117. `sa.line5a`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> How much state and local income tax was taken out of that pay in 2025? Add boxes 17 and 19 of each Form W-2.

- Offered: a dollar amount, zero or more
- Answer: $7,800.00 (persona)
- Words: prompt 24, help 16. Help begins: “Leave out tax you deduct elsewhere, as for a business.”

### 118. `sa.charity_limited`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Were your gifts to charity so large that the law limits what you can deduct for 2025, or is any of them carried over from an earlier year? (A limit can apply only when the year's gifts are more than 20% of your income.)

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 44, help 44. Help begins: “The limits are 20%, 30%, 50% or 60% of your income, by the kind of gift and of charity (Publication 526, "Limits on Deductions").”

### 119. `sa.line11`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> How much money did you or your spouse give to charity in 2025: cash, checks, card payments and payroll deductions? Add what you spent out of pocket as a volunteer, such as mileage, parking and supplies.

- Offered: a dollar amount, zero or more
- Answer: $3,100.00 (persona)
- Words: prompt 36, help 46. Help begins: “Zero if you gave only things.”

### 120. `$gift`

**⟶ topic switch**

Topic: Form 8283 — groups of similar noncash property (`gift`)

> List the kinds of things, other than money, that you gave to charity in 2025, one entry per kind, for example “clothing” or “shares of stock”.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (persona)
- Words: prompt 26, help 19. Help begins: “Group similar things across all the charities you gave to.”

### 121–125. Tick-boxes `rare_deductions`: 5 questions on one screen

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

### 126–127. Tick-boxes `deduction_wishes`: 2 questions on one screen

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you want either of these?
>
> - [ ] To itemize deductions even if the standard deduction is larger  (`sa.elect_itemize`)
> - [ ] To deduct sales tax in place of state and local income tax  (`sa.sales_tax_wish`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 6, labels 22. Behind each box, optional to read: the question's own prompt (17, 22 words) and help (22, 40)

### 128–133. Tick-boxes `home_school`: 6 questions on one screen

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

### 134. `person[spouse].tin`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: Your spouse

> About your spouse — Does your spouse have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 29, help 34. Help begins: “The number must be issued by the date the 2025 return is due, extensions included.”

### 135. `person[taxpayer].tin`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> About you — Do you have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 27, help 34. Help begins: “The number must be issued by the date the 2025 return is due, extensions included.”

### 136. `$sc@person[spouse]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: Your spouse

> About your spouse — In 2025, did your spouse work for himself or herself: freelance or gig work, a side business, or a business of your spouse's own? Add one entry for each business; leave the list empty if your spouse did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 42, help 29. Help begins: “Pay reported to your spouse on Form 1099-NEC, 1099-K or 1099-MISC for your spouse's own work is usually such a business.”

### 137. `$sc@person[taxpayer]`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> About you — In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 36, help 27. Help begins: “Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business.”

### 138. `scope.business_before`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> In any year before 2025, did you or your spouse own a business, a farm, a rental property, or a share of a partnership or an S corporation?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 28, help 0

### 139. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> Which banks, credit unions or others paid you or your spouse interest in 2025? List each one. Leave the list empty if none did.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 24, help 36. Help begins: “Count interest of any amount, with or without a Form 1099-INT: on bank accounts, certificates of deposit, bonds, U.S.”

### 140. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you or your spouse own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 30. Help begins: “Stocks, mutual funds, ETFs and money market funds are all shares.”

### 141. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> In 2025, did you or your spouse sell stocks, bonds, options or fund shares outside a retirement account? A broker reports each sale on Form 1099-B. Add one entry for each sale, or leave the list empty if there were none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 41, help 34. Help begins: “Your broker's year-end statement (Form 1099-B) lists each sale.”

### 142–146. Tick-boxes `sales_rare`: 5 questions on one screen

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

### 147–148. Tick-boxes `invest_other`: 2 questions on one screen

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`); Form 4952 — supported investment-interest deduction and election (`f4952`)

> Is either of these true of your or your spouse's investments?
>
> - [ ] A loss from selling investments in 2024, or one carried into 2024  (`sd.carryover`)
> - [ ] Interest paid on money borrowed to buy investments, in 2025 or before  (`f4952.has_interest`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 11, labels 24. Behind each box, optional to read: the question's own prompt (26, 27 words) and help (34, 37)

### 149. `s3.foreign_any`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> Have you or your spouse ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 150–155. Tick-boxes `outside_us`: 6 questions on one screen

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

### 156–158. Tick-boxes `rare_credits`: 3 questions on one screen

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

### 159. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your or your spouse's 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 28, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 160–162. Tick-boxes `other_taxes`: 3 questions on one screen

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

### 163. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List any other taxable income you or your spouse had in 2025 that you have not been asked about, one entry for each item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 24, help 35. Help begins: “For example a side commission, a reward, or money back for something deducted in an earlier year.”

### 164. `scope.reforestation`

**⟶ topic switch (returns)**

Topic: Proof-of-concept scope screening (`scope`)

> Do you or your spouse own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 165. `scope.attorney_fees`

Topic: Proof-of-concept scope screening (`scope`)

> In 2025, did you or your spouse pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 14. Help begins: “A Yes ends the interview here: this tool cannot prepare a return with it.”

### 166. `qbi.prior_form`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Does your or your spouse's 2024 tax return include Form 8995 or Form 8995-A, the form for the deduction for business income?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 37. Help begins: “The form is titled “Qualified Business Income Deduction”.”

### 167. `qbi.coop_patron`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> In 2025, did you or your spouse sell to, buy from or belong to a farm cooperative, or get a Form 1099-PATR?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 36. Help begins: “This means an agricultural or horticultural cooperative; a person who sells to it, buys from it or belongs to it is its “patron”.”

### 168–169. Tick-boxes `paid_already`: 2 questions on one screen

**⟶ topic switch**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Besides tax taken out of wages, did you or your spouse pay federal tax for 2025 in either of these ways?
>
> - [ ] Tax taken out of a pension, social security or other money  (`f1040.withheld_other_any`)
> - [ ] Estimated tax payments, or a 2024 refund applied to 2025  (`f1040.estimated_any`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: “None of these”: each recorded No (background)
- Words: heading 21, labels 21. Behind each box, optional to read: the question's own prompt (29, 23 words) and help (39, 22)

### 170. `s3.line10`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`), line 10

> How much did you or your spouse pay with a request for more time to file this return (an extension)? Zero if none.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 23, help 25. Help begins: “The payment sent with Form 4868 or Form 2350, or made to get an automatic extension.”

### 171. `household.credit_disallowed`

**⟶ topic switch (returns)**

Topic: Household facts for dependents and head of household (`household`)

> Has the IRS ever reduced or refused a child tax credit, a credit for other dependents or an earned income credit that you or your spouse claimed, for any reason other than a math or clerical error?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 37, help 39. Help begins: “Count any earlier return, including a joint return with someone else: the earned income credit for 1997 or later, the other credits for 2016 or later.”

### 172. `s8812.puerto_rico`

**⟶ topic switch**

Topic: Schedule 8812 — Credits for Qualifying Children and Other Dependents (`s8812`)

> In 2025, were you or your spouse a resident of Puerto Rico (in the tax term, a “bona fide resident”)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 20, help 52. Help begins: “Generally you were one if, during 2025, you met the presence test, had no tax home outside Puerto Rico, and had no closer connection to the United States or to a foreign country than to Puerto Rico (Pub.”

## The end reached

**Complete.** The return is completed after 172 questions.

## Totals

| | |
|---|---|
| Questions asked | 172 |
| Steps (screens; a tick-box group shown together is one) | 97 |
| Answered by the persona / by the background / opened and unanswered | 59 / 113 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 2882 |
| Help words (optional to read) | 4294 |
| Words of the answers offered (Yes and No not counted) | 367 |
| Questions answered no, zero or none | 134 |
| Topics met | 32 |
| Topic switches | 68 |
| of them, returns to a topic already left | 37 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 116 | `sa.property_tax_other_any` | 67 | No |
| 118 | `sa.charity_limited` | 44 | No |
| 136 | `$sc@person[spouse]` | 42 | none (an empty list) |
| 141 | `$sales` | 41 | none (an empty list) |
| 152 | `sb.trust_any` (its own prompt, behind a tick-box) | 41 | No |
| 21 | `dependent[older_child].lived_all_year` | 39 | Yes |
| 30 | `dependent[younger_child].lived_all_year` | 39 | Yes |
| 143 | `sd.sec1256` (its own prompt, behind a tick-box) | 39 | No |
| 67 | `f2441.care` (its own prompt, behind a tick-box) | 38 | No |
| 103 | `sa.state_tax_other_any` (its own prompt, behind a tick-box) | 37 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                         6w  ["taxpayer","spouse"]         [person]
> *  2  household.married_dec31                         7w  true                          [household]
>>   3  person[spouse].birth_year                      10w  1980                          [person]
     4  person[taxpayer].birth_year                     8w  1980
>    5  sa.dependent                                   18w  false                         [sa]
>>   6  person[spouse].blind                           29w  false                         [person]
     7  person[taxpayer].blind                         27w  false
>    8  scope.noncitizen                               19w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                             12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                             12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                                11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                          11w  false                         [s3]
> * 13  $dependent                                     33w  ["older_child","younger_chi…  [dependent]
  * 14  dependent[older_child].relationship             7w  "child"
  * 15  dependent[older_child].age                     10w  6
  * 16  dependent[older_child].younger                 16w  true
  * 17  dependent[older_child].other_claimant          20w+ false                         (screen 14, dependent_facts)
  * 18  dependent[older_child].parents_apart           12w+ false                         (screen 14, dependent_facts)
  * 19  dependent[older_child].ever_married             6w+ false                         (screen 14, dependent_facts)
  * 20  dependent[older_child].own_money               11w+ false                         (screen 14, dependent_facts)
  * 21  dependent[older_child].lived_all_year          39w  true
  * 22  dependent[older_child].citizen_ssn             28w  true
  * 23  dependent[younger_child].relationship           7w  "child"
  * 24  dependent[younger_child].age                   10w  3
  * 25  dependent[younger_child].younger               16w  true
  * 26  dependent[younger_child].other_claimant        20w+ false                         (screen 20, dependent_facts)
  * 27  dependent[younger_child].parents_apart         12w+ false                         (screen 20, dependent_facts)
  * 28  dependent[younger_child].ever_married           6w+ false                         (screen 20, dependent_facts)
  * 29  dependent[younger_child].own_money             11w+ false                         (screen 20, dependent_facts)
  * 30  dependent[younger_child].lived_all_year        39w  true
  * 31  dependent[younger_child].citizen_ssn           28w  true
>>  32  s3.adoption_any                                22w+ false                         [s3]  (screen 23, child_extras)
>>  33  scope.f8814                                    11w+ false                         [scope]  (screen 23, child_extras)
    34  scope.rental                                   22w+ false                         (screen 24, own_income)
    35  scope.k1                                       12w+ false                         (screen 24, own_income)
    36  scope.farm                                      6w+ false                         (screen 24, own_income)
>>  37  person[spouse].rrta                            17w+ false                         [person]  (screen 25, work_kind)
    38  person[spouse].eligible_educator               11w+ false                         (screen 25, work_kind)
> * 39  $w2@person[spouse]                             12w  ["city_schools"]              [w2]
  * 40  person[spouse].w2[city_schools].box1            6w  6800000
  * 41  person[spouse].w2[city_schools].box2            6w  720000
  * 42  person[spouse].w2[city_schools].box4            6w  421600
  * 43  person[spouse].w2[city_schools].box5            6w  6800000
  * 44  person[spouse].w2[city_schools].box6            5w  98600
>>  45  person[taxpayer].rrta                          15w+ false                         [person]  (screen 32, work_kind)
    46  person[taxpayer].eligible_educator             11w+ false                         (screen 32, work_kind)
>>* 47  $w2@person[taxpayer]                           10w  ["northside_hospital"]        [w2]
  * 48  person[taxpayer].w2[northside_hospital].box1    6w  9500000
  * 49  person[taxpayer].w2[northside_hospital].box2    6w  1050000
  * 50  person[taxpayer].w2[northside_hospital].box4    6w  589000
  * 51  person[taxpayer].w2[northside_hospital].box5    6w  9500000
  * 52  person[taxpayer].w2[northside_hospital].box6    5w  137750
> * 53  s2.w2_marks                                    25w+ false                         [s2]  (screen 39, w2_jobs)
> * 54  s1.nqdc_pension                                12w+ false                         [s1]  (screen 39, w2_jobs)
>>* 55  scope.w2_marks                                 10w+ false                         [scope]  (screen 39, w2_jobs)
  * 56  scope.artist_official                          12w+ false                         (screen 39, w2_jobs)
  * 57  scope.excess_deferral                          12w+ false                         (screen 39, w2_jobs)
    58  scope.pay_no_w2                                27w+ false                         (screen 40, other_pay)
    59  scope.medicaid_waiver                          11w+ false                         (screen 40, other_pay)
    60  scope.religious_work                           12w+ false                         (screen 40, other_pay)
>   61  f8959.territory_w2                             10w+ false                         [f8959]  (screen 40, other_pay)
>>  62  s2.options_any                                 11w+ false                         [s2]  (screen 40, other_pay)
>   63  s1a.tips                                       15w+ false                         [s1a]  (screen 41, tips_overtime)
    64  s1a.overtime                                    2w+ false                         (screen 41, tips_overtime)
>>* 65  person[spouse].work_ssn                        21w  true                          [person]
  * 66  person[taxpayer].work_ssn                      18w  true
>   67  f2441.care                                     23w+ false                         [f2441]  (screen 44, care_help)
    68  f2441.benefits                                 12w+ false                         (screen 44, care_help)
>>  69  s2.household_help                              12w+ false                         [s2]  (screen 44, care_help)
>>  70  s1.uc_any                                      13w+ false                         [s1]  (screen 45, money_a)
    71  s1.winnings_any                                 9w+ false                         (screen 45, money_a)
    72  s1.scholarship_any                              9w+ false                         (screen 45, money_a)
    73  s1.jury_any                                     6w+ false                         (screen 45, money_a)
    74  s1.alaska_any                                   5w+ false                         (screen 45, money_a)
    75  s1.hobby_any                                   11w+ false                         (screen 45, money_a)
    76  s1.alimony_any                                 19w+ false                         (screen 46, money_b)
    77  s1.cod_any                                     11w+ false                         (screen 46, money_b)
    78  s1.ltc_payout                                  12w+ false                         (screen 46, money_b)
    79  s1.inmate_wages                                12w+ false                         (screen 46, money_b)
    80  s1.digital_income                              12w+ false                         (screen 46, money_b)
>>  81  scope.recovery                                 12w+ false                         [scope]  (screen 46, money_b)
>   82  refund.any                                     16w  false                         [refund]
>   83  $retirement@person[spouse]                     36w  []                            [retirement]
    84  $retirement@person[taxpayer]                   33w  []
>>  85  person[spouse].ira_owner                       21w+ false                         [person]  (screen 50, accounts)
    86  person[spouse].inherited_account               11w+ false                         (screen 50, accounts)
    87  person[spouse].x_edu_account                   14w+ false                         (screen 50, accounts)
    88  person[spouse].x_archer_excess                 11w+ false                         (screen 50, accounts)
    89  person[taxpayer].ira_owner                     19w+ false                         (screen 51, accounts)
    90  person[taxpayer].inherited_account             11w+ false                         (screen 51, accounts)
    91  person[taxpayer].x_edu_account                 12w+ false                         (screen 51, accounts)
    92  person[taxpayer].x_archer_excess               11w+ false                         (screen 51, accounts)
>   93  ssb.any                                        26w  false                         [ssb]
>   94  $f8889@person[spouse]                          19w  []                            [f8889]
    95  $f8889@person[taxpayer]                        17w  []
>>  96  scope.disaster_distribution                    24w+ false                         [scope]  (screen 55, rare_accounts)
    97  scope.archer_msa                               11w+ false                         (screen 55, rare_accounts)
>>  98  s2.hsa_testing                                 11w+ false                         [s2]  (screen 55, rare_accounts)
>>  99  scope.education_recapture                      11w+ false                         [scope]  (screen 55, rare_accounts)
>  100  $f1095a                                        24w  []                            [f1095a]
>>*101  sa.home_owner                                  23w+ true                          [sa]  (screen 57, paid_2025)
  *102  sa.state_tax_any                               10w+ true                          (screen 57, paid_2025)
   103  sa.state_tax_other_any                         12w+ false                         (screen 57, paid_2025)
   104  sa.personal_property_tax_any                   12w+ false                         (screen 57, paid_2025)
  *105  sa.gifts                                       11w+ true                          (screen 57, paid_2025)
   106  sa.medical_any                                 10w+ false                         (screen 57, paid_2025)
   107  sa.medical_premiums                            24w+ false                         (screen 58, paid_more)
>  108  sd.casualty                                    12w+ false                         [sd]  (screen 58, paid_more)
>>*109  sa.mortgage_interest                           25w  1890000                       [sa]
  *110  sa.mortgage_unreported                         27w  false
  *111  sa.mortgage_over_limit                         25w  false
  *112  sa.mortgage_other_use                          25w  false
>>*113  s3.mcc                                         21w  false                         [s3]
>>*114  s2.mortgage_subsidy                            25w  false                         [s2]
>>*115  sa.line5b                                      29w  520000                        [sa]
  *116  sa.property_tax_other_any                      67w  false
  *117  sa.line5a                                      24w  780000
  *118  sa.charity_limited                             44w  false
  *119  sa.line11                                      36w  310000
> *120  $gift                                          26w  []                            [gift]
>> 121  sa.estate_tax_income                           22w+ false                         [sa]  (screen 71, rare_deductions)
   122  sa.bond_premium                                12w+ false                         (screen 71, rare_deductions)
   123  sa.debt_instrument_loss                        10w+ false                         (screen 71, rare_deductions)
   124  sa.pension_unrecovered                         11w+ false                         (screen 71, rare_deductions)
   125  sa.impairment_work                             12w+ false                         (screen 71, rare_deductions)
   126  sa.elect_itemize                               16w+ false                         (screen 72, deduction_wishes)
   127  sa.sales_tax_wish                              12w+ false                         (screen 72, deduction_wishes)
>> 128  s1a.carloan                                    24w+ false                         [s1a]  (screen 73, home_school)
>> 129  s3.ev                                          11w+ false                         [s3]  (screen 73, home_school)
   130  s3.kerosene                                     9w+ false                         (screen 73, home_school)
>  131  f5695.any                                      11w+ false                         [f5695]  (screen 73, home_school)
>  132  f8863.paid                                     12w+ false                         [f8863]  (screen 73, home_school)
>  133  sli.any                                         6w+ false                         [sli]  (screen 73, home_school)
>>*134  person[spouse].tin                             29w  true                          [person]
  *135  person[taxpayer].tin                           27w  true
>  136  $sc@person[spouse]                             42w  []                            [sc]
   137  $sc@person[taxpayer]                           36w  []
>> 138  scope.business_before                          28w  false                         [scope]
>  139  $interest                                      24w  []                            [interest]
>  140  div.any                                        24w  false                         [div]
>  141  $sales                                         41w  []                            [sales]
>> 142  sd.sold_other                                  28w+ false                         [sd]  (screen 82, sales_rare)
   143  sd.sec1256                                     12w+ false                         (screen 82, sales_rare)
   144  sd.condemned                                    9w+ false                         (screen 82, sales_rare)
   145  sd.small_business_stock                        12w+ false                         (screen 82, sales_rare)
   146  sd.trader_election                              9w+ false                         (screen 82, sales_rare)
   147  sd.carryover                                   23w+ false                         (screen 83, invest_other)
>  148  f4952.has_interest                             12w+ false                         [f4952]  (screen 83, invest_other)
>> 149  s3.foreign_any                                 27w  false                         [s3]
>  150  sb.account_any                                 30w+ false                         [sb]  (screen 85, outside_us)
   151  sb.asset_any                                   11w+ false                         (screen 85, outside_us)
   152  sb.trust_any                                    9w+ false                         (screen 85, outside_us)
   153  sb.company_any                                 12w+ false                         (screen 85, outside_us)
   154  sb.territory_any                               10w+ false                         (screen 85, outside_us)
>> 155  scope.foreign_shares                           12w+ false                         [scope]  (screen 85, outside_us)
>> 156  s3.credit_bond                                 22w+ false                         [s3]  (screen 86, rare_credits)
   157  s3.farmland                                     2w+ false                         (screen 86, rare_credits)
   158  s3.repaid_income                               11w+ false                         (screen 86, rare_credits)
   159  s3.prior_other_forms                           28w  false
>> 160  s2.credit_recapture                            23w+ false                         [s2]  (screen 88, other_taxes)
   161  s2.amt_owed                                     3w+ false                         (screen 88, other_taxes)
   162  s2.other_tax                                    9w+ false                         (screen 88, other_taxes)
>  163  $oi8z                                          24w  []                            [oi8z]
>> 164  scope.reforestation                            25w  false                         [scope]
   165  scope.attorney_fees                            24w  false
>  166  qbi.prior_form                                 22w  false                         [qbi]
   167  qbi.coop_patron                                22w  false
>  168  f1040.withheld_other_any                       32w+ false                         [f1040]  (screen 94, paid_already)
   169  f1040.estimated_any                            10w+ false                         (screen 94, paid_already)
>> 170  s3.line10                                      23w  0                             [s3]
>>*171  household.credit_disallowed                    37w  false                         [household]
> *172  s8812.puerto_rico                              20w  false                         [s8812]
```
