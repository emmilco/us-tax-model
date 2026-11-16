# Lane M-K1S (k1s, f7203, person.k1s_*): result

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/mk1s` (detached at
6649c637). `mk1s.patch` is empty: no fixture, no keyed argument and no bug draft was written.

## Scope after the skip lists

`reports/2025/mutation.md`, "Surviving — not yet explained", lists 62 k1s / f7203 / person.k1s_* ids. All 62 appear
in `round7/mk1-handled-k1s.txt` (already present when this lane started; no wait was needed):
- 47 killed by M-K1 fixtures (`mk1.k1s.*`),
- 7 argued equivalent in the lane-mk1 block,
- 3 left to the no-observable-reader rule (p1_loss, p2_loss, p3_loss .zero),
- 4 marked OPEN by M-K1, not handled.

Of the 4 OPEN ids, `operand.k1s.k1s.p5_income.zero.then1` has no reader on any value sheet (k1.md line 450), so it is
MSTRUCT's. That left three ids with readers that no lane had resolved. This lane examined them:

| Mutant | Outcome |
| --- | --- |
| operand.k1s.k1s.col_h.zero.then1 | OPEN (owner decision); no valid fixture exists |
| operand.k1s.k1s.col_i.zero.then1 | OPEN (owner decision); no valid fixture exists |
| operand.k1s.k1s.col_k.zero.then1 | OPEN (owner decision); no valid fixture exists |

## Why the three are open

Each mutant changes the `k1s.ok = false` alternative of col_h, col_i or col_k from `k1s.zero` to another line.
`k1s.ok` tests `k1s.f7203_n eq 1`. `k1s.f7203_n` sums `f7203.one`, the parameter `ss.one` (1), over the f7203
roster. f7203 is an implicit collection (`collection: {parent: k1s, implicit: form}`). With no roster given it is
exactly `[form]` (`eval.ts` `rosterOf`). `build.ts` makes it a build error for any interview to ask `$f7203`.
- Inspected: the source lines above; `params/2025.yaml` `ss.one` = 1; every fixture that lists the roster lists
  `["form"]` (17 occurrences, none other).
- Inferred: on any input the interview can produce, `k1s.f7203_n` is 1, a refusal or unknown, so `k1s.ok` is never a
  known false and the mutated alternative is never taken.

Probe (`round7/mk1s-work/probe.mjs`, output `probe.out`; nice -n 10, no full mutate). It compared col_h, col_i, col_k
and ok, data against mutant, over the 28 fixture cases that list a K-1 (S corporation) entry:
- as given: no difference for any of the three;
- answers withheld (mutate.ts `withholdAnswers`, rates 0.1 / 0.25 / 0.5, 6 seeds each): no difference;
- f7203 roster `[]`: col_i differs (classm.k1s.1, $0 vs $80,000);
- f7203 roster `[form, w9]`: all three differ (col_k classm.k1s.3; col_i classm.k1s.1; col_h classm.k1s.5).

This agrees with the witness worklist: W6 and W30 were both produced by copying the f7203 entry as `w9`.

### Consequences
- **No fixture.** The only witnesses use a roster the interview cannot produce, so under the brief's rule they are
  not valid fixtures.
- **No keyed argument written.** An argument for every input would be false, because an explicit `$f7203` roster is
  an evaluator input on which the mutants differ.
- **The answered-only list (`ANSWERED_ONLY`) does not fit either.** That list covers differences that come from
  withheld answers. Here the difference comes from a roster the interview never asks, which is a different domain
  restriction from withholding answers.
- **A possible further difference, not shown.** With `k1s.ok` unknown, both alternatives become ways (spec 4.7.3).
  The mutant's way could refuse where `k1s.zero` cannot, which would make the mutant a refusal where the data gives
  an unknown. The sample above found no such case, which does not show none exists.

### Owner decision needed (one of)
1. Treat inputs that list an implicit collection's roster other than its one implicit key as outside the input
   domain. That would need a structural rule, or a third "producible inputs" category in mutate.ts, after which a
   keyed argument holds.
2. Remove the dead `ok = false → zero` alternatives, or the `f7203_n eq 1` test itself. This is a form change. Note
   that i7203 p. 2, Item C allows more than one Form 7203 for a partial stock sale or redemption. The model sends
   that case to the `k1s.disposed` refusal, so the count test protects nothing the refusal does not already cover.
3. Leave them unexplained.

## Verified vs inferred
- Verified: the set difference (62 ids, all in M-K1's list); the probe results above; the f7203 roster cardinality
  facts from source and fixtures.
- Inferred, not verified: that no partial (withheld-answer) return tells the mutants apart. The 54 withheld variants
  per case are a sample, not a proof.
- Not done: Phase 3 fixtures and Phase 4 kill verification. No id in this family was left for this lane that a valid
  fixture could kill.
