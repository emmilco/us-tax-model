# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 92cb22176c48c40f06218decb812733dac7dba7f0c7892816a50e161a8e74c99 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 22 / 0 / 3 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: The filer enters box 2b directly, and the form labels it "Unrecap. Sec. 1250 gain".

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: The filer enters box 2c directly, and the form labels it "Section 1202 gain".

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: The filer enters box 2d directly, and the form labels it "Collectibles (28%) gain".

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: The filer enters box 2e directly, and the form labels it "Section 897 ordinary dividends".

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: The filer enters box 2f directly, and the form labels it "Section 897 capital gain".

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: The form labels box 3 "Nondividend distributions", and the instructions say it "Shows a return of capital."

### box4 — Federal income tax withheld, box 4
Status: **MATCH**

Model: The filer enters box 4 directly, and the form labels it "Federal income tax withheld". The instructions say it shows backup withholding to be included as tax withheld.

### box6 — Investment expenses already included in box 1a, box 6
Status: **MATCH**

Model: The box 6 instructions say "This amount is included in box 1a." That matches the label.

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: The filer enters box 9 directly, and the form labels it "Cash liquidation distributions".

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: The filer enters box 10 directly, and the form labels it "Noncash liquidation distributions".

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: The filer enters box 12 directly, and the form labels it "Exempt-interest dividends".

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: The filer enters box 13 directly, and the form labels it "Specified private activity bond interest dividends".

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: The box 3 instructions say the distribution "reduces your basis" up to basis and that "Any amount received in excess of your basis is taxable to you as capital gain." The question screens for exactly that reconciliation.

### fatca — Is the FATCA reporting checkbox checked? Review Form 8938 requirements separately.
Status: **MATCH**

Model: The box 11 instructions say "You may also have a filing requirement. See the Instructions for Form 8938." This matches deferring Form 8938 review to the filer.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: The value comes from the Schedule B input described as Form 1099-DIV box 1a, "Total ordinary dividends".

### box1b — Amount from f1040.line3a
Status: **UNCLEAR**

Restated: Enter the amount from f1040 line 3a.

Model: Box 1b "Shows the portion of the amount in box 1a that may be eligible", and the box 1b instructions point to "the Instructions for Form 1040 for how to determine this amount". Those instructions aren't provided, so I can't confirm that Form 1040 line 3a always equals box 1b.

Ruling: representation; project retained. Form 1040 line 3a is the filer's qualified dividends, which are 'generally ... shown in box 1b of Form(s) 1099-DIV' (i1040gi p. 25, line 3a). The line is the input the filer answers and the box is rendered as that amount; within the slice they are the same figure. No change to the data.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: The value comes from the Schedule D input described as Form 1099-DIV box 2a, "Total capital gain distr."

### box5 — Amount from qbi.dividends
Status: **UNCLEAR**

Restated: Enter the amount from qbi helper "Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements".

Model: Box 5 shows the portion of box 1a that "may be eligible" for the section 199A deduction. The source helper is box 5 "after confirming holding-period and related-payment requirements", and the Form 8995/8995-A instructions that would show whether that changes the amount aren't provided.

Ruling: representation; project retained. Box 5 is the section 199A dividend amount that 'may be eligible'; `qbi.dividends` is the amount the filer confirms eligible after the holding-period and related-payment requirements of the Form 8995 instructions, which is what Form 8995 line 6 takes. The box is rendered from that input so the eligibility screen is the filer's own answer. No change to the data.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Box 2c gain "may be subject to an exclusion". The Schedule D instructions route it to Form 8949 code "Q" and Form 6251 line 13, which the refusal names.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Box 13 "Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251". The refusal names that form.

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: This flags boxes 2e and 2f (section 897), boxes 9 and 10 (liquidation distributions) and box 3 when basis hasn't been reconciled. The box 3 instructions say excess over basis "is taxable to you as capital gain", which the refusal names.

### bad_special — A gain component exceeds total capital gain distributions
Status: **UNCLEAR**

Restated: (helper "Unrecaptured section 1250 gain, box 2b" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Section 1202 gain, box 2c" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Collectibles (28%) gain, box 2d" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Total special capital-gain distribution components" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a")

Model: The text says boxes 2b, 2c and 2d are each "the portion of the amount in box 2a", which supports the checks on each box alone. It doesn't say the three boxes never overlap, so the rule that their sum can't exceed box 2a can't be confirmed.

Ruling: project retained pending T-006. Boxes 2b, 2c and 2d are each 'the portion of the amount in box 2a'; whether the sum test (2b + 2c + 2d not more than 2a) assumes disjoint portions is the ambiguity-register candidate T-006, still undecided.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: This enters $0 only when no refusal applies. Each refusal matches a case the text sends elsewhere: Form 8949 code Q and Form 6251 for box 2c, Form 6251 for box 13, section 897, liquidation and return-of-capital treatment, and amounts that should be portions of a total.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Box 1b and box 5 are each described as "the portion of the amount in box 1a", so flagging either one when it exceeds ordinary dividends is consistent with the text.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: This adds boxes 2b, 2c and 2d, as its label says. Each box is described as a portion of box 2a.

## Raw response

```yaml
```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "The filer enters box 2b directly, and the form labels it \"Unrecap. Sec. 1250 gain\"."
  - key: "box2c"
    status: MATCH
    reason: "The filer enters box 2c directly, and the form labels it \"Section 1202 gain\"."
  - key: "box2d"
    status: MATCH
    reason: "The filer enters box 2d directly, and the form labels it \"Collectibles (28%) gain\"."
  - key: "box2e"
    status: MATCH
    reason: "The filer enters box 2e directly, and the form labels it \"Section 897 ordinary dividends\"."
  - key: "box2f"
    status: MATCH
    reason: "The filer enters box 2f directly, and the form labels it \"Section 897 capital gain\"."
  - key: "box3"
    status: MATCH
    reason: "The form labels box 3 \"Nondividend distributions\", and the instructions say it \"Shows a return of capital.\""
  - key: "box4"
    status: MATCH
    reason: "The filer enters box 4 directly, and the form labels it \"Federal income tax withheld\". The instructions say it shows backup withholding to be included as tax withheld."
  - key: "box6"
    status: MATCH
    reason: "The box 6 instructions say \"This amount is included in box 1a.\" That matches the label."
  - key: "box9"
    status: MATCH
    reason: "The filer enters box 9 directly, and the form labels it \"Cash liquidation distributions\"."
  - key: "box10"
    status: MATCH
    reason: "The filer enters box 10 directly, and the form labels it \"Noncash liquidation distributions\"."
  - key: "box12"
    status: MATCH
    reason: "The filer enters box 12 directly, and the form labels it \"Exempt-interest dividends\"."
  - key: "box13"
    status: MATCH
    reason: "The filer enters box 13 directly, and the form labels it \"Specified private activity bond interest dividends\"."
  - key: "basis_reconciled"
    status: MATCH
    reason: "The box 3 instructions say the distribution \"reduces your basis\" up to basis and that \"Any amount received in excess of your basis is taxable to you as capital gain.\" The question screens for exactly that reconciliation."
  - key: "fatca"
    status: MATCH
    reason: "The box 11 instructions say \"You may also have a filing requirement. See the Instructions for Form 8938.\" This matches deferring Form 8938 review to the filer."
  - key: "box1a"
    status: MATCH
    reason: "The value comes from the Schedule B input described as Form 1099-DIV box 1a, \"Total ordinary dividends\"."
  - key: "box1b"
    status: UNCLEAR
    reason: "Box 1b \"Shows the portion of the amount in box 1a that may be eligible\", and the box 1b instructions point to \"the Instructions for Form 1040 for how to determine this amount\". Those instructions aren't provided, so I can't confirm that Form 1040 line 3a always equals box 1b."
  - key: "box2a"
    status: MATCH
    reason: "The value comes from the Schedule D input described as Form 1099-DIV box 2a, \"Total capital gain distr.\""
  - key: "box5"
    status: UNCLEAR
    reason: "Box 5 shows the portion of box 1a that \"may be eligible\" for the section 199A deduction. The source helper is box 5 \"after confirming holding-period and related-payment requirements\", and the Form 8995/8995-A instructions that would show whether that changes the amount aren't provided."
  - key: "section1202"
    status: MATCH
    reason: "Box 2c gain \"may be subject to an exclusion\". The Schedule D instructions route it to Form 8949 code \"Q\" and Form 6251 line 13, which the refusal names."
  - key: "amt"
    status: MATCH
    reason: "Box 13 \"Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251\". The refusal names that form."
  - key: "unsupported"
    status: MATCH
    reason: "This flags boxes 2e and 2f (section 897), boxes 9 and 10 (liquidation distributions) and box 3 when basis hasn't been reconciled. The box 3 instructions say excess over basis \"is taxable to you as capital gain\", which the refusal names."
  - key: "bad_special"
    status: UNCLEAR
    reason: "The text says boxes 2b, 2c and 2d are each \"the portion of the amount in box 2a\", which supports the checks on each box alone. It doesn't say the three boxes never overlap, so the rule that their sum can't exceed box 2a can't be confirmed."
  - key: "screen"
    status: MATCH
    reason: "This enters $0 only when no refusal applies. Each refusal matches a case the text sends elsewhere: Form 8949 code Q and Form 6251 for box 2c, Form 6251 for box 13, section 897, liquidation and return-of-capital treatment, and amounts that should be portions of a total."
  - key: "bad_components"
    status: MATCH
    reason: "Box 1b and box 5 are each described as \"the portion of the amount in box 1a\", so flagging either one when it exceeds ordinary dividends is consistent with the text."
  - key: "special_total"
    status: MATCH
    reason: "This adds boxes 2b, 2c and 2d, as its label says. Each box is described as a portion of box 2a."
```
```
