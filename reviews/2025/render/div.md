# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f8e4ece5439c758a6bf5d0bda47e59665044b17b00e0a4bd91baeea7cbe925b6 |
| lines judged | 21 |
| match / mismatch / unclear / missing | 20 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: Box 2b is "Unrecap. Sec. 1250 gain", described as the portion of box 2a that is unrecaptured section 1250 gain. The input matches.

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Box 2c is "Section 1202 gain", the portion of box 2a that is section 1202 gain. The input matches.

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Box 2d is "Collectibles (28%) gain", the portion of box 2a that is 28% rate gain. The input matches.

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Box 2e is "Section 897 ordinary dividends". The input matches.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Box 2f is "Section 897 capital gain". The input matches.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Box 3 is "Nondividend distributions", which "Shows a return of capital." The input matches.

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Box 9 is "Cash liquidation distributions". The input matches.

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Box 10 is "Noncash liquidation distributions". The input matches.

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Box 13 is "Specified private activity bond interest dividends". The input matches.

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: Box 3 instructions say the distribution "reduces your basis and is not taxable" up to basis and that any excess is capital gain. A yes/no screen on whether that basis work has been done, with no excess, is consistent with this.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Box 1a "Shows total ordinary dividends". The source helper is the box 1a total.

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: Box 1b is "Qualified dividends", and Form 1040 line 3a is "Qualified dividends". The instructions refer to the Form 1040 instructions to determine this amount.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Box 2a "Shows total capital gain distributions". The source helper is that box 2a amount.

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: Box 5 shows section 199A dividends that "may be eligible" for the deduction. Taking the confirmed qualified amount narrows this within scope.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: A box 2c gain may require the section 1202 exclusion, reported with code "Q" on Form 8949, and may require an entry on Form 6251 line 13. Gating on box 2c > 0 and refusing to those forms is consistent with this.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 "Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251." Gating on box 13 > 0 matches.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: Boxes 2e/2f (section 897), boxes 9/10 (liquidation) and unreconciled box 3 basis each need treatment beyond this form. The gate flags these cases for refusal, which narrows scope consistently with the text.

### bad_special — A gain component exceeds total capital gain distributions
Status: **UNCLEAR**

Restated: (helper "Unrecaptured section 1250 gain, box 2b" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Section 1202 gain, box 2c" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Collectibles (28%) gain, box 2d" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Total special capital-gain distribution components" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a")

Model: The text supports each of boxes 2b, 2c and 2d being "the portion of the amount in box 2a", which justifies checking each one against 2a. It does not say these components are mutually exclusive, so whether their sum may exceed box 2a cannot be judged from the text given.

Ruling: project retained pending T-006. Boxes 2b, 2c and 2d are each 'the portion of the amount in box 2a'; whether the sum test (2b + 2c + 2d not more than 2a) assumes disjoint portions is the ambiguity-register candidate T-006, still undecided.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: This is a $0 placeholder computed only after the refusals. Each refusal names the excluded case and the form or treatment it needs.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Box 1b and box 5 are each described as "the portion of the amount in box 1a". Flagging either one when it exceeds box 1a matches.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: This is a plain sum of boxes 2b, 2c and 2d, consistent with its label. Whether the sum is a valid consistency test is addressed under bad_special.

## Raw response

```yaml
```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Box 2b is \"Unrecap. Sec. 1250 gain\", described as the portion of box 2a that is unrecaptured section 1250 gain. The input matches."
  - key: "box2c"
    status: MATCH
    reason: "Box 2c is \"Section 1202 gain\", the portion of box 2a that is section 1202 gain. The input matches."
  - key: "box2d"
    status: MATCH
    reason: "Box 2d is \"Collectibles (28%) gain\", the portion of box 2a that is 28% rate gain. The input matches."
  - key: "box2e"
    status: MATCH
    reason: "Box 2e is \"Section 897 ordinary dividends\". The input matches."
  - key: "box2f"
    status: MATCH
    reason: "Box 2f is \"Section 897 capital gain\". The input matches."
  - key: "box3"
    status: MATCH
    reason: "Box 3 is \"Nondividend distributions\", which \"Shows a return of capital.\" The input matches."
  - key: "box9"
    status: MATCH
    reason: "Box 9 is \"Cash liquidation distributions\". The input matches."
  - key: "box10"
    status: MATCH
    reason: "Box 10 is \"Noncash liquidation distributions\". The input matches."
  - key: "box13"
    status: MATCH
    reason: "Box 13 is \"Specified private activity bond interest dividends\". The input matches."
  - key: "basis_reconciled"
    status: MATCH
    reason: "Box 3 instructions say the distribution \"reduces your basis and is not taxable\" up to basis and that any excess is capital gain. A yes/no screen on whether that basis work has been done, with no excess, is consistent with this."
  - key: "box1a"
    status: MATCH
    reason: "Box 1a \"Shows total ordinary dividends\". The source helper is the box 1a total."
  - key: "box1b"
    status: MATCH
    reason: "Box 1b is \"Qualified dividends\", and Form 1040 line 3a is \"Qualified dividends\". The instructions refer to the Form 1040 instructions to determine this amount."
  - key: "box2a"
    status: MATCH
    reason: "Box 2a \"Shows total capital gain distributions\". The source helper is that box 2a amount."
  - key: "box5"
    status: MATCH
    reason: "Box 5 shows section 199A dividends that \"may be eligible\" for the deduction. Taking the confirmed qualified amount narrows this within scope."
  - key: "section1202"
    status: MATCH
    reason: "A box 2c gain may require the section 1202 exclusion, reported with code \"Q\" on Form 8949, and may require an entry on Form 6251 line 13. Gating on box 2c > 0 and refusing to those forms is consistent with this."
  - key: "amt"
    status: MATCH
    reason: "Box 13 \"Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.\" Gating on box 13 > 0 matches."
  - key: "unsupported"
    status: MATCH
    reason: "Boxes 2e/2f (section 897), boxes 9/10 (liquidation) and unreconciled box 3 basis each need treatment beyond this form. The gate flags these cases for refusal, which narrows scope consistently with the text."
  - key: "bad_special"
    status: UNCLEAR
    reason: "The text supports each of boxes 2b, 2c and 2d being \"the portion of the amount in box 2a\", which justifies checking each one against 2a. It does not say these components are mutually exclusive, so whether their sum may exceed box 2a cannot be judged from the text given."
  - key: "screen"
    status: MATCH
    reason: "This is a $0 placeholder computed only after the refusals. Each refusal names the excluded case and the form or treatment it needs."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b and box 5 are each described as \"the portion of the amount in box 1a\". Flagging either one when it exceeds box 1a matches."
  - key: "special_total"
    status: MATCH
    reason: "This is a plain sum of boxes 2b, 2c and 2d, consistent with its label. Whether the sum is a valid consistency test is addressed under bad_special."
```
```
