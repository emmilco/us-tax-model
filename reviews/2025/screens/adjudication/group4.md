# Screen adjudication, group 4: round 2 re-reviews (2026-10-30)

Scope: the 23 screens in `/tmp/s21/stale_screens2.txt`, excluding `refund.box8`. Each was re-reviewed after the round-1 fixes BUG-0228 to BUG-0249. For every screen I checked (a) whether the round-1 defect is closed in the current YAML and (b) whether the rewording opened a new NARROW gap. Every reviewed question matches the current `forms/2025` text, and each entry's `prompt_sha` is copied into `group4.json`. Standard: `screen_review.md` (NARROW is dangerous; WIDE is safe and accepted; sibling and derived gates count as cover).

Evals run (read-only): (1) the stage8 household-member dependent with `dependent.kidnapped` = yes; (2) `eic.died_2025` = yes on stage14.actc.wsb, stage15.f8880.s8 and stage15.f8880.s14 (filers with a qualifying child).

Two of the 11 defects were introduced by this round's rewording: PENDING-4-1 (kidnapped, 'during 2025') and PENDING-4-9 (unemployment, 'employer-paid tax'). PENDING-4-10 was made worse by one. The others are older wording that the re-review surfaced. Every round-1 PENDING for these screens is closed except one part: the qualifying-relative half of PENDING-1-1, which BUG-0234 left ungated on purpose.

## `dependent.divorced_rule`

Round-1 PENDING-0-1 closed (the question now tells the custodial parent who signed the release to answer yes); the rewording adds only WIDE refusals; the third-party claimant is covered by dependent.other_claimant. Bugs: none.

Round 1: PENDING-0-1 (BUG-0228): closed. `prompt_sha` 696407ed2a4e…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi p. 20 | A post-2008 decree without Form 8332 now draws a yes (from the BUG-0228 clause) and is refused; Step 1 would compute the child correctly for the custodial parent. Widening introduced by the fix; safe. |
| 1 | WIDE | accepted WIDE | i1040gi p. 20 | Release exists but conditions 1-3 fail: yes refuses a case the tool computes. Safe (round 1). |
| 2 | UNCLEAR | accepted WIDE | i1040gi p. 20 | Parents' status alone: a yes refuses (safe); a no is the correct answer and the tool computes the ordinary case. |
| 3 | UNCLEAR | accepted WIDE | i1040gi p. 20 | Release only for another year, or revoked: yes refuses (safe); no is correct (no release applies to 2025, ordinary Step 1). The revocation-copy attachment is a filing step, not a computed line. |
| 4 | UNCLEAR | covered | i1040gi pp. 17, 20; forms/2025/dependent.yaml | Grandparent living with the child and the custodial parent: the child is the custodial parent's qualifying child, so dependent.other_claimant is yes and refuses dependent.qualifying_child (refuses: other_claimant, divorced_rule, married). |

## `dependent.kidnapped`

Round-1 wording defect closed (tense, 'a child', Pub. 501 phrase), but the new 'at any time during 2025' anchor drops a presumption made after 2025 for a 2025 kidnapping (PENDING-4-1, low); the qualifying-relative branch stays ungated by BUG-0234's choice (understatement only); the rest WIDE. Bugs: PENDING-4-1.

Round 1: PENDING-1-1 (BUG-0234): part (a) tense closed; part (b) the qualifying-relative branch was deliberately not gated (BUG-0234 note). Eval (stage8 household_member dependent with kidnapped=yes): lived_half refuses but qualifying_child short-circuits to false on qc_relationship, so qualifying_relative still computes. Understates only; left as BUG-0234 decided. `prompt_sha` 94406e81acc6…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | defect | p501 p. 13 | PENDING-4-1. The rule ties the year to when the kidnapping occurred and sets no deadline for the presumption; the BUG-0234 wording ('at any time during 2025, was presumed') lets a filer whose 2025 kidnapping was presumed in early 2026 answer no truthfully. dependent.months then counts the absence, lived_half/eic_child can be false and the CTC/EIC/HOH are denied (understatement). Introduced by the rewording (the old present tense caught it). |
| 1 | WIDE | accepted WIDE | p501 p. 13 | Child already meets the time-lived test: refused though computed correctly. Safe. |
| 2 | WIDE | accepted WIDE | p501 p. 13 | Statements 2 and 3 not met: refused; the ordinary months count would be right. Safe. |
| 3 | WIDE | accepted WIDE | p501 p. 13 | Treatment ended (age 18 / death in an earlier year): refused; ordinary count correct. Safe. |
| 4 | UNCLEAR | accepted WIDE | i1040gi p. 21; p501 p. 13 | An adult or a sibling reading 'a child' as covering them answers yes and is refused (safe); the reading that excludes them computes the ordinary test, which is correct for an adult past the age-18 cutoff and matches i1040gi's 'your child' for the qualifying-child test. |

## `dependent.married`

Round-1 PENDING-0-2 closed (both marriage questions now name a joint return filed by the surviving spouse); both findings are WIDE as in round 1. Bugs: none.

Round 1: PENDING-0-2 (BUG-0229): closed; dependent.joint_return carries the same clause. `prompt_sha` 07e7735bc49a…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi pp. 21, 44 | Married, no joint return or refund-only joint return: refused on qualifying_child/qualifying_relative though computable; still needed for eic_child. Safe (round 1). |
| 1 | WIDE | accepted WIDE | i1040gi pp. 17, 41, 44 | Refund-only joint return by a person whose spouse died: refused though dependent.joint_return carves it out. Safe (round 1). |

## `dependent.other_claimant`

No round-1 defect; re-reviewed because its siblings changed. NARROW findings are covered by dependent.divorced_rule and dependent.married; the rest WIDE or the source's own wording. Bugs: none.

Round 1: No round-1 defect. `prompt_sha` 4690c3d384d6…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040gi p. 20; forms/2025/dependent.yaml | dependent.divorced_rule gates dependent.qualifying_child and now tells both the custodial parent who signed the release and the noncustodial parent using it to answer yes. EIC is unaffected by a release. |
| 1 | NARROW | covered | i1040gi p. 44; forms/2025/dependent.yaml | A child married at the end of 2025 answers yes to dependent.married, which gates dependent.eic_child (and qualifying_child, qualifying_relative). |
| 2 | WIDE | accepted WIDE | i1040gi p. 17 | EIC branch refuses a child who fails the support test for the dependent rules. Safe. |
| 3 | WIDE | accepted WIDE | i1040gi pp. 21, 44 | Sole-parent tie-breaker: refusal of a correct computation. Safe. |
| 4 | UNCLEAR | accepted WIDE | i1040gi pp. 17, 21 | The question repeats i1040gi p. 17 ('meets the conditions to be a qualifying child of any other person'); the literal reading answers yes and refuses. Round-1 ruling kept. |

## `eic.died_2025`

New screen (BUG-0241) closes round-1 PENDING-1-9; the one finding is a model error: a filer with a qualifying child never reaches eic.age_range, and eval shows the refusal does not reach line 27a. Bugs: none.

Round 1: PENDING-1-9 (BUG-0241): closed by the new screen. `prompt_sha` 24a5687f3c8e…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | model error | i1040gi p. 41; forms/2025/eic.yaml; eval | eic.has_qc = false is tested before eic.step4/eic.age_range, and the engine short-circuits. Eval of stage14.actc.wsb, stage15.f8880.s8 and stage15.f8880.s14 with eic.died_2025 = yes: eic.age_range refuses but f1040.line27a is unchanged (e.g. $3,154). The finding's condition ('unless the tool asks this question only on the no-qualifying-child path') holds in effect. |

## `f5695.business_use`

Round-1 PENDING-3-1 closed (the gloss now names renting out and other income-producing use); the reviewer found no gap. Bugs: none.

Round 1: PENDING-3-1 (BUG-0247): closed. `prompt_sha` 9b2533b7b5c8…

No findings (verdict COVERS).

## `f5695.joint_occupancy`

Round-1 PENDING-1-3 closed (no conditional clause; same or different items); two WIDE accepted; 'the home' misses Section B property at a second, shared home (PENDING-4-2, low); the timing ambiguity is safe. Bugs: PENDING-4-2.

Round 1: PENDING-1-3 (BUG-0235): closed. `prompt_sha` e722c6e7f46c…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i5695 p. 3 | Co-occupant paid nothing: fraction is 1, refusal unnecessary. Safe. |
| 1 | WIDE | accepted WIDE | i5695 p. 3 | Aggregate within every limit: refusal unnecessary. Safe. |
| 2 | UNCLEAR | defect | i5695 pp. 3, 6 | PENDING-4-2. Residential energy property is for 'a home that you used during 2025' (p. 3) and line 21c asks for 'each home'; the f5695 cost questions say 'for a home in the United States'. A filer who lives alone in the main home and has a heat pump at a second home shared with a sibling can read 'the home' as the main home and answer no; line 30 then takes the full category limit where the allocable share applies (credit overstated). Pre-existing wording. |
| 3 | UNCLEAR | accepted WIDE | i5695 pp. 1, 3 | 'Did you occupy' is past tense with no limit; the readings a filer with a 2025 co-occupant who paid would take give yes. Any-past-time reading refuses more. Safe. |

## `f8889.unsupported`

Round-1 PENDING-1-4 closed (any contribution by anyone to the spouse's Archer MSA); the reviewer found no gap. Bugs: none.

Round 1: PENDING-1-4 (BUG-0236): closed. `prompt_sha` 9e28cfd08c1e…

No findings (verdict COVERS).

## `f8960.unsupported`

Round-1 PENDING-3-2 closed (NUA named under line 5b); most line 7 and line 13 items are covered by sibling or derived gates; section 404(k) dividends paid directly on Form 1099-DIV have no gate (PENDING-4-3, low). Bugs: PENDING-4-3.

Round 1: PENDING-3-2 (BUG-0248): closed. `prompt_sha` cea788a24d67…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i8960 pp. 14-15; forms/2025/f8960.yaml | f8960.refund ('Any recovery or refund in 2025 of an amount deducted on an earlier Form 8960 ...') gates 11 f8960 lines including line 7 (round 1). |
| 1 | NARROW | covered | i8960 p. 13; forms/2025/s1.yaml | These are Schedule 1 line 8z items; s1.line8_other refuses them, and scope.schedule1 refuses f8960 lines 13/17 (round-1 eval). Form 8814 is also named in scope.other_line16. |
| 2 | NARROW | covered | i8960 p. 13; forms/2025/sa.yaml | Casualty and theft losses: sa.unsupported ('Any casualty or theft loss') refuses (round-1 eval). Life insurance contract gain: the Form 1099-R input offers only traditional_ira, roth_ira or plan (retirement.account), so a contract surrender has no supported entry; see uncertainties. |
| 3 | NARROW | defect | i8960 pp. 7, 13; i1099div p. 4 | PENDING-4-3 for section 404(k) dividends: paid directly by the corporation they are in Form 1099-DIV box 1a (i1099div p. 4), so they are on line 2, and i8960 requires a negative line 7 modification. No screen names them (no match for 404(k) or ESOP outside retirement.yaml's Form 8880 question). NIIT is overstated. Self-charged interest needs a loan to the filer's own partnership or S corporation, whose Schedule K-1 makes the filer answer yes here ('pass-through income') and to scope.schedule1: covered. |
| 4 | NARROW | covered | i8960 p. 9; forms/2025/f8960.yaml | f8960.carryforward_adj gates line 5b for a capital loss carryover with a 2024 Net Gains and Losses Worksheet line 2(i) amount (round 1). |
| 5 | WIDE | accepted WIDE | i8960 p. 13 | Early withdrawal penalty is computed on line 10; a yes only refuses. Safe. |
| 6 | UNCLEAR | covered | i8960 p. 13; forms/2025/scope.yaml | A Schedule K-1 (Form 1041) beneficiary answers yes to scope.schedule1 ('estates or trusts (Schedule E or a Schedule K-1)'), which refuses f8960 lines 13/17 (round-1 eval). |
| 7 | UNCLEAR | covered | i8960 p. 22; forms/2025/scope.yaml | Indirect ownership runs through a partnership, S corporation, estate or trust (Schedule K-1, scope.schedule1) or a foreign corporation (itself a CFC/PFIC holding); a section 1291 holding also draws scope.other_line16 (Form 8621). |
| 8 | UNCLEAR | accepted WIDE | f8960 line 3; i8960 p. 9 | 'Any annuity' sweeps in qualified-plan annuities: refusal only. Safe (round 1). |

## `f8962.alloc`

Round-1 PENDING-1-5 closed (a policy whose Form 1095-A went only to someone else; a child you claim whom someone else enrolled); finding 0 WIDE; finding 1 is caught by the question's own first limb. Bugs: none.

Round 1: PENDING-1-5 (BUG-0237): closed. The round-1 side note (a filer holding no Form 1095-A gets no Form 8962, f8962.any) is outside this screen and still open. `prompt_sha` ad1000871299…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i8962 p. 12 | Condition 2 unmet (each family has an accurate Form 1095-A): refused though computable. Safe. |
| 1 | UNCLEAR | covered | i8962 pp. 3, 12-13 | A former spouse divorced during 2025 is not in the filer's 2025 tax family, so a policy that covered both in earlier months is 'a policy that covered someone in your tax family and also someone who is not in it'. The first limb names 'a former spouse' as its first example, so the filer answers yes there whatever 'while enrolled' means. |

## `f8962.other`

Round-1 PENDING-1-6 closed (unextended due date, 120-day rule); the lawfully present alien and dependent-filer findings are covered; eligibility for other minimum essential coverage has no screen (PENDING-4-4, low to medium); HRA findings WIDE. Bugs: PENDING-4-4.

Round 1: PENDING-1-6 (BUG-0238): closed. `prompt_sha` 5f5fb0245004…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | model error | i8962 p. 9; forms/2025/f8962.yaml | f8962.alien_below asks this exact question, and f8962.alien_branch (Form 1095-A, line 5 < 100, alien_below) refuses f8962.line24. The reviewer saw only the applicable-taxpayer label. |
| 1 | NARROW | defect | i8962 pp. 3-6, 15 | PENDING-4-4. 'An individual in your tax family who is eligible for MEC ... for a month is not in your coverage family for that month' (p. 5). No screen asks about it; the only route is f1095a's 'correct applicable SLCSP premium if column B is ... wrong', which does not say MEC eligibility makes column B wrong (p. 15, Example 3). A filer who took an affordable employer offer mid-year without telling the Marketplace answers no; the months keep the full SLCSP and PTC, understating the excess APTC. |
| 2 | NARROW | covered | i8962 pp. 3, 9; forms/2025/sa.yaml | sa.dependent ('Can someone claim you or your spouse as a dependent for 2025 ...') refuses the standard deduction (sa.yaml) and the EIC, so the return does not complete for a claimable filer on the standard deduction. Itemizers are not caught, so this is a return-level backstop rather than a gate on lines 24/25; see uncertainties. |
| 3 | WIDE | accepted WIDE | i8962 pp. 1, 3 | A QSEHRA that was offered but did not cover anyone: refused. Safe (round 1). |
| 4 | WIDE | accepted WIDE | i8962 p. 3 | HRA of a relative outside the tax family: refused. Safe (round 1). |
| 5 | UNCLEAR | accepted WIDE | i8962 p. 3 | 'Family member' read broadly (relatives) refuses more; read as the tax family, it matches the IRS rule. Safe either way. |

## `gift.special`

Round-1 PENDING-1-7 closed (similar items defined here and in gift.deduction); WIDE findings accepted; 'publicly traded securities' is undefined in this question and in gift.public_securities, so an over-$5,000 gift of thinly traded stock can compute (PENDING-4-5, low). Bugs: PENDING-4-5.

Round 1: PENDING-1-7 (BUG-0239): closed. `prompt_sha` 5c3202601366…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | defect | i8283 p. 9 | PENDING-4-5. i8283 p. 9: publicly traded means '(a) listed on a recognized stock exchange whose quotations are published daily; (b) regularly traded on a national or regional over-the-counter market; or (c) quoted daily in a national newspaper ... mutual fund shares'. A $12,000 gift of stock that has a ticker but is not regularly traded answers no here (the exception) and yes to gift.public_securities ('Is this group publicly traded securities?', no definition), so gift.section_b is false and gift.allowed passes $12,000 with no Section B or appraisal. Round 1 accepted the parallel finding on the assumption the filer knows the p. 9 definition; neither question states it. |
| 1 | WIDE | accepted WIDE | i8283 p. 3 | Partial or restricted interests at $5,000 or less: refused. Safe. |
| 2 | WIDE | accepted WIDE | i8283 p. 3 | Vehicles, intellectual property, inventory reportable in Section A: refused. Safe. |
| 3 | WIDE | accepted WIDE | i8283 p. 3 | 'Certain other securities': refused. Safe (round 1). |
| 4 | UNCLEAR | accepted WIDE | i8283 pp. 3, 9 | Mutual fund shares read as not publicly traded: yes here, or no to gift.public_securities and gift.section_b refuses. Safe either way (round 1). |

## `person.x_other`

Round-1 PENDING-2-1 closed (an RMD not received in full, including a shortfall made up later); the HSA carryover is covered by f8889.unsupported; the present-tense 'are still in the IRA' lets an earlier excess removed in 2026 escape the 2025 6% tax (PENDING-4-6, low to medium); the rest WIDE. Bugs: PENDING-4-6.

Round 1: PENDING-2-1 (BUG-0242): closed. `prompt_sha` a08c66227c6e…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | f5329 p. 2; forms/2025/f8889.yaml | A filer with a 2025 Form 8889 is asked f8889.unsupported ('excess HSA contributions from an earlier year that remain in your HSA'), which refuses f8889.line13/line16; round-1 eval showed the refusal reaching f1040 lines 24 and 37. |
| 1 | NARROW | defect | f5329 p. 1, lines 16-17; forms/2025/person.yaml | PENDING-4-6. Line 17 taxes 6% of the smaller of line 16 or 'the value of your traditional IRAs on December 31, 2025', and only 2025 distributions reduce the carryover. A filer with a 2023 excess that stayed in the IRA through 2025 and was withdrawn in February 2026 truthfully answers no to 'are still in the IRA'. person.ira_excess has the same present tense and is asked only with a 2025 contribution. No Part III/IV lines exist, so the 6% tax is missing from Schedule 2 line 8. Pre-existing wording. |
| 2 | WIDE | accepted WIDE | i5329 p. 9 | RMD shortfall belonging to another year's return: refused. Safe. |
| 3 | WIDE | accepted WIDE | i5329 p. 9 | Returned ABLE excess: refused. Safe. |
| 4 | UNCLEAR | accepted WIDE | f5329 pp. 1-2 | Untimed past-year items: an any-year reading answers yes and refuses (safe); the 2025 reading is correct. |
| 5 | UNCLEAR | accepted WIDE | f5329 p. 2 | HSA excess already cleared: yes refuses (safe); no is correct. |

## `refund.not_2024`

Round-1 PENDING-0-3 closed (any 2024 tax paid in 2025); the other worksheet exceptions are covered by refund.exc_tax and refund.exc_who; a 2024 tax paid before 2024 is still unscreened (PENDING-4-7, very low); WIDE accepted. Bugs: PENDING-4-7.

Round 1: PENDING-0-3 (BUG-0230): closed. `prompt_sha` 46e2e9b74315…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | defect | p525 p. 24 | PENDING-4-7. 'If you receive a refund or other recovery that is for amounts you paid in 2 or more separate years, you must allocate, on a pro rata basis'. A 2024 estimated payment made in December 2023 (deducted in 2023) is not asked about. The filer answers no, and the worksheet treats the whole refund as a recovery of tax paid in 2024. Rare. |
| 1 | NARROW | covered | i1040gi pp. 88-89; forms/2025/refund.yaml | Exceptions 2-4 and 6-9 are asked by refund.exc_tax (AMT, unused credits, 0% rate, refund over the income-minus-sales-tax deduction) and refund.exc_who (dependent, 1040-NR, joint state return), both gating refund.line1. |
| 2 | WIDE | accepted WIDE | i1040gi p. 88 | Non-itemizer or sales-tax elector refused though the taxable refund is zero. Safe. |
| 3 | WIDE | accepted WIDE | p525 p. 24; i1040gi p. 89 | A 2025 payment to a different state or a locality draws yes: refused though the worksheet applies. Widening introduced by BUG-0230; safe. |

## `retirement.special`

Round-1 PENDING-2-2 closed (military disability pension, beneficiary or shared annuity, property or QDRO rollover named); the remaining findings repeat round-1 rulings. Bugs: none.

Round 1: PENDING-2-2 (BUG-0243): closed. `prompt_sha` a04d0663d49f…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040gi p. 27; forms/2025/retirement.yaml | retirement.bad_code refuses a roth_ira distribution with any code other than qualified_roth_Q and gates rolled, taxable and amount_a (round 1, T-008). |
| 1 | UNCLEAR | accepted WIDE | i1040gi p. 27 | 'Nondeductible contributions to any traditional IRA' says any, so a filer with basis answers yes; a 2025 conversion has its own Form 1099-R on which the filer answers yes, refusing f1040 line 4b. Over-reading is WIDE (round 1). |
| 2 | UNCLEAR | model error | i1040gi p. 30; forms/2025/retirement.yaml | retirement.plan_simple is box 1 less box 5 less the rollover for every plan distribution, the p. 30 rule the finding quotes; a no computes it correctly (round 1, T-008). |

## `s1.alimony_unsupported`

Round-1 PENDING-1-8 closed (home payments, child contingencies, and cash-only amount questions); the post-2018 modification and noncash/community items are excluded by the amount questions; a part that must continue after the recipient's death is not screened (PENDING-4-8, low); the rest WIDE or safe. Bugs: PENDING-4-8.

Round 1: PENDING-1-8 (BUG-0240): closed. `prompt_sha` d10d9608daaa…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | defect | p504 p. 15 | PENDING-4-8. 'If any part of payments you make must continue to be made for any period after your spouse's death, that part of your payments isn't alimony whether made before or after the death.' Not in the screen's list of non-alimony parts, nor in s1.alimony_received/paid. A $30,000 payment of which $10,000 must continue after death is entered whole; $10,000 too much is deducted and included. Pre-existing wording. |
| 1 | NARROW | covered | p504 p. 13; forms/2025/s1.yaml | s1.alimony_received and s1.alimony_paid now say 'cash payments only, so do not include child support, noncash property settlements, your spouse's part of community income, or payments to keep up or the use of ... property' (BUG-0240). |
| 2 | NARROW | model error | i1040gi p. 89; forms/2025/s1.yaml | s1.alimony and both amount questions exclude agreements changed after 2018 to make alimony non-includible (round 1). |
| 3 | WIDE | accepted WIDE | p504 p. 13 | Home owned only by the recipient: refused though fully alimony. Widening introduced by BUG-0240; safe. |
| 4 | WIDE | accepted WIDE | p504 p. 16 | Decrease with no 2025 recapture: refused. Safe. |
| 5 | WIDE | accepted WIDE | p504 p. 12 | Post-2018 instruments: refused, no effect on these lines. Safe. |
| 6 | WIDE | accepted WIDE | p504 p. 13 | Fully paid separately stated child support: refused. Safe. |
| 7 | UNCLEAR | accepted WIDE | p504 pp. 13-14 | 'A home either of you owns' includes a home both own (each owns it); a strained reading that excludes joint ownership is the only route to no. The question also cites Pub. 504 Table 4, the joint-ownership table. |
| 8 | UNCLEAR | accepted WIDE | p504 pp. 15-16 | 'Associated with' is looser than 'clearly associated'; the loose reading refuses more. Safe. |

## `s1.cod_unsupported`

Round-1 PENDING-2-3 closed (any other amount deductible if paid); the short-sale finding is covered (p4681's own short-sale example uses the canceled amount, and the property sale is refused by scope.other_income); the rest WIDE. Bugs: none.

Round 1: PENDING-2-3 (BUG-0244): closed. `prompt_sha` a30db9007c7b…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | p4681 pp. 4, 10; forms/2025/scope.yaml | p4681 p. 10, Example 3 (short sale): the lender cancels 'the remaining $115,000 of the outstanding $735,000 debt' and that $115,000 is the canceled debt: the Form 1099-C box 2 amount the tool enters. The gain or loss on selling the property is not a supported securities sale, so scope.other_income ('other income ... outside ... supported securities sales') refuses. |
| 1 | UNCLEAR | accepted WIDE | p525 p. 20 | The 'would have been deductible' qualifier read as also covering box 3 interest: a filer with nondeductible interest answers yes and is refused (safe); the other reading is correct. |
| 2 | WIDE | accepted WIDE | p4681 p. 4 | Taxable nonbusiness student loan: refused. Safe. |
| 3 | WIDE | accepted WIDE | p4681 p. 3 | Nonrecourse discount with collateral kept: refused though computable. Safe. |

## `s1.uc_unsupported`

Round-1 PENDING-2-4 closed (wage withholding and any year named); WIDE accepted; the new 'not counting employer-paid tax' carve-out can lead a self-employed filer who paid for elective state coverage to answer no (PENDING-4-9, very low). Bugs: PENDING-4-9.

Round 1: PENDING-2-4 (BUG-0245): closed. `prompt_sha` c4aa7b67287a…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | WIDE | accepted WIDE | i1040gi p. 89 | Contributions with no 2025 compensation: line 7 zero either way. Safe. |
| 1 | WIDE | accepted WIDE | i1040gi p. 89 | Repayment of $3,000 or less: refused (T-008). Safe. |
| 2 | UNCLEAR | defect | i1040gi p. 89 | PENDING-4-9. 'If you made contributions to a governmental unemployment compensation program and you aren't itemizing deductions, reduce the amount you report on line 7 by those contributions.' The BUG-0245 carve-out 'not counting employer-paid tax' can be read by a self-employed person who paid for their own elective coverage as excluding their payment, so they answer no and line 7 is not reduced (income overstated). Introduced by the rewording; rare. |

## `sales.special`

Round-1 PENDING-0-4 closed (metal ETFs and trusts named); the former-rental and installment findings are covered by scope.other_income and sd.other_forms; 'holding such property' can be read as section 1250 property only (PENDING-4-10, very low); WIDE accepted. Bugs: PENDING-4-10.

Round 1: PENDING-0-4 (BUG-0231): closed. `prompt_sha` b5ecf467534b…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040sd p. 11; forms/2025/scope.yaml, sales.yaml | The sales collection is 'manually classified securities transactions'. Selling a former rental house is not a supported securities sale, so scope.other_income ('other income ... outside ... supported securities sales') is yes and refuses. |
| 1 | NARROW | covered | i1040sd p. 11; forms/2025/sd.yaml | An installment payment belongs on Form 6252, which sd.other_forms names; it gates sd lines 4, 5, 6, 11, 12, 14 and others. It is also not a securities sale (scope.other_income). |
| 2 | WIDE | accepted WIDE | i1040sd pp. 11-12 | S corporation or trust interest holding section 1250 property: refused. Safe (round 1). |
| 3 | WIDE | accepted WIDE | i1040sd p. 11 | Short-term collectibles or section 1250 property: refused. Safe (round 1). |
| 4 | UNCLEAR | defect | i1040sd p. 11 | PENDING-4-10. Line 18 includes gain on 'an interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation of collectibles'. 'Holding such property' follows 'depreciable real property (section 1250 property)', and BUG-0231's parenthetical put more distance between it and 'collectibles'. A long-term sale of S corporation stock (a security) in a company holding appreciated art can be answered no, and the 28% part is taxed at 15/20%. Metal ETFs and trusts are now named. |

## `sb.line8`

Round-1 PENDING-2-5 closed (loans count; a trust that existed at any time during 2025); the grantor-trust owner is outside the line 8 question and the gated lines; WIDE accepted. Bugs: none.

Round 1: PENDING-2-5 (BUG-0246): closed. The opening 'During 2025' remains from the form's own wording; the added 'that existed at any time during 2025' sets the time anchor on the trust, as i1040sb p. 3 does. `prompt_sha` bac1d7745a6c…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | out of scope / presentation | i1040sb p. 3; f1040sb line 8; forms/2025/sb.yaml | Schedule B line 8 asks only about a distribution, a grantor or a transferor. The p. 3 sentence on owners under the grantor trust rules concerns the trust's Form 3520-A, not this return. The gated lines (sb.line2, line3, line6) do not change, and the printed No answers the form's question. |
| 1 | WIDE | accepted WIDE | i1040sb p. 3 | A loan outside the 'generally' rule draws yes: refused. Safe (widening from BUG-0246). |
| 2 | WIDE | accepted WIDE | i1040sb p. 3 | Grantor or transferor with no Form 3520 requirement: refused; lines unaffected. Safe. |
| 3 | UNCLEAR | accepted WIDE | i1040sb p. 3 | Transfer before 2025 to a trust still in existence: the clause 'a foreign trust that existed at any time during 2025' points to yes. A reading that keeps the opening 'During 2025' for the grantor limb prints No on line 8, and lines 2, 3 and 6 are unaffected. The residual comes from the form's own line 8 wording. No action needed. |

## `scope.other_line16`

Round-1 PENDING-0-5 closed (the Form 8615 conditions are stated and match i1040gi p. 36); passive Schedule C is covered; Schedule J is elective; section 965(i) falls under the opening clause; WIDE accepted. Bugs: none.

Round 1: PENDING-0-5 (BUG-0232): closed. `prompt_sha` fa3680b1daae…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040gi p. 40; forms/2025/sc.yaml, scope.yaml | sc.passive -> sc.screened refuses sc.line1, and scope.other_income asks about 'income or loss from a passive activity' (round 1). |
| 1 | NARROW | out of scope / presentation | i1040gi p. 36 | Schedule J is an election ('your tax may be less if you choose'); a no computes the ordinary tax correctly (round 1). |
| 2 | UNCLEAR | out of scope / presentation | i1040gi p. 36 | A section 965(i) triggering event is 'additional Form 1040 line 16 tax' under the opening clause, and 'including' does not limit the list. Section 965 filers also have section 962/CFC facts the list names. Rare; no change needed. |
| 3 | WIDE | accepted WIDE | i1040gi p. 34 | Form 8621 with no line 16e tax: refused. Safe (round 1). |
| 4 | WIDE | accepted WIDE | i1040gi p. 36 | January 1 birthday rule: actual age gives a yes for a filer treated as one year older. Refused. Safe. The rule only ever makes a filer older, so no NARROW reading. |

## `scope.schedule1`

Round-1 PENDING-0-6 closed (the three clergy groups are named); the NARROW findings are covered by sibling gates as in round 1, but 'wages from a church' omits qualified church-controlled organizations (PENDING-4-11, low); WIDE accepted. Bugs: PENDING-4-11.

Round 1: PENDING-0-6 (BUG-0233): closed. `prompt_sha` a378653f24c5…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | NARROW | covered | i1040gi p. 40; forms/2025/sc.yaml, scope.yaml | Passive Schedule C: sc.passive / scope.other_income (round 1). |
| 1 | NARROW | covered | i1040gi p. 104; forms/2025/s1.yaml | s1a.line5_calc is gated by s1.sc_1a (sc.tips_ot) (round 1). |
| 2 | NARROW | covered | i1040gi p. 108; forms/2025/s1.yaml | s1a.line14b_calc is gated by s1.sc_1a; 1099-MISC box 3 outside Schedule C is refused by oi8z.figured (round 1). |
| 3 | NARROW | covered | i1040s8812 p. 8; forms/2025/sd.yaml, person.yaml | A section 1256 dealer answers yes to sd.other_forms (Form 6781) and person.se_screen (round 1). |
| 4 | WIDE | accepted WIDE | i1040gi pp. 42-43 | Minister with W-2 only and Form 4361: refused. Safe (round 1). |
| 5 | WIDE | accepted WIDE | i1040gi p. 42 | Church wages under $108.28: refused. Safe (round 1). |
| 6 | WIDE | accepted WIDE | i1040gi p. 40 | Rental of personal property in a trade or business: refused. Safe. |
| 7 | UNCLEAR | defect | i1040sse p. 1; i1040gi p. 11; p334 p. 44 | PENDING-4-11. Church employee income is wages from 'a church or qualified church-controlled organization that has a certificate in effect electing an exemption' (i1040sse p. 1). The question's gloss 'wages from a church that elected exemption' (also in person.se_screen) lets a filer employed by an electing church-controlled school or hospital answer no. Effect: EIC Step 5 uses line 1z with no adjustment, and no SE tax is figured on wages of $108.28 or more. f8959.unsupported uses the bare term 'church employee income' and may catch a filer who knows it. |
| 8 | UNCLEAR | accepted WIDE | i1040gi p. 43 | The list names 'income as a minister ...' and 'church employee income' after 'including', so a filer reads the named items as part of the question. Either reading that matters leads to yes. Safe. |

## `ssb.terror_disability`

Round-1 PENDING-3-4 closed ('eligible for coverage ... whether or not you made a claim'); the full-retirement-age finding remains WIDE (T-008). Bugs: none.

Round 1: PENDING-3-4 (BUG-0249): closed. `prompt_sha` 32b055c485c0…

| finding | kind | class | deciding source | reason |
| --- | --- | --- | --- | --- |
| 0 | UNCLEAR | accepted WIDE | i1040gi p. 31 | Benefits after full retirement age read as disability payments: yes refuses what the tool computes. Safe (T-008, round 1). |


# PENDING defects

## PENDING-4-1: `dependent.kidnapped`, finding 0 (NARROW; severity low; introduced by BUG-0234)

- **Quote.** p501 p. 13, Kidnapped child: "1. The child is presumed by law enforcement authorities to have been kidnapped by someone who isn't a member of your family or the child's family. 2. In the year the kidnapping occurred, the child lived with you for more than half of the part of the year before the date of the kidnapping." There is no deadline for the presumption.
- **Case.** A child disappears in August 2025. Law enforcement presumes a non-family kidnapping in February 2026, before the return is filed. Asked whether the child "at any time during 2025, was presumed ... to have been kidnapped", the filer answers no.
- **Effect.** `dependent.months` counts the absence, so `lived_half` and `eic_child` can be false. The CTC/ODC, EIC and head of household status for this child are denied where Pub. 501 may allow them (understatement). The old present tense ("is presumed") caught this case.
- **Fix.** "Is this person a child who has been presumed by law enforcement authorities, at any time from the start of 2025 until now, to have been kidnapped by someone who isn't a member of your family or the child's family (even if the child has since been returned)?"

## PENDING-4-2: `f5695.joint_occupancy`, finding 2 (UNCLEAR; severity low)

- **Quote.** i5695 p. 3: "Residential energy property expenditures are costs of new qualified energy property that is installed on or in connection with a home that you used during 2025"; p. 6, Line 21c: "Enter the full address of each home where you installed qualified energy property."; p. 3, Joint occupancy: "If the aggregate credit that would be allowed to all occupants for any item of property exceeds the credit limit below, then you must figure your allocable share".
- **Case.** The filer lives alone in their main home and installs a $5,000 heat pump at a vacation home shared with a sibling, who pays for a second heat pump there. Reading "the home" as the main home, the filer answers no.
- **Effect.** `f5695.line30` takes the full $2,000 heat-pump limit instead of the allocable share (credit overstated).
- **Fix.** "Did you occupy any home for which you are entering costs jointly with someone other than your spouse on a joint return (...)"; keep the rest.

## PENDING-4-3: `f8960.unsupported`, finding 3 (NARROW; severity low)

- **Quote.** i8960 p. 13, Line 7: "Section 404(k) dividends reported on line 2 (enter as a negative amount)"; p. 7: "If line 2 includes dividends from employer securities held in an employee stock ownership plan (ESOP) that are deductible under section 404(k) ... include those amounts as negative modifications on line 7." i1099div p. 4: box 1a includes "section 404(k) dividends paid directly from the corporation".
- **Case.** A filer above the MAGI threshold receives $3,000 of ESOP dividends paid directly on Form 1099-DIV. Nothing in the screen names them, so the filer answers no.
- **Effect.** Line 2 includes $3,000 with no line 7 modification, so the NIIT is overstated by up to $114 (3.8%).
- **Fix.** Add "section 404(k) dividends on employer stock in an ESOP paid to you directly (Form 1099-DIV)" to the list.

## PENDING-4-4: `f8962.other`, finding 1 (NARROW; severity low to medium)

- **Quote.** i8962 p. 5: "An individual in your tax family who is eligible for MEC (except coverage in the individual market) for a month is not in your coverage family for that month. Therefore, you cannot take the PTC for that individual's coverage for the months that individual is eligible for MEC." p. 15, Example 3: "starting on August 1, Mike is eligible for MEC ... and does not notify the Marketplace ... the applicable SLCSP premium reported on Form 1095-A for August through December is incorrect".
- **Case.** A filer has a family Marketplace policy with APTC. From August a spouse is offered affordable, minimum-value employer coverage, and the Marketplace is not told. Nothing in `f8962.other` or the Form 1095-A questions says that this eligibility makes column B wrong, so the filer answers no and enters column B as printed.
- **Effect.** August to December are computed with the full SLCSP for the spouse, so the PTC is overstated and the excess APTC (Schedule 2 line 1a) understated.
- **Fix.** Add to the list: "someone enrolled was eligible for a whole month for other minimum essential coverage (for example Medicaid, CHIP, Medicare Part A, TRICARE, or an employer plan that was affordable and gave minimum value), unless the Marketplace knew of it when it approved your advance payments".

## PENDING-4-5: `gift.special` finding 0, with `gift.public_securities` (UNCLEAR; severity low)

- **Quote.** i8283 p. 9: "A security is generally considered to be publicly traded if the security is (a) listed on a recognized stock exchange whose quotations are published daily; (b) regularly traded on a national or regional over-the-counter market; or (c) quoted daily in a national newspaper of general circulation in the case of mutual fund shares."
- **Case.** A filer gives $12,000 of a thinly traded stock that has a ticker but no regular market. Neither question defines the term, so the filer answers no here (the exception) and yes to "Is this group publicly traded securities?".
- **Effect.** `gift.section_b` is false, and `gift.allowed` passes $12,000 to Schedule A where Section B and a qualified appraisal are required.
- **Fix.** Add the p. 9 definition to `gift.public_securities` and to the exception here: "(other than publicly traded securities: listed on a recognized stock exchange with daily published quotations, regularly traded on a national or regional over-the-counter market, or mutual fund shares quoted daily in a national newspaper)".

## PENDING-4-6: `person.x_other`, finding 1 (NARROW; severity low to medium)

- **Quote.** f5329 (2025) p. 1, Part III, line 17: "Enter 6% (0.06) of the smaller of line 16 or the value of your traditional IRAs on December 31, 2025"; line 12 counts only "2025 distributions of prior year excess contributions" (Part IV, lines 20-25, is the same for Roth IRAs).
- **Case.** A 2023 Roth IRA excess of $4,000 stayed in the account through 2025 and was withdrawn in February 2026. The filer has made no 2025 IRA contribution, so `person.ira_excess` is not asked, and answers no to "excess contributions ... for an earlier year that are still in the IRA".
- **Effect.** The tool has no Part III/IV lines, so the $240 6% tax is missing from Schedule 2 line 8.
- **Fix.** "excess contributions to a traditional or Roth IRA for an earlier year that were still in the IRA at the end of 2025 (even if withdrawn since; whether or not you contributed for 2025)"; make the same change to `person.ira_excess`.

## PENDING-4-7: `refund.not_2024`, finding 0 (NARROW; severity very low)

- **Quote.** p525 p. 24: "If you receive a refund or other recovery that is for amounts you paid in 2 or more separate years, you must allocate, on a pro rata basis, the recovered amount between the years in which you paid it."
- **Case.** An itemizer paid part of the 2024 state estimated tax in December 2023, deducted it on the 2023 return, and gets a 2024 refund in 2025. Nothing was paid in 2025, so the filer answers no.
- **Effect.** `refund.taxable` puts the whole refund through the worksheet as a recovery of 2024 tax, without the allocation to 2023.
- **Fix.** "... or did you pay any of your 2024 state or local income tax in a year other than 2024 (for example a last estimated payment in January 2025, a payment with an extension or a balance due, or an estimated payment made in 2023)?"; update the refusal text to match.

## PENDING-4-8: `s1.alimony_unsupported`, finding 0 (NARROW; severity low)

- **Quote.** p504 p. 15: "If any part of payments you make must continue to be made for any period after your spouse's death, that part of your payments isn't alimony whether made before or after the death. If all of the payments would continue, then none of the payments made before or after the death are alimony."
- **Case.** A 2016 instrument requires $30,000 a year, of which $10,000 continues to a trust after the recipient's death. Neither the screen nor the amount questions mention it, so the filer answers no and enters $30,000.
- **Effect.** `s1.paid_refused` deducts, or `s1.alimony_refused` includes, $10,000 that is not alimony.
- **Fix.** Add to the non-alimony parts: "a part that must continue (or be replaced by a substitute payment) after the recipient's death".

## PENDING-4-9: `s1.uc_unsupported`, finding 2 (UNCLEAR; severity very low; introduced by BUG-0245)

- **Quote.** i1040gi p. 89: "If you made contributions to a governmental unemployment compensation program and you aren't itemizing deductions, reduce the amount you report on line 7 by those contributions."
- **Case.** A self-employed filer pays for their own elective state unemployment coverage and later receives benefits. The carve-out "not counting employer-paid tax" reads to this filer as covering what they paid as their own employer, so they answer no.
- **Effect.** `s1.line7_figured` is not reduced, so line 7 is overstated by those contributions.
- **Fix.** "(including amounts withheld from your wages for it and amounts you paid for your own coverage as a self-employed person; not counting tax an employer paid on your wages, paid family leave or disability insurance contributions)".

## PENDING-4-10: `sales.special`, finding 4 (UNCLEAR; severity very low; made worse by BUG-0231)

- **Quote.** i1040sd p. 11, line 18: "Include on the worksheet any gain (but not loss) from the sale or exchange of an interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation of collectibles."
- **Case.** A filer makes a long-term sale of S corporation stock in a company holding appreciated artwork. Reading "holding such property" as referring back only to the section 1250 property just named, the filer answers no.
- **Effect.** `sales.one` taxes the collectibles part at 0/15/20% instead of through the 28% Rate Gain Worksheet.
- **Fix.** "... or an interest in a partnership, S corporation or trust holding any of these?"

## PENDING-4-11: `scope.schedule1`, finding 7, with `person.se_screen` (UNCLEAR; severity low)

- **Quote.** i1040sse p. 1: church employee income is income as an employee "of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes"; i1040gi p. 11: "wages of $108.28 or more from a church or qualified church-controlled organization that is exempt from employer social security and Medicare taxes".
- **Case.** An employee of a church-controlled hospital that elected the exemption is paid $40,000 on Form W-2. Both questions gloss church employee income as "wages from a church that elected exemption", so the filer answers no.
- **Effect.** `eic.step5_line1` uses line 1z without the church-employee adjustment, and no SE tax is figured (Schedule 2 line 4 omitted). `f8959.unsupported` uses the bare term "church employee income" and may catch a filer who knows it.
- **Fix.** In both glosses: "wages from a church or a qualified church-controlled organization that elected exemption from social security and Medicare taxes".

# Uncertainties

- `f8962.other` finding 2: `sa.dependent` blocks the return for a claimable filer who takes the standard deduction. I did not check the itemizing path. Lines 24/25 themselves have no dependent gate.
- `f8960.unsupported` finding 2: there is no supported Form 1099-R kind for a life insurance contract (`retirement.account` lists IRA, Roth IRA or plan). A filer who enters a surrender as `plan` would get the gain into income, but whether f8960 then omits it from NII was not traced.
- `dependent.kidnapped`: the qualifying-relative branch is still ungated, per BUG-0234's explicit choice. Eval confirms it, and the effect is understatement only. Not re-raised.
- `f8962.alloc`: round 1's side note is still open: a filer who holds no Form 1095-A (`f8962.any`) is never asked.
- Severity for PENDING-4-4 assumes column B on Form 1095-A is uncorrected in the case. Pub. 974 is not archived.
