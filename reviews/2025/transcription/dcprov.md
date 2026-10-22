# Transcription agreement — dcprov

Second transcription of `Form 2441, Part I — persons or organizations who provided the care, one entry per care provider` by an isolated model (spec 6.5), compared line by line with `forms/2025/dcprov.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f59a0690db048169c009262534d7e5cceb6876a2715ecdd9ffe2ab045da74a50 |
| subject sha256 | 4ae8fc63ec63b8b45f85aea7c89ad92d3effa06c866841479a4ad278593e831c |
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
    label: "One care provider"
    type: Count
    expr: {op: param, ref: dc.one}
    note: "No printed line is listed for transcription. This helper counts each provider entry once so that other forms can total providers (i2441, Line 1: 'If you have more than three care providers, check the box above line 1'). It uses the year parameter dc.one (1)."
  - id: dcprov.see_statement
    printed: "(helper)"
    label: "Column (c) reads \"See Attached Statement\""
    type: Bool
    expr: {op: test, eq: [dcprov.tin_kind, {const: "see_statement"}]}
    note: "Source: i2441, Due Diligence: 'Enter \"See Attached Statement\" in the columns for which you don't have the information. Then, attach a statement to your return explaining that the provider didn't give you the information you requested.' The text could also cover other columns, such as the address. Only column (c) is modelled, through the dcprov.tin_kind value \"see_statement\"."
```
```
