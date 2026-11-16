# Lane X-MUT: stale equivalence arguments (release worktree `.claude/worktrees/xint`)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us and ny.

Method. Every argument held at HEAD (acde74b5): HEAD's canonical was built in a temporary export, and each
argument's pinned digest was recomputed there. For each argument the premise facts that `premiseDigest` covers
(expression, gates, type, marker, display condition, readers) were diffed between HEAD's canonical and the
worktree's, and the argument text was re-read against the changed facts. A digest was re-pinned only after
that check. No tool re-pins: the digest strings in `engine/src/mutate.ts` were edited by hand, with values computed
by `premiseDigest` on the worktree canonical. All 61 kept arguments hold on the current canonical (checked before
the rerun).

Totals: 56 re-pinned (52 federal, 4 NY; 4 of them with text corrections and 1 with an added premise), 1 retargeted,
4 removed, 0 findings in scope.

## Federal: re-pinned (what changed, and why the argument still holds)

- s1a.line36a_claim.zero.then2: only person.no (a parameter line) gained readers; the argument uses its value, not who reads it.
- s1a.line30.zero.then0: s1a.line30 gained the reader f1116.asset_method; the argument shows line30 has the same value on both routes, whoever reads it.
- eic.line1.earned_income.then0: eic.zero lost a reader (step5_line2); the argument uses only its value.
- boundary.person.has_educator_expenses: person.zero gained readers (Form 4137, Form 8919 and Medicaid waiver lines); has_educator_expenses's own readers are unchanged.
- person.has_educator_expenses...gt.0: same change as the previous line; the argument still holds.
- person.educator_eligible_amount.zero.then1: same change as the previous line; the argument still holds.
- ssb.line16.line16_together.then0: lived_apart changed from an input to a copy of household.mfs_apart_all_year, which reads inputs and a parameter through chooses with no refusal gates. It is still never a refusal, so lines 8 and 10 never refuse.
- person.edu_adj.zero.then1: only person.zero gained readers.
- sa.gift_carryover_if_no_gifts.no.then1: only sa.no's readers changed; gift_carryover_if_no_gifts is still read only by sa.line13.
- sa.medical_premiums_if_not_large.no.then1: only sa.no's readers changed.
- eic.credit.line6.then0: only eic.zero lost a reader.
- f8962.filing.applicable...: applicable is now a choose on mfs_barred, and f8962.any gained readers. The argument treats applicable as an opaque Bool with memoized value on both routes; any, forms, aptc are unchanged.
- ssb.show16_18.mfs_together...: same lived_apart change as above. lived_apart is unknown only through the status or the mfs_living answer, so "mfs_together unknown implies line 8 unknown" still holds.
- ssb.show16_18.past9...: same as the previous line.
- eic.line1_in_table.line1.ge.0: only eic.zero lost a reader.
- dependent.dc_line2c.dc_incapable...: dc_qp, dc_lived_half and qc_tests gained readers (f2441.mfs_qp_count, tiebreak_settled). Their expressions are unchanged, and the answered-only premise (dc_qp read for every dependent) still holds.
- eic.step5_income.earned_for_limit.lt.0: only person.zero gained readers.
- dependent.qr_dependent.no.then1: only dependent.no gained readers; qr_kidnapped and qualifying_relative are unchanged.
- dependent.eic_ssn_child.no.then1: dependent.relationship and dependent.no gained readers only.
- dependent.married_screen_qr.no: only dependent.no gained readers.
- dependent.married_screen_eic.no: only dependent.no gained readers.
- sales.bad_aggregate.no.then1: sales.one lost its first gate (sales.digital), so bad_aggregate is now gate 3 after bad_code (gate 2). bad_code gained boxes I and L but is still a never-refusing test of inputs. Still sound; the gate numbers in the text were corrected.
- person.ira_dist_gate.no.then1: person.zero and person.no gained readers only.
- dependent.qualifying_relative.no.then1: only dependent.no gained readers. qualifying_relative's gates, with qr_kidnapped still the last, are unchanged.
- dependent.odc_person.no.then1: only dependent.no gained readers.
- dependent.odc_from_tin.no.then1: only dependent.no gained readers.
- f8962.alien_branch.no.then1: the true alternative is now alien_not_barred, and line24 and line25 gained a first gate (dependent_filer). void_form still precedes alien_branch, and alien_branch is still read only by line24 and line25. Sound; the text was corrected (gate 7 after void_form, gate 6; the alternative's name; the unread-difference sentence).
- person.se_line6.zero.then1: the Schedule SE binding gained line8b and line8c, but only in the has_sc-true alternative; the argument is about the false alternative and the se_rrta gate. Unchanged.
- person.eic_se.zero.then1: same binding change. With has_sc false, se_line13 is still person.zero; with it unknown, the se_rrta gate is still unknown.
- person.ira_se.zero.then1: same as the previous line.
- f8889.self_dec_year.zero.then1: married_family gained the reader f8889.mfs_ask, and constants gained readers. The values of split, married_family and line6 are unchanged.
- f8889.self_in_family.self_dec_year.then0: same as the previous line.
- f8889.self_dec_year.zero.then2: same as the previous line.
- f8889.family_dec_year.zero.then2: only f8889.no gained a reader.
- f8889.bad_months.counts_hold.then0: f8889.mfs is now a test of mfs_spouse_hsa_if_asked, not of the status. It is still the first gate of line13_figured and still a Bool, so bad_months is read only where mfs is a memoized false.
- f8889.bad_months.counts_hold.then1: same as the previous line.
- f8889.testing_failed_figured.no.then1: the readers of f1040.status and of constants changed only.
- sa.home_other_if_not_owner.no.then1: only sa.no's readers changed.
- f2441.line13_earned.line20...: line21 is now smaller_of(exclusion_cap, plan_max). The argument reasons about line 21 only as complete, unknown or a refusal.
- f8889.age55_unmarried.age55...: married_family gained a reader, and constants gained readers only.
- f2441.attrib_gate.line31...: only f2441.zero gained readers.
- s8812.line18a.chart_eic.then0: EIC Step 5 line 2 and eiw_4 are each now M, the same sum of person.mw_not_earned (eiw_4 behind scope.schedule1), and Schedule 1 line 10 now sums line10_ex5 and line 5. Re-derived: chart_eic = 1z - M + S1 line 3 - S1 line 15, and eiw_7_figured = max(1z + S1 line 3, 0) - (M + S1 line 15); the floor is idle since wsb_4b > 0. The SE-$0 step holds because S1 line 15 is complete (line 10 path), so ss_base = min(0, line 9) is a complete 0. Sound: the text was rewritten for M, and s1.line10_ex5 was added to the premises.
- household.hoh_community_property.no.then0: only f1040.status's and household.no's readers changed; the status is still an input with no gates.
- household.hoh_community_property.no.then1: same as the previous line.
- household.hoh_community_property.no.then2: same as the previous line.
- household.hoh_community_property.no.then4: same as the previous line.
- household.hoh_missed_test2.no.then1: only household.no gained a reader.
- eic.from_step1_income.no.then1: scope.schedule1 changed its disjuncts (rental to rent_personal_if_rental; recovery and nol dropped). The argument uses it only as an any-test over the scope items that gates f1040.line10 and eic.clergy, and both gates are unchanged.
- f8962.marriage.no.then1: line24 and line25 gained a first gate (dependent_filer), so marriage is gate 3 after alloc (gate 2). Order is preserved, so the argument is sound; the text was corrected.
- f8962.marriage.no.then2: same as the previous line.
- f8962.marriage.no.then3: same as the previous line.
- f8962.marriage.no.then4: same as the previous line.
- s1a.line10_over.line9.gt.1: only f1040.status's readers changed; the argument does not use them.
- s1a.line13_figured.line12: same as the previous line.
- s1a.line18_over.line17.gt.1: same as the previous line.
- s1a.line21_figured.line20: same as the previous line.

## Federal: retargeted

- sa.deduction.standard.then1: the mutant now reads sa.standard_amount (sa.standard's false alternative), not standardraw. Re-read: a known-false itemizes still means a complete standard, which took its false alternative, so the two are the same memoized value. With itemizes unknown, line 17 is no refusal, so deduction is the guard's unknown whatever standard_amount is. Sound. reads, the text and the premises were changed (standardraw and extra_blind replaced by standard_amount) and the argument re-pinned.

## Federal: removed

- f8960.line9d.line9c: the mutant is now killed.
- sa.standard.zero.then0: the mutant (now reading sa.dep_line4c) is killed.
- dependent.qr_kidnapped.no.then1: the mutant (now reading qr_income_fails) is killed.
- dependent.qr_other_relation.household_all_year...: the mutant id is gone, because qr_other_relation is now a choose on spouse_relative_joint over qr_other_lawful. No surviving mutant replaces it: there is no unexplained survivor on qr_other_relation, qr_other_lawful, qr_household_member or spouse_relative_joint, and the one survivor there is explained structurally.

## NY: re-pinned

- ny_it201.gate.spouse_nonresident.no.then{0,2,3,4}: only f1040.status's readers changed (the dependent leak fix added the reader dependent.spouse_relative_joint, among others). The argument uses the status only as an input with no gates. The uncommitted digest 4c1666eba2a00b9d already in the worktree matched neither HEAD nor the current canonical; it is replaced by 9e361ace9b94cb5b.

## Note

Thirteen of the pins (hoh x4, testing_failed, s1a x4 and NY x4; these pin f1040.status) and every pin on a constant
line (person.zero, dependent.no and others) move whenever any lane adds a reader of that line. A concurrent change
by lane X-K1 can therefore make them stale again without any change in soundness.

## Step results after the edits

- `node engine/dist/main.js mutate`: 0 stale arguments, retargeting self-test 0 problems, every self-test 0 problems,
  sampled check 0 problems; exit 1, because 372 surviving mutants have no explanation (`reports/2025/mutation.md`, "Surviving — not
  yet explained"). These were already unexplained in the release run (the run's 429 unexplained = these 372 + the 57
  survivors whose arguments were stale). None is a stale argument: about 300 are on forms and lines new in the coverage
  expansion (f1116, f1116col, f1116sb, k1p, k1s, rental, f8582, rec, royalty, f7203, sche, rprop, scveh, and person.k1p_*
  filters), and about 70 are on changed existing lines (eic.check_27c, f4137, f8919, person.earned_not_w2, f2441.mfs_qp_*,
  household.mfs_apart_last6, ...). Out of this lane's scope.
- `node engine/dist/main.js mutate --ny`: 0 problems, exit 0.
