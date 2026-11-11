# Social Security Benefits Worksheet—Lines 6a and 6b

- Document: `ssb` (worksheet, tax year 2025)
- Note: The worksheet of the Form 1040 instructions; the exceptions that send a filer to Pub. 915 or Pub. 590-A, and the lump-sum election, are refused.

## (helper) — `ssb.benefits`

- **Authored helper label:** Net benefits: total of box 5 of all your Forms SSA-1099 and RRB-1099
- **Encoded (NonNegDollars):** Input — Total of box 5 (net benefits) of all your (or, on a joint return, your spouse's) Forms SSA-1099 and RRB-1099 for 2025
- Expr: `{"op":"input","source":"Total of box 5 (net benefits) of all your (or, on a joint return, your spouse's) Forms SSA-1099 and RRB-1099 for 2025"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 1; p. 31, Lines 6a and 6b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.pub915`

- **Authored helper label:** Does any of these apply: you (or, on a joint return, your spouse) made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment; your social security repayments in 2025 (box 4) were more than your benefits (box 3); you (or, on a joint return, your spouse) file Form 2555, 4563 or 8815; or you (or, on a joint return, your spouse) exclude employer-provided adoption benefits or income from sources within Puerto Rico?
- **Encoded (Bool):** Input — Does any of these apply: you (or, on a joint return, your spouse) made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment; your social security repayments in 2025 (box 4) were more than your benefits (box 3); you (or, on a joint return, your spouse) file Form 2555, 4563 or 8815; or you (or, on a joint return, your spouse) exclude employer-provided adoption benefits or income from sources within Puerto Rico?
- Expr: `{"op":"input","source":"Does any of these apply: you (or, on a joint return, your spouse) made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment; your social security repayments in 2025 (box 4) were more than your benefits (box 3); you (or, on a joint return, your spouse) file Form 2555, 4563 or 8815; or you (or, on a joint return, your spouse) exclude employer-provided adoption benefits or income from sources within Puerto Rico?"}`
- Cite: [i1040gi] p. 31, Lines 6a and 6b, Exception (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.lump_sum`

- **Authored helper label:** Do you elect to use the lump-sum election method for a social security benefit payment to you (or, on a joint return, your spouse) that was for an earlier year?
- **Encoded (Bool):** Input — Do you elect to use the lump-sum election method for a social security benefit payment to you (or, on a joint return, your spouse) that was for an earlier year?
- Expr: `{"op":"input","source":"Do you elect to use the lump-sum election method for a social security benefit payment to you (or, on a joint return, your spouse) that was for an earlier year?"}`
- Cite: [i1040gi] p. 31, Line 6c; p. 32, Social Security Benefits Worksheet, TIP (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.terror_disability`

- **Authored helper label:** Are any of the social security or railroad retirement benefits on your (or, on a joint return, your spouse's) Forms SSA-1099 or RRB-1099 disability payments for injuries incurred as a direct result of a terrorist attack directed against the United States or its allies (for the September 11 attacks, any injury eligible for coverage by the September 11 Victim Compensation Fund, whether or not you made a claim)?
- **Encoded (Bool):** Input — Are any of the social security or railroad retirement benefits on your (or, on a joint return, your spouse's) Forms SSA-1099 or RRB-1099 disability payments for injuries incurred as a direct result of a terrorist attack directed against the United States or its allies (for the September 11 attacks, any injury eligible for coverage by the September 11 Victim Compensation Fund, whether or not you made a claim)?
- Expr: `{"op":"input","source":"Are any of the social security or railroad retirement benefits on your (or, on a joint return, your spouse's) Forms SSA-1099 or RRB-1099 disability payments for injuries incurred as a direct result of a terrorist attack directed against the United States or its allies (for the September 11 attacks, any injury eligible for coverage by the September 11 Victim Compensation Fund, whether or not you made a claim)?"}`
- Cite: [i1040gi] p. 31, Lines 6a and 6b, Disability payments, "In the case of the September 11 attacks, injuries eligible for coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.lived_apart`

- **Authored helper label:** If you are married filing separately: did you live apart from your spouse for all of 2025?
- **Encoded (Bool):** Input — If you are married filing separately: did you live apart from your spouse for all of 2025?
- Expr: `{"op":"input","source":"If you are married filing separately: did you live apart from your spouse for all of 2025?"}`
- Cite: [i1040gi] p. 31, Line 6d; p. 32, worksheet, Before you begin and line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## 1 — `ssb.line1`

- **IRS:** Enter the total amount from box 5 of all your Forms SSA-1099 and RRB-1099
- **Encoded (NonNegDollars):** Enter the amount from helper "Net benefits: total of box 5 of all your Forms SSA-1099 and RRB-1099".
- Expr: `{"from":"ssb.benefits","op":"copy"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.has_benefits`

- **Authored helper label:** Any social security benefits (otherwise the worksheet is not needed)
- **Encoded (Bool):** line 1 > $0 (sales.zero)
- Expr: `{"gt":["ssb.line1",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 31, Lines 6a and 6b ('Use the Social Security Benefits Worksheet ... to see if any of your benefits are taxable') (2025; printed date 2026-02-25; sha256 482e9c48)

## 2 — `ssb.line2`

- **IRS:** Multiply line 1 by 50% (0.50)
- **Encoded (NonNegDollars):** Multiply line 1 by 1/2 (ssb.half).
- **Refusal:** when ssb.pub915 is true, cannot complete Pub. 915 or Pub. 590-A worksheet. The Social Security Benefits Worksheet in the Form 1040 instructions does not apply; use the worksheet in the publication. Cite: [i1040gi] p. 31, Lines 6a and 6b, Exception (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ssb.lump_sum is true, cannot complete Lump-Sum Election (Pub. 915). The lump-sum election method is outside this tool. Cite: [i1040gi] p. 31, Line 6c (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ssb.terror_disability is true, cannot complete Pub. 3920 (disability payments for injuries from a terrorist attack). Excluding disability payments for injuries from a terrorist attack is outside this tool. Cite: [i1040gi] p. 31, Lines 6a and 6b, Disability payments (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"amount":"ssb.line1","op":"multiply_rate","rate":{"param":"ssb.half"}}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `ssb.line3`

- **IRS:** Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8
- **Encoded (Dollars):** Add f1040 line 1z, f1040 line 2b, f1040 line 3b, f1040 line 4b, f1040 line 5b, f1040 line 7a, and f1040 line 8.
- Expr: `{"of":["f1040.line1z","f1040.line2b","f1040.line3b","f1040.line4b","f1040.line5b","f1040.line7a","f1040.line8"],"op":"sum"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 4 — `ssb.line4`

- **IRS:** Enter the amount, if any, from Form 1040 or 1040-SR, line 2a
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 2a.
- Expr: `{"from":"f1040.line2a","op":"copy"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `ssb.line5`

- **IRS:** Combine lines 2, 3, and 4
- **Encoded (Dollars):** Add line 2, line 3, and line 4.
- Expr: `{"of":["ssb.line2","ssb.line3","ssb.line4"],"op":"sum"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.ira_line20`

- **Authored helper label:** Schedule 1, line 20 (IRA deduction) as this worksheet reads it, figured with no one covered by a retirement plan
- **Encoded (NonNegDollars):** Add person.ira_ssb over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"collection":"person","field":"person.ira_ssb","op":"sum_over"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 6; p. 31, Lines 6a and 6b, Exception (2025; printed date 2026-02-25; sha256 482e9c48)

## 6 — `ssb.line6`

- **IRS:** Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
- **Encoded (NonNegDollars):** Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, helper "Schedule 1, line 20 (IRA deduction) as this worksheet reads it, figured with no one covered by a retirement plan", and s1 line 25.
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1 adjustments (Social Security Benefits Worksheet, line 6). Schedule 1 adjustments on lines 12, 14 and 23 are outside this tool. Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"of":["s1.line11","s1.line13","s1.line15","s1.line16","s1.line17","s1.line18","s1.line19a","ssb.ira_line20","s1.line25"],"op":"sum"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 6 (line 20 through its copy for this worksheet, ssb.ira_line20) (2025; printed date 2026-02-25; sha256 482e9c48)

## 7 — `ssb.line7`

- **IRS:** Is the amount on line 6 less than the amount on line 5? If yes, subtract line 6 from line 5 (if no, none of the benefits are taxable)
- **Encoded (NonNegDollars):** Subtract line 6 from line 5. If zero or less, enter -0-.
- Expr: `{"from":"ssb.line5","op":"subtract_floor0","take":"ssb.line6"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.base_single`

- **Authored helper label:** Line 8 amount, $25,000
- **Encoded (NonNegDollars):** Enter $25,000 (ssb.base_single).
- Expr: `{"op":"param","ref":"ssb.base_single"}`
- Cite: [i1040gi] p. 32, line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.base_joint`

- **Authored helper label:** Line 8 amount, $32,000
- **Encoded (NonNegDollars):** Enter $32,000 (ssb.base_joint).
- Expr: `{"op":"param","ref":"ssb.base_joint"}`
- Cite: [i1040gi] p. 32, line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.zero`

- **Authored helper label:** No amount
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 32, line 8 (married filing separately and living with the spouse skips lines 8 to 15) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.mfs_base`

- **Authored helper label:** Line 8 for married filing separately: $25,000 if you lived apart all year (otherwise lines 8 to 15 are skipped)
- **Encoded (NonNegDollars):** Choose — [helper "If you are married filing separately: did you live apart from your spouse for all of 2025?" = true → helper "Line 8 amount, $25,000"] [helper "If you are married filing separately: did you live apart from your spouse for all of 2025?" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["ssb.lived_apart",{"const":true}],"op":"test"},"then":"ssb.base_single"},{"guard":{"eq":["ssb.lived_apart",{"const":false}],"op":"test"},"then":"ssb.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.lines8_to_15`

- **Authored helper label:** Lines 8 through 15 are completed (not married filing separately with your spouse living with you at any time in 2025)
- **Encoded (Bool):** helper "Married filing separately and lived with your spouse at any time in 2025" = false
- Expr: `{"eq":["ssb.mfs_together",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 8, "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16" (2025; printed date 2026-02-25; sha256 482e9c48)

## 8 — `ssb.line8`

- **IRS:** $32,000 if married filing jointly; $25,000 if single, head of household, qualifying surviving spouse, or married filing separately and living apart all year
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 8 amount, $25,000"] [f1040 line Filing Status = 'mfj' → helper "Line 8 amount, $32,000"] [f1040 line Filing Status = 'mfs' → helper "Line 8 for married filing separately: $25,000 if you lived apart all year (otherwise lines 8 to 15 are skipped)"] [f1040 line Filing Status = 'hoh' → helper "Line 8 amount, $25,000"] [f1040 line Filing Status = 'qss' → helper "Line 8 amount, $25,000"]
- **Shown on the values sheet only when:** Lines 8 and 9 are completed (lines 8 to 15 are not skipped, and the worksheet did not stop at line 7) (`ssb.show8_9`)
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"ssb.base_single"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"ssb.base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"ssb.mfs_base"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"ssb.base_single"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"ssb.base_single"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## 9 — `ssb.line9`

- **IRS:** Is the amount on line 8 less than the amount on line 7? If yes, subtract line 8 from line 7 (if no, none of the benefits are taxable)
- **Encoded (NonNegDollars):** Subtract line 8 from line 7. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Lines 8 and 9 are completed (lines 8 to 15 are not skipped, and the worksheet did not stop at line 7) (`ssb.show8_9`)
- Expr: `{"from":"ssb.line7","op":"subtract_floor0","take":"ssb.line8"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 9 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.past7`

- **Authored helper label:** Line 6 is less than line 5, so the worksheet goes on past line 7 (otherwise it stops there)
- **Encoded (Bool):** line 7 > $0 (sales.zero)
- Expr: `{"gt":["ssb.line7",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 7, "Is the amount on line 6 less than the amount on line 5?" and "No. None of your social security benefits are taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.past9`

- **Authored helper label:** Line 8 is less than line 7, so the worksheet goes on past line 9 (otherwise it stops there)
- **Encoded (Bool):** line 9 > $0 (sales.zero)
- Expr: `{"gt":["ssb.line9",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 9, "Is the amount on line 8 less than the amount on line 7?" and "No. None of your social security benefits are taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.show8_9`

- **Authored helper label:** Lines 8 and 9 are completed (lines 8 to 15 are not skipped, and the worksheet did not stop at line 7)
- **Encoded (Bool):** helper "Lines 8 through 15 are completed (not married filing separately with your spouse living with you at any time in 2025)" = true and helper "Line 6 is less than line 5, so the worksheet goes on past line 7 (otherwise it stops there)" = true
- Expr: `{"all":[{"eq":["ssb.lines8_to_15",{"const":true}],"op":"test"},{"eq":["ssb.past7",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 7, "Is the amount on line 6 less than the amount on line 5?" and "No. None of your social security benefits are taxable"; line 8, "skip lines 8 through 15" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.show10_15`

- **Authored helper label:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9)
- **Encoded (Bool):** helper "Lines 8 and 9 are completed (lines 8 to 15 are not skipped, and the worksheet did not stop at line 7)" = true and helper "Line 8 is less than line 7, so the worksheet goes on past line 9 (otherwise it stops there)" = true
- Expr: `{"all":[{"eq":["ssb.show8_9",{"const":true}],"op":"test"},{"eq":["ssb.past9",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 9, "Is the amount on line 8 less than the amount on line 7?" and "No. None of your social security benefits are taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.show16_18`

- **Authored helper label:** Lines 16 through 18 are completed (the worksheet did not stop at line 7, nor at line 9 when lines 8 to 15 are completed)
- **Encoded (Bool):** helper "Line 6 is less than line 5, so the worksheet goes on past line 7 (otherwise it stops there)" = true and (helper "Married filing separately and lived with your spouse at any time in 2025" = true or helper "Line 8 is less than line 7, so the worksheet goes on past line 9 (otherwise it stops there)" = true)
- Expr: `{"all":[{"eq":["ssb.past7",{"const":true}],"op":"test"},{"any":[{"eq":["ssb.mfs_together",{"const":true}],"op":"test"},{"eq":["ssb.past9",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 9, "Is the amount on line 8 less than the amount on line 7?" and "No. None of your social security benefits are taxable"; line 8, "skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16. Then, go to line 17" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.adjust_single`

- **Authored helper label:** Line 10 amount, $9,000
- **Encoded (NonNegDollars):** Enter $9,000 (ssb.adjust_single).
- Expr: `{"op":"param","ref":"ssb.adjust_single"}`
- Cite: [i1040gi] p. 32, line 10 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.adjust_joint`

- **Authored helper label:** Line 10 amount, $12,000
- **Encoded (NonNegDollars):** Enter $12,000 (ssb.adjust_joint).
- Expr: `{"op":"param","ref":"ssb.adjust_joint"}`
- Cite: [i1040gi] p. 32, line 10 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.mfs_adjust`

- **Authored helper label:** Line 10 for married filing separately: $9,000 if you lived apart all year
- **Encoded (NonNegDollars):** Choose — [helper "If you are married filing separately: did you live apart from your spouse for all of 2025?" = true → helper "Line 10 amount, $9,000"] [helper "If you are married filing separately: did you live apart from your spouse for all of 2025?" = false → helper "No amount"]
- Expr: `{"alternatives":[{"guard":{"eq":["ssb.lived_apart",{"const":true}],"op":"test"},"then":"ssb.adjust_single"},{"guard":{"eq":["ssb.lived_apart",{"const":false}],"op":"test"},"then":"ssb.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, line 10 (2025; printed date 2026-02-25; sha256 482e9c48)

## 10 — `ssb.line10`

- **IRS:** Enter $12,000 if married filing jointly; $9,000 if single, head of household, qualifying surviving spouse, or married filing separately and living apart all year
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 10 amount, $9,000"] [f1040 line Filing Status = 'mfj' → helper "Line 10 amount, $12,000"] [f1040 line Filing Status = 'mfs' → helper "Line 10 for married filing separately: $9,000 if you lived apart all year"] [f1040 line Filing Status = 'hoh' → helper "Line 10 amount, $9,000"] [f1040 line Filing Status = 'qss' → helper "Line 10 amount, $9,000"]
- **Shown on the values sheet only when:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9) (`ssb.show10_15`)
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"ssb.adjust_single"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"ssb.adjust_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"ssb.mfs_adjust"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"ssb.adjust_single"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"ssb.adjust_single"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 10 (2025; printed date 2026-02-25; sha256 482e9c48)

## 11 — `ssb.line11`

- **IRS:** Subtract line 10 from line 9. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 10 from line 9. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9) (`ssb.show10_15`)
- Expr: `{"from":"ssb.line9","op":"subtract_floor0","take":"ssb.line10"}`
- Cite: [i1040gi] p. 32, line 11 (2025; printed date 2026-02-25; sha256 482e9c48)

## 12 — `ssb.line12`

- **IRS:** Enter the smaller of line 9 or line 10
- **Encoded (NonNegDollars):** Enter the smaller of line 9 or line 10.
- **Shown on the values sheet only when:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9) (`ssb.show10_15`)
- Expr: `{"of":["ssb.line9","ssb.line10"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 32, line 12 (2025; printed date 2026-02-25; sha256 482e9c48)

## 13 — `ssb.line13`

- **IRS:** Enter one-half of line 12
- **Encoded (NonNegDollars):** Multiply line 12 by 1/2 (ssb.half).
- **Shown on the values sheet only when:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9) (`ssb.show10_15`)
- Expr: `{"amount":"ssb.line12","op":"multiply_rate","rate":{"param":"ssb.half"}}`
- Cite: [i1040gi] p. 32, line 13 (2025; printed date 2026-02-25; sha256 482e9c48)

## 14 — `ssb.line14`

- **IRS:** Enter the smaller of line 2 or line 13
- **Encoded (NonNegDollars):** Enter the smaller of line 2 or line 13.
- **Shown on the values sheet only when:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9) (`ssb.show10_15`)
- Expr: `{"of":["ssb.line2","ssb.line13"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 14 (2025; printed date 2026-02-25; sha256 482e9c48)

## 15 — `ssb.line15`

- **IRS:** Multiply line 11 by 85% (0.85). If line 11 is zero, enter -0-
- **Encoded (NonNegDollars):** Multiply line 11 by 85% (0.85) (ssb.rate85).
- **Shown on the values sheet only when:** Lines 10 through 15 are completed (lines 8 and 9 are completed, and the worksheet did not stop at line 9) (`ssb.show10_15`)
- Expr: `{"amount":"ssb.line11","op":"multiply_rate","rate":{"param":"ssb.rate85"}}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 15 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.mfs_together`

- **Authored helper label:** Married filing separately and lived with your spouse at any time in 2025
- **Encoded (Bool):** f1040 line Filing Status = 'mfs' and helper "If you are married filing separately: did you live apart from your spouse for all of 2025?" = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["ssb.lived_apart",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 32, line 8, third bullet (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.line16_sum`

- **Authored helper label:** Add lines 14 and 15
- **Encoded (NonNegDollars):** Add line 14 and line 15.
- Expr: `{"of":["ssb.line14","ssb.line15"],"op":"sum"}`
- Cite: [i1040gi] p. 32, line 16 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.line16_together`

- **Authored helper label:** Married filing separately and living with your spouse: line 7 times 85% (0.85)
- **Encoded (NonNegDollars):** Multiply line 7 by 85% (0.85) (ssb.rate85).
- Expr: `{"amount":"ssb.line7","op":"multiply_rate","rate":{"param":"ssb.rate85"}}`
- Cite: [i1040gi] p. 32, line 8, 'multiply line 7 by 85% (0.85) and enter the result on line 16' (2025; printed date 2026-02-25; sha256 482e9c48)

## 16 — `ssb.line16`

- **IRS:** Add lines 14 and 15 (if married filing separately and you lived with your spouse at any time in 2025, multiply line 7 by 85% (0.85) instead)
- **Encoded (NonNegDollars):** Choose — [helper "Married filing separately and lived with your spouse at any time in 2025" = true → helper "Married filing separately and living with your spouse: line 7 times 85% (0.85)"] [helper "Married filing separately and lived with your spouse at any time in 2025" = false → helper "Add lines 14 and 15"]
- **Shown on the values sheet only when:** Lines 16 through 18 are completed (the worksheet did not stop at line 7, nor at line 9 when lines 8 to 15 are completed) (`ssb.show16_18`)
- Expr: `{"alternatives":[{"guard":{"eq":["ssb.mfs_together",{"const":true}],"op":"test"},"then":"ssb.line16_together"},{"guard":{"eq":["ssb.mfs_together",{"const":false}],"op":"test"},"then":"ssb.line16_sum"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, line 16 (and line 8 for married filing separately and living with the spouse) (2025; printed date 2026-02-25; sha256 482e9c48)

## 17 — `ssb.line17`

- **IRS:** Multiply line 1 by 85% (0.85)
- **Encoded (NonNegDollars):** Multiply line 1 by 85% (0.85) (ssb.rate85).
- **Shown on the values sheet only when:** Lines 16 through 18 are completed (the worksheet did not stop at line 7, nor at line 9 when lines 8 to 15 are completed) (`ssb.show16_18`)
- Expr: `{"amount":"ssb.line1","op":"multiply_rate","rate":{"param":"ssb.rate85"}}`
- Cite: [i1040gi] p. 32, line 17 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ssb.line18_figured`

- **Authored helper label:** The smaller of line 16 or line 17
- **Encoded (NonNegDollars):** Enter the smaller of line 16 or line 17.
- Expr: `{"of":["ssb.line16","ssb.line17"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 18 (2025; printed date 2026-02-25; sha256 482e9c48)

## 18 — `ssb.line18`

- **IRS:** Taxable social security benefits. Enter the smaller of line 16 or line 17
- **Encoded (NonNegDollars):** Choose — [helper "Any social security benefits (otherwise the worksheet is not needed)" = true → helper "The smaller of line 16 or line 17"] [helper "Any social security benefits (otherwise the worksheet is not needed)" = false → helper "No amount"]
- **Shown on the values sheet only when:** Lines 16 through 18 are completed (the worksheet did not stop at line 7, nor at line 9 when lines 8 to 15 are completed) (`ssb.show16_18`)
- Expr: `{"alternatives":[{"guard":{"eq":["ssb.has_benefits",{"const":true}],"op":"test"},"then":"ssb.line18_figured"},{"guard":{"eq":["ssb.has_benefits",{"const":false}],"op":"test"},"then":"ssb.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 18 (with no benefits, none are taxable) (2025; printed date 2026-02-25; sha256 482e9c48)
