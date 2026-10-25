# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2a98f2c533db68e92c813ab4ca689459a838d854b7a7c5aa4991608a54b5d5ce |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
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
lines:
  - id: gift.section_b
    printed: "(helper)"
    label: "Whether this group is reported in Section B because it needs a qualified appraisal or other special treatment."
    type: Bool
    expr: {op: copy, from: gift.special}
    note: "The Form 8283 instructions place a group in Section B when the claimed deduction or property value requires a qualified appraisal or other special treatment; the supplied screening input gift.special records exactly that condition for this tool. Publicly traded securities and the other Section A categories are outside it."
  - id: gift.allowed
    printed: "(helper)"
    label: "Deduction allowed for this group of similar noncash property."
    type: NonNegDollars
    expr: {op: copy, from: gift.deduction}
    refuses: [gift.special]
    note: "Form 8283 is a reporting form; its instructions say not to use it to figure the charitable contribution deduction. The amount carried forward is therefore the supplied deduction before income limits, after required valuation or basis reductions. Groups needing an appraisal or other special treatment are refused."
```
