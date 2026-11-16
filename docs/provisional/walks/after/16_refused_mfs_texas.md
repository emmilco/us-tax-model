# Walk: 16_refused_mfs_texas

A married person in Texas who files apart from their husband or wife; their income may be half community income under state law, which the tool does not divide.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/16_refused_mfs_texas.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: “Married, and filing apart from my husband or wife (married filing separately)” (`mfs`) (persona)
- Words: prompt 9, help 115. Help begins: “Take the first line that is true for you, with one exception: if you are married but lived apart from your husband or wife for the last six months of 2025 and your child lived with you, look at the line about paying for a home before the first line.”

### 3. `household.married_dec31`

**⟶ topic switch**

Topic: Household facts for dependents and head of household (`household`)

> Were you married on December 31, 2025?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 7, help 64. Help begins: “A divorce that was not yet final on December 31 means you were still married; a final decree of divorce, legal separation or annulment means you were not, unless you divorced only to file as unmarried and married each other again in 2026.”

### 4. `household.community_property`

Topic: Household facts for dependents and head of household (`household`)

> At any time in 2025, did you live in Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 20, help 35. Help begins: “In these nine states a married couple's income belongs to both of them by law (community property).”

## The end reached

**Refused** at the gate `household.mfs_community_property`, after 4 questions. The wording shown:

> Community income on a married filing separately return (Form 8958; Pub. 555)
>
> A married person who files a separate return and lived in a community property state may have to report half of the community income of both spouses under state law; Form 8958 and the community property rules of Pub. 555 are outside this tool.
>
> This tool cannot prepare a separate return for a married person who lived in a community property state in 2025, because part of each spouse's income may belong to the other under state law. If the two of you are putting, or could put, your income on one return, go back to “Who is this tax return for?” and choose “Me and my husband or wife, together on one return”: a married couple can file together even if only one of you had income. Otherwise this return needs tax software or a preparer that handles community income (Form 8958).

## Totals

| | |
|---|---|
| Questions asked | 4 |
| Steps (screens; a tick-box group shown together is one) | 4 |
| Answered by the persona / by the background / opened and unanswered | 4 / 0 / 0 |
| Prompt words (a tick-box screen: its heading and labels) | 42 |
| Help words (optional to read) | 265 |
| Words of the answers offered (Yes and No not counted) | 72 |
| Questions answered no, zero or none | 0 |
| Topics met | 3 |
| Topic switches | 2 |
| of them, returns to a topic already left | 0 |

## The 4 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 4 | `household.community_property` | 20 | Yes |
| 2 | `f1040.status` | 9 | “Married, and filing apart from my husband or wife (married filing separately)” (`mfs`) |
| 3 | `household.married_dec31` | 7 | Yes |
| 1 | `$person` | 6 | “Just me” |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question. A question answered on a tick-box screen has the words of its label (and, the screen's first, of the heading) and `+`, and its screen's number at the right.

```
> *  1  $person                         6w  ["taxpayer"]                  [person]
> *  2  f1040.status                    9w  "mfs"                         [f1040]
> *  3  household.married_dec31         7w  true                          [household]
  *  4  household.community_property   20w  true
```
