# Transcription agreement — tax_on_amount

Second transcription of `Tax on an amount — Tax Table or Tax Computation Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/tax_on_amount.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 331697154a4dda68ffeba3f591bffa1eef33221da5312ebae0aacd1ca5cb88d1 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### tax — Tax on the amount
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfj.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfj.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.hoh.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.hoh.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.mfs.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.mfs.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.mfs.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.mfs.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.mfs.b5.subtract"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b1.upper"}], "test": "le"}, {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b1.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b1.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b2.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b2.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b2.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b3.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b3.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b3.subtract"}}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "tcw.single.b4.upper"}], "test": "le"}, {"args": [{"param": "tcw.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b4.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b4.subtract"}}}, {"guard": {"args": [{"param": "tcw.single.b4.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"from": {"amount": {"input": "amount"}, "op": "multiply_rate", "rate": {"param": "tcw.single.b5.rate"}}, "op": "subtract", "take": {"param": "tcw.single.b5.subtract"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"param": "ordinary.table_boundary"}, {"input": "amount"}], "test": "le"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"ref": "mfj.result"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"ref": "hoh.result"}}, {"guard": {"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, "then": {"ref": "mfs.result"}}, {"guard": {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}, "then": {"ref": "single.result"}}], "op": "choose"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ordinary.table_boundary"}], "test": "lt"}, "then": {"key": {"input": "amount"}, "op": "table_lookup", "status": {"input": "status"}, "table": "tax_table"}}], "op": "choose"}
```

Ruling: equivalent representation; project retained. Below $100,000 both use the Tax Table lookup; at or above it both enter the Tax Computation Worksheet, whose single remaining difference is the redundant lower bound on each section's first row recorded in the `tcw` log. The second transcription groups the joint and surviving-spouse statuses in one alternative where the project lists them separately with the same result; the comparison treats those as one case.

## Raw second transcription

```yaml
```yaml
lines:
  - id: tax_on_amount.line(a)
    printed: "(a)"
    label: "Use the Tax Table"
    type: Bool
    expr: {op: test, lt: [amount, {param: ordinary.table_boundary}]}
    note: "The instructions for line 16 that set when the Tax Table must be used are not in the supplied text. The supplied pages show that every Tax Computation Worksheet section begins 'At least $100,000'. So I read the Tax Table as applying when the amount is less than $100,000, using ordinary.table_boundary."
  - id: tax_on_amount.line(a)_tcw
    printed: "(a)"
    label: "Use the Tax Computation Worksheet"
    type: Bool
    expr: {op: test, ge: [amount, {param: ordinary.table_boundary}]}
    note: "This line has the same printed label '(a)' as the previous line, so the requested id 'tax_on_amount.line(a)' would appear twice. I added the suffix '_tcw' so the two ids are distinct. The threshold reading is the same as on the previous line: 'At least $100,000' is the start of every worksheet section."
  - id: tax_on_amount.h_table_tax
    printed: "(helper)"
    label: "Tax from the Tax Table, read where the taxable income line and filing status column meet"
    type: NonNegDollars
    expr: {op: table_lookup, table: tax_table, key: amount, status: status}
    note: "The Tax Table's married filing jointly column is marked '* This column must also be used by a qualifying surviving spouse.' The pinned tax_table lookup is assumed to map status 'qss' to that column."
  - id: tax_on_amount.h_is_single
    printed: "(helper)"
    label: "Section A—Use if your filing status is Single"
    type: Bool
    expr: {op: test, eq: [status, {const: "single"}]}
  - id: tax_on_amount.h_is_mfj
    printed: "(helper)"
    label: "Filing status is Married filing jointly"
    type: Bool
    expr: {op: test, eq: [status, {const: "mfj"}]}
  - id: tax_on_amount.h_is_qss
    printed: "(helper)"
    label: "Filing status is Qualifying surviving spouse"
    type: Bool
    expr: {op: test, eq: [status, {const: "qss"}]}
  - id: tax_on_amount.h_is_mfj_or_qss
    printed: "(helper)"
    label: "Section B—Use if your filing status is Married filing jointly or Qualifying surviving spouse"
    type: Bool
    expr: {op: test, any: [tax_on_amount.h_is_mfj, tax_on_amount.h_is_qss]}
  - id: tax_on_amount.h_is_mfs
    printed: "(helper)"
    label: "Section C—Use if your filing status is Married filing separately"
    type: Bool
    expr: {op: test, eq: [status, {const: "mfs"}]}
  - id: tax_on_amount.h_is_hoh
    printed: "(helper)"
    label: "Section D—Use if your filing status is Head of household"
    type: Bool
    expr: {op: test, eq: [status, {const: "hoh"}]}
  - id: tax_on_amount.h_tcw_tax
    printed: "(helper)"
    label: "Tax Computation Worksheet tax: Subtract (d) from (c), from the section for your filing status"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: tax_on_amount.h_is_single, then: single.result}
        - {guard: tax_on_amount.h_is_mfj_or_qss, then: mfj.result}
        - {guard: tax_on_amount.h_is_mfs, then: mfs.result}
        - {guard: tax_on_amount.h_is_hoh, then: hoh.result}
  - id: tax_on_amount.line(b)
    printed: "(b)"
    label: "Tax on the amount"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - {guard: tax_on_amount.line(a), then: tax_on_amount.h_table_tax}
        - {guard: tax_on_amount.line(a)_tcw, then: tax_on_amount.h_tcw_tax}
    note: "The Tax Computation Worksheet Note tells you to enter the amount from another form or worksheet in column (a) and to put the result on the line of the form being completed. So the bound 'amount' replaces line 15 in both the table and the worksheet."
  - id: tax
    printed: "(helper)"
    label: "Tax on the amount"
    type: Dollars
    expr: {op: copy, from: tax_on_amount.line(b)}
```
```
