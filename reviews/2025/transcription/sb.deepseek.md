# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 7b190705d62fcd547e52ae93ff6fe7e5af18e2aeb0dc63747df514e8416b7b11 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
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
| 4 | sb.unsupported | - |
| 6 | sb.unsupported | - |

## Raw second transcription

```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Taxable interest. If the total is over $1,500, you must complete Part III."
    type: NonNegDollars
    expr: {op: sum_over, collection: interest, field: interest.amount}
    cite: "i1040sb (TY2025) p.1"
    refuses: [sb.unsupported]
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815."
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    cite: "i1040sb (TY2025) p.2"
    note: "The closed input interface supplies no Form 8815 or savings-bond exclusion amount; within this slice line 3 is treated as zero."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2. Enter the result here and on Form 1040, line 2b."
    type: Dollars
    expr: {op: subtract, from: sb.line2, take: sb.line3}
    cite: "i1040sb (TY2025) p.2"
  - id: sb.line6
    printed: "6"
    label: "Total ordinary dividends. Enter here and on Form 1040, line 3b."
    type: NonNegDollars
    expr: {op: copy, from: sb.ordinary_dividends}
    cite: "i1040sb (TY2025) p.2"
    refuses: [sb.unsupported]
```
