# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c6afe58fc01dd8a5d44a0d27a7b33c56185fa883872628eeb67919411fd88bdc |
| lines judged | 5 |
| match / mismatch / unclear / missing | 4 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees, 
Status: **MATCH**

Model: This matches the instructions' 'amount of your deduction', which means 'your deduction before applying any income limits' after making 'any required reductions'. For a group of similar items, it counts 'all items in the group, even if items in the group were donated to more than one donee organization.'

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: This is a filer-supplied flag for the securities exception. Section A item 2.a–2.d lets securities stay in Section A even when the claimed value is over $5,000. Item 2.d covers 'certain other securities' under Regs. 1.170A-13(c)(7)(xi)(B), so the filer must read this flag broadly enough to include them.

### special — Does this group need an appraisal or other special treatment (including vehicles, pass-thr
Status: **MATCH**

Model: This is a filer-supplied flag for the categories the text treats specially. These are vehicles, intellectual property, inventory, pass-through entity gifts, qualified conservation contributions and partial interests or restricted use property.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: This matches its label and the text's general rule: 'Use Section B to report donations of property for which you claimed a deduction of more than $5,000 per item or group of similar items.' It also applies the securities exception from Section A item 2. The other Section A exceptions are handled by the separate special gate.

### allowed — Amount from gift.deduction
Status: **MISMATCH**

Restated: Enter the amount from helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions".

Model: Copying the deduction amount is correct. However, no refusal covers a case the text sends to Section B below $5,000: 'You must file Form 8283, Section B, if you are contributing a single article of clothing or household item that is not in good used condition or better and for which you are claiming a deduction of over $500.' The program would go ahead in that case without naming the exclusion.

Ruling: second reading right; data changed under BUG-0010. Form 8283 Section B is also required for "a single article of clothing or household item that is not in good used condition or better and for which you are claiming a deduction of over $500" (i8283 p. 3); the screen `gift.special` did not name that case. It now does, so such an item is refused; the line itself is unchanged.

## Raw response

```yaml
```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "This matches the instructions' 'amount of your deduction', which means 'your deduction before applying any income limits' after making 'any required reductions'. For a group of similar items, it counts 'all items in the group, even if items in the group were donated to more than one donee organization.'"
  - key: "public_securities"
    status: MATCH
    reason: "This is a filer-supplied flag for the securities exception. Section A item 2.a–2.d lets securities stay in Section A even when the claimed value is over $5,000. Item 2.d covers 'certain other securities' under Regs. 1.170A-13(c)(7)(xi)(B), so the filer must read this flag broadly enough to include them."
  - key: "special"
    status: MATCH
    reason: "This is a filer-supplied flag for the categories the text treats specially. These are vehicles, intellectual property, inventory, pass-through entity gifts, qualified conservation contributions and partial interests or restricted use property."
  - key: "section_b"
    status: MATCH
    reason: "This matches its label and the text's general rule: 'Use Section B to report donations of property for which you claimed a deduction of more than $5,000 per item or group of similar items.' It also applies the securities exception from Section A item 2. The other Section A exceptions are handled by the separate special gate."
  - key: "allowed"
    status: MISMATCH
    reason: "Copying the deduction amount is correct. However, no refusal covers a case the text sends to Section B below $5,000: 'You must file Form 8283, Section B, if you are contributing a single article of clothing or household item that is not in good used condition or better and for which you are claiming a deduction of over $500.' The program would go ahead in that case without naming the exclusion."
```
```
