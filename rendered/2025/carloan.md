# Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan

- Document: `carloan` (form, tax year 2025)
- Collection: keyed entries; [i1040gi] p. 110, Schedule 1-A, line 22, "If you need to report more than two VINs, attach a statement to your return showing the information required on line 22"; "for each entered VIN, enter the QPVLI paid or accrued on the loan originated for the purchase of that APV" (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: One entry per loan; name each entry by the vehicle's VIN (a vehicle with a loan refinanced during 2025 has one entry for each loan). Interest deducted on Schedule C (column (ii)) is asked when the return has a Schedule C; Schedules E and F are refused. Where a loan also financed amounts that do not qualify, or refinanced a qualifying loan for more than its balance, the interest is allocated pro rata under proposed § 1.163-16(d)(2)(iii) and (d)(4); the ratio is rounded to six places (amb.2025.carloan_ratio_places).

## (helper) — `carloan.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `carloan.kind`

- **Authored helper label:** How you came to owe this loan
- **Encoded (Enum(carloan_kind)):** Input — How you came to owe this loan: original (you took out this loan after December 31, 2024, to buy the vehicle); refinanced (this loan refinanced such a loan and is secured by a first lien on the same vehicle); death (you became the borrower because a previous borrower died, for example by inheriting the vehicle or as its surviving joint owner, and the loan met the requirements when it was taken out)
- Expr: `{"op":"input","source":"How you came to owe this loan: original (you took out this loan after December 31, 2024, to buy the vehicle); refinanced (this loan refinanced such a loan and is secured by a first lien on the same vehicle); death (you became the borrower because a previous borrower died, for example by inheriting the vehicle or as its surviving joint owner, and the loan met the requirements when it was taken out)"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4) and (d)(5); i1040gi p. 109, Schedule 1-A, "Change in obligor by reason of previous obligor's death" and "Refinanced loan" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.requirements`

- **Authored helper label:** Does this loan meet the loan requirements?
- **Encoded (Bool):** Input — Does this loan meet all of these: it was originated after December 31, 2024 (for a refinancing, the loan it refinanced was); it was used to buy the vehicle (lease payments do not qualify); it is secured by a first lien on the vehicle; it is not owed to a person related to you (Internal Revenue Code section 267(b) or 707(b)(1)); and when the loan was taken out you expected the vehicle to be used more than 50% of the time for personal use (not in a trade or business other than as an employee, and not to produce income) by you or certain relatives or members of your household?
- Expr: `{"op":"input","source":"Does this loan meet all of these: it was originated after December 31, 2024 (for a refinancing, the loan it refinanced was); it was used to buy the vehicle (lease payments do not qualify); it is secured by a first lien on the vehicle; it is not owed to a person related to you (Internal Revenue Code section 267(b) or 707(b)(1)); and when the loan was taken out you expected the vehicle to be used more than 50% of the time for personal use (not in a trade or business other than as an employee, and not to produce income) by you or certain relatives or members of your household?"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Qualified passenger vehicle loan interest, requirements 1 to 5, and Personal use; fr-2025-24154 proposed § 1.163-16(d)(3) (related party indebtedness) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `carloan.vehicle`

- **Authored helper label:** Is the vehicle an applicable passenger vehicle?
- **Encoded (Bool):** Input — Is the vehicle all of these: new, with its original use starting with you (a used vehicle does not qualify; the loan documents treat it as new); made primarily for use on public streets, roads and highways (not only on rails); with at least 2 wheels; a car, minivan, van, SUV, pickup truck or motorcycle; with a gross vehicle weight rating under 14,000 pounds; and finally assembled in the United States (shown on the vehicle information label, or by the plant of manufacture in the VIN)?
- Expr: `{"op":"input","source":"Is the vehicle all of these: new, with its original use starting with you (a used vehicle does not qualify; the loan documents treat it as new); made primarily for use on public streets, roads and highways (not only on rails); with at least 2 wheels; a car, minivan, van, SUV, pickup truck or motorcycle; with a gross vehicle weight rating under 14,000 pounds; and finally assembled in the United States (shown on the vehicle information label, or by the plant of manufacture in the VIN)?"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Applicable passenger vehicle and Final assembly in the United States; fr-2025-24154 proposed § 1.163-16(e)(1) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `carloan.eligible`

- **Authored helper label:** The loan and the vehicle qualify
- **Encoded (Bool):** helper "Does this loan meet the loan requirements?" = true and helper "Is the vehicle an applicable passenger vehicle?" = true
- Expr: `{"all":[{"eq":["carloan.requirements",{"const":true}],"op":"test"},{"eq":["carloan.vehicle",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Qualified passenger vehicle loan interest and Applicable passenger vehicle (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `carloan.interest`

- **Authored helper label:** Interest you paid or accrued on this loan in 2025
- **Encoded (NonNegDollars):** Input — Total interest you paid or accrued on this loan in 2025 (generally from the lender's statement), including any part you deduct on Schedule C (that part is entered separately)
- Expr: `{"op":"input","source":"Total interest you paid or accrued on this loan in 2025 (generally from the lender's statement), including any part you deduct on Schedule C (that part is entered separately)"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, column (iii), "the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `carloan.mixed`

- **Authored helper label:** Did this loan also finance amounts that do not qualify?
- **Encoded (Bool):** Input — Did this loan also finance anything other than the vehicle and items customarily financed with it and directly related to it (such as a service plan, extended warranty, sales tax and vehicle fees)? For example negative equity on a vehicle traded in, collision or liability insurance, a trailer or other unrelated property, or cash paid to you.
- Expr: `{"op":"input","source":"Did this loan also finance anything other than the vehicle and items customarily financed with it and directly related to it (such as a service plan, extended warranty, sales tax and vehicle fees)? For example negative equity on a vehicle traded in, collision or liability insurance, a trailer or other unrelated property, or cash paid to you."}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(i) and (ii); i1040gi p. 109, Schedule 1-A, Loan amount (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.financed`

- **Authored helper label:** Total amount of this loan when it was taken out
- **Encoded (NonNegDollars):** Input — The total amount financed by this loan when it was taken out (the indebtedness incurred, after any down payment)
- Expr: `{"op":"input","source":"The total amount financed by this loan when it was taken out (the indebtedness incurred, after any down payment)"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(A) and (d)(4); (d)(6) Examples 3 and 4 (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.nonqualifying`

- **Authored helper label:** Amounts in the purchase that do not qualify
- **Encoded (NonNegDollars):** Input — The total of the amounts in the purchase that do not qualify (negative equity, insurance, unrelated property, cash paid to you), before applying any down payment
- Expr: `{"op":"input","source":"The total of the amounts in the purchase that do not qualify (negative equity, insurance, unrelated property, cash paid to you), before applying any down payment"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(ii) and (d)(6) Example 4 (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.down`

- **Authored helper label:** Down payment
- **Encoded (NonNegDollars):** Input — Any down payment or other consideration you provided when you bought the vehicle (zero if none)
- Expr: `{"op":"input","source":"Any down payment or other consideration you provided when you bought the vehicle (zero if none)"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(B), "any down payment ... is applied first against any negative equity and any other amounts that are not incurred for the purchase of the APV" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.nonqualifying_debt`

- **Authored helper label:** Nonqualifying amounts less the down payment applied first against them
- **Encoded (NonNegDollars):** Subtract helper "Down payment" from helper "Amounts in the purchase that do not qualify". If zero or less, enter -0-.
- Expr: `{"from":"carloan.nonqualifying","op":"subtract_floor0","take":"carloan.down"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(B) and (d)(6) Example 4 (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.mixed_qualifying`

- **Authored helper label:** Part of the loan that is a specified passenger vehicle loan
- **Encoded (NonNegDollars):** Subtract helper "Nonqualifying amounts less the down payment applied first against them" from helper "Total amount of this loan when it was taken out". If zero or less, enter -0-.
- Expr: `{"from":"carloan.financed","op":"subtract_floor0","take":"carloan.nonqualifying_debt"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(A), "Only the portion of the indebtedness allocated to the indebtedness described in paragraph (d)(2)(i) of this section is an SPVL"; p. 22, Example 4, "Negative equity and down payment", "the down payment of $4,000 is allocated against the $6,000 of negative equity" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.refi_balance`

- **Authored helper label:** Outstanding balance of the refinanced loan when it was refinanced
- **Encoded (NonNegDollars):** Input — The outstanding balance of the loan this loan refinanced, on the date of the refinancing
- Expr: `{"op":"input","source":"The outstanding balance of the loan this loan refinanced, on the date of the refinancing"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4), "The amount of the new loan that is an SPVL is limited to the outstanding balance of the refinanced loan as of the date of the refinancing" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.refi_whole`

- **Authored helper label:** Was all of the refinanced loan a specified passenger vehicle loan?
- **Encoded (Bool):** Input — Was all of the loan this loan refinanced a qualifying vehicle loan (it financed only the vehicle and items customarily financed with it, and was not itself a refinancing for more than the balance it replaced)?
- Expr: `{"op":"input","source":"Was all of the loan this loan refinanced a qualifying vehicle loan (it financed only the vehicle and items customarily financed with it, and was not itself a refinancing for more than the balance it replaced)?"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4), "If a taxpayer refinances an SPVL" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.refi_qualifying`

- **Authored helper label:** Part of the new loan that is a specified passenger vehicle loan
- **Encoded (NonNegDollars):** Enter the smaller of helper "Outstanding balance of the refinanced loan when it was refinanced" or helper "Total amount of this loan when it was taken out".
- **Refusal:** when carloan.refi_nested is true, cannot complete Refinancing of a loan that was itself only partly a qualifying vehicle loan. Allocating a refinancing of a partly qualifying loan is outside this tool. Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii) and (d)(4) (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)
- Expr: `{"of":["carloan.refi_balance","carloan.financed"],"op":"smaller_of"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4) and (d)(6) Example 3 (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (gate) — `carloan.refi_nested`

- **Authored helper label:** The refinanced loan was itself only partly a qualifying loan
- **Encoded (Bool):** helper "Was all of the refinanced loan a specified passenger vehicle loan?" = false
- Expr: `{"eq":["carloan.refi_whole",{"const":false}],"op":"test"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4) (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.allocated`

- **Authored helper label:** Interest allocated pro rata to the qualifying part of the loan
- **Encoded (NonNegDollars):** Choose — [helper "How you came to owe this loan" = 'original' → helper "Interest times the qualifying part of the loan divided by the loan, the ratio rounded to six places"] [helper "How you came to owe this loan" = 'refinanced' → helper "Interest times the qualifying part of the new loan divided by the new loan, the ratio rounded to six places"] [helper "How you came to owe this loan" = 'death' → helper "Interest times the qualifying part of the loan divided by the loan, the ratio rounded to six places"]
- Expr: `{"alternatives":[{"guard":{"eq":["carloan.kind",{"const":"original"}],"op":"test"},"then":"carloan.mixed_interest"},{"guard":{"eq":["carloan.kind",{"const":"refinanced"}],"op":"test"},"then":"carloan.refi_interest"},{"guard":{"eq":["carloan.kind",{"const":"death"}],"op":"test"},"then":"carloan.mixed_interest"}],"op":"choose"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(A) and (d)(4), "payments of interest and principal are allocated ... on a pro rata basis" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.refi_interest`

- **Authored helper label:** Interest times the qualifying part of the new loan divided by the new loan, the ratio rounded to six places
- **Encoded (NonNegDollars):** Divide helper "Part of the new loan that is a specified passenger vehicle loan" by helper "Total amount of this loan when it was taken out", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Interest you paid or accrued on this loan in 2025" by the result.
- Interpretation: amb.2025.carloan_ratio_places
- Expr: `{"amount":"carloan.interest","op":"prorate","part":"carloan.refi_qualifying","places":6,"whole":"carloan.financed"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(4), "A taxpayer allocates principal and interest between the amount of the new loan that is an SPVL and the remaining portion of the indebtedness on a pro rata basis" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.mixed_interest`

- **Authored helper label:** Interest times the qualifying part of the loan divided by the loan, the ratio rounded to six places
- **Encoded (NonNegDollars):** Choose — [helper "Did this loan also finance amounts that do not qualify?" = false → helper "Interest you paid or accrued on this loan in 2025"] [helper "Did this loan also finance amounts that do not qualify?" = true → helper "Interest times the qualifying part of the loan divided by the loan, the ratio rounded to six places"]
- Expr: `{"alternatives":[{"guard":{"eq":["carloan.mixed",{"const":false}],"op":"test"},"then":"carloan.interest"},{"guard":{"eq":["carloan.mixed",{"const":true}],"op":"test"},"then":"carloan.mixed_prorated"}],"op":"choose"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(A) and (d)(6) Examples 1, 2 and 4 (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.mixed_prorated`

- **Authored helper label:** Interest times the qualifying part of the loan divided by the loan, the ratio rounded to six places
- **Encoded (NonNegDollars):** Divide helper "Part of the loan that is a specified passenger vehicle loan" by helper "Total amount of this loan when it was taken out", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "Interest you paid or accrued on this loan in 2025" by the result.
- Interpretation: amb.2025.carloan_ratio_places
- Expr: `{"amount":"carloan.interest","op":"prorate","part":"carloan.mixed_qualifying","places":6,"whole":"carloan.financed"}`
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(A), "payments of interest and principal are allocated to the portion of the indebtedness described in paragraph (d)(2)(i) ... and the portion ... described in paragraph (d)(2)(ii) ... on a pro rata basis" (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## (helper) — `carloan.qpvli`

- **Authored helper label:** Interest for this loan, Schedule 1-A
- **Encoded (NonNegDollars):** Choose — [helper "The loan and the vehicle qualify" = false → helper "Year parameter sales.zero"] [helper "The loan and the vehicle qualify" = true → helper "Interest allocated pro rata to the qualifying part of the loan"]
- Expr: `{"alternatives":[{"guard":{"eq":["carloan.eligible",{"const":false}],"op":"test"},"then":"carloan.zero"},{"guard":{"eq":["carloan.eligible",{"const":true}],"op":"test"},"then":"carloan.allocated"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, column (iii), "On line 22, column (iii), enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)" (column (ii), interest deducted on Schedule C, E or F, is outside this tool: scope.schedule1) (2025; printed date 2026-02-25; sha256 482e9c48)

## 22(ii) — `carloan.col_ii_input`

- **IRS:** Interest on this loan deducted on Schedule C
- **Encoded (NonNegDollars):** Input — The part of this loan's 2025 interest you deduct on Schedule C (the business use of the vehicle; zero if none)
- Expr: `{"op":"input","source":"The part of this loan's 2025 interest you deduct on Schedule C (the business use of the vehicle; zero if none)"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, column (ii), "enter the amount of the QPVLI, if any, that was deducted elsewhere on your return (for example, on Schedule C, Schedule E, or Schedule F)"; i1040sc p. 6, Line 9, Caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `carloan.col_ii`

- **Authored helper label:** Interest deducted on Schedule C (zero without a Schedule C)
- **Encoded (NonNegDollars):** Choose — [s1 helper "The return has a Schedule C" = true → line 22(ii)] [s1 helper "The return has a Schedule C" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1.has_sc",{"const":true}],"op":"test"},"then":"carloan.col_ii_input"},{"guard":{"eq":["s1.has_sc",{"const":false}],"op":"test"},"then":"carloan.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, column (ii) (2025; printed date 2026-02-25; sha256 482e9c48)

## 22(iii) — `carloan.col_iii`

- **IRS:** Qualified passenger vehicle loan interest less the amount in column (ii)
- **Encoded (NonNegDollars):** Subtract helper "Interest deducted on Schedule C (zero without a Schedule C)" from helper "Interest for this loan, Schedule 1-A". If zero or less, enter -0-.
- Expr: `{"from":"carloan.qpvli","op":"subtract_floor0","take":"carloan.col_ii"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, column (iii), "the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)" (2025; printed date 2026-02-25; sha256 482e9c48)
