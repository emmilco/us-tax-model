# Qualified business income and section 199A dividends — amounts and the choice of Form 8995

- Document: `qbi` (form, tax year 2025)
- Note: Section 199A dividends and the qualified business income of the Schedule C businesses (with a prior-year qualified business loss carryforward), not PTP amounts. Taxable income before QBI is AGI less the selected deduction; Schedule 1-A is outside scope. The Jan. 27, 2026 Form 8995 instruction correction is followed.

## (helper) — `qbi.dividends`

- **Authored helper label:** Qualified section 199A dividends from Form 1099-DIV box 5, leaving out the part on shares held 45 days or less or that you are obliged to pay to someone else
- **Encoded (NonNegDollars):** Input — Qualified section 199A dividends from Form 1099-DIV box 5. Leave out the part paid on shares you held for 45 days or less, and the part you are obliged to pay to someone else; enter only the part that qualifies.
- Expr: `{"op":"input","source":"Qualified section 199A dividends from Form 1099-DIV box 5. Leave out the part paid on shares you held for 45 days or less, and the part you are obliged to pay to someone else; enter only the part that qualifies."}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4; i8995 p. 3, "Qualified REIT dividends include any dividends you received from a REIT held for more than 45 days and for which the payment isn’t obligated to someone else" (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.no`

- **Authored helper label:** Year parameter s3.no (false)
- **Encoded (Bool):** Enter false (s3.no).
- Expr: `{"op":"param","ref":"s3.no"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.prior_form`

- **Authored helper label:** Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?
- **Encoded (Bool):** Input — Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?
- Expr: `{"op":"input","source":"Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.reit_loss`

- **Authored helper label:** Does the latest of your (or, on a joint return, your spouse's) Forms 8995 or 8995-A, from 2024 or earlier, show a qualified REIT dividends and PTP (loss) carryforward (Form 8995, line 17, or the corresponding line of Form 8995-A)?
- **Encoded (Bool):** Input — Does the latest of your (or, on a joint return, your spouse's) Forms 8995 or 8995-A, from 2024 or earlier, show a qualified REIT dividends and PTP (loss) carryforward (Form 8995, line 17, or the corresponding line of Form 8995-A)?
- Expr: `{"op":"input","source":"Does the latest of your (or, on a joint return, your spouse's) Forms 8995 or 8995-A, from 2024 or earlier, show a qualified REIT dividends and PTP (loss) carryforward (Form 8995, line 17, or the corresponding line of Form 8995-A)?"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (gate) — `qbi.reit_loss_if_prior_form`

- **Authored helper label:** Whether the latest Form 8995 or 8995-A, from 2024 or earlier, carries forward a REIT or PTP loss, asked only when a return of 2024 or earlier includes that form (false without it)
- **Encoded (Bool):** Choose — [helper "Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?" = true → helper "Does the latest of your (or, on a joint return, your spouse's) Forms 8995 or 8995-A, from 2024 or earlier, show a qualified REIT dividends and PTP (loss) carryforward (Form 8995, line 17, or the corresponding line of Form 8995-A)?"] [helper "Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["qbi.prior_form",{"const":true}],"op":"test"},"then":"qbi.reit_loss"},{"guard":{"eq":["qbi.prior_form",{"const":false}],"op":"test"},"then":"qbi.no"}],"op":"choose"}`
- Cite: [i8995] p. 4, Line 7, "Include here the qualified portion of PTP (loss) carryforward allowed in calculating taxable income in the current year" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `qbi.suspended`

- **Authored helper label:** Do you (or, on a joint return, your spouse) have losses or deductions of a trade or business that were suspended in an earlier year by another provision (such as the at-risk or passive activity limits) and are allowed in calculating taxable income this year? Leave out a section 179 deduction carried over from 2018 or later and deducted on this return's Schedule C, which is already counted in that Schedule C's profit or loss.
- **Encoded (Bool):** Input — Do you (or, on a joint return, your spouse) have losses or deductions of a trade or business that were suspended in an earlier year by another provision (such as the at-risk or passive activity limits) and are allowed in calculating taxable income this year? Leave out a section 179 deduction carried over from 2018 or later and deducted on this return's Schedule C, which is already counted in that Schedule C's profit or loss.
- Expr: `{"op":"input","source":"Do you (or, on a joint return, your spouse) have losses or deductions of a trade or business that were suspended in an earlier year by another provision (such as the at-risk or passive activity limits) and are allowed in calculating taxable income this year? Leave out a section 179 deduction carried over from 2018 or later and deducted on this return's Schedule C, which is already counted in that Schedule C's profit or loss."}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4; i8995 p. 3, "Such Code provisions include, but aren’t limited to, sections 163(j), 179, 461(l), 465, 469, 704(d), and 1366(d)", "In general, losses and deductions incurred prior to 2018 are not qualified losses or deductions" (2025; created 2025-09-12; sha256 55380ad2)

## (gate) — `qbi.suspended_if_business`

- **Authored helper label:** Whether losses or deductions suspended in an earlier year are allowed this year, asked only when the return has a Schedule C (false without one)
- **Encoded (Bool):** Choose — [s1 helper "The return has a Schedule C" = true → helper "Do you (or, on a joint return, your spouse) have losses or deductions of a trade or business that were suspended in an earlier year by another provision (such as the at-risk or passive activity limits) and are allowed in calculating taxable income this year? Leave out a section 179 deduction carried over from 2018 or later and deducted on this return's Schedule C, which is already counted in that Schedule C's profit or loss."] [s1 helper "The return has a Schedule C" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1.has_sc",{"const":true}],"op":"test"},"then":"qbi.suspended"},{"guard":{"eq":["s1.has_sc",{"const":false}],"op":"test"},"then":"qbi.no"}],"op":"choose"}`
- Cite: [i8995] p. 3, Determining Your Qualified Business Income, "When losses or deductions previously suspended by other Code provisions are allowed in calculating taxable income" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `qbi.coop_patron`

- **Authored helper label:** Are you (or, on a joint return, your spouse) a patron of any agricultural or horticultural cooperative, specified or not (including any qualified payments from one on Form 1099-PATR)?
- **Encoded (Bool):** Input — Are you (or, on a joint return, your spouse) a patron of any agricultural or horticultural cooperative, specified or not (including any qualified payments from one on Form 1099-PATR)?
- Expr: `{"op":"input","source":"Are you (or, on a joint return, your spouse) a patron of any agricultural or horticultural cooperative, specified or not (including any qualified payments from one on Form 1099-PATR)?"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (gate) — `qbi.has_amount`

- **Authored helper label:** The return has a Schedule C or qualified section 199A dividends, so that Form 8995 or 8995-A could be filed
- **Encoded (Bool):** (s1 helper "The return has a Schedule C" = true or helper "Qualified section 199A dividends (Form 1099-DIV box 5), when ordinary dividends (box 1a) are above zero; zero otherwise" > $0 (sales.zero))
- Expr: `{"any":[{"eq":["s1.has_sc",{"const":true}],"op":"test"},{"gt":["qbi.dividends_if_ordinary",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [i8995] p. 1, Who Can Take the Deduction, "Individuals and eligible estates and trusts that have QBI use Form 8995 to figure the QBI deduction if: • You have QBI, qualified REIT dividends, or qualified PTP income or loss" (2025; printed date 2026-01-26; sha256 875843ba)

## (gate) — `qbi.coop_patron_if_amount`

- **Authored helper label:** Whether you are a patron of an agricultural or horticultural cooperative, asked only when the return has a Schedule C or qualified section 199A dividends (false otherwise)
- **Encoded (Bool):** Choose — [helper "The return has a Schedule C or qualified section 199A dividends, so that Form 8995 or 8995-A could be filed" = true → helper "Are you (or, on a joint return, your spouse) a patron of any agricultural or horticultural cooperative, specified or not (including any qualified payments from one on Form 1099-PATR)?"] [helper "The return has a Schedule C or qualified section 199A dividends, so that Form 8995 or 8995-A could be filed" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["qbi.has_amount",{"const":true}],"op":"test"},"then":"qbi.coop_patron"},{"guard":{"eq":["qbi.has_amount",{"const":false}],"op":"test"},"then":"qbi.no"}],"op":"choose"}`
- Cite: [i8995] p. 1, Who Can Take the Deduction, "You have QBI, qualified REIT dividends, or qualified PTP income or loss (all defined later); and", "You aren’t a patron in a specified agricultural or horticultural cooperative" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `qbi.unreported_loss`

- **Authored helper label:** Did you (or, on a joint return, your spouse) have a qualified business net loss in any year from 2018 to 2024 whose return included neither Form 8995 nor Form 8995-A?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) have a qualified business net loss (the qualified business income of all your trades or businesses together less than zero) in any year from 2018 to 2024 whose return included neither Form 8995 nor Form 8995-A?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) have a qualified business net loss (the qualified business income of all your trades or businesses together less than zero) in any year from 2018 to 2024 whose return included neither Form 8995 nor Form 8995-A?"}`
- Cite: [i8995a] p. 6, Schedule C (Form 8995-A), "This includes prior year loss carryforwards even if the loss was unreported or the trade or business that generated the loss is no longer in existence"; i8995 p. 5, Line 16, "This amount will offset QBI in later tax years regardless of whether"; i8995 p. 3, "In general, losses and deductions incurred prior to 2018 are not qualified losses or deductions" (2025; printed date 2026-01-26; sha256 6df1301c)

## (gate) — `qbi.unreported_loss_if_business`

- **Authored helper label:** Whether a qualified business net loss of 2018 to 2024 was never reported on Form 8995 or 8995-A, asked only when the return has a Schedule C (false without one)
- **Encoded (Bool):** Choose — [s1 helper "The return has a Schedule C" = true → helper "Did you (or, on a joint return, your spouse) have a qualified business net loss in any year from 2018 to 2024 whose return included neither Form 8995 nor Form 8995-A?"] [s1 helper "The return has a Schedule C" = false → helper "Year parameter s3.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1.has_sc",{"const":true}],"op":"test"},"then":"qbi.unreported_loss"},{"guard":{"eq":["s1.has_sc",{"const":false}],"op":"test"},"then":"qbi.no"}],"op":"choose"}`
- Cite: [i8995a] p. 6, Schedule C (Form 8995-A), "This includes prior year loss carryforwards even if the loss was unreported or the trade or business that generated the loss is no longer in existence" (2025; printed date 2026-01-26; sha256 6df1301c)

## (helper) — `qbi.unsupported`

- **Authored helper label:** Any of these: a prior-year REIT or PTP loss carryforward; losses or deductions suspended in an earlier year by another provision and allowed this year; being a patron of any agricultural or horticultural cooperative, specified or not. Qualified business income or loss, or PTP income or loss, other than section 199A dividends and the Schedule C businesses is refused by the scope questions on Schedule E, Schedule K-1 and Schedule F income
- **Encoded (Bool):** (helper "Whether the latest Form 8995 or 8995-A, from 2024 or earlier, carries forward a REIT or PTP loss, asked only when a return of 2024 or earlier includes that form (false without it)" = true or helper "Whether losses or deductions suspended in an earlier year are allowed this year, asked only when the return has a Schedule C (false without one)" = true or helper "Whether you are a patron of an agricultural or horticultural cooperative, asked only when the return has a Schedule C or qualified section 199A dividends (false otherwise)" = true)
- Interpretation: amb.2025.qbi_cooperative_patron
- Expr: `{"any":[{"eq":["qbi.reit_loss_if_prior_form",{"const":true}],"op":"test"},{"eq":["qbi.suspended_if_business",{"const":true}],"op":"test"},{"eq":["qbi.coop_patron_if_amount",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8995] p. 4, Line 7, "Include here the qualified portion of PTP (loss) carryforward allowed in calculating taxable income in the current year"; p. 3, Determining Your Qualified Business Income, "When losses or deductions previously suspended by other Code provisions are allowed in calculating taxable income"; p. 1, Who Can Take the Deduction, "You aren’t a patron in a specified agricultural or horticultural cooperative"; p. 3, Determining Your Qualified Business Income, "If you received qualified payments reported to you on Form 1099-PATR from a specified agricultural or horticultural cooperative, you must reduce your QBI by the patron reduction and use Form 8995-A" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `qbi.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.eligible`

- **Authored helper label:** Amount from qbi.dividends_if_ordinary
- **Encoded (NonNegDollars):** Enter the amount from helper "Qualified section 199A dividends (Form 1099-DIV box 5), when ordinary dividends (box 1a) are above zero; zero otherwise".
- **Refusal:** when qbi.unreported_loss_if_business is true, cannot complete Form 8995, line 3, a qualified business loss of 2018 to 2024 never reported on Form 8995 or 8995-A. A business loss of an earlier year that no Form 8995 or 8995-A carried forward is outside this tool. Cite: [i8995a] p. 6, Schedule C (Form 8995-A), "This includes prior year loss carryforwards even if the loss was unreported or the trade or business that generated the loss is no longer in existence" (2025; printed date 2026-01-26; sha256 6df1301c)
- **Refusal:** when qbi.unsupported is true, cannot complete Forms 8995 / 8995-A business or PTP path. Only section 199A dividend income without loss carryovers is supported. Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)
- Expr: `{"from":"qbi.dividends_if_ordinary","op":"copy"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## 3 — `qbi.carryforward`

- **IRS:** Qualified business net (loss) carryforward from the prior year (as a positive amount)
- **Encoded (NonNegDollars):** Input — The qualified business loss carryforward from line 16 of your latest Form 8995 from 2024 or earlier (or, if that form was a Form 8995-A, from line 6 of Schedule C (Form 8995-A) attached to it), entered as a positive amount (zero if none)
- Expr: `{"op":"input","source":"The qualified business loss carryforward from line 16 of your latest Form 8995 from 2024 or earlier (or, if that form was a Form 8995-A, from line 6 of Schedule C (Form 8995-A) attached to it), entered as a positive amount (zero if none)"}`
- Cite: [i8995] p. 4, Line 3, "Include here the qualified portion of trade or business (loss) carryforward allowed in calculating taxable income in the current year"; p. 5, Line 16, "This is the amount to be carried forward to the next year" (owner: the printed amount); i8995a p. 6, Line 6, "The amount reported on this line must be reported in the next tax year on Schedule C (Form 8995-A), line 2, or Form 8995, line 3" (2025; printed date 2026-01-26; sha256 875843ba)

## (gate) — `qbi.carryforward_if_prior_form`

- **Authored helper label:** The qualified business loss carryforward, asked only when a return of 2024 or earlier includes Form 8995 or 8995-A (zero without it)
- **Encoded (NonNegDollars):** Choose — [helper "Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?" = true → line 3] [helper "Did your (or, on a joint return, your spouse's) 2024 return, or any earlier one, include Form 8995 or Form 8995-A (Qualified Business Income Deduction)?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["qbi.prior_form",{"const":true}],"op":"test"},"then":"qbi.carryforward"},{"guard":{"eq":["qbi.prior_form",{"const":false}],"op":"test"},"then":"qbi.zero"}],"op":"choose"}`
- Cite: [i8995] p. 4, Line 3, "Include here the qualified portion of trade or business (loss) carryforward allowed in calculating taxable income in the current year"; p. 5, Line 16, "This is the amount to be carried forward to the next year" (2025; printed date 2026-01-26; sha256 875843ba)

## (gate) — `qbi.business_any`

- **Authored helper label:** Business income or a carryforward with taxable income above the Form 8995 threshold
- **Encoded (Bool):** (f8995 line 2 ≠ $0 (sales.zero) or helper "The qualified business loss carryforward, asked only when a return of 2024 or earlier includes Form 8995 or 8995-A (zero without it)" > $0 (sales.zero))
- Expr: `{"any":[{"ne":["f8995.line2",{"param":"sales.zero"}],"op":"test"},{"gt":["qbi.carryforward_if_prior_form",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [i8995] p. 1, Who Can Take the Deduction (owner: Form 8995-A with business income refused) (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `qbi.via_8995a`

- **Authored helper label:** Form 8995-A (section 199A dividends only)
- **Encoded (NonNegDollars):** Enter the amount from f8995a line 39.
- **Refusal:** when qbi.business_any is true, cannot complete Form 8995-A with qualified business income (taxable income above the threshold). The qualified business income deduction above the Form 8995 threshold is outside this tool. Cite: [i8995a] p. 1, Who Can Take the Deduction (2025; printed date 2026-01-26; sha256 6df1301c)
- Expr: `{"from":"f8995a.line39","op":"copy"}`
- Cite: [f8995a] Form 8995-A (2025), line 39 (2025; created 2025-09-12; sha256 3362db81)

## (helper) — `qbi.deductions_before`

- **Authored helper label:** Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction
- **Encoded (NonNegDollars):** Add sa helper "Deduction selected for Form 1040 line 12e" and f1040 line 13b.
- Expr: `{"of":["sa.deduction","f1040.line13b"],"op":"sum"}`
- Cite: [i8995-correction] Correction to 2025 Form 8995 instructions, Line 11, "Form 1040 or 1040-SR filers: Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b" (Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28; sha256 926735a0)

## (helper) — `qbi.taxable_before`

- **Authored helper label:** Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, negative when the deductions are more than adjusted gross income
- **Encoded (Dollars):** Subtract helper "Form 1040 lines 12e and 13b, the deductions taken before the QBI deduction" from sa helper "Form 1040 line 11b adjusted gross income".
- Expr: `{"from":"sa.agi","op":"subtract","take":"qbi.deductions_before"}`
- Cite: [i8995-correction] Correction to 2025 Form 8995 instructions, Line 11, "Enter your taxable income figured before any QBI deduction", "Form 1040 or 1040-SR filers: Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b" (Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28; sha256 926735a0)

## (helper) — `qbi.net_capital_gain`

- **Authored helper label:** Add sd.net_gain, f1040.line3a
- **Encoded (NonNegDollars):** Add sd helper "Nonnegative net capital gain for QDCGT" and f1040 helper "Qualified dividends (Form 1040 line 3a), when ordinary dividends (box 1a) are above zero; zero otherwise".
- Expr: `{"of":["sd.net_gain","f1040.line3a_if_ordinary"],"op":"sum"}`
- Cite: [f8995] p. 1, "Enter your net capital gain, if any, increased by any qualified dividends" (line 12); i8995 p. 4, Line 12, "line 3a, plus your net capital gain", "your net capital gain is the smaller of Schedule D (Form 1040), line 15 or 16, unless line 15 or 16 is zero or less" (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.threshold`

- **Authored helper label:** Year parameter qbi.threshold
- **Encoded (NonNegDollars):** Enter single $197,300; mfj $394,600; mfs $197,300; hoh $197,300; qss $197,300 (qbi.threshold).
- Expr: `{"op":"param","ref":"qbi.threshold"}`
- Cite: [f8995] Form 8995 (2025), lines 1–17; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.use_8995a`

- **Authored helper label:** Taxable income before QBI exceeds the Form 8995 threshold
- **Encoded (Bool):** helper "Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, negative when the deductions are more than adjusted gross income" > helper "Year parameter qbi.threshold"
- Expr: `{"gt":["qbi.taxable_before","qbi.threshold"],"op":"test"}`
- Cite: [f8995] p. 1, "Use this form if your taxable income, before your qualified business income deduction, is at or below $197,300 ($394,600 if married filing jointly)"; i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.deduction`

- **Authored helper label:** Select Form 8995 or dividend-only Form 8995-A
- **Encoded (NonNegDollars):** Choose — [helper "Taxable income before QBI exceeds the Form 8995 threshold" = true → helper "Form 8995-A (section 199A dividends only)"] [helper "Taxable income before QBI exceeds the Form 8995 threshold" = false → f8995 line 15]
- Expr: `{"alternatives":[{"guard":{"eq":["qbi.use_8995a",{"const":true}],"op":"test"},"then":"qbi.via_8995a"},{"guard":{"eq":["qbi.use_8995a",{"const":false}],"op":"test"},"then":"f8995.line15"}],"op":"choose"}`
- Cite: [f8995] p. 1, "Use this form if your taxable income, before your qualified business income deduction, is at or below $197,300 ($394,600 if married filing jointly)", "Qualified business income deduction. Enter the smaller of line 10 or line 14" (line 15); i8995 pp. 3–4 (2025; created 2025-09-12; sha256 55380ad2)

## (helper) — `qbi.dividends_if_ordinary`

- **Authored helper label:** Qualified section 199A dividends (Form 1099-DIV box 5), when ordinary dividends (box 1a) are above zero; zero otherwise
- **Encoded (NonNegDollars):** Choose — [div helper "Ordinary dividends (box 1a) are above zero" = true → helper "Qualified section 199A dividends from Form 1099-DIV box 5, leaving out the part on shares held 45 days or less or that you are obliged to pay to someone else"] [div helper "Ordinary dividends (box 1a) are above zero" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["div.has_ordinary",{"const":true}],"op":"test"},"then":"qbi.dividends"},{"guard":{"eq":["div.has_ordinary",{"const":false}],"op":"test"},"then":"qbi.zero"}],"op":"choose"}`
- Cite: [f1099div] p. 5, Instructions for Recipient, "Box 5. Shows the portion of the amount in box 1a that may be eligible for the 20% qualified business income deduction under section 199A" (January 2024 (continuous-use form); sha256 4ea1de80)
