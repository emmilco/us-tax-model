# Transcription agreement — tax_on_amount

Second transcription of `Tax on an amount — Tax Table or Tax Computation Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/tax_on_amount.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f9c8150e3cb8c95449276817c1b3a38957c47602e26fa8729160053a5d99f553 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
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
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Second transcription's note: The Tax Table is used below ordinary.table_boundary ($100,000) and the Tax Computation Worksheet at or above that boundary.

Ruling: representation; i1040gi (2025) Tax Table and Tax Computation Worksheet SectionsA-D use the$100,000 split. The returned tax selector makes that same split and uses the same filing-status row rates/subtractions above it. Its status-specific worksheet helpers also return Tax Table amounts below$100,000, but those extra helper branches are never selected by tax in that range; the outer tax selector already uses the Tax Table. All admitted final tax results therefore use the same source computations. No identical standalone behavior is claimed for unselected worksheet helpers.

## Raw second transcription

```yaml
lines:
  - id: table_tax
    printed: "(a) (table_tax)"
    label: "Tax from the Tax Table"
    type: NonNegDollars
    expr: {op: table_lookup, table: tax_table, key: amount, status: status}
  - id: worksheet_tax
    printed: "(a) (worksheet_tax)"
    label: "Tax from the Tax Computation Worksheet"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [status, {const: "single"}]}
          then: tax_on_amount.h_single_ws
        - guard: {op: test, eq: [status, {const: "mfj"}]}
          then: tax_on_amount.h_mfj_ws
        - guard: {op: test, eq: [status, {const: "mfs"}]}
          then: tax_on_amount.h_mfs_ws
        - guard: {op: test, eq: [status, {const: "hoh"}]}
          then: tax_on_amount.h_hoh_ws
        - guard: {op: test, eq: [status, {const: "qss"}]}
          then: tax_on_amount.h_mfj_ws
    note: "The Tax Computation Worksheet applies only when the amount is $100,000 or more. Below that boundary each status helper returns the Tax Table amount so this line is total, although the top-level tax line selects the Tax Table directly there."
  - id: tax
    printed: "(b)"
    label: "Tax"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
          then: table_tax
        - guard: {op: test, ge: [amount, {param: ordinary.table_boundary}]}
          then: worksheet_tax
    note: "The Tax Table is used below ordinary.table_boundary ($100,000) and the Tax Computation Worksheet at or above that boundary."

  - id: tax_on_amount.h_single_b1_product
    printed: "(helper)"
    label: "Single row 1: amount multiplied by 22%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b1.rate}}
  - id: tax_on_amount.h_single_b1_tax
    printed: "(helper)"
    label: "Single row 1: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_b1_product, take: {param: tcw.single.b1.subtract}}
  - id: tax_on_amount.h_single_b2_product
    printed: "(helper)"
    label: "Single row 2: amount multiplied by 24%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b2.rate}}
  - id: tax_on_amount.h_single_b2_tax
    printed: "(helper)"
    label: "Single row 2: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_b2_product, take: {param: tcw.single.b2.subtract}}
  - id: tax_on_amount.h_single_b3_product
    printed: "(helper)"
    label: "Single row 3: amount multiplied by 32%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b3.rate}}
  - id: tax_on_amount.h_single_b3_tax
    printed: "(helper)"
    label: "Single row 3: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_b3_product, take: {param: tcw.single.b3.subtract}}
  - id: tax_on_amount.h_single_b4_product
    printed: "(helper)"
    label: "Single row 4: amount multiplied by 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b4.rate}}
  - id: tax_on_amount.h_single_b4_tax
    printed: "(helper)"
    label: "Single row 4: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_b4_product, take: {param: tcw.single.b4.subtract}}
  - id: tax_on_amount.h_single_b5_product
    printed: "(helper)"
    label: "Single row 5: amount multiplied by 37%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.single.b5.rate}}
  - id: tax_on_amount.h_single_b5_tax
    printed: "(helper)"
    label: "Single row 5: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_single_b5_product, take: {param: tcw.single.b5.subtract}}

  - id: tax_on_amount.h_mfj_b1_product
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 1: amount multiplied by 22%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b1.rate}}
  - id: tax_on_amount.h_mfj_b1_tax
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 1: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_b1_product, take: {param: tcw.mfj.b1.subtract}}
  - id: tax_on_amount.h_mfj_b2_product
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 2: amount multiplied by 24%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b2.rate}}
  - id: tax_on_amount.h_mfj_b2_tax
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 2: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_b2_product, take: {param: tcw.mfj.b2.subtract}}
  - id: tax_on_amount.h_mfj_b3_product
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 3: amount multiplied by 32%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b3.rate}}
  - id: tax_on_amount.h_mfj_b3_tax
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 3: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_b3_product, take: {param: tcw.mfj.b3.subtract}}
  - id: tax_on_amount.h_mfj_b4_product
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 4: amount multiplied by 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b4.rate}}
  - id: tax_on_amount.h_mfj_b4_tax
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 4: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_b4_product, take: {param: tcw.mfj.b4.subtract}}
  - id: tax_on_amount.h_mfj_b5_product
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 5: amount multiplied by 37%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfj.b5.rate}}
  - id: tax_on_amount.h_mfj_b5_tax
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse row 5: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfj_b5_product, take: {param: tcw.mfj.b5.subtract}}

  - id: tax_on_amount.h_mfs_b1_product
    printed: "(helper)"
    label: "Married filing separately row 1: amount multiplied by 22%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b1.rate}}
  - id: tax_on_amount.h_mfs_b1_tax
    printed: "(helper)"
    label: "Married filing separately row 1: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_b1_product, take: {param: tcw.mfs.b1.subtract}}
  - id: tax_on_amount.h_mfs_b2_product
    printed: "(helper)"
    label: "Married filing separately row 2: amount multiplied by 24%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b2.rate}}
  - id: tax_on_amount.h_mfs_b2_tax
    printed: "(helper)"
    label: "Married filing separately row 2: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_b2_product, take: {param: tcw.mfs.b2.subtract}}
  - id: tax_on_amount.h_mfs_b3_product
    printed: "(helper)"
    label: "Married filing separately row 3: amount multiplied by 32%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b3.rate}}
  - id: tax_on_amount.h_mfs_b3_tax
    printed: "(helper)"
    label: "Married filing separately row 3: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_b3_product, take: {param: tcw.mfs.b3.subtract}}
  - id: tax_on_amount.h_mfs_b4_product
    printed: "(helper)"
    label: "Married filing separately row 4: amount multiplied by 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b4.rate}}
  - id: tax_on_amount.h_mfs_b4_tax
    printed: "(helper)"
    label: "Married filing separately row 4: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_b4_product, take: {param: tcw.mfs.b4.subtract}}
  - id: tax_on_amount.h_mfs_b5_product
    printed: "(helper)"
    label: "Married filing separately row 5: amount multiplied by 37%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.mfs.b5.rate}}
  - id: tax_on_amount.h_mfs_b5_tax
    printed: "(helper)"
    label: "Married filing separately row 5: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_mfs_b5_product, take: {param: tcw.mfs.b5.subtract}}

  - id: tax_on_amount.h_hoh_b1_product
    printed: "(helper)"
    label: "Head of household row 1: amount multiplied by 22%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b1.rate}}
  - id: tax_on_amount.h_hoh_b1_tax
    printed: "(helper)"
    label: "Head of household row 1: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_b1_product, take: {param: tcw.hoh.b1.subtract}}
  - id: tax_on_amount.h_hoh_b2_product
    printed: "(helper)"
    label: "Head of household row 2: amount multiplied by 24%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b2.rate}}
  - id: tax_on_amount.h_hoh_b2_tax
    printed: "(helper)"
    label: "Head of household row 2: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_b2_product, take: {param: tcw.hoh.b2.subtract}}
  - id: tax_on_amount.h_hoh_b3_product
    printed: "(helper)"
    label: "Head of household row 3: amount multiplied by 32%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b3.rate}}
  - id: tax_on_amount.h_hoh_b3_tax
    printed: "(helper)"
    label: "Head of household row 3: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_b3_product, take: {param: tcw.hoh.b3.subtract}}
  - id: tax_on_amount.h_hoh_b4_product
    printed: "(helper)"
    label: "Head of household row 4: amount multiplied by 35%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b4.rate}}
  - id: tax_on_amount.h_hoh_b4_tax
    printed: "(helper)"
    label: "Head of household row 4: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_b4_product, take: {param: tcw.hoh.b4.subtract}}
  - id: tax_on_amount.h_hoh_b5_product
    printed: "(helper)"
    label: "Head of household row 5: amount multiplied by 37%"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: amount, rate: {param: tcw.hoh.b5.rate}}
  - id: tax_on_amount.h_hoh_b5_tax
    printed: "(helper)"
    label: "Head of household row 5: product less subtraction amount"
    type: Dollars
    expr: {op: subtract, from: tax_on_amount.h_hoh_b5_product, take: {param: tcw.hoh.b5.subtract}}

  - id: tax_on_amount.h_single_ws
    printed: "(helper)"
    label: "Tax Computation Worksheet Section A: Single"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
          then: table_tax
        - guard:
            op: test
            all:
              - {op: test, ge: [amount, {param: ordinary.table_boundary}]}
              - {op: test, le: [amount, {param: tcw.single.b1.upper}]}
          then: tax_on_amount.h_single_b1_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.single.b1.upper}]}
              - {op: test, le: [amount, {param: tcw.single.b2.upper}]}
          then: tax_on_amount.h_single_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.single.b2.upper}]}
              - {op: test, le: [amount, {param: tcw.single.b3.upper}]}
          then: tax_on_amount.h_single_b3_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.single.b3.upper}]}
              - {op: test, le: [amount, {param: tcw.single.b4.upper}]}
          then: tax_on_amount.h_single_b4_tax
        - guard:
            op: test
            gt: [amount, {param: tcw.single.b4.upper}]
          then: tax_on_amount.h_single_b5_tax
  - id: tax_on_amount.h_mfj_ws
    printed: "(helper)"
    label: "Tax Computation Worksheet Section B: Married filing jointly or qualifying surviving spouse"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
          then: table_tax
        - guard:
            op: test
            all:
              - {op: test, ge: [amount, {param: ordinary.table_boundary}]}
              - {op: test, le: [amount, {param: tcw.mfj.b1.upper}]}
          then: tax_on_amount.h_mfj_b1_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.mfj.b1.upper}]}
              - {op: test, le: [amount, {param: tcw.mfj.b2.upper}]}
          then: tax_on_amount.h_mfj_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.mfj.b2.upper}]}
              - {op: test, le: [amount, {param: tcw.mfj.b3.upper}]}
          then: tax_on_amount.h_mfj_b3_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.mfj.b3.upper}]}
              - {op: test, le: [amount, {param: tcw.mfj.b4.upper}]}
          then: tax_on_amount.h_mfj_b4_tax
        - guard:
            op: test
            gt: [amount, {param: tcw.mfj.b4.upper}]
          then: tax_on_amount.h_mfj_b5_tax
  - id: tax_on_amount.h_mfs_ws
    printed: "(helper)"
    label: "Tax Computation Worksheet Section C: Married filing separately"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
          then: table_tax
        - guard:
            op: test
            all:
              - {op: test, ge: [amount, {param: ordinary.table_boundary}]}
              - {op: test, le: [amount, {param: tcw.mfs.b1.upper}]}
          then: tax_on_amount.h_mfs_b1_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.mfs.b1.upper}]}
              - {op: test, le: [amount, {param: tcw.mfs.b2.upper}]}
          then: tax_on_amount.h_mfs_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.mfs.b2.upper}]}
              - {op: test, le: [amount, {param: tcw.mfs.b3.upper}]}
          then: tax_on_amount.h_mfs_b3_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.mfs.b3.upper}]}
              - {op: test, le: [amount, {param: tcw.mfs.b4.upper}]}
          then: tax_on_amount.h_mfs_b4_tax
        - guard:
            op: test
            gt: [amount, {param: tcw.mfs.b4.upper}]
          then: tax_on_amount.h_mfs_b5_tax
  - id: tax_on_amount.h_hoh_ws
    printed: "(helper)"
    label: "Tax Computation Worksheet Section D: Head of household"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
          then: table_tax
        - guard:
            op: test
            all:
              - {op: test, ge: [amount, {param: ordinary.table_boundary}]}
              - {op: test, le: [amount, {param: tcw.hoh.b1.upper}]}
          then: tax_on_amount.h_hoh_b1_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.hoh.b1.upper}]}
              - {op: test, le: [amount, {param: tcw.hoh.b2.upper}]}
          then: tax_on_amount.h_hoh_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.hoh.b2.upper}]}
              - {op: test, le: [amount, {param: tcw.hoh.b3.upper}]}
          then: tax_on_amount.h_hoh_b3_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: tcw.hoh.b3.upper}]}
              - {op: test, le: [amount, {param: tcw.hoh.b4.upper}]}
          then: tax_on_amount.h_hoh_b4_tax
        - guard:
            op: test
            gt: [amount, {param: tcw.hoh.b4.upper}]
          then: tax_on_amount.h_hoh_b5_tax
```
