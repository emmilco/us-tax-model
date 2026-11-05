# New York City tax rate schedule

- Document: `ny_city_rs` (def, tax year 2025)
- Parameters: amount, status

## (line 47) — `amount`

- **Authored helper label:** New York City taxable income (line 47)
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the taxable income whose tax is computed).
- Expr: `{"op":"input","source":"Bound by the calling line (the taxable income whose tax is computed)."}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "If line 47 is:" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (status) — `status`

- **Authored helper label:** Use the schedule for your filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (the federal filing status, IT-201 item A).
- Expr: `{"op":"input","source":"Bound by the calling line (the federal filing status, IT-201 item A)."}`
- Cite: [ny_it201i] p. 4, Item A, "In most cases, you must use the same filing status you used on your federal return." (Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20; sha256 29489d6e)

## (band 1) — `single.b1.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $0 (ny.city.single.b1.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.single.b1.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `single.b1.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 1) (single.b1.excess) by 3078/100000 (ny.city.b1.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b1.excess","op":"multiply_rate","rate":{"param":"ny.city.b1.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `single.b1.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $0 (ny.city.single.b1.base).
- Expr: `{"op":"param","ref":"ny.city.single.b1.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b1.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 1) (single.b1.base) and column (band 1) (single.b1.product).
- Expr: `{"of":["single.b1.base","single.b1.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `single.b2.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $12,000 (ny.city.single.b2.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.single.b2.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `single.b2.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 2) (single.b2.excess) by 3762/100000 (ny.city.b2.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b2.excess","op":"multiply_rate","rate":{"param":"ny.city.b2.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `single.b2.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $369 (ny.city.single.b2.base).
- Expr: `{"op":"param","ref":"ny.city.single.b2.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b2.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 2) (single.b2.base) and column (band 2) (single.b2.product).
- Expr: `{"of":["single.b2.base","single.b2.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `single.b3.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $25,000 (ny.city.single.b3.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.single.b3.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `single.b3.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 3) (single.b3.excess) by 3819/100000 (ny.city.b3.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b3.excess","op":"multiply_rate","rate":{"param":"ny.city.b3.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `single.b3.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $858 (ny.city.single.b3.base).
- Expr: `{"op":"param","ref":"ny.city.single.b3.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b3.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 3) (single.b3.base) and column (band 3) (single.b3.product).
- Expr: `{"of":["single.b3.base","single.b3.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `single.b4.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $50,000 (ny.city.single.b4.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.single.b4.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `single.b4.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 4) (single.b4.excess) by 3876/100000 (ny.city.b4.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"single.b4.excess","op":"multiply_rate","rate":{"param":"ny.city.b4.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `single.b4.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $1,813 (ny.city.single.b4.base).
- Expr: `{"op":"param","ref":"ny.city.single.b4.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.b4.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 4) (single.b4.base) and column (band 4) (single.b4.product).
- Expr: `{"of":["single.b4.base","single.b4.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `single.result`

- **IRS:** Single and married filing separately—filing status ① and ③: the tax for the band that holds the amount
- **Encoded (NonNegDollars):** Choose — [column (line 47) ≥ $0 and column (line 47) ≤ $12,000 (ny.city.single.b1.upper) → line The tax is (single.b1.tax)] [column (line 47) > $12,000 (ny.city.single.b1.upper) and column (line 47) ≤ $25,000 (ny.city.single.b2.upper) → line The tax is (single.b2.tax)] [column (line 47) > $25,000 (ny.city.single.b2.upper) and column (line 47) ≤ $50,000 (ny.city.single.b3.upper) → line The tax is (single.b3.tax)] [column (line 47) > $50,000 (ny.city.single.b3.upper) → line The tax is (single.b4.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"const":0}],"op":"test"},{"le":["amount",{"param":"ny.city.single.b1.upper"}],"op":"test"}],"op":"test"},"then":"single.b1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.city.single.b1.upper"}],"op":"test"},{"le":["amount",{"param":"ny.city.single.b2.upper"}],"op":"test"}],"op":"test"},"then":"single.b2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.city.single.b2.upper"}],"op":"test"},{"le":["amount",{"param":"ny.city.single.b3.upper"}],"op":"test"}],"op":"test"},"then":"single.b3.tax"},{"guard":{"gt":["amount",{"param":"ny.city.single.b3.upper"}],"op":"test"},"then":"single.b4.tax"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Single and married filing separately—filing status ① and ③", "If line 47 is:", "over", "but not over" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `mfj.b1.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $0 (ny.city.mfj.b1.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.mfj.b1.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `mfj.b1.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 1) (mfj.b1.excess) by 3078/100000 (ny.city.b1.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b1.excess","op":"multiply_rate","rate":{"param":"ny.city.b1.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `mfj.b1.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $0 (ny.city.mfj.b1.base).
- Expr: `{"op":"param","ref":"ny.city.mfj.b1.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b1.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 1) (mfj.b1.base) and column (band 1) (mfj.b1.product).
- Expr: `{"of":["mfj.b1.base","mfj.b1.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `mfj.b2.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $21,600 (ny.city.mfj.b2.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.mfj.b2.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `mfj.b2.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 2) (mfj.b2.excess) by 3762/100000 (ny.city.b2.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b2.excess","op":"multiply_rate","rate":{"param":"ny.city.b2.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `mfj.b2.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $665 (ny.city.mfj.b2.base).
- Expr: `{"op":"param","ref":"ny.city.mfj.b2.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b2.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 2) (mfj.b2.base) and column (band 2) (mfj.b2.product).
- Expr: `{"of":["mfj.b2.base","mfj.b2.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `mfj.b3.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $45,000 (ny.city.mfj.b3.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.mfj.b3.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `mfj.b3.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 3) (mfj.b3.excess) by 3819/100000 (ny.city.b3.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b3.excess","op":"multiply_rate","rate":{"param":"ny.city.b3.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `mfj.b3.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $1,545 (ny.city.mfj.b3.base).
- Expr: `{"op":"param","ref":"ny.city.mfj.b3.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b3.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 3) (mfj.b3.base) and column (band 3) (mfj.b3.product).
- Expr: `{"of":["mfj.b3.base","mfj.b3.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `mfj.b4.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $90,000 (ny.city.mfj.b4.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.mfj.b4.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `mfj.b4.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 4) (mfj.b4.excess) by 3876/100000 (ny.city.b4.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"mfj.b4.excess","op":"multiply_rate","rate":{"param":"ny.city.b4.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `mfj.b4.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $3,264 (ny.city.mfj.b4.base).
- Expr: `{"op":"param","ref":"ny.city.mfj.b4.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.b4.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 4) (mfj.b4.base) and column (band 4) (mfj.b4.product).
- Expr: `{"of":["mfj.b4.base","mfj.b4.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `mfj.result`

- **IRS:** Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: the tax for the band that holds the amount
- **Encoded (NonNegDollars):** Choose — [column (line 47) ≥ $0 and column (line 47) ≤ $21,600 (ny.city.mfj.b1.upper) → line The tax is (mfj.b1.tax)] [column (line 47) > $21,600 (ny.city.mfj.b1.upper) and column (line 47) ≤ $45,000 (ny.city.mfj.b2.upper) → line The tax is (mfj.b2.tax)] [column (line 47) > $45,000 (ny.city.mfj.b2.upper) and column (line 47) ≤ $90,000 (ny.city.mfj.b3.upper) → line The tax is (mfj.b3.tax)] [column (line 47) > $90,000 (ny.city.mfj.b3.upper) → line The tax is (mfj.b4.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"const":0}],"op":"test"},{"le":["amount",{"param":"ny.city.mfj.b1.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.city.mfj.b1.upper"}],"op":"test"},{"le":["amount",{"param":"ny.city.mfj.b2.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.city.mfj.b2.upper"}],"op":"test"},{"le":["amount",{"param":"ny.city.mfj.b3.upper"}],"op":"test"}],"op":"test"},"then":"mfj.b3.tax"},{"guard":{"gt":["amount",{"param":"ny.city.mfj.b3.upper"}],"op":"test"},"then":"mfj.b4.tax"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", "If line 47 is:", "over", "but not over" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `hoh.b1.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $0 (ny.city.hoh.b1.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.hoh.b1.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `hoh.b1.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 1) (hoh.b1.excess) by 3078/100000 (ny.city.b1.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b1.excess","op":"multiply_rate","rate":{"param":"ny.city.b1.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 1) — `hoh.b1.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $0 (ny.city.hoh.b1.base).
- Expr: `{"op":"param","ref":"ny.city.hoh.b1.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b1.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 1) (hoh.b1.base) and column (band 1) (hoh.b1.product).
- Expr: `{"of":["hoh.b1.base","hoh.b1.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 1 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `hoh.b2.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $14,400 (ny.city.hoh.b2.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.hoh.b2.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `hoh.b2.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 2) (hoh.b2.excess) by 3762/100000 (ny.city.b2.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b2.excess","op":"multiply_rate","rate":{"param":"ny.city.b2.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 2) — `hoh.b2.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $443 (ny.city.hoh.b2.base).
- Expr: `{"op":"param","ref":"ny.city.hoh.b2.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b2.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 2) (hoh.b2.base) and column (band 2) (hoh.b2.product).
- Expr: `{"of":["hoh.b2.base","hoh.b2.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 2 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `hoh.b3.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $30,000 (ny.city.hoh.b3.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.hoh.b3.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `hoh.b3.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 3) (hoh.b3.excess) by 3819/100000 (ny.city.b3.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b3.excess","op":"multiply_rate","rate":{"param":"ny.city.b3.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 3) — `hoh.b3.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $1,030 (ny.city.hoh.b3.base).
- Expr: `{"op":"param","ref":"ny.city.hoh.b3.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b3.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 3) (hoh.b3.base) and column (band 3) (hoh.b3.product).
- Expr: `{"of":["hoh.b3.base","hoh.b3.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 3 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `hoh.b4.excess`

- **Authored helper label:** The amount over the band's lower bound (the excess over)
- **Encoded (NonNegDollars):** Subtract $60,000 (ny.city.hoh.b4.over) from column (line 47). If zero or less, enter -0-.
- Expr: `{"from":"amount","op":"subtract_floor0","take":{"param":"ny.city.hoh.b4.over"}}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `hoh.b4.product`

- **Authored helper label:** Multiply the excess by the band's rate, rounded to the whole dollar
- **Encoded (NonNegDollars):** Multiply column (band 4) (hoh.b4.excess) by 3876/100000 (ny.city.b4.rate), rounded to the nearest multiple of $1 (half up).
- Interpretation: amb.ny.2025.whole_dollars
- Expr: `{"amount":"hoh.b4.excess","op":"multiply_rate","rate":{"param":"ny.city.b4.rate"},"unit":100}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## (band 4) — `hoh.b4.base`

- **Authored helper label:** The band's base amount
- **Encoded (NonNegDollars):** Enter $2,176 (ny.city.hoh.b4.base).
- Expr: `{"op":"param","ref":"ny.city.hoh.b4.base"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.b4.tax`

- **IRS:** The base amount plus the rate times the excess
- **Encoded (NonNegDollars):** Add column (band 4) (hoh.b4.base) and column (band 4) (hoh.b4.product).
- Expr: `{"of":["hoh.b4.base","hoh.b4.product"],"op":"sum"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", band 4 (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `hoh.result`

- **IRS:** Head of household—filing status ④: the tax for the band that holds the amount
- **Encoded (NonNegDollars):** Choose — [column (line 47) ≥ $0 and column (line 47) ≤ $14,400 (ny.city.hoh.b1.upper) → line The tax is (hoh.b1.tax)] [column (line 47) > $14,400 (ny.city.hoh.b1.upper) and column (line 47) ≤ $30,000 (ny.city.hoh.b2.upper) → line The tax is (hoh.b2.tax)] [column (line 47) > $30,000 (ny.city.hoh.b2.upper) and column (line 47) ≤ $60,000 (ny.city.hoh.b3.upper) → line The tax is (hoh.b3.tax)] [column (line 47) > $60,000 (ny.city.hoh.b3.upper) → line The tax is (hoh.b4.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"const":0}],"op":"test"},{"le":["amount",{"param":"ny.city.hoh.b1.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.city.hoh.b1.upper"}],"op":"test"},{"le":["amount",{"param":"ny.city.hoh.b2.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"ny.city.hoh.b2.upper"}],"op":"test"},{"le":["amount",{"param":"ny.city.hoh.b3.upper"}],"op":"test"}],"op":"test"},"then":"hoh.b3.tax"},{"guard":{"gt":["amount",{"param":"ny.city.hoh.b3.upper"}],"op":"test"},"then":"hoh.b4.tax"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Head of household—filing status ④", "If line 47 is:", "over", "but not over" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)

## The tax is — `tax`

- **IRS:** The tax from the schedule for the filing status
- **Encoded (NonNegDollars):** Choose — [helper "Use the schedule for your filing status" = 'single' → line The tax is (single.result)] [helper "Use the schedule for your filing status" = 'mfj' → line The tax is (mfj.result)] [helper "Use the schedule for your filing status" = 'qss' → line The tax is (mfj.result)] [helper "Use the schedule for your filing status" = 'mfs' → line The tax is (single.result)] [helper "Use the schedule for your filing status" = 'hoh' → line The tax is (hoh.result)]
- Expr: `{"alternatives":[{"guard":{"eq":["status",{"const":"single"}],"op":"test"},"then":"single.result"},{"guard":{"eq":["status",{"const":"mfj"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"qss"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"mfs"}],"op":"test"},"then":"single.result"},{"guard":{"eq":["status",{"const":"hoh"}],"op":"test"},"then":"hoh.result"}],"op":"choose"}`
- Cite: [ny_it201i-html] New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤", "Single and married filing separately—filing status ① and ③", "Head of household—filing status ④" (Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny); sha256 b866b238)
