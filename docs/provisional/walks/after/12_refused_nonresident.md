# Walk: 12_refused_nonresident

A single person with wages from one job who was a nonresident alien for part of 2025; the tool does not prepare that return.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/12_refused_nonresident.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
> - [x] Not a U.S. citizen at some time in 2025  (`scope.noncitizen`)
> - [ ] In the U.S. armed forces, reserves or National Guard since January 2022  (`scope.armed_forces`)
> - [ ] Leaving out income earned abroad, in Puerto Rico or in American Samoa  (`sa.excluded_income`)
> - [ ] In a chapter 11 bankruptcy case at some time in 2025  (`scope.chapter11`)

- Offered: a box for each, “Continue” with the boxes ticked, and “None of these”
- Answer: ticked “Not a U.S. citizen at some time in 2025”; the others recorded No (persona; background)
- Words: heading 7, labels 44. Behind each box, optional to read: the question's own prompt (11, 19, 26, 13 words) and help (0, 0, 36, 25)

### 12. `scope.nonresident`

Topic: Proof-of-concept scope screening (`scope`)

> For any part of 2025, were you a nonresident alien, that is, neither a U.S. citizen nor a U.S. resident for tax?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 22, help 22. Help begins: “A person who held a green card for all of 2025 was a resident all year.”

## The end reached

**Refused** at the gate `scope.other_income`, after 12 questions. The wording shown:

> Form 1040 additional income/return forms
>
> Prepare the required unsupported income or return treatment.
>
> This tool cannot prepare a return with what you just answered Yes to. The most common cases are a person who was a nonresident alien for part of 2025 (that return is Form 1040-NR, or a dual-status return), wages or tips that are not on a W-2, and a chapter 11 bankruptcy case. If that Yes was a mistake, go back and change it. If it was right, this return needs tax software or a preparer that handles it.

## Totals

| | |
|---|---|
| Questions asked | 12 |
| Steps (screens; a tick-box group shown together is one) | 9 |
| Answered by the persona / by the background / opened and unanswered | 4 / 8 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 159 |
| Help words (optional to read) | 378 |
| Words of the answers offered (Yes and No not counted) | 72 |
| Questions answered no, zero or none | 7 |
| Topics met | 5 |
| Topic switches | 8 |
| of them, returns to a topic already left | 4 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 10 | `sa.excluded_income` (its own prompt, behind a tick-box) | 26 | No |
| 7 | `person[taxpayer].blind` | 25 | No |
| 12 | `scope.nonresident` | 22 | Yes |
| 4 | `household.community_property` | 20 | No |
| 9 | `scope.armed_forces` (its own prompt, behind a tick-box) | 19 | No |
| 6 | `sa.dependent` | 15 | No |
| 11 | `scope.chapter11` (its own prompt, behind a tick-box) | 13 | No |
| 8 | `scope.noncitizen` (its own prompt, behind a tick-box) | 11 | Yes |
| 2 | `f1040.status` | 9 | “None of these: I was not married (single)” (`single`) |
| 1 | `$person` | 6 | “Just me” |

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
> *  8  scope.noncitizen               16w+ true                          [scope]  (screen 8, about_you)
     9  scope.armed_forces             12w+ false                         (screen 8, about_you)
>>  10  sa.excluded_income             12w+ false                         [sa]  (screen 8, about_you)
>>  11  scope.chapter11                11w+ false                         [scope]  (screen 8, about_you)
  * 12  scope.nonresident              22w  true
```
