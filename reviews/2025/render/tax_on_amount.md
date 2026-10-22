# Render comparison — tax_on_amount

The rendered English of every printed line of `Tax on an amount — Tax Table or Tax Computation Worksheet` (`rendered/2025/tax_on_amount.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 40934e3dc4da7ab254c74404c93c57759961a8214aba870975559a7c75189678 |
| subject sha256 | 22ccea2eddd72070bd9860d3ec62e1a63646409d38403d413ae8082c6f637752 |
| lines judged | 4 |
| match / mismatch / unclear / missing | 4 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (a) (amount) — Amount to compute the tax on
Status: **MATCH**

Model: The Note on the Tax Computation Worksheet says to 'enter the amount from that form or worksheet in column (a)' when figuring tax on an amount from another form or worksheet. That matches an input supplied by the calling line.

### (a) (table_tax) — Use the Tax Table
Status: **MATCH**

Model: The Tax Table says to 'find the ... taxable income line', then 'find the column for' the filing status and read where they meet. That matches a lookup by amount and filing status. The table marks the married filing jointly column with '* This column must also be used by a qualifying surviving spouse'; the restatement leaves this to the filing-status lookup.

### (a) (worksheet_tax) — Use the Tax Computation Worksheet
Status: **MATCH**

Model: The worksheet Note says to 'enter the amount from that form or worksheet in column (a) of the row that applies' and 'Enter the result on the appropriate line of the form or worksheet that you are completing'. Each Section is chosen by filing status, which matches computing the worksheet tax with this amount and status.

### (b) — Tax on the amount
Status: **MATCH**

Model: Every Section of the Tax Computation Worksheet starts at 'At least $100,000', so amounts below $100,000 use the Tax Table and amounts of $100,000 or more use the worksheet. That matches the strict less-than-$100,000 test. The line 16 instructions mentioned in the CAUTION notes are not in the text provided, but the worksheet rows set the same boundary.

## Raw response

```yaml
```yaml
lines:
  - key: "(a) (amount)"
    status: MATCH
    reason: "The Note on the Tax Computation Worksheet says to 'enter the amount from that form or worksheet in column (a)' when figuring tax on an amount from another form or worksheet. That matches an input supplied by the calling line."
  - key: "(a) (table_tax)"
    status: MATCH
    reason: "The Tax Table says to 'find the ... taxable income line', then 'find the column for' the filing status and read where they meet. That matches a lookup by amount and filing status. The table marks the married filing jointly column with '* This column must also be used by a qualifying surviving spouse'; the restatement leaves this to the filing-status lookup."
  - key: "(a) (worksheet_tax)"
    status: MATCH
    reason: "The worksheet Note says to 'enter the amount from that form or worksheet in column (a) of the row that applies' and 'Enter the result on the appropriate line of the form or worksheet that you are completing'. Each Section is chosen by filing status, which matches computing the worksheet tax with this amount and status."
  - key: "(b)"
    status: MATCH
    reason: "Every Section of the Tax Computation Worksheet starts at 'At least $100,000', so amounts below $100,000 use the Tax Table and amounts of $100,000 or more use the worksheet. That matches the strict less-than-$100,000 test. The line 16 instructions mentioned in the CAUTION notes are not in the text provided, but the worksheet rows set the same boundary."
```
```
