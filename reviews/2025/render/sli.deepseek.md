# Render comparison — sli

The rendered English of every printed line of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` (`rendered/2025/sli.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| line-scoped reviews | 1 (latest 2026-11-04); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b6d8bb710b67f5296af76c7849ff8e61fc8837977d9e2ebc72cc5cfbe7a82ced |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 45830749bffa8b7df0c0523207e522a36b1f83bfcbd6b48fa5a3ee55b3f2e1df |
| lines judged | 8 |
| match / mismatch / unclear / missing | 5 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the total interest you paid in 2025 on qualified student loans (see the instructions
Status: **MATCH**

Model: The IRS line says to enter total interest paid in 2025 on qualified student loans and not enter more than $2,500, which the restatement computes as the smaller of those two amounts. The refusal correctly mirrors the Exception requiring Pub. 970 for Form 2555, Form 4563, or excluded Puerto Rico income.
Reviewed in: pass 751dd786467e

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: The IRS line says to enter the amount from Form 1040 or 1040-SR line 9; the restatement uses f1040 line 9.

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, s1 line 20, and s1 line 25.

Model: The IRS line says to total "Schedule 1, lines 11 through 20, and 23 and 25"; the restatement omits Schedule 1 line 23 (Archer MSA deduction).

Ruling: open

### 4 — Subtract line 3 from line 2
Status: **MATCH**

Model: The IRS line says "Subtract line 3 from line 2," which is exactly what the restatement does.

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **MISMATCH**

Restated: Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.base_joint ($170,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.base_other ($85,000)"]

Model: The IRS says the deduction requires "any status except married filing separately" and line 5 lists only $85,000 for single/HOH/QSS and $170,000 for MFJ; assigning MFS $0 is not in the IRS text and does not exclude MFS.

Ruling: open

### 6 — Subtract line 5 from line 4
Status: **MISMATCH**

Restated: Subtract line 5 from line 4.

Model: The IRS line says "No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9"; the restatement subtracts line 5 from line 4 without that condition, so line 6 would be negative when line 4 is not more than line 5.

Ruling: open

### 8 — Multiply line 1 by line 7
Status: **MATCH**

Model: The restatement implements line 8 as line 1 times the line 7 ratio, with the ratio capped at 1.000 and zero when line 4 is not more than line 5, matching the IRS worksheet.

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **MATCH**

Model: The IRS line says to subtract line 8 from line 1; the added zero-or-less floor does not change the value because line 8 is capped at line 1.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1 | 7c4dbaaa35532b3e06522ca9e324fbffe4b43eb335ff32b4da97d2a4ef49e9b2 |
| 2 | 44a322e52fce7e7a028df233a318d945fcc9a2726176337b964ce5f20c99d463 |
| 3 | 9a7502bf57f013ced47f8150707fb8e150be4eb5138caec1da8a48527632a73b |
| 4 | e4e03402ab3d98b2d59c43c95d6607f6b5291dadd68687d950576d408e73913f |
| 5 | 5a97e4bc0f0144ba2ea1ed5e71505d3b7ff5e059ecc9bbb141867e92ed25f876 |
| 6 | 720bb61c4e5a977f8e56a97d2ee72953edcda9d2cf9ef9285a673caed8771e75 |
| 8 | ed1bc3b0be293664c0793145429d0ce816af825a511247376827c8866c5cfed5 |
| 9 | 9f5a76e3866c7af0a334d8fdc9aeff29357e2668cb6482285d1c11d0226ec0b6 |
| (rest of the document) | d6d486c34c7306cec96ffd4fcb63dac9cbe5b3cae1dbe18fa37601df3331b603 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 751dd786467e

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines 1 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 751dd786467e9323ebfc2146ac9e69579c335af528597549b10ba6653071183c |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 63584a89dc97ecdde8f26dd31069530cf9800f2f788d3960a48a72ddea4faff4 |
| receipt | .transcription/sli.deepseek.render.lines-6b86b273ff34 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| p4681 | 2025 | 5 | pages named by another document's citation | c280f0029d95f9f4186840c73600efd2af4bd3370a86a31fb4f2a9391887b2b6 | 5 | 21875d96efa2d4d7885584db3cf06d5830154aeff1eaf3370efad4fab5cc3a17 |

##### Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line says to enter total interest paid in 2025 on qualified student loans and not enter more than $2,500, which the restatement computes as the smaller of those two amounts. The refusal correctly mirrors the Exception requiring Pub. 970 for Form 2555, Form 4563, or excluded Puerto Rico income."
```

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: 'The restatement takes the smaller of total qualified student loan interest and $2,500, matching the IRS instruction not to enter more than $2,500, and the Pub. 970 refusal matches the stated exception.'
  - key: "2"
    status: MATCH
    reason: 'The IRS line says to enter the amount from Form 1040 or 1040-SR line 9; the restatement uses f1040 line 9.'
  - key: "3"
    status: MISMATCH
    reason: 'The IRS line says to total "Schedule 1, lines 11 through 20, and 23 and 25"; the restatement omits Schedule 1 line 23 (Archer MSA deduction).'
  - key: "4"
    status: MATCH
    reason: 'The IRS line says "Subtract line 3 from line 2," which is exactly what the restatement does.'
  - key: "5"
    status: MISMATCH
    reason: 'The IRS says the deduction requires "any status except married filing separately" and line 5 lists only $85,000 for single/HOH/QSS and $170,000 for MFJ; assigning MFS $0 is not in the IRS text and does not exclude MFS.'
  - key: "6"
    status: MISMATCH
    reason: 'The IRS line says "No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9"; the restatement subtracts line 5 from line 4 without that condition, so line 6 would be negative when line 4 is not more than line 5.'
  - key: "8"
    status: MATCH
    reason: 'The restatement implements line 8 as line 1 times the line 7 ratio, with the ratio capped at 1.000 and zero when line 4 is not more than line 5, matching the IRS worksheet.'
  - key: "9"
    status: MATCH
    reason: 'The IRS line says to subtract line 8 from line 1; the added zero-or-less floor does not change the value because line 8 is capped at line 1.'
```
