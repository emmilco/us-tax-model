# Form 8949 and Schedule D — manually classified securities transactions

- Document: `sales` (form, tax year 2025)
- Collection: keyed entries; [f8949] Parts I and II, transaction rows (2025; created 2025-05-05; sha256 27451389)
- Note: Stable keys identify transactions. The taxpayer supplies holding-period and reporting classifications from records. Dates/descriptions and completed PDF preparation are deferred; this is a calculation values sheet. Wash-sale detection and basis determination are not automated.

## (helper) — `sales.box`

- **Authored helper label:** Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets
- **Encoded (Enum(sales_box)):** Input — Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets
- Expr: `{"op":"input","source":"Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets"}`
- Cite: [i8949] pp. 2–5, holding period and checkbox classifications (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.route`

- **Authored helper label:** Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals
- **Encoded (Enum(sales_route)):** Input — Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals
- Expr: `{"op":"input","source":"Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals"}`
- Cite: [i1040sd] p. 10, lines 1a and 8a (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sales.code`

- **Authored helper label:** Adjustment codes: none, B, W, BW; choose other for any additional code
- **Encoded (Enum(sales_code)):** Input — Adjustment codes: none, B, W, BW; choose other for any additional code
- Expr: `{"op":"input","source":"Adjustment codes: none, B, W, BW; choose other for any additional code"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.special`

- **Authored helper label:** Does this sale involve collectibles, section 1202 stock, or section 1250 property?
- **Encoded (Bool):** Input — Does this sale involve collectibles, section 1202 stock, or section 1250 property?
- Expr: `{"op":"input","source":"Does this sale involve collectibles, section 1202 stock, or section 1250 property?"}`
- Cite: [i1040sd] pp. 11–12, lines 18 and 19 (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sales.aggregate_eligible`

- **Authored helper label:** Confirm all aggregate conditions: basis reported, no broker adjustments, no Ordinary box, no QOF disposition/deferral, no corrections, no collectibles
- **Encoded (Bool):** Input — Confirm all aggregate conditions: basis reported, no broker adjustments, no Ordinary box, no QOF disposition/deferral, no corrections, no collectibles
- Expr: `{"op":"input","source":"Confirm all aggregate conditions: basis reported, no broker adjustments, no Ordinary box, no QOF disposition/deferral, no corrections, no collectibles"}`
- Cite: [i1040sd] p. 10, lines 1a and 8a (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sales.proceeds`

- **Authored helper label:** Column (d): proceeds per broker report, or net proceeds if no report
- **Encoded (NonNegDollars):** Input — Column (d): proceeds per broker report, or net proceeds if no report
- Expr: `{"op":"input","source":"Column (d): proceeds per broker report, or net proceeds if no report"}`
- Cite: [i8949] p. 6, column (d) (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.reported_basis`

- **Authored helper label:** Basis shown on broker report
- **Encoded (NonNegDollars):** Input — Basis shown on broker report
- Expr: `{"op":"input","source":"Basis shown on broker report"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.correct_basis`

- **Authored helper label:** Correct adjusted basis from records
- **Encoded (NonNegDollars):** Input — Correct adjusted basis from records
- Expr: `{"op":"input","source":"Correct adjusted basis from records"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.wash_loss`

- **Authored helper label:** Correct nondeductible wash-sale loss; positive cents, including losses not reported by broker
- **Encoded (NonNegDollars):** Input — Correct nondeductible wash-sale loss; positive cents, including losses not reported by broker
- Expr: `{"op":"input","source":"Correct nondeductible wash-sale loss; positive cents, including losses not reported by broker"}`
- Cite: [i8949] p. 10, code W; a lower corrected loss requires an explanation statement (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.covered`

- **Authored helper label:** Basis reported to IRS
- **Encoded (Bool):** (line (helper) = 'A' or line (helper) = 'D')
- Expr: `{"any":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.box",{"const":"D"}],"op":"test"}],"op":"test"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.digital`

- **Authored helper label:** Digital asset box G–L
- **Encoded (Bool):** (line (helper) = 'G' or line (helper) = 'H' or line (helper) = 'I' or line (helper) = 'J' or line (helper) = 'K' or line (helper) = 'L')
- Expr: `{"any":[{"eq":["sales.box",{"const":"G"}],"op":"test"},{"eq":["sales.box",{"const":"H"}],"op":"test"},{"eq":["sales.box",{"const":"I"}],"op":"test"},{"eq":["sales.box",{"const":"J"}],"op":"test"},{"eq":["sales.box",{"const":"K"}],"op":"test"},{"eq":["sales.box",{"const":"L"}],"op":"test"}],"op":"test"}`
- Cite: [f8949] Parts I and II, boxes G–L (2025; created 2025-05-05; sha256 27451389)

## (helper) — `sales.has_b`

- **Authored helper label:** Basis correction code B applies
- **Encoded (Bool):** (line (helper) = 'B' or line (helper) = 'BW')
- Expr: `{"any":[{"eq":["sales.code",{"const":"B"}],"op":"test"},{"eq":["sales.code",{"const":"BW"}],"op":"test"}],"op":"test"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.has_w`

- **Authored helper label:** Wash-sale code W applies
- **Encoded (Bool):** (line (helper) = 'W' or line (helper) = 'BW')
- Expr: `{"any":[{"eq":["sales.code",{"const":"W"}],"op":"test"},{"eq":["sales.code",{"const":"BW"}],"op":"test"}],"op":"test"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.bad_code`

- **Authored helper label:** Unsupported adjustment or code B without a broker basis report
- **Encoded (Bool):** (line (helper) = 'other' or line (helper) = true and (line (helper) = 'C' or line (helper) = 'F'))
- Expr: `{"any":[{"eq":["sales.code",{"const":"other"}],"op":"test"},{"all":[{"eq":["sales.has_b",{"const":true}],"op":"test"},{"any":[{"eq":["sales.box",{"const":"C"}],"op":"test"},{"eq":["sales.box",{"const":"F"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.bad_aggregate`

- **Authored helper label:** Aggregate route fails its eligibility conditions
- **Encoded (Bool):** line (helper) = 'aggregate' and (line (helper) = false or line (helper) ≠ 'none' or line (helper) = false)
- Expr: `{"all":[{"eq":["sales.route",{"const":"aggregate"}],"op":"test"},{"any":[{"eq":["sales.covered",{"const":false}],"op":"test"},{"ne":["sales.code",{"const":"none"}],"op":"test"},{"eq":["sales.aggregate_eligible",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 10, lines 1a and 8a (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sales.one`

- **Authored helper label:** Screen this transaction before any aggregation
- **Encoded (Count):** Enter 1 (sales.one).
- **Refusal:** when sales.digital is true, cannot complete Form 8949 digital asset boxes G–L. Digital asset transactions are outside this tool; prepare the applicable digital-asset part. Cite: [f8949] Parts I and II, boxes G–L (2025; created 2025-05-05; sha256 27451389)
- **Refusal:** when sales.special is true, cannot complete Schedule D special gains worksheets. Direct sales of collectibles, section 1202 stock and section 1250 property are unsupported. Cite: [i1040sd] pp. 11–12, lines 18 and 19 (2025; printed date 2025-12-11; sha256 650643a6)
- **Refusal:** when sales.bad_code is true, cannot complete Form 8949 adjustment instructions. Only applicable B and W adjustments are supported. Review the required code and prepare the unsupported adjustment. Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)
- **Refusal:** when sales.bad_aggregate is true, cannot complete Form 8949. Use the detail route; this transaction does not qualify for Schedule D lines 1a/8a. Cite: [i1040sd] p. 10, lines 1a and 8a (2025; printed date 2025-12-11; sha256 650643a6)
- Expr: `{"op":"param","ref":"sales.one"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.zero`

- **Authored helper label:** No adjustment
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (e) — `sales.e`

- **Authored helper label:** Column (e): reported basis if covered; correct basis otherwise
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sales.covered",{"const":true}],"op":"test"},"then":"sales.reported_basis"},{"guard":{"eq":["sales.covered",{"const":false}],"op":"test"},"then":"sales.correct_basis"}],"op":"choose"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.b_difference`

- **Authored helper label:** Reported basis minus correct basis
- **Encoded (Dollars):** Subtract line (helper) from line (helper).
- Expr: `{"from":"sales.reported_basis","op":"subtract","take":"sales.correct_basis"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.adjust_b`

- **Authored helper label:** Correct reported basis in column (g)
- **Encoded (Bool):** line (helper) = true and line (helper) = true
- Expr: `{"all":[{"eq":["sales.covered",{"const":true}],"op":"test"},{"eq":["sales.has_b",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.b`

- **Authored helper label:** Basis correction in column (g)
- **Encoded (Dollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sales.adjust_b",{"const":true}],"op":"test"},"then":"sales.b_difference"},{"guard":{"eq":["sales.adjust_b",{"const":false}],"op":"test"},"then":"sales.zero"}],"op":"choose"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.w`

- **Authored helper label:** Wash-sale adjustment in column (g)
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sales.has_w",{"const":true}],"op":"test"},"then":"sales.wash_loss"},{"guard":{"eq":["sales.has_w",{"const":false}],"op":"test"},"then":"sales.zero"}],"op":"choose"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (g) — `sales.g`

- **Authored helper label:** Column (g): net adjustments
- **Encoded (Dollars):** Add line (helper) and line (helper).
- Expr: `{"of":["sales.b","sales.w"],"op":"sum"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (helper) — `sales.before_adjustment`

- **Authored helper label:** Proceeds less column (e)
- **Encoded (Dollars):** Subtract line (e) from line (helper).
- Expr: `{"from":"sales.proceeds","op":"subtract","take":"sales.e"}`
- Cite: [i8949] pp. 7–11, columns (e) through (h), codes B and W (2025; printed date 2026-01-20; sha256 f077991c)

## (h) — `sales.h`

- **Authored helper label:** Column (h): proceeds less basis plus adjustments
- **Encoded (Dollars):** Add line (helper) and line (g).
- Interpretation: amb.2025.sales_rounding
- Expr: `{"of":["sales.before_adjustment","sales.g"],"op":"sum"}`
- Cite: [i8949] p. 11, column (h) (2025; printed date 2026-01-20; sha256 f077991c)
