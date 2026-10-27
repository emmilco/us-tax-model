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

## E. Coverage route to the first goal (owner amendment, 2026-10-27)

Gate D was met on 2026-10-27 (BUG-0180 closed by BUG-0181, commit 671826a). The owner set the aim of
the resumed coverage work as reaching the first goal of spec 2.4, 80% of returns, with results that can
be shown stage by stage.

The order in item 2.6 (Schedule E, the rest of Schedule 1, the premium tax credit) and in spec 2.4 is
the estimator's greedy order over whole groups. Run over single categories with the same raking and
data (`tools/coverage/estimate.py`, `covered()` with chosen categories removed), the gains if covered
alone from 68.6% are: premium tax credit +4.4, education credits +3.3, rental and royalty +3.2, capital
loss carryover +2.5, other income +2.4, Form 5329 +2.2, married filing separately +2.1, partnership and
S corporation +1.4. The cheapest set that includes Schedule E and reaches 80% is the premium tax credit,
rentals and education credits (80.2%). Four stages without Schedule E reach 82.2%: the premium tax
credit, education credits, the capital loss carryover and Form 5329.

The owner approved that route. Stages run in this order:

1. Stage 20, the capital loss carryover (premise map `research/premises/stage20-capital-loss-carryover.md`).
2. Stage 18, the premium tax credit (Form 8962).
3. Stage 19, the education credits (Form 8863).
4. Stage 21, Form 5329.

Schedule E (Stage 17) and the rest of Schedule 1 follow the first goal. Each stage starts from a
decision batch for the owner, written from its premise map and verification and checked against the
current tree, and closes under the standing regime.

Limits recorded with the decision. The capital loss carryover and Form 5329 are IRS-only categories,
combined as independent of everything else; their gains are the least certain, and without Form 5329
the route reaches 79.6%. The 80% is the estimator's figure for measured situations, and each stage adds
refusal gates it cannot measure. Stages are built on the final TY2025 sources and carried to TY2026 by
year adoption when the final 2026 instructions post; P.L. 119-21 sec. 71305 removes the excess advance
credit repayment limitation for tax years after 2025, so the premium tax credit's year diff will be
substantive.
