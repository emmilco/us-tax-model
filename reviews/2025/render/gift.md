# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c75f31927102ad5339d8700749ae2d47de7fe82777ecdfe00e08ac2445d883fa |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 1102a5e587158cec42118ecc1bfba1831269200b78d784b95cf3f0f74177302d |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees,
Status: **MATCH**

Model: The instructions define the amount as the 'deduction before applying any income limits' after 'any required reductions', counting similar items across all donees. Leaving out items not in good used condition and $250+ gifts without a contemporaneous written acknowledgment follows Schedule A. The appraised over-$500 exception is caught by the special refusal.

### public_securities — Is this group publicly traded securities (listed on a recognized stock exchange whose quot
Status: **MATCH**

Model: The definition repeats the Line 2 Securities instruction's three criteria. Answering No for privately held stock, LLC and partnership interests matches the nonpublicly traded examples. The 'certain other securities' of Section A item 2.d are only refused, never miscomputed.

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: Each trigger is in the text: the over-$5,000 appraisal rule, partial interests, restricted use, clothing or household items over $500 not in good used condition, pass-through contributions, and the Section A carve-outs. As a refusal gate it only narrows what the program supports.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: The instructions put in Section B items 'for which you claimed a deduction of more than $5,000', except Section A items such as publicly traded securities. The gate tests not-publicly-traded and deduction > $5,000. Vehicles, intellectual property and inventory are refused separately by special, so the gate is right within supported cases.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: This passes through the pre-income-limit deduction. The refusals exclude every case needing Section B, a qualified appraisal or special-property treatment. Within the remaining Section A cases, the amount matches the instructions' 'amount of your deduction'.

## Raw response

```yaml
```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The instructions define the amount as the 'deduction before applying any income limits' after 'any required reductions', counting similar items across all donees. Leaving out items not in good used condition and $250+ gifts without a contemporaneous written acknowledgment follows Schedule A. The appraised over-$500 exception is caught by the special refusal."
  - key: "public_securities"
    status: MATCH
    reason: "The definition repeats the Line 2 Securities instruction's three criteria. Answering No for privately held stock, LLC and partnership interests matches the nonpublicly traded examples. The 'certain other securities' of Section A item 2.d are only refused, never miscomputed."
  - key: "special"
    status: MATCH
    reason: "Each trigger is in the text: the over-$5,000 appraisal rule, partial interests, restricted use, clothing or household items over $500 not in good used condition, pass-through contributions, and the Section A carve-outs. As a refusal gate it only narrows what the program supports."
  - key: "section_b"
    status: MATCH
    reason: "The instructions put in Section B items 'for which you claimed a deduction of more than $5,000', except Section A items such as publicly traded securities. The gate tests not-publicly-traded and deduction > $5,000. Vehicles, intellectual property and inventory are refused separately by special, so the gate is right within supported cases."
  - key: "allowed"
    status: MATCH
    reason: "This passes through the pre-income-limit deduction. The refusals exclude every case needing Section B, a qualified appraisal or special-property treatment. Within the remaining Section A cases, the amount matches the instructions' 'amount of your deduction'."
```
```
