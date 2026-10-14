# tax-formalization — Project Index

An open, verifiable formalization of the IRS forms-and-instructions layer for US federal individual income tax, plus a guided self-preparation interview tool as its first client. The user files their own return; the software never files, signs, or transmits.

Stages 0–2 are implemented, and the owner approved proceeding after Stage 2.
Stage 3 adds manually classified securities sales, Form 8949 B/W adjustments,
Schedule D through line 22, loss limits, tax-method selection and a sales CLI
interview. Required Schedule D Tax Worksheet cases are refused until Stage 4.
See `reports/2025/stage3-review.md`; independent human hand-work remains pending.

## Folder structure

| Path | Purpose |
|------|---------|
| `PROJECT_INDEX.md` | This file: structure, directory purposes, naming conventions |
| `HANDOFF-STAGE-2.md` | Stage 2 handoff and acceptance checklist |
| `spec/stage2-proposal.md` | Owner-approved modeling choices and concrete collection binding |
| `reviews/2025/stage2.md` | Preserved owner approval and hand-work record (not generated) |
| `interview/` | Cited 2025 question data and CLI/collection documentation |
| `HANDOFF.md` | Prompt for starting the build in a fresh session: reading order, settled decisions, constraints, and the first stage |
| `spec/` | `spec.md` (scope, non-goals, data model, provenance, tests, versioning, explanation model) and `design.md` (architecture, components, build order). The agreed contract for the build |
| `research/` | Research pass outputs. `report.md` is the cross-workstream synthesis with the committed recommendation; one detailed findings file per workstream sits beside it |
| `sources/2025/` | Archived IRS sources (PDFs and instruction web-page snapshots), extracted text, hash/revision manifest, and Stage 0 premise findings; sources require revision review before encoding |
| `tools/` | Source fetcher (`fetch_sources.py`), source catalog, Tax Table extractor (`extract_tax_table.py`); fixture generator, mutation tool and year diff land here or in `engine/` as they grow |
| `schema/` | JSON Schema for all canonical data (`data.schema.json`) |
| `forms/2025/` | Form and worksheet definitions as YAML: `f1040.yaml` (selected lines), `qdcg.yaml`, `tcw.yaml`, `tax_on_amount.yaml`; Stage 2 adds `w2.yaml`, `person.yaml`, `s3.yaml`; Stage 3 adds `sales.yaml` and `sd.yaml` |
| `params/2025.yaml` | Year parameters (bracket ceilings, Tax Computation Worksheet rows, table boundary), each with a citation |
| `tables/2025/` | Pinned data tables: `tax_table.yaml` (cell-by-cell 2025 Tax Table) and `rate_schedule.yaml` (Rev. Proc. 2024-40 schedules for the midpoint conjecture) |
| `ambiguities/2025.yaml` | Ambiguity register (readings chosen where the instructions are silent) |
| `engine/` | TypeScript: build (YAML to canonical JSON), checker, renderer, evaluator, interview, finite path checks, CLI integration tests, and the command-line program (the backend; every client and integration test goes through it) |
| `lean/` | Lean 4: atom semantics over the integers, lemmas, and the reference evaluator that reads the same canonical JSON |
| `fixtures/2025/stage*.json` | Test fixtures: covering cases with inputs, expected values, evidence labels and notes; Stage 3 adds official column-arithmetic examples; synthetic values remain regressions pending human hand-work |
| `rendered/2025/` | Committed renderer output (each line beside its IRS label and citation) for line-by-line review |
| `reports/2025/` | Generated reports: Tax Table midpoint conjecture, branch/gate/arithmetic coverage and evidence, evaluator agreement, mutation score, Stage 2/3 review packets and CLI values sheets |

## Naming conventions

- Workstream findings: `research/<nn>_<snake_case_workstream>.md`, numbered in the order of the project brief:
  - `01_prior_art_formalization.md`
  - `02_prior_art_tax_software.md`
  - `03_source_material.md`
  - `04_legal_liability.md`
  - `05_tooling_language.md`
  - `06_architecture.md`
- Synthesis: `research/report.md`
- Spec documents: `spec/spec.md`, `spec/design.md`
- Form and worksheet definitions: `forms/<year>/<form>.yaml`; line ids are `<form>.<name>` and survive renumbering (the printed number is a field)
- Parameters and registers: one file per tax year (`params/<year>.yaml`, `ambiguities/<year>.yaml`)
- Tables: `tables/<year>/<table>.yaml`; generated tables record their extractor and source hash in a header comment

## Constraints on contents

- No personal tax documents or figures taken from them are stored in this repository. Fixtures are synthetic or drawn from official IRS worked examples.
- Money is integer cents; rates are integer pairs; rounding only through cited steps.
- Nothing below the data layer contains tax rules: every value is an atom application with a citation, and the build fails if a check fails.
