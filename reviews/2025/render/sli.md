# Render comparison — sli

The rendered English of every printed line of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` (`rendered/2025/sli.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b6d8bb710b67f5296af76c7849ff8e61fc8837977d9e2ebc72cc5cfbe7a82ced |
| subject sha256 | 45830749bffa8b7df0c0523207e522a36b1f83bfcbd6b48fa5a3ee55b3f2e1df |
| lines judged | 8 |
| match / mismatch / unclear / missing | 6 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the total interest you paid in 2025 on qualified student loans (see the instructions
Status: **MATCH**

Model: The IRS line says to enter the total interest paid in 2025 on qualified student loans and "Don't enter more than $2,500", which the restatement takes as the smaller of the two. The refusal correctly sends filers who file Form 2555 or 4563, or who exclude Puerto Rico income, to Pub. 970, as the Exception requires.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: The IRS line says "Enter the amount from Form 1040 or 1040-SR, line 9", which is what the restatement does.

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, s1 line 20, and s1 line 25.

Model: The IRS says "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25". The restatement leaves out lines 12 and 14 (both inside "11 through 20") and line 23 (Archer MSA deduction), so line 3 is too small whenever any of those has an amount.

Ruling: refusal located elsewhere; project retained (as the prior rulings). Schedule 1 lines 12, 14 and 23 are outside this tool: scope.schedule1 asks about "an adjustment on Schedule 1 line 12, 14 or 23" and refuses Form 1040 lines 8 and 10, so worksheet line 2 (Form 1040 line 9) refuses whenever one applies and within scope they are zero. The lines in scope (11, 13, 15 to 20 and 25) are all added. i1040gi, Student Loan Interest Deduction Worksheet, line 3, "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25".

### 4 — Subtract line 3 from line 2
Status: **MATCH**

Model: The IRS line says "Subtract line 3 from line 2", which is what the restatement does.

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **MISMATCH**

Restated: Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.base_joint ($170,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.base_other ($85,000)"]

Model: The worksheet gives amounts only for "Single, head of household, or qualifying surviving spouse—$85,000" and "Married filing jointly—$170,000", and the instructions allow the deduction only if "Your filing status is any status except married filing separately." The restatement gives married filing separately $0 instead of refusing it or setting the deduction to zero. A married-filing-separately filer with line 4 under $15,000 would then get a deduction above zero.

Ruling: representation; project retained (as the prior rulings). A married filer filing separately cannot take the deduction (i1040gi p. 98, Line 21, "Your filing status is any status except married filing separately"), and the project gives zero for that status on Schedule 1 line 21 (sli.eligible tests the filing status), so the zero on line 5 changes nothing; a separate return is also refused (scope.ready, s3.mfs).

### 6 — Subtract line 5 from line 4
Status: **MATCH**

Model: The IRS line says "Subtract line 5 from line 4" when the answer is Yes, and the restatement does that. It also computes line 6 when the answer is No, but line 8 is set to zero in that case, so the result does not change.

### 8 — Multiply line 1 by line 7
Status: **MATCH**

Model: This follows the IRS lines 6–8: if No, "enter -0- on line 8"; if Yes, "Divide line 6 by $15,000 ($30,000 if married filing jointly)", round to at least three places, cap at 1.000, and "Multiply line 1 by line 7". Rounding to exactly three places is allowed by "at least three places", and the floor at 0 never applies because line 6 is positive.

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **MATCH**

Model: The IRS line says "Subtract line 8 from line 1". The added floor at -0- has no effect because line 8 cannot be more than line 1. The married-filing-separately problem is flagged at line 5.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The IRS line says to enter the total interest paid in 2025 on qualified student loans and \"Don't enter more than $2,500\", which the restatement takes as the smaller of the two. The refusal correctly sends filers who file Form 2555 or 4563, or who exclude Puerto Rico income, to Pub. 970, as the Exception requires."
  - key: "2"
    status: MATCH
    reason: "The IRS line says \"Enter the amount from Form 1040 or 1040-SR, line 9\", which is what the restatement does."
  - key: "3"
    status: MISMATCH
    reason: "The IRS says \"Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25\". The restatement leaves out lines 12 and 14 (both inside \"11 through 20\") and line 23 (Archer MSA deduction), so line 3 is too small whenever any of those has an amount."
  - key: "4"
    status: MATCH
    reason: "The IRS line says \"Subtract line 3 from line 2\", which is what the restatement does."
  - key: "5"
    status: MISMATCH
    reason: "The worksheet gives amounts only for \"Single, head of household, or qualifying surviving spouse—$85,000\" and \"Married filing jointly—$170,000\", and the instructions allow the deduction only if \"Your filing status is any status except married filing separately.\" The restatement gives married filing separately $0 instead of refusing it or setting the deduction to zero. A married-filing-separately filer with line 4 under $15,000 would then get a deduction above zero."
  - key: "6"
    status: MATCH
    reason: "The IRS line says \"Subtract line 5 from line 4\" when the answer is Yes, and the restatement does that. It also computes line 6 when the answer is No, but line 8 is set to zero in that case, so the result does not change."
  - key: "8"
    status: MATCH
    reason: "This follows the IRS lines 6–8: if No, \"enter -0- on line 8\"; if Yes, \"Divide line 6 by $15,000 ($30,000 if married filing jointly)\", round to at least three places, cap at 1.000, and \"Multiply line 1 by line 7\". Rounding to exactly three places is allowed by \"at least three places\", and the floor at 0 never applies because line 6 is positive."
  - key: "9"
    status: MATCH
    reason: "The IRS line says \"Subtract line 8 from line 1\". The added floor at -0- has no effect because line 8 cannot be more than line 1. The married-filing-separately problem is flagged at line 5."
```
```
