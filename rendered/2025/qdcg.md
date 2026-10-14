# Qualified Dividends and Capital Gain Tax Worksheet—Line 16

- Document: `qdcg` (worksheet, tax year 2025)
- Note: The Form 2555 alternatives printed on lines 1 and 25 are outside Stage 1 and are not encoded.

## (question) — `qdcg.schedule_d_filed`

- **Authored helper label:** Are you filing Schedule D?
- **Encoded (Bool):** Input — The taxpayer's answer to the worksheet question 'Are you filing Schedule D?'
- Expr: `{"op":"input","source":"The taxpayer's answer to the worksheet question 'Are you filing Schedule D?'"}`
- Cite: [i1040gi] QDCGT worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (input) — `qdcg.schedule_d_net_gain`

- **Authored helper label:** Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-.
- **Encoded (NonNegDollars):** Input — Schedule D (Form 1040) lines 15 and 16: the smaller of the two, or 0 if either is blank or a loss. Schedule D is outside Stage 1; the value is supplied directly.
- Expr: `{"op":"input","source":"Schedule D (Form 1040) lines 15 and 16: the smaller of the two, or 0 if either is blank or a loss. Schedule D is outside Stage 1; the value is supplied directly."}`
- Cite: [i1040gi] QDCGT worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 1 — `qdcg.line1`

- **IRS:** Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 15.
- Expr: `{"from":"f1040.line15","op":"copy"}`
- Cite: [i1040gi] QDCGT worksheet, line 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## 2 — `qdcg.line2`

- **IRS:** Enter the amount from Form 1040 or 1040-SR, line 3a
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 3a.
- Expr: `{"from":"f1040.line3a","op":"copy"}`
- Cite: [i1040gi] QDCGT worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `qdcg.line3`

- **IRS:** Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-. No. Enter the amount from Form 1040 or 1040-SR, line 7a
- **Encoded (NonNegDollars):** Choose — [line (question) = true → line (input)] [line (question) = false → f1040 line 7a]
- Expr: `{"alternatives":[{"guard":{"eq":["qdcg.schedule_d_filed",{"const":true}],"op":"test"},"then":"qdcg.schedule_d_net_gain"},{"guard":{"eq":["qdcg.schedule_d_filed",{"const":false}],"op":"test"},"then":"f1040.line7a"}],"op":"choose"}`
- Cite: [i1040gi] QDCGT worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 4 — `qdcg.line4`

- **IRS:** Add lines 2 and 3
- **Encoded (NonNegDollars):** Add line 2 and line 3.
- Expr: `{"of":["qdcg.line2","qdcg.line3"],"op":"sum"}`
- Cite: [i1040gi] QDCGT worksheet, line 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `qdcg.line5`

- **IRS:** Subtract line 4 from line 1. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 4 from line 1. If zero or less, enter -0-.
- Expr: `{"from":"qdcg.line1","op":"subtract_floor0","take":"qdcg.line4"}`
- Cite: [i1040gi] QDCGT worksheet, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## 6 — `qdcg.line6`

- **IRS:** Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly or qualifying surviving spouse, $64,750 if head of household
- **Encoded (NonNegDollars):** Enter single $48,350; mfj $96,700; mfs $48,350; hoh $64,750; qss $96,700 (qdcg.zero_rate_ceiling).
- Expr: `{"op":"param","ref":"qdcg.zero_rate_ceiling"}`
- Cite: [i1040gi] QDCGT worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## 7 — `qdcg.line7`

- **IRS:** Enter the smaller of line 1 or line 6
- **Encoded (NonNegDollars):** Enter the smaller of line 1 or line 6.
- Expr: `{"of":["qdcg.line1","qdcg.line6"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## 8 — `qdcg.line8`

- **IRS:** Enter the smaller of line 5 or line 7
- **Encoded (NonNegDollars):** Enter the smaller of line 5 or line 7.
- Expr: `{"of":["qdcg.line5","qdcg.line7"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## 9 — `qdcg.line9`

- **IRS:** Subtract line 8 from line 7. This amount is taxed at 0%
- **Encoded (Dollars):** Subtract line 8 from line 7.
- Expr: `{"from":"qdcg.line7","op":"subtract","take":"qdcg.line8"}`
- Cite: [i1040gi] QDCGT worksheet, line 9 (2025; printed date 2026-02-25; sha256 482e9c48)

## 10 — `qdcg.line10`

- **IRS:** Enter the smaller of line 1 or line 4
- **Encoded (NonNegDollars):** Enter the smaller of line 1 or line 4.
- Expr: `{"of":["qdcg.line1","qdcg.line4"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 10 (2025; printed date 2026-02-25; sha256 482e9c48)

## 11 — `qdcg.line11`

- **IRS:** Enter the amount from line 9
- **Encoded (Dollars):** Enter the amount from line 9.
- Expr: `{"from":"qdcg.line9","op":"copy"}`
- Cite: [i1040gi] QDCGT worksheet, line 11 (2025; printed date 2026-02-25; sha256 482e9c48)

## 12 — `qdcg.line12`

- **IRS:** Subtract line 11 from line 10
- **Encoded (Dollars):** Subtract line 11 from line 10.
- Expr: `{"from":"qdcg.line10","op":"subtract","take":"qdcg.line11"}`
- Cite: [i1040gi] QDCGT worksheet, line 12 (2025; printed date 2026-02-25; sha256 482e9c48)

## 13 — `qdcg.line13`

- **IRS:** Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married filing jointly or qualifying surviving spouse, $566,700 if head of household
- **Encoded (NonNegDollars):** Enter single $533,400; mfj $600,050; mfs $300,000; hoh $566,700; qss $600,050 (qdcg.fifteen_rate_ceiling).
- Expr: `{"op":"param","ref":"qdcg.fifteen_rate_ceiling"}`
- Cite: [i1040gi] QDCGT worksheet, line 13 (2025; printed date 2026-02-25; sha256 482e9c48)

## 14 — `qdcg.line14`

- **IRS:** Enter the smaller of line 1 or line 13
- **Encoded (NonNegDollars):** Enter the smaller of line 1 or line 13.
- Expr: `{"of":["qdcg.line1","qdcg.line13"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 14 (2025; printed date 2026-02-25; sha256 482e9c48)

## 15 — `qdcg.line15`

- **IRS:** Add lines 5 and 9
- **Encoded (Dollars):** Add line 5 and line 9.
- Expr: `{"of":["qdcg.line5","qdcg.line9"],"op":"sum"}`
- Cite: [i1040gi] QDCGT worksheet, line 15 (2025; printed date 2026-02-25; sha256 482e9c48)

## 16 — `qdcg.line16`

- **IRS:** Subtract line 15 from line 14. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 15 from line 14. If zero or less, enter -0-.
- Expr: `{"from":"qdcg.line14","op":"subtract_floor0","take":"qdcg.line15"}`
- Cite: [i1040gi] QDCGT worksheet, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## 17 — `qdcg.line17`

- **IRS:** Enter the smaller of line 12 or line 16
- **Encoded (Dollars):** Enter the smaller of line 12 or line 16.
- Expr: `{"of":["qdcg.line12","qdcg.line16"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 17 (2025; printed date 2026-02-25; sha256 482e9c48)

## 18 — `qdcg.line18`

- **IRS:** Multiply line 17 by 15% (0.15)
- **Encoded (Dollars):** Multiply line 17 by 15% (0.15) (qdcg.rate_15).
- Expr: `{"amount":"qdcg.line17","op":"multiply_rate","rate":{"param":"qdcg.rate_15"}}`
- Cite: [i1040gi] QDCGT worksheet, line 18 (2025; printed date 2026-02-25; sha256 482e9c48)

## 19 — `qdcg.line19`

- **IRS:** Add lines 9 and 17
- **Encoded (Dollars):** Add line 9 and line 17.
- Expr: `{"of":["qdcg.line9","qdcg.line17"],"op":"sum"}`
- Cite: [i1040gi] QDCGT worksheet, line 19 (2025; printed date 2026-02-25; sha256 482e9c48)

## 20 — `qdcg.line20`

- **IRS:** Subtract line 19 from line 10
- **Encoded (Dollars):** Subtract line 19 from line 10.
- Expr: `{"from":"qdcg.line10","op":"subtract","take":"qdcg.line19"}`
- Cite: [i1040gi] QDCGT worksheet, line 20 (2025; printed date 2026-02-25; sha256 482e9c48)

## 21 — `qdcg.line21`

- **IRS:** Multiply line 20 by 20% (0.20)
- **Encoded (Dollars):** Multiply line 20 by 20% (0.20) (qdcg.rate_20).
- Expr: `{"amount":"qdcg.line20","op":"multiply_rate","rate":{"param":"qdcg.rate_20"}}`
- Cite: [i1040gi] QDCGT worksheet, line 21 (2025; printed date 2026-02-25; sha256 482e9c48)

## 22 — `qdcg.line22`

- **IRS:** Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 5 is $100,000 or more, use the Tax Computation Worksheet
- **Encoded (Dollars):** Enter the amount from tax_on_amount(amount = line 5, status = f1040 "Filing Status").tax.
- Expr: `{"from":{"bind":{"amount":"qdcg.line5","status":"f1040.status"},"def":"tax_on_amount","line":"tax"},"op":"copy"}`
- Cite: [i1040gi] QDCGT worksheet, line 22 (2025; printed date 2026-02-25; sha256 482e9c48)

## 23 — `qdcg.line23`

- **IRS:** Add lines 18, 21, and 22
- **Encoded (Dollars):** Add line 18, line 21, and line 22.
- Expr: `{"of":["qdcg.line18","qdcg.line21","qdcg.line22"],"op":"sum"}`
- Cite: [i1040gi] QDCGT worksheet, line 23 (2025; printed date 2026-02-25; sha256 482e9c48)

## 24 — `qdcg.line24`

- **IRS:** Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use the Tax Table to figure the tax. If the amount on line 1 is $100,000 or more, use the Tax Computation Worksheet
- **Encoded (Dollars):** Enter the amount from tax_on_amount(amount = line 1, status = f1040 "Filing Status").tax.
- Expr: `{"from":{"bind":{"amount":"qdcg.line1","status":"f1040.status"},"def":"tax_on_amount","line":"tax"},"op":"copy"}`
- Cite: [i1040gi] QDCGT worksheet, line 24 (2025; printed date 2026-02-25; sha256 482e9c48)

## 25 — `qdcg.line25`

- **IRS:** Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amount on the entry space on Form 1040 or 1040-SR, line 16. If you are filing Form 2555, don't enter this amount on the entry space on Form 1040 or 1040-SR, line 16. Instead, enter it on line 4 of the Foreign Earned Income Tax Worksheet
- **Encoded (Dollars):** Enter the smaller of line 23 or line 24.
- Expr: `{"of":["qdcg.line23","qdcg.line24"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 25 (2025; printed date 2026-02-25; sha256 482e9c48)
