# us-tax-model

The forms-and-instructions layer of US federal individual income tax as public, cited, machine-checkable
data, with a guided self-preparation interview as its first client. The interview asks a person
questions, decides which forms apply, computes them, explains every value and hands back a values sheet
the person files themselves. The software never files, signs or transmits a return, and no return data
leaves the machine. What is encoded is the IRS's published procedure, not the Internal Revenue Code.

## Why you can check it

The encoding was written largely by language-model agents, so it cannot be trusted because of who wrote
it; it is built so that what matters can be checked from the repository alone by someone who trusts none
of the authors. Each layer states what it is, what it guarantees, what it does not, and where to look.

### 1. Forms as data, with a citation on every line

Each form or worksheet is a YAML file under `forms/<year>/`. A line is a record: id, printed line number,
IRS label, type, one expression, and a citation naming the document, tax year, revision, locator and the
hash of the archived page under `sources/<year>/` it was read from (`spec/spec.md` section 5).
Guarantees: the build fails if any line, parameter, gate or question lacks a citation or cites a hash
absent from the manifest, and `tools/citations.py` verifies every quote and locator against the archived
text; `reports/2025/citations.md` reports 2,313 anchors and 1,252 quotes, 0 findings without a recorded
ruling, and 305 computed-line locator segments too coarse to verify. Does not guarantee: that the
expression says what the cited page says. A citation proves a line points at a page, not that it was read
correctly.

### 2. A closed atom vocabulary

Every computed line is one application of one atom from the list in `spec/spec.md` section 4.2 (`sum`,
`subtract_floor0`, `smaller_of`, `multiply_rate`, `round`, `table_lookup`, `choose` and a dozen others);
there are no user-defined functions, loops, variables, strings or recursion. Guarantees: the whole
meaning of the data is the meaning of about twenty operations, each small enough to read; the one escape,
`opaque`, a host-language function, is counted and published, and `reports/2025/coverage.md` reports 0 of
2,384 lines use it. Does not guarantee: that the right atom was chosen for a line.

### 3. The build-time checker

`engine/src/check.ts` fails the build unless every `copy`, operand and `param` reference resolves within
the stated revision; the line graph is acyclic; every expression type-checks (cents, rates, counts and
booleans do not mix); every `choose` has exhaustive and disjoint guards, decided by enumeration and
interval analysis; and the provenance rules of layer 1 hold (`spec/design.md` section 2.3). Guarantees:
no dangling reference, cycle, unit confusion, or gap or overlap in a guarded alternative anywhere in the
data. Does not guarantee: agreement with the IRS text; a wrong operand that type-checks passes.

### 4. The renderer

Each atom has one English template in IRS worksheet phrasing, and the renderer writes every line's
English beside the IRS label and the citation into `rendered/<year>/`, which is committed. Guarantees: a
non-programmer can read any line against the printed form, and a change to the data appears in review as
a readable English diff. Does not guarantee: that anyone has done that reading.

### 5. Integer arithmetic

Money is integer cents, rates are integer pairs, and the evaluator (`engine/`, `BigInt`) has no floating
point. Rounding happens only in the `round` atom, only where a cited instruction says to round, by the
rule it states (`spec/spec.md` section 3, item 10). Guarantees: every value is exact and every rounding
is cited. Does not guarantee: that the IRS meant its arithmetic to be exact; where the text leaves
rounding open, the reading chosen is in `ambiguities/<year>.yaml`.

### 6. Lean

`lean/TaxFormalization/` defines every atom over the integers (`Atoms.lean`), proves the properties of
`spec/spec.md` section 6.3 (`Lemmas.lean`: `subtractFloor0_nonneg`, `roundHalfUpToUnit_idem`,
`prorate_le_amount`), and has a reference evaluator over the same canonical JSON as the TypeScript one,
proved to terminate and to be deterministic (`EvalProps.lean`). Both evaluators run over every fixture
and generated return; `reports/2025/evaluator_agreement.md` reports 1,648 cases, 2,895,826 line values
compared, 0 differences. Guarantees: the atoms behave as specified, and two independently written
evaluators of the same data compute the same values. Does not guarantee: anything about whether the data
matches the IRS text. Both evaluators read the same files, so agreement shows the evaluators agree, not
that the data is right. `BUG_INVENTORY.md` entry BUG-0001 is the canonical case: Form 1040 line 9 summed
line 3a as well as 3b; every fixture and both evaluators agreed with the wrong sum; an outside engine
caught it.

### 7. Independent constructions

No comprehensive human line-by-line reading is claimed, so the project supplements optional readings with constructions that share
nothing but the archived pages (`spec/spec.md` section 6.5): a second transcription of each worksheet by
an isolated model given only the pages and the schema, compared atom by atom with the project's; a render
comparison, in which an isolated model that has not seen the YAML reads each line's English against the
page; class M hand-work, in which an isolated model works branch-covering inputs on the printed
worksheet; and blind predictions of whole-return values made before the encoding was run. Each model runs
with no repository access and no network (`tools/transcription/README.md`); every disagreement is ruled
against the source with the page and quote recorded, and the logs are committed under `reviews/2025/`.
Guarantees: for each line, two readings of the same page produced the same structure, or the difference
is on record with its ruling. Does not guarantee: independence of the readers.

### 8. Engines

`tools/engines/` generates whole returns and runs them through three engines, PolicyEngine-US 2.49.4,
Tax-Calculator 6.8.5 and OpenTaxSolver 23.06, comparing line for line where the engine computes a line;
`reports/2025/engine_differential.md` covers 1,700 returns. Every difference must be explained to a cited
cause or the run fails; a margin is never accepted, and the current report lists no unexplained
difference. The line-level OpenTaxSolver adapter is in use; UsTaxes remains to be added under
`docs/2026-10-22_integrity_plan.md`. Guarantees: the summary lines the engines reach agree with code
written by other people from the rules. Does not guarantee: anything about worksheet lines the engines do
not compute; the first two primarily reach summary lines, while OpenTaxSolver also reaches worksheet lines.

### 9. The evidence report and the scoreboard

`reports/2025/evidence.md` lists every line with the classes of evidence that assert it (A, an official
IRS example; B, human hand-work; C, a named outside calculator; M, isolated model hand-work; H, human source reading; E, an
engine; R, the project's own regression; `spec/spec.md` section 6.1). Its first line is the scoreboard,
the share of computed lines with at least one assertion from outside the Claude model family. The
2026-10-24 regenerated report reads 198 of 1,515 (13.1%); H: 0, B: 0, second-family M: 44, E: 163
(the sub-counts overlap). This reflects the recorded numeric assertions after the skipped-response
audit; it does not establish complete form or whole-return coverage. Form2441's three missing STOP
outputs remain uncredited and its form-level review remains pending. Optional human findings no
longer prevent report generation. This report refresh is not a new full-suite pass. Guarantees: the evidence behind any line can
be looked up, and the one number the project is moving is printed first. H credits a source reading
with a current receipt and the exact log committed by its named reader; it supplies no worked values
and never fills B. The owner completed the first packet; original findings are preserved and current
H credit remains zero. Further human packets and ruling samples are optional under the
[2026-10-24 policy amendment](docs/2026-10-24_validation_policy.md). Does not guarantee: that a line
with only A, Claude-family M or R assertions has been checked by anyone but one model family.

### 10. Mutation testing, properties, interview checks

The mutation tool applies single-atom mutations to the data (swap `smaller_of` for `larger_of`, drop a
floor, change an operand) and asks whether the checker or a fixture notices; `reports/2025/mutation.md`
reports 2,278 mutants, 128 surviving, each with a written proof of equivalence, so 94.4% raw and 100.0%
with equivalents excluded. Property tests check the data-level properties of spec 6.3 over 400 generated
returns; `reports/2025/properties.md` reports 8 properties, all holding. The interview's finite path
checks (`engine/`, `spec/spec.md` section 6.4) enumerate answer combinations: every path ends in a
complete form set or a cited refusal, answer order does not change the return, and no question is asked
whose answer cannot reach a line. Guarantees: the fixtures are sensitive to the data they claim to test,
the stated invariants hold, and the interview has no dead ends. Does not guarantee: anything a mutation
cannot express or a fixture already encodes wrongly (BUG-0001 again).

### 11. The bug inventory and the commit guard

`BUG_INVENTORY.md` records every defect caught by any check or reading, before or with its fix: how it
was caught, the symptom, the root cause, why the existing checks missed it, the fix and its commit. It is
append-only; `check-all` fails if the committed prefix changes or the ids are not sequential.
`tools/hooks/pre-commit` refuses any commit whose tree is not the tree the last green `npm run check-all`
tested, and a run is green only if nothing outside its own outputs changed while it ran
(`tools/README.md`, "Commit guard"). Guarantees: the defect record cannot be edited, and no commit lands
without the whole suite having passed on that exact tree. Does not guarantee: that the suite catches what
it does not test for; the "why it survived" field exists to turn each such miss into a new check.

## What this does not establish

From `spec/spec.md` section 3, item 11: *human source-reading coverage is limited to the per-line
evidence records; independent constructions and their recorded disagreements provide the broader
verification.* The report identifies qualifying outside-family assertions and the source of each.
Unfinished verification is reported as a gap; adopting the requirement does not establish its completion.

The original layer-7 constructions used one model family, Claude. Flash has now completed transcription
and render calls over all 55 forms and worked six active Form 2441 cases and one W-2 return. Many
source disagreements and three blank numeric outputs after a Form2441 STOP remain; the second
family has not been promoted. The regenerated scoreboard credits 198 computed lines across the
recorded engine and second-family worked-value assertions; complete-form coverage remains separate.
Current source-reading eligibility is in `reports/2025/second_family.md`. Transcription/render readings are
subject to their individual gates. BUG-0129 exposed unit erasure in the transcription comparer;
transcription qualification is held until that defect and prior agreements are audited. Model worked
values and external-engine assertions are separate from this hold. Source readings are
reported separately and are not yet wired into the scoreboard. The amended integrity plan strengthens
second-family and engine checks, with human readings optional. Online tax interpretation is recorded
as non-authoritative corroboration under `research/secondary/`; it earns no scoreboard credit and
stays separate from blind source-only model requests.

The IRS forms and instructions are not the law. They embed judgments about the Internal Revenue Code that
are not announced, and this project encodes the published procedure, judgments included; where the text
is ambiguous or silent, the reading chosen is recorded in `ambiguities/<year>.yaml` and shown to the user
when it affects their return. No lawyer has reviewed the legal position the project operates under
(`spec/spec.md` section 9).

## Scope and coverage

The forms and lines computed are listed in `spec/spec.md` section 2.1, the situations refused with a
cited explanation in section 2.2, and the order of the remaining additions in section 2.4; the tool never
refuses silently. Coverage is measured over whole returns (a return counts only when nothing on it is
refused) by `tools/coverage/estimate.py` into `reports/2025/filer_coverage.md`, which today reads 68.6%
of individual returns. Its caveat: 148 of the 157 refusal gates are not measured (no IRS count or
microdata variable), so the figure is of the measured situations only and the true coverage is lower by
the unmeasured gates' share.

## How to run everything

One command rebuilds the data, runs every check and records the tested tree:

```sh
npm install
npm run check-all
```

Prerequisites, as inspected when the toolchain was first checked (`tools/README.md`, "Toolchain
inspected"): Node and npm; Lean 4 through elan (`lean/lean-toolchain` pins the version) with Lake;
Poppler's `pdftotext`; Python 3 with PyYAML; curl; and, for the extraction check's PDFKit reading of the
PDFs (`tools/extraction/pdfkit_text.swift`), macOS with the Swift toolchain. The check runs offline on a
fresh clone. The engine differential (`tools/engines/README.md`) needs the two outside engines installed
with `tools/engines/setup.sh`, the one network step; without them that step skips visibly and the check
is not claimed. The commit guard is a git hook, enabled with `git config core.hooksPath tools/hooks`.

## Standing notices

Shown at first run and on every output (`spec/spec.md` section 8):

- This is not tax or legal advice.
- The user is responsible for the return.
- The tool implements published IRS forms and instructions, which are not the law itself.
- It is not affiliated with or endorsed by the IRS.
- The list of what it covers and does not cover (above).

## Where things are

`PROJECT_INDEX.md` lists every directory, what it holds and the naming conventions. `HANDOFF.md` and the
current `HANDOFF-STAGE-*.md` are the reading order for a session continuing the build.

## Licences

Code is licensed under the Apache License, Version 2.0 (`LICENSE`). The data is dedicated to the public
domain under CC0 1.0 Universal (`LICENSE-DATA`): `forms/`, `params/`, `tables/`, `fixtures/`,
`ambiguities/` and `interview/`. The archived IRS sources under `sources/` are IRS publications.
