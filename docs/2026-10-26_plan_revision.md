# Plan revision — owner amendment, 2026-10-26

This amendment re-sequences the remaining integrity work in `2026-10-22_integrity_plan.md` (as
amended by `2026-10-24_validation_policy.md`) and fixes the gate for resuming coverage. It does not
change the evidence definitions, the scoreboard rule, the noise floor, the provenance rules or any
owner verdict or ambiguity decision. Where it conflicts with the execution order in
`HANDOFF-NEXT-SESSION.md` or `HANDOFF-INTEGRITY.md`, this document controls.

The owner approved each item below in the session that wrote it. TY2026 is the project's target
year: the first return the tool is meant to prepare.

## Why the sequence changed

Between 2026-10-24 and 2026-10-26 nearly all work went to item 1.3 (source transcription under two
model families) and the tooling that checks it. Of BUG-0129 to BUG-0146, one entry (BUG-0138) changes
a tax value; the rest are defects in review tooling. The scoreboard stayed at 209 of 1,515 computed
lines. Each checker change made recorded reviews stale, which required fresh requests, which exposed
the next checker gap. Meanwhile the items that add outside-family assertions (1.4b UsTaxes, 1.2 blind
whole returns) and the item that tests next year's adoption (2.1) had not started, and 622 source
disagreements (Claude 207, deepseek-flash 415) awaited rulings by visual comparison of expression trees.

## A. Close the open source-review batch by execution

Every open transcription disagreement is triaged by evaluating the project's line and the model's
validated candidate on the same inputs: generated returns (`engine/src/generate.ts`), the existing
fixtures, and partial-input variants that withhold conditionally asked answers.

- **Same value on every input run:** ruled *representation*. The ruling cites the triage record
  (input bank, its hash, the number of inputs, the branches reached) and says the equivalence is
  observed on that sample, not proved.
- **Different values:** the triage yields a witness input with both values. The ruling decides
  which side the archived IRS text supports and quotes the deciding sentence (the existing regime).
  A project error is a *finding* with a BUG entry, fix and source-backed regression. Doubtful
  readings may use online interpretation recorded under `research/secondary/` as soft evidence
  (validation policy); it never substitutes for the primary citation.
- **Candidate unusable** (fails schema, types or reference checks, or cannot be evaluated): ruled
  *model error* on the validation failure. A fresh fixed-prompt request is made only when that leaves
  a source-defined target with no usable review.
- Existing ambiguity-register choices and owner rulings are preserved; a difference that is the
  recorded alternative of an ambiguity is ruled *ambiguity* with the register id, not model error.

Raw replies are never repaired. Each form gets an adjudication summary beside its logs listing every
ruling, its class and its evidence. Then the full suite, then one commit.

## B. Freeze the review tooling

Review policy versions stay as they are (`project-expression-types-v3`,
`required-review-interfaces-v2`). A new checker version or review-policy change requires a concrete
case where the current tooling yields a wrong tax value or a wrong ruling. BUG-0129's hold on
transcription qualification (T-062) lifts when A is committed and the read-only audit shows every
ruled row bound to its current request, reply and context.

Owner's decision, 2026-10-27: after the commit of A the audit showed every log ruled under the current
comparison bound and unchanged, while 21 older Claude logs predate it (130 of their agreements change
when re-compared). The global hold is therefore replaced by per-form conditions already in
`compare_families.py`: a transcription pair qualifies only when both logs use the unit-preserving
comparison, pass current type validation and complete input context, and their bound requests verify
live. The older logs stay pending and are migrated when their forms next change.

DeepSeek review pairs on forms that have not changed stay pending; they are refreshed when their
form changes, not re-swept.

## C. Parallel work after A

Each item lands as its own commit behind a green check-all. Agents run on Opus in separate worktrees;
deepseek-flash remains the second family.

1. **UsTaxes** as the fourth engine (1.4b), under the plan's adapter and counting rules.
2. **Blind whole returns** worked by deepseek-flash (1.2), including the previously selected blind
   cases.
3. **TY2026 rehearsal** (2.1) on the posted drafts. Drafts are archived as drafts and 2026 is not
   added to `years.json` until final documents exist.
4. **Citation locators** (0.2): rewrite the 301 segments listed in `reports/2025/citations.md`, then
   put `--strict` into check-all.
5. **Mutation equivalences** (1.6): a second reader over the remaining prose-only arguments;
   mechanize recurring shapes.
6. **OpenTaxSolver tolerance**: replace `OTS_SUBCENT` with a derived per-line bound or remove it
   (spec 6.2 forbids tolerance by margin).

## D. Gate for resuming coverage

Coverage extension resumes, targeting TY2026, when all of the following hold:

- A and B are committed;
- the TY2026 rehearsal (2.1) has run and its tool-defect list is worked;
- every confirmed defect has its investigation closed under the revised stop rule;
- the UsTaxes adapter has landed.

The remaining items continue alongside coverage work rather than ahead of it: 1.2 and the other
items in C not yet finished, 1.5/T-066 (class M on printed lines), 2.2 ("complete" in the spec),
2.3 (prevalence buckets), 2.4 if still open, and 2.5 (product surface).
