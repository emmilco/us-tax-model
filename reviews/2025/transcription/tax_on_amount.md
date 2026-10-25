# Transcription agreement — tax_on_amount

Second transcription of `Tax on an amount — Tax Table or Tax Computation Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/tax_on_amount.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f9c8150e3cb8c95449276817c1b3a38957c47602e26fa8729160053a5d99f553 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d0c69f842ce9ea7bd22a5bbf00f294261f16fed7b31f05acc1c765da59b58c5d |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tax — Tax on the amount
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}, {"guard": {"args": [{"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, {"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Second transcription's note: The line 16 instructions that say which method to use are not in the supplied pages. I chose the split from the supplied pages themselves: the Tax Table runs in 'At least / But less than' bands, and the worksheet's first rows begin 'At least $100,000'. So the table applies when amount < $100,000 (ordinary.table_boundary) and the worksheet applies otherwise.

Ruling: representation within the selected worksheet domain; i1040gi (2025) Tax Table and Tax Computation Worksheet (SectionsA-D, first row At least$100,000) split ordinary tax at$100,000. Both returned branches use the Tax Table below the boundary and the same worksheet row rates/subtractions at or above it. The reply flattens filing-status and bracket guards into one choose, omits each first-row lower bound already guaranteed by the outer selector, and groups mfj/qss in SectionB. The project nests the status/bracket choices and keeps the redundant lower bound. No equivalence of standalone worksheet evaluation below$100,000 is claimed.

## Raw second transcription

```yaml
```yaml
lines:
  - id: table_tax
    printed: "(a) (table_tax)"
    label: "Tax Table: find the line for the amount (At least / But less than) and read down the column for your filing status (married filing jointly column also used by a qualifying surviving spouse). Your tax is—"
    type: NonNegDollars
    expr: {op: table_lookup, table: tax_table, key: amount, status: status}
    note: "The Tax Table covers amounts below $100,000 only. For larger amounts the lookup has no row, and line tax does not read this value."

  - id: tax_on_amount.h_single_r1_c
    printed: "(helper)"
    label: "Section A, row 'At least $100,000 but not over $103,350': (c) Multiply (a) by (b) [22% (0.22)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
  - id: tax_on_amount.h_single_r1_tax
    printed: "(helper)"
    label: "Section A, row 1: Subtract (d) $5,086.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r1_c, take: {param: tcw.single.b1.subtract}}
  - id: tax_on_amount.h_single_r2_c
    printed: "(helper)"
    label: "Section A, row 'Over $103,350 but not over $197,300': (c) Multiply (a) by (b) [24% (0.24)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
  - id: tax_on_amount.h_single_r2_tax
    printed: "(helper)"
    label: "Section A, row 2: Subtract (d) $7,153.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r2_c, take: {param: tcw.single.b2.subtract}}
  - id: tax_on_amount.h_single_r3_c
    printed: "(helper)"
    label: "Section A, row 'Over $197,300 but not over $250,525': (c) Multiply (a) by (b) [32% (0.32)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
  - id: tax_on_amount.h_single_r3_tax
    printed: "(helper)"
    label: "Section A, row 3: Subtract (d) $22,937.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r3_c, take: {param: tcw.single.b3.subtract}}
  - id: tax_on_amount.h_single_r4_c
    printed: "(helper)"
    label: "Section A, row 'Over $250,525 but not over $626,350': (c) Multiply (a) by (b) [35% (0.35)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
  - id: tax_on_amount.h_single_r4_tax
    printed: "(helper)"
    label: "Section A, row 4: Subtract (d) $30,452.75 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r4_c, take: {param: tcw.single.b4.subtract}}
  - id: tax_on_amount.h_single_r5_c
    printed: "(helper)"
    label: "Section A, row 'Over $626,350': (c) Multiply (a) by (b) [37% (0.37)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
  - id: tax_on_amount.h_single_r5_tax
    printed: "(helper)"
    label: "Section A, row 5: Subtract (d) $42,979.75 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_r5_c, take: {param: tcw.single.b5.subtract}}

  - id: tax_on_amount.h_mfj_r1_c
    printed: "(helper)"
    label: "Section B, row 'At least $100,000 but not over $206,700': (c) Multiply (a) by (b) [22% (0.22)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
  - id: tax_on_amount.h_mfj_r1_tax
    printed: "(helper)"
    label: "Section B, row 1: Subtract (d) $10,172.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r1_c, take: {param: tcw.mfj.b1.subtract}}
  - id: tax_on_amount.h_mfj_r2_c
    printed: "(helper)"
    label: "Section B, row 'Over $206,700 but not over $394,600': (c) Multiply (a) by (b) [24% (0.24)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
  - id: tax_on_amount.h_mfj_r2_tax
    printed: "(helper)"
    label: "Section B, row 2: Subtract (d) $14,306.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r2_c, take: {param: tcw.mfj.b2.subtract}}
  - id: tax_on_amount.h_mfj_r3_c
    printed: "(helper)"
    label: "Section B, row 'Over $394,600 but not over $501,050': (c) Multiply (a) by (b) [32% (0.32)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
  - id: tax_on_amount.h_mfj_r3_tax
    printed: "(helper)"
    label: "Section B, row 3: Subtract (d) $45,874.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r3_c, take: {param: tcw.mfj.b3.subtract}}
  - id: tax_on_amount.h_mfj_r4_c
    printed: "(helper)"
    label: "Section B, row 'Over $501,050 but not over $751,600': (c) Multiply (a) by (b) [35% (0.35)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
  - id: tax_on_amount.h_mfj_r4_tax
    printed: "(helper)"
    label: "Section B, row 4: Subtract (d) $60,905.50 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r4_c, take: {param: tcw.mfj.b4.subtract}}
  - id: tax_on_amount.h_mfj_r5_c
    printed: "(helper)"
    label: "Section B, row 'Over $751,600': (c) Multiply (a) by (b) [37% (0.37)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
  - id: tax_on_amount.h_mfj_r5_tax
    printed: "(helper)"
    label: "Section B, row 5: Subtract (d) $75,937.50 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_r5_c, take: {param: tcw.mfj.b5.subtract}}

  - id: tax_on_amount.h_mfs_r1_c
    printed: "(helper)"
    label: "Section C, row 'At least $100,000 but not over $103,350': (c) Multiply (a) by (b) [22% (0.22)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
  - id: tax_on_amount.h_mfs_r1_tax
    printed: "(helper)"
    label: "Section C, row 1: Subtract (d) $5,086.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r1_c, take: {param: tcw.mfs.b1.subtract}}
  - id: tax_on_amount.h_mfs_r2_c
    printed: "(helper)"
    label: "Section C, row 'Over $103,350 but not over $197,300': (c) Multiply (a) by (b) [24% (0.24)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
  - id: tax_on_amount.h_mfs_r2_tax
    printed: "(helper)"
    label: "Section C, row 2: Subtract (d) $7,153.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r2_c, take: {param: tcw.mfs.b2.subtract}}
  - id: tax_on_amount.h_mfs_r3_c
    printed: "(helper)"
    label: "Section C, row 'Over $197,300 but not over $250,525': (c) Multiply (a) by (b) [32% (0.32)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
  - id: tax_on_amount.h_mfs_r3_tax
    printed: "(helper)"
    label: "Section C, row 3: Subtract (d) $22,937.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r3_c, take: {param: tcw.mfs.b3.subtract}}
  - id: tax_on_amount.h_mfs_r4_c
    printed: "(helper)"
    label: "Section C, row 'Over $250,525 but not over $375,800': (c) Multiply (a) by (b) [35% (0.35)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
  - id: tax_on_amount.h_mfs_r4_tax
    printed: "(helper)"
    label: "Section C, row 4: Subtract (d) $30,452.75 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r4_c, take: {param: tcw.mfs.b4.subtract}}
  - id: tax_on_amount.h_mfs_r5_c
    printed: "(helper)"
    label: "Section C, row 'Over $375,800': (c) Multiply (a) by (b) [37% (0.37)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
  - id: tax_on_amount.h_mfs_r5_tax
    printed: "(helper)"
    label: "Section C, row 5: Subtract (d) $37,968.75 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_r5_c, take: {param: tcw.mfs.b5.subtract}}

  - id: tax_on_amount.h_hoh_r1_c
    printed: "(helper)"
    label: "Section D, row 'At least $100,000 but not over $103,350': (c) Multiply (a) by (b) [22% (0.22)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
  - id: tax_on_amount.h_hoh_r1_tax
    printed: "(helper)"
    label: "Section D, row 1: Subtract (d) $6,825.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r1_c, take: {param: tcw.hoh.b1.subtract}}
  - id: tax_on_amount.h_hoh_r2_c
    printed: "(helper)"
    label: "Section D, row 'Over $103,350 but not over $197,300': (c) Multiply (a) by (b) [24% (0.24)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
  - id: tax_on_amount.h_hoh_r2_tax
    printed: "(helper)"
    label: "Section D, row 2: Subtract (d) $8,892.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r2_c, take: {param: tcw.hoh.b2.subtract}}
  - id: tax_on_amount.h_hoh_r3_c
    printed: "(helper)"
    label: "Section D, row 'Over $197,300 but not over $250,500': (c) Multiply (a) by (b) [32% (0.32)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
  - id: tax_on_amount.h_hoh_r3_tax
    printed: "(helper)"
    label: "Section D, row 3: Subtract (d) $24,676.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r3_c, take: {param: tcw.hoh.b3.subtract}}
  - id: tax_on_amount.h_hoh_r4_c
    printed: "(helper)"
    label: "Section D, row 'Over $250,500 but not over $626,350': (c) Multiply (a) by (b) [35% (0.35)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
  - id: tax_on_amount.h_hoh_r4_tax
    printed: "(helper)"
    label: "Section D, row 4: Subtract (d) $32,191.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r4_c, take: {param: tcw.hoh.b4.subtract}}
  - id: tax_on_amount.h_hoh_r5_c
    printed: "(helper)"
    label: "Section D, row 'Over $626,350': (c) Multiply (a) by (b) [37% (0.37)]"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
  - id: tax_on_amount.h_hoh_r5_tax
    printed: "(helper)"
    label: "Section D, row 5: Subtract (d) $44,718.00 from (c)"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_r5_c, take: {param: tcw.hoh.b5.subtract}}

  - id: worksheet_tax
    printed: "(a) (worksheet_tax)"
    label: "2025 Tax Computation Worksheet: use the section for your filing status and complete the row that applies to the amount. Tax. Subtract (d) from (c)."
    type: Dollars
    note: "Each section's first row reads 'At least $100,000'. The worksheet applies only from $100,000, which line tax enforces, so the guard for row 1 tests only the upper bound. This keeps the guards exhaustive. Section B is used for both married filing jointly and qualifying surviving spouse."
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [status, {const: "single"}]}, {op: test, le: [amount, {param: tcw.single.b1.upper}]}]}
          then: tax_on_amount.h_single_r1_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "single"}]}, {op: test, gt: [amount, {param: tcw.single.b1.upper}]}, {op: test, le: [amount, {param: tcw.single.b2.upper}]}]}
          then: tax_on_amount.h_single_r2_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "single"}]}, {op: test, gt: [amount, {param: tcw.single.b2.upper}]}, {op: test, le: [amount, {param: tcw.single.b3.upper}]}]}
          then: tax_on_amount.h_single_r3_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "single"}]}, {op: test, gt: [amount, {param: tcw.single.b3.upper}]}, {op: test, le: [amount, {param: tcw.single.b4.upper}]}]}
          then: tax_on_amount.h_single_r4_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "single"}]}, {op: test, gt: [amount, {param: tcw.single.b4.upper}]}]}
          then: tax_on_amount.h_single_r5_tax
        - guard: {op: test, all: [{op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}, {op: test, le: [amount, {param: tcw.mfj.b1.upper}]}]}
          then: tax_on_amount.h_mfj_r1_tax
        - guard: {op: test, all: [{op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}, {op: test, gt: [amount, {param: tcw.mfj.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b2.upper}]}]}
          then: tax_on_amount.h_mfj_r2_tax
        - guard: {op: test, all: [{op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}, {op: test, gt: [amount, {param: tcw.mfj.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b3.upper}]}]}
          then: tax_on_amount.h_mfj_r3_tax
        - guard: {op: test, all: [{op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}, {op: test, gt: [amount, {param: tcw.mfj.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfj.b4.upper}]}]}
          then: tax_on_amount.h_mfj_r4_tax
        - guard: {op: test, all: [{op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}, {op: test, gt: [amount, {param: tcw.mfj.b4.upper}]}]}
          then: tax_on_amount.h_mfj_r5_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "mfs"}]}, {op: test, le: [amount, {param: tcw.mfs.b1.upper}]}]}
          then: tax_on_amount.h_mfs_r1_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "mfs"}]}, {op: test, gt: [amount, {param: tcw.mfs.b1.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b2.upper}]}]}
          then: tax_on_amount.h_mfs_r2_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "mfs"}]}, {op: test, gt: [amount, {param: tcw.mfs.b2.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b3.upper}]}]}
          then: tax_on_amount.h_mfs_r3_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "mfs"}]}, {op: test, gt: [amount, {param: tcw.mfs.b3.upper}]}, {op: test, le: [amount, {param: tcw.mfs.b4.upper}]}]}
          then: tax_on_amount.h_mfs_r4_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "mfs"}]}, {op: test, gt: [amount, {param: tcw.mfs.b4.upper}]}]}
          then: tax_on_amount.h_mfs_r5_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "hoh"}]}, {op: test, le: [amount, {param: tcw.hoh.b1.upper}]}]}
          then: tax_on_amount.h_hoh_r1_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "hoh"}]}, {op: test, gt: [amount, {param: tcw.hoh.b1.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b2.upper}]}]}
          then: tax_on_amount.h_hoh_r2_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "hoh"}]}, {op: test, gt: [amount, {param: tcw.hoh.b2.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b3.upper}]}]}
          then: tax_on_amount.h_hoh_r3_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "hoh"}]}, {op: test, gt: [amount, {param: tcw.hoh.b3.upper}]}, {op: test, le: [amount, {param: tcw.hoh.b4.upper}]}]}
          then: tax_on_amount.h_hoh_r4_tax
        - guard: {op: test, all: [{op: test, eq: [status, {const: "hoh"}]}, {op: test, gt: [amount, {param: tcw.hoh.b4.upper}]}]}
          then: tax_on_amount.h_hoh_r5_tax

  - id: tax
    printed: "(b)"
    label: "Tax on the amount: from the Tax Table if the amount is less than $100,000; otherwise from the Tax Computation Worksheet (enter the result on the appropriate line of the form or worksheet you are completing)"
    type: Dollars
    note: "The line 16 instructions that say which method to use are not in the supplied pages. I chose the split from the supplied pages themselves: the Tax Table runs in 'At least / But less than' bands, and the worksheet's first rows begin 'At least $100,000'. So the table applies when amount < $100,000 (ordinary.table_boundary) and the worksheet applies otherwise."
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
          then: table_tax
        - guard: {op: test, ge: [amount, {param: ordinary.table_boundary}]}
          then: worksheet_tax
```
```
