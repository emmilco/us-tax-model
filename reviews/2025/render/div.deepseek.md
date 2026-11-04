# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1778c4ca6275720af58f1a3ee8f80e2626e709f958faccda1dc7f7ab98a04116 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | bb04e5c4028849b3e76ebf138151c7dd3ffde5befd99506428206e6b1b32cf77 |
| lines judged | 22 |
| match / mismatch / unclear / missing | 21 / 1 / 0 / 0 |
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

Model: Matches Box 2b unrecaptured section 1250 gain.

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Matches Box 2c section 1202 gain.

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Matches Box 2d collectibles (28%) gain.

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Matches Box 2e section 897 ordinary dividends.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Matches Box 2f section 897 capital gain.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Matches Box 3 nondividend distributions/return of capital.

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Matches Box 9 cash liquidation distributions.

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Matches Box 10 noncash liquidation distributions.

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Matches Box 12 exempt-interest dividends; IRS text confirms Box 13 is included in Box 12.

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Matches Box 13 specified private activity bond interest dividends subject to AMT.

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: The helper asks whether basis reductions were applied for Box 3, consistent with the IRS instruction that distributions reduce basis.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Matches Box 1a total ordinary dividends.

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: Matches Box 1b qualified dividends as a portion of Box 1a.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Matches Box 2a total capital gain distributions.

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: Matches Box 5 section 199A dividends; the Form 8995 instructions support the holding-period and related-payment confirmation.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Box 2c section 1202 gain is present when the amount is greater than zero.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 AMT-exempt-interest dividends are present when the amount is greater than zero.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MISMATCH**

Restated: (helper "Section 897 ordinary dividends, box 2e" > $0 or helper "Section 897 capital gain, box 2f" > $0 or helper "Cash liquidation distributions, box 9" > $0 or helper "Noncash liquidation distributions, box 10" > $0 or helper "Nondividend distributions/return of capital, box 3" > $0 and helper "For box 3, have basis reductions been applied to records with no distribution exceeding basis?" = false)

Model: MISMATCH: The IRS text says 'Any amount received in excess of your basis is taxable to you as capital gain.' The condition only flags Box 3 when basis reductions were not applied to records with no distribution exceeding basis, so it omits distributions exceeding basis.

Ruling: model error; f1099div p. 5, Box 3: "To the extent of your cost (or other basis) in the stock, the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain." The input div.basis_reconciled asks "For box 3, have basis reductions been applied to records with no distribution exceeding basis?"; for a positive box 3 a No (which includes any distribution exceeding basis) makes div.unsupported true and div.screen refuses. The excess-distribution case the model says is omitted is therefore inside the question and refused. Same reading as the prior ruling on this line (sidecar `reviews/2025/render/div.deepseek.rulings.json`); the restatement is unchanged, and the line reopened only because the review context changed. Project stands.

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: Matches the IRS statements that Boxes 2b, 2c, and 2d are portions of Box 2a.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: The refusals correctly name the excluded section 1202, AMT, section 897/liquidation/Box 3 excess, and inconsistent portion cases.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Matches the IRS statements that qualified dividends and section 199A dividends are portions of ordinary dividends.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: Sums the three special components 2b, 2c, and 2d, consistent with their being portions of Box 2a.

## Raw response

```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Matches Box 2b unrecaptured section 1250 gain."
  - key: "box2c"
    status: MATCH
    reason: "Matches Box 2c section 1202 gain."
  - key: "box2d"
    status: MATCH
    reason: "Matches Box 2d collectibles (28%) gain."
  - key: "box2e"
    status: MATCH
    reason: "Matches Box 2e section 897 ordinary dividends."
  - key: "box2f"
    status: MATCH
    reason: "Matches Box 2f section 897 capital gain."
  - key: "box3"
    status: MATCH
    reason: "Matches Box 3 nondividend distributions/return of capital."
  - key: "box9"
    status: MATCH
    reason: "Matches Box 9 cash liquidation distributions."
  - key: "box10"
    status: MATCH
    reason: "Matches Box 10 noncash liquidation distributions."
  - key: "box12"
    status: MATCH
    reason: "Matches Box 12 exempt-interest dividends; IRS text confirms Box 13 is included in Box 12."
  - key: "box13"
    status: MATCH
    reason: "Matches Box 13 specified private activity bond interest dividends subject to AMT."
  - key: "basis_reconciled"
    status: MATCH
    reason: "The helper asks whether basis reductions were applied for Box 3, consistent with the IRS instruction that distributions reduce basis."
  - key: "box1a"
    status: MATCH
    reason: "Matches Box 1a total ordinary dividends."
  - key: "box1b"
    status: MATCH
    reason: "Matches Box 1b qualified dividends as a portion of Box 1a."
  - key: "box2a"
    status: MATCH
    reason: "Matches Box 2a total capital gain distributions."
  - key: "box5"
    status: MATCH
    reason: "Matches Box 5 section 199A dividends; the Form 8995 instructions support the holding-period and related-payment confirmation."
  - key: "section1202"
    status: MATCH
    reason: "Box 2c section 1202 gain is present when the amount is greater than zero."
  - key: "amt"
    status: MATCH
    reason: "Box 13 AMT-exempt-interest dividends are present when the amount is greater than zero."
  - key: "unsupported"
    status: MISMATCH
    reason: "MISMATCH: The IRS text says 'Any amount received in excess of your basis is taxable to you as capital gain.' The condition only flags Box 3 when basis reductions were not applied to records with no distribution exceeding basis, so it omits distributions exceeding basis."
  - key: "bad_special"
    status: MATCH
    reason: "Matches the IRS statements that Boxes 2b, 2c, and 2d are portions of Box 2a."
  - key: "screen"
    status: MATCH
    reason: "The refusals correctly name the excluded section 1202, AMT, section 897/liquidation/Box 3 excess, and inconsistent portion cases."
  - key: "bad_components"
    status: MATCH
    reason: "Matches the IRS statements that qualified dividends and section 199A dividends are portions of ordinary dividends."
  - key: "special_total"
    status: MATCH
    reason: "Sums the three special components 2b, 2c, and 2d, consistent with their being portions of Box 2a."
```
