# Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student

- Document: `aqee` (def, tax year 2025)
- Parameters: inst, mat, adj

## (helper) — `inst`

- **Authored helper label:** Qualified education expenses required to be paid to the institution (tuition, fees, and books, supplies and equipment required as a condition of enrollment or attendance)
- **Encoded (NonNegDollars):** Input — Bound by the calling line (this student's expenses required to be paid to the institution).
- Expr: `{"op":"input","source":"Bound by the calling line (this student's expenses required to be paid to the institution)."}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "Lifetime learning credit: Qualified education expenses include amounts paid for books, supplies, and equipment only if required to be paid to the institution as a condition of enrollment or attendance." (2025; sha256 195cfd5e)

## (helper) — `mat`

- **Authored helper label:** Other course materials needed for a course of study (books, supplies and equipment not required to be paid to the institution; American opportunity credit only)
- **Encoded (NonNegDollars):** Input — Bound by the calling line (this student's other course materials).
- Expr: `{"op":"input","source":"Bound by the calling line (this student's other course materials)."}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "American opportunity credit: Qualified education expenses include amounts paid for tuition, fees, and course materials, which include books, supplies, and equipment needed for a course of study, whether or not the materials are purchased from the educational institution as a condition of enrollment or attendance." (2025; sha256 195cfd5e)

## (helper) — `adj`

- **Authored helper label:** Worksheet line 3: total adjustments (lines 2a, 2b and 2c)
- **Encoded (NonNegDollars):** Input — Bound by the calling line (this student's tax-free educational assistance and refunds).
- Expr: `{"op":"input","source":"Bound by the calling line (this student's tax-free educational assistance and refunds)."}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (helper) — `ws1_aoc`

- **Authored helper label:** Worksheet line 1 for the American opportunity credit: total qualified education expenses (tuition, fees and course materials)
- **Encoded (NonNegDollars):** Add helper "Qualified education expenses required to be paid to the institution (tuition, fees, and books, supplies and equipment required as a condition of enrollment or attendance)" and helper "Other course materials needed for a course of study (books, supplies and equipment not required to be paid to the institution; American opportunity credit only)".
- Expr: `{"of":["inst","mat"],"op":"sum"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "1. Total qualified education expenses paid for or on behalf of the student in 2025 for the academic period" (2025; sha256 195cfd5e)

## (helper) — `ws4_aoc`

- **Authored helper label:** Worksheet line 4 for the American opportunity credit: subtract line 3 from line 1; if zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Worksheet line 3: total adjustments (lines 2a, 2b and 2c)" from helper "Worksheet line 1 for the American opportunity credit: total qualified education expenses (tuition, fees and course materials)". If zero or less, enter -0-.
- Expr: `{"from":"ws1_aoc","op":"subtract_floor0","take":"adj"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "4. Adjusted qualified education expenses. Subtract line 3 from line 1. If zero or less, enter -0-" (2025; sha256 195cfd5e)

## (helper) — `ws4_llc`

- **Authored helper label:** Worksheet line 4 for the lifetime learning credit: the expenses required to be paid to the institution less line 3; if zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Worksheet line 3: total adjustments (lines 2a, 2b and 2c)" from helper "Qualified education expenses required to be paid to the institution (tuition, fees, and books, supplies and equipment required as a condition of enrollment or attendance)". If zero or less, enter -0-.
- Expr: `{"from":"inst","op":"subtract_floor0","take":"adj"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "4. Adjusted qualified education expenses. Subtract line 3 from line 1. If zero or less, enter -0-" (2025; sha256 195cfd5e)

## (helper) — `cap`

- **Authored helper label:** Year parameter aoc.expense_cap ($4,000)
- **Encoded (NonNegDollars):** Enter $4,000 (aoc.expense_cap).
- Expr: `{"op":"param","ref":"aoc.expense_cap"}`
- Cite: [f8863] p. 2, Part III, line 27, "Adjusted qualified education expenses (see instructions). Don’t enter more than $4,000" (2025; sha256 a251a1cf)

## (helper) — `band`

- **Authored helper label:** Year parameter aoc.full_band ($2,000)
- **Encoded (NonNegDollars):** Enter $2,000 (aoc.full_band).
- Expr: `{"op":"param","ref":"aoc.full_band"}`
- Cite: [f8863] p. 2, Part III, line 28, "Subtract $2,000 from line 27. If zero or less, enter -0-" (2025; sha256 a251a1cf)

## (helper) — `rate25`

- **Authored helper label:** Year parameter aoc.second_rate (25%)
- **Encoded (Rate):** Enter 25% (0.25) (aoc.second_rate).
- Expr: `{"op":"param","ref":"aoc.second_rate"}`
- Cite: [f8863] p. 2, Part III, line 29, "Multiply line 28 by 25% (0.25)" (2025; sha256 a251a1cf)

## (helper) — `zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f8863] p. 2, Part III, line 30, "If line 28 is zero, enter the amount from line 27." (2025; sha256 a251a1cf)

## 27 — `line27`

- **IRS:** Adjusted qualified education expenses. Don't enter more than $4,000
- **Encoded (NonNegDollars):** Enter the smaller of helper "Worksheet line 4 for the American opportunity credit: subtract line 3 from line 1; if zero or less, enter -0-" or helper "Year parameter aoc.expense_cap ($4,000)".
- Expr: `{"of":["ws4_aoc","cap"],"op":"smaller_of"}`
- Cite: [f8863] p. 2, Part III, line 27, "Adjusted qualified education expenses (see instructions). Don’t enter more than $4,000" (2025; sha256 a251a1cf)

## 28 — `line28`

- **IRS:** Subtract $2,000 from line 27. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter aoc.full_band ($2,000)" from line 27. If zero or less, enter -0-.
- Expr: `{"from":"line27","op":"subtract_floor0","take":"band"}`
- Cite: [f8863] p. 2, Part III, line 28, "Subtract $2,000 from line 27. If zero or less, enter -0-" (2025; sha256 a251a1cf)

## 29 — `line29`

- **IRS:** Multiply line 28 by 25% (0.25)
- **Encoded (NonNegDollars):** Multiply line 28 by helper "Year parameter aoc.second_rate (25%)".
- Expr: `{"amount":"line28","op":"multiply_rate","rate":"rate25"}`
- Cite: [f8863] p. 2, Part III, line 29, "Multiply line 28 by 25% (0.25)" (2025; sha256 a251a1cf)

## (helper) — `line29_plus`

- **Authored helper label:** Add $2,000 to the amount on line 29
- **Encoded (NonNegDollars):** Add line 29 and helper "Year parameter aoc.full_band ($2,000)".
- Expr: `{"of":["line29","band"],"op":"sum"}`
- Cite: [f8863] p. 2, Part III, line 30, "Otherwise, add $2,000 to the amount on line 29 and enter the result." (2025; sha256 a251a1cf)

## (helper) — `line28_zero`

- **Authored helper label:** Line 28 is zero
- **Encoded (Bool):** line 28 = $0
- Expr: `{"eq":["line28",{"const":0}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 30, "If line 28 is zero, enter the amount from line 27." (2025; sha256 a251a1cf)

## 30 — `line30`

- **IRS:** If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29
- **Encoded (NonNegDollars):** Choose — [helper "Line 28 is zero" = true → line 27] [helper "Line 28 is zero" = false → helper "Add $2,000 to the amount on line 29"]
- Expr: `{"alternatives":[{"guard":{"eq":["line28_zero",{"const":true}],"op":"test"},"then":"line27"},{"guard":{"eq":["line28_zero",{"const":false}],"op":"test"},"then":"line29_plus"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 30, "If line 28 is zero, enter the amount from line 27.", "Otherwise, add $2,000 to the amount on line 29 and enter the result." (2025; sha256 a251a1cf)
