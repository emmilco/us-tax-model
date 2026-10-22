# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4246337d73d2c1c2f178c6633b9abb5ee5ccfe96e85a8433d2161003306d2225 |
| subject sha256 | ab66706db2ea8567d4a4199c6ad096a6382090f8cd6ec34b7047b72f91af1eec |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: Schedule A line 1 is 'Medical and dental expenses' with the caution 'Do not include expenses reimbursed or paid by others.' The input is unreimbursed medical and dental expenses, which agrees.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a lets the filer include 'either income taxes or general sales taxes … but not both.' The program supports income taxes only, and the sales-tax election is refused through sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Line 5b is 'State and local real estate taxes (see instructions)', and the input is deductible state and local real estate taxes.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Line 5c is 'State and local personal property taxes', and the input is the same.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is 'Home mortgage interest and points reported to you on Form 1098. See instructions if limited.' Cases where debt or use limits apply are refused through sa.unsupported.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is 'Gifts by cash or check.' Income-limited charitable deductions are refused through sa.charity_limited, so taking the amount before income limits is correct within the supported cases.

### 2 — Amount from sa.agi
Status: **MATCH**

Model: Line 2 says 'Enter amount from Form 1040 or 1040-SR, line 11b', and the restatement does that.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Line 3 says 'Multiply line 2 by 7.5% (0.075)', and 75/1000 equals 0.075.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Line 4 says 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-', and the restatement does that.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Line 5d says 'Add lines 5a through 5c', and the restatement does that.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The restatement takes the smaller of line 5d and a ceiling. The ceiling is max($40,000 − 30% × (AGI − $500,000, or $250,000 if MFS), $10,000), halved if MFS. This reproduces SALT Worksheet lines 1–10, including 'half the amount on line 9 if married filing separately'. When AGI is under the threshold it reduces to the form's $40,000 ($20,000 MFS). Cases with excluded income are refused through sa.excluded_income.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: The instructions say line 6 includes 'income taxes you paid to a foreign country and generation-skipping tax (GST)'. Both are refused through sa.unsupported, so $0 is correct within the supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Line 8b is 'Home mortgage interest not reported to you on Form 1098'. Mortgage interest not on Form 1098 is refused through sa.unsupported, so $0 is correct within the supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Line 8c is 'Points not reported to you on Form 1098'. Points not on Form 1098 are refused through sa.unsupported, so $0 is correct within the supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Line 13 is 'Carryover from prior year'. Carried-over charitable deductions are refused through sa.charity_limited, so $0 is correct within the supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Line 15 is 'Casualty and theft loss(es) from a federally declared disaster'. Any casualty or theft loss is refused through sa.unsupported, so $0 is correct within the supported cases.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: The instructions allow 'Gambling losses … but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'; the restatement takes the smaller of losses and s1 line 8b. Other list items and net qualified disaster losses are refused through sa.unsupported.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Line 7 says 'Add lines 5e and 6', and the restatement does that.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Line 8e says 'Add lines 8a through 8c'; line 8d is 'Reserved for future use'. The restatement adds 8a, 8b and 8c.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Line 9 is 'Investment interest. Attach Form 4952 if required.' Form 4952 line 8 is the 'Investment interest deduction', so taking that amount agrees.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Line 10 says 'Add lines 8e and 9', and the restatement does that.

### 12 — Total supported noncash donations before income limits
Status: **UNCLEAR**

Restated: Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 12 is 'Other than by cash or check.' The restatement sums 'gift.allowed' over gift entries, but gift.allowed and the gift roster are not defined in the glossary. Without that definition I cannot tell whether the sum covers only noncash gifts at the deductible amount.

Ruling: representation; project retained. The gift collection holds noncash gifts only (forms/2025/gift.yaml, cited to i8283), and gift.allowed is each entry's deductible amount after its Form 8283 screens; cash and check gifts are the line 11 input (f1040sa line 12, "Other than by cash or check"). The per-gift rules are judged in the logs of `gift`. Same in substance as the earlier rulings on this line. No change to the data.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Line 14 says 'Add lines 11 through 13', and the restatement does that.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Line 17 says 'Add the amounts in the far right column for lines 4 through 16'. Those far-right lines are 4, 7, 10, 14, 15 and 16, which is what the restatement adds.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Schedule A line 1 is 'Medical and dental expenses' with the caution 'Do not include expenses reimbursed or paid by others.' The input is unreimbursed medical and dental expenses, which agrees."
  - key: "5a"
    status: MATCH
    reason: "Line 5a lets the filer include 'either income taxes or general sales taxes … but not both.' The program supports income taxes only, and the sales-tax election is refused through sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "Line 5b is 'State and local real estate taxes (see instructions)', and the input is deductible state and local real estate taxes."
  - key: "5c"
    status: MATCH
    reason: "Line 5c is 'State and local personal property taxes', and the input is the same."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is 'Home mortgage interest and points reported to you on Form 1098. See instructions if limited.' Cases where debt or use limits apply are refused through sa.unsupported."
  - key: "11"
    status: MATCH
    reason: "Line 11 is 'Gifts by cash or check.' Income-limited charitable deductions are refused through sa.charity_limited, so taking the amount before income limits is correct within the supported cases."
  - key: "2"
    status: MATCH
    reason: "Line 2 says 'Enter amount from Form 1040 or 1040-SR, line 11b', and the restatement does that."
  - key: "3"
    status: MATCH
    reason: "Line 3 says 'Multiply line 2 by 7.5% (0.075)', and 75/1000 equals 0.075."
  - key: "4"
    status: MATCH
    reason: "Line 4 says 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-', and the restatement does that."
  - key: "5d"
    status: MATCH
    reason: "Line 5d says 'Add lines 5a through 5c', and the restatement does that."
  - key: "5e"
    status: MATCH
    reason: "The restatement takes the smaller of line 5d and a ceiling. The ceiling is max($40,000 − 30% × (AGI − $500,000, or $250,000 if MFS), $10,000), halved if MFS. This reproduces SALT Worksheet lines 1–10, including 'half the amount on line 9 if married filing separately'. When AGI is under the threshold it reduces to the form's $40,000 ($20,000 MFS). Cases with excluded income are refused through sa.excluded_income."
  - key: "6"
    status: MATCH
    reason: "The instructions say line 6 includes 'income taxes you paid to a foreign country and generation-skipping tax (GST)'. Both are refused through sa.unsupported, so $0 is correct within the supported cases."
  - key: "8b"
    status: MATCH
    reason: "Line 8b is 'Home mortgage interest not reported to you on Form 1098'. Mortgage interest not on Form 1098 is refused through sa.unsupported, so $0 is correct within the supported cases."
  - key: "8c"
    status: MATCH
    reason: "Line 8c is 'Points not reported to you on Form 1098'. Points not on Form 1098 are refused through sa.unsupported, so $0 is correct within the supported cases."
  - key: "13"
    status: MATCH
    reason: "Line 13 is 'Carryover from prior year'. Carried-over charitable deductions are refused through sa.charity_limited, so $0 is correct within the supported cases."
  - key: "15"
    status: MATCH
    reason: "Line 15 is 'Casualty and theft loss(es) from a federally declared disaster'. Any casualty or theft loss is refused through sa.unsupported, so $0 is correct within the supported cases."
  - key: "16"
    status: MATCH
    reason: "The instructions allow 'Gambling losses … but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'; the restatement takes the smaller of losses and s1 line 8b. Other list items and net qualified disaster losses are refused through sa.unsupported."
  - key: "7"
    status: MATCH
    reason: "Line 7 says 'Add lines 5e and 6', and the restatement does that."
  - key: "8e"
    status: MATCH
    reason: "Line 8e says 'Add lines 8a through 8c'; line 8d is 'Reserved for future use'. The restatement adds 8a, 8b and 8c."
  - key: "9"
    status: MATCH
    reason: "Line 9 is 'Investment interest. Attach Form 4952 if required.' Form 4952 line 8 is the 'Investment interest deduction', so taking that amount agrees."
  - key: "10"
    status: MATCH
    reason: "Line 10 says 'Add lines 8e and 9', and the restatement does that."
  - key: "12"
    status: UNCLEAR
    reason: "Line 12 is 'Other than by cash or check.' The restatement sums 'gift.allowed' over gift entries, but gift.allowed and the gift roster are not defined in the glossary. Without that definition I cannot tell whether the sum covers only noncash gifts at the deductible amount."
  - key: "14"
    status: MATCH
    reason: "Line 14 says 'Add lines 11 through 13', and the restatement does that."
  - key: "17"
    status: MATCH
    reason: "Line 17 says 'Add the amounts in the far right column for lines 4 through 16'. Those far-right lines are 4, 7, 10, 14, 15 and 16, which is what the restatement adds."
```
```
