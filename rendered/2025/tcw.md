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
- **Encoded (NonNegDollars):** Multiply line (a) by 22% (0.22) (tcw.single.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b1.rate"}}`
- Cite: [i1040gi] TCW Section A, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `single.row1.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $5,086 (tcw.single.b1.subtract) from line (c).
- Expr: `{"from":"single.row1.product","op":"subtract","take":{"param":"tcw.single.b1.subtract"}}`
- Cite: [i1040gi] TCW Section A, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply line (a) by 24% (0.24) (tcw.single.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b2.rate"}}`
- Cite: [i1040gi] TCW Section A, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `single.row2.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $7,153 (tcw.single.b2.subtract) from line (c).
- Expr: `{"from":"single.row2.product","op":"subtract","take":{"param":"tcw.single.b2.subtract"}}`
- Cite: [i1040gi] TCW Section A, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply line (a) by 32% (0.32) (tcw.single.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b3.rate"}}`
- Cite: [i1040gi] TCW Section A, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `single.row3.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $22,937 (tcw.single.b3.subtract) from line (c).
- Expr: `{"from":"single.row3.product","op":"subtract","take":{"param":"tcw.single.b3.subtract"}}`
- Cite: [i1040gi] TCW Section A, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply line (a) by 35% (0.35) (tcw.single.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b4.rate"}}`
- Cite: [i1040gi] TCW Section A, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `single.row4.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $30,452.75 (tcw.single.b4.subtract) from line (c).
- Expr: `{"from":"single.row4.product","op":"subtract","take":{"param":"tcw.single.b4.subtract"}}`
- Cite: [i1040gi] TCW Section A, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `single.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply line (a) by 37% (0.37) (tcw.single.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.single.b5.rate"}}`
- Cite: [i1040gi] TCW Section A, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `single.row5.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $42,979.75 (tcw.single.b5.subtract) from line (c).
- Expr: `{"from":"single.row5.product","op":"subtract","take":{"param":"tcw.single.b5.subtract"}}`
- Cite: [i1040gi] TCW Section A, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `single.result`

- **IRS:** Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [line (a) ≥ $100,000 (ordinary.table_boundary) and line (a) < $103,350 (tcw.single.b1.upper) → line (d)] [line (a) ≥ $103,350 (tcw.single.b1.upper) and line (a) < $197,300 (tcw.single.b2.upper) → line (d)] [line (a) ≥ $197,300 (tcw.single.b2.upper) and line (a) < $250,525 (tcw.single.b3.upper) → line (d)] [line (a) ≥ $250,525 (tcw.single.b3.upper) and line (a) < $626,350 (tcw.single.b4.upper) → line (d)] [line (a) ≥ $626,350 (tcw.single.b4.upper) → line (d)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"lt":["amount",{"param":"tcw.single.b1.upper"}],"op":"test"}],"op":"test"},"then":"single.row1.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.single.b1.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.single.b2.upper"}],"op":"test"}],"op":"test"},"then":"single.row2.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.single.b2.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.single.b3.upper"}],"op":"test"}],"op":"test"},"then":"single.row3.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.single.b3.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.single.b4.upper"}],"op":"test"}],"op":"test"},"then":"single.row4.tax"},{"guard":{"ge":["amount",{"param":"tcw.single.b4.upper"}],"op":"test"},"then":"single.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] TCW Section A (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply line (a) by 22% (0.22) (tcw.mfj.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b1.rate"}}`
- Cite: [i1040gi] TCW Section B, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfj.row1.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $10,172 (tcw.mfj.b1.subtract) from line (c).
- Expr: `{"from":"mfj.row1.product","op":"subtract","take":{"param":"tcw.mfj.b1.subtract"}}`
- Cite: [i1040gi] TCW Section B, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply line (a) by 24% (0.24) (tcw.mfj.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b2.rate"}}`
- Cite: [i1040gi] TCW Section B, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfj.row2.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $14,306 (tcw.mfj.b2.subtract) from line (c).
- Expr: `{"from":"mfj.row2.product","op":"subtract","take":{"param":"tcw.mfj.b2.subtract"}}`
- Cite: [i1040gi] TCW Section B, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply line (a) by 32% (0.32) (tcw.mfj.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b3.rate"}}`
- Cite: [i1040gi] TCW Section B, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfj.row3.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $45,874 (tcw.mfj.b3.subtract) from line (c).
- Expr: `{"from":"mfj.row3.product","op":"subtract","take":{"param":"tcw.mfj.b3.subtract"}}`
- Cite: [i1040gi] TCW Section B, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply line (a) by 35% (0.35) (tcw.mfj.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b4.rate"}}`
- Cite: [i1040gi] TCW Section B, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfj.row4.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $60,905.50 (tcw.mfj.b4.subtract) from line (c).
- Expr: `{"from":"mfj.row4.product","op":"subtract","take":{"param":"tcw.mfj.b4.subtract"}}`
- Cite: [i1040gi] TCW Section B, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfj.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply line (a) by 37% (0.37) (tcw.mfj.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfj.b5.rate"}}`
- Cite: [i1040gi] TCW Section B, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfj.row5.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $75,937.50 (tcw.mfj.b5.subtract) from line (c).
- Expr: `{"from":"mfj.row5.product","op":"subtract","take":{"param":"tcw.mfj.b5.subtract"}}`
- Cite: [i1040gi] TCW Section B, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfj.result`

- **IRS:** Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [line (a) ≥ $100,000 (ordinary.table_boundary) and line (a) < $206,700 (tcw.mfj.b1.upper) → line (d)] [line (a) ≥ $206,700 (tcw.mfj.b1.upper) and line (a) < $394,600 (tcw.mfj.b2.upper) → line (d)] [line (a) ≥ $394,600 (tcw.mfj.b2.upper) and line (a) < $501,050 (tcw.mfj.b3.upper) → line (d)] [line (a) ≥ $501,050 (tcw.mfj.b3.upper) and line (a) < $751,600 (tcw.mfj.b4.upper) → line (d)] [line (a) ≥ $751,600 (tcw.mfj.b4.upper) → line (d)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfj.b1.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row1.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.mfj.b1.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfj.b2.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row2.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.mfj.b2.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfj.b3.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row3.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.mfj.b3.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfj.b4.upper"}],"op":"test"}],"op":"test"},"then":"mfj.row4.tax"},{"guard":{"ge":["amount",{"param":"tcw.mfj.b4.upper"}],"op":"test"},"then":"mfj.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] TCW Section B (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply line (a) by 22% (0.22) (tcw.mfs.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b1.rate"}}`
- Cite: [i1040gi] TCW Section C, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfs.row1.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $5,086 (tcw.mfs.b1.subtract) from line (c).
- Expr: `{"from":"mfs.row1.product","op":"subtract","take":{"param":"tcw.mfs.b1.subtract"}}`
- Cite: [i1040gi] TCW Section C, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply line (a) by 24% (0.24) (tcw.mfs.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b2.rate"}}`
- Cite: [i1040gi] TCW Section C, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfs.row2.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $7,153 (tcw.mfs.b2.subtract) from line (c).
- Expr: `{"from":"mfs.row2.product","op":"subtract","take":{"param":"tcw.mfs.b2.subtract"}}`
- Cite: [i1040gi] TCW Section C, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply line (a) by 32% (0.32) (tcw.mfs.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b3.rate"}}`
- Cite: [i1040gi] TCW Section C, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfs.row3.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $22,937 (tcw.mfs.b3.subtract) from line (c).
- Expr: `{"from":"mfs.row3.product","op":"subtract","take":{"param":"tcw.mfs.b3.subtract"}}`
- Cite: [i1040gi] TCW Section C, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply line (a) by 35% (0.35) (tcw.mfs.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b4.rate"}}`
- Cite: [i1040gi] TCW Section C, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfs.row4.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $30,452.75 (tcw.mfs.b4.subtract) from line (c).
- Expr: `{"from":"mfs.row4.product","op":"subtract","take":{"param":"tcw.mfs.b4.subtract"}}`
- Cite: [i1040gi] TCW Section C, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `mfs.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply line (a) by 37% (0.37) (tcw.mfs.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.mfs.b5.rate"}}`
- Cite: [i1040gi] TCW Section C, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `mfs.row5.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $37,968.75 (tcw.mfs.b5.subtract) from line (c).
- Expr: `{"from":"mfs.row5.product","op":"subtract","take":{"param":"tcw.mfs.b5.subtract"}}`
- Cite: [i1040gi] TCW Section C, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `mfs.result`

- **IRS:** Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [line (a) ≥ $100,000 (ordinary.table_boundary) and line (a) < $103,350 (tcw.mfs.b1.upper) → line (d)] [line (a) ≥ $103,350 (tcw.mfs.b1.upper) and line (a) < $197,300 (tcw.mfs.b2.upper) → line (d)] [line (a) ≥ $197,300 (tcw.mfs.b2.upper) and line (a) < $250,525 (tcw.mfs.b3.upper) → line (d)] [line (a) ≥ $250,525 (tcw.mfs.b3.upper) and line (a) < $375,800 (tcw.mfs.b4.upper) → line (d)] [line (a) ≥ $375,800 (tcw.mfs.b4.upper) → line (d)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfs.b1.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row1.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.mfs.b1.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfs.b2.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row2.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.mfs.b2.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfs.b3.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row3.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.mfs.b3.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.mfs.b4.upper"}],"op":"test"}],"op":"test"},"then":"mfs.row4.tax"},{"guard":{"ge":["amount",{"param":"tcw.mfs.b4.upper"}],"op":"test"},"then":"mfs.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] TCW Section C (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row1.product`

- **Authored helper label:** Multiply line (a) by 22% (0.22)
- **Encoded (NonNegDollars):** Multiply line (a) by 22% (0.22) (tcw.hoh.b1.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b1.rate"}}`
- Cite: [i1040gi] TCW Section D, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `hoh.row1.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $6,825 (tcw.hoh.b1.subtract) from line (c).
- Expr: `{"from":"hoh.row1.product","op":"subtract","take":{"param":"tcw.hoh.b1.subtract"}}`
- Cite: [i1040gi] TCW Section D, row 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row2.product`

- **Authored helper label:** Multiply line (a) by 24% (0.24)
- **Encoded (NonNegDollars):** Multiply line (a) by 24% (0.24) (tcw.hoh.b2.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b2.rate"}}`
- Cite: [i1040gi] TCW Section D, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `hoh.row2.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $8,892 (tcw.hoh.b2.subtract) from line (c).
- Expr: `{"from":"hoh.row2.product","op":"subtract","take":{"param":"tcw.hoh.b2.subtract"}}`
- Cite: [i1040gi] TCW Section D, row 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row3.product`

- **Authored helper label:** Multiply line (a) by 32% (0.32)
- **Encoded (NonNegDollars):** Multiply line (a) by 32% (0.32) (tcw.hoh.b3.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b3.rate"}}`
- Cite: [i1040gi] TCW Section D, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `hoh.row3.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $24,676 (tcw.hoh.b3.subtract) from line (c).
- Expr: `{"from":"hoh.row3.product","op":"subtract","take":{"param":"tcw.hoh.b3.subtract"}}`
- Cite: [i1040gi] TCW Section D, row 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row4.product`

- **Authored helper label:** Multiply line (a) by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply line (a) by 35% (0.35) (tcw.hoh.b4.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b4.rate"}}`
- Cite: [i1040gi] TCW Section D, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `hoh.row4.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $32,191 (tcw.hoh.b4.subtract) from line (c).
- Expr: `{"from":"hoh.row4.product","op":"subtract","take":{"param":"tcw.hoh.b4.subtract"}}`
- Cite: [i1040gi] TCW Section D, row 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (c) — `hoh.row5.product`

- **Authored helper label:** Multiply line (a) by 37% (0.37)
- **Encoded (NonNegDollars):** Multiply line (a) by 37% (0.37) (tcw.hoh.b5.rate).
- Expr: `{"amount":"amount","op":"multiply_rate","rate":{"param":"tcw.hoh.b5.rate"}}`
- Cite: [i1040gi] TCW Section D, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (d) — `hoh.row5.tax`

- **Authored helper label:** Subtract (d) from (c)
- **Encoded (Dollars):** Subtract $44,718 (tcw.hoh.b5.subtract) from line (c).
- Expr: `{"from":"hoh.row5.product","op":"subtract","take":{"param":"tcw.hoh.b5.subtract"}}`
- Cite: [i1040gi] TCW Section D, row 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `hoh.result`

- **IRS:** Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [line (a) ≥ $100,000 (ordinary.table_boundary) and line (a) < $103,350 (tcw.hoh.b1.upper) → line (d)] [line (a) ≥ $103,350 (tcw.hoh.b1.upper) and line (a) < $197,300 (tcw.hoh.b2.upper) → line (d)] [line (a) ≥ $197,300 (tcw.hoh.b2.upper) and line (a) < $250,500 (tcw.hoh.b3.upper) → line (d)] [line (a) ≥ $250,500 (tcw.hoh.b3.upper) and line (a) < $626,350 (tcw.hoh.b4.upper) → line (d)] [line (a) ≥ $626,350 (tcw.hoh.b4.upper) → line (d)]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["amount",{"param":"ordinary.table_boundary"}],"op":"test"},{"lt":["amount",{"param":"tcw.hoh.b1.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row1.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.hoh.b1.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.hoh.b2.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row2.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.hoh.b2.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.hoh.b3.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row3.tax"},{"guard":{"all":[{"ge":["amount",{"param":"tcw.hoh.b3.upper"}],"op":"test"},{"lt":["amount",{"param":"tcw.hoh.b4.upper"}],"op":"test"}],"op":"test"},"then":"hoh.row4.tax"},{"guard":{"ge":["amount",{"param":"tcw.hoh.b4.upper"}],"op":"test"},"then":"hoh.row5.tax"}],"op":"choose"}`
- Cite: [i1040gi] TCW Section D (2025; printed date 2026-02-25; sha256 482e9c48)

## Tax — `tax`

- **IRS:** Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
- **Encoded (Dollars):** Choose — [line (status) = 'single' → line Tax] [line (status) = 'mfj' → line Tax] [line (status) = 'qss' → line Tax] [line (status) = 'mfs' → line Tax] [line (status) = 'hoh' → line Tax]
- Expr: `{"alternatives":[{"guard":{"eq":["status",{"const":"single"}],"op":"test"},"then":"single.result"},{"guard":{"eq":["status",{"const":"mfj"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"qss"}],"op":"test"},"then":"mfj.result"},{"guard":{"eq":["status",{"const":"mfs"}],"op":"test"},"then":"mfs.result"},{"guard":{"eq":["status",{"const":"hoh"}],"op":"test"},"then":"hoh.result"}],"op":"choose"}`
- Cite: [i1040gi] TCW, sections A-D (2025; printed date 2026-02-25; sha256 482e9c48)
