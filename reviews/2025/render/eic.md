# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d8931883c119aa41efe00e17693f55ca6cc3f20ce1d78296e11af3aba9c91031 |
| lines judged | 13 |
| match / mismatch / unclear / missing | 12 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: Step 5 worksheet line 1 is "Enter the amount from Form 1040 or 1040-SR, line 1z". The clergy and church-employee adjustments are excluded by the refusal on Schedule 1 items, which names clergy and church employee income.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 asks for the Medicaid waiver payments excluded on Schedule 1, line 8s, or -0- if the filer includes them in earned income. The refusals on Medicaid waiver payments and the Schedule 1 line 8s exclusion leave $0 as the only supported value.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: The IRS line reads "Subtract line 2 from line 1".

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 is elective nontaxable combat pay. The refusal excludes any combat pay, so $0 is correct within the supported cases.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: The IRS line reads "Add lines 3 and 4. This is your earned income".

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: Worksheet B line 4b reads "Combine lines 1e, 2c, 3, and 4a", where line 4a is the Step 5 earned income. Line 3 (statutory employee income) is excluded by the Schedule 1 refusal naming statutory-employee wages, so 1e+2c plus Step 5 line 5 matches.

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b 
Status: **MATCH**

Model: Worksheet B line 6 is "Enter your total earned income from Part 4, line 4b". Where line 4b is zero or less the IRS says "STOP You can't take the credit"; entering -0- produces a $0 credit through the table step, so the result is the same.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: Worksheet A line 1 is "Enter your earned income from Step 5". Self-employed filers are routed to the Worksheet B total earned income, which the program uses as the same pipeline. Self-employment other than Schedule C (farm, partnerships) is excluded by the Schedule 1 refusal.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Line 2 looks up line 1 in the EIC Table by filing status and number of qualifying children with valid SSNs. The table begins at $1, so amounts below that yield no credit, which is consistent with "If line 2 is zero... You can't take the credit".

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: The IRS line reads "Enter the amount from Form 1040 or 1040-SR, line 11b".

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: The IRS line asks "Are the amounts on lines 3 and 1 the same?".

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MISMATCH**

Restated: Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 3, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 3, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 3, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 3, three or more qualifying children with valid SSNs"]

Model: The restatement always enters the EIC Table credit for line 3, but the IRS says to fill line 5 only in the No case: "Yes. Skip line 5" (line 4) and "Yes. Leave line 5 blank" (when line 3 is under $10,620/$17,730 or $23,350/$30,470). The printed line 5 should be blank in those cases rather than show a table amount.

Ruling: representation; project retained. As the transcription ruling on line 5: the project figures line 5 always and line 6 reads it only in the case the worksheet uses it (line 4 No and line 3 at or above the line 5 amount), so line 6 and the credit are the same; the model says so too.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: Line 6 is line 2 when line 4 is Yes. When line 4 is No it is line 2 if line 5 is left blank, and otherwise "the smaller amount" of lines 5 and 2. The thresholds $10,620 ($17,730 MFJ) and $23,350 ($30,470 MFJ) match the IRS text.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 worksheet line 1 is \"Enter the amount from Form 1040 or 1040-SR, line 1z\". The clergy and church-employee adjustments are excluded by the refusal on Schedule 1 items, which names clergy and church employee income."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 asks for the Medicaid waiver payments excluded on Schedule 1, line 8s, or -0- if the filer includes them in earned income. The refusals on Medicaid waiver payments and the Schedule 1 line 8s exclusion leave $0 as the only supported value."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "The IRS line reads \"Subtract line 2 from line 1\"."
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 is elective nontaxable combat pay. The refusal excludes any combat pay, so $0 is correct within the supported cases."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "The IRS line reads \"Add lines 3 and 4. This is your earned income\"."
  - key: "4b"
    status: MATCH
    reason: "Worksheet B line 4b reads \"Combine lines 1e, 2c, 3, and 4a\", where line 4a is the Step 5 earned income. Line 3 (statutory employee income) is excluded by the Schedule 1 refusal naming statutory-employee wages, so 1e+2c plus Step 5 line 5 matches."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "Worksheet B line 6 is \"Enter your total earned income from Part 4, line 4b\". Where line 4b is zero or less the IRS says \"STOP You can't take the credit\"; entering -0- produces a $0 credit through the table step, so the result is the same."
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 is \"Enter your earned income from Step 5\". Self-employed filers are routed to the Worksheet B total earned income, which the program uses as the same pipeline. Self-employment other than Schedule C (farm, partnerships) is excluded by the Schedule 1 refusal."
  - key: "2"
    status: MATCH
    reason: "Line 2 looks up line 1 in the EIC Table by filing status and number of qualifying children with valid SSNs. The table begins at $1, so amounts below that yield no credit, which is consistent with \"If line 2 is zero... You can't take the credit\"."
  - key: "3"
    status: MATCH
    reason: "The IRS line reads \"Enter the amount from Form 1040 or 1040-SR, line 11b\"."
  - key: "4"
    status: MATCH
    reason: "The IRS line asks \"Are the amounts on lines 3 and 1 the same?\"."
  - key: "5"
    status: MISMATCH
    reason: "The restatement always enters the EIC Table credit for line 3, but the IRS says to fill line 5 only in the No case: \"Yes. Skip line 5\" (line 4) and \"Yes. Leave line 5 blank\" (when line 3 is under $10,620/$17,730 or $23,350/$30,470). The printed line 5 should be blank in those cases rather than show a table amount."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "Line 6 is line 2 when line 4 is Yes. When line 4 is No it is line 2 if line 5 is left blank, and otherwise \"the smaller amount\" of lines 5 and 2. The thresholds $10,620 ($17,730 MFJ) and $23,350 ($30,470 MFJ) match the IRS text."
```
```
