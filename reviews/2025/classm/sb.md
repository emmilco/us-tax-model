# Class M hand-work — sb

`Schedule B — supported interest and ordinary dividends` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-07 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 8a174ff282482b1eccc09eb06c33e36f14691fae2c7d40caa600ff32b0140081 |
| cases | 2 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

## Lines

### case classm.sb.1 — prompt sha256 4ae80a87b2256a609850278485be280d2d156162686cb083d3ed0e3ff4aff769; branches: sb.unsupported:false, sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.partIII:true, sb.form5471:false, sb.has_income:true, sb.no:false, sb.ordinary_dividends_if_dividends#0, sb.unsupported_if_income#0, sb.unsupported_if_income:false

### classm.sb.1 — 2 — Total taxable interest from all payers
Status: **AGREE**

Value: $0.00

### classm.sb.1 — 3 — Amount from sb.zero
Status: **AGREE**

Value: $0.00

### classm.sb.1 — 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

Value: $0.00

### classm.sb.1 — 6 — Amount from sb.ordinary_dividends_if_dividends
Status: **AGREE**

Value: $80,000.00

### case classm.sb.2 — prompt sha256 9c1b7ed405132fdc14b212af9edfba36822cc5b4e75d7ae33b3f812181531acc; branches: sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.form5471:false, sb.has_income:false, sb.no:false, sb.ordinary_dividends_if_dividends#1, sb.unsupported_if_income#1, sb.unsupported_if_income:false

### classm.sb.2 — 2 — Total taxable interest from all payers
Status: **AGREE**

Value: $0.00

### classm.sb.2 — 3 — Amount from sb.zero
Status: **AGREE**

Value: $0.00

### classm.sb.2 — 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

Value: $0.00

### classm.sb.2 — 6 — Amount from sb.ordinary_dividends_if_dividends
Status: **SKIPPED**

Model: blank
Work: Filer received no dividends in 2025, so Part II lines 5-6 are left blank

No numeric assertion or class M credit: the model left this line blank.

## Raw responses

### classm.sb.1

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "No taxable interest amounts given; line 1 total = 0.00"
  - printed: "3"
    value: "0.00"
    work: "No savings bond interest exclusion (no special treatment); Form 8815 amount = 0.00"
  - printed: "4"
    value: "0.00"
    work: "Line 2 0.00 - line 3 0.00 = 0.00"
  - printed: "6"
    value: "80000.00"
    work: "Line 5 ordinary dividends from Form 1099-DIV box 1a = 80,000.00; no nominee subtraction"
```
```

### classm.sb.2

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "Sum of taxable interest from all payers: bank_a $0.00 = $0.00"
  - printed: "3"
    value: "0.00"
    work: "No excludable series EE/I savings bond interest from Form 8815, so 0.00"
  - printed: "4"
    value: "0.00"
    work: "Line 2 minus line 3: 0.00 - 0.00 = 0.00"
  - printed: "6"
    value: "blank"
    work: "Filer received no dividends in 2025, so Part II lines 5-6 are left blank"
```
```
