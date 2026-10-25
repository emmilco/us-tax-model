# Transcription agreement — dcprov

Second transcription of `Form 2441, Part I — persons or organizations who provided the care, one entry per care provider` by an isolated model (spec 6.5), compared line by line with `forms/2025/dcprov.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ad34a5c94d8464884d0d1ef7933c045cfae79684ff18f5810a89a9f9e5b85e8b |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 85e99ab390d88927070f3b10975b790102a5300c78fc4c50d07c5b268cff11cb |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i2441 | 2025 | 2, 3 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 2, 3 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| p503 | For use in preparing 2025 returns | 8 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 8 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |

## Lines

### dcprov.one — One care provider
Status: **AGREE**

### dcprov.see_statement — Column (c) reads "See Attached Statement"
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: dcprov.one
    printed: "(helper)"
    label: "One care provider (this entry), counted toward the number of care providers on line 1"
    type: Count
    expr: {op: param, ref: dc.one}
    note: "The IRS text does not name this value. It reads as the count of 1 for each provider entry, so that summing it gives the number of care providers. The total is compared with three for the 'more than three care providers' box above line 1 and the attached statement. Encoded as the year parameter dc.one (1). Whether to exclude 'employer' or related entries from the count is left to the reading form; the text says to complete columns (a) through (e) for each person or organization that provided the care."
  - id: dcprov.see_statement
    printed: "(helper)"
    label: "If the provider doesn't give you the information ... Enter \"See Attached Statement\" in the columns for which you don't have the information. Then, attach a statement to your return explaining that the provider didn't give you the information you requested."
    type: Bool
    expr: {op: test, eq: [dcprov.tin_kind, {const: "see_statement"}]}
    note: "The IRS text does not name this value. Read as whether this provider's column (c) shows 'See Attached Statement' (Due Diligence, i2441 page 3). If so, a statement explaining that the provider didn't give the requested information must be attached. The closed interface records only column (c) through dcprov.tin_kind, so the flag covers a missing identifying number only, not other missing columns."
```
```
