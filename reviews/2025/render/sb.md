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

Model: This matches Line 7a Question 1: "Check the 'Yes' box if at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country." The input asks the same question.

### 8 — Received a distribution from, or were grantor of or transferor to, a foreign trust during 
Status: **MATCH**

Model: The input covers the same cases as the Line 8 instructions: "received a distribution from a foreign trust" and "were the grantor of, or transferor to, a foreign trust that existed during 2025."

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: Per the instructions, line 2 is the subtotal of all line 1 interest, less any nominee, accrued interest, OID or ABP subtractions. Those cases are refused by sb.unsupported, so in the supported cases line 2 is just the sum of the line 1 amounts. The foreign-reporting refusals only narrow the scope further.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: Line 3 is the Form 8815 savings bond interest exclusion ("you may be able to exclude part or all of the interest on those bonds. See Form 8815"). sb.unsupported refuses the savings-bond exclusion, so line 3 is $0 in every supported case.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The pages provided do not include the form face or any instruction for line 4, so nothing in the text says how line 4 is computed. That includes subtracting line 3 from line 2.

Ruling: representation; project retained. The form face reads "4 Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b" (f1040sb p. 1), which is the restatement. No change to the data.

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Line 5 is "all of your ordinary dividends," which "should be shown in box 1a of your Forms 1099-DIV." Line 6 is that subtotal minus nominee amounts. Nominee income is refused by sb.unsupported, so in supported cases line 6 equals total box 1a ordinary dividends.

## Raw response

```yaml
```yaml
lines:
  - key: "7a"
    status: MATCH
    reason: "This matches Line 7a Question 1: \"Check the 'Yes' box if at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country.\" The input asks the same question."
  - key: "8"
    status: MATCH
    reason: "The input covers the same cases as the Line 8 instructions: \"received a distribution from a foreign trust\" and \"were the grantor of, or transferor to, a foreign trust that existed during 2025.\""
  - key: "2"
    status: MATCH
    reason: "Per the instructions, line 2 is the subtotal of all line 1 interest, less any nominee, accrued interest, OID or ABP subtractions. Those cases are refused by sb.unsupported, so in the supported cases line 2 is just the sum of the line 1 amounts. The foreign-reporting refusals only narrow the scope further."
  - key: "3"
    status: MATCH
    reason: "Line 3 is the Form 8815 savings bond interest exclusion (\"you may be able to exclude part or all of the interest on those bonds. See Form 8815\"). sb.unsupported refuses the savings-bond exclusion, so line 3 is $0 in every supported case."
  - key: "4"
    status: UNCLEAR
    reason: "The pages provided do not include the form face or any instruction for line 4, so nothing in the text says how line 4 is computed. That includes subtracting line 3 from line 2."
  - key: "6"
    status: MATCH
    reason: "Line 5 is \"all of your ordinary dividends,\" which \"should be shown in box 1a of your Forms 1099-DIV.\" Line 6 is that subtotal minus nominee amounts. Nominee income is refused by sb.unsupported, so in supported cases line 6 equals total box 1a ordinary dividends."
```
```
