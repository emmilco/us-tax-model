# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ef805f70f53f9448170fabcd7f3e53691bc4d9196284b6d3a3354a52ddb47115 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a21380f3eb726a48ced641c7dddc4ac05d31aea10ebe61c18477c26361e705ba |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | Use the section for your filing status |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (a) — Enter the amount from line 15
Status: **MATCH**

Model: IRS: 'Enter the amount from line 15'—the restatement takes the amount whose tax is computed from the calling line.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section A first row: 'Multiply (a) by (b)' with '(b) Multiplication amount' 22% (0.22).

### Tax (single.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: 'Subtract (d) from (c)' with (d) subtraction amount $5,086.00.

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section A second row: multiply by 24% (0.24).

### Tax (single.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $7,153.00 from (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section A third row: multiply by 32% (0.32).

### Tax (single.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $22,937.00 from (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section A fourth row: multiply by 35% (0.35).

### Tax (single.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $30,452.75 from (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section A fifth row: multiply by 37% (0.37).

### Tax (single.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $42,979.75 from (c).

### Tax (single.result) — Section A—Use if your taxable income is $100,000 or more and your filing status is Single.
Status: **MATCH**

Model: Row selection matches Section A's 'At least $100,000 but not over $103,350', 'Over $103,350 but not over $197,300', 'Over $197,300 but not over $250,525', 'Over $250,525 but not over $626,350', 'Over $626,350'.

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section B first row: multiply by 22% (0.22).

### Tax (mfj.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $10,172.00 from (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section B second row: multiply by 24% (0.24).

### Tax (mfj.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $14,306.00 from (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section B third row: multiply by 32% (0.32).

### Tax (mfj.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $45,874.00 from (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section B fourth row: multiply by 35% (0.35).

### Tax (mfj.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $60,905.50 from (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section B fifth row: multiply by 37% (0.37).

### Tax (mfj.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $75,937.50 from (c).

### Tax (mfj.result) — Section B—Use if your taxable income is $100,000 or more and your filing status is Married
Status: **MATCH**

Model: Row selection matches Section B's $206,700, $394,600, $501,050, and $751,600 breakpoints.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section C first row: multiply by 22% (0.22).

### Tax (mfs.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $5,086.00 from (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section C second row: multiply by 24% (0.24).

### Tax (mfs.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $7,153.00 from (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section C third row: multiply by 32% (0.32).

### Tax (mfs.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $22,937.00 from (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section C fourth row: multiply by 35% (0.35).

### Tax (mfs.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $30,452.75 from (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section C fifth row: multiply by 37% (0.37).

### Tax (mfs.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $37,968.75 from (c).

### Tax (mfs.result) — Section C—Use if your taxable income is $100,000 or more and your filing status is Married
Status: **MATCH**

Model: Row selection matches Section C's $103,350, $197,300, $250,525, and $375,800 breakpoints.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section D first row: multiply by 22% (0.22).

### Tax (hoh.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $6,825.00 from (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section D second row: multiply by 24% (0.24).

### Tax (hoh.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $8,892.00 from (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section D third row: multiply by 32% (0.32).

### Tax (hoh.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $24,676.00 from (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section D fourth row: multiply by 35% (0.35).

### Tax (hoh.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $32,191.00 from (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section D fifth row: multiply by 37% (0.37).

### Tax (hoh.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS: subtract (d) $44,718.00 from (c).

### Tax (hoh.result) — Section D—Use if your taxable income is $100,000 or more and your filing status is Head of
Status: **MATCH**

Model: Row selection matches Section D's $103,350, $197,300, $250,500, and $626,350 breakpoints.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS directs use of Section A for Single, Section B for Married filing jointly or Qualifying surviving spouse, Section C for Married filing separately, and Section D for Head of household, as the restatement does.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "IRS: 'Enter the amount from line 15'—the restatement takes the amount whose tax is computed from the calling line."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "IRS Section A first row: 'Multiply (a) by (b)' with '(b) Multiplication amount' 22% (0.22)."
  - key: "Tax (single.row1.tax)"
    status: MATCH
    reason: "IRS: 'Subtract (d) from (c)' with (d) subtraction amount $5,086.00."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "IRS Section A second row: multiply by 24% (0.24)."
  - key: "Tax (single.row2.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $7,153.00 from (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "IRS Section A third row: multiply by 32% (0.32)."
  - key: "Tax (single.row3.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $22,937.00 from (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "IRS Section A fourth row: multiply by 35% (0.35)."
  - key: "Tax (single.row4.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $30,452.75 from (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "IRS Section A fifth row: multiply by 37% (0.37)."
  - key: "Tax (single.row5.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $42,979.75 from (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "Row selection matches Section A's 'At least $100,000 but not over $103,350', 'Over $103,350 but not over $197,300', 'Over $197,300 but not over $250,525', 'Over $250,525 but not over $626,350', 'Over $626,350'."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "IRS Section B first row: multiply by 22% (0.22)."
  - key: "Tax (mfj.row1.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $10,172.00 from (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "IRS Section B second row: multiply by 24% (0.24)."
  - key: "Tax (mfj.row2.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $14,306.00 from (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "IRS Section B third row: multiply by 32% (0.32)."
  - key: "Tax (mfj.row3.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $45,874.00 from (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "IRS Section B fourth row: multiply by 35% (0.35)."
  - key: "Tax (mfj.row4.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $60,905.50 from (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "IRS Section B fifth row: multiply by 37% (0.37)."
  - key: "Tax (mfj.row5.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $75,937.50 from (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "Row selection matches Section B's $206,700, $394,600, $501,050, and $751,600 breakpoints."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "IRS Section C first row: multiply by 22% (0.22)."
  - key: "Tax (mfs.row1.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $5,086.00 from (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "IRS Section C second row: multiply by 24% (0.24)."
  - key: "Tax (mfs.row2.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $7,153.00 from (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "IRS Section C third row: multiply by 32% (0.32)."
  - key: "Tax (mfs.row3.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $22,937.00 from (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "IRS Section C fourth row: multiply by 35% (0.35)."
  - key: "Tax (mfs.row4.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $30,452.75 from (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "IRS Section C fifth row: multiply by 37% (0.37)."
  - key: "Tax (mfs.row5.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $37,968.75 from (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "Row selection matches Section C's $103,350, $197,300, $250,525, and $375,800 breakpoints."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "IRS Section D first row: multiply by 22% (0.22)."
  - key: "Tax (hoh.row1.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $6,825.00 from (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "IRS Section D second row: multiply by 24% (0.24)."
  - key: "Tax (hoh.row2.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $8,892.00 from (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "IRS Section D third row: multiply by 32% (0.32)."
  - key: "Tax (hoh.row3.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $24,676.00 from (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "IRS Section D fourth row: multiply by 35% (0.35)."
  - key: "Tax (hoh.row4.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $32,191.00 from (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "IRS Section D fifth row: multiply by 37% (0.37)."
  - key: "Tax (hoh.row5.tax)"
    status: MATCH
    reason: "IRS: subtract (d) $44,718.00 from (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "Row selection matches Section D's $103,350, $197,300, $250,500, and $626,350 breakpoints."
  - key: "Tax (tax)"
    status: MATCH
    reason: "IRS directs use of Section A for Single, Section B for Married filing jointly or Qualifying surviving spouse, Section C for Married filing separately, and Section D for Head of household, as the restatement does."
  - key: "Use the section for your filing status"
    status: MATCH
    reason: "The sections on the worksheet are selected by filing status (Single, MFJ/QSS, MFS, HOH), matching this input helper."
```
