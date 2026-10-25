# Transcription agreement — ltc

Second transcription of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` by an isolated model (spec 6.5), compared line by line with `forms/2025/ltc.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 000546bb75fdfbb34d6a019bd409c4e81381f3677a5b00e08cb23565f9461357 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 7725642cb923e811f4d5df5cade9656856609c785f5d22f318800bdb04234fe8 |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"keys": [{"input": "ltc.age"}], "op": "keyed_lookup", "table": "ltc_limit"}
```

Second:

```json
{"keys": [{"input": "ltc.age"}], "op": "keyed_lookup", "table": "ltc_age_limit"}
```

Ruling: open

## Raw second transcription

```yaml
lines:
  - id: ltc.limit
    printed: "2(b)"
    label: "(b) The amount shown below. Use the person’s age at the end of the tax year."
    type: NonNegDollars
    expr:
      op: keyed_lookup
      table: ltc_age_limit
      keys: [ltc.age]
    cite: "Form 7206 (2025), line 2(b); Instructions for Form 7206 (2025), Qualified long-term care insurance"
  - id: ltc.amount
    printed: "(helper)"
    label: "The smaller of line 2(a) or line 2(b), for this person covered."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [ltc.payments, ltc.limit]
    cite: "Form 7206 (2025), line 2 and instructions; Instructions for Form 7206 (2025), Qualified long-term care insurance"
```
