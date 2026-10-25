# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9b0cdf8ffd59953053a4eaf480a246e08615e56602515368bec49e62205b40c5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 46eb05f70d9f6b0f017adb7b777d93d1c92b6a36f5140c095e9bab8cd545ed25 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 3 / 7 / 0 / 0 |
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

Model: Matches worksheet line 1: enter total pension or annuity payments from Form 1099-R box 1.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: The worksheet's before-you-begin note says to 'include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2'; the restatement uses only the cost helper and omits that addition.

Ruling: scope; i1040gi (2025) p.29 worksheet preamble includes any entitled death-benefit exclusion in line2. The retirement.special question expressly screens a death-benefit exclusion; retirement.taxable and retirement.amount_a refuse it, as does retirement.rolled. A supported completed distribution therefore has no such addition and uses after-tax cost. The broader source case is excluded, not model noise; no standalone correctness claim is made on an excluded distribution.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: The Table 1 helper uses only the after-November 18-1996 numbers; IRS Table 1 also has a before-November 19-1996 column, so a pre-November 19, 1996 annuity would use 300/260/240/170/120 rather than 360/310/260/210/160.

Ruling: scope; i1040gi (2025) p.29 Table1 includes an older-annuity column. retirement.special expressly screens an after-tax-cost annuity starting before November19,1996, and retirement.annuity asks whether the start is after November18,1996; retirement.taxable/amount_a refuse the excluded case. Supported Simplified Method distributions therefore use the later column. The missing older column is a documented scope reduction, not an error in that IRS column.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: Matches worksheet line 5: multiply line 4 by the number of months for which this year's payments were made.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MISMATCH**

Restated: Enter the amount from helper "Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)".

Model: IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7'; the restatement still computes line 6 from the recovered-tax-free helper.

Ruling: scope; i1040gi (2025) p.29 worksheet lines5/10 give skip/STOP rules for annuities beginning before1987. retirement.special excludes every after-tax-cost annuity starting before November19,1996, and retirement.taxable/amount_a enforce that screen; the positive annuity interface also requires a later start. Hence no supported completed Simplified Method case reaches the pre1987 regime. Retain the later-start computation; this does not claim the standalone worksheet values match an excluded old annuity or that the IRS skip is absent.

### (SMW 7) — Subtract line 6 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 6) from column (SMW 2).

Model: IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7'; the restatement still subtracts line 6 from line 2.

Ruling: scope; i1040gi (2025) p.29 worksheet lines5/10 give skip/STOP rules for annuities beginning before1987. retirement.special excludes every after-tax-cost annuity starting before November19,1996, and retirement.taxable/amount_a enforce that screen; the positive annuity interface also requires a later start. Hence no supported completed Simplified Method case reaches the pre1987 regime. Retain the later-start computation; this does not claim the standalone worksheet values match an excluded old annuity or that the IRS skip is absent.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement always takes the smaller of line 5 or line 7.

Ruling: scope; i1040gi (2025) p.29 worksheet lines5/10 give skip/STOP rules for annuities beginning before1987. retirement.special excludes every after-tax-cost annuity starting before November19,1996, and retirement.taxable/amount_a enforce that screen; the positive annuity interface also requires a later start. Hence no supported completed Simplified Method case reaches the pre1987 regime. Retain the later-start computation; this does not claim the standalone worksheet values match an excluded old annuity or that the IRS skip is absent.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: Matches worksheet line 9: subtract line 8 from line 1, but not below zero.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: IRS line 10 says 'Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet'; the restatement adds line 6 and line 8 even for a pre-1987 annuity.

Ruling: scope; i1040gi (2025) p.29 worksheet lines5/10 give skip/STOP rules for annuities beginning before1987. retirement.special excludes every after-tax-cost annuity starting before November19,1996, and retirement.taxable/amount_a enforce that screen; the positive annuity interface also requires a later start. Hence no supported completed Simplified Method case reaches the pre1987 regime. Retain the later-start computation; this does not claim the standalone worksheet values match an excluded old annuity or that the IRS skip is absent.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: IRS line 10 says 'Do not complete the rest of this worksheet' when the annuity starting date was before 1987; the restatement still subtracts line 10 from line 2.

Ruling: scope; i1040gi (2025) p.29 worksheet lines5/10 give skip/STOP rules for annuities beginning before1987. retirement.special excludes every after-tax-cost annuity starting before November19,1996, and retirement.taxable/amount_a enforce that screen; the positive annuity interface also requires a later start. Hence no supported completed Simplified Method case reaches the pre1987 regime. Retain the later-start computation; this does not claim the standalone worksheet values match an excluded old annuity or that the IRS skip is absent.

## Raw response

```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Matches worksheet line 1: enter total pension or annuity payments from Form 1099-R box 1."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "The worksheet's before-you-begin note says to 'include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2'; the restatement uses only the cost helper and omits that addition."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "The Table 1 helper uses only the after-November 18-1996 numbers; IRS Table 1 also has a before-November 19-1996 column, so a pre-November 19, 1996 annuity would use 300/260/240/170/120 rather than 360/310/260/210/160."
  - key: "(SMW 5)"
    status: MATCH
    reason: "Matches worksheet line 5: multiply line 4 by the number of months for which this year's payments were made."
  - key: "(SMW 6)"
    status: MISMATCH
    reason: "IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7'; the restatement still computes line 6 from the recovered-tax-free helper."
  - key: "(SMW 7)"
    status: MISMATCH
    reason: "IRS line 5 says 'If your annuity starting date was before 1987, skip lines 6 and 7'; the restatement still subtracts line 6 from line 2."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement always takes the smaller of line 5 or line 7."
  - key: "(SMW 9)"
    status: MATCH
    reason: "Matches worksheet line 9: subtract line 8 from line 1, but not below zero."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "IRS line 10 says 'Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet'; the restatement adds line 6 and line 8 even for a pre-1987 annuity."
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "IRS line 10 says 'Do not complete the rest of this worksheet' when the annuity starting date was before 1987; the restatement still subtracts line 10 from line 2."
```
