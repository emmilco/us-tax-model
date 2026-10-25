# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1029f15f22721147e31bd0c17653daad2e15602b716ba08b63c9a68e2372e012 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | bebc7c02c8aa1f42d39df14282d7609d61b67f805714977d544e2a0038bc1833 |
| lines judged | 24 |
| match / mismatch / unclear / missing | 21 / 2 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: Line 1 calls for medical and dental expenses, and the form cautions not to include expenses reimbursed or paid by others; the restatement's 'unreimbursed eligible' matches that.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a permits state and local income taxes or general sales taxes, but not both; the program limits to income taxes and the sales-tax election is an excluded unsupported case named by sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Line 5b is state and local real estate taxes; 'deductible state/local real estate taxes' is consistent.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Line 5c is state and local personal property taxes; matches.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is home mortgage interest and points reported on Form 1098; the program narrows to cases where the debt/use limits do not apply, which sa.unsupported names as excluded.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is gifts by cash or check; the program's after-benefits and substantiation conditions match the instructions, and income-limited/carryover cases are excluded by sa.charity_limited.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: IRS line 2 says simply 'Enter amount from Form 1040 or 1040-SR, line 11b'; the program adds a 'but not less than zero' floor, which is not in the line text.

Ruling: open

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: 7.5% equals 75/1000; matches 'Multiply line 2 by 7.5% (0.075)'.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Same direction and zero floor as 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-'.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Adds lines 5a through 5c, as the form says.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MISMATCH**

Restated: Enter the smaller of line 5d or helper "Half the worksheet ceiling if married filing separately".

Model: IRS line 5e says if you completed Form 2555 or 4563, or excluded Puerto Rico income, see the SALT worksheet; that worksheet adds those excluded amounts to line 11b. The program's ceiling helper uses only Form 1040 line 11b and there is no excluded-income refusal on line 5e.

Ruling: open

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Line 6 is other taxes; the only line 6 taxes identified in the provided instructions are foreign income taxes and GST, which the program excludes via sa.unsupported, so zero within supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Line 8b is mortgage interest not reported on Form 1098; the program sets zero and excludes non-1098 mortgage interest through sa.unsupported, naming the excluded item.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Line 8c is points not reported on Form 1098; the program excludes points not on Form 1098 through sa.unsupported, so zero within supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Line 13 is carryover from prior year; the program excludes carryovers and income-limited charitable deductions through sa.charity_limited, so zero within supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Line 15 is casualty and theft losses from a federally declared disaster; the program excludes casualty/theft losses through sa.unsupported, so zero within supported cases.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: Line 16 permits gambling losses only up to gambling winnings; the program computes the smaller of gambling losses and Schedule 1 line 8b and excludes other line 16 items via sa.unsupported.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Adds lines 5e and 6, as the form says.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Adds lines 8a through 8c, as the form says.

### 9 — Amount from f4952.line8
Status: **UNCLEAR**

Restated: Enter the amount from f4952 line 8.

Model: The provided Schedule A text only says 'Investment interest. Attach Form 4952 if required. See instructions'; the line 9 instructions, including how to figure investment interest when Form 4952 is not required, are not provided.

Ruling: open

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Adds lines 8e and 9, as the form says.

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Line 12 is gifts other than by cash or check; summing allowed gift deductions for confirmed gift entries matches the deduction amount, and the gift-helper refusals exclude appraisal/Section B special treatment.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Adds lines 11 through 13, as the form says.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Adds the far-right-column totals for lines 4 through 16, which are lines 4, 7, 10, 14, 15, and 16.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Line 1 calls for medical and dental expenses, and the form cautions not to include expenses reimbursed or paid by others; the restatement's 'unreimbursed eligible' matches that."
  - key: "5a"
    status: MATCH
    reason: "Line 5a permits state and local income taxes or general sales taxes, but not both; the program limits to income taxes and the sales-tax election is an excluded unsupported case named by sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "Line 5b is state and local real estate taxes; 'deductible state/local real estate taxes' is consistent."
  - key: "5c"
    status: MATCH
    reason: "Line 5c is state and local personal property taxes; matches."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is home mortgage interest and points reported on Form 1098; the program narrows to cases where the debt/use limits do not apply, which sa.unsupported names as excluded."
  - key: "11"
    status: MATCH
    reason: "Line 11 is gifts by cash or check; the program's after-benefits and substantiation conditions match the instructions, and income-limited/carryover cases are excluded by sa.charity_limited."
  - key: "2"
    status: MISMATCH
    reason: "IRS line 2 says simply 'Enter amount from Form 1040 or 1040-SR, line 11b'; the program adds a 'but not less than zero' floor, which is not in the line text."
  - key: "3"
    status: MATCH
    reason: "7.5% equals 75/1000; matches 'Multiply line 2 by 7.5% (0.075)'."
  - key: "4"
    status: MATCH
    reason: "Same direction and zero floor as 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-'."
  - key: "5d"
    status: MATCH
    reason: "Adds lines 5a through 5c, as the form says."
  - key: "5e"
    status: MISMATCH
    reason: "IRS line 5e says if you completed Form 2555 or 4563, or excluded Puerto Rico income, see the SALT worksheet; that worksheet adds those excluded amounts to line 11b. The program's ceiling helper uses only Form 1040 line 11b and there is no excluded-income refusal on line 5e."
  - key: "6"
    status: MATCH
    reason: "Line 6 is other taxes; the only line 6 taxes identified in the provided instructions are foreign income taxes and GST, which the program excludes via sa.unsupported, so zero within supported cases."
  - key: "8b"
    status: MATCH
    reason: "Line 8b is mortgage interest not reported on Form 1098; the program sets zero and excludes non-1098 mortgage interest through sa.unsupported, naming the excluded item."
  - key: "8c"
    status: MATCH
    reason: "Line 8c is points not reported on Form 1098; the program excludes points not on Form 1098 through sa.unsupported, so zero within supported cases."
  - key: "13"
    status: MATCH
    reason: "Line 13 is carryover from prior year; the program excludes carryovers and income-limited charitable deductions through sa.charity_limited, so zero within supported cases."
  - key: "15"
    status: MATCH
    reason: "Line 15 is casualty and theft losses from a federally declared disaster; the program excludes casualty/theft losses through sa.unsupported, so zero within supported cases."
  - key: "16"
    status: MATCH
    reason: "Line 16 permits gambling losses only up to gambling winnings; the program computes the smaller of gambling losses and Schedule 1 line 8b and excludes other line 16 items via sa.unsupported."
  - key: "7"
    status: MATCH
    reason: "Adds lines 5e and 6, as the form says."
  - key: "8e"
    status: MATCH
    reason: "Adds lines 8a through 8c, as the form says."
  - key: "9"
    status: UNCLEAR
    reason: "The provided Schedule A text only says 'Investment interest. Attach Form 4952 if required. See instructions'; the line 9 instructions, including how to figure investment interest when Form 4952 is not required, are not provided."
  - key: "10"
    status: MATCH
    reason: "Adds lines 8e and 9, as the form says."
  - key: "12"
    status: MATCH
    reason: "Line 12 is gifts other than by cash or check; summing allowed gift deductions for confirmed gift entries matches the deduction amount, and the gift-helper refusals exclude appraisal/Section B special treatment."
  - key: "14"
    status: MATCH
    reason: "Adds lines 11 through 13, as the form says."
  - key: "17"
    status: MATCH
    reason: "Adds the far-right-column totals for lines 4 through 16, which are lines 4, 7, 10, 14, 15, and 16."
```
