# Walk: 11_refused_rental

A single person with wages from one job who also rents out a house she owns; the tool does not prepare rental income.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/11_refused_rental.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: 1980 (background)
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
> - [x] Anything you own rented out or offered for rent, or royalties  (`scope.rental`)
> - [ ] Income or a loss from a partnership, S corporation, estate or trust  (`scope.k1`)
> - [ ] Income or a loss from farming  (`scope.farm`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Anything you own rented out or offered for rent, or royalties”; the others recorded No (persona; background)
- Words: heading 8, labels 29. Behind each box, optional to read: the question's own prompt (27, 27, 11 words) and help (6, 6, 25)

## The end reached

**Refused** at the gate `scope.schedule1`, after 18 questions. The wording shown:

> Schedule 1
>
> Schedule 1 income and adjustments other than the ones this tool computes (Schedule C business income, a taxable state or local income tax refund, alimony under an agreement made before 2019, unemployment compensation, the supported line 8 items, educator expenses, the HSA deduction, the deductible part of self-employment tax, self-employed SEP and SIMPLE contributions, the self-employed health insurance deduction, the early withdrawal penalty, the IRA deduction, student loan interest and jury duty pay given to your employer) are outside this tool.
>
> This tool cannot prepare a return with what you just answered Yes to. The most common cases are rent or royalties (Schedule E), income or a loss from a partnership, an S corporation, an estate or a trust (Schedule K-1), and farming (Schedule F). If that Yes was a mistake, go back and change it. If it was right, this return needs tax software or a preparer that handles it.

## Totals

| | |
|---|---|
| Questions asked | 18 |
| Steps (screens; a tick-box group shown together is one) | 12 |
| Answered by the persona / by the background / opened and unanswered | 3 / 15 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 242 |
| Help words (optional to read) | 504 |
| Words of the answers offered (Yes and No not counted) | 72 |
| Questions answered no, zero or none | 14 |
| Topics met | 7 |
| Topic switches | 12 |
| of them, returns to a topic already left | 6 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 13 | `$dependent` | 30 | none (an empty list) |
| 16 | `scope.rental` (its own prompt, behind a tick-box) | 27 | Yes |
| 17 | `scope.k1` (its own prompt, behind a tick-box) | 27 | No |
| 10 | `sa.excluded_income` (its own prompt, behind a tick-box) | 26 | No |
| 7 | `person[taxpayer].blind` | 25 | No |
| 15 | `scope.f8814` (its own prompt, behind a tick-box) | 21 | No |
| 4 | `household.community_property` | 20 | No |
| 9 | `scope.armed_forces` (its own prompt, behind a tick-box) | 19 | No |
| 14 | `s3.adoption_any` (its own prompt, behind a tick-box) | 16 | No |
| 6 | `sa.dependent` | 15 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                         6w  ["taxpayer"]                  [person]
> *  2  f1040.status                    9w  "single"                      [f1040]
>    3  household.ever_married          5w  false                         [household]
     4  household.community_property   20w  false
>>   5  person[taxpayer].birth_year     6w  1980                          [person]
>    6  sa.dependent                   15w  false                         [sa]
>>   7  person[taxpayer].blind         25w  false                         [person]
>    8  scope.noncitizen               16w+ false                         [scope]  (screen 8, about_you)
     9  scope.armed_forces             12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income             12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                11w+ false                         [scope]  (screen 8, about_you)
>   12  s3.disability_retired           8w  false                         [s3]
>   13  $dependent                     30w  []                            [dependent]
>>  14  s3.adoption_any                19w+ false                         [s3]  (screen 11, child_extras)
>>  15  scope.f8814                    11w+ false                         [scope]  (screen 11, child_extras)
  * 16  scope.rental                   19w+ true                          (screen 12, own_income)
    17  scope.k1                       12w+ false                         (screen 12, own_income)
    18  scope.farm                      6w+ false                         (screen 12, own_income)
```
