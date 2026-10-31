# Transcription agreement — sb

Second transcription of `Schedule B — supported interest and ordinary dividends` by an isolated model (spec 6.5), compared line by line with `forms/2025/sb.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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
| 2 | sb.fbar_required, sb.form8938, sb.line8, sb.unsupported | - |
| 3 | sb.unsupported | - |
| 4 | sb.fbar_required, sb.form8938, sb.line8, sb.unsupported | - |
| 6 | sb.fbar_required, sb.form8938, sb.line8, sb.unsupported | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sb.line2
    printed: "2"
    label: "Total of all taxable interest listed on line 1 (subtotal of line 1, less any amount subtracted under the Nominee, Accrued Interest, OID Adjustment or ABP Adjustment rules)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: interest
      field: interest.amount
    refuses: [sb.unsupported, sb.fbar_required, sb.form8938, sb.line8]
    note: "Subtractions from the line 1 subtotal (nominee, accrued interest, OID adjustment, ABP adjustment) and the other special cases are outside the tool and refused by sb.unsupported, so line 2 is the plain total of the payer amounts. The supplied text does not say where to enforce the Part III screens (FBAR, Form 8938, foreign trust), and Part III has no requested money line. I chose to list them on lines 2 and 6, the two Schedule B lines fed directly by inputs. sb.line7a is not used in a refusal because the instructions make a Yes to Question 1 reportable even if FinCEN Form 114 is not required."
  - id: sb.line3
    printed: "3"
    label: "Excludable interest on series EE and I U.S. savings bonds issued after 1989 (Form 8815)"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
    refuses: [sb.unsupported]
    note: "The savings bond interest exclusion (Form 8815) is refused by sb.unsupported, so the only case the tool computes has no exclusion and the line is zero. The catalog has no zero parameter specific to Schedule B, so I used the zero-valued money parameter ss.zero."
  - id: sb.line4
    printed: "4"
    label: "Subtract line 3 from line 2"
    type: Dollars
    expr:
      op: subtract
      from: sb.line2
      take: sb.line3
    note: "The supplied instructions have no entry for line 4 and do not include the face of the form. I read it as line 2 minus line 3, because line 3 is described as an exclusion from the interest totalled on line 2. The label is my wording, not quoted IRS text."
  - id: sb.line6
    printed: "6"
    label: "Total of all ordinary dividends listed on line 5 (subtotal of line 5, less any nominee distribution)"
    type: NonNegDollars
    expr:
      op: copy
      from: sb.ordinary_dividends
    refuses: [sb.unsupported, sb.fbar_required, sb.form8938, sb.line8]
    note: "Line 5 reports the ordinary dividends shown in box 1a of Forms 1099-DIV. The interface supplies that total as sb.ordinary_dividends, and the nominee subtraction is refused by sb.unsupported, so line 6 equals that total. The Part III screens are repeated here so that a return with dividends but no interest entries still stops on them."
```
```
