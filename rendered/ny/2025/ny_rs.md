# New York State tax rate schedule

- Document: `ny_rs` (def, tax year 2025)
- Parameters: amount, status

## (line 38) — `amount`

- **Authored helper label:** Taxable income (line 38)
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the taxable income whose tax is computed).
- Expr: `{"op":"input","source":"Bound by the calling line (the taxable income whose tax is computed)."}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "If line 38 is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (status) — `status`

- **Authored helper label:** Use the schedule for your filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (the federal filing status, IT-201 item A).
- Expr: `{"op":"input","source":"Bound by the calling line (the federal filing status, IT-201 item A)."}`
- Cite: [ny_it201i] p. 4, Item A, "In most cases, you must use the same filing status you used on your federal return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (band 1) — `single.b1.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $0 (ny.rs.single.b1.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b1.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `single.b1.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 1) (single.b1.excess) by 4% (0.04) (ny.rs.b1.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b1.excess","op":"multiply_rate","rate":{"param":"ny.rs.b1.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `single.b1.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $0 (ny.rs.single.b1.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b1.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b1.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 1) (single.b1.base) and column (band 1) (single.b1.product).
- Expr: `{"of":["single.b1.base","single.b1.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `single.b2.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $8,500 (ny.rs.single.b2.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b2.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `single.b2.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 2) (single.b2.excess) by 45/1000 (ny.rs.b2.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b2.excess","op":"multiply_rate","rate":{"param":"ny.rs.b2.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `single.b2.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $340 (ny.rs.single.b2.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b2.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b2.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 2) (single.b2.base) and column (band 2) (single.b2.product).
- Expr: `{"of":["single.b2.base","single.b2.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `single.b3.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $11,700 (ny.rs.single.b3.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b3.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `single.b3.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 3) (single.b3.excess) by 525/10000 (ny.rs.b3.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b3.excess","op":"multiply_rate","rate":{"param":"ny.rs.b3.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `single.b3.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $484 (ny.rs.single.b3.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b3.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b3.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 3) (single.b3.base) and column (band 3) (single.b3.product).
- Expr: `{"of":["single.b3.base","single.b3.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `single.b4.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $13,900 (ny.rs.single.b4.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b4.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `single.b4.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 4) (single.b4.excess) by 55/1000 (ny.rs.b4.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b4.excess","op":"multiply_rate","rate":{"param":"ny.rs.b4.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `single.b4.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $600 (ny.rs.single.b4.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b4.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b4.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 4) (single.b4.base) and column (band 4) (single.b4.product).
- Expr: `{"of":["single.b4.base","single.b4.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `single.b5.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $80,650 (ny.rs.single.b5.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b5.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `single.b5.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 5) (single.b5.excess) by 6% (0.06) (ny.rs.b5.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b5.excess","op":"multiply_rate","rate":{"param":"ny.rs.b5.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `single.b5.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $4,271 (ny.rs.single.b5.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b5.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b5.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 5) (single.b5.base) and column (band 5) (single.b5.product).
- Expr: `{"of":["single.b5.base","single.b5.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `single.b6.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $215,400 (ny.rs.single.b6.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b6.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `single.b6.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 6) (single.b6.excess) by 685/10000 (ny.rs.b6.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b6.excess","op":"multiply_rate","rate":{"param":"ny.rs.b6.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `single.b6.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $12,356 (ny.rs.single.b6.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b6.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b6.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 6) (single.b6.base) and column (band 6) (single.b6.product).
- Expr: `{"of":["single.b6.base","single.b6.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `single.b7.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $1,077,550 (ny.rs.single.b7.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b7.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `single.b7.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 7) (single.b7.excess) by 965/10000 (ny.rs.b7.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b7.excess","op":"multiply_rate","rate":{"param":"ny.rs.b7.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `single.b7.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $71,413 (ny.rs.single.b7.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b7.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b7.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 7) (single.b7.base) and column (band 7) (single.b7.product).
- Expr: `{"of":["single.b7.base","single.b7.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `single.b8.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $5,000,000 (ny.rs.single.b8.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b8.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `single.b8.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 8) (single.b8.excess) by 103/1000 (ny.rs.b8.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b8.excess","op":"multiply_rate","rate":{"param":"ny.rs.b8.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `single.b8.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $449,929 (ny.rs.single.b8.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b8.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b8.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 8) (single.b8.base) and column (band 8) (single.b8.product).
- Expr: `{"of":["single.b8.base","single.b8.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `single.b9.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $25,000,000 (ny.rs.single.b9.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.single.b9.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `single.b9.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 9) (single.b9.excess) by 109/1000 (ny.rs.b9.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b9.excess","op":"multiply_rate","rate":{"param":"ny.rs.b9.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `single.b9.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $2,509,929 (ny.rs.single.b9.base).
- Expr: `{"op":"param","ref":"ny.rs.single.b9.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b9.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 9) (single.b9.base) and column (band 9) (single.b9.product).
- Expr: `{"of":["single.b9.base","single.b9.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.result`

- **IRS:** Single and married filing separately—filing status ① and ③: the tax for the band that holds the amount
- **Encoded (NonNegDollars):** Choose — [column (line 38) ≥ $0 and column (line 38) ≤ $8,500 (ny.rs.single.b1.upper) → line The tax is (single.b1.tax)] [column (line 38) > $8,500 (ny.rs.single.b1.upper) and column (line 38) ≤ $11,700 (ny.rs.single.b2.upper) → line The tax is (single.b2.tax)] [column (line 38) > $11,700 (ny.rs.single.b2.upper) and column (line 38) ≤ $13,900 (ny.rs.single.b3.upper) → line The tax is (single.b3.tax)] [column (line 38) > $13,900 (ny.rs.single.b3.upper) and column (line 38) ≤ $80,650 (ny.rs.single.b4.upper) → line The tax is (single.b4.tax)] [column (line 38) > $80,650 (ny.rs.single.b4.upper) and column (line 38) ≤ $215,400 (ny.rs.single.b5.upper) → line The tax is (single.b5.tax)] [column (line 38) > $215,400 (ny.rs.single.b5.upper) and column (line 38) ≤ $1,077,550 (ny.rs.single.b6.upper) → line The tax is (single.b6.tax)] [column (line 38) > $1,077,550 (ny.rs.single.b6.upper) and column (line 38) ≤ $5,000,000 (ny.rs.single.b7.upper) → line The tax is (single.b7.tax)] [column (line 38) > $5,000,000 (ny.rs.single.b7.upper) and column (line 38) ≤ $25,000,000 (ny.rs.single.b8.upper) → line The tax is (single.b8.tax)] [column (line 38) > $25,000,000 (ny.rs.single.b8.upper) → line The tax is (single.b9.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"const":0}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b1.upper"}],"op":"test"}],"op":"test"},"then":"single.b1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b1.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b2.upper"}],"op":"test"}],"op":"test"},"then":"single.b2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b2.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b3.upper"}],"op":"test"}],"op":"test"},"then":"single.b3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b3.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b4.upper"}],"op":"test"}],"op":"test"},"then":"single.b4.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b4.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b5.upper"}],"op":"test"}],"op":"test"},"then":"single.b5.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b5.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b6.upper"}],"op":"test"}],"op":"test"},"then":"single.b6.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b6.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b7.upper"}],"op":"test"}],"op":"test"},"then":"single.b7.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.single.b7.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.single.b8.upper"}],"op":"test"}],"op":"test"},"then":"single.b8.tax"},{"guard":{"gt":["amount",{"param":"ny.rs.single.b8.upper"}],"op":"test"},"then":"single.b9.tax"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Single and married filing separately—filing status ① and ③", "If line 38 is:", "over", "but not over" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `mfj.b1.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $0 (ny.rs.mfj.b1.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b1.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `mfj.b1.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 1) (mfj.b1.excess) by 4% (0.04) (ny.rs.b1.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b1.excess","op":"multiply_rate","rate":{"param":"ny.rs.b1.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `mfj.b1.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $0 (ny.rs.mfj.b1.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b1.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b1.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 1) (mfj.b1.base) and column (band 1) (mfj.b1.product).
- Expr: `{"of":["mfj.b1.base","mfj.b1.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `mfj.b2.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $17,150 (ny.rs.mfj.b2.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b2.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `mfj.b2.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 2) (mfj.b2.excess) by 45/1000 (ny.rs.b2.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b2.excess","op":"multiply_rate","rate":{"param":"ny.rs.b2.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `mfj.b2.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $686 (ny.rs.mfj.b2.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b2.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b2.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 2) (mfj.b2.base) and column (band 2) (mfj.b2.product).
- Expr: `{"of":["mfj.b2.base","mfj.b2.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `mfj.b3.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $23,600 (ny.rs.mfj.b3.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b3.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `mfj.b3.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 3) (mfj.b3.excess) by 525/10000 (ny.rs.b3.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b3.excess","op":"multiply_rate","rate":{"param":"ny.rs.b3.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `mfj.b3.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $976 (ny.rs.mfj.b3.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b3.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b3.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 3) (mfj.b3.base) and column (band 3) (mfj.b3.product).
- Expr: `{"of":["mfj.b3.base","mfj.b3.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `mfj.b4.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $27,900 (ny.rs.mfj.b4.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b4.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `mfj.b4.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 4) (mfj.b4.excess) by 55/1000 (ny.rs.b4.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b4.excess","op":"multiply_rate","rate":{"param":"ny.rs.b4.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `mfj.b4.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $1,202 (ny.rs.mfj.b4.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b4.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b4.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 4) (mfj.b4.base) and column (band 4) (mfj.b4.product).
- Expr: `{"of":["mfj.b4.base","mfj.b4.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `mfj.b5.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $161,550 (ny.rs.mfj.b5.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b5.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `mfj.b5.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 5) (mfj.b5.excess) by 6% (0.06) (ny.rs.b5.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b5.excess","op":"multiply_rate","rate":{"param":"ny.rs.b5.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `mfj.b5.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $8,553 (ny.rs.mfj.b5.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b5.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b5.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 5) (mfj.b5.base) and column (band 5) (mfj.b5.product).
- Expr: `{"of":["mfj.b5.base","mfj.b5.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `mfj.b6.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $323,200 (ny.rs.mfj.b6.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b6.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `mfj.b6.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 6) (mfj.b6.excess) by 685/10000 (ny.rs.b6.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b6.excess","op":"multiply_rate","rate":{"param":"ny.rs.b6.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `mfj.b6.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $18,252 (ny.rs.mfj.b6.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b6.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b6.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 6) (mfj.b6.base) and column (band 6) (mfj.b6.product).
- Expr: `{"of":["mfj.b6.base","mfj.b6.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `mfj.b7.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $2,155,350 (ny.rs.mfj.b7.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b7.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `mfj.b7.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 7) (mfj.b7.excess) by 965/10000 (ny.rs.b7.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b7.excess","op":"multiply_rate","rate":{"param":"ny.rs.b7.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `mfj.b7.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $143,754 (ny.rs.mfj.b7.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b7.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b7.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 7) (mfj.b7.base) and column (band 7) (mfj.b7.product).
- Expr: `{"of":["mfj.b7.base","mfj.b7.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `mfj.b8.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $5,000,000 (ny.rs.mfj.b8.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b8.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `mfj.b8.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 8) (mfj.b8.excess) by 103/1000 (ny.rs.b8.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b8.excess","op":"multiply_rate","rate":{"param":"ny.rs.b8.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `mfj.b8.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $418,263 (ny.rs.mfj.b8.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b8.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b8.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 8) (mfj.b8.base) and column (band 8) (mfj.b8.product).
- Expr: `{"of":["mfj.b8.base","mfj.b8.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `mfj.b9.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $25,000,000 (ny.rs.mfj.b9.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.mfj.b9.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `mfj.b9.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 9) (mfj.b9.excess) by 109/1000 (ny.rs.b9.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b9.excess","op":"multiply_rate","rate":{"param":"ny.rs.b9.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `mfj.b9.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $2,478,263 (ny.rs.mfj.b9.base).
- Expr: `{"op":"param","ref":"ny.rs.mfj.b9.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b9.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 9) (mfj.b9.base) and column (band 9) (mfj.b9.product).
- Expr: `{"of":["mfj.b9.base","mfj.b9.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.result`

- **IRS:** Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: the tax for the band that holds the amount
- **Encoded (NonNegDollars):** Choose — [column (line 38) ≥ $0 and column (line 38) ≤ $17,150 (ny.rs.mfj.b1.upper) → line The tax is (mfj.b1.tax)] [column (line 38) > $17,150 (ny.rs.mfj.b1.upper) and column (line 38) ≤ $23,600 (ny.rs.mfj.b2.upper) → line The tax is (mfj.b2.tax)] [column (line 38) > $23,600 (ny.rs.mfj.b2.upper) and column (line 38) ≤ $27,900 (ny.rs.mfj.b3.upper) → line The tax is (mfj.b3.tax)] [column (line 38) > $27,900 (ny.rs.mfj.b3.upper) and column (line 38) ≤ $161,550 (ny.rs.mfj.b4.upper) → line The tax is (mfj.b4.tax)] [column (line 38) > $161,550 (ny.rs.mfj.b4.upper) and column (line 38) ≤ $323,200 (ny.rs.mfj.b5.upper) → line The tax is (mfj.b5.tax)] [column (line 38) > $323,200 (ny.rs.mfj.b5.upper) and column (line 38) ≤ $2,155,350 (ny.rs.mfj.b6.upper) → line The tax is (mfj.b6.tax)] [column (line 38) > $2,155,350 (ny.rs.mfj.b6.upper) and column (line 38) ≤ $5,000,000 (ny.rs.mfj.b7.upper) → line The tax is (mfj.b7.tax)] [column (line 38) > $5,000,000 (ny.rs.mfj.b7.upper) and column (line 38) ≤ $25,000,000 (ny.rs.mfj.b8.upper) → line The tax is (mfj.b8.tax)] [column (line 38) > $25,000,000 (ny.rs.mfj.b8.upper) → line The tax is (mfj.b9.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"const":0}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b1.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b1.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b2.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b2.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b3.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b3.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b4.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b4.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b4.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b5.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b5.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b5.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b6.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b6.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b6.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b7.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b7.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.mfj.b7.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.mfj.b8.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b8.tax"},{"guard":{"gt":["amount",{"param":"ny.rs.mfj.b8.upper"}],"op":"test"},"then":"mfj.b9.tax"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", "If line 38 is:", "over", "but not over" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `hoh.b1.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $0 (ny.rs.hoh.b1.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b1.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `hoh.b1.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 1) (hoh.b1.excess) by 4% (0.04) (ny.rs.b1.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b1.excess","op":"multiply_rate","rate":{"param":"ny.rs.b1.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `hoh.b1.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $0 (ny.rs.hoh.b1.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b1.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b1.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 1) (hoh.b1.base) and column (band 1) (hoh.b1.product).
- Expr: `{"of":["hoh.b1.base","hoh.b1.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `hoh.b2.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $12,800 (ny.rs.hoh.b2.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b2.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `hoh.b2.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 2) (hoh.b2.excess) by 45/1000 (ny.rs.b2.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b2.excess","op":"multiply_rate","rate":{"param":"ny.rs.b2.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `hoh.b2.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $512 (ny.rs.hoh.b2.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b2.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b2.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 2) (hoh.b2.base) and column (band 2) (hoh.b2.product).
- Expr: `{"of":["hoh.b2.base","hoh.b2.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `hoh.b3.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $17,650 (ny.rs.hoh.b3.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b3.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `hoh.b3.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 3) (hoh.b3.excess) by 525/10000 (ny.rs.b3.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b3.excess","op":"multiply_rate","rate":{"param":"ny.rs.b3.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `hoh.b3.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $730 (ny.rs.hoh.b3.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b3.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b3.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 3) (hoh.b3.base) and column (band 3) (hoh.b3.product).
- Expr: `{"of":["hoh.b3.base","hoh.b3.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `hoh.b4.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $20,900 (ny.rs.hoh.b4.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b4.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `hoh.b4.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 4) (hoh.b4.excess) by 55/1000 (ny.rs.b4.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b4.excess","op":"multiply_rate","rate":{"param":"ny.rs.b4.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `hoh.b4.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $901 (ny.rs.hoh.b4.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b4.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b4.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 4) (hoh.b4.base) and column (band 4) (hoh.b4.product).
- Expr: `{"of":["hoh.b4.base","hoh.b4.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `hoh.b5.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $107,650 (ny.rs.hoh.b5.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b5.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `hoh.b5.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 5) (hoh.b5.excess) by 6% (0.06) (ny.rs.b5.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b5.excess","op":"multiply_rate","rate":{"param":"ny.rs.b5.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 5) — `hoh.b5.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $5,672 (ny.rs.hoh.b5.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b5.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b5.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 5) (hoh.b5.base) and column (band 5) (hoh.b5.product).
- Expr: `{"of":["hoh.b5.base","hoh.b5.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 5 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `hoh.b6.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $269,300 (ny.rs.hoh.b6.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b6.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `hoh.b6.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 6) (hoh.b6.excess) by 685/10000 (ny.rs.b6.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b6.excess","op":"multiply_rate","rate":{"param":"ny.rs.b6.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 6) — `hoh.b6.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $15,371 (ny.rs.hoh.b6.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b6.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b6.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 6) (hoh.b6.base) and column (band 6) (hoh.b6.product).
- Expr: `{"of":["hoh.b6.base","hoh.b6.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 6 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `hoh.b7.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $1,616,450 (ny.rs.hoh.b7.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b7.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `hoh.b7.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 7) (hoh.b7.excess) by 965/10000 (ny.rs.b7.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b7.excess","op":"multiply_rate","rate":{"param":"ny.rs.b7.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 7) — `hoh.b7.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $107,651 (ny.rs.hoh.b7.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b7.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b7.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 7) (hoh.b7.base) and column (band 7) (hoh.b7.product).
- Expr: `{"of":["hoh.b7.base","hoh.b7.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 7 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `hoh.b8.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $5,000,000 (ny.rs.hoh.b8.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b8.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `hoh.b8.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 8) (hoh.b8.excess) by 103/1000 (ny.rs.b8.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b8.excess","op":"multiply_rate","rate":{"param":"ny.rs.b8.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 8) — `hoh.b8.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $434,163 (ny.rs.hoh.b8.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b8.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b8.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 8) (hoh.b8.base) and column (band 8) (hoh.b8.product).
- Expr: `{"of":["hoh.b8.base","hoh.b8.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 8 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `hoh.b9.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $25,000,000 (ny.rs.hoh.b9.over) from column (line 38). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.rs.hoh.b9.over"}}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `hoh.b9.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 9) (hoh.b9.excess) by 109/1000 (ny.rs.b9.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b9.excess","op":"multiply_rate","rate":{"param":"ny.rs.b9.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 9) — `hoh.b9.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $2,494,163 (ny.rs.hoh.b9.base).
- Expr: `{"op":"param","ref":"ny.rs.hoh.b9.base"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b9.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 9) (hoh.b9.base) and column (band 9) (hoh.b9.product).
- Expr: `{"of":["hoh.b9.base","hoh.b9.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", band 9 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.result`

- **IRS:** Head of household—filing status ④: the tax for the band that holds the amount
- **Encoded (NonNegDollars):** Choose — [column (line 38) ≥ $0 and column (line 38) ≤ $12,800 (ny.rs.hoh.b1.upper) → line The tax is (hoh.b1.tax)] [column (line 38) > $12,800 (ny.rs.hoh.b1.upper) and column (line 38) ≤ $17,650 (ny.rs.hoh.b2.upper) → line The tax is (hoh.b2.tax)] [column (line 38) > $17,650 (ny.rs.hoh.b2.upper) and column (line 38) ≤ $20,900 (ny.rs.hoh.b3.upper) → line The tax is (hoh.b3.tax)] [column (line 38) > $20,900 (ny.rs.hoh.b3.upper) and column (line 38) ≤ $107,650 (ny.rs.hoh.b4.upper) → line The tax is (hoh.b4.tax)] [column (line 38) > $107,650 (ny.rs.hoh.b4.upper) and column (line 38) ≤ $269,300 (ny.rs.hoh.b5.upper) → line The tax is (hoh.b5.tax)] [column (line 38) > $269,300 (ny.rs.hoh.b5.upper) and column (line 38) ≤ $1,616,450 (ny.rs.hoh.b6.upper) → line The tax is (hoh.b6.tax)] [column (line 38) > $1,616,450 (ny.rs.hoh.b6.upper) and column (line 38) ≤ $5,000,000 (ny.rs.hoh.b7.upper) → line The tax is (hoh.b7.tax)] [column (line 38) > $5,000,000 (ny.rs.hoh.b7.upper) and column (line 38) ≤ $25,000,000 (ny.rs.hoh.b8.upper) → line The tax is (hoh.b8.tax)] [column (line 38) > $25,000,000 (ny.rs.hoh.b8.upper) → line The tax is (hoh.b9.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"const":0}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b1.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b1.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b2.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b2.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b3.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b3.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b4.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b4.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b4.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b5.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b5.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b5.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b6.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b6.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b6.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b7.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b7.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.rs.hoh.b7.upper"}],"op":"test"},{"le":["amount",{"param":"ny.rs.hoh.b8.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b8.tax"},{"guard":{"gt":["amount",{"param":"ny.rs.hoh.b8.upper"}],"op":"test"},"then":"hoh.b9.tax"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Head of household—filing status ④", "If line 38 is:", "over", "but not over" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `tax`

- **IRS:** The tax from the schedule for the filing status
- **Encoded (NonNegDollars):** Choose — [helper "Use the schedule for your filing status" = 'single' → line The tax is (single.result)] [helper "Use the schedule for your filing status" = 'mfj' → line The tax is (mfj.result)] [helper "Use the schedule for your filing status" = 'qss' → line The tax is (mfj.result)] [helper "Use the schedule for your filing status" = 'mfs' → line The tax is (single.result)] [helper "Use the schedule for your filing status" = 'hoh' → line The tax is (hoh.result)]
- Expr: `{"alternatives":[{"guard":{"eq":["status",{"const":"single"}],"op":"test"},"then":"single.result"},{"guard":{"eq":["status",{"const":"mfj"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"qss"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"mfs"}],"op":"test"},"then":"single.result"},{"guard":{"eq":["status",{"const":"hoh"}],"op":"test"},"then":"hoh.result"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York State tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", "Single and married filing separately—filing status ① and ③", "Head of household—filing status ④" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)
