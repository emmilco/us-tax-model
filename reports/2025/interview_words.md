# Interview words: what a filer reads

Written by `node engine/dist/main.js interview-words --write` (engine/src/interview-words.ts; deterministic, no model calls).
Every return is walked in the interview's own order, and each question asked is counted as the page shows it: the prompt
reworded for the filing status answered, counted once per time it is asked (a question asked per person or per entry counts
once per entry). **Prompt words** are the words of the prompts. **Option words** are the words of the answers offered with a
question (an enum's labels or values, a fixed list's choices; Yes and No are not counted). **Help words** are the words of the
help shown with each question, which a filer may skip. **Before the first own item** is the prompt words read before the first
question answered with something of the filer's own (an amount, a number or a list) rather than by choosing an offered answer.
A word is a run of characters holding a letter or a digit. The returns are synthetic.

## The returns the project walks

Means are over complete returns; the last column is the mean prompt words of the refused returns, which end at their refusal.

| Returns | Complete | Refused | Questions asked (mean) | Prompt words (mean) | Prompt words (median) | Prompt words (max) | Option words (mean) | Help words (mean) | Before the first own item (mean) | Prompt words, refused (mean) |
|---|---|---|---|---|---|---|---|---|---|---|
| Stage 5 whole returns | 9 | 2 | 91.1 | 7,419 | 6,980 | 8,832 | 30 | 2,219 | 823 | 492 |
| generated returns | 3 | 9 | 158.3 | 13,532 | 9,154 | 22,809 | 222 | 2,812 | 823 | 3,291 |
| minimal returns | 7 | 0 | 79.1 | 7,094 | 7,052 | 7,361 | 26 | 2,042 | 823 | 0 |
| social-security profile fixtures | 16 | 5 | 11.3 | 209 | 214 | 214 | 5 | 233 | 5 | 96 |
| sales profile fixtures | 58 | 14 | 62.7 | 7,308 | 6,840 | 20,954 | 38 | 1,586 | 668 | 5,783 |
| stage4 profile fixtures | 69 | 62 | 73.5 | 6,672 | 6,376 | 9,279 | 18 | 1,911 | 786 | 2,997 |
| **full profile, Stage 5 and generated** | 12 | 11 | 107.9 | 8,947 | 6,980 | 22,809 | 78 | 2,367 | 823 | 2,782 |

0 return(s) could not be walked.

## The longest prompts met on the full profile

The 15 longest prompts among the questions the 30 full-profile walks ask, with how many of those walks ask each.

| Question | Prompt words | Walks that ask it |
|---|---|---|
| `sales.correct_basis` | 906 | 2 |
| `asset.screen` | 843 | 2 |
| `sb.foreign_any` | 827 | 20 |
| `scveh.screen` | 732 | 1 |
| `sales.box` | 689 | 4 |
| `dependent.supported` | 559 | 3 |
| `sa.line1` | 429 | 20 |
| `f8962.other` | 357 | 2 |
| `sales.wash_loss` | 346 | 2 |
| `f8889.coverage_year` | 328 | 4 |
| `household.unmarried` | 318 | 2 |
| `dependent.relationship` | 297 | 3 |
| `scope.schedule1` | 293 | 25 |
| `sa.gifts` | 292 | 20 |
| `asset.s179` | 271 | 1 |

The longest prompts every one of the 30 full-profile walks asks:

| Question | Prompt words |
|---|---|
| `$person` | 16 |
| `f1040.status` | 5 |

## The longest sentences in the question bank

Of the 626 questions the page's profile can ask, 261 have a sentence of more than 40 words in their prompt, 64 one of more than 80 and 9 one of more than 120.
The twelve longest:

| Question | Longest sentence (words) | Prompt words |
|---|---|---|
| `f8889.unsupported` | 231 | 231 |
| `otjob.method` | 158 | 158 |
| `household.qss_eligible` | 156 | 370 |
| `sc.meals_100` | 154 | 173 |
| `sb.foreign_any` | 150 | 841 |
| `sc.line23` | 145 | 145 |
| `f2441.nondependent` | 128 | 128 |
| `otjob.statement` | 126 | 126 |
| `sb.form5471` | 123 | 123 |
| `sb.line8` | 119 | 218 |
| `person.educator_expenses` | 115 | 115 |
| `sc.at_risk` | 112 | 126 |
