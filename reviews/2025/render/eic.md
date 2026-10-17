# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ba518542bcf34192fe6cd5d496849b04d4893c8a072ed5619e4d51f902ed0c4a |
| lines judged | 11 |
| match / mismatch / unclear / missing | 10 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: Step 5 worksheet line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z." The clergy and church-employee adjustments to line 1 are excluded by the Schedule 1 refusal, which names them.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 is the Medicaid waiver payments excluded on Schedule 1, line 8s. When there are none it is $0. Filers with Medicaid waiver payments are refused by name, so entering $0 is right for the supported cases.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: IRS line 3 says "Subtract line 2 from line 1."

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 is nontaxable combat pay only if the filer elects to include it. With no combat pay the amount is $0, and combat-pay filers are refused by name.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: IRS line 5 says "Add lines 3 and 4. This is your earned income."

### 1 — Enter your earned income from Step 5
Status: **MATCH**

Model: Worksheet A line 1 says "Enter your earned income from Step 5," which is Step 5 worksheet line 5.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Line 2 looks up line 1 in the EIC Table using the column for filing status and number of qualifying children with valid SSNs. The table starts at $1, so a lower amount gives $0, which leads to the "If line 2 is zero" stop.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: IRS line 3 says "Enter the amount from Form 1040 or 1040-SR, line 11b."

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: IRS line 4 asks "Are the amounts on lines 3 and 1 the same?"

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MISMATCH**

Restated: Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 3, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 3, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 3, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 3, three or more qualifying children with valid SSNs"]

Model: The restatement always enters the EIC Table credit for line 3 on line 5. The IRS text says "Yes. Skip line 5" when line 4 is Yes, and "Yes. Leave line 5 blank" when line 3 is less than $10,620/$17,730 or $23,350/$30,470. The table lookup applies only on "No."

Ruling: representation; project retained. The project figures line 5 always and line 6 reads it only when line 4 is No and line 3 is not less than the line 5 amount (eic.after_line4, eic.line6), so the skip and the blank of the printed line are kept in effect; line 6 and the credit are unaffected.

### 6 — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, line 6 is line 2. Otherwise it is line 2 when line 3 is below the IRS thresholds, and the smaller of lines 5 and 2 when it is not. The thresholds used ($10,620/$17,730 and $23,350/$30,470) match the IRS text.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 worksheet line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z.\" The clergy and church-employee adjustments to line 1 are excluded by the Schedule 1 refusal, which names them."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 is the Medicaid waiver payments excluded on Schedule 1, line 8s. When there are none it is $0. Filers with Medicaid waiver payments are refused by name, so entering $0 is right for the supported cases."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "IRS line 3 says \"Subtract line 2 from line 1.\""
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 is nontaxable combat pay only if the filer elects to include it. With no combat pay the amount is $0, and combat-pay filers are refused by name."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "IRS line 5 says \"Add lines 3 and 4. This is your earned income.\""
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 says \"Enter your earned income from Step 5,\" which is Step 5 worksheet line 5."
  - key: "2"
    status: MATCH
    reason: "Line 2 looks up line 1 in the EIC Table using the column for filing status and number of qualifying children with valid SSNs. The table starts at $1, so a lower amount gives $0, which leads to the \"If line 2 is zero\" stop."
  - key: "3"
    status: MATCH
    reason: "IRS line 3 says \"Enter the amount from Form 1040 or 1040-SR, line 11b.\""
  - key: "4"
    status: MATCH
    reason: "IRS line 4 asks \"Are the amounts on lines 3 and 1 the same?\""
  - key: "5"
    status: MISMATCH
    reason: "The restatement always enters the EIC Table credit for line 3 on line 5. The IRS text says \"Yes. Skip line 5\" when line 4 is Yes, and \"Yes. Leave line 5 blank\" when line 3 is less than $10,620/$17,730 or $23,350/$30,470. The table lookup applies only on \"No.\""
  - key: "6"
    status: MATCH
    reason: "If line 4 is Yes, line 6 is line 2. Otherwise it is line 2 when line 3 is below the IRS thresholds, and the smaller of lines 5 and 2 when it is not. The thresholds used ($10,620/$17,730 and $23,350/$30,470) match the IRS text."
```
```
