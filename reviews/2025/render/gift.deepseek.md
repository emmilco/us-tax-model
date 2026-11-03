# Render comparison — gift

The rendered English of every printed line of `Form 8283 — groups of similar noncash property` (`rendered/2025/gift.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | cc2c7fb58c7d5dc48020864cb395b9c38b11c07f039722aa4414e044a16744e7 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 9f6ba8e615ef1875cc2cab00806541b94691c9bbcf0ac2881c173e4e0b817a26 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 3 / 2 / 0 / 0 |
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

Model: The IRS defines the amount of the deduction before income limits and after required reductions; the clothing and acknowledgment limits are conditions on deductibility, and the special gate handles the clothing exception for unsupported cases.

### public_securities — Is this group publicly traded securities?
Status: **MATCH**

Model: The IRS treats publicly traded securities as a Section A category even when the deduction exceeds $5,000.

### special — Does this group need an appraisal or other special treatment: a deduction over $5,000 (bef
Status: **MATCH**

Model: The restatement is a broad special-treatment gate covering the appraisal and Section B categories; over-inclusive cases are refused rather than computed.

### section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **MISMATCH**

Restated: helper "Is this group publicly traded securities?" = false and helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions" > $5,000

Model: The IRS Section B exclusion is broader: 'Donated Property Over $5,000 (Except Publicly Traded Securities, Vehicles, Intellectual Property or Inventory Reportable in Section A),' and Section A also includes certain other securities even over $5,000. The helper excludes only publicly traded securities.

Ruling: scope; accepted over-refusal. f8283 Section B covers "Donated Property Over $5,000 (Except Publicly Traded Securities, Vehicles, Intellectual Property or Inventory Reportable in Section A)". The project sends every over-$5,000 group except publicly traded securities to the Section B refusal, so a vehicle, intellectual property, inventory or certain other securities over $5,000 are refused rather than computed. That refuses returns the tool could support; it never computes a wrong amount.

### allowed — Amount from gift.deduction
Status: **MISMATCH**

Restated: Enter the amount from helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions".

Model: Its Section B refusal inherits that overbroad classification; the IRS excepts vehicles, intellectual property, inventory, and certain other securities reportable in Section A, not just publicly traded securities.

Ruling: scope; accepted over-refusal. f8283 Section B covers "Donated Property Over $5,000 (Except Publicly Traded Securities, Vehicles, Intellectual Property or Inventory Reportable in Section A)". The project sends every over-$5,000 group except publicly traded securities to the Section B refusal, so a vehicle, intellectual property, inventory or certain other securities over $5,000 are refused rather than computed. That refuses returns the tool could support; it never computes a wrong amount.

## Raw response

```yaml
lines:
  - key: "deduction"
    status: MATCH
    reason: "The IRS defines the amount of the deduction before income limits and after required reductions; the clothing and acknowledgment limits are conditions on deductibility, and the special gate handles the clothing exception for unsupported cases."
  - key: "public_securities"
    status: MATCH
    reason: "The IRS treats publicly traded securities as a Section A category even when the deduction exceeds $5,000."
  - key: "special"
    status: MATCH
    reason: "The restatement is a broad special-treatment gate covering the appraisal and Section B categories; over-inclusive cases are refused rather than computed."
  - key: "section_b"
    status: MISMATCH
    reason: "The IRS Section B exclusion is broader: 'Donated Property Over $5,000 (Except Publicly Traded Securities, Vehicles, Intellectual Property or Inventory Reportable in Section A),' and Section A also includes certain other securities even over $5,000. The helper excludes only publicly traded securities."
  - key: "allowed"
    status: MISMATCH
    reason: "Its Section B refusal inherits that overbroad classification; the IRS excepts vehicles, intellectual property, inventory, and certain other securities reportable in Section A, not just publicly traded securities."
```
