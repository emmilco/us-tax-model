# Lane MINT (mutation integrator), round 7

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us and ny. Worktree `.claude/worktrees/mint`
(detached at 6649c637). Patch: `round7/mint.patch` (staged diff against 6649c637). No commits, no check_all, no
paid reviews. Scratch: `round7/mint-work/` (fork work in A/ B/ C/ D/, run logs, `pre.mjs`, `dig.mjs`).

Four forks of this lane (model claude-opus-5-5, class judgment, year 2025, jurisdiction us) analysed the leftovers
in parallel: A (eic, f8962, f8863, mw), B (household, ira, f8853c), C (person, sa, s1, f4137), D (f1116 line 35).
They wrote no file in the worktree. This lane wrote no `agent_runs.jsonl` row: log the lane and its 4 forks.

## Merged

| Patch | Result |
| --- | --- |
| m1116.patch | applied cleanly |
| mk1.patch | 3-way: conflict in engine/src/mutate.ts (lane m1116 and lane mk1 blocks at the same place in EQUIVALENT_IF); both kept, m1116 first |
| mexist.patch | applied cleanly (fixtures only) |
| mk1s.patch | empty, skipped |
| mrental.patch | 3-way: the same kind of conflict (lane mrental block beside m1116 + mk1); all kept. Its 4 new fixture files were first checked by this lane's build (build OK, test-fixtures passed) |
| mstruct.patch | applied cleanly; then changed as the coordinator asked (below) |

### mstruct change: `display` counts as observed

- `unobservedChain`: a line with `display` is observed (`line.display !== undefined` returns false), beside the
  existing refusal-gate / `shown_when` / definition / product-name tests.
- The rule's comment and tools/README.md now say so.
- `unobservedLineSelfTest`: a new planted case, "t.D marked display (shown on the values sheet)", must be rejected.
  Narrow run (`mint-work/pre.mjs`): self-test returns `[]` (0 problems).

## Coordinator item 2a: the k1s col_h / col_i / col_k mutants (STOPPED as instructed)

- Drafted `bug_pending/mint-01.md`, placeholder **BUG-NEW-mint-01**, severity low: "The evaluator accepts a
  hand-listed roster for an implicit collection (Form 7203 under each S corporation K-1); it should be an input
  error". It carries the evidence from mk1s.md. The heading ends in " (open)", the form the check needs once the id is
  assigned.
- **Constraint (engine/src/mutate.ts, in the run's openDefectProblems):** each OPEN_DEFECT_SURVIVORS value `bug` must
  match `^## ${bug} — .*\(open\)$` in BUG_INVENTORY.md, or the run reports "`<id>`: `<bug>` is not an open entry in
  BUG_INVENTORY.md" and fails. A pending entry lives in bug_pending/, not in the inventory, so BUG-NEW-mint-01 cannot
  satisfy it. **Not listed.** After `new_bug.py --assign` (which rewrites placeholders in every tracked file and
  appends the entry with its heading, "(open)" included), add to OPEN_DEFECT_SURVIVORS_ALL:

      "operand.k1s.k1s.col_h.zero.then1": "BUG-NNNN",
      "operand.k1s.k1s.col_i.zero.then1": "BUG-NNNN",
      "operand.k1s.k1s.col_k.zero.then1": "BUG-NNNN",
      "operand.k1s.k1s.p5_income.zero.then1": "BUG-NNNN",
      "operand.person.person.f8919_line10.f8919_line10_figured.then0": "BUG-NNNN",

- Two more mutants were found to be in the same class, and the bug's "Where" was widened to cover them:
  - `operand.k1s.k1s.p5_income.zero.then1`: its `k1s.ok = false` alternative. With `display` counted as observed it
    is no longer the structural rule's: it reaches `person.k1s_total_p5_income`.
  - `operand.person.person.f8919_line10.f8919_line10_figured.then0` (fork C). An argument holding on the implicit
    roster is drafted in `mint-work/C/args.ts`, but it is false on a hand-listed f8919 roster. It is not added, for
    consistency with the coordinator's ruling on mk1s. If the owner prefers, that argument can be used instead.

## Arguments added (block `// ---- lane mint begin/end ----` in EQUIVALENT_IF)

| Mutant | Kind | One line |
| --- | --- | --- |
| operand.rental.rental.home.home_pers10_if_any.all.1.gt.0 | answered-only | personal_c and home_pers10_if_any choose on the same personal_any: true agrees, false makes the first conjunct a known false; only an unanswered personal_any with an answered days_personal differs (mrental.md) |
| operand.rec.rec.to_line1.zero.then1 | answered-only | to_line1's only reader refund.taxable takes it only under the same known rec.path true; with path unknown the mutant's line_c way can refuse (mrental.md) |
| operand.person.person.f4137_line6.zero.then1 | answered-only | filed known false means col_c a known $0, so line 4 = max(0, 0 − col_d) = $0 for a known col_d (fork C) |
| operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0 | answered-only | on a return that is not joint every person entry is the taxpayer's, so cov_you = cov_count. **Judgment call, flagged:** a not-joint roster listing a spouse also tells them apart. It is not a withheld answer, but the model already refuses it at line 1a (household.roster_bad), unlike the mk1s roster, which is accepted silently. Revert if the owner holds the mk1s line for it too (fork B) |
| operand.eic.eic.check_27c.has_qc.any.3.all.1.eq.0 | answered-only | has_qc true: disjunct 2 already gives true; has_qc false: show5 true forces eligible true, which fails the disjunct (fork A) |
| operand.k1s.k1s.p1_loss.zero, p2_loss.zero, p3_loss.zero | every input | max(0, max(B,0) − B) = max(0, −B); a refusal or unknown of B is carried by both routes (same form as mk1's loss1..loss8) |

Each has its premise digest from `premiseDigest` on the built data. Narrow check (`mint-work/pre.mjs`,
single-threaded, mutate.ts's own `sampledShare`): every argument `holds`, its `reads` equals the mutant's replacement,
and none is contradicted. The partial differences are on withheld sets, as expected for answered-only.
rental.home: reached 9, exercised 0 (no set as given exercises it).

## Fixtures added (hand-predicted; ids mint.*)

| Case (file) | Kills | Notes |
| --- | --- | --- |
| mint.eic.step2_other.schedule_e_low_income (eic.json) | refusal.eic.eic.step2_other.1 | line 27a refusal at sche.any (i1040gi p. 40) vs $0 (fork A) |
| mint.f8962.show_applicable.no_1095a (f8962.json) | operand.f8962...show_applicable... | mexist's answered-only reading was wrong: a complete return tells them apart (fork A) |
| mint.f8863.show_after4.mfs_paid_unasked (f8863.json) | operand.f8863...show_after4... | unknown-only kill (paid not asked on MFS) (fork A) |
| mint.person.mw_has_1099.no_1099_business_unasked (pay_not_w2.json) | operand.person...mw_has_1099... | unknown-only kill (mw_business not asked) (fork A) |
| mint.f2441.line_a.mfs_apart_all_year (f2441.json) | household.mfs_apart_last6 mutant | value kill, line 11 $810 (fork B) |
| mint.f8853c.adb_only.nonqualified_not_asked (f8853c.json) | f8853c.has_line17 mutant | unknown-only kill (fork B) |
| mint.household.mfs_community_property.rdp_not_asked (household.json) | household.joint_unmarried mutant | unknown-only kill (fork B) |
| mint.household.mfs_widowed.cp_marriage_not_asked (household.json) | household.cp_marriage_ended mutant | unknown-only kill (fork B) |
| mint.sa.mortgage_limit.over_limit_1098_only (sa.json) | sa.mortgage_interest_not_mfs mutant | class M base classm.tipjob.1 copied (classm.json untouched) (fork C) |
| mint.s1.nol.limit_refused_positive_income (s1.json) | s1.nol_limit_test mutant | value/refusal kill (fork C) |
| f1116.mint_line33_refused_line20_zero_line18 (f1116.json) | operand.f1116.f1116.line35.line33 | **flagged:** the case asserts the model's refusal of line 20/33/35 (Form 8621 tax on line 16, out of scope); the mutant gives $0, which is the legally right line 33. Decide whether this kind of kill is acceptable (fork D) |
| mint.f8919.files.no_firm_wages (f8919.json) | boundary.f8919.f8919.files | asserts f8919[form].line6 $0 and files false on x2pay.f4137.noncash_only's inputs (f8919 p. 1 line 6, Who must file) |

`operand.f4137.f4137.line5_over.line5.gt.0` was already killed by mexist's fixture (fork C).
Diff on fixtures: additions only (`git diff --numstat`: 0 deletions).

## Runs

All on this worktree. Build: `npm run compile` and `main.js build`: build OK (after mrental, and again after the
final changes, which include the 12 new cases).
test-fixtures: us 2528/2528 and ny 358/358 on the final tree. The first pass, after mrental, gave 2516/2516 and 358/358.

| Run | Tree | Result | Exit | Wall |
| --- | --- | --- | --- | --- |
| federal mutate 1 (`mint-work/mutate1.log`, `mutation1.md`) | m1116 + mk1 + mexist + mrental + the 2 rental arguments | 10022 mutants; checker 3770, fixtures 5784; surviving 468 (433 every input, 9 answered-only); 3 open-defect; **23 not yet explained**; every self-test 0 problems; sampled check 135 arguments, 0 problems | 1 | 66m56s (a second mutate, lane mstruct's, ran at the same time) |
| federal mutate 2, final (`mutate2.log`, `mutation2.md`) | all of the above + mstruct (with the display change) + every lane mint argument and fixture | 10022 mutants; checker 3770, fixtures 5796 (84 only class M); surviving 456 (436 every input, 12 answered-only); 3 open-defect (BUG-0764); unobserved-line rule 0 survivors, self-test 0 problems; 0 stale arguments; sampled check 141 arguments on 120 lines, 0 problems; **5 not yet explained** | **1** | 47m29s |
| ny mutate, final (`mutate2ny.log`) | the same | 878 mutants; checker 249, fixtures 577; surviving 52, all explained; unobserved-line 0; every self-test 0 problems; sampled check 45 arguments, 0 problems | **0** | 4m41s |

The 5 left unexplained in the final federal run are exactly the BUG-NEW-mint-01 class: k1s col_h, col_i, col_k,
p5_income .zero.then1, and person.f8919_line10 .f8919_line10_figured.then0. After `new_bug.py --assign`, list them
in OPEN_DEFECT_SURVIVORS_ALL with the assigned id (the lines are above). The federal step should then exit 0. That is
inferred, not run. The open-defect check also requires each listed mutant to still survive, which run 2 shows.

The structural rule, with `display` counted as observed, explains 0 survivors, as the coordinator expected. Of
mstruct.md's 47:
- most were already killed by mk1's fixtures;
- k1s p1_loss, p2_loss and p3_loss are argued on every input;
- p5_income is in the bug class.

Timing (asked by the coordinator): the run prints no per-stage times (MUTATE_SAMPLE_TIMES was not set). In run 2, ps
showed about 8 cores busy until about 39 minutes in, falling to about 4 cores at 42 minutes and 1 core from about 44
minutes to the end at 47.5 minutes. So the serial tail was about 3 to 5 minutes. Most of the wall time was the
parallel phase, on a machine loaded by other lanes (load average 15 to 35). From this output I cannot say whether the
tail scales with the number of keyed arguments.

The patch includes the regenerated reports/2025/mutation.md and reports/ny/2025/mutation.md of the final runs.

## Verified vs inferred

- **Verified:**
  - The patches applied; the conflicts were resolved by keeping every lane block.
  - The build and test-fixtures results.
  - The final federal and ny mutate outputs above, read from the logs.
  - mint.patch is the staged diff against 6649c637 (`git apply --check -R` passes on the worktree).
  - Fixture diffs are additions only.
- **Verified by the forks, not re-done by me:**
  - Each case's hand prediction against the sources, the page cites, and the kill checks before the full run. The full
    run then counted them as killed: these mutants left the not-yet-explained list.
- **Inferred, not verified:**
  - That listing the 5 under the assigned bug gives exit 0.
  - That the coordinator accepts the two flagged judgment calls: the ira answered-only entry, and the f1116 kill by an
    out-of-scope refusal.
  - Fork B's interview-skip claims for household.rdp and household.cp_married rest on the demand chain, not an
    interview walk. The build's fixture path checks passed on the new cases.
