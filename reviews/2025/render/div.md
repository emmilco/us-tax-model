# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 85c337cb13d3ca1d752e94663e04cc28dc978eca7733ce379634655243a6a199 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 24 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: Direct input of box 2b, which the text describes as 'the portion of the amount in box 2a that is unrecaptured section 1250 gain.'

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Direct input of box 2c, 'the portion of the amount in box 2a that is section 1202 gain.'

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Direct input of box 2d, 'the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles.'

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Direct input of box 2e, 'Section 897 ordinary dividends.'

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Direct input of box 2f, 'Section 897 capital gain.'

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Direct input of box 3, which 'Shows a return of capital.'

### box4 — Federal income tax withheld, box 4
Status: **MATCH**

Model: Direct input of box 4, 'Federal income tax withheld'. The instructions say to include it 'as tax withheld.'

### box6 — Investment expenses already included in box 1a, box 6
Status: **MATCH**

Model: Direct input of box 6. The label's claim that it is already in box 1a matches the text: 'This amount is included in box 1a.'

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Direct input of box 9, 'Cash liquidation distributions.'

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Direct input of box 10, 'Noncash liquidation distributions.'

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Direct input of box 12, 'Exempt-interest dividends.'

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Direct input of box 13, 'Specified private activity bond interest dividends.'

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: This filer attestation reflects the box 3 instruction that the distribution 'reduces your basis and is not taxable' to the extent of basis, with 'Any amount received in excess of your basis' taxable as capital gain.

### fatca — Is the FATCA reporting checkbox checked? Review Form 8938 requirements separately.
Status: **MATCH**

Model: Matches box 11: if checked, 'You may also have a filing requirement. See the Instructions for Form 8938.'

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Takes the supplied total of box 1a, 'Total ordinary dividends.'

### box1b — Amount from f1040.line3a
Status: **MATCH**

Model: Box 1b is 'Qualified dividends' and the text says 'See the Instructions for Form 1040 for how to determine this amount.' Using the determined Form 1040 line 3a amount is a labeled narrowing and is consistent with box 1b being a portion of box 1a.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Takes the supplied capital gain distributions, which the text calls box 2a, 'Total capital gain distr.'

### box5 — Amount from qbi.dividends
Status: **MATCH**

Model: Box 5 'Shows the portion of the amount in box 1a that may be eligible' for the section 199A deduction. Taking the amount after eligibility confirmation is a labeled narrowing.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: Gates on box 2c > 0. The text says such gain 'may be subject to an exclusion', with code 'Q' on Form 8949 and AMT entry on 'line 13 of Form 6251', and the refusal names both.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: Gates on box 13 > 0. The text says box 13 'Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.'

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: Refuses on any box 2e, 2f, 9 or 10 amount, or on box 3 when basis is unreconciled. This narrows to supported cases, and the refusal names the excluded section 897, liquidation and return-of-capital treatment ('reduces your basis', excess 'taxable to you as capital gain').

### bad_special — A gain component exceeds total capital gain distributions
Status: **UNCLEAR**

Restated: (helper "Unrecaptured section 1250 gain, box 2b" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Section 1202 gain, box 2c" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Collectibles (28%) gain, box 2d" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a" or helper "Total special capital-gain distribution components" > sd helper "Capital gain distributions, generally Form 1099-DIV box 2a")

Model: The text supports each of 2b, 2c and 2d being no more than 2a, since each is 'the portion of the amount in box 2a'. However, it never says these portions are mutually exclusive, so the check that their sum must not exceed 2a cannot be confirmed from the text.

Ruling: representation; project retained, with a recorded reservation. Boxes 2b, 2c and 2d are each "the portion of the amount in box 2a" (i1099div p. 4), which supports the per-box test. The further test that their sum not exceed box 2a assumes the portions are disjoint; the text does not say so, though unrecaptured section 1250 gain, section 1202 gain and collectibles gain are gains on different property. Where that assumption fails the gate refuses rather than computes, which is the safe direction. Recorded: the sum test is a candidate for the ambiguity register. No change to the data.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: Enters $0 only after the scope refusals. Each refusal's stated rationale is supported, e.g. 2b–2d are 'portion[s] of the amount in box 2a', and boxes 1b and 5 are 'the portion of the amount in box 1a.'

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: Boxes 1b and 5 each show 'the portion of the amount in box 1a', so qualified dividends or section 199A dividends exceeding ordinary dividends is inconsistent.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: Simple sum of boxes 2b, 2c and 2d, as labeled. Whether that sum is a meaningful bound is addressed under bad_special.

## Raw response

```yaml
```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Direct input of box 2b, which the text describes as 'the portion of the amount in box 2a that is unrecaptured section 1250 gain.'"
  - key: "box2c"
    status: MATCH
    reason: "Direct input of box 2c, 'the portion of the amount in box 2a that is section 1202 gain.'"
  - key: "box2d"
    status: MATCH
    reason: "Direct input of box 2d, 'the portion of the amount in box 2a that is 28% rate gain from sales or exchanges of collectibles.'"
  - key: "box2e"
    status: MATCH
    reason: "Direct input of box 2e, 'Section 897 ordinary dividends.'"
  - key: "box2f"
    status: MATCH
    reason: "Direct input of box 2f, 'Section 897 capital gain.'"
  - key: "box3"
    status: MATCH
    reason: "Direct input of box 3, which 'Shows a return of capital.'"
  - key: "box4"
    status: MATCH
    reason: "Direct input of box 4, 'Federal income tax withheld'. The instructions say to include it 'as tax withheld.'"
  - key: "box6"
    status: MATCH
    reason: "Direct input of box 6. The label's claim that it is already in box 1a matches the text: 'This amount is included in box 1a.'"
  - key: "box9"
    status: MATCH
    reason: "Direct input of box 9, 'Cash liquidation distributions.'"
  - key: "box10"
    status: MATCH
    reason: "Direct input of box 10, 'Noncash liquidation distributions.'"
  - key: "box12"
    status: MATCH
    reason: "Direct input of box 12, 'Exempt-interest dividends.'"
  - key: "box13"
    status: MATCH
    reason: "Direct input of box 13, 'Specified private activity bond interest dividends.'"
  - key: "basis_reconciled"
    status: MATCH
    reason: "This filer attestation reflects the box 3 instruction that the distribution 'reduces your basis and is not taxable' to the extent of basis, with 'Any amount received in excess of your basis' taxable as capital gain."
  - key: "fatca"
    status: MATCH
    reason: "Matches box 11: if checked, 'You may also have a filing requirement. See the Instructions for Form 8938.'"
  - key: "box1a"
    status: MATCH
    reason: "Takes the supplied total of box 1a, 'Total ordinary dividends.'"
  - key: "box1b"
    status: MATCH
    reason: "Box 1b is 'Qualified dividends' and the text says 'See the Instructions for Form 1040 for how to determine this amount.' Using the determined Form 1040 line 3a amount is a labeled narrowing and is consistent with box 1b being a portion of box 1a."
  - key: "box2a"
    status: MATCH
    reason: "Takes the supplied capital gain distributions, which the text calls box 2a, 'Total capital gain distr.'"
  - key: "box5"
    status: MATCH
    reason: "Box 5 'Shows the portion of the amount in box 1a that may be eligible' for the section 199A deduction. Taking the amount after eligibility confirmation is a labeled narrowing."
  - key: "section1202"
    status: MATCH
    reason: "Gates on box 2c > 0. The text says such gain 'may be subject to an exclusion', with code 'Q' on Form 8949 and AMT entry on 'line 13 of Form 6251', and the refusal names both."
  - key: "amt"
    status: MATCH
    reason: "Gates on box 13 > 0. The text says box 13 'Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.'"
  - key: "unsupported"
    status: MATCH
    reason: "Refuses on any box 2e, 2f, 9 or 10 amount, or on box 3 when basis is unreconciled. This narrows to supported cases, and the refusal names the excluded section 897, liquidation and return-of-capital treatment ('reduces your basis', excess 'taxable to you as capital gain')."
  - key: "bad_special"
    status: UNCLEAR
    reason: "The text supports each of 2b, 2c and 2d being no more than 2a, since each is 'the portion of the amount in box 2a'. However, it never says these portions are mutually exclusive, so the check that their sum must not exceed 2a cannot be confirmed from the text."
  - key: "screen"
    status: MATCH
    reason: "Enters $0 only after the scope refusals. Each refusal's stated rationale is supported, e.g. 2b–2d are 'portion[s] of the amount in box 2a', and boxes 1b and 5 are 'the portion of the amount in box 1a.'"
  - key: "bad_components"
    status: MATCH
    reason: "Boxes 1b and 5 each show 'the portion of the amount in box 1a', so qualified dividends or section 199A dividends exceeding ordinary dividends is inconsistent."
  - key: "special_total"
    status: MATCH
    reason: "Simple sum of boxes 2b, 2c and 2d, as labeled. Whether that sum is a meaningful bound is addressed under bad_special."
```
```
