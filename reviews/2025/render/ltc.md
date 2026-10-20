# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 56034c0085eb7128f9236c72f54e519b2e7ee4a2d2028fa9234f4b4512455e03 |
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

Model: Line 2(a) is 'Total payments made for that person during the year' under a qualified long-term care insurance contract. The restatement adds the line 2 note's exclusion of any month the filer was eligible for an employer-subsidized long-term care plan, and the instructions' requirement that the plan be established under this business.

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: Line 2(b) uses 'the person's age at the end of the tax year'. The age buckets match the form's brackets: 40 or younger, 41 to 50, 51 to 60, 61 to 70, and 71 or older. The dollar entries of the program's lookup table ($480/$900/$1,800/$4,810/$6,020 on the form) are not shown, so only the bracket structure could be checked.

## Raw response

```yaml
```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "Line 2(a) is 'Total payments made for that person during the year' under a qualified long-term care insurance contract. The restatement adds the line 2 note's exclusion of any month the filer was eligible for an employer-subsidized long-term care plan, and the instructions' requirement that the plan be established under this business."
  - key: "2(b)"
    status: MATCH
    reason: "Line 2(b) uses 'the person's age at the end of the tax year'. The age buckets match the form's brackets: 40 or younger, 41 to 50, 51 to 60, 61 to 70, and 71 or older. The dollar entries of the program's lookup table ($480/$900/$1,800/$4,810/$6,020 on the form) are not shown, so only the bracket structure could be checked."
```
```
