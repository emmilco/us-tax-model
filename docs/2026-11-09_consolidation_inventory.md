# Consolidation inventory (T-256 phase 0)

Read-only inventory of the tree at `e2252227` (2026-11-09), for the owner to decide what to consolidate, prune or
delete. Nothing was deleted, moved or changed except this file. Written by a mechanical-class agent
(claude-sonnet-5-5); no paid calls.

Method. Every number below was measured in this worktree by a command listed with it, or in the main checkout
(`/Users/elliotmilco/Documents/GitHub/tax-formalization`) for git-ignored data. Where a document is quoted, it is
quoted as testimony and the measurement is given beside it. Classifications ("current", "superseded", "looks
redundant") are this agent's reading of the evidence named, not owner decisions. Several greps used basename
matching, so a "no referrer" finding means no reference was found by that search, not proof of non-use; the search
method is stated where it matters.

Contents: 1 stray files; 2 docs and plans; 3 check-all steps; 4 tools; 5 the 11-01 audit; 6 conventions;
7 retrospective numbers re-grounded.

---

## 1. Stray files

### 1.1 Tracked files at the root or in odd places

The root holds 14 tracked files (`git ls-files | grep -v /`). Referenced by an index, README or tool:

| File | Size | References found | Reading |
|---|---:|---|---|
| `BUG_INVENTORY.md` | 661,750 B, 467 entries (`grep -c '^## BUG-'`) | PROJECT_INDEX, README, 10+ tools (`check_bug_inventory.py` enforces append-only in check-all) | Load-bearing |
| `TASKS.md`, `TASKS-DONE.md` | 18 KB; 133,050 B | tools (`task_row.py`, `tier_paths.py`, `docs_paths.txt`) | Load-bearing; TASKS-DONE is not named in PROJECT_INDEX or README |
| `years.json` | 24 B | PROJECT_INDEX (4 mentions), engine `year.ts`, `taxyear.py` | Load-bearing |
| `package.json` / `package-lock.json` | 1.5 KB / 17 KB | npm | Standard |
| `LICENSE`, `LICENSE-DATA` | | LICENSE-DATA is in PROJECT_INDEX and README | Standard |
| `experiment_log.md` | 239 lines, last commit 2026-11-02, entries dated 2026-11-01 | Only `handoffs/HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md`; no PROJECT_INDEX or README mention | The QMS experiment log; unindexed and not touched in 7 days |
| `HANDOFF-NEXT-SESSION.md` | 225 lines, 7 entries | CLAUDE.md, PROJECT_INDEX | Current. PROJECT_INDEX line 30 says it holds "the latest two entries"; it holds 7 (`grep -n '^# '`) |

Stray tracked files elsewhere (no index, README or tool reference found):

| Path | Evidence | Note |
|---|---|---|
| `tools/transcription/README.md.orig` | `grep -rl "README.md.orig"` finds nothing; differs from `README.md` (`diff -q`); added in `bdac4121` (2026-11-05, the New York commit) | A merge-conflict leftover |
| `.transcription/` (36 tracked files) and `.classm/` (15 tracked files) | `git ls-files .transcription .classm`; both directories are in `.gitignore` | Force-added raw review output (prompts and responses for `dependent`, `person`, completeness and screens, plus one archive snapshot `before-f1-dependent-reruns-2026-11-03/`, 17 files). 20.2 MB and 1.7 MB tracked (`git ls-files -z \| xargs -0 stat`). They contradict the ignore rule |
| `docs/patches/BUG-0111.patch`, `BUG-0111-check.mjs` | cited only by PROJECT_INDEX, `docs/2026-10-23_independent_validation.md`, `handoffs/HANDOFF-INTEGRITY.md` (historical documents) | A 24 KB patch artifact from 2026-10-24 |
| `docs/2026-10-30_completeness_experiment/call1.txt`, `call2.txt`, `call1.out`, `call2.out`, `sys.txt` | 827, 718, 98, 98, 2 lines; cited by the experiment's own README | Prompts and raw outputs of a one-off experiment, 2026-10-30 |
| `reports/roadmap.html`, `reports/2026/*` (11 files) | `reports/2026` is described in PROJECT_INDEX only as the rehearsal output | Generated or one-off |
| `research/audits/` (84 files), `research/ty2026/` (20), `research/premises/` (19) | `research/audits` is mentioned once in PROJECT_INDEX (`research/audits/ny/`); the other audit subdirectories are not individually indexed | Agent audit transcripts; `T152_DISPOSITIONS.md` here is the earlier item-by-item processing of the 11-01 audit |
| `tools/structural_leaks.mjs` | header: "Prototype, not part of check-all"; cited only by `docs/ARGON_CLAUDE_DISCUSSION.md` | See section 4 |

Tracked bytes by top-level directory (`git ls-files -z | xargs -0 stat -f '%z'`): sources 262 MB, reviews 115 MB,
reports 55 MB, fixtures 21 MB, `.transcription` 20 MB, rendered 3.8 MB, research 3.5 MB, forms 2.3 MB, tools
2.2 MB, docs 1.1 MB. Tracked files: 3,380 (sources 1,724; reviews 837; tools 152; research 137; rendered 112;
reports 90; forms 68).

### 1.2 Untracked or ignored clutter in the main checkout (listed, not touched)

Listing method: `find` over the main checkout, compared with `git ls-files` here (main and this worktree are both at
`e2252227`; the five key bookkeeping files are byte-identical, `cmp`). `git status` could not be run in the main
checkout from this sandbox, so ignore status of items outside `.gitignore` is inferred.

| Path (main checkout) | Size (`du`) | Status | Note |
|---|---:|---|---|
| `.transcription/` | 1.0 GB, 1,954 top-level entries | ignored | Load-bearing review data (`check_logs.py` fails if a referenced raw file is missing) |
| `.transcription/archive/` | 853 MB, 5,180 files | ignored | The snapshots, see 1.3 |
| `.classm/` | 61 MB | ignored | |
| `.engines/` | 5.9 GB (`work` 4.2 GB, `venv` 0.96 GB, `data` 0.8 GB, `ustaxes-deps` 71 MB) | ignored | External-engine environments |
| `.extraction-review/` | 233 MB; last modified 2026-10-17 | ignored | |
| `.direct-file/` | 279 MB; last modified 2026-10-24 | ignored | A clone of IRS Direct File (prior art) |
| `.human-review/` | 52 MB; last modified 2026-10-25 | ignored | Human review is optional (validation policy) |
| `node_modules/` | 39 MB | ignored | |
| `canonical/`, `engine/dist/` | 8.2 MB, 836 KB | ignored | Build output |
| `.DS_Store` | 29 files outside node_modules and worktrees | ignored | |
| `__pycache__/` | five tool directories | ignored | |
| `docs/2026-11-01_contributor_safe_gating_sketch.md` | 13,295 B | untracked, listed in `.git/info/exclude` | "Left untracked at the owner's decision: speculative architecture sketch" |
| `.claude/handoff-backup/` (8 files, from 2026-10-18), `.claude/scheduled_tasks.lock` | 52 KB | not in `.gitignore`; whether excluded elsewhere was not verified | Old handoff-hook backup |
| `.claude/worktrees/` | 239 GB by `du -sk`, 31 agent worktrees (one is this one) | untracked or excluded | The largest item by far. About 8 to 12 GB each, mostly a full `.engines` copy (7.9 GB in the one sampled), `engine` (1.9 GB) and `.transcription` (1.0 GB). `cp -cR` (APFS clones) is used to create them, so real disk use is lower than `du` reports (disk shows 13 GiB used on a 1.8 TiB volume); the figure is logical size |
| `.git/` | 6.6 GB (`check-all-worktree` 6.3 GB, objects 289 MB, `worktrees` 53 MB) | | The check-all snapshot worktree is 96% of the repository directory |
| Branches and worktrees | 50 local branches, 9 remote (`git branch`, `git branch -r`); `git worktree list` shows 33 entries (main, 31 agent worktrees, the check-all worktree), 24 marked locked | | |

### 1.3 The git-ignored snapshots of invalidated review data

The retrospective counted 91. Measured in `/Users/elliotmilco/Documents/GitHub/tax-formalization/.transcription/archive/`:

| Measure | Value | Command |
|---|---|---|
| Entries | 91 (90 directories and one file, `BUG-0111-before-line14-rebase.patch`) | `find archive -maxdepth 1 -mindepth 1 -type d \| wc -l`; `-type f` |
| Total size | 853 MB | `du -sh archive` |
| Files inside | 5,180 | `find archive -type f \| wc -l` |
| Date range by directory name | 2026-10-23 (`pro-before-flash-2026-10-23`) to 2026-11-07 (`stale-deepseek-transcription-2026-11-07-*`) | `ls archive` |
| Date range by modification time | 2026-10-24 to 2026-11-07 | `stat -f %Sm` |
| Largest | `before-catalog-refresh-2026-11-03` 73 MB; `before-p4-persondep-2026-11-03` 40 MB; `before-fix-round2-2026-10-30` 38 MB; `v3-replies-unchanged-forms-2026-11-03` 34 MB; `stage19-before-round2-2026-10-29` 32 MB | `du -sk * \| sort -rn` |
| Separate: `archive/verified-replays/` | 23 MB, 36 form directories, 2026-11-04 | `du -sh` |

One snapshot, `before-f1-dependent-reruns-2026-11-03`, is also partly tracked in git (section 1.1). Inferred
(unverified): that none of these snapshots is still read by a tool. This was not checked; `check_logs.py` and
`worktree_data.py` were not read for archive paths.

---

## 2. Docs and plans

Status key. **current**: still the working authority or reference. **superseded**: replaced in whole or part (by what).
**historical**: a record of finished work. "Cited by" lists referrers other than the retrospective, `BUG_INVENTORY.md`,
`TASKS-DONE.md`, `reviews/`, `research/` and the handoff archive (basename grep over tracked text files; ambiguous
basenames such as `README.md` were not counted).

### 2.1 Top-level Markdown

| File | Date (first / last commit) | Subject | Status |
|---|---|---|---|
| `CLAUDE.md` | 10-21 / 11-08 | Project guidance, cost rules, worktree and wait rules | current. Its first paragraph names `HANDOFF-INTEGRITY.md`, `HANDOFF-STAGE-16.md` and `HANDOFF.md` as "historical" without the `handoffs/` path |
| `README.md` | 10-22 / 11-07 | Product description, prior art (512 lines, 35,816 B) | current |
| `PROJECT_INDEX.md` | 10-13 / 11-08 | Folder index (138 lines, 47,511 B) | current, but its opening paragraph names the 11-01 backlog plan as the "current execution order" (see 2.2) |
| `TASKS.md` | 10-17 / 11-09 | Task register (55 lines). Header line 3 also names the backlog plan and "Coverage expansion is last" | current; header stale |
| `TASKS-DONE.md` | 10-31 / 11-06 | Closed tasks (234 lines, 133 KB) | historical, appended |
| `BUG_INVENTORY.md` | 10-16 / 11-08 | Append-only defect record | current |
| `HANDOFF-NEXT-SESSION.md` | 10-26 / 11-08 | Continuation entrypoint; top entry "Merge chain cleared, consolidation started" | current |
| `experiment_log.md` | 11-01 / 11-02 | QMS empirical log, one household-closure episode | historical |

### 2.2 `docs/`

| File | Date | Subject (one line) | Status | Cited by (live) |
|---|---|---|---|---|
| `2026-10-22_integrity_plan.md` | 10-22 / 10-26 | Integrity plan v7, two stacked owner amendments (399 lines) | partly superseded: validation policy (10-24) and plan revision (10-26) amend it | PROJECT_INDEX, spec.md, ambiguities/2025.yaml, plan revision, root-cause analysis |
| `2026-10-22_project_evaluation.md` | 10-22 | Outside-eye evaluation that led to the integrity plan | historical | integrity plan |
| `2026-10-23_independent_validation.md` | 10-24 | Independent validation continuation; opens "Superseding owner amendment ... Historical run record, superseded" | superseded by the validation policy | integrity plan, root-cause analysis, HANDOFF-INTEGRITY |
| `2026-10-24_validation_policy.md` | 10-24 / 11-02 | Owner amendment: human packets and ruling samples optional | **current** (CLAUDE.md names it controlling) | CLAUDE.md, PROJECT_INDEX, TRUST, 8 more |
| `2026-10-26_plan_revision.md` | 10-26 / 11-01 | Plan revision after the tooling treadmill | partly superseded: execution order superseded by the backlog plan on 11-01 (retrospective 02 section 2.5) | PROJECT_INDEX, integrity plan, 8 handoffs |
| `2026-10-29_bug_root_cause_analysis.md` | 10-30 | Root causes of BUG-0001 to 0210; status line "Mostly fixed with mechanical guards" | historical reference (its findings were implemented as T-084 to T-090) | PROJECT_INDEX, README, TRUST, pressure test, HARDENING-1 |
| `2026-10-30_completeness_experiment/` (6 files) | 10-30 | The completeness-review experiment, prompts, outputs and adjudication | historical | its own README; PROJECT_INDEX |
| `2026-10-30_mitigation_strategy_pressure_test.md` | 10-30 | Ranked mitigations for value-changing bugs | historical (ranks 1 to 6 and 9 implemented by 10-31 per the retrospective) | PROJECT_INDEX, TRUST, HARDENING-1 |
| `2026-11-01_backlog_plan.md` | 11-01 / 11-04 | "Temporary backlog plan", packages P0 to P6, coverage expansion last. Banner: "Status: active ... Delete this document when the retirement checklist below is satisfied" | **stale** (retrospective: stale since about 11-04, never retired). Still cited | PROJECT_INDEX (line 3), TASKS.md (line 3), plan revision, HANDOFF-HOUSEHOLD-CLOSE |
| `2026-11-01_tech_debt_audit.md` | 11-01 | Model-written audit, 37 findings. Banner: "Every finding below needs to be verified" | historical testimony. Section 5 re-checks it. Already processed once as T-152 (`research/audits/p4-docs/T152_DISPOSITIONS.md`, rows T-188 to T-204) | HARDENING-1, HANDOFF-INTEGRITY, HANDOFF-STAGE-16, HANDOFF (no live non-historical citer) |
| `2026-11-04_process_optimization.md` | 11-05 | Cost and process opportunities | current in effect (its cost rules are in CLAUDE.md); some proposals unbuilt | HANDOFF-NEXT-SESSION, PROJECT_INDEX, TASKS |
| `2026-11-05_release_gating_design.md` | 11-05 | Fast, docs and full tiers; approved | current (implemented) | HANDOFF-NEXT-SESSION |
| `2026-11-06_formal_gates_design.md` | 11-06 / 11-07 | Formal gates (`gated_by`); approved | current, in progress | HANDOFF-NEXT-SESSION, PROJECT_INDEX, TASKS, schema, `gate_frequencies-2025.yaml`, tools/transcription/README, Argon discussion |
| `2026-11-06_question_structure_design.md` | 11-06 | T-251 question structure; banner "Built on the T-236 branch, merged with T-236" | partly superseded: the retrospective (01 and 03) says the topic layer was dropped for formal gates; no "topic" occurs in `engine/src`, `ui/` or `interview/questions-2025.yaml` (`grep -rli topic`). The banner was not updated | none (one retrospective mention) |
| `2026-11-06_web_ui_design.md` | 11-06 | T-236 web UI pilot; approved | current (`ui/` has 5 tracked files) | PROJECT_INDEX |
| `2026-11-07_process_retrospective/` (5 files, 1,531 lines) | 11-07 | The retrospective; 00 is the synthesis | current reference (the basis of T-256) | `00_synthesis.md` is cited by the Argon discussion |
| `ARGON_CLAUDE_DISCUSSION.md` | 11-08 / 11-09 | Append-only agent-to-agent discussion protocol (974 lines, 105 KB) | current, living | HANDOFF-NEXT-SESSION |
| `COVERAGE.md` | 10-31 / 11-08 | Generated coverage reference (174,361 B) | current, generated; `coverage_tree --check` keeps it current | PROJECT_INDEX, README, spec, `check_all_steps.sh`, `tools/coverage/` |
| `TRUST.md` | 10-31 / 11-05 | Checks in detail (215 lines) | current | PROJECT_INDEX, README, both cloud briefs |
| `ny/2026-11-04_ny_cloud_brief.md` | 11-05 | Brief for the cloud New York work | historical (executed) | NY docs, IT-201 form file, spec |
| `ny/DECISIONS.md` | 11-05 | Owner decisions, batch 1 ("Decided 2026-11-04") | current reference (cited by engine `year.ts`, `lean/Main.lean`, 20+ NY data files) | many |
| `ny/INTEGRATION.md` | 11-05 | Phase 4 integration notes | historical | HANDOFF-NEXT-SESSION, NY docs |
| `ny/LOG.md` | 11-05 / 11-06 | NY work log | historical | PROJECT_INDEX |
| `ty2026/2026-11-04_ty2026_cloud_brief.md` | 11-04 | Brief for the TY2026 preparation | historical | ADOPTION, LOG |
| `ty2026/ADOPTION.md` | 11-04 | TY2026 adoption plan, T-011 | current plan, waits on final IRS 2026 documents | HANDOFF-NEXT-SESSION, TASKS, HARDENING-1 |
| `ty2026/LOG.md` | 11-04 | TY2026 preparation log | historical | PROJECT_INDEX |
| `patches/BUG-0111.patch`, `BUG-0111-check.mjs` | 10-24 | Patch artifact | historical | historical docs only |
| `2026-11-01_contributor_safe_gating_sketch.md` | untracked (main only), 11-01 | Speculative sketch the owner left untracked | not part of the tree | |

Flagged stale plans and what still cites them: the 11-01 backlog plan is the only document the retrospective calls
stale. It is cited by PROJECT_INDEX line 3, TASKS.md line 3, `docs/2026-10-26_plan_revision.md` and
`handoffs/HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md`, so deleting it leaves dangling live references in the two files a
fresh session reads first. Its own banner says it should be deleted when its retirement checklist is satisfied; the
retrospective (02, section 2.7) reports that checklist as entirely unchecked. The plan revision and the integrity plan
are also layered with supersession text; `grep -o -i supersed` over the planning-layer files gives 35 occurrences
(the retrospective counted 32).

### 2.3 `handoffs/`

CLAUDE.md names `HARDENING-1` as the live standing-decisions file and everything else in `handoffs/` as historical.

| File | Date (first / last) | Subject | Status |
|---|---|---|---|
| `HANDOFF-HARDENING-1.md` | 10-31 / 11-04 | Owner's standing decisions and operational facts (93 lines) | **current** (CLAUDE.md) |
| `HANDOFF-HOUSEHOLD-CLOSE-2026-11-01.md` | 11-01 | Household closure and usage pause (167 lines) | historical; cited by the backlog plan and the experiment log |
| `HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md` | 11-04 | Entries moved out of the root handoff (802 lines, 22 entries) | historical |
| `HANDOFF-INTEGRITY.md` | 10-22 / 11-04 | Integrity plan state, 574 lines, stacked sections | historical (superseded by the validation policy and plan revision) |
| `HANDOFF-T091.md` | 10-31 | T-091 done, next T-092 | historical; no citer found |
| `HANDOFF.md` | 10-13 / 11-04 | Stage 0 starter prompt | historical |
| `HANDOFF-STAGE-2.md` | 10-16 | Stage 2 | historical |
| `HANDOFF-STAGE-7.md` | 10-17 | Stage 7, the integrity stack | historical |
| `HANDOFF-STAGE-8.md` | 10-17 | Stage 8, extraction as evidence, commit guard | historical |
| `HANDOFF-STAGE-9.md` | 10-17 | Stage 9, earned income credit | historical |
| `HANDOFF-STAGE-10.md` | 10-18 | Stage 10, retirement income | historical |
| `HANDOFF-STAGE-11.md` | 10-18 | Stage 11, unemployment and Schedule 1 adjustments | historical |
| `HANDOFF-STAGE-12.md` | 10-18 | Stage 12, Schedule 1-A | historical |
| `HANDOFF-STAGE-13.md` | 10-19 | Stage 13, married filing jointly | historical |
| `HANDOFF-STAGE-14.md` | 10-19 | Stage 14, self-employment (316 lines) | historical |
| `HANDOFF-STAGE-15.md` | 10-22 | Stage 15, other credits | historical |
| `HANDOFF-STAGE-16.md` | 10-22 / 11-04 | Stage 16, Schedule 1 items (253 lines) | historical |
| `HANDOFF-STAGE-18.md` | 10-29 | Stage 18, premium tax credit | historical |
| `HANDOFF-STAGE-19.md` | 10-29 | Stage 19, education credits | historical |
| `HANDOFF-STAGE-20.md` | 10-27 | Stage 20, capital loss carryover | historical |
| `HANDOFF-STAGE-21.md` | 10-29 / 10-30 | Stage 21, Form 5329 | historical |

All stage handoffs except the three called out in CLAUDE.md are cited only by PROJECT_INDEX and by each other. The 19
historical handoffs plus the archive and household-closure files total 3,598 lines; all 21 files in `handoffs/` total 3,691 lines
(`cat handoffs/*.md | wc -l`).

---

## 3. Check-all steps

Source: `tools/check_all_steps.sh` (216 lines). Counted by parsing the script and cross-checked against the step
headers of a green full-tier log (`.git/check-all-bg/runs/734b2552...-20261108-143913/log`: 94 `== name` headers).

| Tier | Steps | How selected |
|---|---:|---|
| full | **94** (92 `^step` lines; `human_review` is defined on two conditional lines, `build` on two branches) | every step |
| fast | 89 | full minus `slow_steps`: `mutate`, `engine_differential`, `compare`, `ny_compare`, `ny_mutate` |
| docs | 8 | `compile`, `build`, `check_bug_inventory`, `siblings_check`, `siblings_self_test`, `bookkeeping_tools`, `coverage_tree`, `green_self_test` |

Step list by wave (the order the script runs them; the steps of a wave run in parallel):

- **Wave 0 (1):** `compile`.
- **Wave 1 (2):** `build` (build, render, `render --ny`; in the docs tier build only), `check_self_test`.
- **Wave 2 (67):**
  - Fetch and extraction: `fetch_sources`, `check_extraction`, `check_macrs_tables`, `check_ptc_tables`,
    `check_auto_limits`, `check_source_titles`, `check_bug_inventory`, `adapter_contracts`, `classm_skipped`,
    `compare_families`, `check_logs`, `check_table_logs`, `citations`, `gate_frequencies`.
  - Source-coverage checks: `instruction_cites`, `operands`, `signs`, `screen_currency`, `false_no_currency`,
    `consumers`, `limits`, `completeness`, `siblings_check`.
  - Tool self-tests (29, among the 34 listed in 3.1).
  - New York (15): `ny_fetch_sources`, `ny_check_extraction`, `ny_citations`, `ny_instruction_cites`,
    `ny_operands`, `ny_signs`, `ny_consumers`, `ny_limits`, `ny_tax_table`, `ny_predict_self_test`,
    `ny_review_tools`, `ny_check_logs`, `ny_completeness`, `ny_screen_currency`, `ny_false_no_currency`.
- **Wave 3 (17):** `conjecture`, `test_fixtures`, `refusal_reach`, `interview_rules`, `test_integration`,
  `test_serve`, `human_review` (fast and docs tiers only), `classm_job_seeds`, `coverage`, `coverage_tree`,
  `properties`, `differential`, `engine_differential`, `mutate`, `compare`, `ny_test_fixtures`, `ny_properties`.
- **Wave 4 (8):** `evidence`, `review_stage2`, `review_stage3`, `review_stage4`, `review_stage5`, `human_review`
  (full tier only), `ny_compare`, `ny_mutate`.

### 3.1 Classification

| Class | Count | Members |
|---|---:|---|
| Tool self-tests and tool test suites | 34 | `check_self_test`, `interview_rules_self_test`, `fetch_sources_self_test`, `archive_text_self_test`, `check_extraction_self_test`, `check_macrs_tables_self_test`, `check_auto_limits_self_test`, `check_source_titles_self_test`, `review_tools`, `input_context`, `rerun_all_tools`, `bookkeeping_tools`, `pre_push_self_test`, `green_self_test`, `worktree_data_self_test`, `check_slot_self_test`, `check_bg_self_test`, `consistency_checks`, `siblings_self_test`, `citations_self_test`, `year_diff_self_test`, `fixtures_year_self_test`, `engine_compare_tests`, `coverage_tree_self_test`, `instruction_cites_self_test`, `operands_self_test`, `signs_self_test`, `consumers_self_test`, `limits_self_test`, `completeness_self_test`, `ny_predict_self_test`, `ny_review_tools`, `human_review`, `classm_job_seeds`. (Classified by `--self-test`, `check-self-test`, `unittest` or a `test_*.py/.mjs/.sh` command. Adding the three engine test commands, `test_fixtures`, `test_integration`, `test_serve`, gives 37.) |
| New York steps (`ny_` prefix) | 19 | 16 mirror a federal step run with `--jurisdiction ny` or `--ny` (`ny_fetch_sources`, `ny_check_extraction`, `ny_citations`, `ny_instruction_cites`, `ny_operands`, `ny_signs`, `ny_consumers`, `ny_limits`, `ny_check_logs`, `ny_completeness`, `ny_screen_currency`, `ny_false_no_currency`, `ny_test_fixtures`, `ny_properties`, `ny_compare`, `ny_mutate`); 3 are New York only (`ny_tax_table`, `ny_predict_self_test`, `ny_review_tools`) |
| Other checks, builds and product tests | 41 | the remainder |

14 steps are a tool plus a separate `_self_test` step of the same tool (for example `citations` and `citations_self_test`;
counted as names `X` and `X_self_test` both present). The tier selector is step-name based, so a self-test runs
whether or not its tool changed.

### 3.2 Steps that look redundant or low-yield (this agent's reading; each needs an owner decision)

| Step(s) | Why it looks redundant or heavy | Evidence |
|---|---|---|
| `review_stage2` to `review_stage5` | Regenerate frozen Stage 2 to 5 prose packets on every run; Stage-named residue | `engine/src/fixtures.ts:478-572`, `main.ts:45-52`; output `reviews/2025/stage{2..5}.md`; 1 to 2 s each |
| `human_review` | Tests the human-review tooling (11 files, 2,283 lines); human packets became optional on 2026-10-24 and only 3 human logs exist (`ls reviews/2025/human`: `f1040.md`, `person.md`, `sa.md`) | 119 to 217 s in recorded runs |
| 16 `ny_` mirrors | Each repeats a federal check for the second jurisdiction | section 3.1 |
| 34 tool self-tests | Run on every commit of their tier regardless of whether the tool changed; most take under 3 s, a few dominate | see timings below |
| `coverage`, `coverage_tree`, `coverage_tree_self_test` | Three steps around one subsystem | `coverage_tree` is also in the docs tier |
| `compare` and `ny_compare` | Both run the Lean comparison; `compare` runs every fixture case plus 200 generated cases with one `taxeval` process per case (`engine/src/compare.ts:165,176`) | 309 to 639 s |
| `check_extraction` and `ny_check_extraction` | PDFKit check needs macOS and `swift`; 53 to 178 s | `tools/check_extraction.py:36` |

Not redundant by name: `differential` (internal class C records) versus `engine_differential` (external engines).
Two tests exist that no step runs (section 4): `tools/transcription/test_review_yield.py` and
`tools/human_review/test_browser.mjs` / `ui/test_browser.mjs`.

### 3.3 Timings

`.git/check-all-bg/runs/` does not record per-step timings: each run directory holds `log`, `pid`, `status` and
`tree` only (`ls`). Timings are written per worktree to `check-all-times` in each worktree's gitdir; the main
checkout's own file (`.git/check-all-times`, 60 lines, 2026-11-02) predates the New York steps. The latest records
found are from 2026-11-07, in `.git/worktrees/<agent>/check-all-times`, so they pre-date the 2026-11-08 changes.
They are sums of per-step wall seconds under parallel load from many agents, not run wall time.

| Record | Tier | Steps recorded | Largest steps (seconds) |
|---|---|---:|---|
| `agent-ae9781e05658ccd40`, 11-07 22:40 | full | 84 | mutate 3,439; engine_differential 979; compare 627; check_logs 310; review_tools 208; compare_families 207; check_extraction 171; properties 149; build 129; test_serve 126; test_fixtures 110; coverage 96; test_integration 95; classm_job_seeds 83 |
| `agent-a7ecb56289bb92900`, 11-07 20:39 | full | 86 | mutate 5,253; engine_differential 1,098; compare 639; check_logs 323; review_tools 279; properties 195; test_serve 191 |
| `agent-a5e08fb94b711fa89`, 11-07 21:00 | fast (no slow steps) | 87 | check_logs 349; compare_families 228; review_tools 226; human_review 217; check_extraction 178; build 150; properties 138; test_serve 127; test_fixtures 115; test_integration 103 |

In the fast-tier record, 4 steps account for 1,020 of 2,737 summed seconds (check_logs, compare_families,
review_tools, human_review), and 47 of 87 steps took 2 s or less. The 2026-11-09 docs-tier run for this file is
reported in the commit hand-back, not here.

---

## 4. `tools/` scripts

Counts (tracked, `git ls-files tools`): 152 files in all. Scripts: **125**.

| Language | Files | Lines |
|---|---:|---:|
| Python | 96 | 30,406 |
| Node `.mjs` | 14 | |
| Shell `.sh` | 12 | |
| Swift | 1 | |
| Extensionless hooks (`tools/hooks/pre-commit`, `pre-push`) | 2 | |
| **All scripts** | **125** | **32,964** (`wc -l` over the 125) |

By directory (all tracked files): `transcription/` 58, top level 54, `engines/` 13, `human_review/` 11, `coverage/` 7,
`hooks/` 5, `extraction/` 4. The remaining 27 non-script files are JSON catalogs and baselines (16), Markdown (6),
text (4) and `README.md.orig` (1).

### 4.1 Who invokes what

Method: for each of the 125 scripts, a regex search of the tracked tool, engine, UI, `package.json` and Lean sources
for its path or basename (including `./x` and `../x` forms) and, for Python, `import x` / `from x import`. A script
counts as reached if it is referenced from `tools/check_all_steps.sh`, `tools/check_all.sh`, `package.json`, the
hooks, or `engine/src`, directly or through other referenced scripts (transitive closure).

| Category | Count |
|---|---:|
| Invoked directly by `check_all_steps.sh` | 48 |
| Reached from check-all (steps, `check_all.sh` and `engine/src`), directly or by import | 119 |
| Reached from check-all, `package.json`, hooks or `engine/src` | 120 |
| **Not reached by any code path** | **5** |

Not reached by any code path (no referrer found in tool, engine or UI code):

| Script | Lines | What it is | Documentation mention |
|---|---:|---|---|
| `tools/engines/ny_policyengine.py` | 126 | Class C differential for New York against PolicyEngine-US | PROJECT_INDEX line 53 only; `run.sh` does not call it |
| `tools/extract_macrs_tables.py` | 143 | Extracts the MACRS tables from Pub. 946; `check_macrs_tables.py` verifies the result | PROJECT_INDEX, HANDOFF-STAGE-14 |
| `tools/extract_tax_table.py` | 233 | Extracts the Tax Table from the PDF | PROJECT_INDEX, NY brief |
| `tools/structural_leaks.mjs` | 255 | Prototype leak check, header: "not part of check-all" | Argon discussion only |
| `tools/transcription/migrate_completeness_debt.py` | 46 | "Explicit one-time migration from an independently built historical checkout" | `tools/README.md`, HANDOFF-HOUSEHOLD-CLOSE |

Reached only from documentation or manual use, not check-all: also `tools/human_review/test_browser.mjs` (162 lines;
referenced by its README and `ui/test_browser.mjs`; 119 reached the closure without it). Reached only through a
test file or a single other tool, and candidates for the one-off category: `tools/transcription/migrate_line_subjects.py`
(223 lines; its README and `test_review_tools.py`), `tools/ocr_audit.py` (136 lines; `archive_text.py` only),
`tools/transcription/completeness_debt.py` (47 lines; used by the migration above and `check_completeness.py`).

Tests that no check-all step runs (3 of 16 `test_*` files): `tools/transcription/test_review_yield.py` (71 lines; only `tools/tier_paths.py`
mentions it) and `tools/human_review/test_browser.mjs`. `tools/structured_text.py` (71 lines) has 8 code referrers and
no documentation mention (the retrospective suspected it was unreferenced; it is not).

Documentation coverage: 7 scripts have no mention in PROJECT_INDEX, README, `docs/`, `handoffs/`, `spec/` or the
tools READMEs: `structured_text.py`, `test_bookkeeping_tools.py`, `test_consistency_checks.mjs`,
`transcription/review_yield.py`, `transcription/test_classm_jobs.mjs`, `transcription/test_ny_review.py`,
`transcription/test_review_yield.py`. All but `test_review_yield.py` are run by check-all or imported.

### 4.2 Python reimplementations of evaluator or renderer logic (still present)

| Class | Location | Lines in file | Note |
|---|---|---:|---|
| `UnroundedModel` | `tools/engines/compare.py:311` (file 1,004 lines) | | A Python evaluator over canonical JSON using `Fraction`; the audit also says it reads the TypeScript evaluator's derivation notes by regex (`taken: `, `band over`), which was not re-checked |
| `Reading` | `tools/human_review/reading.py:236` (file 597 lines) | | Second AST-to-English renderer next to `engine/src/render.ts` (377 lines) |
| `Expander` | `tools/transcription/transcribe.py:1271` (file 2,453 lines) | | AST normalizer and helper inliner |
| `resolve` | `tools/fixtures_year.py:87` | | Parameter-relative input resolution, parallel to `engine/src/fixture-inputs.ts` |

Related: 20 tool files load `manifest.json` (`grep -rln manifest.json tools`), and `bbox-layout` is parsed in 4 files
(`extract_text.py`, `extract_eic_table.py`, `extract_tax_table.py`, `human_review/pages.py`).

---

## 5. The 11-01 tech-debt audit, item by item

Re-checked against `e2252227`. The audit is model-written testimony of 2026-11-01; its banner asks that every
finding be verified. It was first processed as T-152 (done 2026-11-03; dispositions in
`research/audits/p4-docs/T152_DISPOSITIONS.md`; follow-up rows T-188 to T-204 in TASKS-DONE.md). Status codes: **H**
still holds; **F** fixed; **P** partly.

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1.1 | Both evaluators memoize cross-document references under aliased caller keys | **F** | `engine/src/eval.ts:196-203` deletes the in-progress key and returns without caching under the caller key; `Eval.lean:379-387` skips the alias. Commit `05ede53c` (11-01), BUG-0287 |
| 1.2 | `(screen)` missing from render's helper markers; 20 lines misrendered | **F** | `HELPER_MARKERS` now in `engine/src/util.ts:24` including `(screen)`; `grep -c '^### column (screen)' rendered/2025/*.md` finds none. Commit `10c590d3` (11-01) |
| 1.3 | 22 of 38 steps drop `"$@"` (`--year`) | **P** | The source-coverage checks now pass `"$@"`. Still 22 of 92 `step` lines omit it, now self-tests, `compile`, `check_bug_inventory`, `siblings`, `bookkeeping`, `green`, `pre_push`, `check_slot`, `check_bg`, `worktree_data`, `fixtures_year_self_test`, `consistency_checks`, `engine_compare_tests` and the two NY test steps. Whether each is year-independent was not checked |
| 1.4 | Operand mutator skips `multiply_rate.rate`, `prorate.whole`, `percent_floor.whole`, `table_lookup.key/status`, `choose`, `test` | **F** | `engine/src/mutate.ts:55-125` (`collectOperandSites`, `testSites`) covers each. Commit `338a62f8` (11-01, T-156) |
| 1.5 | `differentialClassC` reads every `.json` unfiltered | **F** | `engine/src/differential.ts:98-107` `calculatorRecords()` filters; `differentialClassC` uses it. Commit `05ede53c` |
| 1.6a | `pre-push` checks only the tip commit | **F** | `tools/hooks/pre-push:32-45` walks `git rev-list remote..local` and checks each commit. Commit `05ede53c` |
| 1.6b | `record_green` has no lock | **F** | `tools/green.sh:42-48` uses a `mkdir` lock with a timeout. Commit `05ede53c` |
| 1.6c | `check_all_bg.sh` creates a dangling commit per run | **H** | `tools/check_all_bg.sh:191` `git commit-tree "$tree" -p "$base" -m "check-all snapshot"` |
| 1.7 | `archive_text.py` self-test bypassed by `extract_ptc_tables.py` | **F** | `archive_text.py` now has `BINDS_ARCHIVE` (names bound to `sources`); `python3 tools/archive_text.py --self-test` reports "0 direct read(s)" |
| 2.1 | Five divergent helper-marker definitions | **P** | One shared `isHelperLine` / `HELPER_MARKERS` in `util.ts:24-28` (commit `f27d71d9`, 11-04), used by `check.ts` and `classm.ts`. Still: `mutate.ts:429,771` compares `=== "(helper)"` only; `util.ts:36` `isMarkedLine` is a deliberate second predicate |
| 2.2 | Six AST walkers in `engine/src` (plus seven in `tools/*.py`) | **P** | Walker functions now: `classm.ts:50 walk`, `gates.ts:15 refsOf`, `mutate.ts:347 operandRefs`, `mutate.ts:2287 operandRefsLocal`, `check.ts` and `build.ts` (not re-counted exhaustively). Python copies: 7 files named in the audit were not re-counted |
| 2.3 | Five copy-pasted `templateKey` regexes | **P** | `templateKey` is imported from `branches.ts` by `classm.ts`, `fixtures.ts`, `interview-check.ts`, `interview.ts`, `serve.ts`. One independent regex remains at `properties.ts:405` |
| 2.4 | `year.ts` mutates `process.argv` and binds a global `YEAR` | **H** | `engine/src/year.ts:17-33,40-46` (`splice`, `export const YEAR = resolveYear()`); `mutate-worker.ts:6-7` still pushes `--year`/`--ny` |
| 2.5 | `PRIMITIVE_OPS` duplicate; dead `bracket_schedule`/`opaque` | **P** | `PRIMITIVE_OPS` is gone. `bracket_schedule` and `opaque` remain in `atoms.ts` `VOCABULARY` (lines 20, 26), `types.ts:44,48,117` and `mutate.ts`; the schema still lists `opaque` |
| 2.6 | `generate.ts` exclusion sets and four post-processors; second LCG in `compare.ts` | **H** | `generate.ts:92-135` (`NOT_DRAWN`, `UNDRAWN`, `MODELLED`, `EARLY_ROOTS`, `FIXED`); `putCarryovers/putPtc/putEdu/putEarly` at 730-733. `compare.ts:33-60` still has its own LCG (seed 20261014); the hardcoded deduction amounts are gone (read from `sa.standard_base`) |
| 2.7 | About 400 lines of form-specific provers in `mutate.ts` | **H** | `EQUIVALENT_IF` at `mutate.ts:1731`, `s1aStepSkip` and `prorateSkip` and `vehicle2019` entries at 1808-1942; `mutate.ts` is now 2,571 lines (was 2,557 at the retrospective); 55 `pinned(` entries |
| 2.8 | Stage 1 to 5 scaffolding in build, interview and fixtures code | **P** | Profile filenames are no longer hardcoded in `build.ts`; `loadInterview` still accepts `social-security, sales, stage4, full, ny` (`interview.ts`); `interview-check.ts:16` reads `stage2.json` and `checkSalesInterview` defaults to `stage3`; `fixtures.ts:24` `stage1.json`; `review_stage2..5` still in check-all |
| 3.1 | Lean evaluator over raw `Lean.Json` with silent `.getD` | **H** | 51 `.getD 0` / `.getD ""` uses in `Eval.lean` (`grep -c`); `Cmd` is an inductive but lines and values are `Json` |
| 3.2 | `Eval.lean` does not call most of `Atoms` | **F** | `Eval.lean` calls `sumList`, `subtract`, `subtractFloor0`, `smallerOfList`, `largerOfList`, `multiplyCount`, `prorate`, `percentFloor` (lines 510-631) |
| 3.3a | `rfl` tautologies in `EvalProps.lean` | **H** | `EvalProps.lean:22-31` still `⟨_, rfl⟩` / `rfl`; the file header now says "their force comes from the definition being accepted as total" |
| 3.3b | Missing monotonicity lemmas (`tableLookup`, `prorate`, `percentFloor`, `multiplyRate` rate) | **F** | `Lemmas.lean` has `tableBand_mono` (749), `prorate_mono_*` and `_antitone_whole` (339-652), `percentFloor_mono_part` / `_antitone_whole` (542, 669), `multiplyRateHalfUp_mono_rate` (276) |
| 3.4a | Divergence D6 | **H** (documented) | `spec/spec.md:272` states D6 and says the 2025 data has no such operand; `spec.md:294` calls D6 "unreachable on the 2025 data but not forbidden by the checker" |
| 3.4b | One `taxeval` process per case | **H** | `engine/src/compare.ts:134,176` `spawnSync` per case, in the loop over `[...fixtureCases(), ...generatedCases(data, 200)]` |
| 4.1 | Python reimplementations | **H** | section 4.2 |
| 4.2 | `taxyear.py` mutates `sys.argv`; 8 manifest loaders; 7 AST copies; 4 `bbox` parsers; 8 markdown parsers; duplicate `.mjs` harnesses | **H** (counts changed) | `taxyear.py:6-20` mutates `sys.argv`; 20 tool files load `manifest.json`; 4 files parse `bbox-layout`; `model_candidate.mjs`, `candidate_runtime.mjs`, `check_adapters.mjs`, `check_input_contracts.mjs` all exist. Sentence splitting is now centralized (`citations.split_sentences`, used by `check_limits.py:27` and `year_diff.py:90`), which fixes the `re.split` item |
| 4.3 | Hardcoded 2025 assumptions and a personal username | **P** | Now keyed by year with a failing message for other years: `check_instruction_cites.py:44` `PARTS = {2025: ...}`, `extract_tax_table.py:36` `taxyear.for_year`, `extract_ptc_tables.py:45` `LAYOUT`. Still: `ustaxes_adapter.py:414` `165_000`/`80_000`; `completeness_review.py:43` "2025 IRS" (open as T-230); `transcribe.py:1610` default account `"elliotmilco"` (now overridable by `DEEPSEEK_KEYCHAIN_ACCOUNT`) |
| 4.4a | `citations.py` raw YAML splicer | **H** | `tools/citations.py:1203,1235` `_scalar_offsets`, `_rewrite` |
| 4.4b | `check_auto_limits.py` hyphen-fragment search | **H** | `check_auto_limits.py:33` `"tomobiles (Including Trucks and Vans) Acquired Af-"` |
| 4.4c | `transcribe.py` slices `spec.md` by heading | **H** | `transcribe.py:1042` `spec.index("### 4.1 Values and types")` |
| 4.4d | `re.split` sentence breaks on `Pub.`, `U.S.` | **F** | section above, 4.2 row |
| 4.4e | macOS-only: `cp -cR`; Swift recompiled per PDF | **P** | `check_all_bg.sh:106,114,117` still `cp -cR`. `check_extraction.py:89` `pdfkit_skip_reason` now skips PDFKit off macOS or without `swift` (T-097) |
| 4.4f | On-the-fly TS transpilation for UsTaxes | **H** (not re-read) | `tools/engines/ustaxes/hooks.mjs`, `run.mjs` exist |
| 4.5 | Over 4,300 lines of tools with no self-tests | **P** | `tools/engines/test_compare.py` exists (step `engine_compare_tests`); `ustaxes_adapter.py` has self-test text. `ots_adapter.py` (785), `generate_cases.py` (724), `run_engines.py` (615), `extract_text.py` (380), `extract_tax_table.py` (233), `extract_eic_table.py` (197), `extract_class_lives.py` (181), `extract_ptc_tables.py` (167), `extract_macrs_tables.py` (143) contain no `self-test` string; the table extractors are covered by `--check` steps instead (`check_ptc_tables`, `check_macrs_tables`, `ny_tax_table`) |
| 5.1a | `person.yaml` is a god object (4,667 lines) | **H** | `wc -l forms/2025/person.yaml` = 4,948; `dependent.yaml` 2,592 |
| 5.1b | About 600 lines of Form 8863 Part III duplicated | **H** | `person.edu*`: 48 ids in 997 lines; `dependent.edu*`: 38 ids in 821 lines; after prefix normalization the line similarity is 0.83 (`difflib.SequenceMatcher`). Block starts at `person.yaml:3487` and `dependent.yaml:1773` |
| 5.2a | 12-month unrolled boilerplate | **H** | `f8962.yaml` 2,821 lines, 18 `show_jan`/`show_dec` ids; `f1095a.yaml` 1,158 lines |
| 5.2b | `smaller_of` / `larger_of` binary only | **P** | Schema `maxItems: 2` still; `Eval.lean` already handles lists (`smallerOfList`) |
| 5.2c | `Operand` versus `LineId` asymmetry | **P** | `subtract.take` and `multiply_rate.rate` are now `operand`; `sum.of`, `subtract.from`, `choose.then` (`lineRef`) still require line ids; 212 federal helper lines are bare `param` wrappers (`expr.op == param` with a helper marker) |
| 5.2d | SEP rate faked as `NonNegDollars` | **H** | `person.yaml:1223,1233` `person.cent`, `person.hundred` |
| 5.2e | No `Date` type | **H** (documented) | `spec/spec.md:136` now says `Date` is "Reserved: not in `schema/data.schema.json` and used by no line" (T-192); year-specific Bool inputs remain (`eic.died_2025`, `f2441.paid_2026`, `household.spouse_died_2025`) |
| 5.3a | Copy-pasted generic `help:` placeholder | **F** | `grep -c "Money is integer cents" interview/questions-2025.yaml` = 0 |
| 5.3b | Legacy sub-profiles list every input | **H** | `interview/2025.yaml` 68 lines, `sales-2025.yaml` 355, `stage4-2025.yaml` 388 versus `full-2025.yaml` `questions: all`; still loaded by `build.ts` and `loadInterview` |
| 5.4a | Five-way input ripple | **H** | Unchanged in structure; mitigated by `tools/siblings.py` (423 lines, a check-all step; T-150) |
| 5.4b | Three fixtures do not round-trip `json.dumps(indent=2)` | **F** | `stage4.json`, `stage15.json`, `stage16.json` all round-trip (`python3` comparison, all True) |
| 5.4c | `classm.json` has contradictory input combinations (`mfj` with `unmarried: true`) | **H** | 14 of 198 cases in `fixtures/2025/classm.json` have `f1040.status == mfj` and `household.unmarried == true` |
| 6.1a | Conflicting handoff entrypoints | **F** | CLAUDE.md, PROJECT_INDEX lines 30-42 and 138 agree; root handoffs moved to `handoffs/` (T-203). `HANDOFF-NEXT-SESSION.md` has 7 entries, not "the latest two" (PROJECT_INDEX line 30) |
| 6.1b | Spec drift (Schedule 1 and 1-A refusals, two engines) | **P** | `spec.md:49-60` now reads "Schedule 1 items other than those computed"; `spec 6.5` names four engines (T-204). A full read of spec 2.2 and 11 was not done |
| 6.1c | 12 of 91 ambiguity entries unlinked from any line | **F** | 93 entries, 1 unlinked (`amb.2025.dc_born_died_half_year`), by regex `ambiguity:` over `forms/2025` and `forms/ny/2025`; regex may miss other link syntax |
| 6.2a | 736 suppressed baseline entries | **P** | 622 now across 8 files: consumers 379, instruction_cites 140, limits 67, operands 23, input_quotes 6, signs 5, screens 2, completeness 0 (audit: 423, 152, 67, 24, 6, 5, 3, 56) |
| 6.2b | 78 of 149 paired reviews pending | **P** | `reports/2025/second_family.md:3` now: 136 pairs, 64 eligible, 72 pending |
| Summary | "~29,200 LOC", "62 YAML forms", "1,994 test cases" | | 62 federal YAML forms (plus 6 New York); 1,997 fixture cases (`json` count over `fixtures/2025` and `fixtures/ny/2025`); engine 12,098 + tools 32,671 + Lean 1,933 lines |

Tally of the 50 rows above (the audit's own count was 37 findings; sub-items were split here): fixed 14, partly 14, still holds 22
(rows marked "H (documented)" count as holding). Of the audit's seven "active bugs" (1.1 to 1.7): five are fixed (1.1, 1.2, 1.4,
1.5, 1.7), 1.3 is partly fixed, and in 1.6 two of three sub-items are fixed and one holds (1.6c).

---

## 6. Conventions

Factual, measured; no recommendation.

**Jurisdiction and year layout.** Federal 2025 data is under `<kind>/2025/`; New York is `<kind>/ny/2025/` for forms,
tables, fixtures, reviews, reports and rendered output. Single-file kinds use a year file: `params/2025.yaml` and
`params/ny/2025.yaml`; `ambiguities/2025.yaml` and `ambiguities/ny/2025.yaml`. Interview files put the year in the
filename and the jurisdiction in a subdirectory (`interview/questions-2025.yaml`, `interview/ny/questions-2025.yaml`).
Tool catalogs put the jurisdiction in the filename (`tools/sources-2025.json`, `tools/sources-ny-2025.json`).
`sources/` has `2024`, `2025`, `2026` and `ny`. `reports/` has `2025`, `2026`, `ny`. Tool adapters nest
`tools/transcription/adapter_contracts/2025/` (year directory, no jurisdiction level). 29 tool files take
`--jurisdiction` through `tools/jurisdiction.py`; the engine uses `--ny`.

**Fixtures by stage.** `fixtures/2025/` holds 18 `stage*.json` files (stages 1 to 5, 8 to 16, 18 to 21) plus `classm*.json`,
`mutation.json` and `differential/`; New York has `fixtures/ny/2025/it201.json` (141 cases, named by form not stage).
`stage1.json` has 60 cases with 107 to 121 inputs each (the retrospective: 105).

**Line ids.** Federal lines (3,102): 1,990 descriptive names, 1,058 `lineN`, 54 short-numeric prefixes. New York (478): 370
descriptive, 108 `lineN`. `printed` markers: `(helper)` 1,786, `(gate)` 164, `(screen)` 23, `(status)` 2, other parenthesized
36, and 1,045 numbered lines.

**File naming.** `engine/src`: 35 files, 9 kebab-case (`interview-rules.ts`, `serve-check.ts`, `mutate-worker.ts`), the rest
single words. `tools/`: Python and shell in snake_case, no hyphenated script names; prefixes `check_` 23, `test_` 15,
`extract_` 7, others 77. Docs: 16 of 22 entries in `docs/` carry a `YYYY-MM-DD_` prefix; 6 do not (`ARGON_CLAUDE_DISCUSSION.md`,
`COVERAGE.md`, `TRUST.md`, `ny`, `patches`, `ty2026`). Handoffs: `HANDOFF-STAGE-N`, `HANDOFF-T091`, `HANDOFF-HOUSEHOLD-CLOSE-<date>`,
`HANDOFF-NEXT-SESSION-ARCHIVE-<year-month>`: stage number, task number, topic with date, and bare.

**Test placement.** No `*.test.ts` or `__tests__` files. Engine tests are CLI commands (`test-fixtures`, `test-integration`,
`test-serve`, `check-self-test`, `interview-rules --self-test`). Python tests sit beside the code as `test_*.py` (`test_*` files across
`tools/`, `tools/engines/`, `tools/hooks/` (3 shell), `tools/human_review/`, `tools/transcription/`, `ui/`), and 22 Python tool files also take
`--self-test`. `git ls-files` finds 16 `test_*` files (the 15 under `tools/`, plus `ui/test_browser.mjs`); 13 are run by check-all, and 3 are not
(`tools/transcription/test_review_yield.py`, `tools/human_review/test_browser.mjs`, `ui/test_browser.mjs`).

**Languages (tracked, excluding sources, reviews, reports, rendered and fixtures).** TypeScript 12,909 lines in 36 files; Python 31,193 in
108 files (this includes tool tests and a few files outside `tools/`); `.mjs` 1,964; shell 1,177; Lean 1,933 in 6 files; YAML 86,689 in
125 files; JSON 189,726 in 906 files; Markdown 41,577 in 766 files.

---

## 7. Retrospective numbers re-grounded

Source of each claim is `docs/2026-11-07_process_retrospective/` (R00 = `00_synthesis.md`, R04 = `04_architecture.md`, and so
on). "Retro" is the value the document gives; "now" was measured at `e2252227`.

| Claim (where) | Retro | Now | Command or file |
|---|---|---|---|
| Commits | 211 (R01, R04) | 223, 2026-10-13 to 2026-11-09 | `git rev-list --count HEAD` |
| Evaluator size | 827 lines (R00) | 827 | `wc -l engine/src/eval.ts` |
| Evaluator commits / first size | 20 commits, 415 lines (R04) | 20 commits, 415 first | `git log -- engine/src/eval.ts`; `git show <first>:engine/src/eval.ts \| wc -l` |
| `mutate.ts` | 238 to 2,557, 37 commits (R04) | 238 to 2,571, 41 commits | same method |
| `check.ts`, `build.ts` | 1,269; 467 (R04) | 1,269; 467 | `wc -l` |
| Lines of form data | 3,549 (R00, from `coverage.md:8009`); 3,071 (R04) | **3,580** = 3,102 federal + 478 New York; 0 `opaque` | PyYAML over `forms/2025/*.yaml`, `forms/ny/2025/*.yaml`; `reports/2025/coverage.md:8198` "0 of 3580 lines use opaque" |
| Helper-marked lines | 1,755 of 3,071 (57%) (R04) | 1,977 of 3,102 federal (63.7%); 1,786 are `(helper)` | PyYAML, markers `(helper) (gate) (computed helper) (question) (status) (screen)` |
| Param-wrapper helpers | 206 (R04) | 212 federal | helper lines whose `expr.op` is `param` |
| Input lines | 568 (R04) | 570 federal, 57 New York | `expr.op == input` |
| Atoms added after day 1 | 5 | 19 atoms in `IMPLEMENTED`, 40 entries in `VOCABULARY` (the `VOCABULARY` array also holds non-atom entries) | `engine/src/atoms.ts`; not a like-for-like count |
| Tools scripts | 120 (95 py, 13 mjs, 11 sh, 1 swift); 31,398 lines (R04) | **125** (96, 14, 12, 1, plus 2 extensionless hooks); 32,964 lines | `git ls-files tools`; `wc -l` |
| Tools files | 149 (R04) | 152 | `git ls-files tools \| wc -l` |
| Check-all steps | 90 (R00, R04) | 92 `step` lines on a like-for-like count (90 at `d05db7e6`); **94** distinct steps in the full tier | `grep -c '^step '`; log headers of the green full run |
| Self-test and tool-test steps | about 38 (R00) | 34 strict; 37 with the three engine test commands | section 3.1 |
| New York duplicates | 19 (R00) | 19 `ny_` steps, of which 16 mirror a federal step | section 3.1 |
| Step count history | 24 (10-21) to 90 | not re-measured | |
| Check-all runtime | about 38 min full, about 11 min fast (R04, testimony) | not re-measured; summed step seconds 7,356 (full, 11-07) and 2,737 (fast); wall time not recorded | section 3.3 |
| Derived to authored ratio | about 8:1: 717 authored versus 5,903 derived file changes over 79 commits (R04) | **8.1:1**: 756 authored versus 6,156 derived over 81 commits touching `forms/2025`; code 557 | `/tmp`-style script over `git show --name-only` of those commits; authored = `forms/ params/ tables/ ambiguities/ interview/ schema/ spec/`, derived = `fixtures/ reviews/ reports/ rendered/ .transcription/ .classm/`. A narrower split (YAML forms versus the four derived directories) gives 12.1:1 |
| Dividends gate `1075bb5c` | 153 files (R00) | 153 files, +14,487 / -5,384 | `git show --stat 1075bb5c` |
| Snapshots of invalidated review data | 91 (R00) | **91** (90 directories + 1 file), 853 MB, 5,180 files, 2026-10-23 to 2026-11-07 | section 1.3 |
| `.transcription` on disk | about 1.0 GB (R04) | 1.0 GB | `du -sh` |
| Inputs with `gated_by` | 25 (R04) | **36** (29 federal + 7 New York) | `grep -c gated_by forms/2025/*.yaml forms/ny/2025/*.yaml`; the build prints "gated inputs: 36" |
| "321 leaking" interview-rule baseline entries | 321 (R04) | **The 321 appears to be the character length of the baseline's `about` text.** At `d05db7e6` the file held one entry (`early_completion` with `person.edu`); `len(about) == 321`. Now: 62 `order_dependent_reach`, 11 `walked_unused`, 4 `early_completion` | `git show d05db7e6:tools/interview_rules_baseline.json`; current file |
| Question bank | 577 questions (R04) | 579 questions, 9 frames | `interview/questions-2025.yaml` |
| Schema | 257 to 1,588 lines (R04) | 1,588 | `wc -l schema/data.schema.json` |
| `person.yaml` | 4,782 lines (R04) | 4,948 | `wc -l` |
| Dependent / person 8863 block | about 590 lines each (R04) | `person.edu*`: 48 ids, 997 lines; `dependent.edu*`: 38 ids, 821 lines; the main block starts at `person.yaml:3487` and `dependent.yaml:1773` (the first `person.edu*` id is at line 123, so the ids are not contiguous) | section 5, row 5.1b |
| Spec | 281 to 522 lines, 36 commits (R04) | 522 lines, 36 commits; `design.md` 217 to 242, 8 commits | `git log`, `wc -l` |
| Lean | 1,948 lines (R04) | 1,933 lines in 6 files | `wc -l lean/**/*.lean` |
| Bug inventory | 456 or 458 entries, 640 KB (R02, R04) | 467 entries, 661,750 B | `grep -c '^## BUG-'` |
| Planning-layer words | about 148,000 (R02) | 161,719 | `wc -w` over `handoffs/*.md docs/*.md HANDOFF-NEXT-SESSION.md TASKS.md CLAUDE.md spec/*.md PROJECT_INDEX.md README.md` |
| "supersed*" occurrences | 32 (R02) | 35 | `grep -o -i supersed` over the same files |
| `TASKS-DONE.md` | 133 KB | 133,050 B | `wc -c` |
| `PROJECT_INDEX.md` | 46 KB | 47,511 B | `wc -c` |
| `README.md` | 512 lines | 512 | `wc -l` |
| `COVERAGE.md` | 174 KB | 174,361 B | `wc -c` |
| Review ledger | $328.30, 11-04 onward (R00) | **$345.35**, 1,261 rows, 11-04 to 11-08; transcription $165.82 (48%), render $73.78, completeness $52.34, classm $34.13, screen $13.02, false_no $6.26 | sum of `cost_usd` in main `.transcription/costs.jsonl` |
| Agent run log | covers 11-03 onward | 135 rows | `wc -l research/costs/agent_runs.jsonl` |
| Federal coverage | 78.4% | not recomputed (it needs the estimator run); `reports/2025/filer_coverage.md` was not parsed | |
| 165 questions, 142 answered no or zero | `docs/2026-11-06_question_structure_design.md` | not re-run (needs the compiled engine) | |
| Cost split, repeat reviews, 17% share, and the commit-history phase table | R00 sections 2 and 4 | not re-measured | |

Baseline table (retrospective claims this inventory could not reproduce or that moved materially):
the "321 leaking entries" (likely a character count), the gated-input count (36, not 25), the line count (3,580, not 3,549),
and the script count (125, not 120).

---

## Appendix. Gaps in this inventory

- `git status` of the main checkout was not run (the sandbox limits git to this worktree), so the untracked and ignored
  lists in 1.2 are inferred from `find` and `.gitignore`.
- The 5 "not reached" scripts and the "no referrer" documents are results of regex searches over tracked text; a script
  invoked by a name built at run time, or by a path in an ignored file, would be missed.
- Archive snapshot usage (1.3), the 22 `step` lines that omit `"$@"` (section 5, 1.3), the 7 Python AST-walker copies and the
  8 markdown-parser copies (5, 2.2 and 4.2) were not individually re-counted.
- Check-all timings are from 2026-11-07 per-worktree records; the main checkout's own timing file is older. No wall-clock
  figure for a whole run was found.
