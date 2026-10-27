# Tax Computation Worksheet—Line 16

- Document: `tcw` (def, tax year 2025)
- Parameters: amount, status

## (a) — `amount`

- **Authored helper label:** Enter the amount from line 15
- **Encoded (NonNegDollars):** Input — Bound by the calling line (the amount whose tax is computed).
- Expr: `{"op":"input","source":"Bound by the calling line (the amount whose tax is computed)."}`
- Cite: [i1040gi] TCW, column (a) (2025; printed date 2026-02-25; sha256 482e9c48)

## (status) — `status`

- **Authored helper label:** Use the section for your filing status
- **Encoded (Enum(filing_status)):** Input — Bound by the calling line (Form 1040 filing status).
- Expr: `{"op":"input","source":"Bound by the calling line (Form 1040 filing status)."}`
- Cite: [i1040gi] TCW, sections A-D (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply column (a) by 22% (0.22) (tcw.single.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b1.rate"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 1, "At least $100,000 but not over $103,350", "(c) Multiply (a) by (b)", "× 22% (0.22)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.row1.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $5,086 (tcw.single.b1.subtract) from column (c) (single.row1.product).
- Expr: `{"from":"single.row1.product","op":"subtract","take":{"param":"tcw.single.b1.subtract"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 1, "At least $100,000 but not over $103,350", "$ 5,086.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply column (a) by 24% (0.24) (tcw.single.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b2.rate"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 2, "Over $103,350 but not over $197,300", "(c) Multiply (a) by (b)", "× 24% (0.24)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.row2.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $7,153 (tcw.single.b2.subtract) from column (c) (single.row2.product).
- Expr: `{"from":"single.row2.product","op":"subtract","take":{"param":"tcw.single.b2.subtract"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 2, "Over $103,350 but not over $197,300", "$ 7,153.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply column (a) by 32% (0.32) (tcw.single.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b3.rate"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 3, "Over $197,300 but not over $250,525", "(c) Multiply (a) by (b)", "× 32% (0.32)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.row3.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $22,937 (tcw.single.b3.subtract) from column (c) (single.row3.product).
- Expr: `{"from":"single.row3.product","op":"subtract","take":{"param":"tcw.single.b3.subtract"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 3, "Over $197,300 but not over $250,525", "$ 22,937.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply column (a) by 35% (0.35) (tcw.single.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b4.rate"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 4, "Over $250,525 but not over $626,350", "(c) Multiply (a) by (b)", "× 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.row4.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $30,452.75 (tcw.single.b4.subtract) from column (c) (single.row4.product).
- Expr: `{"from":"single.row4.product","op":"subtract","take":{"param":"tcw.single.b4.subtract"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 4, "Over $250,525 but not over $626,350", "$ 30,452.75", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply column (a) by 37% (0.37) (tcw.single.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b5.rate"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 5, "Over $626,350", "(c) Multiply (a) by (b)", "× 37% (0.37)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.row5.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $42,979.75 (tcw.single.b5.subtract) from column (c) (single.row5.product).
- Expr: `{"from":"single.row5.product","op":"subtract","take":{"param":"tcw.single.b5.subtract"}}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, row 5, "Over $626,350", "$ 42,979.75", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.result`

- **IRS:** Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [column (a) ≥ $100,000 (ordinary.table_boundary) and column (a) ≤ $103,350 (tcw.single.b1.upper) → line Tax (single.row1.tax)] [column (a) > $103,350 (tcw.single.b1.upper) and column (a) ≤ $197,300 (tcw.single.b2.upper) → line Tax (single.row2.tax)] [column (a) > $197,300 (tcw.single.b2.upper) and column (a) ≤ $250,525 (tcw.single.b3.upper) → line Tax (single.row3.tax)] [column (a) > $250,525 (tcw.single.b3.upper) and column (a) ≤ $626,350 (tcw.single.b4.upper) → line Tax (single.row4.tax)] [column (a) > $626,350 (tcw.single.b4.upper) → line Tax (single.row5.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"le":["amount",{"param":"tcw.single.b1.upper"}],"op":"test"}],"op":"test"},"then":"single.row1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.single.b1.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.single.b2.upper"}],"op":"test"}],"op":"test"},"then":"single.row2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.single.b2.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.single.b3.upper"}],"op":"test"}],"op":"test"},"then":"single.row3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.single.b3.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.single.b4.upper"}],"op":"test"}],"op":"test"},"then":"single.row4.tax"},{"guard":{"gt":["amount",{"param":"tcw.single.b4.upper"}],"op":"test"},"then":"single.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] p. 80, Section A—Use if your filing status is Single, "Complete the row below that applies to you", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply column (a) by 22% (0.22) (tcw.mfj.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b1.rate"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 1, "At least $100,000 but not over $206,700", "(c) Multiply (a) by (b)", "× 22% (0.22)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.row1.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $10,172 (tcw.mfj.b1.subtract) from column (c) (mfj.row1.product).
- Expr: `{"from":"mfj.row1.product","op":"subtract","take":{"param":"tcw.mfj.b1.subtract"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 1, "At least $100,000 but not over $206,700", "$ 10,172.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply column (a) by 24% (0.24) (tcw.mfj.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b2.rate"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 2, "Over $206,700 but not over $394,600", "(c) Multiply (a) by (b)", "× 24% (0.24)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.row2.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $14,306 (tcw.mfj.b2.subtract) from column (c) (mfj.row2.product).
- Expr: `{"from":"mfj.row2.product","op":"subtract","take":{"param":"tcw.mfj.b2.subtract"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 2, "Over $206,700 but not over $394,600", "$ 14,306.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply column (a) by 32% (0.32) (tcw.mfj.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b3.rate"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 3, "Over $394,600 but not over $501,050", "(c) Multiply (a) by (b)", "× 32% (0.32)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.row3.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $45,874 (tcw.mfj.b3.subtract) from column (c) (mfj.row3.product).
- Expr: `{"from":"mfj.row3.product","op":"subtract","take":{"param":"tcw.mfj.b3.subtract"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 3, "Over $394,600 but not over $501,050", "$ 45,874.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply column (a) by 35% (0.35) (tcw.mfj.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b4.rate"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 4, "Over $501,050 but not over $751,600", "(c) Multiply (a) by (b)", "× 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.row4.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $60,905.50 (tcw.mfj.b4.subtract) from column (c) (mfj.row4.product).
- Expr: `{"from":"mfj.row4.product","op":"subtract","take":{"param":"tcw.mfj.b4.subtract"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 4, "Over $501,050 but not over $751,600", "$ 60,905.50", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply column (a) by 37% (0.37) (tcw.mfj.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b5.rate"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 5, "Over $751,600", "(c) Multiply (a) by (b)", "× 37% (0.37)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.row5.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $75,937.50 (tcw.mfj.b5.subtract) from column (c) (mfj.row5.product).
- Expr: `{"from":"mfj.row5.product","op":"subtract","take":{"param":"tcw.mfj.b5.subtract"}}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, row 5, "Over $751,600", "$ 75,937.50", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.result`

- **IRS:** Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [column (a) ≥ $100,000 (ordinary.table_boundary) and column (a) ≤ $206,700 (tcw.mfj.b1.upper) → line Tax (mfj.row1.tax)] [column (a) > $206,700 (tcw.mfj.b1.upper) and column (a) ≤ $394,600 (tcw.mfj.b2.upper) → line Tax (mfj.row2.tax)] [column (a) > $394,600 (tcw.mfj.b2.upper) and column (a) ≤ $501,050 (tcw.mfj.b3.upper) → line Tax (mfj.row3.tax)] [column (a) > $501,050 (tcw.mfj.b3.upper) and column (a) ≤ $751,600 (tcw.mfj.b4.upper) → line Tax (mfj.row4.tax)] [column (a) > $751,600 (tcw.mfj.b4.upper) → line Tax (mfj.row5.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"le":["amount",{"param":"tcw.mfj.b1.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.mfj.b1.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.mfj.b2.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.mfj.b2.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.mfj.b3.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.mfj.b3.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.mfj.b4.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row4.tax"},{"guard":{"gt":["amount",{"param":"tcw.mfj.b4.upper"}],"op":"test"},"then":"mfj.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] p. 80, Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse, "Complete the row below that applies to you", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply column (a) by 22% (0.22) (tcw.mfs.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b1.rate"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 1, "At least $100,000 but not over $103,350", "(c) Multiply (a) by (b)", "× 22% (0.22)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.row1.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $5,086 (tcw.mfs.b1.subtract) from column (c) (mfs.row1.product).
- Expr: `{"from":"mfs.row1.product","op":"subtract","take":{"param":"tcw.mfs.b1.subtract"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 1, "At least $100,000 but not over $103,350", "$ 5,086.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply column (a) by 24% (0.24) (tcw.mfs.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b2.rate"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 2, "Over $103,350 but not over $197,300", "(c) Multiply (a) by (b)", "× 24% (0.24)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.row2.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $7,153 (tcw.mfs.b2.subtract) from column (c) (mfs.row2.product).
- Expr: `{"from":"mfs.row2.product","op":"subtract","take":{"param":"tcw.mfs.b2.subtract"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 2, "Over $103,350 but not over $197,300", "$ 7,153.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply column (a) by 32% (0.32) (tcw.mfs.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b3.rate"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 3, "Over $197,300 but not over $250,525", "(c) Multiply (a) by (b)", "× 32% (0.32)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.row3.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $22,937 (tcw.mfs.b3.subtract) from column (c) (mfs.row3.product).
- Expr: `{"from":"mfs.row3.product","op":"subtract","take":{"param":"tcw.mfs.b3.subtract"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 3, "Over $197,300 but not over $250,525", "$ 22,937.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply column (a) by 35% (0.35) (tcw.mfs.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b4.rate"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 4, "Over $250,525 but not over $375,800", "(c) Multiply (a) by (b)", "× 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.row4.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $30,452.75 (tcw.mfs.b4.subtract) from column (c) (mfs.row4.product).
- Expr: `{"from":"mfs.row4.product","op":"subtract","take":{"param":"tcw.mfs.b4.subtract"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 4, "Over $250,525 but not over $375,800", "$ 30,452.75", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply column (a) by 37% (0.37) (tcw.mfs.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b5.rate"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 5, "Over $375,800", "(c) Multiply (a) by (b)", "× 37% (0.37)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.row5.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $37,968.75 (tcw.mfs.b5.subtract) from column (c) (mfs.row5.product).
- Expr: `{"from":"mfs.row5.product","op":"subtract","take":{"param":"tcw.mfs.b5.subtract"}}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, row 5, "Over $375,800", "$ 37,968.75", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.result`

- **IRS:** Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [column (a) ≥ $100,000 (ordinary.table_boundary) and column (a) ≤ $103,350 (tcw.mfs.b1.upper) → line Tax (mfs.row1.tax)] [column (a) > $103,350 (tcw.mfs.b1.upper) and column (a) ≤ $197,300 (tcw.mfs.b2.upper) → line Tax (mfs.row2.tax)] [column (a) > $197,300 (tcw.mfs.b2.upper) and column (a) ≤ $250,525 (tcw.mfs.b3.upper) → line Tax (mfs.row3.tax)] [column (a) > $250,525 (tcw.mfs.b3.upper) and column (a) ≤ $375,800 (tcw.mfs.b4.upper) → line Tax (mfs.row4.tax)] [column (a) > $375,800 (tcw.mfs.b4.upper) → line Tax (mfs.row5.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"le":["amount",{"param":"tcw.mfs.b1.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.mfs.b1.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.mfs.b2.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.mfs.b2.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.mfs.b3.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.mfs.b3.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.mfs.b4.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row4.tax"},{"guard":{"gt":["amount",{"param":"tcw.mfs.b4.upper"}],"op":"test"},"then":"mfs.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] p. 80, Section C—Use if your filing status is Married filing separately, "Complete the row below that applies to you", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply column (a) by 22% (0.22) (tcw.hoh.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b1.rate"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 1, "At least $100,000 but not over $103,350", "(c) Multiply (a) by (b)", "× 22% (0.22)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.row1.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $6,825 (tcw.hoh.b1.subtract) from column (c) (hoh.row1.product).
- Expr: `{"from":"hoh.row1.product","op":"subtract","take":{"param":"tcw.hoh.b1.subtract"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 1, "At least $100,000 but not over $103,350", "$ 6,825.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply column (a) by 24% (0.24) (tcw.hoh.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b2.rate"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 2, "Over $103,350 but not over $197,300", "(c) Multiply (a) by (b)", "× 24% (0.24)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.row2.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $8,892 (tcw.hoh.b2.subtract) from column (c) (hoh.row2.product).
- Expr: `{"from":"hoh.row2.product","op":"subtract","take":{"param":"tcw.hoh.b2.subtract"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 2, "Over $103,350 but not over $197,300", "$ 8,892.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply column (a) by 32% (0.32) (tcw.hoh.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b3.rate"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 3, "Over $197,300 but not over $250,500", "(c) Multiply (a) by (b)", "× 32% (0.32)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.row3.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $24,676 (tcw.hoh.b3.subtract) from column (c) (hoh.row3.product).
- Expr: `{"from":"hoh.row3.product","op":"subtract","take":{"param":"tcw.hoh.b3.subtract"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 3, "Over $197,300 but not over $250,500", "$ 24,676.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply column (a) by 35% (0.35) (tcw.hoh.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b4.rate"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 4, "Over $250,500 but not over $626,350", "(c) Multiply (a) by (b)", "× 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.row4.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $32,191 (tcw.hoh.b4.subtract) from column (c) (hoh.row4.product).
- Expr: `{"from":"hoh.row4.product","op":"subtract","take":{"param":"tcw.hoh.b4.subtract"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 4, "Over $250,500 but not over $626,350", "$ 32,191.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply column (a) by 37% (0.37) (tcw.hoh.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b5.rate"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 5, "Over $626,350", "(c) Multiply (a) by (b)", "× 37% (0.37)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.row5.tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Subtract $44,718 (tcw.hoh.b5.subtract) from column (c) (hoh.row5.product).
- Expr: `{"from":"hoh.row5.product","op":"subtract","take":{"param":"tcw.hoh.b5.subtract"}}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, row 5, "Over $626,350", "$ 44,718.00", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.result`

- **IRS:** Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [column (a) ≥ $100,000 (ordinary.table_boundary) and column (a) ≤ $103,350 (tcw.hoh.b1.upper) → line Tax (hoh.row1.tax)] [column (a) > $103,350 (tcw.hoh.b1.upper) and column (a) ≤ $197,300 (tcw.hoh.b2.upper) → line Tax (hoh.row2.tax)] [column (a) > $197,300 (tcw.hoh.b2.upper) and column (a) ≤ $250,500 (tcw.hoh.b3.upper) → line Tax (hoh.row3.tax)] [column (a) > $250,500 (tcw.hoh.b3.upper) and column (a) ≤ $626,350 (tcw.hoh.b4.upper) → line Tax (hoh.row4.tax)] [column (a) > $626,350 (tcw.hoh.b4.upper) → line Tax (hoh.row5.tax)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"le":["amount",{"param":"tcw.hoh.b1.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row1.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.hoh.b1.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.hoh.b2.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row2.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.hoh.b2.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.hoh.b3.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row3.tax"},{"guard":{"all":[{"gt":["amount",{"param":"tcw.hoh.b3.upper"}],"op":"test"},{"le":["amount",{"param":"tcw.hoh.b4.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row4.tax"},{"guard":{"gt":["amount",{"param":"tcw.hoh.b4.upper"}],"op":"test"},"then":"hoh.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] p. 80, Section D—Use if your filing status is Head of household, "Complete the row below that applies to you", "Tax. Subtract (d) from (c)" (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [helper "Use the section for your filing status" = 'single' → line Tax (single.result)] [helper "Use the section for your filing status" = 'mfj' → line Tax (mfj.result)] [helper "Use the section for your filing status" = 'qss' → line Tax (mfj.result)] [helper "Use the section for your filing status" = 'mfs' → line Tax (mfs.result)] [helper "Use the section for your filing status" = 'hoh' → line Tax (hoh.result)]
- Expr: `{"alternatives":[{"guard":{"eq":["status",{"const":"single"}],"op":"test"},"then":"single.result"},{"guard":{"eq":["status",{"const":"mfj"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"qss"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"mfs"}],"op":"test"},"then":"mfs.result"},{"guard":{"eq":["status",{"const":"hoh"}],"op":"test"},"then":"hoh.result"}],"op":"choose"}`
- Cite: [i1040gi] p. 80, 2025 Tax Computation Worksheet—Line 16, "Section A—Use if your filing status is Single", "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse", "Section C—Use if your filing status is Married filing separately", "Section D—Use if your filing status is Head of household" (2025; printed date 2026-02-25; sha256 482e9c48)
