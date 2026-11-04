# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | c5e34724f5597f8a35f063a54a63e06a53baf969a2fd45067f9294bef26cc7ae |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | ad8ba2fc024442ddf9afa0bcfcb8434b01a39ce4a9122f43caecf6436a1a5d87 |
| lines judged | 10 |
| match / mismatch / unclear / missing | 4 / 6 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p575 | None | 12, 23, 34, 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 12, 23, 34, 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| p590b | 2025 | 28 | pages named by another document's citation | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: Restates Form 1099-R box 1 as the total pension or annuity payments for line 1.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MATCH**

Model: Restates the cost in the plan at the annuity starting date, including the survivor rule from the instructions.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: Table 1 has separate numbers for an annuity starting date before November 19, 1996 (300/260/240/170/120) and after November 18, 1996 (360/310/260/210/160); the restatement uses only the after-November-18-1996 numbers.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, Table 1 for Line 3, which has "before November 19, 1996" (300, 260, 240, 170, 120) and "after November 18, 1996" (360, 310, 260, 210, 160) columns. retirement.special still refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996", and retirement.annuity requires a starting date after November 18, 1996, so only the after-November-18-1996 column is reached. Re-checked against the current forms/2025/retirement.yaml this round: BUG-0393 added the qualified disaster recovery distribution (Form 8915-F) to retirement.special and reworded retirement.rollover and retirement.exception; retirement.special still names "a death benefit exclusion" and "a pension or annuity in which you have after-tax cost whose annuity starting date ... was before November 19, 1996", and the worksheet expressions are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: Multiplies line 4 by the number of months for which this year's payments were made, as the worksheet says.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MISMATCH**

Restated: Enter the amount from helper "Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)".

Model: The worksheet says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always computes line 6.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 6 is the only one reached. Re-checked against the current forms/2025/retirement.yaml this round: BUG-0393 added the qualified disaster recovery distribution (Form 8915-F) to retirement.special and reworded retirement.rollover and retirement.exception; retirement.special still names "a death benefit exclusion" and "a pension or annuity in which you have after-tax cost whose annuity starting date ... was before November 19, 1996", and the worksheet expressions are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 7) — Subtract line 6 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 6) from column (SMW 2).

Model: The worksheet says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always subtracts line 6 from line 2.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 7 is the only one reached. Re-checked against the current forms/2025/retirement.yaml this round: BUG-0393 added the qualified disaster recovery distribution (Form 8915-F) to retirement.special and reworded retirement.rollover and retirement.exception; retirement.special still names "a death benefit exclusion" and "a pension or annuity in which you have after-tax cost whose annuity starting date ... was before November 19, 1996", and the worksheet expressions are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: For a pre-1987 annuity starting date the worksheet says to enter the line 5 amount on line 8, not the smaller of line 5 or line 7 as the restatement does.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 8 is the only one reached. Re-checked against the current forms/2025/retirement.yaml this round: BUG-0393 added the qualified disaster recovery distribution (Form 8915-F) to retirement.special and reworded retirement.rollover and retirement.exception; retirement.special still names "a death benefit exclusion" and "a pension or annuity in which you have after-tax cost whose annuity starting date ... was before November 19, 1996", and the worksheet expressions are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: Subtracts line 8 from line 1 and floors the result at zero, matching the worksheet.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: Line 10 says 'Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet'; the restatement always adds lines 6 and 8.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 10 is the only one reached. Re-checked against the current forms/2025/retirement.yaml this round: BUG-0393 added the qualified disaster recovery distribution (Form 8915-F) to retirement.special and reworded retirement.rollover and retirement.exception; retirement.special still names "a death benefit exclusion" and "a pension or annuity in which you have after-tax cost whose annuity starting date ... was before November 19, 1996", and the worksheet expressions are unchanged. Same model reading as earlier rounds. Project stands on the English.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: Line 11 is part of the 'Do not complete the rest of this worksheet' branch for a pre-1987 annuity starting date, but the restatement always subtracts line 10 from line 2.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 11 is the only one reached. Re-checked against the current forms/2025/retirement.yaml this round: BUG-0393 added the qualified disaster recovery distribution (Form 8915-F) to retirement.special and reworded retirement.rollover and retirement.exception; retirement.special still names "a death benefit exclusion" and "a pension or annuity in which you have after-tax cost whose annuity starting date ... was before November 19, 1996", and the worksheet expressions are unchanged. Same model reading as earlier rounds. Project stands on the English.

## Raw response

```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "Restates Form 1099-R box 1 as the total pension or annuity payments for line 1."
  - key: "(SMW 2)"
    status: MATCH
    reason: "Restates the cost in the plan at the annuity starting date, including the survivor rule from the instructions."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "Table 1 has separate numbers for an annuity starting date before November 19, 1996 (300/260/240/170/120) and after November 18, 1996 (360/310/260/210/160); the restatement uses only the after-November-18-1996 numbers."
  - key: "(SMW 5)"
    status: MATCH
    reason: "Multiplies line 4 by the number of months for which this year's payments were made, as the worksheet says."
  - key: "(SMW 6)"
    status: MISMATCH
    reason: "The worksheet says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always computes line 6."
  - key: "(SMW 7)"
    status: MISMATCH
    reason: "The worksheet says 'If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8'; the restatement always subtracts line 6 from line 2."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "For a pre-1987 annuity starting date the worksheet says to enter the line 5 amount on line 8, not the smaller of line 5 or line 7 as the restatement does."
  - key: "(SMW 9)"
    status: MATCH
    reason: "Subtracts line 8 from line 1 and floors the result at zero, matching the worksheet."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "Line 10 says 'Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet'; the restatement always adds lines 6 and 8."
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "Line 11 is part of the 'Do not complete the rest of this worksheet' branch for a pre-1987 annuity starting date, but the restatement always subtracts line 10 from line 2."
```
