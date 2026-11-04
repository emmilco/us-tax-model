# T-152 intake: disposition of every subclaim of the technical debt audit

Audit: `docs/2026-11-01_tech_debt_audit.md`. Each claim was checked against the tree at 0d9718c plus this package's
uncommitted changes (2026-11-03), not taken from the audit or from the backlog plan's carry-forward table. Checking was done
by reading code, grep or `wc` counts, and some runtime probes, all in this package. The probes: `eval --json` on
`stage16.ira.i1` for alias keys, a Python and Node round-trip of the stage fixtures, a schema walk for operand positions,
and the `archive_text` self-test regexes applied to `extract_ptc_tables.py`. No claim was certified as a bug by
reproduction unless that is stated.

## Disposition kinds

- **fixed (id)**: already corrected, with the record that shows it.
- **task (id)**: an existing row covers it.
- **new row (NEW-n)**: an action remains. The proposed rows are at the end.
- **accepted**: an accepted tradeoff, with its reason. This is proposed under the owner's standing delegation and is a P5
  candidate only if a concrete failure appears.
- **false**: the claim is wrong or obsolete, with the evidence.

Line numbers are current ones and may differ from the audit's.

## 1. Active bugs and latent defects

| Claim | Finding now | Disposition |
| --- | --- | --- |
| 1.1.1 Cross-document calls re-evaluate the target | `eval.ts:181-192` recurses without caching under the caller's key. The target key still memoizes. | fixed (BUG-0287) |
| 1.1.2 Alias keys in derivations, `eval --json` and sheets | Probe on `stage16.ira.i1`: 2,404 keys, 0 matching `\]\.<doc>\.`. `reports/2025/*` hold none. | fixed (BUG-0287) |
| 1.1.3 compare and Lean export alias keys | `Eval.lean:309-317` inserts only own or unshared keys. | fixed (BUG-0287) |
| 1.2 `(screen)` missing from `render.ts` | `render.ts:64` includes it; `grep 'column (screen)' rendered/2025` finds nothing. There are now 22 such lines, not 20. | fixed (T-155) |
| 1.3 `check_all_steps.sh` drops `"$@"` | 05ede53 forwards it to the year-aware steps. 15 of 60 steps still lack it. Four of those are year-sensitive: `siblings_check`, `refusal_reach`, `classm_job_seeds` (each defaults to the newest adopted year) and `check_ptc_tables` (hardcoded 2025; see 4.3.1). Today `years.json` adopts only 2025, so no wrong result is possible yet. | new row NEW-1 (year preparation, before T-011) |
| 1.4 Operand mutator omissions | `multiply_rate.rate`, `prorate.whole` and `percent_floor.whole` are now walked (`mutate.ts:72,84,88`). The `table_lookup` key and status, `choose` branch targets and test operands are "measured but not yet mutated" (`mutate.ts:50-52`). | fixed in part (T-156); rest task T-159 |
| 1.5 Unfiltered scan in `differentialClassC` | `calculatorRecords()` (`differential.ts:99`) serves both readers. | fixed (BUG-0288) |
| 1.6.1 pre-push checks only the tip | `tools/hooks/pre-push:17-30` walks every pushed commit; `test_pre_push.sh` is in check-all. | fixed (BUG-0289) |
| 1.6.2 Green record unlocked | `tools/green.sh:20-33` takes an `mkdir` lock; `test_green.sh` is in check-all. | fixed (BUG-0289) |
| 1.6.3 Dangling snapshot commit per background run | Still true (`check_all_bg.sh:118`). | accepted (BUG-0289 disposed of it as housekeeping; unreferenced objects are a size cost that `git gc` reclaims, not a correctness defect) |
| 1.7 `extract_ptc_tables.py` bypasses the archive-reader self-test | Probe: the self-test's regexes flag nothing in the file, which reads `(SRC / f"{doc}.{layer}")` and `fr-2024-00796.txt` directly. The two documents carry no draft flag, so nothing is mis-stripped today. | new row NEW-2 (with 4.3.1: route the file through `archive_text` and widen the self-test to catch a renamed path constant) |

## 2. TypeScript engine

| Claim | Finding now | Disposition |
| --- | --- | --- |
| 2.1.1, 2.1.2 Helper markers duplicated in `check.ts` and `classm.ts` | Both are true and both hold the same six markers. | new row NEW-3 (one shared `isHelperLine` in `util.ts`; the T-155 bug shows that divergent lists cause defects) |
| 2.1.3 `render.ts` lacks `(screen)` | See 1.2. | fixed (T-155) |
| 2.1.4 `mutate.ts:379,477` test only `(helper)` | True. Equivalence classification is conservative, so a mutant is reported as unexplained rather than hidden. | NEW-3 (same consolidation; no wrong result) |
| 2.1.5 `build.ts:244` `startsWith("(")` | True. The dead-line check also covers column and worksheet markers such as `(c)` and `(CLW 1)`. That may be intended, since those lines are also not printed boxes. | NEW-3 (decide the intended set when consolidating) |
| 2.2 Six AST walkers in `engine/src` | All six exist. Their skip lists differ because their jobs differ (refs, operands, dead lines). `classm.ts:53` `bracket_schedule` is not dead, since the type declares it. | accepted (different responsibilities, as the carry-forward table found; a shared visitor is P5 only with a demonstrated miss such as 1.4) |
| 2.3 Five key-stripping regexes | True. `interview.ts:23` differs (`*`, `[a-zA-Z0-9_-]+`). `fixtures.ts:184` re-implements `templateKey`, which it already imports. No divergent output is shown, because keys are restricted to `[a-zA-Z0-9_-]` elsewhere. | new row NEW-4 (small: use `templateKey` everywhere; bounded and cheap) |
| 2.4 Import-time `argv` splice and fixed `YEAR` | True for `year.ts:16-33` and `mutate-worker.ts:6-7`. `CANON_DIR` and `FORMS_DIR` live in their modules, not in `year.ts`. One year per process is a deliberate simplification. | accepted (one year per process is enough for every tool; reconsider at T-011 only if a two-year tool is needed) |
| 2.5.1 `VOCABULARY` and `PRIMITIVE_OPS` identical; `PRIMITIVE_OPS` unused | True: both sets have 21 entries and no difference, and `PRIMITIVE_OPS` has no reference outside `atoms.ts`. | NEW-4 (delete the unused set) |
| 2.5.2 `bracket_schedule` and `opaque` stale | Only the op forms are stale. `opaque` is counted on purpose (`check.ts:150`, the register of design.md), and `bracket_schedule` is a live table kind. | false in part; the op-form residue goes with NEW-4 |
| 2.6.1 Generator stream-protection sets and derived streams | True. This is the documented means of keeping the seeded sample stable; no wrong output. | accepted (keeps receipts comparable across stages; the cost is per-return JSON serialization, unmeasured) |
| 2.6.2 Second LCG generator in `compare.ts` with 2025 standard deductions | True (`compare.ts:42`). It only shapes the W-2 inputs; both evaluators see the same inputs. | new row NEW-1 (year preparation: read the amounts from params) |
| 2.7 Form-specific equivalence provers in `mutate.ts` | They exist (about 400 lines, hardcoded ids). "Silently breaks" is false: a renamed id makes the mutant unexplained and `mutate` exits 1 (`mutate.ts:563`, `:1106-1122`). `copyTargetMatch` does not exist. | accepted (fails loudly on drift; moving them into data is a P5 design proposal) |
| 2.8.1 Early profile filenames in `build.ts` | True. The names are year-templated. | accepted (these are the shipped profiles) |
| 2.8.2 `interview-check.ts` uses only stages 2 to 5 | True. Order invariance and completion are not exercised on stages 8 to 21. Spec 3.5 says "every interview path ends in either a complete set of forms or a cited refusal", which this does not establish exhaustively. | new row NEW-5 (claim accuracy: either extend the check to later stage fixtures or narrow spec 3.5 and 6.4) |
| 2.8.3 `interview.ts` picks scope prose by target | True. | accepted (one sentence per shipped profile) |
| 2.8.4 Frozen stage 1 to 5 review packets regenerated in check-all | True (`check_all_steps.sh:126-129`). | accepted (cheap, and keeps the historical packets reproducible) |

## 3. Lean

| Claim | Finding now | Disposition |
| --- | --- | --- |
| 3.1 Untyped `Lean.Json` evaluation with `getD` fallbacks | True: 59 `getD`, 26 of them `getD 0`. The TS evaluator and `compare` agree on every case. | accepted for now. The fallbacks hide malformed canonical data, but the build validates it against the schema first. A typed AST is a bounded-investigation item; the backlog plan asks for one before program close, so record it as NEW-6. |
| 3.2 `Eval.lean` does not call `sumList`, `subtractFloor0`, `smallerOf`, `largerOf` | True for those (inline `+`, `max 0`, min/max fold). The audit names functions that do not exist (`multiplyRate`, `roundVal`, `tableLookup`, `rateLookup`; the real ones are `multiplyRateHalfUp`, `roundByRule`, `keyedLookup`, `rateBand`, and those are called). | new row NEW-6 (claim accuracy first: say in spec 6.3 and `docs/TRUST.md` which proved atoms the reference evaluator executes, or make it call them; overlaps T-100) |
| 3.3.1 `rfl` theorems in `EvalProps.lean` | True. The file header already says their force comes from totality. | NEW-6 (make sure no public claim reads them as acyclicity proofs) |
| 3.3.2 Missing monotonicity lemmas | True. | task T-100 |
| 3.4.1 D6: Lean accepts only bare ids where the schema allows operands | False. Lean takes `{param}` and `{const}` at every position where the schema allows an operand (`take`, `multiply_rate.rate`, `prorate.whole`, `percent_floor.whole`). Positions that are strings in Lean are strings in the schema too. Probe: no inline operand sits at a string-only position. Spec 4.7 states D6 as unreachable. | false |
| 3.4.2 One Lean process per case | True (`compare.ts:129-133`). The case count is not settled: the audit, carry-forward table, a static count and BUG-0287 give 1,994, 2,011, 1,642 and 2,025. | accepted (performance only; a `--batch` mode for `lean/Main.lean` is P5 with a measured benefit) |

## 4. Python and MJS tooling

| Claim | Finding now | Disposition |
| --- | --- | --- |
| 4.1.1 `UnroundedModel` re-implements the evaluator and parses note text | True (`engines/compare.py:311-610`, `startswith("taken: ")` at :494, band regex at :590). | new row NEW-7 (the note-text coupling: add the taken guard index, which the evaluator holds as `takenGuardIndex` but `resultToJson` does not emit, and the band to the derivation JSON, and stop parsing prose). The re-implementation itself is accepted: an independent unrounded model is its purpose. |
| 4.1.2 `Reading` second English renderer | True. It is the human-review reading, with a different audience from `render.ts`. | accepted |
| 4.1.3 `Expander` in `transcribe.py` | True. It is review tooling that normalizes for model comparison. | accepted |
| 4.1.4 `fixtures_year.py` `resolve` | True. It lacks the TS validation (`fixture-inputs.ts:20`). | NEW-1 (year preparation: validate or call the engine's resolver) |
| 4.2.1 `taxyear.py` argv mutation | True. 42 of 43 importers use `from taxyear import Y  # noqa: E402`. | accepted (mirrors `year.ts`, as in 2.4) |
| 4.2.2 Eight manifest loaders | Partly true, with wrong sites: `citations.py` already uses `archive_text.manifest()`. About 12 direct reads exist. | NEW-2 (route source reads through `archive_text`, with 1.7) |
| 4.2.3 Seven Python expression walkers | Partly true: `coverage/tree.py` has none, and others exist that the audit missed. Their jobs differ. | accepted (as 2.2) |
| 4.2.4 Locator parsing duplicated | `transcribe.py:86-142` does not import `citations.py`. `pages.py` reuses `citations`' parts and repeats only the loop. | new row NEW-8 (`transcribe.py` should use `citations.page_list` and its relatives; a divergence here mis-sends pages to reviewers) |
| 4.2.5 Four bbox-layout parsers | True. | accepted until T-040's extraction package; NEW-2 if that package touches them |
| 4.2.6 Eight review-log parsers | True. | new row NEW-9 (one `logs.py` parser for the review-log format; the risk is that a divergence drops a review line, which has not been demonstrated) |
| 4.2.7 Duplicate MJS harnesses | True. | accepted (small; 17 and 24 lines) |
| 4.3.1 `extract_ptc_tables.py` hardcodes 2025 | True, and it runs in check-all without `"$@"`. | NEW-1 and NEW-2 |
| 4.3.2 to 4.3.5 Page ranges and coordinates in `check_instruction_cites`, `extract_eic_table`, `extract_tax_table`, `extract_class_lives`, `transcribe_tables` | True. All are 2025-specific; the extractors run only when tables are regenerated. | NEW-1 (move them to a per-year table of pages, or make them fail loudly on another year) |
| 4.3.6 to 4.3.8 2025 amounts in the engine adapters | True. The student-loan pair is a deliberate mismatch window, not plain 2025 amounts. | NEW-1 (read from params where the engine allows) |
| 4.3.9 2025 in the completeness `SYSTEM` prompt | True. Changing it changes the prompt hash and reopens every completeness ruling. | NEW-1, due at T-011 (change at adoption, not before) |
| 4.3.10 2025 quotes in `human_review` | True. | NEW-1 |
| 4.3.11 Keychain account `elliotmilco` in `transcribe.py:1043` | True. It is portability, not year. | new row NEW-10 (read the account from an environment variable with the current value as default; before outside reproduction, with T-097) |
| 4.4.1 Character-offset YAML splicer in `citations.py` | True. It exists to keep YAML formatting on rewrite. | accepted |
| 4.4.2 `check_auto_limits.py` fragment search | True. It will fail loudly if the text reflows. | NEW-1 |
| 4.4.3 `transcribe.py:503` heading slice | True. Both headings exist, and the slice raises (does not mis-read) if they change. | accepted (fails loudly) |
| 4.4.4 Naive sentence split | True for `check_limits.py:50`. Probe: "Pub. 946 and Rev. Proc." splits into five pieces. `year_diff.py:86` has the same flaw. The effect on findings is not shown. | new row NEW-11 (abbreviation-aware split; re-run the limits baseline, which may shift keys) |
| 4.4.5 `cp -cR` in `check_all_bg.sh` | True. | stated in README (this package); accepted (the background runner is macOS-only, as is the owner's machine) |
| 4.4.6 Swift per PDF, force-unwraps | True. | T-097 portion fixed in this package (skip visibly off macOS, error on macOS); the per-call compile and force-unwraps are accepted (the check is offline and correct) |
| 4.4.7 UsTaxes transpile hooks and getter cache | True. `ustaxes_adapter --self-test` compares cached and uncached runs. | accepted |
| 4.5.1 Engine suite: 3,234 lines, zero tests | Inaccurate: it is 3,809 lines. `ustaxes_adapter` has a `--self-test`, and the whole suite runs as the `engine_differential` integration step. compare, ots_adapter, generate_cases and run_engines have no unit tests. | new row NEW-12 (unit tests for `engines/compare.py` matching and tolerance logic, the riskiest part) |
| 4.5.2 Extractors, zero tests | Partly true. `extract_ptc_tables --check`, `check_extraction`'s use of `extract_text`, and `check_macrs_tables` cover three of them. `extract_tax_table`, `extract_eic_table` and `extract_class_lives` have none. The tables they wrote are cross-checked by the conjecture checks (`tax_table_conjecture`, `eic_table_conjecture`). | NEW-1 (at T-011 the regenerated tables are compared with the conjectures; add a `--check` only if that proves insufficient) |

## 5. Data model, YAML and fixtures

| Claim | Finding now | Disposition |
| --- | --- | --- |
| 5.1.1 `person.yaml` catch-all | True (4,691 lines). It follows from the join rule of collections. | accepted; decomposition is a bounded-investigation item (backlog plan "Conditional work") with no current failure |
| 5.1.2 Form 8863 Part III duplicated in person and dependent | True: about 620 lines each, 0.94 similar. The block is 28 or 29 lines, not 21. The dependent side has an extra line. | new row NEW-13 (sibling-drift risk: until it is factored, `tools/siblings.py` should pair `person.edu*` with `dependent.edu*` so every fix is checked on both) |
| 5.2.1 Twelve-month unrolling | True, though the line spans are not a count of boilerplate. | accepted (a month-indexed schema is a bounded investigation) |
| 5.2.2 Binary `smaller_of` and `larger_of` | True (schema maxItems 2). | accepted (helper chains are rendered and reviewed line by line) |
| 5.2.3 Operand positions take only strings | True. | accepted (the same design keeps the Lean and TS operand sets aligned; see 3.4.1) |
| 5.2.4 SEP rate as dollars | True in mechanism. The cited report line has moved. | accepted (the register records the six-place reading; a Count-to-Rate atom is a vocabulary change) |
| 5.2.5 No Date type | Partly true. Spec 4.1 limits Date to holding periods, so the age-cutoff framing is overstated. Year-bearing input ids (`born_before_2001`, `edu_born_2007`, `died_2025`, `paid_2026`) will need renaming at T-011. | NEW-1 (year adoption: the year diff must cover input ids), and the spec 4.1 versus schema mismatch is NEW-5 (claim accuracy) |
| 5.3.1 Placeholder `help:` text | True: about 45 copies, including `person.age65` and `person.blind`. | new row NEW-14 (wording, form by form, with each owning form's next pass; T-177 covers `person.blind`) |
| 5.3.2 Hand-written sub-profile lists | True. | accepted (the build checks them) |
| 5.4.1 Five-way ripple of a new input | True. `tools/siblings.py --input` prints the ripple (T-150). | task T-150 (done; the row should move to TASKS-DONE); decoupling accepted |
| 5.4.2 Fixtures do not round-trip | Partly false. All three round-trip semantically, and stage15 and stage16 round-trip textually with Python. stage4 fails only on three literal en dashes that should be `–`. Node does not round-trip any of them. | new row NEW-15 (normalize stage4's three lines; correct the handoff fact) |
| 5.4.3 Contradictory Class M cases | True: 35 of 199 cases pair `mfj` with `household.unmarried` true. No evaluated error is shown. | task T-142 |

## 6. Documentation and baselines

| Claim | Finding now | Disposition |
| --- | --- | --- |
| 6.1.1 CLAUDE.md marks old handoffs historical | True, and correct. | no action |
| 6.1.2 PROJECT_INDEX.md labels | Partly fixed. HANDOFF-NEXT-SESSION.md is listed, but `PROJECT_INDEX.md:35,36,42` still call HANDOFF-INTEGRITY.md and HANDOFF-STAGE-16.md current. | new row NEW-16 (the parent owns PROJECT_INDEX.md) |
| 6.1.3 Old handoffs in the repo root | True (HANDOFF.md, HANDOFF-INTEGRITY.md, HANDOFF-STAGE-16.md). | NEW-16 (move to `handoffs/` with the index edit) |
| 6.1.4 HANDOFF-NEXT-SESSION.md stacks entries | True: 24 entries, 809 lines. | NEW-16 (keep the top two entries, archive the rest to `handoffs/`) |
| 6.1.5 Spec 2.2 and 11 stale | True at HEAD. | fixed in this package (T-099, T-012 documentation) |
| 6.1.6 "Two engines" | True, at spec.md:357 and :410, not :73. Four engines run (`engines/run.sh`). | new row NEW-17 (spec 6.5: name the four engines; small, P4) |
| 6.1.7 Spec overstates interview enumeration and guard checks | The guard domain part is fixed (T-096). The interview part is true (see 2.8.2). | fixed in part (T-096); rest NEW-5 |
| 6.1.8 12 of 91 ambiguity entries unlinked | True; the recount matches T-095. | task T-095 (this package proposes the links) |
| 6.2 736 baseline entries | Now 715: consumers 417, instruction_cites 148, limits 67, completeness 45, operands 24, input_quotes 6, signs 5, screens 3. Citation exceptions (11) and PDF exceptions (27) are unchanged. | task T-094 (its row says "56 forms never completeness-reviewed"; it is now 45, so update the row) |
| 6.2 "78 of 149 pending" | Stale: the report regenerated on 2026-11-03 says 74 pending of 155 pairs. | no action (a generated figure; report from the regenerated file) |
| 6.2 T-057, ten render logs predate the glossary | Partly fixed: asset, sa, sc and scveh were rerun on 2026-11-02. f4562, f8959, f8995, f8995a, mq and f8606 remain. | task T-057 (narrow the row to the six) |

## 7. The audit's cross-reference

The 37/12/25 split is the audit's own grouping, not an atomic count; this file splits it into about 90 subclaims.

Corrections to section 7:

- T-096 is done, not open.
- T-098 maps to no finding in the audit body.
- T-150 is done (siblings.py exists), not a proposal.
- T-040 covers only 3 of the 27 PDF exceptions; the others are image or chart pages, accepted in `exceptions.json` with reasons.
- Items 1 to 7 of 7.2 are mostly fixed: BUG-0287 to BUG-0289 and T-155/T-156 were done before this intake.

## Proposed new rows

| Id | Task | Source | Due when |
| --- | --- | --- | --- |
| NEW-1 | Year-adoption preparation from the T-152 audit. Forward `"$@"` to `siblings_check`, `refusal_reach` and `classm_job_seeds` (and make the scripts pass `--year` on). Make `extract_ptc_tables.py`, `check_instruction_cites.py` PARTS, the extractors' page ranges and coordinates, `check_auto_limits.py` and `human_review` year-aware or fail on a year other than 2025. Take the engine adapters' 2025 amounts and `compare.ts`'s standard deductions from params. Validate in `fixtures_year.resolve`. Change the completeness `SYSTEM` prompt year. Have the year diff cover year-bearing input ids. | T-152 audit 1.3, 2.6.2, 4.1.4, 4.3, 4.4.2, 4.5.2, 5.2.5 | before T-011 (prepare now; the prompt change at adoption) |
| NEW-2 | Route `extract_ptc_tables.py` and the other direct `sources/<year>` readers through `archive_text`, and widen its self-test to catch a path constant of any name. | audit 1.7, 4.2.2 | next extraction-maintenance package (P5) or with NEW-1 |
| NEW-3 | One `isHelperLine` predicate shared by check, classm, render, mutate and build; decide whether build's dead-line check also means column markers. | audit 2.1 (T-155 showed the cost) | next engine-tool change (P5) |
| NEW-4 | Small engine tidy: `templateKey` everywhere (`fixtures.ts:184`, `interview.ts:23`, `interview-check.ts:18`, `classm.ts:80`); delete the unused `PRIMITIVE_OPS` and the unimplemented `bracket_schedule` op form if no form uses it. | audit 2.3, 2.5 | next engine-tool change (P5) |
| NEW-5 | Claim accuracy, spec 3.5, 4.1 and 6.4: the interview path checks cover stages 2 to 5 only, and Date is in spec 4.1 but not in the schema. Extend the checks to the later stage fixtures, or narrow the spec. | audit 2.8.2, 5.2.5, 6.1.7 | P4 (next spec pass) |
| NEW-6 | Claim accuracy for the Lean evaluator. State which proved atoms `Eval.lean` executes (it inlines sum, subtract-floor and min/max) and that the `EvalProps` theorems are totality facts, or make it call the proved functions. Record the typed-AST investigation's outcome. | audit 3.1–3.3.1 | with T-100 |
| NEW-7 | `engines/compare.py` `UnroundedModel`: read the taken guard and band from structured derivation fields, not note prose. | audit 4.1.1 | next engine-differential change |
| NEW-8 | `transcribe.py` locator parsing: use `citations.py`'s parsers. | audit 4.2.4 | next review-tool change |
| NEW-9 | One parser for the review-log Markdown format shared by the eight readers. | audit 4.2.6 | next review-tool change (P5) |
| NEW-10 | Read the DeepSeek keychain account from the environment (default the current value). | audit 4.3.11 | before outside reproduction (with T-097) |
| NEW-11 | Abbreviation-aware sentence split in `check_limits.py` and `year_diff.py`; rebaseline limits if keys move. | audit 4.4.4 | next limits-check change |
| NEW-12 | Unit tests for the matching and tolerance logic of `tools/engines/compare.py`. | audit 4.5.1 | next engine-differential change |
| NEW-13 | Until Form 8863 Part III is factored, make `tools/siblings.py` pair each `person.edu*` line with its `dependent.edu*` twin. | audit 5.1.2 | next siblings.py change |
| NEW-14 | Replace the generic placeholder `help:` text (about 45 questions) with each question's own help, form by form at each form's next pass. | audit 5.3.1 | each owning form's next pass |
| NEW-15 | Normalize the three literal en dashes in `fixtures/2025/stage4.json` (lines near 14173–14191) so all fixtures round-trip with Python's `json.dumps(indent=2)`, and correct the hardening handoff fact. | audit 5.4.2 | next fixture edit of stage4 |
| NEW-16 | Entrypoint tidy: fix the "Current handoff" labels in PROJECT_INDEX.md, move the root handoffs to `handoffs/`, and archive all but the top entries of HANDOFF-NEXT-SESSION.md. | audit 6.1.2–6.1.4 | next handoff |
| NEW-17 | Spec 6.5: name the four outside engines in use (spec.md:357, :410). | audit 6.1.6 | next spec pass |

## Inspected / inferred (unverified)

- **Inspected:** the current code at the cited lines for every row above, with the counts and probes named in the opening
  paragraph. The probes were run by this package's read-only investigators in a scratch copy for the `eval` run.
- **Inferred (unverified):**
  - That `git gc` reclaims the snapshot commits (1.6.3).
  - That the stage1 to 5 review packets are cheap to regenerate (2.8.4).
  - That divergent review-log parsers could drop a line (NEW-9). This is a risk argument, not a demonstrated drop.
  - The Lean case count of 3.4.2 (four different figures; `compare` was not run).
  - That `interview.ts:23`'s regex never diverges on real keys (2.3).
