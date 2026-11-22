# Qualified Tips From More Than One Employer Worksheet (Schedule 1-A, line 4c) — one row per employer

- Document: `tipjob` (form, tax year 2025)
- Collection: keyed entries within person; [i1040gi] p. 104, Schedule 1-A, line 4c, and the Qualified Tips From More Than One Employer Worksheet (one row per employer) (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: One entry per employer from which you received tips as an employee that you are deducting. Tips reported on Form 4137 (column (c)) are refused with Form 4137, so column (d) is the column (b) amount.

## (helper) — `tipjob.one`

- **Authored helper label:** One employer
- **Encoded (Count):** Enter 1 (ss.one).
- Expr: `{"op":"param","ref":"ss.one"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c, "with respect to employment with more than one employer" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.no`

- **Authored helper label:** Year parameter s3.no (false)
- **Encoded (Bool):** Enter false (s3.no).
- Expr: `{"op":"param","ref":"s3.no"}`
- Cite: [i1040gi] p. 103, Schedule 1-A, "Determining the amount of qualified tips received by an employee for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.listed`

- **Authored helper label:** Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?
- **Encoded (Bool):** Input — Were any of these tips for a job on the IRS list of tipped jobs (such as server, bartender, cook, hairdresser or driver; not manager)?
- Expr: `{"op":"input","source":"Were any of these tips for a job on the IRS list of tipped jobs (such as server, bartender, cook, hairdresser or driver; not manager)?"}`
- Cite: [i1040gi] pp. 101-103, Schedule 1-A, Qualified Tips, "Occupations that customarily and regularly received tips"; "Do not include tips received in occupations that are not included on this list"; tipped-occupations, the list of occupations by Treasury Tipped Occupation Code (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.other_work`

- **Authored helper label:** Were some of the tips from this employer received in an occupation that is not on the IRS list?
- **Encoded (Bool):** Input — Did you also get tips from this employer for other work that is not on that list?
- Expr: `{"op":"input","source":"Did you also get tips from this employer for other work that is not on that list?"}`
- Cite: [i1040gi] p. 103, "If you received tips as an employee in more than one occupation for the same employer, only those tips that were received in an occupation on the list ... are considered qualified tips. Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `tipjob.other_work_if_listed`

- **Authored helper label:** Whether some of this employer's tips were received in an occupation not on the list, asked only where the tips were received in a listed occupation (false otherwise)
- **Encoded (Bool):** Choose — [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = true → helper "Were some of the tips from this employer received in an occupation that is not on the IRS list?"] [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["tipjob.listed",{"const":true}],"op":"test"},"then":"tipjob.other_work"},{"guard":{"eq":["tipjob.listed",{"const":false}],"op":"test"},"then":"tipjob.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 103, Schedule 1-A, "Determining the amount of qualified tips received by an employee for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.charged`

- **Authored helper label:** Do the tips from this employer include amounts not paid voluntarily, not determined by the customer or subject to negotiation (service charges, automatic gratuities), or amounts not paid in a cash medium (cash, check, credit or debit card, gift card, tokens readily exchangeable for a fixed amount such as casino chips, or a payment app)?
- **Encoded (Bool):** Input — Do these tips include a service charge or automatic gratuity that the business added to the bill, an amount you negotiated with the customer, or tips given as tickets, meals, services or goods instead of money (casino chips count as money)?
- Expr: `{"op":"input","source":"Do these tips include a service charge or automatic gratuity that the business added to the bill, an amount you negotiated with the customer, or tips given as tickets, meals, services or goods instead of money (casino chips count as money)?"}`
- Cite: [i1040gi] pp. 101-103, Schedule 1-A, Qualified Tips, Cash tips, "paid in a cash medium, including by cash, check, credit card, debit card, gift card, tangible or intangible tokens that are readily exchangeable for a fixed amount (for example, casino chips)"; "Paid voluntarily, not subject to negotiation, and determined by the customer/payor," "Amounts received that are not qualified tips" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `tipjob.charged_if_listed`

- **Authored helper label:** Whether this employer's tips include amounts not paid voluntarily or not paid in cash, asked only where the tips were received in a listed occupation (false otherwise)
- **Encoded (Bool):** Choose — [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = true → helper "Do the tips from this employer include amounts not paid voluntarily, not determined by the customer or subject to negotiation (service charges, automatic gratuities), or amounts not paid in a cash medium (cash, check, credit or debit card, gift card, tokens readily exchangeable for a fixed amount such as casino chips, or a payment app)?"] [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["tipjob.listed",{"const":true}],"op":"test"},"then":"tipjob.charged"},{"guard":{"eq":["tipjob.listed",{"const":false}],"op":"test"},"then":"tipjob.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 103, Schedule 1-A, "Determining the amount of qualified tips received by an employee for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.unlawful`

- **Authored helper label:** Were any of the tips from this employer received while performing a service that is a felony or misdemeanor under applicable law, or for prostitution or pornographic activity?
- **Encoded (Bool):** Input — Was any of the work you got these tips for against the law (for example, serving alcohol without a license the state requires), or was any of it prostitution or pornographic activity?
- Expr: `{"op":"input","source":"Was any of the work you got these tips for against the law (for example, serving alcohol without a license the state requires), or was any of it prostitution or pornographic activity?"}`
- Cite: [i1040gi] pp. 101-103, Schedule 1-A, Qualified Tips, "Tips received while performing a service that is a felony or misdemeanor under applicable law are not qualified tips", "Amounts received for prostitution and pornographic activity are not qualified tips" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `tipjob.unlawful_if_listed`

- **Authored helper label:** Whether any of this employer's tips were received for an unlawful service, prostitution or pornographic activity, asked only where the tips were received in a listed occupation (false otherwise)
- **Encoded (Bool):** Choose — [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = true → helper "Were any of the tips from this employer received while performing a service that is a felony or misdemeanor under applicable law, or for prostitution or pornographic activity?"] [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["tipjob.listed",{"const":true}],"op":"test"},"then":"tipjob.unlawful"},{"guard":{"eq":["tipjob.listed",{"const":false}],"op":"test"},"then":"tipjob.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 103, Schedule 1-A, "Determining the amount of qualified tips received by an employee for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `tipjob.tips`

- **Authored helper label:** Qualified tips from this employer, as entered
- **Encoded (NonNegDollars):** Input — What were your tips from this employer in 2025? Take box 7 of its W-2 (social security tips), or a tip amount this employer gave you in box 14 or on a separate statement.
- Expr: `{"op":"input","source":"What were your tips from this employer in 2025? Take box 7 of its W-2 (social security tips), or a tip amount this employer gave you in box 14 or on a separate statement."}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b); pp. 103-104, paragraphs 1 through 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(b) — `tipjob.amount`

- **IRS:** Amount of qualified tips reported by this employer on Form W-2, or reported by you to this employer on Form(s) 4070
- **Encoded (NonNegDollars):** Choose — [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = true → helper "Qualified tips from this employer, as entered"] [helper "Were any of the tips from this employer received in an occupation on the IRS list of occupations that customarily and regularly received tips on or before December 31, 2024?" = false → helper "Year parameter sales.zero"]
- **Refusal:** when tipjob.mixed is true, cannot complete Qualified tips from an employer where some tips were not qualified tips. Splitting one employer's reported tips between qualified and nonqualified tips is outside this tool. Cite: [i1040gi] p. 103, "If you received tips as an employee in more than one occupation for the same employer, only those tips that were received in an occupation on the list ... are considered qualified tips. Do not include tips received in occupations that are not included on this list in line 4a, 4b, or 4c" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["tipjob.listed",{"const":true}],"op":"test"},"then":"tipjob.tips"},{"guard":{"eq":["tipjob.listed",{"const":false}],"op":"test"},"then":"tipjob.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b); pp. 103-104, paragraphs 1 through 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `tipjob.mixed`

- **Authored helper label:** Some of this employer's tips are not qualified tips
- **Encoded (Bool):** (helper "Whether some of this employer's tips were received in an occupation not on the list, asked only where the tips were received in a listed occupation (false otherwise)" = true or helper "Whether this employer's tips include amounts not paid voluntarily or not paid in cash, asked only where the tips were received in a listed occupation (false otherwise)" = true or helper "Whether any of this employer's tips were received for an unlawful service, prostitution or pornographic activity, asked only where the tips were received in a listed occupation (false otherwise)" = true)
- Expr: `{"any":[{"eq":["tipjob.other_work_if_listed",{"const":true}],"op":"test"},{"eq":["tipjob.charged_if_listed",{"const":true}],"op":"test"},{"eq":["tipjob.unlawful_if_listed",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 103, Schedule 1-A, "Determining the amount of qualified tips received by an employee for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(c) — `tipjob.col_c`

- **IRS:** Qualified tips reported on Form 4137, column 1(c), for this employer
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when person.f4137_filed is true, cannot complete The deduction for qualified tips included on Form 4137 (worksheet column (c)). This tool prepares Form 4137 but does not figure the part of its tips that is qualified tips for the deduction. Claim the deduction for tips without this tool, or answer that you do not want the deduction for tips. Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (c), and p. 103, method 4 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (c) (2025; printed date 2026-02-25; sha256 482e9c48)

## 1(d) — `tipjob.col_d`

- **IRS:** Enter the greater of column (b) or column (c)
- **Encoded (NonNegDollars):** Enter the larger of line 1(b) or line 1(c).
- Expr: `{"of":["tipjob.amount","tipjob.col_c"],"op":"larger_of"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (d) (2025; printed date 2026-02-25; sha256 482e9c48)
