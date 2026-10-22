# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d7bc1e83b2870a0ed79e77510afef66f9e4cf972137d084374da213e5994bbeb |
| subject sha256 | 5d8bc927b6aa108f949657fdd3ea4773991ad7886415e975b861f7d0e6a7bda3 |
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

Model: Step 5 worksheet line 1 says "Enter the amount from Form 1040 or 1040-SR, line 1z." The clergy and church-employee adjustments to this line are excluded by the scope.schedule1 refusal, which names them.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: Line 2 asks for "the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s." The program enters $0 and refuses any return with Medicaid waiver payments (scope.other_income), so $0 is correct in the cases it handles.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Matches "Subtract line 2 from line 1."

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: Line 4 asks for "all of your nontaxable combat pay if you elect to include it in earned income." The program enters $0 and refuses any return with nontaxable combat pay, so $0 is correct in the cases it handles.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: Matches "Add lines 3 and 4. This is your earned income."

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: IRS says "Combine lines 1e, 2c, 3, and 4a." The program adds 4a (Step 5 earned income) to 1e and 2c. It leaves out line 3 (statutory employee income), but statutory-employee wages are excluded by the scope.schedule1 refusal, so line 3 is zero in the cases it handles.

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b 
Status: **MATCH**

Model: Worksheet B line 6 says "Enter your total earned income from Part 4, line 4b." The program also turns zero or less into -0-. The IRS instead says "If line 4b is zero or less, STOP You can't take the credit," but a -0- line 1 gives a credit of 0 either way, so the result is the same.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: Worksheet A line 1 is "your earned income from Step 5" for filers who answered No to Step 5 question 2; filers who answered Yes use Worksheet B. The program tests self-employment by whether there is a Schedule C. The other ways to answer Yes (clergy, church employee, statutory employee, farm, partnership) are excluded by the scope.schedule1 refusal.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: Matches "Look up the amount on line 1 above in the EIC Table ... correct column for your filing status and the number of qualifying children you have who have valid SSNs." The table's first row starts at $1, so an amount below that correctly gives 0.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: Matches "Enter the amount from Form 1040 or 1040-SR, line 11b."

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: Matches "Are the amounts on lines 3 and 1 the same?"

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MISMATCH**

Restated: Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 3, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 3, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 3, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 3, three or more qualifying children with valid SSNs"]

Model: The program always enters the table credit for line 3. The IRS fills line 5 only conditionally: for Yes on line 4 it says "Skip line 5," and when line 3 is below the threshold it says "Yes. Leave line 5 blank." So the printed line 5 shows an amount where the IRS leaves it blank. Line 6 still applies the blank rule, so the credit itself is not affected.

Ruling: representation; project retained (as the prior rulings). The project figures line 5 always and line 6 reads it only in the case the worksheet uses it (line 4 No and line 3 at or above the line 5 amount), so line 6 and the credit are the same; the model says so too. i1040gi p. 46, Worksheet A, line 4 "Yes. Skip line 5" and line 5 "Yes. Leave line 5 blank". No change.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: Matches the IRS logic. Line 4 Yes enters line 2. Line 4 No with line 3 under the threshold ($10,620/$17,730 MFJ with no children; $23,350/$30,470 MFJ with 1 or more) also enters line 2. Otherwise it is "the smaller amount" of lines 5 and 2.

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "Step 5 worksheet line 1 says \"Enter the amount from Form 1040 or 1040-SR, line 1z.\" The clergy and church-employee adjustments to this line are excluded by the scope.schedule1 refusal, which names them."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "Line 2 asks for \"the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s.\" The program enters $0 and refuses any return with Medicaid waiver payments (scope.other_income), so $0 is correct in the cases it handles."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "Matches \"Subtract line 2 from line 1.\""
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "Line 4 asks for \"all of your nontaxable combat pay if you elect to include it in earned income.\" The program enters $0 and refuses any return with nontaxable combat pay, so $0 is correct in the cases it handles."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "Matches \"Add lines 3 and 4. This is your earned income.\""
  - key: "4b"
    status: MATCH
    reason: "IRS says \"Combine lines 1e, 2c, 3, and 4a.\" The program adds 4a (Step 5 earned income) to 1e and 2c. It leaves out line 3 (statutory employee income), but statutory-employee wages are excluded by the scope.schedule1 refusal, so line 3 is zero in the cases it handles."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "Worksheet B line 6 says \"Enter your total earned income from Part 4, line 4b.\" The program also turns zero or less into -0-. The IRS instead says \"If line 4b is zero or less, STOP You can't take the credit,\" but a -0- line 1 gives a credit of 0 either way, so the result is the same."
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 is \"your earned income from Step 5\" for filers who answered No to Step 5 question 2; filers who answered Yes use Worksheet B. The program tests self-employment by whether there is a Schedule C. The other ways to answer Yes (clergy, church employee, statutory employee, farm, partnership) are excluded by the scope.schedule1 refusal."
  - key: "2"
    status: MATCH
    reason: "Matches \"Look up the amount on line 1 above in the EIC Table ... correct column for your filing status and the number of qualifying children you have who have valid SSNs.\" The table's first row starts at $1, so an amount below that correctly gives 0."
  - key: "3"
    status: MATCH
    reason: "Matches \"Enter the amount from Form 1040 or 1040-SR, line 11b.\""
  - key: "4"
    status: MATCH
    reason: "Matches \"Are the amounts on lines 3 and 1 the same?\""
  - key: "5"
    status: MISMATCH
    reason: "The program always enters the table credit for line 3. The IRS fills line 5 only conditionally: for Yes on line 4 it says \"Skip line 5,\" and when line 3 is below the threshold it says \"Yes. Leave line 5 blank.\" So the printed line 5 shows an amount where the IRS leaves it blank. Line 6 still applies the blank rule, so the credit itself is not affected."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "Matches the IRS logic. Line 4 Yes enters line 2. Line 4 No with line 3 under the threshold ($10,620/$17,730 MFJ with no children; $23,350/$30,470 MFJ with 1 or more) also enters line 2. Otherwise it is \"the smaller amount\" of lines 5 and 2."
```
```
