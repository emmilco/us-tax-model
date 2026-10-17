# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 726712e97130074447c7ac7a4b6f2fc7befe3241899cf12c0865eea49413c701 |
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

## Raw second transcription

```yaml
```yaml
lines:
  - id: gift.allowed
    printed: "(helper)"
    label: "Amount from gift.deduction"
    type: NonNegDollars
    expr: {op: copy, from: gift.deduction}
    note: "The request lists no printed lines to transcribe, so this is the only line. The instructions say not to use Form 8283 to figure the charitable contribution deduction. They say the 'amount of your deduction' is the amount before any income limits, after required reductions (Who Must File; Reductions to contribution). The form computes nothing further, so I copy gift.deduction unchanged. Neither gift.public_securities nor gift.special affects this amount. Those inputs only decide whether Section A or Section B applies."
```
```
