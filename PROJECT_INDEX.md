# tax-formalization — Project Index

An open, verifiable formalization of the IRS forms-and-instructions layer for US federal individual income tax, plus a guided self-preparation interview tool as its first client. The user files their own return; the software never files, signs, or transmits.

Stages 0–5 are implemented. Stage 5 computes the whole single-person return:
Form 1040 lines 1a–37 end to end, the full interview profile, whole-return
fixtures, per-line evidence coverage and the differential scaffolding. See
`reports/2025/stage5-review.md`. The product goal, coverage plan and
verification regime are in `spec/spec.md` sections 1, 2.4 and 6.5; the stages
that follow (integrity stack, household architecture test, coverage) are in
`spec/design.md` section 5. No human line-by-line reading is claimed; see the
trust statement in spec 3. Stage 7 (the integrity stack) and Stage 8 (dependents,
head of household and Schedule 8812) are complete; see `HANDOFF-STAGE-8.md` to
continue.

## Folder structure

| Path | Purpose |
|------|---------|
| `PROJECT_INDEX.md` | This file: structure, directory purposes, naming conventions |
| `HANDOFF-STAGE-8.md` | Current handoff: Stage 8 done, the accepted next step (fixtures and class M for the Stage 8 lines), facts a fresh session needs, process note |
| `HANDOFF-STAGE-7.md` | Previous handoff: the Stage 7 integrity stack in detail, with a Stage 8 section appended during the build |
| `HANDOFF-STAGE-2.md` | Stage 2 handoff and acceptance checklist (historical) |
| `spec/stage2-proposal.md` | Owner-approved modeling choices and concrete collection binding |
| `reviews/2025/stage2.md` | Preserved owner approval and hand-work record (not generated) |
| `interview/` | Cited 2025 question data and CLI/collection documentation; `full-2025.yaml` is the whole-return profile |
| `HANDOFF.md` | Prompt for starting the build in a fresh session: reading order, settled decisions, constraints, and the first stage |
| `spec/` | `spec.md` (scope, non-goals, data model, provenance, tests, versioning, explanation model) and `design.md` (architecture, components, build order). The agreed contract for the build |
| `research/` | Research pass outputs. `report.md` is the cross-workstream synthesis with the committed recommendation; one detailed findings file per workstream sits beside it |
| `sources/2025/` | Archived IRS sources (PDFs and instruction web-page snapshots), their extracted text in two forms (`<id>.txt`, `pdftotext -layout`; `<id>.cols.txt`, reading order from line boxes, with `<id>.pages.json` classifying each page as prose, table, mixed or single), the hash/revision manifest, and Stage 0 premise findings; sources require revision review before encoding |
| `TASKS.md` | The one tracked list of known, undone work: follow-ups from rulings and reviews, stage remainders, scope items, each with its source and trigger |
| `BUG_INVENTORY.md` | Append-only record of every defect caught, with cause, catch method and pattern tags (spec 6.6); `tools/check_bug_inventory.py` enforces append-only in `check-all` |
| `tools/` | Source fetcher (`fetch_sources.py`, which also derives and verifies the reading-order text), source catalog, reading-order extractor (`extract_text.py`), extraction conservation checks (`check_extraction.py`, in `check-all`), Tax Table extractor (`extract_tax_table.py`), bug-inventory check (`check_bug_inventory.py`); fixture generator and year diff land here or in `engine/` as they grow |
| `tools/extraction/` | Data for the conservation checks: the PDFKit reader (`pdfkit_text.swift`, an independent reading of the text layer), page furniture allowed to be absent from the HTML snapshots (`furniture.txt`), and accepted per-page differences with their reasons (`exceptions.json`) |
| `tools/transcription/` | Transcription agreement, render comparison and class M hand-work (spec 6.5); rulings live as data in `<form>.rulings.json` beside each log (`rulings.py`) and the logs are rendered from them: `transcribe.py` has an isolated model re-transcribe one form from its cited archived pages and compares the two structurally; `render_compare.py` has an isolated model judge each printed line's rendered English against the same pages; `classm.py` has an isolated model work a document by hand for branch-covering generated returns, producing class M fixtures; `rule.py` writes rulings into any of the three logs; `check_logs.py` verifies all three sets of logs offline in `check-all` |
| `reviews/2025/transcription/` | One log per form: pages given, model, prompt hash, every printed line's agreement or disagreement with both expansions, and the ruling on each disagreement, written against the source page |
| `reviews/2025/classm/` | One log per document worked by hand (class M): pages given, model and prompt hash per case, branches taken, each line's agreement with the model's arithmetic, and the ruling on each disagreement |
| `reviews/2025/render/` | One log per form: pages given, model, prompt hash, each printed line's MATCH / MISMATCH / UNCLEAR verdict with the model's reason, and the ruling on each non-match, written against the source page |
| `tools/engines/` | Engine differential (spec 6.5, class C at scale): case generator, adapters for PolicyEngine-US and Tax-Calculator, comparison and report; engines install into the git-ignored `.engines/` via `setup.sh` |
| `schema/` | JSON Schema for all canonical data (`data.schema.json`) |
| `forms/2025/` | Form and worksheet definitions as YAML: `f1040.yaml` (the implemented slice, lines 1a–37), `qdcg.yaml`, `tcw.yaml`, `tax_on_amount.yaml`; Stage 2 adds `w2.yaml`, `person.yaml`, `s3.yaml`; Stage 3 adds `sales.yaml` and `sd.yaml`; Stage 4 adds the remaining forms; Stage 8 adds `dependent.yaml` (per-dependent tests), `household.yaml` (filer facts and head of household) and `s8812.yaml` (Schedule 8812) |
| `params/2025.yaml` | Year parameters (bracket ceilings, Tax Computation Worksheet rows, table boundary), each with a citation |
| `tables/2025/` | Pinned data tables: `tax_table.yaml` (cell-by-cell 2025 Tax Table) and `rate_schedule.yaml` (Rev. Proc. 2024-40 schedules for the midpoint conjecture) |
| `ambiguities/2025.yaml` | Ambiguity register (readings chosen where the instructions are silent) |
| `engine/` | TypeScript: build (YAML to canonical JSON), checker, renderer, evaluator, interview, finite path checks, CLI integration tests, the generated-return arbitrary and data-level property tests (`generate.ts`, `properties.ts`), and the command-line program (the backend; every client and integration test goes through it) |
| `lean/` | Lean 4: atom semantics over the integers, lemmas, and the reference evaluator that reads the same canonical JSON |
| `fixtures/2025/differential/` | Calculator records (class C) and `engine_investigations.json`, the cited causes for engine differences |
| `fixtures/2025/classm.json` | Class M fixtures: generated returns whose worksheet lines an isolated model worked by hand; written by `tools/transcription/classm.py` |
| `fixtures/2025/stage*.json` | Test fixtures: covering cases with inputs, expected values, evidence labels and notes; Stage 3 adds official column-arithmetic examples; Stage 5 adds whole-return cases (`stage5.json`) and the calculator-record directory (`differential/`); `stage8.json` asserts the per-person dependent tests, the head of household tests and the Schedule 8812 chain across their branches and refusals; synthetic values remain regressions pending human hand-work |
| `rendered/2025/` | Committed renderer output (each line beside its IRS label and citation) for line-by-line review |
| `reports/2025/` | Generated reports: extraction conservation checks (`extraction.md`), Tax Table midpoint conjecture, branch/gate/arithmetic coverage, per-line evidence coverage, evaluator agreement, data-level properties over generated returns (`properties.md`), mutation score, calculator differential entry sheets, engine differential (`engine_differential.md`), Stage 2–5 review packets and CLI values sheets |

## Naming conventions

- Workstream findings: `research/<nn>_<snake_case_workstream>.md`, numbered in the order of the project brief:
  - `01_prior_art_formalization.md`
  - `02_prior_art_tax_software.md`
  - `03_source_material.md`
  - `04_legal_liability.md`
  - `05_tooling_language.md`
  - `06_architecture.md`
  - `07_text_extraction_prior_art.md` (added after the build: what another extraction pipeline offers this project; source of T-022 to T-024)
- Synthesis: `research/report.md`
- Spec documents: `spec/spec.md`, `spec/design.md`
- Form and worksheet definitions: `forms/<year>/<form>.yaml`; line ids are `<form>.<name>` and survive renumbering (the printed number is a field)
- Parameters and registers: one file per tax year (`params/<year>.yaml`, `ambiguities/<year>.yaml`)
- Tables: `tables/<year>/<table>.yaml`; generated tables record their extractor and source hash in a header comment

## Constraints on contents

- No personal tax documents or figures taken from them are stored in this repository. Fixtures are synthetic or drawn from official IRS worked examples.
- Money is integer cents; rates are integer pairs; rounding only through cited steps.
- Nothing below the data layer contains tax rules: every value is an atom application with a citation, and the build fails if a check fails.
