# Schedule E, Part I — one rental real estate property

- Document: `rental` (form, tax year 2025)
- Collection: keyed entries; [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)
- Note: One entry per rental real estate property (Schedule E types 1 to 5). Its expenses, other than advertising and commissions, are divided by days when it had personal use but was not used as a home; a home rented fewer than 15 days is left out. Its Form 8582 worksheet columns (Parts IV to VIII) are figured here and totalled on Form 8582. Refused: self-rental and other property, average stays of 7 days or less, significant services, less than 10% owned, not for profit, depletion, part of a property the filer lives in, property held mainly for sale or offered in business hours, property incidental to the filer's own business, Form 6198 on an earlier return, a general business credit, costs paid before it was first offered for rent in 2025, car and travel expenses, mortgage interest beyond Form 1098, the cost of a bought leasehold, a home used personally and rented 15 days or more, a held-back loss from a year without active participation, a loss with amounts not at risk, and net income from a rental of nondepreciable property when Form 8582 is required.

## (helper) — `rental.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040se] p. 7, Line 21 (2025; sha256 ad71de35)

## (helper) — `rental.no`

- **Authored helper label:** No (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [i1040se] p. 1, Line 2 (2025; sha256 ad71de35)

## (helper) — `rental.one`

- **Authored helper label:** One
- **Encoded (Count):** Enter 1 (rental.one).
- Expr: `{"op":"param","ref":"rental.one"}`
- Cite: [i1040se] p. 5, Line 1a (2025; sha256 ad71de35)

## 1b — `rental.kind`

- **IRS:** Type of property
- **Encoded (Enum(rental_kind)):** Input — What kind of property is this?

  - sfr: a house, condo or mobile home (one home)
  - multi: a building with two or more homes
  - vacation: a vacation or short-stay rental
  - commercial: shops, offices or other business space
  - land: land only
  - self_rental: property rented to a business you or your spouse run
  - other: something else
- Expr: `{"op":"input","source":"What kind of property is this?\n\n- sfr: a house, condo or mobile home (one home)\n- multi: a building with two or more homes\n- vacation: a vacation or short-stay rental\n- commercial: shops, offices or other business space\n- land: land only\n- self_rental: property rented to a business you or your spouse run\n- other: something else"}`
- Cite: [i1040se] p. 5, Line 1b, "Enter one of the codes listed under “Type of Property” in Part I of the form" (2025; sha256 ad71de35)

## (gate) — `rental.self_rental`

- **Authored helper label:** Self-rental (type 7) or other property (type 8)
- **Encoded (Bool):** (line 1b = 'self_rental' or line 1b = 'other')
- Expr: `{"any":[{"eq":["rental.kind",{"const":"self_rental"}],"op":"test"},{"eq":["rental.kind",{"const":"other"}],"op":"test"}],"op":"test"}`
- Cite: [i1040se] p. 5, Line 1b, "Self-Rental" (2025; sha256 ad71de35)

## 2 — `rental.days_fair`

- **IRS:** Fair rental days
- **Encoded (Count):** Input — How many days in 2025 was it rented at a fair price? Count a day rented at a fair price even if you also used it that day; do not count days it was empty but offered for rent.
- Expr: `{"op":"input","source":"How many days in 2025 was it rented at a fair price? Count a day rented at a fair price even if you also used it that day; do not count days it was empty but offered for rent."}`
- Cite: [i1040se] p. 5, Line 2, "For each property listed on line 1a, report the number of days in the year each property was rented at fair rental value and the number of days of personal use" (2025; sha256 ad71de35)

## (helper) — `rental.personal_any`

- **Authored helper label:** Any day of personal use in 2025
- **Encoded (Bool):** Input — On any day in 2025, did you, another owner or a relative of either use it, or did anyone stay free, below a fair rent or under a home swap?
- Expr: `{"op":"input","source":"On any day in 2025, did you, another owner or a relative of either use it, or did anyone stay free, below a fair rent or under a home swap?"}`
- Cite: [p527] p. 26, What is a day of personal use?, "A day of personal use of a dwelling unit is any day that the unit is used by any of the following persons" (2025; sha256 20c826e9)

## 2 — `rental.days_personal`

- **IRS:** Personal use days
- **Encoded (Count):** Input — How many days in 2025 was it used that way (by you, another owner or a relative of either, or by anyone staying free, below a fair rent or under a home swap)? Leave out days a relative rented it at a fair rent as their main home, days another owner rented it as their main home at a fair rent under a shared equity financing agreement, days spent mostly repairing it, and days it was your main home before or after renting it out (or trying to) for 12 months or more in a row, or for less if you then sold or traded it.
- Expr: `{"op":"input","source":"How many days in 2025 was it used that way (by you, another owner or a relative of either, or by anyone staying free, below a fair rent or under a home swap)? Leave out days a relative rented it at a fair rent as their main home, days another owner rented it as their main home at a fair rent under a shared equity financing agreement, days spent mostly repairing it, and days it was your main home before or after renting it out (or trying to) for 12 months or more in a row, or for less if you then sold or traded it."}`
- Cite: [p527] p. 26, What is a day of personal use?; i1040se p. 5, Line 2, "For each property listed on line 1a, report the number of days in the year each property was rented at fair rental value and the number of days of personal use" (2025; sha256 20c826e9)

## (helper) — `rental.days_overlap`

- **Authored helper label:** Days of personal use that were also fair rental days
- **Encoded (Count):** Input — Of those days, how many were also days it was rented at a fair price (for example, a renter let you stay a weekend)?
- Expr: `{"op":"input","source":"Of those days, how many were also days it was rented at a fair price (for example, a renter let you stay a weekend)?"}`
- Cite: [p527] p. 26, Dwelling Unit Used as a Home, "If a dwelling unit is used for personal purposes on a day it is rented at a fair rental price" (2025; sha256 20c826e9)

## (helper) — `rental.day_cents`

- **Authored helper label:** One day carried as one cent
- **Encoded (NonNegDollars):** Enter $0.01 (rental.day_cents).
- Expr: `{"op":"param","ref":"rental.day_cents"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.tenth_cents`

- **Authored helper label:** One day of personal use carried as ten cents (against one cent per rental day: the 10% test)
- **Encoded (NonNegDollars):** Enter $0.10 (rental.tenth_cents).
- Expr: `{"op":"param","ref":"rental.tenth_cents"}`
- Cite: [p527] p. 26, Dwelling Unit Used as a Home, "10% of the total days it is rented to others at a fair rental price" (2025; sha256 20c826e9)

## (helper) — `rental.fair_c`

- **Authored helper label:** Fair rental days (as cents)
- **Encoded (NonNegDollars):** Multiply helper "One day carried as one cent" by the number on line 2 (rental.days_fair).
- Expr: `{"amount":"rental.day_cents","count":"rental.days_fair","op":"multiply_count"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.personal_raw`

- **Authored helper label:** Personal use days as answered (as cents)
- **Encoded (NonNegDollars):** Multiply helper "One day carried as one cent" by the number on line 2 (rental.days_personal).
- Expr: `{"amount":"rental.day_cents","count":"rental.days_personal","op":"multiply_count"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.personal_c`

- **Authored helper label:** Personal use days (as cents), asked only when there was personal use (none otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = true → helper "Personal use days as answered (as cents)"] [helper "Any day of personal use in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.personal_raw"},{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.overlap_raw`

- **Authored helper label:** Overlap days as answered (as cents)
- **Encoded (NonNegDollars):** Multiply helper "One day carried as one cent" by the number on helper "Days of personal use that were also fair rental days".
- Expr: `{"amount":"rental.day_cents","count":"rental.days_overlap","op":"multiply_count"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.overlap_c`

- **Authored helper label:** Overlap days (as cents), asked only when there was personal use (none otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = true → helper "Overlap days as answered (as cents)"] [helper "Any day of personal use in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.overlap_raw"},{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.use_c`

- **Authored helper label:** Fair rental days plus personal use days, before taking out overlap days (as cents)
- **Encoded (NonNegDollars):** Add helper "Fair rental days (as cents)" and helper "Personal use days (as cents), asked only when there was personal use (none otherwise)".
- Expr: `{"of":["rental.fair_c","rental.personal_c"],"op":"sum"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.total_c`

- **Authored helper label:** Total days of use: rental days plus personal use days not also rental days (as cents)
- **Encoded (NonNegDollars):** Subtract helper "Overlap days (as cents), asked only when there was personal use (none otherwise)" from helper "Fair rental days plus personal use days, before taking out overlap days (as cents)". If zero or less, enter -0-.
- Expr: `{"from":"rental.use_c","op":"subtract_floor0","take":"rental.overlap_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## (helper) — `rental.home_rent_c`

- **Authored helper label:** Fair rental days less days also used personally, for the home test (as cents)
- **Encoded (NonNegDollars):** Subtract helper "Overlap days (as cents), asked only when there was personal use (none otherwise)" from helper "Fair rental days (as cents)". If zero or less, enter -0-.
- Expr: `{"from":"rental.fair_c","op":"subtract_floor0","take":"rental.overlap_c"}`
- Cite: [p527] p. 26, Dwelling Unit Used as a Home, "don't count that day as a day of rental use in applying (2) above" (2025; sha256 20c826e9)

## (helper) — `rental.home_pers10`

- **Authored helper label:** Ten times the personal use days (as cents)
- **Encoded (NonNegDollars):** Multiply helper "One day of personal use carried as ten cents (against one cent per rental day: the 10% test)" by the number on line 2 (rental.days_personal).
- Expr: `{"amount":"rental.tenth_cents","count":"rental.days_personal","op":"multiply_count"}`
- Cite: [p527] p. 26, Dwelling Unit Used as a Home (2025; sha256 20c826e9)

## (helper) — `rental.home_pers10_if_any`

- **Authored helper label:** Ten times the personal use days (as cents), when there was personal use (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = true → helper "Ten times the personal use days (as cents)"] [helper "Any day of personal use in 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.home_pers10"},{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [p527] p. 26, Dwelling Unit Used as a Home (2025; sha256 20c826e9)

## (gate) — `rental.home`

- **Authored helper label:** Used as a home: personal use more than the greater of 14 days or 10% of the fair rental days
- **Encoded (Bool):** helper "Personal use days (as cents), asked only when there was personal use (none otherwise)" > $0.14 (rental.home_days) and helper "Ten times the personal use days (as cents), when there was personal use (zero otherwise)" > helper "Fair rental days less days also used personally, for the home test (as cents)"
- Interpretation: amb.2025.rental_overlap_days
- Expr: `{"all":[{"gt":["rental.personal_c",{"param":"rental.home_days"}],"op":"test"},{"gt":["rental.home_pers10_if_any","rental.home_rent_c"],"op":"test"}],"op":"test"}`
- Cite: [p527] p. 26, Dwelling Unit Used as a Home, "You use a dwelling unit as a home during the tax year if you use it for personal purposes more than the greater of" (2025; sha256 20c826e9)

## (gate) — `rental.excluded`

- **Authored helper label:** Used as a home and rented fewer than 15 days: not reported
- **Encoded (Bool):** helper "Used as a home: personal use more than the greater of 14 days or 10% of the fair rental days" = true and line 2 (rental.days_fair) < 15 (rental.min_rental_days)
- Expr: `{"all":[{"eq":["rental.home",{"const":true}],"op":"test"},{"lt":["rental.days_fair",{"param":"rental.min_rental_days"}],"op":"test"}],"op":"test"}`
- Cite: [i1040se] p. 5, Line 2, "do not report the rental income and do not deduct any rental expenses" (2025; sha256 ad71de35)

## (helper) — `rental.reported`

- **Authored helper label:** The property is reported on Schedule E (not excluded)
- **Encoded (Bool):** helper "Used as a home and rented fewer than 15 days: not reported" = false
- Expr: `{"eq":["rental.excluded",{"const":false}],"op":"test"}`
- Cite: [i1040se] p. 5, Line 2, "do not report the rental income and do not deduct any rental expenses" (2025; sha256 ad71de35)

## (gate) — `rental.ws51`

- **Authored helper label:** Used as a home and rented 15 days or more (Worksheet 5-1)
- **Encoded (Bool):** helper "Used as a home: personal use more than the greater of 14 days or 10% of the fair rental days" = true and helper "Used as a home and rented fewer than 15 days: not reported" = false
- Expr: `{"all":[{"eq":["rental.home",{"const":true}],"op":"test"},{"eq":["rental.excluded",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [p527] p. 28, Used as a home and rented 15 days or more (2025; sha256 20c826e9)

## (helper) — `rental.short_stays`

- **Authored helper label:** Average stay of 30 days or less
- **Encoded (Bool):** Input — Did renters stay 30 days or less, on average? Divide the days it was rented by the number of separate stays.
- Expr: `{"op":"input","source":"Did renters stay 30 days or less, on average? Divide the days it was rented by the number of separate stays."}`
- Cite: [i8582] p. 3, Exceptions, "Figure the average period of customer use for a class of property by dividing the total number of days in all rental periods by the number of rentals" (2025; sha256 76787e11)

## (helper) — `rental.stay7`

- **Authored helper label:** Average stay of 7 days or less
- **Encoded (Bool):** Input — Was the average stay 7 days or less?
- Expr: `{"op":"input","source":"Was the average stay 7 days or less?"}`
- Cite: [i8582] p. 3, Exceptions, "Figure the average period of customer use for a class of property by dividing the total number of days in all rental periods by the number of rentals" (2025; sha256 76787e11)

## (gate) — `rental.stay7_if_short`

- **Authored helper label:** Average stay of 7 days or less, asked only when stays averaged 30 days or less (false otherwise)
- **Encoded (Bool):** Choose — [helper "Average stay of 30 days or less" = true → helper "Average stay of 7 days or less"] [helper "Average stay of 30 days or less" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.short_stays",{"const":true}],"op":"test"},"then":"rental.stay7"},{"guard":{"eq":["rental.short_stays",{"const":false}],"op":"test"},"then":"rental.no"}],"op":"choose"}`
- Cite: [i8582] p. 3, Exceptions (2025; sha256 76787e11)

## (helper) — `rental.services`

- **Authored helper label:** Significant services provided to renters (Schedule C)
- **Encoded (Bool):** Input — Did you, or someone for you, provide services for renters, such as cleaning during their stay, changing linen or meals?
- Expr: `{"op":"input","source":"Did you, or someone for you, provide services for renters, such as cleaning during their stay, changing linen or meals?"}`
- Cite: [i1040se] p. 5, Line 3, "If you provided significant services to the renter, such as maid service, report the rental activity on Schedule C" (2025; sha256 ad71de35)

## (helper) — `rental.under_tenth`

- **Authored helper label:** Less than 10% owned (with the spouse)
- **Encoded (Bool):** Input — At any time in 2025, did you (with your spouse) own less than a tenth of it, by value?
- Expr: `{"op":"input","source":"At any time in 2025, did you (with your spouse) own less than a tenth of it, by value?"}`
- Cite: [i8582] p. 4, Active participation, "in the activity was less than 10% (by value) of all interests in the activity" (2025; sha256 76787e11)

## (helper) — `rental.not_for_profit`

- **Authored helper label:** Not rented to make a profit
- **Encoded (Bool):** Input — Was it rented not to make a profit, for example to a friend at a low rent?
- Expr: `{"op":"input","source":"Was it rented not to make a profit, for example to a friend at a low rent?"}`
- Cite: [p527] p. 17, Not Rented for Profit (2025; sha256 20c826e9)

## (helper) — `rental.depletion`

- **Authored helper label:** Depletion claimed
- **Encoded (Bool):** Input — Do you claim depletion for it (oil, gas, minerals or timber)?
- Expr: `{"op":"input","source":"Do you claim depletion for it (oil, gas, minerals or timber)?"}`
- Cite: [i1040se] p. 6, Line 18, "Depletion" (2025; sha256 ad71de35)

## (helper) — `rental.part_home`

- **Authored helper label:** Part of a property the filer also lives in, lived in during 2025, or uses
- **Encoded (Bool):** Input — Is it part of a property you live in or use yourself, or lived in during 2025, such as a room in your home, one unit of a building you live in, or space in a building that holds your own office?
- Expr: `{"op":"input","source":"Is it part of a property you live in or use yourself, or lived in during 2025, such as a room in your home, one unit of a building you live in, or space in a building that holds your own office?"}`
- Cite: [i1040se] p. 6, Renting out part of your home (2025; sha256 ad71de35)

## (helper) — `rental.held_for_sale`

- **Authored helper label:** Held mainly for sale (as an investment or by a real estate dealer), or made available in business hours for nonexclusive use by many customers
- **Encoded (Bool):** Input — Do you hold it mainly to sell at a gain rather than to rent (as an investment, or for sale to customers as a real estate dealer), or do you make it available during set business hours for use by many customers, such as a parking lot?
- Expr: `{"op":"input","source":"Do you hold it mainly to sell at a gain rather than to rent (as an investment, or for sale to customers as a real estate dealer), or do you make it available during set business hours for use by many customers, such as a parking lot?"}`
- Cite: [i8582] p. 3, Exceptions, "The rental of property is incidental to an activity of holding property for investment"; p. 4, "You customarily make the rental property available during defined business hours for nonexclusive use by various customers" (2025; sha256 76787e11)

## (helper) — `rental.business_incidental`

- **Authored helper label:** Rental incidental to a trade or business activity the filer owns an interest in (mainly used in it, gross rent under 2% of the smaller of unadjusted basis and value)
- **Encoded (Bool):** Input — Was it mainly used in a business you or your spouse owned a part of in 2025, in 2025 or in 2 of the 5 years before, with 2025 rent under 2% of the smaller of its cost and its value?
- Expr: `{"op":"input","source":"Was it mainly used in a business you or your spouse owned a part of in 2025, in 2025 or in 2 of the 5 years before, with 2025 rent under 2% of the smaller of its cost and its value?"}`
- Cite: [i8582] p. 3, Exceptions, "The rental of property is incidental to a trade or business activity if" (2025; sha256 76787e11)

## (helper) — `rental.is_land`

- **Authored helper label:** Land only (nothing on it subject to depreciation)
- **Encoded (Bool):** line 1b = 'land'
- Expr: `{"eq":["rental.kind",{"const":"land"}],"op":"test"}`
- Cite: [p925] p. 16, Rental of Nondepreciable Property, "less than 30% of the unadjusted basis of the property is subject to depreciation" (2025; sha256 dda751f0)

## (helper) — `rental.land_heavy`

- **Authored helper label:** Less than 30% of the unadjusted basis of the property subject to depreciation
- **Encoded (Bool):** Input — Was less than 30% of what it cost (before depreciation) for its buildings and other things that wear out, the rest being for the land?
- Expr: `{"op":"input","source":"Was less than 30% of what it cost (before depreciation) for its buildings and other things that wear out, the rest being for the land?"}`
- Cite: [p925] p. 16, Rental of Nondepreciable Property, "less than 30% of the unadjusted basis of the property is subject to depreciation" (2025; sha256 dda751f0)

## (gate) — `rental.land_heavy_if_built`

- **Authored helper label:** Less than 30% subject to depreciation, asked only when the property is not land only (false otherwise)
- **Encoded (Bool):** Choose — [helper "Land only (nothing on it subject to depreciation)" = false → helper "Less than 30% of the unadjusted basis of the property subject to depreciation"] [helper "Land only (nothing on it subject to depreciation)" = true → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.is_land",{"const":false}],"op":"test"},"then":"rental.land_heavy"},{"guard":{"eq":["rental.is_land",{"const":true}],"op":"test"},"then":"rental.no"}],"op":"choose"}`
- Cite: [p925] p. 16, Rental of Nondepreciable Property, "less than 30% of the unadjusted basis of the property is subject to depreciation" (2025; sha256 dda751f0)

## (helper) — `rental.at_risk_prior`

- **Authored helper label:** At-risk history (Form 6198 filed for it, or a loss held back as not at risk, on an earlier return)
- **Encoded (Bool):** Input — Was Form 6198 (at-risk limits) filed for it on any of your (or, on a joint return, your spouse's) earlier returns, or was a loss from it held back on one because amounts were not at risk?
- Expr: `{"op":"input","source":"Was Form 6198 (at-risk limits) filed for it on any of your (or, on a joint return, your spouse's) earlier returns, or was a loss from it held back on one because amounts were not at risk?"}`
- Cite: [p925] p. 19, At-Risk Limits, "You treat any loss that is disallowed because of the at-risk limits as a deduction from the same activity in the next tax year. If your losses from an at-risk activity are allowed, they’re subject to recapture in later years if your amount at risk is reduced below zero." (2025; sha256 dda751f0)

## (helper) — `rental.business_credit`

- **Authored helper label:** A general business credit (Form 3800) claimed for the rental
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) claim a business tax credit for 2025 for it (Form 3800), such as the low-income housing credit or the rehabilitation credit for an old building?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) claim a business tax credit for 2025 for it (Form 3800), such as the low-income housing credit or the rehabilitation credit for an old building?"}`
- Cite: [i1040gi] p. 116, Lines 6a Through 6z, "The general business credit consists of a number of credits that usually apply only to individuals who are partners, shareholders in an S corporation, self-employed, or who have rental property" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `rental.prerental`

- **Authored helper label:** First offered for rent in 2025, with costs paid before then
- **Encoded (Bool):** Input — Was it first offered for rent in 2025, and did you pay costs for it before then, to get it ready or find tenants, or, for a place you bought to rent, its other costs?
- Interpretation: amb.2025.rental_prerental_costs
- Expr: `{"op":"input","source":"Was it first offered for rent in 2025, and did you pay costs for it before then, to get it ready or find tenants, or, for a place you bought to rent, its other costs?"}`
- Cite: [p527] p. 5, Pre-rental expenses, "You can deduct your ordinary and necessary expenses for managing, conserving, or maintaining rental property from the time you make it available for rent" (2025; sha256 20c826e9)

## (helper) — `rental.vehicle`

- **Authored helper label:** Car, truck or travel expenses for the rental (line 6)
- **Encoded (Bool):** Input — Car, truck or travel costs for the rental
- Expr: `{"op":"input","source":"Car, truck or travel costs for the rental"}`
- Cite: [i1040se] p. 4, Line 6 (2025; sha256 ad71de35)

## (helper) — `rental.active`

- **Authored helper label:** Active participation
- **Encoded (Bool):** Input — Did you or your spouse help make decisions for it, such as approving tenants, setting the rent or approving repairs, even if a manager did the daily work?
- Expr: `{"op":"input","source":"Did you or your spouse help make decisions for it, such as approving tenants, setting the rent or approving repairs, even if a manager did the daily work?"}`
- Cite: [i1040se] p. 4, Active participation, "You can meet the active participation requirement without regular, continuous, and substantial involvement" (2025; sha256 ad71de35)

## (helper) — `rental.rents`

- **Authored helper label:** Rents and other rental income received (your share)
- **Encoded (NonNegDollars):** Input — Rent and other income from it in 2025 (your share), including advance rent, bills a tenant paid for you, and the value of goods or work you got in place of rent
- Expr: `{"op":"input","source":"Rent and other income from it in 2025 (your share), including advance rent, bills a tenant paid for you, and the value of goods or work you got in place of rent"}`
- Cite: [i1040se] p. 4, Line 3; p. 5, Line 3, "If you received services or property instead of money as rent, report the fair market value of the services or property as rental income on line 3" (2025; sha256 ad71de35)

## (helper) — `rental.has_advertising`

- **Authored helper label:** Advertising: any
- **Encoded (Bool):** Input — Advertising
- Expr: `{"op":"input","source":"Advertising"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.amt5`

- **Authored helper label:** Advertising paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Advertising for renters, paid in 2025 (your share)
- Expr: `{"op":"input","source":"Advertising for renters, paid in 2025 (your share)"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (gate) — `rental.amt5_if_any`

- **Authored helper label:** Advertising, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Advertising: any" = true → helper "Advertising paid in 2025, before any division for personal use"] [helper "Advertising: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_advertising",{"const":true}],"op":"test"},"then":"rental.amt5"},{"guard":{"eq":["rental.has_advertising",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## 5 — `rental.line5`

- **IRS:** Advertising
- **Encoded (NonNegDollars):** Enter the amount from helper "Advertising, asked only when ticked (zero otherwise)".
- Interpretation: amb.2025.rental_direct_expenses
- Expr: `{"from":"rental.amt5_if_any","op":"copy"}`
- Cite: [p527] p. 31, Line 2d, "Enter the total of your rental expenses that are directly related only to the rental activity" and "Also, include rental agency fees, advertising"; p. 29, Worksheet 5-1, line 2e, "Fully deductible rental expenses"; pp. 23-24, Renting Part of Property, "You don't have to divide the expenses that belong only to the rental part of your property" (a cost of the rental activity alone is taken whole, also when the unit had personal use) (2025; sha256 20c826e9)

## (helper) — `rental.has_cleaning`

- **Authored helper label:** Cleaning and maintenance: any
- **Encoded (Bool):** Input — Cleaning and maintenance
- Expr: `{"op":"input","source":"Cleaning and maintenance"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.amt7`

- **Authored helper label:** Cleaning and maintenance paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Cleaning and maintenance (not repairs), paid in 2025 (your share)
- Expr: `{"op":"input","source":"Cleaning and maintenance (not repairs), paid in 2025 (your share)"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (gate) — `rental.amt7_if_any`

- **Authored helper label:** Cleaning and maintenance, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Cleaning and maintenance: any" = true → helper "Cleaning and maintenance paid in 2025, before any division for personal use"] [helper "Cleaning and maintenance: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_cleaning",{"const":true}],"op":"test"},"then":"rental.amt7"},{"guard":{"eq":["rental.has_cleaning",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.div7`

- **Authored helper label:** Cleaning and maintenance: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Cleaning and maintenance, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt7_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 7 — `rental.line7`

- **IRS:** Cleaning and maintenance
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Cleaning and maintenance, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Cleaning and maintenance: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt7_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div7"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes" (2025; sha256 ad71de35)

## (helper) — `rental.has_commissions`

- **Authored helper label:** Commissions: any
- **Encoded (Bool):** Input — Commissions
- Expr: `{"op":"input","source":"Commissions"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.amt8`

- **Authored helper label:** Commissions paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Commissions paid, for example to an agent who found a renter, paid in 2025 (your share)
- Expr: `{"op":"input","source":"Commissions paid, for example to an agent who found a renter, paid in 2025 (your share)"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (gate) — `rental.amt8_if_any`

- **Authored helper label:** Commissions, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Commissions: any" = true → helper "Commissions paid in 2025, before any division for personal use"] [helper "Commissions: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_commissions",{"const":true}],"op":"test"},"then":"rental.amt8"},{"guard":{"eq":["rental.has_commissions",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## 8 — `rental.line8`

- **IRS:** Commissions
- **Encoded (NonNegDollars):** Enter the amount from helper "Commissions, asked only when ticked (zero otherwise)".
- Interpretation: amb.2025.rental_direct_expenses
- Expr: `{"from":"rental.amt8_if_any","op":"copy"}`
- Cite: [p527] p. 31, Line 2d, "Enter the total of your rental expenses that are directly related only to the rental activity" and "Also, include rental agency fees, advertising"; p. 29, Worksheet 5-1, line 2e, "Fully deductible rental expenses"; pp. 23-24, Renting Part of Property, "You don't have to divide the expenses that belong only to the rental part of your property" (a cost of the rental activity alone is taken whole, also when the unit had personal use) (2025; sha256 20c826e9)

## (helper) — `rental.has_insurance`

- **Authored helper label:** Insurance: any
- **Encoded (Bool):** Input — Insurance
- Expr: `{"op":"input","source":"Insurance"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.amt9`

- **Authored helper label:** Insurance for 2025 coverage, before any division for personal use
- **Encoded (NonNegDollars):** Input — Insurance on it for 2025 coverage, paid in 2025 or paid earlier for more than one year (only the part for 2025; your share)
- Expr: `{"op":"input","source":"Insurance on it for 2025 coverage, paid in 2025 or paid earlier for more than one year (only the part for 2025; your share)"}`
- Cite: [p527] p. 5, Insurance premiums paid in advance, "For each year of coverage, you can deduct only the part of the premium payment that applies to that year" (2025; sha256 20c826e9)

## (gate) — `rental.amt9_if_any`

- **Authored helper label:** Insurance, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Insurance: any" = true → helper "Insurance for 2025 coverage, before any division for personal use"] [helper "Insurance: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_insurance",{"const":true}],"op":"test"},"then":"rental.amt9"},{"guard":{"eq":["rental.has_insurance",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.div9`

- **Authored helper label:** Insurance: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Insurance, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt9_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 9 — `rental.line9`

- **IRS:** Insurance
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Insurance, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Insurance: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt9_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div9"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes" (2025; sha256 ad71de35)

## (helper) — `rental.has_legal`

- **Authored helper label:** Legal and other professional fees: any
- **Encoded (Bool):** Input — Legal and other professional fees
- Expr: `{"op":"input","source":"Legal and other professional fees"}`
- Cite: [i1040se] p. 6, Line 10 (2025; sha256 ad71de35)

## (helper) — `rental.amt10`

- **Authored helper label:** Legal and other professional fees paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Legal fees and other professional fees, such as tax preparation for the rental, paid in 2025 (your share)
- Expr: `{"op":"input","source":"Legal fees and other professional fees, such as tax preparation for the rental, paid in 2025 (your share)"}`
- Cite: [i1040se] p. 6, Line 10 (2025; sha256 ad71de35)

## (gate) — `rental.amt10_if_any`

- **Authored helper label:** Legal and other professional fees, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Legal and other professional fees: any" = true → helper "Legal and other professional fees paid in 2025, before any division for personal use"] [helper "Legal and other professional fees: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_legal",{"const":true}],"op":"test"},"then":"rental.amt10"},{"guard":{"eq":["rental.has_legal",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, Line 10 (2025; sha256 ad71de35)

## (helper) — `rental.div10`

- **Authored helper label:** Legal and other professional fees: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Legal and other professional fees, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt10_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 10 — `rental.line10`

- **IRS:** Legal and other professional fees
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Legal and other professional fees, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Legal and other professional fees: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt10_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div10"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes"; p. 6, Line 10, "Include on line 10 fees for tax advice and the preparation of tax forms related to your rental real estate or royalty properties" (2025; sha256 ad71de35)

## (helper) — `rental.has_management`

- **Authored helper label:** Management fees: any
- **Encoded (Bool):** Input — Management fees
- Expr: `{"op":"input","source":"Management fees"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.amt11`

- **Authored helper label:** Management fees paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Management fees, paid in 2025 (your share)
- Expr: `{"op":"input","source":"Management fees, paid in 2025 (your share)"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (gate) — `rental.amt11_if_any`

- **Authored helper label:** Management fees, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Management fees: any" = true → helper "Management fees paid in 2025, before any division for personal use"] [helper "Management fees: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_management",{"const":true}],"op":"test"},"then":"rental.amt11"},{"guard":{"eq":["rental.has_management",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.div11`

- **Authored helper label:** Management fees: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Management fees, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt11_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 11 — `rental.line11`

- **IRS:** Management fees
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Management fees, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Management fees: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt11_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div11"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes" (2025; sha256 ad71de35)

## (helper) — `rental.has_mortgage`

- **Authored helper label:** Mortgage interest paid to banks, etc.: any
- **Encoded (Bool):** Input — Mortgage interest paid to banks, etc.
- Expr: `{"op":"input","source":"Mortgage interest paid to banks, etc."}`
- Cite: [i1040se] p. 6, Lines 12 and 13 (2025; sha256 ad71de35)

## (helper) — `rental.amt12`

- **Authored helper label:** Mortgage interest paid to banks, etc. paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Mortgage interest on it shown on Form 1098 (box 1), your share, paid in 2025, leaving out interest on any part of the loan spent on something else
- Expr: `{"op":"input","source":"Mortgage interest on it shown on Form 1098 (box 1), your share, paid in 2025, leaving out interest on any part of the loan spent on something else"}`
- Cite: [i1040se] p. 6, Lines 12 and 13 (2025; sha256 ad71de35)

## (gate) — `rental.amt12_if_any`

- **Authored helper label:** Mortgage interest paid to banks, etc., asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Mortgage interest paid to banks, etc.: any" = true → helper "Mortgage interest paid to banks, etc. paid in 2025, before any division for personal use"] [helper "Mortgage interest paid to banks, etc.: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_mortgage",{"const":true}],"op":"test"},"then":"rental.amt12"},{"guard":{"eq":["rental.has_mortgage",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, Lines 12 and 13 (2025; sha256 ad71de35)

## (helper) — `rental.div12`

- **Authored helper label:** Mortgage interest paid to banks, etc.: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Mortgage interest paid to banks, etc., asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt12_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 12 — `rental.line12`

- **IRS:** Mortgage interest paid to banks, etc.
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Mortgage interest paid to banks, etc., asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Mortgage interest paid to banks, etc.: the rental part (rental days over total days of use)"]
- **Refusal:** when rental.mortgage_excess_if_mortgage is true, cannot complete Schedule E, line 12 (mortgage interest beyond Form 1098, with a statement). Mortgage interest beyond what Form 1098 shows needs a statement explaining the difference and is outside this tool. Cite: [i1040se] p. 7, Line 12, "If you paid more mortgage interest than is shown on your Form 1098 or similar statement" (2025; sha256 ad71de35)
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt12_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div12"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes"; p. 6, Lines 12 and 13, "In most cases, to determine the interest expense allocable to your rental activities, you must have records to show how the proceeds of each debt were used" (2025; sha256 ad71de35)

## (helper) — `rental.mortgage_excess`

- **Authored helper label:** Mortgage interest paid beyond the amount shown on Form 1098
- **Encoded (Bool):** Input — Did you pay more mortgage interest on it in 2025 than your Forms 1098 for it show in total?
- Interpretation: amb.2025.rental_points_on_1098_loan
- Expr: `{"op":"input","source":"Did you pay more mortgage interest on it in 2025 than your Forms 1098 for it show in total?"}`
- Cite: [i1040se] p. 7, Line 12, "If you paid more mortgage interest than is shown on your Form 1098 or similar statement" (2025; sha256 ad71de35)

## (gate) — `rental.mortgage_excess_if_mortgage`

- **Authored helper label:** Mortgage interest beyond Form 1098, asked only when there was mortgage interest (false otherwise)
- **Encoded (Bool):** Choose — [helper "Mortgage interest paid to banks, etc.: any" = true → helper "Mortgage interest paid beyond the amount shown on Form 1098"] [helper "Mortgage interest paid to banks, etc.: any" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_mortgage",{"const":true}],"op":"test"},"then":"rental.mortgage_excess"},{"guard":{"eq":["rental.has_mortgage",{"const":false}],"op":"test"},"then":"rental.no"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 12, "If you paid more mortgage interest than is shown on your Form 1098 or similar statement" (2025; sha256 ad71de35)

## (helper) — `rental.has_other_interest`

- **Authored helper label:** Other interest: any
- **Encoded (Bool):** Input — Other interest
- Expr: `{"op":"input","source":"Other interest"}`
- Cite: [i1040se] p. 6, Lines 12 and 13 (2025; sha256 ad71de35)

## (helper) — `rental.amt13`

- **Authored helper label:** Other interest paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Other interest paid in 2025 on money borrowed and spent on it (your share), such as a home equity loan on another home or a loan with no Form 1098 in your name; not interest for a later year; for points or loan fees, only 2025's share, spread evenly over the loan
- Expr: `{"op":"input","source":"Other interest paid in 2025 on money borrowed and spent on it (your share), such as a home equity loan on another home or a loan with no Form 1098 in your name; not interest for a later year; for points or loan fees, only 2025's share, spread evenly over the loan"}`
- Cite: [i1040se] p. 6, Lines 12 and 13 (2025; sha256 ad71de35)

## (gate) — `rental.amt13_if_any`

- **Authored helper label:** Other interest, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Other interest: any" = true → helper "Other interest paid in 2025, before any division for personal use"] [helper "Other interest: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_other_interest",{"const":true}],"op":"test"},"then":"rental.amt13"},{"guard":{"eq":["rental.has_other_interest",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, Lines 12 and 13 (2025; sha256 ad71de35)

## (helper) — `rental.div13`

- **Authored helper label:** Other interest: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Other interest, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt13_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 13 — `rental.line13`

- **IRS:** Other interest
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Other interest, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Other interest: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt13_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div13"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes"; p. 6, Lines 12 and 13, "In most cases, to determine the interest expense allocable to your rental activities, you must have records to show how the proceeds of each debt were used" (2025; sha256 ad71de35)

## (helper) — `rental.has_repairs`

- **Authored helper label:** Repairs: any
- **Encoded (Bool):** Input — Repairs
- Expr: `{"op":"input","source":"Repairs"}`
- Cite: [i1040se] p. 7, Line 14 (2025; sha256 ad71de35)

## (helper) — `rental.amt14`

- **Authored helper label:** Repairs paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Repairs (not improvements), paid in 2025 (your share)
- Expr: `{"op":"input","source":"Repairs (not improvements), paid in 2025 (your share)"}`
- Cite: [i1040se] p. 7, Line 14 (2025; sha256 ad71de35)

## (gate) — `rental.amt14_if_any`

- **Authored helper label:** Repairs, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Repairs: any" = true → helper "Repairs paid in 2025, before any division for personal use"] [helper "Repairs: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_repairs",{"const":true}],"op":"test"},"then":"rental.amt14"},{"guard":{"eq":["rental.has_repairs",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 14 (2025; sha256 ad71de35)

## (helper) — `rental.div14`

- **Authored helper label:** Repairs: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Repairs, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt14_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 14 — `rental.line14`

- **IRS:** Repairs
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Repairs, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Repairs: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt14_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div14"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes"; p. 7, Line 14, "You can deduct the amounts paid for repairs and maintenance" (2025; sha256 ad71de35)

## (helper) — `rental.has_supplies`

- **Authored helper label:** Supplies: any
- **Encoded (Bool):** Input — Supplies
- Expr: `{"op":"input","source":"Supplies"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.amt15`

- **Authored helper label:** Supplies paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Supplies, paid in 2025 (your share)
- Expr: `{"op":"input","source":"Supplies, paid in 2025 (your share)"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (gate) — `rental.amt15_if_any`

- **Authored helper label:** Supplies, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Supplies: any" = true → helper "Supplies paid in 2025, before any division for personal use"] [helper "Supplies: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_supplies",{"const":true}],"op":"test"},"then":"rental.amt15"},{"guard":{"eq":["rental.has_supplies",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, General Instructions for Lines 5 Through 21 (2025; sha256 ad71de35)

## (helper) — `rental.div15`

- **Authored helper label:** Supplies: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Supplies, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt15_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 15 — `rental.line15`

- **IRS:** Supplies
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Supplies, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Supplies: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt15_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div15"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes" (2025; sha256 ad71de35)

## (helper) — `rental.has_taxes`

- **Authored helper label:** Taxes: any
- **Encoded (Bool):** Input — Taxes
- Expr: `{"op":"input","source":"Taxes"}`
- Cite: [i1040se] p. 6, Line 16 (2025; sha256 ad71de35)

## (helper) — `rental.amt16`

- **Authored helper label:** Taxes paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Property tax and other taxes on it, paid in 2025 (your share), not charges for putting in streets, sidewalks, or water or sewer lines
- Expr: `{"op":"input","source":"Property tax and other taxes on it, paid in 2025 (your share), not charges for putting in streets, sidewalks, or water or sewer lines"}`
- Cite: [i1040se] p. 6, Line 16 (2025; sha256 ad71de35)

## (gate) — `rental.amt16_if_any`

- **Authored helper label:** Taxes, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Taxes: any" = true → helper "Taxes paid in 2025, before any division for personal use"] [helper "Taxes: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_taxes",{"const":true}],"op":"test"},"then":"rental.amt16"},{"guard":{"eq":["rental.has_taxes",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 6, Line 16 (2025; sha256 ad71de35)

## (helper) — `rental.div16`

- **Authored helper label:** Taxes: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Taxes, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt16_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 16 — `rental.line16`

- **IRS:** Taxes
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Taxes, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Taxes: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt16_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div16"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes" (2025; sha256 ad71de35)

## (helper) — `rental.tax_personal`

- **Authored helper label:** Subtract rental.line16 from rental.amt16_if_any (the taxes not taken on Schedule E, carried to Schedule A line 5b)
- **Encoded (NonNegDollars):** Subtract line 16 from helper "Taxes, asked only when ticked (zero otherwise)". If zero or less, enter -0-.
- Expr: `{"from":"rental.amt16_if_any","op":"subtract_floor0","take":"rental.line16"}`
- Cite: [p527] p. 25, Personal Use of Dwelling Unit (Including Vacation Home), "Only your rental expenses may be deducted on Schedule E (Form 1040). Some of your personal expenses may be deductible on Schedule A (Form 1040) if you itemize your deductions"; i1040sca p. 6, Line 5b, "Enter on line 5b the state and local taxes you paid on real estate you own that wasn't used for business" (2025; sha256 20c826e9)

## (helper) — `rental.has_utilities`

- **Authored helper label:** Utilities: any
- **Encoded (Bool):** Input — Utilities
- Expr: `{"op":"input","source":"Utilities"}`
- Cite: [i1040se] p. 7, Line 17 (2025; sha256 ad71de35)

## (helper) — `rental.amt17`

- **Authored helper label:** Utilities paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Utilities for it, paid in 2025 by you or by a tenant in place of rent (your share)
- Expr: `{"op":"input","source":"Utilities for it, paid in 2025 by you or by a tenant in place of rent (your share)"}`
- Cite: [i1040se] p. 7, Line 17 (2025; sha256 ad71de35)

## (gate) — `rental.amt17_if_any`

- **Authored helper label:** Utilities, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Utilities: any" = true → helper "Utilities paid in 2025, before any division for personal use"] [helper "Utilities: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_utilities",{"const":true}],"op":"test"},"then":"rental.amt17"},{"guard":{"eq":["rental.has_utilities",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 17 (2025; sha256 ad71de35)

## (helper) — `rental.div17`

- **Authored helper label:** Utilities: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Utilities, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt17_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 17 — `rental.line17`

- **IRS:** Utilities
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Utilities, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Utilities: the rental part (rental days over total days of use)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt17_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div17"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes"; p. 7, Line 17, "You can deduct the cost of ordinary and necessary telephone calls related to your rental activities or royalty income" (2025; sha256 ad71de35)

## (helper) — `rental.has_other`

- **Authored helper label:** Other: any
- **Encoded (Bool):** Input — Other
- Expr: `{"op":"input","source":"Other"}`
- Cite: [i1040se] p. 7, Line 19 (2025; sha256 ad71de35)

## (helper) — `rental.amt19`

- **Authored helper label:** Other paid in 2025, before any division for personal use
- **Encoded (NonNegDollars):** Input — Other costs of renting it (not depreciation), paid in 2025 (your share)
- Expr: `{"op":"input","source":"Other costs of renting it (not depreciation), paid in 2025 (your share)"}`
- Cite: [i1040se] p. 7, Line 19 (2025; sha256 ad71de35)

## (gate) — `rental.amt19_if_any`

- **Authored helper label:** Other, asked only when ticked (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Other: any" = true → helper "Other paid in 2025, before any division for personal use"] [helper "Other: any" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.has_other",{"const":true}],"op":"test"},"then":"rental.amt19"},{"guard":{"eq":["rental.has_other",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 19 (2025; sha256 ad71de35)

## (helper) — `rental.div19`

- **Authored helper label:** Other: the rental part (rental days over total days of use)
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Other, asked only when ticked (zero otherwise)" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.amt19_if_any","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose"; p. 26, "Any day that the unit is rented at a fair rental price is a", "The total use of the cottage was 99 days" (2025; sha256 20c826e9)

## 19 — `rental.line19`

- **IRS:** Other
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Other, asked only when ticked (zero otherwise)"] [helper "Any day of personal use in 2025" = true → helper "Other: the rental part (rental days over total days of use)"]
- **Refusal:** when rental.bought_lease is true, cannot complete Schedule E, line 19 (cost of a leasehold bought for rental purposes). The cost of a lease you bought, which is spread over the lease's term, is outside this tool. Cite: [p527] p. 5, Rental of property, "If you buy a leasehold for rental purposes, you can deduct an equal part of the cost each year over the term of the lease" (2025; sha256 20c826e9)
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.amt19_if_any"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div19"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "If you rented out a dwelling unit that you also used for personal purposes"; p. 7, Line 19, "Enter on line 19 any ordinary and necessary expenses not listed on lines 5 through 18" (2025; sha256 ad71de35)

## (helper) — `rental.bought_lease`

- **Authored helper label:** Cost of buying a leasehold for rental purposes
- **Encoded (Bool):** Input — Did you pay, in 2025 or earlier, to buy a lease on it, or on the land under it, that you held at any time in 2025, for renting it out (a leasehold)?
- Expr: `{"op":"input","source":"Did you pay, in 2025 or earlier, to buy a lease on it, or on the land under it, that you held at any time in 2025, for renting it out (a leasehold)?"}`
- Cite: [p527] p. 5, Rental of property, "If you buy a leasehold for rental purposes, you can deduct an equal part of the cost each year over the term of the lease" (2025; sha256 20c826e9)

## (helper) — `rental.dep_full`

- **Authored helper label:** Depreciation of the buildings and improvements, before any division for personal use
- **Encoded (NonNegDollars):** Add rprop.dep over every confirmed rprop entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rprop","field":"rprop.dep","op":"sum_over"}`
- Cite: [i1040se] p. 6, Line 18 (2025; sha256 ad71de35)

## (helper) — `rental.div18`

- **Authored helper label:** Depreciation: the rental part
- **Encoded (NonNegDollars):** Divide helper "Fair rental days (as cents)" by helper "Total days of use: rental days plus personal use days not also rental days (as cents)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Depreciation of the buildings and improvements, before any division for personal use" by the result.
- Interpretation: amb.2025.rental_use_ratio_places
- Expr: `{"amount":"rental.dep_full","op":"prorate","part":"rental.fair_c","places":6,"whole":"rental.total_c"}`
- Cite: [p527] p. 25, Dividing Expenses, "divide your expenses between the rental use and the personal use based on the number of days used for each purpose" (2025; sha256 20c826e9)

## 18 — `rental.line18`

- **IRS:** Depreciation expense or depletion
- **Encoded (NonNegDollars):** Choose — [helper "Any day of personal use in 2025" = false → helper "Depreciation of the buildings and improvements, before any division for personal use"] [helper "Any day of personal use in 2025" = true → helper "Depreciation: the rental part"]
- Interpretation: amb.2025.rental_prior_depreciation_tables
- Expr: `{"alternatives":[{"guard":{"eq":["rental.personal_any",{"const":false}],"op":"test"},"then":"rental.dep_full"},{"guard":{"eq":["rental.personal_any",{"const":true}],"op":"test"},"then":"rental.div18"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 18, "Depreciation is the annual deduction you must take to recover the cost or other basis of business or investment property" (2025; sha256 ad71de35)

## 20 — `rental.line20`

- **IRS:** Total expenses. Add lines 5 through 19
- **Encoded (NonNegDollars):** Add line 5, line 7, line 8, line 9, line 10, line 11, line 12, line 13, line 14, line 15, line 16, line 17, line 18, and line 19.
- Expr: `{"of":["rental.line5","rental.line7","rental.line8","rental.line9","rental.line10","rental.line11","rental.line12","rental.line13","rental.line14","rental.line15","rental.line16","rental.line17","rental.line18","rental.line19"],"op":"sum"}`
- Cite: [f1040se] Schedule E (2025), line 20 (2025; sha256 c5e2c8fa)

## (helper) — `rental.line21_full`

- **Authored helper label:** Rents less total expenses
- **Encoded (Dollars):** Subtract line 20 from helper "Rents and other rental income received (your share)".
- **Refusal:** when rental.self_rental is true, cannot complete Schedule E, Part I, property type 7 or 8 (self-rental or other). Property rented to a business you or your spouse run, and property of another type, are outside this tool. Cite: [i1040se] p. 5, Self-rental (2025; sha256 ad71de35)
- **Refusal:** when rental.stay7_if_short is true, cannot complete Schedule C or Schedule E with Form 8582 (not a rental activity: average stay of 7 days or less). A rental whose average stay is 7 days or less is not a rental activity under the passive activity rules and is outside this tool. Cite: [i8582] p. 3, Exceptions, "Figure the average period of customer use for a class of property by dividing the total number of days in all rental periods by the number of rentals" (2025; sha256 76787e11)
- **Refusal:** when rental.services is true, cannot complete Schedule C (rental with significant services). A rental where you provide significant services, such as maid service, is reported on Schedule C; this tool does not prepare it. Cite: [i1040se] p. 5, Line 3, "If you provided significant services to the renter" (2025; sha256 ad71de35)
- **Refusal:** when rental.under_tenth is true, cannot complete Form 8582, Part V (ownership of less than 10%). A rental you own less than 10% of is outside this tool. Cite: [i8582] p. 4, Active participation, "in the activity was less than 10% (by value) of all interests in the activity" (2025; sha256 76787e11)
- **Refusal:** when rental.not_for_profit is true, cannot complete Not rented for profit (Schedule 1, line 8l and Schedule A). Property not rented for profit is reported differently and is outside this tool. Cite: [p527] p. 17, Not Rented for Profit (2025; sha256 20c826e9)
- **Refusal:** when rental.depletion is true, cannot complete Schedule E, line 18 (depletion). Depletion is outside this tool. Cite: [i1040se] p. 6, Line 18, "Depletion" (2025; sha256 ad71de35)
- **Refusal:** when rental.part_home is true, cannot complete Schedule E, Part I (rental of part of a property you also live in). Renting out part of a home or building you also live in, such as a room, is outside this tool. Cite: [i1040se] p. 6, Renting out part of your home (2025; sha256 ad71de35)
- **Refusal:** when rental.held_for_sale is true, cannot complete Form 8582 exceptions, or Schedule C (property held mainly for sale, or offered in business hours to many customers). Property held mainly to sell, as an investment or by a real estate dealer, and property offered during business hours to many customers may not be a rental activity, and are outside this tool. Cite: [i8582] p. 3, Exceptions, "The rental of property is incidental to an activity of holding property for investment"; i1040se p. 6, "Do not use Schedule E to report income and expenses from rentals of real estate you held for sale to customers in the ordinary course of your business as a real estate dealer" (2025; sha256 76787e11)
- **Refusal:** when rental.business_incidental is true, cannot complete Form 8582 exceptions (rental incidental to a trade or business). Property mainly used in a business you or your spouse own, and rented for under 2% of its cost or value, is not a rental activity under the passive activity rules and is outside this tool. Cite: [i8582] p. 3, Exceptions, "The rental of property is incidental to a trade or business activity if" (2025; sha256 76787e11)
- **Refusal:** when rental.at_risk_prior is true, cannot complete Form 6198 (at-risk limits, earlier year). A rental with Form 6198 on an earlier return, or a loss held back because amounts were not at risk, can carry that loss into 2025 or owe recapture of losses allowed before; this tool does not prepare Form 6198. Cite: [p925] p. 19, At-Risk Limits, "You treat any loss that is disallowed because of the at-risk limits as a deduction from the same activity in the next tax year" (2025; sha256 dda751f0)
- **Refusal:** when rental.business_credit is true, cannot complete Form 3800 (general business credit). A business credit for a rental (Form 3800) goes on Schedule 3 line 6a; this tool does not prepare it. To go on without the credit, answer No to that question. Cite: [i1040gi] p. 116, Lines 6a Through 6z, "See Form 3800 or Pub. 334" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when rental.prerental is true, cannot complete Costs paid before a rental was first offered for rent. Costs paid before a property is first offered for rent are not rental expenses of that time; depending on what they are, they are added to its cost, amortized as start-up costs on Form 4562, or not deducted, which this tool does not sort out. Cite: [p527] p. 5, Pre-rental expenses, "You can deduct your ordinary and necessary expenses for managing, conserving, or maintaining rental property from the time you make it available for rent"; i4562 p. 18, Startup and organizational costs, "Business startup costs (section 195)" (2025; sha256 20c826e9)
- **Refusal:** when rental.vehicle is true, cannot complete Schedule E, line 6 (auto and travel). Car, truck and travel expenses of a rental are outside this tool. Cite: [i1040se] p. 4, Line 6 (2025; sha256 ad71de35)
- **Refusal:** when rental.ws51 is true, cannot complete Pub. 527, Worksheet 5-1 (dwelling unit used as a home). A home you also lived in or used for more than the greater of 14 days or 10% of the days rented, and rented 15 days or more, is outside this tool. Cite: [p527] p. 28, Used as a home and rented 15 days or more (2025; sha256 20c826e9)
- Expr: `{"from":"rental.rents","op":"subtract","take":"rental.line20"}`
- Cite: [f1040se] Schedule E (2025), line 21, "Subtract line 20 from line 3 (rents)" (2025; sha256 c5e2c8fa)

## 3 — `rental.line3`

- **IRS:** Rents received
- **Encoded (NonNegDollars):** Choose — [helper "Used as a home and rented fewer than 15 days: not reported" = true → helper "Zero"] [helper "Used as a home and rented fewer than 15 days: not reported" = false → helper "Rents and other rental income received (your share)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.excluded",{"const":true}],"op":"test"},"then":"rental.zero"},{"guard":{"eq":["rental.excluded",{"const":false}],"op":"test"},"then":"rental.rents"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "do not report the rental income and do not deduct any rental expenses" (2025; sha256 ad71de35)

## 21 — `rental.line21`

- **IRS:** Subtract line 20 from line 3 (rents)
- **Encoded (Dollars):** Choose — [helper "Used as a home and rented fewer than 15 days: not reported" = true → helper "Zero"] [helper "Used as a home and rented fewer than 15 days: not reported" = false → helper "Rents less total expenses"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.excluded",{"const":true}],"op":"test"},"then":"rental.zero"},{"guard":{"eq":["rental.excluded",{"const":false}],"op":"test"},"then":"rental.line21_full"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Line 2, "do not report the rental income and do not deduct any rental expenses"; p. 7, Line 21, "If you have amounts for which you are not at risk, use Form 6198 to determine the amount of your deductible loss" (2025; sha256 ad71de35)

## IV/V (a) — `rental.net_income`

- **IRS:** Current year net income
- **Encoded (NonNegDollars):** Subtract helper "Zero" from line 21. If zero or less, enter -0-.
- Expr: `{"from":"rental.line21","op":"subtract_floor0","take":"rental.zero"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## IV/V (b) — `rental.net_loss`

- **IRS:** Current year net loss
- **Encoded (NonNegDollars):** Subtract line 21 from helper "Zero". If zero or less, enter -0-.
- Expr: `{"from":"rental.zero","op":"subtract_floor0","take":"rental.line21"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `rental.prior_any`

- **Authored helper label:** A loss from this rental held back on the 2024 return
- **Encoded (Bool):** Input — Was a loss from this rental held back (not deducted) on any of your (or, on a joint return, your spouse's) earlier returns, even a separate one?
- Expr: `{"op":"input","source":"Was a loss from this rental held back (not deducted) on any of your (or, on a joint return, your spouse's) earlier returns, even a separate one?"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `rental.prior_amt`

- **Authored helper label:** Prior years unallowed loss
- **Encoded (NonNegDollars):** Input — The loss held back for this rental, from your 2024 Form 8582, Part VII, column (c)
- Expr: `{"op":"input","source":"The loss held back for this rental, from your 2024 Form 8582, Part VII, column (c)"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `rental.prior_amt_if_any`

- **Authored helper label:** Prior years unallowed loss, asked only when a loss was held back (zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "A loss from this rental held back on the 2024 return" = true → helper "Prior years unallowed loss"] [helper "A loss from this rental held back on the 2024 return" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.prior_any",{"const":true}],"op":"test"},"then":"rental.prior_amt"},{"guard":{"eq":["rental.prior_any",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (helper) — `rental.prior_ws51`

- **Authored helper label:** Part of the carryover is expenses carried over from a year the filer also used it as a home (Worksheet 5-1)
- **Encoded (Bool):** Input — Did any of the held-back loss come from rental costs carried over from an earlier year when the place counted as your home through personal use (by you, a co-owner, a relative, or anyone paying below a fair rent) (Pub. 527, Worksheet 5-1)?
- Expr: `{"op":"input","source":"Did any of the held-back loss come from rental costs carried over from an earlier year when the place counted as your home through personal use (by you, a co-owner, a relative, or anyone paying below a fair rent) (Pub. 527, Worksheet 5-1)?"}`
- Cite: [p527] p. 28, "The excess expenses that can’t be used to offset income from other sources are carried forward to the next year and treated as rental expenses for the same property" (2025; sha256 20c826e9)

## (gate) — `rental.prior_ws51_if_any`

- **Authored helper label:** Asked only when a loss or cost was carried over (false otherwise)
- **Encoded (Bool):** Choose — [helper "A loss from this rental held back on the 2024 return" = true → helper "Part of the carryover is expenses carried over from a year the filer also used it as a home (Worksheet 5-1)"] [helper "A loss from this rental held back on the 2024 return" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.prior_any",{"const":true}],"op":"test"},"then":"rental.prior_ws51"},{"guard":{"eq":["rental.prior_any",{"const":false}],"op":"test"},"then":"rental.no"}],"op":"choose"}`
- Cite: [p527] p. 28, Used as a home and rented 15 days or more (2025; sha256 20c826e9)

## (helper) — `rental.prior_not_active`

- **Authored helper label:** Part of the held-back loss arose in a year without active participation
- **Encoded (Bool):** Input — Did any of that held-back loss come from a year when neither you nor your spouse helped make its decisions, or when you and your spouse together owned under 10% of it at some time?
- Expr: `{"op":"input","source":"Did any of that held-back loss come from a year when neither you nor your spouse helped make its decisions, or when you and your spouse together owned under 10% of it at some time?"}`
- Cite: [i8582] p. 10, Part IV, "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year" (2025; sha256 76787e11)

## (gate) — `rental.prior_not_active_if_both`

- **Authored helper label:** Asked only of an actively managed rental with a held-back loss (false otherwise)
- **Encoded (Bool):** Choose — [helper "A held-back loss on a rental with active participation" = true → helper "Part of the held-back loss arose in a year without active participation"] [helper "A held-back loss on a rental with active participation" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.prior_and_active",{"const":true}],"op":"test"},"then":"rental.prior_not_active"},{"guard":{"eq":["rental.prior_and_active",{"const":false}],"op":"test"},"then":"rental.no"}],"op":"choose"}`
- Cite: [i8582] p. 4, Part IV (2025; sha256 76787e11)

## (helper) — `rental.prior_and_active`

- **Authored helper label:** A held-back loss on a rental with active participation
- **Encoded (Bool):** helper "A loss from this rental held back on the 2024 return" = true and helper "Active participation" = true
- Expr: `{"all":[{"eq":["rental.prior_any",{"const":true}],"op":"test"},{"eq":["rental.active",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 4, Part IV (2025; sha256 76787e11)

## IV/V (c) — `rental.prior_loss`

- **IRS:** Prior years unallowed loss
- **Encoded (NonNegDollars):** Choose — [helper "The property is reported on Schedule E (not excluded)" = true → helper "Prior years unallowed loss, asked only when a loss was held back (zero otherwise)"] [helper "The property is reported on Schedule E (not excluded)" = false → helper "Zero"]
- **Refusal:** when rental.prior_not_active_if_both is true, cannot complete Form 8582, Part IV and Part V (prior-year loss from a year without active participation). A held-back loss from a year in which you did not actively participate is outside this tool. Cite: [i8582] p. 4, Part IV (2025; sha256 76787e11)
- **Refusal:** when rental.prior_ws51_if_any is true, cannot complete Pub. 527, Worksheet 5-1 (expenses carried over from a year of home use). Rental costs carried over from an earlier year's Worksheet 5-1, when the place counted as your home, are outside this tool. Cite: [p527] p. 28, "This limitation will apply to expenses carried forward to another year even if you don’t use the property as your home for that subsequent year" (2025; sha256 20c826e9)
- Expr: `{"alternatives":[{"guard":{"eq":["rental.reported",{"const":true}],"op":"test"},"then":"rental.prior_amt_if_any"},{"guard":{"eq":["rental.reported",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i8582] p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" (2025; sha256 76787e11)

## (gate) — `rental.part4`

- **Authored helper label:** Actively participated, and not a separate filer who lived with the spouse: Part IV (otherwise Part V)
- **Encoded (Bool):** helper "Active participation" = true and f8582 helper "Married filing separately, and you lived with your spouse at some time in 2025" = false
- Expr: `{"all":[{"eq":["rental.active",{"const":true}],"op":"test"},{"eq":["f8582.mfs_together",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV"; p. 10, Part IV, Caution, "Married individuals who file separate returns and lived with their spouses at any time during the tax year don't qualify under the active participation rule and must use Part V instead of Part IV." (2025; sha256 76787e11)

## (helper) — `rental.loss_sum`

- **Authored helper label:** Net loss plus prior years unallowed loss
- **Encoded (NonNegDollars):** Add line IV/V (b) and line IV/V (c).
- Expr: `{"of":["rental.net_loss","rental.prior_loss"],"op":"sum"}`
- Cite: [i8582] p. 13, Part VIII—Allowed Losses, "enter the net loss plus the prior-year unallowed loss for the activity" (2025; sha256 76787e11)

## IV/V (e) — `rental.overall_loss`

- **IRS:** Overall loss
- **Encoded (NonNegDollars):** Subtract line IV/V (a) from helper "Net loss plus prior years unallowed loss". If zero or less, enter -0-.
- Expr: `{"from":"rental.loss_sum","op":"subtract_floor0","take":"rental.net_income"}`
- Cite: [i8582] p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity" (2025; sha256 76787e11)

## VI (a) — `rental.p6_loss`

- **IRS:** Part VI: overall loss of an activity with active participation
- **Encoded (NonNegDollars):** Choose — [helper "Actively participated, and not a separate filer who lived with the spouse: Part IV (otherwise Part V)" = true → line IV/V (e)] [helper "Actively participated, and not a separate filer who lived with the spouse: Part IV (otherwise Part V)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.part4",{"const":true}],"op":"test"},"then":"rental.overall_loss"},{"guard":{"eq":["rental.part4",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i8582] p. 12, Part VI, "Enter the overall loss from column (e) of Part IV for each activity" (2025; sha256 76787e11)

## VI (c) — `rental.p6c`

- **IRS:** Part VI: special allowance
- **Encoded (NonNegDollars):** Choose — [helper "Part VI applies to this activity: an overall loss in Part IV and an amount on line 9" = true → helper "Part VI: line 9 times this activity’s ratio"] [helper "Part VI applies to this activity: an overall loss in Part IV and an amount on line 9" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.p6_on",{"const":true}],"op":"test"},"then":"rental.p6c_share"},{"guard":{"eq":["rental.p6_on",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i8582] p. 12, Part VI, "Multiply each ratio in column (b) by the amount on Part II, line 9" (2025; sha256 76787e11)

## (helper) — `rental.p6_on`

- **Authored helper label:** Part VI applies to this activity: an overall loss in Part IV and an amount on line 9
- **Encoded (Bool):** line VI (a) > $0 and f8582 line 9 > $0
- Expr: `{"all":[{"gt":["rental.p6_loss",{"const":0}],"op":"test"},{"gt":["f8582.line9",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 12, Part VI, "Use Part VI to allocate the special allowance on Part II, line 9" (2025; sha256 76787e11)

## (helper) — `rental.p6c_share`

- **Authored helper label:** Part VI: line 9 times this activity’s ratio
- **Encoded (NonNegDollars):** Divide line VI (a) by f8582 line VI (a) total, rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply f8582 line 9 by the result.
- Interpretation: amb.2025.f8582_ratio_places
- Expr: `{"amount":"f8582.line9","op":"prorate","part":"rental.p6_loss","places":6,"whole":"f8582.p6_total"}`
- Cite: [i8582] p. 12, Part VI, "Divide each of the individual losses shown in column (a) by the total of all the losses in column (a)" (2025; sha256 76787e11)

## VII (a) — `rental.p7a`

- **IRS:** Part VII: loss (Part VI column (d), or Part V column (e))
- **Encoded (NonNegDollars):** Subtract line VI (c) from line IV/V (e). If zero or less, enter -0-.
- Expr: `{"from":"rental.overall_loss","op":"subtract_floor0","take":"rental.p6c"}`
- Cite: [i8582] p. 12, Part VII—Allocation of Unallowed Losses (2025; sha256 76787e11)

## VII (c) — `rental.p7c`

- **IRS:** Part VII: unallowed loss
- **Encoded (NonNegDollars):** Choose — [helper "Part VII applies to this activity: a loss in Part VII column (a) and an unallowed amount on line C" = true → helper "Part VII: line C times this activity’s ratio"] [helper "Part VII applies to this activity: a loss in Part VII column (a) and an unallowed amount on line C" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.p7_on",{"const":true}],"op":"test"},"then":"rental.p7c_share"},{"guard":{"eq":["rental.p7_on",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i8582] p. 13, Column (c), "Multiply each ratio in column (b) by the amount on line C above" (2025; sha256 76787e11)

## (helper) — `rental.p7_on`

- **Authored helper label:** Part VII applies to this activity: a loss in Part VII column (a) and an unallowed amount on line C
- **Encoded (Bool):** line VII (a) > $0 and f8582 line VII worksheet C > $0
- Expr: `{"all":[{"gt":["rental.p7a",{"const":0}],"op":"test"},{"gt":["f8582.p7_C",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i8582] p. 12, Part VII—Allocation of Unallowed Losses (2025; sha256 76787e11)

## (helper) — `rental.p7c_share`

- **Authored helper label:** Part VII: line C times this activity’s ratio
- **Encoded (NonNegDollars):** Divide line VII (a) by f8582 line VII (a) total, rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply f8582 line VII worksheet C by the result.
- Interpretation: amb.2025.f8582_ratio_places
- Expr: `{"amount":"f8582.p7_C","op":"prorate","part":"rental.p7a","places":6,"whole":"f8582.p7_total"}`
- Cite: [i8582] p. 13, Column (c), "Subtract line B from line A" (2025; sha256 76787e11)

## (helper) — `rental.loss_after_p7`

- **Authored helper label:** Loss with prior-year unallowed loss, less the Part VII unallowed loss (the loss line 22 reports)
- **Encoded (NonNegDollars):** Subtract line VII (c) from helper "Net loss plus prior years unallowed loss". If zero or less, enter -0-.
- Expr: `{"from":"rental.loss_sum","op":"subtract_floor0","take":"rental.p7c"}`
- Cite: [i8582] p. 13, Part VIII—Allowed Losses, "Subtract column (b) from column (a)" (2025; sha256 76787e11)

## (helper) — `rental.p7_listed`

- **Authored helper label:** Listed in Part VII: a loss in Part VII column (a)
- **Encoded (Bool):** line VII (a) > $0
- Expr: `{"gt":["rental.p7a",{"const":0}],"op":"test"}`
- Cite: [i8582] p. 12, Part VII, "Complete Part VII if any activities have an overall loss in column (e) of Part V or losses in column (d) of Part VI" (2025; sha256 76787e11)

## VIII (c) — `rental.allowed`

- **IRS:** Part VIII: loss allowed (only for an activity listed in Part VII, a loss in its column (a); zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Listed in Part VII: a loss in Part VII column (a)" = true → helper "Loss with prior-year unallowed loss, less the Part VII unallowed loss (the loss line 22 reports)"] [helper "Listed in Part VII: a loss in Part VII column (a)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.p7_listed",{"const":true}],"op":"test"},"then":"rental.loss_after_p7"},{"guard":{"eq":["rental.p7_listed",{"const":false}],"op":"test"},"then":"rental.zero"}],"op":"choose"}`
- Cite: [i8582] p. 13, Part VIII—Allowed Losses, "Use Part VIII for any activity listed in Part VII"; p. 12, Part VII, "Complete Part VII if any activities have an overall loss in column (e) of Part V or losses in column (d) of Part VI", so an activity with no loss in Part VII column (a) has no Part VIII entry (2025; sha256 76787e11)

## VIII (b) — `rental.carryforward`

- **IRS:** Unallowed loss carried to 2026
- **Encoded (NonNegDollars):** Enter the amount from line VII (c).
- Expr: `{"from":"rental.p7c","op":"copy"}`
- Cite: [i8582] p. 13, Part VIII—Allowed Losses, "Keep a record of these amounts so the losses can be used to figure your PAL next year" (2025; sha256 76787e11)

## (helper) — `rental.not_at_risk`

- **Authored helper label:** Some investment not at risk
- **Encoded (Bool):** Input — Is any money you put in, or any debt on it, owed by no one personally (other than a mortgage on it from a bank, government or other regular lender), protected from loss by a guarantee, stop-loss or similar arrangement, or lent by someone with a stake in it?
- Expr: `{"op":"input","source":"Is any money you put in, or any debt on it, owed by no one personally (other than a mortgage on it from a bank, government or other regular lender), protected from loss by a guarantee, stop-loss or similar arrangement, or lent by someone with a stake in it?"}`
- Cite: [i1040se] p. 3, At-Risk Rules, "In most cases, you are not at risk for amounts such as the following", and Qualified nonrecourse financing (2025; sha256 ad71de35)

## (gate) — `rental.not_at_risk_if_reported`

- **Authored helper label:** Asked of every rental reported on Schedule E, in a year with a loss or with income (false otherwise)
- **Encoded (Bool):** Choose — [helper "The property is reported on Schedule E (not excluded)" = true → helper "Some investment not at risk"] [helper "The property is reported on Schedule E (not excluded)" = false → helper "No (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rental.reported",{"const":true}],"op":"test"},"then":"rental.not_at_risk"},{"guard":{"eq":["rental.reported",{"const":false}],"op":"test"},"then":"rental.no"}],"op":"choose"}`
- Cite: [i1040se] p. 7, Line 21, "If you have amounts for which you are not at risk, use Form 6198 to determine the amount of your deductible loss" (2025; sha256 ad71de35)

## (helper) — `rental.nondep`

- **Authored helper label:** Rental of nondepreciable property: land only, or less than 30% of the unadjusted basis subject to depreciation
- **Encoded (Bool):** (helper "Land only (nothing on it subject to depreciation)" = true or helper "Less than 30% subject to depreciation, asked only when the property is not land only (false otherwise)" = true)
- Expr: `{"any":[{"eq":["rental.is_land",{"const":true}],"op":"test"},{"eq":["rental.land_heavy_if_built",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p925] p. 16, Rental of Nondepreciable Property, "less than 30% of the unadjusted basis of the property is subject to depreciation" (2025; sha256 dda751f0)

## (helper) — `rental.nondep_gain`

- **Authored helper label:** Net passive income including prior-year unallowed losses (net income less the prior years unallowed loss)
- **Encoded (NonNegDollars):** Subtract line IV/V (c) from line IV/V (a). If zero or less, enter -0-.
- Expr: `{"from":"rental.net_income","op":"subtract_floor0","take":"rental.prior_loss"}`
- Cite: [p925] p. 16, Rental of Nondepreciable Property, "If you have net passive income (including prior-year unallowed losses) from renting property in a rental activity" (2025; sha256 dda751f0)

## (gate) — `rental.nondep_income`

- **Authored helper label:** Net passive income from a rental of nondepreciable property, recharacterized as nonpassive, on a return that must file Form 8582
- **Encoded (Bool):** helper "Rental of nondepreciable property: land only, or less than 30% of the unadjusted basis subject to depreciation" = true and helper "Net passive income including prior-year unallowed losses (net income less the prior years unallowed loss)" > $0 and f8582 helper "Form 8582 must be filed" = true
- Expr: `{"all":[{"eq":["rental.nondep",{"const":true}],"op":"test"},{"gt":["rental.nondep_gain",{"const":0}],"op":"test"},{"eq":["f8582.required",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p925] p. 15, Recharacterization of Passive Income, "If the result is net income, don’t enter any of the income or losses from the activity or property on Form 8582 or its separate parts, as they are recharacterized as nonpassive"; p. 16, Rental of Nondepreciable Property (2025; sha256 dda751f0)

## 22 — `rental.line22`

- **IRS:** Deductible rental real estate loss after limitation, if any, on Form 8582
- **Encoded (Dollars):** Subtract helper "Loss with prior-year unallowed loss, less the Part VII unallowed loss (the loss line 22 reports)" from helper "Zero".
- **Refusal:** when rental.not_at_risk_if_reported is true, cannot complete Form 6198 (at-risk limits). A rental with an amount not at risk is outside this tool, in a year with a loss and in a year with income (when the amount at risk falls below zero, losses deducted earlier are recaptured). Cite: [i1040se] p. 2, At-Risk Rules; p925 p. 19, At-Risk Limits, "If your losses from an at-risk activity are allowed, they’re subject to recapture in later years if your amount at risk is reduced below zero" (2025; sha256 ad71de35)
- **Refusal:** when rental.nondep_income is true, cannot complete Form 8582 (rental of nondepreciable property, income recharacterized as nonpassive). Net income from renting land, or property whose buildings were under 30% of its cost, is treated as nonpassive when Form 8582 limits other losses, and is outside this tool. Cite: [p925] p. 16, Rental of Nondepreciable Property, "less than 30% of the unadjusted basis of the property is subject to depreciation" (2025; sha256 dda751f0)
- Expr: `{"from":"rental.zero","op":"subtract","take":"rental.loss_after_p7"}`
- Cite: [i1040se] p. 8, Line 22 (2025; sha256 ad71de35)

## (helper) — `rental.dep_prior`

- **Authored helper label:** MACRS on buildings placed in service before 2025
- **Encoded (NonNegDollars):** Add rprop.dep over every confirmed rprop entry for which helper "Placed in service in 2025" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rprop","field":"rprop.dep","op":"sum_over","where":{"eq":["rprop.placed_this_year",{"const":false}],"op":"test"}}`
- Cite: [i4562] p. 9, Line 17 (2025; sha256 5c1c95b7)

## (helper) — `rental.dep_res25`

- **Authored helper label:** MACRS on residential rental property placed in service in 2025
- **Encoded (NonNegDollars):** Add rprop.dep over every confirmed rprop entry for which helper "Placed in service in 2025" = true and column (a) = 'residential', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rprop","field":"rprop.dep","op":"sum_over","where":{"all":[{"eq":["rprop.placed_this_year",{"const":true}],"op":"test"},{"eq":["rprop.kind",{"const":"residential"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] p. 9, Lines 19a Through 19j (2025; sha256 5c1c95b7)

## (helper) — `rental.dep_non25`

- **Authored helper label:** MACRS on nonresidential real property placed in service in 2025
- **Encoded (NonNegDollars):** Add rprop.dep over every confirmed rprop entry for which helper "Placed in service in 2025" = true and column (a) = 'nonresidential', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rprop","field":"rprop.dep","op":"sum_over","where":{"all":[{"eq":["rprop.placed_this_year",{"const":true}],"op":"test"},{"eq":["rprop.kind",{"const":"nonresidential"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] p. 9, Lines 19a Through 19j (2025; sha256 5c1c95b7)

## (helper) — `rental.count25`

- **Authored helper label:** Buildings or improvements placed in service in 2025, one cent each
- **Encoded (NonNegDollars):** Add rprop.placed_this_year_cent over every confirmed rprop entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"rprop","field":"rprop.placed_this_year_cent","op":"sum_over"}`
- Cite: [i1040se] p. 7, Line 18, "You must complete and attach Form 4562 only if" (2025; sha256 ad71de35)

## (helper) — `rental.needs_4562`

- **Authored helper label:** Form 4562 is needed for this property
- **Encoded (Bool):** helper "Buildings or improvements placed in service in 2025, one cent each" > $0
- Expr: `{"gt":["rental.count25",{"const":0}],"op":"test"}`
- Cite: [i1040se] p. 7, Line 18, "You must complete and attach Form 4562 only if" (2025; sha256 ad71de35)
