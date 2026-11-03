# Why you can check it: the checks in detail

The [README](../README.md) explains the project and walks its layers from the interview down to the
archived IRS page. This document is the reference behind that walk: each check in the repository,
what it guarantees, what it does not, and where to look. Figures are from the committed reports as of
2026-10-31; the reports themselves are current, this page is not regenerated.

The encoding was written largely by language-model agents, so it cannot be trusted because of who
wrote it. It is built so that what matters can be checked from the repository alone by someone who
trusts none of the authors.

## 1. Forms as data, with a citation on every line

Each form or worksheet is a YAML file under `forms/<year>/`. A line is a record: id, printed line
number, IRS label, type, one expression, and a citation naming the document and the locator on the
page; the build adds the tax year, revision and content hash of the archived source under
`sources/<year>/` from its manifest (`spec/spec.md` section 5, `engine/src/build.ts`). **Guarantees:**
the build fails if any line, parameter, gate or question lacks a complete citation or cites a document
absent from the manifest, and `tools/citations.py` verifies every quote and locator
against the archived text; `reports/2025/citations.md` reports 3,306 anchors and 2,731 quotes with 0
findings without a recorded ruling, and no computed-line locator too coarse to verify (the check runs
with `--strict`). **Does not guarantee:** that the expression says what the cited page says. A
citation proves a line points at a page, not that it was read correctly.

## 2. A closed atom vocabulary

Every computed line is one application of one atom from the list in `spec/spec.md` section 4.2 (`sum`,
`subtract_floor0`, `smaller_of`, `multiply_rate`, `round`, `table_lookup`, `choose` and the rest);
there are no user-defined functions, loops, variables, strings or recursion. **Guarantees:** the whole
meaning of the data is the meaning of about twenty operations, each small enough to read; the one
escape, `opaque`, a host-language function, is counted and published, and `reports/2025/coverage.md`
reports 0 of 2,951 lines use it. **Does not guarantee:** that the right atom was chosen for a line.

## 3. The build-time checker

`engine/src/check.ts` fails the build unless every `copy`, operand and `param` reference resolves
within the stated revision; the line graph is acyclic; every expression type-checks (cents, rates,
counts and booleans do not mix); every `choose` has disjoint guards, exhaustive over the range they
declare, decided by enumeration and interval analysis; and the provenance rules of section 1 hold
(`spec/design.md` section 2.3). **Guarantees:** no dangling reference, cycle, unit confusion, or overlap
between guarded alternatives anywhere in the data, and no gap within the range a set of interval guards
declares. **Does not guarantee:** agreement with the IRS text (a wrong operand that type-checks
passes), or that a set of interval guards covers every value its operand can take: the lowest declared
bound is not compared with the operand's domain (the Tax Computation Worksheet rows, for example, start
at the table boundary), and below it the evaluator returns "no guard matched" as an unknown.

## 4. The renderer

Each atom has one English template in IRS worksheet phrasing, and the renderer writes every line's
English beside the IRS label and the citation into `rendered/<year>/`, which is committed.
**Guarantees:** a non-programmer can read any line against the printed form, and a change to the data
appears in review as a readable English diff. **Does not guarantee:** that anyone has done that
reading.

## 5. Integer arithmetic

Money is integer cents, rates are integer pairs, and the evaluator (`engine/`; values held to safe
integers, products in `BigInt`) has no floating point. Rounding happens only where a cited instruction
says to round, by the rule it states, or, where the text is silent, by a reading recorded in the
ambiguity register (`spec/spec.md` section 3, item 10). **Guarantees:** every value is exact and every
rounding is cited or registered.
**Does not guarantee:** that the IRS meant its arithmetic to be exact; where the text leaves rounding
open, the reading chosen is in `ambiguities/<year>.yaml`.

## 6. Lean

`lean/TaxFormalization/` defines the arithmetic atoms over the integers (`Atoms.lean`, including the banded table lookup `tableBand`;
tests and `choose` are defined in the evaluator, `Eval.lean`), proves properties from `spec/spec.md`
section 6.3 (`Lemmas.lean`: non-negativity, rounding idempotence and bounds, proration bounds,
the direction of each atom in each ordered argument, with proved counterexamples where it is neither,
and correctness of the keyed, rate and banded table lookups), and has a reference evaluator over the same canonical JSON as the TypeScript one. That
evaluator is total by construction: each call spends from a step budget, so it always returns, and an
exhausted budget is an error value, never a number. `EvalProps.lean` states termination and
determinism, but as its own docstring says, their force comes from the definition being accepted as
total, not from the proofs. Both evaluators run over every fixture and over 400 generated inputs;
`reports/2025/evaluator_agreement.md` reports 1,994 cases, 4,470,945 line values compared, 0
differences. **Guarantees:** the proved atom properties hold, and two independently written evaluators
of the same data compute the same values. **Does not guarantee:** that the TypeScript evaluator is
formally verified (it is not), or anything about whether
the data matches the IRS text. Both evaluators read the same files, so agreement shows the evaluators
agree, not that the data is right. `BUG_INVENTORY.md` entry BUG-0001 is the canonical case: Form 1040
line 9 summed line 3a as well as 3b; every fixture and both evaluators agreed with the wrong sum; an
outside engine caught it.

## 7. Independent constructions

No comprehensive human line-by-line reading is claimed, so the project relies on constructions that
are made independently of the encoding from the archived pages (`spec/spec.md` section 6.5): a second
transcription of each worksheet by an isolated model given only the pages, the schema and the form's
published input interface (`tools/transcription/input_contracts/`), compared atom by atom with the
project's; a render comparison, in which an isolated model that has not seen the YAML
reads each line's English against the page; class M hand-work, in which an isolated model works
branch-covering inputs on the printed worksheet; and blind predictions of whole-return values made
before the encoding was run. Every model runs with no repository access and no network
(`tools/transcription/README.md`). Transcription and render reviews run under two model families,
Claude and DeepSeek, on every form; class M hand-work under the second family covers fewer forms (about
25, against about 55 under Claude), and blind predictions are not split by family. Every disagreement
must be ruled against the source with the page and quote recorded, and the logs are committed under
`reviews/2025/`. `reports/2025/second_family.md` compares the families: 149 form-and-kind pairs, 71
eligible and 77 pending. Ruled second-family model error is 8.6% in aggregate (401 of 4,661 lines
judged); the 10% limit applies per form-kind run, and several pending forms are well above it.
**Guarantees:** for each eligible review, two readings of the same page produced the same structure,
or the difference is on record with its ruling. **Does not guarantee:** independence of the readers;
two models reading the same English can share a misreading.

## 8. Engines

`tools/engines/` generates whole returns and runs them through four engines, PolicyEngine-US 2.49.4,
Tax-Calculator 6.8.5, OpenTaxSolver 23.06 and UsTaxes 0.1.23, comparing line for line where the engine
computes a line; `reports/2025/engine_differential.md` covers 1,700 returns. Every difference must be
explained to a cited cause or the run fails. No unexplained margin is accepted: the report's bounded
categories (`float`, within two units in the last place; `table-adjusted`, the engine computing from the
rate schedule where the form prescribes the Tax Table; `unrounded`) are each tied to a stated engine
cause, and the current report lists no unexplained difference. **Guarantees:** the lines the engines
reach agree with code written by other people from the rules. **Does not guarantee:** anything about
lines the engines do not compute, or about inputs the project's adapters figure for an engine rather
than the engine's own arithmetic (listed in the header of `reports/2025/evidence.md`); PolicyEngine-US
and Tax-Calculator reach mainly summary lines and a few form lines, while OpenTaxSolver and UsTaxes also
reach some worksheet lines.

## 9. The evidence report and the scoreboard

`reports/2025/evidence.md` lists every line with the classes of evidence that assert it (A, an
official IRS example; B, human hand-work; C, a named outside calculator; M, isolated model hand-work;
H, human source reading; E, an engine; R, the project's own regression; `spec/spec.md` section 6.1).
Its first line is the scoreboard, the share of computed lines with at least one assertion from outside
the Claude model family: **554 of 1,911 (29.0%)**, with H 0, B 0, second-family M 435 and E 220 (the
sub-counts overlap, and include lines credited through exact copies of an asserted line). H credits a source reading only with a current receipt and the exact log
committed by its named reader; it supplies no worked values and never fills B. Human packets are
optional under the [2026-10-24 policy amendment](2026-10-24_validation_policy.md). **Guarantees:** the
evidence behind any line can be looked up, and the one number the project is moving is printed first.
**Does not guarantee:** that a line with only A, Claude-family M or R assertions has been checked by
anyone but one model family.

## 10. Mutation testing, properties, interview checks

The mutation tool applies single-atom mutations to the data (swap `smaller_of` for `larger_of`, drop a
floor, change an operand) and asks whether the checker or a fixture notices; `reports/2025/mutation.md`
reports 2,722 mutants, 113 surviving, each with a written argument of equivalence, so 95.8% raw and
100.0% with equivalents excluded. Property tests check the data-level properties of spec 6.3 over 400
generated returns; `reports/2025/properties.md` reports 9 properties, all holding. The interview checks
(`engine/src/interview-check.ts`, `spec/spec.md` section 6.4) enumerate every finite answer for the
default profile (the Stage 2 Social Security credit slice, over the `stage2.json` fixtures) and walk the
five Stage 5 whole-return fixtures for the full profile: every walk ends in a complete form set or a
cited refusal, and reversing the answer order does not change the return. The full-profile walk is
representative, not exhaustive; the fixtures of Stages 8 to 21 are not walked through the interview. **Guarantees:** the fixtures are sensitive to the data they
claim to test, the stated invariants hold, and the interview has no dead end on the paths walked.
**Does not guarantee:** anything a mutation cannot express or a fixture already encodes wrongly
(BUG-0001 again), or that a question's wording asks what the source asks.

## 11. The bug inventory and the commit guard

`BUG_INVENTORY.md` records every defect caught by any check or reading, before or with its fix: how it
was caught, the symptom, the root cause, why the existing checks missed it, the fix and its commit. It
is append-only; `check-all` fails if the committed prefix changes or the ids are not sequential.
`tools/hooks/pre-commit` refuses any commit whose tree is not a tree a green check-all run tested (in
the working tree, or on a snapshot in a separate worktree), `tools/hooks/pre-push` refuses a push whose
commits' trees no green run tested (git runs no pre-commit hook on a merge), and a run is green only if
nothing outside its own outputs changed while it ran (`tools/README.md`, "Commit guard").
**Guarantees:** a change to the committed defect record fails the suite, and in a clone with the hooks
enabled (`git config core.hooksPath tools/hooks`) no commit lands, and nothing is pushed, unless the
whole suite passed on that exact tree. **Does not guarantee:** that the suite catches
what it does not test for (the "why it survived" field exists to turn each such miss into a new check),
or anything in a clone without the hook, or a commit made with `--no-verify`.

## 12. Source-coverage checks and standing reviews

A root-cause analysis of the recorded bugs (`docs/2026-10-29_bug_root_cause_analysis.md`, tested in
`docs/2026-10-30_mitigation_strategy_pressure_test.md`) found that wrong amounts came mostly from the
gap between the source text and the encoding, which the evaluator, mutation and engine checks cannot
see. Six checks in `check-all` look at that gap directly: every printed line cites the instruction page
with its "Line N" section; printed arithmetic ("Add lines 1 through 3") matches the line's operands;
rate products of amounts that can go negative are floored or ruled; an input read under another page's
rule carries a verdict that the definitions agree; limit sentences ("can't be more than", "per calendar
year") are tied to the line that enforces them; and quotes outside computed lines are verified. Two
model reviews are held to the same standard, though `check-all` runs no model: it checks offline that
each review is current and every finding ruled (`tools/transcription/check_screens.py`,
`check_completeness.py`). Every scope screen has been reviewed against the lines it gates, with all
findings ruled. The completeness review, which reads a form's instruction sections for operative rules
nothing encodes, asks or refuses, has covered 3 forms (dependent, household, Form 2441); the rest are
recorded in its baseline as never reviewed (`reports/2025/completeness.md`). A review goes stale when
its prompt changes. Findings that existed when a check was introduced are recorded in a baseline that
comes due when the line, question or sentence it concerns changes (`TASKS.md` T-094). **Guarantees:**
new gaps of the six checked kinds are caught when they are written, and recorded reviews cannot
silently go stale. **Does not guarantee:** that a question's wording or a rule's reading is right; those are
still judged by review and adjudication.

## What this does not establish

From `spec/spec.md` section 3, item 11: *human source-reading coverage is limited to the per-line
evidence records; independent constructions and their recorded disagreements provide the broader
verification.* The evidence report identifies qualifying outside-family assertions and the source of
each. Unfinished verification is reported as a gap; adopting a requirement does not establish its
completion. Online tax commentary is recorded as non-authoritative corroboration under
`research/secondary/`; it earns no scoreboard credit and stays out of the blind source-only reviews.

The IRS forms and instructions are not the law. They embed judgments about the Internal Revenue Code
that are not announced, and this project encodes the published procedure, judgments included; where the
text is ambiguous or silent, the reading chosen is recorded in `ambiguities/<year>.yaml` and shown to
the user when the entry is linked to a line that affects their return (79 of the 91 entries for 2025
are linked that way; the rest are cited only in locator text or not yet referenced). No lawyer has reviewed the legal position the project operates
under (`spec/spec.md` section 9).
