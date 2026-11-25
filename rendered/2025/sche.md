# Schedule E, Part I — totals (rental real estate and royalties)

- Document: `sche` (form, tax year 2025)
- Note: Totals of Schedule E Part I over the rental and royalty entries; line 41 is line 26 (Parts II to IV are refused). Refused: a real estate professional, rentals grouped as one activity, and a rental that is a trade or business.

## (helper) — `sche.no`

- **Authored helper label:** No (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [i1040se] p. 1, Line 26 (2025; sha256 ad71de35)

## (helper) — `sche.re_pro`

- **Authored helper label:** Real estate professional
- **Encoded (Bool):** Input — Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all your work time?
- Expr: `{"op":"input","source":"Did you (or your spouse) work more than 750 hours in 2025 in real estate businesses, and more than half of all your work time?"}`
- Cite: [i1040se] p. 3, Real estate professionals (2025; sha256 ad71de35)

## (helper) — `sche.grouped`

- **Authored helper label:** A rental grouped with another activity
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) treat a rental and another activity, such as another rental or a business, as one activity?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) treat a rental and another activity, such as another rental or a business, as one activity?"}`
- Cite: [i8582] p. 1, Grouping of Activities; p. 6, Limitation on grouping certain activities, "A rental activity with a trade or business activity unless the activities being grouped together make up an appropriate economic unit" (2025; sha256 76787e11)

## (helper) — `sche.qbi_business`

- **Authored helper label:** A rental that is a trade or business
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) run any of your rentals as a business, renting it out to make money and being involved in it regularly and continuously?
- Interpretation: amb.2025.rental_not_qbi
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) run any of your rentals as a business, renting it out to make money and being involved in it regularly and continuously?"}`
- Cite: [i8995] p. 1, Trade or business, "an activity qualifies as a trade or business if your primary purpose for engaging in the activity is for income or profit and you’re involved in the activity with continuity and regularity"; p. 2, "may still be treated as a trade or business for purposes of the QBI deduction if it’s a section 162 trade or business"; p. 1, "provides a safe harbor under which a rental real estate enterprise will be treated as a trade or business for purposes of the QBI deduction" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `sche.accrual`

- **Authored helper label:** Rental books kept on the accrual method
- **Encoded (Bool):** Input — Do you keep the books for your rentals on the accrual method, counting rent when earned and costs when owed rather than when received or paid?
- Expr: `{"op":"input","source":"Do you keep the books for your rentals on the accrual method, counting rent when earned and costs when owed rather than when received or paid?"}`
- Cite: [p527] p. 4, When To Deduct, "If you use the accrual method, see Pub. 538 for more information" (2025; sha256 20c826e9)

## (helper) — `sche.rents`

- **Authored helper label:** Rents of all reported rental properties
- **Encoded (NonNegDollars):** Add rental.line3 over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.line3","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [f1040se] Schedule E (2025), line 23a, "Total of all amounts reported on line 3 for all rental properties" (2025; sha256 c5e2c8fa)

## 23a — `sche.line23a`

- **IRS:** Total of all amounts reported on line 3 for all rental properties
- **Encoded (NonNegDollars):** Enter the amount from helper "Rents of all reported rental properties".
- Expr: `{"from":"sche.rents","op":"copy"}`
- Cite: [f1040se] Schedule E (2025), line 23a (2025; sha256 c5e2c8fa)

## 23b — `sche.line23b`

- **IRS:** Total of all amounts reported on line 4 for all royalty properties
- **Encoded (NonNegDollars):** Add royalty.line4 over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.line4","op":"sum_over"}`
- Cite: [f1040se] Schedule E (2025), line 23b (2025; sha256 c5e2c8fa)

## 23c — `sche.line23c`

- **IRS:** Total of all amounts reported on line 12 for all properties
- **Encoded (NonNegDollars):** Add rental.line12 over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.line12","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [f1040se] Schedule E (2025), line 23c (2025; sha256 c5e2c8fa)

## 23d — `sche.line23d`

- **IRS:** Total of all amounts reported on line 18 for all properties
- **Encoded (NonNegDollars):** Add rental.line18 over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.line18","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [f1040se] Schedule E (2025), line 23d (2025; sha256 c5e2c8fa)

## (helper) — `sche.rent_exp`

- **Authored helper label:** Line 20 of all reported rental properties
- **Encoded (NonNegDollars):** Add rental.line20 over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.line20","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [f1040se] Schedule E (2025), line 23e, "Total of all amounts reported on line 20 for all properties" (2025; sha256 c5e2c8fa)

## (helper) — `sche.roy_exp`

- **Authored helper label:** Line 20 of all royalty properties
- **Encoded (NonNegDollars):** Add royalty.line20 over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.line20","op":"sum_over"}`
- Cite: [f1040se] Schedule E (2025), line 23e (2025; sha256 c5e2c8fa)

## 23e — `sche.line23e`

- **IRS:** Total of all amounts reported on line 20 for all properties
- **Encoded (NonNegDollars):** Add helper "Line 20 of all reported rental properties" and helper "Line 20 of all royalty properties".
- Expr: `{"of":["sche.rent_exp","sche.roy_exp"],"op":"sum"}`
- Cite: [f1040se] Schedule E (2025), line 23e (2025; sha256 c5e2c8fa)

## (helper) — `sche.rent_income`

- **Authored helper label:** Positive line 21 of rental properties
- **Encoded (NonNegDollars):** Add rental.net_income over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.net_income","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [f1040se] Schedule E (2025), line 24, "Add positive amounts shown on line 21" (2025; sha256 c5e2c8fa)

## (helper) — `sche.roy_income`

- **Authored helper label:** Positive line 21 of royalty properties
- **Encoded (NonNegDollars):** Add royalty.income over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.income","op":"sum_over"}`
- Cite: [f1040se] Schedule E (2025), line 24, "Add positive amounts shown on line 21" (2025; sha256 c5e2c8fa)

## 24 — `sche.line24`

- **IRS:** Income. Add positive amounts shown on line 21. Do not include any losses
- **Encoded (NonNegDollars):** Add helper "Positive line 21 of rental properties" and helper "Positive line 21 of royalty properties".
- Expr: `{"of":["sche.rent_income","sche.roy_income"],"op":"sum"}`
- Cite: [f1040se] Schedule E (2025), line 24 (2025; sha256 c5e2c8fa)

## (helper) — `sche.rent_loss`

- **Authored helper label:** Line 22 of rental properties
- **Encoded (Dollars):** Add rental.line22 over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.line22","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [f1040se] Schedule E (2025), line 25, "rental real estate losses from line 22" (2025; sha256 c5e2c8fa)

## (helper) — `sche.roy_loss`

- **Authored helper label:** Royalty losses from line 21
- **Encoded (Dollars):** Add royalty.loss over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.loss","op":"sum_over"}`
- Cite: [f1040se] Schedule E (2025), line 25 (2025; sha256 c5e2c8fa)

## 25 — `sche.line25`

- **IRS:** Losses. Add royalty losses from line 21 and rental real estate losses from line 22
- **Encoded (Dollars):** Add helper "Line 22 of rental properties" and helper "Royalty losses from line 21".
- Expr: `{"of":["sche.rent_loss","sche.roy_loss"],"op":"sum"}`
- Cite: [f1040se] Schedule E (2025), line 25 (2025; sha256 c5e2c8fa)

## 26 — `sche.line26`

- **IRS:** Total rental real estate and royalty income or (loss). Combine lines 24 and 25
- **Encoded (Dollars):** Add line 24 and line 25.
- **Refusal:** when sche.re_pro is true, cannot complete Schedule E, line 43 (real estate professional). A real estate professional's rentals are outside this tool. Cite: [i1040se] p. 3, Real estate professionals (2025; sha256 ad71de35)
- **Refusal:** when sche.grouped is true, cannot complete Form 8582 (activities grouped). Rentals treated as one activity are outside this tool. Cite: [i8582] p. 1, Grouping of Activities (2025; sha256 76787e11)
- **Refusal:** when sche.qbi_business is true, cannot complete Form 8995 (rental real estate as a trade or business). A rental that is a trade or business is outside this tool. Cite: [i8995] p. 1, Trade or business, "provides a safe harbor under which a rental real estate enterprise will be treated as a trade or business for purposes of the QBI deduction" (2025; printed date 2026-01-26; sha256 875843ba)
- **Refusal:** when sche.accrual is true, cannot complete Schedule E, Part I (accrual method). Rentals kept on the accrual method are outside this tool. Cite: [p527] p. 4, When To Deduct, "If you use the accrual method, see Pub. 538 for more information" (2025; sha256 20c826e9)
- Expr: `{"of":["sche.line24","sche.line25"],"op":"sum"}`
- Cite: [f1040se] Schedule E (2025), line 26 (2025; sha256 c5e2c8fa)

## 41 — `sche.line41`

- **IRS:** Total income or (loss). Combine lines 26, 32, 37, 39, and 40
- **Encoded (Dollars):** Enter the amount from line 26.
- Note: Parts II to IV and line 40 are refused (scope.k1, scope.remic, scope.farm).
- Expr: `{"from":"sche.line26","op":"copy"}`
- Cite: [f1040se] Schedule E (2025), line 41 (2025; sha256 c5e2c8fa)

## (helper) — `sche.loss_prelimit`

- **Authored helper label:** Rental net losses and royalty losses on line 21, before the passive activity limit (positive)
- **Encoded (NonNegDollars):** Add helper "Rental net losses on line 21 (positive)" and helper "Royalty losses on line 21 (positive)".
- Interpretation: amb.2025.s1_ebl_rental
- Expr: `{"of":["sche.rent_netloss","sche.roy_lossabs"],"op":"sum"}`
- Cite: [i1040se] p. 1, Reminders, "If you report a loss on line 26, 32, 37, or 39 of your Schedule E (Form 1040), you may be subject to a business loss limitation" (2025; sha256 ad71de35)

## (helper) — `sche.rent_netloss`

- **Authored helper label:** Rental net losses on line 21 (positive)
- **Encoded (NonNegDollars):** Add rental.net_loss over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.net_loss","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [i1040se] p. 1, Reminders (2025; sha256 ad71de35)

## (helper) — `sche.roy_lossabs`

- **Authored helper label:** Royalty losses on line 21 (positive)
- **Encoded (NonNegDollars):** Add royalty.loss_abs over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.loss_abs","op":"sum_over"}`
- Cite: [i1040se] p. 1, Reminders (2025; sha256 ad71de35)

## (helper) — `sche.nonpassive_net`

- **Authored helper label:** Royalty income or loss (not passive), for modified adjusted gross income on Form 8582
- **Encoded (Dollars):** Add royalty.line21 over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.line21","op":"sum_over"}`
- Cite: [i8582] p. 11, Line 6, "Include in modified adjusted gross income any portfolio income" (2025; sha256 76787e11)

## (helper) — `sche.count`

- **Authored helper label:** Number of reported rental and royalty properties
- **Encoded (Count):** Add helper "Number of reported rental properties" and helper "Number of royalty properties".
- Expr: `{"of":["sche.rental_count","sche.royalty_count"],"op":"sum"}`
- Cite: [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)

## (helper) — `sche.rental_count`

- **Authored helper label:** Number of reported rental properties
- **Encoded (Count):** Add rental.one over every confirmed rental entry for which helper "The property is reported on Schedule E (not excluded)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rental","field":"rental.one","op":"sum_over","where":{"eq":["rental.reported",{"const":true}],"op":"test"}}`
- Cite: [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)

## (helper) — `sche.royalty_count`

- **Authored helper label:** Number of royalty properties
- **Encoded (Count):** Add royalty.one over every confirmed royalty entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"royalty","field":"royalty.one","op":"sum_over"}`
- Cite: [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)

## (helper) — `sche.any_listed`

- **Authored helper label:** A rental is reported, or a royalty is listed
- **Encoded (Bool):** helper "Number of reported rental and royalty properties" > 0 (a count)
- Expr: `{"gt":["sche.count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)

## (gate) — `sche.any`

- **Authored helper label:** Schedule E is filed (a rental reported or a royalty listed)
- **Encoded (Bool):** Choose — [scope helper "In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?" = true → helper "A rental is reported, or a royalty is listed"] [scope helper "In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.rental",{"const":true}],"op":"test"},"then":"sche.any_listed"},{"guard":{"eq":["scope.rental",{"const":false}],"op":"test"},"then":"sche.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 40, Step 2, "You are filing Schedule E" (2025; printed date 2026-02-25; sha256 482e9c48)
