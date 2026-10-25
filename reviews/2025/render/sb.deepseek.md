# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 90a753d8b497c534f6548d9cb811ea1ce524fc72173458f99b5715c5e7c17584 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 1653644d146cd14999e7af99813dfad5a8f3bd84cea082c511a2dc8f699bcf55 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 4 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |

## Lines

### 7a — Any financial interest in or signature authority over a foreign financial account during 2
Status: **MISMATCH**

Restated: Input — Any financial interest in or signature authority over a foreign financial account during 2025?

Model: The restatement covers only Line 7a—Question 1; the IRS also has 'Line 7a—Question 2' requiring a Yes box 'if you are required to file the form' (FinCEN Form 114).

Ruling: open

### 8 — Received a distribution from, or were grantor of or transferor to, a foreign trust during 
Status: **MATCH**

Model: It restates the line 8 condition for receiving a foreign-trust distribution or being grantor/transferor to a foreign trust during 2025.

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: Within supported cases, line 2 is the total taxable interest from the interest entries; the refusals exclude nominee/OID/ABP and other special-treatment items.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: In supported cases line 3 is $0, and the program refuses when a savings bond interest exclusion/Form 8815 issue is present, matching the line 3 exclusion instruction.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The provided IRS instructions do not state line 4's text or computation; they mention lines 2 and 3 but not line 4.

Ruling: open

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Within supported cases, line 6 is total ordinary dividends from Form 1099-DIV box 1a, and the refusals exclude nominee and other adjustments.

## Raw response

```yaml
lines:
  - key: "7a"
    status: MISMATCH
    reason: "The restatement covers only Line 7a—Question 1; the IRS also has 'Line 7a—Question 2' requiring a Yes box 'if you are required to file the form' (FinCEN Form 114)."
  - key: "8"
    status: MATCH
    reason: "It restates the line 8 condition for receiving a foreign-trust distribution or being grantor/transferor to a foreign trust during 2025."
  - key: "2"
    status: MATCH
    reason: "Within supported cases, line 2 is the total taxable interest from the interest entries; the refusals exclude nominee/OID/ABP and other special-treatment items."
  - key: "3"
    status: MATCH
    reason: "In supported cases line 3 is $0, and the program refuses when a savings bond interest exclusion/Form 8815 issue is present, matching the line 3 exclusion instruction."
  - key: "4"
    status: UNCLEAR
    reason: "The provided IRS instructions do not state line 4's text or computation; they mention lines 2 and 3 but not line 4."
  - key: "6"
    status: MATCH
    reason: "Within supported cases, line 6 is total ordinary dividends from Form 1099-DIV box 1a, and the refusals exclude nominee and other adjustments."
```
