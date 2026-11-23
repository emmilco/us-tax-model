# Form 4562 — one building or improvement of a rental property

- Document: `rprop` (form, tax year 2025)
- Collection: keyed entries within rental; [p946] p. 3, Additions and Improvements (For use in preparing 2025 returns; sha256 07fadfb2)
- Note: One entry per building, or improvement to one, of a rental property; depreciated by Table A-6 (residential rental property, 27.5 years) or Table A-7a (nonresidential real property, 39 years), mid-month convention, straight line. Refused: personal property and land improvements, ADS and other methods, basis changes, dispositions, qualified improvement property, basis reduced by a credit or deduction, cooperative stock, farm buildings and motor fuels outlets (10-, 15- and 20-year property), property not bought or built (exchanges, involuntary conversions, gifts, inheritances, spouse transfers, pay for services), and nonresidential real property placed in service before 1994.

## (helper) — `rprop.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i4562] p. 12, Column (g)—Depreciation deduction (2025; sha256 5c1c95b7)

## (a) — `rprop.kind`

- **Authored helper label:** Kind of property
- **Encoded (Enum(rprop_kind)):** Input — What is this?

  - residential: a building (or an improvement to one) whose rent comes mostly (80% or more) from homes
  - nonresidential: any other building, such as shops or offices, or an improvement to one
  - personal: something other than a building or part of one, such as an appliance, carpet, furniture, a fence or a driveway
- Expr: `{"op":"input","source":"What is this?\n\n- residential: a building (or an improvement to one) whose rent comes mostly (80% or more) from homes\n- nonresidential: any other building, such as shops or offices, or an improvement to one\n- personal: something other than a building or part of one, such as an appliance, carpet, furniture, a fence or a driveway"}`
- Cite: [i4562] p. 10, Residential rental property (2025; sha256 5c1c95b7)

## (screen) — `rprop.short_class`

- **Authored helper label:** A farm building, single purpose agricultural or horticultural structure, or retail motor fuels outlet (10-, 15- or 20-year property), or an improvement to one
- **Encoded (Bool):** Input — Is it a farm building (such as a barn, a silo or a greenhouse), or a building where gasoline or other motor fuel is sold (such as a gas station or a store with fuel pumps), or an improvement to one?
- Expr: `{"op":"input","source":"Is it a farm building (such as a barn, a silo or a greenhouse), or a building where gasoline or other motor fuel is sold (such as a gas station or a store with fuel pumps), or an improvement to one?"}`
- Cite: [i4562] p. 10, "Any section 1250 property that is a retail motor fuels outlet"; "Farm buildings (other than single purpose agricultural or horticultural structures)"; "Any single purpose agricultural or horticultural structure"; "Nonresidential real property is any real property that is neither residential rental property nor property with a class life of less than 27.5 years"; p946 p. 31, Retail motor fuels outlet, "used to a substantial extent in the retail marketing of petroleum or petroleum products" (2025; sha256 5c1c95b7)

## (gate) — `rprop.short_class_if_nonres`

- **Authored helper label:** Farm building or motor fuels outlet, asked only of nonresidential real property (false otherwise)
- **Encoded (Bool):** Choose — [column (a) = 'nonresidential' → helper "A farm building, single purpose agricultural or horticultural structure, or retail motor fuels outlet (10-, 15- or 20-year property), or an improvement to one"] [column (a) = 'residential' → helper "Year parameter household.no (false)"] [column (a) = 'personal' → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rprop.kind",{"const":"nonresidential"}],"op":"test"},"then":"rprop.short_class"},{"guard":{"eq":["rprop.kind",{"const":"residential"}],"op":"test"},"then":"rprop.no"},{"guard":{"eq":["rprop.kind",{"const":"personal"}],"op":"test"},"then":"rprop.no"}],"op":"choose"}`
- Cite: [i4562] p. 10, "Any section 1250 property that is a retail motor fuels outlet"; "Farm buildings (other than single purpose agricultural or horticultural structures)"; "Any single purpose agricultural or horticultural structure"; "Nonresidential real property is any real property that is neither residential rental property nor property with a class life of less than 27.5 years"; p946 p. 31, Retail motor fuels outlet, "used to a substantial extent in the retail marketing of petroleum or petroleum products" (2025; sha256 5c1c95b7)

## (b) — `rprop.month`

- **Authored helper label:** Month placed in service
- **Encoded (Enum(month)):** Input — The month it was first ready and available for rent (placed in service) by you
- Expr: `{"op":"input","source":"The month it was first ready and available for rent (placed in service) by you"}`
- Cite: [p946] p. 73, Table A-6, "Month property placed in service" (For use in preparing 2025 returns; sha256 07fadfb2)

## (b) — `rprop.year`

- **Authored helper label:** Year placed in service
- **Encoded (Enum(realty_year)):** Input — The year it was first ready and available for rent (placed in service) by you; before1987 if earlier than 1987
- Expr: `{"op":"input","source":"The year it was first ready and available for rent (placed in service) by you; before1987 if earlier than 1987"}`
- Cite: [p946] p. 37, Using the MACRS Percentage Tables (For use in preparing 2025 returns; sha256 07fadfb2)

## (c) — `rprop.basis`

- **Authored helper label:** Basis for depreciation
- **Encoded (NonNegDollars):** Input — Its basis for depreciation: what you paid for the building or improvement, not the land (for a home you lived in before renting it, the smaller of its value and your adjusted basis when you began renting it); your share
- Expr: `{"op":"input","source":"Its basis for depreciation: what you paid for the building or improvement, not the land (for a home you lived in before renting it, the smaller of its value and your adjusted basis when you began renting it); your share"}`
- Cite: [i1040se] p. 6, Line 18 (2025; sha256 ad71de35)

## (helper) — `rprop.no`

- **Authored helper label:** Year parameter household.no (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [p946] p. 16, Qualified improvement property (For use in preparing 2025 returns; sha256 07fadfb2)

## (gate) — `rprop.new_nonres`

- **Authored helper label:** Nonresidential real property placed in service after 2017, which may be qualified improvement property
- **Encoded (Bool):** column (a) = 'nonresidential' and helper "Year of recovery in 2025" ≤ 8 (a count)
- Expr: `{"all":[{"eq":["rprop.kind",{"const":"nonresidential"}],"op":"test"},{"le":["rprop.recovery_year",{"const":8,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [p946] p. 31, Qualified improvement property, "placed in service by you after 2017 and after the date the building was first placed in service by any person" (For use in preparing 2025 returns; sha256 07fadfb2)

## (screen) — `rprop.qip`

- **Authored helper label:** Qualified improvement property (an improvement to an interior portion of a building that is nonresidential real property, placed in service after the building was first placed in service; not an enlargement, an elevator or escalator, or the internal structural framework)
- **Encoded (Bool):** Input — Is any part of it an improvement to the inside of the building, made after the building was first placed in service by anyone, other than an enlargement, an elevator or escalator, or the internal structural framework?
- Expr: `{"op":"input","source":"Is any part of it an improvement to the inside of the building, made after the building was first placed in service by anyone, other than an enlargement, an elevator or escalator, or the internal structural framework?"}`
- Cite: [p946] p. 16, Qualified improvement property; p. 31, Qualified improvement property (For use in preparing 2025 returns; sha256 07fadfb2)

## (gate) — `rprop.qip_if_new_nonres`

- **Authored helper label:** Qualified improvement property, asked only of nonresidential real property placed in service after 2017 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Nonresidential real property placed in service after 2017, which may be qualified improvement property" = true → helper "Qualified improvement property (an improvement to an interior portion of a building that is nonresidential real property, placed in service after the building was first placed in service; not an enlargement, an elevator or escalator, or the internal structural framework)"] [helper "Nonresidential real property placed in service after 2017, which may be qualified improvement property" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rprop.new_nonres",{"const":true}],"op":"test"},"then":"rprop.qip"},{"guard":{"eq":["rprop.new_nonres",{"const":false}],"op":"test"},"then":"rprop.no"}],"op":"choose"}`
- Cite: [i4562] p. 10, 15-year property, "Qualified improvement property, as defined in section 168(e)(6), placed in service by you after December 31, 2017" (2025; sha256 5c1c95b7)

## (screen) — `rprop.disposed`

- **Authored helper label:** Retired from service in 2025 (sold or exchanged, converted to personal use, abandoned or destroyed)
- **Encoded (Bool):** Input — In 2025, was it sold, traded, given away, destroyed or torn out, or did you stop renting it for good?
- Expr: `{"op":"input","source":"In 2025, was it sold, traded, given away, destroyed or torn out, or did you stop renting it for good?"}`
- Cite: [p527] p. 9, Retired From Service; p946 p. 40, "If you dispose of property before the end of its recovery period" (2025; sha256 20c826e9)

## (screen) — `rprop.fast`

- **Authored helper label:** A special depreciation allowance or section 179 deduction claimed, or depreciated by a method other than straight line over 27.5 or 39 years
- **Encoded (Bool):** Input — Did you deduct any cost in one year (bonus depreciation or section 179), or depreciate it other than straight line over 27.5 or 39 years?
- Expr: `{"op":"input","source":"Did you deduct any cost in one year (bonus depreciation or section 179), or depreciate it other than straight line over 27.5 or 39 years?"}`
- Cite: [p527] p. 12, Decreases to basis, "Special depreciation allowance or a section 179 deduction claimed on qualified property"; i4562 p. 11, Column (f)—Method (2025; sha256 20c826e9)

## (screen) — `rprop.ads`

- **Authored helper label:** Depreciated under the alternative depreciation system (ADS), elected or required
- **Encoded (Bool):** Input — Do you depreciate it over 30 or 40 years (the alternative depreciation system, ADS), by choice or because you must?
- Expr: `{"op":"input","source":"Do you depreciate it over 30 or 40 years (the alternative depreciation system, ADS), by choice or because you must?"}`
- Cite: [p527] p. 12, Depreciation Systems, "You must use GDS unless you are specifically required by law to use ADS or you elect to use ADS"; i4562 p. 13, Line 20c, Residential rental property (2025; sha256 20c826e9)

## (screen) — `rprop.basis_changed`

- **Authored helper label:** Basis adjusted after it was placed in service for anything other than depreciation or an improvement depreciated as a separate item (for example a casualty loss or an easement)
- **Encoded (Bool):** Input — Since renting began, has anything but depreciation changed its cost for tax purposes, like a casualty loss or easement payment?
- Expr: `{"op":"input","source":"Since renting began, has anything but depreciation changed its cost for tax purposes, like a casualty loss or easement payment?"}`
- Cite: [p946] p. 37, Rules Covering the Use of the Tables, rule 4; p527 p. 12, Decreases to basis (For use in preparing 2025 returns; sha256 07fadfb2)

## (screen) — `rprop.credit`

- **Authored helper label:** Basis reduced by a credit or deduction (for example the disabled access credit, the deduction for removal of barriers to the disabled and the elderly, or the section 179D deduction)
- **Encoded (Bool):** Input — Did you take a credit or special deduction for part of its cost, like for disabled access or barrier removal?
- Expr: `{"op":"input","source":"Did you take a credit or special deduction for part of its cost, like for disabled access or barrier removal?"}`
- Cite: [i4562] p. 11, Column (c)—Basis for depreciation, "The following are examples of some credits and deductions that reduce the basis for depreciation" (2025; sha256 5c1c95b7)

## (screen) — `rprop.coop`

- **Authored helper label:** Stock in a cooperative housing corporation
- **Encoded (Bool):** Input — Is it stock in a cooperative housing corporation (a co-op apartment you rent out)?
- Expr: `{"op":"input","source":"Is it stock in a cooperative housing corporation (a co-op apartment you rent out)?"}`
- Cite: [p527] p. 8, Cooperative apartments (2025; sha256 20c826e9)

## (screen) — `rprop.exchanged`

- **Authored helper label:** Acquired other than by purchase or construction (like-kind exchange, involuntary conversion, gift, inheritance, transfer from a spouse or former spouse, or for services)
- **Encoded (Bool):** Input — Did you get it other than by buying or building it, such as in a trade for other property (a like-kind exchange), to replace property destroyed, stolen or taken by a government (an involuntary conversion), as a gift or an inheritance, from your spouse or former spouse, or as pay for work?
- Expr: `{"op":"input","source":"Did you get it other than by buying or building it, such as in a trade for other property (a like-kind exchange), to replace property destroyed, stolen or taken by a government (an involuntary conversion), as a gift or an inheritance, from your spouse or former spouse, or as pay for work?"}`
- Cite: [i4562] p. 9, "Generally, you must depreciate the carryover basis of property you acquire in a like-kind exchange or involuntary conversion during the current tax year over the remaining recovery period of the property exchanged or involuntarily converted"; p527 p. 11, Basis Other Than Cost, "You can’t use cost as a basis for property that you received" (2025; sha256 5c1c95b7)

## (helper) — `rprop.screen`

- **Authored helper label:** Depreciation of this property outside the tables this tool uses
- **Encoded (Bool):** (helper "Retired from service in 2025 (sold or exchanged, converted to personal use, abandoned or destroyed)" = true or helper "A special depreciation allowance or section 179 deduction claimed, or depreciated by a method other than straight line over 27.5 or 39 years" = true or helper "Depreciated under the alternative depreciation system (ADS), elected or required" = true or helper "Basis adjusted after it was placed in service for anything other than depreciation or an improvement depreciated as a separate item (for example a casualty loss or an easement)" = true or helper "Basis reduced by a credit or deduction (for example the disabled access credit, the deduction for removal of barriers to the disabled and the elderly, or the section 179D deduction)" = true or helper "Stock in a cooperative housing corporation" = true or helper "Acquired other than by purchase or construction (like-kind exchange, involuntary conversion, gift, inheritance, transfer from a spouse or former spouse, or for services)" = true or helper "Qualified improvement property, asked only of nonresidential real property placed in service after 2017 (false otherwise)" = true or helper "Farm building or motor fuels outlet, asked only of nonresidential real property (false otherwise)" = true)
- Expr: `{"any":[{"eq":["rprop.disposed",{"const":true}],"op":"test"},{"eq":["rprop.fast",{"const":true}],"op":"test"},{"eq":["rprop.ads",{"const":true}],"op":"test"},{"eq":["rprop.basis_changed",{"const":true}],"op":"test"},{"eq":["rprop.credit",{"const":true}],"op":"test"},{"eq":["rprop.coop",{"const":true}],"op":"test"},{"eq":["rprop.exchanged",{"const":true}],"op":"test"},{"eq":["rprop.qip_if_new_nonres",{"const":true}],"op":"test"},{"eq":["rprop.short_class_if_nonres",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i4562] p. 11, Column (f)—Method (2025; sha256 5c1c95b7)

## (gate) — `rprop.personal`

- **Authored helper label:** Personal property or a land improvement in a rental
- **Encoded (Bool):** column (a) = 'personal'
- Expr: `{"eq":["rprop.kind",{"const":"personal"}],"op":"test"}`
- Cite: [i4562] p. 9, Lines 19a Through 19j (2025; sha256 5c1c95b7)

## (gate) — `rprop.early_nonres`

- **Authored helper label:** Nonresidential real property placed in service before 1994 (31.5-year)
- **Encoded (Bool):** column (a) = 'nonresidential' and helper "Year of recovery in 2025" > 32 (a count)
- Expr: `{"all":[{"eq":["rprop.kind",{"const":"nonresidential"}],"op":"test"},{"gt":["rprop.recovery_year",{"const":32,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [p946] p. 74, Table A-7, "Straight Line—31.5 Years" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `rprop.recovery_year`

- **Authored helper label:** Year of recovery in 2025
- **Encoded (Count):** Find the entry in Year of recovery in 2025 of real property, by year placed in service for placed column (b) (rprop.year).
- Expr: `{"keys":["rprop.year"],"op":"keyed_lookup","table":"realty_recovery_year"}`
- Cite: [p946] p. 37, Using the MACRS Percentage Tables (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `rprop.rate`

- **Authored helper label:** Rate from Table A-6 or A-7a for the month placed in service and the year of recovery
- **Encoded (Rate):** Find the entry in MACRS mid-month straight-line tables for real property (Pub. 946, Tables A-6 and A-7a) for kind column (a) and month column (b) (rprop.month) and year helper "Year of recovery in 2025".
- Expr: `{"keys":["rprop.kind","rprop.month","rprop.recovery_year"],"op":"keyed_lookup","table":"macrs_mm"}`
- Cite: [p946] p. 73, Table A-6, "Month property placed in service" (For use in preparing 2025 returns; sha256 07fadfb2)

## (g) — `rprop.dep`

- **Authored helper label:** Depreciation deduction
- **Encoded (NonNegDollars):** Multiply column (c) by helper "Rate from Table A-6 or A-7a for the month placed in service and the year of recovery".
- **Refusal:** when rprop.personal is true, cannot complete Form 4562 (personal property or land improvements in a rental). Appliances, carpet, furniture, fences and other property that is not a building are outside this tool. Cite: [i4562] p. 9, Lines 19a Through 19j (2025; sha256 5c1c95b7)
- **Refusal:** when rprop.screen is true, cannot complete Form 4562 (real property outside the mid-month tables). Real property depreciated another way, with a changed basis, disposed of, qualified improvement property, property with a credit or deduction for part of its cost, cooperative stock, a farm building or a motor fuels outlet, or property received other than by purchase or construction (in a like-kind exchange or an involuntary conversion, as a gift or an inheritance, from a spouse or former spouse, or for services) is outside this tool. Cite: [i4562] p. 11, Column (f)—Method (2025; sha256 5c1c95b7)
- **Refusal:** when rprop.early_nonres is true, cannot complete Form 4562 (nonresidential real property placed in service before 1994). Nonresidential real property placed in service before 1994 is outside this tool. Cite: [p946] p. 74, Table A-7, "Straight Line—31.5 Years" (For use in preparing 2025 returns; sha256 07fadfb2)
- Interpretation: amb.2025.rental_prior_depreciation_tables
- Expr: `{"amount":"rprop.basis","op":"multiply_rate","rate":"rprop.rate"}`
- Cite: [i4562] p. 12, Column (g)—Depreciation deduction (2025; sha256 5c1c95b7)

## (gate) — `rprop.placed_this_year`

- **Authored helper label:** Placed in service in 2025
- **Encoded (Bool):** column (b) (rprop.year) = 'y2025'
- Expr: `{"eq":["rprop.year",{"const":"y2025"}],"op":"test"}`
- Cite: [i4562] p. 9, Line 17 (2025; sha256 5c1c95b7)

## (helper) — `rprop.cent`

- **Authored helper label:** One cent (a count carried as cents)
- **Encoded (NonNegDollars):** Enter $0.01 (rental.day_cents).
- Expr: `{"op":"param","ref":"rental.day_cents"}`
- Cite: [i4562] p. 9, Line 17 (2025; sha256 5c1c95b7)

## (helper) — `rprop.placed_this_year_cent`

- **Authored helper label:** One cent if placed in service in 2025, zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "One cent (a count carried as cents)"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rprop.placed_this_year",{"const":true}],"op":"test"},"then":"rprop.cent"},{"guard":{"eq":["rprop.placed_this_year",{"const":false}],"op":"test"},"then":"rprop.zero"}],"op":"choose"}`
- Cite: [i4562] p. 9, Line 17 (2025; sha256 5c1c95b7)
