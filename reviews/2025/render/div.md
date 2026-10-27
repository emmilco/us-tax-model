# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1778c4ca6275720af58f1a3ee8f80e2626e709f958faccda1dc7f7ab98a04116 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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

Model: The form prints box 2b as 'Unrecap. Sec. 1250 gain', and the instructions say it 'Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain.' Taking it as a filer input matches.

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: The form prints box 2c as 'Section 1202 gain', which the instructions call the 'portion of the amount in box 2a that is section 1202 gain.' Taking it as a filer input matches.

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: The form prints box 2d as 'Collectibles (28%) gain', which the instructions call the 'portion of the amount in box 2a that is 28% rate gain.' Taking it as a filer input matches.

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: The form prints box 2e as 'Section 897 ordinary dividends'. Taking it as a filer input matches.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: The form prints box 2f as 'Section 897 capital gain'. Taking it as a filer input matches.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: The form prints box 3 as 'Nondividend distributions', and the instructions say it 'Shows a return of capital.' Taking it as a filer input matches.

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: The form prints box 9 as 'Cash liquidation distributions'. Taking it as a filer input matches.

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: The form prints box 10 as 'Noncash liquidation distributions'. Taking it as a filer input matches.

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: The form prints box 12 as 'Exempt-interest dividends'. The note that box 13 is already included matches the instruction for box 13: 'This amount is included in box 12.'

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: The form prints box 13 as 'Specified private activity bond interest dividends', which the instructions describe as 'exempt-interest dividends subject to the alternative minimum tax.' Taking it as a filer input matches.

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: This is a screening input, which the IRS text supports. Box 3 instructions say the distribution 'reduces your basis and is not taxable' up to basis, and that 'Any amount received in excess of your basis is taxable to you as capital gain.' The question asks the filer to confirm that case does not arise.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: The Schedule B instructions say ordinary dividends 'should be shown in box 1a of your Forms 1099-DIV', and the form prints box 1a as 'Total ordinary dividends'. Carrying that input over matches.

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: The form prints box 1b as 'Qualified dividends', the portion of box 1a 'that may be eligible for reduced capital gains rates'. Form 1040 line 3a is 'Qualified dividends'. Using that amount for the box 1b portion check is consistent with the text.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: The form prints box 2a as 'Total capital gain distr.' Carrying the Schedule D capital gain distributions input, described as generally box 2a, matches.

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: The form prints box 5 as 'Section 199A dividends', the portion of box 1a that may be eligible for the qualified business income deduction. The Form 8995 instructions add the holding-period and payment-obligation conditions, which the qbi helper's label reflects.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: A box 2c amount above $0 triggers the section 1202 exclusion process: the Schedule D instructions require Form 8949 code 'Q' and, for the alternative minimum tax, Form 6251 line 13. The gate correctly flags this out-of-scope case.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 'Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.' Flagging any amount above $0 for Form 6251 matches.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: The gate flags any amount in boxes 2e, 2f, 9 or 10, or a box 3 amount whose basis has not been reconciled. The IRS text describes special treatment for each: section 897 character, liquidation distributions, and return of capital that reduces basis with any excess 'taxable to you as capital gain'. The refusal names these exclusions, so this is a legitimate narrowing.

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: The instructions describe each of boxes 2b, 2c and 2d as 'the portion of the amount in box 2a', so none may exceed box 2a. They name distinct categories (unrecaptured section 1250 gain, section 1202 gain, collectibles gain), so the check that their total does not exceed box 2a is consistent.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: This line enters $0 only after the scope checks pass. Each refusal matches an IRS rule: box 2c goes to Form 8949 code Q and Form 6251; box 13 is subject to the alternative minimum tax; boxes 2e, 2f, 9 and 10 and excess box 3 amounts need special treatment; and boxes 2b–2d, 1b and 5 are portions of other boxes.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Box 1b 'Shows the portion of the amount in box 1a', and box 5 'Shows the portion of the amount in box 1a'. Flagging qualified dividends or section 199A dividends that exceed box 1a matches.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: This adds boxes 2b, 2c and 2d, the separately described portions of box 2a, so the bad_special check can compare the total with box 2a. That is consistent with the text.

## Raw response

```yaml
```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "The form prints box 2b as 'Unrecap. Sec. 1250 gain', and the instructions say it 'Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain.' Taking it as a filer input matches."
  - key: "box2c"
    status: MATCH
    reason: "The form prints box 2c as 'Section 1202 gain', which the instructions call the 'portion of the amount in box 2a that is section 1202 gain.' Taking it as a filer input matches."
  - key: "box2d"
    status: MATCH
    reason: "The form prints box 2d as 'Collectibles (28%) gain', which the instructions call the 'portion of the amount in box 2a that is 28% rate gain.' Taking it as a filer input matches."
  - key: "box2e"
    status: MATCH
    reason: "The form prints box 2e as 'Section 897 ordinary dividends'. Taking it as a filer input matches."
  - key: "box2f"
    status: MATCH
    reason: "The form prints box 2f as 'Section 897 capital gain'. Taking it as a filer input matches."
  - key: "box3"
    status: MATCH
    reason: "The form prints box 3 as 'Nondividend distributions', and the instructions say it 'Shows a return of capital.' Taking it as a filer input matches."
  - key: "box9"
    status: MATCH
    reason: "The form prints box 9 as 'Cash liquidation distributions'. Taking it as a filer input matches."
  - key: "box10"
    status: MATCH
    reason: "The form prints box 10 as 'Noncash liquidation distributions'. Taking it as a filer input matches."
  - key: "box12"
    status: MATCH
    reason: "The form prints box 12 as 'Exempt-interest dividends'. The note that box 13 is already included matches the instruction for box 13: 'This amount is included in box 12.'"
  - key: "box13"
    status: MATCH
    reason: "The form prints box 13 as 'Specified private activity bond interest dividends', which the instructions describe as 'exempt-interest dividends subject to the alternative minimum tax.' Taking it as a filer input matches."
  - key: "basis_reconciled"
    status: MATCH
    reason: "This is a screening input, which the IRS text supports. Box 3 instructions say the distribution 'reduces your basis and is not taxable' up to basis, and that 'Any amount received in excess of your basis is taxable to you as capital gain.' The question asks the filer to confirm that case does not arise."
  - key: "box1a"
    status: MATCH
    reason: "The Schedule B instructions say ordinary dividends 'should be shown in box 1a of your Forms 1099-DIV', and the form prints box 1a as 'Total ordinary dividends'. Carrying that input over matches."
  - key: "box1b"
    status: MATCH
    reason: "The form prints box 1b as 'Qualified dividends', the portion of box 1a 'that may be eligible for reduced capital gains rates'. Form 1040 line 3a is 'Qualified dividends'. Using that amount for the box 1b portion check is consistent with the text."
  - key: "box2a"
    status: MATCH
    reason: "The form prints box 2a as 'Total capital gain distr.' Carrying the Schedule D capital gain distributions input, described as generally box 2a, matches."
  - key: "box5"
    status: MATCH
    reason: "The form prints box 5 as 'Section 199A dividends', the portion of box 1a that may be eligible for the qualified business income deduction. The Form 8995 instructions add the holding-period and payment-obligation conditions, which the qbi helper's label reflects."
  - key: "section1202"
    status: MATCH
    reason: "A box 2c amount above $0 triggers the section 1202 exclusion process: the Schedule D instructions require Form 8949 code 'Q' and, for the alternative minimum tax, Form 6251 line 13. The gate correctly flags this out-of-scope case."
  - key: "amt"
    status: MATCH
    reason: "Box 13 'Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.' Flagging any amount above $0 for Form 6251 matches."
  - key: "unsupported"
    status: MATCH
    reason: "The gate flags any amount in boxes 2e, 2f, 9 or 10, or a box 3 amount whose basis has not been reconciled. The IRS text describes special treatment for each: section 897 character, liquidation distributions, and return of capital that reduces basis with any excess 'taxable to you as capital gain'. The refusal names these exclusions, so this is a legitimate narrowing."
  - key: "bad_special"
    status: MATCH
    reason: "The instructions describe each of boxes 2b, 2c and 2d as 'the portion of the amount in box 2a', so none may exceed box 2a. They name distinct categories (unrecaptured section 1250 gain, section 1202 gain, collectibles gain), so the check that their total does not exceed box 2a is consistent."
  - key: "screen"
    status: MATCH
    reason: "This line enters $0 only after the scope checks pass. Each refusal matches an IRS rule: box 2c goes to Form 8949 code Q and Form 6251; box 13 is subject to the alternative minimum tax; boxes 2e, 2f, 9 and 10 and excess box 3 amounts need special treatment; and boxes 2b–2d, 1b and 5 are portions of other boxes."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b 'Shows the portion of the amount in box 1a', and box 5 'Shows the portion of the amount in box 1a'. Flagging qualified dividends or section 199A dividends that exceed box 1a matches."
  - key: "special_total"
    status: MATCH
    reason: "This adds boxes 2b, 2c and 2d, the separately described portions of box 2a, so the bad_special check can compare the total with box 2a. That is consistent with the text."
```
```
