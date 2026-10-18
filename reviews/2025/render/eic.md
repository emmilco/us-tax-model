# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 959de3075c44641891343b559f08c80d6fbce3cc845fd7ff84af9eb4a8468deb |
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

Model: Step 5 worksheet line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z". The clergy and church-employee adjustments, which change this entry, are covered by the schedule1 refusal.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 asks for "the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s", or -0-. The program enters $0 and refuses whenever Medicaid waiver payments are present (scope.other_income, and scope.schedule1 for line 8s), so $0 is right within the supported cases.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: This matches "Subtract line 2 from line 1."

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 says "Enter all of your nontaxable combat pay if you elect to include it in earned income." The program enters $0 and refuses whenever there is any nontaxable combat pay, so $0 is right in the cases it handles.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: This matches "Add lines 3 and 4. This is your earned income."

### 1 — Enter your earned income from Step 5
Status: **MATCH**

Model: Worksheet A line 1 says "Enter your earned income from Step 5", which is Step 5 line 5.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Line 2 says to look up line 1 in the EIC Table using the column for filing status and "the number of qualifying children you have who have valid SSNs". The table starts at "At least 1", so entering $0 below $1 is consistent with it, and the 0/1/2/3-or-more column choice matches the table.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: This matches "Enter the amount from Form 1040 or 1040-SR, line 11b."

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: This matches "Are the amounts on lines 3 and 1 the same?"

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MISMATCH**

Restated: Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 3, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 3, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 3, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 3, three or more qualifying children with valid SSNs"]

Model: The IRS fills line 5 only in some cases: line 4 "Yes. Skip line 5", and the threshold test "Yes. Leave line 5 blank". It does the lookup only under "No. Look up the amount on line 3 in the EIC Table". The program always does the table lookup on line 3, so it prints an amount where the IRS leaves line 5 blank. The credit on line 6 is unaffected because line 6 applies the blank condition.

Ruling: representation; project retained. As the transcription ruling on line 5: the project figures line 5 always and line 6 reads it only in the case the worksheet uses it (line 4 No and line 3 at or above the line 5 amount), so line 6 and the credit are the same; the model says so too.

### 6 — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, line 6 is line 2. If line 4 is No and line 3 is below the threshold ($10,620/$17,730 with no children, $23,350/$30,470 with one or more), line 6 is line 2. Otherwise it is "the smaller amount" of lines 5 and 2. The joint and non-joint thresholds match the worksheet.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 worksheet line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z\". The clergy and church-employee adjustments, which change this entry, are covered by the schedule1 refusal."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 asks for \"the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s\", or -0-. The program enters $0 and refuses whenever Medicaid waiver payments are present (scope.other_income, and scope.schedule1 for line 8s), so $0 is right within the supported cases."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "This matches \"Subtract line 2 from line 1.\""
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 says \"Enter all of your nontaxable combat pay if you elect to include it in earned income.\" The program enters $0 and refuses whenever there is any nontaxable combat pay, so $0 is right in the cases it handles."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "This matches \"Add lines 3 and 4. This is your earned income.\""
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 says \"Enter your earned income from Step 5\", which is Step 5 line 5."
  - key: "2"
    status: MATCH
    reason: "Line 2 says to look up line 1 in the EIC Table using the column for filing status and \"the number of qualifying children you have who have valid SSNs\". The table starts at \"At least 1\", so entering $0 below $1 is consistent with it, and the 0/1/2/3-or-more column choice matches the table."
  - key: "3"
    status: MATCH
    reason: "This matches \"Enter the amount from Form 1040 or 1040-SR, line 11b.\""
  - key: "4"
    status: MATCH
    reason: "This matches \"Are the amounts on lines 3 and 1 the same?\""
  - key: "5"
    status: MISMATCH
    reason: "The IRS fills line 5 only in some cases: line 4 \"Yes. Skip line 5\", and the threshold test \"Yes. Leave line 5 blank\". It does the lookup only under \"No. Look up the amount on line 3 in the EIC Table\". The program always does the table lookup on line 3, so it prints an amount where the IRS leaves line 5 blank. The credit on line 6 is unaffected because line 6 applies the blank condition."
  - key: "6"
    status: MATCH
    reason: "If line 4 is Yes, line 6 is line 2. If line 4 is No and line 3 is below the threshold ($10,620/$17,730 with no children, $23,350/$30,470 with one or more), line 6 is line 2. Otherwise it is \"the smaller amount\" of lines 5 and 2. The joint and non-joint thresholds match the worksheet."
```
```
