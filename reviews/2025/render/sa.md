# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fa5a4123974cf4b93d0e3436c7a0d7aaec2407820b24fe52d34bcdebb5aaa09d |
| lines judged | 24 |
| match / mismatch / unclear / missing | 23 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | 7f4c8c493a59613863198e30bb448788826a174558e6089ec0810eefe3b25334 |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 34 | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: The form asks for medical and dental expenses, with the caution "Do not include expenses reimbursed or paid by others"; an input of unreimbursed eligible expenses matches.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a allows income taxes or general sales taxes, but not both. The program supports income taxes only and refuses the sales-tax election through sa.unsupported.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: This is an input of state and local real estate taxes, matching line 5b.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: This is an input of state and local personal property taxes, matching line 5c.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Line 8a is home mortgage interest and points reported on Form 1098. The case "See instructions if limited" is refused through sa.unsupported (debt/use limits).

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Line 11 is gifts by cash or check, with the caution about benefits received and the $250 substantiation instructions. The restatement reflects both.

### 2 — Amount from sa.agi
Status: **MATCH**

Model: The form says "Enter amount from Form 1040 or 1040-SR, line 11b", and the helper takes f1040 line 11b.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: The form says "Multiply line 2 by 7.5% (0.075)", which equals 75/1000.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: The form says "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-".

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: The form says "Add lines 5a through 5c".

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper computes the larger of $10,000 or $40,000 minus 30% of AGI over $500,000 ($250,000 if MFS), halves it for MFS, and takes the smaller of that or 5d. This matches worksheet lines 1 and 5-10 and the under-threshold rule of smaller of 5d or $40,000 ($20,000 MFS). Excluded-income cases (worksheet line 3) are refused.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Zero within scope. The instructions put foreign income taxes and GST on line 6, and those are refused through sa.unsupported (foreign tax or generation-skipping tax deduction).

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Zero within scope. Mortgage interest not reported on Form 1098 is refused through sa.unsupported.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Zero within scope. Points not reported on Form 1098 are refused through sa.unsupported.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Zero within scope. A "Carryover from prior year" is refused through sa.charity_limited.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Zero within scope. Casualty and theft losses (Form 4684) are refused through sa.unsupported.

### 16 — Amount from sa.zero
Status: **MATCH**

Model: Zero within scope. "Other—from list in instructions" deductions are refused through sa.unsupported (other itemized deduction).

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: The form says "Add lines 5e and 6".

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: The form says "Add lines 8a through 8c", and 8d is reserved.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Line 9 is investment interest, "Attach Form 4952 if required". Form 4952 line 8 is the investment interest deduction.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: The form says "Add lines 8e and 9".

### 12 — Total supported noncash donations before income limits
Status: **UNCLEAR**

Restated: Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The form says only "Other than by cash or check... see instructions. You must attach Form 8283 if over $500". The line 12 instructions are not in the pages given, and the per-entry value gift.allowed is not defined in the glossary, so its computation cannot be checked.

Ruling: representation; project retained. The gift collection holds noncash gifts only (forms/2025/gift.yaml, cited to i8283), and `gift.allowed` is each entry's deductible amount after its Form 8283 screens; cash and check gifts are the line 11 input. No change to the data.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: The form says "Add lines 11 through 13".

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: The form says "Add the amounts in the far right column for lines 4 through 16". The far-right entries are lines 4, 7, 10, 14, 15 and 16.

## Raw response

```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form asks for medical and dental expenses, with the caution \"Do not include expenses reimbursed or paid by others\"; an input of unreimbursed eligible expenses matches."
  - key: "5a"
    status: MATCH
    reason: "Line 5a allows income taxes or general sales taxes, but not both. The program supports income taxes only and refuses the sales-tax election through sa.unsupported."
  - key: "5b"
    status: MATCH
    reason: "This is an input of state and local real estate taxes, matching line 5b."
  - key: "5c"
    status: MATCH
    reason: "This is an input of state and local personal property taxes, matching line 5c."
  - key: "8a"
    status: MATCH
    reason: "Line 8a is home mortgage interest and points reported on Form 1098. The case \"See instructions if limited\" is refused through sa.unsupported (debt/use limits)."
  - key: "11"
    status: MATCH
    reason: "Line 11 is gifts by cash or check, with the caution about benefits received and the $250 substantiation instructions. The restatement reflects both."
  - key: "2"
    status: MATCH
    reason: "The form says \"Enter amount from Form 1040 or 1040-SR, line 11b\", and the helper takes f1040 line 11b."
  - key: "3"
    status: MATCH
    reason: "The form says \"Multiply line 2 by 7.5% (0.075)\", which equals 75/1000."
  - key: "4"
    status: MATCH
    reason: "The form says \"Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-\"."
  - key: "5d"
    status: MATCH
    reason: "The form says \"Add lines 5a through 5c\"."
  - key: "5e"
    status: MATCH
    reason: "The helper computes the larger of $10,000 or $40,000 minus 30% of AGI over $500,000 ($250,000 if MFS), halves it for MFS, and takes the smaller of that or 5d. This matches worksheet lines 1 and 5-10 and the under-threshold rule of smaller of 5d or $40,000 ($20,000 MFS). Excluded-income cases (worksheet line 3) are refused."
  - key: "6"
    status: MATCH
    reason: "Zero within scope. The instructions put foreign income taxes and GST on line 6, and those are refused through sa.unsupported (foreign tax or generation-skipping tax deduction)."
  - key: "8b"
    status: MATCH
    reason: "Zero within scope. Mortgage interest not reported on Form 1098 is refused through sa.unsupported."
  - key: "8c"
    status: MATCH
    reason: "Zero within scope. Points not reported on Form 1098 are refused through sa.unsupported."
  - key: "13"
    status: MATCH
    reason: "Zero within scope. A \"Carryover from prior year\" is refused through sa.charity_limited."
  - key: "15"
    status: MATCH
    reason: "Zero within scope. Casualty and theft losses (Form 4684) are refused through sa.unsupported."
  - key: "16"
    status: MATCH
    reason: "Zero within scope. \"Other—from list in instructions\" deductions are refused through sa.unsupported (other itemized deduction)."
  - key: "7"
    status: MATCH
    reason: "The form says \"Add lines 5e and 6\"."
  - key: "8e"
    status: MATCH
    reason: "The form says \"Add lines 8a through 8c\", and 8d is reserved."
  - key: "9"
    status: MATCH
    reason: "Line 9 is investment interest, \"Attach Form 4952 if required\". Form 4952 line 8 is the investment interest deduction."
  - key: "10"
    status: MATCH
    reason: "The form says \"Add lines 8e and 9\"."
  - key: "12"
    status: UNCLEAR
    reason: "The form says only \"Other than by cash or check... see instructions. You must attach Form 8283 if over $500\". The line 12 instructions are not in the pages given, and the per-entry value gift.allowed is not defined in the glossary, so its computation cannot be checked."
  - key: "14"
    status: MATCH
    reason: "The form says \"Add lines 11 through 13\"."
  - key: "17"
    status: MATCH
    reason: "The form says \"Add the amounts in the far right column for lines 4 through 16\". The far-right entries are lines 4, 7, 10, 14, 15 and 16."
```
