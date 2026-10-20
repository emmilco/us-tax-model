# Form 4562 — one item of depreciable property (other than a vehicle) of a business

- Document: `asset` (form, tax year 2025)
- Collection: keyed entries within sc; [i4562] p. 9, Lines 19a Through 19j, and p. 1, Who Must File, "File a separate Form 4562 for each business or activity" (2025; sha256 5c1c95b7)
- Note: One entry per item of property other than a vehicle (vehicles are scveh entries), placed in service 2005 to 2025 and depreciated by the GDS percentage tables; its lines feed Form 4562 lines 6, 14, 17, 19 and, for listed property, lines 25, 26 and 29 of its business. Refused: the classes outside this tool, dispositions, exchanges, real property, ADS and other methods, basis adjustments, amortization, listed property used 50% or less for business, and the other items of the screen.

## (helper) — `asset.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j (2025; sha256 5c1c95b7)

## (a) — `asset.class`

- **Authored helper label:** Asset class of the property (Pub. 946, Appendix B)
- **Encoded (Enum(asset_class)):** Input — The asset class of this property: find the property in Pub. 946 Appendix B, Table B-1, and the activity it is used in in Table B-2 (use the Table B-2 class when the property is specifically listed there under your activity); or choose A (personal property with no class life), B (qualified technological equipment), C (property used in research and experimentation), or qualified improvement property
- Expr: `{"op":"input","source":"The asset class of this property: find the property in Pub. 946 Appendix B, Table B-1, and the activity it is used in in Table B-2 (use the Table B-2 class when the property is specifically listed there under your activity); or choose A (personal property with no class life), B (qualified technological equipment), C (property used in research and experimentation), or qualified improvement property"}`
- Cite: [p946] p. 98, Appendix B, How To Use the Tables; i4562 p. 10, Determining the classification (For use in preparing 2025 returns; sha256 07fadfb2)

## (d) — `asset.period`

- **Authored helper label:** Recovery period under GDS for the asset class
- **Encoded (Enum(macrs_period)):** Find the entry in GDS recovery period by asset class (Pub. 946, Appendix B, Tables B-1 and B-2) for asset_class column (a).
- Expr: `{"keys":["asset.class"],"op":"keyed_lookup","table":"class_lives"}`
- Cite: [p946] Appendix B, Tables B-1 and B-2, GDS (MACRS) column; i4562 p. 11, Column (d)—Recovery period (For use in preparing 2025 returns; sha256 07fadfb2)

## (gate) — `asset.outside`

- **Authored helper label:** The asset class is outside this tool
- **Encoded (Bool):** column (d) = 'outside'
- Expr: `{"eq":["asset.period",{"const":"outside"}],"op":"test"}`
- Cite: [p946] Appendix B, Tables B-1 and B-2 (farming classes, classes with footnotes, and periods other than 3 to 20 years) (For use in preparing 2025 returns; sha256 07fadfb2)

## (screen) — `asset.screen`

- **Authored helper label:** Does any of these apply to this property?
- **Encoded (Bool):** Input — Does any of these apply to this property: you disposed of it or converted it to personal use in 2025; you acquired it in a like-kind exchange or an involuntary conversion, from a related person, or by gift or inheritance; it is real property (a building or a structural component, other than qualified improvement property) or land; it is a car, truck or other vehicle (enter vehicles separately); you depreciate it under ADS, under an elected straight line or 150% declining balance method, or by a method other than the MACRS percentage tables; its basis was adjusted for anything other than depreciation (for example a casualty loss); it is in a general asset account; you amortize it; it is used predominantly outside the United States, or is tax-exempt use or tax-exempt bond financed property; it was placed in service before 2005; its business use percentage has changed since you placed it in service; or it is property with a long production period, an aircraft, or qualified production property?
- Expr: `{"op":"input","source":"Does any of these apply to this property: you disposed of it or converted it to personal use in 2025; you acquired it in a like-kind exchange or an involuntary conversion, from a related person, or by gift or inheritance; it is real property (a building or a structural component, other than qualified improvement property) or land; it is a car, truck or other vehicle (enter vehicles separately); you depreciate it under ADS, under an elected straight line or 150% declining balance method, or by a method other than the MACRS percentage tables; its basis was adjusted for anything other than depreciation (for example a casualty loss); it is in a general asset account; you amortize it; it is used predominantly outside the United States, or is tax-exempt use or tax-exempt bond financed property; it was placed in service before 2005; its business use percentage has changed since you placed it in service; or it is property with a long production period, an aircraft, or qualified production property?"}`
- Cite: [i4562] pp. 8-12, Part III, Lines 16 to 20 and MACRS recapture; p946 p. 37, Rules Covering the Use of the Tables (2025; sha256 5c1c95b7)

## (gate) — `asset.screened`

- **Authored helper label:** This property is outside this tool
- **Encoded (Bool):** (helper "The asset class is outside this tool" = true or column (screen) (asset.screen) = true)
- Expr: `{"any":[{"eq":["asset.outside",{"const":true}],"op":"test"},{"eq":["asset.screen",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i4562] pp. 8-12, Part III (2025; sha256 5c1c95b7)

## (b) — `asset.placed`

- **Authored helper label:** Year placed in service
- **Encoded (Enum(placed_year)):** Input — The year you placed this property in service in the business (2005 to 2025)
- Expr: `{"op":"input","source":"The year you placed this property in service in the business (2005 to 2025)"}`
- Cite: [i4562] p. 11, Column (b)—Month and year placed in service; p946 p. 39, the example of the third recovery year (2025; sha256 5c1c95b7)

## (helper) — `asset.cost`

- **Authored helper label:** Cost or other basis
- **Encoded (NonNegDollars):** Input — The cost or other basis of the property (what you paid, including sales tax, delivery and installation; for property converted from personal use, the smaller of its adjusted basis or its fair market value on the date of conversion)
- **Refusal:** when asset.screened is true, cannot complete Form 4562 property outside this tool (Pub. 946 Appendix B class, disposition, exchange, real property, ADS, other methods, basis adjustment, amortization and the other items of the screen). This property is outside the depreciation this tool covers. Cite: [i4562] pp. 8-12, Part III, and Pub. 946 Appendix B (2025; sha256 5c1c95b7)
- Expr: `{"op":"input","source":"The cost or other basis of the property (what you paid, including sales tax, delivery and installation; for property converted from personal use, the smaller of its adjusted basis or its fair market value on the date of conversion)"}`
- Cite: [i4562] p. 11, Column (c)—Basis for depreciation; p. 14, Column (d)—Cost or other basis (2025; sha256 5c1c95b7)

## (helper) — `asset.pct`

- **Authored helper label:** Business/investment use percentage (whole percent)
- **Encoded (Count):** Input — The percentage of this property's use that is for this business (a whole number from 1 to 100)
- Expr: `{"op":"input","source":"The percentage of this property's use that is for this business (a whole number from 1 to 100)"}`
- Cite: [i4562] p. 11, Column (c)—Basis for depreciation, "multiply the cost or other basis of the property by the percentage of business/investment use" (2025; sha256 5c1c95b7)

## (helper) — `asset.cent`

- **Authored helper label:** One cent
- **Encoded (NonNegDollars):** Enter $0.01 (sc.one_cent).
- Expr: `{"op":"param","ref":"sc.one_cent"}`
- Cite: [i4562] p. 11, Column (c), percentage of business/investment use (2025; sha256 5c1c95b7)

## (helper) — `asset.hundred`

- **Authored helper label:** One hundred cents (100%)
- **Encoded (NonNegDollars):** Enter $1 (sc.hundred_cents).
- Expr: `{"op":"param","ref":"sc.hundred_cents"}`
- Cite: [i4562] p. 11, Column (c), percentage of business/investment use (2025; sha256 5c1c95b7)

## (helper) — `asset.pct_c`

- **Authored helper label:** The business use percentage, as cents
- **Encoded (NonNegDollars):** Multiply helper "One cent" by the number on helper "Business/investment use percentage (whole percent)".
- Expr: `{"amount":"asset.cent","count":"asset.pct","op":"multiply_count"}`
- Cite: [i4562] p. 11, Column (c) (2025; sha256 5c1c95b7)

## (gate) — `asset.pct_bad`

- **Authored helper label:** The business use percentage is more than 100
- **Encoded (Bool):** helper "Business/investment use percentage (whole percent)" > 100 (a count)
- Expr: `{"gt":["asset.pct",{"const":100,"type":"Count"}],"op":"test"}`
- Cite: [i4562] p. 11, Column (c) (2025; sha256 5c1c95b7)

## (helper) — `asset.listed`

- **Authored helper label:** Is this listed property?
- **Encoded (Bool):** Input — Is this listed property: property used for entertainment or recreation (such as photographic, phonographic, communication or video recording equipment) that is not used exclusively in your business or at your regular business establishment, or a computer placed in service before 2018 that is not used exclusively at your regular business establishment?
- Expr: `{"op":"input","source":"Is this listed property: property used for entertainment or recreation (such as photographic, phonographic, communication or video recording equipment) that is not used exclusively in your business or at your regular business establishment, or a computer placed in service before 2018 that is not used exclusively at your regular business establishment?"}`
- Cite: [i4562] p. 2, Listed Property and its Exceptions; p. 13, Part V (2025; sha256 5c1c95b7)

## (helper) — `asset.half`

- **Authored helper label:** Fifty percent, as cents
- **Encoded (NonNegDollars):** Enter $0.50 (sc.fifty_cents).
- Expr: `{"op":"param","ref":"sc.fifty_cents"}`
- Cite: [i4562] p. 14, Lines 26 and 27, "property used more than 50% in a qualified business use" (2025; sha256 5c1c95b7)

## (helper) — `asset.over_half`

- **Authored helper label:** Business use is more than 50%
- **Encoded (Bool):** helper "The business use percentage, as cents" > helper "Fifty percent, as cents"
- Expr: `{"gt":["asset.pct_c","asset.half"],"op":"test"}`
- Cite: [i4562] p. 14, Lines 26 and 27; p. 3, Part I, "used predominantly (more than 50%) in your trade or business" (2025; sha256 5c1c95b7)

## (gate) — `asset.listed_low`

- **Authored helper label:** Listed property used 50% or less for business, or a percentage over 100
- **Encoded (Bool):** (helper "The business use percentage is more than 100" = true or helper "Is this listed property?" = true and helper "Business use is more than 50%" = false)
- Expr: `{"any":[{"eq":["asset.pct_bad",{"const":true}],"op":"test"},{"all":[{"eq":["asset.listed",{"const":true}],"op":"test"},{"eq":["asset.over_half",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i4562] p. 14, Lines 26 and 27, line 27 (ADS) and Listed property recapture (2025; sha256 5c1c95b7)

## (c) — `asset.basis`

- **Authored helper label:** Basis for depreciation (business/investment use only), before section 179 and the special allowance
- **Encoded (NonNegDollars):** Divide helper "The business use percentage, as cents" by helper "One hundred cents (100%)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cost or other basis" by the result.
- **Refusal:** when asset.listed_low is true, cannot complete Listed property used 50% or less in a qualified business use (Form 4562 line 27), or a business use over 100%. Listed property used 50% or less for business is depreciated under ADS and is outside this tool. Cite: [i4562] p. 14, Lines 26 and 27; p. 15, Column (f), "used 50% or less ... straight line method over its ADS recovery period" (2025; sha256 5c1c95b7)
- Expr: `{"amount":"asset.cost","op":"prorate","part":"asset.pct_c","places":6,"whole":"asset.hundred"}`
- Cite: [i4562] p. 11, Column (c)—Basis for depreciation (2025; sha256 5c1c95b7)

## (helper) — `asset.is2025`

- **Authored helper label:** Placed in service in 2025
- **Encoded (Bool):** column (b) = 'y2025'
- Expr: `{"eq":["asset.placed",{"const":"y2025"}],"op":"test"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j, "Use lines 19a through 19j only for assets placed in service during the tax year beginning in 2025"; Line 17 (2025; sha256 5c1c95b7)

## (helper) — `asset.year`

- **Authored helper label:** Year of recovery in 2025
- **Encoded (Count):** Find the entry in Year of recovery in 2025, by year placed in service for placed column (b).
- Expr: `{"keys":["asset.placed"],"op":"keyed_lookup","table":"recovery_year"}`
- Cite: [p946] p. 37, Using the MACRS Percentage Tables (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.last`

- **Authored helper label:** Last year of recovery for the recovery period
- **Encoded (Count):** Find the entry in Last year of recovery of each GDS recovery period (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period column (d).
- Expr: `{"keys":["asset.period"],"op":"keyed_lookup","table":"macrs_last_year"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5 and A-8 to A-12 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.done`

- **Authored helper label:** The recovery period ended before 2025
- **Encoded (Bool):** helper "Year of recovery in 2025" > helper "Last year of recovery for the recovery period"
- Expr: `{"gt":["asset.year","asset.last"],"op":"test"}`
- Cite: [p946] p. 37, Using the MACRS Percentage Tables (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.quarter`

- **Authored helper label:** Quarter of 2025 in which the property was placed in service
- **Encoded (Enum(quarter)):** Input — The quarter of 2025 in which you placed this property in service: January to March, April to June, July to September, or October to December
- Expr: `{"op":"input","source":"The quarter of 2025 in which you placed this property in service: January to March, April to June, July to September, or October to December"}`
- Cite: [p946] p. 41, Using the Applicable Convention, Mid-quarter convention, "A calendar year is divided into the following quarters" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.qconv`

- **Authored helper label:** Mid-quarter convention for that quarter
- **Encoded (Enum(macrs_convention)):** Find the entry in Mid-quarter convention by quarter placed in service for quarter helper "Quarter of 2025 in which the property was placed in service".
- Expr: `{"keys":["asset.quarter"],"op":"keyed_lookup","table":"quarter_convention"}`
- Cite: [i4562] p. 11, Column (e)—Convention, Mid-quarter convention (2025; sha256 5c1c95b7)

## 6(c) — `asset.s179`

- **IRS:** Section 179 elected cost
- **Encoded (NonNegDollars):** Input — The amount of this property's cost you elect to expense under section 179 (zero if none; not more than its business cost)
- Expr: `{"op":"input","source":"The amount of this property's cost you elect to expense under section 179 (zero if none; not more than its business cost)"}`
- Cite: [i4562] p. 5, Line 6, Column (c)—Elected cost (2025; sha256 5c1c95b7)

## (gate) — `asset.s179_bad`

- **Authored helper label:** The section 179 election is more than the business cost, or the property is not used more than 50% in the business
- **Encoded (Bool):** line 6(c) > helper "Zero" and (line 6(c) > column (c) or helper "Business use is more than 50%" = false)
- Expr: `{"all":[{"gt":["asset.s179","asset.zero"],"op":"test"},{"any":[{"gt":["asset.s179","asset.basis"],"op":"test"},{"eq":["asset.over_half",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i4562] p. 3, Part I, "placed in service during the tax year and used predominantly (more than 50%) in your trade or business"; p. 5, Line 6, Column (c) (2025; sha256 5c1c95b7)

## (helper) — `asset.after179`

- **Authored helper label:** Basis less the section 179 election
- **Encoded (NonNegDollars):** Subtract line 6(c) from column (c). If zero or less, enter -0-.
- **Refusal:** when asset.s179_bad is true, cannot complete Section 179 election above the business cost, or on property used 50% or less in the business. A section 179 election must not exceed the business cost and needs more than 50% business use. Cite: [i4562] p. 3, Part I; p. 5, Line 6, Column (c) (2025; sha256 5c1c95b7)
- Expr: `{"from":"asset.basis","op":"subtract_floor0","take":"asset.s179"}`
- Cite: [i4562] p. 6, How to figure the allowance, "subtract from the business/investment portion of the cost or other basis of the property any credits and deductions allocable to the property ... Section 179 expense deduction" (2025; sha256 5c1c95b7)

## (helper) — `asset.after_jan19`

- **Authored helper label:** Acquired after January 19, 2025
- **Encoded (Bool):** Input — Did you acquire this property after January 19, 2025?
- Expr: `{"op":"input","source":"Did you acquire this property after January 19, 2025?"}`
- Cite: [i4562] p. 5, Line 14, Certain qualified property acquired after January 19, 2025, and Certain qualified property acquired after September 27, 2017, and before January 20, 2025 (2025; sha256 5c1c95b7)

## (helper) — `asset.bonus_choice`

- **Authored helper label:** Special depreciation allowance for this class of property
- **Encoded (Enum(bonus_choice)):** Input — For the class of property this belongs to (its recovery period), did you claim the special depreciation allowance (full), elect the 40% allowance instead of 100% for property acquired after January 19, 2025 (forty), or elect not to claim any special allowance (none)?
- Expr: `{"op":"input","source":"For the class of property this belongs to (its recovery period), did you claim the special depreciation allowance (full), elect the 40% allowance instead of 100% for property acquired after January 19, 2025 (forty), or elect not to claim any special allowance (none)?"}`
- Cite: [i4562] p. 5, Line 14, "you can elect to take a 40% special depreciation allowance"; p. 7, Election out, "for any class of property" (2025; sha256 5c1c95b7)

## (screen) — `asset.bonus_same`

- **Authored helper label:** Is the choice the same for all property of this class placed in service in 2025?
- **Encoded (Bool):** Input — Is that choice the same for all property in the same recovery period class that you (and your spouse, on a joint return) placed in service in 2025?
- Expr: `{"op":"input","source":"Is that choice the same for all property in the same recovery period class that you (and your spouse, on a joint return) placed in service in 2025?"}`
- Cite: [i4562] p. 7, Election out, "for any class of property, to not deduct any special depreciation allowance for all such property in such class placed in service during the tax year" (2025; sha256 5c1c95b7)

## (gate) — `asset.bonus_mixed`

- **Authored helper label:** The special allowance choice differs within a class
- **Encoded (Bool):** column (screen) (asset.bonus_same) = false
- Expr: `{"eq":["asset.bonus_same",{"const":false}],"op":"test"}`
- Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)

## (helper) — `asset.rate40`

- **Authored helper label:** 40% special allowance
- **Encoded (Rate):** Enter 40% (0.40) (sc.bonus_rate_40).
- Expr: `{"op":"param","ref":"sc.bonus_rate_40"}`
- Cite: [i4562] p. 5, Line 14, "is limited to a special depreciation allowance of 40% of the depreciable basis" (2025; sha256 5c1c95b7)

## (helper) — `asset.bonus_full`

- **Authored helper label:** 100% special allowance
- **Encoded (NonNegDollars):** Enter the amount from helper "Basis less the section 179 election".
- **Refusal:** when asset.bonus_mixed is true, cannot complete Different special allowance elections within one class of property. An election that is not the same for the whole class is outside this tool. Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)
- Expr: `{"from":"asset.after179","op":"copy"}`
- Cite: [i4562] p. 5, Line 14, Certain qualified property acquired after January 19, 2025, "is eligible for a 100% special depreciation allowance" (2025; sha256 5c1c95b7)

## (helper) — `asset.bonus_forty`

- **Authored helper label:** 40% special allowance
- **Encoded (NonNegDollars):** Multiply helper "Basis less the section 179 election" by helper "40% special allowance".
- **Refusal:** when asset.bonus_mixed is true, cannot complete Different special allowance elections within one class of property. An election that is not the same for the whole class is outside this tool. Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)
- Expr: `{"amount":"asset.after179","op":"multiply_rate","rate":"asset.rate40"}`
- Cite: [i4562] p. 6, How to figure the allowance, "multiplying the depreciable basis of the property by the applicable percentage" (2025; sha256 5c1c95b7)

## (helper) — `asset.bonus_fullcase`

- **Authored helper label:** The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%
- **Encoded (NonNegDollars):** Choose — [helper "Acquired after January 19, 2025" = true → helper "100% special allowance"] [helper "Acquired after January 19, 2025" = false → helper "40% special allowance"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.after_jan19",{"const":true}],"op":"test"},"then":"asset.bonus_full"},{"guard":{"eq":["asset.after_jan19",{"const":false}],"op":"test"},"then":"asset.bonus_forty"}],"op":"choose"}`
- Cite: [i4562] p. 5, Line 14, Certain qualified property acquired after January 19, 2025, and Certain qualified property acquired after September 27, 2017, and before January 20, 2025 (2025; sha256 5c1c95b7)

## 14 — `asset.bonus`

- **IRS:** Special depreciation allowance for this property
- **Encoded (NonNegDollars):** Choose — [helper "Special depreciation allowance for this class of property" = 'full' → helper "The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%"] [helper "Special depreciation allowance for this class of property" = 'forty' → helper "40% special allowance"] [helper "Special depreciation allowance for this class of property" = 'none' → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.bonus_choice",{"const":"full"}],"op":"test"},"then":"asset.bonus_fullcase"},{"guard":{"eq":["asset.bonus_choice",{"const":"forty"}],"op":"test"},"then":"asset.bonus_forty"},{"guard":{"eq":["asset.bonus_choice",{"const":"none"}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] pp. 5-7, Line 14, Qualified property and Election out (2025; sha256 5c1c95b7)

## (helper) — `asset.ub`

- **Authored helper label:** Basis for MACRS depreciation (after section 179 and the special allowance)
- **Encoded (NonNegDollars):** Subtract line 14 from helper "Basis less the section 179 election". If zero or less, enter -0-.
- Expr: `{"from":"asset.after179","op":"subtract_floor0","take":"asset.bonus"}`
- Cite: [i4562] p. 11, Column (c), "From that result, subtract ... Section 179 expense deduction ... Any special depreciation allowance included on line 14" (2025; sha256 5c1c95b7)

## (helper) — `asset.hy`

- **Authored helper label:** Half-year convention
- **Encoded (Enum(macrs_convention)):** Enter 0 $NaN.NaN; 1 $NaN.NaN (sc.conv_hy).
- Expr: `{"op":"param","ref":"sc.conv_hy"}`
- Cite: [i4562] p. 11, Column (e)—Convention, Half-year convention (2025; sha256 5c1c95b7)

## (helper) — `asset.rate_hy`

- **Authored helper label:** MACRS rate, half-year convention
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period column (d) and convention helper "Half-year convention" and year helper "Year of recovery in 2025".
- Expr: `{"keys":["asset.period","asset.hy","asset.year"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [i4562] p. 12, Column (g), "Multiply column (c) by the applicable rate from the appropriate table"; Pub. 946 Tables A-1 and A-8 (2025; sha256 5c1c95b7)

## (helper) — `asset.rate_mq`

- **Authored helper label:** MACRS rate, mid-quarter convention
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period column (d) and convention helper "Mid-quarter convention for that quarter" and year helper "Year of recovery in 2025".
- Expr: `{"keys":["asset.period","asset.qconv","asset.year"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [i4562] p. 12, Column (g); Pub. 946 Tables A-2 to A-5 and A-9 to A-12 (2025; sha256 5c1c95b7)

## (helper) — `asset.macrs_hy`

- **Authored helper label:** MACRS depreciation, half-year convention
- **Encoded (NonNegDollars):** Multiply helper "Basis for MACRS depreciation (after section 179 and the special allowance)" by helper "MACRS rate, half-year convention".
- Expr: `{"amount":"asset.ub","op":"multiply_rate","rate":"asset.rate_hy"}`
- Cite: [i4562] p. 12, Column (g) (2025; sha256 5c1c95b7)

## (helper) — `asset.macrs_mq`

- **Authored helper label:** MACRS depreciation, mid-quarter convention
- **Encoded (NonNegDollars):** Multiply helper "Basis for MACRS depreciation (after section 179 and the special allowance)" by helper "MACRS rate, mid-quarter convention".
- Expr: `{"amount":"asset.ub","op":"multiply_rate","rate":"asset.rate_mq"}`
- Cite: [i4562] p. 12, Column (g) (2025; sha256 5c1c95b7)

## 19(g) — `asset.macrs2025`

- **IRS:** MACRS depreciation for 2025 property
- **Encoded (NonNegDollars):** Choose — [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = false → helper "MACRS depreciation, half-year convention"] [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = true → helper "MACRS depreciation, mid-quarter convention"]
- Expr: `{"alternatives":[{"guard":{"eq":["mq.applies",{"const":false}],"op":"test"},"then":"asset.macrs_hy"},{"guard":{"eq":["mq.applies",{"const":true}],"op":"test"},"then":"asset.macrs_mq"}],"op":"choose"}`
- Cite: [i4562] p. 11, Column (e), "Half-year convention. This convention applies to all property reported on lines 19a through 19h, unless the mid-quarter convention applies" (2025; sha256 5c1c95b7)

## (helper) — `asset.mqbase`

- **Authored helper label:** Depreciable basis for the mid-quarter test (after section 179, before the special allowance)
- **Encoded (NonNegDollars):** Enter the amount from helper "Basis less the section 179 election".
- Expr: `{"from":"asset.after179","op":"copy"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention, Caution, "reflects the reduction in basis for amounts expensed under section 179 and the part of the basis of property attributable to personal use. However, it does not reflect any reduction in basis for any special depreciation allowance" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.mq_q4_2025`

- **Authored helper label:** That basis when placed in service October to December
- **Encoded (NonNegDollars):** Choose — [helper "Quarter of 2025 in which the property was placed in service" = 'q1' → helper "Zero"] [helper "Quarter of 2025 in which the property was placed in service" = 'q2' → helper "Zero"] [helper "Quarter of 2025 in which the property was placed in service" = 'q3' → helper "Zero"] [helper "Quarter of 2025 in which the property was placed in service" = 'q4' → helper "Depreciable basis for the mid-quarter test (after section 179, before the special allowance)"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.quarter",{"const":"q1"}],"op":"test"},"then":"asset.zero"},{"guard":{"eq":["asset.quarter",{"const":"q2"}],"op":"test"},"then":"asset.zero"},{"guard":{"eq":["asset.quarter",{"const":"q3"}],"op":"test"},"then":"asset.zero"},{"guard":{"eq":["asset.quarter",{"const":"q4"}],"op":"test"},"then":"asset.mqbase"}],"op":"choose"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention, "placed in service during the last 3 months of the tax year" (For use in preparing 2025 returns; sha256 07fadfb2)

## (e) — `asset.prior_conv`

- **Authored helper label:** Convention used in the year placed in service
- **Encoded (Enum(macrs_convention)):** Input — The convention used for this property in the year you placed it in service: half-year, or mid-quarter with the quarter placed in service
- Expr: `{"op":"input","source":"The convention used for this property in the year you placed it in service: half-year, or mid-quarter with the quarter placed in service"}`
- Cite: [i4562] p. 11, Column (e)—Convention; Line 17, "see the instructions for line 19, column (g)" (2025; sha256 5c1c95b7)

## (helper) — `asset.prior_179`

- **Authored helper label:** Section 179 deduction elected for this property in the year placed in service
- **Encoded (NonNegDollars):** Input — The section 179 amount you elected for this property in the year you placed it in service (zero if none)
- Expr: `{"op":"input","source":"The section 179 amount you elected for this property in the year you placed it in service (zero if none)"}`
- Cite: [p946] p. 37, Figuring the Unadjusted Basis of Your Property, "you do reduce your original basis by ... Any section 179 deduction claimed" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.prior_bonus`

- **Authored helper label:** Special depreciation allowance claimed for this property
- **Encoded (NonNegDollars):** Input — The special depreciation allowance claimed for this property in the year you placed it in service (zero if none)
- Expr: `{"op":"input","source":"The special depreciation allowance claimed for this property in the year you placed it in service (zero if none)"}`
- Cite: [p946] p. 37, Figuring the Unadjusted Basis of Your Property, "Any special depreciation allowance taken on the property" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.ub_prior_a`

- **Authored helper label:** Business basis less the section 179 deduction
- **Encoded (NonNegDollars):** Subtract helper "Section 179 deduction elected for this property in the year placed in service" from column (c). If zero or less, enter -0-.
- Expr: `{"from":"asset.basis","op":"subtract_floor0","take":"asset.prior_179"}`
- Cite: [p946] p. 37, Figuring the Unadjusted Basis of Your Property (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.ub_prior`

- **Authored helper label:** Unadjusted basis
- **Encoded (NonNegDollars):** Subtract helper "Special depreciation allowance claimed for this property" from helper "Business basis less the section 179 deduction". If zero or less, enter -0-.
- Expr: `{"from":"asset.ub_prior_a","op":"subtract_floor0","take":"asset.prior_bonus"}`
- Cite: [p946] p. 37, Figuring the Unadjusted Basis of Your Property, "You must apply the table rates to your property's unadjusted basis each year of the recovery period" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.rate_prior`

- **Authored helper label:** MACRS rate for the 2025 year of recovery
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period column (d) and convention column (e) and year helper "Year of recovery in 2025".
- Expr: `{"keys":["asset.period","asset.prior_conv","asset.year"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5 and A-8 to A-12 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `asset.macrs_prior_live`

- **Authored helper label:** MACRS depreciation for 2025
- **Encoded (NonNegDollars):** Multiply helper "Unadjusted basis" by helper "MACRS rate for the 2025 year of recovery".
- Expr: `{"amount":"asset.ub_prior","op":"multiply_rate","rate":"asset.rate_prior"}`
- Cite: [i4562] p. 9, Line 17, "enter the deductions for the current year" (2025; sha256 5c1c95b7)

## 17 — `asset.macrs_prior`

- **IRS:** MACRS deduction for 2025 on property placed in service before 2025
- **Encoded (NonNegDollars):** Choose — [helper "The recovery period ended before 2025" = false → helper "MACRS depreciation for 2025"] [helper "The recovery period ended before 2025" = true → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.done",{"const":false}],"op":"test"},"then":"asset.macrs_prior_live"},{"guard":{"eq":["asset.done",{"const":true}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Line 17; i4562 p. 8, "Prior years' depreciation, plus current year's depreciation, can never exceed the depreciable basis" (2025; sha256 5c1c95b7)

## (helper) — `asset.dep_2025`

- **Authored helper label:** MACRS on 2025 property
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → line 19(g)] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.macrs2025"},{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j and Line 17; p. 4, Line 2 (2025; sha256 5c1c95b7)

## (helper) — `asset.bonus_2025`

- **Authored helper label:** Special allowance on 2025 property
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → line 14] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.bonus"},{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j and Line 17; p. 4, Line 2 (2025; sha256 5c1c95b7)

## (helper) — `asset.s179_2025`

- **Authored helper label:** Section 179 elected on 2025 property
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → line 6(c)] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.s179"},{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j and Line 17; p. 4, Line 2 (2025; sha256 5c1c95b7)

## (helper) — `asset.mq_q4`

- **Authored helper label:** Mid-quarter test basis, fourth quarter
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "That basis when placed in service October to December"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.mq_q4_2025"},{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j and Line 17; p. 4, Line 2 (2025; sha256 5c1c95b7)

## (helper) — `asset.mq_total`

- **Authored helper label:** Mid-quarter test basis, all of 2025
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "Depreciable basis for the mid-quarter test (after section 179, before the special allowance)"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.mqbase"},{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j and Line 17; p. 4, Line 2 (2025; sha256 5c1c95b7)

## (helper) — `asset.cost179`

- **Authored helper label:** Cost of section 179 property placed in service in 2025
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "The business cost when used more than 50% in the business"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.cost179_2025"},{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j and Line 17; p. 4, Line 2 (2025; sha256 5c1c95b7)

## (helper) — `asset.cost179_2025`

- **Authored helper label:** The business cost when used more than 50% in the business
- **Encoded (NonNegDollars):** Choose — [helper "Business use is more than 50%" = true → column (c)] [helper "Business use is more than 50%" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.over_half",{"const":true}],"op":"test"},"then":"asset.basis"},{"guard":{"eq":["asset.over_half",{"const":false}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 4, Line 2, "Enter the total cost of all section 179 property you placed in service during the tax year"; Worksheet 1, line 1, "include the total amount of eligible section 179 property ... not just the amount for which you are making the election" (2025; sha256 5c1c95b7)

## (helper) — `asset.dep_prior`

- **Authored helper label:** MACRS on property placed in service before 2025
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = false → line 17] [helper "Placed in service in 2025" = true → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["asset.is2025",{"const":false}],"op":"test"},"then":"asset.macrs_prior"},{"guard":{"eq":["asset.is2025",{"const":true}],"op":"test"},"then":"asset.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Line 17 (2025; sha256 5c1c95b7)

## 26(h) — `asset.dep_listed`

- **IRS:** Depreciation of this listed property (column (h))
- **Encoded (NonNegDollars):** Add helper "MACRS on 2025 property" and helper "MACRS on property placed in service before 2025".
- Expr: `{"of":["asset.dep_2025","asset.dep_prior"],"op":"sum"}`
- Cite: [i4562] p. 15, Column (h)—Depreciation deduction, "For property used more than 50% in a qualified business use (line 26) ... figure column (h) by following the instructions for line 19, column (g)" (2025; sha256 5c1c95b7)
