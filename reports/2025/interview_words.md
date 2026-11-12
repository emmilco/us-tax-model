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
| Stage 5 whole returns | 9 | 2 | 90.1 | 7,269 | 6,830 | 8,682 | 87 | 2,354 | 796 | 465 |
| generated returns | 3 | 9 | 157.3 | 13,248 | 8,871 | 22,523 | 279 | 2,946 | 796 | 3,240 |
| minimal returns | 7 | 0 | 78.1 | 6,933 | 6,891 | 7,200 | 83 | 2,177 | 796 | 0 |
| social-security profile fixtures | 16 | 5 | 11.3 | 191 | 196 | 196 | 75 | 389 | 9 | 85 |
| sales profile fixtures | 58 | 14 | 62.7 | 7,211 | 6,743 | 20,857 | 108 | 1,742 | 672 | 5,708 |
| stage4 profile fixtures | 69 | 62 | 73.5 | 6,552 | 6,257 | 9,135 | 88 | 2,065 | 790 | 2,940 |
| **full profile, Stage 5 and generated** | 12 | 11 | 106.9 | 8,764 | 6,830 | 22,523 | 135 | 2,502 | 796 | 2,735 |

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
| `household.unmarried` | 318 | 2 |
| `f8889.coverage_year` | 317 | 4 |
| `dependent.relationship` | 297 | 3 |
| `scope.schedule1` | 293 | 25 |
| `sa.gifts` | 292 | 20 |
| `asset.s179` | 271 | 1 |

The longest prompts every one of the 30 full-profile walks asks:

| Question | Prompt words |
|---|---|
| `$person` | 6 |

## The longest sentences in the question bank

Of the 625 questions the page's profile can ask, 261 have a sentence of more than 40 words in their prompt, 64 one of more than 80 and 9 one of more than 120.
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
