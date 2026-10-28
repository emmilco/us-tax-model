# Capital Loss Carryover Worksheet—Lines 6 and 14

- Document: `clcw` (worksheet, tax year 2025)
- Note: The worksheet in the Schedule D instructions, from figures on the 2024 return. It is used only when line 21 of the 2024 Schedule D shows a loss (`sd.carryover`); lines 8 and 13 go to Schedule D lines 6 and 14. Two separate 2024 returns that each carry a loss into a 2025 joint return, and a 2024 joint return with someone other than the 2025 joint spouse, are refused.

## (helper) — `clcw.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 3, "If zero or less, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## (gate) — `clcw.spouse_screen`

- **Authored helper label:** Is either of these true: the 2024 return these figures come from was a joint return, and for 2025 you are not filing a joint return with the same spouse; or, on this 2025 joint return, you and your spouse each filed a separate 2024 return whose Schedule D line 21 showed a loss?
- **Encoded (Bool):** Input — Is either of these true: the 2024 return these figures come from was a joint return, and for 2025 you are not filing a joint return with the same spouse (for example after a divorce, a separation or the death of your spouse in 2024); or, on this 2025 joint return, you and your spouse each filed a separate 2024 return whose Schedule D line 21 showed a loss?
- Expr: `{"op":"input","source":"Is either of these true: the 2024 return these figures come from was a joint return, and for 2025 you are not filing a joint return with the same spouse (for example after a divorce, a separation or the death of your spouse in 2024); or, on this 2025 joint return, you and your spouse each filed a separate 2024 return whose Schedule D line 21 showed a loss?"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If you and your spouse once filed a joint return and are filing separate returns for 2025, any capital loss carryover from the joint return can be deducted only on the return of the spouse who actually had the loss"; p550 p. 103, Joint and separate returns, "combine your separate capital loss carryovers" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_11`

- **Authored helper label:** The amount on line 11 of your 2024 Form 1040 or 1040-SR (adjusted gross income)
- **Encoded (Dollars):** Input — The amount on line 11 of your 2024 Form 1040 or 1040-SR (your adjusted gross income for 2024), negative if it was a loss
- Interpretation: amb.2025.clcw_line1_signed
- Expr: `{"op":"input","source":"The amount on line 11 of your 2024 Form 1040 or 1040-SR (your adjusted gross income for 2024), negative if it was a loss"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 1, "Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_14`

- **Authored helper label:** The amount on line 14 of your 2024 Form 1040 or 1040-SR (your deductions)
- **Encoded (NonNegDollars):** Input — The amount on line 14 of your 2024 Form 1040 or 1040-SR (your standard or itemized deduction plus the qualified business income deduction)
- Interpretation: amb.2025.clcw_line1_signed
- Expr: `{"op":"input","source":"The amount on line 14 of your 2024 Form 1040 or 1040-SR (your standard or itemized deduction plus the qualified business income deduction)"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 1, "If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_sd7`

- **Authored helper label:** The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss)
- **Encoded (Dollars):** Input — The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss), negative if it was a loss
- Expr: `{"op":"input","source":"The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss), negative if it was a loss"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 5, "Enter the loss from your 2024 Schedule D, line 7, as a positive amount", and line 10, "Enter any gain from your 2024 Schedule D, line 7" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_sd15`

- **Authored helper label:** The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss)
- **Encoded (Dollars):** Input — The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss), negative if it was a loss
- Expr: `{"op":"input","source":"The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss), negative if it was a loss"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 6, "Enter any gain from your 2024 Schedule D, line 15", and line 9, "Enter the loss from your 2024 Schedule D, line 15, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_sd21`

- **Authored helper label:** The loss on line 21 of your 2024 Schedule D, as a positive amount
- **Encoded (NonNegDollars):** Input — The loss on line 21 of your 2024 Schedule D, entered as a positive amount (line 21 is printed in parentheses)
- Interpretation: amb.2025.clcw_line2_printed
- Expr: `{"op":"input","source":"The loss on line 21 of your 2024 Schedule D, entered as a positive amount (line 21 is printed in parentheses)"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 2, "Enter the loss from your 2024 Schedule D, line 21, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_16`

- **Authored helper label:** Line 16 of the 2024 Schedule D (lines 7 and 15 combined)
- **Encoded (Dollars):** Add helper "The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss)" and helper "The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss)".
- Expr: `{"of":["clcw.prior_sd7","clcw.prior_sd15"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "if your 2024 Schedule D, line 21, is a loss and (a) that loss is a smaller loss than the loss on your 2024 Schedule D, line 16" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_loss`

- **Authored helper label:** The loss on line 16 of the 2024 Schedule D, as a positive amount
- **Encoded (NonNegDollars):** Subtract helper "Line 16 of the 2024 Schedule D (lines 7 and 15 combined)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- Expr: `{"from":"clcw.zero","op":"subtract_floor0","take":"clcw.prior_16"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "that loss is a smaller loss than the loss on your 2024 Schedule D, line 16" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_limit`

- **Authored helper label:** The $3,000 limit on the deductible capital loss
- **Encoded (NonNegDollars):** Enter $3,000 (clcw.prior_limit).
- Expr: `{"op":"param","ref":"clcw.prior_limit"}`
- Cite: [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_limit_mfs`

- **Authored helper label:** The $1,500 limit on the deductible capital loss for a married person filing separately
- **Encoded (NonNegDollars):** Enter $1,500 (clcw.prior_limit_mfs).
- Expr: `{"op":"param","ref":"clcw.prior_limit_mfs"}`
- Cite: [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.prior_floor`

- **Authored helper label:** The least loss any 2024 Schedule D line 21 can show (the smaller of the line 16 loss and $1,500)
- **Encoded (NonNegDollars):** Enter the smaller of helper "The loss on line 16 of the 2024 Schedule D, as a positive amount" or helper "The $1,500 limit on the deductible capital loss for a married person filing separately".
- Interpretation: amb.2025.clcw_line2_printed
- Expr: `{"of":["clcw.prior_loss","clcw.prior_limit_mfs"],"op":"smaller_of"}`
- Cite: [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6)

## (gate) — `clcw.bad`

- **Authored helper label:** The loss entered for 2024 Schedule D line 21 is more than $3,000, more than the loss on 2024 Schedule D line 16, or less than the smaller of that loss and $1,500
- **Encoded (Bool):** (helper "The loss on line 21 of your 2024 Schedule D, as a positive amount" > helper "The $3,000 limit on the deductible capital loss" or helper "The loss on line 21 of your 2024 Schedule D, as a positive amount" > helper "The loss on line 16 of the 2024 Schedule D, as a positive amount" or helper "The loss on line 21 of your 2024 Schedule D, as a positive amount" < helper "The least loss any 2024 Schedule D line 21 can show (the smaller of the line 16 loss and $1,500)")
- Interpretation: amb.2025.clcw_line2_printed
- Expr: `{"any":[{"gt":["clcw.prior_sd21","clcw.prior_limit"],"op":"test"},{"gt":["clcw.prior_sd21","clcw.prior_loss"],"op":"test"},{"lt":["clcw.prior_sd21","clcw.prior_floor"],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.applies`

- **Authored helper label:** The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero)
- **Encoded (Bool):** (helper "The loss on line 21 of your 2024 Schedule D, as a positive amount" < helper "The loss on line 16 of the 2024 Schedule D, as a positive amount" or helper "The amount on line 11 of your 2024 Form 1040 or 1040-SR (adjusted gross income)" < helper "The amount on line 14 of your 2024 Form 1040 or 1040-SR (your deductions)")
- Expr: `{"any":[{"lt":["clcw.prior_sd21","clcw.prior_loss"],"op":"test"},{"lt":["clcw.prior_11","clcw.prior_14"],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "(a) that loss is a smaller loss than the loss on your 2024 Schedule D, line 16", "if the amount on your 2024 Form 1040, 1040-SR or 1040-NR, line 15 would be less than zero if you could enter a negative amount on that line", "Otherwise, you don’t have any carryovers" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.show_st`

- **Authored helper label:** The worksheet applies and line 7 of the 2024 Schedule D is a loss
- **Encoded (Bool):** helper "The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero)" = true and helper "Line 7 of your 2024 Schedule D is a loss" = true
- Expr: `{"all":[{"eq":["clcw.applies",{"const":true}],"op":"test"},{"eq":["clcw.st_loss",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If line 7 of your 2024 Schedule D is a loss, go to line 5" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.show_lt`

- **Authored helper label:** The worksheet applies and line 15 of the 2024 Schedule D is a loss
- **Encoded (Bool):** helper "The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero)" = true and helper "Line 15 of your 2024 Schedule D is a loss" = true
- Expr: `{"all":[{"eq":["clcw.applies",{"const":true}],"op":"test"},{"eq":["clcw.lt_loss",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If line 15 of your 2024 Schedule D is a loss, go to line 9" (2025; printed date 2025-12-11; sha256 650643a6)

## 1 — `clcw.line1`

- **IRS:** Your 2024 taxable income (2024 Form 1040 line 15), negative if it would have been a loss
- **Encoded (Dollars):** Subtract helper "The amount on line 14 of your 2024 Form 1040 or 1040-SR (your deductions)" from helper "The amount on line 11 of your 2024 Form 1040 or 1040-SR (adjusted gross income)".
- **Refusal:** when clcw.spouse_screen is true, cannot complete Capital Loss Carryover Worksheet for spouses' 2024 returns. A carryover from a 2024 joint return with someone other than your 2025 joint spouse, which only the spouse who had the loss can deduct, and the separate carryovers of two 2024 returns combined on a 2025 joint return, are outside this tool. Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "can be deducted only on the return of the spouse who actually had the loss"; p550 p. 103, Joint and separate returns, "combine your separate capital loss carryovers" (2025; printed date 2025-12-11; sha256 650643a6)
- **Shown on the values sheet only when:** The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero) (`clcw.applies`)
- Interpretation: amb.2025.clcw_line1_signed
- Expr: `{"from":"clcw.prior_11","op":"subtract","take":"clcw.prior_14"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 1, "Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15. If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses" (2025; printed date 2025-12-11; sha256 650643a6)

## 2 — `clcw.line2`

- **IRS:** Enter the loss from your 2024 Schedule D, line 21, as a positive amount
- **Encoded (NonNegDollars):** Enter the amount from helper "The loss on line 21 of your 2024 Schedule D, as a positive amount".
- **Refusal:** when clcw.bad is true, cannot complete Capital Loss Carryover Worksheet line 2. Check your 2024 Schedule D. Line 21 cannot be a larger loss than $3,000 or than the loss on line 16 (lines 7 and 15 combined), nor a smaller loss than the line 16 loss or $1,500, whichever is less; enter the amounts as printed on the 2024 return. Cite: [i1040sd] p. 3, Capital Losses, "You can deduct capital losses up to the amount of your capital gains plus $3,000 ($1,500 if married filing separately)" (2025; printed date 2025-12-11; sha256 650643a6)
- **Shown on the values sheet only when:** The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero) (`clcw.applies`)
- Interpretation: amb.2025.clcw_line2_printed
- Expr: `{"from":"clcw.prior_sd21","op":"copy"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 2, "Enter the loss from your 2024 Schedule D, line 21, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.combined`

- **Authored helper label:** Lines 1 and 2 combined
- **Encoded (Dollars):** Add line 1 and line 2.
- Expr: `{"of":["clcw.line1","clcw.line2"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 3, "Combine lines 1 and 2" (2025; printed date 2025-12-11; sha256 650643a6)

## 3 — `clcw.line3`

- **IRS:** Combine lines 1 and 2. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Lines 1 and 2 combined". If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero) (`clcw.applies`)
- Expr: `{"from":"clcw.combined","op":"subtract_floor0","take":"clcw.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 3, "Combine lines 1 and 2. If zero or less, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 4 — `clcw.line4`

- **IRS:** Enter the smaller of line 2 or line 3
- **Encoded (NonNegDollars):** Enter the smaller of line 2 or line 3.
- **Shown on the values sheet only when:** The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero) (`clcw.applies`)
- Expr: `{"of":["clcw.line2","clcw.line3"],"op":"smaller_of"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 4, "Enter the smaller of line 2 or line 3" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.st_loss`

- **Authored helper label:** Line 7 of your 2024 Schedule D is a loss
- **Encoded (Bool):** helper "The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss)" < $0
- Expr: `{"lt":["clcw.prior_sd7",{"const":0}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If line 7 of your 2024 Schedule D is a loss, go to line 5" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.lt_loss`

- **Authored helper label:** Line 15 of your 2024 Schedule D is a loss
- **Encoded (Bool):** helper "The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss)" < $0
- Expr: `{"lt":["clcw.prior_sd15",{"const":0}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If line 15 of your 2024 Schedule D is a loss, go to line 9" (2025; printed date 2025-12-11; sha256 650643a6)

## 5 — `clcw.line5`

- **IRS:** Enter the loss from your 2024 Schedule D, line 7, as a positive amount (zero if line 7 is not a loss)
- **Encoded (NonNegDollars):** Subtract helper "The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies (the 2024 line 21 loss is smaller than the line 16 loss, or 2024 taxable income would be less than zero) (`clcw.applies`)
- Expr: `{"from":"clcw.zero","op":"subtract_floor0","take":"clcw.prior_sd7"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 5, "Enter the loss from your 2024 Schedule D, line 7, as a positive amount", and "If line 7 of your 2024 Schedule D is a loss, go to line 5" (2025; printed date 2025-12-11; sha256 650643a6)

## 6 — `clcw.line6`

- **IRS:** Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss)". If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies and line 7 of the 2024 Schedule D is a loss (`clcw.show_st`)
- Expr: `{"from":"clcw.prior_sd15","op":"subtract_floor0","take":"clcw.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 6, "Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 7 — `clcw.line7`

- **IRS:** Add lines 4 and 6
- **Encoded (NonNegDollars):** Add line 4 and line 6.
- **Shown on the values sheet only when:** The worksheet applies and line 7 of the 2024 Schedule D is a loss (`clcw.show_st`)
- Expr: `{"of":["clcw.line4","clcw.line6"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 7, "Add lines 4 and 6" (2025; printed date 2025-12-11; sha256 650643a6)

## 8 — `clcw.line8`

- **IRS:** Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 7 from line 5. If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies and line 7 of the 2024 Schedule D is a loss (`clcw.show_st`)
- Expr: `{"from":"clcw.line5","op":"subtract_floor0","take":"clcw.line7"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 8, "Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 6" (2025; printed date 2025-12-11; sha256 650643a6)

## 9 — `clcw.line9`

- **IRS:** Enter the loss from your 2024 Schedule D, line 15, as a positive amount
- **Encoded (NonNegDollars):** Subtract helper "The amount on line 15 of your 2024 Schedule D (net long-term capital gain or loss)" from helper "Year parameter sales.zero". If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies and line 15 of the 2024 Schedule D is a loss (`clcw.show_lt`)
- Expr: `{"from":"clcw.zero","op":"subtract_floor0","take":"clcw.prior_sd15"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 9, "Enter the loss from your 2024 Schedule D, line 15, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## 10 — `clcw.line10`

- **IRS:** Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "The amount on line 7 of your 2024 Schedule D (net short-term capital gain or loss)". If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies and line 15 of the 2024 Schedule D is a loss (`clcw.show_lt`)
- Expr: `{"from":"clcw.prior_sd7","op":"subtract_floor0","take":"clcw.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 10, "Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 11 — `clcw.line11`

- **IRS:** Subtract line 5 from line 4. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 5 from line 4. If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies and line 15 of the 2024 Schedule D is a loss (`clcw.show_lt`)
- Expr: `{"from":"clcw.line4","op":"subtract_floor0","take":"clcw.line5"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 11, "Subtract line 5 from line 4. If zero or less, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 12 — `clcw.line12`

- **IRS:** Add lines 10 and 11
- **Encoded (NonNegDollars):** Add line 10 and line 11.
- **Shown on the values sheet only when:** The worksheet applies and line 15 of the 2024 Schedule D is a loss (`clcw.show_lt`)
- Expr: `{"of":["clcw.line10","clcw.line11"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 12, "Add lines 10 and 11" (2025; printed date 2025-12-11; sha256 650643a6)

## 13 — `clcw.line13`

- **IRS:** Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 12 from line 9. If zero or less, enter -0-.
- **Shown on the values sheet only when:** The worksheet applies and line 15 of the 2024 Schedule D is a loss (`clcw.show_lt`)
- Expr: `{"from":"clcw.line9","op":"subtract_floor0","take":"clcw.line12"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 13, "Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 14" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw.figures_notice`

- **Authored helper label:** Notice: the carryover is figured from the 2024 amounts you entered. If you did not file a 2024 return, or your 2024 Schedule D left out a capital loss carried into 2024, they must be the amounts a correct 2024 return would have shown.
- **Encoded (Bool):** sd helper "Did line 21 of your 2024 Schedule D show a loss?" = true
- Expr: `{"eq":["sd.carryover",{"const":true}],"op":"test"}`
- Cite: [p550] p. 102, Capital Losses, "you must take the current year's allowable deduction into account, whether or not you claimed it and whether or not you filed a return for the current year" (2025 returns; printed date 2026-03-05; sha256 83552968)
