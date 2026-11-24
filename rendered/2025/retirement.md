# Form 1099-R distributions (IRAs, pensions and annuities)

- Document: `retirement` (form, tax year 2025)
- Collection: keyed entries within person; [i1040gi] pp. 26-30, lines 4a-5b ('If you ... received more than one distribution, figure the taxable amount of each distribution') (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: One entry per Form 1099-R. IRA distributions go to Form 1040 lines 4a and 4b, pensions and annuities to lines 5a and 5b. The Simplified Method Worksheet is figured for each annuity with after-tax cost.

## (helper) — `retirement.account`

- **Authored helper label:** Kind of account the distribution came from
- **Encoded (Enum(retirement_account)):** Input — Kind of account: traditional_ira (the IRA/SEP/SIMPLE box on Form 1099-R is checked; includes SEP and traditional SIMPLE IRAs), roth_ira (a Roth IRA or Roth SIMPLE IRA), or plan (a pension, annuity, 401(k), 403(b) or governmental 457(b) plan)
- Expr: `{"op":"input","source":"Kind of account: traditional_ira (the IRA/SEP/SIMPLE box on Form 1099-R is checked; includes SEP and traditional SIMPLE IRAs), roth_ira (a Roth IRA or Roth SIMPLE IRA), or plan (a pension, annuity, 401(k), 403(b) or governmental 457(b) plan)"}`
- Cite: [f1099r] Instructions for Recipient, IRA/SEP/SIMPLE box; i1040gi pp. 26 and 28, lines 4a-4b and 5a-5b (2025 (calendar-year form); sha256 d6b7be48)

## (helper) — `retirement.code`

- **Authored helper label:** Distribution code in box 7
- **Encoded (Enum(retirement_code)):** Input — Distribution code in box 7: normal_7, death_4, early_exception_2, early_1 (code 1, early distribution, no known exception), simple_S (code S, SIMPLE IRA in its first 2 years), disability_3 (code 3, disability), direct_rollover_G, qualified_roth_Q, or other (any other code, or two codes)
- Expr: `{"op":"input","source":"Distribution code in box 7: normal_7, death_4, early_exception_2, early_1 (code 1, early distribution, no known exception), simple_S (code S, SIMPLE IRA in its first 2 years), disability_3 (code 3, disability), direct_rollover_G, qualified_roth_Q, or other (any other code, or two codes)"}`
- Cite: [f1099r] Instructions for Recipient, Box 7 (2025 (calendar-year form); sha256 d6b7be48)

## (helper) — `retirement.box1`

- **Authored helper label:** Gross distribution, box 1
- **Encoded (NonNegDollars):** Input — Gross distribution, Form 1099-R box 1
- Expr: `{"op":"input","source":"Gross distribution, Form 1099-R box 1"}`
- Cite: [f1099r] Instructions for Recipient, Box 1 (2025 (calendar-year form); sha256 d6b7be48)

## (helper) — `retirement.box5`

- **Authored helper label:** Employee contributions recovered tax free, box 5
- **Encoded (NonNegDollars):** Input — Employee contributions, designated Roth contributions or insurance premiums, Form 1099-R box 5 (a pension or annuity; zero for an IRA)
- Expr: `{"op":"input","source":"Employee contributions, designated Roth contributions or insurance premiums, Form 1099-R box 5 (a pension or annuity; zero for an IRA)"}`
- Cite: [f1099r] Instructions for Recipient, Box 5 (2025 (calendar-year form); sha256 d6b7be48)

## (helper) — `retirement.rollover`

- **Authored helper label:** Amount you rolled over to a qualified plan or IRA (not a Roth account) within 60 days, or later under a waiver or frozen-deposit extension, or recontributed to an IRA within 120 days after a first-home purchase was canceled or delayed
- **Encoded (NonNegDollars):** Input — Amount of this distribution you rolled over within 60 days to a qualified plan or an IRA other than a Roth IRA (for a direct rollover, code G, the whole distribution is treated as rolled over).

  Also count:
  - an amount rolled over after the 60 days if the 60-day requirement was waived (you qualify for an automatic waiver, you self-certify that you meet the requirements of a waiver, or you received a private letter ruling granting a waiver) or the period was extended because the amount was a frozen deposit
  - an IRA distribution to buy, build or rebuild a first home that you contributed back to a traditional IRA within 120 days of the distribution because the purchase or construction was canceled or delayed

  Do not count any part of a required minimum distribution, which is not eligible for rollover, nor any of these from a pension, annuity, 401(k), 403(b) or 457(b) plan:

  - any part of a series of substantially equal payments over your life or life expectancy (or yours and your beneficiary's) or over 10 years or more
  - a hardship distribution
  - dividends on employer securities
  - the cost of life insurance coverage

  If you received this distribution as a beneficiary other than the surviving spouse, count nothing: such a beneficiary cannot roll over money paid to them (a direct transfer to an inherited IRA is reported with codes 4 and G, another code).

  If this distribution is from an IRA and went back into an IRA, count none of it if, in the 12 months before this distribution, you had already rolled over another IRA distribution to an IRA (a trustee-to-trustee transfer, or a rollover to a Roth IRA, does not count as such a rollover).

  For code S (a SIMPLE IRA in its first 2 years), count only an amount rolled over to another SIMPLE IRA.

  Do not count an amount rolled over into a SIMPLE IRA during the first 2 years of your participation in that SIMPLE IRA unless it came from another SIMPLE IRA.
- Expr: `{"op":"input","source":"Amount of this distribution you rolled over within 60 days to a qualified plan or an IRA other than a Roth IRA (for a direct rollover, code G, the whole distribution is treated as rolled over).\n\nAlso count:\n- an amount rolled over after the 60 days if the 60-day requirement was waived (you qualify for an automatic waiver, you self-certify that you meet the requirements of a waiver, or you received a private letter ruling granting a waiver) or the period was extended because the amount was a frozen deposit\n- an IRA distribution to buy, build or rebuild a first home that you contributed back to a traditional IRA within 120 days of the distribution because the purchase or construction was canceled or delayed\n\nDo not count any part of a required minimum distribution, which is not eligible for rollover, nor any of these from a pension, annuity, 401(k), 403(b) or 457(b) plan:\n\n- any part of a series of substantially equal payments over your life or life expectancy (or yours and your beneficiary's) or over 10 years or more\n- a hardship distribution\n- dividends on employer securities\n- the cost of life insurance coverage\n\nIf you received this distribution as a beneficiary other than the surviving spouse, count nothing: such a beneficiary cannot roll over money paid to them (a direct transfer to an inherited IRA is reported with codes 4 and G, another code).\n\nIf this distribution is from an IRA and went back into an IRA, count none of it if, in the 12 months before this distribution, you had already rolled over another IRA distribution to an IRA (a trustee-to-trustee transfer, or a rollover to a Roth IRA, does not count as such a rollover).\n\nFor code S (a SIMPLE IRA in its first 2 years), count only an amount rolled over to another SIMPLE IRA.\n\nDo not count an amount rolled over into a SIMPLE IRA during the first 2 years of your participation in that SIMPLE IRA unless it came from another SIMPLE IRA."}`
- Cite: [i1040gi] p. 27, Exception 1 (IRA rollovers); p. 30, Rollovers; p575 p. 21, Eligible rollover distribution, "An eligible rollover distribution is any distribution of all or any part of the balance to your credit in a qualified retirement plan except the following." and "A required minimum distribution (RMD)"; p590b p. 6, Distributions not eligible for rollover, "Amounts that must be distributed (required minimum distributions) during a particular year aren't eligible for rollover treatment."; p575 p. 21, Eligible rollover distribution, "Any of a series of substantially equal distributions paid at least once a year over", "Hardship distributions.", "Dividends paid on employer securities.", "The cost of life insurance coverage." and "a distribution to the plan participant’s beneficiary isn’t generally treated as an eligible rollover distribution"; p575 p. 24, Rollovers by nonspouse beneficiary, "The distribution must be a direct trustee-to-trustee transfer to your traditional or Roth IRA that was set up to receive the distribution."; p590b p. 5, Inherited from someone other than spouse, "you can't roll over any amounts into or out of the inherited IRA"; p590a p. 25, Application of one-rollover-per-year limitation, "You can make only one rollover from an IRA to another (or the same) IRA in any 1-year period regardless of the number of IRAs you own"; p560 p. 18, Distributions (Withdrawals), "a rollover from a SIMPLE IRA to a non-SIMPLE IRA can be made tax free only after a 2-year participation in the SIMPLE IRA plan"; p575 p. 21, Rollovers to SIMPLE retirement accounts, "During the first 2 years of participation in a SIMPLE retirement account, you may roll over amounts from one SIMPLE retirement account into another SIMPLE retirement account"; p575 p. 23, Ways to get a waiver of the 60-day rollover requirement, "There are three ways to obtain a waiver of the 60-day requirement." and Frozen deposits, "The 60-day rollover period is extended by the period for which the amount is a frozen deposit"; p590b p. 28, "the purchase or construction was canceled or delayed, you could generally contribute the amount of the distribution to an IRA within 120 days of the distribution and not pay income tax or the 10% additional tax on early distributions. This contribution is treated as a rollover contribution to the IRA." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.no`

- **Authored helper label:** Year parameter s3.no (false)
- **Encoded (Bool):** Enter false (s3.no).
- Expr: `{"op":"param","ref":"s3.no"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.rollover_any`

- **Authored helper label:** Did any of this money go into a retirement account again (a rollover or a conversion), even if it was first paid to you?
- **Encoded (Bool):** Input — Did any of this money go into a retirement account again (a rollover or a conversion), even if it was first paid to you?
- Expr: `{"op":"input","source":"Did any of this money go into a retirement account again (a rollover or a conversion), even if it was first paid to you?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.rolled_some`

- **Authored helper label:** The filer put some of this money into a retirement account (asked unless the form is a direct rollover, code G)
- **Encoded (Bool):** helper "Did any of this money go into a retirement account again (a rollover or a conversion), even if it was first paid to you?" = true
- Expr: `{"eq":["retirement.rollover_any",{"const":true}],"op":"test"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.put_back`

- **Authored helper label:** Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)
- **Encoded (Bool):** Choose — [helper "Direct rollover (code G)" = true → helper "Direct rollover (code G)"] [helper "Direct rollover (code G)" = false → helper "The filer put some of this money into a retirement account (asked unless the form is a direct rollover, code G)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.direct",{"const":true}],"op":"test"},"then":"retirement.direct"},{"guard":{"eq":["retirement.direct",{"const":false}],"op":"test"},"then":"retirement.rolled_some"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.rollover_if_any`

- **Authored helper label:** Amount rolled over, asked only when some of the money went into another retirement account (none otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Did any of this money go into a retirement account again (a rollover or a conversion), even if it was first paid to you?" = true → helper "Amount you rolled over to a qualified plan or IRA (not a Roth account) within 60 days, or later under a waiver or frozen-deposit extension, or recontributed to an IRA within 120 days after a first-home purchase was canceled or delayed"] [helper "Did any of this money go into a retirement account again (a rollover or a conversion), even if it was first paid to you?" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.rollover_any",{"const":true}],"op":"test"},"then":"retirement.rollover"},{"guard":{"eq":["retirement.rollover_any",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.is_trad`

- **Authored helper label:** A traditional, SEP or SIMPLE IRA
- **Encoded (Bool):** helper "Kind of account the distribution came from" = 'traditional_ira'
- Expr: `{"eq":["retirement.account",{"const":"traditional_ira"}],"op":"test"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.is_death`

- **Authored helper label:** Code 4 (death)
- **Encoded (Bool):** helper "Distribution code in box 7" = 'death_4'
- Expr: `{"eq":["retirement.code",{"const":"death_4"}],"op":"test"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.plan_death`

- **Authored helper label:** A payment from a plan to a beneficiary (code 4, not an IRA)
- **Encoded (Bool):** helper "IRA distribution (lines 4a and 4b)" = false and helper "Code 4 (death)" = true
- Expr: `{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.is_death",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.roth_moved`

- **Authored helper label:** Did any of this money go into a Roth IRA or another Roth account?
- **Encoded (Bool):** Input — Did any of this money go into a Roth IRA or another Roth account?
- Expr: `{"op":"input","source":"Did any of this money go into a Roth IRA or another Roth account?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.roth_moved_if_put_back`

- **Authored helper label:** Did any of this money go into a Roth IRA or another Roth account? Asked only with some of the money went into another retirement account (false otherwise)
- **Encoded (Bool):** Choose — [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = true → helper "Did any of this money go into a Roth IRA or another Roth account?"] [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.put_back",{"const":true}],"op":"test"},"then":"retirement.roth_moved"},{"guard":{"eq":["retirement.put_back",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.rollover_property`

- **Authored helper label:** Did the plan or IRA pay out anything other than cash (such as shares) that was then sold, kept, or put only partly into the new account?
- **Encoded (Bool):** Input — Did the plan or IRA pay out anything other than cash (such as shares) that was then sold, kept, or put only partly into the new account?
- Expr: `{"op":"input","source":"Did the plan or IRA pay out anything other than cash (such as shares) that was then sold, kept, or put only partly into the new account?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.rollover_property_if_put_back`

- **Authored helper label:** Did the plan or IRA pay out anything other than cash (such as shares) that was then sold, kept, or put only partly into the new account? Asked only with some of the money went into another retirement account (false otherwise)
- **Encoded (Bool):** Choose — [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = true → helper "Did the plan or IRA pay out anything other than cash (such as shares) that was then sold, kept, or put only partly into the new account?"] [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.put_back",{"const":true}],"op":"test"},"then":"retirement.rollover_property"},{"guard":{"eq":["retirement.put_back",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.rollover_qdro`

- **Authored helper label:** Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)?
- **Encoded (Bool):** Input — Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)?
- Expr: `{"op":"input","source":"Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.rollover_qdro_if_put_back`

- **Authored helper label:** Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)? Asked only with some of the money went into another retirement account (false otherwise)
- **Encoded (Bool):** Choose — [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = true → helper "Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)?"] [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.put_back",{"const":true}],"op":"test"},"then":"retirement.rollover_qdro"},{"guard":{"eq":["retirement.put_back",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.levy_returned`

- **Authored helper label:** Was this money taken by the IRS under a levy and later returned to you?
- **Encoded (Bool):** Input — Was this money taken by the IRS under a levy and later returned to you?
- Expr: `{"op":"input","source":"Was this money taken by the IRS under a levy and later returned to you?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.levy_returned_if_put_back`

- **Authored helper label:** Was this money taken by the IRS under a levy and later returned to you? Asked only with some of the money went into another retirement account (false otherwise)
- **Encoded (Bool):** Choose — [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = true → helper "Was this money taken by the IRS under a levy and later returned to you?"] [helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.put_back",{"const":true}],"op":"test"},"then":"retirement.levy_returned"},{"guard":{"eq":["retirement.put_back",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.death_put_back`

- **Authored helper label:** A payment to a beneficiary (code 4) of which some went into another retirement account
- **Encoded (Bool):** helper "Code 4 (death)" = true and helper "Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)" = true
- Expr: `{"all":[{"eq":["retirement.is_death",{"const":true}],"op":"test"},{"eq":["retirement.put_back",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p590b] p. 5, Inherited from someone other than spouse, "you can't roll over any amounts into or out of the inherited IRA" (2025; sha256 d18a592e)

## (helper) — `retirement.rollover_nonspouse`

- **Authored helper label:** Did you inherit this money from someone other than your spouse?
- **Encoded (Bool):** Input — Did you inherit this money from someone other than your spouse?
- Expr: `{"op":"input","source":"Did you inherit this money from someone other than your spouse?"}`
- Cite: [p590b] p. 5, Inherited from someone other than spouse, "you can't roll over any amounts into or out of the inherited IRA. However, you can make a trustee-to-trustee transfer"; p575 p. 24, Rollovers by nonspouse beneficiary, "The distribution must be a direct trustee-to-trustee transfer to your traditional or Roth IRA that was set up to receive the distribution." (2025; sha256 d18a592e)

## (helper) — `retirement.nonspouse_beneficiary`

- **Authored helper label:** Inherited from someone other than the spouse: for an IRA, the inherited-IRA answer (retirement.sav_inherited); for a plan, the plan question
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = true → helper "Is this a distribution from an inherited IRA that you received as a beneficiary other than the owner's spouse?"] [helper "IRA distribution (lines 4a and 4b)" = false → helper "Inherited from someone other than the spouse, asked of a plan payment to a beneficiary (code 4) of which some went into another retirement account (false otherwise; for an IRA the inherited-IRA question asks it)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.sav_inherited"},{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.rollover_nonspouse_if_plan"}],"op":"choose"}`
- Cite: [p590b] p. 5, Inherited from someone other than spouse, "you can't roll over any amounts into or out of the inherited IRA" (2025; sha256 d18a592e)

## (gate) — `retirement.rollover_nonspouse_if_plan`

- **Authored helper label:** Inherited from someone other than the spouse, asked of a plan payment to a beneficiary (code 4) of which some went into another retirement account (false otherwise; for an IRA the inherited-IRA question asks it)
- **Encoded (Bool):** Choose — [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = true → helper "Did you inherit this money from someone other than your spouse?"] [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.plan_death",{"const":true}],"op":"test"},"then":"retirement.rollover_nonspouse"},{"guard":{"eq":["retirement.plan_death",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [p590b] p. 5, Inherited from someone other than spouse, "you can't roll over any amounts into or out of the inherited IRA"; p575 p. 24, Rollovers by nonspouse beneficiary, "The distribution must be a direct trustee-to-trustee transfer to your traditional or Roth IRA that was set up to receive the distribution." (2025; sha256 d18a592e)

## (gate) — `retirement.rollover_nonspouse_if_death`

- **Authored helper label:** Inherited from someone other than the spouse (the inherited-IRA answer for an IRA, the plan question for a plan), read only for a beneficiary (code 4) who put some of the money into another retirement account (false otherwise)
- **Encoded (Bool):** Choose — [helper "A payment to a beneficiary (code 4) of which some went into another retirement account" = true → helper "Inherited from someone other than the spouse: for an IRA, the inherited-IRA answer (retirement.sav_inherited); for a plan, the plan question"] [helper "A payment to a beneficiary (code 4) of which some went into another retirement account" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.death_put_back",{"const":true}],"op":"test"},"then":"retirement.nonspouse_beneficiary"},{"guard":{"eq":["retirement.death_put_back",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [p590b] p. 5, Inherited from someone other than spouse, "you can't roll over any amounts into or out of the inherited IRA" (2025; sha256 d18a592e)

## (helper) — `retirement.ira_put_back`

- **Authored helper label:** An IRA distribution, not a direct rollover (code G), of which the filer put some into another retirement account
- **Encoded (Bool):** helper "IRA distribution (lines 4a and 4b)" = true and helper "Direct rollover (code G)" = false and helper "The filer put some of this money into a retirement account (asked unless the form is a direct rollover, code G)" = true
- Expr: `{"all":[{"eq":["retirement.is_ira",{"const":true}],"op":"test"},{"eq":["retirement.direct",{"const":false}],"op":"test"},{"eq":["retirement.rolled_some",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 25, Application of one-rollover-per-year limitation, "You can make only one rollover from an IRA to another (or the same) IRA in any 1-year period regardless of the number of IRAs you own" (2025; sha256 ca0e4287)

## (helper) — `retirement.rollover_second`

- **Authored helper label:** Did this money go back into an IRA, when you had also taken other money out of an IRA in the 12 months before you received this money and put that money back into an IRA?
- **Encoded (Bool):** Input — Did this money go back into an IRA (not a workplace plan), when you had also taken other money out of an IRA in the 12 months before you received this money and put that money back into an IRA (within 60 days, or later under a waiver)? A direct transfer between IRAs, or a conversion from a traditional IRA to a Roth IRA, is not such a rollover; a Roth IRA distribution put back into a Roth IRA is.
- Expr: `{"op":"input","source":"Did this money go back into an IRA (not a workplace plan), when you had also taken other money out of an IRA in the 12 months before you received this money and put that money back into an IRA (within 60 days, or later under a waiver)? A direct transfer between IRAs, or a conversion from a traditional IRA to a Roth IRA, is not such a rollover; a Roth IRA distribution put back into a Roth IRA is."}`
- Cite: [p590a] p. 25, Application of one-rollover-per-year limitation, "You can make only one rollover from an IRA to another (or the same) IRA in any 1-year period regardless of the number of IRAs you own", "However, trustee-to-trustee transfers between IRAs aren’t limited and rollovers from traditional IRAs to Roth IRAs (conversions) aren’t limited"; p. 25, "The 1-year period begins on the date you receive the IRA distribution, not on the date you roll it over into an IRA" (2025; sha256 ca0e4287)

## (gate) — `retirement.rollover_second_if_ira`

- **Authored helper label:** A second IRA-to-IRA rollover within 12 months, asked only of an IRA distribution, not a direct rollover, of which the filer put some into another retirement account (false otherwise)
- **Encoded (Bool):** Choose — [helper "An IRA distribution, not a direct rollover (code G), of which the filer put some into another retirement account" = true → helper "Did this money go back into an IRA, when you had also taken other money out of an IRA in the 12 months before you received this money and put that money back into an IRA?"] [helper "An IRA distribution, not a direct rollover (code G), of which the filer put some into another retirement account" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.ira_put_back",{"const":true}],"op":"test"},"then":"retirement.rollover_second"},{"guard":{"eq":["retirement.ira_put_back",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [p590a] p. 25, Application of one-rollover-per-year limitation, "You can make only one rollover from an IRA to another (or the same) IRA in any 1-year period regardless of the number of IRAs you own" (2025; sha256 ca0e4287)

## (helper) — `retirement.charity_hsa`

- **Authored helper label:** Did any of this money go straight from the IRA to a charity, or into a health savings account?
- **Encoded (Bool):** Input — Did any of this money go straight from the IRA to a charity, or into a health savings account?
- Expr: `{"op":"input","source":"Did any of this money go straight from the IRA to a charity, or into a health savings account?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.charity_hsa_if_ira`

- **Authored helper label:** Did any of this money go straight from the IRA to a charity, or into a health savings account? Asked only with an IRA (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = true → helper "Did any of this money go straight from the IRA to a charity, or into a health savings account?"] [helper "IRA distribution (lines 4a and 4b)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.charity_hsa"},{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ira_returned`

- **Authored helper label:** Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit?
- **Encoded (Bool):** Input — Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit?
- Expr: `{"op":"input","source":"Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.ira_returned_if_ira`

- **Authored helper label:** Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit? Asked only with an IRA (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = true → helper "Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit?"] [helper "IRA distribution (lines 4a and 4b)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.ira_returned"},{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ira_basis`

- **Authored helper label:** A traditional IRA of the owner holds basis: nondeductible contributions, after-tax money rolled over from a work plan, or basis that came with an IRA in a divorce transfer or from a decedent
- **Encoded (Bool):** Input — Does any traditional IRA of yours hold money on which tax was already paid, such as contributions you did not deduct, after-tax money rolled over from a work plan, or basis that came with an IRA from a spouse in a divorce or from someone who died?
- Expr: `{"op":"input","source":"Does any traditional IRA of yours hold money on which tax was already paid, such as contributions you did not deduct, after-tax money rolled over from a work plan, or basis that came with an IRA from a spouse in a divorce or from someone who died?"}`
- Cite: [i8606] p. 2, Who Must File, "You received distributions from a traditional IRA in 2025 and your basis in these IRAs is more than zero", "You or your spouse transferred all or part of their traditional IRA in 2025 to the other spouse under a divorce or separation agreement where the transfer resulted in a change in the basis", and "You received a distribution from an inherited traditional IRA that has a basis"; p. 9, Line 2, "You rolled over any nontaxable portion of your qualified retirement plan to a traditional IRA" (2025; sha256 735fb7ae)

## (gate) — `retirement.ira_basis_if_trad`

- **Authored helper label:** A traditional IRA of the owner holds basis (money already taxed), asked only with a traditional IRA (false otherwise)
- **Encoded (Bool):** Choose — [helper "A traditional, SEP or SIMPLE IRA" = true → helper "A traditional IRA of the owner holds basis: nondeductible contributions, after-tax money rolled over from a work plan, or basis that came with an IRA in a divorce transfer or from a decedent"] [helper "A traditional, SEP or SIMPLE IRA" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_trad",{"const":true}],"op":"test"},"then":"retirement.ira_basis"},{"guard":{"eq":["retirement.is_trad",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.box6`

- **Authored helper label:** Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)?
- **Encoded (Bool):** Input — Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)?
- Expr: `{"op":"input","source":"Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.box6_if_plan`

- **Authored helper label:** Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = false → helper "Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)?"] [helper "IRA distribution (lines 4a and 4b)" = true → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.box6"},{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.loan_offset`

- **Authored helper label:** Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)?
- **Encoded (Bool):** Input — Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)?
- Expr: `{"op":"input","source":"Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.loan_offset_if_plan`

- **Authored helper label:** Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = false → helper "Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)?"] [helper "IRA distribution (lines 4a and 4b)" = true → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.loan_offset"},{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.disability`

- **Authored helper label:** Was any of this paid to you because you became disabled, under a plan that provides for disability retirement?
- **Encoded (Bool):** Input — Was any of this paid to you because you became disabled, under a plan that provides for disability retirement?
- Expr: `{"op":"input","source":"Was any of this paid to you because you became disabled, under a plan that provides for disability retirement?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.disability_if_plan`

- **Authored helper label:** Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = false → helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement?"] [helper "IRA distribution (lines 4a and 4b)" = true → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.disability"},{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.dis_early`

- **Authored helper label:** When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)?
- **Encoded (Bool):** Input — When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)?
- Expr: `{"op":"input","source":"When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.dis_early_if_disability`

- **Authored helper label:** When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)? Asked only with a disability pension (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)?"] [helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.disability_if_plan",{"const":true}],"op":"test"},"then":"retirement.dis_early"},{"guard":{"eq":["retirement.disability_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.dis_all_early`

- **Authored helper label:** Were you younger than that age when each payment of 2025 on this form was made?
- **Encoded (Bool):** Input — Were you younger than that age when each payment of 2025 on this form was made?
- Expr: `{"op":"input","source":"Were you younger than that age when each payment of 2025 on this form was made?"}`
- Cite: [i1040gi] p. 25, "Disability pensions shown on Form 1099-R if you haven’t reached the minimum retirement age set by your employer", "Disability pensions received after you reach minimum retirement age and other payments shown on Form 1099-R (other than payments from an IRA) are reported on lines 5a and 5b" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.dis_all_early_if_early`

- **Authored helper label:** All of 2025's payments made before the minimum retirement age. Asked only with a disability pension paid before that age (false otherwise)
- **Encoded (Bool):** Choose — [helper "When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)? Asked only with a disability pension (false otherwise)" = true → helper "Were you younger than that age when each payment of 2025 on this form was made?"] [helper "When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)? Asked only with a disability pension (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.dis_early_if_disability",{"const":true}],"op":"test"},"then":"retirement.dis_all_early"},{"guard":{"eq":["retirement.dis_early_if_disability",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 25, "Disability pensions received after you reach minimum retirement age and other payments shown on Form 1099-R (other than payments from an IRA) are reported on lines 5a and 5b" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.dis_wages`

- **Authored helper label:** A disability pension paid wholly before the minimum retirement age: its taxable amount is wages on Form 1040, line 1h, not a pension on lines 5a and 5b
- **Encoded (Bool):** helper "All of 2025's payments made before the minimum retirement age. Asked only with a disability pension paid before that age (false otherwise)" = true
- Expr: `{"eq":["retirement.dis_all_early_if_early",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 25, "Disability pensions shown on Form 1099-R if you haven’t reached the minimum retirement age set by your employer" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.dis_split`

- **Authored helper label:** A disability pension paid partly before and partly after the minimum retirement age in 2025, or paid before that age with after-tax cost in the plan
- **Encoded (Bool):** (helper "When any of this was paid, were you younger than the earliest age at which the plan would have allowed retirement without the disability (its minimum retirement age)? Asked only with a disability pension (false otherwise)" = true and helper "All of 2025's payments made before the minimum retirement age. Asked only with a disability pension paid before that age (false otherwise)" = false or helper "A disability pension paid wholly before the minimum retirement age: its taxable amount is wages on Form 1040, line 1h, not a pension on lines 5a and 5b" = true and helper "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)" = true)
- Expr: `{"any":[{"all":[{"eq":["retirement.dis_early_if_disability",{"const":true}],"op":"test"},{"eq":["retirement.dis_all_early_if_early",{"const":false}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.dis_wages",{"const":true}],"op":"test"},{"eq":["retirement.annuity_if_cost",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 25, "Disability pensions shown on Form 1099-R if you haven’t reached the minimum retirement age set by your employer", "Disability pensions received after you reach minimum retirement age and other payments shown on Form 1099-R (other than payments from an IRA) are reported on lines 5a and 5b" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.dis_terror`

- **Authored helper label:** Did the disability result from a terrorist attack?
- **Encoded (Bool):** Input — Did the disability result from a terrorist attack?
- Expr: `{"op":"input","source":"Did the disability result from a terrorist attack?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.dis_terror_if_disability`

- **Authored helper label:** Did the disability result from a terrorist attack? Asked only with a disability pension (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Did the disability result from a terrorist attack?"] [helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.disability_if_plan",{"const":true}],"op":"test"},"then":"retirement.dis_terror"},{"guard":{"eq":["retirement.disability_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.dis_military`

- **Authored helper label:** Is it a disability pension for service in the armed forces?
- **Encoded (Bool):** Input — Is it a disability pension for service in the armed forces?
- Expr: `{"op":"input","source":"Is it a disability pension for service in the armed forces?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.dis_military_if_disability`

- **Authored helper label:** Is it a disability pension for service in the armed forces? Asked only with a disability pension (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Is it a disability pension for service in the armed forces?"] [helper "Was any of this paid to you because you became disabled, under a plan that provides for disability retirement? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.disability_if_plan",{"const":true}],"op":"test"},"then":"retirement.dis_military"},{"guard":{"eq":["retirement.disability_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.pso_exclusion`

- **Authored helper label:** Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance?
- **Encoded (Bool):** Input — Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance?
- Expr: `{"op":"input","source":"Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.pso_exclusion_if_plan`

- **Authored helper label:** Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = false → helper "Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance?"] [helper "IRA distribution (lines 4a and 4b)" = true → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.pso_exclusion"},{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.born_before_averaging_date`

- **Authored helper label:** Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936?
- **Encoded (Bool):** Input — Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936?
- Expr: `{"op":"input","source":"Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.born_before_averaging_date_if_plan`

- **Authored helper label:** Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = false → helper "Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936?"] [helper "IRA distribution (lines 4a and 4b)" = true → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.born_before_averaging_date"},{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.lump_sum`

- **Authored helper label:** Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)?
- **Encoded (Bool):** Input — Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)?
- Expr: `{"op":"input","source":"Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.lump_sum_if_born_before_averaging_date`

- **Authored helper label:** Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)? Asked only with a person born before January 2, 1936 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)?"] [helper "Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.born_before_averaging_date_if_plan",{"const":true}],"op":"test"},"then":"retirement.lump_sum"},{"guard":{"eq":["retirement.born_before_averaging_date_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.death_exclusion`

- **Authored helper label:** Did the person who earned this pension (an employee or a former employee, a retiree included) die before August 21, 1996, so that a death benefit exclusion applies to these payments?
- **Encoded (Bool):** Input — Did the person who earned this pension (an employee or a former employee, a retiree included) die before August 21, 1996, so that a death benefit exclusion applies to these payments?
- Expr: `{"op":"input","source":"Did the person who earned this pension (an employee or a former employee, a retiree included) die before August 21, 1996, so that a death benefit exclusion applies to these payments?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.death_exclusion_if_death`

- **Authored helper label:** Did the person who earned this pension (an employee or a former employee, a retiree included) die before August 21, 1996, so that a death benefit exclusion applies to these payments? Asked only with a payment from a plan after a death (code 4) (false otherwise)
- **Encoded (Bool):** Choose — [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = true → helper "Did the person who earned this pension (an employee or a former employee, a retiree included) die before August 21, 1996, so that a death benefit exclusion applies to these payments?"] [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.plan_death",{"const":true}],"op":"test"},"then":"retirement.death_exclusion"},{"guard":{"eq":["retirement.plan_death",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ben_before_retire`

- **Authored helper label:** Did the person who died do so before this pension's payments to them began (its annuity starting date), even if they had already stopped working?
- **Encoded (Bool):** Input — Did the person who died do so before this pension's payments to them began (its annuity starting date), even if they had already stopped working?
- Expr: `{"op":"input","source":"Did the person who died do so before this pension's payments to them began (its annuity starting date), even if they had already stopped working?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.ben_before_retire_if_death`

- **Authored helper label:** Did the person who died do so before this pension's payments to them began (its annuity starting date), even if they had already stopped working? Asked only with a payment from a plan after a death (code 4) (false otherwise)
- **Encoded (Bool):** Choose — [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = true → helper "Did the person who died do so before this pension's payments to them began (its annuity starting date), even if they had already stopped working?"] [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.plan_death",{"const":true}],"op":"test"},"then":"retirement.ben_before_retire"},{"guard":{"eq":["retirement.plan_death",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ben_guaranteed`

- **Authored helper label:** Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life?
- **Encoded (Bool):** Input — Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life?
- Expr: `{"op":"input","source":"Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.ben_guaranteed_if_death`

- **Authored helper label:** Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life? Asked only with a payment from a plan after a death (code 4) (false otherwise)
- **Encoded (Bool):** Choose — [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = true → helper "Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life?"] [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.plan_death",{"const":true}],"op":"test"},"then":"retirement.ben_guaranteed"},{"guard":{"eq":["retirement.plan_death",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ben_shared`

- **Authored helper label:** Is this pension shared among more than one beneficiary?
- **Encoded (Bool):** Input — Is this pension shared among more than one beneficiary?
- Expr: `{"op":"input","source":"Is this pension shared among more than one beneficiary?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.ben_shared_if_death`

- **Authored helper label:** Is this pension shared among more than one beneficiary? Asked only with a payment from a plan after a death (code 4) (false otherwise)
- **Encoded (Bool):** Choose — [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = true → helper "Is this pension shared among more than one beneficiary?"] [helper "A payment from a plan to a beneficiary (code 4, not an IRA)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.plan_death",{"const":true}],"op":"test"},"then":"retirement.ben_shared"},{"guard":{"eq":["retirement.plan_death",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.cost_any`

- **Authored helper label:** Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes.
- **Encoded (Bool):** Input — Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes.
- Expr: `{"op":"input","source":"Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes."}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.cost_any_if_plan`

- **Authored helper label:** Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)
- **Encoded (Bool):** Choose — [helper "IRA distribution (lines 4a and 4b)" = false → helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes."] [helper "IRA distribution (lines 4a and 4b)" = true → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.cost_any"},{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.own_annuity`

- **Authored helper label:** Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)?
- **Encoded (Bool):** Input — Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)?
- Expr: `{"op":"input","source":"Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.own_annuity_if_cost`

- **Authored helper label:** Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)? Asked only with after-tax cost in the plan (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)?"] [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_any_if_plan",{"const":true}],"op":"test"},"then":"retirement.own_annuity"},{"guard":{"eq":["retirement.cost_any_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.csrs_alt`

- **Authored helper label:** Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)?
- **Encoded (Bool):** Input — Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)?
- Expr: `{"op":"input","source":"Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.csrs_alt_if_cost`

- **Authored helper label:** Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)? Asked only with after-tax cost in the plan (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)?"] [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_any_if_plan",{"const":true}],"op":"test"},"then":"retirement.csrs_alt"},{"guard":{"eq":["retirement.cost_any_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.started_before_simplified_method_date`

- **Authored helper label:** Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.)
- **Encoded (Bool):** Input — Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.)
- Expr: `{"op":"input","source":"Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.)"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.started_before_simplified_method_date_if_cost`

- **Authored helper label:** Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.) Asked only with after-tax cost in the plan (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.)"] [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_any_if_plan",{"const":true}],"op":"test"},"then":"retirement.started_before_simplified_method_date"},{"guard":{"eq":["retirement.cost_any_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.general_rule`

- **Authored helper label:** When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more?
- **Encoded (Bool):** Input — When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more?
- Expr: `{"op":"input","source":"When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.general_rule_if_cost`

- **Authored helper label:** When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more? Asked only with after-tax cost in the plan (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more?"] [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_any_if_plan",{"const":true}],"op":"test"},"then":"retirement.general_rule"},{"guard":{"eq":["retirement.cost_any_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.lump_at_start`

- **Authored helper label:** Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller?
- **Encoded (Bool):** Input — Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller?
- Expr: `{"op":"input","source":"Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.lump_at_start_if_cost`

- **Authored helper label:** Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller? Asked only with after-tax cost in the plan (false otherwise)
- **Encoded (Bool):** Choose — [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller?"] [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_any_if_plan",{"const":true}],"op":"test"},"then":"retirement.lump_at_start"},{"guard":{"eq":["retirement.cost_any_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.disaster`

- **Authored helper label:** Did you take this money out, or put money back, because of a federally declared disaster (Form 8915-F)?
- **Encoded (Bool):** Input — Did you take this money out, or put money back, because of a federally declared disaster (Form 8915-F)?
- Expr: `{"op":"input","source":"Did you take this money out, or put money back, because of a federally declared disaster (Form 8915-F)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.special`

- **Authored helper label:** A Form 1099-R situation that needs a form or rule outside this tool (any of the situations asked about one by one: where the money went, the IRA's history, employer securities, a plan loan offset, a disability pension, the public safety officer exclusion, a lump-sum distribution, a payment after a death, after-tax cost outside the Simplified Method, a disaster)
- **Encoded (Bool):** (helper "Did any of this money go into a Roth IRA or another Roth account? Asked only with some of the money went into another retirement account (false otherwise)" = true or helper "Did the plan or IRA pay out anything other than cash (such as shares) that was then sold, kept, or put only partly into the new account? Asked only with some of the money went into another retirement account (false otherwise)" = true or helper "Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)? Asked only with some of the money went into another retirement account (false otherwise)" = true or helper "Was this money taken by the IRS under a levy and later returned to you? Asked only with some of the money went into another retirement account (false otherwise)" = true or helper "Inherited from someone other than the spouse (the inherited-IRA answer for an IRA, the plan question for a plan), read only for a beneficiary (code 4) who put some of the money into another retirement account (false otherwise)" = true or helper "A second IRA-to-IRA rollover within 12 months, asked only of an IRA distribution, not a direct rollover, of which the filer put some into another retirement account (false otherwise)" = true or helper "Did any of this money go straight from the IRA to a charity, or into a health savings account? Asked only with an IRA (false otherwise)" = true or helper "Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit? Asked only with an IRA (false otherwise)" = true or helper "A traditional IRA of the owner holds basis (money already taxed), asked only with a traditional IRA (false otherwise)" = true or helper "Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true or helper "Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true or helper "A disability pension paid partly before and partly after the minimum retirement age in 2025, or paid before that age with after-tax cost in the plan" = true or helper "Did the disability result from a terrorist attack? Asked only with a disability pension (false otherwise)" = true or helper "Is it a disability pension for service in the armed forces? Asked only with a disability pension (false otherwise)" = true or helper "Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance? Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true or helper "Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)? Asked only with a person born before January 2, 1936 (false otherwise)" = true or helper "Did the person who earned this pension (an employee or a former employee, a retiree included) die before August 21, 1996, so that a death benefit exclusion applies to these payments? Asked only with a payment from a plan after a death (code 4) (false otherwise)" = true or helper "Did the person who died do so before this pension's payments to them began (its annuity starting date), even if they had already stopped working? Asked only with a payment from a plan after a death (code 4) (false otherwise)" = true or helper "Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life? Asked only with a payment from a plan after a death (code 4) (false otherwise)" = true or helper "Is this pension shared among more than one beneficiary? Asked only with a payment from a plan after a death (code 4) (false otherwise)" = true or helper "Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)? Asked only with after-tax cost in the plan (false otherwise)" = true or helper "Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)? Asked only with after-tax cost in the plan (false otherwise)" = true or helper "Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.) Asked only with after-tax cost in the plan (false otherwise)" = true or helper "When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more? Asked only with after-tax cost in the plan (false otherwise)" = true or helper "Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller? Asked only with after-tax cost in the plan (false otherwise)" = true or helper "Did you take this money out, or put money back, because of a federally declared disaster (Form 8915-F)?" = true)
- Expr: `{"any":[{"eq":["retirement.roth_moved_if_put_back",{"const":true}],"op":"test"},{"eq":["retirement.rollover_property_if_put_back",{"const":true}],"op":"test"},{"eq":["retirement.rollover_qdro_if_put_back",{"const":true}],"op":"test"},{"eq":["retirement.levy_returned_if_put_back",{"const":true}],"op":"test"},{"eq":["retirement.rollover_nonspouse_if_death",{"const":true}],"op":"test"},{"eq":["retirement.rollover_second_if_ira",{"const":true}],"op":"test"},{"eq":["retirement.charity_hsa_if_ira",{"const":true}],"op":"test"},{"eq":["retirement.ira_returned_if_ira",{"const":true}],"op":"test"},{"eq":["retirement.ira_basis_if_trad",{"const":true}],"op":"test"},{"eq":["retirement.box6_if_plan",{"const":true}],"op":"test"},{"eq":["retirement.loan_offset_if_plan",{"const":true}],"op":"test"},{"eq":["retirement.dis_split",{"const":true}],"op":"test"},{"eq":["retirement.dis_terror_if_disability",{"const":true}],"op":"test"},{"eq":["retirement.dis_military_if_disability",{"const":true}],"op":"test"},{"eq":["retirement.pso_exclusion_if_plan",{"const":true}],"op":"test"},{"eq":["retirement.lump_sum_if_born_before_averaging_date",{"const":true}],"op":"test"},{"eq":["retirement.death_exclusion_if_death",{"const":true}],"op":"test"},{"eq":["retirement.ben_before_retire_if_death",{"const":true}],"op":"test"},{"eq":["retirement.ben_guaranteed_if_death",{"const":true}],"op":"test"},{"eq":["retirement.ben_shared_if_death",{"const":true}],"op":"test"},{"eq":["retirement.own_annuity_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.csrs_alt_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.started_before_simplified_method_date_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.general_rule_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.lump_at_start_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.disaster",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.annuity`

- **Authored helper label:** Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies. A nonperiodic payment received on or after the annuity starting date, one that is not one of the periodic payments, is generally fully taxable, so if box 1 is only such a payment, answer No; if box 1 also includes the periodic payments, answer for those payments.)
- **Encoded (Bool):** Input — Is this a pension or annuity to which all of these apply?

  - from a qualified plan, section 403(b) plan or tax-sheltered annuity
  - paid in periodic payments in which you have after-tax cost (box 9b or your records)
  - with an annuity starting date after November 18, 1996
  - on that date you were under age 75 or had fewer than 5 years of guaranteed payments

  This is when the Simplified Method applies.

  If you are the survivor of a retiree, answer for the retiree's annuity, with its starting date and the retiree's age on that date.

  A nonperiodic payment received on or after the annuity starting date, one that is not one of the periodic payments, is generally fully taxable, so if box 1 is only such a payment, answer No; if box 1 also includes the periodic payments, answer for those payments.
- Expr: `{"op":"input","source":"Is this a pension or annuity to which all of these apply?\n\n- from a qualified plan, section 403(b) plan or tax-sheltered annuity\n- paid in periodic payments in which you have after-tax cost (box 9b or your records)\n- with an annuity starting date after November 18, 1996\n- on that date you were under age 75 or had fewer than 5 years of guaranteed payments\n\nThis is when the Simplified Method applies.\n\nIf you are the survivor of a retiree, answer for the retiree's annuity, with its starting date and the retiree's age on that date.\n\nA nonperiodic payment received on or after the annuity starting date, one that is not one of the periodic payments, is generally fully taxable, so if box 1 is only such a payment, answer No; if box 1 also includes the periodic payments, answer for those payments."}`
- Cite: [i1040gi] p. 30, Simplified Method, conditions 1 and 2; p. 28, Partially Taxable Pensions and Annuities; p575 p. 16, Distribution On or After Annuity Starting Date, "If you receive a nonperiodic payment from your annuity contract on or after the annuity starting date, you must generally include all of the payment in gross income."; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `retirement.annuity_if_cost`

- **Authored helper label:** The Simplified Method applies, asked only with after-tax cost in the plan (false without it)
- **Encoded (Bool):** Choose — [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = true → helper "Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies. A nonperiodic payment received on or after the annuity starting date, one that is not one of the periodic payments, is generally fully taxable, so if box 1 is only such a payment, answer No; if box 1 also includes the periodic payments, answer for those payments.)"] [helper "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes. Asked only with a pension, annuity or plan (not an IRA) (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_any_if_plan",{"const":true}],"op":"test"},"then":"retirement.annuity"},{"guard":{"eq":["retirement.cost_any_if_plan",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.cost`

- **Authored helper label:** Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)
- **Encoded (NonNegDollars):** Input — Your cost (net investment, after-tax contributions) in the plan at the annuity starting date; it may be shown in Form 1099-R box 9b (if you are the survivor of a retiree, the retiree's cost at the retiree's annuity starting date)
- Expr: `{"op":"input","source":"Your cost (net investment, after-tax contributions) in the plan at the annuity starting date; it may be shown in Form 1099-R box 9b (if you are the survivor of a retiree, the retiree's cost at the retiree's annuity starting date)"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 2; p. 30, Cost; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.used_last_year`

- **Authored helper label:** Did you complete this worksheet for this annuity last year?
- **Encoded (Bool):** Input — Did you complete the Simplified Method Worksheet for this annuity last year? (If you are the survivor of a retiree, answer Yes if you or the retiree completed it for this annuity last year.)
- Expr: `{"op":"input","source":"Did you complete the Simplified Method Worksheet for this annuity last year? (If you are the survivor of a retiree, answer Yes if you or the retiree completed it for this annuity last year.)"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, note under line 2; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.last_line4`

- **Authored helper label:** Line 4 of last year's Simplified Method Worksheet
- **Encoded (NonNegDollars):** Input — The amount on line 4 of last year's Simplified Method Worksheet for this annuity (yours, or the retiree's if you are the survivor of a retiree)
- Expr: `{"op":"input","source":"The amount on line 4 of last year's Simplified Method Worksheet for this annuity (yours, or the retiree's if you are the survivor of a retiree)"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, note under line 2; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.joint_life`

- **Authored helper label:** Annuity starting date after 1997 and payments for your life and that of your beneficiary?
- **Encoded (Bool):** Input — Was the annuity starting date after 1997, with payments for your life and that of your beneficiary (Table 2)? (If you are the survivor of a retiree, answer for the retiree's annuity, that is, whether its starting date was after 1997, with payments for the retiree's life and yours.)
- Expr: `{"op":"input","source":"Was the annuity starting date after 1997, with payments for your life and that of your beneficiary (Table 2)? (If you are the survivor of a retiree, answer for the retiree's annuity, that is, whether its starting date was after 1997, with payments for the retiree's life and yours.)"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 3 and Table 2; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.age`

- **Authored helper label:** Age at the annuity starting date
- **Encoded (Count):** Input — Your age at the annuity starting date (if you are the survivor of a retiree, the retiree's age on their annuity starting date)
- Expr: `{"op":"input","source":"Your age at the annuity starting date (if you are the survivor of a retiree, the retiree's age on their annuity starting date)"}`
- Cite: [i1040gi] p. 29, Table 1; p. 30, Age (or Combined Ages) at Annuity Starting Date (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.combined_age`

- **Authored helper label:** Combined ages at the annuity starting date
- **Encoded (Count):** Input — Your combined ages (yours and your beneficiary's) at the annuity starting date (if you are the survivor of a retiree, the retiree's age and yours on the retiree's annuity starting date)
- Expr: `{"op":"input","source":"Your combined ages (yours and your beneficiary's) at the annuity starting date (if you are the survivor of a retiree, the retiree's age and yours on the retiree's annuity starting date)"}`
- Cite: [i1040gi] p. 29, Table 2; p. 30, Age (or Combined Ages) at Annuity Starting Date; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.months`

- **Authored helper label:** Number of months for which this year's payments were made
- **Encoded (Count):** Input — Number of months for which this year's payments were made (at most 12) — the months covered by the payments included in box 1 of this Form 1099-R, not the calendar months of 2025 since the payments began; for example, a pension paid monthly in arrears that began in July, with five payments in 2025 for July through November, is 5
- Expr: `{"op":"input","source":"Number of months for which this year's payments were made (at most 12) — the months covered by the payments included in box 1 of this Form 1099-R, not the calendar months of 2025 since the payments began; for example, a pension paid monthly in arrears that began in July, with five payments in 2025 for July through November, is 5"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.recovered`

- **Authored helper label:** Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)
- **Encoded (NonNegDollars):** Input — Amount, if any, recovered tax free in years after 1986 (if you completed this worksheet last year, line 10 of last year's worksheet; if you are the survivor of a retiree, include the amount the retiree recovered tax free)
- Expr: `{"op":"input","source":"Amount, if any, recovered tax free in years after 1986 (if you completed this worksheet last year, line 10 of last year's worksheet; if you are the survivor of a retiree, include the amount the retiree recovered tax free)"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 6; p575 p. 34, Survivors of retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax free is the same as the tax-free amount figured by the retiree at the annuity starting date"; p575 p. 12, Exclusion limited to cost, "the total amount of annuity income that you can exclude over the years as a recovery of the cost can’t exceed your total cost" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.zero`

- **Authored helper label:** No amount
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 27, line 4b, Exception 2(b) (enter -0-) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.one`

- **Authored helper label:** One distribution
- **Encoded (Count):** Enter 1 (sales.one).
- Expr: `{"op":"param","ref":"sales.one"}`
- Cite: [i1040gi] pp. 26-30, lines 4c and 5c (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.is_ira`

- **Authored helper label:** IRA distribution (lines 4a and 4b)
- **Encoded (Bool):** helper "Kind of account the distribution came from" ≠ 'plan'
- Expr: `{"ne":["retirement.account",{"const":"plan"}],"op":"test"}`
- Cite: [i1040gi] p. 26, Lines 4a and 4b, IRA Distributions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.roth`

- **Authored helper label:** Roth IRA distribution
- **Encoded (Bool):** helper "Kind of account the distribution came from" = 'roth_ira'
- Expr: `{"eq":["retirement.account",{"const":"roth_ira"}],"op":"test"}`
- Cite: [i1040gi] p. 27, Exception 2, item 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.direct`

- **Authored helper label:** Direct rollover (code G)
- **Encoded (Bool):** helper "Distribution code in box 7" = 'direct_rollover_G'
- Expr: `{"eq":["retirement.code",{"const":"direct_rollover_G"}],"op":"test"}`
- Cite: [f1099r] p. 5, Box 2a, "For a direct rollover, other than from a qualified plan, section 403(b) plan, or governmental section 457(b) plan to a designated Roth account in the same plan or to a Roth IRA, zero should be shown and you must enter zero (-0-) on the “Taxable amount” line of your tax return"; pp. 7 and 9, Box 7, "G—Direct rollover of a distribution to a qualified plan, a section 403(b) plan, a governmental section 457(b) plan, or an IRA" (2025 (calendar-year form); sha256 d6b7be48)

## (gate) — `retirement.bad_code`

- **Authored helper label:** Distribution code the tool does not compute
- **Encoded (Bool):** (helper "Distribution code in box 7" = 'other' or helper "Distribution code in box 7" = 'simple_S' and helper "Kind of account the distribution came from" ≠ 'traditional_ira' or helper "Distribution code in box 7" = 'disability_3' and helper "IRA distribution (lines 4a and 4b)" = false and helper "A disability pension paid wholly before the minimum retirement age: its taxable amount is wages on Form 1040, line 1h, not a pension on lines 5a and 5b" = false or helper "Kind of account the distribution came from" = 'roth_ira' and helper "Distribution code in box 7" ≠ 'qualified_roth_Q' or helper "Distribution code in box 7" = 'qualified_roth_Q' and helper "Kind of account the distribution came from" ≠ 'roth_ira')
- Expr: `{"any":[{"eq":["retirement.code",{"const":"other"}],"op":"test"},{"all":[{"eq":["retirement.code",{"const":"simple_S"}],"op":"test"},{"ne":["retirement.account",{"const":"traditional_ira"}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.code",{"const":"disability_3"}],"op":"test"},{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.dis_wages",{"const":false}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.account",{"const":"roth_ira"}],"op":"test"},{"ne":["retirement.code",{"const":"qualified_roth_Q"}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.code",{"const":"qualified_roth_Q"}],"op":"test"},{"ne":["retirement.account",{"const":"roth_ira"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 27, Exception 2 (a Roth IRA distribution other than code Q needs Form 8606); f1099r pp. 7 and 9, Box 7, "The following codes identify the distribution you received", "Q—Qualified distribution from a Roth IRA or Roth SIMPLE IRA" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.rolled`

- **Authored helper label:** Amount rolled over (the whole distribution for a direct rollover)
- **Encoded (NonNegDollars):** Choose — [helper "Direct rollover (code G)" = true → helper "Gross distribution, box 1"] [helper "Direct rollover (code G)" = false → helper "Amount rolled over, asked only when some of the money went into another retirement account (none otherwise)"]
- **Refusal:** when retirement.special is true, cannot complete Form 1099-R special cases (Forms 5329, 8606, 4972, 8915-F, Pub. 575 or 939). This distribution needs a form or rule outside this tool. Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when retirement.bad_code is true, cannot complete Form 8606 or another Form 1099-R code. A Roth IRA distribution other than a qualified distribution (code Q), code S other than from a traditional SIMPLE IRA, code 3 other than from an IRA, or a distribution code other than 7, 4, 2, 1, S, 3, G or Q, is outside this tool. Cite: [i1040gi] p. 27, Exception 2; f1099r Box 7 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.direct",{"const":true}],"op":"test"},"then":"retirement.box1"},{"guard":{"eq":["retirement.direct",{"const":false}],"op":"test"},"then":"retirement.rollover_if_any"}],"op":"choose"}`
- Cite: [i1040gi] p. 27, Exception 1; p. 30, Rollovers (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.has_rollover`

- **Authored helper label:** Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)
- **Encoded (Bool):** (helper "Amount rolled over (the whole distribution for a direct rollover)" > $0 (sales.zero) or helper "Direct rollover (code G)" = true)
- Expr: `{"any":[{"gt":["retirement.rolled",{"param":"sales.zero"}],"op":"test"},{"eq":["retirement.direct",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 27, Exception 1 ('Also check box 1 on line 4c'); p. 30, Rollovers ('Use lines 5a and 5b to report a rollover, including a direct rollover'); p. 31, Line 5c (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw_shown`

- **Authored helper label:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover)
- **Encoded (Bool):** helper "IRA distribution (lines 4a and 4b)" = false and helper "The Simplified Method applies and some cost is left to recover" = true
- Expr: `{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.annuity_with_cost",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 28, Fully Taxable Pensions and Annuities, "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025."; p. 29, Simplified Method Worksheet—Lines 5a and 5b (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 1) — `retirement.smw1`

- **Authored helper label:** Enter the total pension or annuity payments from Form 1099-R, box 1
- **Encoded (NonNegDollars):** Enter the amount from helper "Gross distribution, box 1".
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"from":"retirement.box1","op":"copy"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 2) — `retirement.smw2`

- **Authored helper label:** Enter your cost in the plan at the annuity starting date
- **Encoded (NonNegDollars):** Enter the amount from helper "Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)".
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"from":"retirement.cost","op":"copy"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t1_360`

- **Authored helper label:** Line 2 divided by 360 (Table 1)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/360 (smw.table1_360).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table1_360"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 1 (360) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t1_310`

- **Authored helper label:** Line 2 divided by 310 (Table 1)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/310 (smw.table1_310).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table1_310"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 1 (310) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t1_260`

- **Authored helper label:** Line 2 divided by 260 (Table 1)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/260 (smw.table1_260).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table1_260"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 1 (260) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t1_210`

- **Authored helper label:** Line 2 divided by 210 (Table 1)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/210 (smw.table1_210).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table1_210"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 1 (210) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t1_160`

- **Authored helper label:** Line 2 divided by 160 (Table 1)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/160 (smw.table1_160).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table1_160"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 1 (160) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t2_410`

- **Authored helper label:** Line 2 divided by 410 (Table 2)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/410 (smw.table2_410).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table2_410"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 2 (410) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t2_360`

- **Authored helper label:** Line 2 divided by 360 (Table 2)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/360 (smw.table2_360).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table2_360"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 2 (360) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t2_310`

- **Authored helper label:** Line 2 divided by 310 (Table 2)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/310 (smw.table2_310).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table2_310"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 2 (310) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t2_260`

- **Authored helper label:** Line 2 divided by 260 (Table 2)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/260 (smw.table2_260).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table2_260"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 2 (260) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_t2_210`

- **Authored helper label:** Line 2 divided by 210 (Table 2)
- **Encoded (NonNegDollars):** Multiply column (SMW 2) by 1/210 (smw.table2_210).
- Expr: `{"amount":"retirement.smw2","op":"multiply_rate","rate":{"param":"smw.table2_210"}}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, lines 3 and 4, Table 2 (210) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_table1`

- **Authored helper label:** Line 2 divided by the Table 1 number for the age at the annuity starting date
- **Encoded (NonNegDollars):** Choose — [helper "Age at the annuity starting date" ≥ 0 (a count) and helper "Age at the annuity starting date" < 56 (a count) → helper "Line 2 divided by 360 (Table 1)"] [helper "Age at the annuity starting date" ≥ 56 (a count) and helper "Age at the annuity starting date" < 61 (a count) → helper "Line 2 divided by 310 (Table 1)"] [helper "Age at the annuity starting date" ≥ 61 (a count) and helper "Age at the annuity starting date" < 66 (a count) → helper "Line 2 divided by 260 (Table 1)"] [helper "Age at the annuity starting date" ≥ 66 (a count) and helper "Age at the annuity starting date" < 71 (a count) → helper "Line 2 divided by 210 (Table 1)"] [helper "Age at the annuity starting date" ≥ 71 (a count) → helper "Line 2 divided by 160 (Table 1)"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["retirement.age",{"const":0,"type":"Count"}],"op":"test"},{"lt":["retirement.age",{"const":56,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t1_360"},{"guard":{"all":[{"ge":["retirement.age",{"const":56,"type":"Count"}],"op":"test"},{"lt":["retirement.age",{"const":61,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t1_310"},{"guard":{"all":[{"ge":["retirement.age",{"const":61,"type":"Count"}],"op":"test"},{"lt":["retirement.age",{"const":66,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t1_260"},{"guard":{"all":[{"ge":["retirement.age",{"const":66,"type":"Count"}],"op":"test"},{"lt":["retirement.age",{"const":71,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t1_210"},{"guard":{"ge":["retirement.age",{"const":71,"type":"Count"}],"op":"test"},"then":"retirement.smw4_t1_160"}],"op":"choose"}`
- Cite: [i1040gi] p. 29, Table 1 for Line 3 (annuity starting date after November 18, 1996) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_table2`

- **Authored helper label:** Line 2 divided by the Table 2 number for the combined ages at the annuity starting date
- **Encoded (NonNegDollars):** Choose — [helper "Combined ages at the annuity starting date" ≥ 0 (a count) and helper "Combined ages at the annuity starting date" < 111 (a count) → helper "Line 2 divided by 410 (Table 2)"] [helper "Combined ages at the annuity starting date" ≥ 111 (a count) and helper "Combined ages at the annuity starting date" < 121 (a count) → helper "Line 2 divided by 360 (Table 2)"] [helper "Combined ages at the annuity starting date" ≥ 121 (a count) and helper "Combined ages at the annuity starting date" < 131 (a count) → helper "Line 2 divided by 310 (Table 2)"] [helper "Combined ages at the annuity starting date" ≥ 131 (a count) and helper "Combined ages at the annuity starting date" < 141 (a count) → helper "Line 2 divided by 260 (Table 2)"] [helper "Combined ages at the annuity starting date" ≥ 141 (a count) → helper "Line 2 divided by 210 (Table 2)"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["retirement.combined_age",{"const":0,"type":"Count"}],"op":"test"},{"lt":["retirement.combined_age",{"const":111,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t2_410"},{"guard":{"all":[{"ge":["retirement.combined_age",{"const":111,"type":"Count"}],"op":"test"},{"lt":["retirement.combined_age",{"const":121,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t2_360"},{"guard":{"all":[{"ge":["retirement.combined_age",{"const":121,"type":"Count"}],"op":"test"},{"lt":["retirement.combined_age",{"const":131,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t2_310"},{"guard":{"all":[{"ge":["retirement.combined_age",{"const":131,"type":"Count"}],"op":"test"},{"lt":["retirement.combined_age",{"const":141,"type":"Count"}],"op":"test"}],"op":"test"},"then":"retirement.smw4_t2_260"},{"guard":{"ge":["retirement.combined_age",{"const":141,"type":"Count"}],"op":"test"},"then":"retirement.smw4_t2_210"}],"op":"choose"}`
- Cite: [i1040gi] p. 29, Table 2 for Line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.smw4_new`

- **Authored helper label:** Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Annuity starting date after 1997 and payments for your life and that of your beneficiary?" = true → helper "Line 2 divided by the Table 2 number for the combined ages at the annuity starting date"] [helper "Annuity starting date after 1997 and payments for your life and that of your beneficiary?" = false → helper "Line 2 divided by the Table 1 number for the age at the annuity starting date"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.joint_life",{"const":true}],"op":"test"},"then":"retirement.smw4_table2"},{"guard":{"eq":["retirement.joint_life",{"const":false}],"op":"test"},"then":"retirement.smw4_table1"}],"op":"choose"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 4) — `retirement.smw4`

- **Authored helper label:** Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line 4 of last year's worksheet)
- **Encoded (NonNegDollars):** Choose — [helper "Did you complete this worksheet for this annuity last year?" = true → helper "Line 4 of last year's Simplified Method Worksheet"] [helper "Did you complete this worksheet for this annuity last year?" = false → helper "Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity starting after 1997, Table 1 otherwise)"]
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.used_last_year",{"const":true}],"op":"test"},"then":"retirement.last_line4"},{"guard":{"eq":["retirement.used_last_year",{"const":false}],"op":"test"},"then":"retirement.smw4_new"}],"op":"choose"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 4, and the note under line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 5) — `retirement.smw5`

- **Authored helper label:** Multiply line 4 by the number of months for which this year's payments were made
- **Encoded (NonNegDollars):** Multiply column (SMW 4) by the number on helper "Number of months for which this year's payments were made".
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"amount":"retirement.smw4","count":"retirement.months","op":"multiply_count"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 6) — `retirement.smw6`

- **Authored helper label:** Enter the amount, if any, recovered tax free in years after 1986
- **Encoded (NonNegDollars):** Enter the amount from helper "Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)".
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"from":"retirement.recovered","op":"copy"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 7) — `retirement.smw7`

- **Authored helper label:** Subtract line 6 from line 2
- **Encoded (Dollars):** Subtract column (SMW 6) from column (SMW 2).
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"from":"retirement.smw2","op":"subtract","take":"retirement.smw6"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 8) — `retirement.smw8`

- **Authored helper label:** Enter the smaller of line 5 or line 7
- **Encoded (Dollars):** Enter the smaller of column (SMW 5) or column (SMW 7).
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"of":["retirement.smw5","retirement.smw7"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 9) — `retirement.smw9`

- **Authored helper label:** Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
- **Encoded (NonNegDollars):** Subtract column (SMW 8) from column (SMW 1). If zero or less, enter -0-.
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"from":"retirement.smw1","op":"subtract_floor0","take":"retirement.smw8"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 9 (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 10) — `retirement.smw10`

- **Authored helper label:** Add lines 6 and 8. This is the amount you have recovered tax free through 2025
- **Encoded (Dollars):** Add column (SMW 6) and column (SMW 8).
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"of":["retirement.smw6","retirement.smw8"],"op":"sum"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 10, "No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025" (the worksheet is used here only for an annuity starting date after November 18, 1996, so line 10's question, "Was your annuity starting date before 1987?", is answered No) (2025; printed date 2026-02-25; sha256 482e9c48)

## (SMW 11) — `retirement.smw11`

- **Authored helper label:** Balance of cost to be recovered. Subtract line 10 from line 2
- **Encoded (Dollars):** Subtract column (SMW 10) from column (SMW 2).
- **Shown on the values sheet only when:** The Simplified Method Worksheet is completed (a pension or annuity, not an IRA, with some cost left to recover) (`retirement.smw_shown`)
- Expr: `{"from":"retirement.smw2","op":"subtract","take":"retirement.smw10"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 11, "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year. The payments you receive next year will generally be fully taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.cost_left`

- **Authored helper label:** Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)
- **Encoded (Bool):** column (SMW 7) > $0 (sales.zero)
- Expr: `{"gt":["retirement.smw7",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 28, Fully Taxable Pensions and Annuities, 'you got your entire cost back tax free before 2025' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.annuity_with_cost`

- **Authored helper label:** The Simplified Method applies and some cost is left to recover
- **Encoded (Bool):** helper "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)" = true and helper "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)" = true
- Expr: `{"all":[{"eq":["retirement.annuity_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.cost_left",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 28, Fully Taxable and Partially Taxable Pensions and Annuities (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.annuity_rollover`

- **Authored helper label:** A pension or annuity figured by the Simplified Method of which some amount was rolled over
- **Encoded (Bool):** helper "IRA distribution (lines 4a and 4b)" = false and helper "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)" = true and helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true
- Expr: `{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.annuity_if_cost",{"const":true}],"op":"test"},{"eq":["retirement.has_rollover",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 30, Rollovers, 'See Pub. 575 for more details on rollovers' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.annuity_taxable`

- **Authored helper label:** Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the cost has been recovered
- **Encoded (NonNegDollars):** Choose — [helper "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)" = true → column (SMW 9)] [helper "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)" = false → helper "Gross distribution, box 1"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.cost_left",{"const":true}],"op":"test"},"then":"retirement.smw9"},{"guard":{"eq":["retirement.cost_left",{"const":false}],"op":"test"},"then":"retirement.box1"}],"op":"choose"}`
- Cite: [i1040gi] p. 28, Fully Taxable Pensions and Annuities ('If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b'); p. 29, Simplified Method Worksheet, line 9 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ira_taxable`

- **Authored helper label:** Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA distribution)
- **Encoded (NonNegDollars):** Choose — [helper "Roth IRA distribution" = true → helper "No amount"] [helper "Roth IRA distribution" = false → helper "Box 1 less the amount rolled over"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.roth",{"const":true}],"op":"test"},"then":"retirement.zero"},{"guard":{"eq":["retirement.roth",{"const":false}],"op":"test"},"then":"retirement.ira_not_rolled"}],"op":"choose"}`
- Cite: [i1040gi] p. 27, line 4b, Exception 1 and Exception 2(b) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.ira_not_rolled`

- **Authored helper label:** Box 1 less the amount rolled over
- **Encoded (NonNegDollars):** Subtract helper "Amount rolled over (the whole distribution for a direct rollover)" from helper "Gross distribution, box 1". If zero or less, enter -0-.
- Expr: `{"from":"retirement.box1","op":"subtract_floor0","take":"retirement.rolled"}`
- Cite: [i1040gi] p. 27, Exception 1, 'enter the part not rolled over on line 4b' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.plan_excluded`

- **Authored helper label:** Taxable contributions (box 5) and the amount rolled over
- **Encoded (NonNegDollars):** Add helper "Employee contributions recovered tax free, box 5" and helper "Amount rolled over (the whole distribution for a direct rollover)".
- Expr: `{"of":["retirement.box5","retirement.rolled"],"op":"sum"}`
- Cite: [i1040gi] p. 30, Rollovers, 'subtract any contributions (usually shown in box 5) ... subtract the amount of the rollover' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.plan_simple`

- **Authored helper label:** Box 1 less taxable contributions (box 5) and the amount rolled over
- **Encoded (NonNegDollars):** Subtract helper "Taxable contributions (box 5) and the amount rolled over" from helper "Gross distribution, box 1". If zero or less, enter -0-.
- Expr: `{"from":"retirement.box1","op":"subtract_floor0","take":"retirement.plan_excluded"}`
- Cite: [i1040gi] p. 28, Fully Taxable Pensions and Annuities; p. 30, Rollovers (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.plan_taxable`

- **Authored helper label:** Taxable pension or annuity amount (the Simplified Method for an annuity with after-tax cost)
- **Encoded (NonNegDollars):** Choose — [helper "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)" = true → helper "Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the cost has been recovered"] [helper "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)" = false → helper "Box 1 less taxable contributions (box 5) and the amount rolled over"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.annuity_if_cost",{"const":true}],"op":"test"},"then":"retirement.annuity_taxable"},{"guard":{"eq":["retirement.annuity_if_cost",{"const":false}],"op":"test"},"then":"retirement.plan_simple"}],"op":"choose"}`
- Cite: [i1040gi] p. 28, Partially Taxable Pensions and Annuities; p. 29, Simplified Method Worksheet, line 9 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.taxable`

- **Authored helper label:** Taxable amount of this distribution (line 4b or 5b)
- **Encoded (NonNegDollars):** Choose — [helper "IRA distribution (lines 4a and 4b)" = true → helper "Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA distribution)"] [helper "IRA distribution (lines 4a and 4b)" = false → helper "Taxable pension or annuity amount (the Simplified Method for an annuity with after-tax cost)"]
- **Refusal:** when retirement.special is true, cannot complete Form 1099-R special cases (Forms 5329, 8606, 4972, 8915-F, Pub. 575 or 939). This distribution needs a form or rule outside this tool. Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when retirement.bad_code is true, cannot complete Form 8606 or another Form 1099-R code. A Roth IRA distribution other than a qualified distribution (code Q), code S other than from a traditional SIMPLE IRA, code 3 other than from an IRA, or a distribution code other than 7, 4, 2, 1, S, 3, G or Q, is outside this tool. Cite: [i1040gi] p. 27, Exception 2; f1099r Box 7 (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when retirement.screen_refused is true, cannot complete Form 5329 or Form 8915-F for this Form 1099-R. A qualified disaster recovery distribution, a modified series of substantially equal payments, an annuity or modified endowment contract distribution, a repayment, a December 30-31 long-term care distribution, more than one exception, an exception covering only part of a code 2 distribution, or a code 4 or 7 that does not fit needs Form 5329 or Form 8915-F rules this tool does not apply. Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)
- **Refusal:** when retirement.annuity_rollover is true, cannot complete Pub. 575 (rollover of a pension or annuity figured by the Simplified Method). A rollover from a pension or annuity whose taxable part is figured with the Simplified Method is outside this tool. Cite: [i1040gi] p. 30, Rollovers, 'See Pub. 575 for more details on rollovers' (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_ira",{"const":true}],"op":"test"},"then":"retirement.ira_taxable"},{"guard":{"eq":["retirement.is_ira",{"const":false}],"op":"test"},"then":"retirement.plan_taxable"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4b and 5b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.show_a`

- **Authored helper label:** An exception applies, so the total distribution goes on line 4a or 5a
- **Encoded (Bool):** (helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true or helper "Roth IRA distribution" = true or helper "IRA distribution (lines 4a and 4b)" = false and (helper "The Simplified Method applies and some cost is left to recover" = true or helper "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)" = false and helper "Employee contributions recovered tax free, box 5" > $0 (sales.zero)))
- Expr: `{"any":[{"eq":["retirement.has_rollover",{"const":true}],"op":"test"},{"eq":["retirement.roth",{"const":true}],"op":"test"},{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"any":[{"eq":["retirement.annuity_with_cost",{"const":true}],"op":"test"},{"all":[{"eq":["retirement.annuity_if_cost",{"const":false}],"op":"test"},{"gt":["retirement.box5",{"param":"sales.zero"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 27, line 4b ('If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don't make an entry on line 4a'); p. 28, Fully Taxable and Partially Taxable Pensions and Annuities; p. 30, Rollovers (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.amount_a`

- **Authored helper label:** Total distribution entered on line 4a or 5a (none when fully taxable)
- **Encoded (NonNegDollars):** Choose — [helper "An exception applies, so the total distribution goes on line 4a or 5a" = true → helper "Gross distribution, box 1"] [helper "An exception applies, so the total distribution goes on line 4a or 5a" = false → helper "No amount"]
- **Refusal:** when retirement.special is true, cannot complete Form 1099-R special cases (Forms 5329, 8606, 4972, 8915-F, Pub. 575 or 939). This distribution needs a form or rule outside this tool. Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when retirement.bad_code is true, cannot complete Form 8606 or another Form 1099-R code. A Roth IRA distribution other than a qualified distribution (code Q), code S other than from a traditional SIMPLE IRA, code 3 other than from an IRA, or a distribution code other than 7, 4, 2, 1, S, 3, G or Q, is outside this tool. Cite: [i1040gi] p. 27, Exception 2; f1099r Box 7 (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when retirement.screen_refused is true, cannot complete Form 5329 or Form 8915-F for this Form 1099-R. A qualified disaster recovery distribution, a modified series of substantially equal payments, an annuity or modified endowment contract distribution, a repayment, a December 30-31 long-term care distribution, more than one exception, an exception covering only part of a code 2 distribution, or a code 4 or 7 that does not fit needs Form 5329 or Form 8915-F rules this tool does not apply. Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)
- **Refusal:** when retirement.annuity_rollover is true, cannot complete Pub. 575 (rollover of a pension or annuity figured by the Simplified Method). A rollover from a pension or annuity whose taxable part is figured with the Simplified Method is outside this tool. Cite: [i1040gi] p. 30, Rollovers, 'See Pub. 575 for more details on rollovers' (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.show_a",{"const":true}],"op":"test"},"then":"retirement.box1"},{"guard":{"eq":["retirement.show_a",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i1040gi] pp. 27-30, lines 4a and 5a (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.sav_military`

- **Authored helper label:** Is this a distribution from a military retirement plan (other than the federal Thrift Savings Plan)?
- **Encoded (Bool):** Input — Is this a distribution from a military retirement plan (such as military retired pay), other than the federal Thrift Savings Plan (TSP)?
- Expr: `{"op":"input","source":"Is this a distribution from a military retirement plan (such as military retired pay), other than the federal Thrift Savings Plan (TSP)?"}`
- Cite: [f8880] p. 2, Line 4, "Distributions from a military retirement plan (other than the federal TSP)" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `retirement.sav_404k`

- **Authored helper label:** Is this a distribution of dividends paid on stock held by an employee stock ownership plan (section 404(k))?
- **Encoded (Bool):** Input — Is this a distribution of dividends paid on stock held by an employee stock ownership plan under section 404(k) (reported on its own Form 1099-R)?
- Expr: `{"op":"input","source":"Is this a distribution of dividends paid on stock held by an employee stock ownership plan under section 404(k) (reported on its own Form 1099-R)?"}`
- Cite: [f8880] p. 2, Line 4, "Distributions of dividends paid on stock held by an employee stock ownership plan under section 404(k)" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `retirement.sav_inherited`

- **Authored helper label:** Is this a distribution from an inherited IRA that you received as a beneficiary other than the owner's spouse?
- **Encoded (Bool):** Input — Is this a distribution from an inherited IRA that you (or your spouse, on a joint return) received as a beneficiary who was not the IRA owner's spouse?
- Interpretation: amb.2025.savers_inherited_plans
- Expr: `{"op":"input","source":"Is this a distribution from an inherited IRA that you (or your spouse, on a joint return) received as a beneficiary who was not the IRA owner's spouse?"}`
- Cite: [f8880] p. 2, Line 4, "Distributions from an inherited IRA by a nonspousal beneficiary" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `retirement.sav_excluded`

- **Authored helper label:** A distribution Form 8880 line 4 does not count (from a military retirement plan or of section 404(k) dividends, for a plan; from an inherited IRA as a nonspouse beneficiary, for an IRA)
- **Encoded (Bool):** (helper "IRA distribution (lines 4a and 4b)" = false and helper "Is this a distribution from a military retirement plan (other than the federal Thrift Savings Plan)?" = true or helper "IRA distribution (lines 4a and 4b)" = false and helper "Is this a distribution of dividends paid on stock held by an employee stock ownership plan (section 404(k))?" = true or helper "IRA distribution (lines 4a and 4b)" = true and helper "Is this a distribution from an inherited IRA that you received as a beneficiary other than the owner's spouse?" = true)
- Interpretation: amb.2025.savers_inherited_plans
- Expr: `{"any":[{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.sav_military",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.sav_404k",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.is_ira",{"const":true}],"op":"test"},{"eq":["retirement.sav_inherited",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f8880] p. 2, Line 4, "Don’t include any of the following"; "Distributions of dividends paid on stock held by an employee stock ownership plan under section 404(k)"; "Distributions from a military retirement plan (other than the federal TSP)"; "Distributions from an inherited IRA by a nonspousal beneficiary" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `retirement.sav_gross`

- **Authored helper label:** The distribution less the part rolled over (the whole distribution for a direct rollover)
- **Encoded (NonNegDollars):** Subtract helper "Amount rolled over (the whole distribution for a direct rollover)" from helper "Gross distribution, box 1". If zero or less, enter -0-.
- Interpretation: amb.2025.savers_line4_gross
- Expr: `{"from":"retirement.box1","op":"subtract_floor0","take":"retirement.rolled"}`
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions"; "Distributions not taxable as the result of a rollover or a trustee-to- trustee transfer" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `retirement.sav_amount`

- **Authored helper label:** This distribution's amount on Form 8880 line 4
- **Encoded (NonNegDollars):** Choose — [helper "A distribution Form 8880 line 4 does not count (from a military retirement plan or of section 404(k) dividends, for a plan; from an inherited IRA as a nonspouse beneficiary, for an IRA)" = true → helper "No amount"] [helper "A distribution Form 8880 line 4 does not count (from a military retirement plan or of section 404(k) dividends, for a plan; from an inherited IRA as a nonspouse beneficiary, for an IRA)" = false → helper "The distribution less the part rolled over (the whole distribution for a direct rollover)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.sav_excluded",{"const":true}],"op":"test"},"then":"retirement.zero"},{"guard":{"eq":["retirement.sav_excluded",{"const":false}],"op":"test"},"then":"retirement.sav_gross"}],"op":"choose"}`
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions) from any of the following types of plans" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `retirement.early`

- **Authored helper label:** An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)
- **Encoded (Bool):** (helper "Distribution code in box 7" = 'early_1' or helper "Distribution code in box 7" = 'simple_S')
- Expr: `{"any":[{"eq":["retirement.code",{"const":"early_1"}],"op":"test"},{"eq":["retirement.code",{"const":"simple_S"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 3, Line 1, "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" (2025; sha256 aec3d325)

## (helper) — `retirement.over59_all_year`

- **Authored helper label:** The person whose entry this is was 59½ or older all through 2025 (born in 1964 or earlier)
- **Encoded (Bool):** person helper "The year you were born" ≤ 1964 (age.over59h_all_year)
- Expr: `{"le":["person.birth_year",{"param":"age.over59h_all_year"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, exception 12, "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R. Include on line 2 the amount you received when you were age 59 1/2 or older." (2025; sha256 aec3d325)

## (helper) — `retirement.age_open`

- **Authored helper label:** The person turned 59½ during 2025 or may have (born in 1965 or 1966), so the birth year does not settle the age at each payment
- **Encoded (Bool):** person helper "The year you were born" > 1964 (age.over59h_all_year) and person helper "The year you were born" < 1967 (age.under59h_all_year)
- Expr: `{"all":[{"gt":["person.birth_year",{"param":"age.over59h_all_year"}],"op":"test"},{"lt":["person.birth_year",{"param":"age.under59h_all_year"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, exception 12, "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R. Include on line 2 the amount you received when you were age 59 1/2 or older." (2025; sha256 aec3d325)

## (helper) — `retirement.after59`

- **Authored helper label:** Were you age 59½ or older on the date of every payment of this money?
- **Encoded (Bool):** Input — Were you age 59½ or older on the date of every payment of this money?
- Expr: `{"op":"input","source":"Were you age 59½ or older on the date of every payment of this money?"}`
- Cite: [i5329] p. 5, Line 2, exception 12, "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R. Include on line 2 the amount you received when you were age 59 1/2 or older." (2025; sha256 aec3d325)

## (helper) — `retirement.ask_after59`

- **Authored helper label:** An early distribution (code 1 or S) of a person born in 1965 or 1966, whose age at each payment the birth year does not settle
- **Encoded (Bool):** helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true and helper "The person turned 59½ during 2025 or may have (born in 1965 or 1966), so the birth year does not settle the age at each payment" = true
- Expr: `{"all":[{"eq":["retirement.early",{"const":true}],"op":"test"},{"eq":["retirement.age_open",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, exception 12, "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R. Include on line 2 the amount you received when you were age 59 1/2 or older." (2025; sha256 aec3d325)

## (gate) — `retirement.after59_if_open`

- **Authored helper label:** 59½ or older at every payment, asked only of an early distribution (code 1 or S) when the birth year does not settle it (false otherwise)
- **Encoded (Bool):** Choose — [helper "An early distribution (code 1 or S) of a person born in 1965 or 1966, whose age at each payment the birth year does not settle" = true → helper "Were you age 59½ or older on the date of every payment of this money?"] [helper "An early distribution (code 1 or S) of a person born in 1965 or 1966, whose age at each payment the birth year does not settle" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.ask_after59",{"const":true}],"op":"test"},"then":"retirement.after59"},{"guard":{"eq":["retirement.ask_after59",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, exception 12, "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R. Include on line 2 the amount you received when you were age 59 1/2 or older." (2025; sha256 aec3d325)

## (helper) — `retirement.miscoded`

- **Authored helper label:** Exception 12: an early distribution (code 1 or S) received wholly at age 59½ or older, so all of it goes on Form 5329 line 2
- **Encoded (Bool):** helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true and (helper "The person whose entry this is was 59½ or older all through 2025 (born in 1964 or earlier)" = true or helper "59½ or older at every payment, asked only of an early distribution (code 1 or S) when the birth year does not settle it (false otherwise)" = true)
- Expr: `{"all":[{"eq":["retirement.early",{"const":true}],"op":"test"},{"any":[{"eq":["retirement.over59_all_year",{"const":true}],"op":"test"},{"eq":["retirement.after59_if_open",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, exception 12, "Distributions incorrectly indicated as early distributions by code 1, J, or S in box 7 of Form 1099-R. Include on line 2 the amount you received when you were age 59 1/2 or older." (2025; sha256 aec3d325)

## (gate) — `retirement.early_screen`

- **Authored helper label:** An early distribution of a kind Form 5329 Part I is not computed for here
- **Encoded (Bool):** Input — Is any of these true of this distribution: it is a qualified disaster recovery distribution (Form 8915-F); it is part of a series of substantially equal periodic payments that was modified (recapture); it is from an annuity contract or a modified endowment contract; it repays a birth or adoption, terminal illness, domestic abuse or emergency personal expense distribution; it is an emergency personal expense distribution within 3 years after an earlier one you have not repaid; it is a qualified long-term care distribution made December 30 or 31, 2025; or more than one exception to the additional tax applies to it?
- Expr: `{"op":"input","source":"Is any of these true of this distribution: it is a qualified disaster recovery distribution (Form 8915-F); it is part of a series of substantially equal periodic payments that was modified (recapture); it is from an annuity contract or a modified endowment contract; it repays a birth or adoption, terminal illness, domestic abuse or emergency personal expense distribution; it is an emergency personal expense distribution within 3 years after an earlier one you have not repaid; it is a qualified long-term care distribution made December 30 or 31, 2025; or more than one exception to the additional tax applies to it?"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.under59`

- **Authored helper label:** Were you under age 59½ when you received any of this money?
- **Encoded (Bool):** Input — Were you under age 59½ when you received any of this money?
- Expr: `{"op":"input","source":"Were you under age 59½ when you received any of this money?"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (helper) — `retirement.is_code7`

- **Authored helper label:** Code 7 (normal distribution)
- **Encoded (Bool):** helper "Distribution code in box 7" = 'normal_7'
- Expr: `{"eq":["retirement.code",{"const":"normal_7"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (gate) — `retirement.under59_if_code7`

- **Authored helper label:** Under age 59½ when the money was received, asked only with code 7 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Code 7 (normal distribution)" = true → helper "Were you under age 59½ when you received any of this money?"] [helper "Code 7 (normal distribution)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_code7",{"const":true}],"op":"test"},"then":"retirement.under59"},{"guard":{"eq":["retirement.is_code7",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (helper) — `retirement.sec457`

- **Authored helper label:** Is it from a section 457 plan (a deferred compensation plan of a state or local government or a tax-exempt employer), and not money that was rolled into that plan from another kind of plan?
- **Encoded (Bool):** Input — Is it from a section 457 plan (a deferred compensation plan of a state or local government or a tax-exempt employer), and not money that was rolled into that plan from another kind of plan?
- Expr: `{"op":"input","source":"Is it from a section 457 plan (a deferred compensation plan of a state or local government or a tax-exempt employer), and not money that was rolled into that plan from another kind of plan?"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (gate) — `retirement.sec457_if_under59`

- **Authored helper label:** A section 457 plan distribution not from a rollover, asked only with code 7 under age 59½ (false otherwise)
- **Encoded (Bool):** Choose — [helper "Under age 59½ when the money was received, asked only with code 7 (false otherwise)" = true → helper "Is it from a section 457 plan (a deferred compensation plan of a state or local government or a tax-exempt employer), and not money that was rolled into that plan from another kind of plan?"] [helper "Under age 59½ when the money was received, asked only with code 7 (false otherwise)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.under59_if_code7",{"const":true}],"op":"test"},"then":"retirement.sec457"},{"guard":{"eq":["retirement.under59_if_code7",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (helper) — `retirement.code7_wrong`

- **Authored helper label:** Code 7 although under age 59½, other than a section 457 plan distribution not from a rollover
- **Encoded (Bool):** helper "Under age 59½ when the money was received, asked only with code 7 (false otherwise)" = true and helper "A section 457 plan distribution not from a rollover, asked only with code 7 under age 59½ (false otherwise)" = false
- Expr: `{"all":[{"eq":["retirement.under59_if_code7",{"const":true}],"op":"test"},{"eq":["retirement.sec457_if_under59",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (helper) — `retirement.code2_partial`

- **Authored helper label:** Code 2 means the payer knows of an exception to the extra tax on early withdrawals. Does that exception fail to cover all of this money, or is this money one of a series of substantially equal payments that was changed in 2025?
- **Encoded (Bool):** Input — Code 2 means the payer knows of an exception to the extra tax on early withdrawals. Does that exception fail to cover all of this money, or is this money one of a series of substantially equal payments that was changed in 2025?
- Expr: `{"op":"input","source":"Code 2 means the payer knows of an exception to the extra tax on early withdrawals. Does that exception fail to cover all of this money, or is this money one of a series of substantially equal payments that was changed in 2025?"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude."; p590b p. 26, "You may have to pay a recapture tax if you modify ... the annual amount distributed ... under the substantially equal periodic payment exception" and "The recapture tax is imposed in the tax year in which the modification occurs" (2025; sha256 aec3d325)

## (helper) — `retirement.is_code2`

- **Authored helper label:** Code 2 (early distribution, exception applies)
- **Encoded (Bool):** helper "Distribution code in box 7" = 'early_exception_2'
- Expr: `{"eq":["retirement.code",{"const":"early_exception_2"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (gate) — `retirement.code2_partial_if_code2`

- **Authored helper label:** The code 2 exception does not cover the whole distribution, or the distribution is one of a series of substantially equal payments changed in 2025, asked only with code 2 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Code 2 (early distribution, exception applies)" = true → helper "Code 2 means the payer knows of an exception to the extra tax on early withdrawals. Does that exception fail to cover all of this money, or is this money one of a series of substantially equal payments that was changed in 2025?"] [helper "Code 2 (early distribution, exception applies)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_code2",{"const":true}],"op":"test"},"then":"retirement.code2_partial"},{"guard":{"eq":["retirement.is_code2",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (helper) — `retirement.not_beneficiary`

- **Authored helper label:** Code 4 is for money paid to the beneficiary of a person who has died. Did you get this money some other way, or are you the surviving spouse and have you made the IRA your own (by choosing to, by putting money into it, or by not taking a required minimum distribution from it as a beneficiary)?
- **Encoded (Bool):** Input — Code 4 is for money paid to the beneficiary of a person who has died. Did you get this money some other way, or are you the surviving spouse and have you made the IRA your own (by choosing to, by putting money into it, or by not taking a required minimum distribution from it as a beneficiary)?
- Expr: `{"op":"input","source":"Code 4 is for money paid to the beneficiary of a person who has died. Did you get this money some other way, or are you the surviving spouse and have you made the IRA your own (by choosing to, by putting money into it, or by not taking a required minimum distribution from it as a beneficiary)?"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (gate) — `retirement.not_beneficiary_if_death`

- **Authored helper label:** Code 4 although not a beneficiary, asked only with code 4 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Code 4 (death)" = true → helper "Code 4 is for money paid to the beneficiary of a person who has died. Did you get this money some other way, or are you the surviving spouse and have you made the IRA your own (by choosing to, by putting money into it, or by not taking a required minimum distribution from it as a beneficiary)?"] [helper "Code 4 (death)" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_death",{"const":true}],"op":"test"},"then":"retirement.not_beneficiary"},{"guard":{"eq":["retirement.is_death",{"const":false}],"op":"test"},"then":"retirement.no"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (gate) — `retirement.code_screen`

- **Authored helper label:** A code 2, 4 or 7 distribution whose code does not fit
- **Encoded (Bool):** (helper "The code 2 exception does not cover the whole distribution, or the distribution is one of a series of substantially equal payments changed in 2025, asked only with code 2 (false otherwise)" = true or helper "Code 7 although under age 59½, other than a section 457 plan distribution not from a rollover" = true or helper "Code 4 although not a beneficiary, asked only with code 4 (false otherwise)" = true)
- Expr: `{"any":[{"eq":["retirement.code2_partial_if_code2",{"const":true}],"op":"test"},{"eq":["retirement.code7_wrong",{"const":true}],"op":"test"},{"eq":["retirement.not_beneficiary_if_death",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude." (2025; sha256 aec3d325)

## (gate) — `retirement.screen_refused`

- **Authored helper label:** This Form 1099-R needs Form 5329 parts or codes this tool does not compute
- **Encoded (Bool):** (helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true and helper "An early distribution of a kind Form 5329 Part I is not computed for here" = true or (helper "Distribution code in box 7" = 'early_exception_2' or helper "Distribution code in box 7" = 'normal_7' or helper "Distribution code in box 7" = 'death_4') and helper "A code 2, 4 or 7 distribution whose code does not fit" = true)
- Expr: `{"any":[{"all":[{"eq":["retirement.early",{"const":true}],"op":"test"},{"eq":["retirement.early_screen",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"any":[{"eq":["retirement.code",{"const":"early_exception_2"}],"op":"test"},{"eq":["retirement.code",{"const":"normal_7"}],"op":"test"},{"eq":["retirement.code",{"const":"death_4"}],"op":"test"}],"op":"test"},{"eq":["retirement.code_screen",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.exception`

- **Authored helper label:** Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none
- **Encoded (Enum(early_exception)):** Input — Which exception to the 10% additional tax applies to this distribution?

  Enter the number from the table in the Form 5329 instructions (for example 02 substantially equal periodic payments, 03 disability, 05 medical expenses, 08 higher education expenses, 09 first home, 12 incorrectly coded as early, 19 birth or adoption, 20 terminal illness), or none.

  An exception applies only if its conditions are met, for example:
  - 01, a qualified retirement plan distribution (not an IRA) received after you separated from service in or after the year you reached age 55 (age 50 for qualified public safety employees and private sector firefighters) or after 25 years of service under the plan, whichever is earlier
  - 02, payments made at least annually for your life (or life expectancy) or the joint lives (or joint life expectancies) of you and your designated beneficiary, which from an employer plan must begin after separation from service
  - 03, total and permanent disability, if you can furnish proof that you can't do any substantial gainful activity because of your physical or mental condition and a medical determination has been made that the condition can be expected to result in death or to be of long, continued, and indefinite duration
  - 04, a distribution due to death (not from a modified endowment contract)
  - 08, an IRA distribution for qualified higher education expenses, only for the education of you, your spouse, or your or your spouse's children or grandchildren
  - 09, an IRA distribution for a first home, only for the main home of a first-time homebuyer who is you, your spouse, or your or your spouse's child, grandchild, parent or other ancestor; a first-time homebuyer had no present interest in a main home during the 2-year period ending on the date of acquisition (the date of a binding contract to buy it, or the date building or rebuilding began) and, if married, neither did their spouse
  - 11, a qualified reservist distribution, only if you were ordered or called to active duty after September 11, 2001, for more than 179 days or for an indefinite period because you are a member of a reserve component, the distribution is from an IRA or from amounts attributable to elective deferrals under a section 401(k) or 403(b) plan or a similar arrangement, and it was made no earlier than the date of the order or call and no later than the close of the active duty period
  - 19, a qualified birth or adoption distribution, only if made during the 1-year period beginning on the date your child was born or the legal adoption was finalized, an adopted child being an eligible adoptee (not the child of your spouse, and under age 18 or physically or mentally incapable of self-support)
- Expr: `{"op":"input","source":"Which exception to the 10% additional tax applies to this distribution?\n\nEnter the number from the table in the Form 5329 instructions (for example 02 substantially equal periodic payments, 03 disability, 05 medical expenses, 08 higher education expenses, 09 first home, 12 incorrectly coded as early, 19 birth or adoption, 20 terminal illness), or none.\n\nAn exception applies only if its conditions are met, for example:\n- 01, a qualified retirement plan distribution (not an IRA) received after you separated from service in or after the year you reached age 55 (age 50 for qualified public safety employees and private sector firefighters) or after 25 years of service under the plan, whichever is earlier\n- 02, payments made at least annually for your life (or life expectancy) or the joint lives (or joint life expectancies) of you and your designated beneficiary, which from an employer plan must begin after separation from service\n- 03, total and permanent disability, if you can furnish proof that you can't do any substantial gainful activity because of your physical or mental condition and a medical determination has been made that the condition can be expected to result in death or to be of long, continued, and indefinite duration\n- 04, a distribution due to death (not from a modified endowment contract)\n- 08, an IRA distribution for qualified higher education expenses, only for the education of you, your spouse, or your or your spouse's children or grandchildren\n- 09, an IRA distribution for a first home, only for the main home of a first-time homebuyer who is you, your spouse, or your or your spouse's child, grandchild, parent or other ancestor; a first-time homebuyer had no present interest in a main home during the 2-year period ending on the date of acquisition (the date of a binding contract to buy it, or the date building or rebuilding began) and, if married, neither did their spouse\n- 11, a qualified reservist distribution, only if you were ordered or called to active duty after September 11, 2001, for more than 179 days or for an indefinite period because you are a member of a reserve component, the distribution is from an IRA or from amounts attributable to elective deferrals under a section 401(k) or 403(b) plan or a similar arrangement, and it was made no earlier than the date of the order or call and no later than the close of the active duty period\n- 19, a qualified birth or adoption distribution, only if made during the 1-year period beginning on the date your child was born or the legal adoption was finalized, an adopted child being an eligible adoptee (not the child of your spouse, and under age 18 or physically or mentally incapable of self-support)"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.", "Qualified retirement plan distributions (doesn’t apply to IRAs) you received after separation from service when the separation from service occurs in or after the year you reach age 55 (age 50 for qualified public safety employees and private sector firefighters) or 25 years of service under the plan, whichever is earlier.", "(if from an employer plan, payments must begin after separation from service)", "You are considered disabled if you can furnish proof that you can’t do any substantial gainful activity because of your physical or mental condition.", "Distributions due to death (doesn’t apply to modified endowment contracts)." and "IRA distributions made for qualified higher education expenses."; p590b p. 27, "The education must be for you, your spouse, or the children or grandchildren of you or your spouse.", "who is any of the following.", "Your or your spouse's child.", "Your or your spouse's grandchild." and "Your or your spouse's parent or other ancestor."; p590b p. 28, First-time homebuyer, "you are a first-time homebuyer if you had no present interest in a main home during the 2-year period ending on the date of acquisition of the home which the distribution is being used to buy, build, or rebuild. If you are married, your spouse must also meet this no-ownership requirement.", "You enter into a binding contract to buy the main home", "You were ordered or called to active duty after September 11, 2001.", "of more than 179 days or for an indefinite period because you are a member of a reserve component.", "The distribution is from an IRA or from amounts attributable to elective deferrals under a section 401(k) or 403(b) plan or a similar arrangement.", "the date of the order or call to active duty and no later than the close of the active duty period.", "if made during the 1-year period beginning on the date on which your child was born or the date on which the legal adoption of your child was finalized" and "an eligible adoptee is any individual (other than the child of the taxpayer’s spouse) who has not reached age 18 or is physically or mentally incapable of self-support." (2025; sha256 aec3d325)

## (helper) — `retirement.has_exception`

- **Authored helper label:** An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)
- **Encoded (Bool):** helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true and helper "Exception 12: an early distribution (code 1 or S) received wholly at age 59½ or older, so all of it goes on Form 5329 line 2" = false and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" ≠ 'none'
- Expr: `{"all":[{"eq":["retirement.early",{"const":true}],"op":"test"},{"eq":["retirement.miscoded",{"const":false}],"op":"test"},{"ne":["retirement.exception",{"const":"none"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.exc_amount`

- **Authored helper label:** Amount of this distribution the exception covers
- **Encoded (NonNegDollars):** Input — Amount of this distribution that the exception covers (the tool applies the dollar limits per person).

  - Medical expenses (05), birth or adoption (19) and domestic abuse (22): the amount of the distribution that qualifies, whatever it was spent on; for 05 the tool limits it to the medical expenses above 7.5% of AGI, and for 22 enter no more than 50% of the present value of the IRA or plan account
  - First home (09): the amount used to pay qualified acquisition costs before the close of the 120th day after the day you received it
  - Emergency expenses (23): no more than your total interest in the IRA or plan account minus $1,000
  - Health insurance premiums while unemployed (07): the premiums you paid
  - Higher education (08): your adjusted qualified education expenses (Pub. 970, chapter 8)
  - Other exceptions: the amount the exception covers
- Interpretation: amb.2025.f5329_education_k12
- Expr: `{"op":"input","source":"Amount of this distribution that the exception covers (the tool applies the dollar limits per person).\n\n- Medical expenses (05), birth or adoption (19) and domestic abuse (22): the amount of the distribution that qualifies, whatever it was spent on; for 05 the tool limits it to the medical expenses above 7.5% of AGI, and for 22 enter no more than 50% of the present value of the IRA or plan account\n- First home (09): the amount used to pay qualified acquisition costs before the close of the 120th day after the day you received it\n- Emergency expenses (23): no more than your total interest in the IRA or plan account minus $1,000\n- Health insurance premiums while unemployed (07): the premiums you paid\n- Higher education (08): your adjusted qualified education expenses (Pub. 970, chapter 8)\n- Other exceptions: the amount the exception covers"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (gate) — `retirement.wrong_kind`

- **Authored helper label:** An exception that does not apply to this kind of account
- **Encoded (Bool):** helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true and (helper "IRA distribution (lines 4a and 4b)" = true and (helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e01' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e06' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e13' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e14' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e15' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e16' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e17' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e18') or helper "IRA distribution (lines 4a and 4b)" = false and (helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e07' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e08' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e09'))
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"any":[{"all":[{"eq":["retirement.is_ira",{"const":true}],"op":"test"},{"any":[{"eq":["retirement.exception",{"const":"e01"}],"op":"test"},{"eq":["retirement.exception",{"const":"e06"}],"op":"test"},{"eq":["retirement.exception",{"const":"e13"}],"op":"test"},{"eq":["retirement.exception",{"const":"e14"}],"op":"test"},{"eq":["retirement.exception",{"const":"e15"}],"op":"test"},{"eq":["retirement.exception",{"const":"e16"}],"op":"test"},{"eq":["retirement.exception",{"const":"e17"}],"op":"test"},{"eq":["retirement.exception",{"const":"e18"}],"op":"test"}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"any":[{"eq":["retirement.exception",{"const":"e07"}],"op":"test"},{"eq":["retirement.exception",{"const":"e08"}],"op":"test"},{"eq":["retirement.exception",{"const":"e09"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions (doesn’t apply to IRAs) you received after separation from service", "Distributions from a section 457 plan", "Distributions from a plan maintained by an employer if", "Distributions from annuity contracts", "phased retirement annuity payments made to federal employees", "Permissible withdrawals under section 414(w)"; p590b p. 24, Exceptions, "There are several exceptions to the age" (the IRA exceptions listed there include none of 13 to 18) (2025; sha256 aec3d325)

## (helper) — `retirement.l1`

- **Authored helper label:** Form 5329 line 1 share: the taxable amount of an early distribution
- **Encoded (NonNegDollars):** Choose — [helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true → helper "Taxable amount of this distribution (line 4b or 5b)"] [helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.early",{"const":true}],"op":"test"},"then":"retirement.taxable"},{"guard":{"eq":["retirement.early",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 3, Line 1, "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" (2025; sha256 aec3d325)

## (helper) — `retirement.exc_capped`

- **Authored helper label:** Smaller of the exception amount and the taxable amount
- **Encoded (NonNegDollars):** Enter the smaller of helper "Amount of this distribution the exception covers" or helper "Taxable amount of this distribution (line 4b or 5b)".
- Expr: `{"of":["retirement.exc_amount","retirement.taxable"],"op":"smaller_of"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_exc`

- **Authored helper label:** Form 5329 line 2 share under the exception named for the distribution, before the per-person limits
- **Encoded (NonNegDollars):** Choose — [helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true → helper "Smaller of the exception amount and the taxable amount"] [helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.has_exception",{"const":true}],"op":"test"},"then":"retirement.exc_capped"},{"guard":{"eq":["retirement.has_exception",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.l2`

- **Authored helper label:** Form 5329 line 2 share before the per-person limits
- **Encoded (NonNegDollars):** Choose — [helper "Exception 12: an early distribution (code 1 or S) received wholly at age 59½ or older, so all of it goes on Form 5329 line 2" = true → helper "Form 5329 line 1 share: the taxable amount of an early distribution"] [helper "Exception 12: an early distribution (code 1 or S) received wholly at age 59½ or older, so all of it goes on Form 5329 line 2" = false → helper "Form 5329 line 2 share under the exception named for the distribution, before the per-person limits"]
- **Refusal:** when retirement.wrong_kind is true, cannot complete Form 5329 line 2 exception for another kind of account. Exceptions 01, 06 and 13 to 18 do not apply to IRAs (they are for employer plans, section 457 plans and annuity contracts), and 07, 08 and 09 apply only to IRAs (i5329 p. 5; Pub. 590-B, p. 24). Check the exception number. Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions (doesn’t apply to IRAs) you received after separation from service" (2025; sha256 aec3d325)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.miscoded",{"const":true}],"op":"test"},"then":"retirement.l1"},{"guard":{"eq":["retirement.miscoded",{"const":false}],"op":"test"},"then":"retirement.l2_exc"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e05`

- **Authored helper label:** Exception 05
- **Encoded (Bool):** helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e05'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e05"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e05`

- **Authored helper label:** Line 2 share under exception 05
- **Encoded (NonNegDollars):** Choose — [helper "Exception 05" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 05" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e05",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e05",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e09`

- **Authored helper label:** Exception 09
- **Encoded (Bool):** helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e09'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e09"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "IRA distributions made for the purchase of a first home, up to $10,000." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e09`

- **Authored helper label:** Line 2 share under exception 09
- **Encoded (NonNegDollars):** Choose — [helper "Exception 09" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 09" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e09",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e09",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "IRA distributions made for the purchase of a first home, up to $10,000." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e19`

- **Authored helper label:** Exception 19
- **Encoded (Bool):** helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e19'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e19"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "A qualified distribution from a retirement plan for the birth or adoption of a child is a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e19`

- **Authored helper label:** Line 2 share under exception 19
- **Encoded (NonNegDollars):** Choose — [helper "Exception 19" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 19" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e19",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e19",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "A qualified distribution from a retirement plan for the birth or adoption of a child is a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e22`

- **Authored helper label:** Exception 22
- **Encoded (Bool):** helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e22'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e22"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified distributions to victims of domestic abuse." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e22`

- **Authored helper label:** Line 2 share under exception 22
- **Encoded (NonNegDollars):** Choose — [helper "Exception 22" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 22" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e22",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e22",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Qualified distributions to victims of domestic abuse." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e23`

- **Authored helper label:** Exception 23
- **Encoded (Bool):** helper "An exception applies, other than exception 12 on the whole distribution (an early code received wholly at age 59½ or older)" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e23'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e23"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "meeting the unforeseeable or immediate financial needs relating to necessary personal or family emergency expenses" (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e23`

- **Authored helper label:** Line 2 share under exception 23
- **Encoded (NonNegDollars):** Choose — [helper "Exception 23" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 23" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e23",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e23",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "meeting the unforeseeable or immediate financial needs relating to necessary personal or family emergency expenses" (2025; sha256 aec3d325)

## (helper) — `retirement.is_s`

- **Authored helper label:** Code S (a SIMPLE IRA distribution within 2 years)
- **Encoded (Bool):** helper "Distribution code in box 7" = 'simple_S'
- Expr: `{"eq":["retirement.code",{"const":"simple_S"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (helper) — `retirement.l1_s`

- **Authored helper label:** Line 1 share from a code S distribution
- **Encoded (NonNegDollars):** Choose — [helper "Code S (a SIMPLE IRA distribution within 2 years)" = true → helper "Form 5329 line 1 share: the taxable amount of an early distribution"] [helper "Code S (a SIMPLE IRA distribution within 2 years)" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_s",{"const":true}],"op":"test"},"then":"retirement.l1"},{"guard":{"eq":["retirement.is_s",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_s`

- **Authored helper label:** Line 2 share from a code S distribution
- **Encoded (NonNegDollars):** Choose — [helper "Code S (a SIMPLE IRA distribution within 2 years)" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Code S (a SIMPLE IRA distribution within 2 years)" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_s",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_s",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)
