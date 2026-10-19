# Design

Architecture, components and build order for the proof of concept defined in `spec.md`.

## 1. Shape

```
sources (archived IRS text, hashed)
        │  read by a human and, as one of two transcribers, a language model
        ▼
form data (YAML: lines, parameters, tables, gates, ambiguity register)
        │  build: schema validation + static checks → canonical JSON
        ├──────────────► renderer ──► English worksheets, for side-by-side audit
        ├──────────────► Lean 4: atom semantics, lemmas, reference evaluator
        ▼
TypeScript evaluator ──► values + derivations
        ▲                         │
interview engine                  ▼
(answer log)                values sheet and explanations
        ▲                         │
        └──── command-line program (the backend; every client and every integration test goes through it)
```

The form data is the product. Everything else either checks it or reads it. Nothing below the data layer contains tax rules.

## 2. Layers and components

### 2.1 Sources

`sources/<tax_year>/` holds the archived IRS documents the encoding was read from: HTML instructions and form PDFs, each with a manifest entry giving address, fetch date, revision or posted date, and content hash. Citations point at these snapshots.

A fetch script records what it retrieved. It is run by a person, deliberately, and is the only part of the repository that touches the network.

### 2.2 Form data

Authored as YAML, for readability and comments. One file per form or worksheet per revision; one parameter file and one ambiguity register per tax year; tables as their own files.

The build converts YAML to canonical JSON. The JSON is what the TypeScript evaluator, the Lean evaluator and third parties consume, so nothing downstream depends on a YAML parser.

Shape of a line, for illustration only. The wording is not checked against a revision.

```yaml
- id: qdcg.ordinary_portion
  printed: "5"
  label: "Subtract line 4 from line 1. If zero or less, enter -0-"
  type: NonNegDollars
  expr: { op: subtract_floor0, from: qdcg.taxable_income, take: qdcg.preferential_total }
  cite: { doc: i1040, tax_year: 2025, revision: "<posted date>", locator: "QDCG worksheet, line 5", snapshot: "<sha256>" }
```

### 2.3 Build-time checker

Written in TypeScript. It fails the build unless:

- the data validates against the schema;
- every `copy`, operand and `param` reference resolves within the stated revision;
- the line-level dependency graph is acyclic;
- every expression type-checks, including the non-negative refinement and the ban on mixing dollars and rates;
- every `choose` has exhaustive and disjoint guards, decided by enumeration over enumerated and Boolean guards and by interval analysis over thresholds;
- every line, parameter, gate and question has a complete citation whose snapshot hash exists in the manifest;
- every `opaque` use is listed in a published register.

### 2.4 Renderer

Each atom has one English template in IRS worksheet phrasing. The renderer produces, per worksheet, a document with the rendered line beside the IRS `label` and the citation. It is the main defence against mistranscription, so it is built before the evaluator is trusted.

Rendered output is committed, so a change in the data shows as a readable diff in review.

### 2.5 Evaluator

TypeScript, using `BigInt` for cents and rate components. No decimal library.

- Evaluation is lazy and memoized over the line graph. There is no fixed-point iteration.
- Each value carries a completeness state. An unknown operand makes the result unknown; a placeholder makes it a placeholder.
- Evaluating a line returns its value and its derivation: atom, operands with values, citation, rounding applied, and for `choose` the guards examined and not taken.
- Rounding is performed only by the `round` atom. The return-wide rounding setting decides which rounding lines are active.
- A refusal is a value, not an exception: evaluation reports which gate fired and its citation.

The evaluator is small enough to read in one sitting. It contains no form-specific code. `opaque` functions live in one directory, each with its citation and tests.

### 2.6 Lean 4

Written alongside the first worksheet, not after.

- `Atoms`: each atom defined over `Int`, mirroring the TypeScript semantics exactly, including half-up rounding.
- `Lemmas`: the properties listed in `spec.md` section 6.3.
- `Check`: the reference and acyclicity checker, with its soundness proof.
- `Eval`: a reference evaluator that reads the canonical JSON.

Continuous integration runs the Lean evaluator and the TypeScript evaluator over every fixture and over generated inputs, and fails on any difference. Lean is not shipped to users.

The claim made from this layer is narrow: the atoms have these properties, and two independently written evaluators agree. It is not a claim that the TypeScript evaluator is verified.

### 2.7 Interview engine

- The set of inputs needed is derived, not authored: it is the backward slice from the target lines, given the answers so far.
- The order, grouping and wording of questions are authored as data, each question tied to the input it fills and carrying a citation.
- Answers are stored as an append-only log. The whole return is recomputed from the log on every change.
- Gates are evaluated as early as their inputs allow, so a refusal arrives before the user has entered data that cannot be used.
- The checks in `spec.md` section 6.4 run in the build by enumerating answer combinations.

### 2.8 Command-line interface

The command-line program is the backend of the system. Every capability is reached through it: validating and building the data, rendering worksheets, starting and advancing an interview, recording an answer, evaluating a return, and producing the values sheet and explanations. It reads and writes structured data (JSON) as well as human-readable text, so another program can drive it.

Any later interface, including a browser one, is a client of the command-line program and holds no tax logic or interview logic of its own.

Integration tests exercise the system through the command-line program, as a user or client would: they invoke it with inputs and answer logs and assert on its output and exit status. They do not call engine internals. Unit and property tests of atoms and the evaluator may call code directly.

### 2.9 Output

A values sheet: each form in printed order with line number, label, value and citation, followed by the path explanation, any ambiguity notes, and the standing notices. Plain text and HTML, generated locally.

### 2.10 Test harness

- Fixtures are data: inputs, expected line values, evidence class, and the source of each expected value.
- Fixture-driven tests of worksheets, forms and whole returns are integration tests and run through the command-line program (section 2.8).
- A generator produces branch-covering inputs for a worksheet from its encoded structure. A person works those by hand on the official document to produce class B expectations.
- Property tests use fast-check.
- Differential tests run named, versioned independent calculators outside the repository and record their outputs as class C fixtures.
- A mutation tool applies single-atom mutations to a worksheet (swap `smaller_of` for `larger_of`, drop the floor, change an operand, shift a parameter) and reports which survive.
- A coverage report lists every line with the evidence classes that cover it.

## 3. Repository layout

```
sources/<tax_year>/            archived IRS documents and manifest
forms/<tax_year>/              form and worksheet definitions (YAML)
params/<tax_year>.yaml         year parameters
tables/<tax_year>/             Tax Table and other pinned tables
ambiguities/<tax_year>.yaml    ambiguity register
interview/                     questions and ordering
schema/                        JSON Schema for all data
engine/                        TypeScript: checker, evaluator, renderer, interview, output
lean/                          Lean 4: Atoms, Lemmas, Check, Eval
fixtures/<tax_year>/           test fixtures by evidence class
rendered/<tax_year>/           committed renderer output
tools/                         source fetcher, fixture generator, mutation tool, year diff
research/                      research pass
spec/                          this specification and design
```

## 4. Authoring a worksheet

1. Archive the source and record its hash.
2. Two independent transcriptions of the worksheet into YAML, each by a language model in an isolated context given only the archived text and the schema, neither having seen the other or any existing data. Differences are resolved against the source and the resolution is recorded (spec 6.5). A person may supply either transcription when available.
3. Run the checker.
4. Render, and compare the rendering against the IRS text line by line by an isolated model that has not seen the YAML. Record which model, which prompt, and which snapshot; a person may do this reading when available, and is recorded the same way.
5. Enter parameters separately and confirm each against a second official source where one exists.
6. Generate branch-covering inputs; have them worked on the archived worksheet by an isolated model (class M), or by a person when available (class B); add as fixtures.
7. Add every official example as a class A fixture.
8. Run differential tests and investigate every difference.
9. Run the mutation tool; add fixtures until the surviving mutations are understood and listed.

No language model output reaches the data without steps 3, 4 and 6. Every model invocation in steps 2, 4 and 6 runs under the AI Security and Isolation Protocol: isolated context, archived source and schema only, no network, model and prompt recorded.

## 5. Build order

Each stage ends with something a third party can run and check.

### Stage 0. Ground the premises

Archive the TY2025 Form 1040 instructions, Schedule D instructions, Form 8949 instructions and the forms in scope. Check each premise in `spec.md` section 10 against the archived text and record the finding.

Done when: every premise is confirmed or corrected in writing, with a locator.

### Stage 1. Format spike: tax on ordinary income and the Qualified Dividends worksheet

Schema, checker, renderer, evaluator, Lean atoms and the first command-line commands, exercised on the Tax Computation Worksheet, the Tax Table, and the Qualified Dividends and Capital Gain Tax Worksheet.

This tests whether the data format, citations and rendering are legible. It is a weak test of the architecture: no collections, no refusals, one path choice.

Done when:
- the rendered worksheets have been read against the IRS text;
- fixtures run through the command-line program;
- class B fixtures take both sides of every branch;
- the Tax Table midpoint conjecture has been tested against every cell and the result recorded;
- the Lean lemmas for the atoms used are proved, and the two evaluators agree;
- the mutation score is published;
- the share of lines needing `opaque` is known. If it is above roughly one line in eight, stop and reconsider the atom language.

### Stage 2. Architecture test: excess Social Security tax withheld

Form W-2 as a collection, grouping by person, the per-employer rule, a year parameter, Schedule 3, and the first refusal gate.

Done when: `sum_over` and gates work end to end from interview answers to a values sheet with derivations, and the single-employer case produces a cited refusal with the correct remedy named.

### Stage 3. Sales: Form 8949 and Schedule D

Manual entry of sales, classification into boxes A to F, the aggregate path for lines 1a and 8a, the supported adjustment codes, Schedule D through line 22, and the choice between the two tax worksheets.

Done when: the official single-transaction examples in the Schedule D and Form 8949 instructions pass as class A fixtures, and the rounding question between row and total rounding has an entry in the ambiguity register.

### Stage 4. The remaining forms

Schedule A with Forms 4952 and 8283 and the choice between it and the standard deduction; Schedule B; the Schedule D Tax Worksheet with its two feeder worksheets; Form 8959; Form 8960; Forms 8995 and 8995-A for section 199A dividends, with cited form selection; the simple foreign tax credit path; Schedule 2.

Done when: every refusal in `spec.md` section 2.2 has a gate, a citation and a test.

### Stage 5. Whole return

Form 1040 end to end, the full interview, the values sheet, whole-return differential tests, the interview checks, and the per-line evidence report.

Done when: one command, with no network, rebuilds the data, runs every check and test, and produces the reports.

### Stage 6. Tax year 2026

Archive the TY2026 documents as they are published, produce the diff, re-derive the fixtures, and release only against final documents.

Done when: the TY2026 return for the proof-of-concept slice passes every check of Stage 7 that exists at the time, and the year-diff tool reports every changed line, parameter and table cell.

### Stage 7. Integrity stack

The independent constructions of spec 6.5, built as pipeline steps and run by `check-all`: the engine differential over generated returns, the second transcription of every existing worksheet with its disagreement log, the render comparison, class M hand-work for every worksheet's branch-covering inputs, and the data-level properties of spec 6.3. Mutation survivors and unasserted lines are driven down with the fixtures these produce.

Done when: every existing worksheet has a second transcription and a logged adjudication; every generated branch has a class M or B fixture; the engine differential runs over at least a thousand generated returns per supported year with every difference carrying a cited cause; and the evidence report shows no computed line without an asserted fixture.

### Stage 8. Household architecture test

One dependent: the qualifying-child tests, head of household, the child tax credit with its refundable part, and the credit for other dependents. Small by design; the question is whether the atom vocabulary expresses household predicates without `opaque` escapes, and whether the person dimension carries relationships, ages and months without rework.

Done when: the slice passes the Stage 7 checks, and the share of lines needing `opaque` is published. If that share exceeds one in eight, the atom language is reconsidered before Stage 9.

### Stage 9 onward. Coverage

The items of spec 2.4 in order, one or more per stage, each with the Stage 7 checks. Direct File's public scenarios and other published cases become comparators where their situations fall in scope. New York follows federal coverage as its own stage sequence with its own sources.

## 6. Choices made here that are open to challenge

- YAML for authoring with canonical JSON as the published form. A typed TypeScript builder is the alternative.
- `table_lookup` and `bracket_schedule` as two atoms.
- Schedule A limited to medical, state and local taxes, Form 1098 mortgage interest, investment interest (Form 4952) and gifts to charity (Form 8283 Section A for non-cash), with the rest refused.
- Form 8949 adjustment codes limited to B and W.
- fast-check for property tests.
- Rendered output committed to the repository.
