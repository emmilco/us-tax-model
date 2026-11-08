# Retrospective, slice 4: architecture and file construction

Investigator: claude-opus-5-5 (judgment). Read-only. Repository: `/Users/elliotmilco/Documents/GitHub/tax-formalization`, HEAD `d05db7e6` (2026-11-07), 211 commits from 2026-10-13.
Scratch scripts and intermediate outputs: `/tmp/process-retro/scratch04/`.

Credence labels: **high** = several independent measurements agree; **moderate** = one measurement, or one measurement plus testimony; **low** = inference from structure.

---

## 0. Bottom line

1. **The computational core was designed up front, and it fits the problem well.** The day-1 design (`d3f06cb3`, 2026-10-13: `spec/spec.md` at 281 lines, `spec/design.md` at 217 lines) fixed these choices: YAML lines over a closed atom vocabulary, canonical JSON, a citation on every line, refusals as values, a lazy memoized evaluator, a Lean reference evaluator, and the CLI as the only backend. All of them still stand. `design.md` has changed in only 8 commits and is now 242 lines. The evaluator is 827 lines (`engine/src/eval.ts`). Across 3,549 lines, 0 use `opaque` (`reports/2025/coverage.md:8009`); the design's stop condition was one line in eight. Only five atoms were added after day 1 (multiply_count, prorate, percent_floor, keyed_lookup, rate_lookup), and `bracket_schedule` was never used. **High credence that this layer was coherent and well matched to forms-referencing-forms arithmetic.**

2. **The architecture is weakest at the boundary between a person's life and the formal model: questions, applicability, and which forms apply.** The day-1 spec says the tool "decides which forms apply" (spec d1 line 11) and that "no question is asked whose answer cannot affect a reachable line" (spec d1 line 221). Nothing in the model expressed form applicability or existence facts, though, so every input stayed reachable. That check passed only because it was vacuous. The cost became visible only when the web UI was built on day 24: the single-filer fixture asks 165 questions, and 142 of them (86%) are answered no or zero (`docs/2026-11-06_question_structure_design.md`). The fix went through three framings in two days:
   - an interview-layer "topic" design approved on 2026-11-06 (`a68b8dfa`);
   - an independent review of that design that found 43 problems, 16 of them high;
   - formal gates (`3c1e5d17`, then `05aa3039`, `a061e282`, `2bcfd009`, `1075bb5c`, `fa178b50`, `71de1fe2`).

   The formal-gates work is still underway. Only 25 inputs carry `gated_by`, and `tools/interview_rules_baseline.json` lists 321 "leaking" entries that are only allowed to shrink. The top root-cause class in the project's own bug analysis is also question wording: class Q, 30 bugs, 26 of them value-affecting (`docs/2026-10-29_bug_root_cause_analysis.md:55`). **High credence that this was the main architecture/problem mismatch, and that the design foresaw it in words but never gave it a representation.**

3. **Verification evidence is coupled to form content at a ratio of roughly 8 derived files to 1 authored file.** Across the 79 commits that touch `forms/2025`, authored data files changed 717 times. Fixtures, reviews, reports and rendered output changed 5,903 times (`scratch04/ratio.txt`). One existence gate for dividends (`1075bb5c`) touched 153 files: 10 form files and 143 derived ones. Much of that ripple was designed in on purpose: committed renders, subject-hash-pinned review logs, and whole-return fixtures that list every input. **High credence on the measurement; moderate credence that a different fixture and evidence design could have cut the ripple a lot without losing guarantees.**

4. **Tooling grew by accretion, not by plan.** There are 120 scripts (95 Python, 13 .mjs, 11 shell, 1 Swift; 31,398 lines). The `check-all` step count went from 24 (2026-10-21) to 90 (2026-11-07), and about 38 of the 90 steps are self-tests. Testimony about runtime: about 7 minutes in the integrity phase, about 15 minutes around 10-30, about 25 minutes on 11-04, about 38 minutes for the full tier on 11-05 (fast tier about 11 minutes on 11-06). Large subsystems are reimplemented across languages: a Python evaluator, a Python renderer, a Python AST normalizer, at least 7 Python AST walkers, and 20 files that load `manifest.json`. **High credence on the counts; moderate credence on the runtimes, which come from docs only.**

Overall judgment: there was a coherent vision, and it fit the computational half of tax law very well. It did not fit the interview half. That half was left as free prose and hand-ordered data outside the verified model. After the 2026-10-16 pivot from proof of concept to an 80%-coverage product, the architecture was not revisited. Gaps that became visible in Stages 8 to 21 (person and collection joins, months, dates, applicability) were absorbed by helpers, duplicated blocks, generator special cases and new checkers, rather than by changes to the model.

---

## 1. The layers, as built

These are verified against the tree. `PROJECT_INDEX.md` and `README.md` were read as testimony; the index is 46 KB, and many rows are paragraph-length descriptions of tool behaviour.

| Layer | Path | Tracked files | First added | What it is |
|---|---|---:|---|---|
| Sources | `sources/2025/` (+`2024`, `2026` drafts, `ny/2025`) | 1,724 | 10-13 | IRS PDFs and HTML; per document `<id>.txt` (pdftotext -layout), `<id>.cols.txt` (reading order), `<id>.pages.json`; a manifest with hashes; catalog `tools/sources-2025.json` |
| Form data | `forms/2025/*.yaml` (61 files), `forms/ny/2025/` | 68 | 10-14 | Lines with `id`, `printed`, `label`, `type`, `expr` (an atom tree), `cite`, optional `refuses`, and `gated_by` (since 11-06) |
| Parameters | `params/2025.yaml` | 2 | 10-14 | 282 values and 28 **enums**. Enum types are defined in the year-parameter file. |
| Tables | `tables/2025/` | 39 | 10-14 | Tax Table, EIC tables, MACRS and PTC tables; extracted by tools and checked cell by cell |
| Ambiguities | `ambiguities/2025.yaml` + `research/` memos | 3 | 10-14 | Readings chosen where the instructions are silent |
| Schema | `schema/data.schema.json` | 1 | 10-14 | Grew from 257 lines to 1,588. 19 commits; the 261→1,217 jump at `e61ed50f` was a reformat. |
| Build/check | `engine/src/build.ts`, `check.ts`, `gates.ts` | | 10-14 | YAML to `canonical/` (git-ignored); static checks: references, acyclicity, types, exhaustive and disjoint `choose`, citations |
| Renderer | `engine/src/render.ts` → `rendered/2025/*.md` (committed) | 112 | 10-14 | English rendering of each line beside its IRS label |
| Evaluator | `engine/src/eval.ts` | | 10-14 | Lazy and memoized; refusals and unknowns as values |
| Lean | `lean/TaxFormalization/{Atoms,Lemmas,Eval,EvalProps}.lean` | 9 | 10-14 | 1,948 lines; a reference evaluator over the same canonical JSON; compared in `check-all` |
| Interview | `interview/questions-2025.yaml` (577 questions, each with a hand-set `order`), 4 federal profiles, NY bank | 10 | 10-14 | The asked set is derived from reachability; order, help and frames are authored |
| CLI / server / UI | `engine/src/main.ts`, `serve.ts`, `ui/` | 5 (ui) | 10-14 / 11-06 | CLI-as-backend held; the UI added on 11-06 holds no tax logic, as designed |
| Fixtures | `fixtures/2025/stage{1..21}.json`, `classm*.json`, `mutation.json`, `differential/` | 28 | 10-14 | Organized **by build stage (time), not by form** |
| Reviews | `reviews/2025/{transcription,render,classm,screens,completeness,false_no,...}` | 833 | 10-14 | Model-review logs, rulings, triage, adjudication; ~1.0 GB of raw review data in git-ignored `.transcription/` |
| Reports | `reports/2025/` (committed, generated) | 89 | 10-14 | Coverage, evidence, mutation, differential, etc. |
| Tools | `tools/` | 149 | 10-13 | See §4 |

The day-1 diagram (`spec/design.md` §1) still describes the dataflow correctly. What the diagram does not show is the size of the evidence layer: reviews, fixtures and reports make up most of the repository's churn.

### 1.1 End-to-end trace: Form 8889 (HSA)

The trace uses the files that define it or check it, from `/tmp/f8889files.txt`: 361 tracked non-source files mention `f8889`.

- **Sources:** `sources/2025/{f8889,i8889}.{pdf,txt,cols.txt,pages.json}`; catalog entry in `tools/sources-2025.json:427`.
- **Definition:** `forms/2025/f8889.yaml` (1,965 lines, 19 commits, first added `0b3939ec` on 10-18). The per-person frame lives in `forms/2025/person.yaml`, for example the collection `f8889` at lines 272 and 296. The consumers are `forms/2025/s1.yaml` and `s2.yaml`.
- **Parameters and types:** `params/2025.yaml` holds the enums `hsa_allocation`, `hsa_coverage` and `hsa_year_coverage` (lines 63–78) and values such as `hsa.additional_rate` (1392) and `hsa.no_last_month` (1609, a `Bool false` constant that exists to serve as a `choose` alternative).
- **Ambiguities:** 12 mentions in `ambiguities/2025.yaml`.
- **Interview:** `interview/questions-2025.yaml` (frame `f8889`, orders, help), plus `conflict_checks-2025.yaml`, `gate_frequencies-2025.yaml`, `sales-2025.yaml` and `stage4-2025.yaml`.
- **Engine code with form knowledge:**
  - `engine/src/generate.ts` lines 21, 36, 511, 672–705, 823 (HSA roots and spouse coherence).
  - `engine/src/hsa-calendar.ts`, 37 lines added `9bb82055` on 10-26: a generator-only calendar model.
  - `engine/src/serve-check.ts:285`.
  - `engine/src/mutate.ts` lines 1898–1947: several hand-written prose equivalence arguments. Each pins the line ids and a content hash.
- **Rendered:** `rendered/2025/f8889.md`, plus index, params, person, s1 and s2.
- **Fixtures:** stage11, 13, 16 and 21 with values. Every whole-return fixture carries `$f8889@person[taxpayer]`. Also `classm.json`, `classm.deepseek.json` and `mutation.json`.
- **Reviews (14 tracked files):**
  - transcription log and rulings, triage (2 files), adjudication;
  - render logs (Claude and DeepSeek, each with rulings);
  - class M logs (Claude and DeepSeek, each with rulings);
  - `false_no/f8889.json`;
  - entries in screens, completeness and `tools/transcription/input_contracts/2025`.
- **Other:** engine adapters (`tools/engines/ustaxes_adapter.py`, `test_compare.py`), `tools/coverage/tree.json`, `tools/human_review/reading_list.json`, and 33 report files.

Two observations from this trace:
- `f8889.zero` is a helper that wraps the parameter `sales.zero`. That parameter is referenced 143 times across 45 form files. Form 8889 depends on a parameter named for the sales slice only because a `choose` alternative must be a line id (§2.3).
- The `label` (the IRS line text) and the input `source` (the question prompt) are written separately for each input. That is correct in principle. In practice they are long parallel prose; the `f8889.unsupported` screen prompt is about 1,500 characters.

### 1.2 Form 5695 and Schedule B

- `forms/2025/f5695.yaml` (2,242 lines, first added on 10-22 in the Stage 15 commit `8d7c0fdc`): 4 transcription files, 4 render files, 4 class M files, 2 triage files and 1 adjudication file. `engine/src/generate.ts` mentions f5695 32 times, more than any other form apart from `person` (65). Its inputs (`f5695.part1_any`, `part2_any`) appear in every stage fixture from stage1 to stage21, including `stage1.json`, the Tax Table / QDCG slice, which has nothing to do with energy credits. Each of `stage1.json`'s 60 cases now carries 105 inputs.
- `forms/2025/sb.yaml` (356 lines): the same review set. Its readers include `engine/src/compare.ts` and `fixtures.ts`, as well as the forms `div.yaml`, `f1040.yaml` and `params`.

So, for the three forms traced, a form is spread over about 12 to 15 distinct artifact kinds, and 4 to 5 of them are hand-maintained in parallel: form YAML, question bank order and help, generator code, mutate equivalence arguments, fixture inputs.

---

## 2. Fit to the problem

### 2.1 Where the shape matches tax law (evidence it was well chosen)

- **Forms referencing forms:** line ids `<form>.<name>`, `copy` and operands, and an acyclic graph checked at build. Atom usage over 3,071 lines: 2,845 `test`, 568 `input`, 425 `choose`, 294 `sum_over`, 271 `copy`, 227 `param`, and so on. 0 `opaque`. **High.**
- **Year parameters:** one params file per year with citations, `years.json`, and `--year` threaded through every tool. Year adoption tooling (`year_diff.py`, `fixtures_year.py`) was built 10-20/21 and rehearsed against 2026 drafts. **Moderate–high** (rehearsed, not yet exercised on a final year).
- **Refusals and unsupported cases:** refusal as a value, with 265 `refuses:` entries, and a coverage tree that places every gate (`tools/coverage/tree.py`, `docs/COVERAGE.md`). **High.**
- **Citations:** a structured `cite` on every line, checked verbatim against the archived text by `tools/citations.py` (1,319 lines). **High.**
- **Independent evaluators:** the TypeScript and Lean evaluators agree, as the design required. One caveat from the 11-01 tech-debt audit (§3.2) is now at least partly stale: `Eval.lean` imports `Atoms` and calls `prorate` and `subtractFloor0`.

### 2.2 Where the shape fights the problem

1. **Applicability and existence ("does this form or amount apply to you?") had no representation until 11-06.**
   - *Observations:*
     - Day-1 spec §4.6 defines a gate only as path selection or refusal.
     - `docs/2026-11-06_formal_gates_design.md` ("What the evaluator already does") states that a gate hides an input only when every reader of that input sits under a `choose` on the gate.
     - The 165/142 measurement above.
     - No earlier measurement of interview length was found in docs before HEAD on 11-05. This was a grep search; it does not prove absence.
   - *Interpretation:* the interview was exercised through fixtures and generators, which "supply answers directly, so wording never moves a tested value" (root-cause doc, class Q). As a result, the verification stack was blind to the interview's main product property until a human-facing UI existed.
   - *Was it foreseeable?* Yes. The spec's own words, "decides which forms apply", say so. Direct File's Fact Graph, cited in the README as prior art, models exactly these existence facts. **Moderate–high credence that this was foreseeable at design time.**
2. **Natural-language legal predicates as Bool inputs.**
   - *Observations:*
     - 11 `*.unsupported` screens and 23 `(screen)` lines.
     - 54 of 568 input prompts are over 800 characters.
     - Bug class Q (30 bugs, 26 value-affecting) is the largest class.
     - Tags `question-incomplete` (31) and `scope-screen-narrower-than-line` (25) across 458 bugs.
     - The structured-question-text change came on day 25 (`b66f4ea6`: 50 files, +2,358/−398).
   - *Interpretation:* the model is precise about arithmetic and imprecise about the facts it consumes. The verification regime (render review, screen review, completeness review, false-no review) grew around this soft boundary instead of the boundary being formalized.
3. **Person and dependent dimension.**
   - *Observations:*
     - `forms/2025/person.yaml` is 4,782 lines and holds per-person lines for many forms (ira 63 ids, edu 34, sav 18, sep 15, ...).
     - The Form 8863 student block is duplicated: `person.yaml:3487–4072` (585 lines) and `dependent.yaml:1773–2372` (599 lines). This was verified today.
     - The tech-debt audit (§5.1) attributes this to sibling sub-collections being unable to join except through the parent collection.
   - *Interpretation:* Stage 8 was planned explicitly as the "household architecture test" (design §5). It passed on the `opaque` metric, but the collection model's limits were absorbed by duplication. **Moderate.**
4. **Time within the year (months, dates).**
   - *Observations:*
     - The spec lists `Date` as a type, but the schema has none; verified, there is no `Date` in `schema/data.schema.json`.
     - Month calendars are unrolled: in `f8962.yaml`, 24 `show_<month>` / `show_<month>_calc` ids; `f1095a.yaml` is 1,158 lines.
     - The HSA calendar logic exists only in the generator (`hsa-calendar.ts`).
   - *Interpretation:* a month-indexed collection or a date type would have matched HSA, PTC and dependent-month rules. **Moderate.**
5. **Atom operand asymmetry.**
   - *Observations:*
     - 1,755 of 3,071 lines (57%) are `(helper)`.
     - 206 helpers simply wrap a `param`.
     - `sales.zero` is used 143 times.
     - `choose.then` and others require line ids (tech-debt audit §5.2, consistent with the `f8889.zero` pattern verified above).
   - *Interpretation:* more than half the "lines" are scaffolding the IRS never printed. That inflates review, mutation and rendering volume. The `printed` field is overloaded: it holds markers such as `(helper)`, `(gate)` and `(screen)` as well as worksheet labels such as `(CLW B 7)` and `(SMW 4)`. The audit found five divergent marker definitions on 11-01, since consolidated into `util.ts:24` `HELPER_MARKERS`. **High on the counts, moderate on the cost interpretation.**

---

## 3. Accretion: designed up front versus bolted on

| Structure | First appears | Day-1 design? | Forced migration? | Foreseeable? |
|---|---|---|---|---|
| Atom DSL, YAML to canonical, cite, refusals, Lean, CLI backend | 10-13/14 | Yes | No | n/a. Held. |
| Five new atoms | 10-17 to 10-22 (`d3935b40`, `64f50513`, `6051ec00`) | Partly (vocabulary "frozen", then extended) | Small | Mostly. keyed/rate lookups for depreciation and PTC tables. |
| Verification by model transcription / render / class M | Spec amendment `7b60e465` (10-16); tools 10-16/17 | **No.** Day 1 assumed human class B. | Every form got review logs | Partly; it became policy on 10-24 |
| Human-review tooling (`tools/human_review/`, 11 files, 2,790 lines) | 10-22 to 10-24 | Implied by "a person works by hand" | No | Made optional on **10-24** (`735e6442`), the same week it was built. Only 3 human logs exist (`reviews/2025/human/{f1040,person,sa}.md`). |
| Source-coverage checks (operands, signs, consumers, limits, instruction_cites) | 10-30 | No | Baselines for every form | After the fact; prompted by the 10-29 root-cause analysis |
| Jurisdiction (NY) | 11-05, `bdac4121` (239 files, +255k lines) | **No.** "State returns" was a day-1 non-goal; restored as an intent on 10-19 (`2587c1b4`). | 36 Python tools gained `--jurisdiction`; 19 `ny_*` check-all steps; asymmetric paths (`forms/2025` vs `forms/ny/2025`) | Foreseeable from 10-19 at the latest |
| Release tiers, pre-push, worker pools | 11-05/06 (`e2adfe68`, `cb5e58ff`) | No | n/a | Driven by check-all runtime |
| Web UI / `serve` | 11-06 (`814a1ea7`) | Yes as "a later client" (design §2.8) | Question wording "without entry syntax" | Yes; the CLI-backend rule held, which is to the design's credit |
| Topic layer, then **formal gates** (`gated_by`, `choose` with Bool, one gate line per input, "keep the id") | 11-06/07 | Gate concept yes; existence gates no | Ongoing: 25 inputs gated, 321 baseline leaks; one dividends gate touched 153 files | **Yes** (see §2.2.1). "Keep the id" (owner, 11-07) was chosen precisely to avoid reworking fixture keys and refusal ids, which is itself evidence that the fixture coupling was felt. |
| Structured question text | 11-07 (`b66f4ea6`) | No | 50 files | Plausibly; long screen prose was flagged as early as BUG-0032 (25 screens reworded) |
| `worktree_data.py` (clone git-ignored review data into agent worktrees) | 11-07 | No | n/a | Follows from keeping ~1 GB of load-bearing review data outside git |

Stage-shaped residue that is still live:
- Fixtures are named `stage1.json` … `stage21.json`.
- The profiles `2025.yaml` (Social Security slice), `sales-2025.yaml` and `stage4-2025.yaml` remain, and `build.ts` reads them.
- `check-all` still runs `review-stage2` … `review-stage5` (`tools/check_all_steps.sh`, wave 3).
- The header comment of `mutate.ts` still says "the Stage 1 data".

The organizing unit of the evidence is the build episode, not the form. That is why one form's evidence is scattered across up to 18 fixture files.

Growth of the core files from first commit to now: `eval.ts` 415→827 (20 commits); `check.ts` 872→1,269; `build.ts` 176→467; **`mutate.ts` 238→2,557 (37 commits, the most-changed engine file)**. The verification harness grew about 10×, while the evaluator grew 2×.

---

## 4. Tooling sprawl

- **Inventory:** 120 script files in `tools/` (95 .py, 13 .mjs, 11 .sh, 1 .swift; 31,398 lines). By subdirectory: `transcription/` 58 tracked files, top level 52, `engines/` 13, `human_review/` 11, `coverage/` 7, `hooks/` 4, `extraction/` 4.
- **Load-bearing versus not** (`scratch04/toolref.txt`: check-all membership and referrer counts):
  - About 41 scripts run in `check-all`.
  - About 30 are paid-review or run-on-demand drivers: `transcribe.py` (2,450 lines), `screen_review.py`, `completeness_review.py`, `classm.py`, `render_compare.py`, `false_no_review.py`.
  - About 15 are extractors and engine adapters.
  - At least 4 are visible one-offs or migrations: `migrate_line_subjects.py`, `migrate_completeness_debt.py`, `completeness_debt.py`, `ocr_audit.py`.
  - `tools/structured_text.py` (added 11-07) has no referrer outside itself in the searched paths. That may be a search artifact.
- **check-all organization:** `tools/check_all_steps.sh` runs compile, then build and render, then three parallel waves. It has 90 steps; about 38 are self-tests or tool tests; 19 are `ny_` duplicates of federal steps under `--jurisdiction ny`. There are three tiers (`full`, `fast`, `docs`), selected by `tools/tier_paths.py` and enforced by `tools/hooks/pre-commit` and `pre-push`. The pre-commit hook requires a green check-all on the **exact tree**; it was introduced 10-17 (`290d550d`) and tiered on 11-05. The script's own header notes: "Nothing checks these rules [wave placement]; a new step must be placed by them."
- **Step count over time:** 24 (10-21), 33 (10-26), 41 (10-29), 52 (10-30), 56 (10-31), 63 (11-04), 80 (11-05, NY), 90 (11-07).
- **Runtime (testimony):**
  - about 7 min (`handoffs/HANDOFF-INTEGRITY.md:517`);
  - about 15 min ("mutation is most of it"; `HANDOFF-HARDENING-1.md:93`);
  - about 25 min (`docs/2026-11-04_process_optimization.md:190`);
  - about 38 min full, fast about 11 min (`docs/2026-11-05_release_gating_design.md:46`).
  - The last local timings in `.git/check-all-times` are mutate 713 s, engine_differential 547 s, compare 309 s, test_fixtures 257 s, test_integration 147 s.
- **Overlap.** These are verified by locating the classes and functions; the counts come from the tech-debt audit and were spot-checked:
  - A second evaluator in Python: `tools/engines/compare.py:311 UnroundedModel`.
  - A second renderer: `tools/human_review/reading.py:236 Reading`.
  - An AST normalizer: `tools/transcription/transcribe.py:1271 Expander`.
  - 20 tool files load the source manifest.
  - Several audit items have since been fixed: `HELPER_MARKERS` unified, `PRIMITIVE_OPS` removed, the hardcoded standard deduction gone from `compare.ts`, the generic help placeholder gone. The audit is therefore partly stale testimony.
- **Interpretation:** the tooling is mostly load-bearing, not dead weight. But it is organized around review *events* (one checker per bug class that surfaced) and not around a shared library over canonical JSON. The language split (evaluator in TS; review and check tools in Python reading canonical JSON) caused the reimplementations. **Moderate–high.**

---

## 5. Duplication and coupling

| Fact | Encoded in | Kind |
|---|---|---|
| Which inputs exist | form YAML `input` lines; `questions-2025.yaml` (577 entries with hand `order`); 3 legacy profiles listing inputs explicitly (54 / 332 / 358 inputs per the audit); `generate.ts`; `tools/engines/generate_cases.py`; `input_contracts/`; every whole-return fixture | 5–7-way ripple; the project names it "input ripple" in `CLAUDE.md` and assigns it to Sonnet agents |
| A line's meaning | YAML `expr`; `label`; input `source`; committed `rendered/`; review logs pinned by subject hash; `mutate.ts` prose equivalence arguments (48 `pinned(` entries holding line ids and hashes) | Generated and pinned copies; a form edit invalidates the reviews (by design) and can invalidate pinned arguments |
| Form-specific knowledge "below the data layer" | `generate.ts` (f5695 ×32, household ×28, …), `hsa-calendar.ts`, `mutate.ts` equivalence provers, `serve-check.ts` | Contradicts design §2.5 ("contains no form-specific code") outside the evaluator proper; the evaluator itself stays clean |
| Student eligibility (8863 Part III) | `person.yaml` and `dependent.yaml` | ~590-line near-duplicate |
| Project/tool descriptions | `PROJECT_INDEX.md` (46 KB), `README.md` (512 lines), `docs/TRUST.md`, `docs/COVERAGE.md` (174 KB, generated), `spec/spec.md` (grown 281→522 lines, 36 commits) | Prose duplicates of code behaviour; drift risk (root-cause class D, 8 bugs) |
| Review data | ~1.0 GB in git-ignored `.transcription/`; `check_logs.py` fails if a referenced raw file is missing | Required `worktree_data.py` (442 lines) and a standing owner rule |

Measured ripple:
- Across 79 commits touching `forms/2025`: 717 authored-data file changes, 5,903 derived or evidence file changes, 558 code file changes.
- 15 commits each touched 11 to 18 stage-fixture files (`scratch04/fixripple.txt`). Examples: `a428e8bb` Stage 21 (18), `1075bb5c` dividends gate (17), `2d971adf` Stage 18 (15).

---

## 6. What a clear up-front design would have changed (counterfactual, low–moderate credence)

1. **Model applicability and existence facts as first-class data from Stage 2:** a Bool fact per form or amount family, cited, with the interview's reachable set computed through it. That is also where Direct File's fact graph sits. Interview length would then have been a measured property from the first full profile (Stage 5) instead of a day-24 discovery. It would probably also have absorbed part of bug class Q.
2. **Make fixtures partial and per-form.** Unspecified inputs would default by rule, with whole-return fixtures kept as a separate, small set. Then a new form would not rewrite `stage1.json`, and "keep the id" would not be needed to protect fixture keys. Organize fixtures and evidence by form, not by stage.
3. **Widen the atom operand positions** (allow `param`/`const` where line ids are required now) and add month-indexed collections and a `Date` type. Expected effect: fewer of the 1,755 helpers and of the unrolled calendars.
4. **Build one shared library over canonical JSON** (AST walker, manifest, locator parser, log parser), used by both TS and Python. Or keep all checkers in TS.
5. **Decide jurisdiction in the layout on 10-19** (`forms/us/…`), when NY was restored as an intent, and not by a flag retrofit on 11-05.
6. **Keep the evidence store versioned or content-addressed** from the start, instead of 1 GB of load-bearing, git-ignored raw logs.

Disconfirming considerations:
- (a) Several of these items (partial fixtures, existence facts) trade away some guarantees that the project chose deliberately, such as total-input fixtures that catch reachability leaks. Simpler is not automatically better here.
- (b) The core DSL bet paid off decisively, so the up-front design effort was not wasted.
- (c) The post-10-16 scope pivot changed the problem's size. A design sized for a 5-stage proof of concept would reasonably not include month arrays or existence facts. The failure was not re-designing at the pivot, more than not designing on day 1.
- (d) The 11-06/07 formal-gates work shows the architecture *can* absorb the fix without a rewrite. The evaluator needed only "choose takes Bool" (`a061e282`, 10 files).

---

## 7. What I could not determine

- Agent-hours or cost per architectural change. That belongs to the logs investigator.
- Whether the 165-question interview length was observed and accepted earlier through the CLI interview. My grep of pre-11-05 docs found no measurement; that is not proof.
- Actual check-all runtimes before 11-06 beyond the docs' approximations. `.git/check-all-times` holds only the latest run.
- Whether the 321 interview-rule baseline entries map one-to-one onto inputs needing gates. Only the top-level count was read.
- Referrer counts in `scratch04/toolref.txt` come from a basename grep and are approximate. For example, `human_review/logs.py` is overcounted because `check_logs.py` matches its name.
- The tech-debt audit (`docs/2026-11-01_tech_debt_audit.md`) is model-written testimony from 11-01. I verified 9 of its claims: 4 have since been fixed, and 5 still hold (edu duplication, no Date type, Python reimplementations, the `mutate.ts` form-specific provers, the stage-named profiles and review steps). Its other claims are cited above only where re-checked.
