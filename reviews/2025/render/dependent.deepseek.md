# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2173eacbc031c94545c0fcc58953615c8fde0dcbf86e682427e6004041ef7e26 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: The helper includes expenses paid with dependent care benefits, but the Form 2441 line 2(d) instructions say: 'If you completed Part III, don't include in column (d) any benefits shown on line 28.'

Ruling: ambiguity; amb.2025.dc_line30 (owner ruling, Stage 15 decision 6, T-048). Form 2441 line 30: "Complete line 2 on page 1 of this form. Don't include in column (d) any benefits shown on line 28 above. Then, add the amounts in column (d) and enter the total here"; i2441 p. 3, Column (d): "If you completed Part III, don't include in column (d) any benefits shown on line 28"; the instructions give no rule for dividing line 28 among persons. The model reads the register's rejected reading (column (d) net of benefits). The chosen reading shows each person's expenses including those paid with dependent care benefits and subtracts line 28 once at line 30 (f2441.line30 is f2441.paid_total less f2441.line28), and the helper's English says what the project asks. Unchanged by Stage 19 and by the round-2 fixes; as ruled in rounds 2 to 4, Stage 18 and Stage 19 rounds 1 and 2. Project stands.

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MATCH**

Model: Within the dependents-only scope, the restatement tracks the column (c) condition that the qualifying person was over age 12 at the time care was provided and disabled.

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MISMATCH**

Restated: Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Model: The eligible-student gate uses the TIN helper that allows a student who has only 'applied for' an ITIN/ATIN; the IRS AOC text requires the student to have been 'issued a TIN by the due date'.

Ruling: interface gap; p970 p. 11 (not among the reviewer's pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return." i8863 p. 3, item 5: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." The model read the i8863 sentence correctly, but the pages it got omit the Pub. 970 rule that treats an ITIN or ATIN applied for by the due date, and then issued, as issued by the due date; under it the English of dependent.tin ("issued on or before the due date ... or have you applied for an ITIN or ATIN for this person by then") and household.all_tin ("or have applied for an ITIN") say what the source allows, as ruled in Stage 19 round 1 (person.findings.md, Checked, not findings). Line 23's own question matches, as the model says; the TIN test sits in the eligible-student gate. Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: The restatement matches the Form 8863 line 24 half-time enrollment test, including treating a period beginning in the first 3 months of 2026 as 2025 when expenses were paid in 2025.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: The restatement matches the line 25 four-years-of-postsecondary-education test, including excluding credit awarded solely for proficiency examinations.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: The restatement matches the line 26 felony drug conviction test.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The AOC student gate lets filers or students who have only applied for an ITIN qualify, but the IRS says 'If you haven’t been issued a TIN by the due date ... you can’t claim the American opportunity credit.'

Ruling: interface gap; p970 p. 11 (not among the reviewer's pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return." i8863 p. 3, item 5: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." The model read the i8863 sentence correctly, but the pages it got omit the Pub. 970 rule that treats an ITIN or ATIN applied for by the due date, and then issued, as issued by the due date; under it the English of dependent.tin ("issued on or before the due date ... or have you applied for an ITIN or ATIN for this person by then") and household.all_tin ("or have applied for an ITIN") say what the source allows, as ruled in Stage 19 round 1 (person.findings.md, Checked, not findings). The line's arithmetic is not disputed; the model objects only to the American opportunity gate (dependent.edu_aoc, household.all_tin for the filers). Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The line uses the same AOC student gate, which is broader than the IRS rule requiring filers and students to have been issued a TIN by the due date.

Ruling: interface gap; p970 p. 11 (not among the reviewer's pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return." i8863 p. 3, item 5: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." The model read the i8863 sentence correctly, but the pages it got omit the Pub. 970 rule that treats an ITIN or ATIN applied for by the due date, and then issued, as issued by the due date; under it the English of dependent.tin ("issued on or before the due date ... or have you applied for an ITIN or ATIN for this person by then") and household.all_tin ("or have applied for an ITIN") say what the source allows, as ruled in Stage 19 round 1 (person.findings.md, Checked, not findings). The line's arithmetic is not disputed; the model objects only to the American opportunity gate (dependent.edu_aoc, household.all_tin for the filers). Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 29 — Multiply line 28 by 25% (0.25)
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The line uses the same AOC student gate, which is broader than the IRS rule requiring filers and students to have been issued a TIN by the due date.

Ruling: interface gap; p970 p. 11 (not among the reviewer's pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return." i8863 p. 3, item 5: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." The model read the i8863 sentence correctly, but the pages it got omit the Pub. 970 rule that treats an ITIN or ATIN applied for by the due date, and then issued, as issued by the due date; under it the English of dependent.tin ("issued on or before the due date ... or have you applied for an ITIN or ATIN for this person by then") and household.all_tin ("or have applied for an ITIN") say what the source allows, as ruled in Stage 19 round 1 (person.findings.md, Checked, not findings). The line's arithmetic is not disputed; the model objects only to the American opportunity gate (dependent.edu_aoc, household.all_tin for the filers). Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MISMATCH**

Restated: Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]

Model: The line uses the same AOC student gate, which is broader than the IRS rule requiring filers and students to have been issued a TIN by the due date.

Ruling: interface gap; p970 p. 11 (not among the reviewer's pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return." i8863 p. 3, item 5: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." The model read the i8863 sentence correctly, but the pages it got omit the Pub. 970 rule that treats an ITIN or ATIN applied for by the due date, and then issued, as issued by the due date; under it the English of dependent.tin ("issued on or before the due date ... or have you applied for an ITIN or ATIN for this person by then") and household.all_tin ("or have applied for an ITIN") say what the source allows, as ruled in Stage 19 round 1 (person.findings.md, Checked, not findings). The line's arithmetic is not disputed; the model objects only to the American opportunity gate (dependent.edu_aoc, household.all_tin for the filers). Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MISMATCH**

Restated: Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → helper "No amount for this person"]

Model: The LLC student gate uses the same eligible-student TIN helper allowing only-applied ITINs, while the IRS table says for the lifetime learning credit 'Students must have been issued a TIN by the due date.'

Ruling: interface gap; p970 p. 11 (not among the reviewer's pages): "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return." i8863 p. 3, item 5: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." The model read the i8863 sentence correctly, but the pages it got omit the Pub. 970 rule that treats an ITIN or ATIN applied for by the due date, and then issued, as issued by the due date; under it the English of dependent.tin ("issued on or before the due date ... or have you applied for an ITIN or ATIN for this person by then") and household.all_tin ("or have applied for an ITIN") say what the source allows, as ruled in Stage 19 round 1 (person.findings.md, Checked, not findings). The amount is not disputed; the model objects only to the eligible-student gate's student TIN (dependent.tin). Why this line is new this round: the render prompt changed from round 2 only in dependent.qr_relationship (lawful now also for sibling_descendant), the dependent.lawful question and the dependent.edu_over label (diff of .transcription/dependent.render.prompt.txt against the round-2 archive); the text the model objects to is unchanged and was judged MATCH last round, so the new MISMATCH is reviewer variance, not the lawful change or its English.

## Raw response

```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The helper includes expenses paid with dependent care benefits, but the Form 2441 line 2(d) instructions say: 'If you completed Part III, don't include in column (d) any benefits shown on line 28.'"
  - key: "2(c)"
    status: MATCH
    reason: "Within the dependents-only scope, the restatement tracks the column (c) condition that the qualifying person was over age 12 at the time care was provided and disabled."
  - key: "23"
    status: MISMATCH
    reason: "The eligible-student gate uses the TIN helper that allows a student who has only 'applied for' an ITIN/ATIN; the IRS AOC text requires the student to have been 'issued a TIN by the due date'."
  - key: "24"
    status: MATCH
    reason: "The restatement matches the Form 8863 line 24 half-time enrollment test, including treating a period beginning in the first 3 months of 2026 as 2025 when expenses were paid in 2025."
  - key: "25"
    status: MATCH
    reason: "The restatement matches the line 25 four-years-of-postsecondary-education test, including excluding credit awarded solely for proficiency examinations."
  - key: "26"
    status: MATCH
    reason: "The restatement matches the line 26 felony drug conviction test."
  - key: "27"
    status: MISMATCH
    reason: "The AOC student gate lets filers or students who have only applied for an ITIN qualify, but the IRS says 'If you haven’t been issued a TIN by the due date ... you can’t claim the American opportunity credit.'"
  - key: "28"
    status: MISMATCH
    reason: "The line uses the same AOC student gate, which is broader than the IRS rule requiring filers and students to have been issued a TIN by the due date."
  - key: "29"
    status: MISMATCH
    reason: "The line uses the same AOC student gate, which is broader than the IRS rule requiring filers and students to have been issued a TIN by the due date."
  - key: "30"
    status: MISMATCH
    reason: "The line uses the same AOC student gate, which is broader than the IRS rule requiring filers and students to have been issued a TIN by the due date."
  - key: "31"
    status: MISMATCH
    reason: "The LLC student gate uses the same eligible-student TIN helper allowing only-applied ITINs, while the IRS table says for the lifetime learning credit 'Students must have been issued a TIN by the due date.'"
```
