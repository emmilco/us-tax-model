# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 85b5021b5ca4b22458931d5005b7fb09b38a868b6784828675d76241c7896e4c |
| printed lines compared | 4 |
| agree / disagree / missing | 4 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

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
  - id: sb.line2
    printed: "2"
    label: "Add the amounts on line 1"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: interest
      field: interest.amount
    note: "The text describes line 2 as the line 1 subtotal less any Nominee Distribution, Accrued Interest, OID Adjustment or ABP Adjustment. Those subtractions are screened out by sb.unsupported. Line 2 is therefore the total of interest.amount over all payer entries."
  - id: sb.h_zero
    printed: "(helper)"
    label: "Zero amount for the screened-out excludable savings bond interest"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    note: "The task label says 'Amount from sb.zero', but no line sb.zero is defined in the provided inputs. Helper ids must follow the sb.h_<name> pattern, so this helper takes the zero year parameter sales.zero, as the other forms do for their zero lines."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.h_zero
    note: "Form 8815 exclusion is out of scope; sb.unsupported screens out the savings-bond exclusion. Line 3 is therefore zero (task label: 'Amount from sb.zero', implemented as sb.h_zero)."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b"
    type: NonNegDollars
    expr:
      op: subtract
      from: sb.line2
      take: sb.line3
    note: "The text prints a plain subtraction with no zero floor, so subtract is used rather than subtract_floor0. The type is NonNegDollars because line 3 is zero in the supported scope."
  - id: sb.line6
    printed: "6"
    label: "Add the amounts on line 5. Enter the total here and on Form 1040 or 1040-SR, line 3b"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    note: "The text describes line 6 as the line 5 subtotal less any Nominee Distribution. Nominee dividends are screened out by sb.unsupported, so line 6 is the total of Form 1099-DIV box 1a ordinary dividends (task label: 'Amount from sb.ordinary_dividends')."
```
```
