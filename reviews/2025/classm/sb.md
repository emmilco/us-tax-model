# Class M hand-work — sb

`Schedule B — supported interest and ordinary dividends` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 |

## Lines

### case classm.sb.1 — prompt sha256 6f4dd71e3c709e08129919a0b31cbf939aa9f6889503b9833517fc394e65e40f; branches: sb.unsupported:false, sb.line7a:false, sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.partIII:false

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

Value: $0.00

### case classm.sb.2 — prompt sha256 fac0a2db777330ff0aab26fff1dd90399f4f2091c7fe492ade77c3ff6e646320; branches: sb.unsupported:false, sb.line7a:true, sb.fbar_required:false, sb.form8938:false, sb.line8:false, sb.partIII:true

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

## Raw responses

### classm.sb.1

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "No taxable interest amounts given for line 1 and no nominee/OID/ABP/accrued-interest subtractions; total = 0.00"
  - printed: "3"
    value: "0.00"
    work: "No savings-bond exclusion (Form 8815) claimed; amount from sb.zero = 0.00"
  - printed: "4"
    value: "0.00"
    work: "line 2 0.00 - line 3 0.00 = 0.00"
  - printed: "6"
    value: "0.00"
    work: "Ordinary dividends, Form 1099-DIV box 1a = 0.00; no nominee distribution"
```
```

### classm.sb.2

```yaml
```yaml
lines:
  - printed: "2"
    value: "0.00"
    work: "Sum of line 1 interest: bank_a 0.00 = 0.00; no nominee/OID/ABP/accrued-interest subtractions"
  - printed: "3"
    value: "0.00"
    work: "No savings-bond exclusion (no Form 8815); amount from sb.zero = 0.00"
  - printed: "4"
    value: "0.00"
    work: "Line 2 0.00 - line 3 0.00 = 0.00"
  - printed: "6"
    value: "0.00"
    work: "Total ordinary dividends, 1099-DIV box 1a 0.00; no nominee subtraction = 0.00"
```
```
