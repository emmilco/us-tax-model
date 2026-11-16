# Post-release runbook: fix round F (F1 + F2 + F3), then the K-1 stack

Lane POST. Model claude-fable-5-2, class judgment (planning, text only), year 2025, jurisdiction us and ny.
Written 2026-11-16 about 12:15, while the release commit was in its release-mode check. Nothing was built or run.

`P` = `.claude/nightplan-2026-11-16`. `R` = the release commit (expansion + mutation-survivor work + tooling +
sources + records), tagged r2026.11.16.1 once its check is green.

Marks: **[log]** from the coordinator log (`P/coordinator/morning-report-notes.md`, its end is authoritative).
**[V1]**, **[V2]** from `P/nightplan/round6/v1.md`, `v2.md`. **[read]** I read the artifact in this pass.
**[I]** my inference, not checked by a run. Times are the night's measured times on this machine.

## 0. Shape of the plan

1. **Round F** = F1, then F2, then F3 as one chain in one worktree, one mutation pass, one paid review round, one
   `release_prep.sh`, one release-mode full check, one commit, one tag.
2. **Round K** = the K-1 integration stack (13 patches), then k1e. Form 8615 follows as its own round.

Why one chain and not three lanes: nearly every patch edits `interview/2025/questions.yaml`, and F2 and F3 were
cut against F1's text [log 01:45 revision; V1].

Why round F cannot commit in pieces: F1 changes `engine/src/mutate.ts` (it removes one pinned argument)
[read: `git diff 50895515 5a180443 -- engine/src/mutate.ts`]. That file is a full-tier path
(`tools/full_paths.txt`), so `commit_tested.sh` refuses a commit on a fast-tier green [log 10:25]. The round
therefore lives in its worktree as staged work and saved patches until the one full check. Each step below ends by
saving a patch and a tree id to `P/post-release/state/`, which is the interruption point.

Open before starting (see OWNER-DECISIONS.md): the review budget (A1), decision 8 (A2), the thrift-store item (A3),
the `any` design issue (A4). A2 and A3 ride inside F1 at their defaults; A4 decides which F2 patches are in.

The next tag: the release under check takes r2026.11.16.1. `coordinator/PHASE-B-RUNBOOK.md` gave that same name to
the fix round's release, and it is stale on this point. Round F takes the next free name on its date.

## 1. Step F-0: confirm the base (10 min, no CPU)

Inputs: `main` after the release; the tag.

1. `git log -1 main`, `git tag -l 'r2026.11.16*'`, `git status` in the main checkout. Set aside any hook rows in
   `research/costs/agent_runs.jsonl` before any rebase or release step [log 00:50].
2. Confirm what R holds, because the plan below assumes it [I until checked]:
   - `tools/release_prep.sh`, `tools/rename_ids.py` (T-337, T-338) [read: both are in the xint worktree].
   - the five lane blocks in `engine/src/mutate.ts` (m1116, mk1, mrental, mint, mstruct) [read: present in xint].
   - `bug_pending/mint-01.md` assigned, and the 5 `OPEN_DEFECT_SURVIVORS` lines carrying its BUG number.
   - the sources of S0 (p936, p926, i1040sh, usc-26-402, usc-26-457) in `sources/2025/manifest.json`.
   - **Not in R:** `screens.patch` and `screens-joint.patch`. The xint copy of
     `tools/transcription/screen_review.py` still tells reviewers that married filing statuses are refused elsewhere
     [read]. They land in step F-5.
3. Write `agent_runs.jsonl` rows that the night left out: lane MINT and its 4 forks, lane M-rental
   (`round7/mint.md:9`, `round7/mrental.md:212`), and this lane.

Interruption point: none needed; nothing is changed.

## 2. Step F-1: rebase F1 onto R (lane F1R, judgment)

Inputs, in order:

| # | Input | What it is |
|---|---|---|
| 1 | branch `fix-round-1` in `.claude/worktrees/f1`: 40b28ede, bf1a47b6, 5a180443 on 50895515 (`refs/scratch/f1-base`) | unit 1 the 79-file `patches/v3/fix-round.patch`; unit 2 trimB; unit 3 trimA |
| 2 | `P/nightplan/round6/v1/f1b-0452.patch` (V1's snapshot of the 04:52 `f1/fix2/f1b.patch`, 20 files) | unit 4: build errors and fixture debt; message `P/f1/msg4.txt` |
| 3 | `P/nightplan/patches/v4/personas.p1.patch` | unit 5: personas 23 to 31 (walked clean at 05:12) |
| check | `P/f1/f1-staged-with-personas.patch` (29 files) | must equal 2 + 3 applied on 5a180443 |

Before rebasing, prove the inputs agree, with git only (a private `GIT_INDEX_FILE`, `read-tree 5a180443`,
`apply --cached` 2 then 3, `write-tree`; compare with the same for the 29-file patch, and with
`git -C .claude/worktrees/f1 write-tree`). If they differ, the staged worktree wins and the difference is reported.
`msg4.txt` describes unit 4 only; unit 5 needs its own message.

Rebase: `git rebase --onto R 50895515 fix-round-1` in a new worktree cut from R (keep the old `f1` worktree until
the result is checked), then `git apply --3way` for 2 and 3. Clone review data with `tools/worktree_data.py clone`.

Known conflict points. The base 50895515 is the release candidate of 02:01; everything XINT did after that is new
under F1:

| Where | What R changed after 02:01 | What to do |
|---|---|---|
| `fixtures/2025/classm.json`, `f8853c.json`, rulings | the collection-key rename fix (`f8853c[p0].pre1996`) [log 02:15] | take R; F1's 2 standing failures (`classm.f8853c.1`, `x2s1o.f8853c.refuse.pre1996`) should disappear [I]. If they stay, that is a finding |
| `fixtures/*/classm*.json`, `mutation.json` (us and ny) | X-MUT re-pins; cases added in R | f1b adds `household.spouse_cp_domicile: false` to 47 MFS and married-HOH cases. Do not trust the hunks: after the merge, find every MFS or married-HOH case in the no-defaults files that lacks the input and state it. These files take no defaults (`engine/src/fixture-inputs.ts:439`) |
| `engine/src/mutate.ts` | 65 re-pins; the lane blocks in `EQUIVALENT_IF`; the unobserved-line rule; open-defect lines | F1 removes the pinned argument `operand.sa.sa.gift_carryover_if_no_gifts.no.then1` (BUG-0817a). Re-do that deletion by hand on R's file; keep every lane block whole |
| `fixtures/2025/k1p.json`, `k1s.json` | +19 cases with `scope.k1: true` (X-K1) and +64 `mk1.*` cases [read: 64 ids in `round7/mk1.patch`] | F1 changes the K-1 forms (0837, 0838/0886, 0841, 0843/0882, the k1s.qbi refusal, `k1s.interest_buy`, the four `ask_*` helpers). Textual merge is by case id. The 64 hand-predicted cases were derived on R's forms: any that fail on F1's forms are re-derived from the sources, never copied from the evaluator |
| `forms/2025/dependent.yaml`, 3 pinned fixtures | the completion-leak fix (helper chooses; xleak-01, -02) [log 04:20] | take R. F1's fix3 problem "generated.53 complete while `dependent.absence_no_return` is reachable" may be this leak [I]; recheck in group D |
| `tools/interview_rules_baseline.json`, the pruning in interview-rules | rewritten in R [log 04:20] | take R, then apply what fix3 asks: remove `person.work_ssn`, `scveh.suv`, `dependent.born_died`, `.kidnapped`, `.months`, `.placed` if still reported [read: `P/f1/fix3/interview_rules.txt`] |
| tests that expected MFS refused (test_serve, test_integration, classm job seeds, ny_mutate args) | re-pointed in R [log 02:45] | take R |
| rulings sidecars of clcw_next_year, f8962, rec, refund | 26 witness names renamed by the T-338 migration [log 02:45] | if F1 touches these sidecars, re-run `rename_ids.py` rather than merging by hand |
| `tools/coverage/consumers.json`, sibling lists, `bug_status`, review packets | repaired in R [log 06:50, 09:35] | take R, regenerate |
| every generated report: `reports/2025/interview_coverage.md`, `mutation.md` (us, ny), `interview_length.md`, `docs/COVERAGE.md`, `bug_status`, `doc_figures`, review packets | regenerated in R | never merge by hand. Take R's side, then regenerate with the tool's own `--write` at the end of the step |
| `bug_pending/` | R assigned its pending entries | F1's `bug_pending/fix-round-1-01.md` keeps its placeholder until step F-4 |

Checks, run directly and in this order (each one is cheap next to a full check; a step that crashes hides the
later ones, so after fixing a crash rerun that step before going on):

1. build.
2. `test-fixtures`, us and `--ny`. Night's figures to compare: F1 fix3 2404/2406 and 361/361 on the old base; R has
   2528/2528 and 358/358 [log 10:00, `round7/mint.md`].
3. `interview-coverage` full and ny (0 problems in fix3), then `--write`.
4. `tick-groups` (0 in fix3).
5. `interview-rules`: this is group D, deferred to after the rebase [log 04:40]. Triage each line; a completion
   leak is fixed and pinned, not baselined (the night's ruling on the two leaks, log 02:15).
6. `draft-walk`, us and ny, all 31 personas. Known: personas 05 and 13 leave `s2.amt_business` unanswered (present on
   base too). Fix answers, never the expected ends.
7. `tools/coverage/tree.py --check`: F1 has 11 k1p/k1s refusal gates with no `tree.json` entry [V2 section 1]. Place
   them here; they are F1's debt, not the K-1 stack's.
8. BUG-0836: the fix is in unit 1 (`f8582.mfs_together`) but the inventory entry has no Fix line [V2 section 5].
   Write the closure in step F-4.
9. List every prompt, label and help over the N10 limits in the changed entries (the trim lanes kept 7 overruns
   with reasons; the owner decided tick members take the 25-word limit).

Interruption point F-1: all nine green or triaged; save `state/F1.patch` (diff against R) and the tree id. Nothing
is committed. A later session resumes by applying that patch on R.

## 3. Step F-2: the trim follow-ups (same lane, same worktree)

Inputs, in order [V1 section 5]: `patches/v4/tf-a-f3.v1.patch`, `tf-a-f4.v1.patch`, `tf-b-f2.v1.patch`,
`tf-b-f1.v1.patch`, `tf-a-f1.v1.patch`. Which of these are in depends on owner decision A4; the default there holds
`tf-b-f1` and `tf-a-f4` out until their derived lines read every member.

The `.v1` patches were validated on 5a180443 + f1b-0452, without the personas and without R's later work. Expect:

- **Context drift** in the bank and in the fixture files. Use `git apply --3way`; V1's `chain3.py` and `resolve.py`
  (`P/nightplan/round6/v1/tools/`) did the same job on the old base.
- **Fixture restatement must be re-run, not applied.** The restatements are mechanical and large (B-F1: 935 false
  and 39 true in every file; A-F1: 305 + 3 in the no-defaults files; A-F4: 126; B-F2: 125 + 14; A-F3: 10)
  [V1 section 2]. R added about 150 cases the hunks do not know (64 mk1, 10 m1116, 24 mexist, 32 mrental, 12 mint,
  the 19 X-K1 edits). Apply the form and bank hunks, then run `round6/v1/tools/restate.py` and `fix_f2.py` on the
  merged tree, then diff against the patch's fixture hunks to see only the new cases differ.
- **Personas 23 to 31** were written before F2. tf-a-f4 edits persona 13 and tf-b-f1 personas 17 and 18; the new
  nine need the same treatment where they answer `asset.listed`, `f1040.digital_assets`, `gift.special` or NY
  `owes_use_tax` [I].
- **Retired inputs are collection-indexed** (`asset[...].listed`, `gift[...].special`). This is the rename class
  that broke five steps on 11-16. Use `tools/rename_ids.py` and its check; then grep fixtures, coverage rows,
  personas, rulings, `tools/limits.json`, `changes/2026/*` (operation `from` locators) and the frozen review packets
  for every old id.
- `engine/src/generate.ts` and `interview/ny/2025/ny.yaml` are part of the v1 patches (the drafts missed them)
  [V1 section 2].

Checks: the same nine as F-1. Expected from V1's run: fixtures equal to the F-1 result; `interview_coverage.md`
needs `--write` (676 rows from 674); tick-groups pass; walks +1 question, +5 prompt words and +22 help words for
every persona if `tf-b-f1` is in (the design had predicted "about equal").

Interruption point F-2: save `state/F2.patch` (diff against the F-1 tree) and the tree id.

## 4. Step F-3: the deferred lows (same lane, same worktree)

Inputs, in order [V1 section 5]: `def-0871`, `def-0795.v1`, `def-0765`, `def-0891.v1`, `def-0779.v1`, `def-0889`,
`def-0786`, `def-0778.v1`, `def-0828.v1`, `def-0895`, `def-0570a`, `def-0791.v1`. Held: `def-0570b`, `def-0719`
(owner decision C5). `def-0791.v1` assumes tf-a-f4's asset numbering: if A4 holds tf-a-f4 out, use the original
`def-0791.patch` and re-check.

Unfinished at V1's stop, to do first:

1. The 11 coverage-row problems (table in V1 section 2, F3 item 3). The fixes there are proposals, none verified.
   Start with the `royalty_only` set: its `sche.*` answers went stale, which may mean def-0889 changed royalty
   routing. Decide that before touching the rows.
2. Read `P/nightplan/round6/v1/f3/interview_rules.txt` (the run was left to finish on its own); compare with
   `f2/interview_rules.txt` using `tools/cmp.py`.
3. tick-groups and draft-walk (us, ny) were never run on F3.
4. Two v1 fixes were not re-run: the def-0795 spouse phrase and the `xfix.r11.qip_screen` remedy text.

def-0765 also edits generated or quoted text: regenerate `f1040.md`, `interview_coverage.md`, `docs/COVERAGE.md`
and edit `research/ty2026/forms-proposed/f1040.yaml` in the same step [log 02:50]. Its restated expectation is
owner item C6.

Checks: the same nine. Interruption point F-3: save `state/F3.patch` and the tree id.

## 5. Step F-4: bookkeeping on the merged tree (mechanical; Sonnet, or Fable if the owner says so)

1. `new_bug.py --assign` for the pending entries the round carries: `fix-round-1-01`, the JR entries
   (BUG-NEW-JR-01..06, `round4/jr.md`), `mk1-01` if R did not assign it, `rec-01..04` and the drafts in
   `P/post-release/bug_pending-drafts/` once the owner has read the ones marked "pending owner reading".
2. Closures for every entry the round fixes, with the closure commands the plans drafted (`lows.md`,
   `round4/lows-*.md`, `round5/deferred.md`); BUG-0836's Fix line; BUG-0916 gains the `f8853c.line22` note
   [log 00:30].
3. `tools/claims.py`: claim the forms the round touches; release at the commit.
4. `tree.py` (write), `bug_status`, `doc_figures`, `check_bug_inventory`, `check_agent_runs`, `siblings_check`,
   `check_consumers`, `citations --strict`, `year_changes --check`, `check_limits`, `tools/defaults_guard.mjs`,
   `refusal_reach`, review packets.

Interruption point F-4: save `state/F-merged.patch` (whole diff against R) and the tree id. From here the tree's
form content is frozen except for review rulings.

## 6. Step F-5: mutation pass (one measuring run, then lanes, then one confirming run)

A unit is not release-ready until mutate and refusal_reach complete on it; an expansion carries its own kill work
[log 07:45].

1. **One** federal mutate and one NY mutate on the F-4 tree, alone on the machine, `MUTATE_WORKERS=12`. Measured:
   33 min alone at 10,022 mutants and 2,528 cases with 8 workers; 47 to 67 min when sharing [log 11:30, 10:45].
   Round F adds mutants and cases, so plan 40 to 45 min.
2. Read three lists from the report: stale arguments, retarget problems, and "not yet explained".
   - **Stale arguments.** Every keyed argument pins a premise digest; a changed line on its chain makes it stale.
     The night's rate: 65 stale from the expansion, resolved per argument (56 re-pinned, 1 retargeted, 4 removed)
     [log 05:20; method in `round6/xmut.md`]. Forms round F changes that carry arguments: household, k1p, k1s
     (mk1's 11, mint's 3), rental and rec (mrental's 10, mint's 2), sa, s1, ira, eic, f8853c, f1040, dependent.
   - **New survivors, by unit** [I, from the patch contents]:
     - F1: the three cp-domicile helpers and their gate; the five Bool helper gates of unit 4; the K-1 `ask_*`
       helpers and `interest_buy`; `rental.not_at_risk`; `f8582.mfs_together`; the two canceled-debt tick groups
       (ten inputs and a derived line); `f1040.tax_exempt_any`; the `rprop.screen` parts and the QIP child;
       the 0817a carryover asked of every giver; the NY lines of older-ny.
     - F2: every derived `any` line. `gift.special` over 11 items alone gives at least 11 operand mutants, each
       killed only by a case that ticks that one item; the same for `asset.listed` (2), `f1040.digital_assets` (2)
       and NY use tax (2, in the NY run).
     - F3: `retirement.ira_basis`, `scope.treaty`, `rprop.exchanged`, `rental.held_for_sale`, the `royalty_rare`
       members, the new sche line, `rental.prior_ws51`, the f8960 section 6013(g) refusal, `refund.exc_who`, the
       def-0791 asset lines.
   - **Kills that stop killing.** A hand case that F changed, or whose form changed, may no longer tell its mutant
     apart. They show up as new survivors on old lines.
3. **Budget.** The night cleared 372 survivors in about 3.5 hours of wall time with a witness search, five family
   lanes and an integrator, and most of that time was lost to CPU contention [log 07:35 to 10:45]. Round F is
   smaller: plan for 60 to 150 unexplained [I; the measuring run replaces this guess]. Under about 40, one lane does
   it. Above, split by form family into at most three lanes, each with its own fixture files and its own delimited
   block in `EQUIVALENT_IF`.
4. Lane rules, written into every brief:
   - `tools/mutant_witness.mjs --only <ids>` for the lane's own mutants, at most 4 workers, `nice -n 10`.
   - **No lane runs a full mutate.** The integrator runs the one confirming run. Never two full mutates at once on
     this machine: two ran 63 and 79 minutes against each other [log 09:35].
   - Fixtures are hand-predicted from the sources, in the form's own fixture file, not in `mutation.json`.
   - An equivalence argument must pass the sampled check; an answered-only argument says so. A kill that rests
     on which refusal comes first, or on an unanswered input, is flagged as weak (see the test-strength draft).
   - Any new case in a no-defaults file states every input the round added.
5. One confirming federal mutate (and NY if NY files changed) on the merged result: exit 0, 0 stale arguments.

Interruption point F-5: after any lane's patch is saved; after the confirming run, save `state/F-mut.patch`.
The kill lanes can start on forms the reviews (step F-6) are not expected to touch while the reviews run.

## 7. Step F-6: the one paid review round

Order inside the step: land the screen-prompt patches, list what is due, dry-run the cost, get the approval
(owner A1), run, adjudicate, apply rulings, stop.

1. Apply `patches/v3/screens.patch` then `screens-joint.patch` (review tooling; prompts show the interview wording
   and stop telling reviewers that joint-only gaps are refused elsewhere). Every screen record becomes due: 149
   federal and 12 NY, about $21 [log, A10]. No migration.
2. What is due. `check_logs` (us and ny) names the stale logs; `tools/release_reviews.sh` names the stale sampled
   reviews (run its checks without `set -e`, or through `release_prep.sh`, so every due item prints). Expected, to
   compare against the tools' lists:

   | Kind | Scope | Forms and subjects expected due |
   |---|---|---|
   | transcription, render | line-scoped (the default in `rerun_all.py`; `--whole` only if the tool refuses) | F1: household, scope, person, tipjob, s1, s2, f1040, sa, gift, rental, rprop, f8582, sche, k1p, k1s, f8853c, ftc, the credits forms of older-credits, `ny_it201`. F2: dependent, asset, f1040, s1, gift, `ny_it201`. F3: retirement, scope, f1040 (line 12e refusal; line 3a), rprop, rental, royalty, sche, f8960, refund, asset |
   | class M | only where arithmetic changed | F1: f8582 (0836), household (cp split), s1 (canceled debt), rprop, sa (0817a), k1p, k1s. F3: rprop, rental, royalty, f8960. F2: dependent only if the review rules count a gate as content [trimfollow.md:114]. Input-only restatements are OD-31: leave due and list them |
   | screen | all, after item 1 | 161 records |
   | false-no | sampled | `f1040.digital_*` (tf-b-f1), `gate:asset.industry` (0791), `gate:scope.other_income` |
   | completeness | sampled per release | every federal form whose content changed; 11 forms were stale after the expansion [log 23:55] |
   | question review | per entry | every new or reworded bank entry (F1's trims count) |

   One review per form per round, after all of that form's fixes: f1040, rental, rprop, asset, gift, scope and
   `ny_it201` are each touched by two or three units, which is the reason the round reviews once, here.
   Known limit: the person prompt is 820k characters, over the 700k limit [log 23:55]; person must stay line-scoped.
3. Dry-run. `tools/transcription/rerun_all.py --dry-run` prints the plan and the estimate per job and in total and
   stops; `completeness_review.py`, `screen_review.py` and `false_no_review.py` have the same `--dry-run`
   (tools/README.md, "Review rerun guards", "Cost estimate", "Owner gate"). Any run estimated above $3.00 needs
   `--approve-cost DOLLARS`; a log that already answers its subject needs `--force-rerun REASON`. Earlier
   estimates, for comparison only: F1's lines about $64 core and $103 with options, approval sought $135
   [lane-briefs OD-14]; screens $21; F2 and F3 were never priced.
4. Run with the approved figure. Every call is logged in `.transcription/costs.jsonl` with year and jurisdiction.
   Reviews keep their default model (`claude-opus-5-5`); the Fable instruction of 10:02 named subagents only.
5. Adjudicate by form family in parallel forks (judgment); apply rulings and bug entries on a mechanical agent.
   Rule repeat disagreements with the carry-over tool where it allows.
6. A ruling that edits a form's YAML makes that form's logs due again and can add mutants. Batch all such edits,
   rerun only those forms' line-scoped reviews once, and send the changed lines to the mutation integrator before
   the confirming run. A round whose reviews find only lows starts no further round.

Interruption points F-6: after the dry run (nothing spent); after each form's logs are written (the ledger and the
store are the state; carry them with `worktree_data.py carry-back`, never by hand); after adjudication of each
family.

## 8. Step F-7: release_prep, the one full check, commit, tag

1. `tools/release_prep.sh` (it runs every step and reports every due item; `--fail-fast` exists). Measured: over
   22 min, the interview-rules step alone about 10 [log 11:50]. Fix everything it reports, then rerun any step
   that crashed before believing the rest.
2. Directly, the slow steps the fast tier skips, except mutate (done in F-5): `compare`, `ny_compare`,
   `engine_differential`, `lean_build`, `interview_length`, the renamed-ids step.
3. Check `tools/full_paths.txt` against the diff, to know which tier the commit needs (full, here).
4. ONE release-mode full check through `tools/check_all_bg.sh` (one at a time per clone), 75 to 90 min. Renice
   every lane before it starts. Wait on its pid or poll `tools/check_all_bg.sh --status`, with a timeout; never
   `pgrep -f`.
5. Green: confirm `git write-tree` equals the tested tree (the run can copy regenerated reports back);
   `commit_tested.sh`; set the agent_runs hook rows aside; fast-forward `main`; push; `tools/release.sh --push`
   (the skip path fires when HEAD's tree is release-listed). Tag with the next free name.

Interruption point F-7: before item 4 (a green `release_prep` is a stable state); after item 5.

## 9. Round K: the K-1 integration stack, then k1e

Base: the round F commit. Blocked until owner decision B1 (tick-group placement); B2 and B3 change what lands.

Inputs, in order [V2 section 7]:

1. `patches/v3/k1int-1-f8582.v2.patch`
2. `patches/v3/k1int-2-ebl-qbi.v2.patch`
3. `patches/v4/k1block-0-k1int3-rebased.v2.patch` (in place of `k1int-3-return.patch`)
4. `patches/v3/k1int-4-fixtures.patch`
5. `patches/v4/k1block-1-lift-gate.v2.patch`, then `round6/v2/restate_k1e.py ROOT` (do not rely on its 948
   restatement hunks on a moved base)
6. `patches/v4/k1block-2-passive.patch`
7. `patches/v4/k1block-3-line25c.v2.patch`
8. `patches/v4/k1block-4-line3a.patch`, then `scratch/round5-k1block/restate_line3a.py ROOT --check` must print 0
9. `patches/v4/k1block-5-f8960.patch`
10. `patches/v4/k1block-6-f4952.v2.patch`
11. `patches/v4/k1block-7-qbi-label.patch`
12. `patches/v4/k1block-8-f8582-exception.patch`
13. `patches/v4/k1block-9-coverage.v2.patch`

Known conflict points:

| Where | Why | What to do |
|---|---|---|
| the whole stack | validated on 5a180443 + f1b-0452 only: no personas, no R-after-02:01, no F2, no F3 | replay in a scratch index first (V2 section 7 item 2), then fix contexts one patch at a time; several patches checked together miss clashes |
| `fixtures/2025/k1p.json`, `k1s.json` | R added the 19 X-K1 cases (`scope.k1: true`, refusing at `scope.schedule1`) and the 64 `mk1.*` cases | the lift removes the `scope.schedule1` refusal, so the 19 refuse fixtures' ends must be re-derived [I]. The mk1 cases state `scope.k1: true` and assert only K-1 lines and person totals, by design, so they should hold [`round7/mk1.md`], but 24 person lines become gated: run them first |
| every no-defaults file, and all cases R and F added | `scope.k1e` is a new input | `restate_k1e.py` after the merge; then grep the no-defaults files for `scope.k1` without `scope.k1e` |
| line 3a (775 restated occurrences) | F and R added cases that state line 3a | `restate_line3a.py`, not the hunks |
| `f8960.unsupported` (k1block-5) against def-0828 (F3); `sche` (k1block-1) against def-0889, def-0786; `f1040` (k1block-3, -4) against tf-b-f1 and def-0765, def-0570a | same lines, different rounds | 3-way, then re-read the merged text against both designs |
| `engine/src/mutate.ts` | the mk1 and mint arguments on k1p, k1s and f7203 pin premise digests; the wiring changes their chains. The unobserved-line rule lapses as readers appear. The 5 open-defect survivors must still survive, or the run fails | re-pin per argument after the measuring run; re-check the 5 |
| 4 `mutation.m3.scope.l16_f8615_*` cases | to be restated in the K-1 merge as a separate commit [log 02:55] | tool-managed file: use the tool |
| reports, `tree.json`, `docs/COVERAGE.md`, README table | regenerated | take base, regenerate; the README item wording is owner item B2 |

Unfinished at V2's stop, to do first (V2 section 6):

1. The 12 incomplete rows (10 in `coverage/k1p.yaml`, 2 in `k1s.yaml`) with `round6/v2/fill_rows.py`; check that
   each row's end and situation still hold; `interview-coverage --write`; re-cut k1block-9.
2. Decision B1, then tick-groups (4 problems, one defect).
3. The steps V2 did not run: `citations --strict`, `check_consumers.py` (6 drafted rulings to adjudicate),
   `interview-order`, `year_changes --check`, `defaults_guard.mjs`, `estimate.py`.
4. Three K-1 personas (a limited partner with a passive loss and portfolio income; an S corporation
   owner-employee; a refused publicly traded partnership), walked before and after. No persona has a K-1 today, so
   no walk reaches the rosters; V2 suspects about 30 per-box questions for a portfolio-only K-1 (N1).
5. The unexplained disappearance of three interview-rules problems under the stack (generated.53, generated.327).

Mutation for round K: the K-1 family was 132 of the 372 survivors while its lines were latent. Wiring adds readers
in sche, f8582, s1, s1a, s8812, f1040 (3a, 25c), qdcg, sdtw, f8960, f4952, qbi and sd. Plan it as large as the
night's K-1 lane: one measuring run, two family lanes (k1p side, k1s and f7203 side) and an integrator, under the
F-5 rules.

Reviews for round K: `round5/k1block.md` section 4 lists them per unit, on top of the k1int reviews. Batch person,
f1040, sche and f8582 so each is reviewed once. Price with `rerun_all.py --dry-run`. Question review for
`scope.k1` and `scope.k1e`.

k1e rides as the last step of round K [log, A8]: carry its paid reviews ($1.35) and the pending low `xrevk1e-01`
back from the `x2-k1e` worktree with `worktree_data.py carry-back` before any rerun; its 19 fixtures set
`scope.k1: true` and need `scope.k1e` instead after the split [I].

Then one `release_prep.sh`, one release-mode check, commit, tag. Interruption points: after each of the 13 patches
(save the tree id, as `round6/v2/trees.txt` did); after the rows; after the mutation pass; before the full check.

Form 8615 comes after round K: `patches/v4/f8615-form.patch` then `f8615-int.patch`; renumber its personas to 32
and 33; about 1,330 fixture lines retire; blocked on owner items D1 to D3.

## 10. Parallel lanes

The chain F-1 to F-3 is one lane because of the shared bank file. What can run beside it:

| Lane | When | Class | CPU |
|---|---|---|---|
| F1R (the chain) | F-1 to F-3 | judgment | builds and checks; the critical path |
| REVLIST: from the patches alone, write the expected due-review list and the dry-run command lines for F-6 | from F-1 | mechanical | none |
| PERS-K1: draft the three K-1 personas with hand-derived values | from F-1 | judgment | none |
| ROWS-F3: re-derive the 11 F3 coverage rows from the designs (`deferred.md`) on paper, for F1R to apply | from F-1 | judgment | none |
| BOOK: closure commands, pending-entry texts, agent_runs rows for F-4 | from F-2 | mechanical | none |
| kill lanes (1 to 3) | after the F-5 measuring run | judgment | `mutant_witness --only`, 4 workers, nice 10 |
| adjudication forks, by family | during F-6 | judgment | none |
| round K re-context (replay the 13 patches in a scratch index on the F-4 tree) | after F-4 | judgment | git only until F-7 is green |

Rules for every brief (the night's lessons):

- State the model, the class, the year and the jurisdiction; the `agent_runs.jsonl` row records all four. New
  subagents ran on `claude-fable-5-2` by the owner's word for the last session; a new session needs the owner's
  word again, otherwise mechanical work is Sonnet and judgment is Opus (CLAUDE.md).
- Start every engine command under `nice -n 10` (15 while a critical check runs). Cap workers at 4. About one
  build per two cores at most, and fewer while the full check runs.
- No full-suite verification in a lane: no full mutate, no check_all, no fast tier unless called in to commit.
- No shell functions, no bulk process spawning. One long wait on a pid, with a timeout; no `pgrep -f`, no polling
  every few seconds.
- Worktrees clone review data with `tools/worktree_data.py clone`; results come back with `carry-back`.
- A design that says "no fixture changes" or "the default covers it" is checked against the class M and mutation
  files, which take no defaults, and against asserted remedy strings, before it is believed.
- A rename is followed at once by test-fixtures and coverage, and covers collection-indexed keys.
- A repair that edits a form's YAML schedules that form's line-scoped reviews in the same repair.
- Estimates are given only after a measured pass of the step in question.

## 11. Cleanup, after round F lands

Worktrees s0, t1, v1, v2, mw, m1116, m1116sb, mk1, mk1s, mrental, mexist, mint, mstruct, p1, f1 (after the rebased
copy is checked); `refs/scratch/xint-fast`, `refs/scratch/f1-base`; `/tmp/t1-xint.diff`. Keep
`refs/scratch/qdcg-amount` (Form 8615 needs it) and the `x2-k1e` worktree (it holds k1e's reviews).

## Provenance

Inspected: the coordinator log (whole file); `round6/v1.md`, `v2.md`, `owner-sources.md`; `round7/mint.md`,
`mstruct.md`, parts of `mrental.md`, `mexist.md`, `mk1.md`; `round5/k1block.md` sections 3 to 6 and the review and
owner lines of `trimfollow.md`, `deferred.md`, `f8615.md`; `records-staging/MORNING-REPORT.md` and
`protocol-8.10-additions-v2.md`; `coordinator/PHASE-B-RUNBOOK.md`; `f1/msg4.txt`, `f1/fix3/exits.txt` and
`interview_rules.txt`; `tools/full_paths.txt`; `git worktree list`, the scratch refs, F1's three commits and its
staged file list; the listing of `patches/v3` and `v4`.

Inferred (unverified): every conflict point marked [I]; the contents of R beyond what the xint worktree showed
at about 12:00 (the release check was still running, so R did not exist yet); the per-unit lists of new mutants and
of forms due for review, which are read from patch descriptions and not from `check_logs` or a mutate run; all
time budgets beyond the measured figures quoted.

Gaps: `round4/*.md`, `lane-briefs.md` sections 1 to 4, `round5/tools.md`, `round5/personas.md` and
`round6/s0.md`, `t1.md`, `xmut.md` were read only by search, not in full. No patch was test-applied.
