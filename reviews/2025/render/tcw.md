# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ef805f70f53f9448170fabcd7f3e53691bc4d9196284b6d3a3354a52ddb47115 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | a21380f3eb726a48ced641c7dddc4ac05d31aea10ebe61c18477c26361e705ba |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (a) — Enter the amount from line 15
Status: **MATCH**

Model: Column (a) takes the line 15 amount or, per the Note, the amount from the other form or worksheet that requires this worksheet. An input bound by the calling line covers both cases.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section A, first row: "Multiply (a) by (b)" with (b) of 22% (0.22).

### Tax (single.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section A, first row: "Subtract (d) from (c)" with (d) of $5,086.00.

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section A, second row: (a) times (b) of 24% (0.24).

### Tax (single.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section A, second row: (c) minus (d) of $7,153.00.

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section A, third row: (a) times (b) of 32% (0.32).

### Tax (single.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section A, third row: (c) minus (d) of $22,937.00.

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section A, fourth row: (a) times (b) of 35% (0.35).

### Tax (single.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section A, fourth row: (c) minus (d) of $30,452.75.

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section A, fifth row: (a) times (b) of 37% (0.37).

### Tax (single.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section A, fifth row: (c) minus (d) of $42,979.75.

### Tax (single.result) — Section A—Use if your taxable income is $100,000 or more and your filing status is Single.
Status: **MATCH**

Model: The conditions match Section A's rows: at least $100,000 but not over $103,350, then over/not over $197,300, $250,525 and $626,350, then over $626,350. Each range selects the correct row.

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section B, first row: (a) times (b) of 22% (0.22).

### Tax (mfj.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section B, first row: (c) minus (d) of $10,172.00.

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section B, second row: (a) times (b) of 24% (0.24).

### Tax (mfj.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section B, second row: (c) minus (d) of $14,306.00.

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section B, third row: (a) times (b) of 32% (0.32).

### Tax (mfj.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section B, third row: (c) minus (d) of $45,874.00.

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section B, fourth row: (a) times (b) of 35% (0.35).

### Tax (mfj.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section B, fourth row: (c) minus (d) of $60,905.50.

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section B, fifth row: (a) times (b) of 37% (0.37).

### Tax (mfj.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section B, fifth row: (c) minus (d) of $75,937.50.

### Tax (mfj.result) — Section B—Use if your taxable income is $100,000 or more and your filing status is Married
Status: **MATCH**

Model: The conditions match Section B's rows: at least $100,000 but not over $206,700, then over/not over $394,600, $501,050 and $751,600, then over $751,600. Each range selects the correct row.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section C, first row: (a) times (b) of 22% (0.22).

### Tax (mfs.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section C, first row: (c) minus (d) of $5,086.00.

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section C, second row: (a) times (b) of 24% (0.24).

### Tax (mfs.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section C, second row: (c) minus (d) of $7,153.00.

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section C, third row: (a) times (b) of 32% (0.32).

### Tax (mfs.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section C, third row: (c) minus (d) of $22,937.00.

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section C, fourth row: (a) times (b) of 35% (0.35).

### Tax (mfs.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section C, fourth row: (c) minus (d) of $30,452.75.

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section C, fifth row: (a) times (b) of 37% (0.37).

### Tax (mfs.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section C, fifth row: (c) minus (d) of $37,968.75.

### Tax (mfs.result) — Section C—Use if your taxable income is $100,000 or more and your filing status is Married
Status: **MATCH**

Model: The conditions match Section C's rows: at least $100,000 but not over $103,350, then over/not over $197,300, $250,525 and $375,800, then over $375,800. Each range selects the correct row.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section D, first row: (a) times (b) of 22% (0.22).

### Tax (hoh.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section D, first row: (c) minus (d) of $6,825.00.

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section D, second row: (a) times (b) of 24% (0.24).

### Tax (hoh.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section D, second row: (c) minus (d) of $8,892.00.

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section D, third row: (a) times (b) of 32% (0.32).

### Tax (hoh.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section D, third row: (c) minus (d) of $24,676.00.

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section D, fourth row: (a) times (b) of 35% (0.35).

### Tax (hoh.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section D, fourth row: (c) minus (d) of $32,191.00.

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section D, fifth row: (a) times (b) of 37% (0.37).

### Tax (hoh.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section D, fifth row: (c) minus (d) of $44,718.00.

### Tax (hoh.result) — Section D—Use if your taxable income is $100,000 or more and your filing status is Head of
Status: **MATCH**

Model: The conditions match Section D's rows: at least $100,000 but not over $103,350, then over/not over $197,300, $250,500 and $626,350, then over $626,350. Each range selects the correct row.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: The sections are selected by filing status: A for Single, B for Married filing jointly or Qualifying surviving spouse, C for Married filing separately, and D for Head of household. The restatement routes each status the same way.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Column (a) takes the line 15 amount or, per the Note, the amount from the other form or worksheet that requires this worksheet. An input bound by the calling line covers both cases."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "Section A, first row: \"Multiply (a) by (b)\" with (b) of 22% (0.22)."
  - key: "Tax (single.row1.tax)"
    status: MATCH
    reason: "Section A, first row: \"Subtract (d) from (c)\" with (d) of $5,086.00."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "Section A, second row: (a) times (b) of 24% (0.24)."
  - key: "Tax (single.row2.tax)"
    status: MATCH
    reason: "Section A, second row: (c) minus (d) of $7,153.00."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "Section A, third row: (a) times (b) of 32% (0.32)."
  - key: "Tax (single.row3.tax)"
    status: MATCH
    reason: "Section A, third row: (c) minus (d) of $22,937.00."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "Section A, fourth row: (a) times (b) of 35% (0.35)."
  - key: "Tax (single.row4.tax)"
    status: MATCH
    reason: "Section A, fourth row: (c) minus (d) of $30,452.75."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "Section A, fifth row: (a) times (b) of 37% (0.37)."
  - key: "Tax (single.row5.tax)"
    status: MATCH
    reason: "Section A, fifth row: (c) minus (d) of $42,979.75."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "The conditions match Section A's rows: at least $100,000 but not over $103,350, then over/not over $197,300, $250,525 and $626,350, then over $626,350. Each range selects the correct row."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "Section B, first row: (a) times (b) of 22% (0.22)."
  - key: "Tax (mfj.row1.tax)"
    status: MATCH
    reason: "Section B, first row: (c) minus (d) of $10,172.00."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "Section B, second row: (a) times (b) of 24% (0.24)."
  - key: "Tax (mfj.row2.tax)"
    status: MATCH
    reason: "Section B, second row: (c) minus (d) of $14,306.00."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "Section B, third row: (a) times (b) of 32% (0.32)."
  - key: "Tax (mfj.row3.tax)"
    status: MATCH
    reason: "Section B, third row: (c) minus (d) of $45,874.00."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "Section B, fourth row: (a) times (b) of 35% (0.35)."
  - key: "Tax (mfj.row4.tax)"
    status: MATCH
    reason: "Section B, fourth row: (c) minus (d) of $60,905.50."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "Section B, fifth row: (a) times (b) of 37% (0.37)."
  - key: "Tax (mfj.row5.tax)"
    status: MATCH
    reason: "Section B, fifth row: (c) minus (d) of $75,937.50."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "The conditions match Section B's rows: at least $100,000 but not over $206,700, then over/not over $394,600, $501,050 and $751,600, then over $751,600. Each range selects the correct row."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "Section C, first row: (a) times (b) of 22% (0.22)."
  - key: "Tax (mfs.row1.tax)"
    status: MATCH
    reason: "Section C, first row: (c) minus (d) of $5,086.00."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "Section C, second row: (a) times (b) of 24% (0.24)."
  - key: "Tax (mfs.row2.tax)"
    status: MATCH
    reason: "Section C, second row: (c) minus (d) of $7,153.00."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "Section C, third row: (a) times (b) of 32% (0.32)."
  - key: "Tax (mfs.row3.tax)"
    status: MATCH
    reason: "Section C, third row: (c) minus (d) of $22,937.00."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "Section C, fourth row: (a) times (b) of 35% (0.35)."
  - key: "Tax (mfs.row4.tax)"
    status: MATCH
    reason: "Section C, fourth row: (c) minus (d) of $30,452.75."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "Section C, fifth row: (a) times (b) of 37% (0.37)."
  - key: "Tax (mfs.row5.tax)"
    status: MATCH
    reason: "Section C, fifth row: (c) minus (d) of $37,968.75."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "The conditions match Section C's rows: at least $100,000 but not over $103,350, then over/not over $197,300, $250,525 and $375,800, then over $375,800. Each range selects the correct row."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "Section D, first row: (a) times (b) of 22% (0.22)."
  - key: "Tax (hoh.row1.tax)"
    status: MATCH
    reason: "Section D, first row: (c) minus (d) of $6,825.00."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "Section D, second row: (a) times (b) of 24% (0.24)."
  - key: "Tax (hoh.row2.tax)"
    status: MATCH
    reason: "Section D, second row: (c) minus (d) of $8,892.00."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "Section D, third row: (a) times (b) of 32% (0.32)."
  - key: "Tax (hoh.row3.tax)"
    status: MATCH
    reason: "Section D, third row: (c) minus (d) of $24,676.00."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "Section D, fourth row: (a) times (b) of 35% (0.35)."
  - key: "Tax (hoh.row4.tax)"
    status: MATCH
    reason: "Section D, fourth row: (c) minus (d) of $32,191.00."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "Section D, fifth row: (a) times (b) of 37% (0.37)."
  - key: "Tax (hoh.row5.tax)"
    status: MATCH
    reason: "Section D, fifth row: (c) minus (d) of $44,718.00."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "The conditions match Section D's rows: at least $100,000 but not over $103,350, then over/not over $197,300, $250,500 and $626,350, then over $626,350. Each range selects the correct row."
  - key: "Tax (tax)"
    status: MATCH
    reason: "The sections are selected by filing status: A for Single, B for Married filing jointly or Qualifying surviving spouse, C for Married filing separately, and D for Head of household. The restatement routes each status the same way."
```
```
