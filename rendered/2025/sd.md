# Schedule D — securities sales and supplied distribution subtotals

- Document: `sd` (form, tax year 2025)
- Note: Special-gain feeders are computed from 1099-DIV box 2b/2d. Section 1202 distributions, non-securities source forms and prior-year carryovers are refused. Boolean flow predicates are shown even when their printed line is skipped.

## (helper) — `sd.other_forms`

- **Authored helper label:** Are there gains/losses from Forms 4797, 2439, 6252, 4684, 6781, 8824 or Schedule K-1?
- **Encoded (Bool):** Input — Are there gains/losses from Forms 4797, 2439, 6252, 4684, 6781, 8824 or Schedule K-1?
- Expr: `{"op":"input","source":"Are there gains/losses from Forms 4797, 2439, 6252, 4684, 6781, 8824 or Schedule K-1?"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.carryover`

- **Authored helper label:** Is there a capital loss carryover from the prior year?
- **Encoded (Bool):** Input — Is there a capital loss carryover from the prior year?
- Expr: `{"op":"input","source":"Is there a capital loss carryover from the prior year?"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.distributions`

- **Authored helper label:** Capital gain distributions, generally Form 1099-DIV box 2a
- **Encoded (NonNegDollars):** Input — Capital gain distributions, generally Form 1099-DIV box 2a
- Expr: `{"op":"input","source":"Capital gain distributions, generally Form 1099-DIV box 2a"}`
- Cite: [i1040sd] p. 11, line 13 (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sd.line18`

- **Authored helper label:** 28% Rate Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)
- **Encoded (NonNegDollars):** Enter the amount from g28 line 7.
- Expr: `{"from":"g28.line7","op":"copy"}`
- Cite: [i1040sd] p. 11, line 18 (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sd.line19`

- **Authored helper label:** Unrecaptured Section 1250 Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)
- **Encoded (NonNegDollars):** Enter the amount from u1250 line 18.
- Expr: `{"from":"u1250.line18","op":"copy"}`
- Cite: [i1040sd] pp. 11–12, line 19 (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sd.filing4952`

- **Authored helper label:** Are you filing Form 4952?
- **Encoded (Bool):** Enter the amount from f4952 helper "File for an election, or to claim interest when the exception does not apply".
- Expr: `{"from":"f4952.required","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.investment_election`

- **Authored helper label:** Form 4952 line 4g (supplied subtotal; Form 4952 deferred to Stage 4)
- **Encoded (NonNegDollars):** Enter the amount from f4952 helper "Validated default-allocation election".
- Expr: `{"from":"f4952.election","op":"copy"}`
- Cite: [i1040sd] p. 15, Schedule D Tax Worksheet applicability (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `sd.count`

- **Authored helper label:** Count screened transactions
- **Encoded (Count):** Add sales.one over every confirmed sales entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.one","op":"sum_over"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.screen`

- **Authored helper label:** Transaction screening dependency
- **Encoded (Bool):** helper "Count screened transactions" < 0 (a count)
- Note: Structural propagation gate: a valid Count is never negative, so true is unreachable. Unknown or refused transaction screening propagates through this test before any category filter can omit a transaction.
- Expr: `{"lt":["sd.count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.filed`

- **Authored helper label:** Schedule D required for entered sales or special distribution gains
- **Encoded (Bool):** (helper "Count screened transactions" > 0 (a count) or helper "28% Rate Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)" > $0 or helper "Unrecaptured Section 1250 Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)" > $0)
- Expr: `{"any":[{"gt":["sd.count",{"const":0,"type":"Count"}],"op":"test"},{"gt":["sd.line18",{"const":0}],"op":"test"},{"gt":["sd.line19",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.zero`

- **Authored helper label:** No amount on an inapplicable line
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1a(d) — `sd.line1a.d`

- **IRS:** Line 1a, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1a(e) — `sd.line1a.e`

- **IRS:** Line 1a, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1a(g) — `sd.line1a.g`

- **IRS:** Line 1a, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1a(h) — `sd.line1a.h`

- **IRS:** Line 1a, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1b(d) — `sd.line1b.d`

- **IRS:** Line 1b, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1b(e) — `sd.line1b.e`

- **IRS:** Line 1b, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1b(g) — `sd.line1b.g`

- **IRS:** Line 1b, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 1b(h) — `sd.line1b.h`

- **IRS:** Line 1b, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'A' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"A"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 2(d) — `sd.line2.d`

- **IRS:** Line 2, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"B"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 2(e) — `sd.line2.e`

- **IRS:** Line 2, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"B"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 2(g) — `sd.line2.g`

- **IRS:** Line 2, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"B"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 2(h) — `sd.line2.h`

- **IRS:** Line 2, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'B' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"B"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 3(d) — `sd.line3.d`

- **IRS:** Line 3, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"C"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 3(e) — `sd.line3.e`

- **IRS:** Line 3, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"C"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 3(g) — `sd.line3.g`

- **IRS:** Line 3, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"C"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 3(h) — `sd.line3.h`

- **IRS:** Line 3, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'C' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"C"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8a(d) — `sd.line8a.d`

- **IRS:** Line 8a, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8a(e) — `sd.line8a.e`

- **IRS:** Line 8a, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8a(g) — `sd.line8a.g`

- **IRS:** Line 8a, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8a(h) — `sd.line8a.h`

- **IRS:** Line 8a, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'aggregate', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"aggregate"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8b(d) — `sd.line8b.d`

- **IRS:** Line 8b, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8b(e) — `sd.line8b.e`

- **IRS:** Line 8b, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8b(g) — `sd.line8b.g`

- **IRS:** Line 8b, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 8b(h) — `sd.line8b.h`

- **IRS:** Line 8b, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'D' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"D"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 9(d) — `sd.line9.d`

- **IRS:** Line 9, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"E"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 9(e) — `sd.line9.e`

- **IRS:** Line 9, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"E"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 9(g) — `sd.line9.g`

- **IRS:** Line 9, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"E"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 9(h) — `sd.line9.h`

- **IRS:** Line 9, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'E' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"E"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 10(d) — `sd.line10.d`

- **IRS:** Line 10, column (d) totals
- **Encoded (NonNegDollars):** Add sales.proceeds over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.proceeds","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"F"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 10(e) — `sd.line10.e`

- **IRS:** Line 10, column (e) totals
- **Encoded (NonNegDollars):** Add sales.e over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.e","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"F"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 10(g) — `sd.line10.g`

- **IRS:** Line 10, column (g) totals
- **Encoded (Dollars):** Add sales.g over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.g","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"F"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 10(h) — `sd.line10.h`

- **IRS:** Line 10, column (h) totals
- **Encoded (Dollars):** Add sales.h over every confirmed sales entry for which helper "Classification from records: A/B/C short-term, D/E/F long-term; G–L digital assets" = 'F' and helper "Report this transaction in detail on Form 8949 or directly in Schedule D aggregate totals" = 'detail', within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sd.screen is true, cannot complete Schedule D. Resolve transaction screening before calculating totals. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"collection":"sales","field":"sales.h","op":"sum_over","where":{"all":[{"eq":["sales.box",{"const":"F"}],"op":"test"},{"eq":["sales.route",{"const":"detail"}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 4 — `sd.line4`

- **IRS:** Line 4: zero only after unsupported source/carryover screening
- **Encoded (Dollars):** Enter the amount from helper "No amount on an inapplicable line".
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"from":"sd.zero","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 5 — `sd.line5`

- **IRS:** Line 5: zero only after unsupported source/carryover screening
- **Encoded (Dollars):** Enter the amount from helper "No amount on an inapplicable line".
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"from":"sd.zero","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 6 — `sd.line6`

- **IRS:** Line 6: zero only after unsupported source/carryover screening
- **Encoded (Dollars):** Enter the amount from helper "No amount on an inapplicable line".
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"from":"sd.zero","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 11 — `sd.line11`

- **IRS:** Line 11: zero only after unsupported source/carryover screening
- **Encoded (Dollars):** Enter the amount from helper "No amount on an inapplicable line".
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"from":"sd.zero","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 12 — `sd.line12`

- **IRS:** Line 12: zero only after unsupported source/carryover screening
- **Encoded (Dollars):** Enter the amount from helper "No amount on an inapplicable line".
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"from":"sd.zero","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 14 — `sd.line14`

- **IRS:** Line 14: zero only after unsupported source/carryover screening
- **Encoded (Dollars):** Enter the amount from helper "No amount on an inapplicable line".
- **Refusal:** when sd.other_forms is true, cannot complete Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- **Refusal:** when sd.carryover is true, cannot complete Capital Loss Carryover Worksheet. Prior-year capital loss carryovers are unsupported; prepare the carryover worksheet. Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)
- Expr: `{"from":"sd.zero","op":"copy"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 13 — `sd.line13`

- **IRS:** Capital gain distributions
- **Encoded (NonNegDollars):** Add helper "Capital gain distributions, generally Form 1099-DIV box 2a" and div helper "Zero only after distribution scope checks".
- Expr: `{"of":["sd.distributions","div.screen"],"op":"sum"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 7 — `sd.line7`

- **IRS:** Combine the amounts for Schedule D line 7
- **Encoded (Dollars):** Add line 1a(h), line 1b(h), line 2(h), line 3(h), line 4, line 5, and line 6.
- Expr: `{"of":["sd.line1a.h","sd.line1b.h","sd.line2.h","sd.line3.h","sd.line4","sd.line5","sd.line6"],"op":"sum"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 15 — `sd.line15`

- **IRS:** Combine the amounts for Schedule D line 15
- **Encoded (Dollars):** Add line 8a(h), line 8b(h), line 9(h), line 10(h), line 11, line 12, line 13, and line 14.
- Expr: `{"of":["sd.line8a.h","sd.line8b.h","sd.line9.h","sd.line10.h","sd.line11","sd.line12","sd.line13","sd.line14"],"op":"sum"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 16 — `sd.line16`

- **IRS:** Combine the amounts for Schedule D line 16
- **Encoded (Dollars):** Add line 7 and line 15.
- Expr: `{"of":["sd.line7","sd.line15"],"op":"sum"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 17 — `sd.line17`

- **IRS:** Are lines 15 and 16 both gains?
- **Encoded (Bool):** line 15 > $0 and line 16 > $0
- Expr: `{"all":[{"gt":["sd.line15",{"const":0}],"op":"test"},{"gt":["sd.line16",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 20 — `sd.line20`

- **IRS:** Are lines 18 and 19 zero and are you not filing Form 4952?
- **Encoded (Bool):** helper "28% Rate Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)" = $0 and helper "Unrecaptured Section 1250 Gain Worksheet result (supplied subtotal; worksheet deferred to Stage 4)" = $0 and helper "Are you filing Form 4952?" = false
- Expr: `{"all":[{"eq":["sd.line18",{"const":0}],"op":"test"},{"eq":["sd.line19",{"const":0}],"op":"test"},{"eq":["sd.filing4952",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.loss_limit`

- **Authored helper label:** Signed annual capital loss limit
- **Encoded (Dollars):** Enter single -$3,000; mfj -$3,000; mfs -$1,500; hoh -$3,000; qss -$3,000 (sd.loss_limit).
- Expr: `{"op":"param","ref":"sd.loss_limit"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.limited_loss`

- **Authored helper label:** Loss limited to the annual deduction
- **Encoded (Dollars):** Enter the larger of line 16 or helper "Signed annual capital loss limit".
- Expr: `{"of":["sd.line16","sd.loss_limit"],"op":"larger_of"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.has_loss`

- **Authored helper label:** Line 16 is a loss
- **Encoded (Bool):** line 16 < $0
- Expr: `{"lt":["sd.line16",{"const":0}],"op":"test"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 21 — `sd.line21`

- **IRS:** Deductible loss, signed; zero when line 21 is skipped
- **Encoded (Dollars):** Choose — [helper "Line 16 is a loss" = true → helper "Loss limited to the annual deduction"] [helper "Line 16 is a loss" = false → helper "No amount on an inapplicable line"]
- Expr: `{"alternatives":[{"guard":{"eq":["sd.has_loss",{"const":true}],"op":"test"},"then":"sd.limited_loss"},{"guard":{"eq":["sd.has_loss",{"const":false}],"op":"test"},"then":"sd.zero"}],"op":"choose"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## 22 — `sd.line22`

- **IRS:** Do you have qualified dividends?
- **Encoded (Bool):** f1040 line 3a > $0
- Expr: `{"gt":["f1040.line3a",{"const":0}],"op":"test"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.to1040`

- **Authored helper label:** Capital gain or limited capital loss for Form 1040 line 7a
- **Encoded (Dollars):** Choose — [helper "Line 16 is a loss" = true → line 21] [helper "Line 16 is a loss" = false → line 16]
- Expr: `{"alternatives":[{"guard":{"eq":["sd.has_loss",{"const":true}],"op":"test"},"then":"sd.line21"},{"guard":{"eq":["sd.has_loss",{"const":false}],"op":"test"},"then":"sd.line16"}],"op":"choose"}`
- Cite: [f1040sd] Schedule D (2025), Parts I–III (2025; created 2025-10-06; sha256 90564c8b)

## (helper) — `sd.net_gain_raw`

- **Authored helper label:** Smaller of Schedule D lines 15 and 16
- **Encoded (Dollars):** Enter the smaller of line 15 or line 16.
- Expr: `{"of":["sd.line15","sd.line16"],"op":"smaller_of"}`
- Cite: [i1040gi] QDCGT worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sd.net_gain`

- **Authored helper label:** Nonnegative net capital gain for QDCGT
- **Encoded (NonNegDollars):** Subtract $0 from helper "Smaller of Schedule D lines 15 and 16". If zero or less, enter -0-.
- Expr: `{"from":"sd.net_gain_raw","op":"subtract_floor0","take":{"const":0}}`
- Cite: [i1040gi] QDCGT worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)
