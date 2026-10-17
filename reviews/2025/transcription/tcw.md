# Transcription agreement — tcw

Second transcription of `Tax Computation Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/tcw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | aa509e21bc0cdab8e99a28061aca23f559cedbc1e577f035fe282784c30c293f |
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

Ruling: equivalent representation; project retained after BUG-0002. The first row of each section reads “At least $100,000 but not over …” (i1040gi, 2025 Tax Computation Worksheet, Sections A–D); the project encodes both bounds, the second transcription only the upper one, because the worksheet is entered only for amounts of $100,000 or more (the table-or-worksheet switch in `tax_on_amount`). Within that switch the two agree. Every other row, and the per-status parameters, agree exactly once the project's upper bounds were corrected to inclusive (BUG-0002, BUG_INVENTORY.md): before that fix this comparison showed the strict bounds the text does not have.

## Raw second transcription

```yaml
```yaml
lines:
  - id: tcw.lineA1(c)
    printed: "(c)"
    label: "Section A—Single. At least $100,000 but not over $103,350. Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
    note: "The printed labels (c), (d) and Tax repeat in every row and section, so the literal id 'tcw.line<printed>' would not be unique. Chosen: insert the section letter (A-D) and row number (1-5) after 'line', e.g. tcw.lineA1(c). Each section's Tax line is tcw.lineTax_<section> and the overall Tax line is tcw.lineTax. Column (a) is the bound input 'amount', which the Note says may come from another form or worksheet. The text does not say whether the product in (c) is rounded. Chosen: no rounding beyond the multiply_rate atom."
  - id: tcw.lineA1(d)
    printed: "(d)"
    label: "Section A—Single. At least $100,000 but not over $103,350. Subtraction amount $5,086.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.single.b1.subtract}
    note: "The supplied label for this line reads 'Subtract (d) from (c)', which is the wording of the Tax column. Printed column (d) is headed 'Subtraction amount.' Chosen: (d) holds the printed subtraction amount, and the row result (c) minus (d) is a helper line."
  - id: tcw.h_A1_result
    printed: "(helper)"
    label: "Section A, row 1: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineA1(c), take: tcw.lineA1(d)}
  - id: tcw.lineA2(c)
    printed: "(c)"
    label: "Section A—Single. Over $103,350 but not over $197,300. Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
  - id: tcw.lineA2(d)
    printed: "(d)"
    label: "Section A—Single. Over $103,350 but not over $197,300. Subtraction amount $7,153.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.single.b2.subtract}
  - id: tcw.h_A2_result
    printed: "(helper)"
    label: "Section A, row 2: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineA2(c), take: tcw.lineA2(d)}
  - id: tcw.lineA3(c)
    printed: "(c)"
    label: "Section A—Single. Over $197,300 but not over $250,525. Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
  - id: tcw.lineA3(d)
    printed: "(d)"
    label: "Section A—Single. Over $197,300 but not over $250,525. Subtraction amount $22,937.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.single.b3.subtract}
  - id: tcw.h_A3_result
    printed: "(helper)"
    label: "Section A, row 3: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineA3(c), take: tcw.lineA3(d)}
  - id: tcw.lineA4(c)
    printed: "(c)"
    label: "Section A—Single. Over $250,525 but not over $626,350. Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
  - id: tcw.lineA4(d)
    printed: "(d)"
    label: "Section A—Single. Over $250,525 but not over $626,350. Subtraction amount $30,452.75"
    type: NonNegDollars
    expr: {op: param, ref: tcw.single.b4.subtract}
  - id: tcw.h_A4_result
    printed: "(helper)"
    label: "Section A, row 4: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineA4(c), take: tcw.lineA4(d)}
  - id: tcw.lineA5(c)
    printed: "(c)"
    label: "Section A—Single. Over $626,350. Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
  - id: tcw.lineA5(d)
    printed: "(d)"
    label: "Section A—Single. Over $626,350. Subtraction amount $42,979.75"
    type: NonNegDollars
    expr: {op: param, ref: tcw.single.b5.subtract}
  - id: tcw.h_A5_result
    printed: "(helper)"
    label: "Section A, row 5: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineA5(c), take: tcw.lineA5(d)}
  - id: tcw.lineTax_A
    printed: "Tax"
    label: "Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.single.b1.upper}]}
          then: tcw.h_A1_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b1.upper}]}, {op: test, le: [amount, {param: tcw.single.b2.upper}]}]}
          then: tcw.h_A2_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b2.upper}]}, {op: test, le: [amount, {param: tcw.single.b3.upper}]}]}
          then: tcw.h_A3_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b3.upper}]}, {op: test, le: [amount, {param: tcw.single.b4.upper}]}]}
          then: tcw.h_A4_result
        - guard: {op: test, gt: [amount, {param: tcw.single.b4.upper}]}
          then: tcw.h_A5_result
    note: "Row 1 applies only to amounts of at least $100,000; amounts below $100,000 are outside this worksheet. Chosen: row 1's guard is simply 'not over' the row-1 upper bound, so the guards are exhaustive. The caller is expected to send only amounts of $100,000 or more. The same reading applies to Sections B, C and D."
  - id: tcw.lineB1(c)
    printed: "(c)"
    label: "Section B—MFJ or QSS. At least $100,000 but not over $206,700. Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
  - id: tcw.lineB1(d)
    printed: "(d)"
    label: "Section B—MFJ or QSS. At least $100,000 but not over $206,700. Subtraction amount $10,172.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfj.b1.subtract}
  - id: tcw.h_B1_result
    printed: "(helper)"
    label: "Section B, row 1: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineB1(c), take: tcw.lineB1(d)}
  - id: tcw.lineB2(c)
    printed: "(c)"
    label: "Section B—MFJ or QSS. Over $206,700 but not over $394,600. Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
  - id: tcw.lineB2(d)
    printed: "(d)"
    label: "Section B—MFJ or QSS. Over $206,700 but not over $394,600. Subtraction amount $14,306.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfj.b2.subtract}
  - id: tcw.h_B2_result
    printed: "(helper)"
    label: "Section B, row 2: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineB2(c), take: tcw.lineB2(d)}
  - id: tcw.lineB3(c)
    printed: "(c)"
    label: "Section B—MFJ or QSS. Over $394,600 but not over $501,050. Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
  - id: tcw.lineB3(d)
    printed: "(d)"
    label: "Section B—MFJ or QSS. Over $394,600 but not over $501,050. Subtraction amount $45,874.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfj.b3.subtract}
  - id: tcw.h_B3_result
    printed: "(helper)"
    label: "Section B, row 3: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineB3(c), take: tcw.lineB3(d)}
  - id: tcw.lineB4(c)
    printed: "(c)"
    label: "Section B—MFJ or QSS. Over $501,050 but not over $751,600. Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
  - id: tcw.lineB4(d)
    printed: "(d)"
    label: "Section B—MFJ or QSS. Over $501,050 but not over $751,600. Subtraction amount $60,905.50"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfj.b4.subtract}
  - id: tcw.h_B4_result
    printed: "(helper)"
    label: "Section B, row 4: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineB4(c), take: tcw.lineB4(d)}
  - id: tcw.lineB5(c)
    printed: "(c)"
    label: "Section B—MFJ or QSS. Over $751,600. Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
  - id: tcw.lineB5(d)
    printed: "(d)"
    label: "Section B—MFJ or QSS. Over $751,600. Subtraction amount $75,937.50"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfj.b5.subtract}
  - id: tcw.h_B5_result
    printed: "(helper)"
    label: "Section B, row 5: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineB5(c), take: tcw.lineB5(d)}
  - id: tcw.lineTax_B
    printed: "Tax"
    label: "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfj.b1.upper}]}
          then: tcw.h_B1_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b2.upper}]}]}
          then: tcw.h_B2_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b3.upper}]}]}
          then: tcw.h_B3_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b4.upper}]}]}
          then: tcw.h_B4_result
        - guard: {op: test, gt: [amount, {param: tcw.mfj.b4.upper}]}
          then: tcw.h_B5_result
  - id: tcw.lineC1(c)
    printed: "(c)"
    label: "Section C—MFS. At least $100,000 but not over $103,350. Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
  - id: tcw.lineC1(d)
    printed: "(d)"
    label: "Section C—MFS. At least $100,000 but not over $103,350. Subtraction amount $5,086.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfs.b1.subtract}
  - id: tcw.h_C1_result
    printed: "(helper)"
    label: "Section C, row 1: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineC1(c), take: tcw.lineC1(d)}
  - id: tcw.lineC2(c)
    printed: "(c)"
    label: "Section C—MFS. Over $103,350 but not over $197,300. Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
  - id: tcw.lineC2(d)
    printed: "(d)"
    label: "Section C—MFS. Over $103,350 but not over $197,300. Subtraction amount $7,153.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfs.b2.subtract}
  - id: tcw.h_C2_result
    printed: "(helper)"
    label: "Section C, row 2: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineC2(c), take: tcw.lineC2(d)}
  - id: tcw.lineC3(c)
    printed: "(c)"
    label: "Section C—MFS. Over $197,300 but not over $250,525. Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
  - id: tcw.lineC3(d)
    printed: "(d)"
    label: "Section C—MFS. Over $197,300 but not over $250,525. Subtraction amount $22,937.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfs.b3.subtract}
  - id: tcw.h_C3_result
    printed: "(helper)"
    label: "Section C, row 3: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineC3(c), take: tcw.lineC3(d)}
  - id: tcw.lineC4(c)
    printed: "(c)"
    label: "Section C—MFS. Over $250,525 but not over $375,800. Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
  - id: tcw.lineC4(d)
    printed: "(d)"
    label: "Section C—MFS. Over $250,525 but not over $375,800. Subtraction amount $30,452.75"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfs.b4.subtract}
  - id: tcw.h_C4_result
    printed: "(helper)"
    label: "Section C, row 4: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineC4(c), take: tcw.lineC4(d)}
  - id: tcw.lineC5(c)
    printed: "(c)"
    label: "Section C—MFS. Over $375,800. Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
  - id: tcw.lineC5(d)
    printed: "(d)"
    label: "Section C—MFS. Over $375,800. Subtraction amount $37,968.75"
    type: NonNegDollars
    expr: {op: param, ref: tcw.mfs.b5.subtract}
  - id: tcw.h_C5_result
    printed: "(helper)"
    label: "Section C, row 5: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineC5(c), take: tcw.lineC5(d)}
  - id: tcw.lineTax_C
    printed: "Tax"
    label: "Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfs.b1.upper}]}
          then: tcw.h_C1_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b2.upper}]}]}
          then: tcw.h_C2_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b3.upper}]}]}
          then: tcw.h_C3_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b4.upper}]}]}
          then: tcw.h_C4_result
        - guard: {op: test, gt: [amount, {param: tcw.mfs.b4.upper}]}
          then: tcw.h_C5_result
  - id: tcw.lineD1(c)
    printed: "(c)"
    label: "Section D—Head of household. At least $100,000 but not over $103,350. Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
  - id: tcw.lineD1(d)
    printed: "(d)"
    label: "Section D—Head of household. At least $100,000 but not over $103,350. Subtraction amount $6,825.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.hoh.b1.subtract}
  - id: tcw.h_D1_result
    printed: "(helper)"
    label: "Section D, row 1: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineD1(c), take: tcw.lineD1(d)}
  - id: tcw.lineD2(c)
    printed: "(c)"
    label: "Section D—Head of household. Over $103,350 but not over $197,300. Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
  - id: tcw.lineD2(d)
    printed: "(d)"
    label: "Section D—Head of household. Over $103,350 but not over $197,300. Subtraction amount $8,892.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.hoh.b2.subtract}
  - id: tcw.h_D2_result
    printed: "(helper)"
    label: "Section D, row 2: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineD2(c), take: tcw.lineD2(d)}
  - id: tcw.lineD3(c)
    printed: "(c)"
    label: "Section D—Head of household. Over $197,300 but not over $250,500. Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
  - id: tcw.lineD3(d)
    printed: "(d)"
    label: "Section D—Head of household. Over $197,300 but not over $250,500. Subtraction amount $24,676.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.hoh.b3.subtract}
  - id: tcw.h_D3_result
    printed: "(helper)"
    label: "Section D, row 3: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineD3(c), take: tcw.lineD3(d)}
  - id: tcw.lineD4(c)
    printed: "(c)"
    label: "Section D—Head of household. Over $250,500 but not over $626,350. Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
  - id: tcw.lineD4(d)
    printed: "(d)"
    label: "Section D—Head of household. Over $250,500 but not over $626,350. Subtraction amount $32,191.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.hoh.b4.subtract}
  - id: tcw.h_D4_result
    printed: "(helper)"
    label: "Section D, row 4: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineD4(c), take: tcw.lineD4(d)}
  - id: tcw.lineD5(c)
    printed: "(c)"
    label: "Section D—Head of household. Over $626,350. Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
  - id: tcw.lineD5(d)
    printed: "(d)"
    label: "Section D—Head of household. Over $626,350. Subtraction amount $44,718.00"
    type: NonNegDollars
    expr: {op: param, ref: tcw.hoh.b5.subtract}
  - id: tcw.h_D5_result
    printed: "(helper)"
    label: "Section D, row 5: Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.lineD5(c), take: tcw.lineD5(d)}
  - id: tcw.lineTax_D
    printed: "Tax"
    label: "Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.hoh.b1.upper}]}
          then: tcw.h_D1_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b1.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b2.upper}]}]}
          then: tcw.h_D2_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b2.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b3.upper}]}]}
          then: tcw.h_D3_result
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b3.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b4.upper}]}]}
          then: tcw.h_D4_result
        - guard: {op: test, gt: [amount, {param: tcw.hoh.b4.upper}]}
          then: tcw.h_D5_result
  - id: tcw.lineTax
    printed: "Tax"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [status, {const: "single"}]}
          then: tcw.lineTax_A
        - guard: {op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}
          then: tcw.lineTax_B
        - guard: {op: test, eq: [status, {const: "mfs"}]}
          then: tcw.lineTax_C
        - guard: {op: test, eq: [status, {const: "hoh"}]}
          then: tcw.lineTax_D
    note: "Sections A-D are each selected by filing status. Section B covers both Married filing jointly and Qualifying surviving spouse. The five enum values make these guards exhaustive and disjoint."
  - id: tax
    printed: "(helper)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr: {op: copy, from: tcw.lineTax}
```
```
