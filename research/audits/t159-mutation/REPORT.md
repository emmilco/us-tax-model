# T-159 mutation coverage: report

Branch `claude/t159-mutation`, from `main` at 5eec22f.

## Outcome

- **Tier 1 (`table_lookup` key and status) is complete and ungated.** It is now part of the shipped score.
- **Tiers 2 (choose branch values) and 3 (test operands) stay gated behind `MUTATE_TIER`**, because tier 2
  still has 114 unexplained survivors. Tier 3 was counted but not evaluated.
- **The final mutation line on this tree:**
  `mutation: 2794 mutants, killed by checker 296, by fixtures 2371, surviving 127 (127 equivalent; score 95.5%, adjusted 100.0%)`.
  The step exits 0. The report is `reports/2025/mutation.md`.
- **No tax defects were found** (see `PROPOSED_BUGS.md`).

| Tier | New mutants | Killed (existing) | Killed by new fixtures | Equivalent | Unexplained |
| --- | --- | --- | --- | --- | --- |
| baseline (main) | 2,786 | 2,663 | — | 123 | 0 |
| 1: table_lookup key/status | 8 | 1 | 3 | 4 | **0** |
| 2: choose `then` (gated) | 775 | 516 (495 fixtures, 21 checker) | 45 | 100 | **114** |
| 3: test operands (gated) | 1,429 | not measured | — | — | not measured |

Totals by tier setting: tier 0 (shipped) has 2,794 mutants, tier 2 has 3,569 and tier 3 has 4,998. These
counts match the task row's measurements of 2,794 and 3,569. The earlier 4,981 for tier 3 came from a
different site walk.

The surviving counts also match what the task measured on `main`. Tier 1 left 7 survivors before any
work. Tier 2 left 259 new survivors, against 392 − 130 = 262 in the measurement. The difference is the
three tier-1 mutants that the new fixtures kill.

## Code changes (`engine/src/mutate.ts`, `engine/src/fixtures.ts`)

- **New operand sites in `collectOperandSites`:**
  - `table_lookup`/`bracket_schedule` key and status (tier 0 now).
  - Each choose alternative's `then` (tier 2).
  - String operands inside `test` expressions, both `test` lines and choose guards, recursing through
    `all`/`any`/`not` (tier 3).
- **Tier gate.** It reads `MUTATE_TIER` (default 0). The candidate-exclusion set is computed from all
  tiers, so a tier's mutants do not change when a higher tier is switched on.
- **Mutant ids.** Test-operand ids carry the operand path, so they are unique.
- **Corrected comment.** The comment above `OperandSite` was wrong. It now says that `keyed_lookup` keys and
  `rate_lookup` key and status are already sites.
- **Fixture loader.** `loadCases` now reads `fixtures/2025/mutation.json`. `test-fixtures` runs all 34 cases
  in it (1,471/1,471 passed).
- **Failure behaviour is unchanged.** The step still fails on any unexplained survivor, and no check was
  weakened.

## Equivalence rules added

Each rule is re-checked against the data on every run.

1. **`line1KeyInTable`.** This is a conditional (`EQUIVALENT_IF`) entry for
   `operand.eic.eic.line1_table{0..3}.line1.key`, the 4 tier-1 survivors where line 1 is replaced by
   `earned_for_limit`.
   - The lookups are helpers. `eic.line1_table` is their only reader, and `eic.line2` reads it only in the
     alternative where `eic.line1 >= eic.table_start` (100 cents).
   - Line 1 and `earned_for_limit` choose on the same `self_employed` test. Where they differ
     (`wsb_6 = max(0, wsb_4b)` against `wsb_4b`), they differ only when line 4b is negative. Line 1 is then
     $0 and the lookup is not read.
   - The rule's `holds` checks every one of these structural facts.
   - The task row recorded this pair as a fixture gap. I re-measured instead of relying on that, and found
     that no input can make a printed line differ. A paid second reading agrees (`claude -p` with
     `--setting-sources "" --tools ""`): `receipts/eic-line1-key.prompt.txt` and `.response.txt`, verdict
     EQUIVALENT.
2. **`settledBranch` (structural).** It applies to a choose alternative whose value X is replaced by Y.
   - From the alternative's guard, which is known true, it derives facts. The guard's earlier alternatives
     are false and the lines it compares are complete. The facts are exact values, intervals and excluded
     values, and they extend through ungated flag lines (`eq(F, v)` adds what F's own test, true or false,
     establishes).
   - It counts a fact only through a comparison whose result implies completeness. The evaluator's
     lower-bound rule can make `gt`/`ge`/`ne` true, or `lt`/`le`/`eq` false, on an unknown count, so those
     cases are excluded.
   - It then reduces X and Y under those facts. Chooses that the facts settle become their taken branch, and
     copies are followed. These reduce to zero: a zero parameter, a non-negative line bounded at 0, and sums,
     subtractions, rounds and min/max of zeros. A rate or count applied to a zero amount also reduces to
     zero, provided the rate or count is a parameter.
   - Lines whose refusal gates are all among the mutated line's own non-`when_known` gates count as ungated,
     because those gates were already evaluated false.
   - All-tests and any-tests are settled only at a deciding conjunct after earlier conjuncts are all
     settled, which matches spec 4.7.2.
   - The mutant is equivalent if both reduce to the same form.
   - Spot-checked by hand: `sd.to1040` with `has_loss` gives `line21 = limited_loss`; when Form 8606 is not
     filed, nondeductible contributions are ≤ 0 and therefore $0; the Schedule 1-A part-skip chains; the
     settled siblings in `f1095a.*`.
   - It accepts 94 tier-2 survivors.
3. **`unreachableAlternative` (structural).** It applies when the mutated line is a helper and every printed
   reader path passes choices whose guards make an ungated test line F true. This reuses the existing
   `dominatedBy` path-dominance check. F true must settle the replaced alternative's guard false.
   - Example: the married-filing-separately alternatives of Schedule 1-A Part II, III and V helpers. Those
     parts require the status to be other than MFS.
   - Example: `f8889` December-coverage `none` alternatives that are read only under `use_last_month`, which
     requires December coverage other than none.
   - It accepts 6 tier-2 survivors.

## Fixtures added (`fixtures/2025/mutation.json`, 34 cases)

All expectations were predicted by hand from the archived sources before the evaluator was run on the case.
The prediction and its source quote are in each case's `evidence_note`. Every prediction agreed with the
evaluator on the first run.

- **Tier 1, EIC Worksheet A line 5 key (3 cases).** These are 0, 2 and 3 qualifying children with AGI above
  earned income, inside the phase-out. The values come from the EIC Table rows (i1040gi pp. 51–53):
  - 0 children: $542 at $12,000 and $465 at $13,000.
  - 2 children: $6,799 at $25,000 and $5,746 at $30,000.
  - 3 children: $7,693 at $25,000 and $6,640 at $30,000.

  I cross-checked each against the statutory phase-out formula.
- **Tier 2, skipped or copied printed lines (18 cases).** These reuse corpus inputs and expect lines that
  the mutants change:
  - Schedule 1-A Parts II–V blank when the part does not apply.
  - Schedule D Tax Worksheet lines 23, 25, 35 and 41 blank under the worksheet's skip rules (quoted).
  - Form 8962 monthly columns (a) and (b) copying the Form 1095-A inputs.
  - Form 8863 line 1, Form 8880 line 4(b), IRA worksheet lines 2a/6a/7a and Form 8960 line 9a at $0 when
    they do not apply.
  - Schedule 3 lines 5a and 9 at $0.
  - Student loan interest worksheet line 5: $85,000 for QSS and blank for MFS.
- **Tier 2, filing-status amounts (7 cases).** Schedule 1-A lines 9, 17 and 26 for HOH and QSS ($150,000,
  $150,000 and $100,000), and Part V for HOH and QSS aged 65+ with $100,000 MAGI: line 32 $75,000, line 35
  $4,500 and line 36a $4,500.
- **Tier 2, EIC filing-status limits and thresholds (6 cases):**
  - MFJ with no children at $20,000: $473.
  - MFJ with one child at $52,000: $884.
  - MFJ with two children at $60,000: $928.
  - Line 5 skipped for MFJ below $30,470 (one or more children) and below $17,730 (no children).
  - QSS with one child: $1,743, the 34% phase-in at the $5,125 midpoint.

## How the tier-2 survivors were grouped

Per survivor I recorded the mutated line, the guard, the original and replacement lines, and a corpus
witness. The witness search used the evaluator on the mutant: it found the first fixture case in which any
derived value changes, and listed the changed printed lines. The groups were:

1. **Replacement equals the original under the guard** (sibling chooses on the same or implied flag, and
   zero chains). These were cleared by rules 2 and 3.
2. **The witness changes a printed line that no fixture expects** (skip lines, 1095-A copies, filing-status
   amounts). These were cleared by fixtures.
3. **Remaining (114).** The full list is in `tier2-unexplained.md`. By form:
   - s1a 25, person 16, eic 12, f8889 10, scveh 8, refund 7, ssb 6, f1095a 6, retirement 4, s8812 3.
   - 2 each: sli, sc, sa, ira, f8880, dependent.
   - 1 each: sdtw, sd, s1, f5695, asset.

What I saw in group 3:
- **Witness changes only helper values, or a refusal's identity** (for example `refusal(sb.line8)` →
  `refusal(scope.schedule1)` on `s1a.line13`). A fixture would need a printed expectation on a return
  whose refusal order I did not predict from the source.
- **Status-keyed EIC limits not yet exercised:** MFJ with 3 children, QSS and MFS above the other-status
  limits, and HOH with 3 children between $61,555 and $68,675. At that last point the "other" column is
  already $0, so only `eic.eligible` (a helper) differs.
- **Schedule 1-A `line13_claim`/`line21_claim`/`line36a_claim` status alternatives.** These differ from the
  original only when the SSN condition is false or incomplete. Proving them would need a case split on
  incompleteness, which no rule does yet.
- **Form 1095-A March/October/November/December months, `f8889` part-year charts, Schedule C vehicle
  section 179 and 4th-quarter chains, the `refund` worksheet and Social Security worksheet filing-status
  amounts.** These need new returns or deeper proofs.

None of these is labelled equivalent.

## Checks run

- `npm run compile` and `node engine/dist/main.js build` passed.
- `node engine/dist/main.js test-fixtures`: 1,471/1,471 passed through the command-line program, exit 0.
- `node engine/dist/main.js mutate` with `MUTATE_WORKERS=4`, on the final tree: the line above, exit 0,
  about 71 minutes on 4 cores. With the default worker count this machine would use 1 worker.
- Per-tier survivors were measured with a scratch harness, not the shipped step. The harness evaluates only
  the fixture cases whose baseline derived the mutated line; this is sound because a mutation of line L's
  expression cannot change whether L is evaluated. On the 70 tier-2 mutants that both harnesses ran, it
  agreed with the full harness on every outcome.

## Checks not run

- **The tier-2 and tier-3 counts come from the scratch harness.** The full mutation step was not run with
  `MUTATE_TIER=2` or `3`.
- **Tier 3 survivors were not evaluated.** Only the mutant count (1,429 new) was measured.
- **`check-all` and the Lean comparison** were not run. The local integrator runs the full suite.

## What I inspected and what I inferred

**Inspected:**
- Every rule's acceptance on spot-checked survivors.
- The source rows and quotes behind every fixture.
- The evaluator semantics for choose, all/any and refusal gates (`eval.ts`, spec 4.7.2–4.7.4).

**Inferred:**
- That the 114 remaining survivors are fixture gaps or unproven equivalences rather than defects. Most were
  not examined individually to that depth.
- That the rule acceptances I did not spot-check are correct. This rests on the rules' construction.

## What remains

- **Tier 2.** Clear the 114 survivors in `tier2-unexplained.md`, then ungate it. A rule that splits cases
  on the alternatives of an absorbed choose would cover the Schedule 1-A `*_claim` group. MFJ-3, QSS and MFS
  EIC returns would cover the EIC group.
- **Tier 3.** Measure it and classify its survivors.
- **Defaults.** Consider making the default `MUTATE_WORKERS` usable on 4-core machines. It is currently
  `cores − 6` with a floor of 1.
