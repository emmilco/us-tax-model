# Screen adjudication, group 0 (2026-10-30)

Standard: reviews/2025/screens/screen_review.md (NARROW dangerous, WIDE safe, sibling or derived refusals cover). Each screen re-checked against the current forms/2025 YAML; one derived refusal verified by `node engine/dist/main.js eval` (s8812.puerto_rico finding 0).

Counts: 58 findings; accepted WIDE 29, covered 16, defect 6, presentation 5, model error 2.

## `clcw.spouse_screen`

WIDE only; both findings refuse cases the worksheet computes correctly.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040sd p. 10 | First limb has no loss condition; a filer with no 2024 loss is refused though the tool computes zero carryover (i1040sd p. 10). Safe. |
| 1 | WIDE | accepted WIDE | i1040sd p. 10 | Filer who had the whole joint loss is refused though the full carryover is deductible (i1040sd p. 10). Safe. |

## `dependent.divorced_rule`

One defect: a custodial parent who signed the release can read the question as not applying to them and the tool then lets them claim the child for the CTC/ODC; two WIDE accepted. Bugs: PENDING-0-1

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | UNCLEAR | defect | i1040gi p. 20 | i1040gi p. 20: 'If conditions (1) through (4) apply, only the noncustodial parent can claim the child for purposes of the child tax credit and credit for other dependents'. A custodial parent who signed Form 8332 who answers no gets dependent.qualifying_child = true (forms/2025/dependent.yaml: residency/age/relationship tests only), so the CTC/ODC is claimed on both parents' returns. dependent.other_claimant is not a reliable backstop (the other parent fails residency on its face). |
| 1 | WIDE | accepted WIDE | i1040gi p. 20 | Ordinary custodial parent with no release answers yes and is refused; the tool computes the residency case. Safe. |
| 2 | WIDE | accepted WIDE | i1040gi p. 20 | Release holder failing the support/custody conditions is refused; tool would compute non-qualifying. Safe. |

## `dependent.married`

One defect (low): a dependent who died during 2025 while married, whose surviving spouse files a joint return including them, can be answered no to both this screen and dependent.joint_return; two WIDE accepted. Bugs: PENDING-0-2

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi pp. 17, 21, 44 | Married non-joint filer refused on qualifying_child/qualifying_relative where i1040gi p. 21 lets the flow continue. Safe (and needed for eic_child, i1040gi p. 44). |
| 1 | WIDE | accepted WIDE | i1040gi pp. 17, 21, 44 | Refund-only joint filer refused though dependent.joint_return computes the exception. Safe. |
| 2 | UNCLEAR | defect | i1040gi pp. 17, 21, 44 | i1040gi p. 21: 'If the person is married and files a joint return, you can't claim that person as your dependent.' The example covers only the case where this person's spouse died; the sibling input dependent.joint_return ('Is this person filing a joint return for 2025...') carries the same ambiguity and computes rather than refuses, so a no to both lets the dependency/CTC compute for a person on a joint return. |

## `f2441.prior_year`

WIDE only.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i2441 p. 4 | Filer who already claimed the 2024 maximum is refused though line 9b is zero (i2441 p. 4, Line 9b). Safe. |

## `f4952.alternative_allocation`

No defect: the two NARROW findings (line 5 investment expenses) are covered by f4952.unsupported, which gates the same four lines; the UNCLEARs either err wide or misread 'alternative allocation'.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | f4952 pp. 3-4 | f4952.unsupported asks 'any deductible investment expense other than interest (for example depreciation or depletion ... or investment expenses on a Schedule K-1)' and gates f4952.line2, election, line5 and required (forms/2025/f4952.yaml). |
| 1 | NARROW | covered | f4952 pp. 3-4 | Same: other deductible investment expenses (the Who Must File exception) are screened by f4952.unsupported on f4952.required. |
| 2 | UNCLEAR | accepted WIDE | f4952 pp. 3-4 | The doubtful reading (any line 4g election counts) produces yes and a refusal of a default-allocation case the tool computes. Safe direction only. |
| 3 | UNCLEAR | model error | f4952 pp. 3-4 | f4952 p. 4 Note: any shift ('treat less of the amount on line 4e as attributable to line 4g', entering 'Elec.') is an alternative to the default; a filer deliberately making that entry is electing 'an alternative allocation' and the question names that election. No plausible truthful no. |

## `f5695.construction_later`

No defect: WIDE accepted; installation completed in 2026 is excluded by the cost inputs' own definition; 'reconstruction' is the IRS's undefined term.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i5695 p. 1 | Reconstructed home first used in 2025 may be answered yes and refused; tool's costs would be correct. Safe. |
| 1 | NARROW | covered | i5695 p. 1 | The amount inputs f5695.line1-line5a, battery_cost (interview/questions-2025.yaml help) say 'A cost counts in 2025 when the original installation is completed' (i5695 p. 1, Costs), so costs completed in 2026 are not entered; the screen does not need to carry this. |
| 2 | UNCLEAR | out of scope / presentation | i5695 p. 1 | i5695 p. 1 itself does not define reconstruction; the screen repeats the IRS term. A renovation of an occupied home answered no falls back on the installation-completed rule, which is the ordinary rule. |

## `f8959.unsupported`

No defect: SE income that reaches Schedule SE but not through this tool's Schedule C path is refused by person.se_screen (and K-1/Schedule F by scope.schedule1); territory W-2s other than 499R-2 are WIDE.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | UNCLEAR | covered | i8959 p. 1; person.se_screen | person.se_screen (forms/2025/person.yaml) asks about partnership SE (K-1 box 14 code A), other SE income not on Schedule C, farm income, optional methods, church/clergy income, Forms 4137/8919, and refuses person.se_line2 -> person.se_line6 -> f8959.line8 (sum_over person.se_line6). A filer with K-1 or Schedule F income is also refused by scope.schedule1. |
| 1 | WIDE | accepted WIDE | i8959 p. 1; person.se_screen | W-2AS/CM/GU/VI use boxes 5 and 6 (i8959 p. 1) and would compute; refusing them is safe. |

## `household.credit_disallowed`

WIDE only; the UNCLEAR's doubtful reading also errs wide.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi pp. 39, 43; i1040s8812 p. 2 | Recertified EIC (i1040gi p. 43 exception) refused. Safe. |
| 1 | WIDE | accepted WIDE | i1040gi pp. 39, 43; i1040s8812 p. 2 | No-child EIC after a child-only disallowance (i1040gi p. 43) refused. Safe. |
| 2 | WIDE | accepted WIDE | i1040gi pp. 39, 43; i1040s8812 p. 2 | CTC recertified for 2024 (i1040gi p. 39) refused. Safe. |
| 3 | WIDE | accepted WIDE | i1040gi pp. 39, 43; i1040s8812 p. 2 | One answer refuses both credit families. Safe. |
| 4 | UNCLEAR | accepted WIDE | i1040gi pp. 39, 43; i1040s8812 p. 2 | Reading 'reduced' as an ordinary phase-out gives yes (refusal); the no reading is the correct one (i1040s8812 p. 2). Only the safe direction is at risk. |

## `refund.not_2024`

One defect: the second limb asks only about a late estimated payment, but Pub. 525's pro rata rule (which the refusal itself cites) applies to any 2024 tax paid in 2025, e.g. an extension or balance-due payment; WIDE accepted; 'refunds' is defined by the preceding amount input. Bugs: PENDING-0-3

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | defect | p525 p. 24; i1040gi pp. 88-89 | p525 p. 24, Recovery for 2 or more years: 'If you receive a refund or other recovery that is for amounts you paid in 2 or more separate years, you must allocate, on a pro rata basis...'. A 2024 refund partly from an April 2025 extension payment is answered no; refund.taxable runs the i1040gi worksheet on the whole refund and Schedule A line 5a keeps the whole 2025 payment (Example 28 reduces it). |
| 1 | WIDE | accepted WIDE | p525 p. 24; i1040gi pp. 88-89 | Non-itemizer for 2024 with a January 2025 estimate refused though the tool's zero is right. Safe (amb.2025.refund_exceptions chose to ask item 5 of every refund). |
| 2 | WIDE | accepted WIDE | p525 p. 24; i1040gi pp. 88-89 | Other-year refund for a year without itemizing refused. Safe. |
| 3 | UNCLEAR | model error | p525 p. 24; i1040gi pp. 88-89 | 'These refunds' refers to the preceding amount input refund.line1 (forms/2025/refund.yaml: 'State or local income tax refunds, credits or offsets ... including any part you chose to apply to your 2025 estimated ... tax and any part offset against a debt'), which the reviewer did not see. |

## `s8812.combat_pay`

WIDE only.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi p. 42; i2441 pp. 4-5; i1040s8812 p. 8 | Non-electing combat-pay recipient refused on lines whose amount would be zero (i1040gi p. 42; i2441 pp. 4-5). Safe. |
| 1 | WIDE | accepted WIDE | i1040gi p. 42; i2441 pp. 4-5; i1040s8812 p. 8 | Recipient never sent to the Earned Income Worksheet refused on line 1b. Safe. |

## `s8812.puerto_rico`

No defect: Puerto Rico withholding of a non-resident is caught by f8959.unsupported (derived refusal of line 21, verified by eval); residency-term doubts can only under-claim the ACTC.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | f1040s8812 p. 2; i1040s8812 p. 5 | A Form 499R-2/W-2PR holder answers yes to f8959.unsupported ('Medicare wages on a wage statement from a U.S. territory (such as Form 499R-2/W-2PR)'), which refuses f8959.line19 -> s8812.amt_ws4 -> s8812.line21 -> clwb_7 and Part II-B. Eval of fixtures stage4.base with f8959.unsupported=true: s8812.amt_ws4 = refusal (gate f8959.unsupported). |
| 1 | WIDE | accepted WIDE | f1040s8812 p. 2; i1040s8812 p. 5 | Resident refused where Part II-B cannot change the result (f1040s8812 p. 2). Safe. |
| 2 | UNCLEAR | out of scope / presentation | f1040s8812 p. 2; i1040s8812 p. 5 | The screen uses the form's own term ('If you are a bona fide resident of Puerto Rico, go to line 21'). A wrong no can only lower the credit: line 26 is 'the larger of line 20 or line 25' and CLW B line 11 is zero off the Puerto Rico path, so no overclaim results. |
| 3 | UNCLEAR | out of scope / presentation | f1040s8812 p. 2; i1040s8812 p. 5 | Same: IRS term of art, same direction argument. |

## `sa.excluded_income`

No defect: the five NARROW Schedule A items are screened by sa.unsupported and sa.charity_limited, which gate the same lines; the WIDE findings are accepted; bare form numbers are a presentation point.

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | f1040sa p. 1; i1040sca pp. 7, 11 | sa.unsupported asks 'a foreign tax or generation-skipping tax deduction' and gates sa.line6. |
| 1 | NARROW | covered | f1040sa p. 1; i1040sca pp. 7, 11 | sa.unsupported asks 'mortgage interest or points not on Form 1098' and gates sa.line8b, sa.line8c. |
| 2 | NARROW | covered | f1040sa p. 1; i1040sca pp. 7, 11 | sa.charity_limited asks 'carried over from a prior year' and gates sa.line13. |
| 3 | NARROW | covered | f1040sa p. 1; i1040sca pp. 7, 11 | sa.unsupported asks 'Any casualty or theft loss' and gates sa.line15. |
| 4 | NARROW | covered | f1040sa p. 1; i1040sca pp. 7, 11 | sa.unsupported asks 'a deduction from the Schedule A line 16 list other than gambling losses' and gates sa.line16. |
| 5 | WIDE | accepted WIDE | f1040sa p. 1; i1040sca pp. 7, 11 | Form 4563/Puerto Rico filer refused at EIC Step 1 q. 3 (i1040gi p. 40 names only Form 2555). Safe. |
| 6 | WIDE | accepted WIDE | f1040sa p. 1; i1040sca pp. 7, 11 | Same on Form 2441 lines 4, 5, 18, 19 (i2441 p. 4). Safe. |
| 7 | WIDE | accepted WIDE | f1040sa p. 1; i1040sca pp. 7, 11 | Same on Form 8962 Worksheet 1-1 line 3 (i8962 p. 8). Safe. |
| 8 | WIDE | accepted WIDE | f1040sa p. 1; i1040sca pp. 7, 11 | SALT at or below the cap refused (i1040sca p. 7). Safe. |
| 9 | UNCLEAR | out of scope / presentation | f1040sa p. 1; i1040sca pp. 7, 11 | The exclusions cannot be claimed without the forms; a Form 2555 exclusion is also Schedule 1 line 8d, refused by s1.line8_other ('the foreign earned income or housing exclusion from Form 2555 (8d)'), and foreign wages not on a W-2 by scope.other_income. Naming the income would help but nothing unsupported computes. |

## `sales.special`

One defect: shares of a physically backed precious-metals trust are strictly 'an interest in a ... trust holding' collectibles, but a holder of exchange-traded shares can reasonably answer no; the two WIDE findings are accepted. Bugs: PENDING-0-4

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040sd pp. 11-12 | S corporation/trust interest holding only section 1250 property or QSB stock refused (i1040sd pp. 11-12 look-throughs). Safe. |
| 1 | WIDE | accepted WIDE | i1040sd pp. 11-12 | Short-term entity interest refused. Safe. |
| 2 | UNCLEAR | defect | i1040sd pp. 11-12 | i1040sd p. 11: 'Collectibles include ... metals (such as gold, silver, and platinum bullion)' and line 18 includes gain from 'an interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation of collectibles'. A long-term sale of gold-trust ETF shares on Form 1099-B answered no is computed as ordinary long-term gain at 0/15/20% instead of through the 28% Rate Gain Worksheet. |

## `scope.other_line16`

One defect: Form 8615 is named only by number, so a child who must file it can answer no and be taxed at their own rates; passive Schedule C income and Form 2555 are refused elsewhere; WIDE and elective Schedule J accepted. Bugs: PENDING-0-5

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040gi pp. 34, 36, 40 | A Schedule C business without material participation is refused by sc.passive -> sc.screened on sc.line1 (forms/2025/sc.yaml), and scope.other_income asks 'income or loss from a passive activity', refusing f1040.line8. |
| 1 | NARROW | covered | i1040gi pp. 34, 36, 40 | Form 2555 is Schedule 1 line 8d, named in s1.line8_other, which refuses s1.line9 -> f1040.line8 -> AGI -> taxable income -> line 16. |
| 2 | WIDE | accepted WIDE | i1040gi pp. 34, 36, 40 | Form 8621 with no line 16e tax refused (i1040gi p. 34). Safe. |
| 3 | UNCLEAR | defect | i1040gi pp. 34, 36, 40 | i1040gi p. 36: 'You must file Form 8615 if you meet all of the following conditions. 1. You had more than $2,700 of unearned income ... 3. You were either: a. Under age 18 ...'. No other input tests these conditions (the age/support/parent inputs in person.yaml serve only Form 8863 line 7). A 16-year-old filer with $10,000 of dividends who answers no gets f1040.line16 at their own rates. |
| 4 | UNCLEAR | out of scope / presentation | i1040gi pp. 34, 36, 40 | Schedule J is an optional election (i1040gi p. 36 'your tax may be less if you choose'); a no computes the ordinary tax correctly. A Schedule D/Form 4952 filer reading 'filing' as yes is refused: WIDE, safe. |

## `scope.schedule1`

One low defect: 'clergy income' is not defined, so a member of a religious order without a vow of poverty or a Christian Science practitioner paid on Form W-2 can answer no; the other NARROW findings are refused by sibling or derived gates; WIDE accepted. Bugs: PENDING-0-6

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040gi pp. 40, 42-43, 104, 108 | Passive Schedule C business refused by sc.passive -> sc.screened on sc.line1; scope.other_income also asks 'income or loss from a passive activity'. |
| 1 | NARROW | covered | i1040gi pp. 40, 42-43, 104, 108 | s1a.line5_calc is also gated by s1.sc_1a, counting Schedules C with sc.tips_ot ('qualified tips you received in the course of this business'). |
| 2 | NARROW | covered | i1040gi pp. 40, 42-43, 104, 108 | s1a.line14b_calc is gated by s1.sc_1a (sc.tips_ot asks about 'qualified overtime compensation reported to you on Form 1099-NEC or 1099-MISC'); outside Schedule C, a 1099-MISC box 3 amount entered on line 8z as 'other' is refused by oi8z.figured. |
| 3 | NARROW | covered | i1040gi pp. 40, 42-43, 104, 108 | A section 1256 dealer answers yes to sd.other_forms ('Count section 1256 contracts', Form 6781) and to person.se_screen; every amount the Earned Income Worksheet feeds (ACTC line 27 via the tax limit, EIC via AGI) is then a derived refusal. |
| 4 | UNCLEAR | defect | i1040gi pp. 40, 42-43, 104, 108 | i1040gi p. 43, Clergy: 'The following instructions apply to ministers, members of religious orders who have not taken a vow of poverty, and Christian Science practitioners.' person.se_screen names all three but is asked only with a Schedule C; a W-2-only member of a religious order who answers no gets eic.step5_line1 from line 1z (no Worksheet B) and no SE tax on the ministerial earnings. |
| 5 | WIDE | accepted WIDE | i1040gi pp. 40, 42-43, 104, 108 | Church wages under $108.28 refused (i1040gi p. 42). Safe. |
| 6 | WIDE | accepted WIDE | i1040gi pp. 40, 42-43, 104, 108 | Clergy with an approved Form 4361 and W-2 only refused. Safe. |

# PENDING defects

## PENDING-0-1 — `dependent.divorced_rule`, finding 0 (UNCLEAR; severity medium)

Quote (i1040gi p. 20, Children of divorced or separated parents): "If conditions (1) through (4) apply, only the noncustodial parent can claim the child for purposes of the child tax credit and credit for other dependents ... The custodial parent or another taxpayer, if eligible, can claim the child for the earned income credit and these other benefits."

Case: a divorced custodial parent signed Form 8332 releasing the 2025 claim. The question's example ("a Form 8332 release or a decree lets the noncustodial parent claim the child") is written from the noncustodial side; the custodial parent can read "apply to this person" as not their situation and answer no.

Effect: `dependent.qualifying_child` is computed from relationship, age, support, joint return and residency only, so it is true; the child counts for the CTC/ODC on the custodial return as well as the noncustodial one (overclaim). The EIC line does not use this screen, so the fix does not narrow the custodial parent's EIC.

Fix: append "Answer yes whether you are the parent who signed the release (or whom the decree affects) or the parent using it."

## PENDING-0-2 — `dependent.married`, finding 2 (UNCLEAR; severity low)

Quote (i1040gi p. 21, Married person): "If the person is married and files a joint return, you can't claim that person as your dependent."

Case: the would-be dependent died in 2025 while married; the surviving spouse files a 2025 joint return that includes them (not only for a refund). The filer reads "is this person filing a joint return" as asking whether the deceased filed, and the example covers only the reverse case (this person's spouse died). The sibling input `dependent.joint_return` ("Is this person filing a joint return for 2025, other than only to claim a refund...") has the same reading and computes rather than refuses.

Effect: both answered no; the dependency and CTC/ODC compute for a person on a joint return.

Fix: in both `dependent.married` and `dependent.joint_return`, say "is a joint return being filed for 2025 that includes this person (including one filed by this person's surviving spouse after this person died, or by this person with a spouse who died during 2025)".

## PENDING-0-3 — `refund.not_2024`, finding 0 (NARROW; severity low-medium)

Quote (p525 p. 24, Recovery for 2 or more years): "If you receive a refund or other recovery that is for amounts you paid in 2 or more separate years, you must allocate, on a pro rata basis, the recovered amount between the years in which you paid it. This allocation is necessary to determine the amount of recovery from any earlier years and to determine the amount, if any, of your allowable deduction for this item for the current year." The refusal on `refund.taxable` already cites this passage. i1040gi p. 89, exception 5, names only the estimated-tax case; the Pub. 525 rule covers any 2024 tax paid in 2025.

Case: itemizer for 2024 and 2025; 2024 state withholding $4,000 plus a $1,000 extension payment in April 2025; a $500 refund in 2025. Truthful answer: no (not an estimated payment).

Effect: `refund.taxable` puts the whole $500 through the State and Local Income Tax Refund Worksheet as a 2024 recovery, and the 2025 Schedule A taxes keep the full $1,000; Pub. 525 attributes $100 (1,000/5,000) to the 2025 payment, which reduces the 2025 deduction and is not 2024 recovery income. Either income or the 2025 deduction is misstated.

Fix: reword the second limb to "or did you pay any of your 2024 state or local income tax in 2025 (for example a last estimated payment in January 2025, a payment with an extension, or a balance due)?", and update the refusal text to match.

## PENDING-0-4 — `sales.special`, finding 2 (UNCLEAR; severity medium)

Quote (i1040sd p. 11, line 18): "Collectibles include works of art, rugs, antiques, metals (such as gold, silver, and platinum bullion) ... Include on the worksheet any gain (but not loss) from the sale or exchange of an interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation of collectibles."

Case: a long-term sale of shares in a physically backed gold or silver exchange-traded trust, reported on Form 1099-B like a stock. The holder thinks of it as selling shares, not "an interest in a ... trust", and answers no.

Effect: `sales.one` computes the gain as ordinary long-term gain at 0/15/20% instead of through the 28% Rate Gain Worksheet; tax is understated whenever the filer's ordinary rate exceeds the 15% or 20% rate applied (the 28% rate gain is capped at 28%, not at 15/20%).

Fix: add to the question "(including shares of an exchange-traded fund or trust that holds gold, silver, platinum or other metals)".

## PENDING-0-5 — `scope.other_line16`, finding 3 (UNCLEAR; severity medium)

Quote (i1040gi p. 36): "You must file Form 8615 if you meet all of the following conditions. 1. You had more than $2,700 of unearned income (such as taxable interest, ordinary dividends, or capital gains (including capital gain distributions)). 2. You are required to file a tax return. 3. You were either: a. Under age 18 at the end of 2025, b. Age 18 at the end of 2025 and didn't have earned income that was more than half of your support, or c. A full-time student at least age 19 but under age 24 at the end of 2025 and didn't have earned income that was more than half of your support. 4. At least one of your parents was alive at the end of 2025. 5. You don't file a joint return in 2025."

Case: a 16-year-old files with $10,000 of dividends; the question lists "filing ... Form 8615" by number only and the filer, not already preparing it, answers no. No other input tests these conditions (the age, support and parent inputs in person.yaml feed only Form 8863 line 7).

Effect: `f1040.line16` is computed at the child's own rates; the kiddie tax at the parent's rate is omitted.

Fix: replace "Form 8615" in the question with "Form 8615 (required if you had more than $2,700 of unearned income, are required to file, do not file jointly, have a living parent, and were under 18 at the end of 2025, or 18, or a full-time student 19 to 23, whose earned income was not more than half of your support)".

## PENDING-0-6 — `scope.schedule1`, finding 4 (UNCLEAR; severity low)

Quote (i1040gi p. 43, Clergy): "The following instructions apply to ministers, members of religious orders who have not taken a vow of poverty, and Christian Science practitioners."

Case: a member of a religious order without a vow of poverty, paid on Form W-2 with no Schedule C, reads "clergy income" as ministers only and answers no. `person.se_screen` names all three groups, but it is reached only when the person has a Schedule C (`person.se_line6` is zero when `person.has_sc` is false).

Effect: `eic.step5_line1` uses Form 1040 line 1z without Worksheet B, and no SE tax is figured on the earnings that are SE income for these filers.

Fix: replace "clergy income" with "income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner", matching `person.se_screen`.

