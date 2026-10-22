# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9eab6a6957a55b7a56bf66ce44e2634ae44967898fe58dea12e6e11ca14df857 |
| subject sha256 | 3527279fb5d48036ff2f19346df56ca14dc621ca3c24e2ff1e7e5f97e5074d8e |
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

Model: This matches the instructions: "amount of your deduction" means "your deduction before applying any income limits," after "any required reductions." The instructions also say to "consider all items in the group, even if items in the group were donated to more than one donee organization."

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: The filer answers this yes/no question directly. It matches the publicly traded securities the instructions list as Section A items "even if the claimed value was more than $5,000" (items 2.a–2.d).

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: This is an input used only as a refusal gate. It covers the cases the instructions treat specially: K-1 contributions from pass-through entities, vehicles, intellectual property, inventory, partial interests and restricted-use property, conservation contributions, clothing or household items over $500 not in good used condition, and property over $5,000 needing an appraisal. Gating some Section A cases, such as vehicles, IP and inventory, only narrows what the program supports.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: This matches "Include in Section B only items (or groups of similar items) for which you claimed a deduction of more than $5,000" with publicly traded securities excepted. The other Section A exceptions (vehicles, intellectual property, inventory) are already caught by the special gate, so for supported cases the condition is correct.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: This passes through the deduction amount for the supported cases, which are Section A groups over $500 and up to $5,000. The refusals name the excluded cases: Section B or appraisal cases and special-treatment property.

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "This matches the instructions: \"amount of your deduction\" means \"your deduction before applying any income limits,\" after \"any required reductions.\" The instructions also say to \"consider all items in the group, even if items in the group were donated to more than one donee organization.\""
  - key: "public_securities"
    status: MATCH
    reason: "The filer answers this yes/no question directly. It matches the publicly traded securities the instructions list as Section A items \"even if the claimed value was more than $5,000\" (items 2.a–2.d)."
  - key: "special"
    status: MATCH
    reason: "This is an input used only as a refusal gate. It covers the cases the instructions treat specially: K-1 contributions from pass-through entities, vehicles, intellectual property, inventory, partial interests and restricted-use property, conservation contributions, clothing or household items over $500 not in good used condition, and property over $5,000 needing an appraisal. Gating some Section A cases, such as vehicles, IP and inventory, only narrows what the program supports."
  - key: "section_b"
    status: MATCH
    reason: "This matches \"Include in Section B only items (or groups of similar items) for which you claimed a deduction of more than $5,000\" with publicly traded securities excepted. The other Section A exceptions (vehicles, intellectual property, inventory) are already caught by the special gate, so for supported cases the condition is correct."
  - key: "allowed"
    status: MATCH
    reason: "This passes through the deduction amount for the supported cases, which are Section A groups over $500 and up to $5,000. The refusals name the excluded cases: Section B or appraisal cases and special-treatment property."
```
