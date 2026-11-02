# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 98dcb5fd5496a0a0beb16828b8347396bf996e433a913272a3345e25a6c83de1 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d3da815e06eeea1e381805a795dd0c772122a188eb854cd37cc6f033559b5d2c |
| lines judged | 2 |
| match / mismatch / unclear / missing | 1 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### 2(a) — Total payments made for that person during the year
Status: **MATCH**

Model: The restatement matches line 2(a), "Total payments made for that person during the year," and correctly applies the line 2 note excluding months of eligibility for a subsidized long-term care plan through the listed employers. Its limit to a policy established under this business is consistent with the form's note and the instructions requiring a separate Form 7206 for each business.

### 2(b) — The amount for that person's age
Status: **UNCLEAR**

Restated: Find the entry in Qualified long-term care premium limit by age (Form 7206, line 2(b)) for age helper "That person's age at the end of 2025".

Model: The age bands and use of age at year-end match "Use the person's age at the end of the tax year," but the restated table's dollar amounts are not provided, so they cannot be compared with the IRS's $480, $900, $1,800, $4,810, and $6,020. The restatement also does not show how it handles the multiple-business rule that the total on line 2 of "all Form(s) 7206 can't be more than the appropriate limit shown on line 2 for that person."

Ruling: representation; restatement accepted. tables/2025/ltc_limit.yaml holds $480, $900, $1,800, $4,810 and $6,020, the f7206 line 2 amounts by age at year-end. The multiple-business rule is refused by sc.hi_screen ("anyone is covered by qualified long-term care insurance entered for more than one business on this return").

## Raw response

```yaml
```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "The restatement matches line 2(a), \"Total payments made for that person during the year,\" and correctly applies the line 2 note excluding months of eligibility for a subsidized long-term care plan through the listed employers. Its limit to a policy established under this business is consistent with the form's note and the instructions requiring a separate Form 7206 for each business."
  - key: "2(b)"
    status: UNCLEAR
    reason: "The age bands and use of age at year-end match \"Use the person's age at the end of the tax year,\" but the restated table's dollar amounts are not provided, so they cannot be compared with the IRS's $480, $900, $1,800, $4,810, and $6,020. The restatement also does not show how it handles the multiple-business rule that the total on line 2 of \"all Form(s) 7206 can't be more than the appropriate limit shown on line 2 for that person.\""
```
```
