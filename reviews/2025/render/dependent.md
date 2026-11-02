# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 803b6b0ccffb494cac88f15bd5a36afd206d92ef45d3e68f8e241b1e143b4d22 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 28e045bd0204ff24cd65160e24083d802e4d1f73c6404a64c9a494c3c0789466 |
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

Model: The helper includes expenses paid with dependent care benefits and leaves Form 2441 to subtract the excluded benefits elsewhere. The column (d) instruction keeps them out of this line: "If you completed Part III, don't include in column (d) any benefits shown on line 28."

Ruling: ambiguity — amb.2025.dc_line30 (owner's decision, Stage 15 decision 6). Column (d) shows each person's expenses before excluding the dependent care benefits, and line 30 subtracts line 28 from the total; the instructions give no rule for dividing line 28 among the qualifying persons. The rendering's reading (net each column (d)) is the unchosen reading.

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MATCH**

Model: The box is checked for a qualifying person who "was over age 12 at the time the care was provided and was disabled." The age test, the 13-at-year-end care question and the incapacity input restate that within the qualifying-person cases.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: This restates line 23, "Has the American opportunity credit been claimed for this student for any 4 prior tax years?" The "by you or anyone else" wording comes from the student qualifications text.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: This restates line 24 and its instruction, including that an academic period beginning in the first 3 months of 2026 counts if the expenses for it were paid in 2025. It is reached only when line 23 is No, as the form directs.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: This restates line 25 and its instruction that 4 years of academic credit awarded by the institution count, disregarding credit "awarded solely on the basis of the student's performance on proficiency examinations." It is reached only when line 24 is Yes.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: This restates line 26 with the instruction's "federal or state felony for possession or distribution of a controlled substance." It is reached only when line 25 is No.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: Line 27 takes the smaller of worksheet line 4 (total AOC expenses less line 3, floored at 0) and $4,000, matching "Don't enter more than $4,000." It is gated on the AOC requirements, including the TINs and EIN. The refusal covers the period-by-period worksheet case where totals could differ.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: This computes "Subtract $2,000 from line 27. If zero or less, enter -0-" for AOC students.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: This computes "Multiply line 28 by 25% (0.25)."

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: This computes "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29."

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: For a student not taking the AOC, line 31 uses worksheet line 4 with lifetime learning credit expenses: tuition, fees and materials required to be paid to the institution, less adjustments, floored at 0. This matches the line 31 instruction and the LLC definition of qualified expenses.

## Raw response

```yaml
```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The helper includes expenses paid with dependent care benefits and leaves Form 2441 to subtract the excluded benefits elsewhere. The column (d) instruction keeps them out of this line: \"If you completed Part III, don't include in column (d) any benefits shown on line 28.\""
  - key: "2(c)"
    status: MATCH
    reason: "The box is checked for a qualifying person who \"was over age 12 at the time the care was provided and was disabled.\" The age test, the 13-at-year-end care question and the incapacity input restate that within the qualifying-person cases."
  - key: "23"
    status: MATCH
    reason: "This restates line 23, \"Has the American opportunity credit been claimed for this student for any 4 prior tax years?\" The \"by you or anyone else\" wording comes from the student qualifications text."
  - key: "24"
    status: MATCH
    reason: "This restates line 24 and its instruction, including that an academic period beginning in the first 3 months of 2026 counts if the expenses for it were paid in 2025. It is reached only when line 23 is No, as the form directs."
  - key: "25"
    status: MATCH
    reason: "This restates line 25 and its instruction that 4 years of academic credit awarded by the institution count, disregarding credit \"awarded solely on the basis of the student's performance on proficiency examinations.\" It is reached only when line 24 is Yes."
  - key: "26"
    status: MATCH
    reason: "This restates line 26 with the instruction's \"federal or state felony for possession or distribution of a controlled substance.\" It is reached only when line 25 is No."
  - key: "27"
    status: MATCH
    reason: "Line 27 takes the smaller of worksheet line 4 (total AOC expenses less line 3, floored at 0) and $4,000, matching \"Don't enter more than $4,000.\" It is gated on the AOC requirements, including the TINs and EIN. The refusal covers the period-by-period worksheet case where totals could differ."
  - key: "28"
    status: MATCH
    reason: "This computes \"Subtract $2,000 from line 27. If zero or less, enter -0-\" for AOC students."
  - key: "29"
    status: MATCH
    reason: "This computes \"Multiply line 28 by 25% (0.25).\""
  - key: "30"
    status: MATCH
    reason: "This computes \"If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29.\""
  - key: "31"
    status: MATCH
    reason: "For a student not taking the AOC, line 31 uses worksheet line 4 with lifetime learning credit expenses: tuition, fees and materials required to be paid to the institution, less adjustments, floored at 0. This matches the line 31 instruction and the LLC definition of qualified expenses."
```
```
