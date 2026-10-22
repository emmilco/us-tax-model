# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ce0dc65622a81dad89d8ef3e99d136fcd9c683f67dc992802c39635e341678e7 |
| subject sha256 | 583ad7a6fa5b933fa0a0fffda31e2cc72eab6b74f021ea484f649729eb2516bb |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |

## Lines

### gift.allowed — Amount from gift.deduction
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| gift.allowed | gift.special | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: gift.allowed
    printed: "(helper)"
    label: "Amount from gift.deduction"
    type: NonNegDollars
    expr: {op: copy, from: gift.deduction}
    refuses: [gift.special]
    note: "The task lists no printed lines to transcribe, so this is the only line. The provided text says Form 8283 is not used to figure the deduction ('do not use Form 8283 to figure your charitable contribution deduction'). The amount therefore passes through unchanged from gift.deduction, which is already the deduction before income limits after required reductions. Section B items need a qualified appraisal and are outside what this tool computes. These include groups over $5,000 that are not publicly traded securities, partial interests, restricted-use property, and clothing or household items not in good used condition claimed over $500. Section A special items include vehicles, intellectual property and inventory. These cases are covered by the screening input gift.special, so this line refuses when it is true instead of computing them."
```
```
