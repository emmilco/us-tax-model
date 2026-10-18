# Render comparison — sli

The rendered English of every printed line of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` (`rendered/2025/sli.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 351e625a899b8201d346f34e8e75ad34ead1837d10b67f26cc7368bb898f0a06 |
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

Model: IRS line 1 says 'Enter the total interest you paid in 2025 on qualified student loans... Don't enter more than $2,500', which the restatement computes; the QTP-earnings exclusion matches the line 21 instructions. The refusal correctly names the Pub. 970 exception for Form 2555 or 4563 filers and excluded Puerto Rico income.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: IRS line 2 says 'Enter the amount from Form 1040 or 1040-SR, line 9', and the restatement does the same.

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11 and s1 line 13.

Model: IRS line 3 says 'Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25'. The restatement adds only Schedule 1 lines 11 and 13, omitting lines 12, 14–20, 23 and 25.

Ruling: scope; project retained. Schedule 1 lines 12, 14 to 20, 23 and 25 are outside this tool: scope.schedule1 refuses Form 1040 lines 8 and 10, and worksheet line 2 reads Form 1040 line 9, so the worksheet refuses whenever any of them applies; within scope they are zero.

### 4 — Subtract line 3 from line 2
Status: **MATCH**

Model: IRS line 4 says 'Subtract line 3 from line 2', and the restatement does the same.

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **MISMATCH**

Restated: Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.base_joint ($170,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.base_other ($85,000)"]

Model: The IRS amounts are 'Single, head of household, or qualifying surviving spouse—$85,000' and 'Married filing jointly—$170,000', and the instructions say the deduction applies only if 'Your filing status is any status except married filing separately.' The restatement instead assigns $0 to married filing separately and goes on to compute a deduction, with no refusal for that status.

Ruling: representation; project retained. A married filer filing separately cannot take the deduction, and the project gives zero for that status on Schedule 1 line 21 (sli.eligible tests the filing status and sli.deduction is zero), so the zero on line 5 for that status changes nothing; the line itself is shown only because the project figures every line.

### 6 — Subtract line 5 from line 4
Status: **MATCH**

Model: IRS line 6 says 'Subtract line 5 from line 4' when line 4 is more than line 5. The restatement always subtracts, but line 8 applies the Yes/No gate, so the value that matters is the same.

### 8 — Multiply line 1 by line 7
Status: **MATCH**

Model: IRS line 7 says to divide line 6 by '$15,000 ($30,000 if married filing jointly)', round 'to at least three places', and cap at 1.000; line 8 says 'Multiply line 1 by line 7', with -0- when line 4 is not more than line 5. The restatement does all of this, and exactly three places satisfies 'at least three places.'

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **MATCH**

Model: IRS line 9 says 'Subtract line 8 from line 1.' The restatement's zero floor cannot change the result, because line 8 never exceeds line 1.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "IRS line 1 says 'Enter the total interest you paid in 2025 on qualified student loans... Don't enter more than $2,500', which the restatement computes; the QTP-earnings exclusion matches the line 21 instructions. The refusal correctly names the Pub. 970 exception for Form 2555 or 4563 filers and excluded Puerto Rico income."
  - key: "2"
    status: MATCH
    reason: "IRS line 2 says 'Enter the amount from Form 1040 or 1040-SR, line 9', and the restatement does the same."
  - key: "3"
    status: MISMATCH
    reason: "IRS line 3 says 'Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25'. The restatement adds only Schedule 1 lines 11 and 13, omitting lines 12, 14–20, 23 and 25."
  - key: "4"
    status: MATCH
    reason: "IRS line 4 says 'Subtract line 3 from line 2', and the restatement does the same."
  - key: "5"
    status: MISMATCH
    reason: "The IRS amounts are 'Single, head of household, or qualifying surviving spouse—$85,000' and 'Married filing jointly—$170,000', and the instructions say the deduction applies only if 'Your filing status is any status except married filing separately.' The restatement instead assigns $0 to married filing separately and goes on to compute a deduction, with no refusal for that status."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 says 'Subtract line 5 from line 4' when line 4 is more than line 5. The restatement always subtracts, but line 8 applies the Yes/No gate, so the value that matters is the same."
  - key: "8"
    status: MATCH
    reason: "IRS line 7 says to divide line 6 by '$15,000 ($30,000 if married filing jointly)', round 'to at least three places', and cap at 1.000; line 8 says 'Multiply line 1 by line 7', with -0- when line 4 is not more than line 5. The restatement does all of this, and exactly three places satisfies 'at least three places.'"
  - key: "9"
    status: MATCH
    reason: "IRS line 9 says 'Subtract line 8 from line 1.' The restatement's zero floor cannot change the result, because line 8 never exceeds line 1."
```
```
