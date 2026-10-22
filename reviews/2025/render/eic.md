# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 29b82e7027c09a9a08c634ffb009b49991f9b0a6fe3ae4d82445690b6d033215 |
| subject sha256 | c4acd4834c60576a73d3e149a31c1a6eb17f2e0b3ca8c969940587f5eefbf8f8 |
| lines judged | 13 |
| match / mismatch / unclear / missing | 13 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: The Step 5 worksheet line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z". The clergy and church-employee adjustments that replace this amount are excluded by the scope.schedule1 refusal, which names clergy and church employee income.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 is "the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s". The program enters $0 and refuses any Medicaid waiver payments through scope.other_income, so $0 is correct in every case it computes.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Matches "Subtract line 2 from line 1."

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 is "all of your nontaxable combat pay if you elect to include it in earned income". The program enters $0 and refuses any nontaxable combat pay, so $0 is correct in every case it computes.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: Matches "Add lines 3 and 4. This is your earned income."

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: Worksheet B 4b says "Combine lines 1e, 2c, 3, and 4a". Line 3 (statutory employee income from Schedule C) is left out, but statutory-employee wages are refused by scope.schedule1, so line 3 is zero in every supported case; 4a is the Step 5 earned income (Step 5, 5).

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b 
Status: **MATCH**

Model: Worksheet B line 6 says "Enter your total earned income from Part 4, line 4b." The floor at zero only changes the value where the IRS says "If line 4b is zero or less, STOP You can't take the credit"; a zero then gives no table credit at line 2, so the result is the same.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: Worksheet A line 1 is "your earned income from Step 5" and applies only to filers who answered No to Step 5 question 2; Worksheet B (lines 6-11, which parallel Worksheet A lines 1-6) applies otherwise, and the program routes to Worksheet B line 6. Using Schedule C as the self-employment test is enough here because farm, partnership, clergy and statutory-employee cases are refused.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Matches "Look up the amount on line 1 above in the EIC Table ... correct column for your filing status and the number of qualifying children you have who have valid SSNs". The table's first row begins at $1, so an amount under $1 gets no credit.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: Matches "Enter the amount from Form 1040 or 1040-SR, line 11b."

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: Matches "Are the amounts on lines 3 and 1 the same?"

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Matches "Look up the amount on line 3 in the EIC Table ... correct column for your filing status and the number of qualifying children you have who have valid SSNs". The blank-line condition is handled at line 6.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: Matches the IRS rules: line 4 Yes enters line 2. Otherwise, if line 3 is less than $10,620/$17,730 (no qualifying children) or $23,350/$30,470 (one or more), line 5 is left blank and line 2 is entered; if not, "enter the smaller amount" of lines 5 and 2.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "The Step 5 worksheet line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z\". The clergy and church-employee adjustments that replace this amount are excluded by the scope.schedule1 refusal, which names clergy and church employee income."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 is \"the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s\". The program enters $0 and refuses any Medicaid waiver payments through scope.other_income, so $0 is correct in every case it computes."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "Matches \"Subtract line 2 from line 1.\""
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 is \"all of your nontaxable combat pay if you elect to include it in earned income\". The program enters $0 and refuses any nontaxable combat pay, so $0 is correct in every case it computes."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "Matches \"Add lines 3 and 4. This is your earned income.\""
  - key: "4b"
    status: MATCH
    reason: "Worksheet B 4b says \"Combine lines 1e, 2c, 3, and 4a\". Line 3 (statutory employee income from Schedule C) is left out, but statutory-employee wages are refused by scope.schedule1, so line 3 is zero in every supported case; 4a is the Step 5 earned income (Step 5, 5)."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "Worksheet B line 6 says \"Enter your total earned income from Part 4, line 4b.\" The floor at zero only changes the value where the IRS says \"If line 4b is zero or less, STOP You can't take the credit\"; a zero then gives no table credit at line 2, so the result is the same."
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 is \"your earned income from Step 5\" and applies only to filers who answered No to Step 5 question 2; Worksheet B (lines 6-11, which parallel Worksheet A lines 1-6) applies otherwise, and the program routes to Worksheet B line 6. Using Schedule C as the self-employment test is enough here because farm, partnership, clergy and statutory-employee cases are refused."
  - key: "2"
    status: MATCH
    reason: "Matches \"Look up the amount on line 1 above in the EIC Table ... correct column for your filing status and the number of qualifying children you have who have valid SSNs\". The table's first row begins at $1, so an amount under $1 gets no credit."
  - key: "3"
    status: MATCH
    reason: "Matches \"Enter the amount from Form 1040 or 1040-SR, line 11b.\""
  - key: "4"
    status: MATCH
    reason: "Matches \"Are the amounts on lines 3 and 1 the same?\""
  - key: "5"
    status: MATCH
    reason: "Matches \"Look up the amount on line 3 in the EIC Table ... correct column for your filing status and the number of qualifying children you have who have valid SSNs\". The blank-line condition is handled at line 6."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "Matches the IRS rules: line 4 Yes enters line 2. Otherwise, if line 3 is less than $10,620/$17,730 (no qualifying children) or $23,350/$30,470 (one or more), line 5 is left blank and line 2 is entered; if not, \"enter the smaller amount\" of lines 5 and 2."
```
```
