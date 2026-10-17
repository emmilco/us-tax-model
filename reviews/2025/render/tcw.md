# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e23cfec3f6488e05cbd7d001084cec8d6f7ec1d757020effa03e9e61fa7c35a0 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### (a) — Enter the amount from line 15
Status: **MATCH**

Model: Column (a) says "Enter the amount from line 15," and the Note says to enter the amount from another form or worksheet when one is being looked up. The restatement's binding to the calling line covers both cases.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section A row 1 multiplies (a) by "22% (0.22)".

### (d) (single.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A row 1 subtraction amount is $5,086.00, and the tax column says "Subtract (d) from (c)".

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section A row 2 multiplies (a) by "24% (0.24)".

### (d) (single.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A row 2 subtraction amount is $7,153.00, subtracted from (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section A row 3 multiplies (a) by "32% (0.32)".

### (d) (single.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A row 3 subtraction amount is $22,937.00, subtracted from (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section A row 4 multiplies (a) by "35% (0.35)".

### (d) (single.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A row 4 subtraction amount is $30,452.75, subtracted from (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section A row 5 multiplies (a) by "37% (0.37)".

### (d) (single.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A row 5 subtraction amount is $42,979.75, subtracted from (c).

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: The row conditions match Section A: "At least $100,000 but not over $103,350", then over $103,350 to $197,300, over $197,300 to $250,525, over $250,525 to $626,350, and over $626,350.

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section B row 1 multiplies (a) by "22% (0.22)".

### (d) (mfj.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B row 1 subtraction amount is $10,172.00, subtracted from (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section B row 2 multiplies (a) by "24% (0.24)".

### (d) (mfj.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B row 2 subtraction amount is $14,306.00, subtracted from (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section B row 3 multiplies (a) by "32% (0.32)".

### (d) (mfj.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B row 3 subtraction amount is $45,874.00, subtracted from (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section B row 4 multiplies (a) by "35% (0.35)".

### (d) (mfj.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B row 4 subtraction amount is $60,905.50, subtracted from (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section B row 5 multiplies (a) by "37% (0.37)".

### (d) (mfj.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B row 5 subtraction amount is $75,937.50, subtracted from (c).

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: The row conditions match Section B: $100,000 to $206,700, then over $206,700 to $394,600, over $394,600 to $501,050, over $501,050 to $751,600, and over $751,600.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section C row 1 multiplies (a) by "22% (0.22)".

### (d) (mfs.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C row 1 subtraction amount is $5,086.00, subtracted from (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section C row 2 multiplies (a) by "24% (0.24)".

### (d) (mfs.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C row 2 subtraction amount is $7,153.00, subtracted from (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section C row 3 multiplies (a) by "32% (0.32)".

### (d) (mfs.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C row 3 subtraction amount is $22,937.00, subtracted from (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section C row 4 multiplies (a) by "35% (0.35)".

### (d) (mfs.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C row 4 subtraction amount is $30,452.75, subtracted from (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section C row 5 multiplies (a) by "37% (0.37)".

### (d) (mfs.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C row 5 subtraction amount is $37,968.75, subtracted from (c).

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: The row conditions match Section C: $100,000 to $103,350, then over $103,350 to $197,300, over $197,300 to $250,525, over $250,525 to $375,800, and over $375,800.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section D row 1 multiplies (a) by "22% (0.22)".

### (d) (hoh.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D row 1 subtraction amount is $6,825.00, subtracted from (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section D row 2 multiplies (a) by "24% (0.24)".

### (d) (hoh.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D row 2 subtraction amount is $8,892.00, subtracted from (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section D row 3 multiplies (a) by "32% (0.32)".

### (d) (hoh.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D row 3 subtraction amount is $24,676.00, subtracted from (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section D row 4 multiplies (a) by "35% (0.35)".

### (d) (hoh.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D row 4 subtraction amount is $32,191.00, subtracted from (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section D row 5 multiplies (a) by "37% (0.37)".

### (d) (hoh.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D row 5 subtraction amount is $44,718.00, subtracted from (c).

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: The row conditions match Section D as printed: $100,000 to $103,350, then over $103,350 to $197,300, over $197,300 to $250,500, over $250,500 to $626,350, and over $626,350.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: The sections are chosen by filing status: A for Single, B for "Married filing jointly or Qualifying surviving spouse", C for Married filing separately, and D for Head of household. The restatement sends qss to the mfj result, as Section B does.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Column (a) says \"Enter the amount from line 15,\" and the Note says to enter the amount from another form or worksheet when one is being looked up. The restatement's binding to the calling line covers both cases."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "Section A row 1 multiplies (a) by \"22% (0.22)\"."
  - key: "(d) (single.row1.tax)"
    status: MATCH
    reason: "Section A row 1 subtraction amount is $5,086.00, and the tax column says \"Subtract (d) from (c)\"."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "Section A row 2 multiplies (a) by \"24% (0.24)\"."
  - key: "(d) (single.row2.tax)"
    status: MATCH
    reason: "Section A row 2 subtraction amount is $7,153.00, subtracted from (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "Section A row 3 multiplies (a) by \"32% (0.32)\"."
  - key: "(d) (single.row3.tax)"
    status: MATCH
    reason: "Section A row 3 subtraction amount is $22,937.00, subtracted from (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "Section A row 4 multiplies (a) by \"35% (0.35)\"."
  - key: "(d) (single.row4.tax)"
    status: MATCH
    reason: "Section A row 4 subtraction amount is $30,452.75, subtracted from (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "Section A row 5 multiplies (a) by \"37% (0.37)\"."
  - key: "(d) (single.row5.tax)"
    status: MATCH
    reason: "Section A row 5 subtraction amount is $42,979.75, subtracted from (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "The row conditions match Section A: \"At least $100,000 but not over $103,350\", then over $103,350 to $197,300, over $197,300 to $250,525, over $250,525 to $626,350, and over $626,350."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "Section B row 1 multiplies (a) by \"22% (0.22)\"."
  - key: "(d) (mfj.row1.tax)"
    status: MATCH
    reason: "Section B row 1 subtraction amount is $10,172.00, subtracted from (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "Section B row 2 multiplies (a) by \"24% (0.24)\"."
  - key: "(d) (mfj.row2.tax)"
    status: MATCH
    reason: "Section B row 2 subtraction amount is $14,306.00, subtracted from (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "Section B row 3 multiplies (a) by \"32% (0.32)\"."
  - key: "(d) (mfj.row3.tax)"
    status: MATCH
    reason: "Section B row 3 subtraction amount is $45,874.00, subtracted from (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "Section B row 4 multiplies (a) by \"35% (0.35)\"."
  - key: "(d) (mfj.row4.tax)"
    status: MATCH
    reason: "Section B row 4 subtraction amount is $60,905.50, subtracted from (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "Section B row 5 multiplies (a) by \"37% (0.37)\"."
  - key: "(d) (mfj.row5.tax)"
    status: MATCH
    reason: "Section B row 5 subtraction amount is $75,937.50, subtracted from (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "The row conditions match Section B: $100,000 to $206,700, then over $206,700 to $394,600, over $394,600 to $501,050, over $501,050 to $751,600, and over $751,600."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "Section C row 1 multiplies (a) by \"22% (0.22)\"."
  - key: "(d) (mfs.row1.tax)"
    status: MATCH
    reason: "Section C row 1 subtraction amount is $5,086.00, subtracted from (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "Section C row 2 multiplies (a) by \"24% (0.24)\"."
  - key: "(d) (mfs.row2.tax)"
    status: MATCH
    reason: "Section C row 2 subtraction amount is $7,153.00, subtracted from (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "Section C row 3 multiplies (a) by \"32% (0.32)\"."
  - key: "(d) (mfs.row3.tax)"
    status: MATCH
    reason: "Section C row 3 subtraction amount is $22,937.00, subtracted from (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "Section C row 4 multiplies (a) by \"35% (0.35)\"."
  - key: "(d) (mfs.row4.tax)"
    status: MATCH
    reason: "Section C row 4 subtraction amount is $30,452.75, subtracted from (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "Section C row 5 multiplies (a) by \"37% (0.37)\"."
  - key: "(d) (mfs.row5.tax)"
    status: MATCH
    reason: "Section C row 5 subtraction amount is $37,968.75, subtracted from (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "The row conditions match Section C: $100,000 to $103,350, then over $103,350 to $197,300, over $197,300 to $250,525, over $250,525 to $375,800, and over $375,800."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "Section D row 1 multiplies (a) by \"22% (0.22)\"."
  - key: "(d) (hoh.row1.tax)"
    status: MATCH
    reason: "Section D row 1 subtraction amount is $6,825.00, subtracted from (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "Section D row 2 multiplies (a) by \"24% (0.24)\"."
  - key: "(d) (hoh.row2.tax)"
    status: MATCH
    reason: "Section D row 2 subtraction amount is $8,892.00, subtracted from (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "Section D row 3 multiplies (a) by \"32% (0.32)\"."
  - key: "(d) (hoh.row3.tax)"
    status: MATCH
    reason: "Section D row 3 subtraction amount is $24,676.00, subtracted from (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "Section D row 4 multiplies (a) by \"35% (0.35)\"."
  - key: "(d) (hoh.row4.tax)"
    status: MATCH
    reason: "Section D row 4 subtraction amount is $32,191.00, subtracted from (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "Section D row 5 multiplies (a) by \"37% (0.37)\"."
  - key: "(d) (hoh.row5.tax)"
    status: MATCH
    reason: "Section D row 5 subtraction amount is $44,718.00, subtracted from (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "The row conditions match Section D as printed: $100,000 to $103,350, then over $103,350 to $197,300, over $197,300 to $250,500, over $250,500 to $626,350, and over $626,350."
  - key: "Tax (tax)"
    status: MATCH
    reason: "The sections are chosen by filing status: A for Single, B for \"Married filing jointly or Qualifying surviving spouse\", C for Married filing separately, and D for Head of household. The restatement sends qss to the mfj result, as Section B does."
```
```
