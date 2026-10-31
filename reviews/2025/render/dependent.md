# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 28fa49b1970c8899a65b36e8950baed85fdb8a704cbb6c7d4fc14b42e512dfee |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | a912066380307126cf7fdc54dc2d4cae644ddc358e66e92e6310ac906ac234ac |
| lines judged | 11 |
| match / mismatch / unclear / missing | 8 / 3 / 0 / 0 |
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

Model: The restatement's input includes expenses paid with dependent care benefits and leaves Form 2441 to subtract them later, so the printed column holds the gross amount. The IRS text says 'If you completed Part III, don't include in column (d) any benefits shown on line 28' (also Form 2441 line 30: 'Don't include in column (d) any benefits shown on line 28 above').

Ruling: ambiguity; amb.2025.dc_line30 (owner ruling, Stage 15 decision 6, T-048). Form 2441 line 30: "Complete line 2 on page 1 of this form. Don't include in column (d) any benefits shown on line 28 above. Then, add the amounts in column (d) and enter the total here"; i2441 p. 3, Column (d): "If you completed Part III, don't include in column (d) any benefits shown on line 28"; the instructions give no rule for dividing line 28 among persons. The model reads the register's rejected reading (column (d) net of benefits). The chosen reading shows each person's expenses including those paid with dependent care benefits and subtracts line 28 once at line 30. dependent.dc_paid is unchanged since fix round 2. As ruled since round 2. The subject change of this round (BUG-0258, dependent.parent_home_paid) does not touch this line. Project stands.

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MISMATCH**

Restated: helper "A qualifying person for Form 2441 (you have care expenses, and this person is your dependent and either your qualifying child under 13 or not able to care for themselves and living with you for more than half the year)" = true and helper "Physically or mentally not able to care for themselves?" = true and (helper "Age at the end of 2025" > 13 (dc.child_age) or helper "Age at the end of 2025" = 13 (dc.child_age) and helper "Care provided while this qualifying person was age 13 or older and disabled" = true)

Model: The age and disability logic fits 'over age 12 at the time the care was provided and was disabled', but the qualifying-person helper requires the person to be your dependent, and no refusal covers all the exceptions. The Form 2441 instructions also include a disabled person whom you 'could claim as a dependent except: a. The disabled person had gross income of $5,200 or more, ... or c. You (or your spouse if filing jointly) could be claimed as a dependent on another taxpayer's 2025 tax return', so the box is wrongly left unchecked in those cases.

Ruling: interface gap; i2441 p. 1, Qualifying Person(s), item 3: "... whom you can claim as a dependent or could claim as a dependent except: a. The disabled person had gross income of $5,200 or more, b. The disabled person filed a joint return, or c. You (or your spouse if filing jointly) could be claimed as a dependent". The cases the model names are refused, but on Form 2441: f2441.qp_count refuses f2441.nondependent_gate ("A qualifying person you cannot claim as a dependent ... is outside this tool"), which is not in the dependent render the reviewer was given. The column (c) test itself matches, as the model says. BUG-0253's gross income definition does not change who reaches the gate. Same objection and ruling as fix rounds 2 and 3. Project stands.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MISMATCH**

Restated: Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Model: The question matches the form, but its gate uses a 1098-T exception requiring a request 'after February 2, 2026', while the Form 8863 instructions say 'After January 31, 2026, but before you file the return'. A request made February 1 or 2 fails the gate and drops the student from lines 23 to 31; this shared defect is reported only here.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29): i8863 p. 1, "After January 31, 2026, but before you file the return"; p970 p. 2, "After February 2, 2026 (January 31 falls on a Saturday)"; the register chooses Pub. 970, which the reviewer was not given. Line 23's own question matches, as the model says. The model objects only to the date in the eligible-student gate (dependent.edu_1098t), unchanged since fix round 2. Same objection as round 3. Project stands.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: This restates line 24 and its instruction that an academic period in the first 3 months of 2026 paid for in 2025 is treated as beginning in 2025, and the gate follows line 23's 'No' path. The Form 1098-T box 8 reference is not in the text given but does not change the test; the shared gate defect is reported at line 23.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: This matches line 25 and its instruction on 4 years of academic credit, disregarding credit awarded solely for proficiency examinations, and the gate follows line 24's 'Yes' path. The shared gate defect is reported at line 23.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: This matches line 26 and its instruction on a federal or state felony conviction before the end of 2025 for possession or distribution of a controlled substance, and the gate follows line 25's 'No' path. The shared gate defect is reported at line 23.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: Expenses including course materials, less worksheet line 3, floored at zero and capped at $4,000, match line 27 and the worksheet, and the refusal names the period-by-period case it excludes. The conditions for the American opportunity credit match the instructions; the shared gate defect is reported at line 23.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: Subtracting $2,000 from line 27 and entering zero if the result is zero or less matches 'Subtract $2,000 from line 27. If zero or less, enter -0-'. The shared gate defect is reported at line 23.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: Multiplying line 28 by 25% matches 'Multiply line 28 by 25% (0.25)'. The shared gate defect is reported at line 23.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: Using line 27 when line 28 is zero, and otherwise adding $2,000 to line 29, matches the printed line 30. The shared gate defect is reported at line 23.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: Expenses required to be paid to the institution, less worksheet line 3 and floored at zero, match the lifetime learning credit definition and worksheet, and the line is reported only when lines 27 to 30 are not, as the form requires. The refusal names the period-by-period case it excludes; the shared gate defect is reported at line 23.

## Raw response

```yaml
```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The restatement's input includes expenses paid with dependent care benefits and leaves Form 2441 to subtract them later, so the printed column holds the gross amount. The IRS text says 'If you completed Part III, don't include in column (d) any benefits shown on line 28' (also Form 2441 line 30: 'Don't include in column (d) any benefits shown on line 28 above')."
  - key: "2(c)"
    status: MISMATCH
    reason: "The age and disability logic fits 'over age 12 at the time the care was provided and was disabled', but the qualifying-person helper requires the person to be your dependent, and no refusal covers all the exceptions. The Form 2441 instructions also include a disabled person whom you 'could claim as a dependent except: a. The disabled person had gross income of $5,200 or more, ... or c. You (or your spouse if filing jointly) could be claimed as a dependent on another taxpayer's 2025 tax return', so the box is wrongly left unchecked in those cases."
  - key: "23"
    status: MISMATCH
    reason: "The question matches the form, but its gate uses a 1098-T exception requiring a request 'after February 2, 2026', while the Form 8863 instructions say 'After January 31, 2026, but before you file the return'. A request made February 1 or 2 fails the gate and drops the student from lines 23 to 31; this shared defect is reported only here."
  - key: "24"
    status: MATCH
    reason: "This restates line 24 and its instruction that an academic period in the first 3 months of 2026 paid for in 2025 is treated as beginning in 2025, and the gate follows line 23's 'No' path. The Form 1098-T box 8 reference is not in the text given but does not change the test; the shared gate defect is reported at line 23."
  - key: "25"
    status: MATCH
    reason: "This matches line 25 and its instruction on 4 years of academic credit, disregarding credit awarded solely for proficiency examinations, and the gate follows line 24's 'Yes' path. The shared gate defect is reported at line 23."
  - key: "26"
    status: MATCH
    reason: "This matches line 26 and its instruction on a federal or state felony conviction before the end of 2025 for possession or distribution of a controlled substance, and the gate follows line 25's 'No' path. The shared gate defect is reported at line 23."
  - key: "27"
    status: MATCH
    reason: "Expenses including course materials, less worksheet line 3, floored at zero and capped at $4,000, match line 27 and the worksheet, and the refusal names the period-by-period case it excludes. The conditions for the American opportunity credit match the instructions; the shared gate defect is reported at line 23."
  - key: "28"
    status: MATCH
    reason: "Subtracting $2,000 from line 27 and entering zero if the result is zero or less matches 'Subtract $2,000 from line 27. If zero or less, enter -0-'. The shared gate defect is reported at line 23."
  - key: "29"
    status: MATCH
    reason: "Multiplying line 28 by 25% matches 'Multiply line 28 by 25% (0.25)'. The shared gate defect is reported at line 23."
  - key: "30"
    status: MATCH
    reason: "Using line 27 when line 28 is zero, and otherwise adding $2,000 to line 29, matches the printed line 30. The shared gate defect is reported at line 23."
  - key: "31"
    status: MATCH
    reason: "Expenses required to be paid to the institution, less worksheet line 3 and floored at zero, match the lifetime learning credit definition and worksheet, and the line is reported only when lines 27 to 30 are not, as the form requires. The refusal names the period-by-period case it excludes; the shared gate defect is reported at line 23."
```
```
