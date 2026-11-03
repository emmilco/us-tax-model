# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | df21c568e8d5c57cb2c7887f7d2d4e23395b454aeb0ba9440a3ef4bee0528302 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 706efc8a5332c5032595790a67e04e77c307862645257157501ba570f6869f8b |
| lines judged | 11 |
| match / mismatch / unclear / missing | 1 / 10 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 10, 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 15, 18, 19, 20, 21, 22 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 15, 18, 19, 20, 21, 22 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 6, 8, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 6, 8, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 2, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 2, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i8962 | 2025 | 8 | cited pages | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 8 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| i8863 | 2025 | 1, 2, 3, 4, 8, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 8, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| p970 | 2025 | 11 | pages named by another document's citation | a5c80030374da420bbaf3118a8a42fe79092e8529663d02ef601b6ae06657e00 | 11 | f6622ed07641c7d4e2a217fb9d9b1fecb7ab16f08dbc758f1a0963e1fe677e0a |

## Lines

### 2(d) — Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
Status: **MISMATCH**

Restated: Enter the amount from helper "Qualified expenses incurred and paid in 2025 for this person's care".

Model: The helper includes expenses paid with dependent care benefits and leaves the subtraction to Form 2441. The IRS instructions say to leave them out of this column: "If you completed Part III, don't include in column (d) any benefits shown on line 28" (Form 2441, line 30: "Don't include in column (d) any benefits shown on line 28 above").

Ruling: ambiguity — amb.2025.dc_line30 (owner's decision, Stage 15 decision 6), as ruled before this rerun. Form 2441 line 30 says "Don't include in column (d) any benefits shown on line 28 above"; the project keeps each person's column (d) before excluding the dependent care benefits and subtracts line 28 from the total, because the instructions give no rule for dividing line 28 among the qualifying persons. The rendering's reading (net each column (d)) is the unchosen reading. The F1 pass changed this line only by hiding it for a person who is not a qualifying person (i2441 p. 3, "Don't list a person on line 2 unless they are listed as an eligible person under Qualifying Person(s), earlier").

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MATCH**

Model: This matches "Check the box in column (c) if the qualifying person listed in column (a) was over age 12 at the time the care was provided and was disabled." Age 14 or older at year end means over 12 all year. For age 13 at year end, the program asks about care given at 13 or older while disabled.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MISMATCH**

Restated: Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Model: The question matches line 23, but the line is gated on the eligible-student helper. That helper accepts a Form 1098-T request only "after February 2, 2026". The IRS text says "After January 31, 2026, but before you file the return, you or the student must request", so a request on February 1 or 2 wrongly fails.

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MISMATCH**

Restated: Input — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?

Model: The question matches line 24 and its instructions, including the first-3-months-of-2026 rule. The line is reached only through the same eligible-student gate, which uses "after February 2, 2026" where the IRS says "After January 31, 2026" for the Form 1098-T request exception.

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MISMATCH**

Restated: Input — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?

Model: The question matches line 25 and its instructions, including disregarding proficiency-exam credit. The line is reached only through the eligible-student gate, whose Form 1098-T exception date differs from the IRS "After January 31, 2026".

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MISMATCH**

Restated: Input — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?

Model: The question matches line 26 ("convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance"). The line is reached only through the eligible-student gate, whose Form 1098-T exception date differs from the IRS "After January 31, 2026".

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The amount is right: worksheet line 4 (expenses paid to the institution plus course materials, less lines 2a+2b+2c, not below zero), capped at $4,000, with periods that cannot be netted refused. The student gate differs from the IRS Form 1098-T exception, "After January 31, 2026" versus the program's "after February 2, 2026", which changes who gets the line.

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The computation matches "Subtract $2,000 from line 27. If zero or less, enter -0-." The line is gated by the AOC student test, which relies on the eligible-student helper's Form 1098-T date ("after February 2, 2026" versus the IRS "After January 31, 2026").

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 29 — Multiply line 28 by 25% (0.25)
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The computation matches "Multiply line 28 by 25% (0.25)." The line is gated through the eligible-student helper, whose Form 1098-T request window differs from the IRS "After January 31, 2026".

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The computation matches "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29." The line is gated through the eligible-student helper, whose Form 1098-T request window differs from the IRS "After January 31, 2026".

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MISMATCH**

Restated: Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → helper "No amount for this person"]

Model: The amount is right: LLC adjusted expenses are tuition, fees and required institution-paid materials less lines 2a+2b+2c, not below zero, for a student not completing lines 27–30, with the TIN case refused. The eligible-student gate's Form 1098-T exception says "after February 2, 2026" where the IRS says "After January 31, 2026".

Ruling: ambiguity — amb.2025.edu_1098t_date (owner's decision D7(d), 2026-10-29). The model's only objection is the Form 1098-T request date in the eligible-student helper (dependent.edu_1098t): i8863 p. 1 says "After January 31, 2026, but before you file the return", and p970 p. 2 says "After February 2, 2026 (January 31 falls on a Saturday)"; the project chose Pub. 970, the later revision. The model found the line's own question or computation to match the page. This line's rendering is otherwise unchanged by the F1 pass except for line 31's new refusal, which the model accepted ("with the TIN case refused").

## Raw response

```yaml
```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The helper includes expenses paid with dependent care benefits and leaves the subtraction to Form 2441. The IRS instructions say to leave them out of this column: \"If you completed Part III, don't include in column (d) any benefits shown on line 28\" (Form 2441, line 30: \"Don't include in column (d) any benefits shown on line 28 above\")."
  - key: "2(c)"
    status: MATCH
    reason: "This matches \"Check the box in column (c) if the qualifying person listed in column (a) was over age 12 at the time the care was provided and was disabled.\" Age 14 or older at year end means over 12 all year. For age 13 at year end, the program asks about care given at 13 or older while disabled."
  - key: "23"
    status: MISMATCH
    reason: "The question matches line 23, but the line is gated on the eligible-student helper. That helper accepts a Form 1098-T request only \"after February 2, 2026\". The IRS text says \"After January 31, 2026, but before you file the return, you or the student must request\", so a request on February 1 or 2 wrongly fails."
  - key: "24"
    status: MISMATCH
    reason: "The question matches line 24 and its instructions, including the first-3-months-of-2026 rule. The line is reached only through the same eligible-student gate, which uses \"after February 2, 2026\" where the IRS says \"After January 31, 2026\" for the Form 1098-T request exception."
  - key: "25"
    status: MISMATCH
    reason: "The question matches line 25 and its instructions, including disregarding proficiency-exam credit. The line is reached only through the eligible-student gate, whose Form 1098-T exception date differs from the IRS \"After January 31, 2026\"."
  - key: "26"
    status: MISMATCH
    reason: "The question matches line 26 (\"convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance\"). The line is reached only through the eligible-student gate, whose Form 1098-T exception date differs from the IRS \"After January 31, 2026\"."
  - key: "27"
    status: MISMATCH
    reason: "The amount is right: worksheet line 4 (expenses paid to the institution plus course materials, less lines 2a+2b+2c, not below zero), capped at $4,000, with periods that cannot be netted refused. The student gate differs from the IRS Form 1098-T exception, \"After January 31, 2026\" versus the program's \"after February 2, 2026\", which changes who gets the line."
  - key: "28"
    status: MISMATCH
    reason: "The computation matches \"Subtract $2,000 from line 27. If zero or less, enter -0-.\" The line is gated by the AOC student test, which relies on the eligible-student helper's Form 1098-T date (\"after February 2, 2026\" versus the IRS \"After January 31, 2026\")."
  - key: "29"
    status: MISMATCH
    reason: "The computation matches \"Multiply line 28 by 25% (0.25).\" The line is gated through the eligible-student helper, whose Form 1098-T request window differs from the IRS \"After January 31, 2026\"."
  - key: "30"
    status: MISMATCH
    reason: "The computation matches \"If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29.\" The line is gated through the eligible-student helper, whose Form 1098-T request window differs from the IRS \"After January 31, 2026\"."
  - key: "31"
    status: MISMATCH
    reason: "The amount is right: LLC adjusted expenses are tuition, fees and required institution-paid materials less lines 2a+2b+2c, not below zero, for a student not completing lines 27–30, with the TIN case refused. The eligible-student gate's Form 1098-T exception says \"after February 2, 2026\" where the IRS says \"After January 31, 2026\"."
```
```
