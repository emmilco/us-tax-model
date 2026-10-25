# Handoff: begin the build

**Historical Stage0 starter prompt.** This records the original setup and repository state, not the
current execution instructions. Read `HANDOFF-INTEGRITY.md` and
`docs/2026-10-24_validation_policy.md` for current policy and priorities. The owner has retired the
mandatory packet/ruling-sample workload; Stage0 confirmation and the historical "start here" steps
below must not restart completed work or supersede that amendment.

You are starting the implementation phase of this project in a fresh session. A research-and-design phase is complete and committed. Your job is to build the proof of concept in the stages set out in `spec/design.md`, beginning with Stage 0, stopping for my review at the end of each stage.

## What this project is

An open, verifiable formalization of the IRS individual income tax forms-and-instructions layer, plus a guided self-preparation tool as its first client. The formalization is the primary asset. Trust is meant to come from two kinds of evidence a non-programmer can check: forensic (a citation on every line, encoded lines rendered back as IRS-style English for side-by-side comparison, labelled tests) and structural (a small closed set of primitive operations with proved properties, from which every computation is composed). The user files their own return; the software never files, signs or transmits.

## Read these first, in this order

1. `spec/spec.md` — scope, refusals, data model, provenance model, test strategy. This is the agreed contract.
2. `spec/design.md` — architecture, components, repository layout, authoring procedure, build order.
3. `research/report.md` — why these choices were made, and what the research could not verify.
4. `PROJECT_INDEX.md` — current folder structure. Keep it accurate as you add directories.

Consult `research/01` to `06` only when a stage needs the detail.

## Decisions already made; do not reopen without cause

- Build fresh. Not on Catala, not on IRS Direct File or the Fact Graph engine.
- Forms are data: one record per IRS line, each a single application of an atom from a frozen vocabulary, each with a mandatory structured citation.
- Money is integer cents; rates are integer pairs; rounding only through an explicit, cited rounding step. No floating point anywhere.
- TypeScript for the engine, chosen for type safety. Lean 4 for atom semantics, lemmas and a reference evaluator, written alongside the first worksheet and not afterwards.
- **The command-line program is the backend of the system.** Every capability is reached through it and any later interface is its client. **Integration tests exercise the system through the command-line program**: they invoke it and assert on its output and exit status. Only unit and property tests of atoms and the evaluator call code directly.
- Development targets tax year 2025 final forms and instructions. Tax year 2026 follows as a reviewed diff when its instructions are published.
- Rounding is a return-wide setting, whole dollars by default.
- Stock sales are entered manually. No broker import.
- Output is a cited line-by-line values sheet. Filling official PDFs is deferred.
- Form 1116 is deferred and must be returned to after the proof of concept. Only the simple foreign tax credit path is built now.
- Licences: Apache-2.0 for code; CC0 for form definitions, parameters, tables and fixtures.
- No language model in the runtime path.

## Hard constraints

- **Never read the owner's personal tax documents**, and never ask for them to be pasted or run through a shell command whose output enters the session. Any figure you need from a document, the owner types. Fixtures are synthetic or from official IRS examples. No personal figures are stored in the repository.
- The tool runs locally and makes no network calls carrying return data. The only network use in the repository is the deliberate source-fetch script.
- No e-file data, no automation of IRS systems, no hosting, no telemetry.
- No IRS or Treasury insignia; no claims of accuracy, approval or certification.
- Do not call the Anthropic API from code.
- Do not write implementation ahead of the stage you are in.

## The most important warning

The research was done by web-only agents reading through a summarising tool. Nearly every tax fact in `research/` is unverified testimony, including worksheet wording, thresholds and the conditions that select one worksheet over another. **Do not encode any line from memory or from the research files.** Encode only from IRS text you have archived in `sources/` and read yourself. `spec/spec.md` section 10 lists the premises that must be checked first.

One research finding you should carry: no official source was found that supplies expected values for the Qualified Dividends and Capital Gain Tax Worksheet or for a whole return in scope. The IRS e-file test scenario that includes Schedule D appeared, on the four pages viewed, to give inputs with computed lines left blank. Worksheet arithmetic therefore rests on hand-worked branch-covering cases, runs against independent calculators, and a published mutation score. Label every expected value with its evidence class and do not present calculator agreement as official confirmation.

## Start here: Stage 0

1. Give me an intent readback of the build as you understand it and wait for my confirmation.
2. Check the toolchain on this machine (Node and package manager, Lean via elan, `pdftotext`) and tell me what is missing before installing anything.
3. Write the source-fetch script and archive the TY2025 documents needed for the scope in `spec/spec.md` section 2.1 into `sources/2025/`, with a manifest recording address, fetch date, revision or posted date, and content hash. IRS current-year addresses change content when a new year is released, so the hash matters.
4. Check each premise in `spec/spec.md` section 10 against the archived text. Record each finding with a locator, as confirmed or corrected, in a file under `sources/2025/`.
5. Where a premise is wrong, propose the change to the spec and stop for my decision.

Stage 0 is done when every premise is confirmed or corrected in writing. Then stop and report before Stage 1.

## How to work with me

- Stop at the end of each stage and at any decision with more than one defensible answer. `spec/design.md` section 6 lists choices that were made without my explicit ruling; raise any of them if the work gives a reason to.
- Keep the work at a size I can check. I have to be able to vouch for what is produced.
- When you report something as done, say what you actually inspected and what you are inferring.
- Stage 1 has a stop condition: if more than roughly one line in eight needs an `opaque` escape, stop and reconsider the atom language with me.

## State of the repository

One commit containing `PROJECT_INDEX.md`, `research/` and `spec/`. This file is not yet committed. There is no code, no `sources/` directory and no toolchain configuration.
