# Transcription agreement — ltc

Second transcription of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` by an isolated model (spec 6.5), compared line by line with `forms/2025/ltc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| review provenance | verified saved-response replay; no model call |
| parent review log sha256 | dee8257a2ddc623925c5fc4567f1478b831e8f7cfbe540e4e66f67b2bed113ed |
| original review date | 2026-10-26 |
| original comparison policy | checked-expression-types-v2 |
| original type validation policy | project-expression-types-v2 |
| original input context policy | required-review-interfaces-v2 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0218f8f68548456e1b5fdab5bef66d9cfb6e0896357f6f4f4b3bc91ded87c5a4 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 0b1eb00f49c949648ce90a2b057d2c9b2da5a14cc7627c6c7f0ee46a60966134 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7725642cb923e811f4d5df5cade9656856609c785f5d22f318800bdb04234fe8 |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### ltc.amount — The smaller of (a) or (b)
Status: **AGREE**

### 2(b) — The amount for that person's age
Status: **AGREE**

## Raw second transcription

```yaml
lines:
  - id: ltc.limit
    printed: "2(b)"
    label: "(b) The amount shown below. Use the person's age at the end of the tax year. $480— if that person is age 40 or younger; $900— if age 41 to 50; $1,800— if age 51 to 60; $4,810— if age 61 to 70; $6,020— if age 71 or older"
    type: NonNegDollars
    expr: {op: keyed_lookup, table: ltc_limit, keys: [ltc.age]}
  - id: ltc.amount
    printed: "(helper)"
    label: "For coverage under a qualified long-term care insurance contract, enter for each person covered the smaller of (a) or (b). If more than one person is covered, figure separately the amount to enter for each person."
    type: NonNegDollars
    expr: {op: smaller_of, of: [ltc.payments, ltc.limit]}
    note: "Line 2 itself is the total of these per-person amounts over all persons covered; that total belongs to the Form 7206 line 2 of the business entry, which is outside this per-person slice. Two points in the IRS text are not computed here. First, the i7206 rule that the line 2 amounts for one person, added across all Forms 7206, can't be more than that person's limit. Second, the exclusion of months in which the person was eligible for an employer-subsidized long-term care plan. The first is left to the business-level screen (sc.hi_screen, which covers long-term care insurance entered for more than one business). The second is already excluded by the definition of the ltc.payments input."
```
