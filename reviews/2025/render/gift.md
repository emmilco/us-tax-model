# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cc2c7fb58c7d5dc48020864cb395b9c38b11c07f039722aa4414e044a16744e7 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 9f6ba8e615ef1875cc2cab00806541b94691c9bbcf0ac2881c173e4e0b817a26 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees,
Status: **MATCH**

Model: The instructions say the 'amount of your deduction' is the amount 'before applying any income limits that could result in a carryover', after 'any required reductions', and that a similar-items group counts all items 'even if items in the group were donated to more than one donee organization'. Leaving out clothing and household items in poor condition and $250+ gifts with no contemporaneous written acknowledgment follows the Schedule A instructions, and the over-$500 poor-condition case is sent to the 'special' refusal.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: This is a yes/no input for publicly traded securities. The text treats them as a Section A exception: 'Also list publicly traded securities ... even if the deduction is more than $5,000.'

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: Each listed case has a basis in the text: an appraisal is needed 'for any gift of property valued in excess of $5,000'; there are separate rules for pass-through members; Section B covers single clothing or household items over $500 not in good used condition; and partial-interest and restricted-use property are covered. Some cases it refuses, such as vehicles, intellectual property and inventory, could be reported in Section A, but refusing them only narrows what the program supports.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: This matches 'Use Section B to report donations of property for which you claimed a deduction of more than $5,000 per item or group of similar items' with the publicly traded securities exception. The other Section A exceptions (vehicles, intellectual property, inventory) are already caught by the 'special' refusal.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: This copies the deduction amount and is only computed when the special-treatment and Section B refusals don't apply, so it stays within the Section A range of 'more than $500 but not more than $5,000'. The refusals correctly name what is excluded: Section B with a qualified appraisal, and special property.

## Raw response

```yaml
```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The instructions say the 'amount of your deduction' is the amount 'before applying any income limits that could result in a carryover', after 'any required reductions', and that a similar-items group counts all items 'even if items in the group were donated to more than one donee organization'. Leaving out clothing and household items in poor condition and $250+ gifts with no contemporaneous written acknowledgment follows the Schedule A instructions, and the over-$500 poor-condition case is sent to the 'special' refusal."
  - key: "public_securities"
    status: MATCH
    reason: "This is a yes/no input for publicly traded securities. The text treats them as a Section A exception: 'Also list publicly traded securities ... even if the deduction is more than $5,000.'"
  - key: "special"
    status: MATCH
    reason: "Each listed case has a basis in the text: an appraisal is needed 'for any gift of property valued in excess of $5,000'; there are separate rules for pass-through members; Section B covers single clothing or household items over $500 not in good used condition; and partial-interest and restricted-use property are covered. Some cases it refuses, such as vehicles, intellectual property and inventory, could be reported in Section A, but refusing them only narrows what the program supports."
  - key: "section_b"
    status: MATCH
    reason: "This matches 'Use Section B to report donations of property for which you claimed a deduction of more than $5,000 per item or group of similar items' with the publicly traded securities exception. The other Section A exceptions (vehicles, intellectual property, inventory) are already caught by the 'special' refusal."
  - key: "allowed"
    status: MATCH
    reason: "This copies the deduction amount and is only computed when the special-treatment and Section B refusals don't apply, so it stays within the Section A range of 'more than $500 but not more than $5,000'. The refusals correctly name what is excluded: Section B with a qualified appraisal, and special property."
```
```
