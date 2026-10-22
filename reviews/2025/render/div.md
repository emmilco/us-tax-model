# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b7a7d184024eaf4070dd8db4ecc8ec5e9333b4baa8f28be436c8a7b551d77606 |
| subject sha256 | 4ad39baafac680e2a95d81964b30abeac08ebe2d3b396d444dd8508e7f4e4924 |
| lines judged | 22 |
| match / mismatch / unclear / missing | 22 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: Direct input of box 2b, "Unrecap. Sec. 1250 gain", which the instructions describe as "the portion of the amount in box 2a that is unrecaptured section 1250 gain."

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Direct input of box 2c, "Section 1202 gain", which is "the portion of the amount in box 2a that is section 1202 gain from certain small business stock."

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Direct input of box 2d, "Collectibles (28%) gain", which is "the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles."

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Direct input of box 2e, "Section 897 ordinary dividends", as printed on the form.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Direct input of box 2f, "Section 897 capital gain", as printed on the form.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Direct input of box 3, "Nondividend distributions", which the instructions say "Shows a return of capital."

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Direct input of box 9, "Cash liquidation distributions".

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Direct input of box 10, "Noncash liquidation distributions".

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Direct input of box 12, "Exempt-interest dividends". The note that box 13 is already included agrees with the box 13 instruction "This amount is included in box 12."

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Direct input of box 13, "Specified private activity bond interest dividends".

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: This filer-supplied flag tracks the box 3 rule: "the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain." It only confirms that basis reductions were applied and no distribution exceeded basis.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Takes the Schedule B helper for "Total ordinary dividends, Form 1099-DIV box 1a", which corresponds to box 1a "Total ordinary dividends".

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: Box 1b is "the portion of the amount in box 1a that may be eligible for reduced capital gains rates", and the instructions refer to "the Instructions for Form 1040 for how to determine this amount." Form 1040 line 3a "Qualified dividends" is that determined portion, which is all the program needs for its portion-of-1a check.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Takes the Schedule D helper for capital gain distributions, generally box 2a, which corresponds to box 2a "Total capital gain distr."

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: Takes the QBI helper for box 5 "Section 199A dividends". Box 5 is "the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction."

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Tests box 2c > 0. Under the text, a box 2c gain "may be eligible for the section 1202 exclusion", is reported with code "Q" on Form 8949, and may require Form 6251 entries, all of which the refusal excludes.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Tests box 13 > 0. Box 13 "Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251", and the refusal excludes Form 6251.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: Flags boxes 2e, 2f, 9 and 10, and also box 3 when basis has not been reconciled. This matches the box 3 rule that any excess over basis "is taxable to you as capital gain" and the special treatment of 2e/2f; the refusal names what is excluded.

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: Boxes 2b, 2c and 2d are each "the portion of the amount in box 2a", so neither one nor their total may exceed box 2a. The categories describe distinct property types, which supports the total check as well.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: Enters $0 only after the scope gates pass. Each refusal names the excluded treatment (code Q/Form 6251, the AMT, section 897/liquidation/return of capital, inconsistent components), consistent with the box instructions.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Box 1b and box 5 are each described as "the portion of the amount in box 1a", so qualified dividends or section 199A dividends greater than total ordinary dividends would be inconsistent.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: Adds boxes 2b, 2c and 2d, the three printed portions of box 2a, for use in the consistency check against box 2a.

## Raw response

```yaml
```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Direct input of box 2b, \"Unrecap. Sec. 1250 gain\", which the instructions describe as \"the portion of the amount in box 2a that is unrecaptured section 1250 gain.\""
  - key: "box2c"
    status: MATCH
    reason: "Direct input of box 2c, \"Section 1202 gain\", which is \"the portion of the amount in box 2a that is section 1202 gain from certain small business stock.\""
  - key: "box2d"
    status: MATCH
    reason: "Direct input of box 2d, \"Collectibles (28%) gain\", which is \"the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles.\""
  - key: "box2e"
    status: MATCH
    reason: "Direct input of box 2e, \"Section 897 ordinary dividends\", as printed on the form."
  - key: "box2f"
    status: MATCH
    reason: "Direct input of box 2f, \"Section 897 capital gain\", as printed on the form."
  - key: "box3"
    status: MATCH
    reason: "Direct input of box 3, \"Nondividend distributions\", which the instructions say \"Shows a return of capital.\""
  - key: "box9"
    status: MATCH
    reason: "Direct input of box 9, \"Cash liquidation distributions\"."
  - key: "box10"
    status: MATCH
    reason: "Direct input of box 10, \"Noncash liquidation distributions\"."
  - key: "box12"
    status: MATCH
    reason: "Direct input of box 12, \"Exempt-interest dividends\". The note that box 13 is already included agrees with the box 13 instruction \"This amount is included in box 12.\""
  - key: "box13"
    status: MATCH
    reason: "Direct input of box 13, \"Specified private activity bond interest dividends\"."
  - key: "basis_reconciled"
    status: MATCH
    reason: "This filer-supplied flag tracks the box 3 rule: \"the distribution reduces your basis and is not taxable. Any amount received in excess of your basis is taxable to you as capital gain.\" It only confirms that basis reductions were applied and no distribution exceeded basis."
  - key: "box1a"
    status: MATCH
    reason: "Takes the Schedule B helper for \"Total ordinary dividends, Form 1099-DIV box 1a\", which corresponds to box 1a \"Total ordinary dividends\"."
  - key: "box1b"
    status: MATCH
    reason: "Box 1b is \"the portion of the amount in box 1a that may be eligible for reduced capital gains rates\", and the instructions refer to \"the Instructions for Form 1040 for how to determine this amount.\" Form 1040 line 3a \"Qualified dividends\" is that determined portion, which is all the program needs for its portion-of-1a check."
  - key: "box2a"
    status: MATCH
    reason: "Takes the Schedule D helper for capital gain distributions, generally box 2a, which corresponds to box 2a \"Total capital gain distr.\""
  - key: "box5"
    status: MATCH
    reason: "Takes the QBI helper for box 5 \"Section 199A dividends\". Box 5 is \"the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction.\""
  - key: "section1202"
    status: MATCH
    reason: "Tests box 2c > 0. Under the text, a box 2c gain \"may be eligible for the section 1202 exclusion\", is reported with code \"Q\" on Form 8949, and may require Form 6251 entries, all of which the refusal excludes."
  - key: "amt"
    status: MATCH
    reason: "Tests box 13 > 0. Box 13 \"Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251\", and the refusal excludes Form 6251."
  - key: "unsupported"
    status: MATCH
    reason: "Flags boxes 2e, 2f, 9 and 10, and also box 3 when basis has not been reconciled. This matches the box 3 rule that any excess over basis \"is taxable to you as capital gain\" and the special treatment of 2e/2f; the refusal names what is excluded."
  - key: "bad_special"
    status: MATCH
    reason: "Boxes 2b, 2c and 2d are each \"the portion of the amount in box 2a\", so neither one nor their total may exceed box 2a. The categories describe distinct property types, which supports the total check as well."
  - key: "screen"
    status: MATCH
    reason: "Enters $0 only after the scope gates pass. Each refusal names the excluded treatment (code Q/Form 6251, the AMT, section 897/liquidation/return of capital, inconsistent components), consistent with the box instructions."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b and box 5 are each described as \"the portion of the amount in box 1a\", so qualified dividends or section 199A dividends greater than total ordinary dividends would be inconsistent."
  - key: "special_total"
    status: MATCH
    reason: "Adds boxes 2b, 2c and 2d, the three printed portions of box 2a, for use in the consistency check against box 2a."
```
```
