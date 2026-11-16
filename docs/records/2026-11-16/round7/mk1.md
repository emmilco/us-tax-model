# Lane mk1: mutation family K-1 (k1p, k1s, f7203, person.k1p_* / k1s_* filters)

Lane mk1. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. 2026-11-16, round 7.
Worktree `.claude/worktrees/mk1` (detached at 6649c637, the release candidate's tested tree). No commit, no
check_all, no paid call. Patch: `round7/mk1.patch` (fixtures/2025/k1p.json, fixtures/2025/k1s.json,
engine/src/mutate.ts lane block, bug_pending/mk1-01.md).

## Summary

- Family: 134 unexplained survivors in reports/2025/mutation.md that match k1p, k1s, f7203 or f4952. **The 2 f4952
  survivors (`f4952.exception`) are not K-1 related** (f4952 reads no K-1 line); I left them to their own family.
  That leaves 132.
- **114 killed** by 50 new fixture cases (k1p.json +34, k1s.json +30; ids `mk1.k1p.*`, `mk1.k1s.*`).
- **11 argued equivalent** in EQUIVALENT_IF, one block `// ---- lane mk1 begin/end ----`, pinned with premiseDigest.
  Each `holds()` returns true on the built data.
- **3 left to the structural "no observable reader" rule**: k1s p1_loss, p2_loss and p3_loss (coordinator
  instruction 2). I removed their keyed arguments.
- **4 open**: the k1s choices whose `k1s.ok = false` branch can only be reached through a malformed Form 7203 roster
  (see "Open").
- **1 defect drafted**: BUG-NEW-mk1-01, Form 7203 column (c) can exceed line 10 when the ratio rounds up.
- **What I did not use**: the witness list. I designed my own witnesses from the expressions and wrote them before it
  arrived. It then confirmed the same lines: its 78 "equivalence candidates" are mostly helper-only lines (the person
  totals, sche_row, passive_loss and others), and the new fixtures assert those directly.
- **Fixture placement**: the f7203 cases are in k1s.json, not a new f7203.json, because f7203 is the implicit
  collection nested under each k1s entry (`$f7203@person[...].k1s[...]`), and existing f7203 assertions already live
  in k1s.json.
- **scope.k1**: every new case sets `"scope.k1": true`. Each one asserts only K-1 form lines or the person totals,
  never a return-level line, so the cases stay valid after the K-1 wiring unit.

## Scope change mid-lane (coordinator)

**Hand-off.** Lane M-K1S took over k1s and f7203 after these cases were written.

- My k1s.json cases (ids `mk1.k1s.*`) stay in the patch, to be merged by id.
- The k1s/f7203 mutants they handle are listed in `round7/mk1-handled-k1s.txt`.
- I wrote nothing for k1s or f7203 after the hand-off.

**No-reader survivors.** These are left to the separate structural "no observable reader" rule. I removed my keyed
arguments for the k1s ones (p1_loss, p2_loss and p3_loss). Fixtures I had already written still kill several of them,
for example the k1p sche_row operands, passive_loss, prior_total and the person filters, and those kills stand.

**Verification limits.** I ran no full mutate, and no mutant_witness search. The kill check below runs only my own
ids, on the two fixture files.

## How predictions were made and checked

- For each case I worked out the value by hand from i1065sk1 (pp. 9, 11, 14 to 15, 22), i1120ssk (pp. 4 to 7, 17),
  i7203 (pp. 2 to 4) and i8582 (p. 10). The case's evidence_note records that arithmetic and the page cites. I did
  this before running the evaluator.
- Refusal expectations take their gate, form, remedy and cite from the form's own refusal entry, plus the manifest's
  revision and snapshot.
- **Evaluation**: a script resolves each case with the fixture defaults (`resolveCase`), evaluates it, and compares
  the result with `isDeepStrictEqual`, as test-fixtures does. All 61 k1p cases (27 existing + 34 new) and all 47 k1s
  cases (17 + 30) pass on the data. Every new case matched its hand prediction on the first evaluation; no expectation
  was revised after running.
- **Kills**: the same script applies each of the 132 mutations (`mutations(data)`, `m.apply`) and re-evaluates every
  case of both files. A mutant counts as killed when some expectation's value changes, compared by mutate.ts
  `normal`.
- **Not run**: a federal `mutate` run, and lane MW's `mutant_witness.mjs`. MW's tool judges only value-sheet lines,
  while most of these kills land on helper lines and person totals. So the kills are verified directly against the
  mutations, but not inside a mutate run.
- **Build**: `node engine/dist/main.js build` with the new fixtures and the mutate.ts block ended "build OK" (exit 0). It included the fixture-path reachability check. After I removed the 3 arguments, the engine was recompiled and all 11 remaining arguments' `holds()` are true.

## Per mutant

| Mutant | Outcome | Killed by / argument | Verified vs inferred |
| --- | --- | --- | --- |
| `boundary.f7203.f7203.dist_over` | killed | `mk1.k1s.f7203_distribution_equal_to_basis` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_count` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_count_general` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_count_inv` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_count_passive_loss` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_backup_wh` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_collectibles` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_nonpassive` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_nonpassive_loss` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_ord_div` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_p4_income` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_p4_loss` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_p5_income` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_p5_prior` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_p6_loss` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_prior` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_qbi_stmt` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_qual_div` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_se_pos` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_st_gain` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_taxexempt_int` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1p_total_unrecap_1250` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `filter.person.person.k1s_count_sche` | killed | `mk1.k1s.count_schedule_e_rows` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.f7203.f7203.l3f.zero` | killed | `mk1.k1s.f7203_dividends_and_gain_with_loss` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.f7203.f7203.l3h.zero` | killed | `mk1.k1s.box3_loss_box7_gain` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.f7203.f7203.line14.line11` | killed | `mk1.k1s.f7203_loss_over_basis_line14` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.any_loss.box14a_if_any.any.5.lt.0` | killed | `mk1.k1p.box14a_loss_not_material` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.any_loss.box3_if_any.any.2.lt.0` | killed | `mk1.k1p.passive_box3_loss_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.any_loss.box9a_if_any.any.4.lt.0` | killed | `mk1.k1p.box9a_loss_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.ask_five.under500.all.0.eq.0` | killed | `mk1.k1p.refuse_test6` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.ask_other.five_of_ten_if_asked.all.1.eq.0` | killed | `mk1.k1p.limited_test5` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b1_loss_sum.b1_net_loss` | killed | `mk1.k1p.passive_three_losses` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b1_net_income.zero.then1` | killed | `mk1.k1p.material_box1_box3_loss` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b1_pos.zero` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b2_pos.zero` | killed | `mk1.k1p.box1_loss_box2_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b3_neg.box3_if_any` | killed | `mk1.k1p.passive_three_losses` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b3_net_loss.b3_neg` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b3_overall_loss.b3_net_income` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b3_pos.zero` | killed | `mk1.k1p.box2_loss_box3_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.col_i.zero.then0` | killed | `mk1.k1p.passive_box1_with_guaranteed_payments` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.has_activity.has_b2.any.1.eq.0` | killed | `mk1.k1p.box2_income_prior_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.has_activity.has_b3.any.2.eq.0` | killed | `mk1.k1p.box3_income_prior_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.p4_income.zero.then1` | killed | `mk1.k1p.passive_three_losses` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.p5_b2_income.b2_net_income.then1` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.p5_income.b3_net_income` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.p5_income.p5_b2_income` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.passive_loss.b1_loss_sum.any.0.gt.0` | killed | `mk1.k1p.passive_box1_loss_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.passive_loss.b3_loss_sum.any.2.gt.0` | killed | `mk1.k1p.passive_box3_loss_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.prior_total.prior_b1_if` | killed | `mk1.k1p.passive_three_income_with_priors` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.sche_row.box1_if_any.any.0.ne.0` | killed | `mk1.k1p.passive_box1_income_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.sche_row.box2_if_any.any.1.ne.0` | killed | `mk1.k1p.box2_income_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.sche_row.box3_if_any.any.2.ne.0` | killed | `mk1.k1p.passive_box3_loss_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.sche_row.box4a_if_any.any.3.gt.0` | killed | `mk1.k1p.guaranteed_payments_only` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.sche_row.prior_total.any.4.gt.0` | killed | `mk1.k1p.box1_zero_prior_loss` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.se_loss_not_material.material.all.1.eq.0` | killed | `mk1.k1p.material_box1_and_se_loss` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.former_passive.b1_prior_if_any.all.1.gt.0` | killed | `mk1.k1s.refuse_former_passive` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.g28.box8b_if_any.then0` | killed | `mk1.k1s.box7_loss_box8_gain` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.gain2.zero` | killed | `mk1.k1s.passive_box1_loss_box2_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.gain3.zero` | killed | `mk1.k1s.box2_loss_box3_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.gain7.zero` | killed | `mk1.k1s.box3_loss_box7_gain` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.gain8.zero` | killed | `mk1.k1s.box7_loss_box8_gain` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.has_loss.loss_items.gt.0` | killed | `mk1.k1s.refuse_not_at_risk` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p1_loss.b1_passive` | killed | `mk1.k1s.passive_box1_loss_box2_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p2_income.zero` | killed | `mk1.k1s.passive_box1_loss_box2_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p3_income.zero` | killed | `mk1.k1s.box2_loss_box3_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p4_income_raw.p2_income.then0` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p4_income.p4_income_raw.then0` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p4_prior_raw.b2_prior_if_any.then0` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p4_prior.p4_prior_raw.then0` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p5_b2_income.zero.then1` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p5_income_raw.p3_income` | killed | `mk1.k1s.box2_loss_box3_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p5_loss_raw.p1_loss` | killed | `mk1.k1s.passive_box1_loss_box2_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.p5_loss_raw.p5_b2_loss` | killed | `mk1.k1s.passive_box1_loss_box2_income` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.part4.active_if_b2.all.0.eq.0` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.part4.tenth_if_active.all.1.eq.0` | killed | `mk1.k1s.rental_active_with_prior_and_box3` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.past_ask.mp_now.all.1.eq.0` | killed | `mk1.k1s.test1_earlier_years_not_used` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.qbi_cut.qbi_stmt_if_any.all.0.lt.0` | killed | `mk1.k1s.passive_loss_over_basis_qbi_loss` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.qbi.qbi_stmt_if_any.then0` | killed | `mk1.k1s.material_box1_qbi` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.sche_any.box1_any.any.0.eq.0` | killed | `mk1.k1s.count_schedule_e_rows` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.sche_any.box2_any.any.1.eq.0` | killed | `mk1.k1s.count_schedule_e_rows` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.sche_any.box3_any.any.2.eq.0` | killed | `mk1.k1s.count_schedule_e_rows` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1s.k1s.under500.hours500_if_work.all.1.eq.0` | killed | `mk1.k1s.test3_with_ptp_qbi` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.f7203.f7203.one.0` | killed | `mk1.k1s.refuse_f7203_election` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.1` | killed | `mk1.k1p.refuse_box4b` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.10` | killed | `mk1.k1p.refuse_box17` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.11` | killed | `mk1.k1p.refuse_box20` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.12` | killed | `mk1.k1p.refuse_box21` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.14` | killed | `mk1.k1p.refuse_foreign` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.16` | killed | `mk1.k1p.refuse_box19_other` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.18` | killed | `mk1.k1p.refuse_z_other` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.2` | killed | `mk1.k1p.refuse_box7` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.20` | killed | `mk1.k1p.refuse_test6` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.22` | killed | `mk1.k1p.refuse_test7` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.4` | killed | `mk1.k1p.refuse_box11` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.5` | killed | `mk1.k1p.refuse_box12` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.6` | killed | `mk1.k1p.refuse_box13` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.7` | killed | `mk1.k1p.refuse_box14bc` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.8` | killed | `mk1.k1p.refuse_box15` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1p.k1p.screened.9` | killed | `mk1.k1p.refuse_box16` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.1` | killed | `mk1.k1s.refuse_disposed` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.10` | killed | `mk1.k1s.refuse_box16ef` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.11` | killed | `mk1.k1s.refuse_box17_other` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.12` | killed | `mk1.k1s.refuse_v_other` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.14` | killed | `mk1.k1s.refuse_former_passive` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.15` | killed | `mk1.k1s.refuse_basis_carry` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.16` | killed | `mk1.k1s.refuse_risk_carry` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.17` | killed | `mk1.k1s.refuse_not_at_risk` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.2` | killed | `mk1.k1s.refuse_box6` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.3` | killed | `mk1.k1s.refuse_box8_stmt` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.4` | killed | `mk1.k1s.refuse_box9` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.5` | killed | `mk1.k1s.refuse_box10` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.6` | killed | `mk1.k1s.refuse_box11_12` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.7` | killed | `mk1.k1s.refuse_box13_other` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `refusal.k1s.k1s.ok.8` | killed | `mk1.k1s.refuse_box14` | verified (evaluated: case passes on the data, expectation changes on the mutant) |
| `operand.k1p.k1p.b1_neg.zero` | argued | pinned: b1_neg = max(0,-B); mutant max(0, max(B,0)-B), identical for every B; no gate on either route | holds() verified; equivalence is inferred (argument), checked on all 61 k1p cases (no expectation moves) |
| `operand.k1p.k1p.b2_neg.zero` | argued | same pattern on box 2 | as above |
| `operand.k1p.k1p.b3_neg.zero` | argued | same pattern on box 3 | as above |
| `operand.k1s.k1s.loss1.zero` | argued | same pattern, k1s.gain1 / box1_if_any | holds() verified; argument inferred |
| `operand.k1s.k1s.loss2.zero` | argued | same pattern, box 2 | as above |
| `operand.k1s.k1s.loss3.zero` | argued | same pattern, box 3 | as above |
| `operand.k1s.k1s.loss7.zero` | argued | same pattern, box 7 | as above |
| `operand.k1s.k1s.loss8.zero` | argued | same pattern, box 8a | as above |
| `operand.k1s.k1s.np_loss.zero` | argued | same pattern, np_income / b1_np | as above |
| `operand.k1s.k1s.p1_loss.zero` | left to the structural "no observable reader" rule (coordinator) | equivalent by the same floor pattern, but it has no value-sheet reader, so no keyed argument was written | inferred |
| `operand.k1s.k1s.p2_loss.zero` | left to the structural "no observable reader" rule (coordinator) | equivalent by the same floor pattern, but it has no value-sheet reader, so no keyed argument was written | inferred |
| `operand.k1s.k1s.p3_loss.zero` | left to the structural "no observable reader" rule (coordinator) | equivalent by the same floor pattern, but it has no value-sheet reader, so no keyed argument was written | inferred |
| `operand.k1p.k1p.active.decisions_if_asked.all.0.eq.0` | argued | decisions_if_asked true implies ask_active true; false makes tenth_if_decisions false; unknown makes both conjunctions unknown | holds() verified; argument inferred |
| `operand.k1s.k1s.p1_income.zero` | argued (reader) | p1_income itself can differ where ok is a refusal or unknown. Its only readers, passive_income and p5_income_raw, are read only by col_h and p5_income, which choose on ok and agree on both routes. Readers checked by grep over forms/2025 | holds() verified; the reader list is pinned in the digest |
| `operand.k1s.k1s.col_k.zero.then1` | **open** | see Open | inferred |
| `operand.k1s.k1s.col_i.zero.then1` | **open** | see Open | inferred |
| `operand.k1s.k1s.col_h.zero.then1` | **open** | see Open | inferred |
| `operand.k1s.k1s.p5_income.zero.then1` | **open** | see Open | inferred |
| `operand.f4952.f4952.exception.line4c.all.0.gt.0` | not taken | not K-1 related | n/a |
| `operand.f4952.f4952.exception.line1_if_interest.all.0.gt.1` | not taken | not K-1 related | n/a |

## Open: the k1s.ok false branch (4 mutants)

**The four lines.** `k1s.col_k`, `col_i`, `col_h` and `p5_income` each choose on `k1s.ok`:

- `ok = true` takes the computed value.
- `ok = false` takes `k1s.zero`. The four mutants replace that zero with another line.

**When ok is false.** `k1s.ok` is `k1s.f7203_n = 1`, and f7203 is an implicit collection with one entry per K-1. So
ok is true or a refusal on every interview return. It is false only when an input gives a `$f7203@...k1s[x]` roster
with no entries or with two or more. `validateInputs` accepts such a roster.

**How the mutants could be killed.**

- `col_i` and `p5_income` with an empty roster.
- `col_k` and `col_h` with two entries and a loss.

**Why I did not kill or argue them.**

- **No kill**: a fixture would have to pin "$0 for a K-1 with no (or two) Forms 7203". The sources give no such value;
  it is a model design choice.
- **No argument**: the mutants are not equivalent on every input. ANSWERED_ONLY is about withheld answers, not roster
  shapes.

**Owner decision needed.** Pick one:

- (a) Make a non-single f7203 roster a refusal or a build-time input error. Then the branch is unreachable and an
  argument can pin it, including the collection's `implicit`, which the premise digest does not cover today, so
  `holds` would need an extra check.
- (b) Accept a fixture that pins the zero.

## Defect drafted

**BUG-NEW-mk1-01** (bug_pending/mk1-01.md, low, latent).

- **Case**: box 1 loss $30,000 with materially participation and stock basis $20,000. f7203.c35 and c47 are
  **$20,000.01**, because the ratio 0.666667 rounds up. That is above line 10 ($20,000).
- **Effect**: k1s.col_i is $20,000.01, so a loss one cent above stock basis is allowed. The instruction is i7203 p. 4:
  "The total allocation amount reported in column (c), line 47, can't exceed the amount reported on line 10".
- **What the model caps instead**: only f7203.line11, which no K-1 line reads.
- **The fixture does not pin the wrong value**: `mk1.k1s.f7203_loss_over_basis_line14` asserts lines 10, 11, 14 and
  15, which are right under either reading, and does not assert c35 or col_i. Once the defect is fixed, c47 <= line 10
  always, and `operand.f7203.f7203.line14.line11` becomes equivalent. The fixture's line 14 still holds.

## Notes for the owner (not new defects)

- `mk1.k1s.rental_active_with_prior_and_box3` puts a held-back box 2 loss in Part IV column (c). The scenario states
  active participation in both years. BUG-0883 (open) says the form does not ask about the loss year. If BUG-0883 is
  fixed by adding a refusing `prior_not_active` input that defaults to No, the case stays valid.
- Two cases give an answer that is gated off on the data:
  - `mk1.k1p.limited_test5`: t6 true. It kills `ask_other`, because the mutant asks t6 and refuses.
  - `mk1.k1s.test1_earlier_years_not_used`: past_years true. It asserts the gate `k1s.past_years_if_ask` = false and
    kills `past_ask`.

  The second one asserts interview behaviour (the earlier-years test is not reached once test 1 holds), not a tax
  amount. Both resolve with the fixture defaults without error.
- No witness addendum (`k1.addendum.md`) had appeared when I finished.
