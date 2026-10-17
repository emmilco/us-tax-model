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
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 34 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: The form asks for medical and dental expenses and cautions 'Do not include expenses reimbursed or paid by others'. The input says unreimbursed eligible expenses, which matches.

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a allows income taxes or general sales taxes. The restatement takes income taxes only, and the sales-tax election is refused through sa.unsupported, which is an allowed narrowing.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Matches 'State and local real estate taxes (see instructions)'. The instruction text given limits deductible amounts to taxes paid in 2025 and assessed before 2026, consistent with 'deductible'.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Matches 'State and local personal property taxes'.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Matches 'Home mortgage interest and points reported to you on Form 1098'. Interest subject to debt or use limits is refused through sa.unsupported.

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Matches 'Gifts by cash or check'. The form's caution about benefits received and $250 substantiation is reflected, and income-limited cases are refused through sa.charity_limited.

### 2 — Amount from sa.agi
Status: **MATCH**

Model: Matches 'Enter amount from Form 1040 or 1040-SR, line 11b'.

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Matches 'Multiply line 2 by 7.5% (0.075)'.

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Matches 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-'.

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Matches 'Add lines 5a through 5c'.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: The helper gives max($40,000 − 30% of AGI above $500,000 ($250,000 MFS), $10,000), halved if MFS, then takes the smaller of that or 5d. This agrees with worksheet lines 1 and 5–10 and with the form's $40,000/$20,000 cap when AGI is at or below the threshold. Excluded-income addbacks (worksheet line 3) are refused.

### 6 — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. The instructions say line 6 includes foreign income taxes and generation-skipping tax, and both are refused through sa.unsupported.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. 'Home mortgage interest not reported to you on Form 1098' is refused through sa.unsupported.

### 8c — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. 'Points not reported to you on Form 1098' is refused through sa.unsupported.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. 'Carryover from prior year' is refused through sa.charity_limited.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. Casualty and theft losses ('Attach Form 4684') are refused through sa.unsupported.

### 16 — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. 'Other—from list in instructions' is refused through sa.unsupported's 'other itemized deduction'.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Matches 'Add lines 5e and 6'.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Matches 'Add lines 8a through 8c'; line 8d is 'Reserved for future use'.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: The form line is 'Investment interest. Attach Form 4952 if required', and Form 4952 line 8 is the 'Investment interest deduction'. The Schedule A line 9 instructions are not included, but nothing in the text given contradicts this.

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Matches 'Add lines 8e and 9'.

### 12 — Total supported noncash donations before income limits
Status: **UNCLEAR**

Restated: Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The form line is 'Other than by cash or check', but gift.allowed and the gift roster are not defined in the glossary. I cannot confirm the sum is limited to non-cash gifts, so cash gifts already counted on line 11 might be counted again.

Ruling: representation; project retained. The gift collection holds noncash gifts only (forms/2025/gift.yaml, cited to i8283), and `gift.allowed` is each entry's deductible amount after its Form 8283 screens; cash and check gifts are the line 11 input. No change to the data.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Matches 'Add lines 11 through 13'.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Lines 4, 7, 10, 14, 15 and 16 are the far-right-column entries in 'Add the amounts in the far right column for lines 4 through 16'.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The form asks for medical and dental expenses and cautions 'Do not include expenses reimbursed or paid by others'. The input says unreimbursed eligible expenses, which matches."
  - key: "5a"
    status: MATCH
    reason: "Line 5a allows income taxes or general sales taxes. The restatement takes income taxes only, and the sales-tax election is refused through sa.unsupported, which is an allowed narrowing."
  - key: "5b"
    status: MATCH
    reason: "Matches 'State and local real estate taxes (see instructions)'. The instruction text given limits deductible amounts to taxes paid in 2025 and assessed before 2026, consistent with 'deductible'."
  - key: "5c"
    status: MATCH
    reason: "Matches 'State and local personal property taxes'."
  - key: "8a"
    status: MATCH
    reason: "Matches 'Home mortgage interest and points reported to you on Form 1098'. Interest subject to debt or use limits is refused through sa.unsupported."
  - key: "11"
    status: MATCH
    reason: "Matches 'Gifts by cash or check'. The form's caution about benefits received and $250 substantiation is reflected, and income-limited cases are refused through sa.charity_limited."
  - key: "2"
    status: MATCH
    reason: "Matches 'Enter amount from Form 1040 or 1040-SR, line 11b'."
  - key: "3"
    status: MATCH
    reason: "Matches 'Multiply line 2 by 7.5% (0.075)'."
  - key: "4"
    status: MATCH
    reason: "Matches 'Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-'."
  - key: "5d"
    status: MATCH
    reason: "Matches 'Add lines 5a through 5c'."
  - key: "5e"
    status: MATCH
    reason: "The helper gives max($40,000 − 30% of AGI above $500,000 ($250,000 MFS), $10,000), halved if MFS, then takes the smaller of that or 5d. This agrees with worksheet lines 1 and 5–10 and with the form's $40,000/$20,000 cap when AGI is at or below the threshold. Excluded-income addbacks (worksheet line 3) are refused."
  - key: "6"
    status: MATCH
    reason: "Set to $0. The instructions say line 6 includes foreign income taxes and generation-skipping tax, and both are refused through sa.unsupported."
  - key: "8b"
    status: MATCH
    reason: "Set to $0. 'Home mortgage interest not reported to you on Form 1098' is refused through sa.unsupported."
  - key: "8c"
    status: MATCH
    reason: "Set to $0. 'Points not reported to you on Form 1098' is refused through sa.unsupported."
  - key: "13"
    status: MATCH
    reason: "Set to $0. 'Carryover from prior year' is refused through sa.charity_limited."
  - key: "15"
    status: MATCH
    reason: "Set to $0. Casualty and theft losses ('Attach Form 4684') are refused through sa.unsupported."
  - key: "16"
    status: MATCH
    reason: "Set to $0. 'Other—from list in instructions' is refused through sa.unsupported's 'other itemized deduction'."
  - key: "7"
    status: MATCH
    reason: "Matches 'Add lines 5e and 6'."
  - key: "8e"
    status: MATCH
    reason: "Matches 'Add lines 8a through 8c'; line 8d is 'Reserved for future use'."
  - key: "9"
    status: MATCH
    reason: "The form line is 'Investment interest. Attach Form 4952 if required', and Form 4952 line 8 is the 'Investment interest deduction'. The Schedule A line 9 instructions are not included, but nothing in the text given contradicts this."
  - key: "10"
    status: MATCH
    reason: "Matches 'Add lines 8e and 9'."
  - key: "12"
    status: UNCLEAR
    reason: "The form line is 'Other than by cash or check', but gift.allowed and the gift roster are not defined in the glossary. I cannot confirm the sum is limited to non-cash gifts, so cash gifts already counted on line 11 might be counted again."
  - key: "14"
    status: MATCH
    reason: "Matches 'Add lines 11 through 13'."
  - key: "17"
    status: MATCH
    reason: "Lines 4, 7, 10, 14, 15 and 16 are the far-right-column entries in 'Add the amounts in the far right column for lines 4 through 16'."
```
```
