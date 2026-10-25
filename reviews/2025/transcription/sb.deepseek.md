# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | bfedbf7e5675dda81cdb01d0bf165e212af6a645e8896e39ae75e55f2792680c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 8cbf53cdc390adfc64adcee83de78308e2bfaf4ad1ed432d17ec6cdd93e463a5 |
| printed lines compared | 4 |
| agree / disagree / missing | 3 / 1 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"from": {"line": "2"}, "op": "subtract", "take": {"line": "3"}}
```

Second:

```json
{"from": {"line": "2"}, "op": "subtract_floor0", "take": {"line": "3"}}
```

Ruling: representation; f1040sb (2025) p.1 line4 says to subtract line3 from line2. Within the admitted scope, savings-bond exclusion is refused and line3 is the zero-dollar parameter; line2 sums NonNegDollars interest entries. The returned subtract_floor0 therefore never binds, and equals the project subtraction on all admitted values. Both preserve the required Dollars result type. This does not admit the excluded bond-exclusion regime.

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

## Raw second transcription

```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Taxable interest. Add the amounts on line 1."
    type: NonNegDollars
    expr: {op: sum_over, collection: interest, field: interest.amount}
    refuses: [sb.unsupported]
  - id: sb.line3
    printed: "3"
    label: "Exclusion of interest from series EE and I U.S. savings bonds issued after 1989. Attach Form 8815."
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    refuses: [sb.unsupported]
  - id: sb.line4
    printed: "4"
    label: "Interest. Subtract line 3 from line 2. If line 3 is more than line 2, enter -0-."
    type: Dollars
    expr: {op: subtract_floor0, from: sb.line2, take: sb.line3}
  - id: sb.line6
    printed: "6"
    label: "Ordinary dividends. Add the amounts on line 5."
    type: NonNegDollars
    expr: {op: copy, from: sb.ordinary_dividends}
    refuses: [sb.unsupported]
```
