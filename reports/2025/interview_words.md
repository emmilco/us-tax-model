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
| Stage 5 whole returns | 9 | 2 | 96.3 | 7,220 | 6,777 | 8,647 | 78 | 2,529 | 678 | 584 |
| generated returns | 3 | 9 | 144.7 | 10,308 | 10,569 | 12,266 | 102 | 3,689 | 678 | 3,204 |
| minimal returns | 13 | 0 | 84.2 | 6,860 | 6,838 | 7,147 | 74 | 2,361 | 678 | 0 |
| social-security profile fixtures | 15 | 6 | 13.2 | 226 | 231 | 231 | 75 | 430 | 9 | 102 |
| sales profile fixtures | 58 | 14 | 62.7 | 7,154 | 6,686 | 20,800 | 99 | 1,802 | 672 | 5,651 |
| stage4 profile fixtures | 69 | 62 | 81.6 | 6,528 | 6,231 | 9,165 | 79 | 2,278 | 672 | 2,869 |
| **full profile, Stage 5 and generated** | 12 | 11 | 108.4 | 7,992 | 6,777 | 12,266 | 84 | 2,819 | 678 | 2,728 |

0 return(s) could not be walked.

## The longest prompts met on the full profile

The 15 longest prompts among the questions the 36 full-profile walks ask, with how many of those walks ask each.

| Question | Prompt words | Walks that ask it |
|---|---|---|
| `sales.correct_basis` | 906 | 2 |
| `asset.screen` | 843 | 1 |
| `sb.foreign_any` | 827 | 26 |
| `sales.box` | 689 | 4 |
| `dependent.supported` | 559 | 3 |
| `sa.line1` | 429 | 26 |
| `f8962.other` | 357 | 1 |
| `sales.wash_loss` | 346 | 2 |
| `household.unmarried` | 318 | 3 |
| `dependent.relationship` | 297 | 4 |
| `scope.schedule1` | 293 | 32 |
| `sa.gifts` | 292 | 26 |
| `asset.s179` | 271 | 1 |
| `sli.interest` | 244 | 26 |
| `sa.line5a` | 237 | 26 |

The longest prompts every one of the 36 full-profile walks asks:

| Question | Prompt words |
|---|---|
| `$person` | 6 |

## The longest sentences in the question bank

Of the 663 questions the page's profile can ask, 250 have a sentence of more than 40 words in their prompt, 60 one of more than 80 and 8 one of more than 120.
The twelve longest:

| Question | Longest sentence (words) | Prompt words |
|---|---|---|
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
| `sc.f7206_line1` | 112 | 112 |
