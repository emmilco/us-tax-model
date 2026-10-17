# Render comparison — div

The rendered English of every printed line of `Form 1099-DIV — distribution components and scope screening` (`rendered/2025/div.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 92cb22176c48c40f06218decb812733dac7dba7f0c7892816a50e161a8e74c99 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 23 / 0 / 2 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | bfaac0e73b8640fe9cb209f96905d33fc22bf29f3aec472330d0132cda9cc329 |
| i1040sd | 2025; printed date 2025-12-11 | 8 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 8 | ac7a0c9cbb9e635491b2505e7d04cea3381b892402408ddc97f8d49d80a6640b |

## Lines

### box2b — Unrecaptured section 1250 gain, box 2b
Status: **MATCH**

Model: Box 2b is entered as supplied. The form calls it "Unrecap. Sec. 1250 gain", the portion of box 2a that is unrecaptured section 1250 gain.

### box2c — Section 1202 gain, box 2c
Status: **MATCH**

Model: Box 2c "Section 1202 gain" is entered as supplied.

### box2d — Collectibles (28%) gain, box 2d
Status: **MATCH**

Model: Box 2d "Collectibles (28%) gain" is entered as supplied.

### box2e — Section 897 ordinary dividends, box 2e
Status: **MATCH**

Model: Box 2e "Section 897 ordinary dividends" is entered as supplied.

### box2f — Section 897 capital gain, box 2f
Status: **MATCH**

Model: Box 2f "Section 897 capital gain" is entered as supplied.

### box3 — Nondividend distributions/return of capital, box 3
Status: **MATCH**

Model: Box 3 "Nondividend distributions" is entered as supplied. The instructions say box 3 "Shows a return of capital."

### box4 — Federal income tax withheld, box 4
Status: **MATCH**

Model: Box 4 "Federal income tax withheld" is entered as supplied. The instructions say it shows backup withholding.

### box6 — Investment expenses already included in box 1a, box 6
Status: **MATCH**

Model: Box 6 "Investment expenses" is entered as supplied. The instructions say "This amount is included in box 1a."

### box9 — Cash liquidation distributions, box 9
Status: **MATCH**

Model: Box 9 "Cash liquidation distributions" is entered as supplied.

### box10 — Noncash liquidation distributions, box 10
Status: **MATCH**

Model: Box 10 "Noncash liquidation distributions" is entered as supplied.

### box12 — Exempt-interest dividends, box 12
Status: **MATCH**

Model: Box 12 "Exempt-interest dividends" is entered as supplied.

### box13 — Specified private activity bond interest dividends, box 13
Status: **MATCH**

Model: Box 13 "Specified private activity bond interest dividends" is entered as supplied.

### basis_reconciled — For box 3, have basis reductions been applied to records with no distribution exceeding ba
Status: **MATCH**

Model: The box 3 instructions say the distribution "reduces your basis and is not taxable" up to basis, and any excess "is taxable to you as capital gain". A yes/no input confirming that reconciliation fits that text.

### fatca — Is the FATCA reporting checkbox checked? Review Form 8938 requirements separately.
Status: **MATCH**

Model: The box 11 checkbox is entered as supplied. The instructions say "You may also have a filing requirement. See the Instructions for Form 8938," which matches the label's note to review Form 8938 separately.

### box1a — Amount from sb.ordinary_dividends
Status: **MATCH**

Model: Box 1a "Total ordinary dividends" is taken from the Schedule B input labeled as Form 1099-DIV box 1a.

### box1b — Amount from f1040.line3a
Status: **UNCLEAR**

Restated: Enter the amount from f1040 line 3a.

Model: Box 1b is the amount the payer reports as qualified dividends that "may be eligible". The program uses Form 1040 line 3a instead, which is the amount the filer determines per "the Instructions for Form 1040 for how to determine this amount". Those instructions are not in the text given, so I can't confirm the two amounts are the same.

Ruling: representation; project retained. Form 1040 line 3a is the filer's qualified dividends, which are 'generally ... shown in box 1b of Form(s) 1099-DIV' (i1040gi p. 25, line 3a). The line is the input the filer answers and the box is rendered as that amount; within the slice they are the same figure. No change to the data.

### box2a — Amount from sd.distributions
Status: **MATCH**

Model: Box 2a "Total capital gain distr." is taken from the Schedule D input labeled as generally Form 1099-DIV box 2a.

### box5 — Amount from qbi.dividends
Status: **UNCLEAR**

Restated: Enter the amount from qbi helper "Qualified section 199A dividends from Form 1099-DIV box 5 after confirming holding-period and related-payment requirements".

Model: Box 5 shows the portion of box 1a that "may be eligible" for the section 199A deduction. The program takes the QBI value after confirming holding-period requirements, which may be smaller than the box. The Form 8995/8995-A instructions that would define that value are not in the text given.

Ruling: representation; project retained. Box 5 is the section 199A dividend amount that 'may be eligible'; `qbi.dividends` is the amount the filer confirms eligible after the holding-period and related-payment requirements of the Form 8995 instructions, which is what Form 8995 line 6 takes. The box is rendered from that input so the eligibility screen is the filer's own answer. No change to the data.

### section1202 — Section 1202 distribution present
Status: **MATCH**

Model: A box 2c amount above $0 triggers a refusal. The text says box 2c gain "may be subject to an exclusion", is reported with code "Q" on Form 8949, and may require AMT entries on Form 6251. The refusal names those excluded cases.

### amt — Specified private activity bond dividends present
Status: **MATCH**

Model: A box 13 amount above $0 triggers a refusal. The text says box 13 "Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251."

### unsupported — Unsupported section 897, liquidation or unreconciled basis/excess distribution
Status: **MATCH**

Model: The program refuses section 897 amounts (boxes 2e/2f), liquidation distributions (boxes 9/10), and box 3 amounts whose basis has not been reconciled. The text gives each of these special treatment ("Any amount received in excess of your basis is taxable to you as capital gain"), and the refusal names them.

### bad_special — A gain component exceeds total capital gain distributions
Status: **MATCH**

Model: The text says boxes 2b, 2c and 2d each show "the portion of the amount in box 2a", so any one of them above box 2a is inconsistent. The check on their combined total also assumes the three categories don't overlap, which the text implies but never states. Box 2f is not checked here, but it already triggers the unsupported refusal.

### screen — Zero only after distribution scope checks
Status: **MATCH**

Model: The program enters $0 only after all the scope refusals, and each refusal names what is excluded. This is a permitted narrowing.

### bad_components — Qualified or section 199A dividends exceed ordinary dividends
Status: **MATCH**

Model: The text says box 1b shows "the portion of the amount in box 1a" and box 5 shows "the portion of the amount in box 1a". Flagging either one above box 1a is consistent with that.

### special_total — Total special capital-gain distribution components
Status: **MATCH**

Model: This is the sum of boxes 2b, 2c and 2d, each a portion of box 2a. It is used only for the consistency check against box 2a.

## Raw response

```yaml
```yaml
lines:
  - key: "box2b"
    status: MATCH
    reason: "Box 2b is entered as supplied. The form calls it \"Unrecap. Sec. 1250 gain\", the portion of box 2a that is unrecaptured section 1250 gain."
  - key: "box2c"
    status: MATCH
    reason: "Box 2c \"Section 1202 gain\" is entered as supplied."
  - key: "box2d"
    status: MATCH
    reason: "Box 2d \"Collectibles (28%) gain\" is entered as supplied."
  - key: "box2e"
    status: MATCH
    reason: "Box 2e \"Section 897 ordinary dividends\" is entered as supplied."
  - key: "box2f"
    status: MATCH
    reason: "Box 2f \"Section 897 capital gain\" is entered as supplied."
  - key: "box3"
    status: MATCH
    reason: "Box 3 \"Nondividend distributions\" is entered as supplied. The instructions say box 3 \"Shows a return of capital.\""
  - key: "box4"
    status: MATCH
    reason: "Box 4 \"Federal income tax withheld\" is entered as supplied. The instructions say it shows backup withholding."
  - key: "box6"
    status: MATCH
    reason: "Box 6 \"Investment expenses\" is entered as supplied. The instructions say \"This amount is included in box 1a.\""
  - key: "box9"
    status: MATCH
    reason: "Box 9 \"Cash liquidation distributions\" is entered as supplied."
  - key: "box10"
    status: MATCH
    reason: "Box 10 \"Noncash liquidation distributions\" is entered as supplied."
  - key: "box12"
    status: MATCH
    reason: "Box 12 \"Exempt-interest dividends\" is entered as supplied."
  - key: "box13"
    status: MATCH
    reason: "Box 13 \"Specified private activity bond interest dividends\" is entered as supplied."
  - key: "basis_reconciled"
    status: MATCH
    reason: "The box 3 instructions say the distribution \"reduces your basis and is not taxable\" up to basis, and any excess \"is taxable to you as capital gain\". A yes/no input confirming that reconciliation fits that text."
  - key: "fatca"
    status: MATCH
    reason: "The box 11 checkbox is entered as supplied. The instructions say \"You may also have a filing requirement. See the Instructions for Form 8938,\" which matches the label's note to review Form 8938 separately."
  - key: "box1a"
    status: MATCH
    reason: "Box 1a \"Total ordinary dividends\" is taken from the Schedule B input labeled as Form 1099-DIV box 1a."
  - key: "box1b"
    status: UNCLEAR
    reason: "Box 1b is the amount the payer reports as qualified dividends that \"may be eligible\". The program uses Form 1040 line 3a instead, which is the amount the filer determines per \"the Instructions for Form 1040 for how to determine this amount\". Those instructions are not in the text given, so I can't confirm the two amounts are the same."
  - key: "box2a"
    status: MATCH
    reason: "Box 2a \"Total capital gain distr.\" is taken from the Schedule D input labeled as generally Form 1099-DIV box 2a."
  - key: "box5"
    status: UNCLEAR
    reason: "Box 5 shows the portion of box 1a that \"may be eligible\" for the section 199A deduction. The program takes the QBI value after confirming holding-period requirements, which may be smaller than the box. The Form 8995/8995-A instructions that would define that value are not in the text given."
  - key: "section1202"
    status: MATCH
    reason: "A box 2c amount above $0 triggers a refusal. The text says box 2c gain \"may be subject to an exclusion\", is reported with code \"Q\" on Form 8949, and may require AMT entries on Form 6251. The refusal names those excluded cases."
  - key: "amt"
    status: MATCH
    reason: "A box 13 amount above $0 triggers a refusal. The text says box 13 \"Shows exempt-interest dividends subject to the alternative minimum tax... See the Instructions for Form 6251.\""
  - key: "unsupported"
    status: MATCH
    reason: "The program refuses section 897 amounts (boxes 2e/2f), liquidation distributions (boxes 9/10), and box 3 amounts whose basis has not been reconciled. The text gives each of these special treatment (\"Any amount received in excess of your basis is taxable to you as capital gain\"), and the refusal names them."
  - key: "bad_special"
    status: MATCH
    reason: "The text says boxes 2b, 2c and 2d each show \"the portion of the amount in box 2a\", so any one of them above box 2a is inconsistent. The check on their combined total also assumes the three categories don't overlap, which the text implies but never states. Box 2f is not checked here, but it already triggers the unsupported refusal."
  - key: "screen"
    status: MATCH
    reason: "The program enters $0 only after all the scope refusals, and each refusal names what is excluded. This is a permitted narrowing."
  - key: "bad_components"
    status: MATCH
    reason: "The text says box 1b shows \"the portion of the amount in box 1a\" and box 5 shows \"the portion of the amount in box 1a\". Flagging either one above box 1a is consistent with that."
  - key: "special_total"
    status: MATCH
    reason: "This is the sum of boxes 2b, 2c and 2d, each a portion of box 2a. It is used only for the consistency check against box 2a."
```
```
