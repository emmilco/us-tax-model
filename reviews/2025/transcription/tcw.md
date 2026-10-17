# Transcription agreement — tcw

Second transcription of `Tax Computation Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/tcw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 01707e97dc2dd7d38bbf04f7e9785069d3a95d203997c5d53212238a25332ddb |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

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
  # ---------------- Section A — Single ----------------
  - id: tcw.line(c).single.b1
    printed: "(c)"
    label: "Section A—Single. At least $100,000 but not over $103,350. Multiply line (a) by 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
    note: "Open: the requested id pattern tcw.line<printed> repeats across rows and sections. Chosen: suffix .<section>.<row> so each id is unique. Open: no rounding is printed for (a)×(b). Chosen: no round atom."
  - id: tcw.line(d).single.b1
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $5,086.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b1, take: {param: tcw.single.b1.subtract}}
  - id: tcw.line(c).single.b2
    printed: "(c)"
    label: "Section A—Single. Over $103,350 but not over $197,300. Multiply line (a) by 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
  - id: tcw.line(d).single.b2
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $7,153.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b2, take: {param: tcw.single.b2.subtract}}
  - id: tcw.line(c).single.b3
    printed: "(c)"
    label: "Section A—Single. Over $197,300 but not over $250,525. Multiply line (a) by 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
  - id: tcw.line(d).single.b3
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $22,937.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b3, take: {param: tcw.single.b3.subtract}}
  - id: tcw.line(c).single.b4
    printed: "(c)"
    label: "Section A—Single. Over $250,525 but not over $626,350. Multiply line (a) by 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
  - id: tcw.line(d).single.b4
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $30,452.75)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b4, take: {param: tcw.single.b4.subtract}}
  - id: tcw.line(c).single.b5
    printed: "(c)"
    label: "Section A—Single. Over $626,350. Multiply line (a) by 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
  - id: tcw.line(d).single.b5
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $42,979.75)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b5, take: {param: tcw.single.b5.subtract}}
  - id: tcw.lineTax.single
    printed: "Tax"
    label: "Section A—Use if your filing status is Single. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.single.b1.upper}]}
          then: tcw.line(d).single.b1
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b1.upper}]}, {op: test, le: [amount, {param: tcw.single.b2.upper}]}]}
          then: tcw.line(d).single.b2
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b2.upper}]}, {op: test, le: [amount, {param: tcw.single.b3.upper}]}]}
          then: tcw.line(d).single.b3
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b3.upper}]}, {op: test, le: [amount, {param: tcw.single.b4.upper}]}]}
          then: tcw.line(d).single.b4
        - guard: {op: test, gt: [amount, {param: tcw.single.b4.upper}]}
          then: tcw.line(d).single.b5
    note: "Open: the first row begins 'At least $100,000', and the worksheet gives no row below that amount. Chosen: the first guard is amount <= upper bound with no lower bound, so the guards stay exhaustive. Amounts under $100,000 are routed to the Tax Table by the calling line, not by this worksheet."

  # ---------------- Section B — MFJ / QSS ----------------
  - id: tcw.line(c).mfj.b1
    printed: "(c)"
    label: "Section B—MFJ/QSS. At least $100,000 but not over $206,700. Multiply line (a) by 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
  - id: tcw.line(d).mfj.b1
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $10,172.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b1, take: {param: tcw.mfj.b1.subtract}}
  - id: tcw.line(c).mfj.b2
    printed: "(c)"
    label: "Section B—MFJ/QSS. Over $206,700 but not over $394,600. Multiply line (a) by 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
  - id: tcw.line(d).mfj.b2
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $14,306.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b2, take: {param: tcw.mfj.b2.subtract}}
  - id: tcw.line(c).mfj.b3
    printed: "(c)"
    label: "Section B—MFJ/QSS. Over $394,600 but not over $501,050. Multiply line (a) by 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
  - id: tcw.line(d).mfj.b3
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $45,874.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b3, take: {param: tcw.mfj.b3.subtract}}
  - id: tcw.line(c).mfj.b4
    printed: "(c)"
    label: "Section B—MFJ/QSS. Over $501,050 but not over $751,600. Multiply line (a) by 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
  - id: tcw.line(d).mfj.b4
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $60,905.50)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b4, take: {param: tcw.mfj.b4.subtract}}
  - id: tcw.line(c).mfj.b5
    printed: "(c)"
    label: "Section B—MFJ/QSS. Over $751,600. Multiply line (a) by 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
  - id: tcw.line(d).mfj.b5
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $75,937.50)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b5, take: {param: tcw.mfj.b5.subtract}}
  - id: tcw.lineTax.mfj
    printed: "Tax"
    label: "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfj.b1.upper}]}
          then: tcw.line(d).mfj.b1
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b2.upper}]}]}
          then: tcw.line(d).mfj.b2
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b3.upper}]}]}
          then: tcw.line(d).mfj.b3
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b4.upper}]}]}
          then: tcw.line(d).mfj.b4
        - guard: {op: test, gt: [amount, {param: tcw.mfj.b4.upper}]}
          then: tcw.line(d).mfj.b5
    note: "Same lower-bound reading as Section A: the first guard has no $100,000 floor."

  # ---------------- Section C — MFS ----------------
  - id: tcw.line(c).mfs.b1
    printed: "(c)"
    label: "Section C—MFS. At least $100,000 but not over $103,350. Multiply line (a) by 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
  - id: tcw.line(d).mfs.b1
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $5,086.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b1, take: {param: tcw.mfs.b1.subtract}}
  - id: tcw.line(c).mfs.b2
    printed: "(c)"
    label: "Section C—MFS. Over $103,350 but not over $197,300. Multiply line (a) by 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
  - id: tcw.line(d).mfs.b2
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $7,153.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b2, take: {param: tcw.mfs.b2.subtract}}
  - id: tcw.line(c).mfs.b3
    printed: "(c)"
    label: "Section C—MFS. Over $197,300 but not over $250,525. Multiply line (a) by 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
  - id: tcw.line(d).mfs.b3
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $22,937.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b3, take: {param: tcw.mfs.b3.subtract}}
  - id: tcw.line(c).mfs.b4
    printed: "(c)"
    label: "Section C—MFS. Over $250,525 but not over $375,800. Multiply line (a) by 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
  - id: tcw.line(d).mfs.b4
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $30,452.75)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b4, take: {param: tcw.mfs.b4.subtract}}
  - id: tcw.line(c).mfs.b5
    printed: "(c)"
    label: "Section C—MFS. Over $375,800. Multiply line (a) by 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
  - id: tcw.line(d).mfs.b5
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $37,968.75)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b5, take: {param: tcw.mfs.b5.subtract}}
  - id: tcw.lineTax.mfs
    printed: "Tax"
    label: "Section C—Use if your filing status is Married filing separately. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfs.b1.upper}]}
          then: tcw.line(d).mfs.b1
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b2.upper}]}]}
          then: tcw.line(d).mfs.b2
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b3.upper}]}]}
          then: tcw.line(d).mfs.b3
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b4.upper}]}]}
          then: tcw.line(d).mfs.b4
        - guard: {op: test, gt: [amount, {param: tcw.mfs.b4.upper}]}
          then: tcw.line(d).mfs.b5
    note: "Same lower-bound reading as Section A: the first guard has no $100,000 floor."

  # ---------------- Section D — HOH ----------------
  - id: tcw.line(c).hoh.b1
    printed: "(c)"
    label: "Section D—HOH. At least $100,000 but not over $103,350. Multiply line (a) by 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
  - id: tcw.line(d).hoh.b1
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $6,825.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b1, take: {param: tcw.hoh.b1.subtract}}
  - id: tcw.line(c).hoh.b2
    printed: "(c)"
    label: "Section D—HOH. Over $103,350 but not over $197,300. Multiply line (a) by 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
  - id: tcw.line(d).hoh.b2
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $8,892.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b2, take: {param: tcw.hoh.b2.subtract}}
  - id: tcw.line(c).hoh.b3
    printed: "(c)"
    label: "Section D—HOH. Over $197,300 but not over $250,500. Multiply line (a) by 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
  - id: tcw.line(d).hoh.b3
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $24,676.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b3, take: {param: tcw.hoh.b3.subtract}}
  - id: tcw.line(c).hoh.b4
    printed: "(c)"
    label: "Section D—HOH. Over $250,500 but not over $626,350. Multiply line (a) by 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
  - id: tcw.line(d).hoh.b4
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $32,191.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b4, take: {param: tcw.hoh.b4.subtract}}
  - id: tcw.line(c).hoh.b5
    printed: "(c)"
    label: "Section D—HOH. Over $626,350. Multiply line (a) by 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
  - id: tcw.line(d).hoh.b5
    printed: "(d)"
    label: "Subtract (d) from (c) (subtraction amount $44,718.00)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b5, take: {param: tcw.hoh.b5.subtract}}
  - id: tcw.lineTax.hoh
    printed: "Tax"
    label: "Section D—Use if your filing status is Head of household. Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.hoh.b1.upper}]}
          then: tcw.line(d).hoh.b1
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b1.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b2.upper}]}]}
          then: tcw.line(d).hoh.b2
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b2.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b3.upper}]}]}
          then: tcw.line(d).hoh.b3
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b3.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b4.upper}]}]}
          then: tcw.line(d).hoh.b4
        - guard: {op: test, gt: [amount, {param: tcw.hoh.b4.upper}]}
          then: tcw.line(d).hoh.b5
    note: "Same lower-bound reading as Section A: the first guard has no $100,000 floor."

  # ---------------- Section selection ----------------
  - id: tcw.lineTax
    printed: "Tax"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [status, {const: "single"}]}
          then: tcw.lineTax.single
        - guard: {op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}
          then: tcw.lineTax.mfj
        - guard: {op: test, eq: [status, {const: "mfs"}]}
          then: tcw.lineTax.mfs
        - guard: {op: test, eq: [status, {const: "hoh"}]}
          then: tcw.lineTax.hoh
    note: "Section chosen by filing status as printed in the section headings: A Single; B MFJ or QSS; C MFS; D HOH."

  - id: tax
    printed: "(helper)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr: {op: copy, from: tcw.lineTax}
```
```
