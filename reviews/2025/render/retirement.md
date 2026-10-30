# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bde748bdedd036c7e5eef6ba0d68b19dac31e058cd3185dcaba9d65842d98b0b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 9fa70321a0b369d480bb0595a79eddd7e288f01aec30a53bac2cd5cdc8499ac9 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 5 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: Line 1 says "Enter the total pension or annuity payments from Form 1099-R, box 1", and the restatement uses the box 1 gross distribution.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: The input is only the filer's net investment (after-tax contributions), and no refusal excludes the death-benefit case. The worksheet says "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2."

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below." retirement.special asks about "a death benefit exclusion" and refuses the entry's taxable amount, so line 2 is the cost alone on every entry the worksheet reaches. The new hiding condition retirement.smw_shown was checked by evaluating cases (IRA with the pension answers unasked, cost recovered, fully taxable, cost left): it hides the worksheet exactly where i1040gi pp. 28-30 skip it. Same model reading as earlier rounds. Project stands on the English.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: The prior-year branch and the Table 2 bands match. The Table 1 branch uses only the post-November 18, 1996 column (360/310/260/210/160) and does not refuse other cases, but Table 1 has a separate column for annuity starting dates "before November 19, 1996" (300, 260, 240, 170, 120).

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: Table 1 for Line 3 has "before November 19, 1996" and "after November 18, 1996" columns. retirement.special refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996", so only the after-November-18-1996 column is reached. The new hiding condition retirement.smw_shown was checked by evaluating cases (IRA with the pension answers unasked, cost recovered, fully taxable, cost left): it hides the worksheet exactly where i1040gi pp. 28-30 skip it. Same model reading as earlier rounds. Project stands on the English.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: Line 5 says "Multiply line 4 by the number of months for which this year's payments were made", which the restatement does.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MATCH**

Model: Line 6 says "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet", which the input describes. The pre-1987 skip of this line is not handled, and that affects line 8.

### (SMW 7) — Subtract line 6 from line 2
Status: **MATCH**

Model: Line 7 says "Subtract line 6 from line 2", which the restatement does.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: The restatement always takes the smaller of line 5 or line 7, with no pre-1987 branch or refusal. Line 5 says "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8."

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown, so the before-1987 branch and STOP are never reached. The new hiding condition retirement.smw_shown was checked by evaluating cases (IRA with the pension answers unasked, cost recovered, fully taxable, cost left): it hides the worksheet exactly where i1040gi pp. 28-30 skip it. Same model reading as earlier rounds. Project stands on the English.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: Line 9 says "Subtract line 8 from line 1. Enter the result, but not less than zero", which the restatement does with a floor at zero.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: The restatement always adds lines 6 and 8. Line 10 asks "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet", and adds lines 6 and 8 only on "No."

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown, so the before-1987 branch and STOP are never reached. The new hiding condition retirement.smw_shown was checked by evaluating cases (IRA with the pension answers unasked, cost recovered, fully taxable, cost left): it hides the worksheet exactly where i1040gi pp. 28-30 skip it. Same model reading as earlier rounds. Project stands on the English.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: The restatement always computes line 2 minus line 10. For an annuity starting date before 1987, line 10 says "STOP Do not complete the rest of this worksheet", so line 11 is not completed, and the program has no refusal for that case.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown, so the before-1987 branch and STOP are never reached. The new hiding condition retirement.smw_shown was checked by evaluating cases (IRA with the pension answers unasked, cost recovered, fully taxable, cost left): it hides the worksheet exactly where i1040gi pp. 28-30 skip it. Same model reading as earlier rounds. Project stands on the English.

## Raw response

```yaml
```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Line 1 says \"Enter the total pension or annuity payments from Form 1099-R, box 1\", and the restatement uses the box 1 gross distribution."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "The input is only the filer's net investment (after-tax contributions), and no refusal excludes the death-benefit case. The worksheet says \"If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2.\""
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "The prior-year branch and the Table 2 bands match. The Table 1 branch uses only the post-November 18, 1996 column (360/310/260/210/160) and does not refuse other cases, but Table 1 has a separate column for annuity starting dates \"before November 19, 1996\" (300, 260, 240, 170, 120)."
  - key: "(SMW 5)"
    status: MATCH
    reason: "Line 5 says \"Multiply line 4 by the number of months for which this year's payments were made\", which the restatement does."
  - key: "(SMW 6)"
    status: MATCH
    reason: "Line 6 says \"Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet\", which the input describes. The pre-1987 skip of this line is not handled, and that affects line 8."
  - key: "(SMW 7)"
    status: MATCH
    reason: "Line 7 says \"Subtract line 6 from line 2\", which the restatement does."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "The restatement always takes the smaller of line 5 or line 7, with no pre-1987 branch or refusal. Line 5 says \"If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8.\""
  - key: "(SMW 9)"
    status: MATCH
    reason: "Line 9 says \"Subtract line 8 from line 1. Enter the result, but not less than zero\", which the restatement does with a floor at zero."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "The restatement always adds lines 6 and 8. Line 10 asks \"Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet\", and adds lines 6 and 8 only on \"No.\""
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "The restatement always computes line 2 minus line 10. For an annuity starting date before 1987, line 10 says \"STOP Do not complete the rest of this worksheet\", so line 11 is not completed, and the program has no refusal for that case."
```
```
