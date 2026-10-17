# Class M hand-work — sb

`Schedule B — supported interest and ordinary dividends` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

## Lines

### case classm.sb.1 — prompt sha256 72cb9b094e80f6e97ac3252671405b0cfb3b8a1788f0c97bb3b1950045421f9a; branches: sb.unsupported:false, sb.line7a:false, sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.partIII:true

### classm.sb.1 — 2 — Total taxable interest from all payers
Status: **AGREE**

Value: $0.00

### classm.sb.1 — 3 — Amount from sb.zero
Status: **AGREE**

Value: $0.00

### classm.sb.1 — 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

Value: $0.00

### classm.sb.1 — 6 — Amount from sb.ordinary_dividends
Status: **AGREE**

Value: $128,064.00

### case classm.sb.2 — prompt sha256 d1fe6675f34ae8a58af6f273055d7a04f7514350b8af353736ca2024b48b7adf; branches: sb.unsupported:false, sb.line7a:false, sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.partIII:false

### classm.sb.2 — 2 — Total taxable interest from all payers
Status: **AGREE**

Value: $0.00

### classm.sb.2 — 3 — Amount from sb.zero
Status: **AGREE**

Value: $0.00

### classm.sb.2 — 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

Value: $0.00

### classm.sb.2 — 6 — Amount from sb.ordinary_dividends
Status: **AGREE**

Value: $0.00

### case classm.sb.3 — prompt sha256 568dd0f75113373f18f8900fb1ba56183610af099e1d931bd9cb3190cdd65c90; branches: sb.unsupported:false, sb.line7a:true, sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.partIII:true

### classm.sb.3 — 2 — Total taxable interest from all payers
Status: **AGREE**

Value: $0.00

### classm.sb.3 — 3 — Amount from sb.zero
Status: **AGREE**

Value: $0.00

### classm.sb.3 — 4 — Subtract sb.line3 from sb.line2
Status: **AGREE**

Value: $0.00

### classm.sb.3 — 6 — Amount from sb.ordinary_dividends
Status: **AGREE**

Value: $42,005.00

## Raw responses

### classm.sb.1

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "No interest payers given and no nominee/OID/accrued/ABP subtraction; line 1 total = 0.00"
  - printed: "3"
    value: "0.00"
    work: "No savings-bond exclusion (Form 8815) claimed; amount from sb.zero = 0.00"
  - printed: "4"
    value: "0.00"
    work: "Line 2 0.00 - line 3 0.00 = 0.00"
  - printed: "6"
    value: "128064.00"
    work: "Form 1099-DIV box 1a 128,064.00; no nominee distribution; line 5 total = line 6"
```
```

### classm.sb.2

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "No interest payers or amounts given; no nominee or other subtractions, so line 2 = line 1 total = 0.00"
  - printed: "3"
    value: "0.00"
    work: "Amount from sb.zero = 0.00; no savings-bond exclusion (Form 8815)"
  - printed: "4"
    value: "0.00"
    work: "Line 2 0.00 - line 3 0.00 = 0.00"
  - printed: "6"
    value: "0.00"
    work: "Ordinary dividends, Form 1099-DIV box 1a = 0.00; no nominee subtraction"
```
```

### classm.sb.3

```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "No taxable interest from any payer was given, and there was no nominee or other adjustment, so line 2 = line 1 total = 0.00"
  - printed: "3"
    value: "0.00"
    work: "No savings-bond exclusion (Form 8815) applies, so line 3 = 0.00"
  - printed: "4"
    value: "0.00"
    work: "Line 2 minus line 3 = 0.00 - 0.00 = 0.00"
  - printed: "6"
    value: "42005.00"
    work: "Line 5 total of 1099-DIV box 1a = 42,005.00, with no nominee distribution, so line 6 = 42,005.00"
```
