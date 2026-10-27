# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1778c4ca6275720af58f1a3ee8f80e2626e709f958faccda1dc7f7ab98a04116 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 6598a6f635c04edcaa5692a3c853bed1c4368436c016d206cc3fc39b49b95c23 |
| lines judged | 22 |
| match / mismatch / unclear / missing | 22 / 0 / 0 / 0 |
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

Model: The IRS text says box 2b 'Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain'; the helper simply carries the box 2b amount as a nonnegative input.

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: The IRS text says box 2c 'Shows the portion of the amount in box 2a that is section 1202 gain'; the helper carries the box 2c amount as supplied.

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: The IRS text says box 2d 'Shows the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles'; the helper carries the box 2d amount.

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: The IRS text says box 2e shows the portion of box 1a that is section 897 gain attributable to disposition of USRPI; the label and input match that line.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: The IRS text says box 2f shows the portion of box 2a that is section 897 gain attributable to disposition of USRPI; the helper carries the box 2f amount.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: 'Box 3. Shows a return of capital'; the helper carries the nondividend distribution/return-of-capital amount as supplied.

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: 'Boxes 9 and 10. Show cash and noncash liquidation distributions'; the helper carries the box 9 cash liquidation amount.

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: 'Boxes 9 and 10. Show cash and noncash liquidation distributions'; the helper carries the box 10 noncash liquidation amount.

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Box 12 'Shows exempt-interest dividends from a mutual fund or other RIC paid to you during the calendar year,' and the IRS text confirms for box 13 that 'This amount is included in box 12,' matching the parenthetical.

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Box 13 'Shows exempt-interest dividends subject to the alternative minimum tax'; the helper carries that amount as supplied.

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: Consistent with box 3 instructions that to the extent of basis 'the distribution reduces your basis and is not taxable,' with any excess 'taxable to you as capital gain'; the flag records whether that basis reduction was applied.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Box 1a 'Shows total ordinary dividends that are taxable,' and Schedule B line 5 says this 'should be shown in box 1a of your Forms 1099-DIV,' so drawing box 1a from sb.ordinary_dividends matches.

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: Box 1b is the portion of box 1a eligible for reduced capital gains rates, which the IRS directs the recipient to report as qualified dividends; taking that reported amount (Form 1040 line 3a, 'Qualified dividends') is consistent.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Box 2a 'Shows total capital gain distributions from a regulated investment company (RIC) or real estate investment trust (REIT),' matching the sd.distributions source.

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: Box 5 'Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction under section 199A'; the i8995 text supports the holding-period and no-obligation-to-another conditions.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Box 2c reports section 1202 gain from small business stock, so testing box 2c > $0 correctly identifies a section 1202 distribution.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 shows exempt-interest dividends subject to the alternative minimum tax, so testing box 13 > $0 correctly identifies AMT-relevant dividends.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: Boxes 2e/2f (section 897), 9/10 (liquidation), and unreconciled box 3 basis/excess gain are all special treatments outside a plain dividend computation; flagging them narrows scope rather than changing a supported value.

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: Boxes 2b, 2c and 2d are each 'the portion of the amount in box 2a,' so testing each component (and their total) against box 2a correctly detects inconsistent amounts.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: The $0 screen with refusals is a scope gate; each refusal names the excluded case and the form needed (Form 8949 code Q and Form 6251 for section 1202 exclusion, Form 6251 for box 13 AMT interest), consistent with the IRS text.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: The IRS text makes box 1b and box 5 portions of box 1a, so testing qualified dividends and section 199A dividends against total ordinary dividends correctly detects inconsistent totals.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: Boxes 2b, 2c and 2d are each portions of box 2a, so summing them as the total special capital-gain components is consistent with the IRS text.

## Raw response

```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "The IRS text says box 2b 'Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain'; the helper simply carries the box 2b amount as a nonnegative input."
  - key: "box2c"
    status: MATCH
    reason: "The IRS text says box 2c 'Shows the portion of the amount in box 2a that is section 1202 gain'; the helper carries the box 2c amount as supplied."
  - key: "box2d"
    status: MATCH
    reason: "The IRS text says box 2d 'Shows the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles'; the helper carries the box 2d amount."
  - key: "box2e"
    status: MATCH
    reason: "The IRS text says box 2e shows the portion of box 1a that is section 897 gain attributable to disposition of USRPI; the label and input match that line."
  - key: "box2f"
    status: MATCH
    reason: "The IRS text says box 2f shows the portion of box 2a that is section 897 gain attributable to disposition of USRPI; the helper carries the box 2f amount."
  - key: "box3"
    status: MATCH
    reason: "'Box 3. Shows a return of capital'; the helper carries the nondividend distribution/return-of-capital amount as supplied."
  - key: "box9"
    status: MATCH
    reason: "'Boxes 9 and 10. Show cash and noncash liquidation distributions'; the helper carries the box 9 cash liquidation amount."
  - key: "box10"
    status: MATCH
    reason: "'Boxes 9 and 10. Show cash and noncash liquidation distributions'; the helper carries the box 10 noncash liquidation amount."
  - key: "box12"
    status: MATCH
    reason: "Box 12 'Shows exempt-interest dividends from a mutual fund or other RIC paid to you during the calendar year,' and the IRS text confirms for box 13 that 'This amount is included in box 12,' matching the parenthetical."
  - key: "box13"
    status: MATCH
    reason: "Box 13 'Shows exempt-interest dividends subject to the alternative minimum tax'; the helper carries that amount as supplied."
  - key: "basis_reconciled"
    status: MATCH
    reason: "Consistent with box 3 instructions that to the extent of basis 'the distribution reduces your basis and is not taxable,' with any excess 'taxable to you as capital gain'; the flag records whether that basis reduction was applied."
  - key: "box1a"
    status: MATCH
    reason: "Box 1a 'Shows total ordinary dividends that are taxable,' and Schedule B line 5 says this 'should be shown in box 1a of your Forms 1099-DIV,' so drawing box 1a from sb.ordinary_dividends matches."
  - key: "box1b"
    status: MATCH
    reason: "Box 1b is the portion of box 1a eligible for reduced capital gains rates, which the IRS directs the recipient to report as qualified dividends; taking that reported amount (Form 1040 line 3a, 'Qualified dividends') is consistent."
  - key: "box2a"
    status: MATCH
    reason: "Box 2a 'Shows total capital gain distributions from a regulated investment company (RIC) or real estate investment trust (REIT),' matching the sd.distributions source."
  - key: "box5"
    status: MATCH
    reason: "Box 5 'Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction under section 199A'; the i8995 text supports the holding-period and no-obligation-to-another conditions."
  - key: "section1202"
    status: MATCH
    reason: "Box 2c reports section 1202 gain from small business stock, so testing box 2c > $0 correctly identifies a section 1202 distribution."
  - key: "amt"
    status: MATCH
    reason: "Box 13 shows exempt-interest dividends subject to the alternative minimum tax, so testing box 13 > $0 correctly identifies AMT-relevant dividends."
  - key: "unsupported"
    status: MATCH
    reason: "Boxes 2e/2f (section 897), 9/10 (liquidation), and unreconciled box 3 basis/excess gain are all special treatments outside a plain dividend computation; flagging them narrows scope rather than changing a supported value."
  - key: "bad_special"
    status: MATCH
    reason: "Boxes 2b, 2c and 2d are each 'the portion of the amount in box 2a,' so testing each component (and their total) against box 2a correctly detects inconsistent amounts."
  - key: "screen"
    status: MATCH
    reason: "The $0 screen with refusals is a scope gate; each refusal names the excluded case and the form needed (Form 8949 code Q and Form 6251 for section 1202 exclusion, Form 6251 for box 13 AMT interest), consistent with the IRS text."
  - key: "bad_components"
    status: MATCH
    reason: "The IRS text makes box 1b and box 5 portions of box 1a, so testing qualified dividends and section 199A dividends against total ordinary dividends correctly detects inconsistent totals."
  - key: "special_total"
    status: MATCH
    reason: "Boxes 2b, 2c and 2d are each portions of box 2a, so summing them as the total special capital-gain components is consistent with the IRS text."
```
