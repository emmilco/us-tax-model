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

Model: The IRS text says 'Enter the amount from Form 1040 or 1040-SR, line 1z.' The clergy and church-employee adjustments, which would replace line 1z or line 1a amounts, are excluded by the refusal, which names Schedule SE and Worksheet B.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: This line enters 'Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s.' The program enters $0 and refuses when Medicaid waiver payments exist, so $0 is correct in the supported cases.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: The IRS text says 'Subtract line 2 from line 1', and the restatement does that.

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: This line enters 'all of your nontaxable combat pay if you elect to include it in earned income.' The program enters $0 and refuses whenever there is nontaxable combat pay, so $0 is correct in the supported cases.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: The IRS text says 'Add lines 3 and 4. This is your earned income', and the restatement does that.

### 1 — Enter your earned income from Step 5
Status: **MATCH**

Model: The IRS text says 'Enter your earned income from Step 5', which is the Step 5 worksheet line 5.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: The IRS says to look up line 1 in the EIC Table using the column for filing status and the number of qualifying children with valid SSNs. The table's first row starts 'At least 1', so $0 below $1 is consistent. Married filing separately uses the single/HOH column (marked ★), which a filing-status lookup can cover.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: The IRS text says 'Enter the amount from Form 1040 or 1040-SR, line 11b.'

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: The IRS asks 'Are the amounts on lines 3 and 1 the same?', which equals the restatement's test line 3 = line 1.

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MISMATCH**

Restated: Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 3, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 3, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 3, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 3, three or more qualifying children with valid SSNs"]

Model: The restatement always fills line 5 with the table credit for line 3. The IRS says 'Yes. Skip line 5' at line 4 and 'Yes. Leave line 5 blank' when line 3 is under the threshold, so the printed line should be blank in those cases. The lookup itself and line 6 are correct.

Ruling: representation; project retained. The project figures line 5 always and line 6 reads it only when line 4 is No and line 3 is not less than the line 5 amount (eic.after_line4, eic.line6), so the skip and the blank of the printed line are kept in effect; line 6 and the credit are unaffected.

### 6 — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, 'enter the amount from line 2 on line 6'. If line 4 is No, line 6 takes line 2 when line 3 is less than $10,620/$17,730 (no children) or $23,350/$30,470 (1 or more children), and otherwise 'the smaller amount' of lines 5 and 2. The helpers implement exactly this.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "The IRS text says 'Enter the amount from Form 1040 or 1040-SR, line 1z.' The clergy and church-employee adjustments, which would replace line 1z or line 1a amounts, are excluded by the refusal, which names Schedule SE and Worksheet B."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "This line enters 'Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s.' The program enters $0 and refuses when Medicaid waiver payments exist, so $0 is correct in the supported cases."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "The IRS text says 'Subtract line 2 from line 1', and the restatement does that."
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "This line enters 'all of your nontaxable combat pay if you elect to include it in earned income.' The program enters $0 and refuses whenever there is nontaxable combat pay, so $0 is correct in the supported cases."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "The IRS text says 'Add lines 3 and 4. This is your earned income', and the restatement does that."
  - key: "1"
    status: MATCH
    reason: "The IRS text says 'Enter your earned income from Step 5', which is the Step 5 worksheet line 5."
  - key: "2"
    status: MATCH
    reason: "The IRS says to look up line 1 in the EIC Table using the column for filing status and the number of qualifying children with valid SSNs. The table's first row starts 'At least 1', so $0 below $1 is consistent. Married filing separately uses the single/HOH column (marked ★), which a filing-status lookup can cover."
  - key: "3"
    status: MATCH
    reason: "The IRS text says 'Enter the amount from Form 1040 or 1040-SR, line 11b.'"
  - key: "4"
    status: MATCH
    reason: "The IRS asks 'Are the amounts on lines 3 and 1 the same?', which equals the restatement's test line 3 = line 1."
  - key: "5"
    status: MISMATCH
    reason: "The restatement always fills line 5 with the table credit for line 3. The IRS says 'Yes. Skip line 5' at line 4 and 'Yes. Leave line 5 blank' when line 3 is under the threshold, so the printed line should be blank in those cases. The lookup itself and line 6 are correct."
  - key: "6"
    status: MATCH
    reason: "If line 4 is Yes, 'enter the amount from line 2 on line 6'. If line 4 is No, line 6 takes line 2 when line 3 is less than $10,620/$17,730 (no children) or $23,350/$30,470 (1 or more children), and otherwise 'the smaller amount' of lines 5 and 2. The helpers implement exactly this."
```
```
