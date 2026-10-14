# Stage 0 premise checks — complete

Status: **complete**. Every premise in `spec/spec.md` section 10 is recorded below
as confirmed or corrected. One premise required a scope decision: the owner
approved the dividend-only Form 8995-A expansion on 2026-10-13, and it is applied
in `spec/spec.md` section 2.1 and `spec/design.md` Stage 4. Two items belong to
the ambiguity register rather than a specification change (P03, P13; noted in
their sections). Stage 1 may begin after the owner's review of this file.

Method and reviewers: the P09 pass was made by Codex (agent); the remaining
checks and this consolidation were made in an OpenCode session (DeepSeek agent).
All findings are inspection of local `pdftotext` extracts of the archived
snapshots (linear extraction used where two-column layout interleaves), not a
human transcription review, proof of correctness, or a class B fixture. SHA-256
hashes and fetch times for every cited snapshot are in `manifest.json`; offline
verification (`python3 tools/fetch_sources.py`) passes for all 45 archived
documents. Page references are PDF page numbers of the archived snapshots; web
snapshots are cited by section.

| ID | Premise | Result |
| --- | --- | --- |
| P01 | Schedule D versus Qualified Dividends worksheet selection | Confirmed — `i1040gi` p. 36; `i1040sd` p. 15 |
| P02 | $100,000 Tax Table / Tax Computation Worksheet switch | Confirmed — `i1040gi` p. 36, p. 68, p. 80 |
| P03 | Rounding, including Form 8949 rows versus Schedule D totals | Confirmed; row-versus-total reconciliation is not stated in any snapshot — ambiguity register entry required |
| P04 | Schedule D lines 1a and 8a aggregate reporting conditions | Confirmed — `i1040sd` pp. 10–11; `i8949` p. 4 |
| P05 | Foreign tax credit without Form 1116 | Confirmed — `i1116` p. 1; `f1040s3` p. 1 |
| P06 | Forms 8959 and 8960 thresholds by filing status | Confirmed — `i8959` p. 1; `i8960` p. 2 |
| P07 | Excess Social Security and the single-employer exception | Confirmed — `i1040gi` p. 117; `f1040s3` p. 1 |
| P08 | Form 8949 box set and adjustment codes | Confirmed; printed code set is larger than the encoding subset — the narrowing is deliberate (spec 2.2) |
| P09 | Form 8995 sufficiency for section 199A dividends alone | Corrected; owner approved 2026-10-13; applied to spec |
| P10 | Schedule A structure, medical floor, SALT limit and reduction | Confirmed — `f1040sa` p. 1; `i1040sca` pp. 1, 3, 7 |
| P11 | Form 4952 structure, election, worksheet routing and filing exception | Confirmed — `f4952` pp. 1, 3–4; `i1040gi` p. 36; `i1040sd` p. 15 |
| P12 | Form 8283 sections and charitable deduction limitations | Confirmed — `i8283` pp. 1–3, 9; `p526` pp. 23–25, 28; `i1040sca` p. 9 |
| P13 | Form 8960 deductions and prior-year state tax refunds | Confirmed — `i8960` pp. 14–18; `i1040gi` p. 90; scope note |
| P14 | TY2026 charitable floor and itemized deduction value cap | Confirmed — `p505-2026` pp. 2, 36–37; research phrasing reconciled |

## P01 — Schedule D versus Qualified Dividends worksheet selection

**Finding: confirmed.**

Directly inspected evidence:

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 36, “Line 16” | “Schedule D Tax Worksheet. Use the Schedule D Tax Worksheet in the Instructions for Schedule D … if: • You have to file Schedule D, line 18 or 19 of Schedule D is more than zero, and lines 15 and 16 of Schedule D are gains; or • You have to file Form 4952 and you have an amount on line 4g, even if you don’t need to file Schedule D.” The same passage gives the Qualified Dividends and Capital Gain Tax Worksheet when the Schedule D Tax Worksheet is not required and any of: qualified dividends on line 3a; no Schedule D and capital gain distributions on line 7a; or Schedule D lines 15 and 16 both more than zero. Form 8615 and Form 2555 route to other worksheets. |
| [i1040sd.pdf](i1040sd.pdf) | TY2025, printed 2025-12-11 | p. 15, head of the Schedule D Tax Worksheet | “Complete this worksheet only if line 18 or line 19 of Schedule D is more than zero and lines 15 and 16 of Schedule D are gains or if you file Form 4952 and you have an amount on line 4g, even if you don’t need to file Schedule D. Otherwise, complete the Qualified Dividends and Capital Gain Tax Worksheet…” Same page states the exception: don’t use either worksheet if Schedule D line 15 or 16 is zero or less and there are no qualified dividends, or if Form 1040 line 15 is zero or less. |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 38, head of the Qualified Dividends and Capital Gain Tax Worksheet | “Before you begin: See the earlier instructions for line 16 to see if you can use this worksheet to figure your tax.” |

Interpretation: selection is determined by Schedule D lines 15, 16, 18, 19 and
Form 4952 line 4g alone. This matches the spec's scope: the Schedule D Tax
Worksheet is fed only by 1099‑DIV boxes 2b–2d and by the Form 4952 election.
Form 8615, Form 2555 and Form 8814 routing are outside scope and become cited
refusals when encoding.

## P02 — $100,000 Tax Table / Tax Computation Worksheet switch

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 36, “Line 16” | “Tax Table or Tax Computation Worksheet. If your taxable income is less than $100,000, you must use the Tax Table, later in these instructions, to figure your tax. … If your taxable income is $100,000 or more, use the Tax Computation Worksheet right after the Tax Table.” |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 68 (2025 Tax Table banner); p. 80 (Tax Computation Worksheet) | The Tax Table carries the banner “See the instructions for line 16 to see if you must use the Tax Table below to figure your tax.” The Tax Computation Worksheet's first row is “At least $100,000 but not over $103,350.” |

Interpretation: exact switch language is “less than $100,000” / “$100,000 or
more”; the $100,000 value is a boundary, not a round-to-lookup range, and both
sides of the boundary must be covered by tests at Stage 1.

## P03 — Rounding, including Form 8949 rows versus Schedule D totals

**Finding: confirmed as to wording; the row-versus-total reconciliation the
premise asks about is not stated in any archived instruction. Record the chosen
reading in the ambiguity register (spec section 5) at encoding time.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 23, “Rounding Off to Whole Dollars” | “You can round off cents to whole dollars on your return and schedules. If you do round to whole dollars, you must round all amounts. To round, drop amounts under 50 cents and increase amounts from 50 to 99 cents to the next dollar. … If you have to add two or more amounts to figure the amount to enter on a line, include cents when adding the amounts and round off only the total.” |
| [i1040sd.pdf](i1040sd.pdf) | TY2025, printed 2025-12-11 | p. 9, “Rounding Off to Whole Dollars” | Same rule, scoped: “You can round off cents to whole dollars on your Schedule D.…” |
| [i8949.pdf](i8949.pdf) | TY2025, printed 2026-01-20 | p. 3, “Rounding Off to Whole Dollars” | “You can round off cents to whole dollars on Form 8949. If you do round to whole dollars, round all amounts. To round, drop cent amounts under 50 cents and increase cent amounts over 49 cents to the next dollar. For example, $1.49 becomes $1 and $1.50 becomes $2.” The Form 8949 text does **not** carry the “include cents when adding … round off only the total” sentence. |

Interpretation: all three documents describe half-up rounding to whole dollars.
Form 8949 instructs rounding of all amounts on the form; the 1040 and Schedule D
instruct rounding off only totals when adding. The documents do not state how a
rounded Form 8949 row feeds a Schedule D total. The reading must be chosen,
justified and recorded in the ambiguity register before the Schedule D path is
encoded; the natural reading consistent with both texts is: keep cents through
additions, round at the point where the instructions direct a whole-dollar entry
(line-by-line on Form 8949 if the taxpayer rounds there; totals on Schedule D by
summing exact cents and rounding the total). This is a register matter, not a
specification change.

## P04 — Schedule D lines 1a and 8a aggregate reporting conditions

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i1040sd.pdf](i1040sd.pdf) | TY2025, printed 2025-12-11 | pp. 10–11, “Lines 1a and 8a—Transactions Not Reported on Form 8949” | “You can report on line 1a (for short-term transactions) or line 8a (for long-term transactions) the aggregate totals from any transactions (except sales of collectibles) for which:” — a 1099‑B/1099‑DA (or substitute) showing basis reported to the IRS with no adjustments in box 1f/1g (1099‑B) or 1h/1i (1099‑DA); the Ordinary box (box 2 on 1099‑B; box 6 on 1099‑DA) not checked; the QOF box (box 3 on 1099‑B; box 3b on 1099‑DA) not checked; no QOF deferral or termination; and no adjustments needed to basis or to the type of gain or loss. If chosen, the transactions are not reported on Form 8949 and no statement is attached. |
| [i1040sd.pdf](i1040sd.pdf) | TY2025, printed 2025-12-11 | p. 11, examples | Worked examples: a single transaction enters on line 8a columns (d), (e), (h); two like transactions are combined into aggregate totals. If the basis shown is incorrect, the transaction must go on Form 8949 instead. |
| [i8949.pdf](i8949.pdf) | TY2025, printed 2026-01-20 | p. 4, “Exception 1” | “Form 8949 isn’t required for certain transactions. You may be able to aggregate those transactions and report them directly on either line 1a … or line 8a … of Schedule D.” Conditions as above. |

Interpretation: matches spec section 2.1 (“Broker totals where basis was reported
and no adjustments apply”). The exclusion for collectibles and the QOF
conditions are refusal triggers to encode. The aggregate path and the Form 8949
path are alternatives for the same transactions; the tool must pick one treatment
and explain it (spec section 8).

## P05 — Foreign tax credit without Form 1116

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i1116.pdf](i1116.pdf) | TY2025, printed 2025-12-23 | p. 1, “Election To Claim the Foreign Tax Credit Without Filing Form 1116” | Available only if **all** of: foreign source gross income was “passive category income” (including most interest and dividends; for this purpose also high-taxed income and certain export financing interest); the income and foreign taxes were reported on a qualified payee statement (1099‑DIV, 1099‑INT, K‑1 forms, similar substitutes); and total creditable foreign taxes are not more than $300 ($600 if married filing jointly). Not available to estates or trusts. |
| [i1116.pdf](i1116.pdf) | TY2025, printed 2025-12-23 | p. 1, election paragraphs | Rules that follow: no carryovers to or from any year to which the election applies; the creditability rules still apply; the taxes available for credit are reduced by any amount for line 12. |
| [i1116.pdf](i1116.pdf) | TY2025, printed 2025-12-23 | p. 1, election paragraphs | “To make the election, just enter on the foreign tax credit line of your tax return (for example, Schedule 3 (Form 1040), Part I, line 1) the smaller of (a) your total foreign tax, or (b) your regular tax.” |
| [f1040s3.pdf](f1040s3.pdf) | TY2025, created 2025-11-17 | p. 1, line 1 | “Foreign tax credit. Attach Form 1116 if required.” |

Interpretation: the limit and conditions are the $300/$600 ceiling with the
passive/qualified-payee conditions, matching spec section 2.1 (“Simple path
only: the election for small amounts of passive foreign tax”) and section 2.2
(refusal above the limit or when Form 1116 is otherwise required). Encoding
note: the credit is the smaller of total foreign tax or regular tax; K‑1 payee
statements are listed by the instructions but those income types are outside the
tool's scope, so in-scope payee statements are Form 1099‑INT and Form 1099‑DIV.

## P06 — Forms 8959 and 8960 thresholds by filing status

**Finding: confirmed; the two forms treat qualifying surviving spouses
differently, and both must be encoded per filing status.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i8959.pdf](i8959.pdf) | TY2025, printed 2025-08-07 | p. 1, “Threshold Amounts for Additional Medicare Tax” | Married filing jointly $250,000; married filing separately $125,000; single $200,000; head of household $200,000; qualifying surviving spouse $200,000. “The threshold amounts below aren't indexed for inflation.” |
| [i8959.pdf](i8959.pdf) | TY2025, printed 2025-08-07 | p. 1, intro and filing triggers | Employer withholds on wages above $200,000 in the year; filing is triggered when Medicare wages on any single W‑2 (box 5) exceed $200,000 or total Medicare wages plus RRTA exceed the filing-status threshold. |
| [i8960.pdf](i8960.pdf) | TY2025, printed 2026-02-04 | p. 2, “Application to Individuals” | NIIT is 3.8% of the smaller of MAGI over the threshold or NII, with: married filing jointly **or qualifying surviving spouse** $250,000; married filing separately $125,000; single or head of household $200,000. |

Interpretation: qualifying surviving spouse is $200,000 for Form 8959 and
$250,000 for Form 8960. Parameters must be keyed per form and filing status; a
shared filing-status table would be wrong for this one cell.

## P07 — Excess Social Security and the single-employer exception

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 117, “Line 11—Excess Social Security and Tier 1 RRTA Tax Withheld” | “If you, or your spouse if filing a joint return, had more than one employer for 2025 and total wages of more than $176,100, too much social security or tier 1 railroad retirement (RRTA) tax may have been withheld. You can take a credit on this line for the amount withheld in excess of $10,918.20. But if any one employer withheld more than $10,918.20, you can't claim the excess on your return. The employer should adjust the tax for you. If the employer doesn't adjust the overcollection, you can file a claim for refund using Form 843. Figure this amount separately for you and your spouse.” |
| [f1040s3.pdf](f1040s3.pdf) | TY2025, created 2025-11-17 | p. 1, line 11 | “Excess social security and tier 1 RRTA tax withheld.” |

Interpretation: the credit is total withholding in excess of $10,918.20 across
employers (>$176,100 of wages), with the single-employer exception: if any one
employer withheld more than $10,918.20, the excess is not claimed on the return
(Form 843 refund instead). $10,918.20 is 6.2% of $176,100 (arithmetic check).
The amount is figured separately for each spouse; in scope only the single-filer
path will be reachable until joint returns are supported.

## P08 — Form 8949 box set and adjustment codes

**Finding: confirmed. The printed box set now includes digital-asset boxes, and
the printed adjustment-code set is larger than the encoding subset; the spec's
narrowing stands and each refused code must produce a cited refusal.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i8949.pdf](i8949.pdf) | TY2025, printed 2026-01-20 | p. 1, “What's New” | “New boxes G, H, and I for short-term digital asset transactions. … Do not use box C to report short-term digital asset transactions. … New boxes J, K, and L for long-term digital asset transactions. … Do not use box F to report long-term digital asset transactions.” |
| [i8949.pdf](i8949.pdf) | TY2025, printed 2026-01-20 | pp. 3–4, box definitions | Part I: box A or G — short-term, basis reported to the IRS; box B or H — short-term, no basis reported; box C or I — short-term transactions for which none of A, B, G, H can be checked. Part II: box D or J — long-term, basis reported; box E or K — long-term, no basis reported; box F or L — long-term for which none of D, E, J, K can be checked. |
| [i1040sd.pdf](i1040sd.pdf) | TY2025, printed 2025-12-11 | p. 1, “What's New” | “Codes G, H, I, J, K, and L were added to lines 1b, 2, 3, 8b, 9, and 10 [of Schedule D] to represent the reporting of digital asset transactions.” |
| [i8949.pdf](i8949.pdf) | TY2025, printed 2026-01-20 | pp. 8–11, “How To Complete Form 8949, Columns (f) and (g)” | Printed adjustment codes: B (basis shown is incorrect), C (collectibles), D (accrued market discount), E (selling expenses, option premiums, digital asset transaction costs), H (main home exclusion), L (nondeductible loss other than a wash sale), M (multiple transactions on one row), N (nominee), O (other), P (foreign partner sale), Q (QSB stock exclusion), R (gain postponement), S (section 1244 loss over the limit), T (incorrect type of gain or loss), W (wash sale), X (DC Zone / qualified community assets exclusion), Y (QOF prior-year deferral), Z (QOF deferral election). Multiple codes on one row are entered in alphabetical order with no separators, and the net adjustment is entered in column (g). |

Interpretation: for securities the box set is A–F; boxes G–L are digital assets
and refused (spec section 2.2). The spec allows only adjustments: none, code B,
code W — every other printed code is a refusal path and each refusal must cite
the instruction requiring the form as printed. Because a wrong broker basis
(code B) is a plausible situation and is in scope, the column
(g) handling of code B (reported basis in column (e), correcting adjustment in
column (g), per the “Worksheet for Basis Adjustments in Column (g)”, p. 11) must
be encoded and tested with both signs of the adjustment.

## P09 — Does Form 8995 suffice for section 199A dividends alone?

**Finding: no, not for every income level in scope. Corrected; owner approved
the proposed expansion 2026-10-13; applied.**

Directly inspected evidence:

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i8995.pdf](i8995.pdf) | TY2025, printed 2026-01-26 | PDF p. 1, “Who Can Take the Deduction” | Eligibility includes qualified REIT dividends, but use of Form 8995 also requires taxable income before the QBI deduction no greater than $394,600 for married filing jointly or $197,300 for all other returns, and no specified cooperative patron status. Otherwise the instructions direct use of Form 8995-A. |
| [f8995.pdf](f8995.pdf) | TY2025, created 2025-09-12 | PDF p. 1, applicability statement above line 1 | The form itself repeats the income ceiling and cooperative exclusion. |
| [i8995a.pdf](i8995a.pdf) | TY2025, printed 2026-01-26 | PDF p. 1, “Who Can Take the Deduction” | The higher-income applicability conditions explicitly include qualified REIT dividends. |
| [f8995a.pdf](f8995a.pdf) | TY2025, created 2025-09-12 | PDF p. 1, applicability statement; p. 2, Part IV | The form states the higher-income condition and has a REIT/PTP component within the deduction calculation. |

Interpretation: having only section 199A dividends does not exempt the filer from
the form-selection income threshold. A high-income return with this income can
therefore exceed the agreed Form 8995-only scope. This is a form-selection
boundary, not a conclusion that the dividend deduction itself disappears above
the threshold. No conclusion is drawn about any particular filer's taxable income
or dividend boxes.

### Decision and application (2026-10-13)

The owner approved the recommended dividend-only expansion. Applied:
`spec/spec.md` section 2.1 now reads “Forms 8995 and 8995-A — Section 199A
dividends from Form 1099-DIV box 5 only; select the form using its cited
applicability conditions. Form 8995-A coverage is limited to the dividend-only
path and the lines necessary to compute and report that deduction”, and
`spec/design.md` Stage 4 now reads “Forms 8995 and 8995-A for section 199A
dividends, with cited form selection.” The refusal of other qualified business
income is unchanged. Exact gates, carryover treatment, holding-period
conditions, and required lines still need source review; that review belongs to
Stage 4.

### Post-release correction to the Form 8995 instructions (flagged for Stage 4)

The IRS published a correction to the 2025 Instructions for Form 8995: for
copies viewed, printed, or downloaded before 2026-01-27, page 4, line 11 (the
computation of taxable income before the QBI deduction) was incorrect for the
first two bullets. The notice is archived as `i8995-correction.html` (published
2026-02-13; page last reviewed 2026-06-28) and states the corrected text:
“Form 1040 or 1040-SR filers: Form 1040 or 1040-SR, line 11a, minus lines 12e
and 13b. / 1040-NR filers: 1040-NR, line 11a, minus lines 12, 13b, and 13c.”
The archived `i8995.pdf` snapshot (printed 2026-01-26) and the current web
version (`i8995-html.html`) both extract with line 11 matching the corrected
text. Stage 4 must encode line 11 from the corrected wording and pin both
snapshots. The correction does not change form selection; the P09 decision
stands.

## P10 — Schedule A structure, medical floor, SALT limit and reduction

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [f1040sa.pdf](f1040sa.pdf) | TY2025, created 2025-11-20 | p. 1, form | Line structure: 1 medical and dental expenses; 2 Form 1040 line 11b; 3 line 2 × 7.5%; 4 line 1 minus line 3, floored at zero; 5a–5c state and local income/sales, real estate, personal property taxes; 5d add; 5e “Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately) … see instructions” if Form 1040 or 1040-SR, line 11b is more than $500,000 ($250,000 married filing separately), or if Form 2555, Form 4563, or Puerto Rico income applies; 6 other taxes; 7 lines 5e + 6; 8a–8c home mortgage interest and points, 8e total; 9 investment interest, “Attach Form 4952 if required”; 10 lines 8e + 9; 11 gifts by cash or check; 12 “Other than by cash or check … You must attach Form 8283 if over $500”; 13 carryover from prior year; 14 add lines 11–13; 15 casualty and theft losses (refused); 16 other (list); 17 total, lines 4 through 16. |
| [i1040sca.pdf](i1040sca.pdf) | TY2025, printed 2025-12-08 | p. 1, “What's New” | “State and local tax (SALT) deduction limit increased. The overall limit on the deduction for state and local income, sales, and property taxes has increased to $40,000 ($20,000 if married filing separately). The overall limit is reduced if your modified adjusted gross income is more than $500,000 ($250,000 if married filing separately) but will not be reduced below $10,000 ($5,000 if married filing separately).” |
| [i1040sca.pdf](i1040sca.pdf) | TY2025, printed 2025-12-08 | p. 1, “Medical and Dental Expenses” | “You can deduct only the part of your medical and dental expenses that exceeds 7.5% of the amount of your adjusted gross income on Form 1040 or 1040-SR, line 11b.” |
| [i1040sca.pdf](i1040sca.pdf) | TY2025, printed 2025-12-08 | p. 3, “Line 5” | “The deduction for state and local taxes is generally limited to $40,000 ($20,000 if married filing separately). State and local taxes subject to this limit are the taxes that you include on lines 5a, 5b, and 5c.” |
| [i1040sca.pdf](i1040sca.pdf) | TY2025, printed 2025-12-08 | p. 7, “State and Local Tax Deduction” and the worksheet | If Form 1040 line 11b is $500,000 or less ($250,000 married filing separately) and no Form 2555/4563/Puerto Rico income, enter the smaller of line 5d or $40,000; otherwise complete the worksheet: (1) if 5d is more than $10,000 ($5,000 married filing separately) enter $40,000; (2) Form 1040 line 11b; (3a–3e) Puerto Rico/2555/4563 addbacks; (4) lines 2 + 3e; (5) enter $500,000 ($250,000 married filing separately); (6) excess over line 5, or skip; (7) line 6 × 30%; (8) line 1 minus line 7; (9) larger of line 8 or $10,000; (10) smaller of line 9 (half if married filing separately) or line 5d → line 5e. |

Interpretation: the 2025 Schedule A carries the raised SALT limit ($40,000 at a
$500,000 phase-down start, 30% phase-down rate, $10,000 floor; halves for
married filing separately) inside a cited worksheet. The medical floor (7.5%)
and the itemized line structure match spec section 2.1. Line 13 (charitable
carryover) and line 15/16 sub-cases remain refusals per spec section 2.2.

## P11 — Form 4952 structure, election, worksheet routing and filing exception

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [f4952.pdf](f4952.pdf) | TY2025, created 2025-05-28 | p. 1, form | Part I: 1 investment interest paid or accrued; 2 disallowed from 2024 line 7; 3 total. Part II: 4a gross income from property held for investment; 4b qualified dividends included on 4a; 4c 4a − 4b; 4d net gain from dispositions; 4e smaller of 4d or net capital gain; 4f 4d − 4e; 4g “Enter the amount from lines 4b and 4e that you elect to include in investment income”; 4h 4c + 4f + 4g; 5 investment expenses; 6 4h − 5, floored at zero. Part III: 7 carryforward to 2026; 8 deduction, smaller of 3 or 6. |
| [f4952.pdf](f4952.pdf) | TY2025, created 2025-05-28 | p. 3, “Who Must File,” Exception | “You don't have to file Form 4952 if all of the following apply. • Your investment income from interest and ordinary dividends minus any qualified dividends is more than your investment interest expense. • You don't have any other deductible investment expenses. • You don't have any carryover of disallowed investment interest expense from 2024.” |
| [f4952.pdf](f4952.pdf) | TY2025, created 2025-05-28 | pp. 3–4, line 4g instructions | Election mechanics: enter the amount on line 4g (not more than 4b + 4e) and also “on … The Schedule D Tax Worksheet, line 3.” “If you file Form 1040 or 1040-SR and enter an amount on line 4g, use the Schedule D Tax Worksheet … to figure the amount to enter on Form 1040 or 1040-SR, line 16.” “Don't reduce the amount of qualified dividends on Form 1040 or 1040-SR, line 3a … by any part of the amount on line 4g.” Attribution note: the 4g amount is treated first as attributable to net capital gain (4e), then qualified dividends (4b); the taxpayer may elect to attribute less to 4e and more to 4b (relevant to Form 1116, which is out of scope; the default treatment must be encoded). |
| [i1040sd.pdf](i1040sd.pdf) | TY2025, printed 2025-12-11 | p. 15, Schedule D Tax Worksheet line 3 | “Enter the amount from Form 4952 (used to figure investment interest expense deduction), line 4g.” |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 36, “Line 16” | The line 4g election forces the Schedule D Tax Worksheet “even if you don't need to file Schedule D” (see P01). |
| [f4952.pdf](f4952.pdf) | TY2025, created 2025-05-28 | p. 4, line 8 instructions | Individuals enter the line 8 amount on Schedule A line 9; the part attributable to royalties goes on Schedule E; the part attributable to a non-passive trade or business goes on the business schedule; at-risk parts go through Form 6198. Deductible interest may be an AMT adjustment (Form 6251, out of scope). |

Interpretation: the premise's three questions resolve as: (a) line structure as
above; (b) the 4g election routes the return to the Schedule D Tax Worksheet and
adds the elected amount at its line 3, while qualified dividends on line 3a are
not reduced; (c) the form can be skipped only under the three-part exception.
Encoding notes: the royalties / non-passive trade-or-business / Form 6198
allocation branches of line 8 should be encoded as cited refusals (spec section
2.1 computes the plain individual case); the optional attribution election tied
to Form 1116 is out of scope, and the default attribution (4e first, then 4b)
is the one to encode. A prior-year carryover (line 2 > 0) is refused per spec
section 2.2; the line 6 floors and smaller-ofs need both-side tests.

## P12 — Form 8283 sections and charitable deduction limitations

**Finding: confirmed.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i8283.pdf](i8283.pdf) | December 2025, printed 2026-01-30 | pp. 1–2, “Who Must File” | “You must file one or more Forms 8283 if the amount of your deduction for each noncash contribution is more than $500. You must also file Form 8283 if you have a group of similar items for which a total deduction of over $500 is claimed. … 'amount of your deduction' means your deduction before applying any income limits that could result in a carryover.” |
| [i8283.pdf](i8283.pdf) | December 2025, printed 2026-01-30 | pp. 2–3, “Which Sections To Complete,” “Section A” | Section A: items (or groups of similar items) with a deduction of more than $500 but not more than $5,000; plus specified items even above $5,000 — publicly traded securities (any amount), certain intellectual property, qualified vehicles, and inventory-type property. Section B: items over $5,000 per item or group; “Items reportable in Section B require a written qualified appraisal by a qualified appraiser.” |
| [i8283.pdf](i8283.pdf) | December 2025, printed 2026-01-30 | p. 9, “Securities” | “For donations of publicly traded securities in any amount, you should only use Section A.” |
| [p526.pdf](p526.pdf) | 2025 returns, printed 2026-02-05 | pp. 23–25, “Limits on Deductions” | Cash to 50%-limit organizations: 60% of AGI. Noncash to 50%-limit organizations: 50% of AGI limit. Capital gain property: 30% limits (with an election to use the 50% limit); contributions to non-50%-limit organizations / “for the use of”: 20% limit. Contributions subject to multiple limits are applied in a stated order; excess may be carried forward. |
| [p526.pdf](p526.pdf) | 2025 returns, printed 2026-02-05 | p. 28, “Carryovers” | “You can carry over any contributions you can't deduct in the current year because they exceed the limits based on your AGI. Except for qualified conservation contributions, you may be able to deduct the excess in each of the next 5 years until it is used up…” |

Interpretation: Section A is the encoding target and covers the in-scope
cases (cash gifts; noncash items under the appraisal thresholds; publicly
traded securities). The refusal triggers named in spec section 2.2 are the
income-limited and carried-over contributions (the 60/50/30/20 machinery), i.e.
any contribution whose deductible amount is reduced by a limit, and any
carryover from prior years. Detection must use the deduction amount **before**
income limits when testing the Section A/B thresholds, per the instruction
quoted above.

## P13 — Form 8960 deductions and prior-year state tax refunds

**Finding: confirmed. The premise's scope question resolves to a refusal
requirement, recorded here for Stage 1 encoding.**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i8960.pdf](i8960.pdf) | TY2025, printed 2026-02-04 | pp. 17–18, “Line 9a—Investment Interest Expense,” “Line 9b—State, Local, and Foreign Income Tax” | Individuals enter on line 9a “interest expense you paid or accrued during the tax year deducted on Schedule A (Form 1040), line 9.” Line 9b includes state, local, and foreign income taxes attributable to NII, plus real and personal property taxes attributable to NII, allocated by any reasonable method (with a worked allocation example in the instructions). Line 9c takes allowed miscellaneous investment expenses. |
| [i8960.pdf](i8960.pdf) | TY2025, printed 2026-02-04 | p. 18, caution box | “DO NOT use the Lines 9 and 10—Itemized Deduction Limitations on Deductions Properly Allocable to Investment Income Worksheet to calculate limitations for tax year 2025. Limitations under sections 67 and 68 are suspended in tax year 2025.” |
| [i8960.pdf](i8960.pdf) | TY2025, printed 2026-02-04 | pp. 14–15, “Deduction recoveries” and “Line 7—Deduction Recoveries Worksheet” | “A recovery or refund of a previously deducted item increases NII in the year of the recovery,” with stated exceptions (items already included in NII; pre-2013 deductions; and the worksheet's carve-out where the deduction year predates NIIT applicability). The worksheet computes the amount to include on line 7. |
| [i1040gi.pdf](i1040gi.pdf) | TY2025, printed 2026-02-25 | p. 90, “State and Local Income Tax Refund Worksheet—Schedule 1, Line 1” | A taxable refund of state or local income taxes deducted in a prior year is reported through Schedule 1, line 1, with a dedicated worksheet; p. 88 states the exceptions (“None of your refund is taxable if, in the year you paid the tax, you either (a) didn't itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes”). |

Interpretation: itemized deductions enter Form 8960 through Part II —
investment interest (9a, from Schedule A line 9, itself fed by Form 4952) and
allocable state/local taxes (9b) — and a prior-year state tax refund from an
itemized year would touch **two** places: Schedule 1, line 1 as income and Form
8960 line 7 (deduction recoveries) when NII-relevant. Spec section 2.2
refuses Schedule 1 income; the tool
must therefore detect this situation and refuse with citations to both
provisions rather than silently omitting either effect. Also note the printed
2025 instruction that the sections 67/68 limitation worksheets are not to be
used for tax year 2025.

## P14 — TY2026 changes to itemized deductions (research-reported)

**Finding: confirmed; both reported changes appear in the published 2026
edition, and the research pass's “35% cap” phrasing is reconciled with the
printed mechanics below. This premise is evidence-gathering only; encoding
TY2026 remains a later reviewed diff (spec sections 2 and 7).**

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [p505-2026.pdf](p505-2026.pdf) | Publication 505 (2026), “For use in 2026,” printed 2026-03-31 | p. 2, “What's New for 2026” | “Limit on itemized deductions. For 2026, your overall itemized deductions may be reduced. If your taxable income is more than the following amounts, your itemized deductions will be reduced by 5.4% of the lesser of (1) your total itemized deductions or (2) the amount your taxable income is more than the following amounts. • $768,700 if Married filing jointly or Qualifying surviving spouse, • $640,600 if Head of household or Single, or • $384,350 if Married filing separately. The limitation will be applied after any other…” |
| [p505-2026.pdf](p505-2026.pdf) | same | pp. 36–37, Worksheets 2‑5 and 2‑6 | Worksheet 2‑5 (charitable floor): “Caution: For 2026, if you plan to take an itemized deduction for a charitable contribution, you can only deduct charitable contributions that are more than 0.5% of your AGI.” Steps: total contributions (cash + other), minus 0.5% of AGI. Worksheet 2‑6 (overall limitation): subtract the filing-status threshold from taxable income; multiply the lesser of the total itemized deductions or the excess by 5.4% (0.054); subtract to get total itemized deductions. |

Interpretation: the research pass reported “a 0.5%-of-AGI charitable floor and a
35% cap on the value of itemized deductions” (`research/03_source_material.md`,
item 2, marked secondary/medium). The published 2026 mechanics are: the 0.5%
charitable floor (confirmed as reported), and an overall reduction of 5.4% of
the lesser of total itemized deductions or the threshold excess — 5.4% is the
printed approximation of 2/37 (arithmetic: 2/37 ≈ 5.405%); a 2/37 reduction on a
deduction taken at the 37% top rate leaves 35 cents per dollar, which is the
“35% cap on value” in substance. Both changes are confirmed as published; the
description in the research file should be read through this operational
detail when the TY2026 diff is prepared. `p505-2026` is archived as evidence
only (“not a TY2025 computational source”, per the catalog entry).

## Snapshot identifiers for P09

- `f8995.pdf`: SHA-256 `55380ad230303e1586ce97f0f224265b8337ad18c9204f0fb7325e95a76b5cde`.
- `f8995a.pdf`: SHA-256 `3362db81b8ef60cfaa93354858c6c92bac16e63984be0805c6479d272a6ec9aa`.
- `i8995.pdf`: SHA-256 `875843baead68f6fa9aa7c3f6f27d6c1f37cb971ac334bcf414acdb4c1487684`.
- `i8995a.pdf`: SHA-256 `6df1301c1ce74ef391219094831accd22cfeac26ce510f4499c4834484f55d97`.
- `i8995-correction.html`: SHA-256 in `manifest.json` (id `i8995-correction`).

All other snapshots cited above are identified by id in `manifest.json`, which
records the SHA-256 for both the archived file and its extracted text.

---

Stage 0 is complete: every premise is confirmed or corrected in writing above.
Per `HANDOFF.md`, Stage 1 does not begin until the owner has reviewed this file.
