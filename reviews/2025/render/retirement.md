# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 256d42ace74eaed69b4310797b405f5ee3a7af93ac247434d960fa775a8d9ccf |
| lines judged | 8 |
| match / mismatch / unclear / missing | 5 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: Line 1 says "Enter the total pension or annuity payments from Form 1099-R, box 1". The restatement enters gross distribution from box 1.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: The input is only cost/net investment (box 9b). It leaves out the worksheet's instruction: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2." No refusal covers that case.

Ruling: covered by a screen; project retained. A death benefit exclusion is on retirement.special ('a death benefit exclusion'), which refuses the distribution's lines 4a to 5b.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: The last-year branch and the Table 2 amounts match. Table 1, however, only uses the column "after November 18, 1996" (360/310/260/210/160). It leaves out the column "before November 19, 1996, enter on line 3... 300, 260, 240, 170, 120", and no refusal excludes those annuity starting dates.

Ruling: covered by a screen; project retained. The Simplified Method question (retirement.annuity) asks for an annuity starting date after November 18, 1996, and retirement.special refuses a pension or annuity with after-tax cost 'whose annuity starting date was before November 19, 1996', so only the after-November-18-1996 column is reached.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: Line 5 says "Multiply line 4 by the number of months for which this year's payments were made", and the restatement does the same.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MATCH**

Model: Line 6 says "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet." The input says the same.

### (SMW 7) — Subtract line 6 from line 2
Status: **MATCH**

Model: Line 7 says "Subtract line 6 from line 2", and the restatement does the same.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: It always enters the smaller of line 5 or line 7. The IRS text says "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount [line 5] on line 8." The program has no condition and no refusal for pre-1987 starting dates.

Ruling: covered by a screen; project retained. A starting date before 1987 is before November 19, 1996, so it is refused by retirement.special and never reaches the worksheet.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: Line 9 says "Subtract line 8 from line 1. Enter the result, but not less than zero", and the restatement does the same.

## Raw response

```yaml
```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Line 1 says \"Enter the total pension or annuity payments from Form 1099-R, box 1\". The restatement enters gross distribution from box 1."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "The input is only cost/net investment (box 9b). It leaves out the worksheet's instruction: \"If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2.\" No refusal covers that case."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "The last-year branch and the Table 2 amounts match. Table 1, however, only uses the column \"after November 18, 1996\" (360/310/260/210/160). It leaves out the column \"before November 19, 1996, enter on line 3... 300, 260, 240, 170, 120\", and no refusal excludes those annuity starting dates."
  - key: "(SMW 5)"
    status: MATCH
    reason: "Line 5 says \"Multiply line 4 by the number of months for which this year's payments were made\", and the restatement does the same."
  - key: "(SMW 6)"
    status: MATCH
    reason: "Line 6 says \"Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet.\" The input says the same."
  - key: "(SMW 7)"
    status: MATCH
    reason: "Line 7 says \"Subtract line 6 from line 2\", and the restatement does the same."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "It always enters the smaller of line 5 or line 7. The IRS text says \"If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount [line 5] on line 8.\" The program has no condition and no refusal for pre-1987 starting dates."
  - key: "(SMW 9)"
    status: MATCH
    reason: "Line 9 says \"Subtract line 8 from line 1. Enter the result, but not less than zero\", and the restatement does the same."
```
```
