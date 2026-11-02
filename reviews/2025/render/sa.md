# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5de99380799ad1169fa5acb2ca84317a6364e3fc97c141539848fdf2d0ad1dfe |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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

Model: The form asks for medical and dental expenses and cautions "Do not include expenses reimbursed or paid by others"; the input asks for unreimbursed eligible expenses.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a takes income taxes or general sales taxes, not both. The program uses income taxes only, and the sales-tax election is refused through sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: This restates "State and local real estate taxes" as a deductible input.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: This restates "State and local personal property taxes" as an input.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is "Home mortgage interest and points reported to you on Form 1098." Cases where the debt or use limits apply are refused through sa.unsupported.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is gifts by cash or check. Income-limited amounts and carryovers are refused through sa.charity_limited.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: The form says "Enter amount from Form 1040 or 1040-SR, line 11b" with no floor at zero. The helper floors AGI at zero, which changes lines 2 through 4 when line 11b is negative.

Ruling: ambiguity — amb.2025.sa_medical_negative_agi. The project floors AGI at zero for the medical-expense 7.5% limitation (the recorded reading), and the helper line 2 displays that floored amount; a negative AGI is the registered ambiguity.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: This matches "Multiply line 2 by 7.5% (0.075)."

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: This matches "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-."

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: This matches "Add lines 5a through 5c."

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper follows the SALT worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 MFS), not below $10,000, halved if MFS, then the smaller of that or line 5d. Below the threshold this gives $40,000 ($20,000 MFS), and excluded-income cases are refused.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Line 6 covers foreign income taxes and GST. The program sets it to zero and refuses those deductions through sa.unsupported.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: The program sets line 8b to zero. Mortgage interest not on Form 1098 is refused through sa.unsupported.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: The program sets line 8c to zero. Points not on Form 1098 are refused through sa.unsupported.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: The program sets line 13 to zero. Prior-year carryovers are refused through sa.charity_limited.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: The program sets line 15 to zero. Casualty and theft losses are refused through sa.unsupported.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: The instructions allow gambling losses "but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b"; the program uses the smaller of losses or line 8b. All other line 16 items are refused.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: This matches "Add lines 5e and 6."

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: This matches "Add lines 8a through 8c"; line 8d is reserved.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Line 9 is investment interest, with Form 4952 attached if required. Form 4952 line 8 is the investment interest deduction.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: This matches "Add lines 8e and 9."

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Line 12 is gifts other than by cash or check. The program sums noncash deductions before income limits, with appraisal and special-property cases refused.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: This matches "Add lines 11 through 13."

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: This matches "Add the amounts in the far right column for lines 4 through 16": lines 4, 7, 10, 14, 15 and 16.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form asks for medical and dental expenses and cautions \"Do not include expenses reimbursed or paid by others\"; the input asks for unreimbursed eligible expenses."
  - key: "5a"
    status: MATCH
    reason: "Line 5a takes income taxes or general sales taxes, not both. The program uses income taxes only, and the sales-tax election is refused through sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "This restates \"State and local real estate taxes\" as a deductible input."
  - key: "5c"
    status: MATCH
    reason: "This restates \"State and local personal property taxes\" as an input."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is \"Home mortgage interest and points reported to you on Form 1098.\" Cases where the debt or use limits apply are refused through sa.unsupported."
  - key: "11"
    status: MATCH
    reason: "Line 11 is gifts by cash or check. Income-limited amounts and carryovers are refused through sa.charity_limited."
  - key: "2"
    status: MISMATCH
    reason: "The form says \"Enter amount from Form 1040 or 1040-SR, line 11b\" with no floor at zero. The helper floors AGI at zero, which changes lines 2 through 4 when line 11b is negative."
  - key: "3"
    status: MATCH
    reason: "This matches \"Multiply line 2 by 7.5% (0.075).\""
  - key: "4"
    status: MATCH
    reason: "This matches \"Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.\""
  - key: "5d"
    status: MATCH
    reason: "This matches \"Add lines 5a through 5c.\""
  - key: "5e"
    status: MATCH
    reason: "The helper follows the SALT worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 MFS), not below $10,000, halved if MFS, then the smaller of that or line 5d. Below the threshold this gives $40,000 ($20,000 MFS), and excluded-income cases are refused."
  - key: "6"
    status: MATCH
    reason: "Line 6 covers foreign income taxes and GST. The program sets it to zero and refuses those deductions through sa.unsupported."
  - key: "8b"
    status: MATCH
    reason: "The program sets line 8b to zero. Mortgage interest not on Form 1098 is refused through sa.unsupported."
  - key: "8c"
    status: MATCH
    reason: "The program sets line 8c to zero. Points not on Form 1098 are refused through sa.unsupported."
  - key: "13"
    status: MATCH
    reason: "The program sets line 13 to zero. Prior-year carryovers are refused through sa.charity_limited."
  - key: "15"
    status: MATCH
    reason: "The program sets line 15 to zero. Casualty and theft losses are refused through sa.unsupported."
  - key: "16"
    status: MATCH
    reason: "The instructions allow gambling losses \"but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b\"; the program uses the smaller of losses or line 8b. All other line 16 items are refused."
  - key: "7"
    status: MATCH
    reason: "This matches \"Add lines 5e and 6.\""
  - key: "8e"
    status: MATCH
    reason: "This matches \"Add lines 8a through 8c\"; line 8d is reserved."
  - key: "9"
    status: MATCH
    reason: "Line 9 is investment interest, with Form 4952 attached if required. Form 4952 line 8 is the investment interest deduction."
  - key: "10"
    status: MATCH
    reason: "This matches \"Add lines 8e and 9.\""
  - key: "12"
    status: MATCH
    reason: "Line 12 is gifts other than by cash or check. The program sums noncash deductions before income limits, with appraisal and special-property cases refused."
  - key: "14"
    status: MATCH
    reason: "This matches \"Add lines 11 through 13.\""
  - key: "17"
    status: MATCH
    reason: "This matches \"Add the amounts in the far right column for lines 4 through 16\": lines 4, 7, 10, 14, 15 and 16."
```
