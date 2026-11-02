# Transcription agreement — ltc

Second transcription of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` by an isolated model (spec 6.5), compared line by line with `forms/2025/ltc.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 7f20b1f058536fef47681530ccd97e2351404ce06fa95e6041fced2169c293a5 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 1133623277ebbee04df833cd34e52da1ce46437b30608d9ec5bf7daf3ab3bf59 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 82179fa79df561ead41677aec2bae4c74cce769404aabd860a16977fb583e4d2 |
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
    label: "The amount shown below. Use the person’s age at the end of the tax year."
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
```
