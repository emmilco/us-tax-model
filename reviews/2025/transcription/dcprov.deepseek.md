# Transcription agreement — dcprov

Second transcription of `Form 2441, Part I — persons or organizations who provided the care, one entry per care provider` by an isolated model (spec 6.5), compared line by line with `forms/2025/dcprov.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 53ec64337d2122a977206f1cf743b323af63e12173c51b2fe870305c19764f1f |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
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
lines:
  - id: dcprov.one
    printed: "(helper)"
    label: "One care provider (helper)"
    type: Count
    expr: {op: param, ref: dc.one}
  - id: dcprov.see_statement
    printed: "(helper)"
    label: 'Enter "See Attached Statement" in column (c) for this provider'
    type: Bool
    expr: {op: test, eq: ["dcprov.tin_kind", {const: "see_statement"}]}
```
