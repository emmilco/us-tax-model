# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 56918cfb5828357c522e3d56a85b74d12c9b9b29d976fd6f8dca2f159d1f499b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | c990f4de1e73a1429110d78877304823bc730f52f307705e1742fd3d361d177b |
| lines judged | 10 |
| match / mismatch / unclear / missing | 7 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: IRS line 1 says to enter the total pension or annuity payments from Form 1099-R box 1; the helper supplies that box 1 gross distribution.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MATCH**

Model: IRS line 2 says to enter your cost in the plan at the annuity starting date; the helper supplies that cost, including possible box 9b net investment.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: The true branch matches, but for non-joint annuities the Table 1 helper uses only the after-November 18, 1996 numbers; IRS Table 1 separately provides a before-November 19, 1996 column (for example, 300 rather than 360 for age 55 or under).

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, Table 1 for Line 3: "AND your annuity starting date was-- before November 19, 1996, enter on line 3... after November 18, 1996, enter on line 3... 300 360 260 310 240 260 170 210 120 160". The before-November-19-1996 column is screened: retirement.special refuses ("Form 1099-R special cases") a distribution involving "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996", and retirement.annuity, which routes to the worksheet, asks for "an annuity starting date after November 18, 1996". The refused set includes the p. 30 condition 1 annuities ("Your annuity starting date was after July 1, 1986, and you used this method last year") that start before November 19, 1996; that is a documented scope reduction, not a computation error. Same as the archived rulings, rechecked against the current rendering.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: IRS line 5 says to multiply line 4 by the number of months for which this year's payments were made; the restatement does that.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MATCH**

Model: IRS line 6 says to enter the amount recovered tax free in years after 1986, using line 10 of last year's worksheet if applicable; the helper matches.

### (SMW 7) — Subtract line 6 from line 2
Status: **MATCH**

Model: IRS line 7 says to subtract line 6 from line 2; the restatement subtracts SMW 6 from SMW 2.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: IRS line 5 says that if your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8; the restatement always computes the smaller of line 5 or line 7.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6". A starting date before 1987 is before November 19, 1996, so every such annuity with after-tax cost is refused by retirement.special ("a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996") and retirement.annuity requires a start after November 18, 1996; on every completed return the "Otherwise" branch applies and line 8 is "the smaller of line 5 or line 7". Same as the archived rulings, rechecked.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: IRS line 9 says to subtract line 8 from line 1, not below zero; the restatement does that.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: IRS line 10 asks whether the annuity starting date was before 1987 and says Yes means STOP and do not complete the rest of the worksheet; the restatement unconditionally adds lines 6 and 8.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 10: "Was your annuity starting date before 1987? Yes. Do not complete the rest of this worksheet. STOP No. Add lines 6 and 8." The Yes branch is unreachable: annuities with after-tax cost starting before November 19, 1996 (so before 1987) are refused by retirement.special, and retirement.annuity requires a start after November 18, 1996, so the question is answered No on every completed return and lines 10 and 11 are figured, as the line 10 cite records. The skipped-line rule is therefore not engaged. Same as the archived rulings, rechecked.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MATCH**

Model: IRS line 11 says to subtract line 10 from line 2; the restatement subtracts SMW 10 from SMW 2.

## Raw response

```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "IRS line 1 says to enter the total pension or annuity payments from Form 1099-R box 1; the helper supplies that box 1 gross distribution."
  - key: "(SMW 2)"
    status: MATCH
    reason: "IRS line 2 says to enter your cost in the plan at the annuity starting date; the helper supplies that cost, including possible box 9b net investment."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "The true branch matches, but for non-joint annuities the Table 1 helper uses only the after-November 18, 1996 numbers; IRS Table 1 separately provides a before-November 19, 1996 column (for example, 300 rather than 360 for age 55 or under)."
  - key: "(SMW 5)"
    status: MATCH
    reason: "IRS line 5 says to multiply line 4 by the number of months for which this year's payments were made; the restatement does that."
  - key: "(SMW 6)"
    status: MATCH
    reason: "IRS line 6 says to enter the amount recovered tax free in years after 1986, using line 10 of last year's worksheet if applicable; the helper matches."
  - key: "(SMW 7)"
    status: MATCH
    reason: "IRS line 7 says to subtract line 6 from line 2; the restatement subtracts SMW 6 from SMW 2."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "IRS line 5 says that if your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8; the restatement always computes the smaller of line 5 or line 7."
  - key: "(SMW 9)"
    status: MATCH
    reason: "IRS line 9 says to subtract line 8 from line 1, not below zero; the restatement does that."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "IRS line 10 asks whether the annuity starting date was before 1987 and says Yes means STOP and do not complete the rest of the worksheet; the restatement unconditionally adds lines 6 and 8."
  - key: "(SMW 11)"
    status: MATCH
    reason: "IRS line 11 says to subtract line 10 from line 2; the restatement subtracts SMW 10 from SMW 2."
```
