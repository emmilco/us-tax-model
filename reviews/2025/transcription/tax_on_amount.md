# Transcription agreement — tax_on_amount

Second transcription of `Tax on an amount — Tax Table or Tax Computation Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/tax_on_amount.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | eb3f901f710a29d6bd4650c63a8fba816e6bd9e49422349ce7af5467c7ce127e |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### tax — Tax on the amount
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Ruling: equivalent representation; project retained. Below $100,000 both use the Tax Table lookup; at or above it both enter the Tax Computation Worksheet, whose single remaining difference is the redundant lower bound on each section's first row recorded in the `tcw` log. The second transcription groups the joint and surviving-spouse statuses in one alternative where the project lists them separately with the same result; the comparison treats those as one case.

## Raw second transcription

```yaml
```yaml
lines:
  - id: tax_on_amount.line(a)_table
    printed: "(a)"
    label: "Use the Tax Table"
    type: Bool
    expr:
      op: test
      lt: [amount, {param: ordinary.table_boundary}]
    note: "Two printed lines share the printed number '(a)', so the pattern tax_on_amount.line(a) would give both the same id. Suffixes _table and _tcw were added to keep the ids distinct. The Tax Computation Worksheet rows begin 'At least $100,000', so the Tax Table is read as applying when the amount is less than $100,000."
  - id: tax_on_amount.line(a)_tcw
    printed: "(a)"
    label: "Use the Tax Computation Worksheet"
    type: Bool
    expr:
      op: test
      ge: [amount, {param: ordinary.table_boundary}]
    note: "Id suffixed _tcw to avoid colliding with the Tax Table line. The worksheet applies 'At least $100,000'."

  # Section A — Single
  - id: tax_on_amount.h_single_r1_c
    printed: "(helper)"
    label: "Section A, at least $100,000 but not over $103,350: (c) Multiply (a) by (b), 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
  - id: tax_on_amount.h_single_r1_tax
    printed: "(helper)"
    label: "Section A row 1 Tax. Subtract (d) from (c), (d) $5,086.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r1_c, take: {param: tcw.single.b1.subtract}}
  - id: tax_on_amount.h_single_r2_c
    printed: "(helper)"
    label: "Section A, over $103,350 but not over $197,300: (c) Multiply (a) by (b), 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
  - id: tax_on_amount.h_single_r2_tax
    printed: "(helper)"
    label: "Section A row 2 Tax. Subtract (d) from (c), (d) $7,153.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r2_c, take: {param: tcw.single.b2.subtract}}
  - id: tax_on_amount.h_single_r3_c
    printed: "(helper)"
    label: "Section A, over $197,300 but not over $250,525: (c) Multiply (a) by (b), 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
  - id: tax_on_amount.h_single_r3_tax
    printed: "(helper)"
    label: "Section A row 3 Tax. Subtract (d) from (c), (d) $22,937.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r3_c, take: {param: tcw.single.b3.subtract}}
  - id: tax_on_amount.h_single_r4_c
    printed: "(helper)"
    label: "Section A, over $250,525 but not over $626,350: (c) Multiply (a) by (b), 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
  - id: tax_on_amount.h_single_r4_tax
    printed: "(helper)"
    label: "Section A row 4 Tax. Subtract (d) from (c), (d) $30,452.75"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r4_c, take: {param: tcw.single.b4.subtract}}
  - id: tax_on_amount.h_single_r5_c
    printed: "(helper)"
    label: "Section A, over $626,350: (c) Multiply (a) by (b), 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
  - id: tax_on_amount.h_single_r5_tax
    printed: "(helper)"
    label: "Section A row 5 Tax. Subtract (d) from (c), (d) $42,979.75"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r5_c, take: {param: tcw.single.b5.subtract}}
  - id: tax_on_amount.h_single
    printed: "(helper)"
    label: "Section A—Use if your filing status is Single. Complete the row below that applies to you."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.single.b1.upper}]}
          then: tax_on_amount.h_single_r1_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b1.upper}]}, {op: test, le: [amount, {param: tcw.single.b2.upper}]}]}
          then: tax_on_amount.h_single_r2_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b2.upper}]}, {op: test, le: [amount, {param: tcw.single.b3.upper}]}]}
          then: tax_on_amount.h_single_r3_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.single.b3.upper}]}, {op: test, le: [amount, {param: tcw.single.b4.upper}]}]}
          then: tax_on_amount.h_single_r4_tax
        - guard: {op: test, gt: [amount, {param: tcw.single.b4.upper}]}
          then: tax_on_amount.h_single_r5_tax
    note: "Row 1 is printed 'At least $100,000 but not over $103,350'. Its lower bound is left out of the guard so the choice is exhaustive. This worksheet is reached only when the amount is at least $100,000."

  # Section B — Married filing jointly or Qualifying surviving spouse
  - id: tax_on_amount.h_mfj_r1_c
    printed: "(helper)"
    label: "Section B, at least $100,000 but not over $206,700: (c) Multiply (a) by (b), 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
  - id: tax_on_amount.h_mfj_r1_tax
    printed: "(helper)"
    label: "Section B row 1 Tax. Subtract (d) from (c), (d) $10,172.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r1_c, take: {param: tcw.mfj.b1.subtract}}
  - id: tax_on_amount.h_mfj_r2_c
    printed: "(helper)"
    label: "Section B, over $206,700 but not over $394,600: (c) Multiply (a) by (b), 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
  - id: tax_on_amount.h_mfj_r2_tax
    printed: "(helper)"
    label: "Section B row 2 Tax. Subtract (d) from (c), (d) $14,306.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r2_c, take: {param: tcw.mfj.b2.subtract}}
  - id: tax_on_amount.h_mfj_r3_c
    printed: "(helper)"
    label: "Section B, over $394,600 but not over $501,050: (c) Multiply (a) by (b), 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
  - id: tax_on_amount.h_mfj_r3_tax
    printed: "(helper)"
    label: "Section B row 3 Tax. Subtract (d) from (c), (d) $45,874.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r3_c, take: {param: tcw.mfj.b3.subtract}}
  - id: tax_on_amount.h_mfj_r4_c
    printed: "(helper)"
    label: "Section B, over $501,050 but not over $751,600: (c) Multiply (a) by (b), 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
  - id: tax_on_amount.h_mfj_r4_tax
    printed: "(helper)"
    label: "Section B row 4 Tax. Subtract (d) from (c), (d) $60,905.50"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r4_c, take: {param: tcw.mfj.b4.subtract}}
  - id: tax_on_amount.h_mfj_r5_c
    printed: "(helper)"
    label: "Section B, over $751,600: (c) Multiply (a) by (b), 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
  - id: tax_on_amount.h_mfj_r5_tax
    printed: "(helper)"
    label: "Section B row 5 Tax. Subtract (d) from (c), (d) $75,937.50"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r5_c, take: {param: tcw.mfj.b5.subtract}}
  - id: tax_on_amount.h_mfj
    printed: "(helper)"
    label: "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse. Complete the row below that applies to you."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfj.b1.upper}]}
          then: tax_on_amount.h_mfj_r1_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b2.upper}]}]}
          then: tax_on_amount.h_mfj_r2_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b3.upper}]}]}
          then: tax_on_amount.h_mfj_r3_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfj.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b4.upper}]}]}
          then: tax_on_amount.h_mfj_r4_tax
        - guard: {op: test, gt: [amount, {param: tcw.mfj.b4.upper}]}
          then: tax_on_amount.h_mfj_r5_tax

  # Section C — Married filing separately
  - id: tax_on_amount.h_mfs_r1_c
    printed: "(helper)"
    label: "Section C, at least $100,000 but not over $103,350: (c) Multiply (a) by (b), 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
  - id: tax_on_amount.h_mfs_r1_tax
    printed: "(helper)"
    label: "Section C row 1 Tax. Subtract (d) from (c), (d) $5,086.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r1_c, take: {param: tcw.mfs.b1.subtract}}
  - id: tax_on_amount.h_mfs_r2_c
    printed: "(helper)"
    label: "Section C, over $103,350 but not over $197,300: (c) Multiply (a) by (b), 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
  - id: tax_on_amount.h_mfs_r2_tax
    printed: "(helper)"
    label: "Section C row 2 Tax. Subtract (d) from (c), (d) $7,153.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r2_c, take: {param: tcw.mfs.b2.subtract}}
  - id: tax_on_amount.h_mfs_r3_c
    printed: "(helper)"
    label: "Section C, over $197,300 but not over $250,525: (c) Multiply (a) by (b), 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
  - id: tax_on_amount.h_mfs_r3_tax
    printed: "(helper)"
    label: "Section C row 3 Tax. Subtract (d) from (c), (d) $22,937.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r3_c, take: {param: tcw.mfs.b3.subtract}}
  - id: tax_on_amount.h_mfs_r4_c
    printed: "(helper)"
    label: "Section C, over $250,525 but not over $375,800: (c) Multiply (a) by (b), 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
  - id: tax_on_amount.h_mfs_r4_tax
    printed: "(helper)"
    label: "Section C row 4 Tax. Subtract (d) from (c), (d) $30,452.75"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r4_c, take: {param: tcw.mfs.b4.subtract}}
  - id: tax_on_amount.h_mfs_r5_c
    printed: "(helper)"
    label: "Section C, over $375,800: (c) Multiply (a) by (b), 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
  - id: tax_on_amount.h_mfs_r5_tax
    printed: "(helper)"
    label: "Section C row 5 Tax. Subtract (d) from (c), (d) $37,968.75"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r5_c, take: {param: tcw.mfs.b5.subtract}}
  - id: tax_on_amount.h_mfs
    printed: "(helper)"
    label: "Section C—Use if your filing status is Married filing separately. Complete the row below that applies to you."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.mfs.b1.upper}]}
          then: tax_on_amount.h_mfs_r1_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b2.upper}]}]}
          then: tax_on_amount.h_mfs_r2_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b3.upper}]}]}
          then: tax_on_amount.h_mfs_r3_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.mfs.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b4.upper}]}]}
          then: tax_on_amount.h_mfs_r4_tax
        - guard: {op: test, gt: [amount, {param: tcw.mfs.b4.upper}]}
          then: tax_on_amount.h_mfs_r5_tax

  # Section D — Head of household
  - id: tax_on_amount.h_hoh_r1_c
    printed: "(helper)"
    label: "Section D, at least $100,000 but not over $103,350: (c) Multiply (a) by (b), 22% (0.22)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
  - id: tax_on_amount.h_hoh_r1_tax
    printed: "(helper)"
    label: "Section D row 1 Tax. Subtract (d) from (c), (d) $6,825.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r1_c, take: {param: tcw.hoh.b1.subtract}}
  - id: tax_on_amount.h_hoh_r2_c
    printed: "(helper)"
    label: "Section D, over $103,350 but not over $197,300: (c) Multiply (a) by (b), 24% (0.24)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
  - id: tax_on_amount.h_hoh_r2_tax
    printed: "(helper)"
    label: "Section D row 2 Tax. Subtract (d) from (c), (d) $8,892.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r2_c, take: {param: tcw.hoh.b2.subtract}}
  - id: tax_on_amount.h_hoh_r3_c
    printed: "(helper)"
    label: "Section D, over $197,300 but not over $250,500: (c) Multiply (a) by (b), 32% (0.32)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
  - id: tax_on_amount.h_hoh_r3_tax
    printed: "(helper)"
    label: "Section D row 3 Tax. Subtract (d) from (c), (d) $24,676.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r3_c, take: {param: tcw.hoh.b3.subtract}}
  - id: tax_on_amount.h_hoh_r4_c
    printed: "(helper)"
    label: "Section D, over $250,500 but not over $626,350: (c) Multiply (a) by (b), 35% (0.35)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
  - id: tax_on_amount.h_hoh_r4_tax
    printed: "(helper)"
    label: "Section D row 4 Tax. Subtract (d) from (c), (d) $32,191.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r4_c, take: {param: tcw.hoh.b4.subtract}}
  - id: tax_on_amount.h_hoh_r5_c
    printed: "(helper)"
    label: "Section D, over $626,350: (c) Multiply (a) by (b), 37% (0.37)"
    type: Dollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
  - id: tax_on_amount.h_hoh_r5_tax
    printed: "(helper)"
    label: "Section D row 5 Tax. Subtract (d) from (c), (d) $44,718.00"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r5_c, take: {param: tcw.hoh.b5.subtract}}
  - id: tax_on_amount.h_hoh
    printed: "(helper)"
    label: "Section D—Use if your filing status is Head of household. Complete the row below that applies to you."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: tcw.hoh.b1.upper}]}
          then: tax_on_amount.h_hoh_r1_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b1.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b2.upper}]}]}
          then: tax_on_amount.h_hoh_r2_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b2.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b3.upper}]}]}
          then: tax_on_amount.h_hoh_r3_tax
        - guard: {op: test, all: [{op: test, gt: [amount, {param: tcw.hoh.b3.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b4.upper}]}]}
          then: tax_on_amount.h_hoh_r4_tax
        - guard: {op: test, gt: [amount, {param: tcw.hoh.b4.upper}]}
          then: tax_on_amount.h_hoh_r5_tax

  - id: tax_on_amount.h_tcw
    printed: "(helper)"
    label: "Tax Computation Worksheet result for the section matching filing status"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [status, {const: "single"}]}
          then: tax_on_amount.h_single
        - guard: {op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}
          then: tax_on_amount.h_mfj
        - guard: {op: test, eq: [status, {const: "mfs"}]}
          then: tax_on_amount.h_mfs
        - guard: {op: test, eq: [status, {const: "hoh"}]}
          then: tax_on_amount.h_hoh
    note: "Section B states it applies to 'Married filing jointly or Qualifying surviving spouse', so qss is routed to Section B."
  - id: tax_on_amount.h_table
    printed: "(helper)"
    label: "Tax Table: find the taxable income line and filing status column; the amount where they meet"
    type: Dollars
    expr: {op: table_lookup, table: tax_table, key: amount, status: status}
    note: "The Tax Table footnote says the Married filing jointly column 'must also be used by a qualifying surviving spouse'. The table_lookup is assumed to map qss to the mfj column."

  - id: tax_on_amount.line(b)
    printed: "(b)"
    label: "Tax on the amount"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [tax_on_amount.line(a)_table, {const: true}]}
          then: tax_on_amount.h_table
        - guard: {op: test, eq: [tax_on_amount.line(a)_tcw, {const: true}]}
          then: tax_on_amount.h_tcw
    note: "The Tax Computation Worksheet text gives no rounding rule, so its result is kept in cents with no rounding. Tax Table results are whole dollars as printed."

  - id: tax
    printed: "(helper)"
    label: "Tax on the amount"
    type: Dollars
    expr: {op: copy, from: tax_on_amount.line(b)}
```
```
