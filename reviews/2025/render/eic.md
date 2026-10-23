# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a617618aeaba56eb00e596d7f9a5415df71a067cb077fd0ced48ffa4f75a1284 |
| subject sha256 | bd8402b363f39c982f3f55589e95af2b506be6447d0843c3f84746f72b0864de |
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

Model: Step 5 worksheet line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z". The clergy and church-employee adjustments that would change this line are refused through scope.schedule1, which names them.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 is "the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s". The program enters $0 and refuses any return with Medicaid waiver payments through scope.other_income (and the line 8s exclusion through scope.schedule1), so $0 is correct within scope.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Line 3 says "Subtract line 2 from line 1"; the restatement does the same.

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 is "all of your nontaxable combat pay if you elect to include it in earned income". The program enters $0 and refuses any return with nontaxable combat pay through s8812.combat_pay.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: Line 5 says "Add lines 3 and 4. This is your earned income"; the restatement does the same.

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: Line 4b says "Combine lines 1e, 2c, 3, and 4a", including a spouse's amounts on a joint return. The helper sums, per person, either Schedule SE line 3 less line 13 (lines 1a–1e, with line 1b zero because optional methods and church income are refused) or the Schedule C net profit (line 2b). Farm, K-1 and statutory-employee amounts (lines 2a and 3) are refused, so the restatement is right within scope.

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b 
Status: **MATCH**

Model: Worksheet B line 6 says "Enter your total earned income from Part 4, line 4b". The zero floor only applies where the IRS says "If line 4b is zero or less, STOP You can't take the credit", and the downstream line 2 gate then yields no credit, so the outcome is the same.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: Worksheet A line 1 is "your earned income from Step 5" for filers who answered No to Step 5 question 2. For self-employed filers the program uses Worksheet B's line 6 and reuses Worksheet A lines 2–6, which mirror Worksheet B lines 7–11 exactly. The other Yes cases for question 2 (clergy, church employees, statutory employees, farm and partnership income) are refused.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Line 2 says "Look up the amount on line 1 above in the EIC Table … correct column for your filing status and the number of qualifying children you have who have valid SSNs". The table starts at "At least 1", so amounts below $1 get no credit.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: Line 3 says "Enter the amount from Form 1040 or 1040-SR, line 11b"; the restatement does the same.

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: Line 4 asks "Are the amounts on lines 3 and 1 the same?"; the restatement tests line 3 = line 1.

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Line 5 says "Look up the amount on line 3 in the EIC Table … correct column for your filing status and the number of qualifying children … with valid SSNs", and the restatement does this lookup. The "Skip line 5" and "Leave line 5 blank" cases are not applied on this line; the program handles them in the line 6 selection instead.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, line 6 is line 2. If No, line 6 is line 2 when line 3 is under $10,620 ($17,730 MFJ) with no qualifying children, or under $23,350 ($30,470 MFJ) with one or more; otherwise it is "the smaller amount" of lines 5 and 2. The thresholds and the comparison direction match the IRS text.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 worksheet line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z\". The clergy and church-employee adjustments that would change this line are refused through scope.schedule1, which names them."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 is \"the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s\". The program enters $0 and refuses any return with Medicaid waiver payments through scope.other_income (and the line 8s exclusion through scope.schedule1), so $0 is correct within scope."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "Line 3 says \"Subtract line 2 from line 1\"; the restatement does the same."
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 is \"all of your nontaxable combat pay if you elect to include it in earned income\". The program enters $0 and refuses any return with nontaxable combat pay through s8812.combat_pay."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "Line 5 says \"Add lines 3 and 4. This is your earned income\"; the restatement does the same."
  - key: "4b"
    status: MATCH
    reason: "Line 4b says \"Combine lines 1e, 2c, 3, and 4a\", including a spouse's amounts on a joint return. The helper sums, per person, either Schedule SE line 3 less line 13 (lines 1a–1e, with line 1b zero because optional methods and church income are refused) or the Schedule C net profit (line 2b). Farm, K-1 and statutory-employee amounts (lines 2a and 3) are refused, so the restatement is right within scope."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "Worksheet B line 6 says \"Enter your total earned income from Part 4, line 4b\". The zero floor only applies where the IRS says \"If line 4b is zero or less, STOP You can't take the credit\", and the downstream line 2 gate then yields no credit, so the outcome is the same."
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 is \"your earned income from Step 5\" for filers who answered No to Step 5 question 2. For self-employed filers the program uses Worksheet B's line 6 and reuses Worksheet A lines 2–6, which mirror Worksheet B lines 7–11 exactly. The other Yes cases for question 2 (clergy, church employees, statutory employees, farm and partnership income) are refused."
  - key: "2"
    status: MATCH
    reason: "Line 2 says \"Look up the amount on line 1 above in the EIC Table … correct column for your filing status and the number of qualifying children you have who have valid SSNs\". The table starts at \"At least 1\", so amounts below $1 get no credit."
  - key: "3"
    status: MATCH
    reason: "Line 3 says \"Enter the amount from Form 1040 or 1040-SR, line 11b\"; the restatement does the same."
  - key: "4"
    status: MATCH
    reason: "Line 4 asks \"Are the amounts on lines 3 and 1 the same?\"; the restatement tests line 3 = line 1."
  - key: "5"
    status: MATCH
    reason: "Line 5 says \"Look up the amount on line 3 in the EIC Table … correct column for your filing status and the number of qualifying children … with valid SSNs\", and the restatement does this lookup. The \"Skip line 5\" and \"Leave line 5 blank\" cases are not applied on this line; the program handles them in the line 6 selection instead."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "If line 4 is Yes, line 6 is line 2. If No, line 6 is line 2 when line 3 is under $10,620 ($17,730 MFJ) with no qualifying children, or under $23,350 ($30,470 MFJ) with one or more; otherwise it is \"the smaller amount\" of lines 5 and 2. The thresholds and the comparison direction match the IRS text."
```
```
