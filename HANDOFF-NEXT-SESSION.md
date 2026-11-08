# Merge chain cleared, consolidation started — 2026-11-07/08

**State:** `main` is pushed through `63273754` (the education lane, the last of the merge chain); the full tier is green on it.
The education lane (`63273754`: BUG-0446/0454 fixed, BUG-0456 data fix, NY pins, `tools/structural_leaks.mjs`
prototype) closed the merge chain; its review data was carried back with `--prefer-worktree` for the person
completeness files. No release has been
cut since `r2026.11.06.1`.

**Landed this session:** Form 8889 decedent remedy (`d05db7e6`); the retrospective archived in
`docs/2026-11-07_process_retrospective/` (`f6607ed6`); `worktree_data.py fill` (`7744f501`) and
`carry-back --prefer-worktree` (`fb3bc7f6`); T-255 carry.py fixes and rerun_all.py guards (`1525cae5`: a $3.00
owner cost gate, once per round, line-scoped by default); main's mutation and engine differential green again
(`8969807a`, BUG-0457); the triage.py refusal for line-scoped passes (`f733797f`); gates lane C (`5dbc39d4`);
check-all concurrency (`c595f9ee`: per-run records under `.git/check-all-bg/runs/`, two machine-wide slots).

**Owner decisions (2026-11-07/08):**
- Consolidation (T-256) comes before coverage growth; federal coverage stays at 78.4% until the project stabilizes.
- The review machinery and the fixtures are fixed **before** any further gate lanes: step (a) T-255 (done), step (b)
  T-258 (sound leak check), step (c) per-form partial fixtures with test-data defaults plus a small whole-return set.
- Partial fixtures: explicit defaults written into the test data, never engine defaults. (This settles decision 1 of
  the entry below.)
- The cost gate is $3.00. The carry-over tool stays strict about reworded input questions.
- Discussion with Gemini 4 Argon continues in `docs/ARGON_CLAUDE_DISCUSSION.md` (append-only protocol); use it for
  analysis and design critique. Decisions stay with the owner.

**Next:** T-258 (brief to be reviewed with Argon first); then T-256 step (c) and phase 0
(charter, inventory, TY2026 rollover measurement); T-257 (triage reads line-scoped passes).

# Web UI, formal gates and readable questions — 2026-11-06/07

**State:** `main` is pushed through `5d8c6fd` (R4, the last restructuring lane). The UI runs from `main` at
http://127.0.0.1:8791 (`node engine/dist/main.js serve --dir ~/Documents/Tax-Interview`). No release was made this
session; the next `tools/release.sh` is the first full run of everything below (G2's merge had its own full run).

**Landed (in order):**
- T-236 web UI: the server and page (`814a1ea`); the re-layout with sources and tabs (`2c1b77b`); source titles and
  designations, verbatim and checked (`2c1b77b`, `c41851e`).
- Formal gates, owner-approved design `docs/2026-11-06_formal_gates_design.md` (standing rules: the interview only
  words, formats, orders, groups and labels; only the evaluator's reachability hides a question). G1 tooling
  (`05aa303`: interview-rule checks, `gated_by`, gate screen review, false-no review); G2 (`a061e28`: `choose` takes
  Bool and enum alternatives; full tier green). The T-251 interview-layer topic layer is superseded and stays unmerged
  on its branch (`worktree-agent-aeba046e877ced9d9`).
- Structured question text (`b66f4ea`, R0) and every question over 800 characters restructured into a question,
  headings and lists with no word lost: scope screens (R0), f5695 (R1, `42a384d`), dependent/retirement/f8962/f1095a
  (R2, `c1e852d`), sales/asset/sc and seven more (R3, `6c7d46a`), person/s1/sa/household/ny_it201 (R4). Each form's
  stale reviews were rerun and ruled: $28.67 in paid calls (ledger 746 rows), no meaning change found.
- T-254 check-all speed: interview checks lean (`14a06ba`, build 258 s to 64 s); worker pools for the fixture,
  integration and server tests (`cb5e58f`); interview-rules on worker threads (`e0a59b6`). Fast tier about 11 min
  to about 5 min.
- BUG-0437 fixed (`ce992c6`: structured text kept in review prompts' one-line listings). Bugs registered: BUG-0431
  to BUG-0439.

**Decisions waiting for the owner** (details in the commit messages and agent reports):
1. Partial fixtures and gates (blocks the G2 leak rewrite and every gate round): a nested gate turns a partial
   fixture's decided value unknown where an earlier operand is unanswered. Are partial fixtures' decided values
   authoritative (complete those fixtures first), or may gates turn them unknown? Measured on f8880/f8889: the owner's
   AGI-first order fails 7 recorded fixtures; the sequential order fails none but saves no questions. Also: extend the
   mutation tool to reason through Bool `choose` first (3 pinned arguments name `use_last_month`).
2. T-254 items 3-4 (branch `worktree-agent-a4eceeb8ee9a5f170`, commits `d4067d5`, `a5c2d9b`, `6358a7f`, held): a
   traced dependency scheduler and a step cache. Fresh fast tier not faster (tracing doubles traced steps); reruns
   190 s; docs tier 90 s vs 133 s; the final tree never ran the full tier; cache soundness rests on stated untraced
   assumptions. The same commit holds the BUG-0431 guard and `tools/worktree_data.py` (clone, carry-back), and fixes two
   real races of the old waves. Adopt, adopt in part, or drop. Its bug numbers clash and need renumbering.
3. R4 wording: two numbered household lists became bullets (the format has none); one `household.unmarried` sentence
   moved after its list. Reviews accepted both.
4. Stale optional-family logs: `check_logs` fails on a stale DeepSeek log even where it is not second-family eligible,
   forcing small reruns or archiving (R1, R3, R4). Tolerate them?
5. Content fixes registered, each adding a clause: BUG-0433 (Form 8615 examples), 0434 (f5695 lived-in home), 0435
   (SIMPLE IRA rollover), 0436 (sales.code adjustments), 0438 (s1.line8r grant), 0439 (IT-201 line 1 cite).
6. Review tooling (R2, R3): `triage.py` evaluates only the whole reply, not a line-scoped pass reply; line-scoped
   requests list other lines by id and type only, so models zero hidden lines (f8962 11e, f8960's Form 1040 line 11).

**Hazard learned:** agents in worktrees write paid-review outputs and ledger rows into their own clone of the
git-ignored `.transcription/`. Until `worktree_data.py carry-back` lands, carry them back by hand: append the ledger
rows after the clone point and copy changed files three-way against an untouched clone (a plain sync overwrote newer
files once this session; repaired).

**Next:** the owner's decisions above, then the first gate round (C gates) on the formal-gates design.

# Process packages, release gating and T-245 — 2026-11-05/06

**State:** `main` is pushed through `f2850ce`, release **`r2026.11.06.1`** (the first release, made by `tools/release.sh --push`: a full
run on `e04b741`, whose only rewritten report, a date stamp in `second_family.md`, is the release commit). The
working tree is clean apart from this handoff.

**Landed this session:**
- `ce1e69a`, T-237 and T-240:
  - wording-blind transcription subjects (`WORDING` = label, help, note, display, ambiguity; display and ambiguity added
    by the owner), with a no-call migration;
  - a scoped catalog on line-scoped prompts (lines-v2). The A/B cost $2.75: prompts were 33–40% cheaper, and the
    verdicts were identical except for one sales model-error disagreement, which became AGREE;
  - a usage-limit circuit breaker;
  - `tools/new_bug.py` and `tools/task_row.py`.
- `e2adfe6`, T-238, release-gated check-all (`docs/2026-11-05_release_gating_design.md`, owner-approved). Also BUG-0426:
  background runs had compared HEAD-relative checks with the snapshot itself.
- `90d823d`, T-241: inference-cost guidance in `CLAUDE.md`. It was the first fast-tier commit (7.5 min).
- `e04b741`, T-245 (BUG-0427):
  - a choose past an unknown guard is a refusal only when every way refuses, in both evaluators;
  - `properties --ny`;
  - the mutation rules sharpened, with 21 pinned arguments.

  An independent review found BUG-0428 (fixed) and BUG-0429 (labelled). BUG-0430 is registered open.

**Committing now (the tiers, T-238):** the hooks require the exact tree green in the tier the commit needs. The hook
names the path that decides it (`tools/tier_paths.py`).
- Code or data change: `tools/check_all_bg.sh --tier fast` (about 7.5 min), then `tools/commit_tested.sh -F <msg>`.
- Bookkeeping only (`tools/docs_paths.txt`): `--tier docs` (about 3 min).
- Full-tier triggers (`tools/full_paths.txt`: mutate*.ts, compare.ts, lean/, tools/engines/, engine_investigations):
  `--tier full` (about 40 min).
- Session end: commit and push, then `tools/release.sh --push`. If it commits rewritten reports, `git push` again.

**Owner decisions (2026-11-05):**
- T-238 design: fast commits on main; release at session end plus the path triggers; the docs tier kept at ~3 min.
- Sentinel alert (lab-server): a Safari top-hit preload from the owner's own phone. No action.
- T-245: the engine rule; survivors handled by the sharpened rule plus pins, after an independent check; the seven
  answered-only pins registered for later (T-250).
- New backlog after T-236: T-246 (file-tree and docs sweep) and T-247 (contributor strategy).

**Next:**
1. T-236, the web UI pilot. An AP-12 readback is required first. Decide T-248 (eager all/any refusals, BUG-0430),
   T-249 (BUG-0083 refusal gates) and T-250 (seven answered-only pins) at that readback: the UI will show refusals on
   incomplete returns.
2. T-239 (triage auto-rulings) can run alongside the pilot or after it.
3. Unregistered:
   - the NY case `ny.household.single.4000`, whose id and note misstate its taxable income ($32,000);
   - `new_bug.py` accepts a Fix field without Fix lines, a rule only `siblings.py --check` enforces. It should refuse
     or warn.
4. Leftover agent worktree `.claude/worktrees/agent-aaacbb6063a95164a`: its work is in `e04b741`. Removal needs the
   owner's command (the classifier blocks a forced removal).

**Cost this session:**
- paid review calls: $2.75 (the A/B);
- agents: Opus about 1.53M tokens (A 290k, T-238 272k, T-245 723k, review 245k); Sonnet 59k.

**Verified vs inferred:**
- Verified: every commit's tree was green in its tier, and each was pushed; the A/B results; the BUG-0426 probe; the
  T-245 full run (mutation 280+7 federal and 44 NY; compare 0 differing).
- Inferred: the 21 pinned arguments and the transparency reasoning in BUG-0428's fix. These are hand-reasoned. The
  review covered the arguments, but came before the transparency fix.

---

# New York integration — 2026-11-05

**State:** New York (Form IT-201, full-year New York City resident, tax year 2025) is on `main`. That includes the
cloud session's Phases 1 to 3 (branch `ny/2025-foundation` keeps its history) and the local integration
(`docs/ny/INTEGRATION.md`, last section). Paid review calls cost $11.64; there were no medium or higher findings; the
lows are BUG-0424 (T-244). Tax-year 2026 preparation is `d601762` (`docs/ty2026/ADOPTION.md`).

**Owner decisions (2026-11-04):**
- Keep the equivalence-review standard (parenthesized lines count as printed).
- New York reviews staged.
- The New York catalog is source-only, with printed-label matching.
- The GPT family becomes GPT-6.1 Sol (T-217).
- The process-optimization plan (`docs/2026-11-04_process_optimization.md`): register, then implement (T-237 to T-241).
- Package B is to be redesigned around release-gated check-all.
- Package C auto-rules identical-value disagreements, sampling 1 in 10.

**Next:** T-237 items 2, 3 and 9, then T-240, the T-238 release-gating design for the owner, and T-239; T-236 (the web UI
pilot, tax year 2025, local and single-user) before coverage expansion resumes; T-217 with Sol after that.

---

# Round 2 and the tooling batch — 2026-11-04

**State:** the tooling batch is f27d71d (T-218 carry-over, T-219 line-scoped reviews, T-220 yield, T-225, T-228 and
the P5 rows). Round 2 is the commit after it:
- the review-tool rows T-223 (ruling stamps), T-224 (mechanical model-error rulings), T-226 (BUG-0411), T-227 (foreign interfaces);
- the engine rows T-206 (class M selection on route branches) and T-213's input check (BUG-0412);
- the form pass: every BUG-0402 low (BUG-0408), T-216 (BUG-0409), T-215 (BUG-0410), the NUA refusal (BUG-0413), T-201 and T-207;
- the first real line-scoped review round on the 17 changed forms, with completeness and screens, all adjudicated.

Round 2 cost $41.12 in paid calls (90 calls); the yield report has an exact-join table from now on.

**Decisions taken under the standing instruction (Elliot can reverse):**
- T-191: the `bracket_schedule` op form stays in the frozen vocabulary.
- T-181 and T-208: left open as coverage expansion.
- Stale DeepSeek transcription logs of ineligible changed forms are archived (`.transcription/archive/stale-deepseek-transcription-2026-11-04/`), not rerun.
- `--lines auto` records a verified line-subject table for a pre-table log with no stale line, with no model call.
- Sibling-form review evidence comes from a line-scoped review of the sibling lines alone (f1040, f8863).

**Owner questions:** T-232 (`expect_shown`, a fixture-schema and spec change); whether transcription reviews should stop running on wording-only changes (round 2: $20.48 for 0 findings; completeness $6.70 for 1 medium and 12 lows).

**After the round-2 commit (T-094):** every form is now completeness-reviewed. f4952 and f8880 use their printed instructions; person is reviewed
whole, with the prompt limit raised to 700k characters. Cost $2.23; 2 more lows were added to BUG-0414's list.

**Round 3 (after the T-094 commit):**
- every BUG-0414 low is fixed (BUG-0415), and round 3's own lows are fixed too (BUG-0416);
- T-232 is done with no schema change: source-predicted gate values on class A and synthetic regression cases, plus 10 new synthetic cases, kill 138 of the 145 display-condition mutants, and a new rule (conjunctPrefix) proves 5 more equivalent;
- T-231 and T-196 were closed by cost decision;
- T-159: tier-3 mutation is the default and fully explained (adjusted 100.0%; the step takes about 22 minutes); T-235's retarget self-test guards the pinned arguments; T-234 fixed the EIC Worksheet A line 4 display; T-181 moved to coverage expansion (owner, 2026-11-04);
- the two rare sales lows (BUG-0417) and the findings of the sales reviews after them are fixed (BUG-0418); the last sales completeness review found nothing that isn't refused elsewhere.

Paid calls this round: $36.85 (70 calls).

**Next:** T-217 after 2026-11-06 15:49; the owner question on transcription for wording-only changes; coverage expansion stays last.

---

# Backlog and refresh rounds — 2026-11-03

**Owner decisions (2026-11-03):**
1. Inference cost: use inference only where it adds evidence (CLAUDE.md, "Inference cost"). Review and adjudicate only forms whose content changed; review-prompt changes apply prospectively; Sonnet for mechanical agent work; every paid call is logged in `.transcription/costs.jsonl` and every agent run in `research/costs/agent_runs.jsonl`. Tooling to build: T-218 (mechanical carry-over of repeat rulings), T-219 (line-scoped reviews), T-220 (findings per dollar), T-221 (noise comparison of the archived v3 replies).
2. The transcription catalog is a subset chosen from the IRS source (prompt policy `source-only-computation-v3`, BUG-0390), with the T-163 `shown_when` note.

**State:** commit 0a43f15 integrated eight parallel packages (BUG-0341 to BUG-0390). The refresh-round commit after it fixed T-212, T-210, T-175, T-211, T-214, T-205 and the T-101 remainder (BUG-0391 to BUG-0401), recorded the refresh lows as BUG-0402 (T-222), and reran and adjudicated the 17 changed forms only; the 45 unchanged forms keep their v2 logs, and their v3 replies are archived for T-221. GPT-6 Astra is at codex's usage limit until 2026-11-06 15:49 (T-217); its stale logs are archived in `.transcription/archive/stale-gpt-logs-2026-11-03/`.

**Next:** T-218, T-220 and T-219 (T-221 closed by the owner: the measurement would not change a decision), then T-222 and the remaining open rows; T-217 after 2026-11-06. Coverage expansion stays last.

---

# F1 and T-176 integration — 2026-11-03

**Owner decisions (2026-11-03), on the F1 owner questions:**
1. The dependency and EIC tie-breaker refusals stay when the other person is a non-taxpayer (no exception in p501 pp. 15-17; a refusal cannot give a wrong answer).
2. T-113's "or filer" means the filer who is the student; a filer with only an applied-for ITIN claiming the lifetime learning credit for a student with an issued number is not refused (i8863 Table 1).
3. T-104's question covers a child kidnapped before 2025 and still missing at some time in 2025.

**State:** T-176 (BUG-0325, fixed by BUG-0328) is on `main`. The F1 cloud batch (T-104 to T-113, T-153, T-154, T-167, T-168; BUG-0329 to BUG-0337, open BUG-0338 and BUG-0339) is integrated on this branch with its DeepSeek reviews rerun locally. Next: integrate `claude/t159-mutation` (tier 1 shipped; tier 2 still gated with 114 unexplained survivors), then T-178 to T-185 and the remaining backlog.

---

---

Older entries (2026-10-31 to 2026-11-03) are in [handoffs/HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md](handoffs/HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md).
