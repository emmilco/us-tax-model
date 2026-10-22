# Project evaluation — 2026-10-22

An outside-eye evaluation of the project's organization, the degree to which it meets its stated goals, and the flaws worth treating as serious. Written by Claude Fable 5.1 in a session with the owner, from a read of the repository at commit 3748f74 with the working tree in progress. It is an assessment, not a measurement: see the provenance section at the end for what was and was not inspected.

## Summary

The project is unusually well organized and most of its evidentiary promises are kept. Its trust claim rests on one model family reading the same text, its own evidence accounting has drifted from the spec, and the tax year it encodes can no longer be filed on time.

## Organization and structure

The layering is clean and the discipline is real. Forms are data, the engine has no form-specific tax logic, the build fails on a missing citation, and every check runs from one command behind a commit guard that refuses any tree the suite has not passed. The append-only bug inventory, the task list, the ambiguity register, and the per-stage premise maps with adversarial verifications are better records than most funded projects keep. The last commit matches the green marker, so HEAD passed the full suite.

The weak spots are housekeeping, not architecture:

- **No README, no LICENSE file, no git remote.** The spec calls the project open and Apache-2.0/CC0. At the time of writing it is a single copy on one disk with ten days of work and no stated licence.
- **Twelve handoff files at the root.** Only the newest is current. The rest belong in a `handoffs/` directory.
- **The interview README is stale.** It still describes the Stage 2 interview, sixteen stages later.
- **The reports directory mixes kinds.** Generated reports, hand-written review packets, and raw values-sheet dumps sit side by side.
- **Design and spec disagree in small ways.** The design still lists a Lean checker with a soundness proof that the spec says was not pursued, and the design says whole-dollar rounding is the default while the output says it is deferred.

## Fulfilment of the stated goals

Against the eleven evidentiary requirements in spec section 3, nine are met as written: provenance on every line, rendered English beside the IRS text, a closed atom vocabulary with zero opaque escapes, proved atom lemmas, structural checks, a visible ambiguity register, revision pinning, integer cents, and one offline command. Two are not met as written, and they are the two that carry the trust statement.

**Requirement 6, evidence labelling, has drifted.** The per-line evidence report (`reports/2025/evidence.md`) has columns for classes A, B, C and R only. Class M, the 169 model hand-worked fixtures, does not appear in it at all. Class C is redefined in the report's own header as agreement with the Lean evaluator, which reads the same data, rather than agreement with an outside engine as spec 6.1 defines it. One Stage 1 fixture (`qdcg.handworked.single`) is labelled B, human hand-work, while its note says it was worked by the agent; spec 6.1 says model work is never labelled B.

| Evidence report (2025) | Count |
| --- | --- |
| Line rows | 2,365 |
| Rows with no evidence of any class | 996 |
| Computed lines unasserted | 626 |

**Requirement 11, independent construction, is overstated.** The constructions share no artifact, as promised. They do share a reader. Authoring, the second transcription, the render comparison, class M hand-work, and the blind fixture predictions are all Claude models (the review tools default to claude-opus-5-5). Spec 6.5 names the shared-English blind spot but not the shared-reader one. The one outside check, the engine differential, compares about eighteen summary lines against PolicyEngine-US and Tax-Calculator, each with several excluded lines. Nothing outside the model family has read Schedule C, Form 4562, Form 5695, Form 2441, or Form 8889, and those are where the recent stages live.

**The coverage goal is advancing on schedule.** The estimate reads 68.6 percent toward the 80 percent first goal. The report itself notes that 148 of 157 refusal gates are unmeasured, so the true figure is lower.

**The product goal is the least advanced.** The client is a JSON command-line interview. Only 21 questions have authored wording; the rest show the filer the IRS line label as the prompt, and the scope screens are long legal sentences. The sample walk in `reports/2025/interview-exercise.txt` took 83 steps for a wages-plus-investments return. The values sheet opens with fifteen helper lines of zero dollars from Form 1099-DIV before anything a filer recognizes. The explanation model of spec section 8 exists in the data but not yet in anything a person would use.

## Flaws worth treating as serious

None of these breaks the architecture. Each undercuts the claim the project makes about itself, and two are cheap to fix.

1. **The fixture suite mostly pins the evaluator to itself.** Of roughly 1,034 fixture cases, all but about 180 are labelled synthetic regression, meaning their expected values were recorded from the project's own evaluator. The mutation score measures whether those recordings are sensitive to change, not whether they are right. The actual independent evidence is the class M values, the Stage 15 and 16 blind predictions, about ten official examples, the engine differential on its eighteen lines, and the 448 ruled review disagreements (348 transcription, 100 render). That is a respectable base, but the handoffs present fixture counts and mutation scores beside it as if they were the same kind of evidence.

2. **Equivalence classification is an unproved escape hatch.** Of 149 surviving mutants, 129 are marked equivalent by prose arguments paired with structural predicates in `engine/src/mutate.ts`, and the working tree adds 171 more lines of them. Each argument is written by an agent and checked by no one else. This is where a wrong encoding would most easily be explained away rather than caught.

3. **The encoded year can no longer be filed on time.** The TY2025 extended deadline passed on 2026-10-15. The first real use is TY2026, whose final Form 1040 instructions will likely arrive in February 2027 if the 2025 pattern holds (i1040gi printed 2026-02-25), leaving about six weeks to adopt them. The year-adoption tooling (T-045) has been validated only on 2024 to 2025 and on a fabricated 2026. Meanwhile the roadmap keeps adding TY2025 scope that will all need re-deriving. The strategic question is whether to pause coverage growth and rehearse adoption on the TY2026 drafts as they appear.

4. **The legal position is unreviewed.** `research/04_legal_liability.md` concludes that free, local, non-transmitting software is probably outside the preparer and section 7216 definitions, and says plainly that no lawyer has read it. For the owner's own return this is fine. Publishing it as a tool for most of the filing population is a different act and should wait for that review.

5. **Vouchability.** The project's own trust statement says no human has read the encoding. The owner's contact with it is 25-question decision batches per stage. The honest position is that the owner vouches for the checking regime, not the encoding. That is defensible only if the regime's independence is real, which returns to the shared-reader problem. The cheapest remedies are to run the transcription, render and class M tools under a second model family (they already take a model flag), and to have a human read the dozen highest-stakes lines end to end.

## Provenance

**Inspected:** the root listing, `PROJECT_INDEX.md`, `spec/spec.md` and `spec/design.md` in full, `HANDOFF.md` and `HANDOFF-STAGE-16.md`, `TASKS.md`, the bug inventory header and tags, the coverage, mutation, properties, engine-differential and evidence reports, sample YAML (`qdcg`), its rendering and render review log, a values sheet, the Lean theorem files, the model-calling code in `tools/transcription/`, the fixture evidence labels by file, the commit-guard marker against HEAD, the source manifest, and git history sizes.

**Inferred (unverified):** that the full suite still passes on the dirty working tree (21 modified files, another session editing); that the TY2026 instruction timing will match 2025; and that the model flag on the review tools works with a non-Claude model. No check was run, no form's YAML was read against its IRS pages, and the legal research's sources were not read.
