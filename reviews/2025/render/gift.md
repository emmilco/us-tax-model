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

Model: The instructions define the amount as 'your deduction before applying any income limits' after 'any required reductions'. They also say to 'consider all items in the group, even if items in the group were donated to more than one donee organization.' Leaving out the excluded items follows the Schedule A text: clothing and household items are deductible 'only if the items are in good used condition or better', and gifts of $250 or more 'must also have a contemporaneous written acknowledgment'.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: This is a plain filer input. It matches the Section A exception for 'publicly traded securities' listed in the form and instructions.

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: Each listed condition appears in the instructions as a case that needs Section B, an appraisal or special reporting. These include the over-$5,000 thresholds, pass-through (K-1) contributions, vehicles, intellectual property, inventory, partial interests and restricted use, conservation contributions, and a single clothing or household item over $500 not in good used condition. As a refusal gate, it only narrows the program to the cases it supports.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: Section B covers items or groups 'for which you claimed a deduction of more than $5,000', except publicly traded securities and other items reportable in Section A. The test is 'more than $5,000', which matches '> $5,000'. The other Section A exceptions (vehicles, IP, inventory) are already caught by the special refusal.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: It passes through the deduction amount as its label says. Its refusals name the excluded Section B and special-treatment cases, leaving the Section A cases of more than $500 but not more than $5,000 that the text says to report there.

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The instructions define the amount as 'your deduction before applying any income limits' after 'any required reductions'. They also say to 'consider all items in the group, even if items in the group were donated to more than one donee organization.' Leaving out the excluded items follows the Schedule A text: clothing and household items are deductible 'only if the items are in good used condition or better', and gifts of $250 or more 'must also have a contemporaneous written acknowledgment'."
  - key: "public_securities"
    status: MATCH
    reason: "This is a plain filer input. It matches the Section A exception for 'publicly traded securities' listed in the form and instructions."
  - key: "special"
    status: MATCH
    reason: "Each listed condition appears in the instructions as a case that needs Section B, an appraisal or special reporting. These include the over-$5,000 thresholds, pass-through (K-1) contributions, vehicles, intellectual property, inventory, partial interests and restricted use, conservation contributions, and a single clothing or household item over $500 not in good used condition. As a refusal gate, it only narrows the program to the cases it supports."
  - key: "section_b"
    status: MATCH
    reason: "Section B covers items or groups 'for which you claimed a deduction of more than $5,000', except publicly traded securities and other items reportable in Section A. The test is 'more than $5,000', which matches '> $5,000'. The other Section A exceptions (vehicles, IP, inventory) are already caught by the special refusal."
  - key: "allowed"
    status: MATCH
    reason: "It passes through the deduction amount as its label says. Its refusals name the excluded Section B and special-treatment cases, leaving the Section A cases of more than $500 but not more than $5,000 that the text says to report there."
```
