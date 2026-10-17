# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-16 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | bc0aee5c36193c49642480fd885e817beb1d66f7095d0613a81c88f41f9a3d0b |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad |

## Lines

### gift.allowed — Amount from gift.deduction
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: gift.allowed
    printed: "(helper)"
    label: "Amount from gift.deduction"
    type: NonNegDollars
    expr: {op: copy, from: gift.deduction}
    note: "Open point: Form 8283 does not figure the deduction. The instructions say 'do not use Form 8283 to figure your charitable contribution deduction' and point to the return instructions and Pub. 526. So this line only carries forward the deduction before income limits, after the required reductions, as supplied in gift.deduction. Choice made: no further reduction is applied on this form."
  - id: gift.h_over5000
    printed: "(helper)"
    label: "Deduction claimed of more than $5,000 per item or group of similar items (all donees combined)"
    type: Bool
    expr: {op: test, gt: [gift.deduction, {const: 500000}]}
    note: "The instructions say that in figuring whether the deduction for a group of similar items was more than $5,000, you count all items in the group, even if they went to more than one donee. gift.deduction is already defined across all donees, so it is compared directly against $5,000 (500000 cents)."
  - id: gift.h_not_public
    printed: "(helper)"
    label: "Group is not publicly traded securities"
    type: Bool
    expr: {op: test, eq: [gift.public_securities, {const: false}]}
  - id: gift.section_b
    printed: "(helper)"
    label: "Appraisal threshold: non-publicly-traded group over $5,000"
    type: Bool
    expr: {op: test, all: [gift.h_over5000, gift.h_not_public]}
    note: "Open point 1: Section A also takes vehicles, intellectual property and inventory even when they are over $5,000. Section B is also required for partial interests or restricted-use property, and for clothing or household items not in good used condition with a deduction over $500. Those cases are flagged by gift.special and are left out of scope. Choice made: this line encodes only the over-$5,000 test with the publicly-traded-securities exclusion. Open point 2: this field is listed in the collection but was not on the requested list, so it is included here as a transcription of the Section B threshold."
```
```
