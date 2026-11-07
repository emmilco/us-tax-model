# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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

Model: The restatement matches line 2(a) and the line 2 note: it captures total qualified long-term care premiums paid for the covered person, excluding months of eligibility for a subsidized long-term care plan, and it correctly limits covered persons and describes qualified long-term care contracts.
Reviewed in: pass 51740e632e16

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: It uses the person’s age at the end of 2025 to select the IRS limit for that age; the age helper brackets match the form’s age ranges and amounts.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 2(a) | 3a0c14f6380a27934b690ecce7f9076636ae738430b99d03bfe6ed3bcd90e8cc |
| 2(b) | bedb626f9e3a0590b30ab49cff0ca8207490010f34f7529d0909e4853e18f541 |
| (rest of the document) | 9680d6b2041e715d2fbd99eee9f6f1d7e9ed0a159eea2e0316d9712917df7063 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 51740e632e16

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 2(a) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 51740e632e16a8df08f553a16d2e00f625dac68a1faa002ea4eabbf3ba609c7e |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | b433732223700287e464a285405fbc46f101ccede743f56d7565835290fb2d45 |
| receipt | .transcription/ltc.deepseek.render.lines-bd9fdb118f70 |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

##### Raw response

```yaml
lines:
  - key: "2(a)"
    status: MATCH
    reason: "The restatement matches line 2(a) and the line 2 note: it captures total qualified long-term care premiums paid for the covered person, excluding months of eligibility for a subsidized long-term care plan, and it correctly limits covered persons and describes qualified long-term care contracts."
```

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
