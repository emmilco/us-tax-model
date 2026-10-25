# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b7a7d184024eaf4070dd8db4ecc8ec5e9333b4baa8f28be436c8a7b551d77606 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 4ad39baafac680e2a95d81964b30abeac08ebe2d3b396d444dd8508e7f4e4924 |
| lines judged | 22 |
| match / mismatch / unclear / missing | 19 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: IRS Box 2b is the unrecaptured section 1250 gain portion of box 2a; the helper simply inputs that box amount.

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: IRS Box 2c is the section 1202 gain portion of box 2a; the helper inputs that box amount.

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: IRS Box 2d is the collectibles (28%) gain portion of box 2a; the helper inputs that box amount.

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: IRS Box 2e is section 897 ordinary dividends (a portion of box 1a); the helper inputs that box amount.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: IRS Box 2f is section 897 capital gain (a portion of box 2a); the helper inputs that box amount.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: IRS Box 3 is return of capital/nondividend distributions; the helper inputs that box amount.

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: IRS Boxes 9 and 10 show cash and noncash liquidation distributions; the helper inputs box 9.

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: IRS Boxes 9 and 10 show cash and noncash liquidation distributions; the helper inputs box 10.

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: IRS Box 12 shows exempt-interest dividends, and the text states Box 13 amounts are included in Box 12; the helper inputs that box amount.

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: IRS Box 13 shows specified private activity bond interest dividends subject to AMT and included in Box 12; the helper inputs that box amount.

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: The IRS text says Box 3 reduces basis to the extent of basis and excess is capital gain; asking whether basis reductions were applied is consistent with that treatment.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: IRS Box 1a is total ordinary dividends; the helper takes that amount from sb.ordinary_dividends.

### box1b — Amount from f1040.line3a
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 3a.

Model: IRS says 'Box 1b. Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates'; the helper instead takes Form 1040 line 3a, not the Form 1099-DIV box 1b portion.

Ruling: scope; archived f1099div recipient instructions p. 5 describes each payer box 1b. div is expressly an aggregate values sheet, not a prepared information return: div.box1b displays the supplied Form 1040 line 3a subtotal after its qualification exceptions (i1040gi p. 26), not an individual payer box. The objection correctly distinguishes those quantities. Retain that disclosed aggregate-input scope; this does not validate raw per-payer box 1b amounts or claim the adjusted subtotal is always their unadjusted sum.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: IRS Box 2a is total capital gain distributions; the helper takes that amount from sd.distributions.

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: IRS Box 5 shows the portion of box 1a potentially eligible for the section 199A deduction; the helper takes the box 5 amount from qbi.dividends.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: IRS Box 2c is section 1202 gain; a presence check for box 2c > 0 is consistent.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: IRS Box 13 is exempt-interest dividends subject to AMT; a presence check for box 13 > 0 is consistent.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MISMATCH**

Restated: (helper "Section 897 ordinary dividends, box 2e" > $0 or helper "Section 897 capital gain, box 2f" > $0 or helper "Cash liquidation distributions, box 9" > $0 or helper "Noncash liquidation distributions, box 10" > $0 or helper "Nondividend distributions/return of capital, box 3" > $0 and helper "For box 3, have basis reductions been applied to records with no distribution exceeding basis?" = false)

Model: IRS says 'Any amount received in excess of your basis is taxable to you as capital gain'; the helper only tests box 3 > 0 with basis_reconciled false and omits an excess-distribution condition.

Ruling: model error; archived f1099div recipient instructions p. 5 Box 3 taxes amounts exceeding basis. div.basis_reconciled explicitly asks whether basis reductions were applied WITH NO DISTRIBUTION EXCEEDING BASIS. For positive box 3, a false answer makes div.unsupported true and div.screen refuses, with a remedy naming basis reconciliation and excess gain. Thus the alleged omitted excess-distribution condition is present in the shared question and its enforcement. One model error among 22 judged lines is below the 10% limit; this does not turn the aggregate-display scope into per-payer verification.

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: IRS says Boxes 2b, 2c, and 2d are portions of box 2a; the helper flags components or their total exceeding box 2a.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: The refusals name the out-of-scope Section 1202/AMT, section 897/liquidation/return-of-capital, and inconsistent component cases; entering $0 after those checks is a scope screen.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MISMATCH**

Restated: (f1040 line 3a > sb helper "Total ordinary dividends, Form 1099-DIV box 1a" or qbi helper "Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements" > sb helper "Total ordinary dividends, Form 1099-DIV box 1a")

Model: IRS says Box 1b and Box 5 are portions of the amount in box 1a; the helper compares Form 1040 line 3a (total qualified dividends) to box 1a instead of comparing box 1b to box 1a.

Ruling: scope; f1099div recipient instructions p. 5 says boxes 1b/5 are portions of box 1a. div.bad_components is a necessary consistency check on shared aggregate supplied totals (f1040.line3a, qbi.dividends and sb.ordinary_dividends); div is a values sheet rather than per-payer information-return preparation. This gate checks that supplied qualified/199A dividends do not exceed supplied ordinary dividends. It does not assert per-payer validation or equality between an adjusted Form 1040 subtotal and each raw box.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: The IRS text identifies boxes 2b, 2c, and 2d as portions/components of box 2a; summing those components is consistent.

## Raw response

```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "IRS Box 2b is the unrecaptured section 1250 gain portion of box 2a; the helper simply inputs that box amount."
  - key: "box2c"
    status: MATCH
    reason: "IRS Box 2c is the section 1202 gain portion of box 2a; the helper inputs that box amount."
  - key: "box2d"
    status: MATCH
    reason: "IRS Box 2d is the collectibles (28%) gain portion of box 2a; the helper inputs that box amount."
  - key: "box2e"
    status: MATCH
    reason: "IRS Box 2e is section 897 ordinary dividends (a portion of box 1a); the helper inputs that box amount."
  - key: "box2f"
    status: MATCH
    reason: "IRS Box 2f is section 897 capital gain (a portion of box 2a); the helper inputs that box amount."
  - key: "box3"
    status: MATCH
    reason: "IRS Box 3 is return of capital/nondividend distributions; the helper inputs that box amount."
  - key: "box9"
    status: MATCH
    reason: "IRS Boxes 9 and 10 show cash and noncash liquidation distributions; the helper inputs box 9."
  - key: "box10"
    status: MATCH
    reason: "IRS Boxes 9 and 10 show cash and noncash liquidation distributions; the helper inputs box 10."
  - key: "box12"
    status: MATCH
    reason: "IRS Box 12 shows exempt-interest dividends, and the text states Box 13 amounts are included in Box 12; the helper inputs that box amount."
  - key: "box13"
    status: MATCH
    reason: "IRS Box 13 shows specified private activity bond interest dividends subject to AMT and included in Box 12; the helper inputs that box amount."
  - key: "basis_reconciled"
    status: MATCH
    reason: "The IRS text says Box 3 reduces basis to the extent of basis and excess is capital gain; asking whether basis reductions were applied is consistent with that treatment."
  - key: "box1a"
    status: MATCH
    reason: "IRS Box 1a is total ordinary dividends; the helper takes that amount from sb.ordinary_dividends."
  - key: "box1b"
    status: MISMATCH
    reason: "IRS says 'Box 1b. Shows the portion of the amount in box 1a that may be eligible for reduced capital gains rates'; the helper instead takes Form 1040 line 3a, not the Form 1099-DIV box 1b portion."
  - key: "box2a"
    status: MATCH
    reason: "IRS Box 2a is total capital gain distributions; the helper takes that amount from sd.distributions."
  - key: "box5"
    status: MATCH
    reason: "IRS Box 5 shows the portion of box 1a potentially eligible for the section 199A deduction; the helper takes the box 5 amount from qbi.dividends."
  - key: "section1202"
    status: MATCH
    reason: "IRS Box 2c is section 1202 gain; a presence check for box 2c > 0 is consistent."
  - key: "amt"
    status: MATCH
    reason: "IRS Box 13 is exempt-interest dividends subject to AMT; a presence check for box 13 > 0 is consistent."
  - key: "unsupported"
    status: MISMATCH
    reason: "IRS says 'Any amount received in excess of your basis is taxable to you as capital gain'; the helper only tests box 3 > 0 with basis_reconciled false and omits an excess-distribution condition."
  - key: "bad_special"
    status: MATCH
    reason: "IRS says Boxes 2b, 2c, and 2d are portions of box 2a; the helper flags components or their total exceeding box 2a."
  - key: "screen"
    status: MATCH
    reason: "The refusals name the out-of-scope Section 1202/AMT, section 897/liquidation/return-of-capital, and inconsistent component cases; entering $0 after those checks is a scope screen."
  - key: "bad_components"
    status: MISMATCH
    reason: "IRS says Box 1b and Box 5 are portions of the amount in box 1a; the helper compares Form 1040 line 3a (total qualified dividends) to box 1a instead of comparing box 1b to box 1a."
  - key: "special_total"
    status: MATCH
    reason: "The IRS text identifies boxes 2b, 2c, and 2d as portions/components of box 2a; summing those components is consistent."
```
