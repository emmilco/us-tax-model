# Transcription agreement — dcprov

Second transcription of `Form 2441, Part I — persons or organizations who provided the care, one entry per care provider` by an isolated model (spec 6.5), compared line by line with `forms/2025/dcprov.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 53ec64337d2122a977206f1cf743b323af63e12173c51b2fe870305c19764f1f |
| prompt policy | source-only-computation-v2 |
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
lines:
  - id: dcprov.one
    printed: "(helper)"
    label: "One care provider (this entry): counts toward the number of persons or organizations listed on line 1. If you have more than three care providers, check the box above line 1 and attach a statement."
    type: Count
    expr: {op: param, ref: dc.one}
    cite: "i2441 (2025), p. 2, Part I, Line 1: 'Complete columns (a) through (e) for each person or organization that provided the care ... If you have more than three care providers, check the box above line 1 and attach a statement to your return with the required information.'"
    note: "The IRS text does not name this result. It is read as a per-entry count of one, so that totals across entries give the number of care providers. Other forms compare that number with three (the box above line 1) and use it to tell whether line 1 is complete. The value comes from the declared year parameter dc.one, which is 1. No new input is added."
  - id: dcprov.see_statement
    printed: "(helper)"
    label: "Enter “See Attached Statement” in the columns for which you don't have the information. Then, attach a statement to your return explaining that the provider didn't give you the information you requested."
    type: Bool
    expr: {op: test, eq: [dcprov.tin_kind, {const: "see_statement"}]}
    cite: "i2441 (2025), p. 3, Due Diligence: 'If the provider doesn't give you the information, complete the entries you can on line 1 ... Enter “See Attached Statement” in the columns for which you don't have the information. Then, attach a statement to your return explaining that the provider didn't give you the information you requested.'"
    note: "The IRS text does not name this result. It is read as true when the filer enters “See Attached Statement” in column (c), the provider's identifying number. That happens because the provider did not give the information, and the filer must then attach a due-diligence statement. This uses only the existing input dcprov.tin_kind, value \"see_statement\". The instructions also allow “See Attached Statement” in other columns (for example the address). The closed interface has no input for those columns, so they are not covered."
```
