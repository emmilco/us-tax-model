# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 72a08db71a3611702e179abf706d3aa699c4304f922f1d487126472a596e8d2c |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: Line 1 is 'Medical and dental expenses' and the caution says 'Do not include expenses reimbursed or paid by others.' An input of unreimbursed eligible expenses matches.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a allows 'either income taxes or general sales taxes.' The program supports only income taxes, and the sales-tax election is excluded by the sa.unsupported refusal.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Line 5b is 'State and local real estate taxes.' An input of the deductible amount matches.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Line 5c is 'State and local personal property taxes.' An input of the deductible amount matches.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is 'Home mortgage interest and points reported to you on Form 1098.' The limited cases (loans not used to buy, build or improve the home, or debt over the limit) are excluded by the sa.unsupported refusal.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is 'Gifts by cash or check.' Income-limited and carryover cases are excluded by the sa.charity_limited refusal.

### 2 — Amount from sa.agi
Status: **MATCH**

Model: Line 2 says 'Enter amount from Form 1040 or 1040-SR, line 11b.' The helper takes f1040 line 11b.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Line 3 says 'Multiply line 2 by 7.5% (0.075).' The program multiplies by 75/1000, which is the same rate.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Line 4 says 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.'

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Line 5d says 'Add lines 5a through 5c.'

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper chain follows worksheet lines 1 and 5–10: $40,000 less 30% of AGI over $500,000 ($250,000 MFS), then the larger of that or $10,000, halved if MFS, then the smaller of that or line 5d. The excluded-income addback on worksheet lines 3a–3e is excluded by the sa.excluded_income refusal.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: The instructions say line 6 includes 'income taxes you paid to a foreign country and generation-skipping tax.' Both are excluded by the sa.unsupported refusal, so $0 is right within the supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Line 8b is 'Home mortgage interest not reported to you on Form 1098.' This case is excluded by the sa.unsupported refusal, so $0 is right within the supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Line 8c is 'Points not reported to you on Form 1098.' This case is excluded by the sa.unsupported refusal, so $0 is right within the supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Line 13 is 'Carryover from prior year.' Carryovers are excluded by the sa.charity_limited refusal, so $0 is right within the supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Line 15 is casualty and theft losses from Form 4684. These are excluded by the sa.unsupported refusal, so $0 is right within the supported cases.

### 16 — Amount from sa.zero
Status: **MATCH**

Model: Line 16 is 'Other—from list in instructions.' Any deduction from that list is excluded by the sa.unsupported refusal, so $0 is right within the supported cases.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Line 7 says 'Add lines 5e and 6.'

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Line 8e says 'Add lines 8a through 8c.' Line 8d is reserved.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Line 9 is 'Investment interest. Attach Form 4952 if required.' Form 4952 line 8 is the 'Investment interest deduction.'

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Line 10 says 'Add lines 8e and 9.'

### 12 — Total supported noncash donations before income limits
Status: **UNCLEAR**

Restated: Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 12 is gifts 'Other than by cash or check.' The value gift.allowed and the gift entries it is summed over are not defined in the text given, so it cannot be confirmed that only noncash gifts are counted and that the cash gifts on line 11 are excluded.

Ruling: representation; project retained. The gift collection holds noncash gifts only (forms/2025/gift.yaml, cited to i8283), and `gift.allowed` is each entry's deductible amount after its Form 8283 screens; cash and check gifts are the line 11 input. No change to the data.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Line 14 says 'Add lines 11 through 13.'

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Line 17 says 'Add the amounts in the far right column for lines 4 through 16.' Those are lines 4, 7, 10, 14, 15 and 16.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Line 1 is 'Medical and dental expenses' and the caution says 'Do not include expenses reimbursed or paid by others.' An input of unreimbursed eligible expenses matches."
  - key: "5a"
    status: MATCH
    reason: "Line 5a allows 'either income taxes or general sales taxes.' The program supports only income taxes, and the sales-tax election is excluded by the sa.unsupported refusal."
  - key: "5b"
    status: MATCH
    reason: "Line 5b is 'State and local real estate taxes.' An input of the deductible amount matches."
  - key: "5c"
    status: MATCH
    reason: "Line 5c is 'State and local personal property taxes.' An input of the deductible amount matches."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is 'Home mortgage interest and points reported to you on Form 1098.' The limited cases (loans not used to buy, build or improve the home, or debt over the limit) are excluded by the sa.unsupported refusal."
  - key: "11"
    status: MATCH
    reason: "Line 11 is 'Gifts by cash or check.' Income-limited and carryover cases are excluded by the sa.charity_limited refusal."
  - key: "2"
    status: MATCH
    reason: "Line 2 says 'Enter amount from Form 1040 or 1040-SR, line 11b.' The helper takes f1040 line 11b."
  - key: "3"
    status: MATCH
    reason: "Line 3 says 'Multiply line 2 by 7.5% (0.075).' The program multiplies by 75/1000, which is the same rate."
  - key: "4"
    status: MATCH
    reason: "Line 4 says 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.'"
  - key: "5d"
    status: MATCH
    reason: "Line 5d says 'Add lines 5a through 5c.'"
  - key: "5e"
    status: MATCH
    reason: "The helper chain follows worksheet lines 1 and 5–10: $40,000 less 30% of AGI over $500,000 ($250,000 MFS), then the larger of that or $10,000, halved if MFS, then the smaller of that or line 5d. The excluded-income addback on worksheet lines 3a–3e is excluded by the sa.excluded_income refusal."
  - key: "6"
    status: MATCH
    reason: "The instructions say line 6 includes 'income taxes you paid to a foreign country and generation-skipping tax.' Both are excluded by the sa.unsupported refusal, so $0 is right within the supported cases."
  - key: "8b"
    status: MATCH
    reason: "Line 8b is 'Home mortgage interest not reported to you on Form 1098.' This case is excluded by the sa.unsupported refusal, so $0 is right within the supported cases."
  - key: "8c"
    status: MATCH
    reason: "Line 8c is 'Points not reported to you on Form 1098.' This case is excluded by the sa.unsupported refusal, so $0 is right within the supported cases."
  - key: "13"
    status: MATCH
    reason: "Line 13 is 'Carryover from prior year.' Carryovers are excluded by the sa.charity_limited refusal, so $0 is right within the supported cases."
  - key: "15"
    status: MATCH
    reason: "Line 15 is casualty and theft losses from Form 4684. These are excluded by the sa.unsupported refusal, so $0 is right within the supported cases."
  - key: "16"
    status: MATCH
    reason: "Line 16 is 'Other—from list in instructions.' Any deduction from that list is excluded by the sa.unsupported refusal, so $0 is right within the supported cases."
  - key: "7"
    status: MATCH
    reason: "Line 7 says 'Add lines 5e and 6.'"
  - key: "8e"
    status: MATCH
    reason: "Line 8e says 'Add lines 8a through 8c.' Line 8d is reserved."
  - key: "9"
    status: MATCH
    reason: "Line 9 is 'Investment interest. Attach Form 4952 if required.' Form 4952 line 8 is the 'Investment interest deduction.'"
  - key: "10"
    status: MATCH
    reason: "Line 10 says 'Add lines 8e and 9.'"
  - key: "12"
    status: UNCLEAR
    reason: "Line 12 is gifts 'Other than by cash or check.' The value gift.allowed and the gift entries it is summed over are not defined in the text given, so it cannot be confirmed that only noncash gifts are counted and that the cash gifts on line 11 are excluded."
  - key: "14"
    status: MATCH
    reason: "Line 14 says 'Add lines 11 through 13.'"
  - key: "17"
    status: MATCH
    reason: "Line 17 says 'Add the amounts in the far right column for lines 4 through 16.' Those are lines 4, 7, 10, 14, 15 and 16."
```
