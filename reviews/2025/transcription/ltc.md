# Transcription agreement — ltc

Second transcription of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` by an isolated model (spec 6.5), compared line by line with `forms/2025/ltc.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2aa712660a430672a4efd9fbbac18cf9ac90382d91c1ee0e177bbffd52b5e085 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | d553f55e1a3970c2da6b37ad2150455ba12209e5f62fc7960ed1849ea290ffc2 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | f9e39ed9d2c2b0ba17935aef482627ac3080e485ca6dce354c788868c2b8e59e |
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
    label: "The amount shown below. Use the person's age at the end of the tax year. $480 if that person is age 40 or younger; $900 if age 41 to 50; $1,800 if age 51 to 60; $4,810 if age 61 to 70; $6,020 if age 71 or older"
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: ltc_limit
      keys: [ltc.age]
  - id: ltc.amount
    printed: "(helper)"
    label: "For coverage under a qualified long-term care insurance contract, enter for each person covered the smaller of (a) or (b)."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [ltc.payments, ltc.limit]
    note: "Form 7206 line 2 gives this per-person amount; the form then totals the amounts over all persons covered. Totalling them over the collection belongs to the calling Schedule C entry (sc.f7206_line2), not to this entry. The instructions also say that a person's amounts on line 2 of all Forms 7206 together can't be more than that person's limit. This entry can't check that, because it is computed for one business only. The scope assumes the screening question sc.hi_screen refuses cases where the same person is covered under more than one business."
```
