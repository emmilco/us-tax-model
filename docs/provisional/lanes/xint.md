# XINT: the coverage-expansion lanes merged onto B1 final (running log)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/xint`, base
`refs/scratch/b1-final` (0c8cd21d). Lanes are uncommitted trees on `refs/scratch/x1-base` (825024d8). Nothing
committed; `check_all.sh` not run; no paid reviews or model calls. Tools (copies of B1's, pointed at xint, base x1-base,
plus `b1` as a side meaning `refs/scratch/b1-final`): `/tmp/xint/tools/` (`verify_merge.py`, `merge_nway.py`,
`merge_keyed_json.py`, `applylane.sh`, `union.py`, `resolve_dec.py`); checks `/tmp/xint/check.sh TAG`,
`/tmp/xint/quick.sh TAG` (logs `/tmp/xint/check-TAG.log`, `quick-TAG.log`).

Method per lane: `applylane.sh` applies the lane's diff with `git apply --3way`, excluding `sources/`, `tools/sources/`
(taken from nx-src, of which every lane's copy is a subset, checked by `cmp`/`diff`), `fixtures/` (merged by case with
`merge_nway.py`, ours = the xint file, base x1-base; new fixture files copied), `reviews/2025/consumers.json` (by key,
`merge_keyed_json.py`), and the shared lane docs already present (identical, checked by `cmp`). `defaults.json` is never
taken: each lane's defaults script is run on the integrated file. Every structured file is then checked by id against
x1-base, b1-final and every lane merged so far (`verify_merge.py`).

## Log

### nx-src (archived sources)
- `git -C nx-src diff --binary HEAD -- tools/sources sources` applied with `--3way`. One conflict: `sources/2025/manifest.json`
  (B1's 289-292 vs nx-src's additions), merged by document id: 289 + 3 (B1) + 33 (nx-src) = 325, written as
  `fetch_sources.py` writes it (indent 2, ASCII). Catalogs `tools/sources/2025.json` (325) and `2026.json` (118) merged
  cleanly; ids unique in all four files. Pure additions against b1-final.

### x1-f1116: deferred (not merged in the first batch)
- Its second pass (x1-f1116b) is already editing the same worktree: at 15:02 `forms/2025/f1116sb.yaml`, `f1116sbyr.yaml`,
  `scope.yaml`, `s3.yaml`, `ftc.yaml`, the bank, params, fixtures and catalogs had changed since the first-pass note
  (12:41), and no snapshot of the first pass exists (no ref, no stash, no saved diff). A diff taken now would be a
  half-done second pass. The lane is merged whole once x1-f1116b reports.

### x1-digital
- Text: one conflict, `docs/provisional/DECISIONS.md` (B1 rewrote section 5; the lane's side still had the x1-base
  section 5 table): kept B1's section 5, appended the lane's section. Everything else (`s1.yaml`, `sales.yaml`,
  `sd.yaml`, `f1040.yaml`, `f8960.yaml`, the bank, `coverage/other.yaml`, `tree.json`, personas 17/18, changes/2026)
  applied cleanly.
- Fixtures by case (12 files, incl. the class M and mutation files B1 also changed): no conflict.
- defaults: `/tmp/x1d/defaults_patch.py` (adds `f1040.digital_assets`, `s1.digital_amount`, one consistency rule;
  checked against the lane's own additions over nx-b1's copy: identical).
- `research/ty2026/changes.md` (lane request): the i8960 "Digital assets" row now names C-X1-F8960-01.

### x2-k1p
- Text: DECISIONS.md conflict as above (same resolution). `k1p.yaml`, person block, bank, tree topic applied cleanly.
- `fixtures/2025/k1p.json` new. consumers.json by key (+28). defaults: the lane script (72 entries).

### x2-k1s
- Text conflicts, all both-sides additions, resolved as k1p then k1s: `ambiguities/2025.yaml`, `forms/2025/person.yaml`
  (the two delimited blocks after `# --- end Stage 21 ---`), `interview/2025/questions.yaml` (frames; groups), and
  DECISIONS.md. `x2-brief.md` not taken (the k1p copy is in; each lane's brief differs, and is quoted in its note).
- **(order, seq) collision:** k1p uses order 264 seq 1-96, k1s seq 20-83 (50 collisions). k1s/f7203 entries moved to
  seq 120-183 (+100: same relative order, after k1p's). No other collision in the bank.
- `tree.json`: one K-1 topic: `k1_partnership` renamed `k1` ("Partnership and S corporation Schedules K-1"); k1p's 28
  and k1s/f7203's 23 gates placed in it (k1s had them under `other_income`).
- `fixtures/2025/k1s.json` new. consumers.json by key (+25). defaults: lane script (63).

### mfs-l4
- Text: ambiguities, DECISIONS conflicts (additions; resolved as above). Bank renumbering of order 120 applied cleanly.
- `fixtures/2025/dependent.json` by case; consumers.json (+2); defaults script (3).

### Checks after the first batch (nx-src, x1-digital, x2-k1p, x2-k1s, mfs-l4)
- By id (`verify_merge.py`, sides b1 + the four lanes): every fixture file the lanes changed: 0 problems;
  consumers.json (851 keys): 0; questions.yaml (1004 entries): 63 differences, all the deliberate k1s/f7203 `seq` move.
- Class M / mutation inputs: four mutation cases B1 added after x1-base (`mutation.t2.sli.mfs_divisor`,
  `mutation.t2.scveh.mq_q2_suv_179`, `mutation.m2.f1095a.same_months_b_doubt`, `mutation.t3.roster_ok_role_unanswered`)
  answer `s1.digital_income` without `f1040.digital_assets`: `"f1040.digital_assets": false` added (input only, as the
  lane did for its 244).
- Check r1 (`/tmp/xint/check-r1.log`, quick `/tmp/xint/quick-r1.log`), tree = nx-src + x1-digital + x2-k1p + x2-k1s +
  mfs-l4: compile rc 0; build OK (3332 s, machine load about 220); render, render --ny OK; **test-fixtures 2112/2112;
  --ny 357/357**; year_changes --check rc 0; citations --strict 0 findings, 0 unused rulings; tick-groups,
  check_questions, check_screens, check_false_no, check_twins rc 0.
  - check_consumers rc 1: exactly x1-digital's known findings (new `consumer:s1.digital_income@i1040gi:p15`, `@p16`;
    stale `@p91`, `@p92`), which the lane left to round-2 review (ruling is review work). Nothing else.
  - siblings --check, check_bug_inventory rc 1: B1's entries only (BUG-0649..0757 sibling-review fields; the goal-1 placeholders
    placeholders cited in b1-integration.md and lane notes, already numbered); none of these lanes'.
  - `tree.py --check`: only B1's six unplaced gates (household.hoh_missed, refund.two_itemized_if_two, s2.amt_pab_over,
    s3.business_credit_any, s3.business_fuel_any, sd.f2439_if_dividends); every lane gate placed.

### x1-sche
- Text conflicts, all additions: ambiguities, the bank (frames, groups, entries at the end), DECISIONS.md. s1.yaml
  (line 5, line 10, EBL lines) merged cleanly with x1-digital's line 9; scope, f8960, eic, tables, extractor,
  check_all_steps.sh, tools/README.md cleanly.
- Fixtures eic/returns/scope by case; rental.json new. consumers.json (+19, -8 stale `scope.rental` rulings: 870 keys,
  0 problems by id). defaults: `/tmp/x1sche/defaults_patch.py`.
- `categories.json` (lane request): `rental_royalty` gates `[]`, label "supported since lane x1-sche; its remaining
  refusals are unmeasured gates" (the form other supported categories use).

### x2-k1e (coordinator: merge with k1p/k1s; rows and personas stay parked)
- Text conflicts, additions: ambiguities, bank (groups; entries at order 266, no collision), DECISIONS.md, tree.json.
  Its 8 gates moved from `other_income` to the `k1` topic (59 gates: k1p 28, k1s/f7203 23, k1e 8).
- person.yaml k1e block (with `display`) applied cleanly; `x2-k1e_work/` taken (parked rows and personas, not in
  `interview/2025/`). `fixtures/2025/k1e.json` new; defaults script (36). Its sources/catalogs: subsets of nx-src (by id).
- By id after both: eic, returns, scope, rental, k1e, mutation fixtures 0 problems (mutation: only the 4 inputs above).
- Check r2 (`/tmp/xint/check-r2.log`; tree adds x1-sche, x2-k1e): build OK (1142 s), render both, **test-fixtures
  2158/2158, --ny 357/357**, year_changes rc 0, citations --strict 0 findings. check_consumers rc 1: x1-digital's four
  (above) plus seven new `k1e.*` gate pairs (`k1e.interest_any`, `dividends_any`, `gains_any`, `other_any`,
  `business_any` @i1041sk1:p2, `codes_any`@p4, `box12_any`@f1041sk1:p2) that x2-k1e did not rule. Bank by id: 1103
  entries, only the 63 k1s seq moves.

### mfs-l1 (first of the MFS lanes)
- Text: DECISIONS.md only. Fixtures by case (eic, f1040, household, qdcg, scope, ny it201); `s3.json` `ss.mfs`
  conflicted (B1 set `div.any` false and dropped `s2.amt_owed`; L1 dropped every null input): L1's case plus
  `div.any: false`. consumers.json: five `eic.us_home` rulings written by both B1 and L1 (both "same"): B1's kept (they
  quote the question as F9 reworded it). defaults script.
- Persona `14_mfs_separate_finances` renumbered `15_mfs_separate_finances` (14 is x1-f1116's).

### mfs-l2
- Text: ambiguities, DECISIONS (additions). Fixtures by case (classm x3, ira, mutation, sa, sli); consumers (two stale
  `sli.any` rulings removed); defaults script; `ripple_mortgage.py` (35 cases: its 33 plus 2 B1 added).

### mfs-l3
- L1 stubs dropped: `params/2025.yaml` and `forms/2025/household.yaml` taken as before the lane (its only changes there
  were the stubs; checked by its diff), its bank entry `household.mfs_living` 102/9 removed. f2441/f8863/f8889/f8962
  and the bank applied cleanly. Fixtures by case; consumers: four f2441/f8863 rulings written by both B1 and L3 ("same"
  both): B1's kept. defaults script (its `household.mfs_living` stub not added: L1's is present).

### L5 (inputs only; `/tmp/xint/tools/l5_restate.py`, idempotent; list `/tmp/xint/l5-changes.txt`)
- 249 cases: `ssb.lived_apart` dropped (derived now; true on MFS -> `household.mfs_living: apart_all_year`); every MFS
  case states `household.married_dec31: true` (39 stated false, now refused at `household.filing_status_conflict`; the
  rest absent); MFS `eic.same_home` dropped, restated as `household.mfs_living` (false -> apart_last6, true ->
  together_late). Rerun after the later lanes: 0 further changes.

### x2-dep
- sa.yaml (with L2), eic.yaml, f8962.yaml (with L3), the bank applied cleanly. Fixtures by case; consumers (+7).
- `dependent.json` `stage8.single.filer_is_dependent`: the 13 values restated exactly as the lane note lists
  (coordinator decision), evidence note extended.
- `tools/check_qdcg_ceiling.py` wired: step `check_qdcg_ceiling` after `check_realty_tables` in check_all_steps.sh (the
  tool has no `--check` flag: it checks by default), `--self-test` in tools/self_tests.py (code group, year-aware),
  README row. Both run: rc 0, self-test 6/6.
- categories.json `dependent_filer`: gates [], `refused: false`. Persona `14_dependent_student` -> `20_dependent_student`.

### x2-s1o (its base carried x1-digital's in-progress work)
- Files x1-digital also changed were merged with x1-digital's copy as the base (`git merge-file`; fixtures by case or
  by input key): s1.yaml, f1040.yaml, the bank, other.yaml, persona 18 cleanly; ambiguities, DECISIONS by union. Every
  other x1-digital file in its tree was byte-identical to x1-digital's (checked), so nothing of x1-digital was
  reverted. `classm.s1.1`-`13`: only `scope.nol: false` added (B1's input fixes kept). Sources not taken.
- `s1.line9` now sums 8a, 8b, 8c, 8e-8k, 8r, 8u, 8v, 8z (type Dollars); 8s waits for x2-paynow2.
- Dropped `mutation.m3.scope.s1_recovery`, `mutation.m3.scope.s1_nol`. defaults script (without `--with-digital`).

### x1-f1116 (both passes, whole)
- Text: ambiguities, research/ty2026/changes.md, DECISIONS (additions). Fixtures by case except mutation.json, where
  the lane's only change is deleting `ftc.elect` (checked case by case): `ftc.elect` deleted from every fixture case in
  the tree (236 in mutation.json: its 234 + B1's, less the two m3 cases dropped), ny mutation by case. defaults script.
- Coordinator fix: `s3.other_credit_9` (the chain link that refused on `ftc.carryover_no_tax`) removed, `_8` now goes to
  `_10`; row `credits.gap.foreign_tax_carryover_form` expects `refused: ftc.carryover_no_tax` (told at `ftc.credit`).
- Schedule E caution (x1-f1116 note, x1-sche now in): new gate `f1116.rental` (`sche.any`), refusal on `f1116.line35`
  after `f1116.business` (i1116 p. 17 gross income), placed in tree.json. No fixture pins it yet (left open).

### Check r3 (all lanes but x2-paynow2; `/tmp/xint/check-r3.log`, rerun logs `/tmp/xint/tf-r3b.log`, `tfny-r3b.log`)
- First build failed: `s3.mfs` unread once L1 and L3 removed its last refusals: deleted (coordinator allowed it).
- Build OK (866 s), render both. test-fixtures first 2273/2283, --ny 356/358, all MFS input gaps of the no-defaults
  files; fixed input-only (second rule set of `l5_restate.py`: `household.mfs_living: together_late` on 96 MFS class
  M/mutation cases, `f8962.mfs_exception: false` on MFS cases with a Form 1095-A; L1's own `mfs.household.not_married`
  and `spouse_died` restored as L1 wrote them). Then 2281/2283, --ny 358/358; the two left:
  - `mutation.t2.f1095a.monthly_columns`: inputs `f8962.mfs_exception: true`, `mfs_three_years: false` (the abuse
    exception keeps its monthly columns; all 11 values checked by eval). Coordinator accepted.
  - `mutation.t2.sli.mfs_divisor`: `sli.line8` $2,500 -> $0 (coordinator decision (a), approved end change under D2; the
    MFS branch of the line 7 divisor is now unreachable: for the follow-up mutation lane).
  - `redesign.credits.refuse.ftc_carryover` and `_prior_return`: `s3.other_credit` true -> false (consequence of the
    coordinator's chain fix; accepted).
- year_changes rc 0; citations --strict 0 findings. check_consumers: x2-s1o's 18 rulings written
  (`/tmp/xint/tools/s1o_rulings.py`), 35 stale entries removed (34 pairs), and the 12 pairs no lane ruled read and ruled
  "same" on the coordinator's instruction (`/tmp/xint/tools/rule12.py`): 0 new, 0 stale.
- check_questions: one orphan, `ssb.lived_apart` in `reviews/2025/questions/ssb.json` (the input is derived now): removed.
- Review records: x1-f1116's diff (taken 16:50) carried xrev-new's review files (reviews/2025/render|transcription
  f1116*, reviews/store/*): removed from xint; they come by `worktree_data.py carry-back` when xrev-new finishes.
  Every later diff excludes `reviews/` (except the lanes' consumers.json and questions/ftc.json edits).
- quick r3: tick-groups, check_screens, check_false_no, check_twins rc 0; siblings, bug inventory: B1's entries only.
- interview-coverage (r3 canonical; sales, other, dependents, rental, scope, mfs, opening, mfs_deductions, mfs_credits,
  dependent_filers, s1_other, ftc1116, credits, home: 327 rows): 14 problems: `opening.widowed_this_year_alone` (known
  base, ignored per coordinator); `other.digital_income_niit` refused at B1's `person.over` because the row's W-2 box 4
  was 6.2% of wages above the 2025 wage base: box 3 $176,100 and box 4 $10,918.20 stated (the row's scenario kept);
  `other.professional_gambler` answered `s1.ltc_payout`/`s1.inmate_wages`, ticks x2-s1o removed: dropped.
- Tree saved as a tree object (not a commit) before x2-paynow2: `076d2bf8` (`/tmp/xint/r3.tree`).

### x2-paynow2 (r4, its own step)
- reviews/ excluded (xrev-new's records). Text conflicts: ambiguities, DECISIONS (additions); params (x2-s1o's line 8z
  kinds locator kept, paynow2's enum `contractor_reason` added); s1.yaml: the x2-s1o NOL block and paynow2's 8s lines
  both kept (both share the `subtract from s1.zero` shape); `s1.line9` = 8a, 8b, 8c, 8e-8k, 8r, 8u, 8v, 8s (negative),
  8z, its cite no longer names 8s as refused.
- Fixtures by case (classm x2, eic, mutation, s1a); new f4137, f8919, pay_not_w2. defaults script (22).
- tree.json `scope.other_income` question no longer names wages not on a W-2 or Medicaid waiver payments.
  categories.json: neither `scope.pay_no_w2` nor `scope.medicaid_waiver` is named there; nothing to drop.
- r4 first build OK (680 s); test-fixtures 2298/2308, --ny 358/358. The 10 failures (classm.s2.2, s2.3, se.1-3,
  f1040.1/3/5/6/7) were unknowns on W-2 box 3: Form 8919 and Form 4137 are implicit collections (one per person), so
  their lines read box 3 (line 6) on every return, and class M cases state no box 3. Fixed at the cause, not by inputs:
  `person.f8919_line10`, `f8919_tax` (on new `person.f8919_any`, line 6 > 0) and `person.f4137_line6`, `_line10`,
  `_tax` (on `person.f4137_filed`) now choose the figured value (`*_figured`) only when the form is filed, zero
  otherwise. citations --strict 0 findings.
- r4b (after the gating fix): build OK (376 s); test-fixtures 2305/2308, --ny 358/358. The three left
  (`classm.se.1`-`3`) named the Schedule SE def instance by its old binding (`line2`, `line8a`); x2-paynow2 binds
  `line8b`, `line8c` too, so the instance key changed: 45 expectation keys renamed, values unchanged (checked by eval).
  Then **test-fixtures 2308/2308, --ny 358/358**.
- consumers after x2-paynow2: 12 stale (`scope.pay_no_w2`, `scope.medicaid_waiver` pairs) removed; 5 new pairs read and
  ruled "same" (`person.rrta`@f4137:p1, @f8919:p1; `scope.medicaid_waiver`@i1040gi:p92; `scope.pay_no_w2`@f8919:p1,
  @i1040gi:p25): 0 new, 0 stale.
- xrev-new's outputs that rode in on x2-paynow2's diff (taken after 17:10) removed: class M cases `classm.f8919.1`,
  `.2`, `classm.f4137.1`, `.2` and `bug_pending/xrevpay-01.md` (they come with xrev-new's carry-back). No such file from
  any other lane (checked: classm ids of the new forms, bug_pending).
- r4b runs started 18:10 (interview-coverage on 16 row files, interview-rules, mutate, quick): quick r4 rc 0 for
  tick-groups, check_questions, check_screens, check_false_no, check_twins; interview-rules 11 problems (below);
  coverage and mutate stopped at 18:47 (37 min in) when the tree changed (coordinator's 18:45 steps): rerun on the final tree.
  interview-rules (r4b): minimal returns `f1040.status = mfj alone`, `hoh alone`, `scope.nol = true alone` end refused
  (full; mfj/hoh also ny); completion `generated.260` reported complete while `person.work_ssn` reachable; reach
  `scveh.suv` before `s179_elect`; baseline entries no longer needed (`dependent.disabled`, `eic.legally_separated`,
  `eic.same_home`); pruning report stale. Not yet traced.

### Coordinator's 18:45 steps
- **x2-k1e dropped** (class M cannot build a k1e log before the K-1 wiring): `forms/2025/k1e.yaml`,
  `fixtures/2025/k1e.json`, `changes/2026/k1e.yaml` removed; 18 `person.k1e_*` lines, 36 bank entries (order 266), 3
  groups and the frame, 2 ambiguity entries, 36 defaults, 8 tree.json gates, 7 consumer rulings, DECISIONS section 6
  removed. Its lane note and `x2-k1e_work/` stay as documents (parked; the wiring lane takes them).
- **xfix deltas** (forms/, interview/, fixtures/, tree.json, bug_pending/, docs/ only): each lane's tree as merged was
  rebuilt from x1-base + its saved diff (`/tmp/xint/tools/xfix_delta.sh`) and every changed file merged 3-way
  (`git merge-file`): x1-sche rental/royalty/rprop, coverage rental/scope, persona 19, bank (rental.part_home, the
  130 renumbering), tree.json; x2-k1p k1p, person, bank, its docs; x2-k1s k1s, bank (two conflicts: the k1s `seq`
  values I had moved by 100 against xfix's help changes: xint's seq kept, xfix's help taken), its note. Bank: no
  (order, seq) collision. Fixtures: new class M cases (x1-sche 11, x2-k1p 10, x2-k1s 11, x1-f1116 9, x2-s1o's rec/
  f8853c 8, and x2-paynow2's f8919/f4137 4, restored now that their review data comes in), rental.json (3 new xfix
  cases, 4 restated), k1p.json (1 new), f1116.json (covers only, 34 cases; nothing else differed). Default
  `rental.part_home` added. bug_pending: xfix-01 (x1-sche), x2-k1p's xfix-01 renamed **xfix-02** (and its mention in
  x2-k1p.md), and xrev-new's entries (xrev-01, xrevftc-01, xrevk1s-01/02, xrevpay-01, xrevs1o-01/02,
  xrevsche-01..05). (A copy loop briefly brought back the x1-base `g1-*` pending files: removed; B1 numbered them.)
- **Review data**: `worktree_data.py carry-back` (dry run, then real) from x1-sche, x2-k1p, x2-k1s, x1-f1116, x2-s1o,
  x2-paynow2: ledgers appended (33, 24, 17, 17, 12, 12 rows), 121/64/63/70/45/51 files. From x2-k1p on, two derived
  files had changed on both sides after x1-sche's carry: `.classm/jobs.json` (rebuilt by classm-jobs) and
  `.transcription/rerun_summary.json`: taken from the worktree with `--prefer-worktree`, jobs.json to be rebuilt.
  Tracked review files of the new forms (index, rulings, adjudication) and the reviews/store records they reference:
  171 files (`/tmp/xint/tools/take_reviews.py`).
- r5 build failed one fixture lint: `household.married_dec31: its withholding condition holds in no case that takes
  the default` (the withheld default on mfj/mfs): the only defaults-taking MFJ/MFS case without the input was x2-k1e's
  `k1e.two_entries_and_spouse`. The input dropped from `f1040.json` `stage13.refuse.joint_without_spouse` (a roster
  refusal on line 1a that does not read the marriage; passes). A first try on `f1116.c10_two_columns` failed (it reads
  it) and was reverted.
- The 49 class M cases taken from the x1-base-era lanes lacked `f1040.digital_assets` (x1-digital's question to
  everyone): `false` added to 45 (inputs only; none states `s1.digital_income` true).
- `classm.f7203.3` (coordinator: I rule it): its 7 disagreeing lines (c35, c47, e35, e47, line11, line14, line15) were
  already ruled ambiguity (`amb.2025.f7203_prorata_places`) in the carried-back log, without a drop, so the fixture kept
  the model's exact-division values and failed by a cent. `rule.py` writes only open sections and `--amend` refuses a
  drop change, so the drop was applied as `rule.py` applies it: the 7 expectations removed from the case (evidence note
  "dropped after ruling: ..."), `drop: true` in `reviews/2025/classm/f7203.rulings.json`, " [dropped]" on the 7 log rulings.
- r6: build OK (426 s), test-fixtures 2342/2342, --ny 358/358, year_changes rc 0.

### interview-rules (r4b's 11 problems), traced
- `minimal: f1040.status = mfj | hoh alone ends refused` (full, ny): `f1040.status` became an existence gate because
  mfs-l4's `dependent.other_only_spouse_if_mfs` chose on `f1040.status` directly (five alternatives), so the check
  opened each status alone with the taxpayer alone (MFJ without a spouse refuses at the roster, HOH without a
  qualifying person at `hoh_fails`). Fixed at the cause: the gate chooses on `household.mfs` (L1's line), same values.
- `minimal: scope.nol = true alone ends refused` at `s1.nol_limit` (x2-s1o): with a zero carryover and taxable income
  below zero, `nol_ti4` (negative) < 0 made the 80%-limit test true. Fixed: the test also requires a carryover above
  zero (a zero carryover has no limit to apply). No fixture value moves (r7 checks).
- Baseline entries the run said to remove: `dependent.disabled` (early_completion), `eic.legally_separated`,
  `eic.same_home` (order_dependent_reach): removed.
- New, held in `tools/interview_rules_baseline.json` with the cause as far as traced: `person.work_ssn` early
  completion (generated.260) and `scveh.suv` reached before `s179_elect` (generated.253). No lane changed any line that
  reads either (diff of every lane's forms); inferred, not probed: mfs-l1's lift of `s3.mfs` makes generated MFS returns
  complete that used to refuse (mfs-l1's note section 7 names the Schedule 1-A questions asked on MFS).
- Pruning report: regenerate with `interview-rules --write-pruning` on the final tree.
- r7: build OK (347 s), test-fixtures 2342/2342, --ny 358/358, year_changes rc 0, citations --strict rc 0.
  check_logs on the new forms: f7203's 7 dropped rulings differed log/sidecar (the log is a view of the review store;
  the edited view was ingested with `rulings.write_log`, as rule.py does): 0 differences after. Also the retirement
  row `retirement.dis_early` answers the saver's-credit chain (sav_claimed, sav_able, sav_voluntary, sav_prior_other,
  retirement sav_military / sav_404k / sav_inherited), as the coordinator asked; the coverage walk confirms.

### Rebase onto B1's current tree (coordinator 19:22)
- nx-b1's working tree taken with a copy of its index (`git add -A`, `write-tree` on the copy: d4526bac; nx-b1's own
  index untouched). Delta = d4526bac minus 0c8cd21d (xint's base), 316 files outside rendered/canonical/reports.
  xint before the rebase saved as tree 9880db05 (`/tmp/xint/r7.tree`).
- Applied with `git apply --3way` except fixtures: one conflict, `tools/interview_rules_baseline.json` (B1 rewrote the
  reasons of entries xint had removed as no longer seen): xint's removals and additions kept, B1's new reason for
  `ny_it201.ask.moved_out` taken. forms s1/f1040, the bank, tree.json, engine, check_all_steps, review files: clean.
- Fixtures by case (`case_patch.py`, base 0c8cd21d, theirs B1): household 2, s2 12, s3 3, scveh 1 applied; classm.json:
  84 cases B1's class M reruns rewrote that xint had changed by input: merged field by field (`field_merge.py`: B1's
  expectations, both sides' input keys); two input conflicts (`classm.f8962.1`, `classm.f1095a.2`: B1 restated them as
  single, married_dec31 false): B1's taken, and the MFS-only inputs xint had added dropped. L5 rerun: B1's two new MFS
  cases in s2.json state married_dec31 true.
- Review data: `worktree_data.py carry-back` from nx-b1 (dry run, then real): 156 ledger rows, 728 files;
  `.classm/jobs.json`, `.transcription/rerun_summary.json` and a person preview prompt changed on both sides: nx-b1's
  kept. `worktree_data.py check`: OK.
- r8 (rebased): build OK (357 s); test-fixtures 2361/2369 first: B1's re-run class M cases still stated the retired
  `ftc.elect` (5) and lacked `f1040.digital_assets` (new ones): `ftc.elect` deleted, `f1040.digital_assets: false`
  stated on class M cases lacking it (19); then **2369/2369, --ny 358/358**. year_changes rc 0; citations --strict 0
  findings; check_consumers: one stale (`f1040.status@i1040gi:p17`, mfs-l4's, no longer read since the gate fix):
  removed, 0 new 0 stale. tick-groups, check_questions, check_screens, check_false_no, check_twins rc 0.
  siblings --check rc 1: BUG-0610 and BUG-0619 (committed entries) name `s3.mfs` and `s3.other_credit_9`, both removed
  in this merge; the xfix/xrev pending entries lack Fix lines / sibling lists (their lanes'). check_bug_inventory rc 1
  only on "BUG_INVENTORY.md committed content modified": B1's own edits against xint's base commit; clears when xint
  is re-parented on the B1 commit. Two placeholders cited in lane notes mapped (g1-f9-02 -> BUG-0729, g1-t2-01 ->
  BUG-0752). new_bug.py --assign deferred until the re-parent (B1 may number more entries).

### check_logs on the candidate (r8)
- New forms: every one has current transcription, render and class M logs except: `f1116` (line 35: the
  `f1116.rental` refusal this merge added: transcription and render line-scoped, class M rerun); `f8919` render lines
  8 and 9 (they read `person.f4137_line10`, now gated by this merge's Form 4137/8919 fix); `qdcg_amount` (x2-dep's
  new def, unread until Form 8615) has no log of any kind.
- Shared forms stale (transcription / render / class M): dependent T R M; eic T R M; f1040 T R M; f2441 T R(whole) M;
  f8863 T R(whole) M; f8889 T R(whole) M; f8959 T R M; f8960 T R M; f8962 T R(whole) M; ftc T(whole) R(whole);
  household T R; ira T R M; oi8z T R(whole) M; person T R M; refund T R(whole) M; retirement T M; s1 T R M; s1a T
  R(whole) M; s2 T R M; s3 T R M; s8812 T R M; sa T R M; sales T R M; scope T R; sd T R M; se T(whole) R(whole) M; sli T
  R M; ssb T R M; tipjob T R. (T transcription, R render, M class M; "whole" where the tool asks for a whole rerun.)

## Round-2 review list (from the lanes' notes, as merged; NEW = brand-new form)
- NEW, whole transcription + render + class M (most already run by xrev-new and carried in; current except as noted):
  rental, rprop, rf4562, royalty, sche, f8582 (x1-sche); k1p (x2-k1p); k1s, f7203 (x2-k1s); f1116, f1116col, f1116sb,
  f1116sbyr (x1-f1116; f1116 line 35 stale); rec, f8853c (x2-s1o); f8919, f8919firm, f4137, f4137row (x2-paynow2;
  f8919 render 8, 9 stale); qdcg_amount def (x2-dep; none run: transcription and class M once Form 8615 reads it).
  Completeness: f1116, f1116sb, f8582, sche, rec, f8853c.
- Shared forms, line-scoped (`--lines auto`) per the stale list above; class M where arithmetic changed: s1 (8a, 8e,
  8k, 8s, 8u, 8v, 9, 5, 10, EBL, NOL block, 20 box), f1040 (digital question, 1b-1h, 1z, 6d, 7a, 12b, 15), f8960
  (4a, 4c, 7, digital_nii), sales, sd (A/G..F/L, sd.filed), eic (step2_other, step4, step5, MFS home), ftc (whole:
  ftc.elect derived, credit, carryover_no_tax), s3 (other_credit chain, line 11), scope (schedule1, other_income,
  ready_credits, rent_personal, pay gates), household (MFS lines, conflict), ssb (lived_apart derived), sa (dependent
  worksheet, MFS spouse itemizes, mortgage MFS), sli, ira, person (k1p/k1s totals, f4137/f8919 lines, MFS IRA,
  dc_earned), dependent (MFS tiebreak), f2441, f8863, f8889, f8962 (MFS lanes; dependent_filer), s2 (5-7, 21),
  f8959 (2, 3), se (8b, 8c), s8812, retirement, tipjob, s1a, oi8z, refund (rec path).
- Question reviews: x1-digital 10 (f1040.digital_assets, s1.digital_income, s1.digital_amount, $sales, sales.box,
  .special, .proceeds, .reported_basis, .correct_basis, .code); x1-f1116 10 + 7 (pass 2) + ftc.carryover; x2-k1p 72;
  x2-k1s 63; x1-sche 66 (+ rental.part_home); mfs-l1 household.mfs_living, household.community_property; mfs-l2 4;
  mfs-l3 5; mfs-l4 5; x2-dep sa.dependent; x2-s1o 36 + 8 changed helps; x2-paynow2 21.
- Screen / false-no samples (per release): each lane's new gates (listed in each note's section 9), plus
  `f1116.rental` (this merge) and `dependent.other_only_spouse_if_mfs` (now on household.mfs).
- Consumers: all pairs ruled (x2-s1o's 18 on the coordinator's instruction; 17 more read and ruled at integration,
  listed above).

### Final checks on the candidate (r8)
- interview-rules --write-pruning: **0 problems** (293 walks; 83 minimal returns with one existence gate opened, down
  from 91 now that the status is not an existence gate); reports/2025/interview_pruning.md rewritten.
- interview-coverage on the 16 row files the lanes touched (383 rows): first 13 problems, all row answers, fixed in
  the rows only: seven retirement rows answer `retirement[r].disability: false` (x2-paynow2 now asks it of every plan
  distribution); `retirement.dis_early` keeps `sav_able`, `sav_voluntary` (five saver's answers it never reaches
  dropped); `other.digital_income_niit` answers `f8960.unsupported`, `f8960.refund` false and no longer states box 3.
  Then **0 problems**. Full run (every row file): see below.
- Not run, on the coordinator's instruction: mutate, mutate --ny (the full check runs them). Expected survivors to
  explain are listed in the lane notes (x1-f1116 sections 8 and 12.7, x1-sche section 7, mfs-l4 section 7, x2-k1p
  section 11), plus the MFS branch of the student loan interest divisor (unreachable since mfs-l2) and the zero-NOL
  arm of `s1.nol_limit_test`.
- Full interview-coverage (27 files, 637 rows): 0 problems on the rows; reports/2025/interview_coverage.md regenerated
  with `--write`.
- Candidate staged in xint's index (not committed); its tree object is in `/tmp/xint/r8final.tree`.

## Left open
1. Re-parent onto the B1 commit with b1-w1's delta when it lands; then `new_bug.py --assign` (pending: mfs-l1-01,
   xfix-01, xfix-02, xrev-01, xrevftc-01, xrevk1s-01/02, xrevpay-01, xrevs1o-01/02, xrevsche-01..05) and
   `bug_status --write`; siblings: BUG-0610/0619 name lines this merge removed (append-only entries: for the owner).
2. Stale logs listed above (sampled reviews start on this candidate).
3. `f1116.rental` has no fixture pinning it; mutate will show it (Schedule E filer on the Form 1116 path).
4. x2-k1e: lands with the K-1 wiring (its forms and data are in its worktree and `x2-k1e_work/`).
5. person.work_ssn / scveh.suv baseline entries: probe the MFS-lift inference.

### Owner decision 20:05 (BUG-0610/0619) and follow-ups
- `tools/siblings.py --check`: a Siblings-checked id that names no line now is split by `unknown_siblings`: for a
  committed entry, an id some revision of forms/ or defs/ declared (`ever_declared`, `git log -S "id: <id>"`) is reported
  as "removed since the fix" and does not fail (a deleted line cannot regress); any other unknown id, and every unknown
  id of a pending entry, still fails. Self-test: two planted cases (removed vs typo; pending). The self-test's two
  sa.dependent reach assertions named lines x2-dep changed (`eic.step4`, `sa.standard`): now `eic.step4_dependent`,
  `sa.standard_amount`. BUG-0610 (`s3.mfs`) and BUG-0619 (`s3.other_credit_9`) now print as removed, not failed.
- Pending entries taken from the lanes: proposals relabelled "Proposed fix:" (xfix-01, xrevftc-01, xrevpay-01,
  xrevs1o-01, xrevs1o-02, xrevsche-05); made fixes keep Fix lines and their Siblings checked now also lists the siblings
  the tool generates (xrevsche-01: 19, and `rental.div*` written out; -03: 4; -04: 3); xrevsche-02 names the Schedule C
  vehicle and asset screens in words (they are forms, not lines). `siblings --check` now fails only on the release
  reviewers' in-flight pending xrel* entries (27 findings; not this lane's).
- Fixture `f1116.rental` (fixtures/2025/f1116.json, after `f1116.business`), predicted before the run: that case's
  return with x1sche.f1.profit's rental instead of the Schedule C; refused at `f1116.rental` on ftc.credit. Passes;
  test-fixtures 2370/2370.

### Coordinator 20:55
- **classm-jobs failing on 11 forms** (eic, f1040, f8889, person, s1, s2, s3, s8812, sa, sli, ssb): reproduced in a
  scratch worktree of xint's tree (/tmp/xint-cmj, `worktree_data.py clone`, xint's canonical copied): V8 out of heap
  ("Ineffective mark-compacts near heap limit") at classm.py's `--max-old-space-size=8192`. classm-jobs keeps every
  corpus return's full evaluation (2,000 sampled returns plus the fixtures that cover the document); B1's tree already
  peaked at 8.03 GB for sli, and the merged forms (5,908 lines against 5,118) take the large documents over. With a
  16 GB heap s1 builds 17 jobs in 110 s, peak 10.2 GB. Not a fixture or corpus defect (seeds per document barely
  moved). Fix: `tools/transcription/classm.py` heap as `JOBS_HEAP_MB = 16384`, with its reason; the coordinator's
  jobs-lock edit kept. About 10 GB per build on 64 GB: at most 3 or 4 large class M builds at once.
- **x2-dep's unread def dropped** (lands with Form 8615): `forms/2025/qdcg_amount.yaml`,
  `tables/2025/qdcg_zero_ceiling.yaml`, `qdcg_fifteen_ceiling.yaml`, `tools/check_qdcg_ceiling.py` and its
  check_all_steps.sh step, self_tests.py entry and README row; its review indexes
  `reviews/2025/{transcription,render}/qdcg_amount.index.json`, the two store records only they referenced, and the
  generated log views. No tree, consumer or ambiguity entry named it. Release-review files that mention it in passing
  (completeness and screen adjudications of the `inv` family) left as written. x2-dep's batch D (the dependent
  standard deduction) stays.
- Checked in the scratch worktree after the drop (xint left to xadj's own builds): build OK, test-fixtures
  2376/2376 (xrel's and xadj's cases included), check_consumers 0 new, 0 stale after removing
  `status@i1040gi:p38` (the def's pair), check_logs names no qdcg_amount log.
- `tree.py --check` (not rerun since r1) failed on 15 gates the later lanes did not place and one stop: placed now in
  tools/coverage/tree.json: x2-s1o's `rec.*` (5, state_refund), `s1.nol_*` (4), `f8853c.*` (4), `oi8z.injury_if_damages`
  (other_income), mfs-l3's `f2441.mfs_spouse_deemed_if_married` (dependent_care); `refund.exc_tax` (refusing under two
  form names now that rec.yaml also lists it) given a `stop`. docs/COVERAGE.md and the README table regenerated
  (`tree.py`, 353 gates): `tree.py --check` passes.
- xrel: `bug_pending/xrelret-08.md` marked "Duplicate of: BUG-0871" (the same retirement.ira_basis
  false-no defect), before assign as the coordinator asked.
- rendered/ in xint is stale until the next render (the def's pages): xadj's class M runs are rebuilding canonical in
  xint now, so render after they finish (`node engine/dist/main.js render`).
