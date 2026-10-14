# Tooling and language choice

## Summary

- **Recommendation: a hybrid.** Form and worksheet definitions are stored as plain data (YAML or JSON with a schema) in a closed expression language over about 15 atoms. A TypeScript interpreter using integer arithmetic (`BigInt` cents and integer-pair rates, no decimal library) evaluates them and produces traces. A renderer prints every line back in IRS worksheet phrasing. fast-check property tests cover atoms and compositions. A small Lean 4 mirror, added second, proves the atom lemmas and static checks. Exhaustive enumeration checks the interview tree, with Z3 only where numeric guards appear.
- **Runner-up: Catala used directly** (1.3.0, Apache-2.0). It is the only candidate with first-class default-and-exception semantics, exact money, a literate source format and JSON traces already built. It loses because it targets statute text rather than line-numbered worksheets, and because it does nothing for the atoms goal.
- The dominant risk is mistranscribing the IRS text, not arithmetic or type errors. No proof addresses that; the renderer, worked examples and differential testing do. This is my opinion, and it drives the ranking.
- Integer arithmetic removes the decimal-library question. Amounts are integer cents, rates are integer pairs, and rounding is an explicit atom. The same semantics can be stated identically in TypeScript, Lean and Z3.
- Lean 4 everywhere is rejected as the shipping stack. Its WebAssembly target is Tier 2 and the docs warn releases "may be silently broken". It is also the least accessible option for contributors.
- The IRS's own Fact Graph is the closest precedent and is alive again as a standalone CC0 repository at v3.1. Its operator list already shows the "small DSL grows" problem, and its spec defines no citation metadata.
- Proofs worth having are mostly static checks on the data: closed references, acyclicity, unit typing, citation coverage and non-negativity typing. Proving the interpreter correct, or building a verified extraction chain, would be proof theatre for this audience.
- The TY2026 sketch below uses worksheet wording recalled from a prior year, not verified against a 2026 revision.

## Candidates

### 1. Catala

- **Status.** Version 1.3.0 was added to opam on 1 Oct 2026; 1.0.0 is dated 10 Nov, presumably 2025. Apache-2.0, about 2.4k stars, 5,730 commits. (https://ocaml.org/p/catala/latest, https://github.com/CatalaLang/catala/releases — High)
- **Arithmetic.** Money is an arbitrary-precision integer count of cents (`Z.t`) and decimals are exact rationals (`Q.t`), both from Zarith. Money times decimal computes the exact product and rounds to the nearest cent; rounding money to the unit is a separate operator. (https://ocaml.org/p/catala/1.1.0/catala.runtime_ocaml/Catala_runtime/index.html — High for representation, Medium for tie-breaking, which I read only from source snippets.)
- **Traces.** `clerk run --trace --trace-format=json` exists. Generated OCaml, Python and Java can record traces; C cannot yet. (https://github.com/CatalaLang/catala/releases/tag/1.3.0 — High)
- **Verification.** The compiler has encoded its intermediate language into Z3, with conditions for "no empty value" and "no overlapping exceptions". I confirmed this through 1.1.0 docs only. The 1.3.0 opam page lists no z3 dependency, so its current status is unverified. (https://ocaml.org/p/catala/1.1.0/verification.html — Medium)
- **Precedent.** The ICFP 2021 paper formalized about 15% of IRC §121 in roughly 350 lines. (https://arxiv.org/pdf/2103.03198 — High)
- **Opinion.** Catala's unit is a statute article paired with a scope; the owner's unit is a numbered worksheet line. A worksheet has little default logic inside it, so the best feature is wasted there and useful only in the applicability layer. Installing means opam, Docker or Nix. I could not confirm a current JS backend; a `catala-js.opam` file exists.

### 2. Typed functional and pragmatic general-purpose languages

Library facts below are recollection unless a URL is given.

| Language | Exact money arithmetic | Property testing | Browser route |
|---|---|---|---|
| OCaml | Zarith `Z`/`Q`, exact (confirmed as Catala's dependency) | QCheck | js_of_ocaml / wasm_of_ocaml 6.4, with `zarith_stubs_js` (https://discuss.ocaml.org/t/ann-js-of-ocaml-wasm-of-ocaml-6-4/18282 — Medium) |
| F# | `System.Decimal`, 96-bit, `MidpointRounding`; `BigInteger` | FsCheck | Fable |
| Haskell | `Integer` and `Rational` in base; `Data.Fixed` | QuickCheck, Hedgehog | GHC JS/Wasm backends, immature |
| Scala | `BigDecimal` plus `RoundingMode`; `BigInt` | ScalaCheck | Scala.js, as the Fact Graph does |
| Rust | `rust_decimal` 1.43.0: 96-bit mantissa, scale 0–28, `RoundingStrategy` (https://docs.rs/rust_decimal/latest/rust_decimal/ — High); `num-bigint` | proptest | Wasm, excellent |
| TypeScript | No native decimal. TC39 Decimal is still Stage 1 (https://github.com/tc39/proposal-decimal — High). Native `BigInt`; decimal.js is MIT and arbitrary precision | fast-check v4.10.2 (https://github.com/dubzzz/fast-check/releases — High) | Native |
| Python | Stdlib `decimal`: eight rounding modes, `quantize`, and an `Inexact` trap that turns silent rounding into an exception (https://docs.python.org/3/library/decimal.html — High); `fractions.Fraction` | Hypothesis 6.15x | Pyodide 314.0.3, a heavy download (Medium) |

**Opinion.** Written as ordinary functions, all of these fail the first criterion: a lay auditor cannot read `max(0n, l3 - l4)` in any of them. They also bury the dependency graph in code, so traces, citations and year-to-year diffs must be bolted on. They are host languages for an interpreter, not representations.

On AI assistance: older MultiPL-E work shows a clear gap for low-resource languages such as OCaml (https://arxiv.org/pdf/2410.03981 — Medium, dated). My opinion is that TypeScript, Python and Rust are handled best, OCaml, Haskell, Scala and F# adequately, and Lean, F*, Agda and Idris worst for proof work.

### 3. Dependently typed and refinement-typed tools

- **Lean 4.** 4.35.0 was released 2026-10-12, on a roughly monthly cadence. (https://lean-lang.org/doc/reference/latest/releases/ — High) Emscripten WebAssembly is Tier 2: cross-compiled, untested in CI, "may be silently broken". (https://lean-lang.org/doc/reference/latest/platforms/ — High) Plausible provides property testing, Apache-2.0. (https://github.com/leanprover-community/plausible — High)
- **F\*.** v2026.10.11 was published 11 Oct 2026. (https://github.com/FStarLang/FStar/releases — High)
- **Rocq.** 9.3.0, seen only in distro packaging notices. (https://discourse.rocq-prover.org/c/announcements/8 — Medium)
- **Dafny.** 4.11.0 is the latest, dated 25 Aug with the year not shown. If that is 2025, there has been no release in over a year. It compiles to C#, Python, Go, JavaScript and Java. (https://github.com/dafny-lang/dafny/releases — Medium)
- **Liquid Haskell.** Builds with GHC 9.14.1 and supports "only one version of GHC at any given time". (https://github.com/ucsd-progsys/liquidhaskell — High) That is a yearly maintenance tax.
- **Agda, Idris.** Not checked live. My opinion is that their ecosystems are too thin for a solo shipping project.

**Opinion on "write everything in it".** This costs more than it returns. The properties that need dependent types here are few, the auditor cannot read the result, and contributors disappear.

**Opinion on "verify the atoms, then mirror".** This is the right use, and Lean 4 is the right tool: an active toolchain, executable, and it reads JSON. Because form definitions are data, Lean can load the same files the shipping engine loads. That allows a reference interpreter and static checks without any extraction chain. Dafny is the second choice; it is more SMT-automatic but its release cadence is a concern.

### 4. Data-first precedents

- **Direct File.** The repository is archived and "no longer maintained". (https://github.com/IRS-Public/direct-file — High)
- **Fact Graph.** It now lives separately at https://github.com/IRS-Public/fact-graph, described as "production-ready", at v3.1 and CC0. It is developed privately and mirrored publicly. Scala 3 runs on the JVM and, through Scala.js, in JavaScript. (High)
- **Fact Graph spec.** Facts are `Writable` or `Derived`. Types include `Dollar` (a BigDecimal) and `Rational`. Operators include `Add`, `Subtract`, `GreaterOf`, `LesserOf`, `Round`, `Floor`, `Ceiling`, `Switch` and `StepwiseMultiply`. They also include `AddPayrollMonths`, `PayrollMonthsBetween`, `Today`, `LastDayOfMonth`, `IndexOf` and `Filter`. Placeholders and `IsComplete` give reasoning over incomplete information. The spec defines no citation metadata. (https://raw.githubusercontent.com/IRS-Public/fact-graph/main/docs/fact-dictionary-specification-3.1.md — High)
- **Fact Graph's own assessment.** Its design record admits Direct File developers found Scala harder to modify, that the team "may lack resources", and that many names are not final. (https://raw.githubusercontent.com/IRS-Public/fact-graph/main/docs/fact-graph-3.1-adr.md — High)
- **Opinion.** The Fact Graph validates the architecture of declared facts, a small engine and completeness-driven interviewing. It also warns: its operator list has already grown domain-specific verbs, and XML is not lay-legible. Borrow the completeness model; do not adopt the engine.
- **PolicyEngine-US.** AGPL-3.0, Python, very active, with `1.824.7` cited as a published version. (https://github.com/PolicyEngine/policyengine-us — High) It models the law for microsimulation, not forms. I recall it uses NumPy floats but could not confirm that from the docs. It is useful only as a black-box differential oracle, and AGPL precludes borrowing code under a permissive licence.
- **DMN.** Completeness and overlap of decision tables are well studied. Calvanese et al. use a geometric hyper-rectangle algorithm and note that Z3 gives only yes/no without naming the missing or overlapping rules. (https://arxiv.org/pdf/1603.07466.pdf — High) DMN's FEEL numbers and spreadsheets fail the no-float and diffability constraints (opinion).
- **CUE, Dhall, Nickel.** CUE is at v0.17.0 with a v0.18 alpha, still pre-1.0 with breaking syntax changes. (https://newreleases.io/project/github/cue-lang/cue/release/v0.17.0 — Medium) I did not verify Dhall or Nickel. My opinion is that a configuration language adds a toolchain where YAML plus JSON Schema plus the engine's own checker does the same job.

### 5. Hybrid

This composes parts verified above: `BigInt`, fast-check, Lean 4, Plausible and Z3. The assessment is in the Comparison and Recommendation sections.

## Comparison

Scores are 1 to 5 and are my judgment. The criteria are: 1 lay legibility, 2 default/exception fidelity, 3 decimal arithmetic, 4 testability, 5 traces and citations, 6 yearly diffing, 7 contributor accessibility, 8 atoms and structural evidence.

| Candidate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| **Hybrid: data atoms, TypeScript engine, renderer, Lean mirror** | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | **37** |
| **Catala direct** | 3 | 5 | 5 | 4 | 4 | 3 | 2 | 2 | **28** |
| Python with types, plain code | 3 | 2 | 4 | 5 | 3 | 2 | 5 | 1 | 25 |
| Haskell | 2 | 3 | 4 | 5 | 3 | 2 | 2 | 3 | 24 |
| OCaml | 2 | 3 | 5 | 4 | 3 | 2 | 2 | 3 | 24 |
| Lean 4 for everything | 1 | 3 | 5 | 3 | 3 | 2 | 1 | 5 | 23 |
| TypeScript, plain code | 2 | 2 | 3 | 4 | 3 | 2 | 5 | 1 | 22 |
| Dafny for everything | 2 | 3 | 4 | 3 | 2 | 2 | 2 | 4 | 22 |
| Rust | 1 | 3 | 4 | 4 | 3 | 2 | 3 | 2 | 22 |
| F# / Scala | 2 | 3 | 4 | 4 | 3 | 2 | 2 | 2 | 22 |
| Adopt Fact Graph | 2 | 3 | 4 | 3 | 2 | 3 | 2 | 2 | 21 |
| Liquid Haskell | 1 | 3 | 4 | 4 | 2 | 2 | 1 | 4 | 21 |
| DMN / spreadsheet | 4 | 3 | 2 | 2 | 2 | 2 | 4 | 1 | 20 |
| OpenFisca / PolicyEngine style | 2 | 2 | 1 | 4 | 2 | 4 | 4 | 1 | 20 |

Justifications for the notable scores:

- **Hybrid, criterion 1 = 5.** It is the only candidate where the audit artifact is generated English in IRS phrasing, set beside the PDF.
- **Hybrid, criterion 2 = 4.** Worksheets are procedural. Default-and-exception structure lives in the applicability layer, where Catala's labelled-exception idea should be borrowed.
- **Hybrid, criterion 6 = 5.** A year's change is a textual diff of data files plus a diff of rendered English.
- **Hybrid, criterion 8 = 4, not 5.** The proofs cover atoms and static properties of the data. They do not cover the TypeScript interpreter, which is tied to the Lean mirror only by differential testing.
- **Catala, criterion 1 = 3.** Literate pairing with source text is good, but the code half is still code, and it pairs with statute rather than a line-numbered worksheet.
- **Catala, criterion 7 = 2.** A niche language with an opam toolchain and thin AI training data.
- **Lean for everything, criterion 7 = 1 and criterion 4 = 3.** Very few contributors, and browser delivery is on a Tier 2 target.
- **OpenFisca style, criterion 3 = 1.** Vectorised NumPy; the float claim is unverified, but exact per-return rounding is not the design goal.
- **Spreadsheet, criterion 1 = 4.** Familiar to lay readers, but formulas hide in cells and arithmetic is binary floating point.

## The atoms question

### Proposed vocabulary

Values have four types: `Dollars` (integer cents), `Rate` (integer numerator and denominator), `Count` and `Bool`, plus enumerations such as filing status.

1. `input` — a taxpayer-entered value, with type and source box.
2. `line` — a reference to another line on this or another form.
3. `const` — a year-pinned parameter, cited to the instruction that states it.
4. `sum` — add a list of lines.
5. `subtract` — signed subtraction.
6. `subtract_floor0` — "if zero or less, enter -0-".
7. `smaller_of` and `larger_of`.
8. `multiply_rate` — amount times rate, with a mandatory rounding mode.
9. `round` — explicit unit and mode. Per the 2025 Form 1040 instructions: "drop amounts under 50 cents and increase amounts from 50 to 99 cents to the next dollar", and when adding amounts, "round off only the total". (https://www.irs.gov/instructions/i1040gi — High)
10. `by_status` — a lookup keyed on an enumeration.
11. `table_lookup` — a banded table such as the Tax Table, or a bracket schedule.
12. `test` — a threshold comparison yielding `Bool`; `all`, `any`, `not`.
13. `if` — choose between two expressions on a `Bool`.
14. `sum_over` — a total over a row collection, such as Form 8949 rows or Schedule B payers.
15. `opaque` — a named host-language function with its own citation and tests. Every use is listed publicly.

There are no user-defined functions, no variables other than lines, no loops, no strings and no recursion. That closure is where the proofs come from.

### Properties worth establishing

| Property | How | Value to a lay reader |
|---|---|---|
| Every reference resolves; no line is defined twice | Static check in the engine, mirrored in Lean | High: "nothing dangles" |
| No cycles in the line graph | Topological sort; Lean proof that the checker is sound | High |
| Totality, termination, determinism | Free from the closed language: structural recursion over a finite acyclic graph, no clock, no randomness | High, and nearly free |
| Unit consistency | A typing judgment on atoms; never dollars times dollars or dollars plus rate | High |
| Non-negativity where the form says "enter -0-" | A `NonNeg` output type on `subtract_floor0`, propagated through `sum`, `smaller_of` and non-negative rates | High |
| Every line has a citation | Required schema field plus lint | High; it is the forensic claim |
| Rounding atom is correct | Lean proof of half-up on integers; idempotence | Medium |
| Monotonicity and bounds (0 ≤ tax ≤ top rate × taxable income) | Per-atom monotone/antitone lemmas in Lean with a sign analysis over compositions; end-to-end by property test | Medium. State it narrowly, as line 16 tax in taxable income with other inputs fixed. Tax law has real cliffs, and a global claim would be false. |
| Interview is total, terminates, has no contradictory states, and every path ends in a complete form set | Exhaustive enumeration over the finite enumeration and Boolean answers; Z3 only where numeric thresholds guard branches | High |

### Proof theatre

All of these are my opinion.

- Proving the TypeScript interpreter correct against a semantics that is itself an interpreter.
- A verified extraction or compilation chain.
- Headline lemmas such as "`smaller_of` is commutative".
- Encoding forms as dependent types.
- Any "formally verified taxes" framing. The theorem is always relative to the transcription, and the transcription is where errors will be.

### Illustrative sketch

This is illustration only. The wording is recalled from a prior-year Qualified Dividends and Capital Gain Tax Worksheet, not checked against a TY2026 revision.

```yaml
worksheet: qdcgt
tax_year: 2026
revision: "<pinned Form 1040 instructions revision>"
lines:
  - id: 4
    op: sum
    of: [line 2, line 3]
    cite: {doc: i1040, worksheet: qdcgt, line: 4}
  - id: 5
    op: subtract_floor0
    from: line 1
    take: line 4
    cite: {doc: i1040, worksheet: qdcgt, line: 5}
  - id: 6
    op: by_status
    of: const qdcgt.zero_rate_ceiling
    cite: {doc: i1040, worksheet: qdcgt, line: 6}
  - id: 7
    op: smaller_of
    of: [line 1, line 6]
    cite: {doc: i1040, worksheet: qdcgt, line: 7}
  - id: 8
    op: smaller_of
    of: [line 5, line 7]
    cite: {doc: i1040, worksheet: qdcgt, line: 8}
```

Rendered for audit, to lay beside the PDF:

```
4. Add lines 2 and 3.
5. Subtract line 4 from line 1. If zero or less, enter -0-.
6. Enter the amount for your filing status: ...
7. Enter the smaller of line 1 or line 6.
8. Enter the smaller of line 5 or line 7.
```

A trace entry for an invented example: `line 5 = 41,200 = max(0, line 1 [58,000] − line 4 [16,800])`, citing the 2026 worksheet, line 5.

## Recommendation

**Commit to the hybrid.**

1. **Representation.** YAML or JSON form definitions with a JSON Schema, one entry per IRS line, citation mandatory. Use no custom parser and no configuration language.
2. **Engine.** TypeScript with `BigInt` integer arithmetic and no decimal dependency. It runs in the browser with no install and as a CLI. Evaluation returns a value together with its derivation tree.
3. **Renderer.** Each atom has one English template in IRS phrasing. The rendered worksheet is a published artifact and is diffed year over year.
4. **Tests.** IRS worked examples as data fixtures. fast-check properties per atom and per form. Black-box differential runs against PolicyEngine-US and the Fact Graph where they overlap.
5. **Interview.** Rules as data with explicit, labelled exceptions in Catala's style. Use the Fact Graph's completeness idea to decide the next question. Check by exhaustive enumeration.
6. **Lean 4, phase two.** Build it only after the first slice passes its worked examples. Scope: atom semantics over `Int`, the lemmas in the table above, and a reference evaluator run natively in CI against the same data files. Budget it as a fixed, small workstream.

**Guardrails against DSL growth.** Freeze the atom list. Adding an atom requires a written justification and a renderer template. Count `opaque` uses and publish the count. If a form needs a loop, a local variable or a user-defined function, do not extend the language; write that form's piece as an `opaque` function.

**Runner-up: Catala directly**, with the IRS instructions as the literate text.

**What would change the recommendation:**

- A spike on the first slice shows more than roughly 10–15% of lines need `opaque`. Then the atom language is the wrong abstraction; move to Catala or typed host code with a tracing wrapper.
- The owner decides the lay artifact can be Catala's literate pairing rather than rendered worksheet English. Then Catala wins on effort.
- Lean's WebAssembly target reaches Tier 1. Then a single Lean implementation becomes defensible.
- The Fact Graph gains citation metadata, an explanation API and a stable spec. Then adopt it for the interview layer.
- The contributor pool turns out to be programming-language researchers rather than general programmers. Then use an OCaml host and reuse Catala's runtime.

## Could not verify / weak spots

- **Release years.** GitHub showed only day and month for Catala 1.0.0 through 1.2.1, Dafny 4.11.0 and fast-check 4.10.2. The Catala 1.3.0 year comes from opam.
- **Catala.** book.catala-lang.org and catala-lang.org returned no content. Money semantics come from runtime API docs for 1.0 and 1.1, not 1.3. I did not confirm the Z3 backend in 1.3.0, a JS backend, or any current US-tax example beyond the 2021 paper.
- **Fact Graph.** I read the spec and design record through a summarising fetch and saw no verbatim XML. Last-commit date is unknown. The design record's "Double" remark sits oddly beside `Dollar` as BigDecimal. I found no evidence of an explanation or trace feature, which is not evidence of absence.
- **Library facts from recollection.** .NET, Haskell, Scala, Dafny numerics, `BigInt`, and whether Lean's `Rat` is in core.
- **Not checked.** Dhall, Nickel, Agda, Idris, QCheck and proptest versions.
- **AI-assistant quality by language.** Opinion plus dated benchmarks; I found no current primary benchmark.
- **OpenFisca/PolicyEngine float usage.** Not confirmed.
- **Rounding rule.** Quoted from the 2025 instructions. TY2026 wording and any e-file whole-dollar requirement are unverified.
- **Scores.** The comparison is my judgment, not measurement. The gap between the hybrid and Catala is wide, but the ordering in the middle of the table is soft.

## Open questions

1. Should the engine carry cents and round only where the form rounds, or adopt whole-dollar rounding throughout? This changes the `round` atom's placement and every expected value in the fixtures.
2. Are YAML definitions authored by hand, or generated from a typed TypeScript builder with JSON as the canonical published form?
3. Can the renderer's output be compared automatically with text extracted from the IRS PDF, so wording drift is caught mechanically?
4. Which licence? CC0 matches the Fact Graph; AGPL sources can be used only as black-box oracles.
5. How large is the Lean budget, and who maintains it each year?
6. The Tax Table is banded and the Tax Computation Worksheet is not. Is `table_lookup` one atom or two?
7. Is the Fact Graph's fact dictionary worth mining for interview questions for this slice, even if the engine is not adopted?

## Sources

- https://github.com/CatalaLang/catala
- https://github.com/CatalaLang/catala/releases
- https://github.com/CatalaLang/catala/releases/tag/1.3.0
- https://ocaml.org/p/catala/latest
- https://ocaml.org/p/catala/1.1.0/catala.runtime_ocaml/Catala_runtime/index.html
- https://ocaml.org/p/catala/1.1.0/verification.html
- https://arxiv.org/pdf/2103.03198
- https://github.com/IRS-Public/direct-file
- https://github.com/IRS-Public/fact-graph
- https://github.com/IRS-Public/fact-graph/blob/main/LICENSE.md
- https://raw.githubusercontent.com/IRS-Public/fact-graph/main/docs/fact-dictionary-specification-3.1.md
- https://raw.githubusercontent.com/IRS-Public/fact-graph/main/docs/fact-graph-3.1-adr.md
- https://lean-lang.org/doc/reference/latest/releases/
- https://lean-lang.org/doc/reference/latest/platforms/
- https://github.com/leanprover-community/plausible
- https://github.com/FStarLang/FStar/releases
- https://github.com/dafny-lang/dafny/releases
- https://github.com/ucsd-progsys/liquidhaskell
- https://discourse.rocq-prover.org/c/announcements/8
- https://github.com/tc39/proposal-decimal
- https://scrapbox.io/petamoriken/2026-07_%E3%81%AE_TC39_meeting (secondary)
- https://github.com/MikeMcl/decimal.js
- https://docs.python.org/3/library/decimal.html
- https://docs.rs/rust_decimal/latest/rust_decimal/
- https://github.com/dubzzz/fast-check/releases
- https://github.com/PolicyEngine/policyengine-us
- https://openfisca.org/doc/coding-the-legislation/25_vectorial_computing.html
- https://arxiv.org/pdf/1603.07466.pdf
- https://www.irs.gov/instructions/i1040gi
- https://discuss.ocaml.org/t/ann-js-of-ocaml-wasm-of-ocaml-6-4/18282
- https://ocaml.org/p/zarith_stubs_js
- https://zenodo.org/records/21529338 (Pyodide 314.0.3)
- https://newreleases.io/project/github/cue-lang/cue/release/v0.17.0 (secondary)
- https://arxiv.org/pdf/2410.03981
