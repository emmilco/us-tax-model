# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 510fdea1c490855126160954a386c2bbcdf41a38f66508675fe28b731b200315 |
| printed lines compared | 4 |
| agree / disagree / missing | 4 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 |

## Lines

### 2 — Total taxable interest from all payers
Status: **AGREE**

### 3 — Amount from sb.zero
Status: **AGREE**

### 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

### 6 — Amount from sb.ordinary_dividends
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: sb.zero
    printed: "(helper)"
    label: "Zero amount: no excludable savings bond interest (Form 8815 exclusion screened out by sb.unsupported)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Line 3 is specified as 'Amount from sb.zero', but sb.zero is not among the existing lines. The id sb.zero is used here, rather than the sb.h_<name> helper convention, so that line 3 resolves as specified. It is pinned to the year parameter sales.zero (0), as other forms' zero helpers are."
  - id: sb.line2
    printed: "2"
    label: "Total taxable interest from all payers"
    type: NonNegDollars
    expr: {op: sum_over, collection: interest, field: interest.amount}
    note: "The IRS text says to subtract nominee, accrued interest, OID adjustment and ABP adjustment amounts from the line 1 subtotal to get line 2. The input sb.unsupported screens out all of these cases. This line therefore takes line 2 as the plain total of line 1 payer amounts and does not encode any subtraction. A single atom cannot express the screen itself."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815"
    type: NonNegDollars
    expr: {op: copy, from: sb.zero}
    note: "The Form 8815 exclusion is out of scope; sb.unsupported covers the savings-bond exclusion. This line is therefore zero."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b"
    type: Dollars
    expr: {op: subtract, from: sb.line2, take: sb.line3}
    note: "The printed instruction is a plain subtraction with no -0- floor, so subtract is used rather than subtract_floor0. The type is signed Dollars for that reason, although with line 3 fixed at zero the result equals line 2 and is nonnegative."
  - id: sb.line6
    printed: "6"
    label: "Add the amounts on line 5. Enter the total here and on Form 1040 or 1040-SR, line 3b"
    type: NonNegDollars
    expr: {op: copy, from: sb.ordinary_dividends}
    note: "The IRS text says line 6 is the line 5 total of Form 1099-DIV box 1a amounts, less any nominee distribution. Nominee income is screened out by sb.unsupported, so line 6 copies the supplied total of ordinary dividends."
```
```
