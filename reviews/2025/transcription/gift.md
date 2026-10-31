# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2dbd765a089f05441a9c73436ecb58a8958834a3db4d0cd9112d5a93e2bf42db |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ff096ba9e6dee4a9f73d729331f8e6f82b8954b1042ab1e942ef4e1e05ad27ef |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 4b41963405bbce880647ac9dc9dbdfcc9507404cb92dc7cb300a4c5c877321a2 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### gift.allowed — Amount from gift.deduction
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| gift.allowed | gift.h_over_5000_not_public, gift.special | gift.h_over_5000_not_public |

## Raw second transcription

```yaml
lines:
  - id: gift.h_over_5000_not_public
    printed: "(helper)"
    label: "Deduction of more than $5,000 for an item or group of similar items that is not publicly traded securities (Section B: \"Include in Section B only items (or groups of similar items) for which you claimed a deduction of more than $5,000.\")"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          gt: [gift.deduction, {const: 500000}]
        - op: test
          eq: [gift.public_securities, {const: false}]
    note: "The source supplies no Year parameter for the $5,000 threshold, so it is written as a constant from i8283 and Form 8283 Section B. Section A also admits vehicles, intellectual property and inventory above $5,000, but gift.special routes those cases to refusal, so only publicly traded securities are excepted here."
  - id: gift.allowed
    printed: "(helper)"
    label: "Amount of your deduction for this item or group of similar items, before applying any income limits (Form 8283: \"Figure the amount of your contribution deduction before completing this form.\")"
    type: NonNegDollars
    expr:
      op: copy
      from: gift.deduction
    refuses:
      - gift.special
      - when: gift.h_over_5000_not_public
        when_known: true
    note: "The pages do not name an 'allowed' amount, and the instructions say not to use Form 8283 to figure the deduction. I read gift.allowed as the supplied deduction before income limits, carried through once the group is within Section A treatment. Income limits and carryovers are not figured here (i8283 refers to Pub. 526). A group over $5,000 that is not publicly traded securities conflicts with a 'no' answer to gift.special and needs Section B and a qualified appraisal, so it refuses as a consistency check."
```
