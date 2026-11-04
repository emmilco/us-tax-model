# Render comparison — retirement

The rendered English of every printed line of `Form 1099-R distributions (IRAs, pensions and annuities)` (`rendered/2025/retirement.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5ba8a692de10eaefb8c0af0f11ce1db3f1514587f8b791e99d151ca077890ee2 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a5fb550fbd75bc269a77ba969fc3050bc5defb94260c0597d87eec14136b4991 |
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
| p575 | None | 12, 23, 34 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 12, 23, 34 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |

## Lines

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **MATCH**

Model: IRS line 1 is the total pension or annuity payments from Form 1099-R box 1; the helper uses gross distribution box 1 and the gate is consistent.

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **MISMATCH**

Restated: Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".

Model: IRS worksheet says to include the up-to-$5,000 death benefit exclusion for a beneficiary of a deceased employee/former employee who died before August 21, 1996 in the amount entered on line 2; the restatement uses only plan cost and never adds that exclusion.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, Before you begin: "If you are the beneficiary of a deceased employee or former employee who died before August 21, 1996, include any death benefit exclusion that you are entitled to (up to $5,000) in the amount entered on line 2 below." retirement.special asks about "a death benefit exclusion" and refuses the entry (retirement.taxable and retirement.rolled), so line 2 is the cost alone on every entry the worksheet reaches. Re-checked after the BUG-0354 review correction: the reworded item still names the death benefit exclusion, and it also refuses the beneficiary of an employee who died before retiring and an annuity with after-tax cost whose starting date (for a survivor of a retiree, the retiree's) was before November 19, 1996, which covers any death before August 21, 1996. No worksheet expression changed. As the Claude family's ruling on this line. render MISMATCH. Project stands on the English.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **MISMATCH**

Restated: Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]

Model: Table 1 has separate columns for annuity starting dates before November 19, 1996 and after November 18, 1996; the restatement uses only the after-November 18, 1996 numbers, so it miscomputes a before-November 19, 1996 annuity.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, Table 1 for Line 3, which has "before November 19, 1996" (300, 260, 240, 170, 120) and "after November 18, 1996" (360, 310, 260, 210, 160) columns. retirement.special still refuses "a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996", and retirement.annuity requires a starting date after November 18, 1996, so only the after-November-18-1996 column is reached. Re-checked against the current forms/2025/retirement.yaml: the income package (PENDING-4) narrowed other items of retirement.special and added survivor wording to the worksheet questions. The item relied on here is unchanged, and so are the worksheet expressions. Same model reading as earlier rounds. Project stands on the English.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **MATCH**

Model: IRS line 5 multiplies line 4 by the number of months for which this year's payments were made; the restatement does the same.

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **MISMATCH**

Restated: Enter the amount from helper "Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)".

Model: IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement reports line 6 for all Simplified Method Worksheet cases.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 6 is the only one reached. Re-checked against the current forms/2025/retirement.yaml: the income package (PENDING-4) narrowed other items of retirement.special and added survivor wording to the worksheet questions. The item relied on here is unchanged, and so are the worksheet expressions. Same model reading as earlier rounds. Project stands on the English.

### (SMW 7) — Subtract line 6 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 6) from column (SMW 2).

Model: IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7; the restatement computes line 7 in all Simplified Method Worksheet cases.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 7 is the only one reached. Re-checked against the current forms/2025/retirement.yaml: the income package (PENDING-4) narrowed other items of retirement.special and added survivor wording to the worksheet questions. The item relied on here is unchanged, and so are the worksheet expressions. Same model reading as earlier rounds. Project stands on the English.

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **MISMATCH**

Restated: Enter the smaller of column (SMW 5) or column (SMW 7).

Model: IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement instead always enters the smaller of line 5 or line 7.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 8 is the only one reached. Re-checked against the current forms/2025/retirement.yaml: the income package (PENDING-4) narrowed other items of retirement.special and added survivor wording to the worksheet questions. The item relied on here is unchanged, and so are the worksheet expressions. Same model reading as earlier rounds. Project stands on the English.

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **MATCH**

Model: IRS line 9 subtracts line 8 from line 1 and floors the result at zero; the restatement matches.

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **MISMATCH**

Restated: Add column (SMW 6) and column (SMW 8).

Model: IRS line 10 asks whether the annuity starting date was before 1987 and says 'Yes. STOP Do not complete the rest of this worksheet'; the restatement unconditionally adds lines 6 and 8.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 10 is the only one reached. Re-checked against the current forms/2025/retirement.yaml: the income package (PENDING-4) narrowed other items of retirement.special and added survivor wording to the worksheet questions. The item relied on here is unchanged, and so are the worksheet expressions. Same model reading as earlier rounds. Project stands on the English.

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **MISMATCH**

Restated: Subtract column (SMW 10) from column (SMW 2).

Model: IRS line 10 says 'Yes. STOP Do not complete the rest of this worksheet'; the restatement unconditionally subtracts line 10 from line 2.

Ruling: scope; i1040gi p. 29, Simplified Method Worksheet, line 5: "If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6", and line 10's before-1987 STOP. A starting date before 1987 is before November 19, 1996, which retirement.special refuses for an annuity with after-tax cost, and retirement.annuity asks for a starting date after November 18, 1996. So the post-1986 path of line 11 is the only one reached. Re-checked against the current forms/2025/retirement.yaml: the income package (PENDING-4) narrowed other items of retirement.special and added survivor wording to the worksheet questions. The item relied on here is unchanged, and so are the worksheet expressions. Same model reading as earlier rounds. Project stands on the English.

## Raw response

```yaml
lines:
  - key: "(SMW 1)"
    status: MATCH
    reason: "IRS line 1 is the total pension or annuity payments from Form 1099-R box 1; the helper uses gross distribution box 1 and the gate is consistent."
  - key: "(SMW 2)"
    status: MISMATCH
    reason: "IRS worksheet says to include the up-to-$5,000 death benefit exclusion for a beneficiary of a deceased employee/former employee who died before August 21, 1996 in the amount entered on line 2; the restatement uses only plan cost and never adds that exclusion."
  - key: "(SMW 4)"
    status: MISMATCH
    reason: "Table 1 has separate columns for annuity starting dates before November 19, 1996 and after November 18, 1996; the restatement uses only the after-November 18, 1996 numbers, so it miscomputes a before-November 19, 1996 annuity."
  - key: "(SMW 5)"
    status: MATCH
    reason: "IRS line 5 multiplies line 4 by the number of months for which this year's payments were made; the restatement does the same."
  - key: "(SMW 6)"
    status: MISMATCH
    reason: "IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement reports line 6 for all Simplified Method Worksheet cases."
  - key: "(SMW 7)"
    status: MISMATCH
    reason: "IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7; the restatement computes line 7 in all Simplified Method Worksheet cases."
  - key: "(SMW 8)"
    status: MISMATCH
    reason: "IRS line 5 says if the annuity starting date was before 1987, skip lines 6 and 7 and enter the line 5 amount on line 8; the restatement instead always enters the smaller of line 5 or line 7."
  - key: "(SMW 9)"
    status: MATCH
    reason: "IRS line 9 subtracts line 8 from line 1 and floors the result at zero; the restatement matches."
  - key: "(SMW 10)"
    status: MISMATCH
    reason: "IRS line 10 asks whether the annuity starting date was before 1987 and says 'Yes. STOP Do not complete the rest of this worksheet'; the restatement unconditionally adds lines 6 and 8."
  - key: "(SMW 11)"
    status: MISMATCH
    reason: "IRS line 10 says 'Yes. STOP Do not complete the rest of this worksheet'; the restatement unconditionally subtracts line 10 from line 2."
```
