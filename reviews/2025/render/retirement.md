# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0ee876b574177fd661e52dc8af1c088464122d498bb2db9e8eea118a820ada15 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 5 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: Line 1 says "Enter the total pension or annuity payments from Form 1099-R, box 1", which is what the restatement enters.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: Line 2 is the cost in the plan, but the worksheet also says "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2." The input leaves this out and no refusal covers it, so line 2 comes out too low for these beneficiaries.

Ruling: covered by a screen; project retained. A death benefit exclusion is on retirement.special ('a death benefit exclusion'), which refuses the distribution's lines 4a to 5b.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: Table 1 has a separate column for an annuity starting date "before November 19, 1996" with the numbers 300/260/240/170/120. The program only uses the "after November 18, 1996" numbers (360/310/260/210/160), and no refusal excludes the earlier dates. The rest matches: using last year's line 4, the choice between Table 2 and Table 1, and the age brackets.

Ruling: covered by a screen; project retained. The Simplified Method question (retirement.annuity) asks for an annuity starting date after November 18, 1996, and retirement.special refuses a pension or annuity with after-tax cost 'whose annuity starting date was before November 19, 1996', so only the after-November-18-1996 column is reached.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: Line 5 says "Multiply line 4 by the number of months for which this year's payments were made", which is what the restatement does. Its skip instruction for pre-1987 starting dates is a problem for line 8, covered there.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MATCH**

Model: Line 6 says "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet", and the restatement enters that amount.

### (SMW 7) — Subtract line 6 from line 2
Status: **MATCH**

Model: Line 7 says "Subtract line 6 from line 2", which is what the restatement does.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: Line 5 says "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8." The program always takes the smaller of line 5 and line 7, with no input or refusal for a pre-1987 starting date, so the result differs when line 7 is smaller.

Ruling: covered by a screen; project retained. A starting date before 1987 is before November 19, 1996, so it is refused by retirement.special and never reaches the worksheet.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: Line 9 says "Subtract line 8 from line 1. Enter the result, but not less than zero", which is what the restatement does.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: Line 10 asks "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." The program always adds lines 6 and 8 and has no pre-1987 condition or refusal.

Ruling: covered by a screen; project retained. Line 10's question, 'Was your annuity starting date before 1987?', is answered No for every annuity that reaches the worksheet: the Simplified Method question (retirement.annuity) asks for a starting date after November 18, 1996, and retirement.special refuses an annuity with after-tax cost whose starting date was before November 19, 1996 (so before 1987 too). Lines 10 and 11 are therefore always figured, as the 'No' branch says.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: The subtraction matches "Subtract line 10 from line 2", but line 10 says that for a starting date before 1987 you should "STOP Do not complete the rest of this worksheet." The program computes line 11 anyway and has no condition for this case.

Ruling: covered by a screen; project retained. Line 10's question, 'Was your annuity starting date before 1987?', is answered No for every annuity that reaches the worksheet: the Simplified Method question (retirement.annuity) asks for a starting date after November 18, 1996, and retirement.special refuses an annuity with after-tax cost whose starting date was before November 19, 1996 (so before 1987 too). Lines 10 and 11 are therefore always figured, as the 'No' branch says.

## Raw response

```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Line 1 says \"Enter the total pension or annuity payments from Form 1099-R, box 1\", which is what the restatement enters."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "Line 2 is the cost in the plan, but the worksheet also says \"If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2.\" The input leaves this out and no refusal covers it, so line 2 comes out too low for these beneficiaries."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "Table 1 has a separate column for an annuity starting date \"before November 19, 1996\" with the numbers 300/260/240/170/120. The program only uses the \"after November 18, 1996\" numbers (360/310/260/210/160), and no refusal excludes the earlier dates. The rest matches: using last year's line 4, the choice between Table 2 and Table 1, and the age brackets."
  - key: "(SMW 5)"
    status: MATCH
    reason: "Line 5 says \"Multiply line 4 by the number of months for which this year's payments were made\", which is what the restatement does. Its skip instruction for pre-1987 starting dates is a problem for line 8, covered there."
  - key: "(SMW 6)"
    status: MATCH
    reason: "Line 6 says \"Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet\", and the restatement enters that amount."
  - key: "(SMW 7)"
    status: MATCH
    reason: "Line 7 says \"Subtract line 6 from line 2\", which is what the restatement does."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "Line 5 says \"If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8.\" The program always takes the smaller of line 5 and line 7, with no input or refusal for a pre-1987 starting date, so the result differs when line 7 is smaller."
  - key: "(SMW 9)"
    status: MATCH
    reason: "Line 9 says \"Subtract line 8 from line 1. Enter the result, but not less than zero\", which is what the restatement does."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "Line 10 asks \"Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet.\" The program always adds lines 6 and 8 and has no pre-1987 condition or refusal."
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "The subtraction matches \"Subtract line 10 from line 2\", but line 10 says that for a starting date before 1987 you should \"STOP Do not complete the rest of this worksheet.\" The program computes line 11 anyway and has no condition for this case."
```
