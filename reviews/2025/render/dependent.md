# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2173eacbc031c94545c0fcc58953615c8fde0dcbf86e682427e6004041ef7e26 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 99dd95c666b61d357e22cb2375b184e69153af3319e427d29484249e3dc0c829 |
| lines judged | 11 |
| match / mismatch / unclear / missing | 4 / 7 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 10, 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 19 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 19 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i8962 | 2025 | 8 | cited pages | 6b2be38425bc1a8b3073bfec01f18b7042e21187f37eec114ba185878be59976 | 8 | 11c5be397953d0f6bf8303148ac17e51c68c3cfed87cf2dc2de8a4173be5f309 |
| i8863 | 2025 | 1, 2, 3, 4, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |

## Lines

### 2(d) — Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
Status: **MISMATCH**

Restated: Enter the amount from helper "Qualified expenses incurred and paid in 2025 for this person's care".

Model: The helper includes 'expenses paid with dependent care benefits' and relies on Form 2441 to subtract them later. The IRS text says 'If you completed Part III, don't include in column (d) any benefits shown on line 28' (Form 2441, line 30), so column (d) itself must exclude those benefits.

Ruling: ambiguity; amb.2025.dc_line30 (owner ruling, Stage 15 decision 6, T-048). Form 2441 line 30: "Complete line 2 on page 1 of this form. Don't include in column (d) any benefits shown on line 28 above. Then, add the amounts in column (d) and enter the total here"; i2441 p. 3, Column (d): "If you completed Part III, don't include in column (d) any benefits shown on line 28"; the instructions give no rule for dividing line 28 among persons. The model reads the register's rejected reading (column (d) net of benefits). The chosen reading shows each person's expenses including those paid with dependent care benefits and subtracts line 28 once at line 30 (f2441.line30 is f2441.paid_total less f2441.line28), and the helper's English says what the project asks. Unchanged by Stage 19 and by the round-2 fixes; as ruled in rounds 2 to 4, Stage 18 and Stage 19 rounds 1 and 2. Project stands.

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MATCH**

Model: The box is checked when the qualifying person 'was over age 12 at the time the care was provided and was disabled.' The restatement checks it for a disabled qualifying person aged 14 or more at year end, or aged 13 at year end when the included care was given at 13 or older while disabled.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MISMATCH**

Restated: Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Model: The question matches the form and instructions ('claimed (by you or anyone else) for this student for any 4 tax years before 2025'). However, the gate's Form 1098-T exception requires the request to be made 'after February 2, 2026', while the IRS text says 'After January 31, 2026, but before you file the return'. That would wrongly exclude a student whose 1098-T was requested on February 1 or 2.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T"; p970 p. 2, Reminders: "After February 2, 2026 (January 31 falls on a Saturday), but before you file your 2025 tax return, you or the student must request that the educational institution furnish Form 1098-T." The model read i8863 correctly and the English says what the project asks (dependent.edu_1098t: "after February 2, 2026, but before you file"); the register records both dates and chooses Pub. 970, the later revision, which the reviewer was not given (p970 is not among its pages: an interface note, not a defect). Line 23's own question matches, as the model says; the date sits in the eligible-student gate (dependent.edu_student) that shows the line. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: Matches Form 8863 line 24 and requirement 3: at least half-time in at least one academic period beginning in 2025, or in the first 3 months of 2026 if paid in 2025, in a program leading to a degree or credential. The line is reached only when line 23 says No.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: Matches line 25 and requirement 1: the first 4 years were completed before 2025 as determined by the institution, excluding credit 'awarded solely because of the student's performance on proficiency examinations.'

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: Matches line 26 and requirement 4: 'convicted of a federal or state felony for possessing or distributing a controlled substance' as of the end of 2025.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The computation matches: worksheet line 4 (tuition, fees and course materials minus lines 2a+2b+2c, floored at 0), capped at '$4,000', with a refusal for netting across academic periods. The gate, however, uses the Form 1098-T exception date 'after February 2, 2026', where the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T"; p970 p. 2, Reminders: "After February 2, 2026 (January 31 falls on a Saturday), but before you file your 2025 tax return, you or the student must request that the educational institution furnish Form 1098-T." The model read i8863 correctly and the English says what the project asks (dependent.edu_1098t: "after February 2, 2026, but before you file"); the register records both dates and chooses Pub. 970, the later revision, which the reviewer was not given (p970 is not among its pages: an interface note, not a defect). The worksheet arithmetic, the $4,000 cap and the period refusal match, as the model says. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: 'Subtract $2,000 from line 27. If zero or less, enter -0-' is computed correctly. The gate inherits the 1098-T exception date error ('after February 2, 2026' instead of the IRS 'After January 31, 2026').

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T"; p970 p. 2, Reminders: "After February 2, 2026 (January 31 falls on a Saturday), but before you file your 2025 tax return, you or the student must request that the educational institution furnish Form 1098-T." The model read i8863 correctly and the English says what the project asks (dependent.edu_1098t: "after February 2, 2026, but before you file"); the register records both dates and chooses Pub. 970, the later revision, which the reviewer was not given (p970 is not among its pages: an interface note, not a defect). The subtraction matches, as the model says. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: 'Multiply line 28 by 25% (0.25)' is computed correctly. The gate inherits the 1098-T exception date error ('after February 2, 2026' instead of the IRS 'After January 31, 2026').

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T"; p970 p. 2, Reminders: "After February 2, 2026 (January 31 falls on a Saturday), but before you file your 2025 tax return, you or the student must request that the educational institution furnish Form 1098-T." The model read i8863 correctly and the English says what the project asks (dependent.edu_1098t: "after February 2, 2026, but before you file"); the register records both dates and chooses Pub. 970, the later revision, which the reviewer was not given (p970 is not among its pages: an interface note, not a defect). The 25% matches, as the model says. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: 'If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29' is computed correctly. The gate inherits the 1098-T exception date error ('after February 2, 2026' instead of the IRS 'After January 31, 2026').

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T"; p970 p. 2, Reminders: "After February 2, 2026 (January 31 falls on a Saturday), but before you file your 2025 tax return, you or the student must request that the educational institution furnish Form 1098-T." The model read i8863 correctly and the English says what the project asks (dependent.edu_1098t: "after February 2, 2026, but before you file"); the register records both dates and chooses Pub. 970, the later revision, which the reviewer was not given (p970 is not among its pages: an interface note, not a defect). The line 30 rule matches, as the model says. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MISMATCH**

Restated: Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → helper "No amount for this person"]

Model: The computation matches the lifetime learning credit's adjusted expenses: amounts required to be paid to the institution minus lines 2a+2b+2c, floored at 0, for a student not taking the AOC. The eligible-student gate uses 'after February 2, 2026' for the 1098-T exception, where the IRS text says 'After January 31, 2026'.

Ruling: ambiguity; amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T"; p970 p. 2, Reminders: "After February 2, 2026 (January 31 falls on a Saturday), but before you file your 2025 tax return, you or the student must request that the educational institution furnish Form 1098-T." The model read i8863 correctly and the English says what the project asks (dependent.edu_1098t: "after February 2, 2026, but before you file"); the register records both dates and chooses Pub. 970, the later revision, which the reviewer was not given (p970 is not among its pages: an interface note, not a defect). The lifetime learning amount matches, as the model says. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

## Raw response

```yaml
```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The helper includes 'expenses paid with dependent care benefits' and relies on Form 2441 to subtract them later. The IRS text says 'If you completed Part III, don't include in column (d) any benefits shown on line 28' (Form 2441, line 30), so column (d) itself must exclude those benefits."
  - key: "2(c)"
    status: MATCH
    reason: "The box is checked when the qualifying person 'was over age 12 at the time the care was provided and was disabled.' The restatement checks it for a disabled qualifying person aged 14 or more at year end, or aged 13 at year end when the included care was given at 13 or older while disabled."
  - key: "23"
    status: MISMATCH
    reason: "The question matches the form and instructions ('claimed (by you or anyone else) for this student for any 4 tax years before 2025'). However, the gate's Form 1098-T exception requires the request to be made 'after February 2, 2026', while the IRS text says 'After January 31, 2026, but before you file the return'. That would wrongly exclude a student whose 1098-T was requested on February 1 or 2."
  - key: "24"
    status: MATCH
    reason: "Matches Form 8863 line 24 and requirement 3: at least half-time in at least one academic period beginning in 2025, or in the first 3 months of 2026 if paid in 2025, in a program leading to a degree or credential. The line is reached only when line 23 says No."
  - key: "25"
    status: MATCH
    reason: "Matches line 25 and requirement 1: the first 4 years were completed before 2025 as determined by the institution, excluding credit 'awarded solely because of the student's performance on proficiency examinations.'"
  - key: "26"
    status: MATCH
    reason: "Matches line 26 and requirement 4: 'convicted of a federal or state felony for possessing or distributing a controlled substance' as of the end of 2025."
  - key: "27"
    status: MISMATCH
    reason: "The computation matches: worksheet line 4 (tuition, fees and course materials minus lines 2a+2b+2c, floored at 0), capped at '$4,000', with a refusal for netting across academic periods. The gate, however, uses the Form 1098-T exception date 'after February 2, 2026', where the IRS text says 'After January 31, 2026'."
  - key: "28"
    status: MISMATCH
    reason: "'Subtract $2,000 from line 27. If zero or less, enter -0-' is computed correctly. The gate inherits the 1098-T exception date error ('after February 2, 2026' instead of the IRS 'After January 31, 2026')."
  - key: "29"
    status: MISMATCH
    reason: "'Multiply line 28 by 25% (0.25)' is computed correctly. The gate inherits the 1098-T exception date error ('after February 2, 2026' instead of the IRS 'After January 31, 2026')."
  - key: "30"
    status: MISMATCH
    reason: "'If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29' is computed correctly. The gate inherits the 1098-T exception date error ('after February 2, 2026' instead of the IRS 'After January 31, 2026')."
  - key: "31"
    status: MISMATCH
    reason: "The computation matches the lifetime learning credit's adjusted expenses: amounts required to be paid to the institution minus lines 2a+2b+2c, floored at 0, for a student not taking the AOC. The eligible-student gate uses 'after February 2, 2026' for the 1098-T exception, where the IRS text says 'After January 31, 2026'."
```
```
