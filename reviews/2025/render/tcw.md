# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a3ca2faf380eef0217147c5dfd6f963ef880e7083d40a7a0f05e53cabbaec61e |
| lines judged | 46 |
| match / mismatch / unclear / missing | 46 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### (a) — Enter the amount from line 15
Status: **MATCH**

Model: Column (a) says "Enter the amount from line 15." The Note says that when the worksheet is used for another form or worksheet, you enter that form's amount instead. An input bound by the calling line covers both cases.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section A, row 1: "Multiply (a) by (b)" with (b) = "× 22% (0.22)".

### (d) (single.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, row 1 has subtraction amount "$ 5,086.00". The Tax column says "Subtract (d) from (c)", so the computed value is right. On the form, (d) is the subtraction amount and the result is the Tax column.

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section A, row 2: "× 24% (0.24)".

### (d) (single.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, row 2 has subtraction amount "$ 7,153.00", subtracted from (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section A, row 3: "× 32% (0.32)".

### (d) (single.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, row 3 has subtraction amount "$ 22,937.00", subtracted from (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section A, row 4: "× 35% (0.35)".

### (d) (single.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, row 4 has subtraction amount "$ 30,452.75", subtracted from (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section A, row 5: "× 37% (0.37)".

### (d) (single.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, row 5 has subtraction amount "$ 42,979.75", subtracted from (c).

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: The row ranges match Section A: "At least $100,000 but not over $103,350", "Over $103,350 but not over $197,300", "Over $197,300 but not over $250,525", "Over $250,525 but not over $626,350" and "Over $626,350".

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section B, row 1: "× 22% (0.22)".

### (d) (mfj.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, row 1 has subtraction amount "$ 10,172.00", subtracted from (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section B, row 2: "× 24% (0.24)".

### (d) (mfj.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, row 2 has subtraction amount "$ 14,306.00", subtracted from (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section B, row 3: "× 32% (0.32)".

### (d) (mfj.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, row 3 has subtraction amount "$ 45,874.00", subtracted from (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section B, row 4: "× 35% (0.35)".

### (d) (mfj.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, row 4 has subtraction amount "$ 60,905.50", subtracted from (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section B, row 5: "× 37% (0.37)".

### (d) (mfj.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, row 5 has subtraction amount "$ 75,937.50", subtracted from (c).

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: The row ranges match Section B: $100,000–$206,700, over $206,700–$394,600, over $394,600–$501,050, over $501,050–$751,600, and "Over $751,600".

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section C, row 1: "× 22% (0.22)".

### (d) (mfs.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, row 1 has subtraction amount "$ 5,086.00", subtracted from (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section C, row 2: "× 24% (0.24)".

### (d) (mfs.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, row 2 has subtraction amount "$ 7,153.00", subtracted from (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section C, row 3: "× 32% (0.32)".

### (d) (mfs.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, row 3 has subtraction amount "$ 22,937.00", subtracted from (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section C, row 4: "× 35% (0.35)".

### (d) (mfs.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, row 4 has subtraction amount "$ 30,452.75", subtracted from (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section C, row 5: "× 37% (0.37)".

### (d) (mfs.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, row 5 has subtraction amount "$ 37,968.75", subtracted from (c).

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: The row ranges match Section C: $100,000–$103,350, over $103,350–$197,300, over $197,300–$250,525, over $250,525–$375,800, and "Over $375,800".

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section D, row 1: "× 22% (0.22)".

### (d) (hoh.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, row 1 has subtraction amount "$ 6,825.00", subtracted from (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section D, row 2: "× 24% (0.24)".

### (d) (hoh.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, row 2 has subtraction amount "$ 8,892.00", subtracted from (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section D, row 3: "× 32% (0.32)".

### (d) (hoh.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, row 3 has subtraction amount "$ 24,676.00", subtracted from (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section D, row 4: "× 35% (0.35)".

### (d) (hoh.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, row 4 has subtraction amount "$ 32,191.00", subtracted from (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section D, row 5: "× 37% (0.37)".

### (d) (hoh.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, row 5 has subtraction amount "$ 44,718.00", subtracted from (c).

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: The row ranges match Section D: $100,000–$103,350, over $103,350–$197,300, over $197,300–$250,500, over $250,500–$626,350, and "Over $626,350".

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: Section A is for "Single", Section B for "Married filing jointly or Qualifying surviving spouse", Section C for "Married filing separately" and Section D for "Head of household". The restatement routes each status to the matching section.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Column (a) says \"Enter the amount from line 15.\" The Note says that when the worksheet is used for another form or worksheet, you enter that form's amount instead. An input bound by the calling line covers both cases."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "Section A, row 1: \"Multiply (a) by (b)\" with (b) = \"× 22% (0.22)\"."
  - key: "(d) (single.row1.tax)"
    status: MATCH
    reason: "Section A, row 1 has subtraction amount \"$ 5,086.00\". The Tax column says \"Subtract (d) from (c)\", so the computed value is right. On the form, (d) is the subtraction amount and the result is the Tax column."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "Section A, row 2: \"× 24% (0.24)\"."
  - key: "(d) (single.row2.tax)"
    status: MATCH
    reason: "Section A, row 2 has subtraction amount \"$ 7,153.00\", subtracted from (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "Section A, row 3: \"× 32% (0.32)\"."
  - key: "(d) (single.row3.tax)"
    status: MATCH
    reason: "Section A, row 3 has subtraction amount \"$ 22,937.00\", subtracted from (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "Section A, row 4: \"× 35% (0.35)\"."
  - key: "(d) (single.row4.tax)"
    status: MATCH
    reason: "Section A, row 4 has subtraction amount \"$ 30,452.75\", subtracted from (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "Section A, row 5: \"× 37% (0.37)\"."
  - key: "(d) (single.row5.tax)"
    status: MATCH
    reason: "Section A, row 5 has subtraction amount \"$ 42,979.75\", subtracted from (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "The row ranges match Section A: \"At least $100,000 but not over $103,350\", \"Over $103,350 but not over $197,300\", \"Over $197,300 but not over $250,525\", \"Over $250,525 but not over $626,350\" and \"Over $626,350\"."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "Section B, row 1: \"× 22% (0.22)\"."
  - key: "(d) (mfj.row1.tax)"
    status: MATCH
    reason: "Section B, row 1 has subtraction amount \"$ 10,172.00\", subtracted from (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "Section B, row 2: \"× 24% (0.24)\"."
  - key: "(d) (mfj.row2.tax)"
    status: MATCH
    reason: "Section B, row 2 has subtraction amount \"$ 14,306.00\", subtracted from (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "Section B, row 3: \"× 32% (0.32)\"."
  - key: "(d) (mfj.row3.tax)"
    status: MATCH
    reason: "Section B, row 3 has subtraction amount \"$ 45,874.00\", subtracted from (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "Section B, row 4: \"× 35% (0.35)\"."
  - key: "(d) (mfj.row4.tax)"
    status: MATCH
    reason: "Section B, row 4 has subtraction amount \"$ 60,905.50\", subtracted from (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "Section B, row 5: \"× 37% (0.37)\"."
  - key: "(d) (mfj.row5.tax)"
    status: MATCH
    reason: "Section B, row 5 has subtraction amount \"$ 75,937.50\", subtracted from (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "The row ranges match Section B: $100,000–$206,700, over $206,700–$394,600, over $394,600–$501,050, over $501,050–$751,600, and \"Over $751,600\"."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "Section C, row 1: \"× 22% (0.22)\"."
  - key: "(d) (mfs.row1.tax)"
    status: MATCH
    reason: "Section C, row 1 has subtraction amount \"$ 5,086.00\", subtracted from (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "Section C, row 2: \"× 24% (0.24)\"."
  - key: "(d) (mfs.row2.tax)"
    status: MATCH
    reason: "Section C, row 2 has subtraction amount \"$ 7,153.00\", subtracted from (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "Section C, row 3: \"× 32% (0.32)\"."
  - key: "(d) (mfs.row3.tax)"
    status: MATCH
    reason: "Section C, row 3 has subtraction amount \"$ 22,937.00\", subtracted from (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "Section C, row 4: \"× 35% (0.35)\"."
  - key: "(d) (mfs.row4.tax)"
    status: MATCH
    reason: "Section C, row 4 has subtraction amount \"$ 30,452.75\", subtracted from (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "Section C, row 5: \"× 37% (0.37)\"."
  - key: "(d) (mfs.row5.tax)"
    status: MATCH
    reason: "Section C, row 5 has subtraction amount \"$ 37,968.75\", subtracted from (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "The row ranges match Section C: $100,000–$103,350, over $103,350–$197,300, over $197,300–$250,525, over $250,525–$375,800, and \"Over $375,800\"."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "Section D, row 1: \"× 22% (0.22)\"."
  - key: "(d) (hoh.row1.tax)"
    status: MATCH
    reason: "Section D, row 1 has subtraction amount \"$ 6,825.00\", subtracted from (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "Section D, row 2: \"× 24% (0.24)\"."
  - key: "(d) (hoh.row2.tax)"
    status: MATCH
    reason: "Section D, row 2 has subtraction amount \"$ 8,892.00\", subtracted from (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "Section D, row 3: \"× 32% (0.32)\"."
  - key: "(d) (hoh.row3.tax)"
    status: MATCH
    reason: "Section D, row 3 has subtraction amount \"$ 24,676.00\", subtracted from (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "Section D, row 4: \"× 35% (0.35)\"."
  - key: "(d) (hoh.row4.tax)"
    status: MATCH
    reason: "Section D, row 4 has subtraction amount \"$ 32,191.00\", subtracted from (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "Section D, row 5: \"× 37% (0.37)\"."
  - key: "(d) (hoh.row5.tax)"
    status: MATCH
    reason: "Section D, row 5 has subtraction amount \"$ 44,718.00\", subtracted from (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "The row ranges match Section D: $100,000–$103,350, over $103,350–$197,300, over $197,300–$250,500, over $250,500–$626,350, and \"Over $626,350\"."
  - key: "Tax (tax)"
    status: MATCH
    reason: "Section A is for \"Single\", Section B for \"Married filing jointly or Qualifying surviving spouse\", Section C for \"Married filing separately\" and Section D for \"Head of household\". The restatement routes each status to the matching section."
```
```
