# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9fcdfcf5edbdf84448827f5ebbd5117d31d05a8d2e04b24f1c628d33f80098fc |
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
    note: "No printed lines were listed for transcription, so only the requested helper is produced. The instructions say 'amount of your deduction' means the deduction before any income limits, after required reductions (i8283 p.1, Who Must File; p.3, Reductions to contribution). The text also says Form 8283 is not used to figure the deduction. So the allowed amount is a straight copy of the input gift.deduction, with no further computation on this form."
```
```
