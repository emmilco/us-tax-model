# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4abdcb9867f12d41bc90be42730618ca1d74159513cc91e38c5f727e89089892 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 5 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 |

## Lines

### 7a — Any financial interest in or signature authority over a foreign financial account during 2
Status: **MATCH**

Model: The instructions for Line 7a Question 1 say to check "Yes" if "at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country." The input asks the same question.

### 8 — Received a distribution from, or were grantor of or transferor to, a foreign trust during 
Status: **MATCH**

Model: The Line 8 instructions cover receiving "a distribution from a foreign trust" and being "the grantor of, or transferor to, a foreign trust that existed during 2025." The input asks the same thing, and the line8 refusal points to Form 3520 / 3520-A.

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: The instructions put "all of your taxable interest" on line 1 and carry the subtotal to line 2, less any "Nominee Distribution" (or Accrued Interest/OID/ABP adjustments). Summing the interest entries matches for supported cases, and sb.unsupported refuses the adjustment cases. This assumes interest.amount holds only taxable interest, which the restatement does not state.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: Per the instructions, line 3 holds the Form 8815 exclusion for series EE or I savings bonds used for qualified higher education expenses. Entering $0 is correct within scope, because sb.unsupported (which includes "savings-bond exclusion") refuses and names Form 8815.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The IRS text given has no instruction or form-face wording for line 4, so "subtract line 3 from line 2" cannot be checked against it.

Ruling: representation; project retained. The form face reads "4 Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b" (f1040sb p. 1), which is the restatement. No change to the data.

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: The instructions put "all of your ordinary dividends" ("box 1a of your Forms 1099-DIV") on line 5 and carry the total to line 6, less any "Nominee Distribution." Using the box 1a total matches for supported cases, and sb.unsupported refuses nominee cases.

## Raw response

```yaml
```yaml
lines:
  - key: "7a"
    status: MATCH
    reason: "The instructions for Line 7a Question 1 say to check \"Yes\" if \"at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country.\" The input asks the same question."
  - key: "8"
    status: MATCH
    reason: "The Line 8 instructions cover receiving \"a distribution from a foreign trust\" and being \"the grantor of, or transferor to, a foreign trust that existed during 2025.\" The input asks the same thing, and the line8 refusal points to Form 3520 / 3520-A."
  - key: "2"
    status: MATCH
    reason: "The instructions put \"all of your taxable interest\" on line 1 and carry the subtotal to line 2, less any \"Nominee Distribution\" (or Accrued Interest/OID/ABP adjustments). Summing the interest entries matches for supported cases, and sb.unsupported refuses the adjustment cases. This assumes interest.amount holds only taxable interest, which the restatement does not state."
  - key: "3"
    status: MATCH
    reason: "Per the instructions, line 3 holds the Form 8815 exclusion for series EE or I savings bonds used for qualified higher education expenses. Entering $0 is correct within scope, because sb.unsupported (which includes \"savings-bond exclusion\") refuses and names Form 8815."
  - key: "4"
    status: UNCLEAR
    reason: "The IRS text given has no instruction or form-face wording for line 4, so \"subtract line 3 from line 2\" cannot be checked against it."
  - key: "6"
    status: MATCH
    reason: "The instructions put \"all of your ordinary dividends\" (\"box 1a of your Forms 1099-DIV\") on line 5 and carry the total to line 6, less any \"Nominee Distribution.\" Using the box 1a total matches for supported cases, and sb.unsupported refuses nominee cases."
```
```
