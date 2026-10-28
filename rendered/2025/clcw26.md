# Capital loss carryover to 2026 (Capital Loss Carryover Worksheet applied to this return)

- Document: `clcw26` (worksheet, tax year 2025)
- Note: The carryovers to 2026, shown on the values sheet and read by no other line. The Schedule D instructions point to the 2026 worksheet or Pub. 550; the 13 lines of the 2025 worksheet are applied to this return with each 2024 figure read as the 2025 one (amb.2025.clcw_to_2026). Shown only when the instructions' test for a carryover to 2026 holds.

## (helper) — `clcw26.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 3, "If zero or less, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw26.show`

- **Authored helper label:** Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured
- **Encoded (Bool):** sd helper "Line 16 is a loss" = true and (sd line 16 < sd line 21 or f1040 line 11b < f1040 line 14)
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"all":[{"eq":["sd.has_loss",{"const":true}],"op":"test"},{"any":[{"lt":["sd.line16","sd.line21"],"op":"test"},{"lt":["f1040.line11b","f1040.line14"],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 14, Line 21, "You have a capital loss carryover from 2025 to 2026 if you have a loss on line 16 and either", "That loss is more than the loss on line 21", "The amount on Form 1040, 1040-SR, or 1040-NR, line 15, would be less than zero if you could enter a negative amount on that line" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw26.show_st`

- **Authored helper label:** Schedule D line 16 and line 7 are losses
- **Encoded (Bool):** helper "Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured" = true and sd line 7 < $0
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"all":[{"eq":["clcw26.show",{"const":true}],"op":"test"},{"lt":["sd.line7",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If line 7 of your 2024 Schedule D is a loss, go to line 5" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw26.show_lt`

- **Authored helper label:** Schedule D line 16 and line 15 are losses
- **Encoded (Bool):** helper "Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured" = true and sd line 15 < $0
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"all":[{"eq":["clcw26.show",{"const":true}],"op":"test"},{"lt":["sd.line15",{"const":0}],"op":"test"}],"op":"test"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, "If line 15 of your 2024 Schedule D is a loss, go to line 9" (2025; printed date 2025-12-11; sha256 650643a6)

## 1 — `clcw26.line1`

- **IRS:** Form 1040 line 15 for 2025, negative if it would have been a loss (line 11b less line 14)
- **Encoded (Dollars):** Subtract f1040 line 14 from f1040 line 11b.
- **Shown on the values sheet only when:** Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured (`clcw26.show`)
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"from":"f1040.line11b","op":"subtract","take":"f1040.line14"}`
- Cite: [i1040sd] p. 14, Line 21, "The amount on Form 1040, 1040-SR, or 1040-NR, line 15, would be less than zero if you could enter a negative amount on that line" (2025; printed date 2025-12-11; sha256 650643a6)

## 2 — `clcw26.line2`

- **IRS:** The loss on Schedule D line 21, as a positive amount
- **Encoded (NonNegDollars):** Subtract sd line 21 from helper "Year parameter sales.zero". If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured (`clcw26.show`)
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"from":"clcw26.zero","op":"subtract_floor0","take":"sd.line21"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 2, "Enter the loss from your 2024 Schedule D, line 21, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw26.combined`

- **Authored helper label:** Lines 1 and 2 combined
- **Encoded (Dollars):** Add line 1 and line 2.
- Expr: `{"of":["clcw26.line1","clcw26.line2"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 3, "Combine lines 1 and 2" (2025; printed date 2025-12-11; sha256 650643a6)

## 3 — `clcw26.line3`

- **IRS:** Combine lines 1 and 2. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from helper "Lines 1 and 2 combined". If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured (`clcw26.show`)
- Expr: `{"from":"clcw26.combined","op":"subtract_floor0","take":"clcw26.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 3, "Combine lines 1 and 2. If zero or less, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 4 — `clcw26.line4`

- **IRS:** Enter the smaller of line 2 or line 3
- **Encoded (NonNegDollars):** Enter the smaller of line 2 or line 3.
- **Shown on the values sheet only when:** Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured (`clcw26.show`)
- Expr: `{"of":["clcw26.line2","clcw26.line3"],"op":"smaller_of"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 4, "Enter the smaller of line 2 or line 3" (2025; printed date 2025-12-11; sha256 650643a6)

## 5 — `clcw26.line5`

- **IRS:** The loss on Schedule D line 7, as a positive amount (zero if line 7 is not a loss)
- **Encoded (NonNegDollars):** Subtract sd line 7 from helper "Year parameter sales.zero". If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 is a loss that is more than the loss on line 21, or taxable income would be less than zero, so a carryover to 2026 is figured (`clcw26.show`)
- Expr: `{"from":"clcw26.zero","op":"subtract_floor0","take":"sd.line7"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 5, "Enter the loss from your 2024 Schedule D, line 7, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## 6 — `clcw26.line6`

- **IRS:** Any gain on Schedule D line 15. If a loss, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from sd line 15. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 and line 7 are losses (`clcw26.show_st`)
- Expr: `{"from":"sd.line15","op":"subtract_floor0","take":"clcw26.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 6, "Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 7 — `clcw26.line7`

- **IRS:** Add lines 4 and 6
- **Encoded (NonNegDollars):** Add line 4 and line 6.
- **Shown on the values sheet only when:** Schedule D line 16 and line 7 are losses (`clcw26.show_st`)
- Expr: `{"of":["clcw26.line4","clcw26.line6"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 7, "Add lines 4 and 6" (2025; printed date 2025-12-11; sha256 650643a6)

## 8 — `clcw26.line8`

- **IRS:** Short-term capital loss carryover to 2026. Subtract line 7 from line 5. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 7 from line 5. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 and line 7 are losses (`clcw26.show_st`)
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"from":"clcw26.line5","op":"subtract_floor0","take":"clcw26.line7"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 8, "Subtract line 7 from line 5. If zero or less, enter -0-"; p. 14, Line 21, "If you want to figure your carryover to 2026 now, see Pub. 550" (2025; printed date 2025-12-11; sha256 650643a6)

## 9 — `clcw26.line9`

- **IRS:** The loss on Schedule D line 15, as a positive amount
- **Encoded (NonNegDollars):** Subtract sd line 15 from helper "Year parameter sales.zero". If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 and line 15 are losses (`clcw26.show_lt`)
- Expr: `{"from":"clcw26.zero","op":"subtract_floor0","take":"sd.line15"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 9, "Enter the loss from your 2024 Schedule D, line 15, as a positive amount" (2025; printed date 2025-12-11; sha256 650643a6)

## 10 — `clcw26.line10`

- **IRS:** Any gain on Schedule D line 7. If a loss, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sales.zero" from sd line 7. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 and line 15 are losses (`clcw26.show_lt`)
- Expr: `{"from":"sd.line7","op":"subtract_floor0","take":"clcw26.zero"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 10, "Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 11 — `clcw26.line11`

- **IRS:** Subtract line 5 from line 4. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 5 from line 4. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 and line 15 are losses (`clcw26.show_lt`)
- Expr: `{"from":"clcw26.line4","op":"subtract_floor0","take":"clcw26.line5"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 11, "Subtract line 5 from line 4. If zero or less, enter -0-" (2025; printed date 2025-12-11; sha256 650643a6)

## 12 — `clcw26.line12`

- **IRS:** Add lines 10 and 11
- **Encoded (NonNegDollars):** Add line 10 and line 11.
- **Shown on the values sheet only when:** Schedule D line 16 and line 15 are losses (`clcw26.show_lt`)
- Expr: `{"of":["clcw26.line10","clcw26.line11"],"op":"sum"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 12, "Add lines 10 and 11" (2025; printed date 2025-12-11; sha256 650643a6)

## 13 — `clcw26.line13`

- **IRS:** Long-term capital loss carryover to 2026. Subtract line 12 from line 9. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 12 from line 9. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Schedule D line 16 and line 15 are losses (`clcw26.show_lt`)
- Interpretation: amb.2025.clcw_to_2026
- Expr: `{"from":"clcw26.line9","op":"subtract_floor0","take":"clcw26.line12"}`
- Cite: [i1040sd] p. 10, Capital Loss Carryover Worksheet—Lines 6 and 14, line 13, "Subtract line 12 from line 9. If zero or less, enter -0-"; p. 14, Line 21, "If you want to figure your carryover to 2026 now, see Pub. 550" (2025; printed date 2025-12-11; sha256 650643a6)

## (helper) — `clcw26.decedent_notice`

- **Authored helper label:** Notice: if your spouse died in 2025, the part of these carryovers that came from your spouse's losses does not carry over to 2026; it can be deducted only on this return.
- **Encoded (Bool):** f1040 line Filing Status = 'mfj' and (line 8 > $0 or line 13 > $0)
- Expr: `{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"any":[{"gt":["clcw26.line8",{"const":0}],"op":"test"},{"gt":["clcw26.line13",{"const":0}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [p550] p. 103, Decedent's capital loss, "can be deducted only on the final income tax return filed for the decedent" (2025 returns; printed date 2026-03-05; sha256 83552968)
