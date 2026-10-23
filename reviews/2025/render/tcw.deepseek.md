# Render comparison — tcw

The rendered English of every printed line of `Tax Computation Worksheet—Line 16` (`rendered/2025/tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | deepseek-v4-pro |
| model reported | deepseek-v4-pro |
| prompt sha256 | a3ca2faf380eef0217147c5dfd6f963ef880e7083d40a7a0f05e53cabbaec61e |
| subject sha256 | c1a361001e6d9ce7e77b2893ef190e0970997d6c30121c865bd0fa21ff3af0f1 |
| lines judged | 46 |
| match / mismatch / unclear / missing | 26 / 20 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (a) — Enter the amount from line 15
Status: **MATCH**

Model: The IRS column (a) says to enter the amount from line 15 (or the other form/worksheet amount being computed); the restatement uses the amount whose tax is computed.

### (c) (single.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: The IRS single row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches.

### (d) (single.row1.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $5,086 (tcw.single.b1.subtract) from column (c) (single.row1.product).

Model: The IRS line (d) is the 'Subtraction amount' of $5,086.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (single.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: The IRS single row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches.

### (d) (single.row2.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $7,153 (tcw.single.b2.subtract) from column (c) (single.row2.product).

Model: The IRS line (d) is the 'Subtraction amount' of $7,153.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (single.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: The IRS single row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches.

### (d) (single.row3.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $22,937 (tcw.single.b3.subtract) from column (c) (single.row3.product).

Model: The IRS line (d) is the 'Subtraction amount' of $22,937.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (single.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: The IRS single row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches.

### (d) (single.row4.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $30,452.75 (tcw.single.b4.subtract) from column (c) (single.row4.product).

Model: The IRS line (d) is the 'Subtraction amount' of $30,452.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (single.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: The IRS single row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches.

### (d) (single.row5.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $42,979.75 (tcw.single.b5.subtract) from column (c) (single.row5.product).

Model: The IRS line (d) is the 'Subtraction amount' of $42,979.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### Tax (single.result) — Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the resul
Status: **MATCH**

Model: The IRS Section A says to complete the row that applies and enter the result on line 16; the program chooses the row using the Single taxable-income thresholds and the corresponding tax amount.

### (c) (mfj.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: The IRS MFJ row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches.

### (d) (mfj.row1.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $10,172 (tcw.mfj.b1.subtract) from column (c) (mfj.row1.product).

Model: The IRS line (d) is the 'Subtraction amount' of $10,172.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfj.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: The IRS MFJ row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches.

### (d) (mfj.row2.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $14,306 (tcw.mfj.b2.subtract) from column (c) (mfj.row2.product).

Model: The IRS line (d) is the 'Subtraction amount' of $14,306.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfj.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: The IRS MFJ row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches.

### (d) (mfj.row3.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $45,874 (tcw.mfj.b3.subtract) from column (c) (mfj.row3.product).

Model: The IRS line (d) is the 'Subtraction amount' of $45,874.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfj.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: The IRS MFJ row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches.

### (d) (mfj.row4.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $60,905.50 (tcw.mfj.b4.subtract) from column (c) (mfj.row4.product).

Model: The IRS line (d) is the 'Subtraction amount' of $60,905.50, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfj.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: The IRS MFJ row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches.

### (d) (mfj.row5.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $75,937.50 (tcw.mfj.b5.subtract) from column (c) (mfj.row5.product).

Model: The IRS line (d) is the 'Subtraction amount' of $75,937.50, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### Tax (mfj.result) — Section B—Use if your filing status is Married filing jointly or Qualifying surviving spou
Status: **MATCH**

Model: The IRS Section B says to complete the row that applies and enter the result on line 16; the program chooses the row using the MFJ/QSS taxable-income thresholds and the corresponding tax amount.

### (c) (mfs.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: The IRS MFS row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches.

### (d) (mfs.row1.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $5,086 (tcw.mfs.b1.subtract) from column (c) (mfs.row1.product).

Model: The IRS line (d) is the 'Subtraction amount' of $5,086.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfs.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: The IRS MFS row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches.

### (d) (mfs.row2.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $7,153 (tcw.mfs.b2.subtract) from column (c) (mfs.row2.product).

Model: The IRS line (d) is the 'Subtraction amount' of $7,153.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfs.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: The IRS MFS row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches.

### (d) (mfs.row3.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $22,937 (tcw.mfs.b3.subtract) from column (c) (mfs.row3.product).

Model: The IRS line (d) is the 'Subtraction amount' of $22,937.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfs.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: The IRS MFS row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches.

### (d) (mfs.row4.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $30,452.75 (tcw.mfs.b4.subtract) from column (c) (mfs.row4.product).

Model: The IRS line (d) is the 'Subtraction amount' of $30,452.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (mfs.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: The IRS MFS row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches.

### (d) (mfs.row5.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $37,968.75 (tcw.mfs.b5.subtract) from column (c) (mfs.row5.product).

Model: The IRS line (d) is the 'Subtraction amount' of $37,968.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### Tax (mfs.result) — Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (
Status: **MATCH**

Model: The IRS Section C says to complete the row that applies and enter the result on line 16; the program chooses the row using the MFS taxable-income thresholds and the corresponding tax amount.

### (c) (hoh.row1.product) — Multiply line (a) by 22% (0.22)
Status: **MATCH**

Model: The IRS HOH row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches.

### (d) (hoh.row1.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $6,825 (tcw.hoh.b1.subtract) from column (c) (hoh.row1.product).

Model: The IRS line (d) is the 'Subtraction amount' of $6,825.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (hoh.row2.product) — Multiply line (a) by 24% (0.24)
Status: **MATCH**

Model: The IRS HOH row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches.

### (d) (hoh.row2.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $8,892 (tcw.hoh.b2.subtract) from column (c) (hoh.row2.product).

Model: The IRS line (d) is the 'Subtraction amount' of $8,892.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (hoh.row3.product) — Multiply line (a) by 32% (0.32)
Status: **MATCH**

Model: The IRS HOH row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches.

### (d) (hoh.row3.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $24,676 (tcw.hoh.b3.subtract) from column (c) (hoh.row3.product).

Model: The IRS line (d) is the 'Subtraction amount' of $24,676.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (hoh.row4.product) — Multiply line (a) by 35% (0.35)
Status: **MATCH**

Model: The IRS HOH row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches.

### (d) (hoh.row4.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $32,191 (tcw.hoh.b4.subtract) from column (c) (hoh.row4.product).

Model: The IRS line (d) is the 'Subtraction amount' of $32,191.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### (c) (hoh.row5.product) — Multiply line (a) by 37% (0.37)
Status: **MATCH**

Model: The IRS HOH row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches.

### (d) (hoh.row5.tax) — Subtract (d) from (c)
Status: **MISMATCH**

Restated: Subtract $44,718 (tcw.hoh.b5.subtract) from column (c) (hoh.row5.product).

Model: The IRS line (d) is the 'Subtraction amount' of $44,718.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction.

Ruling: open

### Tax (hoh.result) — Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Ente
Status: **MATCH**

Model: The IRS Section D says to complete the row that applies and enter the result on line 16; the program chooses the row using the HOH taxable-income thresholds and the corresponding tax amount.

### Tax (tax) — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **MATCH**

Model: The IRS provides Section A for Single, Section B for MFJ/QSS, Section C for MFS, and Section D for HOH; the program maps those filing statuses to the correct sections.

## Raw response

```yaml
lines:
  - key: "(a)"
    status: MATCH
    reason: "The IRS column (a) says to enter the amount from line 15 (or the other form/worksheet amount being computed); the restatement uses the amount whose tax is computed."
  - key: "(c) (single.row1.product)"
    status: MATCH
    reason: "The IRS single row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches."
  - key: "(d) (single.row1.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $5,086.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (single.row2.product)"
    status: MATCH
    reason: "The IRS single row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches."
  - key: "(d) (single.row2.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $7,153.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (single.row3.product)"
    status: MATCH
    reason: "The IRS single row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches."
  - key: "(d) (single.row3.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $22,937.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (single.row4.product)"
    status: MATCH
    reason: "The IRS single row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches."
  - key: "(d) (single.row4.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $30,452.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (single.row5.product)"
    status: MATCH
    reason: "The IRS single row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches."
  - key: "(d) (single.row5.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $42,979.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "Tax (single.result)"
    status: MATCH
    reason: "The IRS Section A says to complete the row that applies and enter the result on line 16; the program chooses the row using the Single taxable-income thresholds and the corresponding tax amount."
  - key: "(c) (mfj.row1.product)"
    status: MATCH
    reason: "The IRS MFJ row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches."
  - key: "(d) (mfj.row1.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $10,172.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfj.row2.product)"
    status: MATCH
    reason: "The IRS MFJ row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches."
  - key: "(d) (mfj.row2.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $14,306.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfj.row3.product)"
    status: MATCH
    reason: "The IRS MFJ row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches."
  - key: "(d) (mfj.row3.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $45,874.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfj.row4.product)"
    status: MATCH
    reason: "The IRS MFJ row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches."
  - key: "(d) (mfj.row4.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $60,905.50, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfj.row5.product)"
    status: MATCH
    reason: "The IRS MFJ row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches."
  - key: "(d) (mfj.row5.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $75,937.50, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "Tax (mfj.result)"
    status: MATCH
    reason: "The IRS Section B says to complete the row that applies and enter the result on line 16; the program chooses the row using the MFJ/QSS taxable-income thresholds and the corresponding tax amount."
  - key: "(c) (mfs.row1.product)"
    status: MATCH
    reason: "The IRS MFS row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches."
  - key: "(d) (mfs.row1.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $5,086.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfs.row2.product)"
    status: MATCH
    reason: "The IRS MFS row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches."
  - key: "(d) (mfs.row2.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $7,153.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfs.row3.product)"
    status: MATCH
    reason: "The IRS MFS row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches."
  - key: "(d) (mfs.row3.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $22,937.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfs.row4.product)"
    status: MATCH
    reason: "The IRS MFS row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches."
  - key: "(d) (mfs.row4.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $30,452.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (mfs.row5.product)"
    status: MATCH
    reason: "The IRS MFS row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches."
  - key: "(d) (mfs.row5.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $37,968.75, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "Tax (mfs.result)"
    status: MATCH
    reason: "The IRS Section C says to complete the row that applies and enter the result on line 16; the program chooses the row using the MFS taxable-income thresholds and the corresponding tax amount."
  - key: "(c) (hoh.row1.product)"
    status: MATCH
    reason: "The IRS HOH row 1 column (c) says 'Multiply (a) by (b)' with (b) 22% (0.22); the restatement matches."
  - key: "(d) (hoh.row1.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $6,825.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (hoh.row2.product)"
    status: MATCH
    reason: "The IRS HOH row 2 column (c) says 'Multiply (a) by (b)' with (b) 24% (0.24); the restatement matches."
  - key: "(d) (hoh.row2.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $8,892.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (hoh.row3.product)"
    status: MATCH
    reason: "The IRS HOH row 3 column (c) says 'Multiply (a) by (b)' with (b) 32% (0.32); the restatement matches."
  - key: "(d) (hoh.row3.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $24,676.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (hoh.row4.product)"
    status: MATCH
    reason: "The IRS HOH row 4 column (c) says 'Multiply (a) by (b)' with (b) 35% (0.35); the restatement matches."
  - key: "(d) (hoh.row4.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $32,191.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "(c) (hoh.row5.product)"
    status: MATCH
    reason: "The IRS HOH row 5 column (c) says 'Multiply (a) by (b)' with (b) 37% (0.37); the restatement matches."
  - key: "(d) (hoh.row5.tax)"
    status: MISMATCH
    reason: "The IRS line (d) is the 'Subtraction amount' of $44,718.00, not the result of subtracting it from column (c); 'Subtract (d) from (c)' is the separate Tax-column instruction."
  - key: "Tax (hoh.result)"
    status: MATCH
    reason: "The IRS Section D says to complete the row that applies and enter the result on line 16; the program chooses the row using the HOH taxable-income thresholds and the corresponding tax amount."
  - key: "Tax (tax)"
    status: MATCH
    reason: "The IRS provides Section A for Single, Section B for MFJ/QSS, Section C for MFS, and Section D for HOH; the program maps those filing statuses to the correct sections."
```
