# Night 2026-11-10/11: phase 3 fix lanes landed, display rewording, five tech-debt items

**State:** `main` is pushed through `e29575ff` (the next commit after it holds this entry's update, BUG-0605, BUG-0606,
T-280 and T-281). No release has been cut since `r2026.11.06.1`. One lane is still running: T-278, a batch mode for the
Lean binary; it merges with a full run on main when it reports. Review spend in the session, from
`.transcription/costs.jsonl`: $81.59 in 140 calls ($24.87 in 59 calls on `claude-opus-5-5` before the owner's switch,
$56.71 in 81 calls on `claude-fable-5-2` after it). No open rulings; transcription, render and class M logs current.
`canonical/` in the main checkout was rebuilt at `e29575ff`, so a UI server started now shows the merged interview.

**Landed (first-parent, oldest first):**
- `38f7b30c`, `d7c84578`, `3f589ccc`: lanes F (test-serve), B (question review tool, first full pass, 674 findings
  ruled, BUG-0498 to BUG-0576) and E (umbrella gates design).
- `5fd0fa1c`, `bbd20a86`, `cd7aa2e0`, `85c19914`, `b90c2787`, `dbc455da`: fix lanes 1, 4b, 2, 3, 4 and 5. The 45
  value-changing findings of the question review are fixed (Schedule C; IT-201; Form 5695; carloan, s1a, otjob, s179,
  asset, div, sales; person, retirement, dependent, f2441), and once-per-return amount and yes/no questions name the
  spouse with one phrase, "(or, on a joint return, your spouse)". BUG-0577 to BUG-0593.
- `bf599378`: umbrella gate U2 (`sb.foreign_any` before the four Schedule B foreign screens; 3.0 fewer questions on
  complete full-profile returns, 111.2 to 108.2); the launch hook allows Fable for either class of agent work.
  BUG-0594, BUG-0595 open and low.
- `355d7302`: lane 7, `engine/src/spouse-wording.ts`: question text and line labels handed to an interactive client
  read "you or your spouse" on a joint return and "you" otherwise; the stored conditional text shows only while
  `f1040.status` is unanswered (it is the first or second question on every standard walk). Stored text, `canonical/`,
  `rendered/` and reports are unchanged. The build fails on a near-miss of the phrase.
- `131747ca`: lane 6, wording fixes from two independent source checks of the spouse edits (BUG-0596; BUG-0597 open).
  49 one-form Form 8962 fixtures withhold `f1095a.b_counted`.
- `e554f671`: process lane. Review tools refuse to run on stale rendered text (BUG-0599); check-all prints its step
  times by stage (`tools/check_times.py`).
- `ddb6bd99`: T-259. The Lean comparison runs over the general generator's returns (400, seed 7): 562 of 564 federal
  inputs given, 0 differences in either jurisdiction; its self-test plants 16 differences (BUG-0598).
- `2e13fd84`: T-267. The mutation check's pin digest leaves out question wording; all 81 pins re-made after each was
  shown to match and each argument was read.
- `abf6c558`: bookkeeping (T-259, T-267 done; T-269 to T-275; three studies under `docs/`).
- `bdfc9a1e`: twin lane. `tools/check_twins.py` keeps the two copies of Form 8863 Part III in step, with intended
  differences declared in `reviews/2025/twins.json` (BUG-0600).
- `2be2a2cf`: `tools/check_year_ids.py` refuses any new id that carries a tax year (baseline `tools/year_ids.json`).

- `7710ad87`: T-269. All 626 fixture defaults audited; two that were not truthful answers withheld.
- `bc0e582a`: T-271. One corpus definition for the Lean comparison and the properties check; `tools/step_output.py`
  makes check-all require the line each in-step self-test prints. The New York lines stay in the federal run.
- `1fd531f9`: T-277. Conditional withholding and consistency rules in `defaults.json`; `dependent.lawful` defaults to
  yes; 65 per-case nulls removed. BUG-0605 and BUG-0606 open.
- `e29575ff`: gate lane. Five conjunctions on `dependent` and Form 8962 rewritten as nested `choose` (the top four
  families of the interview-rules catalog): asked-and-unread questions fall from 373 to 31 on a 2,000-return sweep, no
  open question at completion can refuse the return, and the interview-rules baseline is empty (BUG-0603; BUG-0604
  closes BUG-0487 and BUG-0601).

**Morning of 2026-11-11, the owner present.** Three lanes had stopped at about 06:30 on a Fable usage-credit error
with nothing changed, and were restarted. The owner then decided: the gate lane continues (it was launched overnight on
the coordinator's recommendation); the remaining 17 interview-rules families and the widening of the check wait until
he has read docs/2026-11-11_interview_rules_catalog.md; untruthful defaults are handled by conditional withholding
with a build check (T-277, done); the Lean binary gets a batch mode (T-278, running); the three newly single-gated
inputs stay unmarked and `gated_by` is decided for all such inputs at once (T-281); a mechanical backing for the
hand-written mutation arguments is opened as T-280, to be done before the remaining families.

**Decisions the owner made in the session (2026-11-10):** fix lanes may make structural changes where wording cannot
fix a finding; the spouse phrase is the conditional one, shown reworded by filing status; the rule goes on Form 5695,
IT-201 and f2441 too; lanes run their forms' reviews before committing; from mid-session all agents and review calls
use Fable (`claude-fable-5-2`) and cost limits are lifted; lanes are replayed onto main where the BUG id checks block
a merge; the restricted-stock-unit clause in `sales.wash_loss` stays only if sourced (it was not, and is removed); U2's
territory wording stays, its Form 5471 and line 8 screens are widened to the gate, the nonprofit-board and deemed-owner
cases are low bugs; independent source checks of the spouse edits; all four tech-debt items added to the queue. Then:
work through the night on the coordinator's recommendations; goals are integrity, consistency, efficiency and
intelligibility; do not minimize cost, remove cost that returns nothing.

**Decisions taken on the owner's behalf overnight, for review (each is reversible):**
- T-267 narrows the digest for parameter, enum, table and definition premises too (citations, titles and notes left
  out), beyond the task row's wording-only scope. Refusal text stays in the digest.
- T-259's self-test was widened from 3 plants on one line to 16 across the value kinds before it merged.
- Form 8863: the twin check (the study's option A) instead of merging the text. Whether the text must exist once is
  T-274.
- Year-bound ids: no id renamed. A rename cannot be carried mechanically (measured), so the check against new ones was
  built and the rename is left for adoption of the 2026 tree (T-261).
- The `f1095a.b_counted` default is unchanged; the one-form fixtures withhold the answer instead.
- Lane 7 also rewords the 32 line labels shown on the interview's values sheet; reports keep stored labels.
- Lane 6 took the extra readings lane 7 flagged (s1, sli, ssb, household), so four more forms were re-reviewed.
- The earlier Opus reviews were not rerun on Fable (no measured defect; the instruction read as forward-looking).
- The interview-rules check was not widened (T-276). The top four families were then launched before the owner woke,
  which he confirmed in the morning; the other 17 await him.

**Open, for the owner:**
- T-276 / BUG-0602: `interview-rules` still classes only the three complete returns its seed draws. Over 5,000
  generated returns 70 question templates were affected (46 lines, 21 families); four families are fixed. Decide the
  other 17 (41 lines on 13 more forms, their reviews, one fixture moving from false to unknown on an incomplete
  state) and whether to widen the check, after T-280. Catalog and a tested patch per family:
  docs/2026-11-11_interview_rules_catalog.md, docs/patches/2026-11-11_interview_rules/.
- T-280: 86 hand-written mutation arguments, none checked by a machine; five were added by the gate lane.
- T-274: must Form 8863 Part III exist once (a build-time template, which the spec does not have), and should the
  unrolled months of Form 8962 and Form 1095-A (2,346 lines) be planned with it?
- T-261: is a verdict carried under a proven rename acceptable evidence; does the 2025 tree stay under change after
  2026 is adopted; the 36 year-free names.
- T-273: options to shorten the full tier (docs/2026-11-11_check_all_timing.md).
- T-272: the older spouse wordings (about 26 parenthesised, 45 plain "you or your spouse", 21 "either of you") and the
  per-person frame are not reworded for display.
- T-275: the BUG id rule that cannot be carried out on a branch.
- U2's umbrella question is about 640 words and its line 8 screen about 190; the owner said he would judge the length
  when walking his return. Its gate's false-no and screen samples are due at the next release.
- Questions left unedited as unsure by the lanes (spouse's separate prior-year carryovers on f4952, qbi, f8960, clcw;
  `f8863.ban`; six Form 5695 "you owned / original use" questions; three IT-201 credits questions; the 8 refund
  worksheet questions, BUG-0593; `ny_it201.ask.item_c` and 13 return-level IT-201 questions).
- Whether the spouse rule should reach questions asked once per roster item (car loans, sales, assets, Form 1095-A).
- T-236: the owner's walk of his own 2025 return in the UI is still the phase's test.

**What was verified and what was only reported.** Verified by the coordinator for every landing: the commit's parent,
its tree against the tree a full-tier (or, for bookkeeping, fast-tier) run passed, the merged index tree before the
commit, and the push. Not read by the coordinator: the lanes' diffs, source pages and rulings. Independent checks
that were run: two read-only source checks of the spouse edits (81 edits: 1 wrong, 13 awkward, all fixed in lanes 5
and 6); the Form 8962 column (b) ruling (the project is right; the cause was the fixture default); deliberate breaks
of the new tests in lane 7, T-259, T-267, the twin check and the year-id check. Two agent claims were found false
and corrected: lane 5's first agent reported its render reviews current when none had run, and said its edits were
grounded in their cited pages when 31 of 43 rested on the general joint-return rule (i1040gi p. 13). Rulings by the
fix lanes' agents have had no independent read except Form 8962's.

**Process cost that returned nothing (and what was done):**
- Stale rendered text: three paid reviews repeated. Fixed (BUG-0599).
- Pin digest covering wording: 35 re-pins. Fixed (T-267).
- BUG ids: every lane replayed or held uncommitted; merges strictly one at a time. Open (T-275).
- The full tier on every wording lane, where the hook asks only the fast tier: about ten minutes per lane run, a
  coordinator mistake. The full tier is half wave 2 (`engine_differential` with `compare`). Open (T-273).
- Fixture defaults that are not truthful answers manufacture reviewer value differences (24 fixtures on Form 8962,
  fixed; `dependent.lawful`, `dependent.edu_tin_issued` not). Open (T-269).
- Review cost estimates are priced from Opus history; Fable runs at about twice the estimate, and the gate refused an
  approval set at its own estimate. Not fixed; pass about 2.2 times the estimate.
- Reviews repeated because two lanes changed forms that read each other (Schedule 3, Schedule C line 5, IT-201 line
  64). Inherent to parallel lanes with line-scoped reviews keyed to readers; order the merges, or review after merge.

**Process lessons:**
- A lane that adds BUG entries cannot merge main into itself. Either keep its work uncommitted until its turn
  (fast-forward main under it, renumber, run, commit once) or replay its commit onto main as one new commit.
- A merge commit may not add a BUG entry, and a `Fix` field is for form lines (it needs `Fix lines` and `Siblings
  checked`); a tooling fix uses `Disposition`. Use `tools/new_bug.py`.
- A lane committed on main's tip, on a tree its own full-tier run passed, merges with no second run: the merged tree
  equals the tested tree. A lane cut from an older tip needs a run on main.
- Rebuild main (`npm run build`) before committing a merge that changes how fixture defaults resolve: the commit-msg
  guard counts affected cases with the built engine, and a stale `engine/dist` makes it count 0 and refuse.
- When two lanes regenerate the same report, take either side at the merge and commit the tree the run tested, which
  carries the regenerated file; do not hand-merge generated numbers.
- `carry-back` refuses files changed on both sides: check which copy the committed log was written from (the pass ids
  in the log against the index's count) before `--prefer-worktree`. `.transcription/rerun_summary.json` is only the
  last run's summary.
- `tools/commit_tested.sh` wants `COMMIT_TESTED_TREE` set to the snapshot tree, not the tested tree.
- Ask an agent to show a new test failing against a broken implementation before trusting it; and when an agent
  reports a count it cannot explain, have it diff the two runs.
- Treat an agent's "current", "none needed" and "grounded in the cited page" as testimony until a check or an
  independent read confirms it.

**Housekeeping left:** the lane worktrees under `.claude/worktrees/` (21 checked at 06:00: every branch merged into main,
none with uncommitted changes; six more lanes have merged since) and five `backup/*` branches of replayed lanes can be removed after the owner has looked. Scratch under
`/tmp/qfix*`, `/tmp/dedup8863`, `/tmp/yearfree`, `/tmp/f1095a`, `/tmp/twinlane` (the three studies worth keeping are
in `docs/`). `tools/README.md` still says the full tier takes about 38 minutes (median 17). The charter still says
"30 input ids and 93 ambiguity ids". The spouse rule is recorded in `interview/README.md`.

**Next:** the owner's decisions above; then U3 and U4 umbrellas, then U1 once its false-no review is clean (T-265),
the interview-rules rewrites he chooses (T-276), and his walk of the return (T-236).

# Night 2026-11-09/10: gate wave finished, phase 1 closed, eight defects fixed

**State:** `main` is pushed through the interview-layout commit below. No release has been cut since `r2026.11.06.1`.
Review spend this session (Claude only, `.transcription/costs.jsonl`): about $117. No open rulings; every review,
completeness and screen check current; interview-rules baseline empty (0/0/0).

**Landed (first-parent):**
- `8ff9b742` eic.zero reviewed (BUG-0468 closed for eic); carry.py judges log currency with `subjects.log_state` (BUG-0469).
- `20edb6bb` phase 1 remainder merged: human_review docs fast tier; the 22 held tech-debt rows decided (inventory 5.1:
  1 fixed, 2 partly, 4 proposals, 4 deferred, 11 won't fix); scripts run by hand documented; source catalogs under
  `tools/sources/<year>.json` and `tools/sources/ny/<year>.json`; charter renamed `docs/consolidation_charter.md`;
  proposals T-259 to T-263.
- `bed2d176` gate wave (BUG-0471): 62/11/4 held templates to 8/6/2; reviews of the changed forms ($65); completeness
  `elsewhere()` no longer reads a param as a line; mutation survivors killed (29 cases) or pinned.
- `164ca7a2` BUG-0479 (line-scoped catalog lists summed collections) and BUG-0470 (review scope parsed outside
  parentheses) fixed.
- `62c47c07` BUG-0474 to BUG-0478 fixed (s179 working-capital interest, Schedule C home expenses, market discount and
  contingent payment refusal, final-return carryover, Form 5695 installed date); open BUG-0487, 0488, 0489.
- `b9c5b37d` T-264: the last four held families, operand order, `person.work_ssn`, BUG-0473; baseline 0/0/0; BUG-0466
  resolved. Owner-accepted fixture changes: refusal or false to unknown on five incomplete-state fixtures. Open
  BUG-0490, 0491.
- `96ef8a7b` BUG-0472 fixed (chapter 11 debtor refused at return level); BUG-0495 fixed (siblings.py found entries
  renumbered at a merge).
- `436261d6` interview layout: `interview/<year>/` and `interview/ny/<year>/` (files named by profile); BUG-0496 fixed
  (siblings.py matched a quoted heading).

**Owner decisions (2026-11-09/10):** charter undated; New York catalog moved; the five phase 1 proposals are T-259 to
T-263; the unknown-on-incomplete trade-off of nested `choose` accepted (BUG-0471, BUG-0492); the five T-264 fixture
changes accepted; Claude review spend uncapped for the night; push without asking.

**Process lessons (now in the tools or worth keeping):**
- Renumber BUG ids in a branch commit before merging, not inside the merge commit (BUG-0495, BUG-0496).
- Rebuild (`npm run compile`, `build`, `render`) on main after every merge before running review checks or triage; a
  stale `canonical/` or `rendered/` gives false failures and wrong fixture counts.
- Only one check-all run per clone at a time; a refused start means wait and retry. The detached runner, not the
  launcher, is the pid to wait on.
- A merge commit must equal the tested tree: copy the run's regenerated reports into the index before committing.

**Open, for the owner:**
- BUG-0487 (Form 8962 question order), BUG-0488 (three sales rules), BUG-0489 (Schedule C refusal display), BUG-0490
  (SIMPLE salary reduction due date), BUG-0491 (New York use tax and DMV-paid vehicle tax): all open, unfixed.
- T-259 to T-263 (phase 1 proposals). Phase 2 (process rules enforced by tools) is next in the charter.
- `reports/2025/coverage.md` is 53 MB; GitHub warns above 50 MB. Consider trimming or Git LFS.
- Two old agent worktrees remain (`agent-a64a29b0e8ab56370`, `agent-ada089006890714fc`): merged and clean, holding only
  older derived review files (log views, triage) that differ from main's; safe to remove.

- The 51 tracked-but-ignored `.transcription/` and `.classm/` files are untracked (they stay on disk; check-all copies those folders in).
