# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1029f15f22721147e31bd0c17653daad2e15602b716ba08b63c9a68e2372e012 |
| subject sha256 | bebc7c02c8aa1f42d39df14282d7609d61b67f805714977d544e2a0038bc1833 |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 1 / 0 / 0 |
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

Model: The form says 'Medical and dental expenses' with 'Do not include expenses reimbursed or paid by others'. The input asks for unreimbursed eligible expenses, which is the same amount.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a allows 'either income taxes or general sales taxes'. The program takes income taxes only and refuses the sales-tax election through sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: This is the 'State and local real estate taxes' amount, entered as the deductible amount.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: This is the 'State and local personal property taxes' amount.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: This is the 'Home mortgage interest and points reported to you on Form 1098'. Cases where the interest is limited, or where loan proceeds were not all used to buy, build or improve the home, are refused through sa.unsupported.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: This is 'Gifts by cash or check' before income limits. Income-limited and carryover cases are refused through sa.charity_limited.

### 2 — Amount from sa.agi_floor
Status: **MISMATCH**

Restated: Enter the amount from helper "Form 1040 line 11b adjusted gross income, but not less than zero".

Model: The form says 'Enter amount from Form 1040 or 1040-SR, line 11b' and gives no floor. The program enters zero when AGI is negative, so the printed line 2 differs whenever line 11b is below zero.

Ruling: genuine ambiguity; project retained (amb.2025.sa_medical_negative_agi). The printed line 2 says "Enter amount from Form 1040 or 1040-SR, line 11b" and the form gives no floor, as the model says (f1040sa p. 1). With line 11b below zero the printed arithmetic makes line 3 ("Multiply line 2 by 7.5% (0.075)") negative and line 4 ("Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-") larger than line 1: a deduction of medical expenses that were not paid. The instruction allows "only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income on Form 1040 or 1040-SR, line 11b" (i1040sca p. 1, Medical and Dental Expenses), and no part of the expenses exceeds the expenses themselves; the project therefore enters line 11b on line 2 at no less than zero, which leaves lines 3 and 4 as printed. Tax-Calculator and PolicyEngine-US floor adjusted gross income at zero before the percentage (BUG-0094). The helper that floors it is named on line 2 and the glossary states the floor; the difference from the printed line is confined to a negative line 11b.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: 'Multiply line 2 by 7.5% (0.075)': 75/1000 is the same rate.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.'

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: 'Add lines 5a through 5c.'

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper reproduces the SALT worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 if married filing separately), but not below $10,000, halved for married filing separately, then the smaller of that or line 5d. When AGI is under the threshold this gives the form's '$40,000 ($20,000 if married filing separately)'. The Form 2555/4563/Puerto Rico addbacks are refused through sa.excluded_income.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: The instructions say to include 'income taxes you paid to a foreign country and generation-skipping tax'. Both are refused through sa.unsupported, so zero is correct within the supported cases.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: 'Home mortgage interest not reported to you on Form 1098' is refused through sa.unsupported, so zero is correct within the supported cases.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: 'Points not reported to you on Form 1098' are refused through sa.unsupported, so zero is correct within the supported cases.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: 'Carryover from prior year' is refused through sa.charity_limited, so zero is correct within the supported cases.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Casualty and theft losses from Form 4684 are refused through sa.unsupported, so zero is correct within the supported cases.

### 16 — Other—from list in instructions. List type and amount:
Status: **MATCH**

Model: The instructions allow 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'; the program takes the smaller of losses or line 8b, and zero when there are no winnings. The other items on the line 16 list, including a net qualified disaster loss, are refused.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: 'Add lines 5e and 6.'

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: 'Add lines 8a through 8c.' Line 8d is reserved.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: The form line is 'Investment interest. Attach Form 4952 if required', and Form 4952 line 8 is the 'Investment interest deduction', so using that amount matches.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: 'Add lines 8e and 9.'

### 12 — Total supported noncash donations before income limits
Status: **MATCH**

Model: Line 12 is 'Other than by cash or check'. The gift roster is the per-item or per-group Form 8283-style record, and appraisal or special-property cases are refused. This assumes the roster holds noncash gifts only and does not repeat line 11 cash gifts.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: 'Add lines 11 through 13.'

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: 'Add the amounts in the far right column for lines 4 through 16.' Those amounts are lines 4, 7, 10, 14, 15 and 16.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form says 'Medical and dental expenses' with 'Do not include expenses reimbursed or paid by others'. The input asks for unreimbursed eligible expenses, which is the same amount."
  - key: "5a"
    status: MATCH
    reason: "Line 5a allows 'either income taxes or general sales taxes'. The program takes income taxes only and refuses the sales-tax election through sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "This is the 'State and local real estate taxes' amount, entered as the deductible amount."
  - key: "5c"
    status: MATCH
    reason: "This is the 'State and local personal property taxes' amount."
  - key: "8a"
    status: MATCH
    reason: "This is the 'Home mortgage interest and points reported to you on Form 1098'. Cases where the interest is limited, or where loan proceeds were not all used to buy, build or improve the home, are refused through sa.unsupported."
  - key: "11"
    status: MATCH
    reason: "This is 'Gifts by cash or check' before income limits. Income-limited and carryover cases are refused through sa.charity_limited."
  - key: "2"
    status: MISMATCH
    reason: "The form says 'Enter amount from Form 1040 or 1040-SR, line 11b' and gives no floor. The program enters zero when AGI is negative, so the printed line 2 differs whenever line 11b is below zero."
  - key: "3"
    status: MATCH
    reason: "'Multiply line 2 by 7.5% (0.075)': 75/1000 is the same rate."
  - key: "4"
    status: MATCH
    reason: "'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-.'"
  - key: "5d"
    status: MATCH
    reason: "'Add lines 5a through 5c.'"
  - key: "5e"
    status: MATCH
    reason: "The helper reproduces the SALT worksheet: $40,000 less 30% of AGI over $500,000 ($250,000 if married filing separately), but not below $10,000, halved for married filing separately, then the smaller of that or line 5d. When AGI is under the threshold this gives the form's '$40,000 ($20,000 if married filing separately)'. The Form 2555/4563/Puerto Rico addbacks are refused through sa.excluded_income."
  - key: "6"
    status: MATCH
    reason: "The instructions say to include 'income taxes you paid to a foreign country and generation-skipping tax'. Both are refused through sa.unsupported, so zero is correct within the supported cases."
  - key: "8b"
    status: MATCH
    reason: "'Home mortgage interest not reported to you on Form 1098' is refused through sa.unsupported, so zero is correct within the supported cases."
  - key: "8c"
    status: MATCH
    reason: "'Points not reported to you on Form 1098' are refused through sa.unsupported, so zero is correct within the supported cases."
  - key: "13"
    status: MATCH
    reason: "'Carryover from prior year' is refused through sa.charity_limited, so zero is correct within the supported cases."
  - key: "15"
    status: MATCH
    reason: "Casualty and theft losses from Form 4684 are refused through sa.unsupported, so zero is correct within the supported cases."
  - key: "16"
    status: MATCH
    reason: "The instructions allow 'Gambling losses ... but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b'; the program takes the smaller of losses or line 8b, and zero when there are no winnings. The other items on the line 16 list, including a net qualified disaster loss, are refused."
  - key: "7"
    status: MATCH
    reason: "'Add lines 5e and 6.'"
  - key: "8e"
    status: MATCH
    reason: "'Add lines 8a through 8c.' Line 8d is reserved."
  - key: "9"
    status: MATCH
    reason: "The form line is 'Investment interest. Attach Form 4952 if required', and Form 4952 line 8 is the 'Investment interest deduction', so using that amount matches."
  - key: "10"
    status: MATCH
    reason: "'Add lines 8e and 9.'"
  - key: "12"
    status: MATCH
    reason: "Line 12 is 'Other than by cash or check'. The gift roster is the per-item or per-group Form 8283-style record, and appraisal or special-property cases are refused. This assumes the roster holds noncash gifts only and does not repeat line 11 cash gifts."
  - key: "14"
    status: MATCH
    reason: "'Add lines 11 through 13.'"
  - key: "17"
    status: MATCH
    reason: "'Add the amounts in the far right column for lines 4 through 16.' Those amounts are lines 4, 7, 10, 14, 15 and 16."
```
```
