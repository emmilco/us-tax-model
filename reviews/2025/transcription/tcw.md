# Transcription agreement — tcw

Second transcription of `Tax Computation Worksheet—Line 16` by an isolated model (spec 6.5), compared line by line with `forms/2025/tcw.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 720ad5b3acf12b5ad914265c1ff8a642d40498c3e7d77912275d809bc7fc99c3 |
| subject sha256 | 9601605f80aadb63f3b3be298a70609732feb6f06dc6aca72db74347e9627493 |
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
  # ---------------- Section A — Single ----------------
  - id: tcw.line(c).single.b1
    printed: "(c)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
    cite: "i1040gi 2025 p.80, Tax Computation Worksheet, Section A, row 1, column (c)"
    note: "Printed ids repeat across rows and sections, so each id has a section/row suffix added after tcw.line<printed>."
  - id: tcw.line(d).single.b1
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b1, take: {param: tcw.single.b1.subtract}}
    cite: "i1040gi 2025 p.80, Section A, row 1 ($5,086.00 subtraction amount)"
  - id: tcw.line(c).single.b2
    printed: "(c)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
    cite: "i1040gi 2025 p.80, Section A, row 2, column (c)"
  - id: tcw.line(d).single.b2
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b2, take: {param: tcw.single.b2.subtract}}
    cite: "i1040gi 2025 p.80, Section A, row 2 ($7,153.00)"
  - id: tcw.line(c).single.b3
    printed: "(c)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
    cite: "i1040gi 2025 p.80, Section A, row 3, column (c)"
  - id: tcw.line(d).single.b3
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b3, take: {param: tcw.single.b3.subtract}}
    cite: "i1040gi 2025 p.80, Section A, row 3 ($22,937.00)"
  - id: tcw.line(c).single.b4
    printed: "(c)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
    cite: "i1040gi 2025 p.80, Section A, row 4, column (c)"
  - id: tcw.line(d).single.b4
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b4, take: {param: tcw.single.b4.subtract}}
    cite: "i1040gi 2025 p.80, Section A, row 4 ($30,452.75)"
  - id: tcw.line(c).single.b5
    printed: "(c)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
    cite: "i1040gi 2025 p.80, Section A, row 5, column (c)"
  - id: tcw.line(d).single.b5
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).single.b5, take: {param: tcw.single.b5.subtract}}
    cite: "i1040gi 2025 p.80, Section A, row 5 ($42,979.75)"
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
    cite: "i1040gi 2025 p.80, Section A, 'Complete the row below that applies to you'"
    note: "The first row reads 'At least $100,000 but not over $103,350'. The worksheet does not cover amounts below $100,000, which go to the Tax Table through the calling line. Because choose guards must be exhaustive, row 1's guard is 'not over $103,350' with no lower bound."

  # ---------------- Section B — MFJ / QSS ----------------
  - id: tcw.line(c).mfj.b1
    printed: "(c)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
    cite: "i1040gi 2025 p.80, Section B, row 1, column (c)"
  - id: tcw.line(d).mfj.b1
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b1, take: {param: tcw.mfj.b1.subtract}}
    cite: "i1040gi 2025 p.80, Section B, row 1 ($10,172.00)"
  - id: tcw.line(c).mfj.b2
    printed: "(c)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
    cite: "i1040gi 2025 p.80, Section B, row 2, column (c)"
  - id: tcw.line(d).mfj.b2
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b2, take: {param: tcw.mfj.b2.subtract}}
    cite: "i1040gi 2025 p.80, Section B, row 2 ($14,306.00)"
  - id: tcw.line(c).mfj.b3
    printed: "(c)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
    cite: "i1040gi 2025 p.80, Section B, row 3, column (c)"
  - id: tcw.line(d).mfj.b3
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b3, take: {param: tcw.mfj.b3.subtract}}
    cite: "i1040gi 2025 p.80, Section B, row 3 ($45,874.00)"
  - id: tcw.line(c).mfj.b4
    printed: "(c)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
    cite: "i1040gi 2025 p.80, Section B, row 4, column (c)"
  - id: tcw.line(d).mfj.b4
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b4, take: {param: tcw.mfj.b4.subtract}}
    cite: "i1040gi 2025 p.80, Section B, row 4 ($60,905.50)"
  - id: tcw.line(c).mfj.b5
    printed: "(c)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
    cite: "i1040gi 2025 p.80, Section B, row 5, column (c)"
  - id: tcw.line(d).mfj.b5
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfj.b5, take: {param: tcw.mfj.b5.subtract}}
    cite: "i1040gi 2025 p.80, Section B, row 5 ($75,937.50)"
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
    cite: "i1040gi 2025 p.80, Section B"
    note: "Row 1 has no lower bound, for the same reason as Section A."

  # ---------------- Section C — MFS ----------------
  - id: tcw.line(c).mfs.b1
    printed: "(c)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
    cite: "i1040gi 2025 p.80, Section C, row 1, column (c)"
  - id: tcw.line(d).mfs.b1
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b1, take: {param: tcw.mfs.b1.subtract}}
    cite: "i1040gi 2025 p.80, Section C, row 1 ($5,086.00)"
  - id: tcw.line(c).mfs.b2
    printed: "(c)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
    cite: "i1040gi 2025 p.80, Section C, row 2, column (c)"
  - id: tcw.line(d).mfs.b2
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b2, take: {param: tcw.mfs.b2.subtract}}
    cite: "i1040gi 2025 p.80, Section C, row 2 ($7,153.00)"
  - id: tcw.line(c).mfs.b3
    printed: "(c)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
    cite: "i1040gi 2025 p.80, Section C, row 3, column (c)"
  - id: tcw.line(d).mfs.b3
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b3, take: {param: tcw.mfs.b3.subtract}}
    cite: "i1040gi 2025 p.80, Section C, row 3 ($22,937.00)"
  - id: tcw.line(c).mfs.b4
    printed: "(c)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
    cite: "i1040gi 2025 p.80, Section C, row 4, column (c)"
  - id: tcw.line(d).mfs.b4
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b4, take: {param: tcw.mfs.b4.subtract}}
    cite: "i1040gi 2025 p.80, Section C, row 4 ($30,452.75)"
  - id: tcw.line(c).mfs.b5
    printed: "(c)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
    cite: "i1040gi 2025 p.80, Section C, row 5, column (c)"
  - id: tcw.line(d).mfs.b5
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).mfs.b5, take: {param: tcw.mfs.b5.subtract}}
    cite: "i1040gi 2025 p.80, Section C, row 5 ($37,968.75)"
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
    cite: "i1040gi 2025 p.80, Section C"
    note: "Row 1 has no lower bound, for the same reason as Section A."

  # ---------------- Section D — HOH ----------------
  - id: tcw.line(c).hoh.b1
    printed: "(c)"
    label: "Multiply line (a) by 22% (0.22)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
    cite: "i1040gi 2025 p.80, Section D, row 1, column (c)"
  - id: tcw.line(d).hoh.b1
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b1, take: {param: tcw.hoh.b1.subtract}}
    cite: "i1040gi 2025 p.80, Section D, row 1 ($6,825.00)"
  - id: tcw.line(c).hoh.b2
    printed: "(c)"
    label: "Multiply line (a) by 24% (0.24)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
    cite: "i1040gi 2025 p.80, Section D, row 2, column (c)"
  - id: tcw.line(d).hoh.b2
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b2, take: {param: tcw.hoh.b2.subtract}}
    cite: "i1040gi 2025 p.80, Section D, row 2 ($8,892.00)"
  - id: tcw.line(c).hoh.b3
    printed: "(c)"
    label: "Multiply line (a) by 32% (0.32)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
    cite: "i1040gi 2025 p.80, Section D, row 3, column (c)"
  - id: tcw.line(d).hoh.b3
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b3, take: {param: tcw.hoh.b3.subtract}}
    cite: "i1040gi 2025 p.80, Section D, row 3 ($24,676.00)"
  - id: tcw.line(c).hoh.b4
    printed: "(c)"
    label: "Multiply line (a) by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
    cite: "i1040gi 2025 p.80, Section D, row 4, column (c)"
  - id: tcw.line(d).hoh.b4
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b4, take: {param: tcw.hoh.b4.subtract}}
    cite: "i1040gi 2025 p.80, Section D, row 4 ($32,191.00)"
  - id: tcw.line(c).hoh.b5
    printed: "(c)"
    label: "Multiply line (a) by 37% (0.37)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
    cite: "i1040gi 2025 p.80, Section D, row 5, column (c)"
  - id: tcw.line(d).hoh.b5
    printed: "(d)"
    label: "Subtract (d) from (c)"
    type: Dollars
    expr: {op: subtract, from: tcw.line(c).hoh.b5, take: {param: tcw.hoh.b5.subtract}}
    cite: "i1040gi 2025 p.80, Section D, row 5 ($44,718.00)"
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
    cite: "i1040gi 2025 p.80, Section D"
    note: "Row 1 has no lower bound, for the same reason as Section A."

  # ---------------- Section selection by filing status ----------------
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
    cite: "i1040gi 2025 p.80, Section headings A–D (filing status)"
    note: "The worksheet does not say to round the column (c) product. The result is kept in exact cents with no rounding."

  - id: tax
    printed: "(helper)"
    label: "Tax. Subtract (d) from (c). Enter the result here and on the entry space on line 16."
    type: Dollars
    expr: {op: copy, from: tcw.lineTax}
    cite: "i1040gi 2025 p.80, Tax Computation Worksheet, Tax column"
```
```
