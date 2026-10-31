# Screen adjudication — group 2 (2026-10-30)

Brief: `BRIEF.md`. Records: `reviews/2025/screens/screen_review.json`. Finding numbers are 0-based indexes into each
screen's `findings`. Thirteen records are current (prompt hash matches); `f4952.carryover` and `scope.schedule1a` are
no longer screens (no line names them as a refusal gate), so their records are obsolete and are classed for the record only.
Pages are `sources/2025/<doc>.cols.txt` pages (form-feed split).

## `f2441.student_disabled`

WIDE and minor UNCLEAR only; no defect. Every finding refuses a case the tool computes (actual earned income) or is wording whose loose reading refuses.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Unmarried student/disabled filer refused; i2441 p. 4 ('These rules ... also apply to you if you were a student or disabled') states no joint-return limit, and refusing is safe either way. |
| 1 | WIDE | accepted WIDE | Actual earnings above the $250/$500 floor every month: the tool's actual earned income is right; refusal costs coverage only. |
| 2 | WIDE | accepted WIDE | Correspondence/internet/on-the-job school (i2441 p. 4 'A school doesn't include...'): YES refuses a case computed correctly from actual earnings. |
| 3 | UNCLEAR | accepted (minor UNCLEAR, leans WIDE) | i2441 p. 1 test (can't dress, clean or feed; constant attention): a filer meeting it would answer yes to 'not able to care for yourself'; the loose reading refuses (WIDE). Narrow misreading not plausible. |

## `f4952.carryover`

Retired as a screen: f4952.carryover is now a plain input (line 2 = f4952.prior_7 when true) and no line names it as a refusal gate, so check_screens no longer lists it; the record is obsolete. Findings classed for the record.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | Other line 5 investment expenses are asked by f4952.unsupported ('any deductible investment expense other than interest (for example depreciation or depletion ... or investment expenses on a Schedule K-1)'), which refuses f4952.line2, election, line5 and required. |
| 1 | UNCLEAR | out of scope (obsolete) | Input now reads 'an amount on line 7 of your 2024 Form 4952' and no longer refuses anything; a yes asks for f4952.prior_7, which a used-up carryover answers with 0. |

## `f4952.unsupported`

No defect: the alternative 4g allocation is screened by f4952.alternative_allocation on the same four lines; the rest is WIDE or a computed case.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | f4952.alternative_allocation ('Elect an alternative allocation of Form 4952 line 4g to qualified dividends instead of capital gains first?') refuses f4952.line2, election, line5 and required — exactly the f4952 p. 4 'Elec.' choice. |
| 1 | WIDE | accepted WIDE | Passive, business or tax-exempt-related interest is not investment interest (f4952 p. 3); 'any interest expense' refuses it. Safe. |
| 2 | UNCLEAR | accepted (computed either way) | f4952.line4d = max(0, sd.line16); Schedule D line 16 already includes capital gain distributions (line 13) and the capital loss carryover (line 14), so a NO computes f4952 p. 3 line 4d correctly; a YES is WIDE. |

## `f8960.refund`

No defect: the section 1411 NOL case is screened by f8960.unsupported on the same lines; the rest is WIDE or leans WIDE.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | f8960.unsupported names 'a section 1411 net operating loss' and refuses all eleven lines including f8960.line7; the i8960 p. 15 worksheet caution ('This rule doesn't apply if you incurred an NOL in such year, and a portion of such NOL constitutes a section 1411 NOL') presupposes such an NOL. Same ruling as T-008. |
| 1 | WIDE | accepted WIDE | Recovery of a deduction that did not reduce section 1411 liability (i8960 p. 15): line 7 is zero, which the tool computes; refusal safe. |
| 2 | UNCLEAR | accepted (minor UNCLEAR, leans WIDE) | The question conditions on 'an amount deducted on an earlier Form 8960'; a filer who did deduct reads YES. The other reading refuses a filer with nothing to recover (WIDE). |

## `person.sav_able`

WIDE only, plus one minor UNCLEAR; no defect. Rollovers, returned excess and rollover contributions are excluded from Form 8880 lines 1 and 4 and refusing them is safe.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | f8880 p. 2 line 4 excludes rollover/trustee-to-trustee distributions; refusing them is safe. |
| 1 | WIDE | accepted WIDE | f8880 p. 2 line 4 excludes distributions of excess contributions; refusing is safe. |
| 2 | WIDE | accepted WIDE | f8880 p. 1 line 1 'Do not include rollover contributions'; refusing is safe. |
| 3 | UNCLEAR | accepted (minor UNCLEAR) | Only an ABLE account's designated beneficiary receives its distributions, so a filer with a line 4 ABLE distribution was the beneficiary when paid; the miss needs a former beneficiary who reads 'As the designated beneficiary' as present status. Optional rewording: 'did you receive, as its designated beneficiary, any distribution...'. |

## `person.x_other`

One defect: a partial or later-corrected RMD shortfall can be answered no and Form 5329 Part IX tax is then silently zero. The HSA carryover finding is covered by f8889.unsupported (derived refusal).

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered (derived refusal) | f5329 lines 42-46 are zero in this tool, but a filer with a 2025 Form 8889 is asked f8889.unsupported ('excess HSA contributions from an earlier year that remain in your HSA'), which refuses f8889.line13/line16; eval of fixture stage16.refuse.f8889.unsupported_part2 shows the refusal reaching s1.line13, s2.line8, f1040.line24 and line37. |
| 1 | UNCLEAR | defect | i5329 p. 9: 'The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed'; f5329 p. 3 line 52a/54a (10% when corrected in the window). No Part IX lines exist; 'a required minimum distribution ... that you did not take' reads as missed entirely. |

Bugs: PENDING-2-1

## `retirement.special`

One defect (three findings): cases i1040gi pp. 28 and 30 route to Pub. 525/575/721 are missing from the list. Roth non-Q is refused by retirement.bad_code; the box 5 finding misreads the computation; rest WIDE/covered.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | retirement.bad_code refuses account roth_ira with any code other than qualified_roth_Q (codes T, J and others) and gates rolled, taxable and amount_a. Same ruling as T-008. |
| 1 | NARROW | defect | i1040gi p. 28: 'Fully taxable pensions and annuities also include military retirement pay shown on Form 1099-R. For details on military disability pensions, see Pub. 525.' Coded 7, a NO computes box 1 less box 5 as taxable (retirement.plan_simple); only code 3 is refused (bad_code). |
| 2 | NARROW | defect | i1040gi p. 30: 'If you are the beneficiary of an employee who died, see Pub. 575. If there is more than one beneficiary, see Pub. 575 or Pub. 721 to figure each beneficiary's taxable amount.' retirement.cost asks 'Your cost ... in the plan' with no allocation, so a shared annuity can take the whole cost. |
| 3 | NARROW | defect | i1040gi p. 30: 'See Pub. 575 for more details on rollovers, including special rules that apply to ... partial rollovers of property, and distributions under qualified domestic relations orders.' The tool subtracts a plain rollover amount. |
| 4 | WIDE | accepted WIDE | A fully taxable plan loan offset not rolled over is computed correctly; refusal safe. |
| 5 | UNCLEAR | accepted (covered / WIDE) | 'nondeductible contributions to any traditional IRA' says any, so a filer with basis answers YES; a 2025 conversion has its own Form 1099-R on which the filer answers YES, refusing the return. The over-reading (pension with IRA basis) is WIDE. |
| 6 | UNCLEAR | model error | retirement.plan_simple = box 1 less box 5 less the rollover for every plan distribution, the i1040gi p. 30 rule the finding quotes; a NO computes it, a YES is WIDE. Same ruling as T-008. |

Bugs: PENDING-2-2

## `s1.cod_unsupported`

One defect: the cash-method deductible-debt exception is screened only for box 3 interest and business debt; other WIDE/UNCLEAR findings accepted.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | defect | p4681 p. 6, Deductible Debt: 'If you use the cash method of accounting, you don't realize income from the cancellation of debt if the payment of the debt would have been a deductible expense.' A canceled medical bill answered NO is copied into line 8c (s1.cod_refused = s1.cod_amount). |
| 1 | WIDE | accepted WIDE | A fully taxable canceled student loan is refused; safe. |
| 2 | WIDE | accepted WIDE | Nonrecourse debt with collateral retained and a discount (p4681 p. 3) is taxable and computable; refusal safe. |
| 3 | UNCLEAR | accepted (minor UNCLEAR) | p4681 p. 6 balance-sheet test; the everyday reading ('can't pay my bills') tends to YES (WIDE). Optional gloss: 'your debts were more than the value of everything you owned, including retirement accounts, just before the cancellation'. |
| 4 | UNCLEAR | accepted (minor UNCLEAR) | f1099c p. 3 box 5 reads 'If checked, the debtor was personally liable', which tells the filer the polarity; a not-liable filer misreading to NO is computed correctly in the case p4681 p. 3 taxes (collateral retained) and foreclosure/abandonment is screened separately (box 7, Form 1099-A). |

Bugs: PENDING-2-3

## `s1.uc_unsupported`

One low defect: the contribution clause does not say payroll-withheld contributions count or that any year counts; WIDE findings accepted as in T-008.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Contributions with no 2025 compensation: line 7 is zero either way; refusal safe. |
| 1 | WIDE | accepted WIDE | Repayment of $3,000 or less is refused; accepted in T-008 (Pub. 525 not archived). |
| 2 | UNCLEAR | defect | i1040gi p. 89: 'If you made contributions to a governmental unemployment compensation program and you aren't itemizing deductions, reduce the amount you report on line 7 by those contributions.' Wage-withheld employee contributions are contributions; a NO leaves line 7 unreduced (s1.line7_figured = uc_paid - uc_repaid). |
| 3 | UNCLEAR | defect | Same sentence, untimed; T-008 reverted a 2025 limit because the instructions do not limit the year, but the question does not say so and a filer whose contributions were earlier can read it as 2025 only. |

Bugs: PENDING-2-4

## `sa.charity_limited`

No defect: every non-charitable item is screened by sa.unsupported, which gates the same eight lines; the two UNCLEARs compute correctly on NO.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sa.unsupported: 'a foreign tax or generation-skipping tax deduction' (gates sa.line6). |
| 1 | NARROW | covered | sa.unsupported: 'mortgage interest or points not on Form 1098' (gates sa.line8b). |
| 2 | NARROW | covered | sa.unsupported: 'mortgage interest or points not on Form 1098' (gates sa.line8c). |
| 3 | NARROW | covered | sa.unsupported: 'Any casualty or theft loss' (gates sa.line15). |
| 4 | NARROW | covered | sa.unsupported: 'a deduction from the Schedule A line 16 list other than gambling losses' (gates sa.line16). |
| 5 | NARROW | covered | sa.unsupported: 'including a disaster loss added to the standard deduction' (gates sa.line16, line17). |
| 6 | UNCLEAR | accepted (minor UNCLEAR) | Expired or currently non-deductible carryover: NO gives line 13 zero, which the finding itself says is correct; YES is WIDE. |
| 7 | UNCLEAR | model error | The appreciated-property reduction is not an income limit; it is asked in gift.deduction ('Deduction before income limits ... after required valuation/basis reductions'), which feeds sa.line12, so a NO computes it. |

## `sa.unsupported`

No defect: a charitable carryover is screened by sa.charity_limited on the same lines; the casualty finding is WIDE.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sa.charity_limited ('or carried over from a prior year') gates sa.line13 and sa.line17 among the same eight lines. Same ruling as T-008. |
| 1 | WIDE | accepted WIDE | A non-disaster personal casualty loss is not deductible (i1040sca p. 11); refusing it is safe. |

## `sb.line8`

Amount findings covered by sb.unsupported (all Schedule B screens gate sb.line2, line3, line6); one low defect: the question is narrower than the i1040sb p. 3 line 8 instruction.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sb.unsupported: 'a savings bond interest exclusion'. |
| 1 | NARROW | covered | sb.unsupported: 'Any nominee income, original issue discount reported in an amount other than on Form 1099-OID, accrued interest paid on a bond purchase, bond premium adjustment'. |
| 2 | NARROW | covered | sb.unsupported: 'Any nominee income' (gates sb.line6). |
| 3 | NARROW | covered | sb.unsupported: 'accrued market discount, a contingent payment debt instrument'. |
| 4 | WIDE | accepted WIDE | Foreign-trust facts do not change lines 2, 3 and 6; refusal safe (T-008). |
| 5 | UNCLEAR | defect | i1040sb p. 3: 'a loan of cash or marketable securities is generally considered to be a distribution' and 'If you were the grantor of, or transferor to, a foreign trust that existed during 2025, you may have to file Form 3520.' The question ('were grantor of ... a foreign trust during 2025') reads as acting in 2025, so line 8 prints No and the return computes. |

Bugs: PENDING-2-5

## `sc.inventory_other`

No defect: a 2025 accounting-method change is screened by sc.method_other (through sc.screened on sc.line1); the rest is WIDE or minor UNCLEAR.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | covered (derived refusal) | sc.method_other asks 'did you change your accounting method for 2025 (Form 3115 or a section 481(a) adjustment)'; it feeds sc.screened, which refuses sc.line1 and so the whole Schedule C. This is the i1040sc p. 15 line 35 case. |
| 1 | WIDE | accepted WIDE | Consistent use of another IRS-approved method (i1040sc p. 15 line 33): line 35 is last year's closing inventory and computable; refusal safe. |
| 2 | UNCLEAR | accepted (minor UNCLEAR) | Small business taxpayer not keeping an inventory (i1040sc p. 15): the method must 'clearly reflect income'; goods on hand at cost entered on lines 35/41 compute the same; risk is a filer entering zero, an input question rather than this screen. Optional gloss: 'Answer No only if you hold no goods for sale.' |
| 3 | UNCLEAR | accepted (leans WIDE) | Reading ordinary count/cost differences as a 'change' refuses a computed case; the narrow misreading is not plausible (it mirrors Schedule C line 34's own wording). |

## `scope.credits`

No defect: the Schedule 3 Part II amounts named are collected as inputs, not dropped.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | NARROW | model error | Line 10 is the input s3.line10 ('Amount paid with request for extension to file') and lines 13a-13z, including 13c and 13d, enter through s3.line14 ('Total other payments or refundable credits (supplied subtotal)'), both summed into s3.line15/f1040.line31; the reviewer did not have these inputs. |

## `scope.schedule1a`

Retired as a screen: Stage 12 (handoffs/HANDOFF-STAGE-12.md: 'scope.schedule1a is retired; Form 1040 line 13b copies Schedule 1-A line 38'); the id is no longer in forms/2025 and check_screens does not list it; the record is obsolete. Findings classed for the record.

| # | kind | class | deciding source / reason |
| --- | --- | --- | --- |
| 0 | WIDE | out of scope (obsolete) | Senior deduction phase-out is now computed (forms/2025/s1a.yaml, $75,000/$150,000 and 6%); no screen remains. |
| 1 | UNCLEAR | out of scope (obsolete) | Tips/overtime qualification is now asked by the Schedule 1-A inputs (s1a, tipjob, otjob), not this screen. |
| 2 | UNCLEAR | out of scope (obsolete) | No screen; f1040.line13b = s1a.line38. |
# PENDING defects

## PENDING-2-1 — `person.x_other`: partial or corrected RMD shortfall (finding 1; severity medium)

- **Quote.** f5329 p. 3, Part IX: "Complete this part if you did not receive the minimum required distribution from your
  qualified retirement plan. 52 a Minimum required distribution for 2025 from all qualified plans for which you received a
  distribution of the full amount of the excess accumulation during the correction window ... 54 a ... multiply the result
  by 10% (0.10) ... b ... multiply the result by 25% (0.25)". i5329 p. 9: "The additional tax is 25% of the excess
  accumulation, which is the difference between the amount that was required to be distributed and the amount that was
  actually distributed."
- **Case.** A filer age 75 had a $10,000 2025 IRA RMD and took $8,000; or took nothing in 2025 and made it up in 2026
  inside the correction window. Asked about "a required minimum distribution from an IRA or plan that you did not take",
  the first plausibly answers No (an RMD was taken) and the second may (it was taken, late).
- **Effect.** The tool has no Part IX lines (none in `forms/2025/f5329.yaml`); `person.x_other` is the only gate, on
  `f5329.l4` and `f5329.l49`. A No computes the return with the $500 (25% of $2,000) or 10% excise tax missing from
  Schedule 2 line 8 — tax understated.
- **Fix.** Replace the last item with: "or a required minimum distribution from an IRA or plan that you did not receive
  in full by its deadline (including a shortfall you made up later)".

## PENDING-2-2 — `retirement.special`: Pub. 525/575/721 cases missing from the list (findings 1, 2, 3; severity low)

- **Quotes.** i1040gi p. 28: "Fully taxable pensions and annuities also include military retirement pay shown on Form
  1099-R. For details on military disability pensions, see Pub. 525." i1040gi p. 30: "If you are the beneficiary of an
  employee who died, see Pub. 575. If there is more than one beneficiary, see Pub. 575 or Pub. 721 to figure each
  beneficiary's taxable amount." and "See Pub. 575 for more details on rollovers, including special rules that apply to
  rollovers from designated Roth accounts, partial rollovers of property, and distributions under qualified domestic
  relations orders."
- **Cases.** (a) A military disability pension on Form 1099-R with code 7 (code 3 is already refused for plans by
  `retirement.bad_code`); none of the listed disability items fits. (b) One of several beneficiaries of a deceased
  employee receiving an annuity with after-tax cost: `retirement.cost` asks "Your cost ... in the plan" with no
  allocation, so the whole cost can be entered. (c) A rollover of distributed property, or a QDRO distribution rolled over.
- **Effect.** A truthful No computes `retirement.plan_simple` (box 1 less box 5 less the rollover) or the Simplified
  Method with the entered cost. (a) can overstate income (the excludable part is taxed); (b) can understate it (cost
  recovered several times over); (c) applies a plain cash rollover. Pubs. 525/575/721 are not archived, so the correct
  amounts cannot be shown here; the archived text routes these cases outside the computation the tool encodes.
- **Fix.** Add to the list: "a military disability pension; an annuity you receive as the beneficiary of an employee who
  died, or that is shared among more than one beneficiary; a rollover of property other than cash, or of a distribution
  under a qualified domestic relations order".

## PENDING-2-3 — `s1.cod_unsupported`: deductible debt beyond box 3 interest (finding 0; severity low-medium)

- **Quote.** p4681 p. 6, Deductible Debt: "If you use the cash method of accounting, you don't realize income from the
  cancellation of debt if the payment of the debt would have been a deductible expense. This exception applies before the
  price reduction exception discussed next."
- **Case.** A filer with a $4,000 unpaid medical bill canceled by a collector (Form 1099-C, no box 3 interest, not
  business). The question reaches deductible debt only through "interest (Form 1099-C box 3) that would have been
  deductible" and "a business, rental or farm debt", so the filer answers No.
- **Effect.** `s1.cod_refused` copies `s1.cod_amount`, so $4,000 goes into Schedule 1 line 8c although the exception may
  exclude it (whether a medical bill "would have been a deductible expense" depends on itemizing and the floor, which is
  exactly what the tool does not decide). Income overstated.
- **Fix.** Reword that item: "it includes interest (Form 1099-C box 3) or any other amount (for example an unpaid medical
  bill) that would have been deductible if you had paid it". Optional, finding 3: gloss "insolvent" as "your debts were
  more than the value of everything you owned, including retirement accounts, just before the cancellation".

## PENDING-2-4 — `s1.uc_unsupported`: which contributions count (findings 2, 3; severity low)

- **Quote.** i1040gi p. 89: "If you made contributions to a governmental unemployment compensation program and you aren't
  itemizing deductions, reduce the amount you report on line 7 by those contributions."
- **Case.** A filer with unemployment compensation whose employee share of state unemployment insurance was withheld from
  wages (in 2025 or an earlier year) does not think of withholding as "contributions you made", or reads the untimed
  clause as 2025 only, and answers No.
- **Effect.** `s1.line7_figured` = `s1.uc_paid` − `s1.uc_repaid`; the contribution reduction is not applied and line 7 is
  overstated by the contributions (usually small).
- **Fix.** "Did you, in 2025 or any earlier year, make contributions to a governmental unemployment compensation program
  (including amounts withheld from your wages for it; not counting employer-paid tax, paid family leave or disability
  insurance contributions), or ...". This keeps the T-008 decision not to limit the year and states it.

## PENDING-2-5 — `sb.line8`: narrower than the line 8 instruction (finding 5; severity low)

- **Quote.** i1040sb p. 3, Line 8: "For this purpose, a loan of cash or marketable securities is generally considered to be
  a distribution ... If you were the grantor of, or transferor to, a foreign trust that existed during 2025, you may have to
  file Form 3520."
- **Case.** A filer who created a foreign trust in 2019 that still exists, or who borrowed cash from a foreign trust in
  2025, reads "were grantor of or transferor to, a foreign trust during 2025" as acting in 2025, and "distribution" as
  excluding a loan, and answers No.
- **Effect.** `sb.line8` is the printed line 8 answer, so the return prints No where the instruction calls for Yes, and the
  Form 3520/3520-A situation (and any grantor-trust income) passes without refusal. Lines 2, 3 and 6 themselves are
  unaffected (finding 4). T-008 accepted the form's own wording; the instruction text above is what decides the answer.
- **Fix.** "During 2025, did you receive a distribution from a foreign trust (a loan of cash or marketable securities
  counts), or were you the grantor of, or a transferor to, a foreign trust that existed at any time during 2025?"

# Notes

- Checks run (read-only): the gate map from `screen_review.load_lines/screens`; `check_screens.findings()` for currency;
  one `eval` of fixture `stage16.refuse.f8889.unsupported_part2` (refusal reaches `s1.line13`, `s2.line8`,
  `f1040.line24`). No model calls.
