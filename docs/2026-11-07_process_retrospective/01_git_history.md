# Process retrospective, slice 1: git history

Repository: `/Users/elliotmilco/Documents/GitHub/tax-formalization` (remote `emmilco/us-tax-model`), branch `main`, 211 commits, 2026-10-13 22:54 to 2026-11-07 22:45.
Investigator: claude-opus-5-5 (judgment class). Read-only. Method: `git log --reverse --numstat --no-renames`, aggregated by script; commit bodies; `git branch -a` and `rev-list main..<branch>`; first-add dates of tool files (`--diff-filter=A`); `BUG_INVENTORY.md` parsed for detection method. Every number below came from those commands unless marked otherwise.

Credence labels on interpretations: **weak** (one observation; "suggests"), **moderate** (several observations agree; "consistent with"), **strong** (several independent measures agree).

---

## 0. Headline findings

1. **The code and content were not chaotic.** Hand-written material was mostly written once. Deleted lines as a share of added lines: content (forms, tables, params, interview, spec) 0.15, engine/Lean/UI 0.13, `tools/` 0.08, process docs 0.24. The current trees roughly match cumulative additions: `forms/` is 56,197 lines today against 64,207 lines of churn; `engine/src` is 11,756 against 15,410; `tools/` is 39,556 against 46,601. The history is linear, with one merge (`286792cd`), and that merge was an accident. (Strong.)
2. **Verification was planned up front but reorganised mid-flight, and two of its layers came only after damage.** The day-0 design (`d3f06cb3`, `spec/design.md` §2.10) already had fixtures, a Lean reference evaluator, mutation, differential and property tests, and human class-B hand-work. Stages 1 to 5 were built in about 2 days (`919322a2` to `8417477f`, 7 commits, none mentioning a bug). Right after that, the spec was amended to replace human reading with "independent-construction" model verification (`7b60e465`, 10-16). Within 24 hours the new checks found BUG-0001 to BUG-0032, including a value error on Form 1040 line 9 (`cbabd7bb`). The completeness review, which asks whether everything in the source was encoded, arrived only on 10-30/31 (`0fd59d31`, `84fa3309`), after 21 stages. Its first sweep found 50 defects (BUG-0211 to BUG-0260), including a value error: BUG-0219, where qualifying surviving spouse was never tested ($10,350 instead of $18,500). (Strong that these layers came late; moderate that earlier use would have prevented the rework.)
3. **Process infrastructure was mostly added after the fact, each piece responding to a specific incident.** Examples: the commit guard (`290d550d`, 10-17), then the merge that bypassed it (BUG-0269, `286792cd`), then a pre-push hook (`0a0d2f4b`, 10-31), then a fix because that hook checked only the tip commit (BUG-0289, `05ede53c`, 11-01). Cost ledger: `465bcfc7`, 11-03 (day 21 of paid reviews). Worktree review-data cloning: `d397fe23`, 11-07, after an agent committed a wrong report from partial data (BUG-0431). Release tiers: `e2adfe68`, 11-05. (Strong.)
4. **The churn sits in generated evidence, not in source.** 8.38M of the 9.51M total churned lines (88%) are committed generated artifacts (`reviews/`, `fixtures/`, `reports/`, `rendered/`, `.transcription/`, `.classm/`). The biggest single contributor is machine triage JSON (`reviews/2025/transcription/triage/*.json`, about 5.4M lines). `fixtures/2025/classm.json` was rewritten in 55 commits (893k lines of churn). Review logs were rerun repeatedly: 439 review `.md` logs, median 4 rewrites, maximum 27 (`reviews/2025/render/f1040.md`). On disk (git-ignored), `.transcription/archive/` holds 91 "before-X" snapshot directories, nearly all from 10-23 to 11-04. These are review data set aside each time a review was invalidated. (Strong.)
5. **The direction changed several times.** The goal widened from a proof of concept to a product to the 80% coverage goal. It then turned to integrity and hardening, then to parallel backlog work, then to TY2026 and New York, then to a web UI and formal gates. Each turn was documented, but coverage growth stopped. The estimate went 17.9% (`d99988aa`, 10-18) → 68.6% (10-22) → 82.2% (`a428e8bb`, 10-29) → corrected down to 78.4% (`e6a8053a`, 11-01). `reports/2025/filer_coverage.md` has not changed since `e6a8053a`. So about 90 commits (11-01 to 11-07) produced no coverage gain. Stage 17 (Schedule E) was named as "next" in at least four handoffs and never started. (Strong on the observation. Whether this was right depends on the owner's priorities, which git does not record.)

---

## 1. Phase timeline

I set the phase boundaries from message themes and from the commits that triggered each transition. Line figures are churn (added + deleted) in hand-written categories: content = `forms tables params interview ambiguities spec schema`; engine = `engine lean ui package*`; tools = `tools/`; process = handoffs, TASKS, BUG_INVENTORY, docs, README, PROJECT_INDEX, CLAUDE.md. Research and generated output are counted separately.

| Phase | Span | Commits | Content | Engine | Tools | Process | Research | Generated | Sources |
|---|---|---|---|---|---|---|---|---|---|
| P0 Design + source archive | 10-13 22:54 → 10-14 00:13 | 8 | 502 | 0 | 404 | 107 | 1,498 | 0 | 110,622 |
| P1 Stages 1–5 build | 10-14 00:13 → 10-15 23:04 | 7 | 15,764 (73%) | 5,564 (26%) | 234 | 100 | 0 | 71,586 | 181 |
| P2 Verification retrofit ("Stage 7") | 10-16 15:12 → 10-17 01:43 | 12 | 226 | 805 | 2,524 (62%) | 525 | 8 | 33,482 | 0 |
| P3 Coverage stages 8–16 | 10-17 02:41 → 10-22 17:26 | 62 | 58,356 (80%) | 3,978 | 7,662 | 2,942 | 4,065 | 768,856 | 402,332 |
| P4 Integrity plan / validation overhaul | 10-22 19:10 → 10-27 13:22 | 21 | 2,707 (10%) | 1,123 | 14,791 (56%) | 7,690 (29%) | 64 | 947,068 | 43,875 |
| P5 Route to 80% (stages 20, 18, 19, 21) | 10-27 15:32 → 10-29 18:36 | 8 | 10,653 (83%) | 463 | 945 | 738 | 810 | 1,003,612 | 6,070 |
| P6 Sweeps and hardening | 10-30 00:14 → 11-02 19:20 | 33 | 1,545 (8%) | 337 | 4,992 (25%) | 12,953 (65%) | 0 | 1,695,339 | 11 |
| P7 Parallel backlog + cost control | 11-02 22:07 → 11-04 12:39 | 16 | 3,775 (24%) | 1,784 | 4,736 (30%) | 5,568 (35%) | 5,865 | 3,025,156 | 9,941 |
| P8 TY2026 prep, New York, release gating | 11-04 18:08 → 11-06 01:19 | 8 | 8,426 (49%) | 1,466 | 5,844 (34%) | 1,495 | 76,702 | 215,103 | 131,363 |
| P9 Web UI + formal gates | 11-06 08:08 → 11-07 22:45 | 36 | 8,285 (44%) | 4,979 (26%) | 4,469 (24%) | 1,072 | 1,139 | 624,300 | 120,633 |

Commits per day: 10-13:7, 14:6, 15:2, 16:7, **17:27**, 18:10, 19:10, 20:5, 21:6, 22:13, (23:0), 24:2, 25:5, 26:2, 27:10, 28:1, 29:5, 30:2, 31:12, 11-01:13, 02:8, 03:6, 04:9, 05:4, 06:14, **07:25**. Hours: 75 of 211 commits fall between 21:00 and 03:59.

### P0: Design and premises (8 commits)
- `d3f06cb3` adds `spec/spec.md` (281 lines), `spec/design.md` (217) and six research notes (about 1,500 lines). Its body says "No implementation code. Research claims are unverified". The design fixes a 7-stage build order (Stage 0 premises → Stage 6 TY2026), each with a done-when list.
- `c97beda5` adds the source archiver with hash verification. `e9192761`/`a43d24f3` record the Form 8995 scope decision. `198610c0` closes Stage 0.
- **Transition:** follows the design's own order (Stage 0 done → Stage 1).

### P1: Stages 1–5 build (7 commits, about 46 hours)
- One commit per stage, each large: `4e62fc71` Stage 4 is 91 files and 7,489 hand-written lines; `8417477f` Stage 5. `919322a2`/`bd35a5ce` (Stage 1) bring in the schema, checker, renderer, evaluator, Lean reference evaluator and `engine/src/mutate.ts` together.
- None of the 7 commits has a body or a co-author trailer. The later bug inventory notes that Stage 1–5 fixtures had expectations "recorded from the engine" (BUG-0001, "Why it survived"; tag `recorded-expectation-laundering`).
- **Transition:** Stage 5 done → spec amendment `7b60e465` (10-16 21:44). Its body widens the goal to "growing toward coverage of most ordinary filers… federal first with New York intended afterward". It also replaces human line-by-line reading with "agreement among independent constructions" and marks the Lean checker soundness proof "not pursued".

### P2: Verification retrofit (12 commits, about 10 hours)
- In order: amendment `7b60e465` → BUG-0001 found by the new engine differential (`cbabd7bb`, 7 minutes later; the bug inventory is created in this commit) → `c3cd1938` differential against PolicyEngine-US/Tax-Calculator → `1b79e5e9`/`4c3a8ef1` transcription agreement (BUG-0002) → `b3357102` property tests → `189ebedc` render comparison (BUG-0003 to 0010) → `f78f9ddf` TASKS.md → `63cb17b1` class M (model hand-work).
- `tools/` gets its main verification tools here (first-add dates: `check_bug_inventory.py`, `engines/compare.py`, `transcription/{transcribe,check_logs,rule}.py` on 10-16; `render_compare.py`, `classm.py`, `green.sh`, `hooks/pre-commit` on 10-17).
- **Interpretation (strong):** the design always meant to verify. But the model-based verification that found the first bugs was built after the five planned stages, not alongside them. BUG-0001 was a plain value error on Form 1040 line 9 that had passed all Stage 1–5 checks.

### P3: Coverage stages 8–16 (62 commits, about 5.6 days)
- A regular rhythm: **stage → follow-up → reviews rerun → owner rulings → handoff.** Examples: Stage 8 `1124aa31` → `6a0a2b48` (fixing the mutation tool for the new atom) → `bc2ecc84` fixtures → `da442776` (class M rerun; BUG-0016, "rerunning a review tool silently dropped standing rulings") → `8e189236` rulings sidecar (T-024). Stage 15: `6051ec00` groundwork → `8d7c0fdc` → `1c465c22` follow-up → `5928bf31` "third fixture round" → `6fb728b5` (Stage 16 plus Stage 15 follow-ups) → `c99e3c54` cleanup.
- Cross-cutting infrastructure arrived inside this phase as it became needed: coverage estimator `d99988aa` (10-18; it re-ordered spec 2.4); year parameterisation T-045 in 5 parts (`402dff21`…`b2b79b16`, 10-20/21); parallel check-all T-047 (`9a7f5099`, 27 min to about 2); review staleness T-044 (`8c8ede84`).
- Source text extraction was redone twice in one day, each time forcing a rerun of every review: `ac3890c0` reading-order text → `80b080fd` image audit → `0c8872a2` "Rerun every review on the reading-order text; fix the eight defects" → `e8a01774` "Per-band gutters…; every review rerun and ruled".
- `7d581797` (10-19): history rewritten with `git filter-repo` before publication. Hashes before 10-19 are post-rewrite values.
- Coverage estimate: 17.9% → 33.9% (`c5219afe`) → 47.8% (`5beb2d7b`) → 58.0% (`f16237f9`) → 68.6% (`6fb728b5`).
- **Transition:** `a946fae5` (10-22 19:10), "Integrity plan Phase 0: honest reporting". It adds `docs/2026-10-22_project_evaluation.md`, an outside-eye read at `3748f74` by a different model (Fable 5.1). The evaluation found that "evidence labelling has drifted" and that the scoreboard credited only 19 of 1,510 computed lines (1.3%) with an outside-family assertion.

### P4: Integrity plan / validation overhaul (21 commits, 10-22 → 10-27)
- Tools dominate (56% of hand-written churn): packet tool, DeepSeek transport and family logs (`ac69196c`); OpenTaxSolver (`a65e6afb`); UsTaxes as fourth engine (`a782c873`); triage (`4d8e51dd`, the `triage.py`/`.mjs` first-adds); `archive_text.py` (`6cae6818`).
- A long rework chain of review-record commits: `735e6442` → `2fdec33c` → `bdb2e127` → `45876d27` → `acad366f` ("Replace incomplete transcription records with schema-guided reviews") → `0ef4912a` → `1b75a3b7` → `9bb82055` → `4d8e51dd` ("Adjudicate source reviews by execution; fix BUG-0147 to BUG-0160"). On disk, 24 `.transcription/archive/` snapshots are dated 10-23 to 10-27.
- `735e6442` makes human review optional (the controlling `docs/2026-10-24_validation_policy.md`). It is preceded by a 47-hour gap with no commits (10-22 22:18 → 10-24 21:17); BUG_INVENTORY entries dated 10-23 (17 of them) show that work went on uncommitted during the gap.
- The commits dated 10-24 to 10-26 (`735e6442`…`9bb82055`, 7 commits) have no co-author trailer and use a different message convention (imperative subjects, a "Validation:" footer). This is consistent with a different agent or tool. The archived handoff shows Codex was used in at least one session ("P0 execution checkpoint — 2026-11-01 (Codex)", `handoffs/HANDOFF-NEXT-SESSION-ARCHIVE-2026-11.md:411`), but I could not tie specific commits to it.
- **Transition:** `a16223be` "Coverage route to 80% (plan revision E)".

### P5: Route to 80% (8 commits, 10-27 → 10-29)
- Stages 20 → 18 → 19 → 21, out of numeric order on purpose: plan revision E orders them by estimated coverage gain. Each stage is one large commit with its BUG range (`4d24cbcb` BUG-0182..0187, `2d971adf` 0188..0193, `34b23461` 0194..0199, `a428e8bb` 0200..0206). Coverage went 71.0% → 75.6% → 79.6% → 82.2%.
- **Transition:** goal reached → `2ca33119` (T-067 and a bug root-cause analysis, `docs/2026-10-29_bug_root_cause_analysis.md`) and `0fd59d31` (source-coverage checks, completeness experiment).

### P6: Sweeps and hardening (33 commits, 10-30 → 11-02)
- `84fa3309` screen and completeness sweep: 50 defects (BUG-0211 to 0260), "reviewed and adjudicated in rounds until a round found nothing medium or higher". `a75729ff` hardening (10 tasks). `3bdb1d3a` README rewrite. Then `5765b6b9` coverage decision tree → `4486fe37` "Coverage table in place of the decision tree charts" (55 minutes later, replaced).
- `e6a8053a` corrects coverage **down** to 78.4% once dependent filers are counted (T-102). The 80% goal is no longer met; nothing raised coverage afterwards.
- Merge accident `286792cd` (`git pull`) → BUG-0269 → pre-push hook `0a0d2f4b` → BUG-0289 (hook checked only the tip) fixed in `05ede53c`.
- 13 commits on 11-01 and 9 on 10-31 have no trailer. The Codex checkpoint dated 11-01 suggests some were Codex sessions (weak).
- Process docs are 65% of hand-written churn: `docs/2026-11-01_backlog_plan.md`, `docs/2026-11-01_tech_debt_audit.md`, BUG_INVENTORY entries, TASKS split (`f44bae48`).
- **Transition:** owner decisions and integration of cloud sessions (`c2a71b13`, `39390e9f`).

### P7: Parallel backlog and cost control (16 commits, 11-02 → 11-04)
- Work moves to parallel cloud sessions and packages, each integrated into `main` as **one squash commit**: `39390e9f` (from `origin/claude/A-backlog`, 12 commits on that branch), `0d9718cc` (from `origin/claude/f1-dependent`, 14 commits), `859741f1` (T-159 tier 1), `0a43f158` ("seven parallel packages", 536 files, 1.38M generated lines, BUG-0341 to 0390).
- `465bcfc7` (11-03) adds the cost ledger `tools/transcription/costs.py` and the owner's "inference only where it adds evidence" rule. `f27d71d9` adds review carry-over and line-scoped reviews (`carry.py`).
- Then round chains: `b8bacf5f` Round 2 → `96347690` "Round 3: the round-2 lows fixed" → `a28b705e` "the round-3 sales lows". The CLAUDE.md rule "a round whose reviews find only lows starts no further round" reads as the correction for this pattern (moderate).
- **Transition:** T-159 done (`288b40c9`) → TY2026 and NY cloud branches.

### P8: TY2026, New York, release gating (8 commits, 11-04 → 11-06)
- `d6017626` squashes `origin/ty2026/prep` (7 step commits) into one main commit with 75,532 lines of research/ty2026. 2026 is not adopted (`years.json` [2025]).
- `bdac4121` squashes `origin/ny/2025-foundation` (22 commits, ending "NY Phase 3: stop for budget") into one commit of 239 files.
- `e2adfe68` release-gated check-all (full/fast/docs tiers; fast is "~7 min"). Check-all, which `9a7f5099` had brought to about 2 min on 10-21, had grown slow enough again to need tiers.
- **Transition:** release gating done → the owner's web UI readback (`5d0d66e8`).

### P9: Web UI and formal gates (36 commits, 11-06 → 11-07)
- `5d0d66e8` UI design → the T-251 "topic layer / question ladder", built on worktree branch `worktree-agent-aeba046e877ced9d9` (5 commits, about 6,349 lines) → **dropped the same day**. `3c1e5d17`: "The design replaces the T-251 interview-layer topic layer, which stays unmerged on its branch". `814a1ea7` merges only the UI commits "without the superseded T-251 topic-layer commits".
- Formal gates G1 `05aa3039` → G2 `a061e282` → round 1 `2bcfd009` → lanes D/A (`71de1fe2`, `1075bb5c`) → two Form 8889 follow-ups (`d563b283`, `d05db7e6`).
- The "long questions as lists" set (`b66f4ea6`, `42a384d7`, `c1e852dc`, `6c7d46a1`, `5d8c6fd8`, 00:15–03:42 on 11-07) is followed by BUG-0437 (`ce992c68`): structured questions broke review prompts.
- About 30 worktree-agent branches, one or two commits each, re-applied (not merged) onto main. `d397fe23`/`2824e9a4` (11-07) add `worktree_data.py` and the background-wait rule (`11883002`), after BUG-0431, where an agent worktree "committed the wrong report (35d04c3, not merged)".

---

## 2. Commit order against dependency order

First-add dates of infrastructure (`git log --diff-filter=A`), compared with when each was first needed:

| Infrastructure | First added | Status | Evidence |
|---|---|---|---|
| Source archive with hashes | `c97beda5` 10-13 | **Ahead** | Before any encoding; design §2.1 |
| Lean reference evaluator, mutation tool | `bd35a5ce` 10-14 (Stage 1) | **Ahead** | Planned in design §2.10. But the Lean evaluator agrees "because it reads the same data" (BUG-0001), so it could not catch transcription errors |
| Bug inventory | `cbabd7bb` 10-16 | Just in time | Created with BUG-0001 |
| Engine differential, transcription agreement, render comparison, class M | 10-16/17 (P2) | **Retrofitted** after 5 stages | Found BUG-0001 to 0010 within hours |
| Rulings sidecar (rulings survive reruns) | `8e189236` 10-17 | **After damage** | BUG-0016: ruling loss had let model values back into `classm.json` |
| Commit guard | `290d550d` 10-17 | Early | T-021 |
| Coverage estimator | `d99988aa` 10-18 (after Stage 12 had started) | Just in time | Re-ordered spec 2.4. Stages 8–11 were chosen before any coverage measure existed |
| Year parameterisation (T-045) | 10-20/21 | Ahead of need | TY2026 not adopted by 11-07; the design always had Stage 6 |
| Review staleness (T-044) | `8c8ede84` 10-21 | Retrofitted | After 5 days of reruns |
| Multi-family reviews (DeepSeek), human packets | `ac69196c` 10-22 | **Retrofitted after evaluation** | Project evaluation: "trust claim rests on one model family" |
| Triage / adjudication by execution | `4d8e51dd` 10-26 | Retrofitted | 14 bugs in the same commit |
| Screen and completeness reviews | `362e08ec` (screen) 10-17; `0fd59d31`/`84fa3309` (completeness) 10-30/31 | **Completeness retrofitted after 21 stages** | 50 defects in the first sweep, including value error BUG-0219 |
| Pre-push guard | `0a0d2f4b` 10-31 | **After damage** | BUG-0269 merge bypass; then BUG-0289 fixed the guard itself |
| Sibling-defect tool | `1a98539e` 11-01 | Retrofitted | After 290 bugs |
| Cost ledger and cost policy | `465bcfc7` 11-03, `90d823da` 11-05 | **Retrofitted at day 21** | Paid reviews ran from 10-16 |
| Review carry-over, line-scoped reviews | `f27d71d9` 11-04 | Retrofitted | After whole-form reruns had produced most of the 8.4M generated-line churn |
| Release tiers | `e2adfe68` 11-05 | Retrofitted | Check-all slow again |
| Worktree data clone / carry-back | `d397fe23` 11-07 | **After damage** | BUG-0431; worktree agents in heavy use from 11-06 (about 30 branches) |

**Interpretation (strong):** the core architecture was laid down before it was needed: data-first forms, a closed atom vocabulary, hashed sources, a CLI as backend, Lean, mutation. That part is coherent and held up, as the low source churn in §3 shows. The **verification-of-the-verification and operations layer** was built reactively, each piece after a specific incident. That layer covers review-record integrity, staleness, rulings persistence, guards, cost and parallel-agent data. Its absence is what produced the regeneration churn in §3.

**Built, then rebuilt or dropped:**
- Human class-B hand-work (design §2.10) → replaced by model class M (`7b60e465`) → human review made optional (`735e6442`).
- Lean checker soundness proof → "not pursued" (`7b60e465`).
- Source text extraction → reading-order text (`ac3890c0`) → per-band gutters (`e8a01774`), each followed by a full review rerun.
- Transcription records → "replace incomplete transcription records with schema-guided reviews" (`acad366f`); prompt policy v2 → v3 (`465bcfc7`), with "45 unchanged forms keep their v2 logs".
- Decision-tree charts (`5765b6b9`) → table (`4486fe37`) within an hour.
- T-251 topic layer (branch `worktree-agent-aeba046e877ced9d9`, 5 commits) → superseded by formal gates (`3c1e5d17`), never merged.
- T-254 items 3–4 scheduler and cache → "dropped" (`d397fe23` body); branch `worktree-agent-a4eceeb8ee9a5f170`, 4 commits unmerged.
- Handoffs: 21 handoff files created (one per stage, 10-13 to 11-04), moved into `handoffs/` by `a946fae5`. Now one current pointer (`HANDOFF-NEXT-SESSION.md`, 32 commits) and HARDENING-1.
- TASKS.md (121 commits, the most-touched file) split into TASKS-DONE.md (`f44bae48`).

**Unmerged branches (`git rev-list main..<b>`):** `origin/claude/ruling-audit-1` (3), `origin/claude/t159-mutation` (7), `origin/claude/A-backlog` (12), `origin/claude/f1-dependent` (14), `origin/ny/2025-foundation` (22), `origin/ty2026/prep` (7), `asset-sc-pass` (4), and about 28 `worktree-agent-*` branches with 1–5 commits each. Nearly all were folded into main by squash or re-application with the same or similar subjects. Two were explicitly superseded rather than integrated (T-251; T-254 items 3–4). `ty2026/prep` holds files that differ from main (the diff of `research/ty2026` shows 6,192 deletions relative to main). This is consistent with main carrying a later revision; I did not verify it.

---

## 3. Churn

**Total churn:** 9.51M lines.

| Category | Added | Deleted | Del/add | Current size |
|---|---|---|---|---|
| Content (`forms tables params interview ambiguities spec schema`) | 95,863 | 14,376 | 0.15 | forms 56,197; tables 12,405; params 3,588; interview 4,907 |
| Engine / Lean / UI | 18,172 | 2,327 | 0.13 | engine/src 11,756; lean 1,948; ui 1,570 |
| tools/ | 43,079 | 3,522 | 0.08 | 39,556 |
| Process docs | 26,829 | 6,361 | 0.24 | — |
| Research | 90,058 | 93 | 0.00 | 89,963 |
| Generated evidence (`reviews fixtures reports rendered .transcription .classm`) | 5,833,037 | 2,551,465 | 0.44 | reviews 2.38M; fixtures 583k; reports 121k |
| Sources (archived IRS text) | 803,093 | 21,935 | 0.03 | — |

- **Most-touched files, by commits:** TASKS.md 121, BUG_INVENTORY.md 88, PROJECT_INDEX.md 85, `reports/2025/evidence.md` 79, `reports/2025/coverage.md` 78 (169,909 churn lines), `evaluator_agreement.md` 70, `stage5.return.*.txt` about 63–65 each, `fixtures/2025/classm.json` 55 (892,758 lines). The top three are bookkeeping; generated reports fill most of the remaining top-45 slots.
- **Most-touched forms:** `person.yaml` 31 commits, `f1040.yaml` 29, `dependent.yaml` 23, `scope.yaml` 22, `f8889.yaml` 19, `eic.yaml` 17. Several touched-in-many-rounds cases:
  - `f8889.yaml`: Stage 11 (10-18) → Stage 13 ×3 → T-045 → Stage 16 ×2 → cleanup → integrity → HSA partial inputs (10-26) → citations → Stage 21 ×2 → sweep → Rounds 2/3 (11-04) → formal gates and two 8889 follow-ups (11-07). Of those 19 commits, 6 are fixes or reruns rather than new scope.
  - `person.yaml`: 31 commits spread over every phase.
- **Fix-subject commits** (subject matches fix / follow-up / rerun / correct / repair / BUG-): 65 of 211. By phase: P3 20, P6 12, P4 9, P9 8.
- **Fix-of-fix chains:**
  - BUG-0016 → rulings sidecar.
  - Extraction → rerun → extraction → rerun (above).
  - Guard → merge bypass → pre-push → tip-only bug.
  - Long-question lists → BUG-0437.
  - Formal gates round 1 → "leaks fixed" in the same commit (`2bcfd009`) → BUG-0448 (`71de1fe2`).
  - T-143 → follow-up 24 minutes later (`8663f046` → `86f5b26c`).
  - `c7f773b6` archive → `dab78961` follow-up.
  - `d397fe23` → `2824e9a4` 6 minutes later.
- **Rate at which IDs were assigned:** BUG ids reached 32 by 10-17, 100 by 10-22, 210 by 10-30, 402 by 11-03, 456 by 11-07. T ids reached 58 by 10-22, 150 by 10-31, 254 by 11-06. Bug discovery accelerated in P6–P7, after coverage growth had stopped. This fits bugs being found by verification layers retrofitted onto already-written content (moderate).
- **How bugs were caught**, from `caught-by-*` tags in BUG_INVENTORY (456 entries; only about 278 carry parseable tags or dates): source-adjudication 52, render-comparison 37, screen-review 28, audit 24, completeness-review 22, review 19, engine-differential 6, external-engine 3, mutation 3, property 3. Free-text "Caught by" mentions: review 146, adjudication 103, render 78, completeness 78, transcription 65. Model reading of source against encoding found far more defects than the classic test machinery (mutation, property, Lean, differential).

**Interpretation (strong):** the "churn" that cost time and money was in verification artifacts and their reruns, not in the formal model. A large share of it is triage JSON and `classm.json` regenerated wholesale and committed. That made diffs unreadable and the repository heavy (pack 250 MB).

---

## 4. Composition and how it shifted

Dominant hand-written category per commit, overall: process 68, tools 59, content 52, engine 29.

| Phase | Content share of hand-written churn | What else dominated |
|---|---|---|
| P1 | 73% | engine 26% |
| P2 | 6% | tools 62% |
| P3 | 80% | — |
| P4 | 10% | tools 56%, process 29% |
| P5 | 83% | — |
| P6 | 8% | process 65% |
| P7 | 24% | process 35%, tools 30% |
| P8 | 49% | plus a 76,702-line research dump |
| P9 | 44% | engine 26%, tools 24% |

The pattern alternates. Content bursts (P1, P3, P5) are followed by verification or process phases (P2, P4, P6–P7), each triggered by what the previous burst exposed. Over the whole history, content was about 37% of hand-written lines (110,239 of 300,680, with research counted as process here) and process plus research plus tools about 56%.

**Interpretation (moderate):** the alternation looks like build → audit → harden cycles rather than random thrash. The ratio got worse as the project went on. After 10-29, content work was mostly fixes and question rewording, not new scope, until P8–P9 opened new fronts (NY, TY2026, UI) rather than finishing federal coverage (Stage 17 Schedule E stayed deferred).

---

## 5. Commit granularity and message discipline

- **Files per commit:** median 24, mean 54, maximum 537. 68 commits touch more than 50 files and 14 touch more than 200. **Hand-written lines per commit:** median 306, mean 1,425.
- Size is driven by regenerated reports: check-all rewrites `reports/` and `rendered/`, so even a one-line form fix is a 20+ file commit.
- **Mixed-purpose commits:** 68 of 211 have two or more hand-written categories each at 20% or more of the commit.
  - The worst: `0186a66f` "Preserve current project work and name project us-tax-model". No body; 62 files; +94,956/−86,970. It mixes forms fixes (`sa.yaml`, `tcw.yaml`), a new OTS adapter, regenerated `classm.json` (163k lines), README, BUG_INVENTORY and an integrity plan edit. It is a checkpoint, not a task.
  - Others: `0a43f158` (seven packages in one commit); `735e6442` (validation policy, tooling and form fix after a 47-hour gap).
- **Mapping to tasks:** strong from 10-17 onward. Subjects cite T-/BUG- ids, and bodies are substantial (median 17 lines). Claude-trailered commits nearly always state "check-all green on this tree".
  - 20 commits have no body: P0/P1 (13), handoff-only commits, the merge, and `0186a66f`.
  - 50 commits have no co-author trailer: P0–P1, 10-24..26, 10-31..11-02, and `a4e593ae` "Update README.md" (probably a GitHub web edit).
  - Trailer models: Opus 5.5 dominates; Fable 5.1 on 10-16..17 and three commits on 10-22; one Sonnet commit.
- **Squash integration** makes main legible as a task list but hides intermediate history. The branch-level history survives only on remotes and local branches (for example 22 NY commits become 1).
- **Commit hygiene incidents:** `Claude-Session:` trailers on some commits (`5d0d66e8`, `a16223be`), later scrubbed from logs (`af87d048`) and now blocked by hook. The history was rewritten for publication (`7d581797`).

---

## 6. Evidence for and against each thesis

**For "coherent strategic vision":**
- Day-0 spec and design with explicit stages and done-when criteria; the core data architecture is unchanged since then (low source churn).
- Stages 8–16 followed the amended design's order, and coverage ordering was driven by a measured estimator (`d99988aa`, plan revision E).
- Every course change is recorded in a dated doc and a commit body: `docs/2026-10-22_*`, `10-24`, `10-26`, `11-01`, `11-04_process_optimization`, `11-05`, `11-06`.
- Append-only bug inventory with root cause and "why it survived" fields; owner rulings recorded.
- Linear history, a commit guard from day 4, a full suite behind every commit.

**For "reactive / inefficient":**
- Model-based verification (P2) and completeness review (P6) were added after the content they check, and each found value errors at once (BUG-0001, BUG-0219).
- About 8.4M lines of generated review output were committed and largely regenerated (deleted 2.55M). The 91 on-disk invalidation snapshots show reviews redone many times, often because the review protocol itself changed (v2 → v3, schema-guided records, extraction changes) rather than the forms.
- Guards, cost control and worktree data tooling each came after an incident.
- The goal widened three times (proof of concept → product, then +NY, then +TY2026, then +web UI) while federal coverage stalled at 78.4% and Stage 17 was repeatedly deferred.
- Same-day design reversals (T-251; decision tree).
- Large checkpoint commits after multi-day gaps.

**Net reading (moderate):** the strategy was coherent at the level of *what the artifact is*. The process for *how confidence is established* was discovered by doing, under a widening goal. The design under-specified the review layer in two ways: how model reviews are recorded, kept current, scoped and paid for; and whether the source has been fully encoded. Those were the costliest gaps. The tools that eventually closed them (rulings sidecar, staleness, triage-by-execution, line-scoped carry-over, cost ledger, completeness review, worktree data) were mostly in place only by days 18–25.

**What would plausibly have been better (interpretation; credence moderate):**
1. Design the review protocol and its storage up front, before stage 1. That means versioned prompts, rulings stored separately from logs, staleness keyed to changed lines, a cost ledger, and generated triage kept out of git or content-addressed.
2. Run completeness ("is everything in the source encoded?") and second-family transcription per stage from Stage 1, instead of retrofitting them after stage 21.
3. Freeze the protocol before scaling coverage, so that protocol changes do not invalidate every form's reviews (the extraction ×2 reruns, v2 → v3).
4. Hold the goal steady (finish federal coverage and Stage 17) before opening NY, TY2026 and the UI. Or, if those were intended as owner priorities, say so; git cannot show it.
5. Build infrastructure for parallel agents (worktree data, carry-back, tier gating) before fanning out to about 30 worktree branches and cloud sessions.

---

## 7. What I could not determine

- **Which agent or tool made the untrailered commits** (P0–P1, 10-24..26, 10-31..11-02). Codex is attested in one handoff checkpoint dated 11-01 but not tied to specific commits.
- **History before 10-19.** It was rewritten with filter-repo, so original timestamps and authorship of the earliest commits may have been altered. Commit structure appears preserved.
- **Elapsed effort and cost per phase.** Git shows commit times, not working time. Cost logs (`.transcription/costs.jsonl`, from 11-03) and `research/costs/agent_runs.jsonl` (119 rows, from 11-03) belong to another investigator's slice and start late.
- **Uncommitted work during gaps** (10-22 22:18 → 10-24 21:17; 10-28). The bug inventory shows work happened but not its shape.
- **Owner intent behind the turns to NY, TY2026 and the UI.** The commit bodies say "owner-approved", but whether these were wanted at the expense of federal coverage is not in git.
- **Whether `origin/ty2026/prep`'s divergent files are superseded or lost.** Not verified.
- **Line counts mix kinds.** YAML, JSON and Markdown lines are not comparable units of effort, and generated-artifact churn overstates "work".

Scratch scripts used for the aggregation were run from `/tmp/process-retro/scratch/` and deleted afterwards. The numbers can be reproduced with `git log --reverse --no-renames --numstat` and the category mapping given in §1.
