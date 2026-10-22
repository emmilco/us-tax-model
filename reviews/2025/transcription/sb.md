# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b46d252cd9632774dcecb4036cd854fe763e44d16578f59df233d4a4b4406636 |
| subject sha256 | 8cbf53cdc390adfc64adcee83de78308e2bfaf4ad1ed432d17ec6cdd93e463a5 |
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

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 2 | sb.unsupported | - |
| 3 | sb.unsupported | - |
| 4 | sb.fbar_required, sb.form8938, sb.line8, sb.unsupported | - |
| 6 | sb.fbar_required, sb.form8938, sb.line8, sb.unsupported | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Add the amounts on line 1"
    type: NonNegDollars
    expr: {op: sum_over, collection: interest, field: interest.amount}
    cite: "i1040sb (2025) p.1, Part I, Line 1: report all taxable interest; list each payer's name and the amount"
    refuses: [sb.unsupported]
    note: "The text has no instruction for line 2 itself. It is read as the total of the line 1 payer entries. The nominee, accrued interest, OID and bond premium subtractions that the text says go between line 1 and line 2 are not computed. sb.unsupported screens them out."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    cite: "i1040sb (2025) p.2, Line 3: savings-bond interest exclusion, see Form 8815"
    refuses: [sb.unsupported]
    note: "The task gives this line as 'Amount from sb.zero', but no line sb.zero is defined. It is written as the year parameter sales.zero (0) instead. The exclusion is computed only as zero. Filers with a savings-bond exclusion are screened out by sb.unsupported."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b"
    type: Dollars
    expr: {op: subtract, from: sb.line2, take: sb.line3}
    cite: "Schedule B (Form 1040) 2025, Part I, line 4"
    refuses: [sb.fbar_required, sb.form8938, sb.line8]
    note: "The Part III screens (FBAR, Form 8938, foreign trust) go here because this line feeds Form 1040 line 2b. The text says nothing about where these screens should apply, so that choice is mine."
  - id: sb.line6
    printed: "6"
    label: "Add the amounts on line 5. Enter the total here and on Form 1040 or 1040-SR, line 3b"
    type: NonNegDollars
    expr: {op: copy, from: sb.ordinary_dividends}
    cite: "i1040sb (2025) p.2, Line 5: report all ordinary dividends, shown in box 1a of Forms 1099-DIV"
    refuses: [sb.unsupported, sb.fbar_required, sb.form8938, sb.line8]
    note: "Line 6 is read as the total of Form 1099-DIV box 1a. The nominee subtraction and foreign corporation (Form 5471) reporting are not computed. sb.unsupported screens them out."
```
```
