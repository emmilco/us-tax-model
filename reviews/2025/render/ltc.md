# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0a51f41f1998b0894db66094f29f41374b76073dc0ae97f8467b0af64660a45e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | fc82dc24c2a922c439a73bcedac40d3a03522d6a921a9ff0bfa927cc2e1939b4 |
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

Model: Line 2(a) asks for 'Total payments made for that person during the year' under a qualified long-term care contract, and its note excludes months eligible for an employer-subsidized long-term care plan (yours, your spouse's, or that of your dependent's or under-27 child's employer). The restatement adds the covered-person rule (you, spouse, dependents, child under 27) and the one-form-per-business rule, which agree with the form and instructions. The cap on the total across all Forms 7206 per person applies across forms, not to this line.

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: Line 2(b) says to use 'the person's age at the end of the tax year' with the bands 40 or younger, 41 to 50, 51 to 60, 61 to 70, and 71 or older, which the age helper's enum reproduces. The program's lookup table values are not shown, so they could not be checked against the printed $480/$900/$1,800/$4,810/$6,020.

## Raw response

```yaml
```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "Line 2(a) asks for 'Total payments made for that person during the year' under a qualified long-term care contract, and its note excludes months eligible for an employer-subsidized long-term care plan (yours, your spouse's, or that of your dependent's or under-27 child's employer). The restatement adds the covered-person rule (you, spouse, dependents, child under 27) and the one-form-per-business rule, which agree with the form and instructions. The cap on the total across all Forms 7206 per person applies across forms, not to this line."
  - key: "2(b)"
    status: MATCH
    reason: "Line 2(b) says to use 'the person's age at the end of the tax year' with the bands 40 or younger, 41 to 50, 51 to 60, 61 to 70, and 71 or older, which the age helper's enum reproduces. The program's lookup table values are not shown, so they could not be checked against the printed $480/$900/$1,800/$4,810/$6,020."
```
```
