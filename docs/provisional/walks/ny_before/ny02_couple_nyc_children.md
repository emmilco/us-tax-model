# Walk: ny02_couple_nyc_children

A married couple in Queens all of 2025, filing together, each with one job, with two children aged 3 and 6; New York's child credit for a child under 17 is not computed by this tool.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/ny02_couple_nyc_children.yaml`: the built interview (profile `ny`, the federal questions, then the New York ones, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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

### 16. `dependent[older_child].lived_all_year`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> Did this person live with you for all of 2025? (For a baby born in 2025, a child adopted or placed with you in 2025, or a person who died in 2025: all of their part of the year.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 39, help 34. Help begins: “Time away at school, on vacation, on business, in hospital, in military service or in juvenile detention counts as living with you.”

### 17. `dependent[older_child].younger`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent older_child

> Is this person younger than you (or, if you file together, younger than either of you)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 0

### 18–21. Tick-boxes `dependent_facts`: 4 questions on one screen

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

### 25. `dependent[younger_child].lived_all_year`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Did this person live with you for all of 2025? (For a baby born in 2025, a child adopted or placed with you in 2025, or a person who died in 2025: all of their part of the year.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 39, help 34. Help begins: “Time away at school, on vacation, on business, in hospital, in military service or in juvenile detention counts as living with you.”

### 26. `dependent[younger_child].younger`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Is this person younger than you (or, if you file together, younger than either of you)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 16, help 0

### 27–30. Tick-boxes `dependent_facts`: 4 questions on one screen

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

### 31. `dependent[younger_child].citizen_ssn`

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`). About: dependent younger_child

> Is this person a U.S. citizen with a social security number? (If the card has a restriction printed on it, such as “Not Valid for Employment”, answer No.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 28, help 22. Help begins: “The number must have been issued before the due date of your 2025 return, extensions included; if it was not, answer No.”

## The end reached

**Refused** at the gate `ny_it201.gate.child_credit`, after 31 questions. The wording shown:

> Form IT-213, Claim for Empire State Child Credit
>
> The Empire State child credit is not computed by this tool.

## Totals

| | |
|---|---|
| Questions asked | 31 |
| Steps (screens; a tick-box group shown together is one) | 22 |
| Answered by the persona / by the background / opened and unanswered | 21 / 10 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 501 |
| Help words (optional to read) | 769 |
| Words of the answers offered (Yes and No not counted) | 332 |
| Questions answered no, zero or none | 16 |
| Topics met | 6 |
| New York stretch (questions of New York forms): questions / steps / prompt words / help words | 0 / 0 / 0 / 0 |
| Topic switches | 9 |
| of them, returns to a topic already left | 4 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 16 | `dependent[older_child].lived_all_year` | 39 | Yes |
| 25 | `dependent[younger_child].lived_all_year` | 39 | Yes |
| 18 | `dependent[older_child].other_claimant` (its own prompt, behind a tick-box) | 36 | No |
| 27 | `dependent[younger_child].other_claimant` (its own prompt, behind a tick-box) | 36 | No |
| 13 | `$dependent` | 33 | the list `older_child`, `younger_child` |
| 6 | `person[spouse].blind` | 29 | No |
| 10 | `sa.excluded_income` (its own prompt, behind a tick-box) | 29 | No |
| 22 | `dependent[older_child].citizen_ssn` | 28 | Yes |
| 31 | `dependent[younger_child].citizen_ssn` | 28 | Yes |
| 7 | `person[taxpayer].blind` | 27 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                                    6w  ["taxpayer","spouse"]         [person]
> *  2  household.married_dec31                    7w  true                          [household]
>>   3  person[spouse].birth_year                 10w  1980                          [person]
     4  person[taxpayer].birth_year                8w  1980
>    5  sa.dependent                              18w  false                         [sa]
>>   6  person[spouse].blind                      29w  false                         [person]
     7  person[taxpayer].blind                    27w  false
>    8  scope.noncitizen                          19w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces                        12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income                        12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                           11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired                     11w  false                         [s3]
> * 13  $dependent                                33w  ["older_child","younger_chi…  [dependent]
  * 14  dependent[older_child].relationship        7w  "child"
  * 15  dependent[older_child].age                10w  6
  * 16  dependent[older_child].lived_all_year     39w  true
  * 17  dependent[older_child].younger            16w  true
  * 18  dependent[older_child].other_claimant     20w+ false                         (screen 15, dependent_facts)
  * 19  dependent[older_child].parents_apart      12w+ false                         (screen 15, dependent_facts)
  * 20  dependent[older_child].ever_married        6w+ false                         (screen 15, dependent_facts)
  * 21  dependent[older_child].own_money          11w+ false                         (screen 15, dependent_facts)
  * 22  dependent[older_child].citizen_ssn        28w  true
  * 23  dependent[younger_child].relationship      7w  "child"
  * 24  dependent[younger_child].age              10w  3
  * 25  dependent[younger_child].lived_all_year   39w  true
  * 26  dependent[younger_child].younger          16w  true
  * 27  dependent[younger_child].other_claimant   20w+ false                         (screen 21, dependent_facts)
  * 28  dependent[younger_child].parents_apart    12w+ false                         (screen 21, dependent_facts)
  * 29  dependent[younger_child].ever_married      6w+ false                         (screen 21, dependent_facts)
  * 30  dependent[younger_child].own_money        11w+ false                         (screen 21, dependent_facts)
  * 31  dependent[younger_child].citizen_ssn      28w  true
```
