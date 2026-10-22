# Schedule SE (Form 1040) — Self-Employment Tax, one per person

- Document: `se` (def, tax year 2025)
- Parameters: line2, line8a

## 2 — `line2`

- **IRS:** Net profit or (loss) from Schedule C, line 31
- **Encoded (Dollars):** Input — Bound by the calling line (this person's Schedule C results).
- Expr: `{"op":"input","source":"Bound by the calling line (this person's Schedule C results)."}`
- Cite: [f1040sse] Schedule SE (2025), line 2; i1040sse p. 2, More Than One Business, "your net earnings from self-employment are the combined net earnings from all of your businesses" (2025; created 2025-05-07; sha256 05bc2b3e)

## 8a — `line8a`

- **IRS:** Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation
- **Encoded (NonNegDollars):** Input — Bound by the calling line (this person's Forms W-2, boxes 3 and 7; railroad retirement compensation is refused, person.se_rrta).
- Expr: `{"op":"input","source":"Bound by the calling line (this person's Forms W-2, boxes 3 and 7; railroad retirement compensation is refused, person.se_rrta)."}`
- Cite: [f1040sse] Schedule SE (2025), line 8a (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040sse] Schedule SE (2025), lines 1a, 1b, 4b, 5a, 8b and 8c (zero under the screen of this person) (2025; created 2025-05-07; sha256 05bc2b3e)

## 3 — `line3`

- **IRS:** Combine lines 1a, 1b, and 2
- **Encoded (Dollars):** Enter the amount from line 2.
- Expr: `{"from":"line2","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), line 3 (lines 1a and 1b are zero: farm income and Conservation Reserve Program payments are refused) (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `positive`

- **Authored helper label:** Line 3 is more than zero
- **Encoded (Bool):** line 3 > $0 (sales.zero)
- Expr: `{"gt":["line3",{"param":"sales.zero"}],"op":"test"}`
- Cite: [f1040sse] Schedule SE (2025), line 4a (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `rate9235`

- **Authored helper label:** 92.35%
- **Encoded (Rate):** Enter 9235/10000 (se.rate_9235).
- Expr: `{"op":"param","ref":"se.rate_9235"}`
- Cite: [f1040sse] Schedule SE (2025), line 4a, "multiply line 3 by 92.35% (0.9235)" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `line3pos`

- **Authored helper label:** Line 3 when more than zero
- **Encoded (NonNegDollars):** Subtract helper "Zero" from line 3. If zero or less, enter -0-.
- Expr: `{"from":"line3","op":"subtract_floor0","take":"zero"}`
- Cite: [f1040sse] Schedule SE (2025), line 4a (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `line4a_pos`

- **Authored helper label:** Line 3 times 92.35%
- **Encoded (NonNegDollars):** Multiply helper "Line 3 when more than zero" by helper "92.35%".
- Expr: `{"amount":"line3pos","op":"multiply_rate","rate":"rate9235"}`
- Cite: [f1040sse] Schedule SE (2025), line 4a (2025; created 2025-05-07; sha256 05bc2b3e)

## 4a — `line4a`

- **IRS:** If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3
- **Encoded (Dollars):** Choose — [helper "Line 3 is more than zero" = true → helper "Line 3 times 92.35%"] [helper "Line 3 is more than zero" = false → line 3]
- Expr: `{"alternatives":[{"guard":{"eq":["positive",{"const":true}],"op":"test"},"then":"line4a_pos"},{"guard":{"eq":["positive",{"const":false}],"op":"test"},"then":"line3"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 4a (2025; created 2025-05-07; sha256 05bc2b3e)

## 4b — `line4b`

- **IRS:** If you elect one or both of the optional methods, enter the total of lines 15 and 17
- **Encoded (NonNegDollars):** Enter the amount from helper "Zero".
- Expr: `{"from":"zero","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), line 4b (the optional methods are refused) (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `line4c_sum`

- **Authored helper label:** Combine lines 4a and 4b
- **Encoded (Dollars):** Add line 4a and line 4b.
- Expr: `{"of":["line4a","line4b"],"op":"sum"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `floor`

- **Authored helper label:** $400
- **Encoded (NonNegDollars):** Enter $400 (se.floor).
- Expr: `{"op":"param","ref":"se.floor"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c, "If less than $400, stop; you don't owe self-employment tax" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `owes`

- **Authored helper label:** Line 4c is $400 or more
- **Encoded (Bool):** helper "Combine lines 4a and 4b" ≥ helper "$400"
- Expr: `{"ge":["line4c_sum","floor"],"op":"test"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `line4c_owes`

- **Authored helper label:** Line 4c when $400 or more
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "Combine lines 4a and 4b". If zero or less, enter -0-.
- Expr: `{"from":"line4c_sum","op":"subtract_floor0","take":"zero"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c (2025; created 2025-05-07; sha256 05bc2b3e)

## 4c — `line4c`

- **IRS:** Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax
- **Encoded (NonNegDollars):** Choose — [helper "Line 4c is $400 or more" = true → helper "Line 4c when $400 or more"] [helper "Line 4c is $400 or more" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["owes",{"const":true}],"op":"test"},"then":"line4c_owes"},{"guard":{"eq":["owes",{"const":false}],"op":"test"},"then":"zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c (church employee income is refused, so the exception does not arise) (2025; created 2025-05-07; sha256 05bc2b3e)

## 5b — `line5b`

- **IRS:** Multiply line 5a by 92.35% (0.9235)
- **Encoded (NonNegDollars):** Enter the amount from helper "Zero".
- Expr: `{"from":"zero","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), lines 5a and 5b (church employee income is refused) (2025; created 2025-05-07; sha256 05bc2b3e)

## 6 — `line6`

- **IRS:** Add lines 4c and 5b
- **Encoded (NonNegDollars):** Add line 4c and line 5b.
- Expr: `{"of":["line4c","line5b"],"op":"sum"}`
- Cite: [f1040sse] Schedule SE (2025), line 6 (2025; created 2025-05-07; sha256 05bc2b3e)

## 7 — `line7`

- **IRS:** Maximum amount of combined wages and self-employment earnings subject to social security tax for 2025
- **Encoded (NonNegDollars):** Enter $176,100 (se.wage_base).
- Expr: `{"op":"param","ref":"se.wage_base"}`
- Cite: [f1040sse] Schedule SE (2025), line 7, "$176,100" (2025; created 2025-05-07; sha256 05bc2b3e)

## 8d — `line8d`

- **IRS:** Add lines 8a, 8b, and 8c
- **Encoded (NonNegDollars):** Enter the amount from line 8a.
- Expr: `{"from":"line8a","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), line 8d (lines 8b and 8c, Forms 4137 and 8919, are refused) (2025; created 2025-05-07; sha256 05bc2b3e)

## 9 — `line9`

- **IRS:** Subtract line 8d from line 7. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 8d from line 7. If zero or less, enter -0-.
- Expr: `{"from":"line7","op":"subtract_floor0","take":"line8d"}`
- Cite: [f1040sse] Schedule SE (2025), line 9 (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `ss_base`

- **Authored helper label:** The smaller of line 6 or line 9
- **Encoded (NonNegDollars):** Enter the smaller of line 6 or line 9.
- Expr: `{"of":["line6","line9"],"op":"smaller_of"}`
- Cite: [f1040sse] Schedule SE (2025), line 10 (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `rate124`

- **Authored helper label:** 12.4%
- **Encoded (Rate):** Enter 124/1000 (se.rate_124).
- Expr: `{"op":"param","ref":"se.rate_124"}`
- Cite: [f1040sse] Schedule SE (2025), line 10, "by 12.4% (0.124)" (2025; created 2025-05-07; sha256 05bc2b3e)

## 10 — `line10`

- **IRS:** Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
- **Encoded (NonNegDollars):** Multiply helper "The smaller of line 6 or line 9" by helper "12.4%".
- Expr: `{"amount":"ss_base","op":"multiply_rate","rate":"rate124"}`
- Cite: [f1040sse] Schedule SE (2025), line 10 (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `rate029`

- **Authored helper label:** 2.9%
- **Encoded (Rate):** Enter 29/1000 (se.rate_029).
- Expr: `{"op":"param","ref":"se.rate_029"}`
- Cite: [f1040sse] Schedule SE (2025), line 11, "by 2.9% (0.029)" (2025; created 2025-05-07; sha256 05bc2b3e)

## 11 — `line11`

- **IRS:** Multiply line 6 by 2.9% (0.029)
- **Encoded (NonNegDollars):** Multiply line 6 by helper "2.9%".
- Expr: `{"amount":"line6","op":"multiply_rate","rate":"rate029"}`
- Cite: [f1040sse] Schedule SE (2025), line 11 (2025; created 2025-05-07; sha256 05bc2b3e)

## 12 — `line12`

- **IRS:** Self-employment tax. Add lines 10 and 11
- **Encoded (NonNegDollars):** Add line 10 and line 11.
- Expr: `{"of":["line10","line11"],"op":"sum"}`
- Cite: [f1040sse] Schedule SE (2025), line 12, "Enter here and on Schedule 2 (Form 1040), line 4" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `rate50`

- **Authored helper label:** 50%
- **Encoded (Rate):** Enter 50% (0.50) (se.rate_50).
- Expr: `{"op":"param","ref":"se.rate_50"}`
- Cite: [f1040sse] Schedule SE (2025), line 13, "Multiply line 12 by 50% (0.50)" (2025; created 2025-05-07; sha256 05bc2b3e)

## 13 — `line13`

- **IRS:** Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
- **Encoded (NonNegDollars):** Multiply line 12 by helper "50%".
- Expr: `{"amount":"line12","op":"multiply_rate","rate":"rate50"}`
- Cite: [f1040sse] Schedule SE (2025), line 13, "Enter here and on Schedule 1 (Form 1040), line 15" (2025; created 2025-05-07; sha256 05bc2b3e)
