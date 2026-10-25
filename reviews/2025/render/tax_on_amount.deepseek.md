# Render comparison — tax_on_amount

The rendered English of every printed line of `Tax on an amount — Tax Table or Tax Computation Worksheet` (`rendered/2025/tax_on_amount.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a0a507606e5fd2805129ffcaf581dedd6b8e2e3478ef1cafdc23118b2e243081 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
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

Model: The IRS worksheet column (a) directs entering the amount from line 15, or from the calling form or worksheet under the Note, so this input restatement matches.

### (a) (table_tax) — Use the Tax Table
Status: **MATCH**

Model: The Tax Table is read using the taxable-income amount and the filing-status column, with the qualifying surviving spouse footnote routing to the married filing jointly column.

### (a) (worksheet_tax) — Use the Tax Computation Worksheet
Status: **MATCH**

Model: The Tax Computation Worksheet sections for filing status compute the line 16 tax using the amount, rates, thresholds, and subtraction amounts reproduced in the glossary.

### (b) — Tax on the amount
Status: **MATCH**

Model: The worksheet applies at $100,000 and above, so using the Tax Table below $100,000 and the worksheet otherwise is consistent with the provided IRS text.

## Raw response

```yaml
lines:
  - key: "(a) (amount)"
    status: MATCH
    reason: "The IRS worksheet column (a) directs entering the amount from line 15, or from the calling form or worksheet under the Note, so this input restatement matches."
  - key: "(a) (table_tax)"
    status: MATCH
    reason: "The Tax Table is read using the taxable-income amount and the filing-status column, with the qualifying surviving spouse footnote routing to the married filing jointly column."
  - key: "(a) (worksheet_tax)"
    status: MATCH
    reason: "The Tax Computation Worksheet sections for filing status compute the line 16 tax using the amount, rates, thresholds, and subtraction amounts reproduced in the glossary."
  - key: "(b)"
    status: MATCH
    reason: "The worksheet applies at $100,000 and above, so using the Tax Table below $100,000 and the worksheet otherwise is consistent with the provided IRS text."
```
