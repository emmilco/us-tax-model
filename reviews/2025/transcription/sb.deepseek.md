# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d2c505cbc097fbee4ffcf21b5afec5ff0babcc0050a4d00257e10075cc7824c9 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | a4ce3487d66ecb85d66e609fa07731ce64dbd9dd38ddc8074e69f61161ceeadc |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | ffe5a4e74bb1183dfab3be1ef94ed1938c33867886cfb8518e6775439cb6f86b |
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
| 4 | sb.unsupported | - |
| 6 | sb.unsupported | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 2 | c50077315e01753f305aeb2faefdec8cf47b1b1b5c07cec069ab870b435db8cc |
| 3 | adc59757e6a1b9b5432546a2629e52eb2085417f19b75ae843e9098856165263 |
| 4 | d225f28e9701cf230747bff686459225d04bd398ce08e2040a616fb8958167c4 |
| 6 | 592f2cf2def1924c2c4599e2709a3a18aa5910d0457f75ea5f71c12ba4bc7469 |
| (rest of the document) | 013e58d3d274e971cd170d48794200b98ac690d600b9af1e38e8133de7ae11db |

## Raw second transcription

```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Taxable interest. Add the amounts on line 1. Enter the total here and on Form 1040 or 1040-SR, line 2b."
    type: NonNegDollars
    expr:
      op: sum_over
      collection: interest
      field: interest.amount
    refuses: [sb.unsupported]
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815."
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
    refuses: [sb.unsupported]
    note: "The tool computes zero when no savings bond interest exclusion applies; the exclusion itself is outside this slice and is refused through sb.unsupported."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b."
    type: Dollars
    expr:
      op: subtract
      from: sb.line2
      take: sb.line3
  - id: sb.line6
    printed: "6"
    label: "Ordinary dividends. Add the amounts on line 5. Enter the total here and on Form 1040 or 1040-SR, line 3b."
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    refuses: [sb.unsupported]
```
