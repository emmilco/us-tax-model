# B1 integration (goal-1 round): running log

Worktree: `.claude/worktrees/nx-b1`, base `refs/scratch/batchB2` (0fb40f25). Lanes are uncommitted trees on
`refs/scratch/g1-base` (b3dc1c0b). Lane diffs saved to `/tmp/b1/<lane>.diff` (excluding rendered/canonical/reports).

No lane file overlaps the g1-base -> batchB2 changes (checked by name), so every conflict is lane-vs-lane.
Files touched by more than one finished lane: questions.yaml (6), consumers.json (3), classm.json (3),
check_all_steps.sh, stage4.yaml/sales.yaml (deleted by T7), mutation.json, f8962.json, defaults.json,
classm.gpt/deepseek.json, interview-rules.ts, generate.ts, classm.ts, ambiguities/2025.yaml.

## Log
- t1, t5: applied cleanly (`git apply --3way`).
- t7: applied cleanly (fixture walk-line deletions, the three slice profiles deleted).
- t2: one text conflict in engine/src/interview-rules.ts: T2's diff context still had the slice-profile
  `INITIAL_ALLOWED` constants that T7 removed; kept T7's `PROFILES = ["full","ny"]` (no slice initial), plus T2's one
  added doc line. Verified fixtures classm*.json and f8962.json by case id against t2+t7 (0 problems;
  `/tmp/b1/tools/verify_merge.py`).
- Check after tools lanes: running (`/tmp/b1/check-tools.log`).
- f10 reported finished by coordinator (wording on otjob/tipjob/carloan, consumers +5 keys); queued after the forms lanes.
- Check after tools lanes (t1 t5 t7 t2): compile, build (1167 s), render, render --ny OK; test-fixtures 2003/2003,
  --ny 357/357; year_changes --check, citations --strict (0 findings), check_consumers (0 new) all rc 0.
- Forms lanes f7a, f8, f12, f2, f3, f4, f1, f10 applied with `git apply --3way`, excluding g1-plan.md (identical in
  every lane), reviews/2025/consumers.json (merged by key, `/tmp/b1/tools/merge_keyed_json.py`: rulings 451 -> 471,
  baseline 307 -> 306) and F1's edits to the deleted interview/2025/{sales,stage4}.yaml (dropped). No text conflict
  otherwise. Semantic check by id (`verify_merge.py`, recursive into case inputs): questions.yaml (859 entries),
  ny questions.yaml, consumers.json, defaults.json, classm/classm.deepseek/classm.gpt (T2's input edits and F1's
  rename land in the same 42 cases, different keys), mutation, f8962, f8889, carloan, s1, refund fixtures,
  coverage hsa/care/home: 0 problems. No (order, seq) collision in the merged bank.
- Coordinator items applied:
  - F7a: s1.ebl_threshold locator is now `p. 17, .32 Threshold for Excess Business Loss, "$313,000 ($626,000 for joint
    returns)"`; the proposed "section 2.32" anchor ruling deleted from reviews/2025/citations.json. citations --strict:
    0 findings, 0 unused rulings. The s1.line3 refusal cite text "rp-2024-40 section 2.32" (an i1040gi citation's
    trailing pointer, quoted in 4 s1.json refusals) kept as F7a left it.
  - F8: changes/2026/person.retirement.yaml C-PEOP-11, person.ira_trad help `to`: "your 2024 return" -> "your 2025 return".
  - F2: ny_it201.federal_care label: "so you (and your spouse) could work" -> "so you (or, on a joint return, your
    spouse) could work".
  - T5: reviewed the relaxed f1095a route assertion in test_classm_jobs.mjs: it exempts only `c_total`, only when
    `same_months` is shown true (f1095a.no_aptc reads it before the route is settled); every other assertion unchanged.
    Sound.
- Placeholders for entries batch A/B already numbered, rewritten in this round's pending files: g1-close-12 (closes
  ty26-o2-01 = BUG-0649, o6-01 = BUG-0653, o3a-01 = BUG-0650); g1-t1-01 (ty26-o5-01 = BUG-0644).
- Check after forms batch 1 (f7a f8 f12 f2 f3 f4 f1 f10): build OK (916 s), render both; test-fixtures 2011/2011
  (2003 + F3 2 + F4 2 + F1 4), --ny 357/357; year_changes --check rc 0; citations --strict 0 findings, 0 unused
  rulings; check_consumers 0 new, 0 stale.
- Quick checks after batch 1: tick-groups, check_questions, check_screens, check_false_no, check_twins rc 0.
  siblings --check rc 1: only "no review log changed since HEAD" on this round's entries, plus BUG-0655 (batch B:
  Fix field without Siblings checked; not this round's). check_bug_inventory rc 1: only placeholders of
  already-numbered entries cited in docs (g1 lane reports, g1-plan.md, coordinator-followups.md) -- to map at the end.
- mutate (federal) started on the batch-1 tree (`/tmp/b1/mutate-1.log`) to refresh F3's stale keyed arguments early.
- mutate run 1 (batch-1 tree): 7524 mutants, 366 surviving; 26 stale arguments + 5 survivors with no argument.
  - Stale arguments: diffed each argument's premise facts between a g1-base build (nx-t7/canonical) and this tree
    (`/tmp/b1/tools/premise_diff.mjs`). 24 moved this round, each by a change the argument does not depend on:
    new readers (refund.joint on f1040.status: s1a x4, dependent, household x4, f8962 x4; F1's new f8889 lines on
    household.married, f8889.no, coverage_year, eligible_all, marriage_possible; f8889.yes lost testing_if_asked);
    a refusal gate appended last on f8889.line13_figured (bad_months x2: the argument's "after mfs, the first gate"
    still holds); refusal remedy/cite text (f8962 line24/25: F3's remedy change, alien_branch's new digest is the one
    F3 predicted; s1.line3's refusal cite: s8812); shown_when added to f2441 Part III lines (display only: f2441 x2).
    Each argument re-read; digests refreshed (`/tmp/b1/tools/refresh_digests.mjs`).
  - 2 were already stale at g1-base with no premise moved this round (sa.gift_carryover_if_no_gifts,
    eic.from_step1_income). Re-read against the current lines: both hold. The sa argument named the wrong parameter:
    sa.no reads the parameter sa.no (false), not household.no; text and premise corrected to `param:sa.no`, digest
    refreshed. eic: digest refreshed.
  - New survivors from lanes that did not run mutate:
    - operand.f8889.f8889.ask_former_spouse_family.no.then1 (F1): not equivalent (a stated Yes to
      former_spouse_family with family coverage refuses under the mutant). Killed by a new fixture
      `g1b1.hsa.family_former_spouse_unread` in fixtures/2025/f8889.json (stage11.hsa.family_all_year_answer with
      former_spouse_family: true; same expected values, predicted from the gate: the question is read only with
      self-only coverage).
    - operand.f8889.f8889.testing_failed_figured.no.then1 (F1) and operand.refund.refund.worksheet.no.then0 (F4):
      equivalent on every input; new pinned arguments in EQUIVALENT_IF (after bad_months.then1), premises built
      from the lines' upstream closure; the upstream of each has no refusal gate (checked).
    - scveh.q4_basis.zero.then1 and sli.divisor.divisor_other.then2: unexplained already at g1-base (F3's report); not
      this round's. Left for the coordinator.
- mutate run 2: test-fixtures 2012/2012; 7524 mutants, 365 surviving (355 equivalent on every input, 8 answered-only),
  0 stale arguments; only scveh.q4_basis.zero.then1 and sli.divisor.divisor_other.then2 unexplained (pre-existing),
  so mutate still exits 1 on them.
- Waiting for lanes f5, f6, f7b, f9, f11, t3.

## State at handback (partial: run ended before the remaining lanes arrived)

Merged: t1, t5, t7, t2, f7a, f8, f12, f2, f3, f4, f1, f10. Not merged: f5, f6, f7b, f9, f11, t3 (method above applies;
merge tools: /tmp/b1/tools/verify_merge.py, merge_keyed_json.py, premise_diff.mjs, refresh_digests.mjs; diffs
/tmp/b1/<lane>.diff; check scripts /tmp/b1/check.sh TAG, /tmp/b1/quick.sh TAG).
Not yet done (all need to wait for the remaining lanes): `new_bug.py --assign` (once, at the end) and mapping
placeholders in untracked docs; regeneration (interview-coverage --write, interview-rules --write-pruning,
interview-length --write and interview-words --write, spouse-wording --report, coverage/tree.py, bug_status.py --write,
mutate --ny); interview-rules, self_tests.py; the final siblings/check_bug_inventory pass.
The git index of nx-b1 holds the merged tree (`git add -A` used; nothing committed).

## Round 2 reviews (from the merged lanes' reports)
- s1 (F7a): render line-scoped (line9, line10, ebl_threshold, line3 + 5 inputs); transcription (5 inputs, 4 cites);
  question review (scholarship_taxable, cod_any, cod_amount, alaska_dividend, prizes). scope: land3-holes rerun still due.
- person (F8): transcription line-scoped + render; completeness. dependent (edu twins), f8863 (paid, ban), ira
  (deferred_comp), retirement (rollover): transcription + render. Question review at the release sample.
- ny_it201 (F12 + B1's federal_care label), ny_it2: render, line-scoped transcription; screen/false-no/question
  review at the sample (incl. gate ny_it201.federal_care, per F2).
- f2441 (F2): transcription + render line-scoped (care, spouse_died, lines 12-31); class M whole form. dcprov: render
  (+ transcription of dcprov.paid). Question review of care, spouse_died, dcprov.paid.
- f1095a (F3): transcription + render (new helpers, 13 column-B sources); class M whole. f8962: render + transcription
  (nonuniform); class M whole. Question review of $f1095a, in_b_*, mo_b help.
- refund (F4): class M whole, render whole, transcription; sa: render + transcription line-scoped (dry run $2.01);
  screen/false-no on refund.two_returns, two_itemized and their gates at the sample.
- f8889 (F1): transcription + render line-scoped; class M whole; sampled question/screen/false-no for inherited_case,
  ira_gap, disabled, former_spouse_family, archer, employer_in_box1.
- otjob, tipjob, carloan (F10): transcription + render; question review at the sample.
- Class M --force-rerun for the corpus restatement (T2): aqee, carloan, clcw, dependent, f1040, f5329, f8863, f8880,
  f8960, f8995, f8995a, g28, ltc, otjob, person, s2, sc, sd, sdtw, se, sli, tax_on_amount, u1250, w2 (24); +14 to
  clear BUG-0752 (asset, clcw_next_year, f4952, f8962, qdcg, s1, s179, s8812, sa, sales, sb, scveh, ssb, tcw).
- t1, t5, t7: none.

## Resumed (coordinator: finish B1)

- Lanes f5, f11, f6, f9, f7b, t3 applied with `git apply --3way`, excluding fixtures (merged by case,
  `/tmp/b1/tools/merge_nway.py`, N-way and recursive into inputs), consumers.json (by key: rulings 451 -> 485,
  baseline 307 -> 305), the deleted stage4/sales/social-security.yaml (F6, F7b, F9 edits dropped), the source catalogs
  (manifest.json merged by text and checked by id; tools/sources/2025.json merged by id; 289 -> 292: F6's
  cfr-26-1-170a-13, F11's cfr-26-301-7701-7 and i5471) and engine/src/mutate.ts (below). One text conflict:
  docs/provisional/DECISIONS.md, F9 and F7b both wrote a section 4: kept F9's as 4, F7b's as 5.
- lmut's three mutation.json cases merged by case (its own HEAD as its base). Restated inputs on them and on T3's new
  case to the merged tree: `s2.amt_owed` dropped (F7b), `f8889[hsa].inherited` -> `inherited_any` (F1), and
  `f1040.withheld_other_any: false`, `sd.qof: false` stated as on every other mutation case (T3, F6).
- Checked by id against every lane: all fixture files (only my fixture and lmut's 3 cases are beyond the lanes),
  questions.yaml (866 entries; no seq collision), every changed coverage file, consumers.json.
- Decisions applied:
  - F7b option (b): s2.line3 has no refusal entries; s2.line2 refuses on s2.amt only; s2.line1z refuses on s2.other
    (the same entry). Expectations restated after the build (below).
  - F9: classm.sdtw.5 `household.home_cost: false` (input only).
  - T3 T-250: row moved to TASKS-DONE.md, closed under D7.
  - BUG-0755: Status fixed, Fix cites lmut's three cases.
  - Old placeholders (ty26-*, land3-adj*, landing-NN) rewritten to their numbers in coordinator-followups.md and the
    round's lane docs (landing-NN have no number: written as `landing-NN`).
- mutate.ts: T3's mutate-worker.ts held aside; building with the old digest function first.
- Check after batch 2 (old digest function): build OK (1652 s), render both; test-fixtures 2026/2028 then 2028/2028
  after two restatements: `stage4.refuse.s2.other` s2.line2 refusal(s2.other) -> $0 (option (b); no AMT owed on
  $100,000 of wages, single; evidence_note added) and `classm.s2.1` `household.home_cost: false` (input only: F7b's
  computed AMT now reads the tax, which reads F9's head-of-household check on a single filer with a dependent; F9's
  treatment of the same kind of case); --ny 357/357; year_changes, citations --strict (0), check_consumers (0 new).
- mutate.ts, the sequence used:
  1. Old digest function on the merged data: 30 arguments stale + 4 New York (spouse_nonresident x4). Premise diffs
     against the g1-base build: new readers only (F9's person.sc_*_count on sc.one, household.no, f1040.status;
     F7b's s2.amt_* on sa.itemizes, f1040.line11b, f1040.status; s2.mortgage_subsidy_if_interest on sa.home_asked;
     F9's renamed s3 gate reading s3.prior_other_forms), plus two structural changes:
     - household.hoh_fails gained F9's refusal gate household.hoh_missed: the hoh_community_property arguments hold
       (hoh_missed's upstream does not read the mutated line; a gate is evaluated at entry, the same on both routes).
     - sc.ho_both_limits gained `ho_uses = true` first (F5): `operand.sc.sc.ho_both.zero` no longer holds (with no
       home office and line 29 below the section 179 amount, printed worksheet line 5 differs). F5's own fixture
       `bug0489.sc.no_home_office_with_179_limit` is that return and kills the mutant, so the argument was removed.
     Re-pinned under the old function (all 98 recorded current).
  2. `repin.mjs before` (EQUIVALENT_IF exported, as T3 has it).
  3. T3's mutate.ts merged onto the B1 version with `git merge-file`: conflicts were digest literals only (or my two
     new arguments, the sa.no correction, the removed sc argument); kept B1's literals, T3's structure (incl. `premises`
     on the closures). T3's mutate-worker.ts restored.
  4. `repin.mjs after`: 46 literals replaced. s8812.line18a (a closure that did not expose premises before) re-pinned
     by hand. All 101 pinned arguments hold on the merged data (checked by `holds`).
- Coordinator items: T-250 closed (TASKS-DONE.md); g1-t3-01 marked fixed.
- Running: mutate (federal, with T3's sampled check) then mutate --ny (`/tmp/b1/mutate-3.log`, `mutate-ny.log`).
- F7b coverage: with option (b) the ISO rows (other.iso_kept, other.iso_vested_2025) pass unchanged; other.amt_owed
  completed with the answers its walk opens (f8960.refund: false, qbi.coop_patron: false). `--rows other.yaml`:
  34 rows, 0 problems.
- DECISIONS.md section 5 rewritten for option (b) (what, why, by, the four restated expectations, how to reverse).
- interview-rules --write-pruning on the merged tree: 10 problems, none an error of the merge's own making that I could
  trace: two templates no longer leak (removed from the baseline as the tool asks), and eight new findings of T2's
  widened sample on the merged tree (early completion: dependent.disabled, which T2's own sweep found and probed;
  out of bank order: eic.legally_separated (also in T2's sweep), eic.same_home, ny_it201.ask.moved_out; asked and
  unread on New York generated returns: dependent.born_died, kidnapped, months, placed). Held in
  tools/interview_rules_baseline.json with the reason "found at integration B1 ... cause not traced", as T2 held its
  own; FOR THE COORDINATOR. Rerun pending to confirm 0 problems.
- mutate (federal, T3's sampled check) on the merged tree: 7758 mutants, 0 stale arguments, every self-test 0 problems;
  sampled check 113 arguments, 1 problem: it contradicted my refund.worksheet argument (received_if_worksheet, a gate
  line, differs, and T3's check holds every non-helper reader). Replaced by a kill: expectation
  `refund.received_if_worksheet` $0 added to F4's `g1f4.refuse.refund.two_itemized` (refund.received is stated
  $2,000; the one-return worksheet is not used); evaluated: base $0, mutant $2,000. Argument removed.
- 83 survivors unexplained, all on lines lanes F7b (71), F9 (10) and F5 (2) added without running mutate: recorded
  as pending BUG-0656 for a follow-up mutation lane (not attempted in B1). mutate exits 1 on them.

- new_bug.py --assign: 102 pending entries -> BUG-0656 to BUG-0757 (map below); no placeholder left in any tracked file (format text in the tool docs untouched). bug_status --write: 757 entries, 43 open. check_bug_inventory: OK (0 pending).

```
g1-b1-01 -> BUG-0656
g1-close-01 -> BUG-0657
g1-close-02 -> BUG-0658
g1-close-03 -> BUG-0659
g1-close-04 -> BUG-0660
g1-close-05 -> BUG-0661
g1-close-06 -> BUG-0662
g1-close-07 -> BUG-0663
g1-close-08 -> BUG-0664
g1-close-09 -> BUG-0665
g1-close-10 -> BUG-0666
g1-close-11 -> BUG-0667
g1-close-12 -> BUG-0668
g1-close-13 -> BUG-0669
g1-close-14 -> BUG-0670
g1-close-15 -> BUG-0671
g1-close-16 -> BUG-0672
g1-f1-01 -> BUG-0673
g1-f1-02 -> BUG-0674
g1-f1-03 -> BUG-0675
g1-f1-04 -> BUG-0676
g1-f1-05 -> BUG-0677
g1-f1-06 -> BUG-0678
g1-f1-07 -> BUG-0679
g1-f1-08 -> BUG-0680
g1-f2-01 -> BUG-0681
g1-f2-02 -> BUG-0682
g1-f2-03 -> BUG-0683
g1-f2-04 -> BUG-0684
g1-f2-05 -> BUG-0685
g1-f2-06 -> BUG-0686
g1-f3-01 -> BUG-0687
g1-f3-02 -> BUG-0688
g1-f3-03 -> BUG-0689
g1-f3-04 -> BUG-0690
g1-f3-05 -> BUG-0691
g1-f4-01 -> BUG-0692
g1-f4-02 -> BUG-0693
g1-f4-03 -> BUG-0694
g1-f5-01 -> BUG-0695
g1-f5-02 -> BUG-0696
g1-f5-03 -> BUG-0697
g1-f5-04 -> BUG-0698
g1-f5-05 -> BUG-0699
g1-f5-06 -> BUG-0700
g1-f5-07 -> BUG-0701
g1-f6-01 -> BUG-0702
g1-f6-02 -> BUG-0703
g1-f6-03 -> BUG-0704
g1-f6-04 -> BUG-0705
g1-f6-05 -> BUG-0706
g1-f6-06 -> BUG-0707
g1-f6-07 -> BUG-0708
g1-f6-08 -> BUG-0709
g1-f6-09 -> BUG-0710
g1-f6-10 -> BUG-0711
g1-f6-11 -> BUG-0712
g1-f7a-01 -> BUG-0713
g1-f7a-02 -> BUG-0714
g1-f7a-03 -> BUG-0715
g1-f7a-04 -> BUG-0716
g1-f7a-05 -> BUG-0717
g1-f7a-06 -> BUG-0718
g1-f8-01 -> BUG-0719
g1-f8-02 -> BUG-0720
g1-f8-03 -> BUG-0721
g1-f8-04 -> BUG-0722
g1-f8-05 -> BUG-0723
g1-f8-06 -> BUG-0724
g1-f8-07 -> BUG-0725
g1-f8-08 -> BUG-0726
g1-f8-09 -> BUG-0727
g1-f9-01 -> BUG-0728
g1-f9-02 -> BUG-0729
g1-f9-03 -> BUG-0730
g1-f9-04 -> BUG-0731
g1-f9-05 -> BUG-0732
g1-f9-06 -> BUG-0733
g1-f10-01 -> BUG-0734
g1-f10-02 -> BUG-0735
g1-f10-03 -> BUG-0736
g1-f10-04 -> BUG-0737
g1-f10-05 -> BUG-0738
g1-f10-06 -> BUG-0739
g1-f11-01 -> BUG-0740
g1-f11-02 -> BUG-0741
g1-f11-03 -> BUG-0742
g1-f11-04 -> BUG-0743
g1-f12-01 -> BUG-0744
g1-f12-02 -> BUG-0745
g1-f12-03 -> BUG-0746
g1-f12-04 -> BUG-0747
g1-f12-05 -> BUG-0748
g1-f12-06 -> BUG-0749
g1-f12-07 -> BUG-0750
g1-t1-01 -> BUG-0751
g1-t2-01 -> BUG-0752
g1-t2-02 -> BUG-0753
g1-t2-03 -> BUG-0754
g1-t3-01 -> BUG-0755
g1-t5-01 -> BUG-0756
g1-t7-01 -> BUG-0757
```

## Final state (tree ready for the coordinator; nothing committed; index = tree via `git add -A`)

Checks on the final tree: test-fixtures 2028/2028, --ny 357/357; year_changes --check, citations --strict (0),
check_consumers (0 new); tick-groups, check_questions/screens/false_no, check_twins rc 0; check_bug_inventory OK
(757, 0 pending); bug_status OK; tier_paths self-test ok; mutate --ny exit 0; mutate (federal) exit 1 on BUG-0656's 83
survivors (the refund.worksheet survivor in reports/2025/mutation.md is killed since; the report predates that fix).
Expected failures until round 2: siblings --check ("no review log changed" on every round form; plus inventory entries
BUG-0649, 0651, 0653, 0655 from batches A/B, append-only), review_tools test
`test_legacy_comparison_blocks_transcription_but_not_render` (reads the live dcprov render log, stale since F2 changed
dcprov.paid).
Not run / not finished (optional regenerations, stopped for time): interview-coverage --write (timed out at 2 h under
load), interview-length --write, interview-words --write, spouse-wording --report, tools/coverage/tree.py,
interview-rules rerun to confirm the updated baseline, a final mutate after the refund kill.

Round 2 adds (batch 2): sc (transcription line-scoped ho_uses/ho_sqft/ho_both_limits/method_other, render, class M);
scveh (transcription, render, class M optional); sales (transcription, render); sd (transcription, render, class M);
div, qbi, f4952 (render), ftc, gift (render + transcription); s2 (transcription, render, class M; about 100 new lines,
plus option (b)'s refusal moves); person (line-scoped: 7 amt_dep lines, 2 sc count lines; class M for those);
household, eic, f5695 (transcription, render; class M household); s3 (transcription, render, class M); sb (render,
transcription line8/unsupported_if_income, class M); samples: sd.qof, gift.special, sales.special, s2.amt_pab/boat/
business, s2.mortgage_subsidy, s2.amt screen, s3.adoption_final/stepchild/prior_amt_deferral, sb line 8 gate.
