# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5dfc7b17f56cb407e481e1b746cbfdc9be8cc1da271b809ffb28500dd2fcc6ac |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: The form asks for medical and dental expenses and cautions 'Do not include expenses reimbursed or paid by others.' Unreimbursed eligible expenses fits that.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a takes either income taxes or general sales taxes, 'but not both.' The program uses income taxes only and refuses the sales-tax election through sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Line 5b is 'State and local real estate taxes.' Deductible amounts as an input agree with it.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Line 5c is 'State and local personal property taxes.' The input agrees with it.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is 'Home mortgage interest and points reported to you on Form 1098. See instructions if limited.' Limited cases, and loans not all used to buy, build or improve the home, are refused through sa.unsupported.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is 'Gifts by cash or check,' with a caution about benefits received and $250 substantiation. Income-limited cases are refused through sa.charity_limited.

### 2 — Amount from sa.agi
Status: **MATCH**

Model: The form says 'Enter amount from Form 1040 or 1040-SR, line 11b.' The restatement does the same.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: The form says 'Multiply line 2 by 7.5% (0.075).' 75/1000 is the same rate.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: The form says 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.' The restatement does the same.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: The form says 'Add lines 5a through 5c.' The restatement does the same.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper chain follows worksheet lines 1–10: start at $40,000; subtract 30% of AGI over $500,000 ($250,000 MFS); take the larger of that or $10,000; halve if MFS; then take the smaller of that or line 5d. Excluded-income addbacks (worksheet lines 3a–3e) are refused through sa.excluded_income. The helper's label says 'Half ... if married filing separately,' but for other filers it correctly uses the full amount.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: The instructions say line 6 includes 'income taxes you paid to a foreign country and generation-skipping tax.' Both are refused through sa.unsupported, so $0 is right within the supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Line 8b is 'Home mortgage interest not reported to you on Form 1098.' Such interest is refused through sa.unsupported, so $0 is right within the supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Line 8c is 'Points not reported to you on Form 1098.' Such points are refused through sa.unsupported, so $0 is right within the supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Line 13 is 'Carryover from prior year.' Carryovers are refused through sa.charity_limited, so $0 is right within the supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Line 15 is 'Casualty and theft loss(es) from a federally declared disaster.' Casualty and theft losses are refused through sa.unsupported, so $0 is right within the supported cases.

### 16 — Amount from sa.zero
Status: **MATCH**

Model: Line 16 is 'Other—from list in instructions.' Line 16 deductions are refused through sa.unsupported, so $0 is right within the supported cases.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: The form says 'Add lines 5e and 6.' The restatement does the same.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: The form says 'Add lines 8a through 8c.' The restatement does the same.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Line 9 is 'Investment interest. Attach Form 4952 if required.' Form 4952 line 8 is 'Investment interest deduction,' which is the amount line 9 asks for.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: The form says 'Add lines 8e and 9.' The restatement does the same.

### 12 — Total supported noncash donations before income limits
Status: **UNCLEAR**

Restated: Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 12 is 'Other than by cash or check' (attach Form 8283 if over $500). The glossary does not define gift.allowed or the gift roster, and the line 12 instructions are not in the pages given, so the per-gift amount cannot be checked.

Ruling: representation; project retained. The gift collection holds noncash gifts only (forms/2025/gift.yaml, cited to i8283), and `gift.allowed` is each entry's deductible amount after its Form 8283 screens; cash and check gifts are the line 11 input. No change to the data.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: The form says 'Add lines 11 through 13.' The restatement does the same.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: The form says 'Add the amounts in the far right column for lines 4 through 16.' Those far-right lines are 4, 7, 10, 14, 15 and 16, which is what the restatement adds.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form asks for medical and dental expenses and cautions 'Do not include expenses reimbursed or paid by others.' Unreimbursed eligible expenses fits that."
  - key: "5a"
    status: MATCH
    reason: "Line 5a takes either income taxes or general sales taxes, 'but not both.' The program uses income taxes only and refuses the sales-tax election through sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "Line 5b is 'State and local real estate taxes.' Deductible amounts as an input agree with it."
  - key: "5c"
    status: MATCH
    reason: "Line 5c is 'State and local personal property taxes.' The input agrees with it."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is 'Home mortgage interest and points reported to you on Form 1098. See instructions if limited.' Limited cases, and loans not all used to buy, build or improve the home, are refused through sa.unsupported."
  - key: "11"
    status: MATCH
    reason: "Line 11 is 'Gifts by cash or check,' with a caution about benefits received and $250 substantiation. Income-limited cases are refused through sa.charity_limited."
  - key: "2"
    status: MATCH
    reason: "The form says 'Enter amount from Form 1040 or 1040-SR, line 11b.' The restatement does the same."
  - key: "3"
    status: MATCH
    reason: "The form says 'Multiply line 2 by 7.5% (0.075).' 75/1000 is the same rate."
  - key: "4"
    status: MATCH
    reason: "The form says 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.' The restatement does the same."
  - key: "5d"
    status: MATCH
    reason: "The form says 'Add lines 5a through 5c.' The restatement does the same."
  - key: "5e"
    status: MATCH
    reason: "The helper chain follows worksheet lines 1–10: start at $40,000; subtract 30% of AGI over $500,000 ($250,000 MFS); take the larger of that or $10,000; halve if MFS; then take the smaller of that or line 5d. Excluded-income addbacks (worksheet lines 3a–3e) are refused through sa.excluded_income. The helper's label says 'Half ... if married filing separately,' but for other filers it correctly uses the full amount."
  - key: "6"
    status: MATCH
    reason: "The instructions say line 6 includes 'income taxes you paid to a foreign country and generation-skipping tax.' Both are refused through sa.unsupported, so $0 is right within the supported cases."
  - key: "8b"
    status: MATCH
    reason: "Line 8b is 'Home mortgage interest not reported to you on Form 1098.' Such interest is refused through sa.unsupported, so $0 is right within the supported cases."
  - key: "8c"
    status: MATCH
    reason: "Line 8c is 'Points not reported to you on Form 1098.' Such points are refused through sa.unsupported, so $0 is right within the supported cases."
  - key: "13"
    status: MATCH
    reason: "Line 13 is 'Carryover from prior year.' Carryovers are refused through sa.charity_limited, so $0 is right within the supported cases."
  - key: "15"
    status: MATCH
    reason: "Line 15 is 'Casualty and theft loss(es) from a federally declared disaster.' Casualty and theft losses are refused through sa.unsupported, so $0 is right within the supported cases."
  - key: "16"
    status: MATCH
    reason: "Line 16 is 'Other—from list in instructions.' Line 16 deductions are refused through sa.unsupported, so $0 is right within the supported cases."
  - key: "7"
    status: MATCH
    reason: "The form says 'Add lines 5e and 6.' The restatement does the same."
  - key: "8e"
    status: MATCH
    reason: "The form says 'Add lines 8a through 8c.' The restatement does the same."
  - key: "9"
    status: MATCH
    reason: "Line 9 is 'Investment interest. Attach Form 4952 if required.' Form 4952 line 8 is 'Investment interest deduction,' which is the amount line 9 asks for."
  - key: "10"
    status: MATCH
    reason: "The form says 'Add lines 8e and 9.' The restatement does the same."
  - key: "12"
    status: UNCLEAR
    reason: "Line 12 is 'Other than by cash or check' (attach Form 8283 if over $500). The glossary does not define gift.allowed or the gift roster, and the line 12 instructions are not in the pages given, so the per-gift amount cannot be checked."
  - key: "14"
    status: MATCH
    reason: "The form says 'Add lines 11 through 13.' The restatement does the same."
  - key: "17"
    status: MATCH
    reason: "The form says 'Add the amounts in the far right column for lines 4 through 16.' Those far-right lines are 4, 7, 10, 14, 15 and 16, which is what the restatement adds."
```
```
