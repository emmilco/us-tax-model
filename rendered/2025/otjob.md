# Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer

- Document: `otjob` (form, tax year 2025)
- Collection: keyed entries within person; [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet (one row per employer); n-25-69 Section III.B.2, "Individuals who had multiple employers during 2025 may use different methods for each employer" (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: One entry per employer that paid you overtime. Qualified overtime is the FLSA Overtime Premium (the "half" of time-and-a-half), figured by one of the methods the instructions and Notice 2025-69 give for 2025. Methods that call for a reasonable estimate, overtime at a rate other than one and one-half or two times the regular rate, and special FLSA overtime rules are refused.

## (helper) — `otjob.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 108, Qualified Overtime Compensation From More Than One Employer Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.flsa`

- **Authored helper label:** Were you an FLSA-eligible employee of this employer (covered by and not exempt from the Fair Labor Standards Act, so that this employer was required to pay you overtime under section 7 of the FLSA)?
- **Encoded (Bool):** Input — Were you an FLSA-eligible employee of this employer (covered by and not exempt from the Fair Labor Standards Act, so that this employer was required to pay you overtime under section 7 of the FLSA)? You can ask your employer.
- Expr: `{"op":"input","source":"Were you an FLSA-eligible employee of this employer (covered by and not exempt from the Fair Labor Standards Act, so that this employer was required to pay you overtime under section 7 of the FLSA)? You can ask your employer."}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Qualified overtime compensation, "you must (among other requirements) be covered by and not exempt from the FLSA (an FLSA-eligible employee)" and "Ask your employer or other service recipients whether you are an FLSA-eligible employee" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.special_rule`

- **Authored helper label:** Is this employer covered by an FLSA overtime rule other than the general rule in section 7(a) (for example section 7(k) for fire protection and law enforcement, 7(o) compensatory time, or 7(j) hospitals and residential care facilities)?
- **Encoded (Bool):** Input — Is this employer covered by an FLSA overtime rule other than the general rule in section 7(a) (for example section 7(k) for fire protection and law enforcement, 7(o) compensatory time off, or 7(j) hospitals and residential care facilities)?
- Expr: `{"op":"input","source":"Is this employer covered by an FLSA overtime rule other than the general rule in section 7(a) (for example section 7(k) for fire protection and law enforcement, 7(o) compensatory time off, or 7(j) hospitals and residential care facilities)?"}`
- Cite: [n-25-69] pp. 22–25, Section III.B.2, method (G) (Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page); sha256 e405c12d)

## (helper) — `otjob.method`

- **Authored helper label:** How you figured the qualified overtime compensation from this employer
- **Encoded (Enum(overtime_method)):** Input — How you figured it: employer_reported (an amount of qualified overtime compensation your employer reported in Form W-2 box 14 or gave you on request); premium (a statement shows the "half" portion of time-and-a-half, the FLSA Overtime Premium); total_time_and_half (a statement shows the total pay for overtime hours paid at time-and-a-half); premium_double (overtime paid at double time, and a statement shows the pay above your regular rate for those hours); total_double (overtime paid at double time, and a statement shows the total pay for those hours); other (any other method, rate or adjustment)
- Expr: `{"op":"input","source":"How you figured it: employer_reported (an amount of qualified overtime compensation your employer reported in Form W-2 box 14 or gave you on request); premium (a statement shows the \"half\" portion of time-and-a-half, the FLSA Overtime Premium); total_time_and_half (a statement shows the total pay for overtime hours paid at time-and-a-half); premium_double (overtime paid at double time, and a statement shows the pay above your regular rate for those hours); total_double (overtime paid at double time, and a statement shows the total pay for those hours); other (any other method, rate or adjustment)"}`
- Cite: [i1040gi] pp. 106-107, Schedule 1-A, "Determining the amount of qualified overtime compensation for 2025," the employer's separate accounting and methods 1 to 5; n-25-69 Section III.B.2, methods (A) to (G) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.statement`

- **Authored helper label:** The amount shown for the method you chose
- **Encoded (NonNegDollars):** Input — The full-year amount for the method you chose (the amount your employer reported; the overtime premium; the total pay for overtime hours; or the pay above your regular rate for overtime hours), from this employer, including overtime pay that is not in Form W-2 box 1 (for example overtime deferred under a qualified retirement plan)
- Expr: `{"op":"input","source":"The full-year amount for the method you chose (the amount your employer reported; the overtime premium; the total pay for overtime hours; or the pay above your regular rate for overtime hours), from this employer, including overtime pay that is not in Form W-2 box 1 (for example overtime deferred under a qualified retirement plan)"}`
- Cite: [i1040gi] pp. 106-107, Schedule 1-A, methods 1 to 4; n-25-69 Section III.B.2, methods (A) to (D), "receives a statement covering the entire 2025 tax year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `otjob.refused`

- **Authored helper label:** Overtime figured by a method, rate or rule outside this tool
- **Encoded (Bool):** helper "Were you an FLSA-eligible employee of this employer (covered by and not exempt from the Fair Labor Standards Act, so that this employer was required to pay you overtime under section 7 of the FLSA)?" = true and (helper "Is this employer covered by an FLSA overtime rule other than the general rule in section 7(a) (for example section 7(k) for fire protection and law enforcement, 7(o) compensatory time, or 7(j) hospitals and residential care facilities)?" = true or helper "How you figured the qualified overtime compensation from this employer" = 'other')
- Expr: `{"all":[{"eq":["otjob.flsa",{"const":true}],"op":"test"},{"any":[{"eq":["otjob.special_rule",{"const":true}],"op":"test"},{"eq":["otjob.method",{"const":"other"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 107, Schedule 1-A, method 5 ("you can use a reasonable method"), the adjustment for underestimating, and other overtime rules in section 7 of the FLSA (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.figured`

- **Authored helper label:** FLSA Overtime Premium from this employer, by the method chosen
- **Encoded (NonNegDollars):** Choose — [helper "How you figured the qualified overtime compensation from this employer" = 'employer_reported' → helper "The amount shown for the method you chose"] [helper "How you figured the qualified overtime compensation from this employer" = 'premium' → helper "The amount shown for the method you chose"] [helper "How you figured the qualified overtime compensation from this employer" = 'total_time_and_half' → helper "Method 2. Divide the total pay for overtime hours by three (3)"] [helper "How you figured the qualified overtime compensation from this employer" = 'premium_double' → helper "Method 3 at double time. Multiply the pay above the regular rate for overtime hours by one-half"] [helper "How you figured the qualified overtime compensation from this employer" = 'total_double' → helper "Method 4 at double time. Multiply the total pay for overtime hours by one-fourth"] [helper "How you figured the qualified overtime compensation from this employer" = 'other' → helper "Year parameter sales.zero"]
- **Refusal:** when otjob.refused is true, cannot complete Qualified overtime compensation by a reasonable-method estimate, at an overtime rate other than one and one-half or two times the regular rate, or under a special FLSA overtime rule. Figure the amount by the method that applies to you; this tool covers the employer-reported amount and methods 1 to 4 at time-and-a-half or double time. Cite: [n-25-69] pp. 22–25, Section III.B.2, methods (E), (F) and (G) (Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page); sha256 e405c12d)
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"alternatives":[{"guard":{"eq":["otjob.method",{"const":"employer_reported"}],"op":"test"},"then":"otjob.statement"},{"guard":{"eq":["otjob.method",{"const":"premium"}],"op":"test"},"then":"otjob.statement"},{"guard":{"eq":["otjob.method",{"const":"total_time_and_half"}],"op":"test"},"then":"otjob.by_third"},{"guard":{"eq":["otjob.method",{"const":"premium_double"}],"op":"test"},"then":"otjob.by_half"},{"guard":{"eq":["otjob.method",{"const":"total_double"}],"op":"test"},"then":"otjob.by_quarter"},{"guard":{"eq":["otjob.method",{"const":"other"}],"op":"test"},"then":"otjob.zero"}],"op":"choose"}`
- Cite: [i1040gi] pp. 106-107, Schedule 1-A, methods 1 to 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.by_third`

- **Authored helper label:** Method 2. Divide the total pay for overtime hours by three (3)
- **Encoded (NonNegDollars):** Multiply helper "The amount shown for the method you chose" by 1/3 (s1a.ot_third).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"otjob.statement","op":"multiply_rate","rate":{"param":"s1a.ot_third"}}`
- Cite: [i1040gi] p. 106, Schedule 1-A, method 2, "you can divide the total amount by three (3)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.by_half`

- **Authored helper label:** Method 3 at double time. Multiply the pay above the regular rate for overtime hours by one-half
- **Encoded (NonNegDollars):** Multiply helper "The amount shown for the method you chose" by 1/2 (s1a.ot_half).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"otjob.statement","op":"multiply_rate","rate":{"param":"s1a.ot_half"}}`
- Cite: [i1040gi] pp. 106-107, Schedule 1-A, method 3 and Example 2; n-25-69 Section III.B.2, method (C), "the appropriate fraction is one-half" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `otjob.by_quarter`

- **Authored helper label:** Method 4 at double time. Multiply the total pay for overtime hours by one-fourth
- **Encoded (NonNegDollars):** Multiply helper "The amount shown for the method you chose" by 1/4 (s1a.ot_quarter).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"otjob.statement","op":"multiply_rate","rate":{"param":"s1a.ot_quarter"}}`
- Cite: [i1040gi] p. 107, Schedule 1-A, method 4 and Example 3; n-25-69 Section III.B.2, method (D), "the appropriate fraction is one-fourth" (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(b) — `otjob.col_b`

- **IRS:** Qualified overtime reported on Form W-2, box 1
- **Encoded (NonNegDollars):** Choose — [helper "Were you an FLSA-eligible employee of this employer (covered by and not exempt from the Fair Labor Standards Act, so that this employer was required to pay you overtime under section 7 of the FLSA)?" = false → helper "Year parameter sales.zero"] [helper "Were you an FLSA-eligible employee of this employer (covered by and not exempt from the Fair Labor Standards Act, so that this employer was required to pay you overtime under section 7 of the FLSA)?" = true → helper "FLSA Overtime Premium from this employer, by the method chosen"]
- Expr: `{"alternatives":[{"guard":{"eq":["otjob.flsa",{"const":false}],"op":"test"},"then":"otjob.zero"},{"guard":{"eq":["otjob.flsa",{"const":true}],"op":"test"},"then":"otjob.figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 108, Qualified Overtime Compensation From More Than One Employer Worksheet, column (b); p. 108, line 14a, including qualified overtime not included in box 1 (for example overtime deferred under a qualified retirement plan) (2025; printed date 2026-02-25; sha256 482e9c48)
