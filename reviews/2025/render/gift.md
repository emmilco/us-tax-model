# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c75f31927102ad5339d8700749ae2d47de7fe82777ecdfe00e08ac2445d883fa |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 1102a5e587158cec42118ecc1bfba1831269200b78d784b95cf3f0f74177302d |
| lines judged | 8 |
| match / mismatch / unclear / missing | 8 / 0 / 0 / 0 |
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

### special — Does this group need an appraisal or other special treatment: any of the following?
Status: **MATCH**

Model: Each trigger is supported by the text, including Section B for deductions over $5,000 per item or group across all donees except publicly traded securities, a qualified appraisal for gifts valued over $5,000, and Section B for clothing or household items over $500 not in good used condition. The text also supports the pass-through member rules, vehicles, intellectual property, inventory, partial interests, conditions on use, and qualified conservation contributions. The few broader triggers, such as all vehicles, all pass-through entity interests and 'certain other securities' not exempted, only route more cases to refusal, which is a permitted narrowing.
Reviewed in: pass 9c89307c0d01

### over_5000 — The deduction for this item or group is more than $5,000
Status: **MATCH**

Model: The instructions use "a deduction of more than $5,000 per item or group of similar items" as the Section B threshold. In figuring this, you "consider all items in the group, even if items in the group were donated to more than one donee organization." The helper tests the cross-donee deduction, after reductions, with a strict greater-than $5,000.
Reviewed in: pass e82bfe70f97a

### not_public — This group is not publicly traded securities
Status: **MATCH**

Model: This is the negation of the publicly-traded-securities input. Its definition matches the Line 2 instructions: listed on a recognized stock exchange whose quotations are published daily, regularly traded over the counter, or mutual fund shares quoted daily. Those securities are reported in Section A in any amount.
Reviewed in: pass e82bfe70f97a

### no — Year parameter sa.no (no)
Status: **MATCH**

Model: This is a constant false used as the default branch of the section_b choice. Nothing in the IRS text bears on it beyond that use.
Reviewed in: pass e82bfe70f97a

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: The helper is true only when the group's deduction exceeds $5,000 and it is not publicly traded securities. That matches its label and the core Section B rule ("more than $5,000", except publicly traded securities). The other Section A exceptions (vehicles, intellectual property, inventory) and the other Section B triggers fall under the separate gift.special refusal, so the narrowing is still correct.
Reviewed in: pass e82bfe70f97a

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: The helper passes through the deduction before income limits, after required reductions, as "amount of your deduction" is defined in Who Must File. The refusals exclude Section B items over $5,000 and the special-property cases. Within the remaining Section A cases the value is correct.
Reviewed in: pass e82bfe70f97a

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| deduction | 2c743be67b29b3d1bc72955e6d9df9a4cf4ff957f8e03656f34f2f1651dd1275 |
| public_securities | e6a87578d54851f8c4cc5e873fc24302bc51124ced33e09660437210e75e16f2 |
| special | 40a1549aba0e72b0e00eb760f5c2ed54b7f87008bc774e60be9e4adb6e91a76c |
| over_5000 | cf86d4f8648cf4a6b9897d576176959c24abb6eb3885764b787b94bf3c4e8a9c |
| not_public | 208bc9f49f33ae44786e8dfad2c8ddec1b80b5949d0fdae3b40ea389131fa14d |
| no | d9fa15f532ffe8528369f1a894ea723d018c837730f4432559a9eef822bb07ab |
| section_b | 41faadbceda9c3c8ee5d88f29ba0785cea9242aa59052f66a5be178e843372f7 |
| allowed | 9b2d891a2631662a76396816fd880615d4c3d39bcfb1d8da5c5661eacd44e13f |
| (rest of the document) | 453167e36426ad055796eee7ca39439492a94ba8c947ab84ce7cc052e0dd764e |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 9c89307c0d01

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines special, allowed |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 9c89307c0d010ddd65a040509647b6a7bc61a69d144c7db7f26351d5fd5f6388 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 6bca41da3d345f96f385d3a5e7ee1bbf5263011c5e7cd811c6cff72c0691246c |
| receipt | .transcription/gift.render.lines-07041c01d2ea |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

##### Raw response

```yaml
```yaml
lines:
  - key: "special"
    status: MATCH
    reason: "Each trigger is supported by the text, including Section B for deductions over $5,000 per item or group across all donees except publicly traded securities, a qualified appraisal for gifts valued over $5,000, and Section B for clothing or household items over $500 not in good used condition. The text also supports the pass-through member rules, vehicles, intellectual property, inventory, partial interests, conditions on use, and qualified conservation contributions. The few broader triggers, such as all vehicles, all pass-through entity interests and 'certain other securities' not exempted, only route more cases to refusal, which is a permitted narrowing."
  - key: "allowed"
    status: MATCH
    reason: "It passes through the filer's deduction 'before applying any income limits', after the required reductions. This matches 'amount of your deduction' in Who Must File. The exclusions for items not in good used condition and for gifts of $250 or more without a contemporaneous written acknowledgment follow the Schedule A instructions. The refusals exclude the special-property cases and groups that are not publicly traded securities and are over $5,000, which 'require a written qualified appraisal' and Section B."
```
```

#### Pass e82bfe70f97a

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines over_5000, not_public, no, section_b, allowed |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e82bfe70f97aeef4fa4c4fdf0f9fd110120d605e8438fcfbdfe3ced08aa81be7 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c645b415c368887f4b51c5f5fdfb79aaab58b99ff09ea6944af6476dea711c2d |
| receipt | .transcription/gift.render.lines-14307570c83a |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

##### Raw response

```yaml
```yaml
lines:
  - key: "over_5000"
    status: MATCH
    reason: "The instructions use \"a deduction of more than $5,000 per item or group of similar items\" as the Section B threshold. In figuring this, you \"consider all items in the group, even if items in the group were donated to more than one donee organization.\" The helper tests the cross-donee deduction, after reductions, with a strict greater-than $5,000."
  - key: "not_public"
    status: MATCH
    reason: "This is the negation of the publicly-traded-securities input. Its definition matches the Line 2 instructions: listed on a recognized stock exchange whose quotations are published daily, regularly traded over the counter, or mutual fund shares quoted daily. Those securities are reported in Section A in any amount."
  - key: "no"
    status: MATCH
    reason: "This is a constant false used as the default branch of the section_b choice. Nothing in the IRS text bears on it beyond that use."
  - key: "section_b"
    status: MATCH
    reason: "The helper is true only when the group's deduction exceeds $5,000 and it is not publicly traded securities. That matches its label and the core Section B rule (\"more than $5,000\", except publicly traded securities). The other Section A exceptions (vehicles, intellectual property, inventory) and the other Section B triggers fall under the separate gift.special refusal, so the narrowing is still correct."
  - key: "allowed"
    status: MATCH
    reason: "The helper passes through the deduction before income limits, after required reductions, as \"amount of your deduction\" is defined in Who Must File. The refusals exclude Section B items over $5,000 and the special-property cases. Within the remaining Section A cases the value is correct."
```
```

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
