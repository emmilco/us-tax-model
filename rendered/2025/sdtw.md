# Schedule D Tax Worksheet

- Document: `sdtw` (worksheet, tax year 2025)
- Note: Default Form 4952 capital-gain-first allocation. Form 2555 and alternative dotted-line allocation are outside scope. Skipped lines contribute zero; raw helpers show arithmetic before skip rules.

## (helper) — `sdtw.zero`

- **Authored helper label:** Zero for skipped worksheet lines
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.ordinary_ceiling`

- **Authored helper label:** Ordinary-income ceiling for line 19
- **Encoded (NonNegDollars):** Enter single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $394,600 (sdtw.ordinary_ceiling).
- Expr: `{"op":"param","ref":"sdtw.ordinary_ceiling"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.after22`

- **Authored helper label:** Continue after line 22 when lines 1 and 16 differ
- **Encoded (Bool):** line 1 ≠ line 16
- Expr: `{"ne":["sdtw.line1","sdtw.line16"],"op":"test"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.after32`

- **Authored helper label:** Continue after line 32 when lines 1 and 32 differ
- **Encoded (Bool):** line (helper) = true and line 1 ≠ line 32
- Expr: `{"all":[{"eq":["sdtw.after22",{"const":true}],"op":"test"},{"ne":["sdtw.line1","sdtw.line32"],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.use1250`

- **Authored helper label:** Compute lines 35–40 when Schedule D line 19 is positive
- **Encoded (Bool):** line (helper) = true and sd "(helper)" > $0
- Expr: `{"all":[{"eq":["sdtw.after32",{"const":true}],"op":"test"},{"gt":["sd.line19",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.use28`

- **Authored helper label:** Follow printed flow to lines 41–43
- **Encoded (Bool):** line (helper) = true and (sd "(helper)" = $0 or sd "(helper)" > $0)
- Expr: `{"all":[{"eq":["sdtw.after32",{"const":true}],"op":"test"},{"any":[{"eq":["sd.line19",{"const":0}],"op":"test"},{"gt":["sd.line18",{"const":0}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 1 — `sdtw.line1`

- **IRS:** Taxable income
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 15.
- Expr: `{"from":"f1040.line15","op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 2 — `sdtw.line2`

- **IRS:** Qualified dividends
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 3a.
- Expr: `{"from":"f1040.line3a","op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 3 — `sdtw.line3`

- **IRS:** Form 4952 line 4g election
- **Encoded (NonNegDollars):** Enter the amount from sd "(helper)".
- Expr: `{"from":"sd.investment_election","op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 4 — `sdtw.line4`

- **IRS:** Form 4952 line 4e, default capital-gain-first allocation
- **Encoded (NonNegDollars):** Enter the amount from f4952 line 4e.
- Expr: `{"from":"f4952.line4e","op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 5 — `sdtw.line5`

- **IRS:** Subtract line 4 from line 3; floor at zero
- **Encoded (NonNegDollars):** Subtract line 4 from line 3. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line3","op":"subtract_floor0","take":"sdtw.line4"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 6 — `sdtw.line6`

- **IRS:** Subtract line 5 from line 2; floor at zero
- **Encoded (NonNegDollars):** Subtract line 5 from line 2. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line2","op":"subtract_floor0","take":"sdtw.line5"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 7 — `sdtw.line7`

- **IRS:** Smaller of Schedule D lines 15 and 16
- **Encoded (Dollars):** Enter the smaller of sd line 15 or sd line 16.
- Expr: `{"of":["sd.line15","sd.line16"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 8 — `sdtw.line8`

- **IRS:** Smaller of lines 3 and 4
- **Encoded (NonNegDollars):** Enter the smaller of line 3 or line 4.
- Expr: `{"of":["sdtw.line3","sdtw.line4"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 9 — `sdtw.line9`

- **IRS:** Subtract line 8 from line 7; floor at zero
- **Encoded (NonNegDollars):** Subtract line 8 from line 7. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line7","op":"subtract_floor0","take":"sdtw.line8"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 10 — `sdtw.line10`

- **IRS:** Add lines 6 and 9
- **Encoded (NonNegDollars):** Add line 6 and line 9.
- Expr: `{"of":["sdtw.line6","sdtw.line9"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 11 — `sdtw.line11`

- **IRS:** Add Schedule D lines 18 and 19
- **Encoded (NonNegDollars):** Add sd "(helper)" and sd "(helper)".
- Expr: `{"of":["sd.line18","sd.line19"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 12 — `sdtw.line12`

- **IRS:** Smaller of lines 9 and 11
- **Encoded (NonNegDollars):** Enter the smaller of line 9 or line 11.
- Expr: `{"of":["sdtw.line9","sdtw.line11"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 13 — `sdtw.line13`

- **IRS:** Subtract line 12 from line 10
- **Encoded (Dollars):** Subtract line 12 from line 10.
- Expr: `{"from":"sdtw.line10","op":"subtract","take":"sdtw.line12"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 14 — `sdtw.line14`

- **IRS:** Subtract line 13 from line 1; floor at zero
- **Encoded (NonNegDollars):** Subtract line 13 from line 1. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line1","op":"subtract_floor0","take":"sdtw.line13"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 15 — `sdtw.line15`

- **IRS:** Zero-rate ceiling by filing status
- **Encoded (NonNegDollars):** Enter single $48,350; mfj $96,700; mfs $48,350; hoh $64,750; qss $96,700 (qdcg.zero_rate_ceiling).
- Expr: `{"op":"param","ref":"qdcg.zero_rate_ceiling"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 16 — `sdtw.line16`

- **IRS:** Smaller of lines 1 and 15
- **Encoded (NonNegDollars):** Enter the smaller of line 1 or line 15.
- Expr: `{"of":["sdtw.line1","sdtw.line15"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 17 — `sdtw.line17`

- **IRS:** Smaller of lines 14 and 16
- **Encoded (NonNegDollars):** Enter the smaller of line 14 or line 16.
- Expr: `{"of":["sdtw.line14","sdtw.line16"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 18 — `sdtw.line18`

- **IRS:** Subtract line 10 from line 1; floor at zero
- **Encoded (NonNegDollars):** Subtract line 10 from line 1. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line1","op":"subtract_floor0","take":"sdtw.line10"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 19 — `sdtw.line19`

- **IRS:** Smaller of taxable income and ordinary-income ceiling
- **Encoded (NonNegDollars):** Enter the smaller of line 1 or line (helper).
- Expr: `{"of":["sdtw.line1","sdtw.ordinary_ceiling"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 20 — `sdtw.line20`

- **IRS:** Smaller of lines 14 and 19
- **Encoded (NonNegDollars):** Enter the smaller of line 14 or line 19.
- Expr: `{"of":["sdtw.line14","sdtw.line19"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 21 — `sdtw.line21`

- **IRS:** Larger of lines 18 and 20
- **Encoded (NonNegDollars):** Enter the larger of line 18 or line 20.
- Expr: `{"of":["sdtw.line18","sdtw.line20"],"op":"larger_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 22 — `sdtw.line22`

- **IRS:** Subtract line 17 from line 16; taxed at zero percent
- **Encoded (Dollars):** Subtract line 17 from line 16.
- Expr: `{"from":"sdtw.line16","op":"subtract","take":"sdtw.line17"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw23`

- **Authored helper label:** Smaller of lines 1 and 13 before skip rule
- **Encoded (Dollars):** Enter the smaller of line 1 or line 13.
- Expr: `{"of":["sdtw.line1","sdtw.line13"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 23 — `sdtw.line23`

- **IRS:** Smaller of lines 1 and 13
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw23"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw24`

- **Authored helper label:** Amount from line 22 before skip rule
- **Encoded (Dollars):** Enter the amount from line 22.
- Expr: `{"from":"sdtw.line22","op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 24 — `sdtw.line24`

- **IRS:** Amount from line 22
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw24"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw25`

- **Authored helper label:** Subtract line 24 from line 23; floor at zero before skip rule
- **Encoded (NonNegDollars):** Subtract line 24 from line 23. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line23","op":"subtract_floor0","take":"sdtw.line24"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 25 — `sdtw.line25`

- **IRS:** Subtract line 24 from line 23; floor at zero
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw25"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw26`

- **Authored helper label:** 15-percent ceiling by filing status before skip rule
- **Encoded (NonNegDollars):** Enter single $533,400; mfj $600,050; mfs $300,000; hoh $566,700; qss $600,050 (qdcg.fifteen_rate_ceiling).
- Expr: `{"op":"param","ref":"qdcg.fifteen_rate_ceiling"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 26 — `sdtw.line26`

- **IRS:** 15-percent ceiling by filing status
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw26"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw27`

- **Authored helper label:** Smaller of lines 1 and 26 before skip rule
- **Encoded (NonNegDollars):** Enter the smaller of line 1 or line 26.
- Expr: `{"of":["sdtw.line1","sdtw.line26"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 27 — `sdtw.line27`

- **IRS:** Smaller of lines 1 and 26
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw27"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw28`

- **Authored helper label:** Add lines 21 and 22 before skip rule
- **Encoded (Dollars):** Add line 21 and line 22.
- Expr: `{"of":["sdtw.line21","sdtw.line22"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 28 — `sdtw.line28`

- **IRS:** Add lines 21 and 22
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw28"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw29`

- **Authored helper label:** Subtract line 28 from line 27; floor at zero before skip rule
- **Encoded (NonNegDollars):** Subtract line 28 from line 27. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line27","op":"subtract_floor0","take":"sdtw.line28"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 29 — `sdtw.line29`

- **IRS:** Subtract line 28 from line 27; floor at zero
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw29"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw30`

- **Authored helper label:** Smaller of lines 25 and 29 before skip rule
- **Encoded (NonNegDollars):** Enter the smaller of line 25 or line 29.
- Expr: `{"of":["sdtw.line25","sdtw.line29"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 30 — `sdtw.line30`

- **IRS:** Smaller of lines 25 and 29
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw30"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw31`

- **Authored helper label:** Multiply line 30 by 15 percent before skip rule
- **Encoded (NonNegDollars):** Multiply line 30 by 15% (0.15) (sdtw.rate15).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sdtw.line30","op":"multiply_rate","rate":{"param":"sdtw.rate15"}}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 31 — `sdtw.line31`

- **IRS:** Multiply line 30 by 15 percent
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw31"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw32`

- **Authored helper label:** Add lines 24 and 30 before skip rule
- **Encoded (Dollars):** Add line 24 and line 30.
- Expr: `{"of":["sdtw.line24","sdtw.line30"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 32 — `sdtw.line32`

- **IRS:** Add lines 24 and 30
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after22",{"const":true}],"op":"test"},"then":"sdtw.raw32"},{"guard":{"eq":["sdtw.after22",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw33`

- **Authored helper label:** Subtract line 32 from line 23 before skip rule
- **Encoded (Dollars):** Subtract line 32 from line 23.
- Expr: `{"from":"sdtw.line23","op":"subtract","take":"sdtw.line32"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 33 — `sdtw.line33`

- **IRS:** Subtract line 32 from line 23
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after32",{"const":true}],"op":"test"},"then":"sdtw.raw33"},{"guard":{"eq":["sdtw.after32",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw34`

- **Authored helper label:** Multiply line 33 by 20 percent before skip rule
- **Encoded (Dollars):** Multiply line 33 by 20% (0.20) (sdtw.rate20).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sdtw.line33","op":"multiply_rate","rate":{"param":"sdtw.rate20"}}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 34 — `sdtw.line34`

- **IRS:** Multiply line 33 by 20 percent
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.after32",{"const":true}],"op":"test"},"then":"sdtw.raw34"},{"guard":{"eq":["sdtw.after32",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw35`

- **Authored helper label:** Smaller of line 9 and Schedule D line 19 before skip rule
- **Encoded (NonNegDollars):** Enter the smaller of line 9 or sd "(helper)".
- Expr: `{"of":["sdtw.line9","sd.line19"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 35 — `sdtw.line35`

- **IRS:** Smaller of line 9 and Schedule D line 19
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use1250",{"const":true}],"op":"test"},"then":"sdtw.raw35"},{"guard":{"eq":["sdtw.use1250",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw36`

- **Authored helper label:** Add lines 10 and 21 before skip rule
- **Encoded (NonNegDollars):** Add line 10 and line 21.
- Expr: `{"of":["sdtw.line10","sdtw.line21"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 36 — `sdtw.line36`

- **IRS:** Add lines 10 and 21
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use1250",{"const":true}],"op":"test"},"then":"sdtw.raw36"},{"guard":{"eq":["sdtw.use1250",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw37`

- **Authored helper label:** Amount from line 1 before skip rule
- **Encoded (NonNegDollars):** Enter the amount from line 1.
- Expr: `{"from":"sdtw.line1","op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 37 — `sdtw.line37`

- **IRS:** Amount from line 1
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use1250",{"const":true}],"op":"test"},"then":"sdtw.raw37"},{"guard":{"eq":["sdtw.use1250",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw38`

- **Authored helper label:** Subtract line 37 from line 36; floor at zero before skip rule
- **Encoded (NonNegDollars):** Subtract line 37 from line 36. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line36","op":"subtract_floor0","take":"sdtw.line37"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 38 — `sdtw.line38`

- **IRS:** Subtract line 37 from line 36; floor at zero
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use1250",{"const":true}],"op":"test"},"then":"sdtw.raw38"},{"guard":{"eq":["sdtw.use1250",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw39`

- **Authored helper label:** Subtract line 38 from line 35; floor at zero before skip rule
- **Encoded (NonNegDollars):** Subtract line 38 from line 35. If zero or less, enter -0-.
- Expr: `{"from":"sdtw.line35","op":"subtract_floor0","take":"sdtw.line38"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 39 — `sdtw.line39`

- **IRS:** Subtract line 38 from line 35; floor at zero
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use1250",{"const":true}],"op":"test"},"then":"sdtw.raw39"},{"guard":{"eq":["sdtw.use1250",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw40`

- **Authored helper label:** Multiply line 39 by 25 percent before skip rule
- **Encoded (NonNegDollars):** Multiply line 39 by 25% (0.25) (sdtw.rate25).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sdtw.line39","op":"multiply_rate","rate":{"param":"sdtw.rate25"}}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 40 — `sdtw.line40`

- **IRS:** Multiply line 39 by 25 percent
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use1250",{"const":true}],"op":"test"},"then":"sdtw.raw40"},{"guard":{"eq":["sdtw.use1250",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw41`

- **Authored helper label:** Add lines 21, 22, 30, 33 and 39 before skip rule
- **Encoded (Dollars):** Add line 21, line 22, line 30, line 33, and line 39.
- Expr: `{"of":["sdtw.line21","sdtw.line22","sdtw.line30","sdtw.line33","sdtw.line39"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 41 — `sdtw.line41`

- **IRS:** Add lines 21, 22, 30, 33 and 39
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use28",{"const":true}],"op":"test"},"then":"sdtw.raw41"},{"guard":{"eq":["sdtw.use28",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw42`

- **Authored helper label:** Subtract line 41 from line 1 before skip rule
- **Encoded (Dollars):** Subtract line 41 from line 1.
- Expr: `{"from":"sdtw.line1","op":"subtract","take":"sdtw.line41"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 42 — `sdtw.line42`

- **IRS:** Subtract line 41 from line 1
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use28",{"const":true}],"op":"test"},"then":"sdtw.raw42"},{"guard":{"eq":["sdtw.use28",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sdtw.raw43`

- **Authored helper label:** Multiply line 42 by 28 percent before skip rule
- **Encoded (Dollars):** Multiply line 42 by 28% (0.28) (sdtw.rate28).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sdtw.line42","op":"multiply_rate","rate":{"param":"sdtw.rate28"}}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 43 — `sdtw.line43`

- **IRS:** Multiply line 42 by 28 percent
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sdtw.use28",{"const":true}],"op":"test"},"then":"sdtw.raw43"},{"guard":{"eq":["sdtw.use28",{"const":false}],"op":"test"},"then":"sdtw.zero"}],"op":"choose"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 44 — `sdtw.line44`

- **IRS:** Tax on line 21 using Tax Table or Tax Computation Worksheet
- **Encoded (Dollars):** Enter the amount from tax_on_amount(amount = line 21, status = f1040 "Filing Status").tax.
- Expr: `{"from":{"bind":{"amount":"sdtw.line21","status":"f1040.status"},"def":"tax_on_amount","line":"tax"},"op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 45 — `sdtw.line45`

- **IRS:** Add lines 31, 34, 40, 43 and 44
- **Encoded (Dollars):** Add line 31, line 34, line 40, line 43, and line 44.
- Expr: `{"of":["sdtw.line31","sdtw.line34","sdtw.line40","sdtw.line43","sdtw.line44"],"op":"sum"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 46 — `sdtw.line46`

- **IRS:** Tax on all taxable income using Tax Table or Tax Computation Worksheet
- **Encoded (Dollars):** Enter the amount from tax_on_amount(amount = line 1, status = f1040 "Filing Status").tax.
- Expr: `{"from":{"bind":{"amount":"sdtw.line1","status":"f1040.status"},"def":"tax_on_amount","line":"tax"},"op":"copy"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)

## 47 — `sdtw.line47`

- **IRS:** Smaller of lines 45 and 46; tax on all taxable income
- **Encoded (Dollars):** Enter the smaller of line 45 or line 46.
- Expr: `{"of":["sdtw.line45","sdtw.line46"],"op":"smaller_of"}`
- Cite: [i1040sd] pp. 15–16, Schedule D Tax Worksheet (2025; printed date 2025-12-11; sha256 650643a6)
