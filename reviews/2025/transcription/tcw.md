# Transcription agreement — tcw

Second transcription of `Tax Computation Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/tcw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4171cc47bc78c5e2e4c50f1c5e84d8a90cadbeee658d468044d0ff3be81b6587 |
| subject sha256 | 55f4a8183a7cb641f369cd46f1f803f53d3b00535d950def877a8b757e4c5d15 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tax — Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16.
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: The task asks for 'tax' both as a printed line ('Tax (tax)') and as a helper with the same id. Ids must be unique, so I wrote one line with id 'tax' and printed 'Tax (tax)'. It also serves as the required intermediate value. The section is chosen by the filing status named in each section heading. Section B covers both mfj and qss.

Ruling: equivalent representation; project retained after BUG-0002. The first row of each section reads “At least $100,000 but not over …” (i1040gi, 2025 Tax Computation Worksheet, Sections A–D); the project encodes both bounds, the second transcription only the upper one, because the worksheet is entered only for amounts of $100,000 or more (the table-or-worksheet switch in `tax_on_amount`). Within that switch the two agree. Every other row, and the per-status parameters, agree exactly once the project's upper bounds were corrected to inclusive (BUG-0002, BUG_INVENTORY.md): before that fix this comparison showed the strict bounds the text does not have.

## Raw second transcription

```yaml
```yaml
lines:
  - id: single.row1.product
    printed: "(c) (single.row1.product)"
    label: "Multiply (a) by (b). At least $100,000 but not over $103,350: × 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 1, column (c)"
  - id: single.row1.tax
    printed: "Tax (single.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $5,086.00"
    type: Dollars
    expr: {op: subtract, from: single.row1.product, take: {param: tcw.single.b1.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 1, columns (d) and Tax"
  - id: single.row2.product
    printed: "(c) (single.row2.product)"
    label: "Multiply (a) by (b). Over $103,350 but not over $197,300: × 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 2, column (c)"
  - id: single.row2.tax
    printed: "Tax (single.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $7,153.00"
    type: Dollars
    expr: {op: subtract, from: single.row2.product, take: {param: tcw.single.b2.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 2, columns (d) and Tax"
  - id: single.row3.product
    printed: "(c) (single.row3.product)"
    label: "Multiply (a) by (b). Over $197,300 but not over $250,525: × 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 3, column (c)"
  - id: single.row3.tax
    printed: "Tax (single.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $22,937.00"
    type: Dollars
    expr: {op: subtract, from: single.row3.product, take: {param: tcw.single.b3.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 3, columns (d) and Tax"
  - id: single.row4.product
    printed: "(c) (single.row4.product)"
    label: "Multiply (a) by (b). Over $250,525 but not over $626,350: × 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 4, column (c)"
  - id: single.row4.tax
    printed: "Tax (single.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $30,452.75"
    type: Dollars
    expr: {op: subtract, from: single.row4.product, take: {param: tcw.single.b4.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 4, columns (d) and Tax"
  - id: single.row5.product
    printed: "(c) (single.row5.product)"
    label: "Multiply (a) by (b). Over $626,350: × 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 5, column (c)"
  - id: single.row5.tax
    printed: "Tax (single.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $42,979.75"
    type: Dollars
    expr: {op: subtract, from: single.row5.product, take: {param: tcw.single.b5.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A, row 5, columns (d) and Tax"
  - id: single.result
    printed: "Tax (single.result)"
    label: "Section A—Use if your filing status is Single. Complete the row below that applies to you. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.single.b1.upper}]}
          then: single.row1.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b1.upper}]}, {op: test, le: [amount, {param: tcw.single.b2.upper}]}]}
          then: single.row2.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b2.upper}]}, {op: test, le: [amount, {param: tcw.single.b3.upper}]}]}
          then: single.row3.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b3.upper}]}, {op: test, le: [amount, {param: tcw.single.b4.upper}]}]}
          then: single.row4.tax
        - guard: {op: test, gt: [amount, {param: tcw.single.b4.upper}]}
          then: single.row5.tax
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section A"
    note: "Row 1 is printed 'At least $100,000 but not over $103,350'. The worksheet is used only for amounts of $100,000 or more (Tax Table otherwise, per the line 16 instructions), so the guards must still be exhaustive. Chosen: row 1's guard has no lower bound."
  - id: mfj.row1.product
    printed: "(c) (mfj.row1.product)"
    label: "Multiply (a) by (b). At least $100,000 but not over $206,700: × 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 1, column (c)"
  - id: mfj.row1.tax
    printed: "Tax (mfj.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $10,172.00"
    type: Dollars
    expr: {op: subtract, from: mfj.row1.product, take: {param: tcw.mfj.b1.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 1, columns (d) and Tax"
  - id: mfj.row2.product
    printed: "(c) (mfj.row2.product)"
    label: "Multiply (a) by (b). Over $206,700 but not over $394,600: × 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 2, column (c)"
  - id: mfj.row2.tax
    printed: "Tax (mfj.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $14,306.00"
    type: Dollars
    expr: {op: subtract, from: mfj.row2.product, take: {param: tcw.mfj.b2.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 2, columns (d) and Tax"
  - id: mfj.row3.product
    printed: "(c) (mfj.row3.product)"
    label: "Multiply (a) by (b). Over $394,600 but not over $501,050: × 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 3, column (c)"
  - id: mfj.row3.tax
    printed: "Tax (mfj.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $45,874.00"
    type: Dollars
    expr: {op: subtract, from: mfj.row3.product, take: {param: tcw.mfj.b3.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 3, columns (d) and Tax"
  - id: mfj.row4.product
    printed: "(c) (mfj.row4.product)"
    label: "Multiply (a) by (b). Over $501,050 but not over $751,600: × 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 4, column (c)"
  - id: mfj.row4.tax
    printed: "Tax (mfj.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $60,905.50"
    type: Dollars
    expr: {op: subtract, from: mfj.row4.product, take: {param: tcw.mfj.b4.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 4, columns (d) and Tax"
  - id: mfj.row5.product
    printed: "(c) (mfj.row5.product)"
    label: "Multiply (a) by (b). Over $751,600: × 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 5, column (c)"
  - id: mfj.row5.tax
    printed: "Tax (mfj.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $75,937.50"
    type: Dollars
    expr: {op: subtract, from: mfj.row5.product, take: {param: tcw.mfj.b5.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B, row 5, columns (d) and Tax"
  - id: mfj.result
    printed: "Tax (mfj.result)"
    label: "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Complete the row below that applies to you. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfj.b1.upper}]}
          then: mfj.row1.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b2.upper}]}]}
          then: mfj.row2.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b3.upper}]}]}
          then: mfj.row3.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b4.upper}]}]}
          then: mfj.row4.tax
        - guard: {op: test, gt: [amount, {param: tcw.mfj.b4.upper}]}
          then: mfj.row5.tax
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section B"
    note: "Row 1 is printed 'At least $100,000'. Chosen: row 1's guard has no lower bound, so the guards are exhaustive; the worksheet is reached only for $100,000 or more."
  - id: mfs.row1.product
    printed: "(c) (mfs.row1.product)"
    label: "Multiply (a) by (b). At least $100,000 but not over $103,350: × 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 1, column (c)"
  - id: mfs.row1.tax
    printed: "Tax (mfs.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $5,086.00"
    type: Dollars
    expr: {op: subtract, from: mfs.row1.product, take: {param: tcw.mfs.b1.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 1, columns (d) and Tax"
  - id: mfs.row2.product
    printed: "(c) (mfs.row2.product)"
    label: "Multiply (a) by (b). Over $103,350 but not over $197,300: × 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 2, column (c)"
  - id: mfs.row2.tax
    printed: "Tax (mfs.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $7,153.00"
    type: Dollars
    expr: {op: subtract, from: mfs.row2.product, take: {param: tcw.mfs.b2.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 2, columns (d) and Tax"
  - id: mfs.row3.product
    printed: "(c) (mfs.row3.product)"
    label: "Multiply (a) by (b). Over $197,300 but not over $250,525: × 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 3, column (c)"
  - id: mfs.row3.tax
    printed: "Tax (mfs.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $22,937.00"
    type: Dollars
    expr: {op: subtract, from: mfs.row3.product, take: {param: tcw.mfs.b3.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 3, columns (d) and Tax"
  - id: mfs.row4.product
    printed: "(c) (mfs.row4.product)"
    label: "Multiply (a) by (b). Over $250,525 but not over $375,800: × 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 4, column (c)"
  - id: mfs.row4.tax
    printed: "Tax (mfs.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $30,452.75"
    type: Dollars
    expr: {op: subtract, from: mfs.row4.product, take: {param: tcw.mfs.b4.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 4, columns (d) and Tax"
  - id: mfs.row5.product
    printed: "(c) (mfs.row5.product)"
    label: "Multiply (a) by (b). Over $375,800: × 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 5, column (c)"
  - id: mfs.row5.tax
    printed: "Tax (mfs.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $37,968.75"
    type: Dollars
    expr: {op: subtract, from: mfs.row5.product, take: {param: tcw.mfs.b5.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C, row 5, columns (d) and Tax"
  - id: mfs.result
    printed: "Tax (mfs.result)"
    label: "Section C—Use if your filing status is Married filing separately. Complete the row below that applies to you. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfs.b1.upper}]}
          then: mfs.row1.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b2.upper}]}]}
          then: mfs.row2.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b3.upper}]}]}
          then: mfs.row3.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b4.upper}]}]}
          then: mfs.row4.tax
        - guard: {op: test, gt: [amount, {param: tcw.mfs.b4.upper}]}
          then: mfs.row5.tax
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section C"
    note: "Row 1 is printed 'At least $100,000'. Chosen: row 1's guard has no lower bound, so the guards are exhaustive; the worksheet is reached only for $100,000 or more."
  - id: hoh.row1.product
    printed: "(c) (hoh.row1.product)"
    label: "Multiply (a) by (b). At least $100,000 but not over $103,350: × 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 1, column (c)"
  - id: hoh.row1.tax
    printed: "Tax (hoh.row1.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $6,825.00"
    type: Dollars
    expr: {op: subtract, from: hoh.row1.product, take: {param: tcw.hoh.b1.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 1, columns (d) and Tax"
  - id: hoh.row2.product
    printed: "(c) (hoh.row2.product)"
    label: "Multiply (a) by (b). Over $103,350 but not over $197,300: × 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 2, column (c)"
  - id: hoh.row2.tax
    printed: "Tax (hoh.row2.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $8,892.00"
    type: Dollars
    expr: {op: subtract, from: hoh.row2.product, take: {param: tcw.hoh.b2.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 2, columns (d) and Tax"
  - id: hoh.row3.product
    printed: "(c) (hoh.row3.product)"
    label: "Multiply (a) by (b). Over $197,300 but not over $250,500: × 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 3, column (c)"
  - id: hoh.row3.tax
    printed: "Tax (hoh.row3.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $24,676.00"
    type: Dollars
    expr: {op: subtract, from: hoh.row3.product, take: {param: tcw.hoh.b3.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 3, columns (d) and Tax"
  - id: hoh.row4.product
    printed: "(c) (hoh.row4.product)"
    label: "Multiply (a) by (b). Over $250,500 but not over $626,350: × 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 4, column (c)"
  - id: hoh.row4.tax
    printed: "Tax (hoh.row4.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $32,191.00"
    type: Dollars
    expr: {op: subtract, from: hoh.row4.product, take: {param: tcw.hoh.b4.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 4, columns (d) and Tax"
  - id: hoh.row5.product
    printed: "(c) (hoh.row5.product)"
    label: "Multiply (a) by (b). Over $626,350: × 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 5, column (c)"
  - id: hoh.row5.tax
    printed: "Tax (hoh.row5.tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16. (d) $44,718.00"
    type: Dollars
    expr: {op: subtract, from: hoh.row5.product, take: {param: tcw.hoh.b5.subtract}}
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D, row 5, columns (d) and Tax"
  - id: hoh.result
    printed: "Tax (hoh.result)"
    label: "Section D—Use if your filing status is Head of household. Complete the row below that applies to you. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.hoh.b1.upper}]}
          then: hoh.row1.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b1.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b2.upper}]}]}
          then: hoh.row2.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b2.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b3.upper}]}]}
          then: hoh.row3.tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b3.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b4.upper}]}]}
          then: hoh.row4.tax
        - guard: {op: test, gt: [amount, {param: tcw.hoh.b4.upper}]}
          then: hoh.row5.tax
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Section D"
    note: "Row 1 is printed 'At least $100,000'. Chosen: row 1's guard has no lower bound, so the guards are exhaustive; the worksheet is reached only for $100,000 or more."
  - id: tax
    printed: "Tax (tax)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [status, {const: "single"}]}
          then: single.result
        - guard: {op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}
          then: mfj.result
        - guard: {op: test, eq: [status, {const: "mfs"}]}
          then: mfs.result
        - guard: {op: test, eq: [status, {const: "hoh"}]}
          then: hoh.result
    cite: "i1040gi 2025 p. 80, Tax Computation Worksheet, Sections A–D (section chosen by filing status)"
    note: "The task asks for 'tax' both as a printed line ('Tax (tax)') and as a helper with the same id. Ids must be unique, so I wrote one line with id 'tax' and printed 'Tax (tax)'. It also serves as the required intermediate value. The section is chosen by the filing status named in each section heading. Section B covers both mfj and qss."
```
```
