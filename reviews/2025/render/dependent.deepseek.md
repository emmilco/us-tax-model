# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d1e47a534101abdad58ea11f747e18dc9bd802952467abc2cd1d462eb6bbcfc6 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 243fbb1b83ecccf2a804d8ec1c79327e2f9a46c72283072f586ae626bb94d95f |
| lines judged | 11 |
| match / mismatch / unclear / missing | 10 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 10, 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 15, 18, 19, 20, 21, 22 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 15, 18, 19, 20, 21, 22 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 6, 7, 8, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 6, 7, 8, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
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

Model: The helper includes 'expenses paid with dependent care benefits', but Form 2441 line 2(d) instructions say 'If you completed Part III, don't include in column (d) any benefits shown on line 28.'

Ruling: ambiguity; amb.2025.dc_line30 (owner's decision, Stage 15 decision 6): column (d) shows each person's expenses including those paid with dependent care benefits and line 30 subtracts line 28 from the total; Form 2441 line 30 and i2441 p. 3, Column (d), "don't include in column (d) any benefits shown on line 28", give no rule for dividing line 28 among persons. The reviewer reads the rejected reading, as in the prior review; the R2 restructure of dependent.dc_paid keeps the words "expenses paid with dependent care benefits ... Form 2441 subtracts the benefits you exclude" unchanged. Project stands.
Reviewed in: pass c369181d2827

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MATCH**

Model: The restatement matches the Form 2441 column (c) checkbox for a qualifying person over age 12 at the time care was provided and disabled, with the age-13 case limited by the care-at-13-or-older-and-disabled helper.
Reviewed in: pass c369181d2827

### 23 — Has the American opportunity credit been claimed for this student for any 4 prior tax year
Status: **MATCH**

Model: This matches Form 8863 line 23 and its instruction that the American opportunity credit cannot be claimed if it was claimed for the student for any 4 prior tax years.

### 24 — Was the student enrolled at least half-time for at least one academic period that began or
Status: **MATCH**

Model: This matches Form 8863 line 24 and the instruction treating an academic period beginning in the first 3 months of 2026 as beginning in 2025 when qualified expenses were paid in 2025.

### 25 — Did the student complete the first 4 years of postsecondary education before 2025?
Status: **MATCH**

Model: This matches Form 8863 line 25 and the instruction on four years of postsecondary academic credit, disregarding credit awarded solely for proficiency examinations.

### 26 — Was the student convicted, before the end of 2025, of a felony for possession or distribut
Status: **MATCH**

Model: This matches Form 8863 line 26, including the federal or state felony controlled-substance conviction before the end of 2025.

### 27 — Adjusted qualified education expenses. Don't enter more than $4,000
Status: **MATCH**

Model: It uses Form 8863 Part III line 27 with the Adjusted Qualified Education Expenses Worksheet and applies only to an American opportunity credit student, matching the Form 8863 line 27 rules and $4,000 limit.
Reviewed in: pass c369181d2827

### 28 — Subtract $2,000 from line 27. If zero or less, enter -0-
Status: **MATCH**

Model: It uses Form 8863 Part III line 28 with the worksheet, matching the IRS line 28 computation of subtracting $2,000 from line 27, not below zero.
Reviewed in: pass c369181d2827

### 29 — Multiply line 28 by 25% (0.25)
Status: **MATCH**

Model: It uses Form 8863 Part III line 29 with the worksheet, matching the IRS line 29 computation of multiplying line 28 by 25%.
Reviewed in: pass c369181d2827

### 30 — American opportunity credit for this student. If line 28 is zero, enter the amount from li
Status: **MATCH**

Model: It uses Form 8863 Part III line 30 with the worksheet, matching the IRS line 30 rule for using line 27 when line 28 is zero and otherwise adding $2,000 to line 29.
Reviewed in: pass c369181d2827

### 31 — Adjusted qualified education expenses for the lifetime learning credit
Status: **MATCH**

Model: It uses Form 8863 Part III line 31 for a lifetime learning credit student, with the worksheet line 4 amount based on expenses required to be paid to the institution less adjustments, matching the LLC rules.
Reviewed in: pass c369181d2827

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 2(d) | f7e42973fe29ad72d98658d96dce0d09b8c81ec36865f67aa53f5dff8f10cf63 |
| 2(c) | d469bd18ec04026f6dbe31e33e6c5de811719198379aac7a89c10eb24d6c027e |
| 23 | 6ef859612fc9225528754b68254a0f904c73e2d5cbe8172eadcfd9a024d89b7e |
| 24 | 950b5911626062d8b6e371390ffa4abaa869d4f8ae8879b4c770300013e47632 |
| 25 | d478c5d661e7a967987ef96c88fb3d604b3cdf01a1cfcb6e3ba0e9ef25c1fcb4 |
| 26 | 411783735e8d1485648d29199c6cec2a0dcf0678979c53de8767046ed22d7ea8 |
| 27 | 8aba89fe5a5b4ddf82a34de55a8cfd6342324b6b09f0697ce4f2da2f20761949 |
| 28 | aa4364db50cf413860d16efcef4ef3ccc12a85659aabf70eab28431ac23cad11 |
| 29 | 4bed2737d8b3d20841ed8c7f71f8c22f5d9a3094f431ebb3143da8d6ccd210b0 |
| 30 | 7e92a188ecad9642020bcea7c1f901cf14013337d81dbdd588c450d89c1ff0f2 |
| 31 | 3444d69a52845c84db326e9275db5008f506d8ea60270a1668c8489f3f56562d |
| (rest of the document) | 85c13429612c31523d60858f9c1f8860027800b8a1a07fdceb234a74b1f8f973 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass c369181d2827

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 2(d), 2(c), 27, 28, 29, 30, 31 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | c369181d2827fe0225f081bb7565b3f894684023134b567f0965c95fbe848536 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | dbfcd664489ef5495d37c1e02641777f731b21167c61bf3f33e7b3eaa4b1eb6e |
| receipt | .transcription/dependent.deepseek.render.lines-808d50c042b1 |
| lines judged | 7 |
| match / mismatch / unclear / missing | 6 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 15, 17, 18, 19, 20, 21, 22 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 20, 21, 22 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 13, 15, 18, 19, 20, 21, 22 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 15, 18, 19, 20, 21, 22 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| p503 | For use in preparing 2025 returns | 3, 6, 7, 8, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 6, 7, 8, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 2, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 2, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| i8863 | 2025 | 1, 2, 3, 4, 8, 9 | cited pages | 71d45c0b03b4521697e7f4fd52bbcc489d7dac6a3645b6d36f514ae5992e2e4d | 1, 3, 4, 8, 9 | 6d486b4afb1f1647b7b99243cde905cf9def6b2813e5ed0bcb9925329c1e8a2b |
| f8863 | 2025 | 1, 2 | whole document | 8e2a766019b69e75af71e8da04f82a27534acb97f9ae4c2b72438a56d10d444e | - | 37bbeebd24c238e54a031ab21ac880feb5d8e9ce98f792e1b45d93e1bf8abc6c |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| p970 | 2025 | 11 | pages named by another document's citation | a5c80030374da420bbaf3118a8a42fe79092e8529663d02ef601b6ae06657e00 | 11 | f6622ed07641c7d4e2a217fb9d9b1fecb7ab16f08dbc758f1a0963e1fe677e0a |

##### Raw response

```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The helper includes 'expenses paid with dependent care benefits', but Form 2441 line 2(d) instructions say 'If you completed Part III, don't include in column (d) any benefits shown on line 28.'"
  - key: "2(c)"
    status: MATCH
    reason: "The restatement matches the Form 2441 column (c) checkbox for a qualifying person over age 12 at the time care was provided and disabled, with the age-13 case limited by the care-at-13-or-older-and-disabled helper."
  - key: "27"
    status: MATCH
    reason: "It uses Form 8863 Part III line 27 with the Adjusted Qualified Education Expenses Worksheet and applies only to an American opportunity credit student, matching the Form 8863 line 27 rules and $4,000 limit."
  - key: "28"
    status: MATCH
    reason: "It uses Form 8863 Part III line 28 with the worksheet, matching the IRS line 28 computation of subtracting $2,000 from line 27, not below zero."
  - key: "29"
    status: MATCH
    reason: "It uses Form 8863 Part III line 29 with the worksheet, matching the IRS line 29 computation of multiplying line 28 by 25%."
  - key: "30"
    status: MATCH
    reason: "It uses Form 8863 Part III line 30 with the worksheet, matching the IRS line 30 rule for using line 27 when line 28 is zero and otherwise adding $2,000 to line 29."
  - key: "31"
    status: MATCH
    reason: "It uses Form 8863 Part III line 31 for a lifetime learning credit student, with the worksheet line 4 amount based on expenses required to be paid to the institution less adjustments, matching the LLC rules."
```

## Raw response

```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The IRS column (d) instruction says, 'If you completed Part III, don't include in column (d) any benefits shown on line 28.' The helper instead includes expenses paid with dependent care benefits and only says Form 2441 subtracts the excluded benefits later."
  - key: "2(c)"
    status: MATCH
    reason: "The checkbox condition matches Form 2441 column (c): the qualifying person must have been over age 12 when the care was provided and disabled, with the age-13 case tied to care provided while age 13 or older and disabled."
  - key: "23"
    status: MATCH
    reason: "This matches Form 8863 line 23 and its instruction that the American opportunity credit cannot be claimed if it was claimed for the student for any 4 prior tax years."
  - key: "24"
    status: MATCH
    reason: "This matches Form 8863 line 24 and the instruction treating an academic period beginning in the first 3 months of 2026 as beginning in 2025 when qualified expenses were paid in 2025."
  - key: "25"
    status: MATCH
    reason: "This matches Form 8863 line 25 and the instruction on four years of postsecondary academic credit, disregarding credit awarded solely for proficiency examinations."
  - key: "26"
    status: MATCH
    reason: "This matches Form 8863 line 26, including the federal or state felony controlled-substance conviction before the end of 2025."
  - key: "27"
    status: MATCH
    reason: "The line uses the adjusted qualified education expenses worksheet amount capped at $4,000, which is what Form 8863 line 27 says."
  - key: "28"
    status: MATCH
    reason: "The line subtracts $2,000 from line 27 and applies the zero floor, matching Form 8863 line 28."
  - key: "29"
    status: MATCH
    reason: "The line multiplies line 28 by 25%, matching Form 8863 line 29."
  - key: "30"
    status: MATCH
    reason: "The line uses line 27 if line 28 is zero; otherwise it adds $2,000 to line 29, matching Form 8863 line 30."
  - key: "31"
    status: MATCH
    reason: "The line uses the lifetime learning worksheet line 4, i.e. institution-paid qualified expenses less worksheet line 3 with a zero floor, which is the adjusted qualified education expenses for Form 8863 line 31."
```
