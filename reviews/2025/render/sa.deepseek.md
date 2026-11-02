# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5de99380799ad1169fa5acb2ca84317a6364e3fc97c141539848fdf2d0ad1dfe |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 131072 |
| subject sha256 | 07cf46dea57cb017583f862171ff7aecbb94337900ce0f92280207140c50232d |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040gi | 2025; printed date 2026-02-25 | 33, 34, 35, 91 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 34, 91 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i1040sca | 2025; printed date 2025-12-08 | 1, 7, 11 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 1, 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| p525 | 2025 | 33 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 33 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: Matches the IRS medical and dental expenses line, with the reimbursement caution reflected as unreimbursed eligible expenses.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Restates state/local income taxes and excludes the sales-tax election, which the unsupported gate refuses.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Matches state and local real estate taxes.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Matches state and local personal property taxes.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Matches Form 1098 home mortgage interest and points, limited to cases where the debt/use limits do not apply.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Matches cash/check gifts, with benefits received and substantiation reflected and income-limited cases refused.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: The IRS line says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement uses a helper that floors line 11b at zero, changing the amount when AGI is negative.

Ruling: ambiguity — amb.2025.sa_medical_negative_agi. The project floors AGI at zero for the medical-expense 7.5% limitation (the recorded reading), and the helper line 2 displays that floored amount. The IRS line says "Enter amount from Form 1040 or 1040-SR, line 11b"; a negative AGI is the registered ambiguity, not a new defect.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Matches multiplying line 2 by 7.5% (75/1000).

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Matches subtracting line 3 from line 1 and entering -0- when the result is zero or less.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Matches adding lines 5a through 5c.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: Matches the smaller-of line 5d or ceiling rule; the excluded-income refusal on the SALT worksheet covers the Form 2555/4563 and Puerto Rico addback cases.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: The only line 6 items in the provided instructions are foreign tax and GST, which the unsupported gate refuses; zero is correct within supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Line 8b is by definition non-Form 1098 mortgage interest, which the unsupported gate refuses; zero is correct within supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Line 8c is by definition points not reported on Form 1098, which the unsupported gate refuses; zero is correct within supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Carryover from a prior year is excluded by the charity_limited gate, so zero is correct within supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Casualty and theft losses are excluded by the unsupported gate, so zero is correct within supported cases.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: Computes gambling losses limited to Schedule 1 line 8b winnings, matching the IRS line 16 instruction for gambling losses.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Matches adding lines 5e and 6.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Matches adding lines 8a through 8c.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Matches the investment interest deduction from Form 4952 line 8.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Matches adding lines 8e and 9.

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Sums noncash charitable deductions through gift.allowed, with special appraisal and Section B cases refused.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Matches adding lines 11 through 13.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Matches adding the far-right-column amounts for lines 4 through 16 via the listed subtotals.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Matches the IRS medical and dental expenses line, with the reimbursement caution reflected as unreimbursed eligible expenses."
  - key: "5a"
    status: MATCH
    reason: "Restates state/local income taxes and excludes the sales-tax election, which the unsupported gate refuses."
  - key: "5b"
    status: MATCH
    reason: "Matches state and local real estate taxes."
  - key: "5c"
    status: MATCH
    reason: "Matches state and local personal property taxes."
  - key: "8a"
    status: MATCH
    reason: "Matches Form 1098 home mortgage interest and points, limited to cases where the debt/use limits do not apply."
  - key: "11"
    status: MATCH
    reason: "Matches cash/check gifts, with benefits received and substantiation reflected and income-limited cases refused."
  - key: "2"
    status: MISMATCH
    reason: "The IRS line says 'Enter amount from Form 1040 or 1040-SR, line 11b'; the restatement uses a helper that floors line 11b at zero, changing the amount when AGI is negative."
  - key: "3"
    status: MATCH
    reason: "Matches multiplying line 2 by 7.5% (75/1000)."
  - key: "4"
    status: MATCH
    reason: "Matches subtracting line 3 from line 1 and entering -0- when the result is zero or less."
  - key: "5d"
    status: MATCH
    reason: "Matches adding lines 5a through 5c."
  - key: "5e"
    status: MATCH
    reason: "Matches the smaller-of line 5d or ceiling rule; the excluded-income refusal on the SALT worksheet covers the Form 2555/4563 and Puerto Rico addback cases."
  - key: "6"
    status: MATCH
    reason: "The only line 6 items in the provided instructions are foreign tax and GST, which the unsupported gate refuses; zero is correct within supported cases."
  - key: "8b"
    status: MATCH
    reason: "Line 8b is by definition non-Form 1098 mortgage interest, which the unsupported gate refuses; zero is correct within supported cases."
  - key: "8c"
    status: MATCH
    reason: "Line 8c is by definition points not reported on Form 1098, which the unsupported gate refuses; zero is correct within supported cases."
  - key: "13"
    status: MATCH
    reason: "Carryover from a prior year is excluded by the charity_limited gate, so zero is correct within supported cases."
  - key: "15"
    status: MATCH
    reason: "Casualty and theft losses are excluded by the unsupported gate, so zero is correct within supported cases."
  - key: "16"
    status: MATCH
    reason: "Computes gambling losses limited to Schedule 1 line 8b winnings, matching the IRS line 16 instruction for gambling losses."
  - key: "7"
    status: MATCH
    reason: "Matches adding lines 5e and 6."
  - key: "8e"
    status: MATCH
    reason: "Matches adding lines 8a through 8c."
  - key: "9"
    status: MATCH
    reason: "Matches the investment interest deduction from Form 4952 line 8."
  - key: "10"
    status: MATCH
    reason: "Matches adding lines 8e and 9."
  - key: "12"
    status: MATCH
    reason: "Sums noncash charitable deductions through gift.allowed, with special appraisal and Section B cases refused."
  - key: "14"
    status: MATCH
    reason: "Matches adding lines 11 through 13."
  - key: "17"
    status: MATCH
    reason: "Matches adding the far-right-column amounts for lines 4 through 16 via the listed subtotals."
```
