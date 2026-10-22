> **Status: draft for the owner (2026-10-22).** Written by a read-only research agent from the archived
> sources in `sources/2025/`, before the stage it maps; its decision batch is a draft and nothing in it is
> decided. Every claim carries a locator and is testimony until checked again at authoring. Spot-checked by the integrating session: the coverage figures against reports/2025/filer_coverage.md. The IRA deduction and social security worksheet cycle was confirmed by the verification (i1040gi p. 97, IRA Deduction Worksheet line 3 reads Form 1040 line 9).
> **Verified after Stage 15:** see `stage16-schedule1-misc.verification.md` (6 errors, 7 items out of date), which supersedes this map where they differ.

# Stage 16 premise map: the remaining Schedule 1 income and adjustments (coverage group `schedule1_misc`)

Read-only research for spec 2.4 roadmap item 2, written by a research agent (Claude Code) on 2026-10-22 from the archived snapshots in `sources/2025/` and the repository at commit 6051ec0 (main). Nothing in the repository was edited; no model was called; no network. Stage 15 (Forms 8880, 2441, 5695) is treated as landed; its worktrees were not read, so where this map names a Stage 15 line it names it by role, not by id.

Locator convention: `doc p. N, heading, "quote"`, where page N is the N-th form-feed chunk of `<doc>.cols.txt` (the layout `<doc>.txt` was used to read worksheet layout where the column text interleaves). Proposed interview wording and project YAML are given in single quotes or backticks, never in double quotes; double quotes are source text.

---

## 1. Scope

### 1.1 Categories and gates the stage retires

All twelve categories of group `schedule1_misc` in `tools/coverage/categories.json`. Ten are refused today by `scope.schedule1` (forms/2025/scope.yaml), one (`hsa_distribution`) by `f8889.unsupported`, one (`foreign_earned_income`) by `sa.excluded_income`.

Shares: from `reports/2025/filer_coverage.md` (checked against the file). Gains: recomputed for this map by running `tools/coverage/estimate.py`'s own functions (raking, `covered`) on the pinned microdata with the cache redirected to `/tmp`; the run reproduces the report (58.0% now, +6.7 for the group alone, 65.3% after Stage 15's group). 'Alone' is the gain from covering only that category; 'last' is the gain from covering it after every other category in the group; both are after the Stage 15 group (`other_credits`) is treated as covered.

| Category | Gate today | Share of returns | IRS returns (2023) | Basis | Gain alone | Gain last |
|---|---|---|---|---|---|---|
| Other income (Sch. 1 line 8z and similar) | scope.schedule1 | 4.85% | 7,787,273 | IRS + microdata | +2.26 | +2.52 |
| Taxable state or local refund | scope.schedule1 | 1.94% | 3,109,096 | IRS + microdata | +0.99 | +1.14 |
| IRA deduction | scope.schedule1 | 1.56% | 2,503,934 | IRS + microdata | +1.00 | +1.12 |
| Gambling winnings | scope.schedule1 | 1.44% | 2,304,901 | IRS only (independence) | +0.95 | +1.05 |
| Sales of business property (Form 4797) | scope.schedule1 | 1.07% | 1,720,509 | IRS only | +0.71 | +0.78 |
| Net operating loss deduction | scope.schedule1 | 0.63% | 1,019,019 | IRS only | +0.42 | +0.46 |
| Penalty on early withdrawal of savings | scope.schedule1 | 0.56% | 904,938 | IRS only | +0.37 | +0.41 |
| Taxable HSA distributions | f8889.unsupported | 0.29% | 464,689 | IRS only | +0.19 | +0.21 |
| Foreign earned income exclusion | sa.excluded_income | 0.27% | 432,724 | IRS only | +0.18 | +0.20 |
| Cancellation of debt | scope.schedule1 | 0.24% | 386,021 | IRS only | +0.16 | +0.18 |
| Alimony paid | scope.schedule1 | 0.17% | 278,541 | IRS + microdata | +0.08 | +0.11 |
| Alimony received | scope.schedule1 | 0.11% | 183,582 | IRS + microdata | +0.04 | +0.04 |

Whole group, after Stage 15: 65.32% to 73.10% (+7.78). Greedy order within the group: other income (67.58), state refund (68.64), IRA deduction (69.72), gambling (70.73), Form 4797 (71.50), NOL (71.95), early withdrawal (72.36), HSA (72.57), FEIE (72.77), COD (72.94), alimony paid (73.05), alimony received (73.10).

Cautions on these numbers (inference, not measured):

- The IRS-only categories are combined as independent of everything else. Form 4797, NOL and COD plausibly co-occur with Schedule C, E and F (business property, business losses), so their real gains are probably smaller than shown.
- "Other income" is the SOI column `Other income / Net income` (soi-23in14ar column 91, 7,468,434 returns) plus `Net loss` (column 93, 318,839). The archived table has no footnote saying which Schedule 1 lines it holds; it is presumably line 8 less the items SOI tabulates separately (NOL, gambling, COD, HSA, FEIE). It therefore mixes trivial inputs (Alaska Permanent Fund dividends, jury duty, prizes) with items this map recommends refusing (8k stock options, 8l personal-property rental, 8n to 8p, 8q, 8s, 8v). The +2.3 is an upper bound for any partial treatment, and the estimator cannot measure a partial one.
- Stage 15's own refusals (traditional IRA contributions on Form 8880, other nonrefundable credits) are not in the 'after Stage 15' baseline, which treats the whole `other_credits` group as covered.

### 1.2 Recommended scope

Compute (in order of gain), with screens for the hard sub-cases listed in section 6:

1. **Other income, a named subset of line 8**: 8b, 8c and 8f (items 4, 7 and 8 below), 8g Alaska Permanent Fund dividends, 8h jury duty pay (with line 24a), 8i prizes and awards, 8j activity not engaged in for profit income, 8r scholarship and fellowship grants not on Form W-2, and 8z for a closed list of plain kinds. Everything else on line 8 stays refused. 2. **Line 1, taxable state or local income tax refund**, by the i1040gi worksheet only (Pub. 525 Worksheet 2 refused). 3. **Line 20, the IRA deduction**, by the i1040gi worksheet, with Form 8606 Part I for nondeductible contributions in the no-distribution case (lines 1 to 3 and 14), and the change to Form 8880 line 1 (section 5.3). 4. **Line 8b gambling winnings**, with gambling losses on Schedule A line 16. 5. **Line 18, early withdrawal penalty** (Form 1099-INT box 2), with Form 8960 line 10. 6. **Lines 2a and 19a, alimony** received and paid (pre-2019 agreements). 7. **Line 8f taxable HSA distributions**, with the 20% additional tax on Schedule 2 line 17c. 8. **Line 8c canceled debt**, fully taxable nonbusiness debt only.

Leave refused: **Form 4797** (line 4; sources not archived, depreciation recapture, section 1231, and the EIC and QBI paths read it), **the NOL deduction** (line 8a; Form 172 and its carryover computation are not archived, and an NOL changes the section 1411 computation, i8960 p. 13, Line 7, "Section 1411 NOL"), and **the foreign earned income exclusion** (line 8d; Form 2555 and the Foreign Earned Income Tax Worksheet are not archived, and `sa.excluded_income` already refuses its MAGI add-backs in Schedule A, Schedule 8812 and Form 8880).

Estimated effect (same method): the recommended set takes coverage from 65.32% to 71.66% (+6.34), against 73.10% for the whole group; the three refused categories together are worth +1.31. The four largest alone (other income, state refund, IRA, gambling) give 70.73% (+5.41). Without other income the rest gives +3.87.

Reasoning: the owner's Stage 15 decisions refuse rare-and-hard and compute common situations. The three refusals are the categories whose computation needs a form that is not archived and that reaches the business, investment-income and foreign-exclusion paths at once. The four small computed categories (early withdrawal, alimony, HSA, COD) are each a few lines on top of existing structure, which is why they are recommended despite their size; any of them can move to "refuse" without affecting the others (decision batch D2).

---

## 2. Sources

### 2.1 Archived, used

| id | document | revision (manifest) | used for |
|---|---|---|---|
| i1040gi | Form 1040 instructions | 2025; printed 2026-02-25 | Schedule 1 instructions pp. 88-100, refund worksheet p. 90, IRA worksheet pp. 97-98, SSB exception p. 31 |
| f1040s1 | Schedule 1 | 2025; created 2025-07-25 | line texts |
| p525 | Pub. 525 | 2025 | recoveries pp. 24-28, other income items pp. 20, 31-35 |
| p590a | Pub. 590-A | 2025 | compensation pp. 6-7, limits pp. 9-11, coverage pp. 12-13, Tables 1-2 and 1-3 p. 14, MAGI pp. 14-16, Appendix B p. 54 |
| p590b | Pub. 590-B | 2025 | Worksheet 1-1 p. 17 (only to confirm the refusal of contributions plus distributions with basis) |
| f8606, i8606 | Form 8606 and instructions | 2025 | Part I; who must file; line 1 and 2 instructions |
| f1099g | Form 1099-G | Rev. March 2024 | boxes 2, 3, 8 |
| f1099int, i1099int | Form 1099-INT and instructions | January 2024 | box 2 |
| p529 | Pub. 529 | Rev. December 2020 | gambling losses p. 10 (old revision; testimony only) |
| i1040sca | Schedule A instructions | 2025 | line 16 gambling losses p. 11 |
| f8889, i8889 | Form 8889 and instructions | 2025 | Part II |
| f1040s2 | Schedule 2 | 2025 | lines 17c, 18, 21 |
| i8960 | Form 8960 instructions | 2025 | line 10 note, deduction recoveries |
| f5329 | Form 5329 | 2025 | Part III (excess contributions, refused) |
| f8880 | Form 8880 | 2025 | line 1 |
| soi-23in14ar | SOI Table 1.4 | TY2023 | category counts |

p463 was named in the task; nothing in this stage reads it (it bears on line 12, reservists' travel, which stays refused).

### 2.2 Needed and not archived (URLs given, nothing fetched)

| Document | URL | What is lost without it |
|---|---|---|
| Form W-2G, Certain Gambling Winnings | https://www.irs.gov/pub/irs-pdf/fw2g.pdf | The box definitions the interview would cite (box 1 gross winnings, box 4 federal tax withheld, box 7 winnings from identical wagers, noncash prizes), and the recipient instructions. The only archived statements are p525 p. 33 ("Include the amount from box 1 on Schedule 1 (Form 1040), line 8b. Include the amount shown in box 4 on Form 1040 or 1040-SR, line 25c, as federal income tax withheld.") and i1040gi p. 39 line 25c ("Federal income tax withheld on your Form(s) W-2G. The amount withheld should be shown in box 4."). The interview can cite those; it cannot cite the form's own box text or the thresholds below which no W-2G is issued, and the help cannot say what box 7 means. |
| Instructions for Forms W-2G and 5754 | https://www.irs.gov/pub/irs-pdf/iw2g.pdf | Same; payer-side, lower priority. |
| Pub. 504, Divorced or Separated Individuals | https://www.irs.gov/pub/irs-pdf/p504.pdf | What counts as alimony (cash, not child support, not property settlement), the recapture rule, the statements for more than one agreement. i1040gi pp. 89 and 95 send the filer there. |
| Pub. 4681, Canceled Debts | https://www.irs.gov/pub/irs-pdf/p4681.pdf | Exclusions (insolvency, bankruptcy, qualified principal residence), foreclosure. Needed only to word the COD screen. |
| Form 982 and instructions | https://www.irs.gov/pub/irs-pdf/f982.pdf, https://www.irs.gov/pub/irs-pdf/i982.pdf | Only to name the refused form precisely. |
| Form 1099-C and instructions | https://www.irs.gov/pub/irs-pdf/f1099c.pdf, https://www.irs.gov/pub/irs-pdf/i1099ac.pdf | Box 2 and box 3 text for the COD input (p525 p. 20 quotes both). |
| Form 5498, IRA Contribution Information | https://www.irs.gov/pub/irs-pdf/f5498.pdf | Help text naming the box that shows traditional contributions (i1040gi p. 95 says only "A statement should be sent to you by June 1, 2026, that shows all contributions to your traditional IRA for 2025."). |
| Form 1099-MISC and instructions | https://www.irs.gov/pub/irs-pdf/f1099msc.pdf, https://www.irs.gov/pub/irs-pdf/i1099mec.pdf | Box 3 (other income: prizes, awards), the usual source of 8i. |
| Form 1099-SA | https://www.irs.gov/pub/irs-pdf/f1099sa.pdf | Box 1 and distribution codes for Form 8889 line 14a (i8889 p. 8 says "These amounts should be shown on Form 1099-SA, box 1"). |
| For the refusals only (not needed to build): Form 4797 and instructions, Form 2555 and instructions, Pub. 54, Form 172 and instructions, Pub. 536 | https://www.irs.gov/pub/irs-pdf/f4797.pdf, i4797.pdf, f2555.pdf, i2555.pdf, p54.pdf, f172.pdf, i172.pdf, p536.pdf | Nothing in this stage. |

The 2024 Form 1040 instructions are not needed: the refund worksheet prints the 2024 standard deduction amounts itself (i1040gi p. 90, line 5 and line 6).

---

## 3. Line map

### 3.1 How the project encodes this (facts checked in the repository)

- `s1.line10` is `sum(s1.line3, s1.line7)` and `s1.line26` is `sum(s1.line11, 13, 15, 16, 17, 21)` (forms/2025/s1.yaml). Every other Schedule 1 line is refused by `scope.schedule1` through `f1040.line8` and `f1040.line10`, both of which copy the Schedule 1 totals and carry the refusal (forms/2025/f1040.yaml).
- Readers of Schedule 1 adjustments that list lines by number: `sli.line3` (sum of 11, 13, 15, 16, 17; its cite says lines 12, 14 and 18 to 20, 23 and 25 are refused) and `ssb.line6` (same sum, with its own `scope.schedule1` refusal).
- `scope.schedule1` is also the trigger of refusals whose reasons are not this stage's: `eic.step2_other` (Schedule E, rental of personal property, passive activity), `eic.step5_line1` and `eic.clergy` (clergy, church and statutory employees), `s8812.eiw_3` (statutory employee, farm, partnership), `s8812.eiw_4` (line 8s Medicaid waiver payments), two Schedule 1-A refusals in `s1a.yaml` (qualified tips in a trade or business with Schedule E or F; qualified overtime reported on Form 1099-NEC box 1 or 1099-MISC box 3) and the `carloan` column (ii) note. See section 5.5.
- `interest` (forms/2025/interest.yaml) has one input per payer, `interest.amount`; Form 1099-INT box 2 is not modelled.
- `sa.line16` is `copy sa.zero`, refused when `sa.unsupported`, whose question includes 'a deduction from the Schedule A line 16 list' (forms/2025/sa.yaml).
- `f8960.line10` is `copy f8960.zero` (forms/2025/f8960.yaml). `f8960.refund` refuses any recovery of an amount deducted on an earlier Form 8960.
- `f1040.line25c` is a supplied total, 'Federal income tax withheld from other forms (supplied total)'.
- `f8889.unsupported` refuses 'HSA distributions in 2025 that were not all used for qualified medical expenses or rolled over' together with five unrelated situations. Form 8889 Part II is not encoded.
- `s2.other` refuses every Schedule 2 amount other than SE tax, Additional Medicare Tax and NIIT, including 'the additional tax on early retirement or HSA distributions'.
- W-2 entries model boxes 1 to 7 only (w2.yaml); box 11, box 12 and box 13 are not modelled.
- `retirement` (one entry per Form 1099-R) is return-level with no owner; `retirement.special` refuses an entry involving 'nondeductible contributions to any traditional IRA' or 'a conversion or recharacterization (Form 8606)'.
- Status-keyed parameters resolve only by the current return's `f1040.status` (engine/src/eval.ts, comment `Status-keyed: resolve by the return's filing status`). A table keyed by a prior-year status must be a `keyed_lookup`.
- The checker's cycle walk is structural: it follows every operand, including every `choose` guard and branch (engine/src/check.ts, `checkCycles`). A cycle that no evaluation can reach is still a build error. This matters for the IRA deduction and the social security worksheet (section 5.2).

### 3.2 Schedule 1, Part I (f1040s1 p. 1)

| Line | Printed text | Computes | Supply | New inputs (collection) |
|---|---|---|---|---|
| 1 | "Taxable refunds, credits, or offsets of state and local income taxes" | refund worksheet line 9 (3.3) | none | return-level, 3.3 |
| 2a | "Alimony received" | input total | none | return: alimony received under pre-2019 agreements |
| 2b | "Date of original divorce or separation agreement (see instructions):" | not a number | n/a | not representable (no strings, `Date` is for holding periods only); see Q12 |
| 3 | "Business income or (loss). Attach Schedule C" | existing `s1.line3` | Stage 14 | none |
| 4 | "Other gains or (losses). Check if any from Form(s): 4797 4684" | refused | n/a | n/a |
| 5, 6 | Schedule E, Schedule F | refused (later stages) | n/a | n/a |
| 7 | "Unemployment compensation" | existing | Stage 11 | none |
| 8a | "Net operating loss" | refused | n/a | n/a |
| 8b | "Gambling" | input total | none | return: winnings (W-2G box 1 plus winnings with no W-2G) |
| 8c | "Cancellation of debt" | input total | none | return: taxable canceled nonbusiness debt (1099-C box 2), screened |
| 8d | "Foreign earned income exclusion from Form 2555" | refused | n/a | n/a |
| 8e | "Income from Form 8853" | refused | n/a | n/a |
| 8f | f1040s1 p. 1, "Income from Form 8889" | sum over person of Form 8889 line 16 (line 20, Part III, stays refused) | f8889 (per person) | Form 8889 lines 14a, 14b, 15, 17a (3.7) |
| 8g | "Alaska Permanent Fund dividends" | input | none | return (or person; Q13) |
| 8h | "Jury duty pay" | input | none | return |
| 8i | "Prizes and awards" | input | none | return; 8m Olympic medals refused |
| 8j | "Activity not engaged in for profit income" | input | none | return |
| 8k, 8l, 8m, 8n, 8o, 8p, 8q | stock options; personal property rental; Olympic and Paralympic medals; 951(a); 951A(a); 461(l); ABLE | refused | n/a | n/a |
| 8r | "Scholarship and fellowship grants not reported on Form W-2" | input | none | return; see Q9 on IRA compensation |
| 8s | "Nontaxable amount of Medicaid waiver payments included on Form 1040, line 1a or 1d" | refused (as today) | n/a | n/a |
| 8t, 8u, 8v | nonqualified deferred compensation; wages while incarcerated; digital assets | refused | n/a | n/a |
| 8z | "Other income. List type and amount:" | sum of supported kinds | none | a collection keyed by an enum of supported kinds, or one total; Q11 |
| 9 | "Total other income. Add lines 8a through 8z" | sum of the computed 8 lines | new | none |
| 10 | "Combine lines 1 through 7 and 9. This is your additional income." | becomes sum(1, 2a, 3, 7, 9) | `s1.line10` changes | none |

Supporting text for line 8 items:

- i1040gi p. 91, Line 8b, "Enter gambling winnings not attributable to a trade or business. Gambling winnings include lotteries, raffles, a lump-sum payment from the sale of a right to receive future lottery payments, etc."
- i1040gi p. 91, Line 8c, "Enter any canceled debt. Canceled debt may be shown in box 2 of Form 1099-C. However, part or all of your income from cancellation of debt may be nontaxable. See Pub. 4681".
- i1040gi p. 91, Line 8f, "Enter the total of the amounts from Form 8889, lines 16 and 20."
- i1040gi p. 91, Line 8h, "Enter any jury duty pay and see the instructions for line 24a." and i1040gi p. 99, Line 24a, "Enter your jury duty pay if you gave the pay to your employer because your employer paid your salary while you served on the jury."
- i1040gi p. 91, Line 8i, "Enter prizes and awards but see the instructions for line 8m".
- p525 p. 31, Alaska Permanent Fund dividend, "report it as income on Schedule 1 (Form 1040), line 8g".
- i1040gi p. 92, Line 8r, "if you were a degree candidate, include on line 8r only the amounts you used for expenses other than tuition and course-related expenses."
- i1040gi p. 92, Line 8z, "Use line 8z to report any taxable income not reported else-where on your return or other schedules. List the type and amount of income." The examples listed there include recoveries ("See Recoveries in Pub. 525 for details on how to figure the amount to report"), RTAA payments ("These payments should be shown in box 5 of Form 1099-G"), corrective distributions, insurance dividends, charitable recaptures, disaster relief and Coverdell or QTP distributions.
- i1040gi p. 89, Lines 8a Through 8z, Caution: "Do not report on lines 8a through 8z any income from self-employment or fees re- ceived as a notary public. Instead, you must use Schedule C, even if you don’t have any business expenses."

### 3.3 State and Local Income Tax Refund Worksheet (i1040gi p. 90), return-level

| Wks line | Printed text (i1040gi p. 90) | Computes | Supply | New inputs |
|---|---|---|---|---|
| 1 | "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d" | `smaller_of(refund, 2024 5d)` | none | refund received in 2025 for 2024 (Form 1099-G box 2, all forms); 2024 Sch. A line 5d (Q2) |
| 2 | "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" No: line 3 = line 1. Yes: subtract 5e from that amount. | `subtract_floor0(5d paid, 5e)` (zero on No) | none | 2024 Sch. A line 5e; the paid amount (Q3) |
| 3 | "Is the amount on line 1 more than the amount on line 2?" No: "None of your refund is taxable." Yes: "Subtract line 2 from line 1." | `subtract_floor0(line1, line2)` | n/a | n/a |
| 4 | "Enter your total itemized deductions from your 2024 Schedule A, line 17." | input | none | 2024 Sch. A line 17 |
| Note | "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7, enter the amount from line 4 on line 8, and go to line 9." | guard on line 8 | none | 2024 filing status (enum); 'did your spouse itemize in 2024' (only when 2024 was MFS) |
| 5 | "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR." "Single or married filing separately—$14,600" "Married filing jointly or qualifying surviving spouse—$29,200" "Head of household—$21,900" | `keyed_lookup` on the 2024 status | none | 2024 status |
| 6 | "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)." Boxes: "You were born before January 2, 1960." "You are blind." "Spouse was born before January 2, 1960." "Spouse is blind." | `multiply_count(keyed_lookup per-box amount, count)` | none | a Count of boxes, or four 2024 Bools (Q4); MFS footnote |
| 7 | "Add lines 5 and 6" | sum | n/a | n/a |
| 8 | "Is the amount on line 7 less than the amount on line 4?" No: none taxable. Yes: "Subtract line 7 from line 4" | `subtract_floor0(line4, line7)`, or line 4 under the MFS note | n/a | n/a |
| 9 | "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1" | `smaller_of(line3, line8)` | n/a | n/a |

Footnote to line 6: i1040gi p. 90, "If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return."

Gate before the worksheet: i1040gi p. 88, "If the refund was for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A, use the State and Local Income Tax Refund Worksheet in these instructions to see if any of your refund is taxable." When the filer did not itemize in 2024, or deducted sales taxes, line 1 of Schedule 1 is zero: i1040gi p. 88, Line 1, "None of your refund is taxable if, in the year you paid the tax, ... you either (a) didn’t itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes." The sales-tax branch is capped, not zeroed, by Pub. 525 (section 4.2, exception 4).

### 3.4 IRA Deduction Worksheet (i1040gi pp. 97-98), columns per person

Columns are "Your IRA" and "Spouse’s IRA" (i1040gi p. 97). Natural encoding: lines 1, 2, 6, 7, 11, 12 per person on `person` (or a new person-bound definition); lines 3, 4, 5, 8, 9, 10 return-level (line 5 is "If married filing jointly, enter the result in both columns"); Schedule 1 line 20 = `sum_over person` of line 12. A column needs to know whether the *other* spouse is covered; that goes through a return-level count of covered persons (an entry cannot read another entry, spec 4.4).

| Wks line | Printed text | Computes | Supply | New inputs |
|---|---|---|---|---|
| 1a / 1b | "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" / "If married filing jointly, was your spouse covered by a retirement plan?" | per-person Bool | `person.plan` (SEP or SIMPLE through self-employment counts as covered, i1040gi p. 96) | per person: covered at work (W-2 box 13, or a question), Q6 |
| Next | "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8." "$7,000 if under age 50 at the end of 2025." "$8,000 if age 50 or older at the end of 2025." | `choose` on (no one covered) | n/a | per person: age 50 or older at the end of 2025 (Q5) |
| 2 | i1040gi p. 97: "Single, head of household, or married filing separately and you lived apart from your spouse for all of 2025, enter $89,000." "Qualifying surviving spouse, enter $146,000." "Married filing jointly, enter $146,000 in both columns. But if you checked “No” on either line 1a or 1b, enter $246,000 for the person who wasn’t covered by a plan." | per person `choose` by status and own coverage | `f1040.status` | none (MFS refused project-wide) |
| 3 | i1040gi p. 97: "Enter the amount from Form 1040 or 1040-SR, line 9" | copy `f1040.line9` (but see 5.2) | existing | none |
| 4 | "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25" | sum(s1.line11, 13, 15, 16, 17, 18, 19a) | lines 12, 14, 23, 25 refused | none |
| 5 | "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns" | `subtract` | n/a | n/a |
| 6 | "Is the amount on line 5 less than the amount on line 2?" No: "None of your IRA contributions are deductible." Yes: "Subtract line 5 from line 2 in each column." | per person `subtract_floor0(line2, line5)` | n/a | n/a |
| 6, full-limit rule | "If single, head of household, or married filing separately, and the result is $10,000 or more, enter the applicable amount below on line 7 for that column and go to line 8." "If married filing jointly or qualifying surviving spouse, and the result is $20,000 or more ($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan)" | see line 7 | n/a | n/a |
| 7 | "If the result isn’t a multiple of $10, increase it to the next multiple of $10 (for example, increase $490.30 to $500). If the result is $200 or more, enter the result. But if it is less than $200, enter $200." Rates: "Single, head of household, or married filing separately, multiply by 70% (0.70) (or by 80% (0.80) in the column for the IRA of a person who is age 50 or older at the end of 2025)." "Married filing jointly or qualifying surviving spouse, multiply by 35% (0.35) (or by 40% (0.40) in the column for the IRA of a person who is age 50 or older at the end of 2025)." and "then in the column for the IRA of the person who wasn’t covered by a retirement plan, multiply by 70% (0.70) (or by 80% (0.80) if age 50 or older at the end of 2025)" | per person: `multiply_rate` in each rate branch, `round` up to 1000 cents, `larger_of` $200, `smaller_of` the age limit, `choose` among branches; zero when line 6 is No | n/a | n/a |
| 8 | i1040gi p. 98: "Wages, salaries, tips, etc. Generally, this is the amount reported in box 1 of Form W-2." Also "Alimony and separate maintenance payments reported on Schedule 1, line 2a." and "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q or reported on Form 1040, line 1i." | return-level sum: W-2 box 1 of both spouses + `s1.line2a` (+ combat pay, refused) | `person.box1` per person, `f1040.line1a` | box 11 or code Z amounts (refuse, Q8) |
| 9 | "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner." "minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-." | per person `person.sc_total` less `person.se_line13` less `person.s16`, summed; floor (Q7) | Stage 14 lines | none |
| 10 | "Add lines 8 and 9" | sum | n/a | n/a |
| Caution | "If married filing jointly and line 10 is less than $14,000 ($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025), stop here and use the worksheet in Pub. 590-A to figure your IRA deduction." | gate, refusal | n/a | n/a |
| 11 | "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b" | per-person input | none | per person: traditional IRA contributions for 2025 |
| 12 | "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct." and "Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606)" | per person: two `smaller_of` | n/a | the election to deduct less (Q10) |
| Sch. 1 20 | "IRA deduction. If you are married filing separately and lived apart from your spouse for the entire year (see instructions), check here" | `sum_over person` line 12 | n/a | checkbox is MFS only (refused) |

Before-you-begin text (i1040gi p. 97): "If the instructions for Schedule 1, line 24z, have you enter a write-in adjustment on line 24z, figure that write-in before completing this worksheet". i1040gi p. 100, Line 24z, says "Leave line 24z blank.", so nothing is needed.

Cross-check with Pub. 590-A (p590a p. 14, Table 1-2 and Table 1-3): covered, single or head of household, full deduction at "$79,000 or less", none at "$89,000 or more"; covered, joint or qualifying surviving spouse, "$126,000 or less" and "$146,000 or more"; not covered but spouse covered, "$236,000 or less" and "$246,000 or more". The worksheet's line 2 amounts are the upper ends and its $10,000 and $20,000 thresholds are the widths; this agreement is a property test, not a parameter. p590a p. 16 confirms the worksheet can be used: "The Instructions for Form 1040 include a similar worksheet that you can use instead of the worksheet in this publication."

Property check (inference from the arithmetic): at the full-limit thresholds the line 7 product equals the limit ($10,000 times 70% is $7,000; times 80% is $8,000; $20,000 times 35% is $7,000; times 40% is $8,000), so encoding line 7 as `smaller_of(limit, larger_of(roundup(product), $200))` agrees with the printed "enter the applicable amount" branch.

### 3.5 Form 8606 Part I, nondeductible contributions only (f8606 p. 1), per person

i8606 p. 8: "If both you and your spouse are required to file 2025 Form 8606, file a separate 2025 Form 8606 for each of you." A per-person form.

| Line | Printed text | Computes | Supply |
|---|---|---|---|
| 1 | f8606 p. 1: "Enter your nondeductible contributions to traditional IRAs for 2025, including those made for 2025 from January 1, 2026, through April 15, 2026." | i8606 p. 9, Line 1: "If you used the IRA Deduction Worksheet in the Form 1040 instructions or as referred to in the Form 1040-NR instructions, subtract line 12 of the worksheet (or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less) from the smaller of line 10 or line 11 of the worksheet." So `subtract_floor0(smaller_of(wks line10, own line11), own line12)`. | IRA worksheet |
| 2 | f8606 p. 1: "Enter your total basis in traditional IRAs." | input; i8606 p. 9, "Generally, if this is the first year you are required to file Form 8606, enter -0-. Otherwise, use the Total Basis Chart to find the amount to enter on line 2." | new per-person input |
| 3 | "Add lines 1 and 2" | sum | n/a |
| question | "In 2025, did you take a distribution ... from a traditional IRA, or make a ... Roth IRA conversion?" No: "Enter the amount from line 3 on line 14." "Do not complete the rest of Part I." | gate: Yes is refused (5.2, R-IRA-8) | `retirement.special` already refuses such entries when basis exists |
| 14 | "Subtract line 13 from line 3. This is your total basis in traditional IRAs for 2025 and earlier years" | on the No path, copy line 3 (display) | n/a |

Lines 4 to 13 (the pro-rata nontaxable part of distributions) are out of scope: they need the person's own traditional IRA distributions and year-end value, and `retirement` entries have no owner.

Filing requirement (i8606 p. 2, Who Must File): "You made nondeductible contributions to a traditional IRA for 2025." Penalty if omitted (i8606 p. 8): "If you are required to file Form 8606 to report a nondeductible contribution to a traditional IRA for 2025 but don’t do so, you must pay a $50 penalty, unless you can show reasonable cause." The form is needed whenever line 1 is above zero, including for a filer with no deduction at all (p590a p. 16, Example: covered, MAGI $90,000, "you can’t deduct your $7,000 IRA contribution").

### 3.6 Part II lines other than 20 (f1040s1 p. 2)

| Line | Printed text | Computes | Supply | New inputs |
|---|---|---|---|---|
| 18 | "Penalty on early withdrawal of savings" | `sum_over interest` of a new per-payer box 2 input | none | per interest entry: Form 1099-INT box 2 (i1040gi p. 95, "The Form 1099-INT or Form 1099-OID you received will show the amount of any penalty you were charged.") |
| 19a | "Alimony paid" | input | none | return: alimony paid under pre-2019 agreements |
| 19b | "Recipient’s SSN" | not representable | n/a | Q12 |
| 19c | "Date of original divorce or separation agreement (see instructions):" | not representable | n/a | Q12 |
| 24a | "Jury duty pay (see instructions)" | input, at most line 8h (Q14) | none | return |
| 25 | "Total other adjustments. Add lines 24a through 24z" | sum (24a only) | new | none |
| 26 | "Add lines 11 through 23 and 25." | becomes sum(11, 13, 15, 16, 17, 18, 19a, 20, 21, 25) | `s1.line26` changes | none |

### 3.7 Form 8889 Part II (f8889 p. 1), per Form 8889 (per person)

| Line | Printed text | Computes | New inputs |
|---|---|---|---|
| 14a | f8889 p. 1: "Total distributions you received in 2025 from all HSAs (see instructions)" | input | per Form 8889 (i8889 p. 8, Line 14a, "These amounts should be shown on Form 1099-SA, box 1.") |
| 14b | "Distributions included on line 14a that you rolled over to another HSA. Also include any excess contributions (and the earnings on those excess contributions) included on line 14a that were withdrawn by the due date of your return." | input | per Form 8889 |
| 14c | "Subtract line 14b from line 14a" | `subtract_floor0` | n/a |
| 15 | "Qualified medical expenses paid using HSA distributions (see instructions)" | input | per Form 8889 |
| 16 | "Taxable HSA distributions. Subtract line 15 from line 14c. If zero or less, enter -0-. Also, include this amount in the total on Schedule 1 (Form 1040), Part I, line 8f" | `subtract_floor0` | n/a |
| 17a | "If any of the distributions included on line 16 meet any of the Exceptions to the Additional 20% Tax (see instructions), check here" | Bool | per Form 8889 |
| 17b | "Additional 20% tax (see instructions). Enter 20% (0.20) of the distributions included on line 16 that are subject to the additional 20% tax. Also, include this amount in the total on Schedule 2 (Form 1040), Part II, line 17c" | `multiply_rate` of the part subject | the part subject (Q15) |

Schedule 2 (f1040s2): "Additional tax on HSA distributions. Attach Form 8889" (17c), "Total additional taxes. Add lines 17a through 17z" (18), and line 21, which adds line 18. All three are new in `s2.yaml`.

---

## 4. Rules

### 4.1 IRA deduction

- Who can deduct. i1040gi p. 95, Line 20: "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction. But you, or your spouse if filing a joint return, must have had earned income to do so." Also "You are entitled to a deduction for your contribution to a tradi- ... tional IRA regardless of age" (the column text breaks the word around a TIP marker).
- Compensation. p590a p. 6, What Is Compensation?: "The IRS treats as compensation any amount properly shown in box 1 (Wages, tips, other compensation) of Form W-2, Wage and Tax Statement, provided that amount is reduced by any amount properly shown in box 11 (Nonqualified plans)." p590a p. 7, "Self-employment loss. If you have a net loss from self-employment, don’t subtract the loss from your salaries or wages when figuring your total compensation." p590a p. 7, Alimony: "compensation includes any taxable alimony and separate maintenance payments you receive under a decree of divorce or separate maintenance but only with respect to divorce or separation instruments executed on or before December 31, 2018". p590a p. 6: "However, for tax years beginning after 2019, certain non-tuition fellowship and stipend payments not reported to you on Form W-2 are treated as taxable compensation for IRA purposes." The i1040gi worksheet line 8 does not list these fellowship payments (Q9).
- The limit. p590a p. 9, General Limit: "For 2025, the most that can be contributed to your traditional IRA is generally the smaller of the following amounts." i8606 p. 5, Overall Contribution Limit: "If you aren’t married filing jointly, your limit on contributions to traditional and Roth IRAs is generally the smaller of $7,000 ($8,000 if age 50 or older at the end of 2025) or your taxable compensation (defined below)." The limit is shared with Roth contributions, which Stage 15 already asks for (Form 8880 line 1).
- Spousal limit. p590a p. 10, Kay Bailey Hutchison Spousal IRA Limit: "This means that the total combined contributions that can be made for the year to your IRA and your spouse's IRA can be as much as $14,000 ($15,000 if only one of you is age 50 or older, or $16,000 if both of you are age 50 or older)." The worksheet's line 10 caution sends couples below those totals to Pub. 590-A.
- Coverage. i1040gi p. 96: "The “Retirement plan” box in box 13 of your Form W-2 should be checked if you were covered by a plan at work even if you weren’t vested in the plan." and "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan." p590a p. 12: "If you aren’t certain whether you were covered by your employer's retirement plan, you should ask your employer." p590a p. 13: "Coverage under social security or railroad retirement isn’t coverage under an employer retirement plan." The plan-year rules (p590a p. 12, For Which Year(s) Are You Covered?) and the reservist and volunteer firefighter exceptions (p590a p. 13) are reasons to ask the filer rather than infer from box 13 alone (Q6).
- Items to read before the worksheet (i1040gi p. 95, numbered list): Roth not deductible; "If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don’t use the IRA Deduction Worksheet in these instructions."; "If you made contributions to your IRA in 2025 that you deducted for 2024, don’t include them in the worksheet."; nonqualified plan income "don’t include that income on line 8 of the worksheet. The income should be shown in (a) box 11 of your Form W-2, (b) box 12 of your Form W-2 with code Z, or (c) box 15 of Form 1099-MISC."; "You must file a joint return to deduct contributions to your spouse’s IRA."; "Don’t include rollover contributions in figuring your deduction."; "Don’t include any repayments of qualified reservist distributions."; and item 10, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules." (the excess-contribution case).
- Exclusions that send the filer to Pub. 590-A. i1040gi p. 96: "If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A to figure the amount, if any, of your IRA deduction." All three are already refused elsewhere (`sa.excluded_income`; Schedule B's savings bond exclusion; `scope.other_income`'s adoption benefits).
- Social security recipients. i1040gi p. 31, Lines 6a and 6b, Exception: "You made contributions to a traditional IRA for 2025 and you or your spouse were covered by a retirement plan at work or through self-employment. Instead, use the worksheets in Pub. 590-A to see if any of your social security benefits are taxable and to figure your IRA deduction." p590a p. 13, Social Security Recipients: "Instead of using Table 1-2 or Table 1-3 and Worksheet 1-2, complete the worksheets in Appendix B of this publication if, for the year, all of the following apply." Appendix B (p590a p. 54) is a parallel computation of modified AGI "without taking into account any social security benefits from Form SSA-1099 or RRB-1099, any deduction for contributions to a traditional IRA, any student loan interest deduction, or any exclusion of interest from savings bonds".
- Distributions with basis. p590a p. 15, Both contributions for 2025 and distributions in 2025: "If this is your situation, you must figure the taxable part of the traditional IRA distribution before you can figure your modified AGI." p590b p. 17, Worksheet 1-1, "Use only if you made contributions to a traditional IRA for 2025 that may not be fully deductible and have to figure the taxable part of your 2025 distributions to determine your modified AGI."
- Timing. p590a p. 11: "Contributions can be made to your traditional IRA for a year at any time during the year or by the due date for filing your return for that year, not including extensions."
- Designation. p590a p. 16: "You don’t have to designate a contribution as nondeductible until you file your tax return. When you file, you can even designate otherwise deductible contributions as nondeductible contributions."

### 4.2 State or local refund (Pub. 525 recovery rule)

- Tax benefit rule. p525 p. 24: "You must include a recovery in your income in the year you receive it up to the amount by which the deduction or credit you took for the recovered amount reduced your tax in the earlier year."
- Not itemized. p525 p. 24, Deductions not itemized: "If you didn’t itemize deductions for the year for which you received the recovery of an expense that was deductible only if you itemized, don’t include any of the recovery amount in your income."
- Sales-tax choice. p525 p. 24, State tax refund: "the maximum refund that you may have to include in income is limited to the excess of the tax you chose to deduct for that year over the tax you didn’t choose to deduct for that year." (Examples 26 and 27, official fixtures for the screen, not for the worksheet.)
- Standard deduction limit. p525 p. 25: "Only your itemized deductions that are more than your standard deduction are subject to the recovery rule (unless you’re required to itemize your deductions)." This is the worksheet's lines 4 to 8.
- Timing. i1040gi p. 88, Line 1: "If you chose to apply part or all of the refund to your 2025 estimated state or local income tax, the amount applied is treated as received in 2025." and "Report any taxable refund you received even if you didn’t receive Form 1099-G."
- Business tax. f1099g p. 5, Instructions for Recipient, Box 8: "If this box is checked, the amount in box 2 is attributable to an income tax that applies exclusively to income from a trade or business and is not a tax of general application. If taxable, report the amount in box 2 on Schedule C or F (Form 1040), as appropriate."
- When the worksheet may not be used (i1040gi p. 89, the Exception continued; p525 pp. 24-25 repeats it): "1. You received a refund in 2025 that is for a tax year other than 2024. 2. You received a refund other than an income tax refund, such as a general sales tax or real property tax refund, in 2025 of an amount deducted or credit claimed in an earlier year. 3. You had taxable income on your 2024 Form 1040 or 1040-SR, line 15, but no tax on your Form 1040 or 1040-SR, line 16, because of the 0% tax rate on net capital gain and qualified dividends in certain situations. 4. Your 2024 state and local income tax refund is more than your 2024 state and local income tax deduction minus the amount you could have deducted as your 2024 state and local general sales taxes. 5. You made your last payment of 2024 estimated state or local income tax in 2025. 6. You owed alternative minimum tax in 2024. 7. You couldn’t use the full amount of credits you were entitled to in 2024 because the total credits were more than the amount shown on your 2024 Form 1040 or 1040-SR, line 18. 8. You could be claimed as a dependent by someone else in 2024. 9. You received a refund because of a jointly filed state or local income tax return, but you aren’t filing a joint 2025 Form 1040 or 1040-SR with the same person."
- Other recoveries. p525 p. 25, Where to report: "Enter your state or local income tax refund on Schedule 1 (Form 1040), line 1, and the total of all other recoveries as other income on Schedule 1 (Form 1040), line 8z." When both kinds are present and only part is taxable, Pub. 525 allocates between lines 1 and 8z (p525 p. 25, Allocating the included part). Worksheet 2 (p525 p. 27) handles these; this map recommends refusing them (6.2).
- Interest on a refund is interest income. p525 p. 24: "report any interest you received on state or local income tax refunds on Form 1040, 1040-SR, or 1040-NR, line 2b." (interview help only).
- Net investment income. i8960 p. 14, Deduction recoveries: "A recovery or refund of a previously deducted item increases NII in the year of the recovery." The existing `f8960.refund` refusal covers it and should stay.

Prior-year facts the worksheet needs (all supplied by the filer from the 2024 return): whether the filer itemized in
2024 and deducted income (not sales) tax; the 2024 refund amount and that it is for 2024 (Form 1099-G box 3, "Box 2 amount is for tax year"); 2024 Schedule A lines 5d, 5e and 17; 2024 filing status; the four 2024 age and blindness boxes; for a 2024 MFS return, whether the spouse itemized; and the nine exception answers.

### 4.3 Gambling

- Winnings: p525 p. 33, "Winnings from fantasy sports leagues are gambling winnings." and "In addition to cash winnings, you must include in your income the FMV of bonds, cars, houses, and other noncash prizes."
- Losses, itemized only and capped: i1040sca p. 11, Other Itemized Deductions, "Gambling losses (gambling losses include, but aren't limited to, the cost of nonwinning bingo, lottery, and raffle tickets) but only to the extent of gambling winnings reported on Schedule 1 (Form 1040), line 8b." p529 p. 10 (Rev. December 2020, testimony): "Gambling losses include the actual cost of wagers plus expenses incurred in connection with the conduct of the gambling activity, such as travel to and from a casino." and "You can't reduce your gambling winnings by your gambling losses and report the difference."
- Professional gamblers: p525 p. 33, "If you’re in the trade or business of gambling, use Schedule C (Form 1040). For tax years 2018 through 2025, professional gambling losses and expenses are limited to the amount of your winnings."
- Withholding: i1040gi p. 39, line 25c, "Federal income tax withheld on your Form(s) W-2G. The amount withheld should be shown in box 4." The existing `f1040.line25c` supplied total already takes it; only its help changes.

### 4.4 Alimony

- Received: i1040gi p. 89, Line 2a, "Enter amounts received as alimony or separate maintenance pursuant to a divorce or separation agreement entered into on or before December 31, 2018, unless that agreement was changed after December 31, 2018, to expressly provide that alimony received isn’t included in your income." and "If you are including alimony in your income, you must let the person who made the payments know your social security num-ber."
- Line 2b: i1040gi p. 89, "If you have alimony payments from more than one divorce or separation agreement, on line 2b enter the month and year of the divorce or separation agreement for which you received the most income. Attach a statement listing the month and year of the other agreements."
- Paid: i1040gi p. 95, Line 19a, "You can’t take a deduction for alimony payments you made to or for your spouse if you entered into your divorce or separation agreement after December 31, 2018".
- Child support is not income: i1040gi p. 93, Nontaxable income, "Child support." and p525 p. 31, "Amounts you receive for child support aren’t income to you."
- Pub. 504 (not archived) holds the definition of alimony and the recapture rule.

### 4.5 Early withdrawal penalty

- i1099int p. 3, Box 2. Early Withdrawal Penalty: "Enter interest or principal forfeited because of an early withdrawal of time deposits, such as an early withdrawal from a certificate of deposit (CD), that is deductible from gross income by the recipient. Do not reduce the amount reported in box 1 by the amount of the forfeiture."
- i8960 p. 13, Line 7: "Note: Early withdrawal penalty (Schedule 1 (Form 1040), line 18) is reported on Form 8960, line 10."

### 4.6 HSA distributions

- i8889 p. 9, Exceptions to the Additional 20% Tax: "The additional 20% tax does not apply to distributions made after the account beneficiary: • Dies, • Becomes disabled or • Turns age 65." and "Enter on line 17b only 20% (0.20) of any amount included on line 16 that does not meet any of the exceptions."
- i8889 p. 8, Line 15: "Only include on line 15 distributions from your HSA that were used to pay you for qualified medical expenses not reimbursed by insurance or other coverage and that you incurred after the HSA was established."

### 4.7 Canceled debt

- p525 p. 20, Canceled Debts: "If the debt is a nonbusiness debt, report the canceled amount on Schedule 1 (Form 1040), line 8c. If it’s a business debt, report the amount on Schedule C (Form 1040), or on Schedule F (Form 1040) if the debt is farm debt and you’re a farmer."
- p525 p. 20, Interest included in canceled debt: "If the interest would not be deductible (such as interest on a personal loan), include in your income the amount from box 2 of Form 1099-C."
- Exceptions (p525 p. 21): student loans, deductible debt, price reductions, excluded debt (Form 982). The 2021-2025 student loan rule: "Cancellation of certain loans after December 31, 2020, and before January 1, 2026".

---

## 5. Ordering and every existing line that must change

### 5.1 Order (no cycle except the one in 5.2)

Part I lines (1, 2a, 8b, 8c, 8f, 8g to 8j, 8r, 8z) read only their inputs and prior-year facts → `s1.line9` → `s1.line10` → `f1040.line8` → `f1040.line9` → IRA worksheet (reads line 9 and Schedule 1 lines 11 to 19a) → `s1.line20` → student loan interest worksheet (`sli.line3` reads lines 11 to 20) → `s1.line21` → `s1.line26` → `f1040.line10` → AGI (`f1040.line11a`) and everything downstream of it. Line 18 and 19a read only inputs. Form 8606 Part I reads the IRA worksheet. Form 8880 (Stage 15) reads AGI and, after this stage, the traditional IRA contribution input.

### 5.2 The social security cycle

`ssb.line3` reads `f1040.line8` and `ssb.line6` must read Schedule 1 line 20 ("Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25", i1040gi p. 32); IRA worksheet line 3 reads Form 1040 line 9, which contains line 6b. Structurally: `ira.line3 → f1040.line9 → f1040.line6b → ssb.* → ssb.line6 → s1.line20 → ira.line12 → ira.line7 → ira.line6 → ira.line5 → ira.line3`. The checker rejects it even though the instructions route every reachable case elsewhere (the SSB exception and p590a Appendix B apply exactly when someone is covered, and when no one is covered lines 2 to 6 are skipped). Two encodings break it; both need the refusal R-IRA-1 (social security benefits, a traditional contribution, and anyone covered):

- (a) IRA worksheet line 3 reads Form 1040 lines 1z, 2b, 3b, 4b, 5b, 7a and 8 (line 9 without 6b). Under R-IRA-1 it equals line 9 whenever it affects the deduction. The worksheet's line 3 then does not literally copy line 9 when there are benefits and no one is covered (where the instructions skip it).
- (b) `ssb.line6` reads a twin of line 20 computed on the no-one-covered branch only (lines 7 at the full limit, 10, 11, 12), which under R-IRA-1 equals line 20 on every return that reaches it; the IRA worksheet stays literal.

Recommendation: (b), because it keeps the IRA worksheet a literal transcription and puts the special case where the instruction itself carves the exception (the SSB worksheet's own exception list). Record either as an ambiguity entry. Computing Appendix B instead is a later addition.

### 5.3 Form 8880 (Stage 15) after the IRA deduction exists

Stage 15 refuses traditional IRA contributions on Form 8880 (PREMISES.md, Stage 15 owner decision 1: 'The IRA deduction stays roadmap item 2; traditional IRA contributions are refused on Form 8880.'). With this stage:

1. The Stage 15 refusal of traditional IRA contributions (its gate id is in the landed Stage 15 encoding, not read here) is removed, and Form 8880 line 1 per person becomes Stage 15's Roth input plus the new traditional contribution input (IRA worksheet line 11a or 11b). f8880 p. 1, line 1: "Traditional and Roth IRA contributions, and ABLE account contributions by the designated beneficiary for 2025. Do not include rollover contributions". The text counts all traditional contributions for 2025, deductible or not, so nondeductible contributions (Form 8606 line 1) count too; Stage 15's R2 refusal (nondeductible contributions) goes with it once Form 8606 Part I is in scope. 2. Form 8880 line 8 is AGI, which now subtracts the IRA deduction; nothing to edit, but fixtures that straddle a line 9 band edge change. 3. One excess-contribution screen per person (traditional plus Roth over the limit, Form 5329 Parts III and IV) should serve both forms; Stage 15 planned its own for Roth (Stage 15 map R3). Merge them. 4. Coverage: the estimator maps `savers` to `scope.credits` and `ira_deduction` to `scope.schedule1`. A return with both is counted covered once both gates are clear; if the Stage 15 traditional-IRA refusal on 8880 is left in place, such returns are still refused but the estimate would not show it. The categories.json note ('in the microdata every saver's credit comes with a traditional IRA deduction') is a microdata artifact, not evidence that saver's credit filers have IRA deductions; most 8880 contributions are W-2 deferrals (inference, from the box 12 list on f8880 p. 2).

### 5.4 Existing lines that must change

| Line id | Today | Change |
|---|---|---|
| `scope.schedule1` | screens everything on Schedule 1 outside the Stage 11/14 lines | narrow its question to the residual (5.5); its label and source text name the computed items |
| `scope.ready` refusal remedy for `scope.schedule1` | 'other than unemployment compensation, educator expenses, the HSA deduction and student loan interest' | rewrite (already stale after Stage 14) |
| `f1040.line8`, `f1040.line10` refusal remedies | same text | rewrite |
| `s1.line10` | sum(3, 7) | sum(1, 2a, 3, 7, 9); cite note |
| `s1.line26` | sum(11, 13, 15, 16, 17, 21) | add 18, 19a, 20, 25 |
| `sli.line3` | sum(11, 13, 15, 16, 17) | add 18, 19a, 20; cite note |
| `ssb.line6` | sum(11, 13, 15, 16, 17), refused by `scope.schedule1` | add 18, 19a and line 20 (or its twin, 5.2); refusal text |
| `sa.line16` | `copy sa.zero` | gambling losses: `smaller_of(losses, s1.line8b)`; narrow `sa.unsupported` to the rest of the line 16 list |
| `sa.unsupported` | includes 'a deduction from the Schedule A line 16 list' | except gambling losses |
| `f8960.line10` | `copy f8960.zero` | copy `s1.line18` (i8960 note above); f8960 line 11 already adds 9d and 10 |
| `f8889.unsupported` | includes taxable HSA distributions | split: distributions computed (Part II), the rest (Part III, QHFD, Archer MSA, prior excess, inherited) refused |
| `s2.other` | includes 'the additional tax on early retirement or HSA distributions' | drop the HSA part; new `s2.line17c`, `s2.line18`; `s2.line21` adds 18 |
| `f1040.line25c` | supplied total | help names W-2G box 4 |
| `interest` collection | `interest.amount` only | add box 2 input |
| Stage 15 Form 8880 line 1 and its traditional-IRA refusal | refused | 5.3 |
| `tools/coverage/categories.json` | twelve categories gated on scope.schedule1, f8889.unsupported, sa.excluded_income | computed categories marked not refused or re-gated; refused ones (NOL, 4797) need a gate that still exists (the estimator stops on unknown gates: `categories.json names gates not in the forms`); other income needs a decision (D11) |

No change is needed in lines that read AGI (`f1040.line11a`), taxable income or line 9 generally: Schedule A's medical floor, Schedule 1-A's MAGI, the EIC's AGI tests, Form 8812's credit limit, Form 8960's MAGI, Forms 2441 and 8880 read them and move with them. Earned income is unaffected: none of the computed Part I items is earned income for the EIC or Schedule 8812 (inference; the EIC worksheet reads `f1040.line1z` and Schedule C, and 8812's earned income worksheet reads lines 1a to 1z, 2b and 5, none of which these items enter).

### 5.5 The riders on `scope.schedule1`

After narrowing, each of these refusals is still triggered by `scope.schedule1`, so the residual question must still cover its reason, or the rider needs its own gate:

| Rider | Its reason | Still in the residual? |
|---|---|---|
| `eic.step2_other` | Schedule E, rental of personal property (line 8l), passive activity | yes if 8l and Schedule E stay in it |
| `eic.step5_line1`, `eic.clergy` | clergy, church employee, statutory employee | yes |
| `s8812.eiw_3` | statutory employee, farm, partnership | yes |
| `s8812.eiw_4` | line 8s | yes if 8s stays in it |
| `s1a.yaml` line 5 refusal | tips in a trade or business with Schedule E or F | yes |
| `s1a.yaml` line 14b refusal | qualified overtime on Form 1099-NEC box 1 or 1099-MISC box 3 | **at risk**: a filer reporting such pay as 8i or 8z would clear the narrowed screen. The 8i/8z interview must keep asking it, or the rider gets its own gate. |
| `carloan` column (ii) note | interest deducted on Schedule C, E or F | yes |
| `eic` Step 2 question 3 cite | 'Form 4797 is refused before this question' | yes while Form 4797 stays refused |

---

## 6. Refuse-or-compute candidates

### 6.1 IRA deduction

| # | Situation | Why hard | Recommendation |
|---|---|---|---|
| R-IRA-1 | Social security benefits, a traditional contribution, and you or your spouse covered | i1040gi p. 31 exception; Pub. 590-A Appendix B is a second SSB computation; the line graph cycle (5.2) | Refuse |
| R-IRA-2 | Joint return, contributions to both traditional and Roth IRAs (by either spouse, Q1) | i1040gi p. 95 item 2 sends to Pub. 590-A | Refuse |
| R-IRA-3 | Joint return with line 10 under $14,000 / $15,000 / $16,000 | worksheet caution, Kay Bailey limit | Refuse |
| R-IRA-4 | Excess contributions (traditional plus Roth over the limit), or an excess from an earlier year still in the IRA | Form 5329 Part III ("Complete this part if you contributed more to your traditional IRAs ... for 2025 than is allowable or you had an amount on line 17 of your 2024 Form 5329"), roadmap item 7 | Refuse (screen and test) |
| R-IRA-5 | W-2 box 11 or box 12 code Z amounts, or 1099-MISC box 15 | worksheet line 8 exclusion; W-2 boxes 11 and 12 not modelled | Refuse by screen (alternative: per-W-2 input) |
| R-IRA-6 | Nontaxable combat pay | line 8 adds it; combat pay is refused elsewhere (`s8812.combat_pay`) | Refuse (inherited) |
| R-IRA-7 | Recharacterization, qualified reservist repayments, difficulty of care payments (p590a p. 16) | Form 8606 lines and special limits | Refuse by screen |
| R-IRA-8 | Nondeductible contributions with a 2025 traditional IRA distribution or a conversion | Form 8606 lines 4 to 13; `retirement` has no owner | Refuse (already caught by `retirement.special`, which should also be checked to fire when the 2025 nondeductible contribution is the basis) |
| R-IRA-9 | Nondeductible contributions with no distribution | Form 8606 lines 1 to 3 and 14 | Compute |
| R-IRA-10 | Electing to deduct less than the maximum | p590a p. 16 and worksheet line 12 allow it | Compute the maximum, refuse the election by screen (alternative: an input for the amount chosen) |
| R-IRA-11 | Covered status: W-2 box 13 vs. the plan-year rules | box 13 is not modelled; p590a p. 12 rules | Compute from a per-person question with box 13 named in help, plus `person.plan` for SEP/SIMPLE (Q6) |
| R-IRA-12 | Self-employment loss of one spouse with W-2 wages | p590a p. 7 says not to net; worksheet line 9 floors the combined amount | Compute, reading per person (Q7) |
| R-IRA-13 | Graduate fellowship or stipend not on W-2 (8r) counted as compensation | p590a p. 6 counts it; worksheet line 8 omits it | Refuse the IRA deduction when present (Q9) |
| R-IRA-14 | Form 2555, 8815, adoption benefits with coverage | i1040gi p. 96 | Already refused elsewhere |
| R-IRA-15 | Divorced or legally separated, contributions to a former spouse's IRA | p590a p. 11 Note | Not reachable (MFS refused; a joint return is needed for a spouse's IRA) |

### 6.2 State refund

| # | Situation | Recommendation |
|---|---|---|
| R-REF-1 | Did not itemize in 2024, or deducted sales tax and the refund is of income tax | Compute: line 1 is zero (no worksheet) |
| R-REF-2 | Any of the nine exceptions (4.2) | Refuse by screen (Pub. 525 Worksheet 2) |
| R-REF-3 | Refunds of real estate, personal property or sales tax, or other itemized recoveries (medical reimbursement, Form 1098 box 4) | Refuse (exception 2; Worksheet 2 and the line 8z allocation). Alternative later: encode Worksheet 2 and 2a. |
| R-REF-4 | Form 1099-G box 8 checked | Refuse (Schedule C or F) |
| R-REF-5 | Refund for 2024 when 2024 was MFS and the spouse itemized | Compute (the worksheet's own note) |
| R-REF-6 | Prior deducted amount on an earlier Form 8960 | Refuse (existing `f8960.refund`) |
| R-REF-7 | 2024 return was a dependent's or nonresident's | Refuse (exception 8; nonresident: p525 p. 25 "Nonresident aliens") |

### 6.3 Other income, gambling, alimony, penalty, HSA, COD

| # | Situation | Recommendation |
|---|---|---|
| R-OI-1 | 8g, 8h (+24a), 8i, 8j, 8r, 8b | Compute as inputs |
| R-OI-2 | 8z kinds with no other form (kickbacks, insurance dividends over premiums, RTAA from 1099-G box 5) | Compute for a closed list (Q11) |
| R-OI-3 | 8z recoveries, corrective distributions, charitable recaptures (Schedule 2 line 17g), disaster relief, Coverdell or QTP distributions (Form 5329) | Refuse |
| R-OI-4 | 8a, 8d, 8e, 8k, 8l, 8m, 8n, 8o, 8p, 8q, 8s, 8t, 8u, 8v; line 4 | Refuse |
| R-OI-5 | The 1099-K entry space at the top of Schedule 1 | Out of this stage; keep refused wherever it is refused now |
| R-GAM-1 | Gambling as a trade or business | Refuse (Schedule C, special loss limit) |
| R-GAM-2 | Losses by a filer who takes the standard deduction | Compute: no deduction (the line 16 cap applies only when itemizing) |
| R-ALI-1 | Agreement after 2018, or modified to exclude | Compute: not on line 2a or 19a (screen; amounts are not income/deductible) |
| R-ALI-2 | More than one agreement, recapture, payments partly child support | Refuse by screen (Pub. 504 not archived) |
| R-EWP-1 | Form 1099-OID penalty (box 3) | Refuse with OID (Schedule B already refuses OID) |
| R-HSA-1 | Part II distributions, all or none of the line 16 amount excepted | Compute |
| R-HSA-2 | Part of the line 16 amount excepted (e.g. turned 65 during 2025) | Refuse, or an input for the part subject (Q15) |
| R-HSA-3 | Part III, QHFD, Archer MSA, inherited HSA | Refuse (as today) |
| R-COD-1 | Nonbusiness debt, fully taxable, interest not deductible | Compute (input box 2) |
| R-COD-2 | Any exclusion (Form 982), business or farm debt, foreclosure or repossession, deductible interest in box 3, stockholder debt | Refuse by screen |
| R-COD-3 | Student loan discharge excluded for 2021-2025 | Compute as not income (screen answer), no Form 982 named in p525 for it (inference: the p525 text lists it under Exceptions, not Excluded debt) |

---

## 7. Parameters for `params/2025.yaml` (cents)

IRA deduction (i1040gi pp. 97-98, IRA Deduction Worksheet):

| Name (proposed) | Type | Value | Locator |
|---|---|---|---|
| `ira.limit` | NonNegDollars | 700000 | p. 97, "$7,000 if under age 50 at the end of 2025." |
| `ira.limit_50` | NonNegDollars | 800000 | p. 97, "$8,000 if age 50 or older at the end of 2025." |
| `ira.top_single` | NonNegDollars | 8900000 | p. 97, line 2, "enter $89,000" |
| `ira.top_joint` | NonNegDollars | 14600000 | p. 97, line 2, "Qualifying surviving spouse, enter $146,000." |
| `ira.top_not_covered` | NonNegDollars | 24600000 | p. 97, line 2, "enter $246,000 for the person who wasn’t covered by a plan" |
| `ira.full_single` | NonNegDollars | 1000000 | p. 97, line 6, "the result is $10,000 or more" |
| `ira.full_joint` | NonNegDollars | 2000000 | p. 97, line 6, "and the result is $20,000 or more" |
| `ira.rate_single` | Rate | 70/100 | p. 98, line 7, "multiply by 70% (0.70)" |
| `ira.rate_single_50` | Rate | 80/100 | p. 98, line 7, "or by 80% (0.80)" |
| `ira.rate_joint` | Rate | 35/100 | p. 98, line 7, "multiply by 35% (0.35)" |
| `ira.rate_joint_50` | Rate | 40/100 | p. 98, line 7, "or by 40% (0.40)" |
| `ira.min` | NonNegDollars | 20000 | p. 98, line 7, "But if it is less than $200, enter $200." |
| (round unit) | `round` unit 1000, rule up | — | p. 98, line 7, "increase it to the next multiple of $10" |
| `ira.kbh_none`, `ira.kbh_one`, `ira.kbh_both` | NonNegDollars | 1400000, 1500000, 1600000 | p. 98, Caution, "less than $14,000 ($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025)" |

The MFS amount ($10,000, line 2) is not needed while MFS is refused.

State refund worksheet (i1040gi p. 90), as `keyed_lookup` tables keyed by the 2024 filing status (status-keyed parameters cannot take a prior-year status):

| Name | Keys → value | Locator |
|---|---|---|
| `refund.std_2024` | single 1460000, mfs 1460000, mfj 2920000, qss 2920000, hoh 2190000 | line 5, "Single or married filing separately—$14,600", "Married filing jointly or qualifying surviving spouse—$29,200", "Head of household—$21,900" |
| `refund.box_2024` | single 195000, hoh 195000, mfj 155000, mfs 155000, qss 155000 | line 6, "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)." |

HSA (f8889 p. 1): `hsa.addl_rate` Rate 20/100, line 17b, "Enter 20% (0.20) of the distributions included on line 16 that are subject to the additional 20% tax."

No parameters for gambling, alimony, the penalty or COD. Dates (December 31, 2018; January 2, 1960; April 15, 2026) belong in screen wording, not parameters.

---

## 8. Open questions

- **Q1. "You or your spouse made contributions to both a traditional IRA and a Roth IRA."** (i1040gi p. 95, item 2.) Does this mean one person contributed to both kinds, or that between the spouses there are contributions of both kinds (you traditional, your spouse Roth)? The Kay Bailey limit reduces one spouse's limit by "Any contributions for the year to a Roth IRA on behalf of your spouse" (p590a p. 10), which suggests the cross case matters. The broader reading refuses more.
- **Q2. Worksheet line 1 cap, "your state and local income taxes shown on your 2024 Schedule A, line 5d".** Line 5d of the 2024 Schedule A is the total of income (or sales), real estate and personal property taxes; the income tax alone is line 5a. Cap at line 5d as printed, or at the income-tax part (line 5a)? Pub. 525's Worksheet 2a line 3 caps the total refunds at line 5d, which fits the literal reading.
- **Q3. Worksheet line 2, "paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d)".** Ask for the amount reported on 5d, or the amount paid when it differs? "Generally" admits a difference without saying when.
- **Q4. Line 6 boxes for 2024.** Ask the four 2024 facts, or derive "born before January 2, 1960" from the 2025 age question (`person.age65`, `Were you born before January 2, 1961?`) plus one more question? A spouse in 2024 may not be the 2025 spouse, so the 2025 person records cannot be reused for the spouse boxes.
- **Q5. "Age 50 or older at the end of 2025." (i1040gi p. 97)** Ask it directly (as `person.simple_age` does for SIMPLE catch-up), or as a birth date cut? p501's day-before rule is stated for age 65 and the standard deduction; whether it applies here the archived text does not say.
- **Q6. Covered by a retirement plan.** One per-person question with help naming W-2 box 13, the self-employed SEP or SIMPLE (`person.plan`) and the plan-year rules; or a per-W-2 box 13 input plus a question for coverage not shown on a W-2?
- **Q7. Line 9 for spouses.** The worksheet takes the couple's self-employment earned income and floors the total at zero; Pub. 590-A says a net self-employment loss is not subtracted from wages. Per person floor, then sum (Pub. 590-A), or sum, then floor (worksheet literal)? They differ only when one spouse has a self-employment loss and the other has self-employment profit.
- **Q8. Box 11 and code Z.** Refuse when present, or add per-W-2 inputs and subtract them on line 8?
- **Q9. Line 8r and IRA compensation.** Pub. 590-A counts certain non-tuition fellowship and stipend payments not on a W-2 as compensation; the worksheet line 8 does not list them. Refuse the IRA deduction when such payments exist, add them to line 8, or follow the worksheet literally?
- **Q10. The election to deduct less.** Compute the maximum and refuse the election, or take an input for the amount the filer chooses (no default allowed, spec 8)?
- **Q11. Line 8z without strings.** The form says "List type and amount". The project has no strings. A collection of 8z entries keyed by an enum of supported kinds (the values sheet shows the kind's name), or one total with a notice that the filer writes the type?
- **Q12. Lines 2b, 19b and 19c.** The agreement date and the recipient's SSN are printed lines with no number. Leave them to the filer with a notice on the values sheet, or ask and show them (an SSN is personal data; spec 9 keeps none in the repository, but a runtime answer is not stored)?
- **Q13. Alaska Permanent Fund dividends and the like: return or person?** Nothing in this stage reads them per person; a return-level total is simplest. A per-person record matters only if a later stage (the kiddie tax, Form 8814) needs it.
- **Q14. Line 24a cap.** "Enter your jury duty pay if you gave the pay to your employer" (i1040gi p. 99). Cap the input at line 8h by a test and refusal, or by `smaller_of`?
- **Q15. HSA line 17b partial exception.** The amount subject to the 20% tax can be part of line 16 (distributions before and after turning 65). An input for the part subject, or refuse a partial exception?
- **Q16. Refund received in 2025 for 2024 when the 2024 return was joint and 2025 is joint with the same spouse:** exception 9 does not apply. When 2024 was joint and 2025 is single after a divorce, exception 9 applies and the refund is refused. Confirm that "the same person" needs no question beyond 'was your 2024 state return joint with someone other than your 2025 spouse'.

---

## 9. Draft owner decision batch

Each item: the recommended answer first, the alternative after the slash.

- **D1. Scope.** Compute other income (named subset), the state refund, the IRA deduction with Form 8606 Part I (no distributions), gambling with Schedule A line 16 losses, the early withdrawal penalty, alimony, taxable HSA distributions and fully taxable canceled debt; refuse Form 4797, the NOL and the foreign earned income exclusion. / Compute only the four largest (other income, refund, IRA, gambling).
- **D2. The four small ones** (penalty, alimony, HSA, COD): compute each. / Refuse any of them by name.
- **D3. Line 8 subset.** 8b, 8c, 8f (Part II only), 8g, 8h with 24a, 8i, 8j, 8r and a closed 8z list; refuse the rest. / Smaller: 8b, 8g, 8h, 8i only.
- **D4. 8z encoding (Q11).** A collection keyed by a supported-kind enum. / One total with a notice.
- **D5. Refund worksheet only.** Compute the i1040gi worksheet; refuse the nine exceptions, non-income-tax refunds and other recoveries (Pub. 525 Worksheet 2). / Also encode Worksheet 2 and 2a.
- **D6. Readings for the refund worksheet.** Q2: cap at line 5d as printed. Q3: ask the amount reported on 5d. Q4: four 2024 Bools. / Q2 at line 5a; Q4 a box count.
- **D7. The SSB cycle (5.2).** Refuse social security plus a traditional contribution plus coverage, and break the cycle with encoding (b) (an SSB-side twin of line 20). / Encoding (a); or compute Pub. 590-A Appendix B.
- **D8. IRA refusals.** R-IRA-2 with the broad reading of Q1; R-IRA-3, 4, 5, 6, 7, 8, 13 refused; R-IRA-10 refused (deduct the maximum). / Narrow Q1; inputs for box 11 and code Z; an input for the deducted amount.
- **D9. IRA readings.** Q5: ask 'age 50 or older at the end of 2025' directly. Q6: one per-person coverage question plus `person.plan`. Q7: per-person floor (Pub. 590-A). / Birth-date cut; per-W-2 box 13; worksheet-literal floor.
- **D10. Form 8880.** Lift the Stage 15 traditional-IRA refusal and count all traditional contributions for 2025 on line 1; one shared excess-contribution screen. / Leave Form 8880 as Stage 15 built it (IRA-deduction filers who claim the saver's credit stay refused).
- **D11. Coverage bookkeeping.** Mark the computed categories not refused; keep `other_income` refused with a note that part of it is now computed and the estimate cannot measure which part. / Mark it covered (overstates).
- **D12. Non-numeric printed lines (Q12).** Notices for 2b, 19b, 19c; nothing asked. / Ask and display.
- **D13. HSA partial exception (Q15).** Input for the part subject to the 20% tax. / Refuse.
- **D14. Gambling.** Losses on Schedule A line 16 capped at line 8b; professional gamblers refused. / Refuse gambling losses (keep `sa.unsupported` as is) and compute winnings only.

Fourteen items; D1, D7, D8 and D10 are the ones that change the structure.

---

## 10. Verified vs inferred

Verified against the archived text (read on the cited pages; quotes copied from `.cols.txt` or `.txt`):

- The Schedule 1 line texts (f1040s1 pp. 1-2); the i1040gi Schedule 1 instructions pp. 88-95 and 99-100; the refund worksheet (p. 90) and the IRA worksheet (pp. 97-98, read in the layout text); the SSB exception (p. 31) and SSB line 6.
- Pub. 525 pp. 20, 24-28, 31, 33-35; Pub. 590-A pp. 6-7, 9-16 and 54; Pub. 590-B p. 17 (heading only); Form 8606 Part I; i8606 pp. 2, 5, 8-9; Form 1099-G boxes 2, 3, 8; i1099int box 2; i8889 Part II; f8889 Part II; Schedule 2 lines 17c, 18, 21; i8960's line 10 note; Schedule A line 16 instructions; p529 p. 10; Form 5329 Part III heading; Form 8880 line 1.
- Repository facts: every line id in 3.1, 5.4 and 5.5 was read in the YAML named; the status-keyed parameter rule in engine/src/eval.ts; the structural cycle walk in engine/src/check.ts; the coverage shares in the report; the SOI column headers and totals in soi-23in14ar (read with pandas).
- Coverage gains: recomputed with estimate.py's functions; the reproduction matches the report's 58.0%, +6.7 and 65.3%.

Inferred, not checked:

- What the SOI "Other income" column contains (no footnote in the archive), and therefore how much of the 4.85% the recommended subset covers.
- That the IRS-only categories overlap Schedule C, E and F more than independence assumes.
- That no computed Part I item is earned income for the EIC or Schedule 8812 (from the worksheets' line references, not a reading of Pub. 596, which is not archived).
- That the Stage 15 encoding has a separate gate for traditional IRA contributions on Form 8880 and a Roth input per person (from the Stage 15 owner decisions in PREMISES.md; the Stage 15 YAML was not read).
- That alimony recapture cannot arise in 2025 for a pre-2019 agreement (no archived source; Pub. 504 would say).
- The proposed parameter and line names, and the claim that encoding (b) of 5.2 passes the checker (not built).
- Plausible gaps: Pub. 590-A chapter 2 (Roth eligibility by MAGI) bears on the excess-contribution screen and was not read; the i1040gi EIC Step 2 investment-income definition was not re-read for line 8 items; W-2G box 7 and the noncash-prize valuation are unsourced without the form.
