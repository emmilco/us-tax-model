# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 98dcb5fd5496a0a0beb16828b8347396bf996e433a913272a3345e25a6c83de1 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | d3da815e06eeea1e381805a795dd0c772122a188eb854cd37cc6f033559b5d2c |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### 2(a) — Total payments made for that person during the year
Status: **MATCH**

Model: The restatement captures line 2(a)’s total payments for the covered person and correctly excludes months of eligibility for an employer-subsidized long-term care insurance plan.

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: The IRS line 2(b) amount is determined from the covered person’s age at the end of 2025 using the listed age bands, which is what the restatement directs.

## Raw response

```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "The restatement captures line 2(a)’s total payments for the covered person and correctly excludes months of eligibility for an employer-subsidized long-term care insurance plan."
  - key: "2(b)"
    status: MATCH
    reason: "The IRS line 2(b) amount is determined from the covered person’s age at the end of 2025 using the listed age bands, which is what the restatement directs."
```
