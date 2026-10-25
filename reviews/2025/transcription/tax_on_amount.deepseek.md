# Transcription agreement — tax_on_amount

Second transcription of `Tax on an amount — Tax Table or Tax Computation Worksheet` by an isolated model (spec 6.5), compared line by line with `forms/2025/tax_on_amount.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | bf1d9ae396c5d7769611eef4a1a2c4dca20dcf93c2a99b833dabcc6fa2083006 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d0c69f842ce9ea7bd22a5bbf00f294261f16fed7b31f05acc1c765da59b58c5d |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### tax — Tax on the amount
Status: **AGREE**

## Raw second transcription

```yaml
lines:
  - id: table_tax
    printed: "(a) (table_tax)"
    label: "Tax from the Tax Table"
    type: NonNegDollars
    expr: {op: table_lookup, table: tax_table, key: amount, status: status}
    cite: "i1040gi (2025) p. 68, Tax Table"
  - id: worksheet_tax
    printed: "(a) (worksheet_tax)"
    label: "Tax from the Tax Computation Worksheet—Line 16"
    type: Dollars
    expr: {op: copy, from: {def: tcw, bind: {amount: amount, status: status}, line: tax}}
    cite: "i1040gi (2025) p. 80, Tax Computation Worksheet—Line 16"
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
    cite: "i1040gi (2025) p. 68 (Tax Table) and p. 80 (Tax Computation Worksheet), line 16 instructions"
    note: "The IRS text uses the Tax Table when taxable income is less than $100,000 and the Tax Computation Worksheet when it is $100,000 or more; ordinary.table_boundary is $100,000."
```
