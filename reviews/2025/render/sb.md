# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 05e8035a29baa702d70000bc13723d9584e8df3d251b0f972e148ca3b75888ab |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e65eb40f5fe17145dcc2dd734860326e0622165c47a3cefa8b422ba36f24419a |
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

Model: The instructions for Line 7a, Question 1 ask whether "at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country," which the restatement asks with only wording differences.

### 8 — During 2025, did you receive a distribution from a foreign trust (a loan of cash or market
Status: **MATCH**

Model: The instructions cover receiving a distribution from a foreign trust, with a loan of cash or marketable securities "generally considered to be a distribution," and being "the grantor of, or transferor to, a foreign trust that existed during 2025." The restatement's "counts" and "at any time" are wording differences that do not change the question.

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: The form's own line 2 wording is not provided, but the instructions have line 1 report all taxable interest, exclude tax-exempt interest, and carry the line 1 subtotal to line 2 less any nominee-style subtraction. Summing taxable interest entries matches this within supported cases, and the refusal names the excluded nominee, accrued interest, OID, premium and similar adjustments.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: The instructions tie line 3 to the exclusion of interest on series EE or I savings bonds under Form 8815. Entering $0 is right within supported cases because the sb.unsupported refusal names the savings bond exclusion and Form 8815.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The provided text has no instruction for line 4 and does not include the form's own line wording, so the subtraction of line 3 from line 2 cannot be confirmed. The face of Schedule B showing line 4 is needed.

Ruling: interface gap; f1040sb (2025) p. 1, line 4: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b", which is the restatement. The model was given only i1040sb pp. 1-3, which has no line 4 instruction, as it says (a coverage gap of the review). Unchanged since the earlier ruling (representation on the form face). Restatement accepted.

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: The instructions say to report all ordinary dividends on line 5, an amount that "should be shown in box 1a of your Forms 1099-DIV or substitute statements," and to carry the subtotal to line 6 less any nominee distribution. The restatement's box 1a total matches within supported cases, and the refusal names nominee income as excluded.

## Raw response

```yaml
```yaml
lines:
  - key: "7a"
    status: MATCH
    reason: "The instructions for Line 7a, Question 1 ask whether \"at any time during 2025 you had a financial interest in or signature authority over a financial account located in a foreign country,\" which the restatement asks with only wording differences."
  - key: "8"
    status: MATCH
    reason: "The instructions cover receiving a distribution from a foreign trust, with a loan of cash or marketable securities \"generally considered to be a distribution,\" and being \"the grantor of, or transferor to, a foreign trust that existed during 2025.\" The restatement's \"counts\" and \"at any time\" are wording differences that do not change the question."
  - key: "2"
    status: MATCH
    reason: "The form's own line 2 wording is not provided, but the instructions have line 1 report all taxable interest, exclude tax-exempt interest, and carry the line 1 subtotal to line 2 less any nominee-style subtraction. Summing taxable interest entries matches this within supported cases, and the refusal names the excluded nominee, accrued interest, OID, premium and similar adjustments."
  - key: "3"
    status: MATCH
    reason: "The instructions tie line 3 to the exclusion of interest on series EE or I savings bonds under Form 8815. Entering $0 is right within supported cases because the sb.unsupported refusal names the savings bond exclusion and Form 8815."
  - key: "4"
    status: UNCLEAR
    reason: "The provided text has no instruction for line 4 and does not include the form's own line wording, so the subtraction of line 3 from line 2 cannot be confirmed. The face of Schedule B showing line 4 is needed."
  - key: "6"
    status: MATCH
    reason: "The instructions say to report all ordinary dividends on line 5, an amount that \"should be shown in box 1a of your Forms 1099-DIV or substitute statements,\" and to carry the subtotal to line 6 less any nominee distribution. The restatement's box 1a total matches within supported cases, and the refusal names nominee income as excluded."
```
```
