# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 66c7eced34f39e0da42b7a22227cbb0d55e0c9a197885f8b4b698b9e27a8e4e8 |
| subject sha256 | 4d52284bf939c6171d813f8bd783decd48710ae12b0cc5fe123aae6d2642b87e |
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

Model: Step 5 line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z". The Clergy and Church employees adjustments are excluded by the scope.schedule1 refusal, which names them.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 is the Medicaid waiver payments excluded on Schedule 1, line 8s. With those payments refused through scope.other_income (which names them), the amount is correctly $0.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: "Subtract line 2 from line 1" is computed as written.

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 is nontaxable combat pay the filer elects to include. Combat pay is refused through s8812.combat_pay, so $0 is correct in the cases the program supports.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: "Add lines 3 and 4. This is your earned income" is computed as written.

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: Worksheet B line 4b says "Combine lines 1e, 2c, 3, and 4a". The program adds Step 5 earned income (4a) to the helper for lines 1e and 2c. Line 3, statutory employee income, is $0 because statutory-employee wages are refused through scope.schedule1.

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b 
Status: **MATCH**

Model: Worksheet B line 6 says "Enter your total earned income from Part 4, line 4b." The floor at zero matches the instruction "If line 4b is zero or less, STOP You can't take the credit", because a $0 amount produces no credit downstream.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: Worksheet A line 1 is the earned income from Step 5. For self-employed filers the program uses Worksheet B line 6 instead. Worksheet B lines 7-11 repeat Worksheet A lines 2-6 exactly, so the credit comes out the same. Within scope, a Schedule C is the only source of self-employment; farm, partnership, clergy and statutory-employee cases are refused.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: The program looks up line 1 in the EIC Table using the column for filing status and number of qualifying children with valid SSNs. The table starts at "At least 1", so an amount below $1 gets no credit, which is the "If line 2 is zero, STOP" case. Married filing separately uses the single column, as the ★ note says.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: "Enter the amount from Form 1040 or 1040-SR, line 11b" is computed as written.

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: "Are the amounts on lines 3 and 1 the same?" is restated as line 3 = line 1.

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: The program looks up line 3 in the EIC Table by number of qualifying children with valid SSNs and filing status, as the line says. Line 5 itself always shows the lookup. The worksheet's "Leave line 5 blank" (Yes) case is handled only at line 6, so the credit is unaffected.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, the program uses line 2. If No, it uses line 2 when line 3 is below $10,620/$17,730 (no qualifying child) or $23,350/$30,470 (one or more), and otherwise "enter the smaller amount" of lines 5 and 2. This follows the worksheet.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z\". The Clergy and Church employees adjustments are excluded by the scope.schedule1 refusal, which names them."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 is the Medicaid waiver payments excluded on Schedule 1, line 8s. With those payments refused through scope.other_income (which names them), the amount is correctly $0."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "\"Subtract line 2 from line 1\" is computed as written."
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 is nontaxable combat pay the filer elects to include. Combat pay is refused through s8812.combat_pay, so $0 is correct in the cases the program supports."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "\"Add lines 3 and 4. This is your earned income\" is computed as written."
  - key: "4b"
    status: MATCH
    reason: "Worksheet B line 4b says \"Combine lines 1e, 2c, 3, and 4a\". The program adds Step 5 earned income (4a) to the helper for lines 1e and 2c. Line 3, statutory employee income, is $0 because statutory-employee wages are refused through scope.schedule1."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "Worksheet B line 6 says \"Enter your total earned income from Part 4, line 4b.\" The floor at zero matches the instruction \"If line 4b is zero or less, STOP You can't take the credit\", because a $0 amount produces no credit downstream."
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 is the earned income from Step 5. For self-employed filers the program uses Worksheet B line 6 instead. Worksheet B lines 7-11 repeat Worksheet A lines 2-6 exactly, so the credit comes out the same. Within scope, a Schedule C is the only source of self-employment; farm, partnership, clergy and statutory-employee cases are refused."
  - key: "2"
    status: MATCH
    reason: "The program looks up line 1 in the EIC Table using the column for filing status and number of qualifying children with valid SSNs. The table starts at \"At least 1\", so an amount below $1 gets no credit, which is the \"If line 2 is zero, STOP\" case. Married filing separately uses the single column, as the ★ note says."
  - key: "3"
    status: MATCH
    reason: "\"Enter the amount from Form 1040 or 1040-SR, line 11b\" is computed as written."
  - key: "4"
    status: MATCH
    reason: "\"Are the amounts on lines 3 and 1 the same?\" is restated as line 3 = line 1."
  - key: "5"
    status: MATCH
    reason: "The program looks up line 3 in the EIC Table by number of qualifying children with valid SSNs and filing status, as the line says. Line 5 itself always shows the lookup. The worksheet's \"Leave line 5 blank\" (Yes) case is handled only at line 6, so the credit is unaffected."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "If line 4 is Yes, the program uses line 2. If No, it uses line 2 when line 3 is below $10,620/$17,730 (no qualifying child) or $23,350/$30,470 (one or more), and otherwise \"enter the smaller amount\" of lines 5 and 2. This follows the worksheet."
```
```
