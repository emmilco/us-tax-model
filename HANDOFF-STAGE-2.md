# Handoff: Stage 2 — excess Social Security tax withheld

You are picking up this project at the start of Stage 2. Stages 0 (source grounding) and 1 (format spike) are complete and committed; the owner is reviewing Stage 1's renderings in parallel. Build Stage 2 as defined in `spec/design.md`, stopping for the owner's review at the end of the stage.

**First: give the owner an intent readback of Stage 2 as you understand it, and wait for confirmation.** This is the pattern the project uses at every stage start.

## What this project is

An open, verifiable formalization of the IRS forms-and-instructions layer for US federal individual income tax, with a guided self-preparation tool as its first client. The form data is the product: every line is one application of an atom from a frozen vocabulary, carrying a structured citation to an archived source snapshot. Read `HANDOFF.md` (the original build handoff) in full — every settled decision, constraint, and working agreement in it still applies.

## Read these first, in this order

1. `HANDOFF.md` — what the project is, decisions not to reopen, hard constraints (in particular: never read the owner's personal tax documents; fixtures are synthetic or official IRS examples only; no network use except the deliberate source fetcher; do not write implementation ahead of the current stage).
2. `PROJECT_INDEX.md` — folder structure, conventions, where everything lives.
3. `spec/design.md` — Stage 2 (section 5) and the architecture you will extend: 2.2 form data, 2.3 checker, 2.4 renderer, 2.5 evaluator, 2.6 Lean, 2.7 interview engine, 2.8 CLI, 2.10 test harness; section 4 authoring procedure; section 6 open choices.
4. `spec/spec.md` — especially 2.1/2.2 (scope and refusals), 4.2 (`sum_over` is already in the frozen vocabulary — you implement it), 4.4 (collections), 4.6 (gates and refusals), 5 (provenance), 6 (tests), 8 (values sheet and how refusals are shown).
5. `sources/2025/PREMISES.md` — premise **P07** is your primary finding, with its locators. Then read the archived text itself: `sources/2025/i1040gi.txt`, page 117 ("Line 11—Excess Social Security and Tier 1 RRTA Tax Withheld"); `sources/2025/f1040s3.txt`, line 11; and the W-2 box structure from `sources/2025/fw2.txt` / `sources/2025/iw2w3.txt` (2025 revisions; hashes in `sources/2025/manifest.json`).
6. Stage 1 as precedent — read `engine/src/eval.ts` and `engine/src/check.ts` carefully (they define the evaluator semantics and the checker's powers *and limits*), one form YAML (`forms/2025/qdcg.yaml`), `lean/TaxFormalization/Atoms.lean` with `Lemmas.lean`, and the four reports in `reports/2025/`.

**The most important rule, carried forward: encode only from IRS text archived in `sources/` that you have read yourself — never from memory, from this handoff, or from the research files.** Every line, parameter and gate carries a citation whose snapshot hash must exist in the manifest, and the build fails otherwise.

## What Stage 2 is (design.md, verbatim)

> Stage 2. Architecture test: excess Social Security tax withheld — Form W-2 as a collection, grouping by person, the per-employer rule, a year parameter, Schedule 3, and the first refusal gate.
>
> Done when: `sum_over` and gates work end to end from interview answers to a values sheet with derivations, and the single-employer case produces a cited refusal with the correct remedy named.

Decomposed:

- **Form W-2 as a collection** — the first use of the keyed-collection model (spec 4.4): W-2s are a collection keyed by employer; aggregation across them is an explicit `sum_over`.
- **Grouping by person** — the credit is figured separately for each spouse, so the person dimension must exist structurally. The interview cannot yet represent two people (spec 2.2 already refuses "married filing statuses where a rule in scope is figured per spouse"), so build the structure with one person reachable; the two-person case should be a data change later, not a rework.
- **The per-employer rule** — orientation only, encode from P07 and page 117: the credit is the combined withholding in excess of $10,918.20 when there was more than one employer and total wages over $176,100; but if any one employer withheld more than $10,918.20, that excess cannot be claimed on the return (the employer should adjust; otherwise Form 843). "Figure this amount separately for you and your spouse."
- **A year parameter** — the 2025 constants from the archived text, each with a citation.
- **Schedule 3** — line 11 and its printed flow (read the archived form; do not infer it).
- **The first refusal gate** — spec 2.5: a refusal is a value, not an exception; spec 8: a refusal names the form the tool cannot prepare, the trigger, and the instruction requiring it.
- **Interview answers end to end** — spec 2.7: the needed inputs derived by backward slice from the target lines; questions authored as data, each with a citation; answers stored as an append-only log; the return recomputed from the log; gates evaluated as early as their inputs allow; the checks in spec 6.4 run in the build (see open question 4 below).

## Known open modeling questions — surface these to the owner, do not decide silently

1. **Refusal shape for the single-employer case.** Whole-return refusal, or a refused-credit value with the named remedy while the rest of the return computes? Read the instruction on page 117 and propose; get a ruling.
2. **Collection encoding and `sum_over` binding.** Spec 4.2 defines `sum_over` as "total of one column over a collection, with an optional filter". Decide how a collection and its entries are expressed in YAML/canonical JSON, how the summed field and the filter are written, and what the checker verifies about them (entry-typing, filter exhaustiveness, acyclicity through entries). Propose before building.
3. **What "grouping by person" means structurally now** — one person reachable but the dimension present. Enough that two people is a data change.
4. **Which of spec 6.4's interview checks land in this stage.** Design says the checks run in the build; the stage's done-condition names the end-to-end path. If everything cannot land cleanly, propose what is deferred explicitly.
5. **The exact gate structure for the credit** (more than one employer AND total wages over $176,100, then the per-employer exception) as gate + `choose` + refusal, read off the text.

## Extension map

- **Atoms and semantics**: `engine/src/atoms.ts` (vocabulary lists), `engine/src/eval.ts` (evaluation; the `Value` union needs a refusal kind), `engine/src/check.ts` (typing and guard analysis — note its limits: interval guards tile from their lowest bound, and each def's domain containment by its callers is by construction, not proved).
- **Renderer and values sheet**: `engine/src/render.ts`, `engine/src/output.ts`.
- **Data**: `forms/2025/` (add the W-2 and Schedule 3 definitions; wire into `f1040.yaml`), `params/2025.yaml` (new constants), `ambiguities/2025.yaml` if anything is silent.
- **Schema**: `schema/data.schema.json`.
- **CLI**: `engine/src/main.ts`. Commands today: `build`, `render`, `eval --inputs F [--json]`, `conjecture`, `record-fixtures`, `test-fixtures`, `coverage`, `mutate`, `compare`. Spec 2.8 expects interview commands (start / advance / record an answer) in this stage.
- **Fixtures**: `engine/src/fixtures.ts` with `fixtures/2025/stage1.json`. The tool currently hardcodes the stage-1 path — generalize it; do not fork it. Suggested new cases: multi-employer excess; no credit (wages at or below $176,100); one employer at exactly $10,918.20 vs one cent more; the refusal case producing the Form 843 remedy; boundary values around both constants.
- **Lean**: `lean/TaxFormalization/` plus `lean/Main.lean`; the two-evaluator harness is `engine/src/compare.ts` — extend its target set to the Stage 2 lines and keep it green.
- **Interview engine**: nothing exists yet; design section 3 places questions and ordering under `interview/`.
- **Outputs**: `canonical/` is generated and git-ignored; `rendered/` and `reports/` are committed.

## Definition of done (checklist)

- [ ] `sum_over` implemented across the checker, schema, evaluator, renderer and Lean (with its lemma for the atoms used), and the TypeScript and Lean evaluators agree on the Stage 2 fixtures and generated inputs.
- [ ] Fixtures cover both sides of every branch (coverage report), including: the multi-employer excess; the no-credit path; employer-withholding exactly at $10,918.20 vs more; total wages exactly at $176,100 vs more; and the single-employer refusal with the remedy named and cited.
- [ ] The interview path works end to end through the command-line program: answers in, values sheet with derivations out.
- [ ] Rendered definitions committed for the owner's line-by-line read.
- [ ] Mutation and coverage reports regenerated; surviving mutants listed and classified.
- [ ] `npm run check-all` green (it builds the data, renders, runs the Tax Table conjecture, the fixtures through the CLI, coverage, mutation, and the evaluator-agreement comparison).
- [ ] `PROJECT_INDEX.md` updated. Then stop and report to the owner before Stage 3.

## How to work with him

- Stop at the end of the stage and at any decision with more than one defensible answer. Ask; it is expected behavior here, not friction.
- Keep the work at a size he can check. He has to be able to vouch for what is produced.
- When you report something as done, say what you actually inspected and what you are inferring.
- Two person-side steps are his, by precedent (design section 4): the line-by-line render read against the archived pages, and hand-working the class B fixture expectations. Generate those artifacts so they are fast to review.
- Commits: coherent units, larger rather than micro; no destructive git operations without explicit approval.

## State of the repository

- Clean tree. Latest commits: `bd35a5c` (Stage 1 evaluator, CLI, fixtures, Lean reference evaluator, reports), `919322a` (Stage 1 data format, checker, renderer), `dd91523` (rate-schedule source).
- Toolchain already installed on this machine: Node 24 + npm, TypeScript 7 (strict config in `engine/tsconfig.json`), Lean v4.29.1 through elan, `pdftotext`, Python 3.
- Baseline check: `npm ci && npm run check-all` should be green before you touch anything.
- Open owner items from Stage 1 (may arrive as corrections — fold them in as ordinary fixes): the render read and the class B hand-work.
- New sources, if a premise needs one: `python3 tools/fetch_sources.py` after reading `tools/README.md`; the manifest is the source of truth, and the offline verifier must stay green.

## Gotchas that will cost you an hour

- **Lean has no Mathlib** (core only): no `ring`, no `set`, sparse `Int` lemma names, `omega` is your friend (it handles `min`/`max`). `TaxFormalization/Lemmas.lean` shows the working style, including the `generalize`-instead-of-`set` pattern.
- The TypeScript is strict (`exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`) under the new native compiler. `Json`-adjacent code and indexed access need care.
- Reference resolution: exact line id within the file first, then split on the first dot for cross-file references. Line ids are fully prefixed (`qdcg.line2`); def-internal ids are bare (`amount`); instances bind def parameters and memoize per binding.
- Rounding: money is integer cents; the only implicit rounding is `multiply_rate`'s half-up at the cent (recorded in `ambiguities/2025.yaml`). The return-wide rounding setting is deferred and not built.
- The standing stop condition: if more than roughly one line in eight needs an `opaque` escape, stop and reconsider the atom language with the owner. (Stage 1's share was zero.)
