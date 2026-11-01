# Technical Debt Audit — 2026-11-01

> **Status (`T-152`):** Initial audit report. Every finding below needs to be verified for accuracy against the codebase, separated from already-tracked tasks, and prioritized before acting on the items worth fixing.

---

## Executive Summary

The repository (~29,200 LOC of TypeScript, Lean 4, Python, MJS, and Bash, plus 62 YAML form definitions and 1,994 test cases) has strong mechanical guardrails, but rapid stage-by-stage expansion (Stages 0–21) and reactive hardening have accumulated structural technical debt across six areas:

1. **7 active or latent bugs** in the evaluators, renderer, mutation engine, and build/hook scripts (including polluted memoization keys in both TS and Lean evaluators, 20 misrendered `(screen)` lines in `rendered/2025/*.md`, and 22 of 38 `check-all` steps silently ignoring `--year`).
2. **High internal duplication**, including **4 evaluators/AST expanders** written across TypeScript, Lean, and Python; **13 separate AST walkers**; **5 divergent helper-marker lists**; and **7+ re-implementations** of manifest/YAML/canonical loaders and markdown review parsers.
3. **Tightly coupled data & test infrastructure**, where adding one tax input requires touching 5 subsystems and every historical fixture file, and where `generate.ts` uses 4 post-hoc hash-stream patches to avoid shifting a single global `fast-check` PRNG seed.
4. **Hardcoded 2025 assumptions** across extractors, checkers, mutation equivalence provers, and engine adapters that will break when adopting TY2026.
5. **736 suppressed baseline items** across `reviews/2025/*.json` and **78 of 149 pending paired model reviews** held behind ratchets.

Of the **37 distinct findings** documented below, **12 are tracked** (8 directly, 4 partially) in `TASKS.md` and **25 are untracked** (see [Section 7](#7-cross-reference-with-tasksmd)).

---

## 1. Active Bugs & Latent Correctness Defects

### 1.1 Cross-Document Memo Key Pollution in Both Evaluators (`eval.ts` & `Eval.lean`)
* **Where:** `evalLine` in `engine/src/eval.ts:169-193` and `evalLine` in `lean/TaxFormalization/Eval.lean:300-313`.
* **Issue:** Both evaluators compute `const key = canonicalKey(frame, lineId)` **before** checking whether `lineId` belongs to the current collection `frame.doc` or is a cross-document reference (e.g., a line inside `person[taxpayer]` or `person[taxpayer].f8606[form]` referencing `f1040.status`, `ira.joint`, or `person.ira_nondeductible`). When the recursive call returns, the outer call caches the result in `ctx.memo` and `ctx.derivations` under a bogus composite key such as `person[taxpayer].f8606[form].person.ira_nondeductible` or `person[taxpayer].ira.joint`.
* **Impact:**
  1. Redundant re-evaluation of top-level/parent lines once per collection entry before hitting the top-level memo key.
  2. Bogus keys leak into `result.derivations`, `resultToJson()` (`eval --json`), and the `Derivations:` section of user-facing values sheets (`engine/src/output.ts:79-94` — visible in `reports/2025/stage5.return.owed.txt:285-535`).
  3. Both `compareCase` in `engine/src/compare.ts:149` and `evalCase` in `lean/Main.lean:161` export every memo key containing `"["`, accidentally comparing these internal cross-document alias keys alongside real collection lines.

### 1.2 Missing `"(screen)"` Helper Marker in `render.ts` (20 Misrendered Lines)
* **Where:** `HELPER_MARKERS` (`engine/src/render.ts:64`) and `lineName` (`engine/src/render.ts:66-74`).
* **Issue:** `engine/src/check.ts:23` (`HELPER_PRINTED`) and `engine/src/classm.ts:42` (`HELPER_MARKERS`) include `"(screen)"`, but `engine/src/render.ts:64` omits `"(screen)"`. Because `"(screen)"` starts with `"("`, `lineName()` falls into the `line.printed.startsWith("(")` branch intended for table columns like `(a)`.
* **Impact:** All **20 lines** with `printed: (screen)` across `rendered/2025/asset.md:16`, `rendered/2025/ira.md:129`, `rendered/2025/person.md:975`, `rendered/2025/sc.md:22`, and `rendered/2025/scveh.md:16` are rendered in committed Markdown as `### column (screen) (sc.ho_uses)` instead of `### helper "..."`.

### 1.3 `tools/check_all_steps.sh` Drops `"$@"` (`--year`) on 22 of 38 Steps
* **Where:** `tools/check_all_steps.sh:3-110`.
* **Issue:** Line 3 states *"every step receives the same arguments"*, but 22 step invocations (lines 73, 76–79, 81, 88, 90–103, 107, 109, 110 — including all source-coverage checks `instruction_cites`, `operands`, `signs`, `screen_currency`, `consumers`, `limits`, `completeness`, `refusal_reach`, and `check_ptc_tables`) omit `"$@"`.
* **Impact:** Running `./tools/check_all.sh --year 2026` silently executes those 22 checks against default tax year 2025.

### 1.4 Incomplete AST Traversal in `mutate.ts` Operand Mutator
* **Where:** `collectOperandTargets` (`engine/src/mutate.ts:96-116`) and `replaceOperandTarget` (`engine/src/mutate.ts:118-140`).
* **Issue:** The operand-replacement mutator handles `sum`, `smaller_of`, `larger_of`, `subtract`, `subtract_floor0`, `multiply_rate.amount`, `multiply_count`, `round`, `prorate.{amount,part}`, `percent_floor.part`, `keyed_lookup`, and `rate_lookup`, but **omits** string line references in:
  * `multiply_rate.rate` (when `typeof expr.rate === "string"`)
  * `prorate.whole` (when `typeof expr.whole === "string"`)
  * `percent_floor.whole` (when `typeof expr.whole === "string"`)
  * `table_lookup.key` and `table_lookup.status`
  * `choose` branch `then` targets and `test` operands
* **Impact:** Operand-replacement mutants are never generated for those expression positions, inflating the reported mutation score on lines using those operations.

### 1.5 Unfiltered Directory Scan in `differentialClassC`
* **Where:** `differentialClassC` (`engine/src/differential.ts:147-154`) vs. `differential` (`engine/src/differential.ts:110-113`).
* **Issue:** `differential()` checks `Array.isArray(raw)` and `raw.every(r => r && typeof r.calculator === "string" ...)` to skip non-calculator files in `fixtures/<year>/differential/` (specifically documented in the header comment at `engine/src/differential.ts:108` and `PROJECT_INDEX.md:81` for `engine_investigations.json`). `differentialClassC()` reads every `.json` file in that directory without filtering and immediately accesses `Object.keys(rec.values)`.

### 1.6 `pre-push` Hook and `green.sh` Commit-Guard Gaps
* **Where:** `tools/hooks/pre-push:2-19`, `tools/green.sh:20-25`, and `tools/check_all_bg.sh:118`.
* **Issues:**
  1. `tools/hooks/pre-push:2` claims it *"Refuses a push unless the tree of every commit being pushed to a ref passed a green check-all run"*, but line 15 only checks `$local_sha^{tree}` (the tip commit), ignoring untested intermediate commits in `$_remote_sha..$local_sha`.
  2. `record_green` (`tools/green.sh:20-25`) reads and overwrites `.git/check-all-green-trees` via `tail -n 49` + `mv` without file locking, risking lost entries if a foreground and background run finish concurrently.
  3. `tools/check_all_bg.sh:118` runs `git commit-tree "$tree" -p "$base" -m "check-all snapshot"` on every run, accumulating unreferenced dangling commits in `.git/objects`.

### 1.7 `archive_text.py` Self-Test Regex Bypassed by `extract_ptc_tables.py`
* **Where:** `_self_test` (`tools/archive_text.py:89-93`) vs. `tools/extract_ptc_tables.py:27-35`.
* **Issue:** `archive_text.py --self-test` enforces that no tool reads `sources/<year>/*.txt` directly (bypassing draft-cover/watermark stripping) by matching variable names against `r"text_file|cols_file|\bARCHIVE\b|\bSOURCES\b|self\.sources\b"`. Because `extract_ptc_tables.py` names its path constant `SRC = ROOT / "sources" / "2025"` and calls `(SRC / f"{doc}.{layer}").read_text()`, it silently bypasses both `archive_text.py` and its self-test.

---

## 2. TypeScript Engine (`engine/src/`) Architectural & Code Debt

### 2.1 Five Divergent Definitions of Helper vs. Printed Line Markers
There is no shared `isHelperLine(line)` predicate in `engine/src/types.ts` or `engine/src/util.ts`. Instead, five files define their own rules:
1. `engine/src/check.ts:23`: `new Set(["(helper)", "(gate)", "(computed helper)", "(question)", "(status)", "(screen)"])`
2. `engine/src/classm.ts:42`: `new Set(["(helper)", "(gate)", "(computed helper)", "(question)", "(status)", "(screen)"])`
3. `engine/src/render.ts:64`: `new Set(["(helper)", "(gate)", "(computed helper)", "(question)", "(status)"])` *(missing `"(screen)"`)*
4. `engine/src/mutate.ts:328` & `:428`: `line?.printed === "(helper)"` *(ignores `(computed helper)`, `(gate)`, `(screen)`, etc.)*
5. `engine/src/build.ts:244`: `String(l.printed).startsWith("(")` *(conflates helper markers with parenthesized worksheet/column numbers like `(CLW A 1)` or `(a)`)*

### 2.2 Six Separate `Expr` / `TestExpr` AST Walkers in `engine/src/`
Instead of a single typed visitor in `engine/src/types.ts`, AST reference walking is implemented six times in `engine/src/` (plus seven more times in `tools/*.py`):
1. `engine/src/build.ts:234-238`: untyped object walk skipping `["cite", "source", "label", "op", "ref"]`.
2. `operandRefs` (`engine/src/mutate.ts:250-258`): untyped object walk skipping `["ref", "collection", "const", "cite", "type", "op", "unit", "rule", "source", "label"]`.
3. `operandRefsLocal` (`engine/src/mutate.ts:858-866`): untyped object walk adding `"param"` to the skip list.
4. `collectRefs` (`engine/src/check.ts:644-713`): typed `switch` over `expr.op`.
5. `walk` (`engine/src/classm.ts:45-71`): typed `switch` over `expr.op` (which still includes dead `case "bracket_schedule"` at line 54).
6. `collectOperandTargets` (`engine/src/mutate.ts:96-140`): incomplete `switch` (see §1.4).

### 2.3 Five Copy-Pasted Collection-Key Stripping Regexes (`templateKey`)
Stripping collection instance keys (`person[taxpayer].w2[a].box1` → `w2.box1`) is duplicated five times in `engine/src/` with subtly different regexes (`[^\]]+` vs `[a-zA-Z0-9_-]+`, `*` vs `+`):
* `templateKey` in `engine/src/branches.ts:8-10`
* `questionTemplate` in `engine/src/interview.ts:21-24`
* `engine/src/interview-check.ts:18`
* `engine/src/fixtures.ts:184` *(even though `fixtures.ts:14` already imports `templateKey` from `./branches.js`)*
* `engine/src/classm.ts:80`

### 2.4 Import-Time `process.argv` Mutation and Global `YEAR` Singleton (`year.ts`)
* **Where:** `resolveYear` (`engine/src/year.ts:16-46`) and `engine/src/mutate-worker.ts:6-7`.
* **Issue:** Importing `year.ts` mutates `process.argv` in-place (`argv.splice(...)`) and binds module-level constants `YEAR`, `CANON_DIR`, `FORMS_DIR`, etc. Because `YEAR` is fixed at module load time, `mutate-worker.ts:6-7` has to push `"--year"` onto `process.argv` before dynamically `await import("./mutate.js")`, and no tool can load two tax years in the same Node process.

### 2.5 Redundant & Stale Atom Sets (`atoms.ts`)
* **Where:** `VOCABULARY` (`engine/src/atoms.ts:5-27`), `IMPLEMENTED` (`engine/src/atoms.ts:29-49`), and `PRIMITIVE_OPS` (`engine/src/atoms.ts:51-73`).
* **Issue:** `VOCABULARY` and `PRIMITIVE_OPS` are identical sets of the same 21 strings in slightly different order (`PRIMITIVE_OPS` is unused in `engine/src/`). `bracket_schedule` and `opaque` remain in `VOCABULARY` and `engine/src/types.ts:76-86` even though `bracket_schedule` was replaced by `rate_lookup` and neither is in `IMPLEMENTED`.

### 2.6 Generator Fragility & PRNG Stream Coupling (`generate.ts` & `compare.ts`)
* **Where:** `engine/src/generate.ts:59-904` and `generatedCases` (`engine/src/compare.ts:31-104`).
* **Issues:**
  1. To keep the 400 generated returns from shifting their `fast-check` random stream (`SEED = 7`) as Stages 16–21 were added, `generate.ts` partitions inputs across five exclusion sets (`NOT_DRAWN` `:85`, `UNDRAWN` `:95`, `MODELLED` `:109`, `EARLY_ROOTS` `:118`, `FIXED` `:127`) and runs four separate FNV-1a/Mulberry32 post-processors (`putCarryovers`, `putPtc`, `putEdu`, `putEarly` at `:897-901`) that JSON-serialize and sort the entire `inputs` dictionary on every generated return to derive secondary PRNG streams.
  2. `engine/src/compare.ts:31-104` (`generatedCases`) maintains a **second**, completely separate 70-line LCG random return generator from Stage 2/3 that hardcodes 2025 standard deduction amounts (`1575000`, `3150000` at line 78) instead of importing `generate.ts`.

### 2.7 ~400 Lines of Form-Specific Equivalence Provers Hardcoded in `mutate.ts`
* **Where:** `EQUIVALENT_IF` (`engine/src/mutate.ts:515-625`) and structural equivalence helpers (`engine/src/mutate.ts:627-915`).
* **Issue:** Despite the architectural rule that *"nothing below the data layer contains tax rules"*, `mutate.ts` embeds ~400 lines of form-specific equivalence theorems (`s1aStepSkip`, `prorateSkip`, `thresholdAtPlateau`, `vehicle2019`, `s1aFigure`, `copyTargetMatch`) that hardcode 2025 form and line IDs (`scveh.is2019`, `sli.line8`, `eic.wsb_4b_positive`, `sdtw.line17`, `f8960.line8`, `person.eic_se`). Renaming or refactoring those lines silently breaks equivalent-mutant classification.

### 2.8 Legacy Stage 1–5 Scaffolding Hardcoded in Build, Interview & Fixture Runners
* `engine/src/build.ts:175-178` and `:253` hardcode 4 early interview profile filenames (`2025.yaml`, `sales-2025.yaml`, `stage4-2025.yaml`, `full-2025.yaml`).
* `checkInterviewPaths` (`engine/src/interview-check.ts:16, 53`) only tests interview order-invariance and completion against `stage2.json`, `stage3.json`, `stage4.json`, and `stage5.json`—ignoring `stage8.json` through `stage21.json`.
* `scopeNotice` (`engine/src/interview.ts:40-53`) inspects `config.targets` for `"f1040.line37"`, `"scope.ready"`, and `"f1040.line7a"` to select hardcoded stage prose.
* `recordFixtures` (`engine/src/fixtures.ts:23, 54-75`) hardcodes `stage1.json`, and `reviewStage2`–`reviewStage5` (`engine/src/fixtures.ts:474-572`) regenerate frozen Stage 2–5 review prose packets on every `check-all` run (`tools/check_all_steps.sh:122-125`).

---

## 3. Lean 4 Formalization Debt (`lean/`)

### 3.1 Untyped `Lean.Json` Evaluation & Silent `.getD` Fallbacks
* **Where:** `lean/TaxFormalization/Eval.lean:1-598` and `lean/Main.lean:1-195`.
* **Issue:** Unlike the TypeScript engine, the Lean reference evaluator does not parse canonical JSON into an inductive AST for `Expr`, `TestExpr`, `Line`, or `FormDoc`. It operates directly on raw `Lean.Json` nodes at every evaluation step, using `.getObjValD`, `.getStr?`, `.getInt?`, and silent default fallbacks (`.toOption.getD 0` or `.getD ""`, e.g., `Eval.lean:86-108, 219-263`).

### 3.2 `Eval.lean` Does Not Call Most Proved Functions in `Atoms.lean`
* **Where:** `lean/TaxFormalization/Eval.lean:420-506` vs. `lean/TaxFormalization/Atoms.lean:36-60` and `lean/TaxFormalization/Lemmas.lean`.
* **Issue:** `Eval.lean` calls `Atoms.multiplyRate`, `Atoms.multiplyCount`, `Atoms.prorate`, `Atoms.percentFloor`, `Atoms.roundVal`, `Atoms.tableLookup`, and `Atoms.rateLookup`, but **never calls** `Atoms.sumList`, `Atoms.sumOver`, `Atoms.subtract`, `Atoms.subtractFloor0`, `Atoms.smallerOf`, or `Atoms.largerOf`. Instead, it re-implements `+`, `-`, `max 0 (a - b)`, `min a b`, and `max a b` inline inside its monadic loop (`Eval.lean:433, 459, 479-480, 502`). Consequently, the lemmas proved in `Lemmas.lean` for those six functions do not apply directly to the code executed by `Eval.lean`.

### 3.3 Trivial `rfl` Tautologies in `EvalProps.lean` & Missing Monotonicity Lemmas
* **Where:** `lean/TaxFormalization/EvalProps.lean:22-60` and `lean/TaxFormalization/Lemmas.lean`.
* **Issues:**
  1. `eval_terminates` (`EvalProps.lean:26-28`), `eval_deterministic` (`:35-37`), and `eval_zero` (`:41-43`) are `⟨_, rfl⟩` / `rfl` tautologies true of *any* Lean function with a `Nat` fuel parameter (`stepBudget := 1000000`), not proofs that the tax line graph is acyclic or that `stepBudget` suffices.
  2. Contrary to `spec/spec.md:88` (*"Each atom is monotone or antitone in each argument, as tabulated"*), `tableLookup` has no lemma at all in `Lemmas.lean`, `prorate` and `percentFloor` lack antotonicity lemmas in `whole`, and `multiplyRate` lacks an antotonicity lemma in `rate.den` (`T-100`).

### 3.4 Evaluator Divergence D6 & Process-Spawning Bottleneck
* **Divergence D6 (`lean/TaxFormalization/Eval.lean:465-580`, `spec/spec.md:266`):** `Eval.lean` only accepts bare string line IDs in `prorate.whole`, `percent_floor.whole`, `multiply_rate.amount`, `round.of`, etc., whereas `schema/data.schema.json:684-736` and `engine/src/eval.ts:502-530` allow inline `{const}` or `{param}` operands.
* **Subprocess-per-case in `leanEval` (`engine/src/compare.ts:131-138`):** `compare.ts` invokes `spawnSync(LEAN_BIN, [tmpInput, "--year", YEAR_STR])` in a tight loop—spawning ~1,994 separate OS processes, each of which re-reads and re-parses every canonical JSON file from disk in `loadBundle` (`lean/Main.lean:16-70`)—instead of supporting a `--batch` mode like `engine/dist/main.js eval --batch`.

---

## 4. Python & MJS Tooling Debt (`tools/`)

### 4.1 Whole-Subsystem Re-Implementations in Python
Several complex TypeScript engine subsystems are re-implemented from scratch in Python:
1. **`UnroundedModel` (`tools/engines/compare.py:311-608`):** A 300-line Python re-implementation of the entire tax evaluator (`test`, `choose`, `copy`, `sum_over`, `prorate`, `round`, `keyed_lookup`, `rate_lookup`, `table_lookup`, collection frame resolution) using `Fraction`. Worse, it determines which branch or rate band the TypeScript evaluator took by regex-matching human-readable derivation note strings (`n.startswith("taken: ")` at line 495 and `r"band over (\S+) but not over (\S+)"` at line 590).
2. **`Reading` (`tools/human_review/reading.py:232-492`):** A second AST-to-English renderer written in Python alongside `engine/src/render.ts`.
3. **`Expander` (`tools/transcription/transcribe.py:725-932`):** A 200-line AST normalizer and helper-inliner in Python.
4. **`resolve` (`tools/fixtures_year.py:72-80`):** Re-implements `engine/src/fixture-inputs.ts` parameter-relative input resolution in Python.

### 4.2 Widespread Duplication Across Python & MJS Scripts
* **Import-time `sys.argv` mutation (`tools/taxyear.py:19-39`):** Like `year.ts`, `taxyear.py` mutates `sys.argv` on import, forcing every Python tool to manually manipulate `sys.path` and `import taxyear  # noqa: E402` before `argparse`. `tools/check_all.sh:15` and `tools/engines/run.sh:16` inline `python3 -I -c '... import taxyear; print(taxyear.Y)'` to parse `--year`.
* **`sources/<year>/manifest.json` loading (8 copies):** Duplicated in `tools/citations.py:130`, `tools/fetch_sources.py:85`, `tools/year_diff.py:124-125`, `tools/human_review/packet.py:183-185`, `tools/transcription/transcribe.py:65-68`, `tools/transcription/check_logs.py:30-31`, `tools/transcription/compare_families.py:227-229`, and `tools/transcription/input_contracts.py:35-36`.
* **Expression AST reference extraction (7 copies in Python):** Duplicated with different key blacklists/whitelists in `tools/check_consumers.py:41-48`, `tools/check_operands.py:55-63`, `tools/check_signs.py:29-40`, `tools/coverage/tree.py:53-62`, `tools/human_review/reading.py:208-229`, `tools/transcription/transcribe.py:205-239`, and `tools/transcription/completeness_review.py:126-136`.
* **Citation locator page parsing:** `tools/transcription/transcribe.py:85-142` (`locator_pages`, `heading_pages`, `secondary_pages`) re-implements citation locator parsing from scratch with its own regexes instead of importing `tools/citations.py:233-286`; `tools/human_review/pages.py:190-232` (`Locator.locate`) duplicates the segment dispatch loop from `tools/citations.py:482-538`.
* **`pdftotext -bbox-layout` parsing (4 copies):** Implemented via regex in `tools/extract_text.py:83-102`, `tools/extract_eic_table.py:57-68`, and `tools/extract_tax_table.py:42-59`, and via `xml.etree.ElementTree` in `tools/human_review/pages.py:42-54`.
* **Markdown review log & fenced YAML parsers (8 copies):** `## Lines` / `### ` / `| field | value |` parsing is re-implemented across `tools/transcription/rulings.py:76-156`, `tools/transcription/rule.py:24-60`, `tools/transcription/compare_families.py:39-83`, `tools/transcription/check_logs.py:86-100`, `tools/transcription/audit_skipped.py:26-34`, `tools/transcription/audit_transcription.py:27-53`, `tools/transcription/triage.py:27-39`, and `tools/human_review/logs.py:23-34`.
* **Duplicate `.mjs` contract harnesses:** `tools/transcription/model_candidate.mjs:59-83` and `tools/transcription/candidate_runtime.mjs:12-38` duplicate refusal gate validation and synthetic gate injection; `tools/transcription/check_adapters.mjs:6-17` and `tools/transcription/check_input_contracts.mjs:7-24` duplicate the batch evaluation loop.

### 4.3 Hardcoded 2025 Assumptions & Personal Username in `tools/`
* **`tools/extract_ptc_tables.py:27-29`:** Completely ignores `taxyear.py`, hardcoding `"2025"` paths, 2025 `i8962` 0-based page indices (`[10]`, `[7]`, `[8]`), and `"fr-2024-00796.txt"`.
* **Hardcoded 2025 PDF page ranges & coordinates:**
  * `tools/check_instruction_cites.py:41-42`: `PARTS = {"f1040": (1, 87), "f1040s1": (88, 100), "f1040s1a": (101, 110), "f1040s2": (111, 114), "f1040s3": (115, 999)}`.
  * `tools/extract_eic_table.py:39-45`: `FIRST_PAGE, LAST_PAGE = 49, 60`, 20 fixed x-coordinates, and `END = 68700` (the 2025 EIC ceiling).
  * `tools/extract_tax_table.py:34`: `FIRST_PAGE, LAST_PAGE = 68, 79`.
  * `tools/extract_class_lives.py:29` & `tools/transcription/transcribe_tables.py:47`: `p946` pages `99..108` and `[71, 72, 73]`.
* **Hardcoded 2025 tax parameters in engine adapters:**
  * `tools/engines/generate_cases.py:236` and `tools/engines/ots_adapter.py:297` hardcode 2025 HSA limits (`855_000` / `430_000`).
  * `tools/engines/generate_cases.py:490-538` hardcodes `1_460_000` (2024 standard deduction) and `700_000` (2025 IRA limit).
  * `tools/engines/ustaxes_adapter.py:407` hardcodes `(165_000, 200_000)` and `(80_000, 100_000)` for 2025 student loan interest phaseout.
* **Hardcoded 2025 strings in prompts & human review:**
  * `tools/transcription/completeness_review.py:40`: `SYSTEM` prompt hardcodes `"You are given the pages of the 2025 IRS instructions or publications..."` regardless of `taxyear.Y`.
  * `tools/human_review/steps.py:33-38`, `tools/human_review/packet.py:240`, and `tools/human_review/reading_list.json:2` hardcode 2025 page numbers and quotes.
* **Hardcoded personal username in source:** `tools/transcription/transcribe.py:1043` hardcodes `DEEPSEEK_KEYCHAIN = ("deepseek-api", "elliotmilco")`.

### 4.4 Fragile Text-Splicing, Prose Regexes & Platform-Specific Subprocesses
* **Custom YAML character-offset splicer (`tools/citations.py:1177-1246`):** `_scalar_offsets` and `_rewrite` manually parse raw YAML text character-by-character to splice page numbers in-place.
* **Fragile table/prose scraping:**
  * `tools/check_auto_limits.py:31-60` locates depreciation tables in `p946.txt` and `p463.txt` by searching for hyphenated line-break fragments (`"tomobiles (Including Trucks and Vans) Acquired Af-"`) and slicing magic `6000`- and `700`-character windows.
  * `tools/transcription/transcribe.py:503` extracts spec text via `spec[spec.index("### 4.1 Values and types"):spec.index("### 4.4 Collections")]`, which raises `ValueError` if those exact Markdown headings in `spec/spec.md` change.
  * `tools/check_limits.py:50` and `tools/year_diff.py:86` split sentences with `re.split(r"(?<=[.!?])\s+", ...)`, breaking mid-sentence on `Pub.`, `Rev.`, `Proc.`, `Fig.`, `No.`, and `U.S.`.
* **macOS-only commands & uncompiled Swift subprocesses:**
  * `tools/check_all_bg.sh:61-72` uses `cp -cR` (macOS APFS `clonefile(2)`), which fails on Linux or non-APFS filesystems.
  * `tools/check_extraction.py:81-86` invokes `swift tools/extraction/pdfkit_text.swift <pdf>` in a subprocess once per PDF document (recompiling from source on each call), and `tools/extraction/pdfkit_text.swift:4-6` uses force-unwraps (`!`).
* **On-the-fly TypeScript transpilation & getter monkey-patching for UsTaxes:** `tools/engines/ustaxes/hooks.mjs:27-54` transpiles UsTaxes `.ts` files on the fly via Node module loader hooks, and `tools/engines/ustaxes/run.mjs:81-96` (`cacheLines`) walks prototype chains to monkey-patch every zero-arg getter/method.

### 4.5 Testing Gaps in `tools/`
While `tools/transcription/` and the source-coverage checkers (`check_limits.py`, `check_operands.py`, etc.) have unit tests or `--self-test` modes, **over 4,300 lines of complex tooling have zero unit tests or self-tests**:
* **External engine differential suite (3,234 LOC):** `tools/engines/compare.py` (970 lines), `tools/engines/ots_adapter.py` (777 lines), `tools/engines/ustaxes_adapter.py` (742 lines), `tools/engines/generate_cases.py` (709 lines), and `tools/engines/run_engines.py` (616 lines).
* **PDF text and table extractors (1,097 LOC):** `tools/extract_text.py` (349 lines), `tools/extract_tax_table.py` (232 lines), `tools/extract_eic_table.py` (192 lines), `tools/extract_class_lives.py` (180 lines), `tools/extract_ptc_tables.py` (151 lines), and `tools/extract_macrs_tables.py` (144 lines).

---

## 5. Data Model, YAML Authoring & Fixture Debt (`forms/2025/`, `schema/`, `interview/`, `fixtures/`)

### 5.1 God-Object Accumulation in `person.yaml` (4,667 Lines) & Duplicated Student Blocks
* **Monolithic `forms/2025/person.yaml` (4,667 lines) and `forms/2025/dependent.yaml` (2,130 lines):** Because sibling sub-collections cannot join directly across forms except via their parent collection (`person`), `person.yaml` has become a catch-all containing per-person lines for 13 different forms and worksheets (Educator Expenses, Form 8889, Schedule 1-A, Excess Social Security, Form 8959, Schedule C/4562/SE, Pub. 560 SEP/SIMPLE, EIC Worksheet B, Form 2441, Form 8880, IRA/Form 8606, Form 8863 Part III, and Form 5329).
* **Near-verbatim 600-line duplication for Form 8863 Part III:** Because a student on Form 8863 can be either a filer/spouse (`person`) or a dependent (`dependent`), and `forms/2025/aqee.yaml` (`def: aqee`) only abstracts lines 27–31, the 21-line student eligibility and adjustment block (`*.edu` through `*.edu_line31`) is duplicated almost line-for-line between `forms/2025/person.yaml:3410-4005` (596 lines) and `forms/2025/dependent.yaml:1529-2125` (597 lines).

### 5.2 Atom Vocabulary Limitations Forcing YAML Workarounds
* **12-month unrolled boilerplate (3,598 YAML lines):** With no fixed-size array/month indexing over the 12 calendar months, `forms/2025/f1095a.yaml:78-1057` (1,057 lines) and `forms/2025/f8962.yaml:690-2192` (2,541 lines) unroll every monthly column (`jan`..`dec`) into hundreds of repetitive lines.
* **Binary-only `smaller_of` / `larger_of` (`schema/data.schema.json:455-483`):** `maxItems: 2` forces every 3-way minimum in IRS instructions (such as Form 2441 lines 6, 20, and 24 in `forms/2025/f2441.yaml:672-706, 1093-1127, 1239-1264`, and IRA line 12 in `forms/2025/person.yaml:3056-3081`) to chain extra `(helper)` lines.
* **Asymmetric `Operand` vs. `LineId` positions (`schema/data.schema.json:395-483`):** Because `sum.of`, `smaller_of.of`, `larger_of.of`, `subtract.from`, and `choose.then` require string line IDs rather than `$ref: "#/$defs/operand"`, forms must define dozens of wrapper `(helper)` lines just to hold a `param` or `const: 0` (e.g., `f2441.zero`, `f2441.limit_one`, `f2441.limit_two` in `forms/2025/f2441.yaml:15-24, 377-396`).
* **SEP rate faked as `NonNegDollars` (`forms/2025/person.yaml:1194-1346`):** Because no atom converts a `Count` (whole percent) into a `Rate` or computes `r / (1 + r)` on rates, `person.yaml` defines `person.cent` (`$0.01` as `NonNegDollars`) and `person.hundred` (`$1.00` as `NonNegDollars`), multiplies `$0.01` by `person.sep_rate`, adds `$1.00`, and passes those fake dollar amounts into `prorate`—which causes the second-family transcription reviewer to flag `person.sep_s5` and `person.sep_s6` as unit mismatches (`reports/2025/second_family.md:224`).
* **Missing `Date` type (`spec/spec.md:132` vs. `schema/data.schema.json:74`):** `spec.md` lists `Date` as one of the 7 value types, but `data.schema.json` omits it, forcing every date/age cutoff to be modeled as year-specific boolean questions (`person.born_before_2001`, `person.edu_born_2007`, `eic.died_2025`, `f2441.paid_2026`).

### 5.3 Interview Authoring Debt (`interview/*.yaml`)
* **Copy-pasted generic `help:` strings (`interview/questions-2025.yaml:100-415`):** Dozens of `Bool` and `Dollars` questions share the exact same 4-sentence placeholder `help:` string (*"Money is integer cents. Answer true/false for screening questions. Unknown may be null; do not guess. Married filing separately and unsupported items are refused with citations."*), even on boolean questions like `person.age65` (line 236) and `person.blind` (line 240).
* **Sub-profile question list explosion:** Unlike `interview/full-2025.yaml:24` (`questions: all`), the legacy sub-profiles `interview/2025.yaml:12-66` (54 inputs), `interview/sales-2025.yaml:13-345` (332 inputs), and `interview/stage4-2025.yaml:20-378` (358 inputs) manually list every transitive upstream input required by their target lines.

### 5.4 5-Way Input Ripple, Non-Round-Trippable Fixtures & Invalid `classm.json` Cases
* **5-way coupling when adding an input:** Adding any return-level or upstream input requires updating (1) every fixture file in `fixtures/2025/*.json`, (2) `interview/questions-2025.yaml` + the 3 sub-profiles, (3) `engine/src/generate.ts`, (4) `tools/engines/generate_cases.py`, and (5) `tools/transcription/input_contracts/`.
* **Non-round-trippable fixture JSON (`handoffs/HANDOFF-HARDENING-1.md:75-76`):** `fixtures/2025/stage4.json` (21,322 lines), `fixtures/2025/stage15.json` (37,622 lines), and `fixtures/2025/stage16.json` (25,529 lines) do not round-trip `json.dumps(..., indent=2)` or `JSON.stringify(..., null, 2)`, requiring text-splicing when adding new inputs.
* **Contradictory input combinations in `fixtures/2025/classm.json:31-54` (`T-142`, `T-147`):** Because Class M job generation fills unchosen inputs with defaults without enforcing domain invariants, `classm.json` (105,910 lines) includes unreachable states such as `f1040.status: "mfj"` paired with `household.unmarried: true`.

---

## 6. Documentation Drift & Verification Baseline Debt

### 6.1 Conflicting Handoff Entrypoints & Spec Drift
* **Contradictory "Read First" instructions:**
  * `CLAUDE.md:3-6` marks `HANDOFF.md`, `HANDOFF-INTEGRITY.md`, and `HANDOFF-STAGE-16.md` as historical and points to `HANDOFF-NEXT-SESSION.md` and `handoffs/HANDOFF-HARDENING-1.md`.
  * `PROJECT_INDEX.md:25-32` still labels `HANDOFF-INTEGRITY.md` and `HANDOFF-STAGE-16.md` as *"Current handoff"* and omits `HANDOFF-NEXT-SESSION.md` from the folder table.
  * `HANDOFF-STAGE-16.md` sits in the repo root while all other stage handoffs live in `handoffs/`.
  * `HANDOFF-NEXT-SESSION.md` stacks 10 `# Handoff — updated ...` sections in reverse chronological order with competing instructions.
* **Stale claims in `spec/spec.md` and `spec/design.md` (`T-012`, `T-096`–`T-100`):**
  * `spec/spec.md:49-60` and `:193-204` still list Schedule 1, Schedule 1-A, capital loss carryovers, QBI, and dependent credits as refused/open.
  * `spec/spec.md:73` still says only two outside engines are integrated (all four are live).
  * `spec/spec.md:108-112` overstates exhaustive interview enumeration and `choose` guard range checking compared to the actual implementation in `engine/src/interview-check.ts` and `analyzeGuards` (`engine/src/check.ts:761-853`).
  * **12 of 91 ambiguity entries** in `ambiguities/2025.yaml` are not linked via `ambiguity:` on any line in `forms/2025/*.yaml` (`T-095`).

### 6.2 Quantified Suppressed Baselines & Pending Reviews
To allow `check-all` to pass while checks were introduced during hardening, **736 open findings** are currently grandfathered in `baseline` arrays across `reviews/2025/*.json`:

| Baseline / Review File | Suppressed `baseline` Entries | Ruled Entries | Notes |
|---|---:|---:|---|
| `reviews/2025/consumers.json:310-734` | **423** | 51 | Unruled input-page consumer pairs |
| `reviews/2025/instruction_cites.json:3-156` | **152** | 0 | 100% unruled instruction citations |
| `reviews/2025/limits.json:18-86` | **67** | 2 | Unruled prose limit sentences |
| `reviews/2025/completeness/rulings.json:113-170` | **56** | 19 | 56 of 59 forms suppressed as `stale:<form>` |
| `reviews/2025/operands.json:7-32` | **24** | 1 | Printed arithmetic vs. operand mismatches |
| `reviews/2025/input_quotes.json:3-10` | **6** | 0 | Unruled input quote checks |
| `reviews/2025/signs.json:3-9` | **5** | 0 | Unruled sign checks |
| `reviews/2025/screens/rulings.json:1830-1834` | **3** | 70 | Plus 9 ruled items deferred to `PENDING-01`..`05` |
| **Total Suppressed Baselines** | **736** | — | Plus **11** citation exceptions in `reviews/2025/citations.json` and **27** PDF page exceptions in `tools/extraction/exceptions.json` |

Additionally, per `reports/2025/second_family.md:3`:
* **78 of 149 (52.3%) paired Claude/DeepSeek review logs are still `pending`** (53 of 62 forms in transcription, 16 of 62 in render comparison, and 9 of 25 in Class M hand-work; 37 forms have no DeepSeek Class M log yet).
* **10 passing Claude render logs** predate the per-entry glossary (`T-057`) because the render subject hash does not cover the glossary.

---

## 7. Cross-Reference with `TASKS.md`

### 7.1 Tracked in `TASKS.md` (12 of 37 findings)

#### Directly Tracked (8)
1. **736 suppressed source-coverage baseline entries in `reviews/2025/*.json` (§6.2)** → `T-094`
2. **12 of 91 ambiguity entries in `ambiguities/2025.yaml` unlinked to any form line (§5.2 / §6.1)** → `T-095`
3. **`analyzeGuards` in `check.ts` not checking the lowest interval bound against the operand's domain (§6.1)** → `T-096`
4. **Standing notices missing from `eval --json` / `eval --batch` and first-run CLI (§6.1)** → `T-098`
5. **Stale proof-of-concept refusal & open-item lists in `spec/spec.md` Sections 2.2 & 11 (§6.1)** → `T-012` and `T-099`
6. **10 Claude render logs predating the per-entry glossary because the render hash omits the glossary (§6.2)** → `T-057`
7. **Pub. 946 multi-column prose interleaving exceptions in `tools/extraction/exceptions.json` (§6.2)** → `T-040`
8. **Stray `w2[*].box10` inputs in 11 Stage 18–21 fixtures (§5.4)** → `T-146`

#### Partially Tracked (4)
9. **Lean monotonicity gaps (§3.3):** `T-100` tracks missing monotonicity lemmas for `prorate.whole`, `percent_floor.whole`, `multiply_rate.rate.den`, and `table_lookup`, plus the missing monotonicity table in `spec/spec.md` 6.3. *(Does not track `Eval.lean` bypassing `Atoms.*` or the `rfl` fuel tautologies in `EvalProps.lean`.)*
10. **macOS-only check suite (§4.4):** `T-097` tracks `tools/check_extraction.py` calling `swift` (PDFKit) unconditionally. *(Does not track `cp -cR` in `tools/check_all_bg.sh` failing on Linux/non-APFS, or `pdfkit_text.swift` being recompiled from source on every PDF invocation.)*
11. **5-way input ripple when adding a new input (§5.4):** `T-150` proposes a `tools/siblings.py` helper script to print a checklist of the 5 places to update, rather than decoupling them.
12. **Invalid/unreachable input combinations in `classm.json` and `generate.ts` (§5.4):** `T-142`, `T-147`, and `T-148` track specific manifestations (`f1095a` uniform + monthly answers, `classm.f5695.2`/`s3.3`/`f5695.8`, and unanswered `dependent[].born_died`), though not all contradictory combinations in `classm.json` (such as `f1040.status: "mfj"` with `household.unmarried: true` in `classm.asset.1`).

### 7.2 Untracked in `TASKS.md` (25 of 37 findings)

#### All 7 Active Bugs & Latent Defects (§1)
1. **Cross-document memo key pollution** in `evalLine` (`engine/src/eval.ts:169-193` and `lean/TaxFormalization/Eval.lean:300-313`) (§1.1)
2. **Missing `"(screen)"` in `HELPER_MARKERS` (`engine/src/render.ts:64`)** misrendering 20 lines as `column (screen)` in `rendered/2025/*.md` (§1.2)
3. **`tools/check_all_steps.sh:73-110` dropping `"$@"` (`--year`)** on 22 of 38 steps (§1.3)
4. **Incomplete operand mutator in `engine/src/mutate.ts:96-140`** skipping `multiply_rate.rate`, `prorate.whole`, `percent_floor.whole`, `table_lookup.{key,status}`, `choose`, and `test` (§1.4)
5. **Unfiltered `.json` scan in `differentialClassC` (`engine/src/differential.ts:147-154`)** (§1.5)
6. **`tools/hooks/pre-push:15` checking only the tip commit**, `tools/green.sh:20-25` lacking a lock on `.git/check-all-green-trees`, and `tools/check_all_bg.sh:118` creating dangling commit objects (§1.6)
7. **`tools/archive_text.py:89-93` self-test regex bypassed** by `tools/extract_ptc_tables.py:27-35` (§1.7)

#### All 8 TypeScript Engine Structural Debt Items (§2)
8. **5 divergent helper-marker lists** across `check.ts`, `classm.ts`, `render.ts`, `mutate.ts`, and `build.ts` (§2.1)
9. **6 separate `Expr` / `TestExpr` AST walkers** in `engine/src/` (§2.2)
10. **5 copy-pasted `templateKey` regexes** in `engine/src/` (§2.3)
11. **Import-time `process.argv` mutation and global `YEAR` singleton** in `engine/src/year.ts:16-46` (§2.4)
12. **Redundant `VOCABULARY` / `PRIMITIVE_OPS` lists and dead `bracket_schedule` / `opaque` types** in `engine/src/atoms.ts` & `engine/src/types.ts` (§2.5)
13. **`engine/src/generate.ts` PRNG stream coupling** (5 exclusion sets + 4 FNV-1a/Mulberry32 post-passes) and the **second legacy LCG generator** in `engine/src/compare.ts:31-104` (§2.6)
14. **~400 lines of hardcoded 2025 form/line equivalence provers** in `engine/src/mutate.ts:515-915` (§2.7)
15. **Hardcoded Stage 1–5 scaffolding** in `build.ts`, `interview-check.ts` (ignoring `stage8.json`–`stage21.json`), `interview.ts`, and `fixtures.ts` (§2.8)

#### 3 Lean 4 Architecture & Evaluator Items (§3)
16. **Untyped `Lean.Json` traversal with silent `.getD 0` / `.getD ""` fallbacks** in `lean/TaxFormalization/Eval.lean` (§3.1)
17. **`lean/TaxFormalization/Eval.lean:420-506` re-implementing arithmetic inline** instead of calling proved functions in `lean/TaxFormalization/Atoms.lean`, plus trivial `rfl` fuel tautologies in `lean/TaxFormalization/EvalProps.lean` (§3.2, §3.3)
18. **Evaluator Divergence D6** and **spawning ~1,994 separate `taxeval` OS processes** in `engine/src/compare.ts:131-138` (§3.4)

#### 4 Python & MJS Tooling Items (§4)
19. **Whole-subsystem re-implementations in Python** (`UnroundedModel` in `tools/engines/compare.py:311-608`, `Reading` in `tools/human_review/reading.py:232-492`, `Expander` in `tools/transcription/transcribe.py:725-932`, `resolve` in `tools/fixtures_year.py:72-80`) (§4.1)
20. **Cross-script duplication in `tools/`** (`taxyear.py` `sys.argv` mutation, 8 manifest loaders, 7 AST walkers, 4 `bbox-layout` parsers, 8 markdown review parsers, duplicate `.mjs` harnesses) (§4.2)
21. **Hardcoded 2025 parameters, PDF page numbers/coordinates, `extract_ptc_tables.py` hardcoded paths, and hardcoded keychain username `"elliotmilco"`** in `tools/transcription/transcribe.py:1043` (§4.3)
22. **Fragile text/prose regexes** (`citations.py` raw YAML splicer, `check_auto_limits.py` hyphen-break search, `transcribe.py` `spec.md` heading slice, `compare.py` derivation note regexes) and **zero unit tests for ~4,300 LOC in `tools/engines/*` and `tools/extract_*.py`** (§4.4, §4.5)

#### 3 Data Model, Fixture & Documentation Organization Items (§5 & §6)
23. **God-object `forms/2025/person.yaml` (4,667 lines)** and **~600 lines of near-identical Form 8863 Part III duplication** between `person.yaml` and `dependent.yaml` (§5.1)
24. **Atom vocabulary & schema workarounds**: 12-month unrolling in `f8962.yaml`/`f1095a.yaml` (3,598 lines), binary-only `smaller_of`/`larger_of`, SEP rate faked as `NonNegDollars`, missing `Date` type in `data.schema.json`, copy-pasted `help:` boilerplate in `questions-2025.yaml`, and 332–358 manual question lists in sub-profiles (§5.2, §5.3)
25. **Non-round-trippable JSON in `stage4.json`, `stage15.json`, and `stage16.json`** *(noted in `handoffs/HANDOFF-HARDENING-1.md:75-76`, not in `TASKS.md`)* and **contradictory "Read First" entrypoints** across `CLAUDE.md`, `PROJECT_INDEX.md`, and `HANDOFF*.md` (§5.4, §6.1)
