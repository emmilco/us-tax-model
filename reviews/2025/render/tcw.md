# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | dd66e4a47546ba6e1cfb4bbf31460beace8ed80baf4b09c6ee116d3c8f12f74e |
| subject sha256 | 7a487f24667a1368cced38ccd8258e98c3d8888dd2b54a39723175c9571c5b6f |
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

Model: Column (a) says "Enter the amount from line 15." The Note allows entering an amount from another form or worksheet instead, which fits a value bound by the calling line.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section A row 1: "Multiply (a) by (b)" with (b) "× 22% (0.22)".

### Tax (single.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: "Subtract (d) from (c)" with (d) $5,086.00.

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section A row 2 multiplies (a) by 24% (0.24).

### Tax (single.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $7,153.00 from (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section A row 3 multiplies (a) by 32% (0.32).

### Tax (single.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $22,937.00 from (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section A row 4 multiplies (a) by 35% (0.35).

### Tax (single.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $30,452.75 from (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section A row 5 multiplies (a) by 37% (0.37).

### Tax (single.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $42,979.75 from (c).

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: Row selection matches Section A: "At least $100,000 but not over $103,350", then over $103,350 to $197,300, over $197,300 to $250,525, over $250,525 to $626,350, and "Over $626,350".

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section B row 1 multiplies (a) by 22% (0.22).

### Tax (mfj.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $10,172.00 from (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section B row 2 multiplies (a) by 24% (0.24).

### Tax (mfj.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $14,306.00 from (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section B row 3 multiplies (a) by 32% (0.32).

### Tax (mfj.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $45,874.00 from (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section B row 4 multiplies (a) by 35% (0.35).

### Tax (mfj.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $60,905.50 from (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section B row 5 multiplies (a) by 37% (0.37).

### Tax (mfj.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $75,937.50 from (c).

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: Row selection matches Section B bounds: $100,000 to $206,700, then $394,600, $501,050, $751,600, and "Over $751,600".

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section C row 1 multiplies (a) by 22% (0.22).

### Tax (mfs.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $5,086.00 from (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section C row 2 multiplies (a) by 24% (0.24).

### Tax (mfs.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $7,153.00 from (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section C row 3 multiplies (a) by 32% (0.32).

### Tax (mfs.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $22,937.00 from (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section C row 4 multiplies (a) by 35% (0.35).

### Tax (mfs.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $30,452.75 from (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section C row 5 multiplies (a) by 37% (0.37).

### Tax (mfs.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $37,968.75 from (c).

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: Row selection matches Section C bounds: $100,000 to $103,350, then $197,300, $250,525, $375,800, and "Over $375,800".

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section D row 1 multiplies (a) by 22% (0.22).

### Tax (hoh.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $6,825.00 from (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section D row 2 multiplies (a) by 24% (0.24).

### Tax (hoh.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $8,892.00 from (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section D row 3 multiplies (a) by 32% (0.32).

### Tax (hoh.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $24,676.00 from (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section D row 4 multiplies (a) by 35% (0.35).

### Tax (hoh.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $32,191.00 from (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section D row 5 multiplies (a) by 37% (0.37).

### Tax (hoh.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Subtracts (d) $44,718.00 from (c).

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: Row selection matches the bounds printed in Section D: $100,000 to $103,350, then $197,300, $250,500, $626,350, and "Over $626,350".

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Sections A–D are chosen by filing status. Section B is "Married filing jointly or Qualifying surviving spouse", so mapping qss to the mfj result matches.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Column (a) says \"Enter the amount from line 15.\" The Note allows entering an amount from another form or worksheet instead, which fits a value bound by the calling line."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "Section A row 1: \"Multiply (a) by (b)\" with (b) \"× 22% (0.22)\"."
  - key: "Tax (single.row1.tax)"
    status: MATCH
    reason: "\"Subtract (d) from (c)\" with (d) $5,086.00."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "Section A row 2 multiplies (a) by 24% (0.24)."
  - key: "Tax (single.row2.tax)"
    status: MATCH
    reason: "Subtracts (d) $7,153.00 from (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "Section A row 3 multiplies (a) by 32% (0.32)."
  - key: "Tax (single.row3.tax)"
    status: MATCH
    reason: "Subtracts (d) $22,937.00 from (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "Section A row 4 multiplies (a) by 35% (0.35)."
  - key: "Tax (single.row4.tax)"
    status: MATCH
    reason: "Subtracts (d) $30,452.75 from (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "Section A row 5 multiplies (a) by 37% (0.37)."
  - key: "Tax (single.row5.tax)"
    status: MATCH
    reason: "Subtracts (d) $42,979.75 from (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "Row selection matches Section A: \"At least $100,000 but not over $103,350\", then over $103,350 to $197,300, over $197,300 to $250,525, over $250,525 to $626,350, and \"Over $626,350\"."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "Section B row 1 multiplies (a) by 22% (0.22)."
  - key: "Tax (mfj.row1.tax)"
    status: MATCH
    reason: "Subtracts (d) $10,172.00 from (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "Section B row 2 multiplies (a) by 24% (0.24)."
  - key: "Tax (mfj.row2.tax)"
    status: MATCH
    reason: "Subtracts (d) $14,306.00 from (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "Section B row 3 multiplies (a) by 32% (0.32)."
  - key: "Tax (mfj.row3.tax)"
    status: MATCH
    reason: "Subtracts (d) $45,874.00 from (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "Section B row 4 multiplies (a) by 35% (0.35)."
  - key: "Tax (mfj.row4.tax)"
    status: MATCH
    reason: "Subtracts (d) $60,905.50 from (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "Section B row 5 multiplies (a) by 37% (0.37)."
  - key: "Tax (mfj.row5.tax)"
    status: MATCH
    reason: "Subtracts (d) $75,937.50 from (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "Row selection matches Section B bounds: $100,000 to $206,700, then $394,600, $501,050, $751,600, and \"Over $751,600\"."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "Section C row 1 multiplies (a) by 22% (0.22)."
  - key: "Tax (mfs.row1.tax)"
    status: MATCH
    reason: "Subtracts (d) $5,086.00 from (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "Section C row 2 multiplies (a) by 24% (0.24)."
  - key: "Tax (mfs.row2.tax)"
    status: MATCH
    reason: "Subtracts (d) $7,153.00 from (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "Section C row 3 multiplies (a) by 32% (0.32)."
  - key: "Tax (mfs.row3.tax)"
    status: MATCH
    reason: "Subtracts (d) $22,937.00 from (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "Section C row 4 multiplies (a) by 35% (0.35)."
  - key: "Tax (mfs.row4.tax)"
    status: MATCH
    reason: "Subtracts (d) $30,452.75 from (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "Section C row 5 multiplies (a) by 37% (0.37)."
  - key: "Tax (mfs.row5.tax)"
    status: MATCH
    reason: "Subtracts (d) $37,968.75 from (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "Row selection matches Section C bounds: $100,000 to $103,350, then $197,300, $250,525, $375,800, and \"Over $375,800\"."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "Section D row 1 multiplies (a) by 22% (0.22)."
  - key: "Tax (hoh.row1.tax)"
    status: MATCH
    reason: "Subtracts (d) $6,825.00 from (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "Section D row 2 multiplies (a) by 24% (0.24)."
  - key: "Tax (hoh.row2.tax)"
    status: MATCH
    reason: "Subtracts (d) $8,892.00 from (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "Section D row 3 multiplies (a) by 32% (0.32)."
  - key: "Tax (hoh.row3.tax)"
    status: MATCH
    reason: "Subtracts (d) $24,676.00 from (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "Section D row 4 multiplies (a) by 35% (0.35)."
  - key: "Tax (hoh.row4.tax)"
    status: MATCH
    reason: "Subtracts (d) $32,191.00 from (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "Section D row 5 multiplies (a) by 37% (0.37)."
  - key: "Tax (hoh.row5.tax)"
    status: MATCH
    reason: "Subtracts (d) $44,718.00 from (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "Row selection matches the bounds printed in Section D: $100,000 to $103,350, then $197,300, $250,500, $626,350, and \"Over $626,350\"."
  - key: "Tax (tax)"
    status: MATCH
    reason: "Sections A–D are chosen by filing status. Section B is \"Married filing jointly or Qualifying surviving spouse\", so mapping qss to the mfj result matches."
```
```
