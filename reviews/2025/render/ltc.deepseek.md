# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 90c2366ed9d8f50b8d7956c2cacca1960f933a6afec172997f23ad21b6de8b48 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 31030eb15df3d3d20594a29784d29e841d2d7017e0ac853955e00efddac388ba |
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

Model: It restates the premiums paid for the covered person under a qualified long-term care contract, including the IRS exclusions for employer-subsidized coverage and the eligible-person limits.

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: It uses the person’s age at the end of 2025 to select the IRS limit for that age; the age helper brackets match the form’s age ranges and amounts.

## Raw response

```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "It restates the premiums paid for the covered person under a qualified long-term care contract, including the IRS exclusions for employer-subsidized coverage and the eligible-person limits."
  - key: "2(b)"
    status: MATCH
    reason: "It uses the person’s age at the end of 2025 to select the IRS limit for that age; the age helper brackets match the form’s age ranges and amounts."
```
