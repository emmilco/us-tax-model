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

## Stage 15 premise maps — other credits (Forms 8880, 2441 and 5695)

Status: **owner decisions taken 2026-10-21** (T-048). The three maps below were
written by research agents (Claude Code) from the archived snapshots and are
kept as written, except that their headings are moved down two levels. They
are testimony for the Stage 15 authoring, not verified encodings: each claim
carries a locator, and each line is checked again against its cited text when
it is encoded.

What was checked before the owner's decisions: every quoted passage in the
three maps was searched for in the archived text (whitespace and line-break
hyphens normalised); the passages not found there were proposed interview
wording, project YAML or the same text in a different archived document. Also
checked by hand: both rate tables (f8880 line 9, f2441 line 8), the f8880
eligibility and line 4 text, the i2441 against p503 deemed-income difference,
the i5695 residence tests, the Credit Limit Worksheet lines, and the project
lines the maps rely on.

Corrections to the maps:

- Pub. 501 is archived (`p501`); its age rule ("considered to reach age 65 on
  the day before the person's 65th birthday", with the January 1 examples)
  bears on the f2441 map's Q8.
- Part II Section B of Form 5695 is not limited to the main home (i5695 p. 3,
  "a home that you used during 2025"; f5695 line 21a). Section A and home
  energy audits are.
- `choose` branches must be money in the checker (`engine/src/check.ts`), so a
  guarded `choose` cannot return the line 9 or line 8 rate as the maps propose.
- Fact Sheets 2025-01 and 2025-05 are now archived (`fs-2025-01`,
  `fs-2025-05`); Pub. 907 and Pub. 590-A are not.

Owner decisions (the recommended answers, accepted):

1. The IRA deduction stays roadmap item 2; traditional IRA contributions are
   refused on Form 8880.
2. Form 8880 lines 1 and 2 count Roth IRA contributions, W-2 box 12 codes D,
   E, F, S, AA, BB and EE, code G with a governmental-plan and elective-share
   question, voluntary after-tax contributions and `person.simple_deferral`;
   refused: ABLE, deferrals over the limit, year-designated (USERRA) box 12
   entries, code H. The self-employed SEP contribution is not counted
   (ambiguity register).
3. Line 4: the 2025 part from the Forms 1099-R (gross less rollovers), with
   per-entry exclusions for military plans, section 404(k) dividends and
   inherited IRAs of a nonspouse beneficiary; one per-person input for 2023,
   2024 and 2026 before the due date, split by joint and non-joint years.
4. Readings: an ineligible spouse zeroes only their column; "is claimed" is a
   new per-person question; line 4 is gross less rollovers; a 2026
   distribution is from a joint year when the 2025 return is joint; inherited
   401(k) and 403(b) distributions count.
5. Form 2441 refuses MFS, own sole proprietorship or partnership benefits and
   combat pay (inherited), line 9b, deemed income and a disabled spouse as
   qualifying person, a qualifying person who is not a dependent, a spouse who
   died in 2025 and a qualifying person with no TIN; computes household
   employee providers, providers without a TIN (with a notice), lines 13 and
   14, more than three providers, a child who turned 13 and a dependent over
   12 incapable of self-care.
6. Box 10 in box 1 asked per W-2; incapable of self-care a new input; line 1e
   assigned to the spouse whose W-2s show box 10 (refused when both do, line
   1e is above zero and a credit remains); one plan-maximum input (refused when
   plans differ); line 30 as total expenses less line 28; ineligible providers
   per p503; rate .35 for AGI of zero or less.
7. Form 5695 refuses business use (less than 80% nonbusiness), joint occupancy
   with non-spouses, spouses with separate main homes, fuel cells, line 17e
   Yes, Part I for a home first used after 2025, and an item without a valid
   QMID; computes the 2024 carryforward, condo and co-op shares and costs net
   of subsidies; 17a to 17c No zeroes Section A only; the form's $600 caps by
   category; a battery on a second home allowed as lines 1 to 4.
8. The rate tables: see T-048 (the owner's choice of encoding).


### Form 8880 (2025): premises for encoding

Read-only research. Sources are the archived texts in `sources/2025/`. Page N means the N-th form-feed chunk of `<id>.cols.txt`. f8880 has 2 pages: p. 1 is the form (classified `table`) and p. 2 holds the instructions (`prose`, 2 columns). The form's revision line reads "Form 8880 (2025) Created 11/4/25" (f8880 p. 1).
Locator style follows PROJECT_INDEX: `doc p. N, heading, "quote"`.

#### 0. How the project encodes forms (relevant facts)

- Each line is one atom application with a citation (spec 4.2, 4.3). There are no functions or loops. Money is integer cents, and rates are integer pairs (spec 4.1).
- Collections: `person` has one entry per person, with `person.role` ∈ {taxpayer, spouse} (forms/2025/person.yaml). `w2` is keyed by employer within a person (forms/2025/w2.yaml `collection.parent: person`). `retirement` (one entry per Form 1099-R) is **return-level with no parent and no owner field** (forms/2025/retirement.yaml, `collection:` with no `parent`).
- Entry lines may read return-level lines. For example, f8889 (parent person) reads `f1040.status` and `household.*`. A line may read lines of its enclosing entry but cannot reach into another entry (spec 4.4). A person's column therefore cannot read the *other* spouse's line directly. It has to go through a return-level `sum_over person` (with a filter).
- W-2 currently models boxes 1–7 only. **Box 12 is not modelled** (w2.yaml).
- `scope.credits` currently refuses every credit except the FTC without Form 1116, the excess social security credit, the 8812 credits and the EIC (forms/2025/scope.yaml). Its refusal text names "Schedule 3 lines 2 to 4". `s3.line8` = s3.line1 + zero (forms/2025/s3.yaml).
- `s8812` Credit Limit Worksheet A line 2 currently copies only `s3.line1` and is guarded by `scope.credits` (forms/2025/s8812.yaml lines 245–258). **It must change once Schedule 3 line 4 exists** (see §3).
- `scope.schedule1` refuses "an IRA deduction" and "other qualified retirement plans for the self-employed (such as a solo 401(k) ...)" (scope.yaml). It also refuses all other Schedule 1 adjustments, which includes line 24f (501(c)(18)(D) contributions).
- Existing reusable lines: `f1040.line11a` (AGI; `f1040.line11b` copies it), `f1040.line18`, `f1040.status`, `s3.line1` (= ftc.credit), `sa.dependent` ("Can someone claim you or your spouse as a dependent ... or are you a dual-status alien?", return-level), `sli.claimed` (return-level "Are you, or your spouse ... claimed as a dependent"), `sa.excluded_income` (the Form 2555/4563/Puerto Rico gate used by s8812 lines 2a–2c), `person.simple_deferral` (self-employed person's own SIMPLE salary reduction contributions), `person.sep_contrib`, and the retirement lines `retirement.box1`, `.rolled`, `.code`, `.account`, `.is_ira`, `.direct`, `.special`, `.bad_code`.
- Params: status-keyed dollar params use `value: {single, mfs, mfj, qss, hoh}`. Rates use `type: Rate, value: {num, den}` (params/2025.yaml, e.g. `qdcg.rate_15`).

#### 1. Line by line

Column (a) is you and column (b) your spouse. f8880 p. 2, Column (b): "Complete column (b) only if you’re filing a joint return."
Natural encoding: lines 1–6 are per-person lines on `person` (or a new person-bound definition such as `se`). Lines 7–12 are return-level, with line 7 = `sum_over person line6`.

**Pre-form caution.** f8880 p. 1, Caution, "You cannot take this credit if either of the following applies." Bullet 1 is the AGI cap. Bullet 2 is "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student (see instructions)." See §2.

| Line | Text (f8880 p. 1) | Computes / asks | Existing supply | New inputs |
|---|---|---|---|---|
| 1 (a),(b) | "Traditional and Roth IRA contributions, and ABLE account contributions by the designated beneficiary for 2025. Do not include rollover contributions" | Per person: IRA contributions for 2025 (traditional + Roth) + own ABLE contributions | None. The traditional IRA deduction is refused by `scope.schedule1`. Nondeductible traditional contributions go on Form 8606, which the project does not prepare. | Per person: Roth IRA contributions for 2025. Traditional contributions are a refusal (§4). ABLE is a refusal or an input (§4). |
| 2 (a),(b) | "Elective deferrals to a 401(k) or other qualified employer plan, voluntary employee contributions, and 501(c)(18)(D) plan contributions for 2025 (see instructions)" | Per person: elective deferrals incl. designated Roth + voluntary after-tax employee contributions + 501(c)(18)(D) | `person.simple_deferral` (self-employed SIMPLE salary reductions; see open question Q6). Nothing from W-2 yet. | Per W-2: box 12 amounts for codes D, E, F, S, AA, BB, EE (and G with a governmental/elective qualifier, see §4). Per person: voluntary after-tax employee contributions (not in box 12, see below). |
| 3 | "Add lines 1 and 2" | sum | n/a | n/a |
| 4 (a),(b) | "Certain distributions received after 2022 and before the due date (including extensions) of your 2025 tax return (see instructions). If married filing jointly, include both spouses’ amounts in both columns. See instructions for an exception" | Testing-period distributions, see §2.3 | 2025 Forms 1099-R: `retirement.box1` less `retirement.rolled` (direct rollover code G counts as fully rolled), summed at return level. The return-level collection is correct here: on MFJ, all 2025 amounts go in both columns, and on other statuses there is only one person. | Per person: qualifying distributions received in 2023, 2024 and 2026 before the due date. Per 1099-R entry: military retirement plan? section 404(k) ESOP dividend? inherited IRA as nonspouse beneficiary? Household: joint return filed for 2023? for 2024? ABLE distributions (Form 1099-QA, not modelled). |
| 5 | "Subtract line 4 from line 3. If zero or less, enter -0-" | `subtract_floor0` per person | n/a | n/a |
| 6 | "In each column, enter the smaller of line 5 or $2,000" | `smaller_of(line5, param savers.cap)` per person | n/a | n/a |
| 7 | "Add the amounts on line 6. If zero, stop; you can’t take this credit" | `sum_over person line6`. The stop gives credit 0. | n/a | n/a |
| 8 | "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11a*" | copy | `f1040.line11a` | Footnote: "* See Pub. 590-A ... for the amount to enter if you claim any exclusion or deduction for foreign earned income, foreign housing, income from Puerto Rico, or income from American Samoa." Gate on the existing `sa.excluded_income` (refuse). |
| 9 | "Enter the applicable decimal amount from the table below." | Rate 0.5 / 0.2 / 0.1 / 0.0 by (line 8, filing status) | `f1040.status` | none. Encode as `choose` over `test lte line8 param(band)` per status (§5). Note: "If line 9 is zero, stop; you can’t take this credit." |
| 10 | "Multiply line 7 by line 9" | `multiply_rate` | n/a | n/a |
| 11 | "Limitation based on tax liability. Enter the amount from the Credit Limit Worksheet in the instructions" | CLW line 3, see §3 | `f1040.line18`, `s3.line1` (+ s3.line2 once Form 2441 lands) | none |
| 12 | "Credit for qualified retirement savings contributions. Enter the smaller of line 10 or line 11 here and on Schedule 3 (Form 1040), line 4" | `smaller_of` → new `s3.line4`, added into `s3.line8` | `s3.line8` sum | n/a |

Supporting instruction text:
- Line 2: f8880 p. 2, Line 2, "Include on line 2 any of the following amounts. • Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP. • Voluntary employee contributions to a qualified retirement plan, as defined in section 4974(c) (including the federal TSP). • Contributions to a 501(c)(18)(D) plan." Also "These amounts may be shown in box 12 of your Form(s) W-2 for 2025."
- Line 2 exclusion: f8880 p. 2, Line 2, "Contributions designated under section 414(h)(2) are treated as employer contributions ... They don’t qualify for the credit and shouldn’t be included on line 2." Corroboration: iw2w3 p. 19, Box 12—Codes, "Do not report in box 12 section 414(h)(2) contributions ... Instead, use box 14". Box 12 alone therefore already excludes them, and the point only matters for the voluntary-contribution input.
- W-2 box 12 codes, iw2w3 p. 20 (Box 12—Codes):
  - "Code D—Elective deferrals under a section 401(k) cash or deferred arrangement (plan). Also show deferrals under a SIMPLE retirement account that is part of a section 401(k) arrangement."
  - "Code E—Elective deferrals under a section 403(b) salary reduction agreement."
  - "Code F—Elective deferrals under a section 408(k) (6) salary reduction SEP (this includes elective deferrals made to a Roth SEP IRA)."
  - "Code G—Elective deferrals and employer contributions (including nonelective deferrals) to any governmental or nongovernmental section 457(b) deferred compensation plan."
  - "Code H—Elective deferrals under section 501(c) (18)(D) tax-exempt organization plan. ... The employee will deduct the amount on their Form 1040 or 1040-SR."
- iw2w3 p. 21:
  - "Code S—Employee salary reduction contributions under a section 408(p) SIMPLE plan (this includes salary reduction contributions made to a Roth SIMPLE IRA)."
  - "Code AA—Designated Roth contributions under a section 401(k) plan."
  - "Code BB—Designated Roth contributions under a section 403(b) plan."
  - "Code EE—Designated Roth contributions under a governmental section 457(b) plan." The text continues on p. 22.
- Voluntary after-tax contributions are not in box 12. iw2w3 p. 20, Box 12—Codes: "The following are not elective deferrals and may be reported in box 14, but not in box 12. ... • After-tax contributions that are not designated Roth contributions, such as voluntary contributions to a pension plan that are deducted from an employee's pay." The Alex example says "The $600 voluntary after-tax contribution may be reported in box 14 (this is optional) but not in box 12."
- Box 12 can carry prior-year USERRA make-up amounts and amounts over the limit:
  - iw2w3 p. 20: "make-up amounts under the Uniformed Services Employment and Reemployment Rights Act of 1994 (USERRA) for a prior year, you must enter the prior-year contributions separately ... D 23 2250.00, D 24 1250.00."
  - Alex example: "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D".
  - Line 2 counts contributions "for 2025" (f8880 p. 1, line 2), so year-designated USERRA entries must be excluded.
- Line 7: f8880 p. 2, Line 7, "Add the amounts from line 6, columns (a) and (b), and enter the total."
- Maximum: f8880 p. 2, Purpose of Form, "The maximum amount of the credit is $1,000 ($2,000 if married filing jointly)." This is consistent with 2 × $2,000 × 0.5 on MFJ and $2,000 × 0.5 otherwise. It is a useful property check, not a param.
- Schedule 3: f1040s3 p. 1, line 4, "Retirement savings contributions credit. Attach Form 8880". Line 8 says "Add lines 1 through 4, 5a, 5b, and 7".

#### 2. Eligibility, contributions counted, testing period, AGI table

##### 2.1 Who qualifies (per person who made the contribution)
- f8880 p. 1 Caution and p. 2, Who Can Take This Credit: "(a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student." Same wording in i1040gi p. 116 (continuing Schedule 3 Line 4 from p. 115), "2. The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008, (b) is claimed as a dependent on someone else’s 2025 tax return, or (c) was a student (defined next)."
  - Age: a person born on or before January 1, 2008 passes. Proposed input: "Were you born before January 2, 2008?", matching the `person.born_before_2001` pattern.
  - Dependent: the text says "**is** claimed". The existing `sa.dependent` asks "**Can** someone claim you **or your spouse**". That is broader, return-level, and also includes dual-status aliens. It cannot stand in directly. A new per-person input is needed, or a refusal when `sa.dependent` is true (§4).
  - Student: f8880 p. 2, Who Can Take This Credit, "You were a student if during any part of 5 calendar months of 2025 you: • Were enrolled as a full-time student at a school; or • Took a full-time, on-farm training course given by a school or a state, county, or local government agency. A school includes technical, trade, and mechanical schools. It doesn’t include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet." Same text in i1040gi p. 116. New per-person input. `dependent.yaml`'s student question belongs to the dependent collection and is not reusable.
- Filing status: column (b) only on a joint return (f8880 p. 2, Column (b)). MFS is already refused project-wide (`s3.mfs` in `scope.ready`).

##### 2.2 Contributions that count
- f8880 p. 2, Who Can Take This Credit: "(a) contributions (other than rollover contributions) to a traditional or Roth IRA; (b) elective deferrals to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal Thrift Savings Plan (TSP); (c) voluntary employee contributions to a qualified retirement plan, as defined in section 4974(c) (including the federal TSP); (d) contributions to a 501(c)(18)(D) plan; or (e) contributions, as a designated beneficiary of an ABLE account, to the ABLE account, as defined in section 529A."
- i1040gi p. 115, Line 4 Retirement Savings Contributions Credit (Saver’s Credit), gives the same list and adds "(including designated Roth contributions)".
- IRA contributions "for 2025" may be made in 2026. i1040gi p. 62, IRA (refund by direct deposit): "If the deposit isn’t made by that date, the deposit isn’t an IRA contribution for 2025. In that case, you must file an amended 2025 return and reduce any IRA deduction and any retirement savings contributions credit you claimed."
- IRA limit: same page, "each may be able to contribute up to $7,000 ($8,000 if age 50 or older at the end of 2025) to a traditional IRA or Roth IRA for 2025."
- Roth is not deductible but counts. i1040gi p. 95, Line 20 IRA Deduction, item 1: "You can’t deduct contributions to a Roth IRA. But you may be able to take the retirement savings contributions credit (saver’s credit). See the instructions for Schedule 3, line 4."
- Nondeductible traditional contributions go on Form 8606: i1040gi p. 95, Line 20 IRA Deduction, "If you made any nondeductible contributions to a traditional ... (IRA) for 2025, you must report them on Form 8606."
- ABLE is permanent for 2025: f8880 p. 2, What’s New, "makes permanent the credit for contributions by a designated beneficiary to their ABLE account. See Pub. 907". **Pub. 907 is not archived.**

##### 2.3 Testing period and line 4
- f8880 p. 2, Line 4: "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions) from any of the following types of plans. • Traditional or Roth IRAs, or ABLE accounts. • 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP, SIMPLE, or the federal TSP. • Qualified retirement plans, as defined in section 4974(c)."
- Excluded (same heading, "Don’t include any of the following."):
  1. "Distributions not taxable as the result of a rollover or a trustee-to- trustee transfer." Use `retirement.rolled`; code G is wholly rolled.
  2. "Distributions that are taxable as the result of an in-plan rollover to your designated Roth account ..." Already refused: `retirement.special`, "a rollover to a Roth IRA or designated Roth account".
  3. "Distributions from your eligible retirement plan (other than a Roth IRA) rolled over or converted to your Roth IRA ..." Already refused: `retirement.special`, conversion / Roth rollover.
  4. "Loans from a qualified employer plan treated as a distribution." Code L becomes code `other`, which is refused (`retirement.bad_code`). A plan loan offset is in `retirement.special`.
  5. "Distributions of excess contributions or deferrals (and income allocable to such contributions or deferrals)." Already refused: `retirement.special`, "a corrective distribution of excess deferrals or contributions".
  6. "Distributions of contributions made to an IRA during a tax year and returned ... on or before the due date". Already refused: `retirement.special`, "a 2024 or 2025 IRA contribution returned to you".
  7. "Distributions of dividends paid on stock held by an employee stock ownership plan under section 404(k)." **Not detectable from current inputs.** i1099r p. 2 (Section 404(k) dividends) says they are on a separate Form 1099-R. A new per-entry question is needed.
  8. "Distributions from a military retirement plan (other than the federal TSP)." **Not detectable.** i1099r p. 2, Military retirement annuities: "Use Code 7 in box 7 for reporting military pensions". A new per-entry question is needed.
  9. "Distributions from an inherited IRA by a nonspousal beneficiary." **Not detectable.** Code 4 (i1099r p. 18, "4—Death") and code Q do not identify the beneficiary's relationship. A new per-entry question is needed for IRA entries.
- Both columns, and the exception. f8880 p. 2, Line 4: "If you’re filing a joint return, include both spouses’ amounts in both columns. Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received." The worked example: "You received a distribution of $5,000 from a qualified retirement plan in 2025. Your spouse received a distribution of $2,000 from a Roth IRA in 2023. You and your spouse file a joint return in 2025, but didn’t file a joint return in 2023. You would include $5,000 in column (a) and $7,000 in column (b)." Use this as an official-example fixture.
- Amount measure: the text says "total amount of distributions", not the taxable amount. Proposed per entry: `box1 − rolled` (not `retirement.taxable`). A qualified Roth distribution (code Q), which is nontaxable, counts in full. See Q3.
- Encoding sketch: column(p) line 4 = R2025 + Σ_{q∈persons} J(q) + S(p).
  - R2025 is the return-level `sum_over retirement` of qualifying 2025 amounts.
  - J(q) is q's prior and post-2025 window amounts from years the couple filed jointly.
  - S(p) is p's own amounts from years they did not file jointly.
  - On a non-joint return there is one person, so this reduces to R2025 + S.

##### 2.4 AGI table (line 9)
f8880 p. 1, line 9 table ("IF line 8 is... Over... But not over... THEN enter on line 9..."), columns MFJ / HOH / "Single, Married filing separately, or Qualifying surviving spouse":

| Over | But not over | MFJ | HOH | Single/MFS/QSS |
|---|---|---|---|---|
| --- | $23,750 | 0.5 | 0.5 | 0.5 |
| $23,750 | $25,500 | 0.5 | 0.5 | 0.2 |
| $25,500 | $35,625 | 0.5 | 0.5 | 0.1 |
| $35,625 | $38,250 | 0.5 | 0.2 | 0.1 |
| $38,250 | $39,500 | 0.5 | 0.1 | 0.1 |
| $39,500 | $47,500 | 0.5 | 0.1 | 0.0 |
| $47,500 | $51,000 | 0.2 | 0.1 | 0.0 |
| $51,000 | $59,250 | 0.1 | 0.1 | 0.0 |
| $59,250 | $79,000 | 0.1 | 0.0 | 0.0 |
| $79,000 | --- | 0.0 | 0.0 | 0.0 |

Reduced to three cut points per status (the rate applies while line 8 is not over the cut point):

| Status | 0.5 up to | 0.2 up to | 0.1 up to |
|---|---|---|---|
| Single / MFS / QSS | 23,750 | 25,500 | 39,500 |
| HOH | 35,625 | 38,250 | 59,250 |
| MFJ | 47,500 | 51,000 | 79,000 |

This matches the caution caps: "more than $39,500 ($59,250 if head of household; $79,000 if married filing jointly)" (f8880 p. 1, Caution; i1040gi p. 116).
Boundary: "Over ... But not over" means the band is inclusive at its top, so line 8 = $23,750 gets 0.5. Negative AGI falls in the first row.

#### 3. Credit limit and credit ordering

**Form 8880 Credit Limit Worksheet** (f8880 p. 2, Line 11):
- "Before you complete the following worksheet, figure the amount of any credit for the elderly or the disabled you’re claiming on Schedule 3 (Form 1040), line 6d."
- Line 1: "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 18".
- Line 2: "Enter the total of your credits from Schedule 3, lines 1 through 3, 6d, and 6l".
- Line 3: "Subtract line 2 from line 1. Also enter this amount on Form 8880, line 11. But if zero or less, stop; you can’t take the credit—don’t file this form."

So the amounts that reduce the available tax are:
- Sch 3 line 1 (FTC)
- line 2 (Form 2441)
- line 3 (education, Form 8863)
- line 6d (elderly/disabled, Sch R)
- line 6l (Form 8978 line 14 amount)

The child tax credit / ODC (Form 1040 line 19) and Form 5695 do **not** reduce it, so the saver's credit is taken ahead of them. In the current project, lines 3, 6d and 6l stay refused. CLW line 2 is therefore s3.line1 + s3.line2, with the others refused (T-048 keeps education, elderly and 8978 refused).

**Schedule 8812 Credit Limit Worksheet A** (i1040s8812 p. 4, Credit Limit Worksheet A):
- Line 1: "Enter the amount from line 18 of your Form 1040".
- Line 2: "Add the following amounts (if applicable) from: Schedule 3, line 1 ... line 2 ... line 3 ... line 4 ... line 5b ... line 6d ... line 6f ... line 6l ... line 6m".
- Line 4 is Credit Limit Worksheet B, which is completed only with Form 8396, 8839, 5695 Part I or 8859, no Form 2555, and 8812 line 4 > 0 (i1040s8812 p. 3, Line 13, "Complete Credit Limit Worksheet B only if you meet all of the following.").
- The saver's credit therefore reduces the CTC/ODC limit, and a larger saver's credit can shift CTC into the refundable ACTC.
- **The current `s8812` CLW A line 2 is `copy s3.line1` and must become sum(s3.line1, s3.line2, s3.line4, s3.line5b)** (plus the still-refused 3, 6d, 6f, 6l, 6m). This is the main cross-form edit.

**Form 2441** Credit Limit Worksheet (i2441 p. 5, Line 10):
- "2. Enter the amount from Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (Form 8978, line 14)". 2441 does not subtract line 4.
- Order: 2441 before 8880, and 8880 reads s3.line2.

**Form 5695:**
- Energy Efficient Home Improvement Credit Limit Worksheet—Line 31 (i5695 p. 7) subtracts "line 6l ... line 1 ... line 2 ... line 6d ... line 3 ... Retirement Savings Contributions Credit, Schedule 3 (Form 1040), line 4". So 5b comes after 8880 and before CTC (8812 CLW A subtracts 5b).
- Residential Clean Energy Credit Limit Worksheet—Line 14 (i5695 p. 5) subtracts 6l, 1, 2, 6d, 3, **4**, Form 5695 line 32, 6m, 6f, "Child tax credit or credit for other dependents, Form 1040, 1040-SR, or 1040-NR, line 19*", 6g, 6c, 6h. The footnote "*" says to use CLW B line 14 instead when 8812 directs CLW B.
- RCE carries forward (i5695 p. 5, Line 16). 8880 has no carryforward: the archived text has none, and the CLW "stop; you can’t take the credit".

**Resulting dependency order (no cycle):**
line 18 → FTC (s3.1) → 2441 (s3.2) → 8880 (s3.4) → 5695 Part II (s3.5b) → 8812 CTC/ODC (line 19) → 5695 Part I (s3.5a).
8880 reads only line 18, s3.1 and s3.2 (and 3, 6d, 6l, which are refused). None of those read s3.4.

Line 8 versus 11a/11b: f8880 reads "line 11a", while i1040gi p. 116 reads "line 11b". The project's `f1040.line11b` copies `line11a`, so there is no practical difference. Cite the form.

#### 4. Refuse or compute

| # | Situation | Why it is hard | Recommendation |
|---|---|---|---|
| R1 | Traditional IRA contributions (deductible) | Requires the Schedule 1 line 20 IRA deduction, already refused by `scope.schedule1` | Refuse (inherited from the scope screen). Note: coverage estimator `tools/coverage/categories.json` "savers" says "in the microdata every saver's credit comes with a traditional IRA deduction", so coverage gain without the IRA deduction will be small. Flag this to the owner. |
| R2 | Nondeductible traditional IRA contributions | Form 8606 required (i1040gi p. 95); not prepared | Refuse |
| R3 | Roth IRA contributions | Plain input. The limit is $7,000/$8,000 (i1040gi p. 62). Roth eligibility under compensation/MAGI rules lives in Pub. 590-A (not archived). | Compute (input "Roth IRA contributions for 2025, made by the due date, not counting rollovers or conversions"). Refuse any excess contribution (Form 5329) and recharacterizations via a screen. |
| R4 | ABLE contributions by the designated beneficiary, and ABLE distributions in the testing period | Pub. 907 not archived. ABLE distributions are on Form 1099-QA, which is not modelled. Line 4 needs them even for people with no ABLE contribution. | Refuse in the first build, via a screen asking "any ABLE contributions or distributions in the testing period". Alternative: archive p907 and take both as plain per-person inputs. Owner decision. |
| R5 | W-2 code G | Covers non-governmental 457(b) and employer/nonelective amounts; 8880 counts governmental 457(b) elective deferrals only | Compute with a per-W-2 qualifier ("Is this a governmental 457(b) plan? Enter only your own elective deferrals"). Simpler alternative: refuse code G. |
| R6 | W-2 code H, 501(c)(18)(D) | Employee deducts it on Schedule 1 line 24f (f1040s1 p. 2, "24f Contributions to section 501(c)(18)(D) pension plans"), which is refused by `scope.schedule1` | Refuse (already caught) |
| R7 | Prior-year USERRA make-up amounts in box 12 (year-designated) | Not "for 2025" | Compute by an interview instruction to omit year-designated entries. Or refuse if any are present. |
| R8 | Excess deferrals (box 12 total over the $23,500 limit, iw2w3 p. 20 Alex example) | Whether the excess counts on line 2 is unaddressed (Q4). Their later distribution is excluded from line 4 and is already refused at the 1099-R. | Refuse when the person's 402(g) total is exceeded (screen). It is low-frequency, and line 6 caps at $2,000 anyway. |
| R9 | Voluntary after-tax employee contributions | Not on W-2 box 12 (box 14 optional) | Compute as a per-person input, excluding 414(h)(2) "pick-up" contributions (f8880 p. 2, Line 2 Note) |
| R10 | Self-employed SIMPLE salary reductions | `person.simple_deferral` already exists | Compute (read it) |
| R11 | Self-employed SEP contribution (`person.sep_contrib`) | An employer nonelective contribution, not an elective deferral (only SARSEP deferrals, code F, are named) | Do not count. Record the reading in the ambiguity register (Q6). |
| R12 | Solo 401(k) / Keogh deferrals | Already refused by `scope.schedule1` | Refuse (already caught) |
| R13 | Distributions in 2023, 2024 and 2026 (before the due date) | Not in the 1099-R collection, which covers 2025 only | Compute from per-person inputs (net of the nine exclusions), plus household "filed jointly for 2023 / 2024?" flags for the exception. Alternative if the owner wants it smaller: refuse when the spouse had prior-period distributions in a year not filed jointly. |
| R14 | Spouse's distributions on a joint return | Rule is "both columns" | Compute. The return-level `retirement` sum already fits for 2025. Use the official example (f8880 p. 2) as a fixture. |
| R15 | 2025 1099-R from a military retirement plan, a 404(k) ESOP dividend, or an inherited IRA by a nonspouse beneficiary | Not distinguishable by `retirement.code` / `account` | Compute with per-entry Bool inputs that exclude the entry (asked only when the 8880 path is live, if the interview supports conditional questions). Or refuse via a screen. Recommendation: compute; the three questions are simple. |
| R16 | Rollovers, conversions, in-plan Roth rollovers, plan loans, corrective/excess and returned-contribution distributions | Already refused (`retirement.special`, `bad_code`) or excluded (`rolled`, code G) | Already handled. Rollover amounts are excluded via `retirement.rolled`. |
| R17 | Person claimed as a dependent on someone else's return | `sa.dependent` is "can claim", return-level, and includes dual-status | Compute with a per-person "is claimed" input. Conservative alternative: refuse 8880 when `sa.dependent` is true. |
| R18 | Foreign earned income/housing exclusion, Puerto Rico or American Samoa income (line 8 footnote → Pub. 590-A, not archived) | Modified AGI needed | Refuse via existing `sa.excluded_income` (same gate as s8812 lines 2a–2c) |
| R19 | Military differential pay | **No mention in the archived 8880 or i1040gi Schedule 3 line 4 text.** iw2w3 p. 12, Military differential pay, only says it is wages in box 1. Deferrals from it appear in box 12 like any other. | Not a refusal candidate for 8880 |
| R20 | Credit for the elderly (6d), education (3), Form 8978 (6l) | Enter the CLW, but those forms are not built | Refuse (stays under the narrowed `scope.credits`) |
| R21 | Testing-period distributions after the date of preparation (Jan to Oct 15, 2026) | Filer may not know yet. The i1040gi p. 62 analogue says to amend if facts change. | Compute from what the filer states, with interview help saying later distributions require amending. No citation for amending in 8880 itself (Q8). |

#### 5. Parameters for params/2025.yaml

Proposed values in cents. All locators are f8880 p. 1.

- `savers.cap`: NonNegDollars 200000. Locator: line 6, "In each column, enter the smaller of line 5 or $2,000".
- `savers.band50`: Dollars by status {single: 2375000, mfs: 2375000, qss: 2375000, hoh: 3562500, mfj: 4750000}. Locator: line 9 table, rows "--- $23,750", "$35,625 $38,250", "$47,500 $51,000".
- `savers.band20`: {single: 2550000, mfs: 2550000, qss: 2550000, hoh: 3825000, mfj: 5100000}. Locator: line 9 table.
- `savers.band10`: {single: 3950000, mfs: 3950000, qss: 3950000, hoh: 5925000, mfj: 7900000}. Locator: line 9 table, and Caution "more than $39,500 ($59,250 if head of household; $79,000 if married filing jointly)".
- `savers.rate_50`: Rate {num: 5, den: 10}. `savers.rate_20`: Rate {num: 2, den: 10}. `savers.rate_10`: Rate {num: 1, den: 10}. `savers.rate_0`: Rate {num: 0, den: 1}, or use the existing `sales.zero` path. Locator: line 9 table, "THEN enter on line 9...".

Not params, but useful for screens and help text:
- the $7,000/$8,000 IRA limit (i1040gi p. 62)
- the $23,500 deferral limit (iw2w3 p. 20, Alex example; a W-2 instruction, so testimony for a screen only)
- the birth-date cut "January 1, 2008"
- "after 2022" for the testing period

Caution: the band dollar amounts are printed only in the f8880 table. i1040gi p. 116 repeats only the three caps. A second printing exists for the caps, not for the inner bands.

#### 6. Open questions

- **Q1. Per-person or whole-credit ineligibility.** The caution says "You cannot take this credit if ... The person(s) who made the qualified contribution or elective deferral (a) was born after ...". It is undecided whether, on MFJ, one ineligible spouse (say a student) zeroes only that spouse's column or the whole credit. The wording ties ineligibility to "the person(s) who made the contribution", which suggests per column. The statute (26 USC 25B, "eligible individual") is not archived. Recommendation: per-column reading, recorded in the ambiguity register; consider archiving 26 USC 25B.
- **Q2. "Is claimed" or "can be claimed".** The 8880 text says "is claimed ... on someone else’s 2025 tax return". The project's existing gate asks "can". Decide whether to add a new per-person input or refuse (R17).
- **Q3. What line 4 measures.** It is undecided whether line 4 is the gross distribution (box 1 less rolled) or the taxable part. The text says "total amount of distributions" and excludes only listed kinds, so the gross reading is the natural one. Box 5 basis recovery and qualified Roth (Q) amounts would count. Recommendation: gross less the rolled-over amount; record it.
- **Q4. Excess deferrals on line 2.** It is undecided whether elective deferrals over the 402(g) limit (reported in box 12 per iw2w3 p. 20) count on line 2. The text is silent. Recommendation: refuse (R8).
- **Q5. Code G.** Should the interview ask for the elective share of a governmental 457(b) code G amount, or refuse code G outright?
- **Q6. Self-employed SEP and SIMPLE.** Only "elective deferrals to a ... SEP, SIMPLE" are named. Is a self-employed person's own SEP contribution (`person.sep_contrib`, an employer-type contribution) outside line 2? Is the SIMPLE salary reduction (`person.simple_deferral`) inside? The archived 8880 text does not settle it; Pub. 590-A and Pub. 560 might (p560 is archived but was not checked here).
- **Q7. The joint exception and 2026.** For distributions received in 2026 before the due date, "the year the distribution was received" is 2026, whose return is not yet filed. Does the spouse's 2026 distribution go in both columns? Recommendation: treat 2026 as joint when the 2025 return is joint, or ask the filer whether they expect to file jointly for 2026. Record either way.
- **Q8. Inherited plans.** The exclusion names only an "inherited IRA by a nonspousal beneficiary". Distributions from an inherited 401(k) or 403(b) to a nonspouse beneficiary appear to count, read literally. Confirm the literal reading.
- **Q9. ABLE.** Should Pub. 907 be archived and ABLE computed as inputs, or refused (R4)? This must also cover ABLE *distributions* in line 4, which apply to filers with only retirement contributions.
- **Q10. Interview for prior-year distributions.** Should the interview ask amounts by year (2023, 2024, 2026 window) per person with household joint flags (compute), or refuse the separate-year spouse case (smaller)?
- **Q11. Coverage value.** The categories.json note says the microdata pairs every saver's credit with a traditional IRA deduction. Should the IRA deduction (Schedule 1 line 20, i1040gi pp. 95–98 worksheet) join Stage 15 for the 8880 to matter? This is outside T-048 as written.
- **Q12. Line 9 encoding.** `table_lookup` bands a money key and returns money, while `keyed_lookup` takes enum or count keys only (spec 4.2). The line 9 rate therefore needs a `choose` over status-keyed band params plus three Rate params (no new atom). Alternatively, use `keyed_lookup` on status for the band edges plus `choose`. Confirm with the owner that a guarded `choose` is acceptable.

### Form 2441 (2025): premises for encoding

Read-only research for T-048 (Stage 15). Nothing in the repository was edited and no model was called.

#### Sources and locator convention

| id | document | revision (manifest) | pages |
|---|---|---|---|
| f2441 | Form 2441 (2025) | "Created 3/18/25" | form p. 1 (header, Parts I, II), p. 2 (Part III) |
| i2441 | Instructions for Form 2441 (2025) | Jul 22, 2025 | pp. 1-7 |
| p503 | Pub. 503 (2025) | Nov 18, 2025 | pp. 1-14 (15-21 are tax help and index) |
| i1040gi | Form 1040 instructions (2025) | | pp. 14, 20-21, 24, 44, 115 |
| iw2w3 | General Instructions for Forms W-2 and W-3 (2025) | | pp. 18-19, 24 |
| i1040s8812 | Schedule 8812 instructions (2025) | | p. 4 |
| f8880 | Form 8880 (2025) | "Created 11/4/25" | p. 2 (instructions printed on the form) |
| i5695 | Instructions for Form 5695 (2025) | | pp. 5, 7 |
| f1040s3 | Schedule 3 (2025) | | line 2 |

Page numbers are the printed page numbers. I checked that the N-th form-feed chunk of the `.cols.txt` file is printed page N for i1040gi (chunks 14, 24 and 115 end with those page numbers), i2441 and p503. Each quote below is short and verbatim from the `.cols.txt` or `.txt` text. Some items repeat or lead into others, so I removed list markers or line breaks in a few places.

The project's form model (spec 4.2 to 4.6 and 5) is described in the summary below, which was checked against `spec/spec.md`, `forms/2025/{person,dependent,w2,scope,s3,s8812,eic,f1040,sli}.yaml` and `engine/src/{check,eval}.ts`. It is relevant to items 1 to 3.

- Collections: `person` (role taxpayer or spouse), `dependent` (one entry per listed person) and `w2`. The `w2` collection sits inside `person`, keyed by employer. Its boxes are 1, 2, 3, 4, 5, 6 and 7. **Box 10 is not modelled.**
- `person.box1` is the sum of a person's W-2 box 1 amounts. `f1040.line1a` is the sum of `person.box1` over persons. `f1040.line1z` is currently a copy of `line1a`.
- Self-employment earned income per person is already computed as `person.eic_se`: Schedule SE line 3 less SE line 13 when the person files SE, and Schedule C net profit or loss otherwise.
- The dependent tests are per entry. The relevant lines are `dependent.age` (age at the end of 2025), `dependent.months`, `dependent.lived_half`, `dependent.qc_dependent`, `dependent.claimed`, `dependent.disabled` ("permanently and totally disabled"), `dependent.tin`, `dependent.gross_income` and `dependent.qr_income`.
- `dependent` already refuses several cases:
  - the divorced or separated parents rule (`dependent.divorced_rule`)
  - married dependents (`dependent.married`)
  - the gross income exception for a disabled person (`dependent.income_exception`)
- `table_lookup` takes only a money key and a filing-status column, and it returns **money** from bands of the form [at_least, less_than) (`engine/src/check.ts` table_lookup, `eval.ts` findBand). `keyed_lookup` keys only on enum or count values.
- Screens that touch this form:
  - `scope.credits` refuses Schedule 3 line 2.
  - `scope.other_income` refuses "dependent care or adoption benefits".
  - `s3.mfs` refuses married filing separately.
  - `s2` refuses household employment taxes.
  - `sc.special` refuses a sole proprietor's own dependent care assistance contributions (BUG-0070).
  - `s8812.combat_pay` asks about nontaxable combat pay.
  - `sa.excluded_income` asks about Form 2555 and Form 4563.

---

#### 1. Line by line

##### Header checkboxes

| Line | What it asks | Locator | Supply |
|---|---|---|---|
| A | Checkbox: a married-filing-separately filer meets the special requirements | f2441 p. 1, line A, "You can't claim a credit ... if your filing status is married filing separately unless you meet the requirements"; i2441 p. 2, Line A, "By checking the box, you are confirming that you meet the requirements" | Not reachable while `s3.mfs` refuses MFS |
| B | Checkbox: deemed income of $250 or $500 a month was entered on line 4, 5, 18 or 19 | f2441 p. 1, line B; i2441 p. 2, Line B, "you're entering deemed income of $250 or $500 a month on Form 2441, line 4, 5, 18, or 19" | A display Bool if deemed income is supported (section 4) |

##### Part I: care providers (line 1). Informational, with no arithmetic.

- **Columns:** (a) name, (b) address, (c) SSN or EIN, (d) household employee yes/no, (e) amount paid. f2441 p. 1, Part I, "You must complete this part."
- **Column (c):**
  - For an individual, the SSN or ITIN; otherwise the EIN.
  - "Tax-Exempt" for a tax-exempt organization.
  - "LAFCP" for a foreign care provider of a filer living abroad.
  - i2441 p. 3, Column (c).
- **Column (d):** "You must check either the "Yes" or "No" box" (i2441 p. 3, Column (d)). Example: "nannies are generally household employees, while daycare centers are not".
- **Column (e):** "Enter the total amount you actually paid in 2025 to the care provider. Also, include amounts your employer paid to a third party on your behalf. It doesn't matter when the expenses were incurred. Don't reduce this amount by any reimbursement you received." (i2441 p. 3, Column (e))
  - Column (e) feeds no other line. The credit runs from line 2(d), and the exclusion from lines 12 and 16.
- **Employer-furnished care:** enter the employer's name and "See W-2", leave column (c) blank, check "No" and enter -0- in column (e). i2441 p. 3, Columns (a) and (b).
- **More than three providers:** check the box and attach a statement; i2441 pp. 2-3, Line 1. Spec 4.4 says pagination is not modelled.
- **No providers and no qualifying person, filing only for Part III:** enter "none" in line 1 column (a). i2441 p. 3, "enter "none" on line 1, column (a)"; p503 p. 9.
- **Fork after line 1:** "Did you receive dependent care benefits? No: Complete only Part II below. Yes: Complete Part III on page 2 next." (f2441 p. 1, under line 1)
- **New input:** a `care_provider` collection at return level (name, address, TIN or tag, household employee Bool, amount paid). It also needs the provider-eligibility facts in section 2.4.

##### Part II: credit

**Line 2, qualifying persons.** Columns: (a) name, (b) SSN, (c) over age 12 and disabled, (d) "Qualified expenses you incurred and paid in 2025 for the person listed in column (a)" (f2441 p. 1, line 2).
- **Column (b):** "You must enter the qualifying person's SSN". A child born and died in 2025 with no SSN is entered as "Died" with records attached (i2441 p. 3, Column (b)). An ITIN or ATIN is allowed (p503 p. 3, Taxpayer identification number). Supply: `dependent.tin`.
- **Column (c):** "Check the box ... if the qualifying person ... was over age 12 at the time the care was provided and was disabled". Don't enter your spouse unless they were incapable of self-care (i2441 p. 3, Column (c)).
- **Column (d) excludes:**
  - 2024 expenses paid in 2025 (these go on line 9b)
  - 2025 expenses paid in 2026
  - 2025 prepayments for 2026 care
  - "If you completed Part III, don't include in column (d) any benefits shown on line 28."
  - Locator: i2441 pp. 3-4, Column (d).
- **Prepaid care:** "If you pay for services before they are provided, you can count the prepaid expenses only in the year the care is received." p503 p. 10, Expenses prepaid in an earlier year.
- **Reimbursed expenses:** Expenses reimbursed under an employer program or by a state social services agency are not counted. p503 p. 10, Expenses reimbursed; i2441 p. 2.
- **Supply:** the dependent collection gives identity and TIN. New inputs per qualifying person:
  - incapable of self-care (Bool)
  - under 13 for some part of 2025 when care was provided (or a birth date)
  - qualified expenses incurred and paid in 2025
  
  The spouse as a qualifying person needs a per-person input on the `person` entry.

**Line 3.** "Add the amounts in column (d) of line 2. Don't enter more than $3,000 if you had one qualifying person or $6,000 if you had two or more persons. If you completed Part III, enter the amount from line 31" (f2441 p. 1, line 3).
- Encoding: `choose`. With Part III completed, copy line 31. Otherwise, the smaller of the sum of column (d) and the limit param, keyed by the count of qualifying persons.
- The count includes qualifying persons with zero expenses: "you can use $6,000 ... list $6,000 for the 3-year-old child and -0- for the 11-year-old child" (i2441 p. 4; p503 p. 12, Dollar Limit, Tip).

**Line 4.** "Enter your earned income." (f2441 p. 1, line 4). The definition is at i2441 p. 4, Lines 4 and 5:
1. "The amount shown on Form 1040 ... line 1z, minus any amount" excluded on Form 2555 line 43, or reported on SE as clergy or church employee income of $108.28 or more.
2. "The amount shown on Schedule SE ... line 3, minus any deduction you claim on Schedule 1 ... line 15". The SE line 4b and 5a variants apply for the optional methods and church employee income.
3. A statutory employee's Schedule C line 1.
4. Elective nontaxable combat pay.

Also: "You must reduce your earned income by any loss from self-employment." p503 p. 11 adds: "Include your self-employment earnings in earned income, even if they are less than $400 and you didn't file Schedule SE".
- **Supply:** the person's share of line 1z, plus `person.eic_se`. `person.eic_se` already implements item 2 exactly: SE line 3 less SE line 13, or Schedule C profit when the person does not file SE (`person.eic_se_has`, cited to i1040gi p. 47).
  - The per-person share of 1z is `person.box1` plus the person's share of line 1e. See open question Q2.
  - Items 1a/1b, 3 and 4 are already refused elsewhere: `sa.excluded_income`, `scope.schedule1` (clergy, church employee, statutory employee), and `s8812.combat_pay` (combat pay, as for the EIC).
- **Excluded from earned income:** pensions, social security, unemployment, interest, dividends, child support and similar items (p503 p. 4, "What isn't earned income?").

**Line 5.** "If married filing jointly, enter your spouse's earned income (if you or your spouse was a student or was disabled, see the instructions); all others, enter the amount from line 4" (f2441 p. 1, line 5). Supply: the spouse `person` entry under `mfj`; otherwise copy line 4. Deemed income: section 2.3.

**Line 6.** "Enter the smallest of line 3, 4, or 5. If zero or less, enter -0-" (f2441 p. 1, line 6). The project's `smaller_of` takes two operands, so this needs two `smaller_of` lines and then `subtract_floor0` (as other forms do).

**Line 7.** "Enter the amount from Form 1040 ... line 11a" (f2441 p. 1, line 7). Supply: `f1040.line11a`.

**Line 8.** "Enter on line 8 the decimal amount shown below that applies to the amount on line 7" (f2441 p. 1, line 8). The table is in section 5. It is banded "Over ... But not over", which is (lo, hi]. That does not match the project's [at_least, less_than) money tables. See Q6 and Q7.

**Line 9a.** "Multiply line 6 by the decimal amount on line 8" (f2441 p. 1, line 9a). Encoding: `multiply_rate`, which accepts a Rate line (spec 4.2, keyed_lookup paragraph).

**Line 9b.** "If you paid 2024 expenses in 2025, complete Worksheet A in the instructions ... Otherwise, enter -0-" (f2441 p. 1, line 9b). This is Worksheet A, lines 1-13 (i2441 p. 7):
- Inputs: 2024 Form 2441 line 3; 2024 expenses paid in 2025; 2024 Form 2441 lines 24+25 and line 6; 2024 earned income of each spouse; 2024 AGI.
- Line 4 limit: $3,000 or $6,000.
- Line 12: the same 35% to 20% table, applied to 2024 AGI.
- The worksheet or an equivalent statement is attached: "Attach to your tax return a copy of this worksheet or a statement" (i2441 p. 7).

See section 4.

**Line 9c.** "Add lines 9a and 9b" (f2441 p. 1, line 9c).

**Line 10.** "Tax liability limit. Enter the amount from the Credit Limit Worksheet in the instructions" (f2441 p. 1, line 10). See section 3.

**Line 11.** "Enter the smaller of line 9c or line 10 here and on Schedule 3 (Form 1040), line 2" (f2441 p. 1, line 11). Schedule 3 line 2: "Credit for child and dependent care expenses from Form 2441, line 11. Attach Form 2441" (f1040s3.txt, line 2).
- Supply: a new `s3.line2`, added into `s3.line8`, whose sum is now `s3.line1` plus zero.

##### Part III: dependent care benefits

**Line 12.** "Enter the total amount of dependent care benefits you received in 2025. Amounts you received as an employee should be shown in box 10 of your Form(s) W-2. Don't include amounts reported as wages in box 1 of Form(s) W-2. If you were self-employed or a partner, include amounts you received under a dependent care assistance program from your sole proprietorship or partnership" (f2441 p. 2, line 12). The instructions add: "don't include amounts reported in box 10 that exceed your plan's exclusion and are therefore reported as wages in box 1" (i2441 p. 5, Line 12).
- **Supply:** a new `w2.box10` per employer, plus the part of box 10 included in box 1 (new input; see Q3). Line 12 is the sum over persons and W-2s of (box 10 less the part in box 1).
- **What box 10 holds** (iw2w3 p. 18, Box 10):
  - "Report all amounts paid or incurred (regardless of any employee forfeitures), including those in excess of the $5,000 exclusion."
  - Amounts "over your plan's exclusion" go in boxes 1, 3 and 5 (iw2w3 p. 19).
  - With a grace period, the employer "may continue to rely on Notice 89-111 by reporting in box 10 the salary reduction amount elected by the employee for the year" (iw2w3 p. 19, Tip). So box 10 can be the election, not the amount received. Lines 13 and 14 correct for this.

**Line 13.** "Enter the amount, if any, you carried over from 2024 and used in 2025 during the grace period" (f2441 p. 2, line 13). i2441 p. 5, Line 13 cites Notice 2005-42. Supply: a new input.

**Line 14.** "Enter the amount, if any, you forfeited or carried forward to 2026" (f2441 p. 2, line 14), printed in parentheses.
- i2441 p. 5, Line 14: "enter on line 14 the total of the following amounts included on line 12". These are forfeited amounts ("you didn't receive it because you didn't incur the expense"), and amounts "you didn't receive but are permitted by your employer to carry forward".
- Example: an election of $5,000 and reimbursed expenses of $4,950 give $50 on line 14.
- Supply: a new input.

**Line 15.** "Combine lines 12 through 14" (f2441 p. 2, line 15). "Add the amounts on lines 12 and 13 and subtract from that total the amount on line 14" (i2441 p. 5, Line 15).

**Line 16.** "Enter the total amount of qualified expenses incurred in 2025 for the care of the qualifying person(s)" (f2441 p. 2, line 16). "It doesn't matter when the expenses were paid." (i2441 p. 5, Line 16). Supply: a new input. This is not the same as line 2(d), which requires expenses incurred **and paid** in 2025.

**Line 17.** "Enter the smaller of line 15 or 16" (f2441 p. 2, line 17).

**Line 18.** "Enter your earned income" (f2441 p. 2, line 18). It is figured as for line 4, "however, for purposes of lines 18 and 19, earned income doesn't include any dependent care benefits shown on line 12" (i2441 p. 5, Line 18).
- Supply: `person.box1` plus `person.eic_se`. Box 1 does not contain benefits up to the plan limit, and line 1e is not added here.
- The combat pay election for lines 18 and 19 is independent of the election for lines 4 and 5 (i2441 p. 5, Line 18).

**Line 19.** "If married filing jointly, enter your spouse's earned income (if you or your spouse was a student or was disabled, see the instructions for line 5). If married filing separately, see instructions. All others, enter the amount from line 18." (f2441 p. 2, line 19). For MFS (i2441 p. 5, Line 19): if considered unmarried, use line 18; if not, use the spouse's earned income.

**Line 20.** "Enter the smallest of line 17, 18, or 19. If zero or less, enter -0-" (f2441 p. 2, line 20).

**Line 21.** "Enter $5,000 ($2,500 if married filing separately and you were required to enter your spouse's earned income on line 19). However, don't enter more than the maximum amount allowed under your dependent care plan" (f2441 p. 2, line 21). i2441 p. 5, Line 21: "if your dependent care plan only allows a maximum of $4,000 to be excluded, substitute $4,000". Supply: a param plus a new input for the plan maximum (see Q4).

**Line 22.** "Is any amount on line 12 or 13 from your sole proprietorship or partnership? No. Enter -0-. Yes. Enter the amount here" (f2441 p. 2, line 22). Recommend refusing (section 4).

**Line 23.** "Subtract line 22 from line 15" (f2441 p. 2, line 23).

**Line 24.** "Deductible benefits. Enter the smallest of line 20, 21, or 22. Also, include this amount on the appropriate line(s) of your return" (f2441 p. 2, line 24). These are Schedule C line 14, Schedule E line 19 or 28, or Schedule F line 15 (i2441 p. 5, Line 24). If line 22 is refused, line 24 is 0.

**Line 25.** "Excluded benefits. If you checked "No" on line 22, enter the smaller of line 20 or line 21. Otherwise, subtract line 24 from the smaller of line 20 or line 21. If zero or less, enter -0-" (f2441 p. 2, line 25). With line 22 = 0, both branches give the smaller of lines 20 and 21.

**Line 26.** "Taxable benefits. Subtract line 25 from line 23. If zero or less, enter -0-. Also, enter this amount on Form 1040 ... line 1e" (f2441 p. 2, line 26). i1040gi p. 24, "Line 1e Taxable Dependent Care Benefits From Form 2441, Line 26 ... But first complete Form 2441 to see if you can exclude part or all of the benefits."
- Supply: a new `f1040.line1e`, with `f1040.line1z` changed to 1a + 1e.
- **Downstream:** line 1z is read by:
  - the EIC (`eic.step5_line1`, i1040gi p. 42)
  - the Schedule 8812 Earned Income Worksheet (`s8812.eiw_1a`, i1040s8812 p. 8)
  - the social security worksheet (`ssb.yaml` line 129)
  - Form 1040 line 9
  
  So taxable benefits reach all of these.

**Line 27.** "Enter $3,000 ($6,000 if two or more qualifying persons)" (f2441 p. 2, line 27). Above it: "To claim the child and dependent care credit, complete lines 27 through 31 below."

**Line 28.** "Add lines 24 and 25" (f2441 p. 2, line 28).

**Line 29.** "Subtract line 28 from line 27. If zero or less, stop. You can't take the credit. Exception. If you paid 2024 expenses in 2025, see the instructions for line 9b" (f2441 p. 2, line 29). Encoding: `subtract_floor0`. A zero flows through to line 3, which gives a zero credit unless line 9b applies. This matches the project's "Stop here" practice (`s8812.line12` note).

**Line 30.** "Complete line 2 on page 1 of this form. Don't include in column (d) any benefits shown on line 28 above. Then, add the amounts in column (d)" (f2441 p. 2, line 30). See Q5 on allocating line 28 across persons.

**Line 31.** "Enter the smaller of line 29 or 30. Also, enter this amount on line 3 on page 1 of this form and complete lines 4 through 11" (f2441 p. 2, line 31).

**Ordering inside the form.** "You must complete Part III of Form 2441 before you can figure the credit, if any, in Part II." (i2441 p. 1, Purpose of Form). Part III must be filed whenever benefits were received, even with no credit: "if you ... received any dependent care benefits for 2025, you must use Form 2441 to figure the amount, if any, of the benefits you can exclude" (i2441 p. 1).

---

#### 2. Rules

##### 2.1 Qualifying person

From i2441 p. 1, Qualifying Person(s), and p503 p. 3, Who Is a Qualifying Person?:
1. "A qualifying child under age 13 whom you can claim as a dependent. If the child turned 13 during the year, the child is a qualifying person for the part of the year they were under age 13."
   - Supply: `dependent.qc_dependent` and a new "under 13 for part of 2025" input. `dependent.age` is the age at the end of the year; see Q8.
   - p503 p. 3: "Your qualifying child who is your dependent and who was under age 13 when the care was provided".
2. "Your disabled spouse who wasn't physically or mentally able to care for themselves and lived with you for more than half the year." New per-person inputs.
3. "Any disabled person who wasn't physically or mentally able to care for themselves who lived with you for more than half the year and whom you can claim as a dependent or could claim as a dependent except:
   a. The disabled person had gross income of $5,200 or more,
   b. The disabled person filed a joint return, or
   c. You (or your spouse if filing jointly) could be claimed as a dependent on another taxpayer's 2025 tax return."

Further rules:
- **Incapable of self-care:** "Persons who can't dress, clean, or feed themselves because of physical or mental disabilities ... Also, persons who must have constant attention to prevent them from injuring themselves or others" (i2441 p. 1; p503 p. 3).
  - This is **not** the project's `dependent.disabled` ("permanently and totally disabled", i1040gi p. 17), so a new Bool is needed.
- **Residence:** "To be a qualifying person, generally the person must have lived with you for more than half of 2025." (i2441 p. 1)
- **Birth or death:** "treated as having lived with you for more than half of 2025 if your home was the person's home more than half the time they were alive in 2025" (p503 p. 3).
- **Status day by day:** "You determine a person's qualifying status each day ... count only those expenses through September 15" (p503 p. 3, Person qualifying for part of year).
- **Yearly limit:** "Use the $3,000 limit if you had one qualifying person at any time during the year. Use $6,000 if you had more than one qualifying person at any time during the year." (p503 p. 12, Yearly limit)
- **Divorced or separated parents:** the custodial parent treats the child as a qualifying person even if they can't claim the child as a dependent. "the noncustodial parent can't treat the child as a qualifying person even if that parent is entitled to claim the child as a dependent" (i2441 p. 1; p503 p. 3).
  - i1040gi p. 20 agrees: a release to the noncustodial parent "doesn't allow the noncustodial parent to claim ... the credit for child and dependent care expenses, the exclusion for dependent care benefits".
  - The tie-breaker benefits list includes Schedule 3 line 2 and Form 2441 Part III (i1040gi p. 21; p. 44).

**Conflict with the existing model.**
- Item 3a (gross income of $5,200 or more) collides with `dependent.income_exception`. That line refuses a "permanently and totally disabled" person whose gross income is at or over the limit (the sheltered-workshop exception).
- Item 3b (a person who filed a joint return) collides with the `dependent.married` refusal.
- So item 3's exceptions are currently unreachable, and the dependent refusals fire first.

##### 2.2 Who can take the credit or exclusion; the joint-return test

"You can take the credit or the exclusion if all five of the following apply" (i2441 p. 2):
1. Filing status is single, HOH, QSS or MFJ. MFS: see below.
2. The care was so you (or your spouse if filing jointly) could work or look for work: "if you didn't find a job and have no earned income for the year, you can't take the credit or the exclusion".
3. The care was for one or more qualifying persons.
4. The provider was not your spouse, not the parent of your qualifying child, and not a person you can claim as a dependent. "If your child ... provided the care, they must have been age 19 or older by the end of 2025 and they can't be your dependent."
5. Provider information is reported on line 1, and qualifying-person information on line 2.

p503 p. 2 lists seven tests, including the Joint Return Test (5) and the Provider Identification Test (6). It also has test 7: the excluded or deducted benefits must be less than the $3,000/$6,000 limit for any credit to remain.

**MFS.**
- i2441 p. 2, Married Persons Filing Separately: the filer is "considered unmarried" if they lived apart from their spouse for the last 6 months of 2025, their home was the qualifying person's main home for more than half of 2025, and they paid more than half the cost of keeping it up. If not considered unmarried, "you can't generally take the credit. However, you can generally take the exclusion if you meet items 2 through 5."
- p503 p. 8 states four conditions (it adds "You file a return apart from your spouse").
- i1040gi p. 14: MFS filers "will only be able to take ... child and dependent care credit in very limited circumstances".

**Death of spouse.** "If your spouse died during the year and you don't remarry before the end of the year, you must generally file a joint return to take the credit." (p503 p. 9). On the earned income limit, the surviving spouse "may, but aren't required to, take into account the earned income of your spouse who died during the year" (p503 p. 11, Surviving spouse). i2441 p. 4 says only: "If your spouse died in 2025, see Pub. 503."

##### 2.3 Earned income test, including student or disabled deemed income

- **Line definition:** see line 4 above (i2441 p. 4; p503 pp. 4, 11).
- **Credit limit:** the credit cannot exceed "the smaller of your or your spouse's earned income for the year if you are married at the end of the year". "Use your spouse's earned income for the entire year, even if you were married for only part of the year." (p503 p. 11, Earned Income Limit)
- **Separated spouse:** "you aren't considered married for purposes of the earned income limit. Use only your income" (p503 p. 11).
- **Community property:** disregard community property laws (i2441 p. 4, Special Situations; p503 p. 11).

**Deemed income** (i2441 p. 4, If You or Your Spouse Was a Student or Disabled):
- "For each month or part of a month your spouse was a student or was disabled, they are considered to have worked and earned income. Their earned income for each month is considered to be at least $250 ($500 if you had two or more qualifying persons at any time during 2025)."
- "If your spouse also worked during that month, use the higher of $250 (or $500) or their actual earned income for that month."
- "Figure your spouse's earned income on a monthly basis."
- "These rules for a spouse who was a student or disabled also apply to you if you were a student or disabled."
- "If, in the same month, both you and your spouse were either students or disabled, only one of you can be treated as having earned income in that month."
- **Full-time student:** "enrolled as a full-time student at a school for some part of each of 5 calendar months during 2025". A school excludes on-the-job training, correspondence schools and schools offering courses only through the Internet.
- **Disabled spouse:** "Your spouse was disabled if they weren't physically or mentally capable of caring for themselves."
- p503 p. 4 adds that a disabled spouse "must also live with you for more than half the year".
- p503 p. 4 limits the rule for oneself to joint returns: "If you are filing a joint return, this rule also applies to you." p503 p. 11 says the same: "These rules also apply if you are a student or not able to care for yourself and are filing a joint return." See Q1.
- **Part of a month:** "If your spouse is a full-time student or not able to care for themselves for only part of a month, the full $250 (or $500) still applies for that month." (p503 p. 11)
- **Worked examples:** p503 p. 12, Example 1 (11 × $250 = $2,750) and Example 2 (both spouses qualify, so the lesser earned income is zero and there is no credit).
- **Lines 18/19:** use the same rules (i2441 p. 5, Line 18 Special Situations; line 19 text).

##### 2.4 Work-related expenses

- **Purpose:** "allow you (or your spouse if filing jointly) to work or look for work" and "for a qualifying person's care" (p503 p. 6). Volunteer work or work for a nominal salary is not work (p503 p. 6).
- **Work for part of year:** "you must figure your expenses for each day". Temporary absences of 2 weeks or less need no allocation. Part-time work: allocate unless payment is required for both days worked and days not worked. "Any day when you work at least 1 hour is a day of work." (p503 p. 6)
- **What counts as care:**
  - Excluded: food, lodging, clothing, education and entertainment (unless incidental), kindergarten and above, overnight camp, summer school, and tutoring.
  - Included: day camp, before- and after-school care, transportation by the care provider, and required agency fees and deposits (but a forfeited deposit is not for care).
  - Locators: i2441 p. 2, Care of the qualifying person; p503 p. 7.
- **Outside the home:** allowed for a dependent under 13, or for another qualifying person "who regularly spends at least 8 hours each day in your home". A dependent care center (more than six persons, for a fee) must meet state and local regulations. i2441 p. 2; p503 p. 7.
- **Household services:** include a cook, maid, babysitter, housekeeper or cleaning person if partly for care; exclude a chauffeur, bartender or gardener. "You can also include your share of the employment taxes paid on wages" (i2441 p. 2; p503 p. 8, Taxes paid on wages). Meals and lodging for a housekeeper count (p503 p. 8).
- **Partly work-related expenses:** divide them, unless only a small part is for other purposes (p503 p. 8).
- **Payments not counted** (p503 p. 8, Payments to Relatives or Dependents):
  1. to a dependent of you or your spouse
  2. to "Your child ... who was under age 19 at the end of the year, even if they aren't your dependent"
  3. to "A person who was your spouse any time during the year"
  4. to "The parent of your qualifying person if your qualifying person is your child and under age 13"
- **Medical expenses:** the same expense cannot be used for both. Any excess over the limits may be added to medical expenses (p503 p. 10; i2441 p. 2). "Amounts excluded from your income under your employer's dependent care benefits plan can't be used to claim a medical expense deduction." (p503 p. 10)
- **Child support** is not a qualified expense (i2441 p. 2).

##### 2.5 Dollar limits and percentage

- **$3,000 / $6,000:** f2441 lines 3 and 27; i2441 p. 4; p503 p. 12, Dollar Limit.
- **Reduced dollar limit:** "If you received dependent care benefits that you exclude or deduct from your income, you must subtract that amount from the dollar limit" (p503 p. 12). Examples: George, $3,000 − $1,000; Randall, $6,000 − $5,000 (p503 pp. 12-13).
- **Percentage:** based on AGI on Form 1040 line 11a, from 35% down to 20% (p503 p. 13, Amount of Credit; f2441 line 8). The table is in section 5.

##### 2.6 Part III specifics

- **Exclusion limit:** "For 2025, the maximum amount that can be excluded from your income through a dependent care assistance program is $5,000 ($2,500 if married filing separately)." (i2441 p. 5, Line 21; p503 p. 10)
- **Smallest-of rule:** the exclusion is the smallest of benefits, expenses incurred, your earned income, your spouse's earned income, and the plan maximum (p503 p. 10, items 1-5).
- **Self-employed:** "If you are self-employed and receive benefits from a qualified dependent care benefit plan, you are treated as both employer and employee ... you would get a deduction on Schedule C ... line 14" (p503 p. 10).
- **Forfeitures and carryforwards:** line 14 (i2441 p. 5).
- **Grace period:** line 13 (i2441 p. 5, Notice 2005-42).
- **Taxable amount:** line 26 to Form 1040 line 1e (i2441 p. 6, Line 26; i1040gi p. 24).
- **Recalculation (lines 27-31):** "If you are reporting dependent care benefits in Part III of the form, you will need to complete lines 27 through 31 if you are also claiming the credit" (i2441 p. 6). Worked example: the Paris family, with $1,000 of benefits and $18,500 for James, gives a $5,000 line 3 limit (p503 p. 13).
- **Effect of exclusion on the credit:** excluded benefits are not work-related expenses, and they reduce the dollar limit (p503 p. 11).

---

#### 3. Credit limit and ordering

**Form 2441 Credit Limit Worksheet (line 10)** (i2441 p. 5, Line 10 Credit Limit Worksheet):
1. "Enter the amount from Form 1040 ... line 18"
2. "Enter the amount from Schedule 3 (Form 1040), line 1 (foreign tax credit) and line 6l (Form 8978, line 14)"
3. "Subtract line 2 from line 1. Also enter this amount on Form 2441, line 10. But if zero or less, stop; you can't take the credit"

Supply: `f1040.line18` and `s3.line1`. Line 6l is refused by `scope.credits` (Form 8978).

**What each later worksheet subtracts:**

| Worksheet | Subtracts from Form 1040 line 18 | Locator |
|---|---|---|
| Form 2441 Credit Limit Worksheet | Sch 3 lines 1, 6l | i2441 p. 5 |
| Form 8880 Credit Limit Worksheet (line 11) | "Schedule 3, lines 1 through 3, 6d, and 6l" | f8880 p. 2, Line 11 |
| 5695 Energy Efficient Home Improvement Credit Limit Worksheet (line 31) | 6l, 1, **2**, 6d, 3, 4 | i5695 p. 7 |
| Schedule 8812 Credit Limit Worksheet A (line 2) | Sch 3 lines 1, **2**, 3, 4, 5b, 6d, 6f, 6l, 6m | i1040s8812 p. 4 |
| 5695 Residential Clean Energy Credit Limit Worksheet (line 14) | 6l, 1, **2**, 6d, 3, 4, 5695 line 32, 6m, 6f, Form 1040 line 19 (or the 8812 CLW B line 14 amount), 6g, 6c, 6h | i5695 p. 5 |

Ordering implied by the table:
- Form 2441
- Form 8880
- Form 5695 Part II (line 32 / Sch 3 line 5b)
- Schedule 8812 CLW A (Form 1040 line 19)
- Form 5695 Part I

Form 2441 comes first among them, after the foreign tax credit (and Form 8978). Its line 11 must exist before 8880, 5695 and 8812 can be evaluated.

**Schedule 8812 CLW B** is completed only for Forms 8396, 8839, 5695 Part I or 8859, with no Form 2555 and Schedule 8812 line 4 above zero (i1040s8812 p. 4). The 5695 Part I worksheet footnote replaces Form 1040 line 19 with "Credit Limit Worksheet B, line 14" in that case (i5695 p. 5).

**Changes to existing lines:**
- `s8812.clw_a2` (currently a copy of `s3.line1`) becomes the sum of `s3.line1` and `s3.line2` (plus lines 4 and 5b from the rest of T-048).
- `s3.line8` gains `s3.line2`.

The credit is nonrefundable: "The amount of credit you can claim is limited to your tax. You can't get a refund for any part of the credit that is more than this limit." (p503 p. 13, How To Claim the Credit)

---

#### 4. Refusal candidates

Each entry gives what the situation needs, why it matters, and a recommendation (compute or refuse). The owner decides.

**R1. Married filing separately (lines A, 19 and 21 at $2,500).**
- Rule: credit only if considered unmarried; otherwise the exclusion only, at $2,500, with the spouse's earned income on line 19 (i2441 pp. 2, 5; p503 p. 8).
- Why refuse: the project refuses MFS altogether (`s3.mfs`).
- Recommendation: **refuse**, inheriting `s3.mfs`.

**R2. Benefits from your own sole proprietorship or partnership (line 22 Yes; line 24 deductible benefits).**
- Why refuse: line 24 feeds Schedule C line 14. That reduces Schedule C profit, so SE line 3 and the earned income on line 18, and so lines 20 and 24 again. This is a cycle the model does not express.
- Partnerships are already refused (`scope.schedule1`). The sole-proprietor case is already refused by `sc.special` (BUG-0070).
- Recommendation: **refuse**. Line 22 is then the constant 0, with a gate citing f2441 line 22 and p503 p. 10.

**R3. Household employee (Part I column (d) "Yes").**
- Form 2441 itself is unaffected, and the employment taxes paid count as expenses (i2441 p. 2).
- Schedule H tax is already refused by the Schedule 2 screen (`s2.yaml`, "household employment taxes").
- Recommendation: **compute**. Collect column (d) and, when it is "Yes", repeat the Schedule H question in the interview.
- The Schedule H filing threshold is not in the archived sources; Pub. 926 is not archived.

**R4. Provider without a TIN (due diligence), "Tax-Exempt" or "LAFCP".**
- The arithmetic is unaffected. The return must show "See Attached Statement" and attach a statement that the provider refused (i2441 p. 3, Due Diligence; p503 p. 9, Provider refusal).
- Recommendation: **compute**. Use a TIN enum with values TIN / tax_exempt / lafcp / see_statement, and display a notice that the statement must be attached.
- Refuse only if the owner wants no outputs that require attachments.

**R5. More than three providers or qualifying persons.**
- This is presentation only (a checkbox and a statement; i2441 pp. 2-3). Spec 4.4: "Pagination is a presentation matter and is not modelled."
- Recommendation: **compute**.

**R6. Dependent care FSA with grace period, forfeiture or carryforward (lines 13, 14).**
- These are two additive inputs. Box 10 may show the election rather than the amount received (iw2w3 p. 19).
- Recommendation: **compute**, with explicit questions (no default) cited to i2441 p. 5.
- See Q12 on carryovers that are not from a grace period.

**R7. Box 10 above the plan limit (excess already in box 1).**
- Line 12 excludes that excess (i2441 p. 5).
- Recommendation: **compute**, with a per-W-2 input for the part of box 10 included in box 1. See Q3.

**R8. Plan maximum below $5,000 (line 21).**
- Recommendation: **compute**, with an input. See Q4.

**R9. Prior-year expenses (line 9b, Worksheet A).**
- It needs about seven 2024 amounts and the same rate table applied to 2024 AGI, plus an attachment (i2441 p. 7). It also reopens the line 29 "stop" exception.
- It is arithmetically simple, and plausibly common (December care paid in January). But every input comes from a prior return the tool does not hold.
- Recommendation: **refuse in the first build** with a gate ("Did you pay in 2025 any 2024 care expenses?"). Computing it later is a self-contained addition.

**R10. Deemed income for a student or disabled spouse or filer (line B; lines 4, 5, 18, 19).**
- It needs month-by-month earned income, the one-spouse-per-month rule, the 5-month student test, and the $250/$500 switch on the count of qualifying persons "at any time" (i2441 p. 4; p503 pp. 4, 11-12).
- A narrow computable case: the deemed person had **no** actual earned income in 2025. Then the amount is the qualifying months times $250 or $500, with the both-spouses months counted once.
- Recommendation: **refuse in the first build**. Option: compute only the zero-actual-earnings case, using a count of months (`multiply_count` exists).
- This case also decides R11, because a disabled spouse who is a qualifying person usually has no earned income.

**R11. Disabled spouse as qualifying person (item 2).**
- It needs inputs for incapable of self-care and lived with you over half the year. In practice it requires R10 for line 5, or the credit is zero.
- Recommendation: decide together with R10. **Refuse** if R10 is refused.

**R12. Qualifying person who is not your dependent (item 3a/b/c: gross income $5,200 or more, joint return, or the filer is claimable).**
- Today these are unreachable: `dependent.income_exception` and `dependent.married` refuse first.
- It needs a "dependent but for" predicate over the qualifying-relative tests with one test removed.
- Recommendation: **refuse** (an explicit gate citing i2441 p. 1, item 3), unless those dependent refusals are reworked.

**R13. Child of divorced or separated parents (custodial parent's non-dependent child).**
- `dependent.divorced_rule` already refuses this.
- Recommendation: **refuse**.

**R14. Spouse died in 2025.**
- There is an optional choice about the deceased spouse's earned income (p503 p. 11), and a remarriage rule (p503 p. 9). The project has no general "spouse died" input.
- Recommendation: **refuse** (a gate). See Q9.

**R15. Nontaxable combat pay (election, lines 4/5 and 18/19 independently).**
- An election only ever raises the credit or exclusion. Computing without it understates.
- The project refuses combat pay for the Schedule 8812 earned income (`s8812.combat_pay`).
- Recommendation: **refuse** on the same input, for consistency.

**R16. Other earned income components already refused.** These are Form 2555 (`sa.excluded_income`), clergy, church employee income, statutory employee (`scope.schedule1`), Medicaid waiver payments (`scope.other_income`), and the optional SE methods (refused under Stage 14).
- Recommendation: **refuse** (inherited); cite i2441 p. 4, items 1-3.

**R17. Expenses prepaid, or incurred in 2025 and paid in 2026.**
- These only change which year the amount belongs to: prepaid amounts count in the year the care is received (p503 p. 10). Line 16 counts expenses incurred in 2025 whenever paid.
- Recommendation: **compute**, through question wording. Ask separately for (i) expenses for 2025 care paid in 2025, including amounts prepaid in 2024 for 2025 care, and (ii) expenses for 2025 care paid in 2026 (line 16 only).

**R18. Child who turned 13 during 2025.**
- Recommendation: **compute**. Count the child as a qualifying person, and ask for expenses only for the part of the year the child was under 13 (i2441 p. 1; p503 p. 3). See Q8.

**R19. A provider who is an ineligible related person** (spouse, parent of a qualifying child under 13, your dependent, your child under 19).
- Payments to them are not qualified expenses (i2441 p. 3, Caution; p503 p. 8).
- Recommendation: **compute**, by excluding such payments in the question wording, or with per-provider Bools whose "Yes" refuses or zeroes. Refusing is simplest to verify.

**R20. Qualifying person without an SSN, ITIN or ATIN (other than "Died").**
- The credit "may" be reduced or disallowed (i2441 p. 3).
- Recommendation: **refuse** (or exclude the person). The "born and died without SSN" case would need an attachment, so refuse it too in the first build.

---

#### 5. Parameters for `params/2025.yaml`

Amounts are in cents, as the existing parameters are.

| Proposed key | Value | Locator |
|---|---|---|
| `dc.limit_one` | 300000 | f2441 p. 1, line 3, "Don't enter more than $3,000 if you had one qualifying person"; line 27; p503 p. 12, Dollar Limit |
| `dc.limit_two` | 600000 | f2441 p. 1, line 3, "or $6,000 if you had two or more persons"; line 27 |
| `dc.persons_two` (Count) | 2 | f2441 line 27, "($6,000 if two or more qualifying persons)" |
| `dc.rate_table` (16 bands, AGI line 7 to a Rate) | 0 to 15,000: .35; 15,000 to 17,000: .34; 17,000 to 19,000: .33; 19,000 to 21,000: .32; 21,000 to 23,000: .31; 23,000 to 25,000: .30; 25,000 to 27,000: .29; 27,000 to 29,000: .28; 29,000 to 31,000: .27; 31,000 to 33,000: .26; 33,000 to 35,000: .25; 35,000 to 37,000: .24; 37,000 to 39,000: .23; 39,000 to 41,000: .22; 41,000 to 43,000: .21; over 43,000 ("No limit"): .20. Each band is "Over / But not over". | f2441 p. 1, line 8; the same table at p503 p. 13, Amount of Credit, and i2441 p. 7, Worksheet A line 12 (2024 AGI) |
| `dc.exclusion_max` | 500000 | f2441 p. 2, line 21, "Enter $5,000"; i2441 p. 5, Line 21, "For 2025, the maximum amount ... is $5,000"; p503 p. 10 |
| `dc.exclusion_mfs` | 250000 | f2441 p. 2, line 21, "($2,500 if married filing separately ...)"; only needed if MFS is supported |
| `dc.deemed_one` (per month) | 25000 | i2441 p. 4, "considered to be at least $250"; p503 p. 11; only if R10 is computed |
| `dc.deemed_two` (per month) | 50000 | i2441 p. 4, "($500 if you had two or more qualifying persons at any time during 2025)" |
| `dc.student_months` (Count) | 5 | i2441 p. 4, "some part of each of 5 calendar months during 2025"; p503 p. 4 |
| `dc.child_age` (Count) | 13 | i2441 p. 1, "A qualifying child under age 13" |
| `dc.provider_child_age` (Count) | 19 | i2441 p. 2, item 4, "age 19 or older by the end of 2025"; p503 p. 8 |
| reuse `qr.gross_income_limit` | 520000 | i2441 p. 1, item 3a, "gross income of $5,200 or more"; p503 p. 3 |
| reuse the "more than half the year" test (`dependent.lived_half`, months > 6) | | i2441 p. 1, "lived with you for more than half of 2025" |

Thresholds that appear only in definitions, for question wording rather than params:
- 8 hours a day in your home (i2441 p. 2)
- a dependent care center cares for more than six persons (i2441 p. 2)
- a temporary absence is 2 weeks (p503 p. 6)
- a day of work is at least 1 hour (p503 p. 6)
- church employee income of $108.28 (i2441 p. 4; refused)
- lived apart for the last 6 months (MFS; i2441 p. 2)

---

#### 6. Open questions (readings the text leaves undecided)

**Q1. Deemed income for a filer who is not married filing jointly.**
- i2441 p. 4: "These rules ... also apply to you if you were a student or disabled", with no restriction to joint returns.
- p503 pp. 4 and 11: "If you are filing a joint return, this rule also applies to you".
- For a single or HOH filer, line 5 copies line 4, so the i2441 reading would let a student with no earnings claim the credit on deemed income.
- The p503 reading matches the form's structure (line 5 "If married filing jointly").
- Matters only if R10 is computed.

**Q2. Whose earned income includes line 1e?**
- Line 4 starts from Form 1040 line 1z, which includes line 1e (taxable benefits, line 26). But line 26 is a return-level amount, and lines 4 and 5 must be figured "separately" for each spouse (i2441 p. 4).
- Candidate readings for MFJ: (a) assign it to the spouse whose W-2 box 10 produced it; (b) assign it in proportion to each spouse's line 12 share; (c) put it with the filer.
- Under (a), when both spouses have box 10, the split of a joint line 26 is still undefined.
- It matters only when line 1e > 0 and the credit is also claimed. That requires benefits above the earned income or $5,000 limit; in that case line 29 is usually 0 anyway ($5,000 or more excluded against a $3,000 limit, or $6,000 with a remainder of up to $1,000).

**Q3. Line 12 from W-2 box 10.**
- Box 10 includes amounts over the exclusion, which are also in box 1 (iw2w3 pp. 18-19). Line 12 must leave out "amounts reported in box 10 that exceed your plan's exclusion and are therefore reported as wages in box 1" (i2441 p. 5).
- Reading (a): ask, per W-2, for the part of box 10 included in box 1.
- Reading (b): compute it per W-2 as box 10 less the plan's limit. This needs the plan limit per employer, and the employer may have used $2,500.
- I recommend (a).

**Q4. Line 21 "maximum amount allowed under your dependent care plan"** when spouses on a joint return have two plans, or one person has two employers.
- The form speaks of one plan. Candidate readings: the $5,000 return limit, reduced only if every plan's maximum is lower; or the sum of the plan maxima, capped at $5,000.
- The text does not say which.

**Q5. Line 30 and the allocation of line 28 to qualifying persons.**
- Column (d) must leave out benefits shown on line 28, per person, but no allocation rule is given. In the Paris example the benefits fully covered one child's expenses (p503 p. 13).
- Encoding choice:
  - compute line 30 as the total gross expenses incurred and paid in 2025 less line 28, floored at 0, and ask the per-person column (d) net only for display; or
  - ask the user to enter column (d) net per person.
- The first choice is verifiable, but the per-person display is then not determined by the computation.
- A related point: line 28 counts excluded benefits against expenses "incurred" in 2025 (line 16), while column (d) needs incurred **and paid**.

**Q6. Line 8 when AGI is zero or less.** The table starts "Over $0". In this slice, AGI ≤ 0 should give Form 1040 line 18 = 0, so line 10 = 0 and the credit is 0 whatever the rate. A rate must still be defined for the line to be known. I propose .35 for line 7 ≤ 0 and recording it as an ambiguity.

**Q7. Encoding the rate table.**
- `table_lookup` returns money over [at_least, less_than) bands, keyed by filing status. The form's bands are (over, not over], and its values are rates.
- Options:
  - a 16-alternative `choose` with `gt`/`lte` guards on line 7 and Rate params (no new atom; verbose but checkable);
  - a variant of `table_lookup` that returns rates, which needs the spec 4.2 atom-addition procedure;
  - for whole-dollar AGI, shift each bound by one cent, (lo, hi] = [lo+1¢, hi+1¢), which still needs a Rate result.
- Owner's choice.

**Q8. Counting a child who turned 13 in 2025, and the birthday edge.**
- `dependent.age` (at the end of 2025) = 13 usually means the child was under 13 for part of 2025. But a child born on January 1, 2012 is treated by the IRS age convention (Pub. 501, not archived) as 13 on December 31, 2024.
- I recommend a direct question ("under 13 at any time in 2025 while care was provided") rather than deriving it.

**Q9. Surviving spouse's earned income.**
- "you may, but aren't required to, take into account the earned income of your spouse who died" (p503 p. 11). The text does not say what replaces it on line 5: line 4 (as for "all others") or the spouse's actual partial-year earnings.
- Reading: if not taken into account, the limit is the survivor's earned income alone.
- Moot if R14 refuses.

**Q10. Which providers are ineligible.**
- i2441 p. 2, item 4: "your spouse, the parent of your qualifying child".
- p503 p. 8: "A person who was your spouse any time during the year" and "The parent of your qualifying person if your qualifying person is your child and under age 13".
- The publication's version is both broader (a spouse at any time) and narrower (a parent only when the child is under 13). The question wording should follow one; I suggest p503 as the more specific.

**Q11. MFS "considered unmarried".** i2441 p. 2 gives three conditions; p503 p. 8 gives four (adding "You file a return apart from your spouse", which MFS implies). Moot while MFS is refused.

**Q12. Carryovers that are not from a grace period.**
- Line 13 covers only amounts "carried over from 2024 and used in 2025 during the grace period" (f2441 line 13; i2441 p. 5).
- Line 14 includes amounts "permitted by your employer to carry forward and use in the following year".
- Where a 2024 carryforward that is not a grace-period amount, used in 2025, belongs on the 2025 form is not stated. It is probably on line 12, if the employer reported it in box 10.

**Q13. "Lived with you more than half the year" for a person born or died in 2025.**
- For Form 2441, p503 p. 3 uses "more than half the time they were alive".
- `dependent.months` asks a person who is not a qualifying child about the "entire time".
- For an item 3 person born or died in 2025 the two disagree, though item 3 is refused under R12.

**Q14. Line 1e's effect downstream.**
- Adding line 1e to line 1z flows taxable benefits into the EIC earned income (`eic.step5_line1`), the Schedule 8812 Earned Income Worksheet line 1a (`s8812.eiw_1a`), and the social security benefits worksheet (`ssb.yaml`).
- Those instructions read line 1z as printed, so this is what the text says. I am noting it only so the fixtures for those forms are rerun. I did not check the EIC or 8812 instructions for any special treatment of line 1e.

**Q15. Line 15 sign.** Line 14 amounts are "included on line 12" (i2441 p. 5), so line 15 should never be negative. Its type should be Dollars, with a refusal or input check if line 14 > line 12 + line 13, rather than a silent floor.

**Q16. Reconciling the screen.**
- `scope.other_income` refuses all "dependent care ... benefits", and `scope.credits` refuses Schedule 3 line 2.
- Both should be narrowed to the refusals chosen above.
- `sc.special` (BUG-0070) stays as the line 22 refusal.

### Form 5695 (2025), Residential Energy Credits: line map and premises for encoding

Read-only research, tax-formalization repository. Nothing in the repository was edited.

#### 0. Sources and locator conventions

| Short name | File | Notes (from `sources/2025/manifest.json`) |
|---|---|---|
| f5695 | `sources/2025/f5695.{cols.txt,txt}` | 4 pages; footer "Form 5695 (2025) Created 3/20/25"; fetched from the current-year URL `irs-pdf/f5695.pdf` |
| i5695 | `sources/2025/i5695.{cols.txt,txt}` | 7 pages; footer "Instructions for Form 5695 (2025) Catalog Number 66412G / Jan 22, 2026" |
| i1040gi | `sources/2025/i1040gi.cols.txt` | Schedule 3 line 5 is on printed p. 116 (cols chunk 116, same number) |
| i1040s8812 | `sources/2025/i1040s8812.{cols.txt,txt}` | CLW A p. 4, CLW B pp. 5-6 |
| plaw-119-21 | `sources/2025/plaw-119-21.txt` | P.L. 119-21, secs. 70505-70506 at 139 Stat. 251 |

"p. N" means the N-th form-feed chunk of the .cols.txt file; for these four documents that equals the printed page number (checked: i5695 chunk 5 ends "5"; i1040gi chunk 116 ends "116"; i8812 chunk 4 ends "4").

Both PDFs were fetched from the current-year `irs-pdf` address, not `irs-prior`. The project's archiving rule (spec 5) means these must stay pinned. Once 2026 revisions are posted, that address will serve different content.

#### 1. How the project encodes forms (what this build has to fit)

- Spec 4.1-4.6 (spec/spec.md): money is integer cents. `Rate` is num/den. Atoms are input, copy, param, sum, subtract, subtract_floor0, smaller_of/larger_of, multiply_rate, multiply_count, prorate, round, table_lookup, keyed_lookup, sum_over, test, choose, opaque. **There are no strings.** That means the address blocks (above line 1, line 7b, 17d, 21c) and the QMID text fields (19b, 19d, 20a, 22a, 23a, 24a, 25d, 29a/c/e) cannot be values. They can only be represented as Bool attestations or left as presentation. Gates are cited `Bool` lines, and refusals are data: a `refuses:` list with `when`, `form`, `remedy` and `cite`.
- Spec 4.5: parameters go in `params/2025.yaml`, one cited entry each. Examples: `sli.max: {type: NonNegDollars, value: 250000, cite: {doc, locator}}` and `actc.rate: {type: Rate, value: {num: 15, den: 100}}`.
- Current credit screen: `forms/2025/scope.yaml` `scope.credits` is a single declared Bool ("Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, ... and the earned income credit ...?"). Its refusal names "Other credit forms (Schedule 3 lines 2 to 4, 5b, 6d, 6f, 6l and 6m; Form 1040 lines 29 to 31)". **Line 5a is not in that list**, although the question covers it; the same list appears on `s3.line8`. T-048 (TASKS.md line 59) narrows `scope.credits` in this stage.
- `forms/2025/s3.yaml`: `s3.line8` = sum(`s3.line1`, `s3.zero`). Lines 5a and 5b are not yet modelled.
- `forms/2025/s8812.yaml`: `s8812.clw_a2` = copy `s3.line1`, refused under `scope.credits`. `s8812.clw_a4` = copy `s8812.zero`, refused under `scope.credits` with form "Credit Limit Worksheet B (Forms 8396, 8839, 5695 Part I, 8859)". Credit Limit Worksheet B is not encoded. The lines it reuses already exist: `s8812.line12`, `line4`, `line16b`, `eiw_7`, `line19` to `line26`, and params `actc.per_child`, `actc.earned_floor`, `actc.rate`, `actc.three_children`.

#### 2. Line map

##### 2.1 General rules that feed both parts

| Rule | Locator / quote |
|---|---|
| Home | i5695 p. 1, Who Can Take the Credits, "Home": "A home is where you lived in 2025 and can include a house, houseboat, mobile home, cooperative apartment, condominium, and a manufactured home ..." |
| Main home | i5695 p. 1, "Main home. Your main home is generally the home where you live most of the time ... Caution: You may only have one main home at a time." |
| When a cost counts as paid | i5695 p. 1, "Costs": "costs are treated as being paid when the original installation of the item is completed ... For purposes of the residential clean energy credit only, costs connected with the construction of a home are treated as being paid when your original use of the constructed home begins." |
| Business use (80% rule) | i5695 p. 1, "Costs": "If less than 80% of the use of an item is for nonbusiness purposes, only that portion of the costs that is allocable to the nonbusiness use can be used to determine either credit." |
| Construction | i5695 p. 1, Caution: "The residential clean energy credit (Part I) is available for both existing homes and homes being constructed. The energy efficient home improvement credit (Part II) is only available for existing homes." |
| Condo / co-op | i5695 p. 2, "Association or cooperative costs ... you are treated as having paid your proportionate share of any costs of such association or corporation." The same rule is in i1040gi p. 116, Line 5, "Condos and co-ops". |
| Utility subsidy | i5695 p. 2, Caution: "If you received a subsidy from a public utility ... and that subsidy wasn't included in your gross income, you must reduce your cost for the product by the amount of that subsidy ... also applies if a third party (such as a contractor) receives the subsidy on your behalf. See Fact Sheet 2025-01". The fact sheet is **not archived**. |
| Subsidized energy financing (Part II only) | i5695 p. 3: "Any amounts provided for by subsidized energy financing can't be used to figure the energy efficient home improvement credit." |
| Basis reduction | i5695 p. 1, "Home": "You must reduce the cost basis of your home if a residential energy credit is allowed". This has no effect on the 2025 computation and could be shown as a notice. |
| Section 48 guidance does not apply | i5695 p. 2, Caution: "Notice 2018-59 and Notice 2021-41, does not apply to the residential energy credits." |

##### 2.2 Part I: residential clean energy credit (to Schedule 3 line 5a)

The rate is 30%: f5695 p. 1 lines 6b and 9, and i5695 p. 1 Reminders, "The credit rate for property placed in service in 2022 through 2025 is 30%." Labor counts: i5695 p. 4 Tip, "Include on lines 1 through 4, 5b, and 8 any labor costs properly allocable to the onsite preparation, assembly, or original installation ... and for piping or wiring to interconnect".

| Line | What it does (f5695 p. 1 unless noted) | Inputs / conditions | Locator for conditions |
|---|---|---|---|
| Note | "Skip lines 1 through 11 if you only have a credit carryforward from 2024." | — | f5695 p. 1, Part I note |
| Address | "Enter the complete address of the home where you installed ... lines 1 through 4 and 5b. For more than one home, see instructions." | If there is more than one home, enter the one "with the greatest total cost", attach a statement listing the others, and put all costs on one form. No value to compute; string. | i5695 p. 4, Part I; p. 2 "enter the total of those costs on the applicable line(s) of one Form 5695" |
| 1 | "Qualified solar electric property costs" | Amount paid, labor included. Home in the US; "The home doesn't have to be your main home." Solar roofing tiles/shingles qualify; decking/rafters don't. | i5695 p. 2, "Qualified solar electric property costs" |
| 2 | "Qualified solar water heating property costs" | At least half the energy from the sun; certified by SRCC or a state-endorsed equivalent; need not be the main home | i5695 p. 2, "Qualified solar water heating property costs" |
| 3 | "Qualified small wind energy property costs" | Need not be the main home | i5695 pp. 2-3 (text runs over the column break): "The home doesn't have to be your main home." |
| 4 | "Qualified geothermal heat pump property costs" | Must meet Energy Star "in effect at the time of purchase"; need not be the main home | i5695 p. 2 |
| 5a | Yes/No: "Does the qualified battery storage technology have a capacity of at least 3 kilowatt hours?" | Gate. "No" means no battery credit. | i5695 p. 4, Lines 5a and 5b |
| 5b | "If you checked the 'Yes' box, enter the qualified battery technology costs" | Cost; "installed in connection with your home located in the United States". The text is **silent** on whether this must be the main home (see Q3). | i5695 p. 2, "Qualified battery storage technology costs" |
| 6a | "Add lines 1 through 5b" | sum | f5695 p. 1 |
| 6b | "Multiply line 6a by 30% (0.30)" | multiply_rate | f5695 p. 1 |
| 7a | Yes/No: "Was qualified fuel cell property installed on, or in connection with, your main home located in the United States? ... If you checked the 'No' box ... Skip lines 7b through 11." | Gate. Fuel cell requires the **main** home. | f5695 p. 1; i5695 p. 4 Lines 7a Through 7c |
| 7b | Address of the main home | String. For MFJ spouses with different main homes, give one address plus a statement for the other, and "add your qualified fuel cell property costs together on line 8 of one Form 5695" | i5695 p. 4 |
| 7c | Checkbox: "If the special rule for joint occupants applies, check here and attach a statement" | Joint occupancy | f5695 p. 1; i5695 p. 2 "Joint occupancy" |
| 8 | "Qualified fuel cell property costs" | Nameplate capacity of at least 0.5 kW and electricity-only efficiency above 30% | i5695 p. 2, "Qualified fuel cell property costs" |
| 9 | "Multiply line 8 by 30% (0.30)" | — | f5695 p. 1 |
| 10 | "Kilowatt capacity of property on line 8 above. If less than 0.5 kW, enter -0-. ... x $1,000" | kW capacity, "may only be claimed in half kW increments. Multiply the kW capacity by $1,000" | i5695 p. 4, Line 10; i5695 p. 2: "limited to $500 for each one-half kilowatt of capacity" |
| 11 | "Enter the smaller of line 9 or line 10" | smaller_of | f5695 p. 1 |
| 12 | "Credit carryforward from 2024. Enter the amount, if any, from your 2024 Form 5695, line 16" | Input (NonNegDollars) | f5695 p. 1; i5695 p. 1 Purpose: "take any residential clean energy credit carryforward from 2024" |
| 13 | "Add lines 6b, 11, and 12" | sum | f5695 p. 1 |
| 14 | "Limitation based on tax liability. Enter the amount from the Residential Clean Energy Credit Limit Worksheet" | See the worksheet below | i5695 p. 4 "Line 14"; worksheet p. 5 |
| 15 | "Residential clean energy credit. Enter the smaller of line 13 or line 14. Also include this amount on Schedule 3 (Form 1040), line 5a" | smaller_of, then to `s3.line5a` | f5695 p. 1 |
| 16 | "Credit carryforward to 2026. If line 15 is less than line 13, subtract line 15 from line 13" | subtract_floor0(13, 15). This is a display line (nothing on the 2025 return reads it). "File this form even if you can't use any of your credit in 2025." | f5695 p. 1; i5695 p. 5 "Line 16" |

**Residential Clean Energy Credit Limit Worksheet, line 14** (i5695 p. 5):
1. "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 18" → `f1040.line18`.
2. "Enter the total of the following credit(s)/adjustment(s) if you are taking the credit(s)/adjustment(s) on your 2025 income tax return":
   - Schedule 3 line 6l
   - Schedule 3 line 1 (foreign tax credit)
   - Schedule 3 line 2 (Form 2441)
   - Schedule 3 line 6d
   - Schedule 3 line 3 (education)
   - Schedule 3 line 4 (Form 8880)
   - **Form 5695 line 32** (Part II)
   - Schedule 3 lines 6m and 6f (clean vehicles)
   - **"Child tax credit or credit for other dependents, Form 1040 ... line 19\*"**
   - Schedule 3 lines 6g, 6c and 6h (mortgage interest, adoption, DC homebuyer)

   The note under the list reads "Enter the total ... only if allowed and taken on your 2025 income tax return."
3. "Subtract line 2 from line 1. Also enter this amount on Form 5695, line 14. If zero or less, enter -0- on Form 5695, lines 14 and 15". In atoms this is subtract_floor0.

The footnote under the worksheet (i5695 p. 5) reads: "\* Include the amount in the instructions for Schedule 8812 (Form 1040), Credit Limit Worksheet B, line 14, instead of the amount from Form 1040 ... line 19, if the instructions for Schedule 8812 (Form 1040) direct you to complete Credit Limit Worksheet B."

The instructions also say to compute those credits first: i5695 p. 4, "Before you begin Part I. Figure the amount of the credits shown in the credit limitation worksheet if you take those credits on your return."

##### 2.3 Part II: energy efficient home improvement credit (to Schedule 3 line 5b)

Summary of the limits (i5695 pp. 2-3): "A total combined credit limit of $1,200 for qualified energy property. A credit limit of $600 for any qualified energy property item. A combined credit limit of $600 for all exterior windows and skylights. A credit limit of $250 for any qualifying exterior door and $500 total for all qualifying exterior doors. A combined credit limit of $2,000 for heat pump and heat pump water heaters; biomass stoves and boilers. A credit limit of $150 for home energy audits."

The QMID requirement appears in two places. i5695 p. 1, What's New: "you must include the four-character alphanumeric unique qualified manufacturer identification number (QMID) for each item". i5695 p. 5, Part II Caution: "To qualify ... for specified property, you must provide a valid QMID for each item." QMIDs are required for doors, windows and skylights (p. 3, Section A: "For exterior doors, windows, and skylights installed in 2025, a valid QMID must be reported") and for all Section B energy property (p. 3: "For qualified energy property installed in 2025, a valid QMID must be reported"). They are **not** asked on line 18 (insulation) or line 26 (audits).

Labor is excluded in Section A (i5695 p. 3: "don't include amounts paid for the onsite preparation, assembly, or original installation of the building envelope component", repeated in the p. 5 Caution for 18a, 19a, 19d, 19e, 20a, 20b). Labor is included in Section B (p. 3, and the p. 6 Tip for 22a-25c and 29a-29f).

**Section A, qualified energy efficiency improvements** (main home, owned, original use, at least 5 years; i5695 p. 3):

| Line | f5695 text | Computation / inputs | Locator |
|---|---|---|---|
| 17a | "Are the qualified energy efficiency improvements installed in or on your main home located in the United States?" | Gate | f5695 p. 2; i5695 p. 5 |
| 17b | "Are you the original user ...?" | Gate | same |
| 17c | "Are the components reasonably expected to remain in use for at least 5 years?" | Gate | same |
| (17a-c No) | Form: "you cannot claim the energy efficient home improvement credit. Do not complete Part II, Section A." | See Q1: the whole credit, or Section A only | f5695 p. 2; i5695 p. 5 |
| 17d | Main-home address. "Caution: You can only have one main home at a time." | String | f5695 p. 2; i5695 p. 5: "You can only claim the energy efficient home improvement credit on one main home." |
| 17e | "Were any of these improvements related to the construction of this main home?" | Gate. Form: "you can only claim ... for qualifying improvements that were not related to the construction". Instructions: "If you check the 'Yes' box, skip lines 18a through 20d." | f5695 p. 2; i5695 p. 5 Line 17e. See Q2. |
| 18a | Cost of insulation / air sealing meeting the IECC | Input; IECC as in effect on January 1, 2021 | i5695 p. 5 |
| 18b | "Multiply line 18a by 30% ... Do not enter more than $1,200" | smaller_of(rate × 18a, 1200) | f5695 p. 2 |
| 19a | "Enter the cost of the most expensive door you bought" | Input | f5695 p. 2; i5695 p. 6 |
| 19b | QMID of that door | Attestation (no strings) | same |
| 19c | "Multiply line 19a by 30% (0.30). Do not enter more than $250" | smaller_of | f5695 p. 2 |
| 19d | QMIDs and costs of "the two next most expensive door(s)" (i), (ii) | 2 inputs | f5695 p. 2; i5695 p. 6 |
| 19e | "Enter the cost of all other qualifying exterior doors" | Input; attach a statement listing each QMID and cost | i5695 p. 6 |
| 19f | "Add lines 19d and 19e" | sum | f5695 p. 2 |
| 19g | "Multiply line 19f by 30% (0.30)" | multiply_rate. No $250 per-door cap appears here. | f5695 p. 2 |
| 19h | "Add lines 19c and 19g. Do not enter more than $500" | smaller_of(sum, 500) | f5695 p. 2 |
| 20a | QMIDs and costs of "four most expensive window(s)/skylight(s)" (i)-(iv) | 4 inputs | f5695 p. 2; i5695 p. 6 |
| 20b | "Enter the cost of all other exterior windows and skylights" | Input plus statement. The instructions say "Energy Star **most efficient** certification", where 20a says "Energy Star certification". | i5695 p. 6 |
| 20c | "Add lines 20a and 20b" | sum | f5695 p. 2 |
| 20d | "Multiply line 20c by 30% ... Do not enter more than $600" | smaller_of | f5695 p. 2 |

Check on line 19: because 19a is the most expensive door, the form's arithmetic gives 250 + min(0.3 × (19d + 19e), 250) whenever 19c = 250. That equals the statutory "$250 per door, $500 total" result. If any other door's 30% is at least $250, both readings give $500. Otherwise no per-door cap binds. If 19c is below $250, every other door is cheaper still, so no per-door cap binds there either. The form's door arithmetic is therefore faithful to the stated per-door limit, and nothing needs to be refused.

**Section B, residential energy property expenditures** ("installed on or in connection with a home that you used during 2025 located in the United States": i5695 p. 3):

| Line | f5695 text | Computation / inputs | Locator |
|---|---|---|---|
| 21a | "Did you incur costs for qualified energy property installed on or in connection with a home located in the United States that you use as a residence?" | Gate; **not** restricted to the main home | f5695 p. 3; i5695 p. 6 |
| 21b | "Was the qualified energy property originally placed into service by you?" | Gate | same |
| (21a/b No) | "Skip lines 22 through 25 and line 29. Go to line 26." | 22d, 23d, 24d, 25e and 29h are 0 | f5695 p. 3 |
| 21c | "Enter the complete address of each home" | String(s) | f5695 p. 3 |
| 22a | QMID and cost of the most expensive central A/C (highest CEE tier) | Input | f5695 p. 3; i5695 p. 6 |
| 22b | Other central A/Cs | Input plus statement | same |
| 22c / 22d | Add; "Multiply line 22c by 30% ... Do not enter more than $600" | The cap applies to the **category**, not each item (Q5) | f5695 p. 3 |
| 23a | QMIDs and costs of the **two** most expensive gas, propane or oil water heaters (i), (ii) | 2 inputs | f5695 p. 3; i5695 p. 6 |
| 23b / 23c / 23d | Others; add; 30% capped at $600 | — | f5695 p. 3 |
| 24a | QMID and cost of the most expensive gas, propane or oil furnace or hot water boiler. Oil units must meet 2021 Energy Star and be rated for at least 20% eligible-fuel blends. | Input | f5695 p. 3; i5695 p. 6 |
| 24b / 24c / 24d | Others; add; 30% capped at $600 | — | f5695 p. 3 |
| 25a | Yes/No: enabling property (panelboards and similar) installed to enable a separate enabled property, "and were both ... installed in 2025?" | Gate. Consecutive-year election: "you can treat both as having been installed in the later of the tax year", and the example uses a 2024 panel | f5695 p. 3; i5695 p. 6 Lines 25a-25e, Note and Example |
| 25b | Code(s) A-G for the enabled property: windows on 20a, A/C on 22a, water heater on 23a, furnace/boiler on 24a, heat pump on 29a, HP water heater on 29c, biomass on 29e | Enum set. Note that doors and insulation are not valid enabled property. | i5695 pp. 6-7 |
| 25c | Cost of enabling property (NEC-consistent, load capacity of at least 200 amps) | Input | i5695 p. 7 |
| 25d | QMID(s) (i), (ii) | Attestation | f5695 p. 3 |
| 25e | "Multiply line 25c by 30% ... Do not enter more than $600" | smaller_of | f5695 p. 3 |
| 26a | Yes/No: audit of the **main home** in the US with a written report by a certified (Qualified) Home Energy Auditor. "If ... No ... Stop. Go to line 27." | Gate; 26c = 0 on No | f5695 p. 4; i5695 p. 3 "Home energy audits", p. 7 |
| 26b / 26c | Audit cost; "Multiply line 26b by 30% ... Do not enter more than $150" | smaller_of | f5695 p. 4 |
| 27 | "Add lines 18b, 19h, 20d, 22d, 23d, 24d, 25e, and 26c" | sum | f5695 p. 4 |
| 28 | "Enter the smaller of line 27 or $1,200" | smaller_of | f5695 p. 4 |
| 29a-29f | QMID and cost of the most expensive, then all others, for each of: electric or natural gas heat pumps (29a/29b), heat pump water heaters (29c/29d), and biomass stoves/boilers with thermal efficiency of at least 75% (29e/29f) | 6 inputs. CEE highest tier for heat pumps. | f5695 p. 4; i5695 p. 7 |
| 29g / 29h | "Add lines 29a through 29f"; "Multiply line 29g by 30% ... Do not enter more than $2,000" | sum; smaller_of | f5695 p. 4 |
| 30 | "Add lines 28 and 29h" | sum. The maximum is $3,200. | f5695 p. 4 |
| 31 | "Limitation based on tax liability. Enter the amount from the Energy Efficient Home Improvement Credit Limit Worksheet" | See below | f5695 p. 4; i5695 p. 7 "Line 31" |
| 32 | "Energy efficient home improvement credit. Enter the smaller of line 30 or line 31. Also include this amount on Schedule 3 (Form 1040), line 5b" | smaller_of, then to `s3.line5b` | f5695 p. 4 |
| 32a | Checkbox for joint occupants, with a statement attached | Joint occupancy | f5695 p. 4; i5695 p. 7 Lines 32a and 32b |
| 32b | Checkbox: "If you live in a condominium or cooperative and have a fractional share ..." | Condo/co-op | same |

Part II has **no carryforward line**. The form has none, and no archived text provides one. Unused Part II credit is not carried.

**Energy Efficient Home Improvement Credit Limit Worksheet, line 31** (i5695 p. 7):
1. Form 1040 line 18.
2. The total of Schedule 3 line 6l, line 1, line 2, line 6d, line 3 and line 4, "only if allowed and taken on your 2025 income tax return".
3. "Subtract line 2 from line 1. Also enter this amount on Form 5695, line 31. If zero or less, enter -0- on Form 5695, lines 31 and 32". In atoms this is subtract_floor0.

#### 3. Ordering

Read from the worksheets themselves:

1. **Before Part II** (EEHIC worksheet line 2, i5695 p. 7): Schedule 3 lines 6l (Form 8978 adjustment), 1 (FTC), 2 (Form 2441), 6d (Schedule R), 3 (Form 8863) and 4 (Form 8880). Part II does not subtract the CTC/ODC.
2. **CTC/ODC (Credit Limit Worksheet A)** reads Part II. CLW A line 2 (i8812 p. 4) adds Schedule 3 lines 1, 2, 3, 4, **5b**, 6d, 6f, 6l and 6m. So Part II comes **before** the CTC. `s8812.clw_a2` must gain `s3.line5b` (and lines 2 and 4).
3. **Part I** (Part I worksheet line 2, i5695 p. 5) subtracts everything in item 1, plus Form 5695 line 32 (Part II), 6m, 6f, the CTC/ODC, 6g, 6c and 6h. So Part I comes **after** Part II and after mortgage interest, adoption and DC homebuyer. How the CTC is counted depends on CLW B:
   - **CLW B is not completed**: Part I subtracts Form 1040 line 19 (the full CTC/ODC). CLW A line 4 = 0 (i8812 p. 4, "If you are not completing Credit Limit Worksheet B, enter -0-"), so the CTC does not depend on 5a and there is no cycle. The CTC/ODC comes before Part I.
   - **CLW B is completed** (i8812 p. 4, CLW A line 4 and p. 3 line 13). All three conditions must hold: "1. You are claiming one or more of ... c. Residential clean energy credit, Form 5695, Part I", "2. You are not filing Form 2555", "3. Line 4 of Schedule 8812 is more than zero". In that case Part I subtracts **CLW B line 14** instead of line 19.
     - CLW B line 14 (i8812 p. 6) is "Is the amount on line 13 ... more than the amount on line 1? No. Subtract line 13 from line 1 ... Yes. Enter -0-". Line 1 is Schedule 8812 line 12 (the CTC/ODC before the tax limit). Line 13 is the smaller of line 2 ($1,700 × qualifying children under 17 with an SSN) and line 12 (larger of the 15% earned-income amount and the social-security-tax excess).
     - So CLW B line 14 is the part of the credit that could not be refundable as ACTC. Only that part is placed ahead of Part I.
     - Then "Next, figure the amount of [Form 8396, 8839, 5695 Part I, 8859]". CLW B line 15 = Schedule 3 lines **5a** + 6c + 6g + 6h, "Enter this amount on line 4 of Credit Limit Worksheet A" (i8812 p. 6, layout text lines 306-320).
     - CLW A line 5 = line 3 − line 4, which becomes Schedule 8812 line 13. The nonrefundable CTC therefore shrinks by the Part I credit, and Schedule 8812 Part II-A (line 16a = line 12 − line 14) can turn the displaced amount into ACTC.
     - There is no cycle. CLW B lines 1-14 do not read 5a. The Part I limit reads CLW B line 14. CLW A line 4 reads 5a.
4. **Form 1040 line 18** is the base of all three worksheets. Schedule 3 line 8 adds 5a and 5b, and that sum goes to Form 1040 line 20.

Encoding notes for CLW B (i8812 pp. 5-6):
- Lines 3-12 parallel Schedule 8812 lines 18a-26 (`s8812.line19` ... `line26` exist), with these differences:
  - Line 3 is "earned income from line 7 of the Earned Income Worksheet" (`s8812.eiw_7`), not line 18a. Line 18a goes through the Earned Income Chart, which can take EIC Worksheet B amounts.
  - The line 6 branch compares line 5 with **line 1** (Schedule 8812 line 12) and tests "line 2 ... $5,100 or more". Schedule 8812 instead compares line 20 with line 17 (`s8812.earned_covers`).
  - "Before you begin" requires the Earned Income Worksheet, line 27a, Schedule 2 lines 5, 6 and 13, and Schedule 3 line 11.
- Existing params can be reused: `actc.per_child` ($1,700), `actc.earned_floor` ($2,500), `actc.rate` (15%), `actc.three_children` ($5,100, checked: params/2025.yaml cites "On line 16b, is the amount $5,100 or more?").

#### 4. Situations a first build might refuse

| Situation | Text | Recommendation |
|---|---|---|
| Any item less than 80% nonbusiness use (business use over 20%) | i5695 p. 1, "Costs": "only that portion of the costs that is allocable to the nonbusiness use can be used". The boundary is exact: 80% nonbusiness use or more gives the full cost. | **Refuse.** Allocation is per item and the text gives no method. Ask one Bool: "Is any item used less than 80% for nonbusiness purposes?" |
| Joint occupancy with non-spouses (Part I fuel cell, line 7c; Part II, line 32a) | i5695 p. 2 (fuel cell: $1,667 per half kW across occupants, prorated by amount paid); p. 3 (Part II: the per-item limit, the $1,200 and the $2,000 are prorated by your share of the total paid by all occupants; "These rules don't apply to married individuals filing a joint return" (p. 2)) | **Refuse.** It needs other occupants' payments and a statement. |
| Neighbors sharing property for both main homes (Part II) | i5695 p. 3, "Joint ownership of qualified property ... You figure your credit on the part of the cost you paid. The limit ... applies to each of you separately." | **Compute.** Enter only your share. The question text must say so. |
| MFJ spouses with separate main homes (Part II) | i5695 p. 3, "Married taxpayers with more than one home": complete lines 17a-30 on a separate form for each main home and combine on line 30 | **Refuse** in the first build. It needs two instances of Part II. It could later become a keyed collection of homes. |
| MFJ spouses with different main homes, fuel cell | i5695 p. 4: add costs on one form | Moot if fuel cells are refused |
| Home not the main home | Part I lines 1-4: "doesn't have to be your main home" (i5695 p. 2). Line 5b: silent. Fuel cell: main home only. Part II Section A and audits: main home only. Part II Section B: "a home that you used during 2025" / line 21a "a home ... that you use as a residence" | **Compute.** Gate each category by its own residence test. Do not assume Part II requires the main home throughout (see Q4). |
| Home outside the United States | Every category requires a US home (i5695 pp. 2-3; lines 7a, 17a, 21a, 26a) | **Compute as not allowed** (zero, by the form's own No boxes). Optionally refuse to make it explicit. Recommend gates, not refusal. |
| Fuel cell property (lines 7-11) | i5695 pp. 2, 4. Main home only. Capacity in half-kW steps (Q6). Joint-occupancy rules. | **Refuse** in the first build (rare). If computed instead: a Count of half-kilowatts, `multiply_count` by $500, and a main-home gate. |
| Condominium or cooperative share | i5695 p. 2 (proportionate share treated as paid); 32b checkbox (p. 7); i1040gi p. 116 | **Compute**, with the share entered as the amount paid. Ask 32b as a Bool for display. Refuse only if the owner wants the share computed from association figures. |
| Carryforward from 2024 (line 12) | f5695 p. 1 line 12 and Note | **Compute.** It is one input from the 2024 Form 5695 line 16. A carryforward-only return skips lines 1-11. |
| Utility subsidy / rebates | i5695 p. 2 Caution (non-income utility subsidy reduces cost; Fact Sheet 2025-01, not archived). Part II: subsidized energy financing excluded (p. 3). | **Compute** with a question asking cost *net of* any utility subsidy not included in income and excluding subsidized financing. Archive Fact Sheet 2025-01 before writing that question, because it covers rebates the instructions do not. |
| Home under construction / new construction | Part I allowed, with cost treated as paid "when your original use of the constructed home begins" (i5695 p. 1). Part II: line 17e (only for existing homes, p. 1 Caution). | Part I: **compute** only if original use began in 2025, with a gate question. If original use began in 2026, the expenditure falls after the 25D termination (Q8). Part II: **refuse** if 17e is Yes (Q2), or zero Section A. |
| Reconstruction of a home | i5695 p. 1, costs paid "when your original use of the reconstructed home begins" | Ask whether original use began in 2025; refuse otherwise. |
| Missing QMID for a Part II item | i5695 p. 5 Caution, p. 1 What's New | **Compute** with a Bool attestation per category ("Do you have a valid QMID for each item?"). No means the item is excluded, or refuse. Strings cannot be stored. |
| Enabling property installed in a different year from enabled property | i5695 p. 6 Note/Example (consecutive-year election) | **Compute** with a single Bool for 25a, worded to include the election. |
| Married filing separately | Already refused (`s3.mfs`, i1040gi p. 14) | Keep refusing. |
| Form 2555 filer | CLW B condition 2 | Already outside scope. |
| Any other Part I worksheet credit (6c, 6f, 6g, 6h, 6m, 6d, 6l) | i5695 pp. 5, 7 | Keep refused under the narrowed `scope.credits`. The worksheets then read only lines 1, 2, 4 and 5b and line 19 (line 3, education, stays refused under T-048) / CLW B line 14. |

#### 5. Parameters for params/2025.yaml

| Proposed key | Type / value | Locator |
|---|---|---|
| `f5695.rate` (or `rce.rate` and `eehi.rate`) | Rate 30/100 | f5695 p. 1 lines 6b and 9 "Multiply ... by 30% (0.30)"; p. 2-4 lines 18b, 19c, 19g, 20d, 22d, 23d, 24d, 25e, 26c, 29h; i5695 p. 1 Reminders "The credit rate ... 2022 through 2025 is 30%"; i5695 p. 2 "a credit equal to 30% of the sum" |
| `f5695.fuel_cell_per_kw` | NonNegDollars 100000 | f5695 p. 1 line 10 "x $1,000"; i5695 p. 4 Line 10 "Multiply the kW capacity by $1,000" |
| `f5695.fuel_cell_per_half_kw` (alternative) | NonNegDollars 50000 | i5695 p. 2 "limited to $500 for each one-half kilowatt of capacity" |
| `f5695.fuel_cell_joint_cost_per_half_kw` | NonNegDollars 166700 | i5695 p. 2 Joint occupancy "$1,667 for each one-half kilowatt" (only if joint occupancy is computed) |
| `f5695.insulation_max` | NonNegDollars 120000 | f5695 p. 2 line 18b "Do not enter more than $1,200"; i5695 p. 5 Line 18a |
| `f5695.door_max` | 25000 | f5695 p. 2 line 19c "Do not enter more than $250"; i5695 p. 3 "$250 for any qualifying exterior door" |
| `f5695.doors_max` | 50000 | f5695 p. 2 line 19h "Do not enter more than $500" |
| `f5695.windows_max` | 60000 | f5695 p. 2 line 20d "Do not enter more than $600" |
| `f5695.item_max` (A/C, water heater, furnace/boiler, enabling) | 60000 | f5695 p. 3 lines 22d, 23d, 24d, 25e "Do not enter more than $600"; i5695 p. 2 "A credit limit of $600 for any qualified energy property item" |
| `f5695.audit_max` | 15000 | f5695 p. 4 line 26c "Do not enter more than $150" |
| `f5695.annual_max` | 120000 | f5695 p. 4 line 28 "Enter the smaller of line 27 or $1,200"; i5695 p. 1 Reminders "up to a maximum of $1,200" |
| `f5695.heat_pump_max` | 200000 | f5695 p. 4 line 29h "Do not enter more than $2,000"; i5695 p. 1 "separate annual credit limit of $2,000" |

These are eligibility thresholds that belong in question text or gates, not arithmetic parameters:
- battery of at least 3 kWh (line 5a)
- fuel cell of at least 0.5 kW and efficiency above 30% (i5695 p. 2)
- 80% nonbusiness use (p. 1)
- at least 5 years in use (17c)
- 200 amps (p. 7)
- biomass at least 75% thermal efficiency (p. 7)
- oil blend at least 20% (p. 6)
- half the energy from the sun (p. 2)

CLW B reuses `actc.per_child`, `actc.earned_floor`, `actc.rate` and `actc.three_children`.

#### 6. The One Big Beautiful Bill Act and the 2025 instructions

- P.L. 119-21 sec. 70505 (139 Stat. 251): section 25C(h) now reads "placed in service after December 31, 2025". The same section rewrites 25C(d)(2)(C) (oil furnace / boiler: 2021 Energy Star and a 20% eligible-fuel blend). That rewrite matches i5695 p. 6, lines 24a/24b.
- P.L. 119-21 sec. 70506 (139 Stat. 251): section 25D(h) now ends the credit "with respect to any expenditures made after December 31, 2025". 25D(g) is changed to "30 percent." for property placed in service after 2021, with the step-downs struck. The carryforward subsection 25D(c) is not touched by these sections.
- i5695 p. 1, What's New, "Termination of credits": "You can't claim residential clean energy credits for expenditures made after December 31, 2025. You can't claim energy efficient home improvement credits for expenditures or property placed in service after December 31, 2025." It also points to Fact Sheet 2025-05 (not archived).
- Effect on 2025: none on the arithmetic. 2025 expenditures and property qualify in full. The instructions still direct the Part I carryforward to 2026 (f5695 line 16; i5695 p. 5 Line 16). The only 2025 edge is timing: when an expenditure is "made" or "paid" (i5695 p. 1 "Costs"), for example new construction first occupied in 2026.
- Other 2025 changes in What's New (i5695 p. 1): QMIDs required from January 1, 2025; new line 25b (enabling/enabled relationship); new checkbox 32b (condo/co-op).

#### 7. Open questions

1. **Line 17a-c "No": the whole Part II, or only Section A?** The form says "you cannot claim the energy efficient home improvement credit. Do not complete Part II, Section A" (f5695 p. 2). The instructions say "you can't take the energy efficient home improvement credit" (i5695 p. 5). Section B has its own residence test (21a: any home used as a residence), so the narrower reading (zero Section A only) is consistent with the structure. The literal sentence reads broader. This needs an ambiguity-register entry.
2. **Line 17e "Yes".** The form permits non-construction improvements ("you can only claim ... for qualifying improvements that were not related to the construction of the home"). The instructions say "If you check the 'Yes' box, skip lines 18a through 20d" (i5695 p. 5). Does Yes zero all of Section A? Does it affect Section B, given "Part II ... is only available for existing homes" (p. 1)?
3. **Battery storage (line 5b) on a second home.** The text for lines 1-4 says "The home doesn't have to be your main home". The battery paragraph says only "installed in connection with your home located in the United States" (i5695 p. 2). The statute is not archived.
4. **Section B on a second home.** i5695 p. 3 and line 21a say "a home that you used during 2025 / use as a residence". But i1040gi p. 116 (line 5b) describes the credit only as improvements "to your main home", and i5695 p. 5 Line 17d says "You can only claim the energy efficient home improvement credit on one main home". Line 21c asks for "each home". The caller's premise that Part II does not allow second homes holds for Section A and audits only. For Section B the archived text points the other way.
5. **The per-item $600 cap vs the form's category cap.** i5695 p. 2 says "A credit limit of $600 for any qualified energy property **item**". Lines 22d, 23d, 24d and 25e cap the whole category total at $600. The joint-occupancy list (p. 3) says "$600 for central air conditioners". With two qualifying A/Cs, the item reading allows up to $1,200 before line 28. The form allows $600. Recommendation: encode the form. Record the reading.
6. **Fuel cell capacity steps.** Line 10 says kW × $1,000 and "If less than 0.5 kW, enter -0-". The instructions add "may only be claimed in half kW increments" (i5695 p. 4). Is a 1.3 kW unit rounded down to 1.0 kW? The text does not say how. Moot if fuel cells are refused.
7. **Window lines 20a vs 20b standard.** "Energy Star certification requirements" (20a) vs "Energy Star most efficient certification requirements" (20b) (i5695 p. 6). Is this a different standard, or a drafting difference? It only affects question wording.
8. **New-home timing for Part I.** Costs for constructing a home are paid "when your original use of the constructed home begins" (i5695 p. 1). Termination applies to "expenditures made after December 31, 2025" (i5695 p. 1; P.L. 119-21 sec. 70506). Is a home built in 2025 but first occupied in 2026 out? The archived text implies it is, by combining the two rules, but neither states it outright.
9. **Rebates and subsidies beyond utility subsidies.** Only public-utility subsidies are addressed (i5695 p. 2), with a pointer to Fact Sheet 2025-01, which is not archived. The treatment of state or IRA rebate programs is undecided in the archived text. Archive FS-2025-01 and FS-2025-05 before writing the cost question.
10. **QMID representation.** The data model has no strings (spec 4.2). An attestation Bool per category is the likely form. Should "no QMID" exclude the item (compute) or refuse? The text says "you must provide a valid QMID for each item" (i5695 p. 5) but does not state the consequence beyond qualification.
11. **Insulation QMID.** Line 18 asks for no QMID, and What's New says "for each item" of "specified property". The archived text never defines "specified property". The p. 3 statements limit the requirement to doors, windows, skylights and Section B property. Recommendation: no attestation on 18 and 26.
12. **CLW B line 3 source.** CLW B line 3 cites the Earned Income Worksheet line 7 (`s8812.eiw_7`). The existing ACTC path uses line 18a through the Earned Income Chart, which for EIC takers uses EIC Worksheet B amounts. Confirm whether CLW B should read `eiw_7` even for EIC takers. The worksheet's "Before you begin: Complete the Earned Income Worksheet" says it should.
13. **`scope.credits` refusal label.** The label lists Schedule 3 lines 2 to 4, 5b, 6d, 6f, 6l and 6m but not 5a, although the question covers 5a (`forms/2025/scope.yaml`, `forms/2025/s3.yaml`). This is cosmetic, and narrowing in T-048 replaces it anyway.
14. **Source pinning.** f5695 and i5695 were fetched from the current-year `irs-pdf` address. The instructions are dated Jan 22, 2026 and the form says "Created 3/20/25". Confirm these are the final 2025 revisions and record them. (Revision status in the manifest: "content review is tracked separately in PREMISES.md".)

## Stage 16 premise map — the remaining Schedule 1 items

Status: **owner decisions taken 2026-10-22** (TASKS.md T-053). The map is `research/premises/stage16-schedule1-misc.md`,
its adversarial verification `stage16-schedule1-misc.verification.md` (6 errors, 7 items out of date after Stage 15),
and the decision batch, written from both, `stage16-schedule1-misc.decisions.md`: the owner accepted D1 to D14 as
recommended. Where the map and its verification differ, the verification's checked facts govern.

