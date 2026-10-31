# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 28fa49b1970c8899a65b36e8950baed85fdb8a704cbb6c7d4fc14b42e512dfee |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a912066380307126cf7fdc54dc2d4cae644ddc358e66e92e6310ac906ac234ac |
| lines judged | 11 |
| match / mismatch / unclear / missing | 10 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 10, 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 15, 18, 19, 20, 21 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 15, 18, 19, 20, 21 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 2, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 2, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i8962 | 2025 | 8 | cited pages | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 8 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| i8863 | 2025 | 1, 2, 3, 4, 8, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 8, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |

## Lines

### 2(d) — Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
Status: **MISMATCH**

Restated: Enter the amount from helper "Qualified expenses incurred and paid in 2025 for this person's care".

Model: Form 2441 line 2(d) says: 'If you completed Part III, don't include in column (d) any benefits shown on line 28.' The helper instead says to include expenses paid with dependent care benefits, and the line does not subtract them.

Ruling: ambiguity; amb.2025.dc_line30 (owner ruling, Stage 15 decision 6, T-048). i2441 p. 3, Column (d): "If you completed Part III, don't include in column (d) any benefits shown on line 28"; Form 2441 line 30 subtracts them once ("Don't include in column (d) any benefits shown on line 28 above. Then, add the amounts in column (d)"); the instructions give no rule for dividing line 28 among persons. The deepseek model reads the register's rejected reading. As ruled since round 2. The subject change of this round (BUG-0258, dependent.parent_home_paid) does not touch this line. Project stands.

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MATCH**

Model: Form 2441 column (c) asks whether the qualifying person was over age 12 when care was provided and disabled; the restatement uses the qualifying-person and disability gates plus the age-13 part-year care input.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: Form 8863 line 23 asks whether the American opportunity credit has been claimed for this student for any 4 prior tax years, matching the restatement.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: Form 8863 line 24 and its instructions match the at-least-half-time, program-leading, 2025 (or first 3 months of 2026 if paid in 2025) test.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: Form 8863 line 25 and its instructions match the first 4 years of postsecondary education before 2025, disregarding proficiency-exam credit.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: Form 8863 line 26 matches the felony conviction question.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: Form 8863 line 27 is adjusted qualified education expenses capped at $4,000; the restatement uses the Form 8863 line 27 worksheet computation with the stated multi-period refusal.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: Form 8863 line 28 subtracts $2,000 from line 27, not below zero, matching the aqee line 28 computation.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: Form 8863 line 29 multiplies line 28 by 25%, matching the aqee line 29 computation.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: Form 8863 line 30 uses line 27 if line 28 is zero, otherwise adds $2,000 to line 29, matching the aqee line 30 computation.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: Form 8863 line 31 is adjusted qualified education expenses for the lifetime learning credit; ws4_llc subtracts worksheet line 3 from expenses required to be paid to the institution, as the LLC rules require.

## Raw response

```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "Form 2441 line 2(d) says: 'If you completed Part III, don't include in column (d) any benefits shown on line 28.' The helper instead says to include expenses paid with dependent care benefits, and the line does not subtract them."
  - key: "2(c)"
    status: MATCH
    reason: "Form 2441 column (c) asks whether the qualifying person was over age 12 when care was provided and disabled; the restatement uses the qualifying-person and disability gates plus the age-13 part-year care input."
  - key: "23"
    status: MATCH
    reason: "Form 8863 line 23 asks whether the American opportunity credit has been claimed for this student for any 4 prior tax years, matching the restatement."
  - key: "24"
    status: MATCH
    reason: "Form 8863 line 24 and its instructions match the at-least-half-time, program-leading, 2025 (or first 3 months of 2026 if paid in 2025) test."
  - key: "25"
    status: MATCH
    reason: "Form 8863 line 25 and its instructions match the first 4 years of postsecondary education before 2025, disregarding proficiency-exam credit."
  - key: "26"
    status: MATCH
    reason: "Form 8863 line 26 matches the felony conviction question."
  - key: "27"
    status: MATCH
    reason: "Form 8863 line 27 is adjusted qualified education expenses capped at $4,000; the restatement uses the Form 8863 line 27 worksheet computation with the stated multi-period refusal."
  - key: "28"
    status: MATCH
    reason: "Form 8863 line 28 subtracts $2,000 from line 27, not below zero, matching the aqee line 28 computation."
  - key: "29"
    status: MATCH
    reason: "Form 8863 line 29 multiplies line 28 by 25%, matching the aqee line 29 computation."
  - key: "30"
    status: MATCH
    reason: "Form 8863 line 30 uses line 27 if line 28 is zero, otherwise adds $2,000 to line 29, matching the aqee line 30 computation."
  - key: "31"
    status: MATCH
    reason: "Form 8863 line 31 is adjusted qualified education expenses for the lifetime learning credit; ws4_llc subtracts worksheet line 3 from expenses required to be paid to the institution, as the LLC rules require."
```
