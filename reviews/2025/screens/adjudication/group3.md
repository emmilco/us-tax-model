# Screen adjudication, group 3 (2026-10-30)

Brief: `BRIEF.md`. Screens: 15; findings: 58. Classes: covered 24, accepted WIDE 20, out of scope / presentation 8, defect 4 (PENDING-3-1 to PENDING-3-4), model error 2.
Evaluations used `node engine/dist/main.js eval` on inputs from `fixtures/2025/stage1.json` (`table.band.first`), `stage12.json` (`stage12.mfj.tips_overtime`) and the dependent of `tcw.hoh.b1`, with the one screen changed; scratch in `/tmp/adj-screens-g3/`. All screens except sd.carryover have a current prompt hash (recomputed with `prompt_for`).

## `dependent.multiple_support`

NARROW findings are all caught by derived refusals through dependent.qualifying_child (divorced_rule, kidnapped via lived_half, other_claimant) or by dependent.income_exception on the same line; WIDE accepted; 'others' UNCLEAR leans WIDE.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | dependent.qualifying_relative reads dependent.qualifying_child, which refuses on dependent.divorced_rule ('for example because a Form 8332 release or a decree lets the noncustodial parent claim the child'). Eval: months 0, supported false, divorced_rule yes -> qualifying_relative refusal gate dependent.divorced_rule. |
| 1 | NARROW | covered | dependent.lived_half refuses on dependent.kidnapped; derived through qualifying_child. Eval: kidnapped yes -> qualifying_relative refusal gate dependent.kidnapped. |
| 2 | NARROW | covered | dependent.income_exception (disabled and gross income not under $5,200) is a refusal gate on dependent.qualifying_relative (forms/2025/dependent.yaml); i1040gi p. 20 sheltered workshop exception falls under it. |
| 3 | NARROW | covered | dependent.qualifying_child refuses on dependent.other_claimant ('meets the conditions to be the qualifying child of any other person for 2025'); derived to qualifying_relative. |
| 4 | WIDE | accepted WIDE | Refuses a contributor who does not claim the person; tool's false would be right. Safe. |
| 5 | WIDE | accepted WIDE | Support alone triggers YES though another test fails. Safe. |
| 6 | UNCLEAR | accepted WIDE | i1040gi p. 21: 'you and another person(s) provided more than half'. Government sources or the person are not persons who could claim the dependent, so NO is correct for the filer+public-source case and supported=false computes not-QR correctly; the other reading gives YES (refusal). Either reading is safe. |

## `f5695.business_use`

One PENDING: the parenthetical 'for a business' narrows the IRS 'nonbusiness purposes' test for rental or other income-producing use; the omitted-item finding presumes a misentered cost; fuel cell WIDE accepted.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | model error | Premise is a filer who omits a cost the cost inputs ask for ('Qualified solar electric property costs you paid ...'). A truthful entry includes the item, then the screen is YES. Not a screen gap. |
| 1 | WIDE | accepted WIDE | Fuel cell costs (line 8) are separately refused by f5695.line7a on line 11; refusing 6a/30 too is safe. |
| 2 | UNCLEAR | defect | i5695 p. 1 Costs: 'If less than 80% of the use of an item is for nonbusiness purposes, only that portion of the costs that is allocable to the nonbusiness use can be used'. The gloss '(that is, is more than 20% of its use for a business)' lets a landlord renting part of the home read rental use as nonbusiness, answer NO, and get the credit on the full cost (lines 6a, 30 overstated). |

## `f5695.line7a`

WIDE accepted; condominium/cooperative UNCLEAR is the form's own line 7a wording, and a NO there only omits a credit.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Property installed but nothing paid: refused though line 11 would be zero. Safe. |
| 1 | UNCLEAR | out of scope / presentation | The question is f5695 line 7a's printed wording; i5695 p. 4 'Any qualified fuel cell property costs must have been for your main home'. Building property 'in connection with' the condo/coop main home reads naturally as YES; the adverse reading only understates a credit. Accepted as minor wording. |

## `f8960.unsupported`

Refund, Schedule 1 line 8z items and Schedule A casualty losses are caught by f8960.refund, s1.line8_other/scope.schedule1 and sa.unsupported; one PENDING: 'disposition adjustment' does not reach NUA gain excluded on line 5b.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | f8960.refund ('Any recovery or refund in 2025 of an amount deducted on an earlier Form 8960 (for example a state or local income tax refund ...)') gates every listed f8960 line including line 7. |
| 1 | NARROW | covered | i8960 p. 13 places these items on Schedule 1 line 8z (Form 8814, substitute payments, NPC payments); s1.line8_other refuses them. Eval (stage12.mfj.tips_overtime base): s1.line8_other yes -> f8960.line17 and s2.line12 refuse; scope.schedule1 yes -> f8960.line13/17 refuse. Annuity contract gain falls under the screen's 'Any annuity ... income'. |
| 2 | NARROW | covered | sa.unsupported names 'Any casualty or theft loss'. Eval: sa.unsupported yes -> f1040.line24 refuses (and f8960.line17 refuses when not itemizing), so the return cannot complete. |
| 3 | WIDE | accepted WIDE | Early withdrawal penalty is computed (line 10 = s1.line18); a YES only refuses. Safe. |
| 4 | WIDE | accepted WIDE | Qualified-plan annuities swept in by 'Any annuity'. Safe. |
| 5 | UNCLEAR | defect | i8960 p. 9: line 5b includes 'Gain attributable to net unrealized appreciation (NUA) in employer securities held by a qualified plan' ... 'is a distribution within the meaning of section 1411(c)(5) and isn't included in NII'. No screen names NUA (grep of forms/ and interview questions); a NO computes line 5b as zero and NII includes the NUA gain. The capital loss carryforward adjustment is covered by f8960.carryforward_adj on line 5b. |
| 6 | UNCLEAR | out of scope / presentation | Catch-all; the line 7 items in i8960 p. 13 are each reached by a named clause or a sibling/derived gate (rows 0-2); remaining gap handled by PENDING-3-2. |

## `person.rrta`

NARROW findings are caught by f8959.unsupported on the lines that consume person.medicare5/6; WIDE and minor UNCLEAR accepted.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | person.medicare5/6 are read only by f8959.line1/line19, which refuse on f8959.unsupported ('uncollected Medicare tax in Form W-2 box 12 (codes B or N)'); s2.other also names codes B and N. Eval: f8959.unsupported yes -> s2.line21 and f1040.line24 refuse. |
| 1 | NARROW | covered | f8959.unsupported names 'Medicare wages on a wage statement from a U.S. territory (such as Form 499R-2/W-2PR)'; same consumers. |
| 2 | WIDE | accepted WIDE | Single railroad employer under the threshold refused. Safe. |
| 3 | UNCLEAR | out of scope / presentation | iw2w3 p. 12 requires the label 'RRTA compensation' alongside 'Tier 1 tax' etc. in box 14; the question says 'railroad retirement compensation or taxes (W-2 box 14)'. Minor; previously accepted (T-008). |
| 4 | UNCLEAR | out of scope / presentation | Form CT-2 year unstated; the adverse readings are WIDE (another year) or a representative who files CT-2 quarterly and has filed for 2025. Minor. |

## `refund.box8`

One PENDING: the screen keys on a checked box, so a refund of a business-only income tax with no Form 1099-G (which refund.received asks to include) is not screened; WIDE accepted.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | f1099g p. 5 Box 8: 'the amount in box 2 is attributable to an income tax that applies exclusively to income from a trade or business ... If taxable, report the amount in box 2 on Schedule C or F'. refund.received includes 'any refund for which you received no Form 1099-G'; for such a refund box8 is NO and the refund is run through the itemized-deduction worksheet (zero if the filer did not itemize) instead of Schedule C or F. |
| 1 | WIDE | accepted WIDE | Box 8 checked with no earlier deduction refused. Safe. |

## `refund.exc_who`

The 2025 nonresident-alien case is refused for the whole return by scope.other_income; WIDE accepted; 'these refunds' refers to refund.received, asked immediately before.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | scope.other_income asks 'Any nonresident alien status (you or your spouse, for any part of 2025)' and gates scope.ready and f1040.line8. Eval: scope.other_income yes -> f1040.line11a, line15, line24 refuse. |
| 1 | WIDE | accepted WIDE | Non-itemizer refused although the worksheet gives zero. Safe. |
| 2 | WIDE | accepted WIDE | Asked only in the refund sequence; even so, refusal is safe. |
| 3 | UNCLEAR | out of scope / presentation | Interview order (stage4-2025.yaml, sales-2025.yaml): refund.received ('refunds, credits or offsets ... including any part you chose to apply ... and any part offset against a debt') precedes this question, which supplies the antecedent. |

## `s2.amt`

Other Schedule 2 amounts are caught by s2.other on the same lines; WIDE accepted; whether Form 6251 is required is decided by i6251, which is not archived (known limit).

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | s2.other ('Any amount on Schedule 2 other than ...', naming household employment taxes and uncollected tax on tips/group-term life) gates s2.line2, line3 and line21. |
| 1 | WIDE | accepted WIDE | Filing requirement without AMT owed refused. Safe. |
| 2 | UNCLEAR | out of scope / presentation | i1040gi p. 112 line 2: 'See the Instructions for Form 6251 to see if you must file the form'. The deciding test lives in i6251, not in the archive; s2.other also names 'the alternative minimum tax'. No archived text to sharpen the wording; recorded as a known limit. |

## `s2.other`

Allocated tips and Form 8919 are caught by f8959.unsupported (and scope.other_income); the Form 8962 finding misreads the tool, which computes line 1a; other Form 5329 taxes are refused by person.x_other.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | f8959.unsupported names 'tips not reported to your employer or allocated tips in Form W-2 box 8 (Form 4137)'; it gates f8959 lines feeding s2.line11 -> s2.line21. Eval (stage1 and stage12 bases): f8959.unsupported yes -> s2.line11 and f1040.line24 refuse, so the return cannot complete. |
| 1 | NARROW | covered | f8959.unsupported names 'Form 8919 wages'; scope.other_income names 'wages or tips not on a Form W-2'. Both refuse the return. |
| 2 | NARROW | model error | s2.line1a is computed from f8962.line29 when f8962.any; line 3 = line1z + line2. The repayment is not set to zero. (Side note: the question's exception list does not name the Form 8962 repayment, so a literal reader with a repayment answers YES; that is WIDE, not NARROW.) |
| 3 | UNCLEAR | covered | s2.line8 sums person.x_tax; person.x_other ('excess contributions to a traditional or Roth IRA for an earlier year that are still in the IRA; excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account; ... a required minimum distribution ... that you did not take') refuses it. Eval: person[taxpayer].x_other yes -> s2.line8, s2.line21, f1040.line24 refuse. |

## `sb.form8938`

Nominee, accrued interest, OID, premium and savings-bond findings are caught by sb.unsupported on the same three lines (T-008 ruling holds); WIDE accepted; 'required' follows the Schedule B text.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sb.unsupported ('Any nominee income ...') gates sb.line2, sb.line3, sb.line6. |
| 1 | NARROW | covered | sb.unsupported names 'accrued interest paid on a bond purchase, bond premium adjustment' and OID 'reported in an amount other than on Form 1099-OID' (plus 'other special treatment'); same lines. |
| 2 | NARROW | covered | sb.unsupported names 'a savings bond interest exclusion'; gates sb.line3. |
| 3 | NARROW | covered | sb.unsupported 'Any nominee income' gates sb.line6. |
| 4 | WIDE | accepted WIDE | Form 8938 filers refused though lines compute. Safe. |
| 5 | UNCLEAR | out of scope / presentation | i1040sb p. 2 states the requirement without thresholds; the filer must determine it under the Form 8938 instructions, as with sb.fbar_required. Accepted (T-008). |

## `scope.other_income`

Every NARROW/UNCLEAR item has its own screen on scope.ready or f1040.line8 (scope.schedule1, scope.schedule1a, scope.other_line16, scope.credits); Schedule C losses are supported; WIDE accepted.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | scope.schedule1 (gates f1040.line8 and scope.ready) names 'a net operating loss deduction' and 'farm income (Schedule F)'; Schedule C income or loss is computed by the tool. |
| 1 | WIDE | accepted WIDE | Nontaxable receipts swept in by 'other income'. Safe. |
| 2 | UNCLEAR | covered | Schedule 1 adjustments: scope.schedule1; Schedule 1-A: scope.schedule1a ('asked separately'); Form 4972: scope.other_line16 and retirement.special; adoption credit: scope.credits. scope.ready refuses on scope.schedule1, scope.credits, scope.other_line16 (forms/2025/scope.yaml). |
| 3 | UNCLEAR | covered | scope.schedule1 names 'sales of business property (Form 4797)'; sd.other_forms names Form 4797 on the Schedule D lines. |

## `sd.carryover`

Not a screen in the current YAML: sd.carryover ('Did line 21 of your 2024 Schedule D show a loss?') is no longer a refusal gate; it selects the Capital Loss Carryover Worksheet (clcw), which the tool computes. The record (old question, model '', cost 0) is orphaned and check_screens.py does not list it. Findings 0-1 are caught by sd.other_forms; finding 2 is resolved by the worksheet.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sd.other_forms ('or capital gains or losses on a Schedule K-1') gates sd.line5 and sd.line12. |
| 1 | NARROW | covered | sd.other_forms names Forms 4797, 2439, 6252, 4684, 6781 and 8824; gates sd.line4 and sd.line11. |
| 2 | UNCLEAR | out of scope / presentation | Obsolete: the current question asks the factual 2024 line 21 test from i1040sd p. 10, and sd.line6/line14 take clcw.line8/line13. |

## `sd.other_forms`

WIDE and safe-either-way UNCLEAR findings accepted; the K-1 section 1231 case is refused by scope.schedule1.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Form 4797 Part II-only filer refused. Safe. |
| 1 | WIDE | accepted WIDE | Personal casualty loss that never reaches Schedule D refused. Safe. |
| 2 | UNCLEAR | accepted WIDE | Either answer is safe: YES refuses; NO leaves lines 4 and 11 at their correct zero. |
| 3 | UNCLEAR | accepted WIDE | Fully deferred like-kind exchange: YES refuses; NO is correct (nothing recognized). |
| 4 | UNCLEAR | covered | scope.schedule1 names 'partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1)' and 'sales of business property (Form 4797)', and refuses f1040.line8 and scope.ready. |

## `ssb.terror_disability`

One PENDING: 'injuries covered by' the Victim Compensation Fund is narrower than the IRS 'eligible for coverage'; the full-retirement-age finding leans WIDE (T-008).

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | i1040gi p. 31: 'In the case of the September 11 attacks, injuries eligible for coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack.' A filer who never claimed can read 'covered by' as 'compensated by' and answer NO; ssb.line1 then includes the excludable benefits. |
| 1 | UNCLEAR | accepted WIDE | Benefits after full retirement age: a YES refuses a case the tool computes; a filer with excludable months answers YES correctly. Safe (T-008 ruling). |

## `w2.box12_userra`

WIDE only.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Year-designated code G from a nongovernmental 457(b) refused though line 2 excludes it. Safe. |

# PENDING defects

## PENDING-3-1 — `f5695.business_use`: the gloss narrows 'nonbusiness purposes' (severity low)

- **Quote:** i5695 (2025) p. 1, Costs: "If less than 80% of the use of an item is for nonbusiness purposes, only that portion of the costs that is allocable to the nonbusiness use can be used to determine either credit."
- **Case:** a filer rents out part of the home (or uses an item more than 20% for another income-producing purpose) and reads the parenthetical "(that is, is more than 20% of its use for a business)" as excluding rental, so answers NO.
- **Effect:** f5695.line6a / line30 include the full cost instead of the nonbusiness share; the residential clean energy or home improvement credit is overstated.
- **Fix:** keep the IRS clause and widen the gloss: "(that is, is more than 20% of its use for a business, for renting out or for another income-producing purpose)". The archived text does not define nonbusiness use, so this widening is the safe direction; it does not resolve the reading itself.

## PENDING-3-2 — `f8960.unsupported`: 'a disposition adjustment' does not reach NUA gain (severity low to moderate)

- **Quote:** i8960 (2025) p. 9, line 5b: "Gain attributable to net unrealized appreciation (NUA) in employer securities held by a qualified plan"; "Any gain attributable to NUA ... that you realize on a disposition of employer securities held by a qualified plan is a distribution within the meaning of section 1411(c)(5) and isn't included in NII."
- **Case:** a filer above the MAGI threshold sells employer stock received in an earlier lump-sum distribution with NUA; the 2025 sale is an ordinary 1099-B sale, and no screen names NUA (no match for 'unrealized' or 'employer securities' in forms/ or interview questions). The filer does not recognize this as 'a disposition adjustment' and answers NO.
- **Effect:** f8960.line5b is the fixed zero, so line 5a's gain including the NUA portion stays in NII; the NIIT on Schedule 2 line 12 is overstated by 3.8% of the NUA gain (up to the line 16 limit). Inferred from the expressions (line 5b copies f8960.zero); not run through eval.
- **Fix:** gloss the clause: "a disposition adjustment (Form 8960 line 5b or 5c, for example gain on employer securities attributable to net unrealized appreciation from a qualified plan, or the sale of property held in a trade or business or of an interest in a partnership or S corporation)".

## PENDING-3-3 — `refund.box8`: refunds of business-only income tax without a Form 1099-G (severity low)

- **Quote:** f1099g (Rev. 3-2024) p. 5, Box 8: "If this box is checked, the amount in box 2 is attributable to an income tax that applies exclusively to income from a trade or business and is not a tax of general application. If taxable, report the amount in box 2 on Schedule C or F (Form 1040), as appropriate."; i1040gi p. 88: "Report any taxable refund you received even if you didn't receive Form 1099-G."
- **Case:** refund.received asks the filer to include "any refund for which you received no Form 1099-G". A Schedule C filer refunded a business-only income tax deducted on Schedule C, with no Form 1099-G (or a box 8 the payer left unchecked), answers the box-8 question NO.
- **Effect:** refund.taxable runs the refund through the itemized-deduction worksheet (zero for a non-itemizer) instead of the recovery going on Schedule C; the business income is understated.
- **Fix:** "Is any of these refunds of a state or local income tax that applies only to income from a trade or business (for example, box 8 is checked on the Form 1099-G that reports it)?"

## PENDING-3-4 — `ssb.terror_disability`: 'covered by' versus 'eligible for coverage' (severity low)

- **Quote:** i1040gi (2025) p. 31, Disability payments: "In the case of the September 11 attacks, injuries eligible for coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack."
- **Case:** a filer receiving SSDI for a September 11 injury eligible for the Fund who never filed a claim reads "injuries covered by the September 11 Victim Compensation Fund" as "compensated by" and answers NO.
- **Effect:** ssb.line1 includes excludable benefits; ssb.line2 and the taxable-benefit computation follow, overstating income.
- **Fix:** replace the parenthetical with "(for the September 11 attacks, any injury eligible for coverage by the September 11 Victim Compensation Fund, whether or not you made a claim)".

# Notes for the coordinator

- `sd.carryover` is no longer a refusal gate (it now selects the clcw worksheet); its record in `screen_review.json` is orphaned (old question, model '', cost 0). Consider retiring it rather than ruling it.
- `s2.other` finding 2 is a model error, but the question's exception list omits the Form 8962 repayment the tool computes (s2.line1a), so a filer reading it literally answers YES and is refused. This costs coverage only (WIDE). Naming the repayment in the parenthetical would fix it.
- `f8960.unsupported` / `sa.unsupported`: with `sa.elect_itemize` yes, f8960.line17 computed 0 while f1040.line24 refused. The return is still refused; recorded as observed, not investigated.
