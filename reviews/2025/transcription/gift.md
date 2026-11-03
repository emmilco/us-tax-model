# Transcription agreement — gift

Second transcription of `Form 8283 — groups of similar noncash property` by an isolated model (spec 6.5), compared line by line with `forms/2025/gift.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c157b548ff4d9ae0b9719d439577fc650131d4aebf4a0c139d7d60749aeec565 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 90a99afbb2bb2eee557a8dac8e9aabed9557fb2fdf632677899c0784721c1150 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | d18c9a40a0ed9b904c7e11e305b8490c9c6ae4e1d7b18063db0f998e97b0822a |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

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
  - id: gift.allowed
    printed: "(helper)"
    label: "Deduction for this item or group of similar items carried to the return (Form 8283, Section A; amount of your deduction before applying any income limits)"
    type: NonNegDollars
    expr: {op: copy, from: gift.deduction}
    refuses: [gift.special]
    note: "The pages do not fully determine what 'allowed' means. The Form 8283 instructions say not to use Form 8283 to figure the deduction. They say that the 'amount of your deduction' is figured before income limits and after the required reductions to the contribution, and gift.deduction already gives that amount. So this result is that amount for an item or group that Section A covers. Income limits and carryovers are outside this slice (sa.charity_limited). Section B items need a qualified appraisal, and so do partial interests, restricted use property, vehicles, K-1 contributions, and single clothing or household items over $500 not in good used condition; for these the tool refuses through gift.special. Publicly traded securities are reported in Section A even when the deduction is over $5,000, and gift.special already leaves them out of its over-$5,000 test. So gift.public_securities does not change the amount, and this line does not read it."
```
