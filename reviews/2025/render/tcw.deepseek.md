# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | deepseek-v4-pro |
| model reported | deepseek-v4-pro |
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

Model: Column (a) is an entry blank for the amount from line 15, or for the other form/worksheet amount described in the note; binding it as the amount whose tax is computed matches the worksheet.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Matches Section A row 1: multiply column (a) by the 22% (0.22) multiplication amount.

### Tax (single.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section A row 1: subtract the $5,086 subtraction amount from column (c).

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Matches Section A row 2: multiply column (a) by the 24% (0.24) multiplication amount.

### Tax (single.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section A row 2: subtract the $7,153 subtraction amount from column (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Matches Section A row 3: multiply column (a) by the 32% (0.32) multiplication amount.

### Tax (single.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section A row 3: subtract the $22,937 subtraction amount from column (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Matches Section A row 4: multiply column (a) by the 35% (0.35) multiplication amount.

### Tax (single.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section A row 4: subtract the $30,452.75 subtraction amount from column (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Matches Section A row 5: multiply column (a) by the 37% (0.37) multiplication amount.

### Tax (single.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section A row 5: subtract the $42,979.75 subtraction amount from column (c).

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: The row selection thresholds match Section A: at least $100,000 through $103,350, then over each upper bound through the next upper bound, and over $626,350.

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Matches Section B row 1: multiply column (a) by the 22% (0.22) multiplication amount.

### Tax (mfj.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section B row 1: subtract the $10,172 subtraction amount from column (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Matches Section B row 2: multiply column (a) by the 24% (0.24) multiplication amount.

### Tax (mfj.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section B row 2: subtract the $14,306 subtraction amount from column (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Matches Section B row 3: multiply column (a) by the 32% (0.32) multiplication amount.

### Tax (mfj.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section B row 3: subtract the $45,874 subtraction amount from column (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Matches Section B row 4: multiply column (a) by the 35% (0.35) multiplication amount.

### Tax (mfj.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section B row 4: subtract the $60,905.50 subtraction amount from column (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Matches Section B row 5: multiply column (a) by the 37% (0.37) multiplication amount.

### Tax (mfj.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section B row 5: subtract the $75,937.50 subtraction amount from column (c).

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: The row selection thresholds match Section B: at least $100,000 through $206,700, then over each upper bound through the next upper bound, and over $751,600.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Matches Section C row 1: multiply column (a) by the 22% (0.22) multiplication amount.

### Tax (mfs.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section C row 1: subtract the $5,086 subtraction amount from column (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Matches Section C row 2: multiply column (a) by the 24% (0.24) multiplication amount.

### Tax (mfs.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section C row 2: subtract the $7,153 subtraction amount from column (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Matches Section C row 3: multiply column (a) by the 32% (0.32) multiplication amount.

### Tax (mfs.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section C row 3: subtract the $22,937 subtraction amount from column (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Matches Section C row 4: multiply column (a) by the 35% (0.35) multiplication amount.

### Tax (mfs.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section C row 4: subtract the $30,452.75 subtraction amount from column (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Matches Section C row 5: multiply column (a) by the 37% (0.37) multiplication amount.

### Tax (mfs.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section C row 5: subtract the $37,968.75 subtraction amount from column (c).

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: The row selection thresholds match Section C: at least $100,000 through $103,350, then over each upper bound through the next upper bound, and over $375,800.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Matches Section D row 1: multiply column (a) by the 22% (0.22) multiplication amount.

### Tax (hoh.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section D row 1: subtract the $6,825 subtraction amount from column (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Matches Section D row 2: multiply column (a) by the 24% (0.24) multiplication amount.

### Tax (hoh.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section D row 2: subtract the $8,892 subtraction amount from column (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Matches Section D row 3: multiply column (a) by the 32% (0.32) multiplication amount.

### Tax (hoh.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section D row 3: subtract the $24,676 subtraction amount from column (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Matches Section D row 4: multiply column (a) by the 35% (0.35) multiplication amount.

### Tax (hoh.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section D row 4: subtract the $32,191 subtraction amount from column (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Matches Section D row 5: multiply column (a) by the 37% (0.37) multiplication amount.

### Tax (hoh.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches Section D row 5: subtract the $44,718 subtraction amount from column (c).

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: The row selection thresholds match Section D: at least $100,000 through $103,350, then over each upper bound through the next upper bound, and over $626,350.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Matches the worksheet's filing-status instructions: single uses Section A, married filing jointly or qualifying surviving spouse uses Section B, married filing separately uses Section C, and head of household uses Section D.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Column (a) is an entry blank for the amount from line 15, or for the other form/worksheet amount described in the note; binding it as the amount whose tax is computed matches the worksheet."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "Matches Section A row 1: multiply column (a) by the 22% (0.22) multiplication amount."
  - key: "Tax (single.row1.tax)"
    status: MATCH
    reason: "Matches Section A row 1: subtract the $5,086 subtraction amount from column (c)."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "Matches Section A row 2: multiply column (a) by the 24% (0.24) multiplication amount."
  - key: "Tax (single.row2.tax)"
    status: MATCH
    reason: "Matches Section A row 2: subtract the $7,153 subtraction amount from column (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "Matches Section A row 3: multiply column (a) by the 32% (0.32) multiplication amount."
  - key: "Tax (single.row3.tax)"
    status: MATCH
    reason: "Matches Section A row 3: subtract the $22,937 subtraction amount from column (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "Matches Section A row 4: multiply column (a) by the 35% (0.35) multiplication amount."
  - key: "Tax (single.row4.tax)"
    status: MATCH
    reason: "Matches Section A row 4: subtract the $30,452.75 subtraction amount from column (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "Matches Section A row 5: multiply column (a) by the 37% (0.37) multiplication amount."
  - key: "Tax (single.row5.tax)"
    status: MATCH
    reason: "Matches Section A row 5: subtract the $42,979.75 subtraction amount from column (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "The row selection thresholds match Section A: at least $100,000 through $103,350, then over each upper bound through the next upper bound, and over $626,350."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "Matches Section B row 1: multiply column (a) by the 22% (0.22) multiplication amount."
  - key: "Tax (mfj.row1.tax)"
    status: MATCH
    reason: "Matches Section B row 1: subtract the $10,172 subtraction amount from column (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "Matches Section B row 2: multiply column (a) by the 24% (0.24) multiplication amount."
  - key: "Tax (mfj.row2.tax)"
    status: MATCH
    reason: "Matches Section B row 2: subtract the $14,306 subtraction amount from column (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "Matches Section B row 3: multiply column (a) by the 32% (0.32) multiplication amount."
  - key: "Tax (mfj.row3.tax)"
    status: MATCH
    reason: "Matches Section B row 3: subtract the $45,874 subtraction amount from column (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "Matches Section B row 4: multiply column (a) by the 35% (0.35) multiplication amount."
  - key: "Tax (mfj.row4.tax)"
    status: MATCH
    reason: "Matches Section B row 4: subtract the $60,905.50 subtraction amount from column (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "Matches Section B row 5: multiply column (a) by the 37% (0.37) multiplication amount."
  - key: "Tax (mfj.row5.tax)"
    status: MATCH
    reason: "Matches Section B row 5: subtract the $75,937.50 subtraction amount from column (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "The row selection thresholds match Section B: at least $100,000 through $206,700, then over each upper bound through the next upper bound, and over $751,600."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "Matches Section C row 1: multiply column (a) by the 22% (0.22) multiplication amount."
  - key: "Tax (mfs.row1.tax)"
    status: MATCH
    reason: "Matches Section C row 1: subtract the $5,086 subtraction amount from column (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "Matches Section C row 2: multiply column (a) by the 24% (0.24) multiplication amount."
  - key: "Tax (mfs.row2.tax)"
    status: MATCH
    reason: "Matches Section C row 2: subtract the $7,153 subtraction amount from column (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "Matches Section C row 3: multiply column (a) by the 32% (0.32) multiplication amount."
  - key: "Tax (mfs.row3.tax)"
    status: MATCH
    reason: "Matches Section C row 3: subtract the $22,937 subtraction amount from column (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "Matches Section C row 4: multiply column (a) by the 35% (0.35) multiplication amount."
  - key: "Tax (mfs.row4.tax)"
    status: MATCH
    reason: "Matches Section C row 4: subtract the $30,452.75 subtraction amount from column (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "Matches Section C row 5: multiply column (a) by the 37% (0.37) multiplication amount."
  - key: "Tax (mfs.row5.tax)"
    status: MATCH
    reason: "Matches Section C row 5: subtract the $37,968.75 subtraction amount from column (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "The row selection thresholds match Section C: at least $100,000 through $103,350, then over each upper bound through the next upper bound, and over $375,800."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "Matches Section D row 1: multiply column (a) by the 22% (0.22) multiplication amount."
  - key: "Tax (hoh.row1.tax)"
    status: MATCH
    reason: "Matches Section D row 1: subtract the $6,825 subtraction amount from column (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "Matches Section D row 2: multiply column (a) by the 24% (0.24) multiplication amount."
  - key: "Tax (hoh.row2.tax)"
    status: MATCH
    reason: "Matches Section D row 2: subtract the $8,892 subtraction amount from column (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "Matches Section D row 3: multiply column (a) by the 32% (0.32) multiplication amount."
  - key: "Tax (hoh.row3.tax)"
    status: MATCH
    reason: "Matches Section D row 3: subtract the $24,676 subtraction amount from column (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "Matches Section D row 4: multiply column (a) by the 35% (0.35) multiplication amount."
  - key: "Tax (hoh.row4.tax)"
    status: MATCH
    reason: "Matches Section D row 4: subtract the $32,191 subtraction amount from column (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "Matches Section D row 5: multiply column (a) by the 37% (0.37) multiplication amount."
  - key: "Tax (hoh.row5.tax)"
    status: MATCH
    reason: "Matches Section D row 5: subtract the $44,718 subtraction amount from column (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "The row selection thresholds match Section D: at least $100,000 through $103,350, then over each upper bound through the next upper bound, and over $626,350."
  - key: "Tax (tax)"
    status: MATCH
    reason: "Matches the worksheet's filing-status instructions: single uses Section A, married filing jointly or qualifying surviving spouse uses Section B, married filing separately uses Section C, and head of household uses Section D."
```
