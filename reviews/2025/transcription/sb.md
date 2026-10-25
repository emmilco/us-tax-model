# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bfedbf7e5675dda81cdb01d0bf165e212af6a645e8896e39ae75e55f2792680c |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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
| 3 | sb.unsupported | - |
| 4 | sb.unsupported | - |
| 6 | sb.unsupported | - |

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
    refuses: [sb.unsupported]
    note: "Line 1 lists each payer's taxable interest. Line 2 is that total. The instructions also cover subtracting nominee distributions, accrued interest, OID adjustments and ABP adjustments from the line 1 subtotal before line 2. The tool does not compute those, so they are refused through sb.unsupported. In the case the tool computes, line 2 is the total of the per-payer taxable interest."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989. Attach Form 8815"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
    refuses: [sb.unsupported]
    note: "Line 3 comes from Form 8815, which this tool does not prepare. A savings bond interest exclusion is refused through sb.unsupported. In the case the tool computes, there is no exclusion, so line 3 is zero. No zero parameter exists for Schedule B, so the zero comes from the money parameter ss.zero (value 0)."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b"
    type: Dollars
    expr:
      op: subtract
      from: sb.line2
      take: sb.line3
  - id: sb.line6
    printed: "6"
    label: "Add the amounts on line 5. Enter the total here and on Form 1040 or 1040-SR, line 3b"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    refuses: [sb.unsupported]
    note: "Line 5 lists ordinary dividends (Form 1099-DIV box 1a) by payer. Line 6 is that total. The only input for this is the supplied total sb.ordinary_dividends, so line 6 copies it. Subtracting nominee dividends before line 6 is not computed and is refused through sb.unsupported."
```
```
