# Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650)

- Document: `ny_tcw_first` (def, tax year 2025)
- Parameters: agi, ti, status, rate

## 1 — `agi`

- **IRS:** Enter your New York adjusted gross income from line 33
- **Encoded (Dollars):** Input — Bound by the calling line (Form IT-201 line 33).
- Expr: `{"op":"input","source":"Bound by the calling line (Form IT-201 line 33)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "1. Enter your New York adjusted gross income from line 33" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 2 — `ti`

- **IRS:** Enter your taxable income from line 38
- **Encoded (NonNegDollars):** Input — Bound by the calling line (Form IT-201 line 38).
- Expr: `{"op":"input","source":"Bound by the calling line (Form IT-201 line 38)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "2. Enter your taxable income from line 38" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (status) — `status`

- **Authored helper label:** Filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (the federal filing status, IT-201 item A).
- Expr: `{"op":"input","source":"Bound by the calling line (the federal filing status, IT-201 item A)."}`
- Cite: [ny_it201i-html] Tax computation—New York adjusted gross income of more than $107,650, "Find your New York State tax by using the correct tax computation worksheet within your filing status (see below)." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (3) — `rate`

- **Authored helper label:** The worksheet's flat rate (5.5% on worksheet 1; 6% on worksheets 7 and 12)
- **Encoded (Rate):** Input — Bound by the calling line (ny.tcw.first.rate or ny.tcw.first.rate6).
- Expr: `{"op":"input","source":"Bound by the calling line (ny.tcw.first.rate or ny.tcw.first.rate6)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "3. Multiply line 2 by 5.5% (0.055)"; Tax computation worksheet 7, "3. Multiply line 2 by 6% (0.06)" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 3 — `line3`

- **IRS:** Multiply line 2 by the flat rate
- **Encoded (NonNegDollars):** Multiply line 2 by column (3), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"ti","op":"multiply_rate","rate":"rate","unit":100}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "3. Multiply line 2 by 5.5% (0.055)" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (3, Stop) — `stop`

- **Authored helper label:** Is the line 1 amount $157,650 or more?
- **Encoded (Bool):** line 1 ≥ $157,650 (ny.tcw.first.stop)
- Expr: `{"ge":["agi",{"param":"ny.tcw.first.stop"}],"op":"test"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "(Stop: If the line 1 amount is $157,650 or more, skip lines 4 through 8 and enter the line 3 amount on line 9)" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 4 — `line4`

- **IRS:** Enter your New York State tax on the line 2 amount from the New York State tax rate schedule
- **Encoded (NonNegDollars):** Enter "tax" of New York State tax rate schedule with amount = line 2 and status = helper "Filing status".
- Expr: `{"from":{"bind":{"amount":"ti","status":"status"},"def":"ny_rs","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "4. Enter your New York State tax on the line 2 amount from the New York State tax rate schedule" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 5 — `line5`

- **IRS:** Subtract line 4 from line 3
- **Encoded (NonNegDollars):** Subtract line 4 from line 3. If zero or less, enter -0-.
- Note: Line 3 is never less than line 4 here (the flat rate is the top rate of every band below the worksheet's taxable-income limit), so the floor at zero never acts; it keeps the amount prorated on line 8 non-negative.
- Expr: `{"from":"line3","op":"subtract_floor0","take":"line4"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "5. Subtract line 4 from line 3" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 6 — `line6`

- **IRS:** Enter the excess of line 1 over $107,650
- **Encoded (NonNegDollars):** Subtract $107,650 (ny.tcw.first.start) from line 1. If zero or less, enter -0-.
- Expr: `{"from":"agi","op":"subtract_floor0","take":{"param":"ny.tcw.first.start"}}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "6. Enter the excess of line 1 over $107,650" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (scale) — `hundred`

- **Authored helper label:** 100
- **Encoded (Count):** Enter 100 (ny.hundred).
- Expr: `{"op":"param","ref":"ny.hundred"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "8. Multiply line 5 by line 7" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (scale) — `line8_scaled`

- **Authored helper label:** The amount times 100, so that the product with a ratio of four decimal places is exact
- **Encoded (NonNegDollars):** Multiply line 5 by the number on column (scale) (hundred).
- Expr: `{"amount":"line5","count":"hundred","op":"multiply_count"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "8. Multiply line 5 by line 7" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 7, 8 — `line8_exact`

- **IRS:** The ratio rounded to the fourth decimal place, times the amount (times 100: exact)
- **Encoded (NonNegDollars):** Divide line 6 by $50,000 (ny.tcw.phase), rounded to 4 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply column (scale) (line8_scaled) by the result.
- Interpretation: amb.ny.2025.fourth_decimal
- Expr: `{"amount":"line8_scaled","op":"prorate","part":"line6","places":4,"whole":{"param":"ny.tcw.phase"}}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "7. Divide line 6 by $50,000 and round the result to the fourth decimal place", "8. Multiply line 5 by line 7" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 8 — `line8`

- **IRS:** Multiply line 5 by line 7 (whole dollars)
- **Encoded (NonNegDollars):** Multiply line 7, 8 by 1% (0.01) (ny.hundredth), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"line8_exact","op":"multiply_rate","rate":{"param":"ny.hundredth"},"unit":100}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "7. Divide line 6 by $50,000 and round the result to the fourth decimal place", "8. Multiply line 5 by line 7" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 9 — `line9_phased`

- **IRS:** Add lines 4 and 8
- **Encoded (NonNegDollars):** Add line 4 and line 8.
- Expr: `{"of":["line4","line8"],"op":"sum"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "9. Add lines 4 and 8. Enter here and on line 39." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 9 — `tax`

- **IRS:** Add lines 4 and 8, or, at the Stop, the line 3 amount. Enter here and on line 39.
- **Encoded (NonNegDollars):** Choose — [column (3, Stop) = true → line 3] [column (3, Stop) = false → line 9 (line9_phased)]
- Expr: `{"alternatives":[{"guard":{"eq":["stop",{"const":true}],"op":"test"},"then":"line3"},{"guard":{"eq":["stop",{"const":false}],"op":"test"},"then":"line9_phased"}],"op":"choose"}`
- Cite: [ny_it201i-html] Tax computation worksheet 1, "(Stop: If the line 1 amount is $157,650 or more, skip lines 4 through 8 and enter the line 3 amount on line 9)", "9. Add lines 4 and 8. Enter here and on line 39." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)
