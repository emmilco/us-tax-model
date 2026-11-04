# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1778c4ca6275720af58f1a3ee8f80e2626e709f958faccda1dc7f7ab98a04116 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | bb04e5c4028849b3e76ebf138151c7dd3ffde5befd99506428206e6b1b32cf77 |
| lines judged | 22 |
| match / mismatch / unclear / missing | 21 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8, 11 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8, 11 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040sb | TY2025; printed April 23, 2025 | 1, 2, 3 | whole document | 2bf62267574473b36fd9a69b6e0837ef74d72ac7d5dcbf1d26e7047d099f1e05 | 1, 2, 3 | 0d38b25d416cb650ef264faf8c1f118dfa4666f3949fbba7120f8c04d4e6914e |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: Direct input of box 2b, "Unrecap. Sec. 1250 gain", described as "the portion of the amount in box 2a that is unrecaptured section 1250 gain".

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Direct input of box 2c, "Section 1202 gain".

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Direct input of box 2d, "Collectibles (28%) gain".

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Direct input of box 2e, "Section 897 ordinary dividends".

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Direct input of box 2f, "Section 897 capital gain".

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Direct input of box 3, "Nondividend distributions", which "Shows a return of capital".

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Direct input of box 9, "Cash liquidation distributions".

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Direct input of box 10, "Noncash liquidation distributions".

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Direct input of box 12, "Exempt-interest dividends". The note that box 13 is already included agrees with the box 13 instruction: "This amount is included in box 12."

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Direct input of box 13, which "Shows exempt-interest dividends subject to the alternative minimum tax".

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: This yes/no input screens the box 3 rule: the distribution "reduces your basis and is not taxable", and any excess over basis "is taxable to you as capital gain". The program refuses the cases it does not handle.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Box 1a "Total ordinary dividends" is the amount the Schedule B instructions say "should be shown in box 1a of your Forms 1099-DIV".

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: Box 1b is "Qualified dividends", the same name as Form 1040 line 3a. The box 1b instruction says "See the Instructions for Form 1040 for how to determine this amount and where to report."

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Box 2a "Total capital gain distr." is taken from the Schedule D capital gain distributions input, which is labeled as generally box 2a.

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: Box 5 "Section 199A dividends" is the portion of box 1a "that may be eligible for the 20% qualified business income deduction". The Form 8995 instructions require holding "for more than 45 days" and say the amount "is reported to you on Form 1099-DIV, line 5".

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Box 2c gain "may be subject to an exclusion". The Schedule D instructions require Form 8949 code "Q" and, for AMT, "enter 7% of your allowable exclusion ... on line 13 of Form 6251". The refusal names both.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 "Shows exempt-interest dividends subject to the alternative minimum tax ... See the Instructions for Form 6251". The program refuses when the amount is above $0.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: The program refuses boxes 2e/2f (section 897 treatment), boxes 9/10 (liquidation distributions), and box 3 when basis is unreconciled ("Any amount received in excess of your basis is taxable to you as capital gain"). This is a narrowing, and the refusal names it.

### bad_special — A gain component exceeds total capital gain distributions
Status: **UNCLEAR**

Restated: (helper "Unrecaptured section 1250 gain, box 2b" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Section 1202 gain, box 2c" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Collectibles (28%) gain, box 2d" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Total special capital-gain distribution components" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a")

Model: The text supports each check on its own, since boxes 2b, 2c and 2d are each "the portion of the amount in box 2a". The text never says these portions are disjoint, so it does not establish that their sum cannot exceed box 2a.

Ruling: ambiguity; amb.2025.div_gain_portions_disjoint (linked to div.bad_special by the p4-docs package). f1099div p. 5, Instructions for Recipient: "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain", "Box 2c. Shows the portion of the amount in box 2a that is section 1202 gain", "Box 2d. Shows the portion of the amount in box 2a that is 28% rate gain". The model accepts each single-box test and objects only that the text does not say the portions are disjoint, so the sum test is not established. That is the register's text at issue; the register chooses the first reading (the portions are disjoint, so their sum cannot exceed box 2a) because each box is a different kind of property (section 1250 real property, section 1202 small business stock, collectibles). Why the line is new to the open list: the restatement and the cited text are unchanged; the previous reviewer judged it MATCH. Project stands.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: The line enters $0 after the scope refusals, and each refusal names the excluded treatment or the correction needed.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Box 1b "Shows the portion of the amount in box 1a" and box 5 "Shows the portion of the amount in box 1a". So neither amount may exceed ordinary dividends.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: This is the sum of boxes 2b, 2c and 2d, used only for the consistency check against box 2a.

## Raw response

```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Direct input of box 2b, \"Unrecap. Sec. 1250 gain\", described as \"the portion of the amount in box 2a that is unrecaptured section 1250 gain\"."
  - key: "box2c"
    status: MATCH
    reason: "Direct input of box 2c, \"Section 1202 gain\"."
  - key: "box2d"
    status: MATCH
    reason: "Direct input of box 2d, \"Collectibles (28%) gain\"."
  - key: "box2e"
    status: MATCH
    reason: "Direct input of box 2e, \"Section 897 ordinary dividends\"."
  - key: "box2f"
    status: MATCH
    reason: "Direct input of box 2f, \"Section 897 capital gain\"."
  - key: "box3"
    status: MATCH
    reason: "Direct input of box 3, \"Nondividend distributions\", which \"Shows a return of capital\"."
  - key: "box9"
    status: MATCH
    reason: "Direct input of box 9, \"Cash liquidation distributions\"."
  - key: "box10"
    status: MATCH
    reason: "Direct input of box 10, \"Noncash liquidation distributions\"."
  - key: "box12"
    status: MATCH
    reason: "Direct input of box 12, \"Exempt-interest dividends\". The note that box 13 is already included agrees with the box 13 instruction: \"This amount is included in box 12.\""
  - key: "box13"
    status: MATCH
    reason: "Direct input of box 13, which \"Shows exempt-interest dividends subject to the alternative minimum tax\"."
  - key: "basis_reconciled"
    status: MATCH
    reason: "This yes/no input screens the box 3 rule: the distribution \"reduces your basis and is not taxable\", and any excess over basis \"is taxable to you as capital gain\". The program refuses the cases it does not handle."
  - key: "box1a"
    status: MATCH
    reason: "Box 1a \"Total ordinary dividends\" is the amount the Schedule B instructions say \"should be shown in box 1a of your Forms 1099-DIV\"."
  - key: "box1b"
    status: MATCH
    reason: "Box 1b is \"Qualified dividends\", the same name as Form 1040 line 3a. The box 1b instruction says \"See the Instructions for Form 1040 for how to determine this amount and where to report.\""
  - key: "box2a"
    status: MATCH
    reason: "Box 2a \"Total capital gain distr.\" is taken from the Schedule D capital gain distributions input, which is labeled as generally box 2a."
  - key: "box5"
    status: MATCH
    reason: "Box 5 \"Section 199A dividends\" is the portion of box 1a \"that may be eligible for the 20% qualified business income deduction\". The Form 8995 instructions require holding \"for more than 45 days\" and say the amount \"is reported to you on Form 1099-DIV, line 5\"."
  - key: "section1202"
    status: MATCH
    reason: "Box 2c gain \"may be subject to an exclusion\". The Schedule D instructions require Form 8949 code \"Q\" and, for AMT, \"enter 7% of your allowable exclusion ... on line 13 of Form 6251\". The refusal names both."
  - key: "amt"
    status: MATCH
    reason: "Box 13 \"Shows exempt-interest dividends subject to the alternative minimum tax ... See the Instructions for Form 6251\". The program refuses when the amount is above $0."
  - key: "unsupported"
    status: MATCH
    reason: "The program refuses boxes 2e/2f (section 897 treatment), boxes 9/10 (liquidation distributions), and box 3 when basis is unreconciled (\"Any amount received in excess of your basis is taxable to you as capital gain\"). This is a narrowing, and the refusal names it."
  - key: "bad_special"
    status: UNCLEAR
    reason: "The text supports each check on its own, since boxes 2b, 2c and 2d are each \"the portion of the amount in box 2a\". The text never says these portions are disjoint, so it does not establish that their sum cannot exceed box 2a."
  - key: "screen"
    status: MATCH
    reason: "The line enters $0 after the scope refusals, and each refusal names the excluded treatment or the correction needed."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b \"Shows the portion of the amount in box 1a\" and box 5 \"Shows the portion of the amount in box 1a\". So neither amount may exceed ordinary dividends."
  - key: "special_total"
    status: MATCH
    reason: "This is the sum of boxes 2b, 2c and 2d, used only for the consistency check against box 2a."
```
