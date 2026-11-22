# Handoff to DeepSeek (opencode), 2026-11-17

Written by the Claude coordinator for the DeepSeek orchestrator that takes over this project. The owner (Elliot) will
not use Claude on this project again until the IRS final 2026 forms are published (expected January 2027). Until then
you orchestrate the work from an opencode session he runs, and DeepSeek does the reviews. Read this file whole before
acting. Where it conflicts with an older document, this file wins; where it conflicts with something the owner tells you,
the owner wins.

## 0. Rules of engagement

- **Owner decision (2026-11-17):** DeepSeek orchestrates (opencode, with subagents) and DeepSeek does the paid reviews.
  This supersedes the CLAUDE.md bullet "Reviews are Claude-only" for this period. Your first task (section 2) records
  that in the repository.
- Read, in this order: this file; the project `CLAUDE.md` (working guidance; its bullets on worktrees, background
  waits, inference cost, and agent-run records still apply); `.claude/nightplan-2026-11-16/STATE-2026-11-17.md` (exact
  state); `docs/records/2026-11-16/post-release/OWNER-DECISIONS.md` and
  `.claude/nightplan-2026-11-16/post-release/OWNER-RULINGS-2026-11-16.md` (the owner's rulings, binding);
  `.claude/nightplan-2026-11-16/post-release/RUNBOOK.md` (the plan of the next rounds; older than this file).
- The owner's global QMS (`~/.claude/CLAUDE.md`) governs how you work with him: ask before decisions with more than one
  defensible answer, report with an inspected / inferred split, no harness memory, files placed per the storage spec.
- **Work linearly, one atomic unit at a time**, each finished (checks green, committed) before the next starts. Nothing
  large left in flight. Combine and delay expensive checks (one release-mode full check per round).
- Never: push or tag without the owner's go-ahead for that release; use `--no-verify` without the owner's explicit
  approval; edit forms without reading `docs/2026-11-13_interview_construction_protocol.md` (questions) and the
  cited archived sources; pin a value no archived source supports; hand-copy `.transcription/` (use
  `tools/worktree_data.py`); wait with `pgrep -f` (a hook blocks it); run two full `mutate` runs at once.
- Python: `~/.pyenv/versions/3.13.6/bin/python3` (the default python3 lacks yaml). Node engine: `npm run compile` then
  `node engine/dist/main.js build`.

## 1. Where things stand (verified 2026-11-17 10:40 EST)

- `main` = `213058b3`, pushed. Last release: `r2026.11.16.1` on `deca6831`. Coverage estimate 85.9% of returns
  (`reports/2025/filer_coverage.md`).
- **Round F (the fix round), uncommitted**, in worktree `.claude/worktrees/fr2`, branch `fix-round-2`, based on
  `213058b3`. 124 files STAGED. Contents: F1 fix round (rebased), the two kept F2 patches (tf-a-f3, tf-b-f2), the F3
  deferred-bug patches (0871, 0795, 0765, 0891, 0779, 0889, 0786, 0778, 0828, 0895, 0570a, 0791), the owner's four
  rulings (A3 gift item narrowed, C7 dependent read order, C1 rental lines 5 and 8 taken whole, BUG-0719 closed by
  statute: `.claude/nightplan-2026-11-16/post-release/rj-report.md`), the mutation fix-up
  (`.claude/nightplan-2026-11-16/roundF/mf.md`), the screen-prompt fix (screens.patch + screens-joint.patch: screen
  reviews no longer skip joint-only gaps), CLAUDE.md bullets (scarce usage; DeepSeek via opencode), TASKS.md T-339..T-346
  (adversarial review findings), `docs/2026-11-16_adversarial_review.md`, agent-run rows.
- Checks on the staged tree before the reviews: build OK; `test-fixtures` us 2569/2569, ny 363/363;
  `interview-coverage` 0; `tick-groups` pass; `interview-rules` 0; federal and NY `mutate` exit 0;
  `tools/transcription/test_review_tools.py` 275 OK.
- Unstaged in fr2, written by the review runs and a re-render (expected; stage them with the review work):
  `rendered/**`, `fixtures/2025/classm.json`, `reviews/2025/**` logs and sidecars.
- **The paid review round of round F is half done** (Claude, $26.58 spent, stopped by the Pro usage limit):
  - Succeeded with disagreements to adjudicate (28): transcription of asset, f1040, f2441, dependent, eic, f8582,
    f8853c, f8863, household, f5695, ftc, ira, k1s, k1p, person, rec, refund, rental, royalty, rprop, s1, retirement,
    sche, scope, s2, sli, sa; render of f1040. (`.claude/nightplan-2026-11-16/roundF/rerun-summary.json`,
    `rerun2-summary.json`: exit 3 = disagreements.)
  - Not run (failed on the limit), 33 jobs: class M of asset, f1040, f8582, f8960, k1p, k1s, rental, royalty, rprop, s1,
    s2, sa, sche; render of f5695, f8582, f8853c, f8960, ftc, gift, household, ira, k1p, k1s, refund, rental, royalty,
    rprop, s1, s2, sa, sche, scope, tipjob.
  - All 288 screen samples not run.

## 2. First unit: switch the review family to DeepSeek (decide with the owner, then do)

**Important: reviews only count if the project's review tools make them.** `tools/transcription/rerun_all.py`,
`transcribe.py`, `screen_review.py`, `completeness_review.py`, `false_no_review.py` write the logs, subjects, receipts,
sidecars and cost rows that `check_logs.py`, `check_screens.py` and `tools/release_reviews.sh` read. A subagent that
reads a form and writes its own opinion produces none of that, and the gates will still call the form unreviewed. So:
run the review tools with a DeepSeek model; use your subagents to orchestrate and to adjudicate.

The tools already have a DeepSeek transport (`transcribe.py` around line 1723: posts to api.deepseek.com; the key is read
from the macOS keychain item `deepseek-api`, which exists). Model names must start with `deepseek`
(e.g. `deepseek-v4-pro`, `deepseek-flash`). Family rules: `tools/transcription/families.py` (docstring) and
`families.json` (now `{"required": ["claude"], "optional": ["deepseek","gpt"], "active": {"claude": true,
"deepseek": false, "gpt": false}, "models": {"deepseek": "deepseek-flash", ...}}`).

As it stands `check_logs.py` requires a current **claude** log for every form, which can no longer be produced. Options
to put to the owner (read `families.py`, `check_logs.py`, `compare_families.py`, `samples.py`, `release_reviews.sh`
first and confirm each consequence before stating it):
- **(A, recommended)** make DeepSeek the required family while Claude is away: `required: ["deepseek"]`,
  `active: {claude: false, deepseek: true}`, `models.deepseek` = the model the owner picks (v4-pro for quality; price
  both with a dry run). Claude logs then become history (inactive families are neither required nor failed). Cost:
  every form needs a current DeepSeek log, so the first run reviews the whole 2025 tree (about 230 transcription,
  render and class M jobs plus the sampled screen, completeness and false-no reviews). DeepSeek is cheap (its whole
  earlier review history cost $7.51), but get the dry-run figure to the owner before spending.
- (B) keep claude required and run single DeepSeek runs with `--inactive-family deepseek --inactive-family-reason`:
  does not satisfy the claude requirement, so round F still cannot commit. Not workable.
- (C) owner waives the review requirement for round F (`--no-verify`). Not recommended.
Then record the decision: amend the CLAUDE.md "Reviews are Claude-only" bullet (owner's words, date), update
`families.json`, run `test_review_tools.py` and the family self-tests, and note it in TASKS.md.
Check `samples.py` / `screen_review.py` / `completeness_review.py` / `false_no_review.py` for how they pick a family
(`--model`, `families.load(kind)`, `by_kind` overrides) before running them.

## 3. Finish round F (in order; each step's checks green before the next)

All commands from `.claude/worktrees/fr2`.
1. **Reviews.** Rebuild and render first if any form changed (`npm run compile --silent && node engine/dist/main.js
   build && node engine/dist/main.js render && node engine/dist/main.js render --ny`). Dry run, then the paid run:
   `python3 tools/transcription/rerun_all.py --kinds transcription,render,classm --model <deepseek model> --dry-run`
   then the same with `--resume --approve-cost <estimate> --summary <file>`; then `screen_review.py --model <model>
   --dry-run`, then with `--approve-cost`. The once-per-round guard skips logs that already answer their subject;
   `--force-rerun REASON` only when a rule requires it. Runs above $3.00 need `--approve-cost`. Each paid call is logged
   in `.transcription/costs.jsonl` with year and jurisdiction (automatic). Planning is slow (about 30 s per job,
   4 at a time) before any call.
2. **Adjudicate** every disagreement and finding. Read first: `tools/README.md` lines 341-460 ("Review rerun guards",
   mechanical rulings, carrying verdicts) and 578+ ("Sampled completeness, screen, false-no and question reviews");
   `docs/2026-10-24_validation_policy.md`; `tools/transcription/rule.py` and `rulings.py`; and earlier adjudications as
   models (`reviews/2025/*/adjudication/*.md`, e.g. `reviews/2025/transcription/adjudication/ira.md`; the night's
   examples are in `.claude/nightplan-2026-11-16/` reports). Each disagreement is ruled against the archived source
   text (quote it with page): model error / representation / scope / ambiguity (register entry) / true defect. A true
   defect: fix it if small and confined to the form, with a hand-predicted fixture; otherwise
   `python3 tools/new_bug.py "<title>" --pending <prefix> --field ...`. Rulings go into the sidecars the tools name;
   `python3 tools/transcription/rulings.py --check` and `check_logs.py` (us and `--jurisdiction ny`) must pass.
   Forms changed by fixes make their reviews due again (review what changed, line-scoped).
3. **Release prep:** `tools/release_prep.sh` lists every failing release gate in one pass. Known artifact: run it on a
   snapshot or after `git add -A`; in a working tree with untracked new files, `tier_paths` and `siblings` self-tests
   misreport (T-337 follow-up). Fix and re-run until it passes.
4. **One release-mode full check** from fr2:
   `CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify MUTATE_WORKERS=12 tools/check_all_bg.sh --tier full`; wait on its pid with a
   timeout (`tools/check_all_bg.sh --status`); about 75 minutes on an idle machine. A failure: fix, run the failed
   step directly, then the full check again.
5. **Commit:** `tools/commit_tested.sh -F <message file>` from fr2 (message: what landed, bug ids assigned, the review
   family change; end with a Co-Authored-By line for the model that wrote it; no session links). Run
   `python3 tools/new_bug.py --assign` before the full check if `bug_pending/` holds entries (the check verifies the
   inventory). If the claims hook refuses, see `tools/claims.py list` (a stale branch's claims may be released with
   `claims.py release`, stated in the commit message).
6. **Land and release** (owner's go-ahead first): in the main checkout, copy `research/costs/agent_runs.jsonl` aside and
   `git checkout --` it (the hook appends rows there; they block a fast-forward), `git merge --ff-only <sha>`,
   `git push origin main`, `tools/release.sh --push` (it tags without rerunning when the tree passed in release mode),
   then re-append the set-aside rows that the commit lacks and commit them with the next change.

## 4. After round F: the queue (one unit at a time)

From the owner's rulings and `post-release/RUNBOOK.md`:
1. **Round K, the K-1 integration.** Patches `.claude/nightplan-2026-11-16/nightplan/patches/v4/k1block-*.v2.patch` and
   v3 `k1int-*`; validation record `nightplan/round6/v2.md` (sections 6-7 = where to resume: 12 parked k1 coverage rows,
   tick-group placement). Owner rulings: B1 move the K-1 rosters to order 130; B2 keep partnership/S corp counted
   refused until box 14 A is wired (README wording in v2.md); B3 add a narrow per-S-corp-K-1 tick when box 17 has an
   amount ("code A or B?"; Yes refuses); B4 the three restated row ends are approved; B5 accept the tips over-refusal.
   Expect new mutation survivors and reviews (round F's pattern).
2. **Estate and trust K-1s** (`nightplan/round4/k1e.md`).
3. **Form 8615** (`nightplan/round5/f8615.md`, patches `v4/f8615-*.patch`; renumber its personas after 31). Rulings
   D1-D4: build it; clear f8615/i8615 sources for encoding (printed revisions in `nightplan/round6/owner-sources.md`);
   AMT cap reaches every section 1(g) child (widen the questions' reach); no coverage category; new under-16 text.
4. **Deferred F2 patches** (owner A4/A5): tf-b-f1 (digital got/disposed), tf-a-f4 (listed property), tf-a-f1 (gift
   tick screens) redone so every box is read (nested-choose pattern) and the gift refusal shows per screen.
5. **sa.line1 redesign** (owner C9: approved in principle; bring the formula to the owner before landing).
6. **BUG-0570b trial** (owner C5a: apply in scratch after F3, count newly refusing cases, land if acceptable).
7. **Rollover readiness before any 2026 adoption:** T-339 (year_carry section truncation), T-340 (carried logs in
   check_logs), T-342 (static checks of the applied 2026 tree), T-345 (multi-year baseline and check-all); then T-341
   (evaluator rollback; show impact by test first), T-343, T-344 (policy is the owner's), T-346.
8. **Weekly while the IRS finals post:** TASKS.md T-322, then T-320 and T-328 as each 2026 document posts.
9. **Next coverage area:** the largest refused category is Schedule 1 line 8z "other income" (4.8% of returns); it needs a
   scout before any design (coverage expansion protocol, `docs/2026-11-15_coverage_expansion_protocol.md`).

## 5. Lessons that cost hours (do not repeat)

- A check that crashes hides every later check in its run: after fixing a crash, rerun the step before estimating.
- Measure the whole gate before promising a release time: run `tools/release_prep.sh`, and `mutate` and
  `refusal_reach` to completion, on any unit before calling it release-ready.
- A change to a full-tier path (`tools/full_paths.txt`, e.g. `engine/src/mutate.ts`) cannot commit on a fast-tier
  green; plan the commit order accordingly.
- Class M and mutation fixture files take no test-data defaults: every new input must be stated there.
- Renames must cover collection-indexed keys (`f8853c[p0].pre1996`): use `tools/rename_ids.py` and `rename_carry.py`.
- A form YAML edit makes that form's review logs due; schedule the reviews with the repair.
- Tests that take "the first fixture that qualifies" break when fixtures are added; pin by id.
- Never run two full `mutate` runs at once; nice parallel lanes; cap worker counts; one full check at a time.
- Patch context written against old wording fails to apply after a rewording: carry the new wording into the patch
  context rather than guessing a merge (`.claude/nightplan-2026-11-16/deepseek/def-0791.fr2.patch` is an example);
  fixture JSON conflicts merge case by case with `.claude/nightplan-2026-11-16/deepseek/json3way.py`.
- Hand predictions of expected values come from the archived sources BEFORE running the evaluator; if the engine
  disagrees, re-derive; a wrong engine is a bug entry, never a pinned value.

## 6. Housekeeping

- Agent-run records: `research/costs/agent_runs.jsonl` rows dated 2026-11-10 or later must carry `model`, `class`,
  `year`, `jurisdiction` (`tools/check_agent_runs.py`). The Claude hook wrote them automatically; DeepSeek runs are not
  hooked, so append a row per subagent unit yourself (model `deepseek-...`, class mechanical or judgment).
- Old worktrees under `.claude/worktrees/` (xint, mw, m1116, mk1, mrental, mexist, mstruct, mint, mk1s, m1116sb, p1,
  s0, t1, v1, v2, rd-dedup, f1 and older lanes) and refs `refs/scratch/*` can be removed once round F is on `main`
  (`git worktree remove`, check each for uncommitted work first; never delete `fr2` before its commit lands).
- Records of the night of 2026-11-15/16 and day of 2026-11-16: `docs/records/2026-11-16/` (committed) and
  `.claude/nightplan-2026-11-16/` (working files, not committed: coordinator log, briefs, reports, patches).
- When Claude returns (IRS finals push): write a short state note at the top of `HANDOFF-NEXT-SESSION.md` naming what
  you landed, what is in flight, and the review family in force.
