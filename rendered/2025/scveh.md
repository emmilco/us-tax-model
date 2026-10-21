# Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business

- Document: `scveh` (form, tax year 2025)
- Collection: keyed entries within sc; [i1040sc] p. 6, Line 9; p. 7, Information on your vehicle, "If you used more than one vehicle during the year, attach a statement with the information requested in Schedule C, Part IV, for each additional vehicle" (2025; sha256 b5536db9)
- Note: One entry per car, truck or van used in the business: the standard mileage rate or actual expenses (Schedule C line 9 and, for a lease, line 20a), and for an owned vehicle on actual expenses its depreciation by Pub. 946's Depreciation Worksheet for Passenger Automobiles (Form 4562 Part V): placed in service 2019 to 2025, a 2019 vehicle's first year after its recovery period from its unrecovered basis. Refused: earlier special allowances, earlier standard mileage, business use of 50% or less, dispositions, trade-ins and the other items of the screen.

## (helper) — `scveh.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sc] p. 6, Line 9 (2025; sha256 b5536db9)

## (helper) — `scveh.method`

- **Authored helper label:** Standard mileage rate or actual expenses
- **Encoded (Enum(vehicle_method)):** Input — For this vehicle, do you take the standard mileage rate (standard) or deduct actual expenses (actual)?
- Expr: `{"op":"input","source":"For this vehicle, do you take the standard mileage rate (standard) or deduct actual expenses (actual)?"}`
- Cite: [i1040sc] p. 6, Line 9, "You can deduct the actual expenses of operating your car or truck or take the standard mileage rate" (2025; sha256 b5536db9)

## (helper) — `scveh.owned`

- **Authored helper label:** Owned (not leased)
- **Encoded (Bool):** Input — Do you own this vehicle (answer No if you lease it)?
- Expr: `{"op":"input","source":"Do you own this vehicle (answer No if you lease it)?"}`
- Cite: [i1040sc] p. 6, Line 9, "Owned the vehicle ... or Leased the vehicle" (2025; sha256 b5536db9)

## 43 — `scveh.placed_date`

- **IRS:** When did you place your vehicle in service for business purposes? (month/day/year)
- **Encoded (Count):** Input — The year you first placed this vehicle in service for business purposes (for example 2023)
- Expr: `{"op":"input","source":"The year you first placed this vehicle in service for business purposes (for example 2023)"}`
- Cite: [f1040sc] Schedule C (2025), line 43 (2025; created 2025-04-03; sha256 ddf401db)

## 44a — `scveh.miles_business`

- **IRS:** Business miles
- **Encoded (Count):** Input — The miles you drove this vehicle in 2025 for this business (not commuting)
- Expr: `{"op":"input","source":"The miles you drove this vehicle in 2025 for this business (not commuting)"}`
- Cite: [f1040sc] Schedule C (2025), line 44a; i1040sc p. 15, Line 44b (2025; created 2025-04-03; sha256 ddf401db)

## 44b — `scveh.miles_commuting`

- **IRS:** Commuting miles
- **Encoded (Count):** Input — The commuting miles you drove this vehicle in 2025 (travel between your home and a work location, as defined in the instructions for line 44b)
- Expr: `{"op":"input","source":"The commuting miles you drove this vehicle in 2025 (travel between your home and a work location, as defined in the instructions for line 44b)"}`
- Cite: [i1040sc] p. 15, Line 44b (2025; sha256 b5536db9)

## 44c — `scveh.miles_other`

- **IRS:** Other miles
- **Encoded (Count):** Input — The other (personal) miles you drove this vehicle in 2025
- Expr: `{"op":"input","source":"The other (personal) miles you drove this vehicle in 2025"}`
- Cite: [f1040sc] Schedule C (2025), line 44c (2025; created 2025-04-03; sha256 ddf401db)

## (helper) — `scveh.cent`

- **Authored helper label:** One cent
- **Encoded (NonNegDollars):** Enter $0.01 (sc.one_cent).
- Expr: `{"op":"param","ref":"sc.one_cent"}`
- Cite: [i4562] p. 14, Column (c)—Business/investment use percentage (2025; sha256 5c1c95b7)

## (helper) — `scveh.bm_c`

- **Authored helper label:** Business miles, as cents
- **Encoded (NonNegDollars):** Multiply helper "One cent" by the number on line 44a.
- Expr: `{"amount":"scveh.cent","count":"scveh.miles_business","op":"multiply_count"}`
- Cite: [i4562] p. 14, Column (c), "dividing the number of miles the vehicle is driven for trade or business purposes" (2025; sha256 5c1c95b7)

## (helper) — `scveh.cm_c`

- **Authored helper label:** Commuting miles, as cents
- **Encoded (NonNegDollars):** Multiply helper "One cent" by the number on line 44b.
- Expr: `{"amount":"scveh.cent","count":"scveh.miles_commuting","op":"multiply_count"}`
- Cite: [i4562] p. 14, Column (c), "(not to include any commuting mileage)" (2025; sha256 5c1c95b7)

## (helper) — `scveh.om_c`

- **Authored helper label:** Other miles, as cents
- **Encoded (NonNegDollars):** Multiply helper "One cent" by the number on line 44c.
- Expr: `{"amount":"scveh.cent","count":"scveh.miles_other","op":"multiply_count"}`
- Cite: [i4562] p. 14, Column (c) (2025; sha256 5c1c95b7)

## (helper) — `scveh.nonbusiness_c`

- **Authored helper label:** Commuting and other miles, as cents
- **Encoded (NonNegDollars):** Add helper "Commuting miles, as cents" and helper "Other miles, as cents".
- Expr: `{"of":["scveh.cm_c","scveh.om_c"],"op":"sum"}`
- Cite: [i4562] p. 14, Column (c) (2025; sha256 5c1c95b7)

## (helper) — `scveh.total_c`

- **Authored helper label:** Total miles, as cents
- **Encoded (NonNegDollars):** Add helper "Business miles, as cents" and helper "Commuting and other miles, as cents".
- Expr: `{"of":["scveh.bm_c","scveh.nonbusiness_c"],"op":"sum"}`
- Cite: [i4562] p. 14, Column (c), "by the total number of miles the vehicle is driven for all purposes" (2025; sha256 5c1c95b7)

## (helper) — `scveh.over_half`

- **Authored helper label:** Business use is more than 50%
- **Encoded (Bool):** helper "Business miles, as cents" > helper "Commuting and other miles, as cents"
- Expr: `{"gt":["scveh.bm_c","scveh.nonbusiness_c"],"op":"test"}`
- Cite: [i4562] p. 14, Lines 26 and 27, "property used more than 50% in a qualified business use" (2025; sha256 5c1c95b7)

## (helper) — `scveh.parking`

- **Authored helper label:** Business parking fees and tolls
- **Encoded (NonNegDollars):** Input — Parking fees and tolls for this vehicle's business use in 2025 (zero if none)
- Expr: `{"op":"input","source":"Parking fees and tolls for this vehicle's business use in 2025 (zero if none)"}`
- Cite: [i1040sc] p. 6, Line 9, "Add to this amount your parking fees and tolls" (2025; sha256 b5536db9)

## (screen) — `scveh.smr_ok`

- **Authored helper label:** May you use the standard mileage rate for this vehicle?
- **Encoded (Bool):** Input — If you own this vehicle: did you use the standard mileage rate for it in the first year you used it for business? If you lease it: are you using the standard mileage rate for the entire lease period? (Answer No if this is one of five or more vehicles you used in the business at the same time.)
- Expr: `{"op":"input","source":"If you own this vehicle: did you use the standard mileage rate for it in the first year you used it for business? If you lease it: are you using the standard mileage rate for the entire lease period? (Answer No if this is one of five or more vehicles you used in the business at the same time.)"}`
- Cite: [i1040sc] p. 6, Line 9, "You must use actual expenses if you used five or more vehicles simultaneously" and "You can take the standard mileage rate for 2025 only if you" (2025; sha256 b5536db9)

## (gate) — `scveh.smr_bad`

- **Authored helper label:** The standard mileage rate is not available for this vehicle
- **Encoded (Bool):** column (screen) (scveh.smr_ok) = false
- Expr: `{"eq":["scveh.smr_ok",{"const":false}],"op":"test"}`
- Cite: [i1040sc] p. 6, Line 9 (2025; sha256 b5536db9)

## (helper) — `scveh.rate`

- **Authored helper label:** Standard mileage rate per mile
- **Encoded (NonNegDollars):** Enter $0.70 (sc.mileage_rate).
- Expr: `{"op":"param","ref":"sc.mileage_rate"}`
- Cite: [n-25-05] Section 3, "The standard mileage rate for transportation or travel expenses for 2025 is 70 cents per mile for all miles of business use" (Notice 2025-5; sha256 aac49246)

## (helper) — `scveh.smr_amount`

- **Authored helper label:** Business miles times the standard mileage rate
- **Encoded (NonNegDollars):** Multiply helper "Standard mileage rate per mile" by the number on line 44a.
- **Refusal:** when scveh.smr_bad is true, cannot complete Standard mileage rate not available (not used in the vehicle's first year or for the whole lease, or five or more vehicles at once). Use actual expenses for this vehicle, or this vehicle is outside this tool. Cite: [i1040sc] p. 6, Line 9 (2025; sha256 b5536db9)
- Expr: `{"amount":"scveh.rate","count":"scveh.miles_business","op":"multiply_count"}`
- Cite: [i1040sc] p. 6, Line 9, "Multiply the number of business miles driven by 0.70" (2025; sha256 b5536db9)

## (helper) — `scveh.line9_standard`

- **Authored helper label:** Standard mileage amount plus parking fees and tolls
- **Encoded (NonNegDollars):** Add helper "Business miles times the standard mileage rate" and helper "Business parking fees and tolls".
- Expr: `{"of":["scveh.smr_amount","scveh.parking"],"op":"sum"}`
- Cite: [i1040sc] p. 6, Line 9, "Add to this amount your parking fees and tolls; and Enter the total on line 9" (2025; sha256 b5536db9)

## (helper) — `scveh.operating`

- **Authored helper label:** Actual operating expenses of the vehicle
- **Encoded (NonNegDollars):** Input — The total 2025 operating expenses of this vehicle: gasoline, oil, repairs, insurance, license plates and similar (not depreciation, not lease or rent payments, not interest, not parking and tolls)
- Expr: `{"op":"input","source":"The total 2025 operating expenses of this vehicle: gasoline, oil, repairs, insurance, license plates and similar (not depreciation, not lease or rent payments, not interest, not parking and tolls)"}`
- Cite: [i1040sc] p. 7, Line 9, If you deduct actual expenses, "Include on line 9 the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc." (2025; sha256 b5536db9)

## (helper) — `scveh.operating_business`

- **Authored helper label:** The business portion of the operating expenses
- **Encoded (NonNegDollars):** Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Actual operating expenses of the vehicle" by the result.
- Expr: `{"amount":"scveh.operating","op":"prorate","part":"scveh.bm_c","places":6,"whole":"scveh.total_c"}`
- Cite: [i1040sc] p. 7, Line 9, "the business portion of expenses" (2025; sha256 b5536db9)

## (helper) — `scveh.line9_actual`

- **Authored helper label:** Business portion of the operating expenses plus parking fees and tolls
- **Encoded (NonNegDollars):** Add helper "The business portion of the operating expenses" and helper "Business parking fees and tolls".
- Expr: `{"of":["scveh.operating_business","scveh.parking"],"op":"sum"}`
- Cite: [i1040sc] p. 7, Line 9, If you deduct actual expenses (2025; sha256 b5536db9)

## 9 — `scveh.line9`

- **IRS:** Car and truck expenses for this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Standard mileage rate or actual expenses" = 'standard' → helper "Standard mileage amount plus parking fees and tolls"] [helper "Standard mileage rate or actual expenses" = 'actual' → helper "Business portion of the operating expenses plus parking fees and tolls"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.method",{"const":"standard"}],"op":"test"},"then":"scveh.line9_standard"},{"guard":{"eq":["scveh.method",{"const":"actual"}],"op":"test"},"then":"scveh.line9_actual"}],"op":"choose"}`
- Cite: [i1040sc] pp. 6-7, Line 9 (2025; sha256 b5536db9)

## (helper) — `scveh.is_actual_owned`

- **Authored helper label:** Owned and on actual expenses
- **Encoded (Bool):** helper "Standard mileage rate or actual expenses" = 'actual' and helper "Owned (not leased)" = true
- Expr: `{"all":[{"eq":["scveh.method",{"const":"actual"}],"op":"test"},{"eq":["scveh.owned",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sc] p. 7, Line 9, "Show depreciation on line 13 and rent or lease payments on line 20a" (2025; sha256 b5536db9)

## (helper) — `scveh.is_actual_leased`

- **Authored helper label:** Leased and on actual expenses
- **Encoded (Bool):** helper "Standard mileage rate or actual expenses" = 'actual' and helper "Owned (not leased)" = false
- Expr: `{"all":[{"eq":["scveh.method",{"const":"actual"}],"op":"test"},{"eq":["scveh.owned",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040sc] p. 7, Line 9 (2025; sha256 b5536db9)

## (helper) — `scveh.lease`

- **Authored helper label:** Lease payments for the vehicle
- **Encoded (NonNegDollars):** Input — Your 2025 lease payments for this vehicle
- Expr: `{"op":"input","source":"Your 2025 lease payments for this vehicle"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b, "enter on line 20a the business portion of your rental cost" (2025; sha256 b5536db9)

## (helper) — `scveh.lease_business`

- **Authored helper label:** The business portion of the lease payments
- **Encoded (NonNegDollars):** Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Lease payments for the vehicle" by the result.
- Expr: `{"amount":"scveh.lease","op":"prorate","part":"scveh.bm_c","places":6,"whole":"scveh.total_c"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b (2025; sha256 b5536db9)

## 20a — `scveh.line20a`

- **IRS:** Rent or lease of this vehicle (business portion)
- **Encoded (NonNegDollars):** Choose — [helper "Leased and on actual expenses" = true → helper "The business portion of the lease payments"] [helper "Leased and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_leased",{"const":true}],"op":"test"},"then":"scveh.lease_business"},{"guard":{"eq":["scveh.is_actual_leased",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b (2025; sha256 b5536db9)

## (gate) — `scveh.low_use`

- **Authored helper label:** Business use is 50% or less
- **Encoded (Bool):** helper "Business use is more than 50%" = false
- Expr: `{"eq":["scveh.over_half",{"const":false}],"op":"test"}`
- Cite: [i4562] p. 14, Lines 26 and 27 (2025; sha256 5c1c95b7)

## (b) — `scveh.placed`

- **Authored helper label:** Year placed in service
- **Encoded (Enum(placed_year)):** Input — The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)
- **Refusal:** when scveh.low_use is true, cannot complete Listed property used 50% or less in a qualified business use (Form 4562 line 27). A vehicle used 50% or less for business is depreciated under ADS and is outside this tool. Cite: [i4562] p. 14, Lines 26 and 27; p. 15, Column (f) (2025; sha256 5c1c95b7)
- Expr: `{"op":"input","source":"The year you placed this vehicle in service in the business (2019 to 2025; a vehicle placed in service earlier is outside this tool)"}`
- Cite: [i4562] p. 14, Column (b)—Date placed in service (2025; sha256 5c1c95b7)

## (screen) — `scveh.screen`

- **Authored helper label:** Does any of these apply to this vehicle?
- **Encoded (Bool):** Input — Does any of these apply to this vehicle: you placed it in service before 2019; you claimed a special depreciation allowance for it in an earlier year; you used the standard mileage rate for it in an earlier year; you disposed of it in 2025; you acquired it in a trade-in or from a related person; its business use was 50% or less in any earlier year; it is an electric vehicle placed in service before 2007; you reduced its basis by a clean-fuel deduction or a vehicle credit; you converted it from personal use to business use during 2025; or you use it in your business of transporting persons or property for hire, or it is an ambulance or hearse?
- Expr: `{"op":"input","source":"Does any of these apply to this vehicle: you placed it in service before 2019; you claimed a special depreciation allowance for it in an earlier year; you used the standard mileage rate for it in an earlier year; you disposed of it in 2025; you acquired it in a trade-in or from a related person; its business use was 50% or less in any earlier year; it is an electric vehicle placed in service before 2007; you reduced its basis by a clean-fuel deduction or a vehicle credit; you converted it from personal use to business use during 2025; or you use it in your business of transporting persons or property for hire, or it is an ambulance or hearse?"}`
- Cite: [i4562] pp. 13-15, Part V, Lines 26 and 27 and Limits for passenger automobiles (p. 14, "If during the tax year you convert property used solely for personal purposes to business/investment use"); p946 p. 63, Deductions for Passenger Automobiles Acquired in a Trade-In (2025; sha256 5c1c95b7)

## (gate) — `scveh.screened`

- **Authored helper label:** This vehicle's depreciation is outside this tool
- **Encoded (Bool):** column (screen) (scveh.screen) = true
- Expr: `{"eq":["scveh.screen",{"const":true}],"op":"test"}`
- Cite: [i4562] pp. 13-15, Part V (2025; sha256 5c1c95b7)

## (d) — `scveh.cost`

- **Authored helper label:** Cost or other basis
- **Encoded (NonNegDollars):** Input — The vehicle's cost (including sales tax) or other basis, not reduced by any section 179 deduction or depreciation (for a vehicle converted from personal use, the smaller of its adjusted basis or its fair market value on the date of conversion)
- **Refusal:** when scveh.screened is true, cannot complete Vehicle depreciation outside this tool (placed in service before 2019, an earlier special allowance, an earlier standard mileage rate, a disposition, a trade-in, earlier business use of 50% or less, and the other items of the screen). This vehicle's depreciation is outside this tool. Cite: [i4562] pp. 13-15, Part V (2025; sha256 5c1c95b7)
- **Refusal:** when scveh.too_old is true, cannot complete Vehicle placed in service before 2019. A vehicle placed in service before 2019 is outside this tool. Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)
- Expr: `{"op":"input","source":"The vehicle's cost (including sales tax) or other basis, not reduced by any section 179 deduction or depreciation (for a vehicle converted from personal use, the smaller of its adjusted basis or its fair market value on the date of conversion)"}`
- Cite: [i4562] p. 14, Column (d)—Cost or other basis (2025; sha256 5c1c95b7)

## (helper) — `scveh.passenger`

- **Authored helper label:** Subject to the limits for passenger automobiles
- **Encoded (Bool):** Input — Is this a passenger automobile subject to the depreciation limits: a 4-wheeled vehicle made mainly for public roads rated at 6,000 pounds unloaded gross vehicle weight or less (for a truck or van, 6,000 pounds gross vehicle weight or less), and not a truck or van specially modified as a qualified nonpersonal use vehicle?
- Expr: `{"op":"input","source":"Is this a passenger automobile subject to the depreciation limits: a 4-wheeled vehicle made mainly for public roads rated at 6,000 pounds unloaded gross vehicle weight or less (for a truck or van, 6,000 pounds gross vehicle weight or less), and not a truck or van specially modified as a qualified nonpersonal use vehicle?"}`
- Cite: [i4562] p. 14, Limits for passenger automobiles, "Passenger automobiles are 4-wheeled vehicles ..." and Exception (2025; sha256 5c1c95b7)

## (helper) — `scveh.suv`

- **Authored helper label:** An SUV or similar vehicle rated 6,000 to 14,000 pounds
- **Encoded (Bool):** Input — If it is not subject to those limits: is it a 4-wheeled vehicle mainly designed or used to carry passengers over public roads, rated at more than 6,000 and not more than 14,000 pounds gross vehicle weight, other than one seating more than nine behind the driver, one with a cargo area of at least 6 feet not readily accessible from the passenger compartment, or one with no seating behind the driver and no body section more than 30 inches ahead of the windshield?
- Expr: `{"op":"input","source":"If it is not subject to those limits: is it a 4-wheeled vehicle mainly designed or used to carry passengers over public roads, rated at more than 6,000 and not more than 14,000 pounds gross vehicle weight, other than one seating more than nine behind the driver, one with a cargo area of at least 6 feet not readily accessible from the passenger compartment, or one with no seating behind the driver and no body section more than 30 inches ahead of the windshield?"}`
- Cite: [i4562] p. 16, Column (i)—Elected section 179 cost, "You cannot elect to expense more than $31,300 of the cost of any SUVs and certain other vehicles" (2025; sha256 5c1c95b7)

## (helper) — `scveh.year`

- **Authored helper label:** Year of recovery in 2025
- **Encoded (Count):** Find the entry in Year of recovery in 2025, by year placed in service for placed column (b).
- Expr: `{"keys":["scveh.placed"],"op":"keyed_lookup","table":"recovery_year"}`
- Cite: [p946] p. 37, Using the MACRS Percentage Tables (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.is2025`

- **Authored helper label:** Placed in service in 2025
- **Encoded (Bool):** column (b) = 'y2025'
- Expr: `{"eq":["scveh.placed",{"const":"y2025"}],"op":"test"}`
- Cite: [i4562] p. 13, Line 25; p. 16, Column (i) (2025; sha256 5c1c95b7)

## (helper) — `scveh.is2019`

- **Authored helper label:** Placed in service in 2019 (2025 is after the recovery period)
- **Encoded (Bool):** column (b) = 'y2019'
- Expr: `{"eq":["scveh.placed",{"const":"y2019"}],"op":"test"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.y5`

- **Authored helper label:** Five-year property
- **Encoded (Enum(macrs_period)):** Enter y5 (sc.period_y5).
- Expr: `{"op":"param","ref":"sc.period_y5"}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a), "5-year property includes the following. Automobiles. Light general purpose trucks" (2025; sha256 5c1c95b7)

## 13 — `scveh.bus_cost`

- **IRS:** Business/investment cost (cost times business use)
- **Encoded (NonNegDollars):** Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply column (d) by the result.
- Expr: `{"amount":"scveh.cost","op":"prorate","part":"scveh.bm_c","places":6,"whole":"scveh.total_c"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 13, "Multiply line 12 by line 8. This is your business/investment cost" (For use in preparing 2025 returns; sha256 07fadfb2)

## (i) — `scveh.s179_elect`

- **Authored helper label:** Elected section 179 cost
- **Encoded (NonNegDollars):** Input — The amount of this vehicle's cost you elect to expense under section 179 (zero if none)
- Expr: `{"op":"input","source":"The amount of this vehicle's cost you elect to expense under section 179 (zero if none)"}`
- Cite: [i4562] p. 16, Column (i)—Elected section 179 cost (2025; sha256 5c1c95b7)

## (helper) — `scveh.suv_cap`

- **Authored helper label:** SUV section 179 limit
- **Encoded (NonNegDollars):** Enter $31,300 (s179.suv_limit).
- Expr: `{"op":"param","ref":"s179.suv_limit"}`
- Cite: [i4562] p. 16, Column (i), "$31,300" (2025; sha256 5c1c95b7)

## (gate) — `scveh.s179_bad`

- **Authored helper label:** The section 179 election is more than the business cost, or than the SUV limit
- **Encoded (Bool):** (column (i) > line 13 or helper "Subject to the limits for passenger automobiles" = false and helper "An SUV or similar vehicle rated 6,000 to 14,000 pounds" = true and column (i) > helper "SUV section 179 limit")
- Expr: `{"any":[{"gt":["scveh.s179_elect","scveh.bus_cost"],"op":"test"},{"all":[{"eq":["scveh.passenger",{"const":false}],"op":"test"},{"eq":["scveh.suv",{"const":true}],"op":"test"},{"gt":["scveh.s179_elect","scveh.suv_cap"],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)

## (helper) — `scveh.after_jan19`

- **Authored helper label:** Acquired after January 19, 2025
- **Encoded (Bool):** Input — Did you acquire this vehicle after January 19, 2025?
- Expr: `{"op":"input","source":"Did you acquire this vehicle after January 19, 2025?"}`
- Cite: [i4562] p. 13, Line 25, "certain qualified property acquired after January 19, 2025" (2025; sha256 5c1c95b7)

## (helper) — `scveh.bonus_choice`

- **Authored helper label:** Special depreciation allowance for 5-year property
- **Encoded (Enum(bonus_choice)):** Input — For 5-year property placed in service in 2025, did you claim the special depreciation allowance (full), elect the 40% allowance instead of 100% for property acquired after January 19, 2025 (forty), or elect not to claim any special allowance (none)?
- Expr: `{"op":"input","source":"For 5-year property placed in service in 2025, did you claim the special depreciation allowance (full), elect the 40% allowance instead of 100% for property acquired after January 19, 2025 (forty), or elect not to claim any special allowance (none)?"}`
- Cite: [i4562] p. 13, Line 25; p. 7, Election out (2025; sha256 5c1c95b7)

## (screen) — `scveh.bonus_same`

- **Authored helper label:** Is the choice the same for all 5-year property placed in service in 2025?
- **Encoded (Bool):** Input — Is that choice the same for all 5-year property (vehicles, computers and other 5-year property) that you (and your spouse, on a joint return) placed in service in 2025?
- Expr: `{"op":"input","source":"Is that choice the same for all 5-year property (vehicles, computers and other 5-year property) that you (and your spouse, on a joint return) placed in service in 2025?"}`
- Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)

## (gate) — `scveh.bonus_mixed`

- **Authored helper label:** The special allowance choice differs within the 5-year class
- **Encoded (Bool):** column (screen) (scveh.bonus_same) = false
- Expr: `{"eq":["scveh.bonus_same",{"const":false}],"op":"test"}`
- Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)

## (helper) — `scveh.claims_bonus`

- **Authored helper label:** A special allowance is claimed
- **Encoded (Bool):** helper "Special depreciation allowance for 5-year property" ≠ 'none'
- Expr: `{"ne":["scveh.bonus_choice",{"const":"none"}],"op":"test"}`
- Cite: [i4562] p. 13, Line 25 (2025; sha256 5c1c95b7)

## (helper) — `scveh.rate40`

- **Authored helper label:** 40% special allowance
- **Encoded (Rate):** Enter 40% (0.40) (sc.bonus_rate_40).
- Expr: `{"op":"param","ref":"sc.bonus_rate_40"}`
- Cite: [i4562] p. 5, Line 14 (2025; sha256 5c1c95b7)

## (helper) — `scveh.lim_first_bonus`

- **Authored helper label:** First-year limit with the special allowance
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year of recovery in 2025".
- Expr: `{"keys":["scveh.placed","scveh.year"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.lim_first_none`

- **Authored helper label:** First-year limit without the special allowance
- **Encoded (NonNegDollars):** Find the entry in First-year limit for passenger automobiles without the special depreciation allowance (Pub. 946, footnotes 1 to 6) for placed column (b).
- Expr: `{"keys":["scveh.placed"],"op":"keyed_lookup","table":"auto_limit_first_nobonus"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, footnote 1, "the maximum depreciation deduction is $12,200" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.lim_2025`

- **Authored helper label:** Limit for a 2025 vehicle
- **Encoded (NonNegDollars):** Choose — [helper "A special allowance is claimed" = true → helper "First-year limit with the special allowance"] [helper "A special allowance is claimed" = false → helper "First-year limit without the special allowance"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.claims_bonus",{"const":true}],"op":"test"},"then":"scveh.lim_first_bonus"},{"guard":{"eq":["scveh.claims_bonus",{"const":false}],"op":"test"},"then":"scveh.lim_first_none"}],"op":"choose"}`
- Cite: [i4562] p. 14, Limits for passenger automobiles; Table 2, "* If you take the special depreciation allowance ... the limit is $20,200" (2025; sha256 5c1c95b7)

## (helper) — `scveh.lim_prior`

- **Authored helper label:** Limit for the vehicle's 2025 year of recovery
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year of recovery in 2025".
- Expr: `{"keys":["scveh.placed","scveh.year"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## 7 — `scveh.line7`

- **IRS:** Maximum depreciation deduction for this year from the appropriate table
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "Limit for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Limit for the vehicle's 2025 year of recovery"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.lim_2025"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.lim_prior"}],"op":"choose"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 7 (For use in preparing 2025 returns; sha256 07fadfb2)

## 9 — `scveh.line9w`

- **IRS:** Adjusted maximum depreciation deduction (line 7 times the business/investment-use percentage)
- **Encoded (NonNegDollars):** Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 7 by the result.
- Expr: `{"amount":"scveh.line7","op":"prorate","part":"scveh.bm_c","places":6,"whole":"scveh.total_c"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 9; i4562 p. 14, "you must reduce the applicable limit to an amount equal to the limit multiplied by that percentage" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.s179_2025_ok`

- **Authored helper label:** Section 179 elected for a 2025 vehicle
- **Encoded (NonNegDollars):** Enter the amount from column (i).
- **Refusal:** when scveh.s179_bad is true, cannot complete Section 179 election above the vehicle's business cost or the SUV limit. A section 179 election must not exceed the business cost, or $31,300 for an SUV. Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)
- Expr: `{"from":"scveh.s179_elect","op":"copy"}`
- Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)

## 10 — `scveh.line10`

- **IRS:** Section 179 deduction claimed this year (not more than line 9 for a passenger automobile)
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Interpretation: amb.2025.vehicle_s179_claimed
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.line10_2025"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 10, "Enter -0- if this is not the year you placed the car in service"; i4562 p. 15, Column (i) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.line10_2025`

- **Authored helper label:** Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
- **Encoded (NonNegDollars):** Choose — [helper "Subject to the limits for passenger automobiles" = true → helper "The section 179 election, not more than line 9"] [helper "Subject to the limits for passenger automobiles" = false → helper "Section 179 elected for a 2025 vehicle"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.passenger",{"const":true}],"op":"test"},"then":"scveh.s179_line10"},{"guard":{"eq":["scveh.passenger",{"const":false}],"op":"test"},"then":"scveh.s179_2025_ok"}],"op":"choose"}`
- Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)

## (helper) — `scveh.s179_line10`

- **Authored helper label:** The section 179 election, not more than line 9
- **Encoded (NonNegDollars):** Enter the smaller of helper "Section 179 elected for a 2025 vehicle" or line 9 (scveh.line9w).
- Expr: `{"of":["scveh.s179_2025_ok","scveh.line9w"],"op":"smaller_of"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 10, "(not more than line 9)" (For use in preparing 2025 returns; sha256 07fadfb2)

## 11 — `scveh.line11`

- **IRS:** Subtract line 10 from line 9
- **Encoded (NonNegDollars):** Subtract line 10 from line 9 (scveh.line9w). If zero or less, enter -0-.
- Expr: `{"from":"scveh.line9w","op":"subtract_floor0","take":"scveh.line10"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 11 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.prior_179`

- **Authored helper label:** Section 179 deduction claimed for this vehicle in the year placed in service
- **Encoded (NonNegDollars):** Input — The section 179 deduction you claimed for this vehicle in the year you placed it in service (zero if none)
- Expr: `{"op":"input","source":"The section 179 deduction you claimed for this vehicle in the year you placed it in service (zero if none)"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 14 (For use in preparing 2025 returns; sha256 07fadfb2)

## 14 — `scveh.line14`

- **IRS:** Section 179 deduction claimed in the year you placed the car in service
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → line 10] [helper "Placed in service in 2025" = false → helper "Section 179 deduction claimed for this vehicle in the year placed in service"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.line10"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.prior_179"}],"op":"choose"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 14 (For use in preparing 2025 returns; sha256 07fadfb2)

## 15 — `scveh.line15`

- **IRS:** Tentative basis for depreciation (line 13 less line 14)
- **Encoded (NonNegDollars):** Subtract line 14 from line 13. If zero or less, enter -0-.
- Expr: `{"from":"scveh.bus_cost","op":"subtract_floor0","take":"scveh.line14"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 15 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.bonus_full`

- **Authored helper label:** 100% special allowance
- **Encoded (NonNegDollars):** Enter the amount from line 15.
- **Refusal:** when scveh.bonus_mixed is true, cannot complete Different special allowance elections within the 5-year class. An election that is not the same for the whole class is outside this tool. Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)
- Expr: `{"from":"scveh.line15","op":"copy"}`
- Cite: [i4562] p. 5, Line 14, 100% special depreciation allowance (2025; sha256 5c1c95b7)

## (helper) — `scveh.bonus_forty`

- **Authored helper label:** 40% special allowance
- **Encoded (NonNegDollars):** Multiply line 15 by helper "40% special allowance".
- **Refusal:** when scveh.bonus_mixed is true, cannot complete Different special allowance elections within the 5-year class. An election that is not the same for the whole class is outside this tool. Cite: [i4562] p. 7, Election out (2025; sha256 5c1c95b7)
- Expr: `{"amount":"scveh.line15","op":"multiply_rate","rate":"scveh.rate40"}`
- Cite: [i4562] p. 7, How to figure the allowance (2025; sha256 5c1c95b7)

## (helper) — `scveh.bonus_fullcase`

- **Authored helper label:** The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%
- **Encoded (NonNegDollars):** Choose — [helper "Acquired after January 19, 2025" = true → helper "100% special allowance"] [helper "Acquired after January 19, 2025" = false → helper "40% special allowance"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.after_jan19",{"const":true}],"op":"test"},"then":"scveh.bonus_full"},{"guard":{"eq":["scveh.after_jan19",{"const":false}],"op":"test"},"then":"scveh.bonus_forty"}],"op":"choose"}`
- Cite: [i4562] p. 5, Line 14 (2025; sha256 5c1c95b7)

## (helper) — `scveh.bonus_2025`

- **Authored helper label:** Special allowance for a 2025 vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Special depreciation allowance for 5-year property" = 'full' → helper "The allowance when it is claimed: 100% if acquired after January 19, 2025, otherwise 40%"] [helper "Special depreciation allowance for 5-year property" = 'forty' → helper "40% special allowance"] [helper "Special depreciation allowance for 5-year property" = 'none' → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.bonus_choice",{"const":"full"}],"op":"test"},"then":"scveh.bonus_fullcase"},{"guard":{"eq":["scveh.bonus_choice",{"const":"forty"}],"op":"test"},"then":"scveh.bonus_forty"},{"guard":{"eq":["scveh.bonus_choice",{"const":"none"}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] pp. 5-7, Line 14 (2025; sha256 5c1c95b7)

## 16 — `scveh.line16`

- **IRS:** Special depreciation allowance
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "Special allowance for a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.bonus_2025"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 16, "Enter -0- if this is not the year you placed the car in service" (For use in preparing 2025 returns; sha256 07fadfb2)

## 25 — `scveh.bonus_allowed`

- **IRS:** Special depreciation allowance allowed (not more than line 11)
- **Encoded (NonNegDollars):** Enter the smaller of line 16 or line 11.
- Expr: `{"of":["scveh.line16","scveh.line11"],"op":"smaller_of"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 16, Note 1, "If line 16 is equal to line 11, stop here. Your depreciation deduction (including your special depreciation allowance) is limited to the amount on line 11" (For use in preparing 2025 returns; sha256 07fadfb2)

## 17 — `scveh.line17`

- **IRS:** Limit on the MACRS depreciation (line 11 less line 16)
- **Encoded (NonNegDollars):** Subtract line 16 from line 11. If zero or less, enter -0-.
- Expr: `{"from":"scveh.line11","op":"subtract_floor0","take":"scveh.line16"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 17 (For use in preparing 2025 returns; sha256 07fadfb2)

## 18 — `scveh.line18`

- **IRS:** Basis for depreciation (line 15 less line 16)
- **Encoded (NonNegDollars):** Subtract line 16 from line 15. If zero or less, enter -0-.
- Expr: `{"from":"scveh.line15","op":"subtract_floor0","take":"scveh.line16"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 18 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.quarter`

- **Authored helper label:** Quarter of 2025 in which the vehicle was placed in service
- **Encoded (Enum(quarter)):** Input — The quarter of 2025 in which you placed this vehicle in service: January to March, April to June, July to September, or October to December
- Expr: `{"op":"input","source":"The quarter of 2025 in which you placed this vehicle in service: January to March, April to June, July to September, or October to December"}`
- Cite: [p946] p. 41, Using the Applicable Convention, Mid-quarter convention (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.qconv`

- **Authored helper label:** Mid-quarter convention for that quarter
- **Encoded (Enum(macrs_convention)):** Find the entry in Mid-quarter convention by quarter placed in service for quarter helper "Quarter of 2025 in which the vehicle was placed in service".
- Expr: `{"keys":["scveh.quarter"],"op":"keyed_lookup","table":"quarter_convention"}`
- Cite: [i4562] p. 11, Column (e)—Convention (2025; sha256 5c1c95b7)

## (helper) — `scveh.hy`

- **Authored helper label:** Half-year convention
- **Encoded (Enum(macrs_convention)):** Enter hy (sc.conv_hy).
- Expr: `{"op":"param","ref":"sc.conv_hy"}`
- Cite: [i4562] p. 11, Column (e)—Convention (2025; sha256 5c1c95b7)

## (helper) — `scveh.prior_conv`

- **Authored helper label:** Convention used in the year placed in service
- **Encoded (Enum(macrs_convention)):** Input — The convention used for this vehicle in the year you placed it in service: half-year, or mid-quarter with the quarter placed in service
- Expr: `{"op":"input","source":"The convention used for this vehicle in the year you placed it in service: half-year, or mid-quarter with the quarter placed in service"}`
- Cite: [i4562] p. 15, Column (g)—Method/convention (2025; sha256 5c1c95b7)

## (helper) — `scveh.rate_hy`

- **Authored helper label:** MACRS rate, half-year convention
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Half-year convention" and year helper "Year of recovery in 2025".
- Expr: `{"keys":["scveh.y5","scveh.hy","scveh.year"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Table A-1, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.rate_mq`

- **Authored helper label:** MACRS rate, mid-quarter convention
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Mid-quarter convention for that quarter" and year helper "Year of recovery in 2025".
- Expr: `{"keys":["scveh.y5","scveh.qconv","scveh.year"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-2 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.rate_prior`

- **Authored helper label:** MACRS rate for the 2025 year of recovery
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year of recovery in 2025".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.year"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.line19_hy`

- **Authored helper label:** Line 18 times the half-year rate
- **Encoded (NonNegDollars):** Multiply line 18 by helper "MACRS rate, half-year convention".
- Expr: `{"amount":"scveh.line18","op":"multiply_rate","rate":"scveh.rate_hy"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 19 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.line19_mq`

- **Authored helper label:** Line 18 times the mid-quarter rate
- **Encoded (NonNegDollars):** Multiply line 18 by helper "MACRS rate, mid-quarter convention".
- Expr: `{"amount":"scveh.line18","op":"multiply_rate","rate":"scveh.rate_mq"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 19 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.line19_prior`

- **Authored helper label:** Line 18 times the rate for the 2025 year of recovery
- **Encoded (NonNegDollars):** Multiply line 18 by helper "MACRS rate for the 2025 year of recovery".
- Expr: `{"amount":"scveh.line18","op":"multiply_rate","rate":"scveh.rate_prior"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 19 (For use in preparing 2025 returns; sha256 07fadfb2)

## 19 — `scveh.line19`

- **IRS:** Tentative MACRS depreciation deduction (line 18 times line 6)
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "Line 19 for a 2025 vehicle, half-year or mid-quarter"] [helper "Placed in service in 2025" = false → helper "Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.line19_2025"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.line19_earlier"}],"op":"choose"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 19 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.line19_earlier`

- **Authored helper label:** Line 19 for a vehicle placed in service before 2025 (zero after the recovery period, when the worksheet is not used)
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2019 (2025 is after the recovery period)" = false → helper "Line 18 times the rate for the 2025 year of recovery"] [helper "Placed in service in 2019 (2025 is after the recovery period)" = true → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2019",{"const":false}],"op":"test"},"then":"scveh.line19_prior"},{"guard":{"eq":["scveh.is2019",{"const":true}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (the unrecovered basis is deducted after the recovery period, not figured on the worksheet) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.line19_2025`

- **Authored helper label:** Line 19 for a 2025 vehicle, half-year or mid-quarter
- **Encoded (NonNegDollars):** Choose — [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = false → helper "Line 18 times the half-year rate"] [mq helper "The mid-quarter convention applies: the October to December bases are more than 40% of all 2025 bases" = true → helper "Line 18 times the mid-quarter rate"]
- Expr: `{"alternatives":[{"guard":{"eq":["mq.applies",{"const":false}],"op":"test"},"then":"scveh.line19_hy"},{"guard":{"eq":["mq.applies",{"const":true}],"op":"test"},"then":"scveh.line19_mq"}],"op":"choose"}`
- Cite: [i4562] p. 11, Column (e)—Convention (2025; sha256 5c1c95b7)

## 20 — `scveh.line20`

- **IRS:** MACRS depreciation deduction (the lesser of line 17 or line 19)
- **Encoded (NonNegDollars):** Enter the smaller of line 17 or line 19.
- Expr: `{"of":["scveh.line17","scveh.line19"],"op":"smaller_of"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 20 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.b100`

- **Authored helper label:** Cost less the section 179 deduction (as if used 100% for business)
- **Encoded (NonNegDollars):** Subtract helper "Section 179 deduction claimed for this vehicle in the year placed in service" from column (d). If zero or less, enter -0-.
- Expr: `{"from":"scveh.cost","op":"subtract_floor0","take":"scveh.prior_179"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, "as if the business use had been 100%" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.k1`

- **Authored helper label:** Year 1 of the recovery period
- **Encoded (Count):** Enter 1 (sc.year1).
- Expr: `{"op":"param","ref":"sc.year1"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.r1`

- **Authored helper label:** MACRS rate for year 1
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year 1 of the recovery period".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.k1"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t1`

- **Authored helper label:** Year 1 MACRS amount as if used 100% for business
- **Encoded (NonNegDollars):** Multiply helper "Cost less the section 179 deduction (as if used 100% for business)" by helper "MACRS rate for year 1".
- Expr: `{"amount":"scveh.b100","op":"multiply_rate","rate":"scveh.r1"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Percentage, Amount) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.l1`

- **Authored helper label:** Year 1 limit (no special allowance)
- **Encoded (NonNegDollars):** Enter the amount from helper "First-year limit without the special allowance".
- Expr: `{"from":"scveh.lim_first_none","op":"copy"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, footnote 6, $10,100 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t1s`

- **Authored helper label:** Year 1 section 179 deduction plus MACRS amount
- **Encoded (NonNegDollars):** Add helper "Section 179 deduction claimed for this vehicle in the year placed in service" and helper "Year 1 MACRS amount as if used 100% for business".
- Expr: `{"of":["scveh.prior_179","scveh.t1"],"op":"sum"}`
- Cite: [p946] pp. 61-62, Depreciation Worksheet for Passenger Automobiles, lines 9 to 20 at 100% business use (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d1`

- **Authored helper label:** Year 1 deduction allowable at 100% business use (the lesser of the limit or the amount)
- **Encoded (NonNegDollars):** Enter the smaller of helper "Year 1 limit (no special allowance)" or helper "Year 1 section 179 deduction plus MACRS amount".
- Expr: `{"of":["scveh.l1","scveh.t1s"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Limit, Allowed) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.k2`

- **Authored helper label:** Year 2 of the recovery period
- **Encoded (Count):** Enter 2 (sc.year2).
- Expr: `{"op":"param","ref":"sc.year2"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.r2`

- **Authored helper label:** MACRS rate for year 2
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year 2 of the recovery period".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.k2"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t2`

- **Authored helper label:** Year 2 MACRS amount as if used 100% for business
- **Encoded (NonNegDollars):** Multiply helper "Cost less the section 179 deduction (as if used 100% for business)" by helper "MACRS rate for year 2".
- Expr: `{"amount":"scveh.b100","op":"multiply_rate","rate":"scveh.r2"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Percentage, Amount) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.l2`

- **Authored helper label:** Year 2 limit
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year 2 of the recovery period".
- Expr: `{"keys":["scveh.placed","scveh.k2"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d2`

- **Authored helper label:** Year 2 deduction allowable at 100% business use
- **Encoded (NonNegDollars):** Enter the smaller of helper "Year 2 limit" or helper "Year 2 MACRS amount as if used 100% for business".
- Expr: `{"of":["scveh.l2","scveh.t2"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Limit, Allowed) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.k3`

- **Authored helper label:** Year 3 of the recovery period
- **Encoded (Count):** Enter 3 (sc.year3).
- Expr: `{"op":"param","ref":"sc.year3"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.r3`

- **Authored helper label:** MACRS rate for year 3
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year 3 of the recovery period".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.k3"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t3`

- **Authored helper label:** Year 3 MACRS amount as if used 100% for business
- **Encoded (NonNegDollars):** Multiply helper "Cost less the section 179 deduction (as if used 100% for business)" by helper "MACRS rate for year 3".
- Expr: `{"amount":"scveh.b100","op":"multiply_rate","rate":"scveh.r3"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Percentage, Amount) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.l3`

- **Authored helper label:** Year 3 limit
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year 3 of the recovery period".
- Expr: `{"keys":["scveh.placed","scveh.k3"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d3`

- **Authored helper label:** Year 3 deduction allowable at 100% business use
- **Encoded (NonNegDollars):** Enter the smaller of helper "Year 3 limit" or helper "Year 3 MACRS amount as if used 100% for business".
- Expr: `{"of":["scveh.l3","scveh.t3"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Limit, Allowed) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.k4`

- **Authored helper label:** Year 4 of the recovery period
- **Encoded (Count):** Enter 4 (sc.year4).
- Expr: `{"op":"param","ref":"sc.year4"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.r4`

- **Authored helper label:** MACRS rate for year 4
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year 4 of the recovery period".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.k4"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t4`

- **Authored helper label:** Year 4 MACRS amount as if used 100% for business
- **Encoded (NonNegDollars):** Multiply helper "Cost less the section 179 deduction (as if used 100% for business)" by helper "MACRS rate for year 4".
- Expr: `{"amount":"scveh.b100","op":"multiply_rate","rate":"scveh.r4"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Percentage, Amount) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.l4`

- **Authored helper label:** Year 4 limit
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year 4 of the recovery period".
- Expr: `{"keys":["scveh.placed","scveh.k4"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d4`

- **Authored helper label:** Year 4 deduction allowable at 100% business use
- **Encoded (NonNegDollars):** Enter the smaller of helper "Year 4 limit" or helper "Year 4 MACRS amount as if used 100% for business".
- Expr: `{"of":["scveh.l4","scveh.t4"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Limit, Allowed) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.k5`

- **Authored helper label:** Year 5 of the recovery period
- **Encoded (Count):** Enter 5 (sc.year5).
- Expr: `{"op":"param","ref":"sc.year5"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.r5`

- **Authored helper label:** MACRS rate for year 5
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year 5 of the recovery period".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.k5"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t5`

- **Authored helper label:** Year 5 MACRS amount as if used 100% for business
- **Encoded (NonNegDollars):** Multiply helper "Cost less the section 179 deduction (as if used 100% for business)" by helper "MACRS rate for year 5".
- Expr: `{"amount":"scveh.b100","op":"multiply_rate","rate":"scveh.r5"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Percentage, Amount) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.l5`

- **Authored helper label:** Year 5 limit
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year 5 of the recovery period".
- Expr: `{"keys":["scveh.placed","scveh.k5"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d5`

- **Authored helper label:** Year 5 deduction allowable at 100% business use
- **Encoded (NonNegDollars):** Enter the smaller of helper "Year 5 limit" or helper "Year 5 MACRS amount as if used 100% for business".
- Expr: `{"of":["scveh.l5","scveh.t5"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Limit, Allowed) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.k6`

- **Authored helper label:** Year 6 of the recovery period
- **Encoded (Count):** Enter 6 (sc.year6).
- Expr: `{"op":"param","ref":"sc.year6"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.r6`

- **Authored helper label:** MACRS rate for year 6
- **Encoded (Rate):** Find the entry in MACRS percentage tables, General Depreciation System (Pub. 946, Tables A-1 to A-5 and A-8 to A-12) for period helper "Five-year property" and convention helper "Convention used in the year placed in service" and year helper "Year 6 of the recovery period".
- Expr: `{"keys":["scveh.y5","scveh.prior_conv","scveh.k6"],"op":"keyed_lookup","table":"macrs_gds"}`
- Cite: [p946] Appendix A, Tables A-1 to A-5, 5-year column (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.t6`

- **Authored helper label:** Year 6 MACRS amount as if used 100% for business
- **Encoded (NonNegDollars):** Multiply helper "Cost less the section 179 deduction (as if used 100% for business)" by helper "MACRS rate for year 6".
- Expr: `{"amount":"scveh.b100","op":"multiply_rate","rate":"scveh.r6"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Percentage, Amount) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.l6`

- **Authored helper label:** Year 6 limit
- **Encoded (NonNegDollars):** Find the entry in Maximum depreciation deduction for passenger automobiles placed in service 2019 to 2025 (Pub. 946) for placed column (b) and year helper "Year 6 of the recovery period".
- Expr: `{"keys":["scveh.placed","scveh.k6"],"op":"keyed_lookup","table":"auto_limit"}`
- Cite: [p946] p. 59, Maximum Depreciation Deduction, Passenger Automobiles (table) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d6`

- **Authored helper label:** Year 6 deduction allowable at 100% business use
- **Encoded (NonNegDollars):** Enter the smaller of helper "Year 6 limit" or helper "Year 6 MACRS amount as if used 100% for business".
- Expr: `{"of":["scveh.l6","scveh.t6"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, example (Limit, Allowed) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.d_total`

- **Authored helper label:** Deductions allowable during the recovery period at 100% business use
- **Encoded (NonNegDollars):** Add helper "Year 1 deduction allowable at 100% business use (the lesser of the limit or the amount)", helper "Year 2 deduction allowable at 100% business use", helper "Year 3 deduction allowable at 100% business use", helper "Year 4 deduction allowable at 100% business use", helper "Year 5 deduction allowable at 100% business use", and helper "Year 6 deduction allowable at 100% business use".
- Expr: `{"of":["scveh.d1","scveh.d2","scveh.d3","scveh.d4","scveh.d5","scveh.d6"],"op":"sum"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, "you would still reduce your basis by the maximum amount allowable as if the business use had been 100%" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.unrecovered`

- **Authored helper label:** Unrecovered basis at the end of the recovery period
- **Encoded (NonNegDollars):** Subtract helper "Deductions allowable during the recovery period at 100% business use" from column (d). If zero or less, enter -0-.
- Expr: `{"from":"scveh.cost","op":"subtract_floor0","take":"scveh.d_total"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, "At the end of 2024, you had an unrecovered basis of $14,565 ($31,500 − $16,935)" (amb.2025.auto_unrecovered_basis) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.post_amount`

- **Authored helper label:** The lesser of the limit or the unrecovered basis
- **Encoded (NonNegDollars):** Enter the smaller of helper "Limit for the vehicle's 2025 year of recovery" or helper "Unrecovered basis at the end of the recovery period".
- Expr: `{"of":["scveh.lim_prior","scveh.unrecovered"],"op":"smaller_of"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, "you can deduct each year the lesser of $1,875 or your remaining unrecovered basis" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.post`

- **Authored helper label:** 2025 deduction after the recovery period (times the business use percentage)
- **Encoded (NonNegDollars):** Divide helper "Business miles, as cents" by helper "Total miles, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "The lesser of the limit or the unrecovered basis" by the result.
- Expr: `{"amount":"scveh.post_amount","op":"prorate","part":"scveh.bm_c","places":6,"whole":"scveh.total_c"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period, "$8,739 ($14,565 × 60% (0.60))" (For use in preparing 2025 returns; sha256 07fadfb2)

## (gate) — `scveh.too_old`

- **Authored helper label:** Placed in service before 2019
- **Encoded (Bool):** helper "Year of recovery in 2025" > 7 (a count)
- Expr: `{"gt":["scveh.year",{"const":7,"type":"Count"}],"op":"test"}`
- Cite: [p946] p. 61, Deductions After the Recovery Period (owner: vehicles placed in service 2019 to 2025) (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.bonus_v`

- **Authored helper label:** Special allowance for this vehicle (line 25)
- **Encoded (NonNegDollars):** Choose — [helper "Subject to the limits for passenger automobiles" = true → line 25] [helper "Subject to the limits for passenger automobiles" = false → line 16]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.passenger",{"const":true}],"op":"test"},"then":"scveh.bonus_allowed"},{"guard":{"eq":["scveh.passenger",{"const":false}],"op":"test"},"then":"scveh.line16"}],"op":"choose"}`
- Cite: [i4562] p. 13, Line 25 (2025; sha256 5c1c95b7)

## (helper) — `scveh.macrs_pass`

- **Authored helper label:** Column (h) for a passenger automobile
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2019 (2025 is after the recovery period)" = false → line 20] [helper "Placed in service in 2019 (2025 is after the recovery period)" = true → helper "2025 deduction after the recovery period (times the business use percentage)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2019",{"const":false}],"op":"test"},"then":"scveh.line20"},{"guard":{"eq":["scveh.is2019",{"const":true}],"op":"test"},"then":"scveh.post"}],"op":"choose"}`
- Cite: [i4562] p. 15, Column (h), "If the recovery period for an automobile ended before your tax year beginning in 2025, enter your unrecovered basis, if any" (2025; sha256 5c1c95b7)

## (helper) — `scveh.macrs_heavy`

- **Authored helper label:** Column (h) for a vehicle not subject to the limits
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2019 (2025 is after the recovery period)" = false → line 19] [helper "Placed in service in 2019 (2025 is after the recovery period)" = true → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2019",{"const":false}],"op":"test"},"then":"scveh.line19"},{"guard":{"eq":["scveh.is2019",{"const":true}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 15, Column (h); Pub. 946, "You cannot claim a depreciation deduction for listed property other than passenger automobiles after the recovery period ends" (2025; sha256 5c1c95b7)

## (helper) — `scveh.macrs_v`

- **Authored helper label:** Column (h)
- **Encoded (NonNegDollars):** Choose — [helper "Subject to the limits for passenger automobiles" = true → helper "Column (h) for a passenger automobile"] [helper "Subject to the limits for passenger automobiles" = false → helper "Column (h) for a vehicle not subject to the limits"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.passenger",{"const":true}],"op":"test"},"then":"scveh.macrs_pass"},{"guard":{"eq":["scveh.passenger",{"const":false}],"op":"test"},"then":"scveh.macrs_heavy"}],"op":"choose"}`
- Cite: [i4562] p. 15, Column (h) (2025; sha256 5c1c95b7)

## (helper) — `scveh.bonus`

- **Authored helper label:** Line 25: special allowance of this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Owned and on actual expenses" = true → helper "Special allowance (owned, actual expenses)"] [helper "Owned and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_owned",{"const":true}],"op":"test"},"then":"scveh.bonus_o"},{"guard":{"eq":["scveh.is_actual_owned",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 13, Part V, Section A (2025; sha256 5c1c95b7)

## (helper) — `scveh.macrs`

- **Authored helper label:** Column (h): depreciation of this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Owned and on actual expenses" = true → helper "Depreciation (owned, actual expenses)"] [helper "Owned and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_owned",{"const":true}],"op":"test"},"then":"scveh.macrs_o"},{"guard":{"eq":["scveh.is_actual_owned",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 13, Part V, Section A (2025; sha256 5c1c95b7)

## (helper) — `scveh.s179_2025`

- **Authored helper label:** Column (i): elected section 179 cost of this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Owned and on actual expenses" = true → helper "Section 179 (owned, actual expenses)"] [helper "Owned and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_owned",{"const":true}],"op":"test"},"then":"scveh.s179_2025_o"},{"guard":{"eq":["scveh.is_actual_owned",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 13, Part V, Section A (2025; sha256 5c1c95b7)

## (helper) — `scveh.mq_q4`

- **Authored helper label:** Mid-quarter test basis, fourth quarter of this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Owned and on actual expenses" = true → helper "mq_q4 (owned, actual expenses)"] [helper "Owned and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_owned",{"const":true}],"op":"test"},"then":"scveh.mq_q4_o"},{"guard":{"eq":["scveh.is_actual_owned",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 13, Part V, Section A (2025; sha256 5c1c95b7)

## (helper) — `scveh.mq_total`

- **Authored helper label:** Mid-quarter test basis, 2025 of this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Owned and on actual expenses" = true → helper "mq_total (owned, actual expenses)"] [helper "Owned and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_owned",{"const":true}],"op":"test"},"then":"scveh.mq_total_o"},{"guard":{"eq":["scveh.is_actual_owned",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 13, Part V, Section A (2025; sha256 5c1c95b7)

## (helper) — `scveh.cost179`

- **Authored helper label:** Cost of section 179 property placed in service in 2025 of this vehicle
- **Encoded (NonNegDollars):** Choose — [helper "Owned and on actual expenses" = true → helper "cost179 (owned, actual expenses)"] [helper "Owned and on actual expenses" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is_actual_owned",{"const":true}],"op":"test"},"then":"scveh.cost179_o"},{"guard":{"eq":["scveh.is_actual_owned",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [i4562] p. 13, Part V, Section A (2025; sha256 5c1c95b7)

## (helper) — `scveh.bonus_o`

- **Authored helper label:** Special allowance (owned, actual expenses)
- **Encoded (NonNegDollars):** Enter the amount from helper "Special allowance for this vehicle (line 25)".
- Expr: `{"from":"scveh.bonus_v","op":"copy"}`
- Cite: [i4562] p. 13, Line 25 (2025; sha256 5c1c95b7)

## (helper) — `scveh.macrs_o`

- **Authored helper label:** Depreciation (owned, actual expenses)
- **Encoded (NonNegDollars):** Enter the amount from helper "Column (h)".
- Expr: `{"from":"scveh.macrs_v","op":"copy"}`
- Cite: [i4562] p. 15, Column (h) (2025; sha256 5c1c95b7)

## (helper) — `scveh.s179_2025_o`

- **Authored helper label:** Section 179 (owned, actual expenses)
- **Encoded (NonNegDollars):** Enter the amount from line 10.
- Expr: `{"from":"scveh.line10","op":"copy"}`
- Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)

## (helper) — `scveh.q4_basis`

- **Authored helper label:** Basis for the mid-quarter test when placed in service October to December
- **Encoded (NonNegDollars):** Choose — [helper "Quarter of 2025 in which the vehicle was placed in service" = 'q1' → helper "Zero"] [helper "Quarter of 2025 in which the vehicle was placed in service" = 'q2' → helper "Zero"] [helper "Quarter of 2025 in which the vehicle was placed in service" = 'q3' → helper "Zero"] [helper "Quarter of 2025 in which the vehicle was placed in service" = 'q4' → line 15]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.quarter",{"const":"q1"}],"op":"test"},"then":"scveh.zero"},{"guard":{"eq":["scveh.quarter",{"const":"q2"}],"op":"test"},"then":"scveh.zero"},{"guard":{"eq":["scveh.quarter",{"const":"q3"}],"op":"test"},"then":"scveh.zero"},{"guard":{"eq":["scveh.quarter",{"const":"q4"}],"op":"test"},"then":"scveh.line15"}],"op":"choose"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.mq_q4_o`

- **Authored helper label:** mq_q4 (owned, actual expenses)
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "mq_q4 of a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.mq_q4_a2"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.mq_q4_a2`

- **Authored helper label:** mq_q4 of a 2025 vehicle
- **Encoded (NonNegDollars):** Enter the amount from helper "Basis for the mid-quarter test when placed in service October to December".
- Expr: `{"from":"scveh.q4_basis","op":"copy"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention, Caution (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.mq_total_o`

- **Authored helper label:** mq_total (owned, actual expenses)
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "mq_total of a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.mq_total_a2"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.mq_total_a2`

- **Authored helper label:** mq_total of a 2025 vehicle
- **Encoded (NonNegDollars):** Enter the amount from line 15.
- Expr: `{"from":"scveh.line15","op":"copy"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention, Caution (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.cost179_o`

- **Authored helper label:** cost179 (owned, actual expenses)
- **Encoded (NonNegDollars):** Choose — [helper "Placed in service in 2025" = true → helper "cost179 of a 2025 vehicle"] [helper "Placed in service in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["scveh.is2025",{"const":true}],"op":"test"},"then":"scveh.cost179_a2"},{"guard":{"eq":["scveh.is2025",{"const":false}],"op":"test"},"then":"scveh.zero"}],"op":"choose"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `scveh.cost179_a2`

- **Authored helper label:** cost179 of a 2025 vehicle
- **Encoded (NonNegDollars):** Enter the amount from line 13.
- Expr: `{"from":"scveh.bus_cost","op":"copy"}`
- Cite: [p946] p. 34, Which Convention Applies?, Mid-quarter convention, Caution (For use in preparing 2025 returns; sha256 07fadfb2)
