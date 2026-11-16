# Decisions settled by the coordinator for the redraft

The owner delegated these to the coordinator on 2026-11-14, with the instruction to settle each question in the
direction the coordinator would recommend. Each entry says what was decided, by whom, the lane note it comes from,
and how to reverse it. "As built" means the redraft's lane made the choice and the coordinator kept it.

## 1. Four scope questions: back to what the old screen asked

- **Decided.** Three questions about a deduction ask whether the filer wants to claim it, as the old Schedule 1 screen
  did ("an adjustment on Schedule 1 line 12, 14 or 23"): `scope.reservist_expenses` (reserve or National Guard travel
  more than 100 miles from home), `scope.military_move` (a move under military orders) and
  `scope.performer_expenses` (a qualified performing artist's or fee-basis official's costs). Each help ends "To go
  on without it, answer No." (MAP Part 4.3: the wish is asked where the return is right without the thing wished
  for). The fourth, `scope.recovery`, is income, not a deduction: a return that leaves out a taxable recovery is not
  right, so it cannot be put as a wish. It is put back to the old screen's scope instead, a recovery that has to be
  reported ("requiring Schedule 1"): the question asks about an amount whose earlier deduction lowered the tax, and
  its help says that a recovery of a deduction that did not lower the tax is answered No.
- **By.** The coordinator, under the owner's delegation of 2026-11-14 (the recovery's form: the coordinator's reading
  of the same instruction, recorded here because it is not the wish).
- **From.** `docs/provisional/lanes/l9.md`, "Where I was unsure", item 2.
- **Shown.** Coverage rows in `interview/2025/coverage/scope.yaml`: for each of the four, the row that refuses (as
  before) and a row for the filer the fact-question refused and the old screen did not (the costs, no wish to deduct
  them; a recovery that gave no tax benefit), which completes.
- **To reverse.** Restore the four prompts (`source` and `label` in `forms/2025/scope.yaml`) and helps
  (`interview/2025/questions.yaml`) from the commit before this one, and delete the four completing rows.

## 2. A birth year is range-checked

- **Decided.** A birth year after the tax year, or more than 125 years before it, is refused as conflicting answers
  (the test `person.birth_year_bad`; the refusal `household.birth_year_bad`, explained in
  `interview/2025/conflict_checks.yaml`), not read as a very young or very old person. The bounds are the parameters `age.birth_year_latest` (the tax year) and `age.birth_year_earliest` (125
  years before it).
- **By.** The coordinator, under the owner's delegation of 2026-11-14.
- **From.** `docs/provisional/lanes/l4b.md`, step B ("Nothing checks the year typed ... A consistency check ... is
  not built").
- **Shown.** Coverage rows `opening.birth_year_after_tax_year` and `opening.birth_year_too_early` (refused);
  `opening.birth_year_earliest_accepted` and `opening.birth_year_latest_accepted` (the bounds themselves are not
  refused for the year).
- **To reverse.** Remove the three lines, the refusal entry on the household roster line, the conflict explanation,
  the two parameters and the four rows.

## 3. Choices of the redraft that stand as built

Each was made by the lane named; the coordinator keeps it under the owner's delegation of 2026-11-14.

| Decision | Lane note | To reverse |
|---|---|---|
| Tips from work that is not on the list of tipped occupations: the return completes with no deduction for them (no refusal) | `lanes/l3.md`, "Coverage rows" (`coverage/jobs.yaml`; `tipjob.other_work`) | make `tipjob.other_work` a refusing question |
| The marketplace question asks about the months of Marketplace insurance only ("While on Marketplace insurance ...") | `lanes/l8a.md`, "`f8962.other` ... taken apart" (the map's proposal, as built) | restore the whole-year wording of the question |
| The qualifying-child tie-breaker is asked as one plain question, whose Yes refuses (`dependent.qc_tiebreak`: the tie-breaker rules are outside the tool) | `lanes/l2a.md`, "The tie-breaker gate" and "Places I was unsure" | restore the 297-word screen |
| Five old Form 1099-R items (corrective distributions, recharacterizations, a qualified plan loan offset and the like, and a Form RRB-1099-R) are asked only by the code in box 7 and end at `retirement.bad_code`'s refusal | `lanes/l4a.md`, "Unsure, and review debt", item 3 | give each its own question beneath the code |
| Equipment acquired before September 28, 2017 is refused whatever year it was first used, as the old screen read (`asset.acquired_before_bonus_date`) | `lanes/l6b.md`, "For the owner", item 1 | ask it only of property placed in service this year, as for a vehicle |
| Support is asked in three answers (clearly less than half, clearly more than half, close or not sure), with the full test only on "close or not sure" (`dependent.self_support_view`, `dependent.supported_view`) | `lanes/l2a.md` | ask the full support tests directly |
| Two deduction wishes are asked of everyone: the sales tax election (`sa.sales_tax_wish`) and the choice to itemize (`sa.elect_itemize`) | `lanes/l7a.md`, "Not finished, in rank order", item 3 | ask each only when the return has an amount it acts on |
| New York: the wish to itemize on the New York return is asked of every New York filer (`ny_it201.ask.itemize`) | `lanes/ny.md`, "`ny_it201.ask.itemize`" | ask it only when the federal Schedule A holds an amount New York itemizes |

## 4. A single filer whose answers meet the head of household tests is told to choose it

- **Decided.** A filer who chose "None of these: I was not married (single)", is unmarried, lists a dependent, paid
  over half the cost of keeping up the home, and has a person who qualifies them under Test 2 of head of household is
  refused with the remedy "Go back and choose head of household" (gate `household.hoh_missed`; helpers
  `household.dependents_listed`, `household.dependents_any`, `household.hoh_missed_test2`, `household.hoh_missed_cost`,
  `household.test2_lived_persons`, `household.hoh_missed_person`; the refusal hangs on `household.hoh_fails`, so it
  reaches Form 1040 line 12e). The tests are read in that order (a choose at each step), so a single filer with no
  dependent is asked nothing new, one with a dependent is asked `household.home_cost`, and only after a Yes are the
  dependent's head of household facts read; no existing expectation of the six fixtures first reported moved. Test 1
  (a parent's separate home) is not checked: reading it per dependent before the relationship is known made
  `interview-rules` fail, and doing it in order needs a line in `dependent.yaml` (another lane's form). Class M cases
  that list a dependent on a single return were given one input, `household.home_cost: false` (inputs only):
  `classm.f8880.4`, `classm.f8863.4`, `classm.s3.2`, `classm.tcw.3`, `classm.tcw.7`, `classm.tcw.8`, `classm.tcw.10`
  and, in `classm.deepseek.json`, `classm.s3.4`, `classm.f8880.4`, `classm.f8863.4`. One case is left for the coordinator: `classm.sdtw.5` states a single filer who paid over half the home cost
  for a sibling who lived with them 10 months, so it is now refused (it was a head of household filer computed at
  single rates).
- **By.** The coordinator of the goal-1 round, 2026-11-15, approving lane g1-f9's design (T-304 item 1); the order of
  the tests and the omission of Test 1 are the lane's.
- **From.** `docs/provisional/lanes/g1-f9.md`, "T-304 (1)".
- **Shown.** Coverage rows `household.single_entitled_hoh` (refused at `household.hoh_missed`) and
  `household.single_parent_home_not_paid` (goes on past the head of household details) in
  `interview/2025/coverage/household_payments.yaml`.
- **To reverse.** Remove the refusal entry from `household.hoh_fails`, the helper lines and the gate, the two rows,
  and the inputs added to the class M cases.

## 5. Schedule 2: where the alternative minimum tax and the other Schedule 2 taxes refuse

- **Decided.** Each refusal sits on the line its tax belongs to, so neither waits for the other.
  - Line 21 no longer refuses on `s2.amt`. f1040s2 (2025) line 21 reads "Add lines 4, 7 through 16, 18, and 19. These
    are your total other taxes". The AMT is line 2, which only line 3 adds.
  - Line 2 refuses on `s2.amt` only.
  - Line 1z refuses on `s2.other` (the same refusal entry).
  - Line 3 has no refusal entries of its own. It is the sum of lines 1z and 2, and a sum returns its operands' first
    refusal, a refusal outranking an unknown (spec 4.7.2). So an `s2.other` item and an incentive stock option item
    are each told as soon as it is answered, and when both are true they arrive together on line 3, as line 1z's
    `s2.other` refusal.
- **Why.** With the AMT computed (T-307), `s2.amt` is settled only once the return's tax is known. Any refusal listed
  after it on one line would wait for the whole return, which conflicts with N11 (a refusal is told at its topic). The
  order first approved, line 3 refusing on `[s2.other, s2.amt]`, removed that wait for the `s2.other` items. It moved
  the wait onto the incentive stock option items instead (coverage rows `other.iso_kept`, `other.iso_vested_2025`).
- **By.** The coordinator of the goal-1 round, 2026-11-15, choosing option (b) of lane g1-f7b's report (section 7).
  Applied at integration B1.
- **Restated.** Expected values, each from f1040s2 (2025) and the case's facts:
  - `stage4.refuse.s2.amt` and `s2.reg.iso_vested_2025`: `s2.line21`, from refusal(s2.amt) to $0 (lane g1-f7b).
  - `stage4.refuse.s2.amt.simultaneous`: `s2.line21`, from refusal(s2.amt) to refusal(s2.other), and `s2.line3` to
    refusal(s2.other) (lane g1-f7b; line 1z comes first in line 3's sum).
  - `stage4.refuse.s2.other`: `s2.line2`, from refusal(s2.other) to $0 (B1). No AMT is owed on $100,000 of wages,
    single, so line 2 (Form 6251 line 11) is $0. Lines 3 and 21 still refuse on `s2.other`.
- **Shown.** Coverage rows `other.iso_kept` and `other.iso_vested_2025` (refused at `s2.amt` without waiting) and the
  `s2.other` rows of `interview/2025/coverage/other.yaml`.
- **To reverse.** Restore line 3's refusal list `[s2.other, s2.amt]`, drop line 1z's refusal, give line 2 back
  `s2.other`, and restate the expectations above.

## X1 lane x1-digital: digital assets (owner decisions D1 to D8 of the digital-asset scout)

The owner delegated these to the coordinator, who settled each as `lanes/scout-digital-assets.md` section 8 recommends;
lane x1-digital built them (2026-11-15). Lane note: `lanes/x1-digital.md`.

| Decision | Settled | Record; to reverse |
|---|---|---|
| D1 Form 1040 digital asset question | Encoded: `f1040.digital_assets` (input, asked of every filer at order 159), with the entry check `f1040.digital_conflict` (a No with a sale under box G to L, refused at Form 1040 line 7a). `s1.digital_income` is asked beneath it. | Rows `sales.crypto_said_no`, `other.digital_income`. Reverse: delete the three f1040 lines and `s1.digital_income_if_assets`, put `s1.digital_income` back in `money_b`, drop the input from the class M and mutation cases |
| D2 NFT of a collectible | Refused through `sales.special` (a bullet in its question); `amb.2025.nft_collectible`; Notice 2023-27 listed for archiving | Row `sales.nft_collectible`, persona 18. Reverse: remove the bullet |
| D3 Line 8v on a return that files Form 8960 | Refused narrowly: `f8960.digital_nii` (line 8v > 0 and MAGI over the threshold), at Form 8960 line 7; `amb.2025.digital_8v_nii` | Row `other.digital_income_niit`, case `s1.refuse.digital_nii`. Reverse: remove the gate and its refusal entry |
| D4 Code E for digital asset transaction costs | Stays refused (code "other"); `amb.2025.digital_transaction_costs` (unlinked) | Row `sales.crypto_cost_code` |
| D5 Code W on boxes G to L | Allowed; the question's wording limits it to tokenized securities; `amb.2025.digital_wash` | Cases `sales.adjust.{G,H,J,K}.{W,BW}`, `sales.adjust.{I,L}.W`, `sales.adjust.G.W.tokenized` |
| D6 T-003's second half (`sd.filed` reading raw Form 1099-DIV boxes) | Left open: the scout makes no recommendation | T-003 stays open for its second half |
| D7 The coverage estimate's silence | Accepted: the gain is unmeasured; a count of Yes answers to the question is listed for archiving | — |
| D8 Code M summary rows (Exception 2) | Out of scope: code M stays refused (scout section 1.2); the scout makes no recommendation to widen it | — |

## Lane x2-k1p: the partnership Schedule K-1 (Form 1065)

- **Decided.** The owner's decisions D-K1 to D-K16 of `docs/provisional/lanes/scout-k1.md` section 8 are settled as the
  scout recommends. Those that govern `forms/2025/k1p.yaml`:
  - D-K2 (partnership basis) and D-K3 (at-risk): asked of the filer on any K-1 with a loss (`k1p.basis_short`,
    `k1p.not_at_risk`); a Yes refuses. Rejected: encoding the partner's basis worksheet; refusing every loss.
    Register: `amb.2025.k1p_basis_by_filer`.
  - D-K4 (publicly traded partnerships): refused at item D (`k1p.ptp`), asked first and alone. Rejected: income-only PTPs.
  - D-K5 (material participation): tests 1, 2, 3 and 5 asked in turn beneath "did you work in it"; a Yes to test 4, 6
    or 7 refuses; a limited partner is asked tests 1, 5 and 6 only. Rejected: one question with the seven tests in
    help. Register: `amb.2025.k1p_material_tests`.
  - D-K6 (box allow-list): computed boxes 1, 2, 3, 4a, 5, 6a, 6b, 8, 9a, 9b, 9c, 14 A, 15 O, 18 A, 19 (code A, not
    above basis), 20 A/B (information), 20 Z; accepted with no return effect 6c, 13 AE, 18 B/C, 20 N, 20 AG; every
    other box refuses at its own tick.
  - D-K10 (box 4b): refused. D-K14 (foreign): foreign partnerships, box 16 (K-3) and box 21 refused.
  - D-K11 (placement): `$k1p` and its questions at order 264.
  - D-K13 (Schedule E presence): a portfolio-only K-1 puts no row on Schedule E (`k1p.sche_row`;
    `amb.2025.k1p_portfolio_no_sche`).
  - D-K16 (activity rows): suffix lines (`k1p.b1_*`, `b2_*`, `b3_*`), no def.
  - D-K1 (Form 7203) is lane x2-k1s's; D-K7, D-K8 (QBI share of a suspended loss, SE attribution) and D-K12, D-K15
    are the return-integration lane's: the lines they need are listed in `/tmp/k1-wiring-k1p.md`.
- **By.** The coordinator, under the owner's delegation (launch message of lane x2-k1p, 2026-11-15).
- **From.** `docs/provisional/lanes/scout-k1.md` section 8; lane note `docs/provisional/lanes/x2-k1p.md`.
- **To reverse.** Each decision is one group of lines in `forms/2025/k1p.yaml` (a refusal entry on `k1p.screened`, or a
  question with its gate line) and its bank entry at order 264.

## x2-k1s. Schedule K-1 (Form 1120-S) and Form 7203 (lane x2-k1s, 2026-11-15)

Owner decisions of the K-1 scout (`docs/provisional/lanes/scout-k1.md` section 8), settled as the scout recommends
(the owner delegated them to the coordinator); D-K1 by the owner. Record: `docs/provisional/lanes/x2-k1s.md`.

| Decision | As settled for the S corporation lane | Alternative rejected |
|---|---|---|
| D-K1 Form 7203 | Encoded: Part I (stock basis) and Part III lines 35 to 38 (losses allowed by stock basis, pro rata), as an implicit `f7203` entry under each `k1s` entry. Part II (loans from the shareholder), the 1.1367-1(g) election, a distribution above basis, a capital loss limited by basis and carryovers from earlier years are refused (owner) | Refuse every S corporation K-1 with a loss or a distribution |
| D-K3 At-risk | Asked on any loss (`k1s.not_at_risk`); a Yes refuses (Form 6198) | Encode Form 6198 |
| D-K5 Material participation | Layered: worked in it, then more than 500 hours, then more than 100 hours and no one more, then earlier years (tests 5 and 6 in one question); a refusing question for tests 2, 4 and 7 asked only of those who worked in it and met none | One question with all seven tests in help |
| D-K6 Box allow-list | Boxes 1 to 5b, 7 to 8c, 13 O, 16 A to D, 17 A, B, V (QBI only), AC accepted; boxes 6, 9 to 12, 13 other codes, 14 (K-3), 15 (AMT), 16 E and F, 17 other codes, and section 199A dividends or PTP income on the code V statement refused | Royalties (box 6) and charitable contributions (12 A) computed |
| D-K7 QBI with a suspended loss | The basis part: a QBI loss on a K-1 whose losses are partly carried by basis refuses (`k1s.qbi_cut`, `amb.2025.k1s_qbi_basis`). The passive part is the integration lane's (`prorate`, as the scout recommends) | Scale by the allowed share now |
| D-K11 Placement | `$k1s` and its questions, and the Form 7203 questions, at order 264, seq 20 to 83 (the scout's 264.20 and following) | Separate order number for Form 7203 |
| D-K16 Activity rows | Suffix lines per box (`k1s.p1_*`, `p2_*`, `p3_*`) | A def per activity |
| Scope of the lane | No return-level line reads the K-1 yet: the lane exposes `person.k1s_total_*` (naming shared with x2-k1p, `/tmp/k1-wiring-k1s.md`) for the integration lane; `scope.k1` still refuses every K-1 until then | Wire Schedule E / Form 8582 here (they are lane x1-sche's, not in this tree) |

## Married filing separately, lane mfs-l4: dependents

| Decision | Reason and source | Record |
|---|---|---|
| D3 (settled as the design scout `scout-mfs.md` §8 recommends; owner delegated to the coordinator, 2026-11-15): on a separate return, a child who is also the qualifying child of the husband or wife only is kept when the husband or wife will not claim the child and the filer is the child's parent by birth or adoption; refused at `dependent.qc_tiebreak` (and `dependent.eic_tiebreak`) when the husband or wife will claim, when another relative could also claim, or when the filer is not a parent. Alternative rejected: keep every such child refused at the tie-breaker (keeps most married-filing-separately parents who live together refused). | p501 p. 17, "Subject to these tiebreaker rules, you and the other person may be able to choose which of you claims the child as a qualifying child"; Example 6 (p. 17), separate returns, "if your spouse doesn’t claim your child as a qualifying child, you can claim this child"; p501 p. 15, the tie-breaker applies when the parents "don’t file a joint return together but both parents claim"; i1040gi p. 21, a non-parent claims only with an AGI higher than any parent's (hence the parent question, which the scout's design lacked). | `amb.2025.mfs_spouse_qc`; `forms/2025/dependent.yaml` (`dependent.other_only_spouse`, `dependent.spouse_claims`, `dependent.filer_parent` and their gates, `dependent.spouse_settles`, `dependent.tiebreak_unsettled`, `dependent.tiebreak_settled`, `dependent.tiebreak_spouse_or_other`, `dependent.eic_tiebreak_unsettled`); `lanes/mfs-l4.md` |

## X1 lane x1-sche: Schedule E Part I, Form 8582 and rental depreciation

Settled by the coordinator under the owner's delegation, each as `docs/provisional/lanes/scout-schedule-e.md` §8
recommends (lane x1-sche, 2026-11-15). Record: `docs/provisional/lanes/x1-sche.md`.

| Decision | Settled as | Alternative not taken |
|---|---|---|
| D1 Form 8582 scope | Parts I to VIII computed, with prior-year unallowed losses and Part V | Exception only (refuse any return needing the form) |
| D2 Mixed use | Not-a-home division computed (every expense line divided by days, `amb.2025.rental_direct_expenses`); a home rented 15 days or more refused (`rental.ws51`) whether profit or loss; a prior loss from a year without active participation refused (`rental.prior_not_active_if_both`) | Compute Worksheet 5-1; ask the year of each prior loss |
| D3 Personal property in rentals | Refused in v1 (`rprop.personal`) | A `rasset` lane now |
| D4 Royalties | Computed without depletion; depletion refused (`royalty.depletion`) | — |
| D5 Vehicles | Refused (`rental.vehicle`, which also takes travel costs, line 6) | Standard mileage now |
| D6 EIC | Refused with Schedule E (`eic.step2_other` on `sche.any`); Pub. 596 to archive | Compute Worksheet 1 |
| D7 NIIT | Form 8960 line 4a = Schedule 1 line 5; "rental, royalty" dropped from `f8960.unsupported` | Keep refusing rentals above the NIIT threshold |
| D8 QBI | Rentals are not a qualified trade or business; a filer who says one is, refused (`sche.qbi_business`) | Compute the safe harbor |
| D9 Commercial | 39-year computed for property placed 1994 and later; earlier refused (`rprop.early_nonres`) | — |
| D10 Prior-year depreciation | Figured from Tables A-6 and A-7a (`amb.2025.rental_prior_depreciation_tables`) | The filer's earlier schedule |
| D11 Placement | Recommended 268/269, but `tick-groups` requires a question a tick-box Yes opens to take the group's order: `scope.rental` at 130 (tick box), `scope.rent_personal` 130.4, the property topic 130.11–61, royalties and the return-level questions 130.71–94 (the scout's alternative) | 268/269 (fails `tick-groups`) |
| D12 Coverage row end changes | `scope.rental` and `scope.royalties` rows: refused `scope.schedule1` → completed (N9 approved end change) | — |
| D13 QJV | Not asked; co-owned property entered once with the filer's share | — |
| D15 EBL | Schedule E rental and royalty losses before the passive limit counted toward the excess business loss screen (`amb.2025.s1_ebl_rental`) | Leave them out |

## MFS L1. Married filing separately: opening and household (lane mfs-l1)

Settled by the coordinator under the owner's delegation, 2026-11-15, as the design scout
(`docs/provisional/lanes/scout-mfs.md`, section 8) recommends. Lane note: `docs/provisional/lanes/mfs-l1.md`.
Decisions D3 to D6 of the scout are recorded by the lanes that build them (L4: D3; L2: D4; L3: D5, D6).

- **D1, community property: refused.** A married filing separately filer who lived in a community property state at
  any time in 2025 is refused at Form 1040 line 1a (gate `household.mfs_community_property`, on the existing question
  `household.community_property`; register `amb.2025.mfs_community_property`). Rejected: computing the Pub. 555 split
  (Pub. 555 and Form 8958 are not archived). To reverse: archive Pub. 555 and build the split; drop the gate.
- **D2, changed expectations approved.** Coverage row `opening.separate` ends in `proceeds: {f1040.status: mfs}`
  instead of `refused: s3.mfs`; fixtures `stage4.refuse.married` (scope.json) and `ss.mfs` (s3.json) are restated
  from the source (lane L1); `stage15.refuse.f2441.mfs`, `stage15.refuse.f2441.mfs_benefits` and
  `stage11.refuse.hsa_married` are L3's. Rejected: keeping married filing separately refused. To reverse: restore the
  `s3.mfs` refusals at `scope.ready_credits` and `s3.line11` and the old expectations.
- **D7, notices only.** The return carries a notice line `household.mfs_spouse_notice` (enter the spouse's name and
  SSN, i1040gi p. 14), a target of the full profile; the interview does not advise that a joint or head of household
  return may cost less. Rejected: a comparison of statuses (the tool prepares one return).
- **D8, New York.** No New York form is changed; once federal married filing separately computes, New York returns
  with that status become reachable, and a New York lane checks them before release (scout D8).
- **Lane choices kept (as built).** (a) `eic.same_home` stays the input (asked now only of a married head of household);
  a new line `eic.same_principal_home` derives Step 3 question 4 from `household.mfs_living` on a separate return,
  instead of renaming the input as the scout proposed (fewer fixtures touched). (b) Line 6d is checked only where the
  return has social security benefits (`amb.2025.mfs_lived_apart_boxes`), so the living question is not asked of every
  separate filer. (c) `household.community_property` keeps its place (order 103); the separate filer reaches it right
  after the marriage questions, which is where the refusal is told. (d) Temporary absences count as living together for
  every test, and EIC question 4 is No only when the spouses did not live together at any time July to December
  (`amb.2025.mfs_lived_apart`).

## MFS lane L2: deductions and adjustments on a married filing separately return

Settled by the coordinator under the owner's delegation (2026-11-15) as `docs/provisional/lanes/scout-mfs.md`
recommends; the lane's note is `docs/provisional/lanes/mfs-l2.md`.

| Decision | Alternative rejected | Reason and source | Record |
|---|---|---|---|
| D4: the spouse's age and blindness boxes on a separate return stay refused (`sa.mfs_spouse_extra`); the question is now asked only when the spouse is not itemizing | Compute them with two spouse questions | Rare (the spouse must have no income and file no return: i1040gi p. 33, Line 12d); with line 12b checked the standard deduction is zero "even if you were born before January 2, 1961, or were blind" (i1040gi p. 34, Exception 2), so the question cannot matter then | `sa.mfs_spouse_not_itemizing`; row `mfs_ded.spouse_extra` |
| The spouse's itemizing is asked as a fact, with help to ask the spouse | Refuse a filer who does not know | i1040gi p. 33, Line 12b; Pub. 504 p. 4 | `amb.2025.sa_mfs_spouse_itemizes` |
| A separate filer is asked the mortgage limit at $375,000 / $500,000, counting the whole of a loan shared with the spouse | Count only the filer's share | i1040sca p. 8; Pub. 936 not archived; the question only refuses | `amb.2025.sa_mfs_mortgage_limit` |
| The student loan question is not asked on a separate return (its readers sit under a `choose` on the status; no `gated_by` marker, since the gate is open on every other status) | Ask it and compute zero | i1040gi p. 98, "Your filing status is any status except married filing separately"; N8 | `sli.any_if_not_mfs` |
| A separate filer not covered by a plan is asked whether the spouse was covered only when they lived together at some time in 2025 and made a traditional contribution; living apart all year gives line 2 $89,000 and the Schedule 1 line 20 box | Ask every separate filer; treat the social security exception literally after living apart | i1040gi pp. 96–97; Pub. 590-A p. 13 ("your filing status, for this purpose, is single") | `amb.2025.ira_mfs_spouse_covered`, `amb.2025.s1_line20_box` |

## MFS lane L3 (credits): owner decisions settled as the scout recommends

Married filing separately expansion, lane mfs-l3 (Forms 2441, 8863, 8962, 8889), 2026-11-15. The owner delegated the
scout's decisions to the coordinator; each is settled as `docs/provisional/lanes/scout-mfs.md` section 8 recommends.
Record: `docs/provisional/lanes/mfs-l3.md`.

| Decision | Settled | Alternative rejected | Source |
|---|---|---|---|
| D5 HSA on a separate return | Refused only when the filer was treated as having family HDHP coverage at some time in 2025 and the spouse has an HSA of their own (`f8889.mfs`, question `f8889.mfs_spouse_hsa`). Narrower than the scout's wording ("own HSA or own HDHP"): a spouse's own HDHP without an HSA is already handled by the existing `f8889.spouse_family` and month questions, as on a joint return where only one spouse has a Form 8889; line 6's division applies only to "spouses who have separate HSAs". | Computing the line 6 division (needs the spouse's agreed allocation, unknown on a separate return); refusing every spouse with an HDHP (refuses returns the form already computes). | i8889 p. 4, How To Complete Part I; p. 7, Line 6 |
| D6 PTC Exception 2 | Asked: `f8962.mfs_exception` (abuse or abandonment, living apart) and `f8962.mfs_three_years`, only on a separate return with a Form 1095-A; wording plain, help states what abuse and abandonment mean and that records are kept, not sent. | Not asking (every separate filer with a 1095-A treated as not applicable). | i8962 p. 7 |
| D2 (the lane's part) | Approved end changes restated from the source: `stage15.refuse.f2441.mfs`, `stage15.refuse.f2441.mfs_benefits`, `stage11.refuse.hsa_married` (see the lane note). | Keeping them refused. | i2441 pp. 2, 5; i8889 p. 7 |
| amb.2025.f2441_mfs_no_credit | Line 11 (Schedule 3 line 2) is zero for a separate filer not considered unmarried; Part III is still completed. | Part II left blank (same return). | i2441 p. 2 |

## Filers who can be claimed as a dependent (lane x2-dep)

Settled by the coordinator under the owner's delegation, as the design scout recommends
(`docs/provisional/lanes/scout-dependent-filers.md`, §8); recorded by lane x2-dep, 2026-11-15. Lane note:
`docs/provisional/lanes/x2-dep.md`.

| Decision | As settled | To reverse |
|---|---|---|
| D1. Expected values and coverage-row ends that change by design | Pre-authorized. The lane restated each from the source and lists it in its note: `stage4.refuse.standard.dependent`, `stage4.refuse.dependent_itemizes` (sa.json), `stage9.eic.refuse.dependent_of_another` (f1040.json) | restore the refusal entries and the three cases' refusal expectations |
| D2. The under-16 gate (`household.filer_under16`, amb.2025.filer_under_16) | Kept. The scout lists it as unchanged unless the owner decides; its reason (Form 8615 refused) still holds while Form 8615 is not built. Revisit when Form 8615 lands | lift the gate (all filers, or claimable filers only) |
| D3. The Qualified Dividends and Capital Gain Tax Worksheet at a bound filing status | (a) keyed tables `qdcg_zero_ceiling` and `qdcg_fifteen_ceiling`, read by the def `qdcg_amount`, with `tools/check_qdcg_ceiling.py` holding them equal to the year parameters | (b) a choose on the status over unkeyed parameters, or (c) a status operand on `param` (an atom change) |
| D4. Form 8814 | Not in this lane; stays refused (`scope.f8814`) | build the scout's batch P |
| D5. Form 8863 line 7 questions reused for Form 8615 conditions 3 and 4 | Reuse (recorded for batch K; not built in this lane) | ask Form 8615's own wording |
| D6. Form 8615 line 7 (other children) | Supported in v1 (recorded for batch K; not built in this lane) | refuse when the parent's return figures the tax for another child |
| D7. `person.sav_claimed` gated on `sa.dependent` | Recommended by the scout only where no other lane holds `person.yaml`; this lane does not own it, so the gate is not built and is left as a request | build the gate in a batch that owns `person.yaml` |
| A qualifying surviving spouse whom someone can claim | Refused at `sa.dep_qss` (amb.2025.sa_dep_qss), because the worksheet gives no amount for the status. The scout's reason (a contradiction) does not hold: i1040gi, Qualifying Surviving Spouse, condition 2c, allows a qualifying surviving spouse who "could be claimed as a dependent on someone else's return". So no consistency rule is added | use the married filing jointly amount for line 3 |
## X2 lane x2-s1o: other Schedule 1 income (owner decisions D1 to D7 of the Schedule 1 scout)

The owner delegated these to the coordinator, who settled each as `lanes/scout-s1-other.md` section 8 recommends;
lane x2-s1o built ranks 1 to 4 (2026-11-15). Lane note: `lanes/x2-s1o.md`.

| Decision | Settled | Record; to reverse |
|---|---|---|
| D1 Form 2555 | Declined this round: line 8d and the 29 `sa.excluded_income` refusal sites are unchanged | — |
| D2 (amends owner decision D4, `amb.2025.line8z_kinds`) New line 8z kinds | Computed: `fiduciary_fees`, `found_property`, `taxable_damages` (with `oi8z.injury` refusing damages in a case about a physical injury or sickness). Not added: the scout's `misc_box3` (the archive has only the payer's Form 1099-MISC instructions, no recipient-side rule for box 3). Insurance dividends stay refused | Rows `s1o.fiduciary_fees`, `s1o.damages_injury`. Reverse: drop the three enum values and `oi8z.damages`, `oi8z.injury`, `oi8z.injury_if_damages` |
| D3 NOL sufficiency test | Accepted: line 8a is computed when the carryover is at most four times taxable income after it; otherwise `s1.nol_limit` refuses at Form 1040 line 15. Premise checked line by line and recorded in `amb.2025.s1_nol_limit_test` | Rows `s1o.nol_*`, `scope.nol`, `scope.nol_casualty_no_business`. Reverse: put `scope.nol` back in `scope.schedule1` |
| D4 NOL and the AMT (i6251 Who Must File, statement 4) | Form 6251 line 2e (the NOL deduction) is added to the AMT screen's largest line 4 (`s2.amt_l4_sum`), with line 2f (ATNOLD) taken at zero, so the screen still bounds lines 1 and 4 of Who Must File from above | Reverse: drop `s1.nol_amount_if_nol` from `s2.amt_l4_sum` |
| D5 Coverage accounting (Pub. 4801, splitting `other_income`) | Approved; left to the integrator (categories.json is the integrator's) | Lane note, "For other lanes and requests" |
| D6 Line 8t | Stays refused (`s1.line8_other`) | — |
| D7 Expected-end changes to coverage rows | Authorized and made: `scope.recovery`, `scope.nol`, `scope.nol_casualty_no_business`, `other.options_income_not_on_w2`, `other.ltc_payout`, `other.inmate_wages` now end in `proceeds` | Lane note, "What the merge must know" |

## X1-F1116. Form 1116, passive category (lane x1-f1116, wave X1)

Settled by the coordinator under the owner's delegation, as the scout (`lanes/scout-form-1116.md`, section 8)
recommends; where the scout gave two options without a recommendation, the brief's rule for unarchived sources
("refuse that part as the scout plans") decided. Record: `lanes/x1-f1116.md`.

| Decision | Settled as | Alternative rejected | Record |
|---|---|---|---|
| D1 carryback | Never carried back by the tool; with Schedule B (Form 1116) not archived, any excess (a carryover generated) refuses at `f1116.carryover_out` | Compute the credit and leave the carryover unreported (i1116 p. 19 requires Schedule B when a carryover is generated) | `forms/2025/f1116.yaml` |
| D2 high-taxed income | Refuse when any column's tax exceeds 20% of its line 7 (`f1116.high_taxed`), the lower of the 37% and 20% readings, until Reg. 1.904-4(c) is archived | 37% only (would compute returns the 20% reading makes high-taxed) | `amb.2025.f1116_high_taxed` |
| D3 the election | Made whenever its conditions are met; `ftc.elect` kept as a derived true line (technique 3.1), its question removed | Keep asking (a No could only refuse or lower the credit) | `forms/2025/ftc.yaml`; 470 `ftc.elect` facts removed from fixtures |
| D4 adjustment exception | Taken whenever available; a return that must adjust is refused (`f1116.adjust`) | Compute both paths; compute the adjusted path (Worksheet for Line 18) | `amb.2025.f1116_exception` |
| D5 state income tax of itemizers | Refused with gifts and other itemized deductions (`f1116.itemized_unread`) until Pub. 514 is archived | Apportion by 3d/3e | `amb.2025.f1116_itemized` |
| D6 rounding and gross income | Ratios half-up to four places (3f, worksheet line 3, line 19); gains per sale entry | Full precision; gross gains behind aggregate entries | `amb.2025.f1116_ratio_places`, `amb.2025.f1116_gross_income` |

Second pass (lane x1-f1116b, 2026-11-15), with Schedule B (Form 1116) and its instructions, Pub. 514 and Reg.
1.904-4 and 1.861-8 archived. D1 stands; D2 and D5 are revised from the sources; one reading is new.

| Decision | Settled as | Alternative rejected | Record |
|---|---|---|---|
| D1 carryback (applied) | Schedule B (Form 1116) prepared for a carryover claimed or generated; line 7 is zero; a return whose 2024 passive limit had room (or 2024 foreign income with no credit) is refused at `f1116sb.carryback`, asked only when line 6 is above zero | Line 7 zero for everyone as an "estimate" (overstates the 2026 carryover the law has reduced); figure the carryback (needs an amended 2024 return) | `amb.2025.f1116_carryback` |
| D2 high-taxed income (revised) | Reg. 1.904-4(c): 37% of each withholding group's income after deductions (groups: tax of 15% or more; above zero and under 15%), the rate per column and kind | Per-column 20% screen (D2 first pass); payment-level rates (not on the return); 20% for qualified dividends (the test precedes the 904(b) adjustments) | `amb.2025.f1116_high_taxed` |
| D5 itemized deductions (revised) | Gifts to charity (Reg. 1.861-8(e)(12)(i)) and gambling losses go to U.S. income, not on Form 1116; state or local income tax still refused (Pub. 514 needs the income the state taxes, not on the return) | Apportion gifts with line 3b; apportion state tax by 3d/3e | `amb.2025.f1116_itemized` |
| D7 the election with a carryover (new) | A filer with foreign tax carried in files Form 1116 (`ftc.elect` false), so the carryover is used | Elect and keep the carryover; figure both | `amb.2025.f1116_carryover_election` (for the owner) |

## Lane x2-paynow2: pay not on a W-2 (coverage expansion, scout-tail part A)

| Decision | Reason and source | Record |
|---|---|---|
| Medicaid waiver earned-income choice: asked of each person with Medicaid waiver payments (`person.mw_earned`), not optimized (scout-tail A.8 item 2, settled as the scout recommends by the coordinator on the owner's delegation) | i1040gi p. 24, Line 1d, "if you choose to include nontaxable payments in earned income for purposes of claiming a credit or other tax benefit"; "you and your spouse can make different choices". The form gives the choice to the filer; help says counting it can raise or lower the credits. | `lanes/x2-paynow2.md` |
| Coverage rows whose end changes from refused to proceeds are restated (scout-tail A.8 item 4, authorized): `scope.pay_no_w2`, `scope.medicaid_waiver`, `scope.strike_benefits` (coverage/scope.yaml), `retirement.dis_early` (coverage/retirement.yaml) | The situations they name are now figured (lines 1b, 1d/8s, 1h). Each row's new answers and end are listed in the lane note; no other row's end was edited. | `lanes/x2-paynow2.md` |
| Allocated tips (W-2 box 8) stay refused through `s2.w2_marks` this round (scout-tail A.8 item 3 not reached) | Taking box 8 out of `s2.w2_marks` changes a Schedule 2 screen another lane (F7b) holds; the box-8 rule ("unless you can prove that your unreported tips are less") is recorded for the next round. | `lanes/x2-paynow2.md` |
| The Schedule 1-A tips deduction with Form 4137 tips stays refused, at a narrowed gate (`s1a.f4137`, `person.f4137_filed`) instead of `s2.other` (scout-tail A.8 item 4, the f4137-to-tipjob match rule, deferred) | Line 4b is "Qualified tips included on Form 4137, line 1, row A, column (c)"; which unreported tips are qualified needs the tipjob tests per employer row, and matching rows is a design decision not made here. A filer can still finish by declining the deduction. | `lanes/x2-paynow2.md` |
| `scope.pay_no_w2` and `scope.medicaid_waiver` stay inputs, as plain parents, not derived lines (variation on the scout's technique 3.1) | Each keeps its tick and wording, so the filer with nothing answers the same screen; a Yes now opens the children (`pay_kinds` group; per-person Medicaid amounts). Residual refusals: `scope.wages_no_form_if_pay` (in `scope.other_income`), `person.tips_gov_if_rows`, `person.mw_business_if_1099`, `person.mw_1099_over`, `retirement.dis_split`. | `lanes/x2-paynow2.md` |
| Medicaid waiver payments reported are all treated as nontaxable (`amb.2025.mw_all_nontaxable`) | Pub. 525 p. 33's count limits (10 under 19, 5 aged 19 or older) are not asked; Notice 2014-7 is not archived. | `ambiguities/2025.yaml` |
