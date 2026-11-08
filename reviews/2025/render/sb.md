# Render comparison — sb

The rendered English of every printed line of `Schedule B — supported interest and ordinary dividends` (`rendered/2025/sb.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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

Model: The instructions say to report on line 1 'all of your taxable interest' and to enter on line 2 the subtotal, less any nominee, accrued-interest, OID or ABP subtraction. Summing taxable interest per payer, excluding tax-exempt interest, gives line 2 when there are no such adjustments, and the special-treatment refusal covers the adjustment cases.
Reviewed in: pass 59ec93f6f8ab

### 3 — Amount from sb.zero
Status: **MATCH**

Model: Line 3 is the excludable savings bond interest figured on Form 8815 ('you may be able to exclude part or all of the interest on those bonds. See Form 8815'). Entering $0 is right when no exclusion is claimed, and the refusal covers a savings bond interest exclusion.
Reviewed in: pass 59ec93f6f8ab

### 4 — Subtract sb.line3 from sb.line2
Status: **UNCLEAR**

Restated: Subtract line 3 from line 2.

Model: The pages given have no printed Schedule B form text and no instruction text for line 4. 'Subtract line 3 from line 2' cannot be checked against the IRS wording for this line.

Ruling: interface gap; f1040sb (2025) p. 1, line 4: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b", which is the restatement. The model was given only i1040sb pp. 1-3, which has no line 4 instruction, as it says (a coverage gap of the review), as the earlier ruling. Restatement accepted.
Reviewed in: pass 59ec93f6f8ab

### 6 — Amount from sb.ordinary_dividends_if_dividends
Status: **MATCH**

Model: The instructions say to report on line 5 'all of your ordinary dividends,' which 'should be shown in box 1a of your Forms 1099-DIV or substitute statements.' Line 6 equals that total less any nominee distribution. Using the box 1a total (zero when no dividends were received) is right without nominee amounts, and the special-treatment refusal covers nominee dividends.
Reviewed in: pass 59ec93f6f8ab

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 7a | 6a532b2dfe92d7e1cd9802a6b8f59bf57f5bef87caac66d805d0fe049bc236f8 |
| 8 | 445d938d4da8dd8b7c57c19b26cb592f89320b91434a451560a7a83b2ce0f333 |
| 2 | 0eeaaf1a147ae7dc14fd5cd955d50fb631bdfe59fa8e0f396ccf4385af13e7d1 |
| 3 | 4ba65cf98028b6883ca69c9aacc7839ce88770afcdb9f01f321bac0b203dac1b |
| 4 | 48fa72f977ae9944236be534a8859bdf10893f2d8d763124dbc754e6e25f5267 |
| 6 | a66837a6dc03e5193c1328556eaa9d211e4905ea0b6f104472940cbed646c065 |
| (rest of the document) | a94af5b651134640cc219aba4abb67814d5b7730c6a2f18c6e978773a29f39cc |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 59ec93f6f8ab

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 2, 3, 4, 6 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 59ec93f6f8abcc4943efc0055b5087b00f24bdca563330bb7b4c298ff904f4e3 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 32d051082ad8126edf36d0349aa416fbf1be85671489dc67ac4710bc69c7299a |
| receipt | .transcription/sb.render.lines-aef7d034b5aa |
| lines judged | 4 |
| match / mismatch / unclear / missing | 3 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 11 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

##### Raw response

```yaml
```yaml
lines:
  - key: "2"
    status: MATCH
    reason: "The instructions say to report on line 1 'all of your taxable interest' and to enter on line 2 the subtotal, less any nominee, accrued-interest, OID or ABP subtraction. Summing taxable interest per payer, excluding tax-exempt interest, gives line 2 when there are no such adjustments, and the special-treatment refusal covers the adjustment cases."
  - key: "3"
    status: MATCH
    reason: "Line 3 is the excludable savings bond interest figured on Form 8815 ('you may be able to exclude part or all of the interest on those bonds. See Form 8815'). Entering $0 is right when no exclusion is claimed, and the refusal covers a savings bond interest exclusion."
  - key: "4"
    status: UNCLEAR
    reason: "The pages given have no printed Schedule B form text and no instruction text for line 4. 'Subtract line 3 from line 2' cannot be checked against the IRS wording for this line."
  - key: "6"
    status: MATCH
    reason: "The instructions say to report on line 5 'all of your ordinary dividends,' which 'should be shown in box 1a of your Forms 1099-DIV or substitute statements.' Line 6 equals that total less any nominee distribution. Using the box 1a total (zero when no dividends were received) is right without nominee amounts, and the special-treatment refusal covers nominee dividends."
```
```

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
