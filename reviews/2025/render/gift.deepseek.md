# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | c75f31927102ad5339d8700749ae2d47de7fe82777ecdfe00e08ac2445d883fa |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 1102a5e587158cec42118ecc1bfba1831269200b78d784b95cf3f0f74177302d |
| lines judged | 8 |
| match / mismatch / unclear / missing | 6 / 0 / 1 / 1 |
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

Model: It matches the deduction before income limits and after required reductions/valuation adjustments; it narrows out clothing/household items not in good used condition and $250+ gifts without a contemporaneous written acknowledgment as unsupported exclusions.

### public_securities — Is this group publicly traded securities (listed on a recognized stock exchange whose quot
Status: **MATCH**

Model: The restatement tracks the IRS definition of publicly traded securities and reasonably says privately held stock, LLC/partnership interests, and stock not listed or regularly traded over the counter are not publicly traded.

### special — Does this group need an appraisal or other special treatment: any of the following?
Status: **MISSING**

Restated: Input — Does this group need an appraisal or other special treatment: any of the following?

- a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together, other than publicly traded securities
  - similar items: items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land or buildings
  - publicly traded securities: listed on a recognized stock exchange whose quotations are published daily, regularly traded on a national or regional over-the-counter market, or mutual fund shares quoted daily in a national newspaper
- a noncash contribution reaching you through a Schedule K-1
- vehicles
- pass-through entity interests
- intellectual property
- inventory
- conservation or partial interests
- property with restrictions on its use
- a clothing or household item over $500 not in good used condition

Model: the model returned no verdict for this line

Ruling: model error; the reply returned no verdict for this line. The restructured gift.special question was judged MATCH in the Claude render pass of the same restatement (reviews/2025/render/gift.md), and its words are the earlier question's (R3 word check: none lost).
Reviewed in: pass 9c89307c0d01

### over_5000 — The deduction for this item or group is more than $5,000
Status: **MATCH**

Model: IRS uses the deduction before income limits and after required reductions, and aggregates all similar items across donees, for the more-than-$5,000 threshold.
Reviewed in: pass e82bfe70f97a

### not_public — This group is not publicly traded securities
Status: **MATCH**

Model: Negating the public-securities input matches the IRS definition of publicly traded securities by exchange, over-the-counter market, or mutual-fund quotations.
Reviewed in: pass e82bfe70f97a

### no — Year parameter sa.no (no)
Status: **UNCLEAR**

Restated: Enter false (sa.no).

Model: The provided IRS text does not mention a 'Year parameter sa.no' or define this helper, so the false value cannot be verified from the text.

Ruling: model error; gift.no is the false alternative of gift.section_b, taken when the deduction is $5,000 or less (f8283 p. 1, Section B, "more than $5,000 per item or group"); it is a structural constant the text need not state, and the restatement (false) matches the project.
Reviewed in: pass e82bfe70f97a

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: The helper is true only for a non-publicly-traded item or group over $5,000, which aligns with the Section B appraisal threshold in the IRS text.
Reviewed in: pass e82bfe70f97a

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: IRS says to use the contribution deduction before income limits after required reductions; the refusals narrow the line to unsupported special-property and Section B cases.
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
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9c89307c0d010ddd65a040509647b6a7bc61a69d144c7db7f26351d5fd5f6388 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 6bca41da3d345f96f385d3a5e7ee1bbf5263011c5e7cd811c6cff72c0691246c |
| receipt | .transcription/gift.deepseek.render.lines-07041c01d2ea |
| lines judged | 2 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 1 |
| verdicts for lines not in the form | Does this group need an appraisal or other special treatment: any of the following? - a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together, other than publicly traded securities - similar items: items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land or buildings - publicly traded securities: listed on a recognized stock exchange whose quotations are published daily, regularly traded on a national or regional over-the-counter market, or mutual fund shares quoted daily in a national newspaper - a noncash contribution reaching you through a Schedule K-1 - vehicles - pass-through entity interests - intellectual property - inventory - conservation or partial interests - property with restrictions on its use - a clothing or household item over $500 not in good used condition |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

##### Raw response

```yaml
lines:
  - key: "Does this group need an appraisal or other special treatment: any of the following? - a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together, other than publicly traded securities - similar items: items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land or buildings - publicly traded securities: listed on a recognized stock exchange whose quotations are published daily, regularly traded on a national or regional over-the-counter market, or mutual fund shares quoted daily in a national newspaper - a noncash contribution reaching you through a Schedule K-1 - vehicles - pass-through entity interests - intellectual property - inventory - conservation or partial interests - property with restrictions on its use - a clothing or household item over $500 not in good used condition"
    status: MATCH
    reason: "The gate tracks the IRS appraisal and Section B/special-property triggers, including the >$5,000 item/group threshold, similar-items aggregation, publicly traded securities exception, K-1 and special property categories, and clothing/household item rule; any broader exclusions are named."
  - key: "Amount from gift.deduction"
    status: MATCH
    reason: "It pulls the deduction before income limits after required reductions for the item or similar-items group across all donees, and its refusals exclude special-property and Section B over-$5,000 appraisal cases as named exceptions."
```

#### Pass e82bfe70f97a

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines over_5000, not_public, no, section_b, allowed |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | e82bfe70f97aeef4fa4c4fdf0f9fd110120d605e8438fcfbdfe3ced08aa81be7 |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | c645b415c368887f4b51c5f5fdfb79aaab58b99ff09ea6944af6476dea711c2d |
| receipt | .transcription/gift.deepseek.render.lines-14307570c83a |
| lines judged | 5 |
| match / mismatch / unclear / missing | 4 / 0 / 1 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3, 9 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3, 9 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |
| i1040sca | 2025; printed date 2025-12-08 | 11 | pages named by another document's citation | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | 11 | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| f8283 | December 2025; created 2025-07-01 | 1, 2 | whole document | d33f4c2762c7366b560ae700f7c403b698b6567187a94eb4f7943b3ab6c20219 | - | 2a4ef5ee41c489f0de7f68915540d45a11937f39759f0c9ffb0f326461ee9320 |

##### Raw response

```yaml
lines:
  - key: "over_5000"
    status: MATCH
    reason: "IRS uses the deduction before income limits and after required reductions, and aggregates all similar items across donees, for the more-than-$5,000 threshold."
  - key: "not_public"
    status: MATCH
    reason: "Negating the public-securities input matches the IRS definition of publicly traded securities by exchange, over-the-counter market, or mutual-fund quotations."
  - key: "no"
    status: UNCLEAR
    reason: "The provided IRS text does not mention a 'Year parameter sa.no' or define this helper, so the false value cannot be verified from the text."
  - key: "section_b"
    status: MATCH
    reason: "The helper is true only for a non-publicly-traded item or group over $5,000, which aligns with the Section B appraisal threshold in the IRS text."
  - key: "allowed"
    status: MATCH
    reason: "IRS says to use the contribution deduction before income limits after required reductions; the refusals narrow the line to unsupported special-property and Section B cases."
```

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "It matches the deduction before income limits and after required reductions/valuation adjustments; it narrows out clothing/household items not in good used condition and $250+ gifts without a contemporaneous written acknowledgment as unsupported exclusions."
  - key: "public_securities"
    status: MATCH
    reason: "The restatement tracks the IRS definition of publicly traded securities and reasonably says privately held stock, LLC/partnership interests, and stock not listed or regularly traded over the counter are not publicly traded."
  - key: "special"
    status: MATCH
    reason: "The triggers align with the IRS appraisal/Section B and special-property rules, including the >$5,000 group threshold, public-securities exception, and special categories such as vehicles, IP, inventory, conservation/partial interests, restrictions, and clothing/household items over $500."
  - key: "section_b"
    status: MATCH
    reason: "For supported non-special groups, Section B applies when the deduction before income limits is over $5,000 and the group is not publicly traded securities; this matches the IRS Section B threshold."
  - key: "allowed"
    status: MATCH
    reason: "It takes the amount from the deduction helper and refuses only special-property or Section B cases, naming those exclusions consistently with the form's supported Section A scope."
```
