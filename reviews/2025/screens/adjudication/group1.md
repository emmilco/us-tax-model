# Screen adjudication — group 1 (2026-10-30)

Rulings on the 15 group-1 screens of `reviews/2025/screens/screen_review.json` under `BRIEF.md` and the T-008 standard
(`screen_review.md`). Finding numbers are 0-based indexes into each screen's `findings`. Sources are
`sources/2025/<doc>.cols.txt` pages. Evals are read-only `node engine/dist/main.js eval` runs on fixture inputs with one
answer changed (scratch in `/tmp/adj-screens-g1/`).

Totals: 58 findings — 13 defect (9 PENDING bugs), 14 covered, 23 accepted WIDE, 5 model error, 3 out of scope / presentation.

## `dependent.kidnapped`

Defect: present tense ('is presumed') and 'your child' let a 2025 kidnapping (since ended) or a non-son/daughter child compute without the Pub. 501 rule; also the qualifying-relative branch is not gated. Rest WIDE.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | p501 p. 13, Kidnapped child: 'This treatment applies for all years until the earlier of' death determination or age 18; condition 3, 'In the year of the child's return, the child lived with you for more than half the part of the year following the date of the child's return.' A child kidnapped in 2025 and returned before the interview gets a truthful No; dependent.months (which lists only temporary absences) then gives fewer months, lived_half/eic_child are false and the CTC/EIC/HOH are denied where Pub. 501 may allow them. PENDING-1-1. |
| 1 | NARROW | defect | For the qualifying-child test the archived text says 'your child' (i1040gi p. 21; p501 p. 13), so a sibling answers No consistently with the source; but p501 p. 18 (qualifying relative) and p. 9 (head of household) apply the rule to 'a child', and the tool's own dependent.relationship enum defines 'child' to include descendants. A kidnapped household_member child (QR branch of dependent.qr_relationship, months = 12, not gated by the screen) answers No and fails the member-of-household test. Folded into PENDING-1-1. |
| 2 | WIDE | accepted WIDE | Refuses a child already meeting the time-lived test; safe. |
| 3 | UNCLEAR | accepted WIDE | p501 p. 13 resolves the phrase: 'someone who isn't a member of your family or the child's family'. A kidnapping by the child's relative is outside the rule, so No computes correctly and Yes refuses (safe). Either reading is safe; the PENDING-1-1 rewording adopts Pub. 501's phrase. |

Bugs: PENDING-1-1

## `dependent.other_claimant`

Re-ruled as round 1: the Form 8332 case is covered by dependent.divorced_rule; the rest is WIDE or source wording read literally.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | dependent.divorced_rule gates dependent.qualifying_child (forms/2025/dependent.yaml, qualifying_child refuses: other_claimant, divorced_rule, married), and its question names 'a Form 8332 release or a decree lets the noncustodial parent claim the child'. The EIC is unaffected by a release (custodial parent keeps it), so eic_child need not be gated. |
| 1 | WIDE | accepted WIDE | Sole-parent tie-breaker outcome equals the computation; refusal is safe. |
| 2 | UNCLEAR | accepted WIDE | The question repeats i1040gi p. 17 verbatim ('meets the conditions to be a qualifying child of any other person'); its literal reading (conditions met, whether or not the other person claims) answers Yes and refuses. A filer substituting 'will claim' departs from the text. Accepted as in round 1; see uncertainty in group1.md. |

## `f2441.plans_differ`

Defect (owner decision): same-maximum plans below $5,000 compute line 21 as one plan's maximum, but amb.2025.dc_plan_maximum's reason says the readings agree there, which is false for its own third reading (the sum, capped at $5,000). Finding 1 is within the same ambiguity.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | i2441 p. 5, Line 21: 'Enter on line 21 the maximum amount that you may exclude for the year under your dependent care plan ... Don't enter more than the maximum amount allowed under your dependent care plan.' Two plans each allowing $3,000: f2441.line21 = smaller_of($5,000, plan_max $3,000) = $3,000; reading 3 of the register gives $5,000. The owner's ruling (Stage 15, decision 6) rests on 'Where every plan allows the same maximum the readings agree'. PENDING-1-2. |
| 1 | UNCLEAR | covered | amb.2025.dc_plan_maximum: eligible-but-unused plan; Yes refuses, No takes the one plan's maximum under the chosen reading 1. The proposed PENDING-1-2 wording ('enrolled in') also settles it. |

Bugs: PENDING-1-2

## `f5695.joint_occupancy`

Defect: the 'so that each occupant completes their own Form 5695 for the same property' clause reads as a condition, letting a joint occupant whose housemate does not file, or who bought different items in the same limit category, answer No and take the full limit.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | i5695 p. 3, Joint occupancy: 'If the aggregate credit that would be allowed to all occupants for any item of property exceeds the credit limit below, then you must figure your allocable share ... The credit allocable to you is the credit limit for that property multiplied by a fraction. The numerator is the amount you paid and the denominator is the total amount paid by you and all other occupants.' Windows: filer pays $2,000, housemate $2,000, housemate does not file; No gives line 30 windows credit $600 (30% x $2,000, capped); allocable share is $600 x 2,000/4,000 = $300. PENDING-1-3. |
| 1 | WIDE | accepted WIDE | Joint occupants under every limit are refused although the computation would be right; safe. |
| 2 | UNCLEAR | defect | Same page: 'The denominator is the total amount paid by you and all other occupants for the corresponding properties'; limits are per category ('$600 for windows'). A housemate's separate windows aggregate with the filer's; reading 'the same property' as the same physical item gives No and the full limit. Folded into PENDING-1-3. |

Bugs: PENDING-1-3

## `f8889.unsupported`

Defect: 'contributions by you or your employer ... or ... to your spouse's Archer MSA' reads as limiting the spouse limb to contributions by you or your employer; line 4 counts any amount contributed to the spouse's Archer MSA.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | f8889 (2025) p. 1, line 4: 'If you or your spouse had family coverage under an HDHP at any time during 2025, also include any amount contributed to your spouse's Archer MSAs'. Spouse's employer contributes to spouse's Archer MSA, family HDHP coverage: a truthful No leaves f8889.line4 = 0 (hard-coded) and line 5/12 too high, so line 13 (HSA deduction) can be overstated. PENDING-1-4. |

Bugs: PENDING-1-4

## `f8962.alloc`

Defect: 'Did any Form 1095-A policy cover ...' with the example 'a child someone else claims' can be read as only the filer's own forms, missing condition 2b (the other tax family received the Form 1095-A that includes a member of your tax family). Finding 0 is WIDE.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Condition (2) unmet (separate accurate forms); refusal safe. |
| 1 | UNCLEAR | defect | i8962 p. 12, Allocating policy amounts, '2. Either: ... b. The other tax family received a Form 1095-A for the policy that includes a member of your tax family' and the example 'your ex-spouse enrolled a child whom you are claiming as a dependent'. A filer with their own Form 1095-A who claims a child on the ex-spouse's policy can answer No; lines 24/25 then omit the child's allocated premiums, SLCSP and APTC (excess APTC understated). PENDING-1-5. |

Bugs: PENDING-1-5

## `f8962.other`

Defect: the unpaid-premium limb omits 'not including extensions' and the 120-day rule after a successful eligibility appeal. HRA findings are WIDE.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | defect | i8962 p. 3: 'if you became eligible for APTC because of a successful eligibility appeal and you retroactively enrolled in the plan, then the portion of the enrollment premium for which you are responsible must be paid on or before the 120th day following the date of the appeals decision.' Paid after the 120th day but before the return due date: truthful No; the month computes as a coverage month. PENDING-1-6. |
| 1 | UNCLEAR | defect | i8962 p. 3: 'paid by the due date of your tax return (not including extensions)'; p. 4: 'unpaid as of the unextended due date'. An extended filer paying between the two dates can answer No. Folded into PENDING-1-6. |
| 2 | WIDE | accepted WIDE | An offered but unused QSEHRA is refused; safe. |
| 3 | WIDE | accepted WIDE | 'family member' outside the tax family is refused; safe. |

Bugs: PENDING-1-6

## `gift.special`

Defect: 'similar items' is undefined in the question and in gift.deduction, so a filer can under-group and stay at or below $5,000 per group (no Section B refusal). Other findings WIDE or safe either way.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Value prong is deliberate: i8283 p. 3 'A separate, qualified appraisal is required for any gift of property valued in excess of $5,000' (T-008 round 3). |
| 1 | WIDE | accepted WIDE | Category prongs without thresholds refuse Section A items; safe. |
| 2 | WIDE | accepted WIDE | 'Certain other securities' (i8283 p. 3, 2.d) refused; safe. |
| 3 | UNCLEAR | accepted WIDE | i8283 p. 9 defines publicly traded to include OTC securities with published quotations and mutual fund shares quoted daily. Yes refuses; No with gift.public_securities = Yes is Section A (correct); No with public_securities = No and a deduction over $5,000 is refused by gift.section_b. Every path is safe. |
| 4 | UNCLEAR | defect | i8283 p. 3, Similar Items of Property: 'Similar items of property are items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land, or buildings.' Two paintings at $3,000 each entered as two groups: gift.section_b (> $5,000) never fires and gift.special gets a No; the tool allows $6,000 where Section B and a qualified appraisal are required. PENDING-1-7. |

Bugs: PENDING-1-7

## `qbi.unsupported`

No defect: the reviewer saw only qbi.eligible; Schedule C QBI (f8995.line2) and the line 3 carryforward (qbi.carryforward) are computed elsewhere; K-1 items are refused by scope.schedule1.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | model error | qbi.carryforward asks 'The qualified business loss carryforward from line 16 of your 2024 Form 8995' and f8995.line3 takes it (forms/2025/qbi.yaml, f8995.yaml). Not ignored. |
| 1 | NARROW | model error | f8995.line2 is 'the qualified business income of the Schedule C businesses (sc.qbi)' (f8995.yaml note); qbi.eligible covers only the dividends limb. Interface gap of the review (gated line only). |
| 2 | WIDE | accepted WIDE | Non-business suspended items refused; safe. |
| 3 | WIDE | accepted WIDE | Pre-2018 suspended losses refused; safe. |
| 4 | UNCLEAR | covered | Any Schedule K-1 is refused by scope.schedule1 ('partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1)'), which refuses Form 1040 line 8/10 upstream of QBI; Form 1099-PATR is named in the question. |

## `refund.exc_tax`

No defect: the other Pub. 525 exceptions are screened by refund.not_2024 (items 1, 5), refund.exc_who (items 8, 9, nonresident) and oi8z.recovery (item 2); the question is not reached for non-itemizers.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | refund.not_2024 ('Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G)') gates refund.taxable, the line every refund passes. |
| 1 | NARROW | covered | Non-income-tax recoveries are line 8z items: oi8z.kind 'recovery (... real estate taxes, general sales taxes ...)' refused by oi8z.recovery. Note: amb.2025.refund_exceptions names a 'refund.other' that does not exist in forms/2025. |
| 2 | NARROW | covered | refund.not_2024 second limb ('did you make your last payment of 2024 estimated state or local income tax in 2025'). |
| 3 | NARROW | covered | refund.exc_who ('Could you be claimed as a dependent by someone else in 2024') gates refund.line1. |
| 4 | NARROW | covered | refund.exc_who third limb (refund from a jointly filed state return, not filing jointly with the same person). |
| 5 | NARROW | covered | refund.exc_who second limb (2024 Form 1040-NR). |
| 6 | WIDE | model error | Eval of stage16.refund.f1 with refund.itemized = false and exc_tax/exc_who withheld: refund.taxable = $0, s1.line1 = $0; refund.line1 is unknown only because it is not needed. The question is not reached for a non-itemizer. |
| 7 | WIDE | model error | Same eval: not reached when the 2024 worksheet does not apply (refund.worksheet false). |
| 8 | UNCLEAR | out of scope / presentation | The limb repeats i1040gi p. 89 item 4 verbatim; whether 'deduction' is before or after the SALT limit is the source's own ambiguity. Not ruled a defect; listed as an uncertainty. |

## `s1.alimony_unsupported`

Defect: non-alimony components other than child support (jointly owned home expenses under Pub. 504 Table 4, noncash settlements, community income, upkeep or use of the payer's property) and child-contingency reductions are not screened or excluded. Post-2018 modification is handled upstream.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | model error | s1.alimony and s1.alimony_received/paid already exclude it: 'and not changed after 2018 to expressly provide that alimony received isn't included in income' / 'do not include ... payments made after the agreement was changed'. The reviewer saw labels only. |
| 1 | NARROW | defect | p504 p. 13: 'Alimony doesn't include: Child support, Noncash property settlements, Payments that are your spouse's part of community income ..., Payments to keep up the payer's property, or Use of the payer's property' and 'If you owned the home jointly with your spouse, see Table 4' (p. 14: half the mortgage payments are alimony). A payer of the mortgage on a jointly owned home answers No and enters the whole payment (or none) on s1.alimony_paid; the amount questions do not define alimony. PENDING-1-8. |
| 2 | UNCLEAR | defect | p504 p. 16: reductions tied to a contingency relating to a child (or presumed so) make that part child support. An instrument with no designated child support but a reduction at a child's age: No gives the full payment as alimony. Folded into PENDING-1-8. |
| 3 | UNCLEAR | accepted WIDE | A decrease with no recapture owed: Yes refuses, No computes correctly. Either reading is safe. |
| 4 | WIDE | accepted WIDE | Past recapture years refused; safe. |
| 5 | WIDE | accepted WIDE | Second agreement with no includible 2025 alimony refused; safe. |
| 6 | WIDE | accepted WIDE | Fully paid child support plus alimony refused; safe. |

Bugs: PENDING-1-8

## `s1.line8_other`

No defect: WIDE examples, line 8z items are collected item by item in oi8z (unsupported kinds refused), and the stock-option example is safe either way.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Not-for-profit personal property rental refused via the 8l example; safe. |
| 1 | WIDE | accepted WIDE | Medicaid waiver payments not on line 1a/1d refused; safe. |
| 2 | UNCLEAR | covered | Line 8z items are entered in the oi8z collection ('insurance_dividends ... or other (any other taxable income for line 8z)'); every kind except RTAA and kickbacks is refused at the entry (oi8z note). |
| 3 | UNCLEAR | accepted WIDE | Stock option income all on line 1h: Yes refuses (safe), No computes correctly (line 8k is zero). |

## `sa.dependent`

Disaster-loss finding covered by sa.unsupported (derived refusal on sa.deduction). Defect: no screen follows i1040gi Step 4 question 2's referral to Pub. 596 for a decedent or a spouse who died in 2025; the EIC age test is computed from birth dates.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sa.unsupported asks 'Any casualty or theft loss (including a disaster loss added to the standard deduction)'. Eval (stage1 table.band.first with sa.unsupported = true): sa.itemizes, sa.deduction and f1040.line12e are refusals (gate sa.unsupported), sa.standard alone computes but feeds nothing printed. |
| 1 | NARROW | defect | i1040gi p. 42, EIC Step 4 question 2: 'If your spouse died in 2025 or if you are preparing a return for someone who died in 2025, see Pub. 596 before you answer.' eic.age_range counts birth-date flags only; no screen asks about a death (person.died_before_65 serves Schedule 1-A only). Pub. 596 is not archived, so the different rule (age at death, per secondary knowledge) is unconfirmed here; the defect is the unhonored referral. PENDING-1-9. |

Bugs: PENDING-1-9

## `sb.fbar_required`

Re-ruled as T-008: the line 2/3/6 adjustments are screened by sb.unsupported, which gates the same lines; the FBAR refusal is WIDE.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | NARROW | covered | sb.unsupported ('Any nominee income, ... accrued interest paid on a bond purchase, bond premium adjustment ...') refuses sb.line2 (sb.yaml line 98). |
| 1 | NARROW | covered | sb.unsupported names 'a savings bond interest exclusion' and refuses sb.line3. |
| 2 | NARROW | covered | sb.unsupported names 'Any nominee income' and refuses sb.line6. |
| 3 | WIDE | accepted WIDE | FBAR filers refused on lines 2, 3, 6; safe. |

## `sb.unsupported`

No defect: WIDE and catch-all wording; the OID wording affects only the Schedule B line 1 presentation because interest.amount asks the taxable amount.

| # | kind | class | deciding source / evidence |
| --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | Form 5471 duty refused; safe. |
| 1 | UNCLEAR | out of scope / presentation | interest.amount asks 'Taxable interest from this payer'; a filer reporting less than box 1/8 enters the taxable amount, so line 2 is right and only the 'OID Adjustment' subtraction layout (i1040sb p. 2) is missing. |
| 2 | UNCLEAR | out of scope / presentation | Catch-all 'other special treatment' (T-008: 'remaining items are WIDE or catch-all wording'). Taxable market discount on a tax-exempt bond is entered as taxable interest by interest.amount's own wording. |

# PENDING defects

## PENDING-1-1 — `dependent.kidnapped`: tense, "your child", and the qualifying-relative branch (findings 0, 1)

- **Quote.** p501 p. 13, Kidnapped child: "The child is presumed by law enforcement authorities to have been kidnapped by
  someone who isn't a member of your family or the child's family." "In the year of the child's return, the child lived
  with you for more than half the part of the year following the date of the child's return." "This treatment applies for
  all years until the earlier of: 1. The year there is a determination that the child is dead, or 2. The year the child would
  have reached age 18." p501 p. 18 (qualifying relative): "You can treat a child as your qualifying relative even if the
  child has been kidnapped"; p. 9 (head of household): "the child who is your qualifying person has been kidnapped".
- **Case.** (a) Your son is kidnapped in March 2025 and returned in November 2025 (or January 2026); asked "Is this person
  your child who is presumed ... kidnapped", you truthfully answer No. (b) A child of your household (relationship
  `household_member`) is kidnapped in 2025; the question says "your child", so you answer No.
- **Effect.** (a) `dependent.months` counts only the listed temporary absences, so the months are short; `lived_half` and
  `eic_child` are false and the CTC/ODC, EIC and head of household computed for this child are denied where Pub. 501 may
  allow them. (b) `dependent.qr_relationship` needs `dependent.months` = 12 for a household member and is not gated, so the
  child fails the qualifying-relative test. Both directions understate the filer's credits; neither over-claims.
- **Fix.** Reword: "Is this person a child who, at any time during 2025, was presumed by law enforcement authorities to
  have been kidnapped by someone who isn't a member of your family or the child's family (even if the child has since
  been returned)?" Add the same refusal to `dependent.qr_relationship` (or to its household-member branch). Severity: low.

## PENDING-1-2 — `f2441.plans_differ`: same-maximum plans under $5,000 (finding 0), for the owner

- **Quote.** i2441 p. 5, Line 21: "Enter on line 21 the maximum amount that you may exclude for the year under your
  dependent care plan ... Don't enter more than the maximum amount allowed under your dependent care plan."
- **Case.** You have two employers, each with a dependent care plan allowing $3,000. Plans do not "allow different maximum
  amounts", so you answer No and enter $3,000 for `f2441.plan_max`.
- **Effect.** Line 21 = $3,000. Reading 3 of `amb.2025.dc_plan_maximum` (the sum of the plans' maximums, not more than
  $5,000) gives $5,000. The register's reason, "Where every plan allows the same maximum the readings agree", is true of
  readings 1 and 2 only, so the owner's ruling rests on a false premise for this case.
- **Fix.** Either the owner confirms reading 1 for same-maximum plans and the register's reason is corrected, or the screen is
  widened to the cases where the readings can differ: "Were you (or your spouse, if filing jointly) enrolled in 2025 in two
  or more dependent care plans, any of which allows less than $5,000 to be excluded?" (also settles finding 1's "covered").
  Severity: low. Line 21 is understated, so too little is excluded (adverse to the filer).

## PENDING-1-3 — `f5695.joint_occupancy`: conditional-sounding clause (findings 0, 2)

- **Quote.** i5695 p. 3, Joint occupancy: "If the aggregate credit that would be allowed to all occupants for any item of
  property exceeds the credit limit below, then you must figure your allocable share of the credit from each property. The
  credit allocable to you is the credit limit for that property multiplied by a fraction. The numerator is the amount you
  paid and the denominator is the total amount paid by you and all other occupants for the corresponding properties." "•
  $600 for windows."
- **Case.** You and a housemate (not your spouse) each pay $2,000 for windows in the home you share. The housemate does
  not file Form 5695, or the windows are different windows. You read "so that each occupant completes their own Form 5695
  for the same property" as a condition and answer No.
- **Effect.** Line 30 includes the windows credit at min(30% × $2,000, $600) = $600. The allocable share is
  $600 × 2,000 / 4,000 = $300. The credit is over-claimed by $300, and the line 32a box is not checked.
- **Fix.** "Did you occupy the home jointly with someone other than your spouse on a joint return (whether or not the other
  occupant claims the credit, and whether you paid for the same items or different ones)?" Keep the neighbor parenthetical.
  Severity: low to medium. The credit is over-claimed.

## PENDING-1-4 — `f8889.unsupported`: spouse's Archer MSA contributions by anyone (finding 0)

- **Quote.** f8889 (2025) p. 1, line 4: "If you or your spouse had family coverage under an HDHP at any time during 2025,
  also include any amount contributed to your spouse's Archer MSAs".
- **Case.** You have family HDHP coverage. Your spouse's employer contributes to your spouse's Archer MSA. The screen's
  "contributions by you or your employer to an Archer MSA ..., or ... to your spouse's Archer MSA" reads as contributions by
  you or your employer, so you answer No.
- **Effect.** `f8889.line4` is fixed at zero, so line 5 and the limit on line 12 are too high, and line 13 (the HSA
  deduction) can be overstated.
- **Fix.** "... contributions by you or your employer to your Archer MSA for 2025 (Form 8853), or, if you or your spouse
  had family coverage under an HDHP at any time during 2025, any contribution by anyone to your spouse's Archer MSA; ...".
  Severity: low (Archer MSAs are rare).

## PENDING-1-5 — `f8962.alloc`: a policy whose Form 1095-A went to the other tax family (finding 1)

- **Quote.** i8962 p. 12, Allocating policy amounts: "2. Either: ... b. The other tax family received a Form 1095-A for the
  policy that includes a member of your tax family." The page's example: "your ex-spouse enrolled a child whom you are
  claiming as a dependent".
- **Case.** You hold a Form 1095-A for your own policy. You claim a child whom your former spouse enrolled on the former
  spouse's policy, and only the former spouse received that form. "Did any Form 1095-A policy cover ..." can be read as the
  forms you hold, and the example "a child someone else claims" points the other way, so you answer No.
- **Effect.** Lines 24 and 25 leave out the child's allocated enrollment premium, SLCSP and APTC, which understates the
  excess APTC to repay (Schedule 2 line 1a).
- **Fix.** "Did any Marketplace policy, including one whose Form 1095-A went to someone else, cover someone in your tax
  family and also someone who is not in it (for example a former spouse, a child someone else claims, or a child you claim
  whom someone else enrolled), or ...". Severity: low to medium.
- **Related, outside this screen.** A filer who holds no Form 1095-A gets no Form 8962 at all (`f8962.any`). The case where
  APTC was paid for a member of the filer's tax family on another family's policy then needs its own check.

## PENDING-1-6 — `f8962.other`: unextended due date and the appeal 120-day rule (findings 0, 1)

- **Quote.** i8962 p. 3: "paid by the due date of your tax return (not including extensions) ... However, if you became
  eligible for APTC because of a successful eligibility appeal and you retroactively enrolled in the plan, then the portion
  of the enrollment premium for which you are responsible must be paid on or before the 120th day following the date of the
  appeals decision." p. 4: "unpaid as of the unextended due date".
- **Case.** (a) You file on extension and pay a month's share after April 15, 2026 but before the extended date. (b) You
  enrolled retroactively after an appeal and paid after the 120th day but before the due date. Either way you answer No.
- **Effect.** The month is computed as a coverage month with the full premium, so the PTC is overstated or the excess APTC
  understated.
- **Fix.** "... any part of a month's premium was not paid by the due date of your return, not including extensions (or,
  for coverage you enrolled in retroactively after a successful eligibility appeal, by the 120th day after the appeals
  decision) ...". Severity: low.

## PENDING-1-7 — `gift.special`: "similar items" undefined (finding 4)

- **Quote.** i8283 p. 3: "Similar items of property are items of the same general category or type, such as coin
  collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land, or buildings." The same page: "A
  separate, qualified appraisal is required for any gift of property valued in excess of $5,000".
- **Case.** You give two paintings worth $3,000 each to two museums and enter them as two groups of $3,000.
- **Effect.** `gift.section_b` (a group over $5,000) never fires, and you answer No to `gift.special`. `gift.allowed`
  passes $6,000 to Schedule A where Section B and a qualified appraisal are required.
- **Fix.** Add the definition to `gift.deduction`'s source and to the screen: "... for one item or for similar items
  (items of the same general category or type, such as coin collections, paintings, books, clothing, jewelry, nonpublicly
  traded stock, land or buildings) given to all donees together ...". Severity: low.

## PENDING-1-8 — `s1.alimony_unsupported`: other non-alimony parts and child contingencies (findings 1, 2)

- **Quote.** p504 p. 13: "Alimony doesn't include: • Child support, • Noncash property settlements, • Payments that are your
  spouse's part of community income ..., • Payments to keep up the payer's property, or • Use of the payer's property." "If
  you owned the home jointly with your spouse, see Table 4" (p. 14, Table 4: half of the mortgage payments on a jointly
  owned home are alimony). p. 16: a reduction tied to a contingency relating to a child is treated as child support.
- **Case.** (a) Under a 2017 agreement you pay all the mortgage payments on a home you and your former spouse own jointly.
  (b) The instrument designates no child support, but the payment drops when the child turns 18.
- **Effect.** The screen names only child support, so you answer No. In (a), `s1.alimony_paid` (which does not define
  alimony) takes the whole payment or none, where half is alimony. In (b), the part that is child support is deducted (or
  included) as alimony.
- **Fix.** Add to the screen: "payments for a home either of you owns (mortgage, real estate taxes, insurance, repairs;
  Pub. 504 Table 4); or payments of which part is child support, including an amount the instrument reduces on a
  contingency relating to a child (such as reaching a certain age) or at a time associated with one". Add "cash payments
  only (not noncash property settlements, your spouse's part of community income, or keeping up or use of the payer's
  property)" to `s1.alimony_received` and `s1.alimony_paid`. Severity: low.

## PENDING-1-9 — Missing screen: EIC age test for a decedent or a spouse who died in 2025 (sa.dependent finding 1)

- **Quote.** i1040gi p. 42, EIC Step 4 question 2: "If your spouse died in 2025 or if you are preparing a return for someone
  who died in 2025, see Pub. 596 before you answer."
- **Case.** A final return for a filer born in June 2000 who died in February 2025, or a joint return with a spouse who
  died in 2025.
- **Effect.** `eic.age_range` uses the birth-date flags (born after December 31, 1960 and before January 2, 2001) without
  the referral, and no screen asks about a death. `person.died_before_65` serves Schedule 1-A only. Pub. 596 is not
  archived. By secondary knowledge (not verified here), it tests age at the time of death, which can differ in either
  direction.
- **Fix.** A new screen, for example `eic.decedent`: "Did your spouse die in 2025, or is this a return for someone who died
  in 2025?" It should refuse `eic.age_range` (or `eic.step4`) with the Pub. 596 referral, or Pub. 596 should be archived and
  the rule encoded. Severity: low to medium, since the EIC can be over- or under-claimed.

# Uncertainties

- `dependent.other_claimant` finding 2: the question repeats i1040gi p. 17's own phrase. A filer who reads it as "will
  claim" can let a non-parent claim through when a parent with a higher AGI does not claim. This is accepted as in round 1,
  but it rests on a literal reading.
- `refund.exc_tax` finding 8: the item 4 SALT-cap reading is the source's own ambiguity. It is not ruled a defect.
- PENDING-1-2 is a request for an owner decision, not a clear source contradiction.
- PENDING-1-9's substantive rule comes from Pub. 596, which is not archived.
- `amb.2025.refund_exceptions` names a gate `refund.other` that does not exist. The coverage it describes is provided by
  `oi8z.recovery`, and the register should be corrected.
