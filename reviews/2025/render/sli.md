# Render comparison — sli

The rendered English of every printed line of `Student Loan Interest Deduction Worksheet—Schedule 1, Line 21` (`rendered/2025/sli.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 39a17ac76f55996e0b4e32b57ab5a2762789defa2aa28e63bdee7455dc5b3d70 |
| subject sha256 | 7d5763f1ef4a0d17396f0302da999d2af49b1ef7b7779af0583a91721eb14138 |
| lines judged | 8 |
| match / mismatch / unclear / missing | 5 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 98, 99 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the total interest you paid in 2025 on qualified student loans (see the instructions
Status: **MATCH**

Model: The worksheet says to 'Enter the total interest you paid in 2025 on qualified student loans... Don't enter more than $2,500', which is the smaller of interest or $2,500. The refusal matches the Exception: 'Use Pub. 970 instead of the worksheet... if you file Form 2555 or 4563, or you exclude income from sources within Puerto Rico.'

### 2 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: The worksheet says 'Enter the amount from Form 1040 or 1040-SR, line 9.'

### 3 — Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, and s1 line 17.

Model: The IRS says 'Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25.' The restatement adds only lines 11, 13, 15, 16 and 17, leaving out lines 12, 14, 18, 19, 20, 23 and 25.

Ruling: scope; project retained. Schedule 1 lines 11, 13, 15, 16 and 17 are the adjustments in scope and the restatement adds them; lines 12, 14, 18 to 20, 23 and 25 are outside this tool: scope.schedule1 refuses 'Any income or adjustment requiring Schedule 1 other than' those in scope (naming alimony and an IRA deduction among others), so within scope they are zero and line 3 is the printed total.

### 4 — Subtract line 3 from line 2
Status: **MATCH**

Model: The worksheet says 'Subtract line 3 from line 2.'

### 5 — Enter the amount shown below for your filing status. Single, head of household, or qualify
Status: **MISMATCH**

Restated: Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.base_joint ($170,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.base_other ($85,000)"]

Model: The worksheet gives $85,000 for single, head of household or qualifying surviving spouse and $170,000 for married filing jointly, and the restatement matches those. It also enters $0 for married filing separately, which lets an MFS filer compute a partial or full deduction. The IRS instead says the deduction applies only if 'Your filing status is any status except married filing separately.'

Ruling: representation; project retained. A married filer filing separately cannot take the deduction, and the project gives zero for that status on Schedule 1 line 21 (sli.eligible tests the filing status and sli.allowed is zero), so the zero on line 5 for that status changes nothing; the line itself is shown only because the project figures every line.

### 6 — Subtract line 5 from line 4
Status: **MATCH**

Model: For 'Yes' the worksheet says 'Subtract line 5 from line 4.' For 'No' the IRS skips line 6. The restatement still computes a value in that case, but line 8 is gated on the same test, so the result is unaffected.

### 8 — Multiply line 1 by line 7
Status: **MATCH**

Model: The worksheet says 'No. Skip lines 6 and 7, enter -0- on line 8.' For 'Yes' it says divide line 6 by '$15,000 ($30,000 if married filing jointly)', round to at least three places, enter 1.000 if the result is 1.000 or more, then 'Multiply line 1 by line 7.' The restatement follows this.

### 9 — Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on
Status: **MISMATCH**

Restated: Subtract line 8 from line 1. If zero or less, enter -0-.

Model: The arithmetic 'Subtract line 8 from line 1' matches. However, the instructions allow the deduction only if 'You, or your spouse if filing jointly, aren't claimed as a dependent on someone else's... 2025 tax return.' Nothing in the restatement applies this condition, so a filer who is claimed as a dependent would still get a nonzero deduction.

Ruling: representation; restatement accepted. Line 9 is the worksheet's arithmetic, which the restatement gives as printed; the conditions of i1040gi p. 98 ('You can take this deduction only if all of the following apply') are applied after it, on Schedule 1 line 21: sli.eligible requires a status other than married filing separately and sli.claimed false, where sli.claimed asks 'Are you, or your spouse if filing jointly, claimed as a dependent on someone else's ... 2025 tax return?', and sli.allowed enters zero otherwise, which sli.deduction and s1.line21 read. A filer, or a spouse on a joint return, claimed as a dependent gets no deduction.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The worksheet says to 'Enter the total interest you paid in 2025 on qualified student loans... Don't enter more than $2,500', which is the smaller of interest or $2,500. The refusal matches the Exception: 'Use Pub. 970 instead of the worksheet... if you file Form 2555 or 4563, or you exclude income from sources within Puerto Rico.'"
  - key: "2"
    status: MATCH
    reason: "The worksheet says 'Enter the amount from Form 1040 or 1040-SR, line 9.'"
  - key: "3"
    status: MISMATCH
    reason: "The IRS says 'Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25.' The restatement adds only lines 11, 13, 15, 16 and 17, leaving out lines 12, 14, 18, 19, 20, 23 and 25."
  - key: "4"
    status: MATCH
    reason: "The worksheet says 'Subtract line 3 from line 2.'"
  - key: "5"
    status: MISMATCH
    reason: "The worksheet gives $85,000 for single, head of household or qualifying surviving spouse and $170,000 for married filing jointly, and the restatement matches those. It also enters $0 for married filing separately, which lets an MFS filer compute a partial or full deduction. The IRS instead says the deduction applies only if 'Your filing status is any status except married filing separately.'"
  - key: "6"
    status: MATCH
    reason: "For 'Yes' the worksheet says 'Subtract line 5 from line 4.' For 'No' the IRS skips line 6. The restatement still computes a value in that case, but line 8 is gated on the same test, so the result is unaffected."
  - key: "8"
    status: MATCH
    reason: "The worksheet says 'No. Skip lines 6 and 7, enter -0- on line 8.' For 'Yes' it says divide line 6 by '$15,000 ($30,000 if married filing jointly)', round to at least three places, enter 1.000 if the result is 1.000 or more, then 'Multiply line 1 by line 7.' The restatement follows this."
  - key: "9"
    status: MISMATCH
    reason: "The arithmetic 'Subtract line 8 from line 1' matches. However, the instructions allow the deduction only if 'You, or your spouse if filing jointly, aren't claimed as a dependent on someone else's... 2025 tax return.' Nothing in the restatement applies this condition, so a filer who is claimed as a dependent would still get a nonzero deduction."
```
```
