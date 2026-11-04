# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 0a51f41f1998b0894db66094f29f41374b76073dc0ae97f8467b0af64660a45e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | fc82dc24c2a922c439a73bcedac40d3a03522d6a921a9ff0bfa927cc2e1939b4 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | ltc.age |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### 2(a) — Total payments made for that person during the year
Status: **MATCH**

Model: IRS line 2(a) calls for total payments made for that person, and the instructions allow qualified long-term care premiums paid for that person while excluding months of eligibility for a subsidized long-term care plan.

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: IRS line 2(b) provides the age-based qualified long-term care premium limits and directs use of the person’s age at the end of the tax year; the restatement points to that table using the age helper.

## Raw response

```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "IRS line 2(a) calls for total payments made for that person, and the instructions allow qualified long-term care premiums paid for that person while excluding months of eligibility for a subsidized long-term care plan."
  - key: "2(b)"
    status: MATCH
    reason: "IRS line 2(b) provides the age-based qualified long-term care premium limits and directs use of the person’s age at the end of the tax year; the restatement points to that table using the age helper."
  - key: "ltc.age"
    status: MATCH
    reason: "The IRS text uses the person’s age at the end of the tax year and lists the same age brackets for the qualified long-term care premium limits."
```
