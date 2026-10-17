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
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (a) — Enter the amount from line 15
Status: **MATCH**

Model: Column (a) is 'Enter the amount from line 15'. The Note says to use the amount from another form or worksheet when this worksheet figures the tax on that amount, so binding (a) to the calling line's amount matches.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section A, first row: '(c) Multiply (a) by (b)', where (b) is '× 22% (0.22)'.

### (d) (single.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, first row: 'Subtract (d) from (c)', where (d) is '$ 5,086.00'.

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section A, second row: multiply (a) by '× 24% (0.24)'.

### (d) (single.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, second row: subtraction amount '$ 7,153.00' is subtracted from (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section A, third row: multiply (a) by '× 32% (0.32)'.

### (d) (single.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, third row: subtraction amount '$ 22,937.00' is subtracted from (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section A, fourth row: multiply (a) by '× 35% (0.35)'.

### (d) (single.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, fourth row: subtraction amount '$ 30,452.75' is subtracted from (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section A, fifth row: multiply (a) by '× 37% (0.37)'.

### (d) (single.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section A, fifth row: subtraction amount '$ 42,979.75' is subtracted from (c).

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: The row conditions match Section A: 'At least $100,000 but not over $103,350', 'Over $103,350 but not over $197,300', 'Over $197,300 but not over $250,525', 'Over $250,525 but not over $626,350', 'Over $626,350'. The result is the chosen row's (c) minus (d).

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section B, first row: multiply (a) by '× 22% (0.22)'.

### (d) (mfj.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, first row: subtraction amount '$ 10,172.00' is subtracted from (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section B, second row: multiply (a) by '× 24% (0.24)'.

### (d) (mfj.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, second row: subtraction amount '$ 14,306.00' is subtracted from (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section B, third row: multiply (a) by '× 32% (0.32)'.

### (d) (mfj.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, third row: subtraction amount '$ 45,874.00' is subtracted from (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section B, fourth row: multiply (a) by '× 35% (0.35)'.

### (d) (mfj.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, fourth row: subtraction amount '$ 60,905.50' is subtracted from (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section B, fifth row: multiply (a) by '× 37% (0.37)'.

### (d) (mfj.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section B, fifth row: subtraction amount '$ 75,937.50' is subtracted from (c).

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: The row conditions match Section B: at least $100,000 but not over $206,700, then over $206,700 / $394,600 / $501,050 / $751,600, each with the matching upper limit.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section C, first row: multiply (a) by '× 22% (0.22)'.

### (d) (mfs.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, first row: subtraction amount '$ 5,086.00' is subtracted from (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section C, second row: multiply (a) by '× 24% (0.24)'.

### (d) (mfs.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, second row: subtraction amount '$ 7,153.00' is subtracted from (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section C, third row: multiply (a) by '× 32% (0.32)'.

### (d) (mfs.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, third row: subtraction amount '$ 22,937.00' is subtracted from (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section C, fourth row: multiply (a) by '× 35% (0.35)'.

### (d) (mfs.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, fourth row: subtraction amount '$ 30,452.75' is subtracted from (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section C, fifth row: multiply (a) by '× 37% (0.37)'.

### (d) (mfs.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section C, fifth row: subtraction amount '$ 37,968.75' is subtracted from (c).

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: The row conditions match Section C: at least $100,000 but not over $103,350, then over $103,350 / $197,300 / $250,525 / $375,800, each with the matching upper limit.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: Section D, first row: multiply (a) by '× 22% (0.22)'.

### (d) (hoh.row1.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, first row: subtraction amount '$ 6,825.00' is subtracted from (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: Section D, second row: multiply (a) by '× 24% (0.24)'.

### (d) (hoh.row2.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, second row: subtraction amount '$ 8,892.00' is subtracted from (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: Section D, third row: multiply (a) by '× 32% (0.32)'.

### (d) (hoh.row3.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, third row: subtraction amount '$ 24,676.00' is subtracted from (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: Section D, fourth row: multiply (a) by '× 35% (0.35)'.

### (d) (hoh.row4.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, fourth row: subtraction amount '$ 32,191.00' is subtracted from (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: Section D, fifth row: multiply (a) by '× 37% (0.37)'.

### (d) (hoh.row5.tax) — Subtract (d) from (c)
Status: **MATCH**

Model: Section D, fifth row: subtraction amount '$ 44,718.00' is subtracted from (c).

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: The row conditions match Section D as printed: 'At least $100,000 but not over $103,350', 'Over $103,350 but not over $197,300', 'Over $197,300 but not over $250,500', 'Over $250,500 but not over $626,350', 'Over $626,350'.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: The section is picked by filing status: Section A for 'Single', Section B for 'Married filing jointly or Qualifying surviving spouse', Section C for 'Married filing separately', Section D for 'Head of household'. The restatement does the same, with qss going to the mfj result.

## Raw response

```yaml
```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "Column (a) is 'Enter the amount from line 15'. The Note says to use the amount from another form or worksheet when this worksheet figures the tax on that amount, so binding (a) to the calling line's amount matches."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "Section A, first row: '(c) Multiply (a) by (b)', where (b) is '× 22% (0.22)'."
  - key: "(d) (single.row1.tax)"
    status: MATCH
    reason: "Section A, first row: 'Subtract (d) from (c)', where (d) is '$ 5,086.00'."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "Section A, second row: multiply (a) by '× 24% (0.24)'."
  - key: "(d) (single.row2.tax)"
    status: MATCH
    reason: "Section A, second row: subtraction amount '$ 7,153.00' is subtracted from (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "Section A, third row: multiply (a) by '× 32% (0.32)'."
  - key: "(d) (single.row3.tax)"
    status: MATCH
    reason: "Section A, third row: subtraction amount '$ 22,937.00' is subtracted from (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "Section A, fourth row: multiply (a) by '× 35% (0.35)'."
  - key: "(d) (single.row4.tax)"
    status: MATCH
    reason: "Section A, fourth row: subtraction amount '$ 30,452.75' is subtracted from (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "Section A, fifth row: multiply (a) by '× 37% (0.37)'."
  - key: "(d) (single.row5.tax)"
    status: MATCH
    reason: "Section A, fifth row: subtraction amount '$ 42,979.75' is subtracted from (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "The row conditions match Section A: 'At least $100,000 but not over $103,350', 'Over $103,350 but not over $197,300', 'Over $197,300 but not over $250,525', 'Over $250,525 but not over $626,350', 'Over $626,350'. The result is the chosen row's (c) minus (d)."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "Section B, first row: multiply (a) by '× 22% (0.22)'."
  - key: "(d) (mfj.row1.tax)"
    status: MATCH
    reason: "Section B, first row: subtraction amount '$ 10,172.00' is subtracted from (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "Section B, second row: multiply (a) by '× 24% (0.24)'."
  - key: "(d) (mfj.row2.tax)"
    status: MATCH
    reason: "Section B, second row: subtraction amount '$ 14,306.00' is subtracted from (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "Section B, third row: multiply (a) by '× 32% (0.32)'."
  - key: "(d) (mfj.row3.tax)"
    status: MATCH
    reason: "Section B, third row: subtraction amount '$ 45,874.00' is subtracted from (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "Section B, fourth row: multiply (a) by '× 35% (0.35)'."
  - key: "(d) (mfj.row4.tax)"
    status: MATCH
    reason: "Section B, fourth row: subtraction amount '$ 60,905.50' is subtracted from (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "Section B, fifth row: multiply (a) by '× 37% (0.37)'."
  - key: "(d) (mfj.row5.tax)"
    status: MATCH
    reason: "Section B, fifth row: subtraction amount '$ 75,937.50' is subtracted from (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "The row conditions match Section B: at least $100,000 but not over $206,700, then over $206,700 / $394,600 / $501,050 / $751,600, each with the matching upper limit."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "Section C, first row: multiply (a) by '× 22% (0.22)'."
  - key: "(d) (mfs.row1.tax)"
    status: MATCH
    reason: "Section C, first row: subtraction amount '$ 5,086.00' is subtracted from (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "Section C, second row: multiply (a) by '× 24% (0.24)'."
  - key: "(d) (mfs.row2.tax)"
    status: MATCH
    reason: "Section C, second row: subtraction amount '$ 7,153.00' is subtracted from (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "Section C, third row: multiply (a) by '× 32% (0.32)'."
  - key: "(d) (mfs.row3.tax)"
    status: MATCH
    reason: "Section C, third row: subtraction amount '$ 22,937.00' is subtracted from (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "Section C, fourth row: multiply (a) by '× 35% (0.35)'."
  - key: "(d) (mfs.row4.tax)"
    status: MATCH
    reason: "Section C, fourth row: subtraction amount '$ 30,452.75' is subtracted from (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "Section C, fifth row: multiply (a) by '× 37% (0.37)'."
  - key: "(d) (mfs.row5.tax)"
    status: MATCH
    reason: "Section C, fifth row: subtraction amount '$ 37,968.75' is subtracted from (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "The row conditions match Section C: at least $100,000 but not over $103,350, then over $103,350 / $197,300 / $250,525 / $375,800, each with the matching upper limit."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "Section D, first row: multiply (a) by '× 22% (0.22)'."
  - key: "(d) (hoh.row1.tax)"
    status: MATCH
    reason: "Section D, first row: subtraction amount '$ 6,825.00' is subtracted from (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "Section D, second row: multiply (a) by '× 24% (0.24)'."
  - key: "(d) (hoh.row2.tax)"
    status: MATCH
    reason: "Section D, second row: subtraction amount '$ 8,892.00' is subtracted from (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "Section D, third row: multiply (a) by '× 32% (0.32)'."
  - key: "(d) (hoh.row3.tax)"
    status: MATCH
    reason: "Section D, third row: subtraction amount '$ 24,676.00' is subtracted from (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "Section D, fourth row: multiply (a) by '× 35% (0.35)'."
  - key: "(d) (hoh.row4.tax)"
    status: MATCH
    reason: "Section D, fourth row: subtraction amount '$ 32,191.00' is subtracted from (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "Section D, fifth row: multiply (a) by '× 37% (0.37)'."
  - key: "(d) (hoh.row5.tax)"
    status: MATCH
    reason: "Section D, fifth row: subtraction amount '$ 44,718.00' is subtracted from (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "The row conditions match Section D as printed: 'At least $100,000 but not over $103,350', 'Over $103,350 but not over $197,300', 'Over $197,300 but not over $250,500', 'Over $250,500 but not over $626,350', 'Over $626,350'."
  - key: "Tax (tax)"
    status: MATCH
    reason: "The section is picked by filing status: Section A for 'Single', Section B for 'Married filing jointly or Qualifying surviving spouse', Section C for 'Married filing separately', Section D for 'Head of household'. The restatement does the same, with qss going to the mfj result."
```
```
