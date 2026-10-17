# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4b49494d280802f76032388e33b3365213fe5e0ab017cac06c1bd727c3a67fde |
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
    label: "Total taxable interest from all payers"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: interest
      field: interest.amount
    note: "The instructions describe subtracting a 'Nominee Distribution', 'Accrued Interest', 'OID Adjustment' or 'ABP Adjustment' from the line 1 subtotal to get line 2. The input sb.unsupported screens all of these out, so line 2 is just the total of the line 1 payer amounts (interest.amount over the interest collection). No subtraction is encoded."
  - id: sb.zero
    printed: "(helper)"
    label: "Zero amount for the excluded savings bond interest (Form 8815 is not supported)"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
    note: "Line 3 refers to sb.zero, which is not among the existing inputs, so it is defined here. Its id is kept as sb.zero, not sb.h_zero, to match the line 3 wording. The Line 3 instructions allow excluding series EE or I savings bond interest through Form 8815. That exclusion is screened out by sb.unsupported, so the amount is the year parameter sales.zero (0)."
  - id: sb.line3
    printed: "3"
    label: "Amount from sb.zero"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.zero
  - id: sb.line4
    printed: "4"
    label: "Subtract sb.line3 from sb.line2"
    type: NonNegDollars
    expr:
      op: subtract
      from: sb.line2
      take: sb.line3
    note: "Signed subtraction, as printed. The type is NonNegDollars because line 3 is always zero here (sb.zero) and line 2 is never negative, so the result cannot be negative."
  - id: sb.line6
    printed: "6"
    label: "Amount from sb.ordinary_dividends"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    note: "The instructions describe subtracting a nominee distribution from the line 5 subtotal to get line 6. Nominee dividends are screened out by sb.unsupported, so line 6 equals the Form 1099-DIV box 1a total."
```
```
