# Proof-of-concept scope screening

- Document: `scope` (form, tax year 2025)
- Note: Stage 4 screening answers are explicit declarations, not automatic determinations of eligibility. Stage 5 wires these gates into the whole-return outcome.

## (helper) — `scope.no`

- **Authored helper label:** Year parameter household.no (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.w2_count`

- **Authored helper label:** Number of Forms W-2 on the return
- **Encoded (Count):** Add person.employers over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.employers","op":"sum_over"}`
- Cite: [i1040gi] p. 23, Line 1a, "Enter the total amount from Form(s) W-2, box 1" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.has_w2`

- **Authored helper label:** The return has a Form W-2
- **Encoded (Bool):** helper "Number of Forms W-2 on the return" > 0 (a count)
- Expr: `{"gt":["scope.w2_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 23, Line 1a, "Enter the total amount from Form(s) W-2, box 1" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.noncitizen`

- **Authored helper label:** At any time in 2025, were you (or, on a joint return, your spouse) not a U.S. citizen?
- **Encoded (Bool):** Input — At any time in 2025, were you (or, on a joint return, your spouse) not a U.S. citizen?
- Expr: `{"op":"input","source":"At any time in 2025, were you (or, on a joint return, your spouse) not a U.S. citizen?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.nonresident`

- **Authored helper label:** For any part of 2025, were you (or, on a joint return, your spouse) a nonresident alien, that is, neither a U.S. citizen nor a U.S. resident for tax?
- **Encoded (Bool):** Input — For any part of 2025, were you (or, on a joint return, your spouse) a nonresident alien, that is, neither a U.S. citizen nor a U.S. resident for tax?
- Expr: `{"op":"input","source":"For any part of 2025, were you (or, on a joint return, your spouse) a nonresident alien, that is, neither a U.S. citizen nor a U.S. resident for tax?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.nonresident_if_noncitizen`

- **Authored helper label:** The answer to scope.nonresident, asked only when the question scope.noncitizen is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "At any time in 2025, were you (or, on a joint return, your spouse) not a U.S. citizen?" = true → helper "For any part of 2025, were you (or, on a joint return, your spouse) a nonresident alien, that is, neither a U.S. citizen nor a U.S. resident for tax?"] [helper "At any time in 2025, were you (or, on a joint return, your spouse) not a U.S. citizen?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.noncitizen",{"const":true}],"op":"test"},"then":"scope.nonresident"},{"guard":{"eq":["scope.noncitizen",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 8, "Most nonresident aliens and dual-status aliens have different filing requirements and may have to file Form 1040-NR" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.chapter11`

- **Authored helper label:** At any time in 2025, were you (or, on a joint return, your spouse) in a chapter 11 bankruptcy case?
- **Encoded (Bool):** Input — At any time in 2025, were you (or, on a joint return, your spouse) in a chapter 11 bankruptcy case?
- Expr: `{"op":"input","source":"At any time in 2025, were you (or, on a joint return, your spouse) in a chapter 11 bankruptcy case?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.treaty`

- **Authored helper label:** Is any of your (or, on a joint return, your spouse's) 2025 income exempt from U.S. tax under a tax treaty?
- **Encoded (Bool):** Input — Is any of your (or, on a joint return, your spouse's) 2025 income exempt from U.S. tax under a tax treaty, such as the pay or scholarship of a student, teacher or researcher from another country (often shown on Form 1042-S or claimed on Form 8833)?
- Expr: `{"op":"input","source":"Is any of your (or, on a joint return, your spouse's) 2025 income exempt from U.S. tax under a tax treaty, such as the pay or scholarship of a student, teacher or researcher from another country (often shown on Form 1042-S or claimed on Form 8833)?"}`
- Cite: [i1040s8812] p. 3, Line 18a, "Income excluded under a tax treaty is also excluded from the computation of earned income on line 18a." (2025; printed date 2026-01-23; sha256 bb9788cd)

## (helper) — `scope.armed_forces`

- **Authored helper label:** In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?
- **Encoded (Bool):** Input — In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?
- Expr: `{"op":"input","source":"In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.reservist_expenses`

- **Authored helper label:** Do you want to deduct costs, not paid back, of travel more than 100 miles from home for reserve or National Guard duty in 2025?
- **Encoded (Bool):** Input — Do you want to deduct costs, not paid back, of travel more than 100 miles from home for reserve or National Guard duty in 2025?
- Expr: `{"op":"input","source":"Do you want to deduct costs, not paid back, of travel more than 100 miles from home for reserve or National Guard duty in 2025?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.reservist_expenses_if_armed_forces`

- **Authored helper label:** The answer to scope.reservist_expenses, asked only when the question scope.armed_forces is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?" = true → helper "Do you want to deduct costs, not paid back, of travel more than 100 miles from home for reserve or National Guard duty in 2025?"] [helper "In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.armed_forces",{"const":true}],"op":"test"},"then":"scope.reservist_expenses"},{"guard":{"eq":["scope.armed_forces",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Line 12, "Certain business expenses of National Guard and reserve members who traveled more than 100 miles from home" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.military_move`

- **Authored helper label:** Do you want to deduct moving costs, not paid back, of a 2025 move to a new permanent post under military orders, or storage fees while you were posted outside the United States?
- **Encoded (Bool):** Input — Do you want to deduct moving costs, not paid back, of a 2025 move to a new permanent post under military orders, or storage fees while you were posted outside the United States?
- Expr: `{"op":"input","source":"Do you want to deduct moving costs, not paid back, of a 2025 move to a new permanent post under military orders, or storage fees while you were posted outside the United States?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; i1040gi p. 93, Line 14, "If you are claiming only storage fees during your absence from the United States, check the box on line 14" (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.military_move_if_armed_forces`

- **Authored helper label:** The answer to scope.military_move, asked only when the question scope.armed_forces is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?" = true → helper "Do you want to deduct moving costs, not paid back, of a 2025 move to a new permanent post under military orders, or storage fees while you were posted outside the United States?"] [helper "In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.armed_forces",{"const":true}],"op":"test"},"then":"scope.military_move"},{"guard":{"eq":["scope.armed_forces",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Line 14, "You can deduct moving expenses if you are a member of the Armed Forces on active duty and due to a military order you move because of a permanent change of station" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.reservist_repaid`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) put back into an IRA money taken out of a retirement plan during a call to active duty as a reservist?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) put back into an IRA money taken out of a retirement plan during a call to active duty as a reservist?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) put back into an IRA money taken out of a retirement plan during a call to active duty as a reservist?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.reservist_repaid_if_armed_forces`

- **Authored helper label:** The answer to scope.reservist_repaid, asked only when the question scope.armed_forces is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?" = true → helper "In 2025, did you (or, on a joint return, your spouse) put back into an IRA money taken out of a retirement plan during a call to active duty as a reservist?"] [helper "In 2022 or later, did you (or, on a joint return, your spouse) serve in the U.S. armed forces, Coast Guard, reserves or National Guard?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.armed_forces",{"const":true}],"op":"test"},"then":"scope.reservist_repaid"},{"guard":{"eq":["scope.armed_forces",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 95, Line 20, "Don’t include any repayments of qualified reservist distributions" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.under24_count`

- **Authored helper label:** Your entry, if you were under 24 at the end of 2025 (from your year of birth)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Under age 24 at the end of 2025 (born after January 1, 2002)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.under24",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i8615] p. 1, Certain January 1 birthdays, "Use the following chart to determine whether certain children with January 1 birthdays meet condition 3 under Who Must File" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 902ca736)

## (helper) — `scope.under24`

- **Authored helper label:** You were under 24 at the end of 2025
- **Encoded (Bool):** helper "Your entry, if you were under 24 at the end of 2025 (from your year of birth)" > 0 (a count)
- Expr: `{"gt":["scope.under24_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i8615] p. 1, Who Must File, "under age 24 at the end of 2025" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 902ca736)

## (gate) — `scope.under24_if_not_joint`

- **Authored helper label:** The answer to scope.under24, asked only when the return is not a joint return (false otherwise)
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "You were under 24 at the end of 2025"] [f1040 line Filing Status = 'hoh' → helper "You were under 24 at the end of 2025"] [f1040 line Filing Status = 'qss' → helper "You were under 24 at the end of 2025"] [f1040 line Filing Status = 'mfs' → helper "You were under 24 at the end of 2025"] [f1040 line Filing Status = 'mfj' → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"scope.under24"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"scope.under24"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"scope.under24"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"scope.under24"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i8615] p. 1, Who Must File, "The child doesn’t file a joint return for 2025" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 902ca736)

## (helper) — `scope.unearned_2700`

- **Authored helper label:** In 2025, did you have more than $2,700 of income that was not pay for work, such as interest, dividends or gains from investments?
- **Encoded (Bool):** Input — In 2025, did you have more than $2,700 of income that was not pay for work, such as interest, dividends or gains from investments?
- Expr: `{"op":"input","source":"In 2025, did you have more than $2,700 of income that was not pay for work, such as interest, dividends or gains from investments?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.unearned_2700_if_under24`

- **Authored helper label:** The answer to scope.unearned_2700, asked only when the question scope.under24 is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "The answer to scope.under24, asked only when the return is not a joint return (false otherwise)" = true → helper "In 2025, did you have more than $2,700 of income that was not pay for work, such as interest, dividends or gains from investments?"] [helper "The answer to scope.under24, asked only when the return is not a joint return (false otherwise)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.under24_if_not_joint",{"const":true}],"op":"test"},"then":"scope.unearned_2700"},{"guard":{"eq":["scope.under24_if_not_joint",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i8615] p. 1, Who Must File, "The child had more than $2,700 of unearned income" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 902ca736)

## (helper) — `scope.f8615`

- **Authored helper label:** At the end of 2025, was a parent of yours alive, and were you either under 18, or 18 (or a full-time student aged 19 to 23) with pay for work of no more than half of what it cost to support you?
- **Encoded (Bool):** Input — At the end of 2025, was a parent of yours alive, and were you either under 18, or 18 (or a full-time student aged 19 to 23) with pay for work of no more than half of what it cost to support you?
- Expr: `{"op":"input","source":"At the end of 2025, was a parent of yours alive, and were you either under 18, or 18 (or a full-time student aged 19 to 23) with pay for work of no more than half of what it cost to support you?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.f8615_if_unearned_2700`

- **Authored helper label:** The answer to scope.f8615, asked only when the question scope.unearned_2700 is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "The answer to scope.unearned_2700, asked only when the question scope.under24 is answered Yes (false otherwise)" = true → helper "At the end of 2025, was a parent of yours alive, and were you either under 18, or 18 (or a full-time student aged 19 to 23) with pay for work of no more than half of what it cost to support you?"] [helper "The answer to scope.unearned_2700, asked only when the question scope.under24 is answered Yes (false otherwise)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.unearned_2700_if_under24",{"const":true}],"op":"test"},"then":"scope.f8615"},{"guard":{"eq":["scope.unearned_2700_if_under24",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i8615] p. 1, Who Must File, "Form 8615 must be filed for any child who meets all of the following conditions" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 902ca736)

## (helper) — `scope.f8814`

- **Authored helper label:** Are you (or, on a joint return, your spouse) reporting a child's 2025 interest or dividends on your own return instead of filing a return for the child?
- **Encoded (Bool):** Input — Are you (or, on a joint return, your spouse) reporting a child's 2025 interest or dividends on your own return instead of filing a return for the child?
- Expr: `{"op":"input","source":"Are you (or, on a joint return, your spouse) reporting a child's 2025 interest or dividends on your own return instead of filing a return for the child?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.adoption_benefits`

- **Authored helper label:** Did an employer pay or repay any of the adoption costs for you (or, on a joint return, your spouse)? Box 12 of a W-2 shows it with the code T.
- **Encoded (Bool):** Input — Did an employer pay or repay any of the adoption costs for you (or, on a joint return, your spouse)? Box 12 of a W-2 shows it with the code T.
- Expr: `{"op":"input","source":"Did an employer pay or repay any of the adoption costs for you (or, on a joint return, your spouse)? Box 12 of a W-2 shows it with the code T."}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.adoption_benefits_if_adoption`

- **Authored helper label:** The answer to scope.adoption_benefits, asked only when there was an adoption or adoption costs since the start of 2024 (false otherwise)
- **Encoded (Bool):** Choose — [s3 helper "In 2024 or 2025, did you (or, on a joint return, your spouse) adopt a child, or pay (or have an employer pay) expenses in connection with adopting a child or trying to adopt one?" = true → helper "Did an employer pay or repay any of the adoption costs for you (or, on a joint return, your spouse)? Box 12 of a W-2 shows it with the code T."] [s3 helper "In 2024 or 2025, did you (or, on a joint return, your spouse) adopt a child, or pay (or have an employer pay) expenses in connection with adopting a child or trying to adopt one?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s3.adoption_any",{"const":true}],"op":"test"},"then":"scope.adoption_benefits"},{"guard":{"eq":["s3.adoption_any",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1f, "Employer-provided adoption benefits should be shown in box 12 of your Form(s) W-2 with code T" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.rental`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; p527 p. 3, Cash method, "You are a cash basis taxpayer if you report income on your return in the year you actually or constructively receive it, regardless of when it was earned" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.rent_personal`

- **Authored helper label:** Was any of what you rented out something other than a building, a room or land, such as a car, a trailer or equipment?
- **Encoded (Bool):** Input — Was any of what you rented out something other than a building, a room or land, such as a car, a trailer or equipment?
- Expr: `{"op":"input","source":"Was any of what you rented out something other than a building, a room or land, such as a car, a trailer or equipment?"}`
- Cite: [i1040se] p. 5, Personal property, "Do not use Schedule E to report income and expenses from the rental of personal property, such as equipment or vehicles" (2025; sha256 ad71de35)

## (gate) — `scope.rent_personal_if_rental`

- **Authored helper label:** The answer to scope.rent_personal, asked only when the question scope.rental is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?" = true → helper "Was any of what you rented out something other than a building, a room or land, such as a car, a trailer or equipment?"] [helper "In 2025, did you (or, on a joint return, your spouse) rent out, offer for rent, or receive rent for, anything you own or lease, or receive royalties?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.rental",{"const":true}],"op":"test"},"then":"scope.rent_personal"},{"guard":{"eq":["scope.rental",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040se] p. 5, Personal property, "Do not use Schedule E to report income and expenses from the rental of personal property, such as equipment or vehicles" (2025; sha256 ad71de35)

## (helper) — `scope.k1`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) have income or a loss from a partnership, an S corporation, an estate or a trust? A paper called Schedule K-1 reports it.
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) have income or a loss from a partnership, an S corporation, an estate or a trust? A paper called Schedule K-1 reports it.
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) have income or a loss from a partnership, an S corporation, an estate or a trust? A paper called Schedule K-1 reports it."}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.farm`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) have income or a loss from farming?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) have income or a loss from farming?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) have income or a loss from farming?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.remic`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) hold a residual interest in a real estate mortgage investment conduit (REMIC), reported to you on Schedule Q?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) hold a residual interest in a real estate mortgage investment conduit (REMIC), reported to you on Schedule Q?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) hold a residual interest in a real estate mortgage investment conduit (REMIC), reported to you on Schedule Q?"}`
- Cite: [i1040se] p. 1, General Instructions, "Use Schedule E (Form 1040) to report income or loss from rental real estate, royalties, partnerships, S corporations, estates, trusts, and residual interests in REMICs"; p. 11, Part IV, "You should receive Schedule Q (Form 1066) and instructions from the REMIC for each quarter"; i6251 p. 9, "If you held a residual interest in a REMIC in 2025, the amount you enter on line 4 may not be less than the amount on Schedule E, line 38, column (c)" (2025; sha256 ad71de35)

## (helper) — `scope.pay_no_w2`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.household_pay`

- **Authored helper label:** In 2025, were you (or, on a joint return, your spouse) paid as a household employee, for work in or around a household's home or for its members (for example as a nanny, carer, housekeeper, gardener or private driver, even in a home you share), by a household that gave you no W-2 and that controlled what work was done and how, not as a self-employed worker offering the work to the public?
- **Encoded (Bool):** Input — In 2025, were you (or, on a joint return, your spouse) paid as a household employee, for work in or around a household's home or for its members (for example as a nanny, carer, housekeeper, gardener or private driver, even in a home you share), by a household that gave you no W-2 and that controlled what work was done and how, not as a self-employed worker offering the work to the public?
- Expr: `{"op":"input","source":"In 2025, were you (or, on a joint return, your spouse) paid as a household employee, for work in or around a household's home or for its members (for example as a nanny, carer, housekeeper, gardener or private driver, even in a home you share), by a household that gave you no W-2 and that controlled what work was done and how, not as a self-employed worker offering the work to the public?"}`
- Cite: [i1040gi] p. 24, Line 1b, "Enter the total of your wages received as a household employee that was not reported on Form(s) W-2"; p926 p. 3, Do You Have a Household Employee?, "The worker is your employee if you can control not only what work is done, but how it is done"; p. 4, "A self-employed worker usually provides their own tools and offers services to the general public in an independent business" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `scope.household_pay_if_pay`

- **Authored helper label:** Wages as a household employee not reported on a W-2 (asked only after a Yes to pay not on a W-2; otherwise no)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = true → helper "In 2025, were you (or, on a joint return, your spouse) paid as a household employee, for work in or around a household's home or for its members (for example as a nanny, carer, housekeeper, gardener or private driver, even in a home you share), by a household that gave you no W-2 and that controlled what work was done and how, not as a self-employed worker offering the work to the public?"] [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.pay_no_w2",{"const":true}],"op":"test"},"then":"scope.household_pay"},{"guard":{"eq":["scope.pay_no_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1b, "Enter the total of your wages received as a household employee that was not reported on Form(s) W-2" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.contractor_pay`

- **Authored helper label:** In 2025, did a firm pay you (or, on a joint return, your spouse) as an independent contractor, when you believe you were its employee, without taking out social security or Medicare tax?
- **Encoded (Bool):** Input — In 2025, did a firm pay you (or, on a joint return, your spouse) as an independent contractor, when you believe you were its employee, without taking out social security or Medicare tax?
- Expr: `{"op":"input","source":"In 2025, did a firm pay you (or, on a joint return, your spouse) as an independent contractor, when you believe you were its employee, without taking out social security or Medicare tax?"}`
- Cite: [f8919] p. 1, Who must file, "You performed services for a firm", "You believe your pay from the firm wasn’t for services as an independent contractor", "The firm didn’t withhold your share of social security and Medicare taxes from your pay" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)

## (gate) — `scope.contractor_pay_if_pay`

- **Authored helper label:** Wages from a firm that treated the worker as an independent contractor (Form 8919) (asked only after a Yes to pay not on a W-2; otherwise no)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = true → helper "In 2025, did a firm pay you (or, on a joint return, your spouse) as an independent contractor, when you believe you were its employee, without taking out social security or Medicare tax?"] [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.pay_no_w2",{"const":true}],"op":"test"},"then":"scope.contractor_pay"},{"guard":{"eq":["scope.pay_no_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [f8919] p. 1, Who must file, "You performed services for a firm", "You believe your pay from the firm wasn’t for services as an independent contractor", "The firm didn’t withhold your share of social security and Medicare taxes from your pay" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)

## (helper) — `scope.tips_unreported`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) get cash or card tips at a job that were not reported in full to the employer, or tips that were not money, such as tickets or other items of value?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) get cash or card tips at a job that were not reported in full to the employer, or tips that were not money, such as tickets or other items of value?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) get cash or card tips at a job that were not reported in full to the employer, or tips that were not money, such as tickets or other items of value?"}`
- Cite: [i1040gi] p. 24, Line 1c, "This should include any tip income you didn’t report to your employer", "Also, include the value of any noncash tips you received, such as tickets, passes, or other items of value" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `scope.tips_unreported_if_pay`

- **Authored helper label:** Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = true → helper "In 2025, did you (or, on a joint return, your spouse) get cash or card tips at a job that were not reported in full to the employer, or tips that were not money, such as tickets or other items of value?"] [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.pay_no_w2",{"const":true}],"op":"test"},"then":"scope.tips_unreported"},{"guard":{"eq":["scope.pay_no_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1c, "This should include any tip income you didn’t report to your employer", "Also, include the value of any noncash tips you received, such as tickets, passes, or other items of value" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.strike_pay`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) get strike or lockout benefits, other than bona fide gifts?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) get strike or lockout benefits, other than bona fide gifts?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) get strike or lockout benefits, other than bona fide gifts?"}`
- Cite: [i1040gi] p. 24, Line 1h, "Strike or lockout benefits (other than bona fide gifts)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `scope.strike_pay_if_pay`

- **Authored helper label:** Strike or lockout benefits (asked only after a Yes to pay not on a W-2; otherwise no)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = true → helper "In 2025, did you (or, on a joint return, your spouse) get strike or lockout benefits, other than bona fide gifts?"] [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.pay_no_w2",{"const":true}],"op":"test"},"then":"scope.strike_pay"},{"guard":{"eq":["scope.pay_no_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1h, "Strike or lockout benefits (other than bona fide gifts)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.wages_no_form`

- **Authored helper label:** In 2025, did an employer pay you (or, on a joint return, your spouse) wages for which you have no W-2, other than the kinds of pay just asked about?
- **Encoded (Bool):** Input — In 2025, did an employer pay you (or, on a joint return, your spouse) wages for which you have no W-2, other than the kinds of pay just asked about?
- Expr: `{"op":"input","source":"In 2025, did an employer pay you (or, on a joint return, your spouse) wages for which you have no W-2, other than the kinds of pay just asked about?"}`
- Cite: [i1040gi] p. 25, Missing or Incorrect Form W-2?, "Even if you don’t get a Form W-2, you must still report your earnings" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `scope.wages_no_form_if_pay`

- **Authored helper label:** Other wages from an employer, with no W-2 (asked only after a Yes to pay not on a W-2; otherwise no)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = true → helper "In 2025, did an employer pay you (or, on a joint return, your spouse) wages for which you have no W-2, other than the kinds of pay just asked about?"] [helper "In 2025, did you (or, on a joint return, your spouse) have wages, tips, or strike or lockout benefits that are not on a W-2?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.pay_no_w2",{"const":true}],"op":"test"},"then":"scope.wages_no_form"},{"guard":{"eq":["scope.pay_no_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 25, Missing or Incorrect Form W-2?, "Even if you don’t get a Form W-2, you must still report your earnings" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.medicaid_waiver`

- **Authored helper label:** In 2025, were you (or, on a joint return, your spouse) paid under Medicaid to care for someone living in your home?
- **Encoded (Bool):** Input — In 2025, were you (or, on a joint return, your spouse) paid under Medicaid to care for someone living in your home?
- Expr: `{"op":"input","source":"In 2025, were you (or, on a joint return, your spouse) paid under Medicaid to care for someone living in your home?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.religious_work`

- **Authored helper label:** In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?
- **Encoded (Bool):** Input — In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?
- Expr: `{"op":"input","source":"In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.clergy`

- **Authored helper label:** Was that work as a minister or other clergy (a chaplain too), as a member of a religious order who has not taken a vow of poverty, or as a Christian Science practitioner?
- **Encoded (Bool):** Input — Was that work as a minister or other clergy (a chaplain too), as a member of a religious order who has not taken a vow of poverty, or as a Christian Science practitioner?
- Expr: `{"op":"input","source":"Was that work as a minister or other clergy (a chaplain too), as a member of a religious order who has not taken a vow of poverty, or as a Christian Science practitioner?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.clergy_if_religious_work`

- **Authored helper label:** The answer to scope.clergy, asked only when the question scope.religious_work is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?" = true → helper "Was that work as a minister or other clergy (a chaplain too), as a member of a religious order who has not taken a vow of poverty, or as a Christian Science practitioner?"] [helper "In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.religious_work",{"const":true}],"op":"test"},"then":"scope.clergy"},{"guard":{"eq":["scope.religious_work",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] i1040sse p. 1, Ministers, Members of Religious Orders, and Christian Science Practitioners, "you must pay SE tax on salaries and other income for services you performed as a minister, member of a religious order who hasn’t taken a vow of poverty, or Christian Science practitioner" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.church_exempt_wages`

- **Authored helper label:** Did a church or church organization pay you (or, on a joint return, your spouse) wages with no social security or Medicare tax taken out (boxes 4 and 6 of its W-2 are empty)?
- **Encoded (Bool):** Input — Did a church or church organization pay you (or, on a joint return, your spouse) wages with no social security or Medicare tax taken out (boxes 4 and 6 of its W-2 are empty)?
- Expr: `{"op":"input","source":"Did a church or church organization pay you (or, on a joint return, your spouse) wages with no social security or Medicare tax taken out (boxes 4 and 6 of its W-2 are empty)?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.church_exempt_wages_if_religious_work`

- **Authored helper label:** The answer to scope.church_exempt_wages, asked only when the question scope.religious_work is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?" = true → helper "Did a church or church organization pay you (or, on a joint return, your spouse) wages with no social security or Medicare tax taken out (boxes 4 and 6 of its W-2 are empty)?"] [helper "In 2025, were you (or, on a joint return, your spouse) paid by a church or religious body, or as clergy or religious order member?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.religious_work",{"const":true}],"op":"test"},"then":"scope.church_exempt_wages"},{"guard":{"eq":["scope.religious_work",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] i1040sse p. 1, Employees of Churches and Church Organizations, "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.w2_marks`

- **Authored helper label:** On any W-2 for 2025, is the 'Statutory employee' box in box 13 ticked, or does box 12 show the code H?
- **Encoded (Bool):** Input — On any W-2 for 2025, is the 'Statutory employee' box in box 13 ticked, or does box 12 show the code H?
- Expr: `{"op":"input","source":"On any W-2 for 2025, is the 'Statutory employee' box in box 13 ticked, or does box 12 show the code H?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.w2_marks_if_w2`

- **Authored helper label:** The answer to scope.w2_marks, asked only when a Form W-2 is listed (false otherwise)
- **Encoded (Bool):** Choose — [helper "The return has a Form W-2" = true → helper "On any W-2 for 2025, is the 'Statutory employee' box in box 13 ticked, or does box 12 show the code H?"] [helper "The return has a Form W-2" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.has_w2",{"const":true}],"op":"test"},"then":"scope.w2_marks"},{"guard":{"eq":["scope.has_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 25, Were You a Statutory Employee?, "Statutory employees report the amount shown in box 1 of Form W-2 on a Schedule C"; p. 100, Line 24f, "Enter contributions to section 501(c)(18)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.artist_official`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) work as a performing artist, or as a state or local government official who is paid from fees?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) work as a performing artist, or as a state or local government official who is paid from fees?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) work as a performing artist, or as a state or local government official who is paid from fees?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.artist_official_if_w2`

- **Authored helper label:** The answer to scope.artist_official, asked only when a Form W-2 is listed (false otherwise)
- **Encoded (Bool):** Choose — [helper "The return has a Form W-2" = true → helper "In 2025, did you (or, on a joint return, your spouse) work as a performing artist, or as a state or local government official who is paid from fees?"] [helper "The return has a Form W-2" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.has_w2",{"const":true}],"op":"test"},"then":"scope.artist_official"},{"guard":{"eq":["scope.has_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Line 12, "Performing-arts-related expenses as a qualified performing artist", "Business expenses of fee-basis state or local government officials" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.performer_expenses`

- **Authored helper label:** Do you want to deduct costs for that work, not paid back, under the rules for a 'qualified performing artist' or an official paid by fees?
- **Encoded (Bool):** Input — Do you want to deduct costs for that work, not paid back, under the rules for a 'qualified performing artist' or an official paid by fees?
- Expr: `{"op":"input","source":"Do you want to deduct costs for that work, not paid back, under the rules for a 'qualified performing artist' or an official paid by fees?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.performer_expenses_if_artist_official`

- **Authored helper label:** The answer to scope.performer_expenses, asked only when the question scope.artist_official is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "The answer to scope.artist_official, asked only when a Form W-2 is listed (false otherwise)" = true → helper "Do you want to deduct costs for that work, not paid back, under the rules for a 'qualified performing artist' or an official paid by fees?"] [helper "The answer to scope.artist_official, asked only when a Form W-2 is listed (false otherwise)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.artist_official_if_w2",{"const":true}],"op":"test"},"then":"scope.performer_expenses"},{"guard":{"eq":["scope.artist_official_if_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Line 12, "Performing-arts-related expenses as a qualified performing artist", "Business expenses of fee-basis state or local government officials"; p. 93, Line 12, "For more details, see Form 2106" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.care_benefits_other`

- **Authored helper label:** Were any of those care benefits not shown in box 10 of a W-2 (for example from your own business or a partnership), or carried into 2025 from a 2024 plan under a grace period?
- **Encoded (Bool):** Input — Were any of those care benefits not shown in box 10 of a W-2 (for example from your own business or a partnership), or carried into 2025 from a 2024 plan under a grace period?
- Expr: `{"op":"input","source":"Were any of those care benefits not shown in box 10 of a W-2 (for example from your own business or a partnership), or carried into 2025 from a 2024 plan under a grace period?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.care_benefits_other_if_benefits`

- **Authored helper label:** The answer to scope.care_benefits_other, asked only when dependent care benefits were received (false otherwise)
- **Encoded (Bool):** Choose — [f2441 helper "Did you receive dependent care benefits?" = true → helper "Were any of those care benefits not shown in box 10 of a W-2 (for example from your own business or a partnership), or carried into 2025 from a 2024 plan under a grace period?"] [f2441 helper "Did you receive dependent care benefits?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f2441.benefits",{"const":true}],"op":"test"},"then":"scope.care_benefits_other"},{"guard":{"eq":["f2441.benefits",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1e, "Dependent care benefits should be shown in box 10 of your Form(s) W-2"; i2441 p. 5, Line 12, "include amounts you received under a dependent care assistance program from your sole proprietorship or partnership"; i2441 p. 5, Line 13, "Enter on line 13 the amount you carried forward and used in 2025 during the grace period" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.recovery`

- **Authored helper label:** In 2025, were you (or, on a joint return, your spouse) paid back an amount you deducted or took a credit for on an earlier year's return, other than a state or local income tax refund?
- **Encoded (Bool):** Input — In 2025, were you (or, on a joint return, your spouse) paid back an amount you deducted or took a credit for on an earlier year's return, other than a state or local income tax refund?
- Expr: `{"op":"input","source":"In 2025, were you (or, on a joint return, your spouse) paid back an amount you deducted or took a credit for on an earlier year's return, other than a state or local income tax refund?"}`
- Cite: [p525] p. 24, Recoveries, "A recovery is a return of an amount you deducted or took a credit for in an earlier year"; p. 26, Example 33, "You must include $50 in your 2025 income, rather than $250" (2025; sha256 39b0fa5e)

## (helper) — `scope.disaster_distribution`

- **Authored helper label:** Did you (or, on a joint return, your spouse) take money from a retirement plan in 2023 or 2024 because of a disaster, and spread its tax over three years or pay any of it back in 2025?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) take money from a retirement plan in 2023 or 2024 because of a disaster, and spread its tax over three years or pay any of it back in 2025?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) take money from a retirement plan in 2023 or 2024 because of a disaster, and spread its tax over three years or pay any of it back in 2025?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.excess_deferral`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) put more of your pay into retirement plans at work than the yearly limit ($23,500 for most people)?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) put more of your pay into retirement plans at work than the yearly limit ($23,500 for most people)?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) put more of your pay into retirement plans at work than the yearly limit ($23,500 for most people)?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.excess_deferral_if_w2`

- **Authored helper label:** The answer to scope.excess_deferral, asked only when a Form W-2 is listed (false otherwise)
- **Encoded (Bool):** Choose — [helper "The return has a Form W-2" = true → helper "In 2025, did you (or, on a joint return, your spouse) put more of your pay into retirement plans at work than the yearly limit ($23,500 for most people)?"] [helper "The return has a Form W-2" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.has_w2",{"const":true}],"op":"test"},"then":"scope.excess_deferral"},{"guard":{"eq":["scope.has_w2",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1h, "If the total amount you (or your spouse if filing jointly) deferred for 2025 under all plans was more than $23,500" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.archer_msa`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) put money into, or take money out of, an Archer MSA or a Medicare Advantage MSA (older kinds of medical savings account, not a health savings account)?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) put money into, or take money out of, an Archer MSA or a Medicare Advantage MSA (older kinds of medical savings account, not a health savings account)?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) put money into, or take money out of, an Archer MSA or a Medicare Advantage MSA (older kinds of medical savings account, not a health savings account)?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.education_recapture`

- **Authored helper label:** In 2025, was tuition or a fee refunded, or tax-free aid given, to a student for a year for which you (or, on a joint return, your spouse) had already claimed an education credit?
- **Encoded (Bool):** Input — In 2025, was tuition or a fee refunded, or tax-free aid given, to a student for a year for which you (or, on a joint return, your spouse) had already claimed an education credit?
- Expr: `{"op":"input","source":"In 2025, was tuition or a fee refunded, or tax-free aid given, to a student for a year for which you (or, on a joint return, your spouse) had already claimed an education credit?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.se_plan_other`

- **Authored helper label:** Did you (or, on a joint return, your spouse) put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k), for 2025?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k), for 2025?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k), for 2025?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.se_plan_other_if_business`

- **Authored helper label:** The answer to scope.se_plan_other, asked only when a business (Schedule C) is listed (false otherwise)
- **Encoded (Bool):** Choose — [s1 helper "The return has a Schedule C" = true → helper "Did you (or, on a joint return, your spouse) put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k), for 2025?"] [s1 helper "The return has a Schedule C" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1.has_sc",{"const":true}],"op":"test"},"then":"scope.se_plan_other"},{"guard":{"eq":["s1.has_sc",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Line 16, "Self-Employed SEP, SIMPLE, and Qualified Plans", "If you were self-employed or a partner, you may be able to take this" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.income_averaging`

- **Authored helper label:** Is your business fishing, and do you (or, on a joint return, your spouse) choose to figure your tax by averaging its income over three years (Schedule J)?
- **Encoded (Bool):** Input — Is your business fishing, and do you (or, on a joint return, your spouse) choose to figure your tax by averaging its income over three years (Schedule J)?
- Expr: `{"op":"input","source":"Is your business fishing, and do you (or, on a joint return, your spouse) choose to figure your tax by averaging its income over three years (Schedule J)?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.income_averaging_if_business`

- **Authored helper label:** The answer to scope.income_averaging, asked only when a business (Schedule C) is listed (false otherwise)
- **Encoded (Bool):** Choose — [s1 helper "The return has a Schedule C" = true → helper "Is your business fishing, and do you (or, on a joint return, your spouse) choose to figure your tax by averaging its income over three years (Schedule J)?"] [s1 helper "The return has a Schedule C" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1.has_sc",{"const":true}],"op":"test"},"then":"scope.income_averaging"},{"guard":{"eq":["s1.has_sc",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 36, Schedule J, "If you had income from farming or fishing, your tax may be less if you choose to figure it using income averaging on Schedule J"; i1040sj p. 1, "all or part of your 2025 taxable income from your trade or business of farming or fishing" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.foreign_shares`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.pfic`

- **Authored helper label:** Was any of it a fund, or a company whose income or assets are mostly investments, set up outside the United States (a 'passive foreign investment company')?
- **Encoded (Bool):** Input — Was any of it a fund, or a company whose income or assets are mostly investments, set up outside the United States (a 'passive foreign investment company')?
- Expr: `{"op":"input","source":"Was any of it a fund, or a company whose income or assets are mostly investments, set up outside the United States (a 'passive foreign investment company')?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.pfic_if_foreign_shares`

- **Authored helper label:** The answer to scope.pfic, asked only when the question scope.foreign_shares is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?" = true → helper "Was any of it a fund, or a company whose income or assets are mostly investments, set up outside the United States (a 'passive foreign investment company')?"] [helper "In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.foreign_shares",{"const":true}],"op":"test"},"then":"scope.pfic"},{"guard":{"eq":["scope.foreign_shares",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 34, Line 16, "Any tax from Form 8621, line 16e, relating to a section 1291 fund"; p. 114, Line 17p, "Enter any interest amount from Form 8621, line 16f" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.cfc`

- **Authored helper label:** Was any of it a foreign company in which U.S. owners together hold more than half (a 'controlled foreign corporation')?
- **Encoded (Bool):** Input — Was any of it a foreign company in which U.S. owners together hold more than half (a 'controlled foreign corporation')?
- Expr: `{"op":"input","source":"Was any of it a foreign company in which U.S. owners together hold more than half (a 'controlled foreign corporation')?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.cfc_if_foreign_shares`

- **Authored helper label:** The answer to scope.cfc, asked only when the question scope.foreign_shares is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?" = true → helper "Was any of it a foreign company in which U.S. owners together hold more than half (a 'controlled foreign corporation')?"] [helper "In 2025, did you (or, on a joint return, your spouse) hold shares or options in a company or fund set up abroad, not through a U.S. fund?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.foreign_shares",{"const":true}],"op":"test"},"then":"scope.cfc"},{"guard":{"eq":["scope.foreign_shares",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 91, Line 8n, "Section 951 generally requires that a U.S. shareholder of a controlled foreign corporation include in income its pro rata share"; p. 91, Line 8o, "Section 951A generally requires that a U.S. shareholder of a controlled foreign corporation include in income its global intangible low-taxed income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.reforestation`

- **Authored helper label:** Do you (or, on a joint return, your spouse) own or lease timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) own or lease timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) own or lease timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.attorney_fees`

- **Authored helper label:** In 2025, were lawyer's fees or court costs paid by you (or, on a joint return, your spouse), or taken out of what you won, for a claim of unlawful discrimination, a claim against the U.S. Government, a Medicare secondary-payer claim or an IRS whistleblower award?
- **Encoded (Bool):** Input — In 2025, were lawyer's fees or court costs paid by you (or, on a joint return, your spouse), or taken out of what you won, for a claim of unlawful discrimination, a claim against the U.S. Government, a Medicare secondary-payer claim or an IRS whistleblower award?
- Expr: `{"op":"input","source":"In 2025, were lawyer's fees or court costs paid by you (or, on a joint return, your spouse), or taken out of what you won, for a claim of unlawful discrimination, a claim against the U.S. Government, a Medicare secondary-payer claim or an IRS whistleblower award?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31; i1040gi p. 100, Line 24h, "Enter attorney fees and court costs for actions involving certain unlawful discrimination claims", Line 24i; p525 p. 32, Deduction for costs involved in unlawful discrimination suits, "a claim against the U.S. Government, or a claim under section 1862(b)(3)(A) of the Social Security Act", "The attorney fees and court costs may be paid by you or on your behalf" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.trade_act_repaid`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) pay back supplemental unemployment benefits from an employer's fund in order to qualify for trade readjustment allowances?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) pay back supplemental unemployment benefits from an employer's fund in order to qualify for trade readjustment allowances?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) pay back supplemental unemployment benefits from an employer's fund in order to qualify for trade readjustment allowances?"}`
- Cite: [i1040gi] p. 99, Line 24e, "Enter repayment of supplemental unemployment benefits under the Trade Act of 1974 (see Pub. 525)"; p525 p. 29, Repayment of benefits, "You may have to repay some of your supplemental unemployment benefits to qualify for trade readjustment allowances under the Trade Act of 1974" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.business_before`

- **Authored helper label:** In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?
- **Encoded (Bool):** Input — In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?
- Expr: `{"op":"input","source":"In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.nol`

- **Authored helper label:** Are you (or, on a joint return, your spouse) carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction (a business, farm, rental or disaster loss, not a capital loss from selling investments)?
- **Encoded (Bool):** Input — Are you (or, on a joint return, your spouse) carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction (a business, farm, rental or disaster loss, not a capital loss from selling investments)?
- Expr: `{"op":"input","source":"Are you (or, on a joint return, your spouse) carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction (a business, farm, rental or disaster loss, not a capital loss from selling investments)?"}`
- Cite: [i1040gi] p. 91, Line 8a, "Enter any deduction for an NOL from an earlier year"; i1040sd p. 1, General Instructions, "To report a capital loss carryover from 2024 to 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.passive`

- **Authored helper label:** In 2025, did you (or, on a joint return, your spouse) have income or a loss from, or sell your share of, a business that you owned but did not help run (a 'passive activity')?
- **Encoded (Bool):** Input — In 2025, did you (or, on a joint return, your spouse) have income or a loss from, or sell your share of, a business that you owned but did not help run (a 'passive activity')?
- Expr: `{"op":"input","source":"In 2025, did you (or, on a joint return, your spouse) have income or a loss from, or sell your share of, a business that you owned but did not help run (a 'passive activity')?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.passive_if_business_before`

- **Authored helper label:** The answer to scope.passive, asked only when the question scope.business_before is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?" = true → helper "In 2025, did you (or, on a joint return, your spouse) have income or a loss from, or sell your share of, a business that you owned but did not help run (a 'passive activity')?"] [helper "In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.business_before",{"const":true}],"op":"test"},"then":"scope.passive"},{"guard":{"eq":["scope.business_before",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] i8582 p. 1, Purpose of Form, "Form 8582 is used by noncorporate taxpayers to figure the amount of any passive activity loss (PAL)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.f8978`

- **Authored helper label:** Did a partnership that you (or, on a joint return, your spouse) were in send a Form 8986 about changes made by an audit?
- **Encoded (Bool):** Input — Did a partnership that you (or, on a joint return, your spouse) were in send a Form 8986 about changes made by an audit?
- Expr: `{"op":"input","source":"Did a partnership that you (or, on a joint return, your spouse) were in send a Form 8986 about changes made by an audit?"}`
- Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `scope.f8978_if_business_before`

- **Authored helper label:** The answer to scope.f8978, asked only when the question scope.business_before is answered Yes (false otherwise)
- **Encoded (Bool):** Choose — [helper "In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?" = true → helper "Did a partnership that you (or, on a joint return, your spouse) were in send a Form 8986 about changes made by an audit?"] [helper "In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.business_before",{"const":true}],"op":"test"},"then":"scope.f8978"},{"guard":{"eq":["scope.business_before",{"const":false}],"op":"test"},"then":"scope.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 34, Line 16, "Tax from Form 8978, line 14 (relating to partner’s audit liability under section 6226)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.schedule1`

- **Authored helper label:** Any income or adjustment requiring Schedule 1 other than the ones this tool computes (true when any of the Schedule 1 screening questions is answered Yes)
- **Encoded (Bool):** (helper "The answer to scope.reservist_expenses, asked only when the question scope.armed_forces is answered Yes (false otherwise)" = true or helper "The answer to scope.military_move, asked only when the question scope.armed_forces is answered Yes (false otherwise)" = true or helper "The answer to scope.rent_personal, asked only when the question scope.rental is answered Yes (false otherwise)" = true or helper "In 2025, did you (or, on a joint return, your spouse) have income or a loss from a partnership, an S corporation, an estate or a trust? A paper called Schedule K-1 reports it." = true or helper "In 2025, did you (or, on a joint return, your spouse) have income or a loss from farming?" = true or helper "The answer to scope.clergy, asked only when the question scope.religious_work is answered Yes (false otherwise)" = true or helper "The answer to scope.church_exempt_wages, asked only when the question scope.religious_work is answered Yes (false otherwise)" = true or helper "The answer to scope.w2_marks, asked only when a Form W-2 is listed (false otherwise)" = true or helper "The answer to scope.performer_expenses, asked only when the question scope.artist_official is answered Yes (false otherwise)" = true or helper "In 2025, did you (or, on a joint return, your spouse) put money into, or take money out of, an Archer MSA or a Medicare Advantage MSA (older kinds of medical savings account, not a health savings account)?" = true or helper "The answer to scope.se_plan_other, asked only when a business (Schedule C) is listed (false otherwise)" = true or helper "Do you (or, on a joint return, your spouse) own or lease timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?" = true or helper "In 2025, were lawyer's fees or court costs paid by you (or, on a joint return, your spouse), or taken out of what you won, for a claim of unlawful discrimination, a claim against the U.S. Government, a Medicare secondary-payer claim or an IRS whistleblower award?" = true or helper "In 2025, did you (or, on a joint return, your spouse) pay back supplemental unemployment benefits from an employer's fund in order to qualify for trade readjustment allowances?" = true or helper "In 2025, did you (or, on a joint return, your spouse) hold a residual interest in a real estate mortgage investment conduit (REMIC), reported to you on Schedule Q?" = true)
- Expr: `{"any":[{"eq":["scope.reservist_expenses_if_armed_forces",{"const":true}],"op":"test"},{"eq":["scope.military_move_if_armed_forces",{"const":true}],"op":"test"},{"eq":["scope.rent_personal_if_rental",{"const":true}],"op":"test"},{"eq":["scope.k1",{"const":true}],"op":"test"},{"eq":["scope.farm",{"const":true}],"op":"test"},{"eq":["scope.clergy_if_religious_work",{"const":true}],"op":"test"},{"eq":["scope.church_exempt_wages_if_religious_work",{"const":true}],"op":"test"},{"eq":["scope.w2_marks_if_w2",{"const":true}],"op":"test"},{"eq":["scope.performer_expenses_if_artist_official",{"const":true}],"op":"test"},{"eq":["scope.archer_msa",{"const":true}],"op":"test"},{"eq":["scope.se_plan_other_if_business",{"const":true}],"op":"test"},{"eq":["scope.reforestation",{"const":true}],"op":"test"},{"eq":["scope.attorney_fees",{"const":true}],"op":"test"},{"eq":["scope.trade_act_repaid",{"const":true}],"op":"test"},{"eq":["scope.remic",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 93, Line 12, "Certain business expenses of National Guard and reserve members who traveled more than 100 miles from home"; p. 93, Line 12, "Performing-arts-related expenses as a qualified performing artist", "Business expenses of fee-basis state or local government officials"; p. 93, Line 14, "You can deduct moving expenses if you are a member of the Armed Forces on active duty and due to a military order you move because of a permanent change of station"; p. 93, Line 16, "Self-Employed SEP, SIMPLE, and Qualified Plans", "If you were self-employed or a partner, you may be able to take this"; i1040se p. 1, General Instructions, "Use Schedule E (Form 1040) to report income or loss from rental real estate, royalties, partnerships, S corporations, estates, trusts, and residual interests in REMICs"; i1040sf p. 2, General Instructions, "Use Schedule F (Form 1040) to report farm income and expenses"; i1040sse p. 1, Ministers, Members of Religious Orders, and Christian Science Practitioners, "you must pay SE tax on salaries and other income for services you performed as a minister, member of a religious order who hasn’t taken a vow of poverty, or Christian Science practitioner"; i1040sse p. 1, Employees of Churches and Church Organizations, "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes"; p. 25, Were You a Statutory Employee?, "Statutory employees report the amount shown in box 1 of Form W-2 on a Schedule C"; p. 100, Line 24f, "Enter contributions to section 501(c)(18)"; p. 99, Line 23, "Archer MSA Deduction"; p. 99, Lines 24a Through 24z, "Enter reforestation amortization and expenses"; p. 100, Line 24h, "Enter attorney fees and court costs for actions involving certain unlawful"; p. 99, Line 24e, "Enter repayment of supplemental unemployment benefits under the Trade Act of 1974"; i1040se p. 11, Part IV, "If you are the holder of a residual interest in a REMIC, use Part IV to report your total share of the REMIC’s taxable income or loss" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.other_income`

- **Authored helper label:** Nonresident alien status, or other income or return treatment outside this tool (true when any of the other-income screening questions is answered Yes)
- **Encoded (Bool):** (helper "The answer to scope.nonresident, asked only when the question scope.noncitizen is answered Yes (false otherwise)" = true or helper "At any time in 2025, were you (or, on a joint return, your spouse) in a chapter 11 bankruptcy case?" = true or helper "Is any of your (or, on a joint return, your spouse's) 2025 income exempt from U.S. tax under a tax treaty?" = true or helper "The answer to scope.reservist_repaid, asked only when the question scope.armed_forces is answered Yes (false otherwise)" = true or helper "The answer to scope.adoption_benefits, asked only when there was an adoption or adoption costs since the start of 2024 (false otherwise)" = true or helper "Other wages from an employer, with no W-2 (asked only after a Yes to pay not on a W-2; otherwise no)" = true or helper "The answer to scope.care_benefits_other, asked only when dependent care benefits were received (false otherwise)" = true or helper "Did you (or, on a joint return, your spouse) take money from a retirement plan in 2023 or 2024 because of a disaster, and spread its tax over three years or pay any of it back in 2025?" = true or helper "The answer to scope.excess_deferral, asked only when a Form W-2 is listed (false otherwise)" = true or helper "The answer to scope.passive, asked only when the question scope.business_before is answered Yes (false otherwise)" = true)
- Expr: `{"any":[{"eq":["scope.nonresident_if_noncitizen",{"const":true}],"op":"test"},{"eq":["scope.chapter11",{"const":true}],"op":"test"},{"eq":["scope.treaty",{"const":true}],"op":"test"},{"eq":["scope.reservist_repaid_if_armed_forces",{"const":true}],"op":"test"},{"eq":["scope.adoption_benefits_if_adoption",{"const":true}],"op":"test"},{"eq":["scope.wages_no_form_if_pay",{"const":true}],"op":"test"},{"eq":["scope.care_benefits_other_if_benefits",{"const":true}],"op":"test"},{"eq":["scope.disaster_distribution",{"const":true}],"op":"test"},{"eq":["scope.excess_deferral_if_w2",{"const":true}],"op":"test"},{"eq":["scope.passive_if_business_before",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 8, "Most nonresident aliens and dual-status aliens have different filing requirements and may have to file Form 1040-NR"; p. 23, Chapter 11 Bankruptcy Cases, "If you are a debtor in a chapter 11 bankruptcy case, income taxable to the bankruptcy estate"; p. 95, Line 20, "Don’t include any repayments of qualified reservist distributions"; p. 24, Line 1f, "Employer-provided adoption benefits should be shown in box 12 of your Form(s) W-2 with code T"; p. 24, Line 1e, "Dependent care benefits should be shown in box 10 of your Form(s) W-2"; i2441 p. 5, Line 12, "include amounts you received under a dependent care assistance program from your sole proprietorship or partnership"; i2441 p. 5, Line 13, "Enter on line 13 the amount you carried forward and used in 2025 during the grace period"; p. 24, Line 1h, "If the total amount you (or your spouse if filing jointly) deferred for 2025 under all plans was more than $23,500"; p. 25, Missing or Incorrect Form W-2?, "Even if you don’t get a Form W-2, you must still report your earnings"; i8915f p. 2, Purpose of Form, "If you were adversely affected by a qualified 2021 or later disaster, use Form 8915-F to report"; i8582 p. 1, Purpose of Form, "Form 8582 is used by noncorporate taxpayers to figure the amount of any passive activity loss (PAL)"; i1040s8812 p. 3, Line 18a, "Income excluded under a tax treaty is also excluded from the computation of earned income on line 18a." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.other_line16`

- **Authored helper label:** An additional Form 1040 line 16 tax or filing outside this tool (true when any of the line 16 screening questions is answered Yes)
- **Encoded (Bool):** (helper "The answer to scope.f8615, asked only when the question scope.unearned_2700 is answered Yes (false otherwise)" = true or helper "Are you (or, on a joint return, your spouse) reporting a child's 2025 interest or dividends on your own return instead of filing a return for the child?" = true or helper "In 2025, was tuition or a fee refunded, or tax-free aid given, to a student for a year for which you (or, on a joint return, your spouse) had already claimed an education credit?" = true or helper "The answer to scope.income_averaging, asked only when a business (Schedule C) is listed (false otherwise)" = true or helper "The answer to scope.pfic, asked only when the question scope.foreign_shares is answered Yes (false otherwise)" = true or helper "The answer to scope.cfc, asked only when the question scope.foreign_shares is answered Yes (false otherwise)" = true or helper "The answer to scope.f8978, asked only when the question scope.business_before is answered Yes (false otherwise)" = true)
- Expr: `{"any":[{"eq":["scope.f8615_if_unearned_2700",{"const":true}],"op":"test"},{"eq":["scope.f8814",{"const":true}],"op":"test"},{"eq":["scope.education_recapture",{"const":true}],"op":"test"},{"eq":["scope.income_averaging_if_business",{"const":true}],"op":"test"},{"eq":["scope.pfic_if_foreign_shares",{"const":true}],"op":"test"},{"eq":["scope.cfc_if_foreign_shares",{"const":true}],"op":"test"},{"eq":["scope.f8978_if_business_before",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 36, Form 8615, "You must file Form 8615 if you meet all of the following conditions"; p. 34, Line 16, "Tax from Form(s) 8814 (relating to the election to report child’s interest or dividends)", "Recapture of an education credit", "Tax with respect to a section 962 election (election made by a domestic shareholder of a controlled foreign corporation to be taxed at corporate rates)"; p. 34, Line 16, "Any tax from Form 8621, line 16e, relating to a section 1291 fund"; p. 114, Line 17p, "Enter any interest amount from Form 8621, line 16f"; p. 34, Line 16, "Tax from Form 8978, line 14 (relating to partner’s audit liability under section 6226)"; p. 36, Schedule J, "If you had income from farming or fishing, your tax may be less if you choose to figure it using income averaging on Schedule J" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `scope.ready_schedule1`

- **Authored helper label:** The Schedule 1 screening questions passed
- **Encoded (Bool):** true = true
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1. Schedule 1 income and adjustments other than the ones this tool computes (Schedule C business income, a taxable state or local income tax refund, alimony under an agreement made before 2019, unemployment compensation, the supported line 8 items, educator expenses, the HSA deduction, the deductible part of self-employment tax, self-employed SEP and SIMPLE contributions, the self-employed health insurance deduction, the early withdrawal penalty, the IRA deduction, student loan interest and jury duty pay given to your employer) are outside this tool. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready_other_income`

- **Authored helper label:** The other-income screening questions passed
- **Encoded (Bool):** true = true
- **Refusal:** when scope.other_income is true, cannot complete Form 1040 additional income/return forms. Prepare the required unsupported income or return treatment. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready_other_line16`

- **Authored helper label:** The line 16 screening questions passed
- **Encoded (Bool):** true = true
- **Refusal:** when scope.other_line16 is true, cannot complete Form 1040 line 16 additional tax forms. Prepare the applicable additional tax or alternative worksheet. Cite: [f1040] Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31 (2025; created 2025-09-05; sha256 3d31c226)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready_credits`

- **Authored helper label:** The filing status and credits screening questions passed
- **Encoded (Bool):** true = true
- **Refusal:** when s3.adoption_if_any is true, cannot complete Form 8839 (adoption credit). An adoption that became final in 2025, or adoption costs paid in 2025, can give the adoption credit (Form 8839, with its refundable part on Form 1040 line 30), which this tool does not prepare. Cite: [i8839] p. 1, Purpose of Form, "You may be able to take this credit in 2025 if any of the following statements are true" (2025; sha256 90dd5f4d)
- **Refusal:** when s3.adoption_us_if_earlier is true, cannot complete Form 8839 (adoption credit). Costs paid in 2024 toward adopting a U.S. child, where the adoption was not final at the end of 2024, are credited on the 2025 return (Form 8839), which this tool does not prepare. Cite: [i8839] p. 1, Purpose of Form, "2024 and the adoption wasn’t final at the end of 2024"; p. 3, Domestic Adoption, "the year after the year of the payment" (2025; sha256 90dd5f4d)
- **Refusal:** when s3.credit_bond is true, cannot complete Form 8912 (credit to holders of tax credit bonds). A tax credit from a bond, or one a fund passes on (Form 1097-BTC), is claimed on Form 8912, which this tool does not prepare. Cite: [i8912] p. 1, Who Can Claim the Credits, "can claim the credit by filing Form 8912 for each tax year in which it holds the bond on a credit allowance date"; p. 2, Line 1, "This amount is the total bond credits reported to you on Form(s) 1097-BTC" (December 2024 (continuous-use revision, the current one on irs.gov/pub/irs-pdf when fetched, so in force for 2025); sha256 8d4a48b7)
- **Refusal:** when s3.elderly_credit_if_asked is true, cannot complete Schedule R (credit for the elderly or the disabled). The credit for the elderly or the disabled (Schedule R) is outside this tool. To go on without the credit, answer No to that question. Cite: [i1040sr] p. 1, Qualified Individual, "You are a qualified individual for this credit if you are a U.S. citizen or resident alien" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 7194fa66)
- **Refusal:** when s3.ev_dealer_if_ev is true, cannot complete Form 8936 (clean vehicle credits). A dealer took the clean vehicle credit off the price, so Form 8936 and its Schedule A must be filed with this return; this tool does not prepare them. Cite: [i8936] p. 1, Purpose of Form, "You must file Form 8936 and Schedule A (Form 8936) if you purchased a new or used clean vehicle from a registered dealer and reduced the amount you paid at the time of sale by transferring the credit to the dealer" (2025; sha256 49aa7277)
- **Refusal:** when s3.ev_credit_if_bought is true, cannot complete Form 8936 (clean vehicle credits). This tool does not prepare the clean vehicle credits (Form 8936). To go on without the credit, answer No to that question. Cite: [i8936] p. 1, Purpose of Form, "to figure the following credits for clean vehicles you placed in service during your tax year" (2025; sha256 49aa7277)
- **Refusal:** when s3.ev_equipment_if_ev is true, cannot complete Form 8911 (alternative fuel vehicle refueling property credit). This tool does not prepare the credit for vehicle charging or fueling equipment (Form 8911). To go on without the credit, answer No to that question. Cite: [i8911] p. 1, Purpose of Form, "to figure your credit for alternative fuel vehicle refueling property you placed in service during your tax year" (December 2025 (for tax years beginning in 2025 or later); sha256 a85de224)
- **Refusal:** when s3.farmland_deferral_if_sold is true, cannot complete Form 1062 (Schedule 3 line 13z). The election to pay the tax on a sale of farmland in installments (Form 1062) is reported on Schedule 3 line 13z, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13z, "Use line 13z to report the credit under section 960(c) with respect to an excess limitation account", "Also use line 13z to report the amount of U.S. tax allocable to the U.S. Virgin Islands" and "If you made the election to defer net income tax attributable to the gain on the sale or exchange of qualified farmland property" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.section960c_if_foreign is true, cannot complete Schedule 3 line 13z (section 960(c) credit). The credit under section 960(c) is reported on Schedule 3 line 13z, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13z, "Use line 13z to report the credit under section 960(c) with respect to an excess limitation account", "Also use line 13z to report the amount of U.S. tax allocable to the U.S. Virgin Islands" and "If you made the election to defer net income tax attributable to the gain on the sale or exchange of qualified farmland property" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.section965_if_foreign is true, cannot complete Schedule 3 line 13d (net 965 tax liability). A net 965 tax liability paid in installments is reported on Schedule 3 line 13d, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13d, "If you elected to pay your net 965 tax liability in installments, report the deferred amount on line 13d" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.virgin_islands_if_foreign is true, cannot complete Form 8689 (Schedule 3 line 13z). Tax allocable to the U.S. Virgin Islands (Form 8689) is reported on Schedule 3 line 13z, which this tool does not prepare. Cite: [i1040gi] p. 117, Line 13z, "Use line 13z to report the credit under section 960(c) with respect to an excess limitation account", "Also use line 13z to report the amount of U.S. tax allocable to the U.S. Virgin Islands" and "If you made the election to defer net income tax attributable to the gain on the sale or exchange of qualified farmland property" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s3.kerosene_credit_if_kerosene is true, cannot complete Form 4136 (credit for federal tax paid on fuels). This tool does not prepare the credit for federal tax paid on fuels (Form 4136). To go on without the credit, answer No to that question. Cite: [i4136] p. 2, Part I—Information About Your Business, "If you are claiming a credit for the tax on undyed kerosene you purchased (other than from a blocked pump) and used in your home during the tax period for heating, lighting, or cooking" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 d3d63fc3)
- **Refusal:** when s3.prior_amt_if_forms is true, cannot complete Form 8801 (credit for prior year minimum tax). Alternative minimum tax on your 2024 return can give a credit for 2025 (Form 8801), which this tool does not prepare. Cite: [i8801] p. 1, Who Should File, "An AMT liability and adjustments or preferences other than exclusion items" (2025; sha256 cf99d034)
- **Refusal:** when s3.prior_forms_if_forms is true, cannot complete Credit carried from an earlier year (Form 3800, 8396, 8801, 8834, 8839, 8859 or 8912). A credit carried over from an earlier year is outside this tool. Cite: [i3800] p. 3, Carryback and Carryforward of Unused Credit, "unused general business credits may be carried back 1 year and carried forward 20 years"; f8396 p. 2, Part II—Mortgage Interest Credit Carryforward to 2026, "you may have an unused credit to carry forward to the next 3 tax years"; i8801 p. 1, Who Should File, "A credit carryforward to 2025 (on 2024 Form 8801, line 26)"; f8834 p. 2, Line 1, "Enter the qualified electric vehicle passive activity credits allowed for your current tax year from Form 8582-CR"; i8839 p. 1, Purpose of Form, "You have a carryforward of an adoption credit from 2024"; f8859 p. 1, Purpose of Form, "to claim a carryforward of the District of Columbia first-time homebuyer credit from 2024"; i8912 p. 3, Line 12, "you may carry the unused portion of the credit to the next tax year" (2025; sha256 97e4570d)
- **Refusal:** when s3.repaid_income is true, cannot complete Repayment of income of an earlier year (Schedule 3 line 13b or Schedule A line 16). A repayment of more than $3,000 of income reported in an earlier year gives a choice between a deduction and a credit (Schedule 3 line 13b), which this tool does not figure. Cite: [p525] p. 36, Repayments, "If the amount you repaid was more than $3,000, you can deduct the repayment as an other itemized deduction on Schedule A (Form 1040), line 16, if you included the income under a claim of right" and "However, you can choose to take a credit for the year of repayment"; i1040gi p. 117, Line 13b, "If you are claiming a credit for repayment of amounts you included in your income in an earlier year because it appeared you had a right to the income" (2025; sha256 39b0fa5e)
- **Refusal:** when s3.mcc_if_interest is true, cannot complete Form 8396 (mortgage interest credit). A mortgage credit certificate gives the mortgage interest credit (Form 8396), which also reduces the home mortgage interest deducted on Schedule A; this tool does not prepare it. Cite: [f8396] p. 2, Who Can Claim the Credit, "You can claim the credit only if you were issued a qualified Mortgage Credit Certificate (MCC) by a state or local governmental unit or agency"; p. 2, Line 3, "you must reduce the amount of home mortgage interest you would otherwise deduct on Schedule A by the amount on Form 8396, line 3" (2025; created 2025-08-28; sha256 5c035af7)
- Expr: `{"eq":[{"const":true},{"const":true}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `scope.ready`

- **Authored helper label:** All declared scope screens passed
- **Encoded (Bool):** helper "The Schedule 1 screening questions passed" = true and helper "The other-income screening questions passed" = true and helper "The line 16 screening questions passed" = true and helper "The filing status and credits screening questions passed" = true
- Expr: `{"all":[{"eq":["scope.ready_schedule1",{"const":true}],"op":"test"},{"eq":["scope.ready_other_income",{"const":true}],"op":"test"},{"eq":["scope.ready_other_line16",{"const":true}],"op":"test"},{"eq":["scope.ready_credits",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), the lines the screens cover: line 8, "Additional income from Schedule 1, line 10", line 10, "Adjustments to income from Schedule 1, line 26", line 13b, "Additional deductions from Schedule 1-A, line 38", line 16, "Tax (see instructions). Check if any from Form(s)", line 19, "Child tax credit or credit for other dependents from Schedule 8812", line 20, "Amount from Schedule 3, line 8", line 27a, "Earned income credit (EIC)", line 28, "Additional child tax credit (ACTC) from Schedule 8812", line 29, "American opportunity credit from Form 8863, line 8", line 30, "Refundable adoption credit from Form 8839, line 13", line 31, "Amount from Schedule 3, line 15" (2025; created 2025-09-05; sha256 3d31c226)
