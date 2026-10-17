# Render comparison — tax_on_amount

The rendered English of every printed line of `Tax on an amount — Tax Table or Tax Computation Worksheet` (`rendered/2025/tax_on_amount.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 40934e3dc4da7ab254c74404c93c57759961a8214aba870975559a7c75189678 |
| lines judged | 4 |
| match / mismatch / unclear / missing | 4 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### (a) (amount) — Amount to compute the tax on
Status: **MATCH**

Model: The worksheet Note says to 'enter the amount from that form or worksheet in column (a) of the row that applies to the amount you are looking up', so the amount comes from the calling line.

### (a) (table_tax) — Use the Tax Table
Status: **MATCH**

Model: The Tax Table is read by finding the 'At least / But less than' row for the amount and reading down the filing-status column ('The amount shown where the taxable income line and filing status column meet'). The rule that a qualifying surviving spouse uses the married filing jointly column ('This column must also be used by a qualifying surviving spouse') is assumed to be handled by the table lookup for the status.

### (a) (worksheet_tax) — Use the Tax Computation Worksheet
Status: **MATCH**

Model: The Tax Computation Worksheet picks a section by filing status (Sections A–D) and a row by the amount in column (a), then gives tax as '(a) by (b)' minus '(d)'. The Note allows it to be used 'to figure the tax on an amount from another form or worksheet', which is what this line does.

### (b) — Tax on the amount
Status: **MATCH**

Model: Every worksheet section starts at 'At least $100,000', so the worksheet covers amounts of $100,000 or more and the Tax Table covers amounts below that. The $100,000 split is consistent with this. The general rule on which method to use is in 'the instructions for line 16', which were not provided, so the split is inferred from where the worksheet rows begin.

## Raw response

```yaml
```yaml
lines:
  - key: "(a) (amount)"
    status: MATCH
    reason: "The worksheet Note says to 'enter the amount from that form or worksheet in column (a) of the row that applies to the amount you are looking up', so the amount comes from the calling line."
  - key: "(a) (table_tax)"
    status: MATCH
    reason: "The Tax Table is read by finding the 'At least / But less than' row for the amount and reading down the filing-status column ('The amount shown where the taxable income line and filing status column meet'). The rule that a qualifying surviving spouse uses the married filing jointly column ('This column must also be used by a qualifying surviving spouse') is assumed to be handled by the table lookup for the status."
  - key: "(a) (worksheet_tax)"
    status: MATCH
    reason: "The Tax Computation Worksheet picks a section by filing status (Sections A–D) and a row by the amount in column (a), then gives tax as '(a) by (b)' minus '(d)'. The Note allows it to be used 'to figure the tax on an amount from another form or worksheet', which is what this line does."
  - key: "(b)"
    status: MATCH
    reason: "Every worksheet section starts at 'At least $100,000', so the worksheet covers amounts of $100,000 or more and the Tax Table covers amounts below that. The $100,000 split is consistent with this. The general rule on which method to use is in 'the instructions for line 16', which were not provided, so the split is inferred from where the worksheet rows begin."
```
```
