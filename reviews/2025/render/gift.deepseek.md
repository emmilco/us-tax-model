# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 9eab6a6957a55b7a56bf66ce44e2634ae44967898fe58dea12e6e11ca14df857 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 3527279fb5d48036ff2f19346df56ca14dc621ca3c24e2ff1e7e5f97e5074d8e |
| lines judged | 5 |
| match / mismatch / unclear / missing | 4 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |

## Lines

### deduction — Deduction before income limits for this item or group of similar items across all donees, 
Status: **MATCH**

Model: IRS defines the deduction amount used for the filing threshold as before income limits but after required reductions, and it aggregates similar items across donees for that threshold.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: IRS expressly treats publicly traded securities as an exception to the usual over-$5,000 Section B rule.

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MISMATCH**

Restated: Input — Does this group need an appraisal or other special treatment: a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together (other than publicly traded securities), a noncash contribution reaching you through a Schedule K-1, vehicles, pass-through entity interests, intellectual property, inventory, conservation or partial interests, property with restrictions on its use, or a clothing or household item over $500 not in good used condition?

Model: IRS places only a qualified vehicle with a gross-proceeds acknowledgment, certain intellectual property, and inventory in Section A even over $5,000, and it requires Section B for partial or restricted interests only when the contribution is over $5,000; the restatement treats all vehicles, intellectual property, inventory, conservation or partial interests, and restricted-use property as special without those limits.

Ruling: open

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MATCH**

Model: IRS requires Section B for claimed deductions over $5,000 per item or group of similar items, while publicly traded securities are reported in Section A.

### allowed — Amount from gift.deduction
Status: **MATCH**

Model: IRS Form 8283 requires the claimed deduction amount and does not itself figure the charitable deduction; the refusals name the special-property and Section B cases the program excludes.

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "IRS defines the deduction amount used for the filing threshold as before income limits but after required reductions, and it aggregates similar items across donees for that threshold."
  - key: "public_securities"
    status: MATCH
    reason: "IRS expressly treats publicly traded securities as an exception to the usual over-$5,000 Section B rule."
  - key: "special"
    status: MISMATCH
    reason: "IRS places only a qualified vehicle with a gross-proceeds acknowledgment, certain intellectual property, and inventory in Section A even over $5,000, and it requires Section B for partial or restricted interests only when the contribution is over $5,000; the restatement treats all vehicles, intellectual property, inventory, conservation or partial interests, and restricted-use property as special without those limits."
  - key: "section_b"
    status: MATCH
    reason: "IRS requires Section B for claimed deductions over $5,000 per item or group of similar items, while publicly traded securities are reported in Section A."
  - key: "allowed"
    status: MATCH
    reason: "IRS Form 8283 requires the claimed deduction amount and does not itself figure the charitable deduction; the refusals name the special-property and Section B cases the program excludes."
```
