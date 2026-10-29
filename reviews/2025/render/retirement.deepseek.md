# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | cae1f00cc07c036b6a79912ac8e3e77ac6e114871c026e283fca4c0db46afe14 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | bfe84c9e2c6c9d038c1382f4c8d345389430c6bd0e03a2cd9d4bd8c100ae2380 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 6 / 4 / 0 / 0 |
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

Model: The restatement uses Form 1099-R box 1, matching the IRS instruction to enter total pension or annuity payments from box 1.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: IRS says to include any death benefit exclusion (up to $5,000) in the amount entered on line 2 for a beneficiary of a deceased employee who died before August 21, 1996; the helper defines only cost/net investment and omits that addition.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below." retirement.special asks about "a death benefit exclusion" and refuses the entry's lines 4a to 5b (retirement.rolled and retirement.taxable), so line 2 is the cost alone on every entry that reaches the worksheet. The model looked for the refusal on line 2. Same model reading as rounds 1 and 2. Project stands.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: Table 1 has a before-November-19-1996 column (300, 260, 240, 170, 120), but the helper uses only the after-November-18-1996 numbers (360, 310, 260, 210, 160); no refusal covers pre-November-19-1996 annuities.

Ruling: scope; i1040gi p. 29, Table 1 for Line 3, "before November 19, 1996" (300, 260, 240, 170, 120) and "after November 18, 1996" (360, 310, 260, 210, 160). retirement.special refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996" (so every annuity starting before 1987), and retirement.annuity, which routes an entry to the worksheet, asks for "an annuity starting date after November 18, 1996", so only the after-November-18-1996 column is reached. Same model reading as rounds 1 and 2. Project stands.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MISMATCH**

Restated: Multiply column (SMW 4) by the number on helper "Number of months for which this year's payments were made".

Model: IRS line 5 adds: 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6'; the restatement omits this condition.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6." retirement.special refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996" (so every annuity starting before 1987), and retirement.annuity, which routes an entry to the worksheet, asks for "an annuity starting date after November 18, 1996"; on every entry that reaches the worksheet the Otherwise branch applies and line 8 is the smaller of lines 5 and 7. The model raised on line 5 the branch it raised on line 8 in round 2. Project stands.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MATCH**

Model: The restatement matches the IRS line 6 instruction to enter the amount recovered tax free in years after 1986, using last year's line 10 if applicable.

### (SMW 7) — Subtract line 6 from line 2
Status: **MATCH**

Model: The restatement subtracts line 6 from line 2, matching the IRS line 7 instruction.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MATCH**

Model: The restatement enters the smaller of line 5 or line 7, matching the IRS line 8 instruction.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: The restatement subtracts line 8 from line 1 and floors the result at zero, matching the IRS line 9 instruction.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: IRS line 10 asks 'Was your annuity starting date before 1987?' and says if Yes, 'STOP Do not complete the rest of this worksheet'; the restatement unconditionally adds lines 6 and 8.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 10: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet. No. Add lines 6 and 8." retirement.special refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996" (so every annuity starting before 1987), and retirement.annuity, which routes an entry to the worksheet, asks for "an annuity starting date after November 18, 1996", so the question is answered No on every entry that reaches the worksheet and its No branch is the project's sum; the skipped-line rule is not engaged. Same model reading as rounds 1 and 2. Project stands.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MATCH**

Model: The restatement subtracts line 10 from line 2, matching the IRS line 11 instruction.

## Raw response

```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "The restatement uses Form 1099-R box 1, matching the IRS instruction to enter total pension or annuity payments from box 1."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "IRS says to include any death benefit exclusion (up to $5,000) in the amount entered on line 2 for a beneficiary of a deceased employee who died before August 21, 1996; the helper defines only cost/net investment and omits that addition."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "Table 1 has a before-November-19-1996 column (300, 260, 240, 170, 120), but the helper uses only the after-November-18-1996 numbers (360, 310, 260, 210, 160); no refusal covers pre-November-19-1996 annuities."
  - key: "(SMW 5)"
    status: MISMATCH
    reason: "IRS line 5 adds: 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6'; the restatement omits this condition."
  - key: "(SMW 6)"
    status: MATCH
    reason: "The restatement matches the IRS line 6 instruction to enter the amount recovered tax free in years after 1986, using last year's line 10 if applicable."
  - key: "(SMW 7)"
    status: MATCH
    reason: "The restatement subtracts line 6 from line 2, matching the IRS line 7 instruction."
  - key: "(SMW 8)"
    status: MATCH
    reason: "The restatement enters the smaller of line 5 or line 7, matching the IRS line 8 instruction."
  - key: "(SMW 9)"
    status: MATCH
    reason: "The restatement subtracts line 8 from line 1 and floors the result at zero, matching the IRS line 9 instruction."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "IRS line 10 asks 'Was your annuity starting date before 1987?' and says if Yes, 'STOP Do not complete the rest of this worksheet'; the restatement unconditionally adds lines 6 and 8."
  - key: "(SMW 11)"
    status: MATCH
    reason: "The restatement subtracts line 10 from line 2, matching the IRS line 11 instruction."
```
