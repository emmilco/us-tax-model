# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 06e7bd4d3d96b2b0e2b5f0a384802e2f161c355180e436bfda71957934aa172e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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

Model: The input follows the instructions: "amount of your deduction" means the deduction "before applying any income limits", after "any required reductions", and a group's total considers all items "even if items in the group were donated to more than one donee organization." The similar-items wording also tracks the instructions' definition.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: This is a filer-supplied yes/no input that mirrors the form's Section A category for "publicly traded securities", which are listed there "even if the deduction is more than $5,000." It computes nothing that could conflict with the text.

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: The gate collects cases the text treats specially, including property "valued in excess of $5,000", Schedule K-1 contributions, vehicles, intellectual property, inventory, partial interests, restricted property, and clothing or household items over $500 not in good used condition. Where it is broader than the text, such as partial interests of $5,000 or less, it only narrows the supported cases through a named refusal.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: The test matches Section B's "deduction of more than $5,000 per item or group" and excepts publicly traded securities. It omits the other Section A exceptions ("Vehicles, Intellectual Property or Inventory" and certain other securities), but that can only cause a refusal, and the special gate already refuses vehicles, intellectual property and inventory.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: This carries the deduction forward unchanged, consistent with the form's note to "Figure the amount of your contribution deduction before completing this form" and the instructions' statement not to use Form 8283 to figure it. The refusals name the excluded Section B and special-treatment cases, leaving only the cases the program supports.

## Raw response

```yaml
```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The input follows the instructions: \"amount of your deduction\" means the deduction \"before applying any income limits\", after \"any required reductions\", and a group's total considers all items \"even if items in the group were donated to more than one donee organization.\" The similar-items wording also tracks the instructions' definition."
  - key: "public_securities"
    status: MATCH
    reason: "This is a filer-supplied yes/no input that mirrors the form's Section A category for \"publicly traded securities\", which are listed there \"even if the deduction is more than $5,000.\" It computes nothing that could conflict with the text."
  - key: "special"
    status: MATCH
    reason: "The gate collects cases the text treats specially, including property \"valued in excess of $5,000\", Schedule K-1 contributions, vehicles, intellectual property, inventory, partial interests, restricted property, and clothing or household items over $500 not in good used condition. Where it is broader than the text, such as partial interests of $5,000 or less, it only narrows the supported cases through a named refusal."
  - key: "section_b"
    status: MATCH
    reason: "The test matches Section B's \"deduction of more than $5,000 per item or group\" and excepts publicly traded securities. It omits the other Section A exceptions (\"Vehicles, Intellectual Property or Inventory\" and certain other securities), but that can only cause a refusal, and the special gate already refuses vehicles, intellectual property and inventory."
  - key: "allowed"
    status: MATCH
    reason: "This carries the deduction forward unchanged, consistent with the form's note to \"Figure the amount of your contribution deduction before completing this form\" and the instructions' statement not to use Form 8283 to figure it. The refusals name the excluded Section B and special-treatment cases, leaving only the cases the program supports."
```
```
