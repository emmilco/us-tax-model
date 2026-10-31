# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bde748bdedd036c7e5eef6ba0d68b19dac31e058cd3185dcaba9d65842d98b0b |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 3530a2d76968f83f6f9da75f55f43d2d25dcba051419544efd298f9c7f212e69 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 3 / 7 / 0 / 0 |
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

Model: Worksheet line 1 says "Enter the total pension or annuity payments from Form 1099-R, box 1", which is the box 1 input the program uses.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: The input covers only cost (net investment), and no refusal excludes the case where the worksheet says "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2". The value would be understated for those filers.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below." retirement.special still asks about "a death benefit exclusion" and refuses the entry's taxable amount (retirement.taxable and retirement.rolled), so line 2 is the cost alone on every entry the worksheet reaches. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: The carryover from last year and Table 2 match, but the program always uses the later Table 1 column (360/310/260/210/160). Table 1 gives different numbers for an annuity starting date "before November 19, 1996" (300/260/240/170/120), and no refusal excludes those dates.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: Table 1 for Line 3 has "before November 19, 1996" (300, 260, 240, 170, 120) and "after November 18, 1996" (360, 310, 260, 210, 160) columns. retirement.special still refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996", so only the after-November-18-1996 column is reached. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: This restates "Multiply line 4 by the number of months for which this year's payments were made". The pre-1987 skip instruction on this line affects lines 6 through 8, not line 5's value.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MISMATCH**

Restated: Enter the amount from helper "Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)".

Model: The amount matches the line's wording, but the restatement is reported for every completed worksheet. Line 5 says "If your annuity starting date was before 1987, skip lines 6 and 7", and no gate or refusal excludes those dates.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special still refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown (an annuity with cost left), so the before-1987 skip and STOP are never reached. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 7) — Subtract line 6 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 6) from column (SMW 2).

Model: The subtraction matches "Subtract line 6 from line 2", but the line is computed for every completed worksheet. Line 5 says "If your annuity starting date was before 1987, skip lines 6 and 7", and no gate or refusal excludes those dates.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special still refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown (an annuity with cost left), so the before-1987 skip and STOP are never reached. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: The restatement always takes the smaller of lines 5 and 7. For a pre-1987 starting date, line 5 instead says to "skip lines 6 and 7 and enter this amount on line 8", which can change the value, and no refusal excludes this case.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special still refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown (an annuity with cost left), so the before-1987 skip and STOP are never reached. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: This restates "Subtract line 8 from line 1. Enter the result, but not less than zero". Any pre-1987 error here comes from line 8, not from this line's own computation.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: The sum matches "Add lines 6 and 8", but only for the "No" answer to "Was your annuity starting date before 1987?". The "Yes" answer says "STOP Do not complete the rest of this worksheet", and the restatement has no such gate or refusal.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special still refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown (an annuity with cost left), so the before-1987 skip and STOP are never reached. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: The subtraction matches "Subtract line 10 from line 2", but the line is computed for every completed worksheet. Line 10 says that for a starting date before 1987, "STOP Do not complete the rest of this worksheet", and no gate or refusal excludes those dates.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8"; line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet." retirement.special still refuses every annuity with after-tax cost whose starting date was before November 19, 1996 (so every pre-1987 annuity), and the worksheet is shown only under retirement.smw_shown (an annuity with cost left), so the before-1987 skip and STOP are never reached. Re-checked against the current forms/2025/retirement.yaml: BUG-0243 only added items to the retirement.special list; the two items relied on here are unchanged and the worksheet lines are unchanged. Same model reading as earlier rounds. Project stands on the English.

## Raw response

```yaml
```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Worksheet line 1 says \"Enter the total pension or annuity payments from Form 1099-R, box 1\", which is the box 1 input the program uses."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "The input covers only cost (net investment), and no refusal excludes the case where the worksheet says \"If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2\". The value would be understated for those filers."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "The carryover from last year and Table 2 match, but the program always uses the later Table 1 column (360/310/260/210/160). Table 1 gives different numbers for an annuity starting date \"before November 19, 1996\" (300/260/240/170/120), and no refusal excludes those dates."
  - key: "(SMW 5)"
    status: MATCH
    reason: "This restates \"Multiply line 4 by the number of months for which this year's payments were made\". The pre-1987 skip instruction on this line affects lines 6 through 8, not line 5's value."
  - key: "(SMW 6)"
    status: MISMATCH
    reason: "The amount matches the line's wording, but the restatement is reported for every completed worksheet. Line 5 says \"If your annuity starting date was before 1987, skip lines 6 and 7\", and no gate or refusal excludes those dates."
  - key: "(SMW 7)"
    status: MISMATCH
    reason: "The subtraction matches \"Subtract line 6 from line 2\", but the line is computed for every completed worksheet. Line 5 says \"If your annuity starting date was before 1987, skip lines 6 and 7\", and no gate or refusal excludes those dates."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "The restatement always takes the smaller of lines 5 and 7. For a pre-1987 starting date, line 5 instead says to \"skip lines 6 and 7 and enter this amount on line 8\", which can change the value, and no refusal excludes this case."
  - key: "(SMW 9)"
    status: MATCH
    reason: "This restates \"Subtract line 8 from line 1. Enter the result, but not less than zero\". Any pre-1987 error here comes from line 8, not from this line's own computation."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "The sum matches \"Add lines 6 and 8\", but only for the \"No\" answer to \"Was your annuity starting date before 1987?\". The \"Yes\" answer says \"STOP Do not complete the rest of this worksheet\", and the restatement has no such gate or refusal."
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "The subtraction matches \"Subtract line 10 from line 2\", but the line is computed for every completed worksheet. Line 10 says that for a starting date before 1987, \"STOP Do not complete the rest of this worksheet\", and no gate or refusal excludes those dates."
```
```
