# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | dc55d3d5d61c150381c004f125fbd58906c10f41b378d15d1ee7df342ecbafc0 |
| lines judged | 11 |
| match / mismatch / unclear / missing | 11 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: Step 5 worksheet line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z." The Clergy and Church employees adjustments to this line are excluded by the scope.schedule1 refusal, which covers Schedule SE, clergy and church employee income.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: The IRS line asks for Medicaid waiver payments excluded on Schedule 1, line 8s. The program enters $0 and refuses whenever Medicaid waiver payments exist (scope.other_income, and scope.schedule1 for line 8s), so $0 is correct within the supported cases.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Matches "Subtract line 2 from line 1."

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: The IRS line asks for "all of your nontaxable combat pay if you elect to include it in earned income." The program enters $0 and refuses when any nontaxable combat pay exists, so the case is excluded rather than miscomputed.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: Matches "Add lines 3 and 4. This is your earned income."

### 1 — Enter your earned income from Step 5
Status: **MATCH**

Model: Matches "Enter your earned income from Step 5," which is Step 5 worksheet line 5.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Matches "Look up the amount on line 1 above in the EIC Table," using the column for filing status and the number of qualifying children with valid SSNs (0, 1, 2, 3 or more). The table's first row starts at $1, so entering $0 below $1 is consistent with the table.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: Matches "Enter the amount from Form 1040 or 1040-SR, line 11b."

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: Matches "Are the amounts on lines 3 and 1 the same?"

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Matches "Look up the amount on line 3 in the EIC Table," using the correct column for filing status and the number of qualifying children with valid SSNs. The "leave line 5 blank" case is handled correctly at line 6.

### 6 — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, line 6 is line 2. Otherwise, if line 3 is less than $10,620 ($17,730 MFJ) with no qualifying children, or $23,350 ($30,470 MFJ) with 1 or more, line 6 is line 2; failing that, it is the smaller of lines 5 and 2. This matches the worksheet text.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 worksheet line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z.\" The Clergy and Church employees adjustments to this line are excluded by the scope.schedule1 refusal, which covers Schedule SE, clergy and church employee income."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "The IRS line asks for Medicaid waiver payments excluded on Schedule 1, line 8s. The program enters $0 and refuses whenever Medicaid waiver payments exist (scope.other_income, and scope.schedule1 for line 8s), so $0 is correct within the supported cases."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "Matches \"Subtract line 2 from line 1.\""
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "The IRS line asks for \"all of your nontaxable combat pay if you elect to include it in earned income.\" The program enters $0 and refuses when any nontaxable combat pay exists, so the case is excluded rather than miscomputed."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "Matches \"Add lines 3 and 4. This is your earned income.\""
  - key: "1"
    status: MATCH
    reason: "Matches \"Enter your earned income from Step 5,\" which is Step 5 worksheet line 5."
  - key: "2"
    status: MATCH
    reason: "Matches \"Look up the amount on line 1 above in the EIC Table,\" using the column for filing status and the number of qualifying children with valid SSNs (0, 1, 2, 3 or more). The table's first row starts at $1, so entering $0 below $1 is consistent with the table."
  - key: "3"
    status: MATCH
    reason: "Matches \"Enter the amount from Form 1040 or 1040-SR, line 11b.\""
  - key: "4"
    status: MATCH
    reason: "Matches \"Are the amounts on lines 3 and 1 the same?\""
  - key: "5"
    status: MATCH
    reason: "Matches \"Look up the amount on line 3 in the EIC Table,\" using the correct column for filing status and the number of qualifying children with valid SSNs. The \"leave line 5 blank\" case is handled correctly at line 6."
  - key: "6"
    status: MATCH
    reason: "If line 4 is Yes, line 6 is line 2. Otherwise, if line 3 is less than $10,620 ($17,730 MFJ) with no qualifying children, or $23,350 ($30,470 MFJ) with 1 or more, line 6 is line 2; failing that, it is the smaller of lines 5 and 2. This matches the worksheet text."
```
```
