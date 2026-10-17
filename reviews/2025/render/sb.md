# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9a86055e618ba4c544e13736a7d7fcba9a56fde9ce13843db501ea05d64ffa6f |
| lines judged | 6 |
| match / mismatch / unclear / missing | 5 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

## Lines

### 7a — Any financial interest in or signature authority over a foreign financial account during 2
Status: **MATCH**

Model: The instructions say to check "Yes" if "at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country," which the restatement captures.

### 8 — Received a distribution from, or were grantor of or transferor to, a foreign trust during 
Status: **MATCH**

Model: The IRS text covers a filer who "received a distribution from, or were a grantor of, or transferor to, a foreign trust," which matches the restatement. The program refuses the Form 3520/3520-A path.

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: Line 1 reports "all of your taxable interest." Line 2 differs from the line 1 subtotal only by the nominee, accrued interest, OID and ABP subtractions, and sb.unsupported refuses those cases. Within the supported cases, summing the interest entries gives line 2.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: Line 3 is the savings-bond interest exclusion from Form 8815. The program refuses that case under sb.unsupported, so $0 is correct within scope.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The instruction pages given have no text for line 4, and the form face is not provided. I cannot confirm from the IRS text that line 4 is line 2 minus line 3.

Ruling: representation; project retained. The form face reads "4 Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b" (f1040sb p. 1), which is the restatement. No change to the data.

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Line 5 ordinary dividends "should be shown in box 1a of your Forms 1099-DIV." Line 6 is the line 5 subtotal less any nominee distribution, and nominee income is refused. Within scope, line 6 equals total box 1a dividends.

## Raw response

```yaml
lines:
  - key: "7a"
    status: MATCH
    reason: "The instructions say to check \"Yes\" if \"at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country,\" which the restatement captures."
  - key: "8"
    status: MATCH
    reason: "The IRS text covers a filer who \"received a distribution from, or were a grantor of, or transferor to, a foreign trust,\" which matches the restatement. The program refuses the Form 3520/3520-A path."
  - key: "2"
    status: MATCH
    reason: "Line 1 reports \"all of your taxable interest.\" Line 2 differs from the line 1 subtotal only by the nominee, accrued interest, OID and ABP subtractions, and sb.unsupported refuses those cases. Within the supported cases, summing the interest entries gives line 2."
  - key: "3"
    status: MATCH
    reason: "Line 3 is the savings-bond interest exclusion from Form 8815. The program refuses that case under sb.unsupported, so $0 is correct within scope."
  - key: "4"
    status: UNCLEAR
    reason: "The instruction pages given have no text for line 4, and the form face is not provided. I cannot confirm from the IRS text that line 4 is line 2 minus line 3."
  - key: "6"
    status: MATCH
    reason: "Line 5 ordinary dividends \"should be shown in box 1a of your Forms 1099-DIV.\" Line 6 is the line 5 subtotal less any nominee distribution, and nominee income is refused. Within scope, line 6 equals total box 1a dividends."
```
