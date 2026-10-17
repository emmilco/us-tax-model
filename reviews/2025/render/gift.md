# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 8c74ff60e608dd574843b5c449277663a57d6b04a865d92b1e18004e2189e121 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees, 
Status: **MATCH**

Model: The text defines "amount of your deduction" as "your deduction before applying any income limits that could result in a carryover", with "any required reductions" made first. For a group, it says to "consider all items in the group, even if items in the group were donated to more than one donee organization." The filer-supplied input says the same.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: The text names "publicly traded securities" as items reported in Section A even above $5,000. The exchange-listed, over-the-counter and mutual fund securities in items 2.a–2.c fit this yes/no input.

### special — Does this group need an appraisal or other special treatment (including vehicles, pass-thr
Status: **MATCH**

Model: The text gives separate treatment to vehicles, intellectual property, inventory, partial interests, conservation contributions and pass-through entity gifts. It also requires Section B for "a single article of clothing or household item that is not in good used condition or better and for which you are claiming a deduction of over $500." Because this input only triggers a refusal, it narrows what the program supports without changing any computed value.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: The text says to use Section B for items or groups "for which you claimed a deduction of more than $5,000," with publicly traded securities excepted to Section A. The restatement's strict > $5,000 test matches. It also refuses 'certain other securities' (item 2.d) that could go in Section A. That is a refusal only and does not change any value.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: Within the supported cases (not special, not Section B), the program reports the deduction before income limits, which is the amount the text uses to decide whether Form 8283 is required and which section applies. The refusals name the excluded cases: special-property treatment and Section B with a qualified appraisal.

## Raw response

```yaml
```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The text defines \"amount of your deduction\" as \"your deduction before applying any income limits that could result in a carryover\", with \"any required reductions\" made first. For a group, it says to \"consider all items in the group, even if items in the group were donated to more than one donee organization.\" The filer-supplied input says the same."
  - key: "public_securities"
    status: MATCH
    reason: "The text names \"publicly traded securities\" as items reported in Section A even above $5,000. The exchange-listed, over-the-counter and mutual fund securities in items 2.a–2.c fit this yes/no input."
  - key: "special"
    status: MATCH
    reason: "The text gives separate treatment to vehicles, intellectual property, inventory, partial interests, conservation contributions and pass-through entity gifts. It also requires Section B for \"a single article of clothing or household item that is not in good used condition or better and for which you are claiming a deduction of over $500.\" Because this input only triggers a refusal, it narrows what the program supports without changing any computed value."
  - key: "section_b"
    status: MATCH
    reason: "The text says to use Section B for items or groups \"for which you claimed a deduction of more than $5,000,\" with publicly traded securities excepted to Section A. The restatement's strict > $5,000 test matches. It also refuses 'certain other securities' (item 2.d) that could go in Section A. That is a refusal only and does not change any value."
  - key: "allowed"
    status: MATCH
    reason: "Within the supported cases (not special, not Section B), the program reports the deduction before income limits, which is the amount the text uses to decide whether Form 8283 is required and which section applies. The refusals name the excluded cases: special-property treatment and Section B with a qualified appraisal."
```
```
