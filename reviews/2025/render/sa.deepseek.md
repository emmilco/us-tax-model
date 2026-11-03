# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a30ff8ec442e3f90231245c434d6e9bf5a496aeb4e308b66920b25522dece917 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | d42c175ca1e109cb98b2250ef0f1ffd8a68f38a4d93defa0eb5738e63cb2092b |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35, 91 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34, 91 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 2, 3, 6, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 2, 3, 6, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| p969 | 2025 | 9, 13 | pages named by another document's citation | 0491c6445304fc8c1b7ae3097b8a3ea30260bb35f706da40900d06416502b9c8 | 9, 13 | f643ce7086d88eabd1d8006ab0b5609f775af36b9b8a5b74637e1f366d8c29c3 |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: The restatement matches Schedule A line 1 and its instructions, including reimbursement reduction, exclusions, long-term-care limits, and the $50 lodging limit.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: The restatement matches line 5a for state and local income taxes when no sales-tax election is made, and it treats U.S. territory taxes as instructed.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: The restatement matches line 5b, including the 2025 payment and assessment-before-2026 rule and U.S. territory taxes except the excluded-income portion.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: The restatement matches line 5c for deductible state and local personal property taxes and U.S. territory taxes except the excluded-income portion.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: The restatement matches line 8a for Form 1098 home mortgage interest and points when the debt and use limits do not apply.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: The restatement matches line 11 for cash and check gifts before income limits, after benefits received and required substantiation.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: IRS line 2 says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement instead uses an AGI floored at zero, which changes the amount if line 11b is negative.

Ruling: ambiguity (amb.2025.sa_medical_negative_agi); the project floors AGI at zero for the 7.5% limit, the recorded reading.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: IRS says multiply line 2 by 7.5% (0.075); 75/1000 equals 0.075.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: IRS says subtract line 3 from line 1 and enter -0- if line 3 is more than line 1; the restatement is equivalent.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: IRS says add lines 5a through 5c; the restatement does that.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: Within supported cases, the helper applies the worksheet ceiling, reduction, and MFS halving correctly; excluded-income cases are refused.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: IRS line 6 covers other taxes such as foreign income taxes and GST; the program refuses those cases and uses zero otherwise.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: IRS line 8b is mortgage interest not reported on Form 1098; the program refuses those cases and uses zero within supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: IRS line 8c is points not reported on Form 1098; the program refuses those cases and uses zero within supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: IRS line 13 is prior-year charitable carryover; the program refuses carryover and income-limited charitable cases and uses zero otherwise.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: IRS line 15 is casualty and theft loss from Form 4684; the program refuses casualty and theft cases and uses zero otherwise.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: IRS line 16 allows gambling losses only to the extent of Schedule 1 line 8b winnings; the program does that and refuses other line 16 items.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: IRS says add lines 5e and 6; the restatement does that.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: IRS says add lines 8a through 8c; the restatement does that.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: IRS line 9 is investment interest from Form 4952 line 8; the restatement uses that amount.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: IRS says add lines 8e and 9; the restatement does that.

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Within supported cases, the restatement aggregates allowed noncash charitable gift deductions before income limits, with special and Section B cases refused.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: IRS says add lines 11 through 13; the restatement does that.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: IRS total is the sum of the far-right amounts for lines 4 through 16, which reduces to lines 4, 7, 10, 14, 15, and 16.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The restatement matches Schedule A line 1 and its instructions, including reimbursement reduction, exclusions, long-term-care limits, and the $50 lodging limit."
  - key: "5a"
    status: MATCH
    reason: "The restatement matches line 5a for state and local income taxes when no sales-tax election is made, and it treats U.S. territory taxes as instructed."
  - key: "5b"
    status: MATCH
    reason: "The restatement matches line 5b, including the 2025 payment and assessment-before-2026 rule and U.S. territory taxes except the excluded-income portion."
  - key: "5c"
    status: MATCH
    reason: "The restatement matches line 5c for deductible state and local personal property taxes and U.S. territory taxes except the excluded-income portion."
  - key: "8a"
    status: MATCH
    reason: "The restatement matches line 8a for Form 1098 home mortgage interest and points when the debt and use limits do not apply."
  - key: "11"
    status: MATCH
    reason: "The restatement matches line 11 for cash and check gifts before income limits, after benefits received and required substantiation."
  - key: "2"
    status: MISMATCH
    reason: "IRS line 2 says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement instead uses an AGI floored at zero, which changes the amount if line 11b is negative."
  - key: "3"
    status: MATCH
    reason: "IRS says multiply line 2 by 7.5% (0.075); 75/1000 equals 0.075."
  - key: "4"
    status: MATCH
    reason: "IRS says subtract line 3 from line 1 and enter -0- if line 3 is more than line 1; the restatement is equivalent."
  - key: "5d"
    status: MATCH
    reason: "IRS says add lines 5a through 5c; the restatement does that."
  - key: "5e"
    status: MATCH
    reason: "Within supported cases, the helper applies the worksheet ceiling, reduction, and MFS halving correctly; excluded-income cases are refused."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 covers other taxes such as foreign income taxes and GST; the program refuses those cases and uses zero otherwise."
  - key: "8b"
    status: MATCH
    reason: "IRS line 8b is mortgage interest not reported on Form 1098; the program refuses those cases and uses zero within supported cases."
  - key: "8c"
    status: MATCH
    reason: "IRS line 8c is points not reported on Form 1098; the program refuses those cases and uses zero within supported cases."
  - key: "13"
    status: MATCH
    reason: "IRS line 13 is prior-year charitable carryover; the program refuses carryover and income-limited charitable cases and uses zero otherwise."
  - key: "15"
    status: MATCH
    reason: "IRS line 15 is casualty and theft loss from Form 4684; the program refuses casualty and theft cases and uses zero otherwise."
  - key: "16"
    status: MATCH
    reason: "IRS line 16 allows gambling losses only to the extent of Schedule 1 line 8b winnings; the program does that and refuses other line 16 items."
  - key: "7"
    status: MATCH
    reason: "IRS says add lines 5e and 6; the restatement does that."
  - key: "8e"
    status: MATCH
    reason: "IRS says add lines 8a through 8c; the restatement does that."
  - key: "9"
    status: MATCH
    reason: "IRS line 9 is investment interest from Form 4952 line 8; the restatement uses that amount."
  - key: "10"
    status: MATCH
    reason: "IRS says add lines 8e and 9; the restatement does that."
  - key: "12"
    status: MATCH
    reason: "Within supported cases, the restatement aggregates allowed noncash charitable gift deductions before income limits, with special and Section B cases refused."
  - key: "14"
    status: MATCH
    reason: "IRS says add lines 11 through 13; the restatement does that."
  - key: "17"
    status: MATCH
    reason: "IRS total is the sum of the far-right amounts for lines 4 through 16, which reduces to lines 4, 7, 10, 14, 15, and 16."
```
