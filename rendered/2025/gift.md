# Form 8283 — groups of similar noncash property

- Document: `gift` (form, tax year 2025)
- Collection: keyed entries; [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
- Note: Group similar property across donees before testing $5,000. Values are supplied from valuation records; this does not determine fair market value or produce a completed signed Form 8283. Dates, descriptions and donee details remain in underlying records.

## (helper) — `gift.deduction`

- **Authored helper label:** Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions
- **Encoded (NonNegDollars):** Input — Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions
- Expr: `{"op":"input","source":"Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.public_securities`

- **Authored helper label:** Is this group publicly traded securities?
- **Encoded (Bool):** Input — Is this group publicly traded securities?
- Expr: `{"op":"input","source":"Is this group publicly traded securities?"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.special`

- **Authored helper label:** Does this group need an appraisal or other special treatment: a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together (other than publicly traded securities), a noncash contribution reaching you through a Schedule K-1, vehicles, pass-through entity interests, intellectual property, inventory, conservation or partial interests, property with restrictions on its use, or a clothing or household item over $500 not in good used condition?
- **Encoded (Bool):** Input — Does this group need an appraisal or other special treatment: a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together (other than publicly traded securities), a noncash contribution reaching you through a Schedule K-1, vehicles, pass-through entity interests, intellectual property, inventory, conservation or partial interests, property with restrictions on its use, or a clothing or household item over $500 not in good used condition?
- Expr: `{"op":"input","source":"Does this group need an appraisal or other special treatment: a deduction over $5,000 (before any income limit), or property worth more than $5,000, for one item or for similar items given to all donees together (other than publicly traded securities), a noncash contribution reaching you through a Schedule K-1, vehicles, pass-through entity interests, intellectual property, inventory, conservation or partial interests, property with restrictions on its use, or a clothing or household item over $500 not in good used condition?"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.section_b`

- **Authored helper label:** Appraisal threshold: non-publicly-traded group over $5,000
- **Encoded (Bool):** helper "Is this group publicly traded securities?" = false and helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions" > $5,000
- Expr: `{"all":[{"eq":["gift.public_securities",{"const":false}],"op":"test"},{"gt":["gift.deduction",{"const":500000}],"op":"test"}],"op":"test"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 p. 1, Section A, "Also list publicly traded securities and certain other property even if the deduction is more than $5,000", Section B, "for which you claimed a deduction of more than $5,000 per item or group (except contributions reportable in Section A)" (December 2025; printed date 2026-01-30; sha256 2de015f7)

## (helper) — `gift.allowed`

- **Authored helper label:** Amount from gift.deduction
- **Encoded (NonNegDollars):** Enter the amount from helper "Deduction before income limits for this item or group of similar items across all donees, after required valuation/basis reductions".
- **Refusal:** when gift.special is true, cannot complete Form 8283 special treatment. This contribution requires unsupported appraisal or special-property treatment. Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
- **Refusal:** when gift.section_b is true, cannot complete Form 8283 Section B. A group of similar items over $5,000 requires Section B and a qualified appraisal; publicly traded securities are excepted. Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
- Expr: `{"from":"gift.deduction","op":"copy"}`
- Cite: [i8283] pp. 1–3, Who Must File and Which Sections To Complete; f8283 Section A (December 2025; printed date 2026-01-30; sha256 2de015f7)
