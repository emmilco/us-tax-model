# Form 4562 — one building or improvement of a rental property

- Document: `rprop` (form, tax year 2025)
- Collection: keyed entries within rental; [p946] p. 3, Additions and Improvements (For use in preparing 2025 returns; sha256 07fadfb2)
- Note: One entry per building, or improvement to one, of a rental property; depreciated by Table A-6 (residential rental property, 27.5 years) or Table A-7a (nonresidential real property, 39 years), mid-month convention, straight line. Refused: personal property and land improvements, ADS and other methods, basis changes, dispositions, qualified improvement property, basis reduced by a credit or deduction, cooperative stock, and nonresidential real property placed in service before 1994.

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

## (helper) — `rprop.screen`

- **Authored helper label:** Depreciation of this property outside the tables this tool uses
- **Encoded (Bool):** Input — Does any of these apply to it?

  - you depreciate it over a longer period (the alternative depreciation system), or chose to
  - its basis changed after you began depreciating it, other than by depreciation (for example, a casualty loss)
  - you sold, gave away or stopped renting it in 2025
  - it is stock in a cooperative housing corporation
  - you deducted any of its cost in one year (a special allowance or section 179) or depreciate it another way
  - it is an improvement to the inside of a nonresidential building, made after the building was first placed in service and placed in service in 2018 or later (not an enlargement, an elevator or escalator, or the internal structural framework)
  - you took a credit or deduction for part of its cost (for example the disabled access credit or the deduction for removing barriers)
- Expr: `{"op":"input","source":"Does any of these apply to it?\n\n- you depreciate it over a longer period (the alternative depreciation system), or chose to\n- its basis changed after you began depreciating it, other than by depreciation (for example, a casualty loss)\n- you sold, gave away or stopped renting it in 2025\n- it is stock in a cooperative housing corporation\n- you deducted any of its cost in one year (a special allowance or section 179) or depreciate it another way\n- it is an improvement to the inside of a nonresidential building, made after the building was first placed in service and placed in service in 2018 or later (not an enlargement, an elevator or escalator, or the internal structural framework)\n- you took a credit or deduction for part of its cost (for example the disabled access credit or the deduction for removing barriers)"}`
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
- **Refusal:** when rprop.screen is true, cannot complete Form 4562 (real property outside the mid-month tables). Real property depreciated another way, with a changed basis, disposed of, qualified improvement property, property with a credit or deduction for part of its cost, or cooperative stock is outside this tool. Cite: [i4562] p. 11, Column (f)—Method (2025; sha256 5c1c95b7)
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
