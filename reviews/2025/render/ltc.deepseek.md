# Render comparison — ltc

The rendered English of every printed line of `Form 7206, line 2 — qualified long-term care insurance, one per person covered` (`rendered/2025/ltc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 56034c0085eb7128f9236c72f54e519b2e7ee4a2d2028fa9234f4b4512455e03 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 7470681aa9b71dbcc40db5df670c57193a834f34ac1be822d03a73c420eb27b9 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 1 / 1 / 0 / 0 |
| verdicts for lines not in the form | ltc.age |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### 2(a) — Total payments made for that person during the year
Status: **MISMATCH**

Restated: Input — The qualified long-term care insurance premiums paid in 2025 for this person under a policy established under this business (not for any month the person was eligible for a long-term care plan subsidized by an employer)

Model: The IRS note excludes payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child who was under age 27 at the end of 2025; the restatement instead states the exclusion in terms of the covered person's eligibility for a plan subsidized by an employer.

Ruling: open

### 2(b) — The amount for that person's age
Status: **MATCH**

Model: The restatement selects the applicable age-based qualified long-term care premium limit using the person's age at the end of 2025, matching Form 7206 line 2(b).

## Raw response

```yaml
lines:
  - key: "2(a)"
    status: MISMATCH
    reason: "The IRS note excludes payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child who was under age 27 at the end of 2025; the restatement instead states the exclusion in terms of the covered person's eligibility for a plan subsidized by an employer."
  - key: "2(b)"
    status: MATCH
    reason: "The restatement selects the applicable age-based qualified long-term care premium limit using the person's age at the end of 2025, matching Form 7206 line 2(b)."
  - key: "ltc.age"
    status: MATCH
    reason: "The age brackets and end-of-2025 measurement match the IRS age categories used for the line 2(b) limit."
```
