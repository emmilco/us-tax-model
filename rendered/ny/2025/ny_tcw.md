# Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650)

- Document: `ny_tcw` (def, tax year 2025)
- Parameters: agi, ti, status, start, recapture, incremental

## 1 — `agi`

- **IRS:** Enter your New York adjusted gross income from line 33
- **Encoded (Dollars):** Input — Bound by the calling line (Form IT-201 line 33).
- Expr: `{"op":"input","source":"Bound by the calling line (Form IT-201 line 33)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "1. Enter your New York adjusted gross income from line 33" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 2 — `ti`

- **IRS:** Enter your taxable income from line 38
- **Encoded (NonNegDollars):** Input — Bound by the calling line (Form IT-201 line 38).
- Expr: `{"op":"input","source":"Bound by the calling line (Form IT-201 line 38)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "2. Enter your taxable income from line 38" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (status) — `status`

- **Authored helper label:** Filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (the federal filing status, IT-201 item A).
- Expr: `{"op":"input","source":"Bound by the calling line (the federal filing status, IT-201 item A)."}`
- Cite: [ny_it201i-html] Tax computation—New York adjusted gross income of more than $107,650, "Find your New York State tax by using the correct tax computation worksheet within your filing status (see below)." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (6) — `start`

- **Authored helper label:** The amount the excess of line 1 is measured over
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the worksheet's printed amount, ny.tcw.<group>.w<N>.start).
- Expr: `{"op":"input","source":"Bound by the calling line (the worksheet's printed amount, ny.tcw.<group>.w<N>.start)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "6. Enter the excess of line 1 over $161,550" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 3 — `line3`

- **IRS:** Enter your New York State tax on the line 2 amount from the New York State tax rate schedule
- **Encoded (NonNegDollars):** Enter "tax" of New York State tax rate schedule with amount = line 2 and status = helper "Filing status".
- Expr: `{"from":{"bind":{"amount":"ti","status":"status"},"def":"ny_rs","line":"tax"},"op":"copy"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "3. Enter your New York State tax on the line 2 amount from the New York State tax rate schedule" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 4 — `recapture`

- **IRS:** Recapture Base amount
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the worksheet's printed Recapture Base amount, ny.tcw.<group>.w<N>.recapture).
- Expr: `{"op":"input","source":"Bound by the calling line (the worksheet's printed Recapture Base amount, ny.tcw.<group>.w<N>.recapture)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "4. Recapture Base amount" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 5 — `incremental`

- **IRS:** Incremental Benefit amount
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the worksheet's printed Incremental Benefit amount, ny.tcw.<group>.w<N>.incremental).
- Expr: `{"op":"input","source":"Bound by the calling line (the worksheet's printed Incremental Benefit amount, ny.tcw.<group>.w<N>.incremental)."}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "5. Incremental Benefit amount" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 6 — `line6`

- **IRS:** Enter the excess of line 1 over the worksheet's amount
- **Encoded (NonNegDollars):** Subtract column (6) from line 1. If zero or less, enter -0-.
- Expr: `{"from":"agi","op":"subtract_floor0","take":"start"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "6. Enter the excess of line 1 over $161,550" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (7) — `phase`

- **Authored helper label:** $50,000
- **Encoded (NonNegDollars):** Enter $50,000 (ny.tcw.phase).
- Expr: `{"op":"param","ref":"ny.tcw.phase"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "7. Enter the lesser of line 6 or $50,000" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 7 — `line7`

- **IRS:** Enter the lesser of line 6 or $50,000
- **Encoded (NonNegDollars):** Enter the smaller of line 6 or column (7).
- Expr: `{"of":["line6","phase"],"op":"smaller_of"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "7. Enter the lesser of line 6 or $50,000" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (scale) — `hundred`

- **Authored helper label:** 100
- **Encoded (Count):** Enter 100 (ny.hundred).
- Expr: `{"op":"param","ref":"ny.hundred"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "9. Multiply line 5 by line 8" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (scale) — `line9_scaled`

- **Authored helper label:** The amount times 100, so that the product with a ratio of four decimal places is exact
- **Encoded (NonNegDollars):** Multiply line 5 by the number on column (scale) (hundred).
- Expr: `{"amount":"incremental","count":"hundred","op":"multiply_count"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "9. Multiply line 5 by line 8" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 8, 9 — `line9_exact`

- **IRS:** The ratio rounded to the fourth decimal place, times the amount (times 100: exact)
- **Encoded (NonNegDollars):** Divide line 7 by $50,000 (ny.tcw.phase), rounded to 4 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply column (scale) (line9_scaled) by the result.
- Interpretation: amb.ny.2025.fourth_decimal
- Expr: `{"amount":"line9_scaled","op":"prorate","part":"line7","places":4,"whole":{"param":"ny.tcw.phase"}}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "8. Divide line 7 by $50,000 and round the result to the fourth decimal place", "9. Multiply line 5 by line 8" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 9 — `line9`

- **IRS:** Multiply line 5 by line 8 (whole dollars)
- **Encoded (NonNegDollars):** Multiply line 8, 9 by 1% (0.01) (ny.hundredth), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"line9_exact","op":"multiply_rate","rate":{"param":"ny.hundredth"},"unit":100}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "8. Divide line 7 by $50,000 and round the result to the fourth decimal place", "9. Multiply line 5 by line 8" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## 10 — `tax`

- **IRS:** Add lines 3, 4, and 9. Enter here and on line 39.
- **Encoded (NonNegDollars):** Add line 3, line 4, and line 9.
- Expr: `{"of":["line3","recapture","line9"],"op":"sum"}`
- Cite: [ny_it201i-html] Tax computation worksheet 2, "10. Add lines 3, 4, and 9. Enter here and on line 39." (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)
