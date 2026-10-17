# Render comparison — tax_on_amount

The rendered English of every printed line of `Tax on an amount — Tax Table or Tax Computation Worksheet` (`rendered/2025/tax_on_amount.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 6e7765b404165dc24fb2a677a1257d8debdcdcce3577ed4a5b8db13e463932f5 |
| lines judged | 4 |
| match / mismatch / unclear / missing | 4 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### (a) (amount) — Amount to compute the tax on
Status: **MATCH**

Model: The worksheet note says to 'enter the amount from that form or worksheet in column (a),' so the amount comes from the calling line. The restatement says the same.

### (a) (table_tax) — Use the Tax Table
Status: **MATCH**

Model: The Tax Table is read where 'the taxable income line and filing status column meet.' The restatement looks up the amount under the return's filing status. The page also says the married filing jointly column 'must also be used by a qualifying surviving spouse,' which the filing status column choice covers.

### (a) (worksheet_tax) — Use the Tax Computation Worksheet
Status: **MATCH**

Model: The Tax Computation Worksheet has one section per filing status (A–D). The tax is '(a) by (b)' minus '(d)' on the row that applies to the amount. The restatement runs the worksheet with that amount and filing status.

### (b) — Tax on the amount
Status: **MATCH**

Model: Every worksheet row starts 'At least $100,000,' which supports using the worksheet at or above $100,000 and the Tax Table below it. The governing line 16 instructions ('See the instructions for line 16 to see if you must use') are not in the pages given, but nothing provided contradicts the $100,000 cut.

## Raw response

```yaml
```yaml
lines:
  - key: "(a) (amount)"
    status: MATCH
    reason: "The worksheet note says to 'enter the amount from that form or worksheet in column (a),' so the amount comes from the calling line. The restatement says the same."
  - key: "(a) (table_tax)"
    status: MATCH
    reason: "The Tax Table is read where 'the taxable income line and filing status column meet.' The restatement looks up the amount under the return's filing status. The page also says the married filing jointly column 'must also be used by a qualifying surviving spouse,' which the filing status column choice covers."
  - key: "(a) (worksheet_tax)"
    status: MATCH
    reason: "The Tax Computation Worksheet has one section per filing status (A–D). The tax is '(a) by (b)' minus '(d)' on the row that applies to the amount. The restatement runs the worksheet with that amount and filing status."
  - key: "(b)"
    status: MATCH
    reason: "Every worksheet row starts 'At least $100,000,' which supports using the worksheet at or above $100,000 and the Tax Table below it. The governing line 16 instructions ('See the instructions for line 16 to see if you must use') are not in the pages given, but nothing provided contradicts the $100,000 cut."
```
```
