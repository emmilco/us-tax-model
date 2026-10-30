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

- **Authored helper label:** Amount you rolled over within 60 days to a qualified plan or IRA (not a Roth account)
- **Encoded (NonNegDollars):** Input — Amount of this distribution you rolled over within 60 days to a qualified plan or an IRA other than a Roth IRA (for a direct rollover, code G, the whole distribution is treated as rolled over)
- Expr: `{"op":"input","source":"Amount of this distribution you rolled over within 60 days to a qualified plan or an IRA other than a Roth IRA (for a direct rollover, code G, the whole distribution is treated as rolled over)"}`
- Cite: [i1040gi] p. 27, Exception 1 (IRA rollovers); p. 30, Rollovers (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.special`

- **Authored helper label:** Does this distribution involve any of these: a disability pension received before minimum retirement age, or a pension partly excludable because you were disabled as a result of a terrorist attack; a corrective distribution of excess deferrals or contributions; a qualified charitable distribution or HSA funding distribution; nondeductible contributions to any traditional IRA; a conversion or recharacterization (Form 8606); a 2024 or 2025 IRA contribution returned to you, or excess contributions for an earlier year returned to you in 2025; a rollover to a Roth IRA or designated Roth account; a lump-sum distribution you may report on Form 4972; a nonqualified annuity; the retired public safety officer premium exclusion; a death benefit exclusion; a plan loan offset; a Form RRB-1099-R; U.S. Civil Service retirement benefits under the alternative annuity option (Pub. 721); or a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996, or for which the Simplified Method does not apply (the General Rule)?
- **Encoded (Bool):** Input — Does this distribution involve any of these: a disability pension received before minimum retirement age, or a pension partly excludable because you were disabled as a result of a terrorist attack; a corrective distribution of excess deferrals or contributions; a qualified charitable distribution or HSA funding distribution; nondeductible contributions to any traditional IRA; a conversion or recharacterization (Form 8606); a 2024 or 2025 IRA contribution returned to you, or excess contributions for an earlier year returned to you in 2025; a rollover to a Roth IRA or designated Roth account; a lump-sum distribution you may report on Form 4972; a nonqualified annuity; the retired public safety officer premium exclusion; a death benefit exclusion; a plan loan offset; a Form RRB-1099-R; U.S. Civil Service retirement benefits under the alternative annuity option (Pub. 721); or a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996, or for which the Simplified Method does not apply (the General Rule)?
- Expr: `{"op":"input","source":"Does this distribution involve any of these: a disability pension received before minimum retirement age, or a pension partly excludable because you were disabled as a result of a terrorist attack; a corrective distribution of excess deferrals or contributions; a qualified charitable distribution or HSA funding distribution; nondeductible contributions to any traditional IRA; a conversion or recharacterization (Form 8606); a 2024 or 2025 IRA contribution returned to you, or excess contributions for an earlier year returned to you in 2025; a rollover to a Roth IRA or designated Roth account; a lump-sum distribution you may report on Form 4972; a nonqualified annuity; the retired public safety officer premium exclusion; a death benefit exclusion; a plan loan offset; a Form RRB-1099-R; U.S. Civil Service retirement benefits under the alternative annuity option (Pub. 721); or a pension or annuity in which you have after-tax cost whose annuity starting date was before November 19, 1996, or for which the Simplified Method does not apply (the General Rule)?"}`
- Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method; f1099r Box 7 codes (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.annuity`

- **Authored helper label:** Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)
- **Encoded (Bool):** Input — Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)
- Expr: `{"op":"input","source":"Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)"}`
- Cite: [i1040gi] p. 30, Simplified Method, conditions 1 and 2; p. 28, Partially Taxable Pensions and Annuities (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.cost`

- **Authored helper label:** Your cost in the plan at the annuity starting date (Simplified Method Worksheet, line 2)
- **Encoded (NonNegDollars):** Input — Your cost (net investment, after-tax contributions) in the plan at the annuity starting date; it may be shown in Form 1099-R box 9b
- Expr: `{"op":"input","source":"Your cost (net investment, after-tax contributions) in the plan at the annuity starting date; it may be shown in Form 1099-R box 9b"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 2; p. 30, Cost (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.used_last_year`

- **Authored helper label:** Did you complete this worksheet for this annuity last year?
- **Encoded (Bool):** Input — Did you complete the Simplified Method Worksheet for this annuity last year?
- Expr: `{"op":"input","source":"Did you complete the Simplified Method Worksheet for this annuity last year?"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, note under line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.last_line4`

- **Authored helper label:** Line 4 of last year's Simplified Method Worksheet
- **Encoded (NonNegDollars):** Input — The amount on line 4 of last year's Simplified Method Worksheet for this annuity
- Expr: `{"op":"input","source":"The amount on line 4 of last year's Simplified Method Worksheet for this annuity"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, note under line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.joint_life`

- **Authored helper label:** Annuity starting date after 1997 and payments for your life and that of your beneficiary?
- **Encoded (Bool):** Input — Was the annuity starting date after 1997, with payments for your life and that of your beneficiary (Table 2)?
- Expr: `{"op":"input","source":"Was the annuity starting date after 1997, with payments for your life and that of your beneficiary (Table 2)?"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 3 and Table 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.age`

- **Authored helper label:** Age at the annuity starting date
- **Encoded (Count):** Input — Your age at the annuity starting date (if you are the survivor of a retiree, the retiree's age on their annuity starting date)
- Expr: `{"op":"input","source":"Your age at the annuity starting date (if you are the survivor of a retiree, the retiree's age on their annuity starting date)"}`
- Cite: [i1040gi] p. 29, Table 1; p. 30, Age (or Combined Ages) at Annuity Starting Date (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.combined_age`

- **Authored helper label:** Combined ages at the annuity starting date
- **Encoded (Count):** Input — Your combined ages (yours and your beneficiary's) at the annuity starting date
- Expr: `{"op":"input","source":"Your combined ages (yours and your beneficiary's) at the annuity starting date"}`
- Cite: [i1040gi] p. 29, Table 2; p. 30, Age (or Combined Ages) at Annuity Starting Date (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.months`

- **Authored helper label:** Number of months for which this year's payments were made
- **Encoded (Count):** Input — Number of months in 2025 for which payments were made
- Expr: `{"op":"input","source":"Number of months in 2025 for which payments were made"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.recovered`

- **Authored helper label:** Amount recovered tax free in years after 1986 (line 10 of last year's worksheet)
- **Encoded (NonNegDollars):** Input — Amount, if any, recovered tax free in years after 1986 (if you completed this worksheet last year, line 10 of last year's worksheet)
- Expr: `{"op":"input","source":"Amount, if any, recovered tax free in years after 1986 (if you completed this worksheet last year, line 10 of last year's worksheet)"}`
- Cite: [i1040gi] p. 29, Simplified Method Worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

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
- **Encoded (Bool):** (helper "Distribution code in box 7" = 'other' or helper "Distribution code in box 7" = 'simple_S' and helper "Kind of account the distribution came from" ≠ 'traditional_ira' or helper "Distribution code in box 7" = 'disability_3' and helper "IRA distribution (lines 4a and 4b)" = false or helper "Kind of account the distribution came from" = 'roth_ira' and helper "Distribution code in box 7" ≠ 'qualified_roth_Q' or helper "Distribution code in box 7" = 'qualified_roth_Q' and helper "Kind of account the distribution came from" ≠ 'roth_ira')
- Expr: `{"any":[{"eq":["retirement.code",{"const":"other"}],"op":"test"},{"all":[{"eq":["retirement.code",{"const":"simple_S"}],"op":"test"},{"ne":["retirement.account",{"const":"traditional_ira"}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.code",{"const":"disability_3"}],"op":"test"},{"eq":["retirement.is_ira",{"const":false}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.account",{"const":"roth_ira"}],"op":"test"},{"ne":["retirement.code",{"const":"qualified_roth_Q"}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.code",{"const":"qualified_roth_Q"}],"op":"test"},{"ne":["retirement.account",{"const":"roth_ira"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 27, Exception 2 (a Roth IRA distribution other than code Q needs Form 8606); f1099r pp. 7 and 9, Box 7, "The following codes identify the distribution you received", "Q—Qualified distribution from a Roth IRA or Roth SIMPLE IRA" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.rolled`

- **Authored helper label:** Amount rolled over (the whole distribution for a direct rollover)
- **Encoded (NonNegDollars):** Choose — [helper "Direct rollover (code G)" = true → helper "Gross distribution, box 1"] [helper "Direct rollover (code G)" = false → helper "Amount you rolled over within 60 days to a qualified plan or IRA (not a Roth account)"]
- **Refusal:** when retirement.special is true, cannot complete Form 1099-R special cases (Forms 5329, 8606, 4972, 8915-F, Pub. 575 or 939). This distribution needs a form or rule outside this tool. Cite: [i1040gi] pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum Distributions, Insurance Premiums for Retired Public Safety Officers, Simplified Method (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when retirement.bad_code is true, cannot complete Form 8606 or another Form 1099-R code. A Roth IRA distribution other than a qualified distribution (code Q), code S other than from a traditional SIMPLE IRA, code 3 other than from an IRA, or a distribution code other than 7, 4, 2, 1, S, 3, G or Q, is outside this tool. Cite: [i1040gi] p. 27, Exception 2; f1099r Box 7 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.direct",{"const":true}],"op":"test"},"then":"retirement.box1"},{"guard":{"eq":["retirement.direct",{"const":false}],"op":"test"},"then":"retirement.rollover"}],"op":"choose"}`
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
- **Encoded (Bool):** helper "Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)" = true and helper "Some cost is left to recover (line 7 of the Simplified Method Worksheet is more than zero)" = true
- Expr: `{"all":[{"eq":["retirement.annuity",{"const":true}],"op":"test"},{"eq":["retirement.cost_left",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 28, Fully Taxable and Partially Taxable Pensions and Annuities (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `retirement.annuity_rollover`

- **Authored helper label:** A pension or annuity figured by the Simplified Method of which some amount was rolled over
- **Encoded (Bool):** helper "IRA distribution (lines 4a and 4b)" = false and helper "Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)" = true and helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true
- Expr: `{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.annuity",{"const":true}],"op":"test"},{"eq":["retirement.has_rollover",{"const":true}],"op":"test"}],"op":"test"}`
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
- **Encoded (NonNegDollars):** Choose — [helper "Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)" = true → helper "Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the cost has been recovered"] [helper "Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)" = false → helper "Box 1 less taxable contributions (box 5) and the amount rolled over"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.annuity",{"const":true}],"op":"test"},"then":"retirement.annuity_taxable"},{"guard":{"eq":["retirement.annuity",{"const":false}],"op":"test"},"then":"retirement.plan_simple"}],"op":"choose"}`
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
- **Encoded (Bool):** (helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true or helper "Roth IRA distribution" = true or helper "IRA distribution (lines 4a and 4b)" = false and (helper "The Simplified Method applies and some cost is left to recover" = true or helper "Is this a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity, paid in periodic payments in which you have after-tax cost (box 9b or your records), with an annuity starting date after November 18, 1996, and on that date you were under age 75 or had fewer than 5 years of guaranteed payments? (This is when the Simplified Method applies.)" = false and helper "Employee contributions recovered tax free, box 5" > $0 (sales.zero)))
- Expr: `{"any":[{"eq":["retirement.has_rollover",{"const":true}],"op":"test"},{"eq":["retirement.roth",{"const":true}],"op":"test"},{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"any":[{"eq":["retirement.annuity_with_cost",{"const":true}],"op":"test"},{"all":[{"eq":["retirement.annuity",{"const":false}],"op":"test"},{"gt":["retirement.box5",{"param":"sales.zero"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
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

## (gate) — `retirement.early_screen`

- **Authored helper label:** An early distribution of a kind Form 5329 Part I is not computed for here
- **Encoded (Bool):** Input — Is any of these true of this distribution: it is a qualified disaster recovery distribution (Form 8915-F); it is part of a series of substantially equal periodic payments that was modified (recapture); it is from an annuity contract or a modified endowment contract; it repays a birth or adoption, terminal illness, domestic abuse or emergency personal expense distribution; it is an emergency personal expense distribution within 3 years after an earlier one you have not repaid; it is a qualified long-term care distribution made December 30 or 31, 2025; or more than one exception to the additional tax applies to it?
- Expr: `{"op":"input","source":"Is any of these true of this distribution: it is a qualified disaster recovery distribution (Form 8915-F); it is part of a series of substantially equal periodic payments that was modified (recapture); it is from an annuity contract or a modified endowment contract; it repays a birth or adoption, terminal illness, domestic abuse or emergency personal expense distribution; it is an emergency personal expense distribution within 3 years after an earlier one you have not repaid; it is a qualified long-term care distribution made December 30 or 31, 2025; or more than one exception to the additional tax applies to it?"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (gate) — `retirement.code_screen`

- **Authored helper label:** A code 2, 4 or 7 distribution whose code does not fit
- **Encoded (Bool):** Input — Is either of these true of this distribution: the exception that code 2 shows covers only part of it; or its code is wrong because you were under age 59½ when you received it (code 7) or you are not the beneficiary of a person who died (code 4)?
- Expr: `{"op":"input","source":"Is either of these true of this distribution: the exception that code 2 shows covers only part of it; or its code is wrong because you were under age 59½ when you received it (code 7) or you are not the beneficiary of a person who died (code 4)?"}`
- Cite: [i5329] p. 1, Who Must File, "You received a distribution subject to the tax on early distributions from a qualified retirement plan (other than a Roth IRA) and you meet an exception to the tax on early distributions from the list shown later, but box 7 of your Form 1099-R doesn’t indicate an exception or the exception doesn’t apply to the entire distribution." (2025; sha256 aec3d325)

## (gate) — `retirement.screen_refused`

- **Authored helper label:** This Form 1099-R needs Form 5329 parts or codes this tool does not compute
- **Encoded (Bool):** (helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true and helper "An early distribution of a kind Form 5329 Part I is not computed for here" = true or (helper "Distribution code in box 7" = 'early_exception_2' or helper "Distribution code in box 7" = 'normal_7' or helper "Distribution code in box 7" = 'death_4') and helper "A code 2, 4 or 7 distribution whose code does not fit" = true)
- Expr: `{"any":[{"all":[{"eq":["retirement.early",{"const":true}],"op":"test"},{"eq":["retirement.early_screen",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"any":[{"eq":["retirement.code",{"const":"early_exception_2"}],"op":"test"},{"eq":["retirement.code",{"const":"normal_7"}],"op":"test"},{"eq":["retirement.code",{"const":"death_4"}],"op":"test"}],"op":"test"},{"eq":["retirement.code_screen",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.exception`

- **Authored helper label:** Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none
- **Encoded (Enum(early_exception)):** Input — Which exception to the 10% additional tax applies to this distribution? Enter the number from the table in the Form 5329 instructions (for example 02 substantially equal periodic payments, 03 disability, 05 medical expenses, 08 higher education expenses, 09 first home, 12 incorrectly coded as early, 19 birth or adoption, 20 terminal illness), or none.
- Expr: `{"op":"input","source":"Which exception to the 10% additional tax applies to this distribution? Enter the number from the table in the Form 5329 instructions (for example 02 substantially equal periodic payments, 03 disability, 05 medical expenses, 08 higher education expenses, 09 first home, 12 incorrectly coded as early, 19 birth or adoption, 20 terminal illness), or none."}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.has_exception`

- **Authored helper label:** An exception applies
- **Encoded (Bool):** helper "An early distribution with no known exception (code 1, or code S from a SIMPLE IRA in the first 2 years)" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" ≠ 'none'
- Expr: `{"all":[{"eq":["retirement.early",{"const":true}],"op":"test"},{"ne":["retirement.exception",{"const":"none"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.exc_amount`

- **Authored helper label:** Amount of this distribution the exception covers
- **Encoded (NonNegDollars):** Input — Amount of this distribution that the exception covers (the tool applies the dollar limits per person). Medical expenses (05), birth or adoption (19) and domestic abuse (22): the amount of the distribution that qualifies, whatever it was spent on; for 05 the tool limits it to the medical expenses above 7.5% of AGI, and for 22 enter no more than 50% of the present value of the IRA or plan account. First home (09): the amount used to pay qualified acquisition costs before the close of the 120th day after the day you received it. Emergency expenses (23): no more than your total interest in the IRA or plan account minus $1,000. Health insurance premiums while unemployed (07): the premiums you paid. Higher education (08): your adjusted qualified education expenses (Pub. 970, chapter 8). Other exceptions: the amount the exception covers.
- Interpretation: amb.2025.f5329_education_k12
- Expr: `{"op":"input","source":"Amount of this distribution that the exception covers (the tool applies the dollar limits per person). Medical expenses (05), birth or adoption (19) and domestic abuse (22): the amount of the distribution that qualifies, whatever it was spent on; for 05 the tool limits it to the medical expenses above 7.5% of AGI, and for 22 enter no more than 50% of the present value of the IRA or plan account. First home (09): the amount used to pay qualified acquisition costs before the close of the 120th day after the day you received it. Emergency expenses (23): no more than your total interest in the IRA or plan account minus $1,000. Health insurance premiums while unemployed (07): the premiums you paid. Higher education (08): your adjusted qualified education expenses (Pub. 970, chapter 8). Other exceptions: the amount the exception covers."}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (gate) — `retirement.wrong_kind`

- **Authored helper label:** An exception that does not apply to this kind of account
- **Encoded (Bool):** helper "An exception applies" = true and (helper "IRA distribution (lines 4a and 4b)" = true and (helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e01' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e06') or helper "IRA distribution (lines 4a and 4b)" = false and (helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e07' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e08' or helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e09'))
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"any":[{"all":[{"eq":["retirement.is_ira",{"const":true}],"op":"test"},{"any":[{"eq":["retirement.exception",{"const":"e01"}],"op":"test"},{"eq":["retirement.exception",{"const":"e06"}],"op":"test"}],"op":"test"}],"op":"test"},{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"any":[{"eq":["retirement.exception",{"const":"e07"}],"op":"test"},{"eq":["retirement.exception",{"const":"e08"}],"op":"test"},{"eq":["retirement.exception",{"const":"e09"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions (doesn’t apply to IRAs) you received after separation from service" (2025; sha256 aec3d325)

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

## (helper) — `retirement.l2`

- **Authored helper label:** Form 5329 line 2 share before the per-person limits
- **Encoded (NonNegDollars):** Choose — [helper "An exception applies" = true → helper "Smaller of the exception amount and the taxable amount"] [helper "An exception applies" = false → helper "No amount"]
- **Refusal:** when retirement.wrong_kind is true, cannot complete Form 5329 line 2 exception for another kind of account. Exceptions 01 and 06 do not apply to IRAs, and 07, 08 and 09 apply only to IRAs (i5329 p. 5). Check the exception number. Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions (doesn’t apply to IRAs) you received after separation from service" (2025; sha256 aec3d325)
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.has_exception",{"const":true}],"op":"test"},"then":"retirement.exc_capped"},{"guard":{"eq":["retirement.has_exception",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e05`

- **Authored helper label:** Exception 05
- **Encoded (Bool):** helper "An exception applies" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e05'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e05"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e05`

- **Authored helper label:** Line 2 share under exception 05
- **Encoded (NonNegDollars):** Choose — [helper "Exception 05" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 05" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e05",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e05",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e09`

- **Authored helper label:** Exception 09
- **Encoded (Bool):** helper "An exception applies" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e09'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e09"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "IRA distributions made for the purchase of a first home, up to $10,000." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e09`

- **Authored helper label:** Line 2 share under exception 09
- **Encoded (NonNegDollars):** Choose — [helper "Exception 09" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 09" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e09",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e09",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "IRA distributions made for the purchase of a first home, up to $10,000." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e19`

- **Authored helper label:** Exception 19
- **Encoded (Bool):** helper "An exception applies" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e19'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e19"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "A qualified distribution from a retirement plan for the birth or adoption of a child is a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e19`

- **Authored helper label:** Line 2 share under exception 19
- **Encoded (NonNegDollars):** Choose — [helper "Exception 19" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 19" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e19",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e19",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "A qualified distribution from a retirement plan for the birth or adoption of a child is a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e22`

- **Authored helper label:** Exception 22
- **Encoded (Bool):** helper "An exception applies" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e22'
- Expr: `{"all":[{"eq":["retirement.has_exception",{"const":true}],"op":"test"},{"eq":["retirement.exception",{"const":"e22"}],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified distributions to victims of domestic abuse." (2025; sha256 aec3d325)

## (helper) — `retirement.l2_e22`

- **Authored helper label:** Line 2 share under exception 22
- **Encoded (NonNegDollars):** Choose — [helper "Exception 22" = true → helper "Form 5329 line 2 share before the per-person limits"] [helper "Exception 22" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["retirement.is_e22",{"const":true}],"op":"test"},"then":"retirement.l2"},{"guard":{"eq":["retirement.is_e22",{"const":false}],"op":"test"},"then":"retirement.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Qualified distributions to victims of domestic abuse." (2025; sha256 aec3d325)

## (helper) — `retirement.is_e23`

- **Authored helper label:** Exception 23
- **Encoded (Bool):** helper "An exception applies" = true and helper "Exception to the additional tax that applies to this distribution (i5329 p. 5 table), or none" = 'e23'
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
