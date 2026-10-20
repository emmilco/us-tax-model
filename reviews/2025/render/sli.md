# Render comparison — sli

The rendered English of every printed line of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` (`rendered/2025/sli.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 39a17ac76f55996e0b4e32b57ab5a2762789defa2aa28e63bdee7455dc5b3d70 |
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

Model: The worksheet says to enter total qualified student loan interest but "Don't enter more than $2,500", which is the smaller of the two. The glossary excludes tax-free QTP amounts, and the refusal covers the Pub. 970 Exception for Form 2555/4563 or Puerto Rico excluded income.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: The worksheet says "Enter the amount from Form 1040 or 1040-SR, line 9".

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, and s1 line 17.

Model: The IRS line says "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25". The restatement adds only lines 11, 13, 15, 16 and 17, so it leaves out lines 12, 14, 18, 19a, 20, 23 and 25.

Ruling: scope; project retained. Schedule 1 lines 12, 14 to 20, 23 and 25 are outside this tool: scope.schedule1 refuses Form 1040 lines 8 and 10, and worksheet line 2 reads Form 1040 line 9, so the worksheet refuses whenever any of them applies; within scope they are zero.

### 4 — Subtract line 3 from line 2
Status: **MATCH**

Model: The worksheet says "Subtract line 3 from line 2".

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **MISMATCH**

Restated: Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.base_joint ($170,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.base_other ($85,000)"]

Model: The worksheet lists amounts only for "Single, head of household, or qualifying surviving spouse—$85,000" and "Married filing jointly—$170,000", and the instructions say the deduction is allowed only if "Your filing status is any status except married filing separately." The restatement instead gives married filing separately a $0 base and has no refusal, so an MFS filer can still get a nonzero deduction.

Ruling: representation; project retained. A married filer filing separately cannot take the deduction, and the project gives zero for that status on Schedule 1 line 21 (sli.eligible tests the filing status and sli.deduction is zero), so the zero on line 5 for that status changes nothing; the line itself is shown only because the project figures every line.

### 6 — Subtract line 5 from line 4
Status: **MATCH**

Model: The worksheet says "Yes. Subtract line 5 from line 4". When the answer is No, line 6 is skipped and line 8 takes the zero branch, so computing it anyway does not change the result.

### 8 — Multiply line 1 by line 7
Status: **MATCH**

Model: This follows "No... enter -0- on line 8" and, for Yes, divides line 6 by "$15,000 ($30,000 if married filing jointly)" with the result capped at 1.000, then multiplies line 1 by it. Rounding to three places meets "rounded to at least three places".

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **MATCH**

Model: The worksheet says "Subtract line 8 from line 1". Line 8 cannot exceed line 1, so the -0- floor never changes the value.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The worksheet says to enter total qualified student loan interest but \"Don't enter more than $2,500\", which is the smaller of the two. The glossary excludes tax-free QTP amounts, and the refusal covers the Pub. 970 Exception for Form 2555/4563 or Puerto Rico excluded income."
  - key: "2"
    status: MATCH
    reason: "The worksheet says \"Enter the amount from Form 1040 or 1040-SR, line 9\"."
  - key: "3"
    status: MISMATCH
    reason: "The IRS line says \"Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25\". The restatement adds only lines 11, 13, 15, 16 and 17, so it leaves out lines 12, 14, 18, 19a, 20, 23 and 25."
  - key: "4"
    status: MATCH
    reason: "The worksheet says \"Subtract line 3 from line 2\"."
  - key: "5"
    status: MISMATCH
    reason: "The worksheet lists amounts only for \"Single, head of household, or qualifying surviving spouse—$85,000\" and \"Married filing jointly—$170,000\", and the instructions say the deduction is allowed only if \"Your filing status is any status except married filing separately.\" The restatement instead gives married filing separately a $0 base and has no refusal, so an MFS filer can still get a nonzero deduction."
  - key: "6"
    status: MATCH
    reason: "The worksheet says \"Yes. Subtract line 5 from line 4\". When the answer is No, line 6 is skipped and line 8 takes the zero branch, so computing it anyway does not change the result."
  - key: "8"
    status: MATCH
    reason: "This follows \"No... enter -0- on line 8\" and, for Yes, divides line 6 by \"$15,000 ($30,000 if married filing jointly)\" with the result capped at 1.000, then multiplies line 1 by it. Rounding to three places meets \"rounded to at least three places\"."
  - key: "9"
    status: MATCH
    reason: "The worksheet says \"Subtract line 8 from line 1\". Line 8 cannot exceed line 1, so the -0- floor never changes the value."
```
```
