# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1b4e65077720724e8bec281c9ef1a95069c825fa6af3d03fbf976bd141352c15 |
| subject sha256 | 1653644d146cd14999e7af99813dfad5a8f3bd84cea082c511a2dc8f699bcf55 |
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

Model: The Line 7a Question 1 instruction asks whether 'at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country,' which the input restates.

### 8 — Received a distribution from, or were grantor of or transferor to, a foreign trust during 
Status: **MATCH**

Model: The Line 8 instructions cover anyone who 'received a distribution from a foreign trust' or 'were the grantor of, or transferor to, a foreign trust that existed during 2025,' which the input captures.

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: Line 1 reports 'all of your taxable interest,' and line 2 is that subtotal less any nominee, accrued-interest, OID or ABP subtraction. Those subtractions are refused via sb.unsupported, so line 2 is the sum of line 1 entries in the supported cases, assuming interest entries hold only taxable interest.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: Line 3 is the Form 8815 exclusion for 'series EE or I U.S. savings bonds issued after 1989.' The savings bond interest exclusion is refused under sb.unsupported, so $0 is correct in the supported cases.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The instructions provided contain no text for line 4, and the Schedule B form face is not included. The subtraction of line 3 from line 2 cannot be confirmed from the given text.

Ruling: representation; project retained. The form face reads "4 Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b" (f1040sb p. 1), which is the restatement. No change to the data.

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Line 5 ordinary dividends 'should be shown in box 1a of your Forms 1099-DIV,' and line 6 is that subtotal less any nominee distribution. Nominee income is refused under sb.unsupported, so total box 1a equals line 6 in the supported cases.

## Raw response

```yaml
```yaml
lines:
  - key: "7a"
    status: MATCH
    reason: "The Line 7a Question 1 instruction asks whether 'at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country,' which the input restates."
  - key: "8"
    status: MATCH
    reason: "The Line 8 instructions cover anyone who 'received a distribution from a foreign trust' or 'were the grantor of, or transferor to, a foreign trust that existed during 2025,' which the input captures."
  - key: "2"
    status: MATCH
    reason: "Line 1 reports 'all of your taxable interest,' and line 2 is that subtotal less any nominee, accrued-interest, OID or ABP subtraction. Those subtractions are refused via sb.unsupported, so line 2 is the sum of line 1 entries in the supported cases, assuming interest entries hold only taxable interest."
  - key: "3"
    status: MATCH
    reason: "Line 3 is the Form 8815 exclusion for 'series EE or I U.S. savings bonds issued after 1989.' The savings bond interest exclusion is refused under sb.unsupported, so $0 is correct in the supported cases."
  - key: "4"
    status: UNCLEAR
    reason: "The instructions provided contain no text for line 4, and the Schedule B form face is not included. The subtraction of line 3 from line 2 cannot be confirmed from the given text."
  - key: "6"
    status: MATCH
    reason: "Line 5 ordinary dividends 'should be shown in box 1a of your Forms 1099-DIV,' and line 6 is that subtotal less any nominee distribution. Nominee income is refused under sb.unsupported, so total box 1a equals line 6 in the supported cases."
```
```
