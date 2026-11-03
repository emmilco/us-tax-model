# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a30ff8ec442e3f90231245c434d6e9bf5a496aeb4e308b66920b25522dece917 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d42c175ca1e109cb98b2250ef0f1ffd8a68f38a4d93defa0eb5738e63cb2092b |
| lines judged | 24 |
| match / mismatch / unclear / missing | 22 / 1 / 0 / 1 |
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

Model: Matches the line 1 instructions. Expenses are reduced by insurance and other reimbursements. Pretax-reduction premiums, retired public safety officer premiums paid by tax-free distributions, the housework share of nursing pay and non-hospital meals are left out. Lodging is capped at $50 a night, premiums are reduced by the Schedule 1 line 17 deduction, and the long-term care limits ($480/$900/$1,800/$4,810/$6,020) match the chart. The HSA/Archer MSA exclusions (Pub. 969) and the deceased-taxpayer rule also match.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: The text tells you to include state and local income taxes, including withholding, when no sales-tax election is made, and to include U.S. territory taxes except those allocable to excluded income. The sales-tax election is refused through sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Matches the line 5b instructions: 'Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025', with assessment determined by state or local law. Territory taxes are included except those allocable to excluded income.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: The restatement asks for deductible state and local personal property taxes, including territory taxes not allocable to excluded income, as the line 5c and territory instructions direct.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Asks for mortgage interest and points reported on Form 1098. The cases subject to the debt or use limits are refused through sa.unsupported.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Asks for gifts by cash or check after any benefit received and with the required substantiation, as line 11 and its caution direct. Income-limited amounts are refused through sa.charity_limited.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: The program floors adjusted gross income at zero, but the IRS line says only 'Enter amount from Form 1040 or 1040-SR, line 11b' and gives no floor. A negative AGI would therefore produce a different line 2.

Ruling: ambiguity (amb.2025.sa_medical_negative_agi); the project floors AGI at zero for the 7.5% limit, the recorded reading.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: 75/1000 is the 'Multiply line 2 by 7.5% (0.075)' on the form.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Same as the form: 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.'

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Same as the form: 'Add lines 5a through 5c'.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The ceiling is the State and Local Tax Deduction Worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 if married filing separately), not below $10,000, halved if married filing separately, then the smaller of that or line 5d. This gives $40,000/$20,000 when AGI is at or below the threshold. Excluded-income cases are refused.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Line 6 holds foreign income taxes and GST. Both are refused through sa.unsupported, so zero is correct in the supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Mortgage interest not reported on Form 1098 is refused through sa.unsupported, so zero is correct in the supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Points not reported on Form 1098 are refused through sa.unsupported, so zero is correct in the supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Charitable carryovers from a prior year are refused through sa.charity_limited, so zero is correct in the supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Casualty and theft losses from Form 4684 are refused through sa.unsupported, so zero is correct in the supported cases.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: The text allows 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'. The program uses the smaller of losses or line 8b, and zero when there are no winnings. Other line 16 items and net qualified disaster losses are refused.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Same as the form: 'Add lines 5e and 6'.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Same as the form: 'Add lines 8a through 8c' (8d is reserved).

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Line 9 is investment interest with 'Attach Form 4952 if required'. Form 4952 line 8 is the 'Investment interest deduction', which is the amount line 9 calls for.

### 10 — Add sa.line8e, sa.line9
Status: **MISSING**

Restated: Add line 8e and line 9.

Model: the model returned no verdict for this line

Ruling: model error; the model returned no verdict for this line, so there is no objection to rule on. The DeepSeek render log judges it.

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Line 12 is gifts 'Other than by cash or check'. The program sums each noncash gift group's deduction before income limits, without clothing not in good used condition or $250+ gifts lacking acknowledgment. Section B and special-property cases are refused.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Same as the form: 'Add lines 11 through 13'.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Lines 4, 7, 10, 14, 15 and 16 are the far-right-column amounts the form says to add: 'Add the amounts in the far right column for lines 4 through 16'.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Matches the line 1 instructions. Expenses are reduced by insurance and other reimbursements. Pretax-reduction premiums, retired public safety officer premiums paid by tax-free distributions, the housework share of nursing pay and non-hospital meals are left out. Lodging is capped at $50 a night, premiums are reduced by the Schedule 1 line 17 deduction, and the long-term care limits ($480/$900/$1,800/$4,810/$6,020) match the chart. The HSA/Archer MSA exclusions (Pub. 969) and the deceased-taxpayer rule also match."
  - key: "5a"
    status: MATCH
    reason: "The text tells you to include state and local income taxes, including withholding, when no sales-tax election is made, and to include U.S. territory taxes except those allocable to excluded income. The sales-tax election is refused through sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "Matches the line 5b instructions: 'Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025', with assessment determined by state or local law. Territory taxes are included except those allocable to excluded income."
  - key: "5c"
    status: MATCH
    reason: "The restatement asks for deductible state and local personal property taxes, including territory taxes not allocable to excluded income, as the line 5c and territory instructions direct."
  - key: "8a"
    status: MATCH
    reason: "Asks for mortgage interest and points reported on Form 1098. The cases subject to the debt or use limits are refused through sa.unsupported."
  - key: "11"
    status: MATCH
    reason: "Asks for gifts by cash or check after any benefit received and with the required substantiation, as line 11 and its caution direct. Income-limited amounts are refused through sa.charity_limited."
  - key: "2"
    status: MISMATCH
    reason: "The program floors adjusted gross income at zero, but the IRS line says only 'Enter amount from Form 1040 or 1040-SR, line 11b' and gives no floor. A negative AGI would therefore produce a different line 2."
  - key: "3"
    status: MATCH
    reason: "75/1000 is the 'Multiply line 2 by 7.5% (0.075)' on the form."
  - key: "4"
    status: MATCH
    reason: "Same as the form: 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.'"
  - key: "5d"
    status: MATCH
    reason: "Same as the form: 'Add lines 5a through 5c'."
  - key: "5e"
    status: MATCH
    reason: "The ceiling is the State and Local Tax Deduction Worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 if married filing separately), not below $10,000, halved if married filing separately, then the smaller of that or line 5d. This gives $40,000/$20,000 when AGI is at or below the threshold. Excluded-income cases are refused."
  - key: "6"
    status: MATCH
    reason: "Line 6 holds foreign income taxes and GST. Both are refused through sa.unsupported, so zero is correct in the supported cases."
  - key: "8b"
    status: MATCH
    reason: "Mortgage interest not reported on Form 1098 is refused through sa.unsupported, so zero is correct in the supported cases."
  - key: "8c"
    status: MATCH
    reason: "Points not reported on Form 1098 are refused through sa.unsupported, so zero is correct in the supported cases."
  - key: "13"
    status: MATCH
    reason: "Charitable carryovers from a prior year are refused through sa.charity_limited, so zero is correct in the supported cases."
  - key: "15"
    status: MATCH
    reason: "Casualty and theft losses from Form 4684 are refused through sa.unsupported, so zero is correct in the supported cases."
  - key: "16"
    status: MATCH
    reason: "The text allows 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'. The program uses the smaller of losses or line 8b, and zero when there are no winnings. Other line 16 items and net qualified disaster losses are refused."
  - key: "7"
    status: MATCH
    reason: "Same as the form: 'Add lines 5e and 6'."
  - key: "8e"
    status: MATCH
    reason: "Same as the form: 'Add lines 8a through 8c' (8d is reserved)."
  - key: "9"
    status: MATCH
    reason: "Line 9 is investment interest with 'Attach Form 4952 if required'. Form 4952 line 8 is the 'Investment interest deduction', which is the amount line 9 calls for."
  - key: "12"
    status: MATCH
    reason: "Line 12 is gifts 'Other than by cash or check'. The program sums each noncash gift group's deduction before income limits, without clothing not in good used condition or $250+ gifts lacking acknowledgment. Section B and special-property cases are refused."
  - key: "14"
    status: MATCH
    reason: "Same as the form: 'Add lines 11 through 13'."
  - key: "17"
    status: MATCH
    reason: "Lines 4, 7, 10, 14, 15 and 16 are the far-right-column amounts the form says to add: 'Add the amounts in the far right column for lines 4 through 16'."
```
```
