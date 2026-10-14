# tax-formalization — Project Index

An open, verifiable formalization of the IRS forms-and-instructions layer for US federal individual income tax, plus a guided self-preparation interview tool as its first client. The user files their own return; the software never files, signs, or transmits.

The project is in its research-and-design phase. There is no implementation code.

## Folder structure

| Path | Purpose |
|------|---------|
| `PROJECT_INDEX.md` | This file: structure, directory purposes, naming conventions |
| `research/` | Research pass outputs. `report.md` is the cross-workstream synthesis with the committed recommendation; one detailed findings file per workstream sits beside it |
| `spec/` | `spec.md` (scope, non-goals, data model, provenance, tests, versioning, explanation model) and `design.md` (architecture, components, first vertical slice). Written only after the research conversation converges |

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

## Constraints on contents

- No personal tax documents or figures taken from them are stored in this repository. Fixtures are synthetic or drawn from official IRS worked examples.
