# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | dd66e4a47546ba6e1cfb4bbf31460beace8ed80baf4b09c6ee116d3c8f12f74e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: The IRS column (a) asks for the amount from line 15, and the program treats it as the amount whose tax is computed under the calling line.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section A row 1 says to multiply (a) by 22%, and the program does that.

### Tax (single.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section A row 1 lists subtraction amount $5,086.00 and says to subtract (d) from (c).

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section A row 2 says to multiply (a) by 24%, and the program does that.

### Tax (single.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section A row 2 lists subtraction amount $7,153.00 and says to subtract (d) from (c).

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section A row 3 says to multiply (a) by 32%, and the program does that.

### Tax (single.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section A row 3 lists subtraction amount $22,937.00 and says to subtract (d) from (c).

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section A row 4 says to multiply (a) by 35%, and the program does that.

### Tax (single.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section A row 4 lists subtraction amount $30,452.75 and says to subtract (d) from (c).

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section A row 5 says to multiply (a) by 37%, and the program does that.

### Tax (single.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section A row 5 lists subtraction amount $42,979.75 and says to subtract (d) from (c).

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: IRS Section A uses the same Single thresholds and row selection conditions.

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section B row 1 says to multiply (a) by 22%, and the program does that.

### Tax (mfj.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section B row 1 lists subtraction amount $10,172.00 and says to subtract (d) from (c).

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section B row 2 says to multiply (a) by 24%, and the program does that.

### Tax (mfj.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section B row 2 lists subtraction amount $14,306.00 and says to subtract (d) from (c).

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section B row 3 says to multiply (a) by 32%, and the program does that.

### Tax (mfj.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section B row 3 lists subtraction amount $45,874.00 and says to subtract (d) from (c).

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section B row 4 says to multiply (a) by 35%, and the program does that.

### Tax (mfj.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section B row 4 lists subtraction amount $60,905.50 and says to subtract (d) from (c).

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section B row 5 says to multiply (a) by 37%, and the program does that.

### Tax (mfj.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section B row 5 lists subtraction amount $75,937.50 and says to subtract (d) from (c).

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: IRS Section B uses the same married filing jointly or qualifying surviving spouse thresholds and row selection conditions.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section C row 1 says to multiply (a) by 22%, and the program does that.

### Tax (mfs.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section C row 1 lists subtraction amount $5,086.00 and says to subtract (d) from (c).

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section C row 2 says to multiply (a) by 24%, and the program does that.

### Tax (mfs.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section C row 2 lists subtraction amount $7,153.00 and says to subtract (d) from (c).

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section C row 3 says to multiply (a) by 32%, and the program does that.

### Tax (mfs.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section C row 3 lists subtraction amount $22,937.00 and says to subtract (d) from (c).

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section C row 4 says to multiply (a) by 35%, and the program does that.

### Tax (mfs.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section C row 4 lists subtraction amount $30,452.75 and says to subtract (d) from (c).

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section C row 5 says to multiply (a) by 37%, and the program does that.

### Tax (mfs.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section C row 5 lists subtraction amount $37,968.75 and says to subtract (d) from (c).

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: IRS Section C uses the same married filing separately thresholds and row selection conditions.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: IRS Section D row 1 says to multiply (a) by 22%, and the program does that.

### Tax (hoh.row1.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section D row 1 lists subtraction amount $6,825.00 and says to subtract (d) from (c).

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: IRS Section D row 2 says to multiply (a) by 24%, and the program does that.

### Tax (hoh.row2.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section D row 2 lists subtraction amount $8,892.00 and says to subtract (d) from (c).

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: IRS Section D row 3 says to multiply (a) by 32%, and the program does that.

### Tax (hoh.row3.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section D row 3 lists subtraction amount $24,676.00 and says to subtract (d) from (c).

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: IRS Section D row 4 says to multiply (a) by 35%, and the program does that.

### Tax (hoh.row4.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section D row 4 lists subtraction amount $32,191.00 and says to subtract (d) from (c).

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: IRS Section D row 5 says to multiply (a) by 37%, and the program does that.

### Tax (hoh.row5.tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Section D row 5 lists subtraction amount $44,718.00 and says to subtract (d) from (c).

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: IRS Section D uses the same head of household thresholds and row selection conditions.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: IRS Sections A through D assign Single, married filing jointly or qualifying surviving spouse, married filing separately, and head of household to the corresponding section results.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The IRS column (a) asks for the amount from line 15, and the program treats it as the amount whose tax is computed under the calling line."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "IRS Section A row 1 says to multiply (a) by 22%, and the program does that."
  - key: "Tax (single.row1.tax)"
    status: MATCH
    reason: "IRS Section A row 1 lists subtraction amount $5,086.00 and says to subtract (d) from (c)."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "IRS Section A row 2 says to multiply (a) by 24%, and the program does that."
  - key: "Tax (single.row2.tax)"
    status: MATCH
    reason: "IRS Section A row 2 lists subtraction amount $7,153.00 and says to subtract (d) from (c)."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "IRS Section A row 3 says to multiply (a) by 32%, and the program does that."
  - key: "Tax (single.row3.tax)"
    status: MATCH
    reason: "IRS Section A row 3 lists subtraction amount $22,937.00 and says to subtract (d) from (c)."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "IRS Section A row 4 says to multiply (a) by 35%, and the program does that."
  - key: "Tax (single.row4.tax)"
    status: MATCH
    reason: "IRS Section A row 4 lists subtraction amount $30,452.75 and says to subtract (d) from (c)."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "IRS Section A row 5 says to multiply (a) by 37%, and the program does that."
  - key: "Tax (single.row5.tax)"
    status: MATCH
    reason: "IRS Section A row 5 lists subtraction amount $42,979.75 and says to subtract (d) from (c)."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "IRS Section A uses the same Single thresholds and row selection conditions."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "IRS Section B row 1 says to multiply (a) by 22%, and the program does that."
  - key: "Tax (mfj.row1.tax)"
    status: MATCH
    reason: "IRS Section B row 1 lists subtraction amount $10,172.00 and says to subtract (d) from (c)."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "IRS Section B row 2 says to multiply (a) by 24%, and the program does that."
  - key: "Tax (mfj.row2.tax)"
    status: MATCH
    reason: "IRS Section B row 2 lists subtraction amount $14,306.00 and says to subtract (d) from (c)."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "IRS Section B row 3 says to multiply (a) by 32%, and the program does that."
  - key: "Tax (mfj.row3.tax)"
    status: MATCH
    reason: "IRS Section B row 3 lists subtraction amount $45,874.00 and says to subtract (d) from (c)."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "IRS Section B row 4 says to multiply (a) by 35%, and the program does that."
  - key: "Tax (mfj.row4.tax)"
    status: MATCH
    reason: "IRS Section B row 4 lists subtraction amount $60,905.50 and says to subtract (d) from (c)."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "IRS Section B row 5 says to multiply (a) by 37%, and the program does that."
  - key: "Tax (mfj.row5.tax)"
    status: MATCH
    reason: "IRS Section B row 5 lists subtraction amount $75,937.50 and says to subtract (d) from (c)."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "IRS Section B uses the same married filing jointly or qualifying surviving spouse thresholds and row selection conditions."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "IRS Section C row 1 says to multiply (a) by 22%, and the program does that."
  - key: "Tax (mfs.row1.tax)"
    status: MATCH
    reason: "IRS Section C row 1 lists subtraction amount $5,086.00 and says to subtract (d) from (c)."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "IRS Section C row 2 says to multiply (a) by 24%, and the program does that."
  - key: "Tax (mfs.row2.tax)"
    status: MATCH
    reason: "IRS Section C row 2 lists subtraction amount $7,153.00 and says to subtract (d) from (c)."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "IRS Section C row 3 says to multiply (a) by 32%, and the program does that."
  - key: "Tax (mfs.row3.tax)"
    status: MATCH
    reason: "IRS Section C row 3 lists subtraction amount $22,937.00 and says to subtract (d) from (c)."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "IRS Section C row 4 says to multiply (a) by 35%, and the program does that."
  - key: "Tax (mfs.row4.tax)"
    status: MATCH
    reason: "IRS Section C row 4 lists subtraction amount $30,452.75 and says to subtract (d) from (c)."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "IRS Section C row 5 says to multiply (a) by 37%, and the program does that."
  - key: "Tax (mfs.row5.tax)"
    status: MATCH
    reason: "IRS Section C row 5 lists subtraction amount $37,968.75 and says to subtract (d) from (c)."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "IRS Section C uses the same married filing separately thresholds and row selection conditions."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "IRS Section D row 1 says to multiply (a) by 22%, and the program does that."
  - key: "Tax (hoh.row1.tax)"
    status: MATCH
    reason: "IRS Section D row 1 lists subtraction amount $6,825.00 and says to subtract (d) from (c)."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "IRS Section D row 2 says to multiply (a) by 24%, and the program does that."
  - key: "Tax (hoh.row2.tax)"
    status: MATCH
    reason: "IRS Section D row 2 lists subtraction amount $8,892.00 and says to subtract (d) from (c)."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "IRS Section D row 3 says to multiply (a) by 32%, and the program does that."
  - key: "Tax (hoh.row3.tax)"
    status: MATCH
    reason: "IRS Section D row 3 lists subtraction amount $24,676.00 and says to subtract (d) from (c)."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "IRS Section D row 4 says to multiply (a) by 35%, and the program does that."
  - key: "Tax (hoh.row4.tax)"
    status: MATCH
    reason: "IRS Section D row 4 lists subtraction amount $32,191.00 and says to subtract (d) from (c)."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "IRS Section D row 5 says to multiply (a) by 37%, and the program does that."
  - key: "Tax (hoh.row5.tax)"
    status: MATCH
    reason: "IRS Section D row 5 lists subtraction amount $44,718.00 and says to subtract (d) from (c)."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "IRS Section D uses the same head of household thresholds and row selection conditions."
  - key: "Tax (tax)"
    status: MATCH
    reason: "IRS Sections A through D assign Single, married filing jointly or qualifying surviving spouse, married filing separately, and head of household to the corresponding section results."
```
