# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9b0cdf8ffd59953053a4eaf480a246e08615e56602515368bec49e62205b40c5 |
| subject sha256 | 46eb05f70d9f6b0f017adb7b777d93d1c92b6a36f5140c095e9bab8cd545ed25 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 5 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: Line 1 says "Enter the total pension or annuity payments from Form 1099-R, box 1", and the restatement enters the box 1 gross distribution.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: The input covers only net investment and after-tax contributions. It leaves out the death benefit exclusion that the worksheet says to add to line 2: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below." No refusal excludes this case.

Ruling: covered by a screen; project retained (as the prior rulings). i1040gi p. 29, Simplified Method Worksheet: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below." A death benefit exclusion is on retirement.special ('a death benefit exclusion'), which refuses the distribution's lines 4a to 5b, so line 2 is the cost alone for every annuity that reaches the worksheet. No change.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: The choice between last year's line 4 and the Table 1/Table 2 division matches the Note and lines 3–4. However, the Table 1 branch always uses the "after November 18, 1996" column (360/310/260/210/160). The IRS table also has a column for starting dates "before November 19, 1996" (300/260/240/170/120), and no refusal excludes those dates.

Ruling: covered by a screen; project retained (as the prior rulings). The Simplified Method question (retirement.annuity) asks for an annuity starting date after November 18, 1996, and retirement.special refuses a pension or annuity with after-tax cost 'whose annuity starting date was before November 19, 1996' (so before 1987 too), so only Table 1's column for a starting date after November 18, 1996 (i1040gi p. 29, Table 1 for Line 3, 360/310/260/210/160) is reached; the 'before November 19, 1996' column (300/260/240/170/120) never applies. No change.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: Line 5 says "Multiply line 4 by the number of months for which this year's payments were made", and the restatement does that.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MATCH**

Model: Line 6 says "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet", and the input says the same.

### (SMW 7) — Subtract line 6 from line 2
Status: **MATCH**

Model: Line 7 says "Subtract line 6 from line 2", and the restatement does that.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: The restatement always takes the smaller of line 5 and line 7. The IRS line 5 says "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8", so for those dates line 8 is line 5 alone. The program has no condition or refusal for pre-1987 starting dates.

Ruling: covered by a screen; project retained (as the prior rulings). The Simplified Method question (retirement.annuity) asks for an annuity starting date after November 18, 1996, and retirement.special refuses a pension or annuity with after-tax cost 'whose annuity starting date was before November 19, 1996' (so before 1987 too). Line 5's direction, "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8" (i1040gi p. 29), therefore never applies, and line 8 is the smaller of lines 5 and 7. No change.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: Line 9 says "Subtract line 8 from line 1. Enter the result, but not less than zero", and the restatement does that with a floor of zero.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: The restatement always adds lines 6 and 8. The IRS line 10 says "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet", and the program has no condition or refusal for pre-1987 starting dates.

Ruling: covered by a screen; project retained (as the prior rulings). The Simplified Method question (retirement.annuity) asks for an annuity starting date after November 18, 1996, and retirement.special refuses a pension or annuity with after-tax cost 'whose annuity starting date was before November 19, 1996' (so before 1987 too). Line 10's question, "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet" (i1040gi p. 29), is answered No for every annuity that reaches the worksheet, and its No branch is "Add lines 6 and 8". No change.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: The subtraction of line 10 from line 2 matches, but it is always computed. Under line 10, "Yes. STOP Do not complete the rest of this worksheet" applies to annuity starting dates before 1987, and no condition or refusal handles that case.

Ruling: covered by a screen; project retained (as the prior rulings). The Simplified Method question (retirement.annuity) asks for an annuity starting date after November 18, 1996, and retirement.special refuses a pension or annuity with after-tax cost 'whose annuity starting date was before November 19, 1996' (so before 1987 too). Line 10's question, "Was your annuity starting date before 1987?" (i1040gi p. 29), is answered No for every annuity that reaches the worksheet, so its STOP never applies and line 11 is always figured, as the No branch says. No change.

## Raw response

```yaml
```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Line 1 says \"Enter the total pension or annuity payments from Form 1099-R, box 1\", and the restatement enters the box 1 gross distribution."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "The input covers only net investment and after-tax contributions. It leaves out the death benefit exclusion that the worksheet says to add to line 2: \"If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below.\" No refusal excludes this case."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "The choice between last year's line 4 and the Table 1/Table 2 division matches the Note and lines 3–4. However, the Table 1 branch always uses the \"after November 18, 1996\" column (360/310/260/210/160). The IRS table also has a column for starting dates \"before November 19, 1996\" (300/260/240/170/120), and no refusal excludes those dates."
  - key: "(SMW 5)"
    status: MATCH
    reason: "Line 5 says \"Multiply line 4 by the number of months for which this year's payments were made\", and the restatement does that."
  - key: "(SMW 6)"
    status: MATCH
    reason: "Line 6 says \"Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet\", and the input says the same."
  - key: "(SMW 7)"
    status: MATCH
    reason: "Line 7 says \"Subtract line 6 from line 2\", and the restatement does that."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "The restatement always takes the smaller of line 5 and line 7. The IRS line 5 says \"If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8\", so for those dates line 8 is line 5 alone. The program has no condition or refusal for pre-1987 starting dates."
  - key: "(SMW 9)"
    status: MATCH
    reason: "Line 9 says \"Subtract line 8 from line 1. Enter the result, but not less than zero\", and the restatement does that with a floor of zero."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "The restatement always adds lines 6 and 8. The IRS line 10 says \"Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet\", and the program has no condition or refusal for pre-1987 starting dates."
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "The subtraction of line 10 from line 2 matches, but it is always computed. Under line 10, \"Yes. STOP Do not complete the rest of this worksheet\" applies to annuity starting dates before 1987, and no condition or refusal handles that case."
```
```
