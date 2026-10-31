# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 05e8035a29baa702d70000bc13723d9584e8df3d251b0f972e148ca3b75888ab |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 131072 |
| subject sha256 | e65eb40f5fe17145dcc2dd734860326e0622165c47a3cefa8b422ba36f24419a |
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

Model: The restatement covers only Question 1; the IRS line also has Line 7a—Question 2, which asks whether you are required to file FinCEN Form 114.

Ruling: representation; i1040sb p. 3, "Line 7a—Question 2. See FinCEN Form 114 and its instructions at FINCEN.gov to determine whether you must file the form. Check the “Yes” box if you are required to file the form." Question 1 is the printed line sb.line7a, which the restatement shows; Question 2 is the separate helper sb.fbar_required ("Are you required to file FinCEN Form 114 (FBAR)? Determine under its instructions ..."), so both answers of line 7a are asked. The render shows only the printed line; nothing is missing. Unchanged by the fix round. Restatement accepted.

### 8 — During 2025, did you receive a distribution from a foreign trust (a loan of cash or market
Status: **MATCH**

Model: It reflects receiving a foreign-trust distribution, including a loan of cash or marketable securities, or being a grantor or transferor to a foreign trust existing in 2025, as the line 8 instructions state.

### 2 — Total taxable interest from all payers
Status: **MATCH**

Model: For the unadjusted interest cases the program supports, summing taxable interest entries gives the line 2 total; the refusals exclude the special-treatment adjustments named in the instructions.

### 3 — Amount from sb.zero
Status: **MATCH**

Model: The program refuses the savings-bond exclusion through sb.unsupported and otherwise enters zero, which is correct for the supported unadjusted case; the refusal names Form 8815.

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The provided IRS text contains no line 4 instruction or statement that line 4 is line 2 minus line 3, so the arithmetic cannot be verified from the text given.

Ruling: interface gap; f1040sb (2025) p. 1, line 4: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b", which is the restatement. The model was given only i1040sb pp. 1-3, which has no line 4 instruction, as it says (a coverage gap of the review). Restatement accepted.

### 6 — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: The instructions say ordinary dividends are reported from Form 1099-DIV box 1a and, after any nominee subtraction, entered on line 6; the program refuses nominee cases through sb.unsupported.

## Raw response

```yaml
lines:
  - key: "7a"
    status: MISMATCH
    reason: "The restatement covers only Question 1; the IRS line also has Line 7a—Question 2, which asks whether you are required to file FinCEN Form 114."
  - key: "8"
    status: MATCH
    reason: "It reflects receiving a foreign-trust distribution, including a loan of cash or marketable securities, or being a grantor or transferor to a foreign trust existing in 2025, as the line 8 instructions state."
  - key: "2"
    status: MATCH
    reason: "For the unadjusted interest cases the program supports, summing taxable interest entries gives the line 2 total; the refusals exclude the special-treatment adjustments named in the instructions."
  - key: "3"
    status: MATCH
    reason: "The program refuses the savings-bond exclusion through sb.unsupported and otherwise enters zero, which is correct for the supported unadjusted case; the refusal names Form 8815."
  - key: "4"
    status: UNCLEAR
    reason: "The provided IRS text contains no line 4 instruction or statement that line 4 is line 2 minus line 3, so the arithmetic cannot be verified from the text given."
  - key: "6"
    status: MATCH
    reason: "The instructions say ordinary dividends are reported from Form 1099-DIV box 1a and, after any nominee subtraction, entered on line 6; the program refuses nominee cases through sb.unsupported."
```
