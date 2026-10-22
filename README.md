# tax-formalization

An open, verifiable formalization of the IRS forms-and-instructions layer for US federal
individual income tax, and a guided self-preparation interview tool built on it as its first
client. The product is a prepared, cited federal return: a tool that asks a person questions,
decides which forms apply, computes them, explains every value, and hands back a values sheet
the person files themselves. The formalization is a public, machine-readable encoding of IRS
forms, worksheets and instructions in which every line carries a structured citation to an
archived source and every computation is built from a small set of primitive operations with
proved properties. What is formalized is the IRS's published procedure, not the Internal
Revenue Code. The software never files, signs or transmits a return, and no return data leaves
the machine.

## Trust statement

*No human has read this encoding against the IRS text; it is verified by agreement among
independent constructions, and every disagreement is recorded.*

As of 2026-10-22 every construction behind that statement is one model family (Claude);
evidence from outside it comes from the engine differential only. The plan to change that is
`docs/2026-10-22_integrity_plan.md`.

## Standing notices

Shown at first run and on every output (`spec/spec.md` section 8):

- This is not tax or legal advice.
- The user is responsible for the return.
- The tool implements published IRS forms and instructions, which are not the law itself.
- It is not affiliated with or endorsed by the IRS.
- The list of what it covers and does not cover (below).

## What it covers and refuses

The forms and lines computed are listed in `spec/spec.md` section 2.1 and the situations
refused with a cited explanation in section 2.2; the stages built beyond that proof-of-concept
slice and the order of the remaining additions are in section 2.4. A refusal names the form
the tool cannot prepare, the answer or box that triggered it, and the instruction that requires
it; the tool never proceeds silently.

Coverage is measured over whole returns (a return counts only when nothing on it is refused)
and estimated by `tools/coverage/estimate.py`, which writes `reports/2025/filer_coverage.md`.
The current estimate is 68.6% of individual returns. Its caveat: 148 of the 157 refusal gates
in the forms are not measured (no IRS count or microdata variable), so the figure is of the
measured situations only and the true coverage is lower by the unmeasured gates' share.

## How to run everything

One command rebuilds the data, runs every check and records the tested tree:

```sh
npm install
npm run check-all
```

Prerequisites, as inspected when the toolchain was first checked (`tools/README.md`,
"Toolchain inspected"): Node and npm; Lean 4 through elan (`lean/lean-toolchain` pins the
version) with Lake; Poppler's `pdftotext`; Python 3 with PyYAML; curl. The extraction check
also runs `swift` for an independent PDFKit reading of the archived PDFs
(`tools/extraction/pdfkit_text.swift`), so it needs macOS with the Swift toolchain. The check
runs offline on a fresh clone. The engine differential (`tools/engines/README.md`) needs the two outside engines
installed once with `tools/engines/setup.sh`, the one network step; without them that step
skips visibly and the check is not claimed.

The commit guard is a git hook, enabled with:

```sh
git config core.hooksPath tools/hooks
```

It refuses any commit whose tree is not exactly the tree the last green `check-all` tested.

## Where things are

`PROJECT_INDEX.md` lists every directory and what it holds, the naming conventions and the
constraints on contents. `HANDOFF.md` and the current `HANDOFF-STAGE-*.md` are the reading
order for a session continuing the build; superseded handoffs are in `handoffs/`.

## Licences

Code is licensed under the Apache License, Version 2.0 (`LICENSE`). The data is dedicated to
the public domain under CC0 1.0 Universal (`LICENSE-DATA`): the form and worksheet
definitions (`forms/`), the year parameters (`params/`), the pinned tables (`tables/`), the
fixtures (`fixtures/`), the ambiguity register and its memos (`ambiguities/`) and the
interview question bank and profiles (`interview/`). The archived IRS sources under
`sources/` are IRS publications.
