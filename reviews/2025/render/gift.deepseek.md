# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 06e7bd4d3d96b2b0e2b5f0a384802e2f161c355180e436bfda71957934aa172e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 808caa0cd460bb4e427733862cabb2bf52943b0f147f103f6aed38a71e18b63a |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees,
Status: **MATCH**

Model: IRS says to use the deduction before income limits and after required reductions, and to consider all similar items even if donated to more than one donee for the group threshold.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: IRS treats publicly traded securities as a Section A category and excludes them from the ordinary over-$5,000 Section B rule.

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: The over-$5,000 appraisal and special-property categories match the IRS instructions, including similar items across donees and the public-securities exception.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: A non-publicly-traded group with a deduction over $5,000 is the ordinary Section B appraisal threshold; public securities are excepted and other special categories are handled by the special helper.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: The line uses the computed deduction amount, and the refusals narrow the program to supported non-special cases while naming the excluded Section B and special-treatment cases.

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "IRS says to use the deduction before income limits and after required reductions, and to consider all similar items even if donated to more than one donee for the group threshold."
  - key: "public_securities"
    status: MATCH
    reason: "IRS treats publicly traded securities as a Section A category and excludes them from the ordinary over-$5,000 Section B rule."
  - key: "special"
    status: MATCH
    reason: "The over-$5,000 appraisal and special-property categories match the IRS instructions, including similar items across donees and the public-securities exception."
  - key: "section_b"
    status: MATCH
    reason: "A non-publicly-traded group with a deduction over $5,000 is the ordinary Section B appraisal threshold; public securities are excepted and other special categories are handled by the special helper."
  - key: "allowed"
    status: MATCH
    reason: "The line uses the computed deduction amount, and the refusals narrow the program to supported non-special cases while naming the excluded Section B and special-treatment cases."
```
