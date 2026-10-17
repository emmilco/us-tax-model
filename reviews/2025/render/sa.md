# Render comparison — sa

The rendered English of every printed line of `Schedule A — supported itemized deductions and standard comparison` (`rendered/2025/sa.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5061f7160b298b6730ec4295d728f2468c744d50cf55b377066f415c83014dc2 |
| lines judged | 24 |
| match / mismatch / unclear / missing | 21 / 2 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b |
| i1040gi | 2025; printed date 2026-02-25 | 34, 35 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### 1 — Unreimbursed eligible medical and dental expenses
Status: **MATCH**

Model: Input of medical and dental expenses not reimbursed or paid by others, consistent with the form's caution 'Do not include expenses reimbursed or paid by others.'

### 5a — State/local income taxes paid, including withholding; no sales-tax election
Status: **MATCH**

Model: Line 5a takes income taxes or general sales taxes. The program supports income taxes only, and the sa.unsupported gate refuses the sales-tax election.

### 5b — Deductible state/local real estate taxes
Status: **MATCH**

Model: Input of state and local real estate taxes, as on the form.

### 5c — Deductible state/local personal property taxes
Status: **MATCH**

Model: Input of state and local personal property taxes, as on the form.

### 8a — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use lim
Status: **MATCH**

Model: Input of mortgage interest and points reported on Form 1098. The sa.unsupported gate refuses the cases limited by debt or use rules ('See instructions if limited').

### 11 — Deductible cash/check charitable gifts before income limits, after benefits received and r
Status: **MATCH**

Model: Input of gifts by cash or check after substantiation for gifts of $250 or more. Income limits are refused through sa.charity_limited.

### 2 — Amount from sa.agi
Status: **MATCH**

Model: Takes Form 1040 line 11b, matching 'Enter amount from Form 1040 or 1040-SR, line 11b.'

### 3 — Multiply sa.line2 by sa.medical_rate
Status: **MATCH**

Model: Multiplies line 2 by 0.075, matching 'Multiply line 2 by 7.5% (0.075).'

### 4 — Subtract sa.line3 from sa.line1; if zero or less, enter zero
Status: **MATCH**

Model: Line 1 minus line 3, floored at zero, matching 'If line 3 is more than line 1, enter -0-.'

### 5d — Add sa.line5a, sa.line5b, sa.line5c
Status: **MATCH**

Model: Adds 5a through 5c, as the form says.

### 5e — Smaller of sa.line5d, sa.saltlimit
Status: **MATCH**

Model: Uses the smaller of 5d and the larger of ($40,000 minus 30% of AGI over $500,000/$250,000 MFS) or $10,000, halved if MFS. This reproduces SALT Worksheet lines 1 and 5–10. Excluded-income add-backs (worksheet line 3) are refused through sa.excluded_income.

### 6 — Amount from sa.zero
Status: **MISMATCH**

Restated: Enter the amount from helper "Year parameter sales.zero".

Model: The instructions say 'Include on this line income taxes you paid to a foreign country and generation-skipping tax (GST) imposed on certain income distributions.' The refusal gate covers only the foreign tax deduction, so a filer with GST would get $0 without a refusal.

Ruling: second reading right; data changed under BUG-0005. The instructions include on line 6 "income taxes you paid to a foreign country and generation-skipping tax (GST) imposed on certain income distributions" (i1040sca p. 7); the screen `sa.unsupported` named only the foreign tax deduction. The screen now names the generation-skipping tax deduction; the line stays zero behind it.

### 8b — Amount from sa.zero
Status: **MATCH**

Model: Set to $0. The sa.unsupported gate refuses 'mortgage interest not on Form 1098', which is exactly line 8b's subject.

### 8c — Amount from sa.zero
Status: **MISMATCH**

Restated: Enter the amount from helper "Year parameter sales.zero".

Model: Line 8c is 'Points not reported to you on Form 1098.' The gate names only 'mortgage interest not on Form 1098', not points, so unreported points would be entered as $0 without a refusal.

Ruling: second reading right; data changed under BUG-0006. Line 8c is "Points not reported to you on Form 1098"; the screen `sa.unsupported` named mortgage interest not on Form 1098 and not points. The screen now names mortgage interest or points not on Form 1098; the line stays zero behind it.

### 13 — Amount from sa.zero
Status: **MATCH**

Model: Line 13 'Carryover from prior year' is set to $0. Carryovers are refused through sa.charity_limited.

### 15 — Amount from sa.zero
Status: **MATCH**

Model: Casualty and theft losses (Form 4684 line 18) are set to $0. Any casualty or theft loss is refused through sa.unsupported.

### 16 — Amount from sa.zero
Status: **MATCH**

Model: Line 16 'Other—from list in instructions' is set to $0. Other itemized deductions are refused through sa.unsupported.

### 7 — Add sa.line5e, sa.line6
Status: **MATCH**

Model: Adds lines 5e and 6, as the form says.

### 8e — Add sa.line8a, sa.line8b, sa.line8c
Status: **MATCH**

Model: Adds 8a through 8c, as the form says ('Add lines 8a through 8c'). Line 8d is reserved.

### 9 — Amount from f4952.line8
Status: **MATCH**

Model: Investment interest is taken from Form 4952 line 8, the investment interest deduction, consistent with 'Investment interest. Attach Form 4952 if required.'

### 10 — Add sa.line8e, sa.line9
Status: **MATCH**

Model: Adds lines 8e and 9, as the form says.

### 12 — Total supported noncash donations before income limits
Status: **UNCLEAR**

Restated: Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 12 is 'Other than by cash or check' (noncash gifts, Form 8283 if over $500). The restatement sums an undefined 'gift.allowed' over gift entries and does not say the entries are restricted to noncash gifts or how the allowed amount is figured.

Ruling: representation; project retained. The gift collection holds noncash gifts only (forms/2025/gift.yaml, cited to i8283), and `gift.allowed` is each entry's deductible amount after its Form 8283 screens; cash and check gifts are the line 11 input. No change to the data.

### 14 — Add sa.line11, sa.line12, sa.line13
Status: **MATCH**

Model: Adds lines 11 through 13, as the form says.

### 17 — Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
Status: **MATCH**

Model: Adds the far-right-column lines 4, 7, 10, 14, 15 and 16, matching 'Add the amounts in the far right column for lines 4 through 16.'

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Input of medical and dental expenses not reimbursed or paid by others, consistent with the form's caution 'Do not include expenses reimbursed or paid by others.'"
  - key: "5a"
    status: MATCH
    reason: "Line 5a takes income taxes or general sales taxes. The program supports income taxes only, and the sa.unsupported gate refuses the sales-tax election."
  - key: "5b"
    status: MATCH
    reason: "Input of state and local real estate taxes, as on the form."
  - key: "5c"
    status: MATCH
    reason: "Input of state and local personal property taxes, as on the form."
  - key: "8a"
    status: MATCH
    reason: "Input of mortgage interest and points reported on Form 1098. The sa.unsupported gate refuses the cases limited by debt or use rules ('See instructions if limited')."
  - key: "11"
    status: MATCH
    reason: "Input of gifts by cash or check after substantiation for gifts of $250 or more. Income limits are refused through sa.charity_limited."
  - key: "2"
    status: MATCH
    reason: "Takes Form 1040 line 11b, matching 'Enter amount from Form 1040 or 1040-SR, line 11b.'"
  - key: "3"
    status: MATCH
    reason: "Multiplies line 2 by 0.075, matching 'Multiply line 2 by 7.5% (0.075).'"
  - key: "4"
    status: MATCH
    reason: "Line 1 minus line 3, floored at zero, matching 'If line 3 is more than line 1, enter -0-.'"
  - key: "5d"
    status: MATCH
    reason: "Adds 5a through 5c, as the form says."
  - key: "5e"
    status: MATCH
    reason: "Uses the smaller of 5d and the larger of ($40,000 minus 30% of AGI over $500,000/$250,000 MFS) or $10,000, halved if MFS. This reproduces SALT Worksheet lines 1 and 5–10. Excluded-income add-backs (worksheet line 3) are refused through sa.excluded_income."
  - key: "6"
    status: MISMATCH
    reason: "The instructions say 'Include on this line income taxes you paid to a foreign country and generation-skipping tax (GST) imposed on certain income distributions.' The refusal gate covers only the foreign tax deduction, so a filer with GST would get $0 without a refusal."
  - key: "8b"
    status: MATCH
    reason: "Set to $0. The sa.unsupported gate refuses 'mortgage interest not on Form 1098', which is exactly line 8b's subject."
  - key: "8c"
    status: MISMATCH
    reason: "Line 8c is 'Points not reported to you on Form 1098.' The gate names only 'mortgage interest not on Form 1098', not points, so unreported points would be entered as $0 without a refusal."
  - key: "13"
    status: MATCH
    reason: "Line 13 'Carryover from prior year' is set to $0. Carryovers are refused through sa.charity_limited."
  - key: "15"
    status: MATCH
    reason: "Casualty and theft losses (Form 4684 line 18) are set to $0. Any casualty or theft loss is refused through sa.unsupported."
  - key: "16"
    status: MATCH
    reason: "Line 16 'Other—from list in instructions' is set to $0. Other itemized deductions are refused through sa.unsupported."
  - key: "7"
    status: MATCH
    reason: "Adds lines 5e and 6, as the form says."
  - key: "8e"
    status: MATCH
    reason: "Adds 8a through 8c, as the form says ('Add lines 8a through 8c'). Line 8d is reserved."
  - key: "9"
    status: MATCH
    reason: "Investment interest is taken from Form 4952 line 8, the investment interest deduction, consistent with 'Investment interest. Attach Form 4952 if required.'"
  - key: "10"
    status: MATCH
    reason: "Adds lines 8e and 9, as the form says."
  - key: "12"
    status: UNCLEAR
    reason: "Line 12 is 'Other than by cash or check' (noncash gifts, Form 8283 if over $500). The restatement sums an undefined 'gift.allowed' over gift entries and does not say the entries are restricted to noncash gifts or how the allowed amount is figured."
  - key: "14"
    status: MATCH
    reason: "Adds lines 11 through 13, as the form says."
  - key: "17"
    status: MATCH
    reason: "Adds the far-right-column lines 4, 7, 10, 14, 15 and 16, matching 'Add the amounts in the far right column for lines 4 through 16.'"
```
```
