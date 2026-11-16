# Lane mfs-l4: married filing separately, dependents (dependent.yaml)

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.
Worktree: `.claude/worktrees/mfs-l4`, base `825024d8` (refs/scratch/x1-base). No paid reviews; no model calls; no
commit; check-all not run (brief); mutate not run (brief: runs at integration).

(Draft written as the lane works; final sections filled at the end.)

## Predictions (written before evaluating)

Common: married filing separately, W-2 $60,000; the filer's 4-year-old child (relationship `child`), lived with the
filer all year, also lived with the husband or wife (`other_claimant` Yes).

| Case | Answers | Predicted |
|---|---|---|
| mfsl4.spouse_not_claiming | only_spouse Yes, spouse_claims No, filer_parent Yes | spouse_settles true; qc_tiebreak false; eic_tiebreak false; qualifying_child true; ctc_child true; ctc_amount $2,200; eic_child true; s8812 line 4 = 1 (p501 p. 17 Example 6) |
| mfsl4.spouse_claims | only_spouse Yes, spouse_claims Yes | refused at qc_tiebreak (ctc_amount, claimed); eic_child refused at eic_tiebreak (p501 p. 15 "both parents claim") |
| mfsl4.not_parent | only_spouse Yes, claims No, filer_parent No | refused at qc_tiebreak; eic_child refused at eic_tiebreak (i1040gi p. 21 higher-AGI rule for a non-parent) |
| mfsl4.other_relative_too | only_spouse No | refused at qc_tiebreak |
| mfsl4.settled_not_qc_spouse_taxpayer | months 5; settled; spouse a taxpayer | tiebreak_settled true; claimed refused at qc_tiebreak (Step 4: QC of any taxpayer) |
| mfsl4.settled_not_qc_spouse_nontaxpayer | months 5; settled; spouse not a taxpayer | tiebreak_settled false; qc_tiebreak false; qualifying_child false |

All six cases evaluated as predicted on the first run (`test-fixtures`: `ok` for each); nothing was edited after
evaluating.

## 1. What the merge must know

- `fixtures/2025/defaults.json` in this tree is the copy of `.claude/worktrees/nx-b1/fixtures/2025/defaults.json` (base
  caution of the brief) plus this lane's three defaults. Merge only the three: `/tmp/mfs-l4/defaults_patch.py <path>`
  (idempotent; inserts `dependent.filer_parent` (true), `dependent.other_only_spouse` (false), `dependent.spouse_claims`
  (false) beside the dependent entries, moves nothing).
- `interview/2025/questions.yaml`: three new entries (order 120, seq 17, 18, 19, after the `dependent_facts` group,
  seq 13 to 16), and **the order-120 entries with seq 17 to 36 renumbered 20 to 39** (`dependent.other_nontaxpayer`
  through `dependent.absence_no_return`; same relative order). Help reworded: `dependent.other_claimant` (one sentence
  added, "On a separate return, your husband or wife counts."), `dependent.us_half` (military sentence).
- `reviews/2025/consumers.json`: two rulings added (`consumer:f1040.status@i1040gi:p17`,
  `consumer:dependent.relationship@p501:p15`).
- `ambiguities/2025.yaml`: `amb.2025.mfs_spouse_qc` appended (the id the scout proposed; L1 does not write it).
- `interview/2025/coverage/dependents.yaml`: two sets (`mfs_one_listed`, `spouse_lives_with_child`) and five rows.
  The four MFS rows fail in this tree only because the base still refuses MFS at `s3.mfs`; with `s3.mfs` lifted
  (a temporary local edit, reverted, and the New York profile set aside for that build) all five rows passed. The set
  answer `household.married_dec31: true` is asked only once L1's tightened `household.filing_status_conflict` lands;
  in this tree it is reported as a stale set answer. Re-run these rows after L1 merges.
- No line id other lanes read was changed. `dependent.qc_tiebreak` and `dependent.eic_tiebreak` keep their ids,
  refusal entries and wording; only their chains changed.

## 2. What changed (forms/2025/dependent.yaml)

New lines (all after `dependent.qc_tiebreak_other_age`):

| id | printed | what |
|---|---|---|
| `dependent.other_only_spouse` | (helper), input, gated | "Is your husband or wife the only relative, besides you, who lived with this child for more than half of 2025 and could claim them?" |
| `dependent.other_only_spouse_if_mfs` | (gate) | choose over the five statuses: mfs → the input; else false |
| `dependent.spouse_claims` | (helper), input, gated | "Will your husband or wife claim this child on their own 2025 return?" |
| `dependent.spouse_claims_if_only_spouse` | (gate) | asked only after Yes to the previous |
| `dependent.filer_parent` | (helper), input, gated | "Are you this child's parent by birth or by adoption?" |
| `dependent.filer_parent_if_child` | (gate) | relationship `child` → the input; any other relationship → false |
| `dependent.spouse_settles` | (helper) | MFS ∧ spouse only other ∧ spouse not claiming ∧ filer a parent |
| `dependent.spouse_settles_unclaimed` | (helper) | chain step of the above |
| `dependent.tiebreak_unsettled` | (gate) | settled → `tiebreak_settled`; else `tiebreak_spouse_or_other` |
| `dependent.tiebreak_settled` | (gate) | not the filer's QC ∧ the other person is a taxpayer (Step 4 keeps refusing a QC of a taxpayer as a qualifying relative) |
| `dependent.tiebreak_spouse_or_other` | (gate) | spouse will claim → true (refusal told at that answer); else the old `dependent.tiebreak_other` |
| `dependent.eic_tiebreak_unsettled` | (gate) | settled → false; else the old `dependent.eic_child_tests` |

Changed: `dependent.qc_tiebreak_claimant` (Yes branch → `dependent.tiebreak_unsettled`), `dependent.eic_tiebreak` (Yes
branch → `dependent.eic_tiebreak_unsettled`), `dependent.us_half` (source and cite: BUG-0729).
On every status but MFS the new chain reduces to the old one and asks nothing new (fixtures unchanged; row
`dependents.single_no_spouse_questions`).

BUG-0729 (fixed here, small): `dependent.us_half` source now reads "If you (or, on a joint return, your
spouse) were on extended active military duty outside the United States (duty ordered for an indefinite period or for
more than 90 days), ..." with the i1040gi p. 44 definition quoted in the cite; the bank help says the same in the
F9 wording. The pending file is lane g1-f9's; the coordinator records the fix.

## 3. Decisions

- D3 settled as the scout recommends (DECISIONS.md section added; `amb.2025.mfs_spouse_qc`). Alternative rejected:
  keep every such child refused.
- Added beyond the scout: `dependent.filer_parent`. The scout's design let any filer claim when the spouse does not;
  i1040gi p. 21 lets a non-parent (stepparent, foster parent, grandparent) claim only with an AGI higher than the
  parent's, which the tool does not ask, so a No falls back to the old test (refused when the child is the filer's QC).
- Added beyond the scout: `dependent.tiebreak_settled`. Without it, a child who is the spouse's QC but not the
  filer's would lose the Step 4 refusal (QC of a taxpayer cannot be a qualifying relative).
- Over-refusal accepted and recorded in the ambiguity entry: when the spouse also claims, the filer is refused even
  if the spouse is only a stepparent (the filer, the only parent, would win).
- Extension not made: a married head-of-household filer ("considered unmarried") whose spouse is the other claimant
  is still refused (status hoh; the questions are asked only on MFS). Same rule would apply; scope kept to MFS.

## 4. Gates replaced and residual refusals

No gate removed or added. `dependent.qc_tiebreak` / `dependent.eic_tiebreak` narrowed on MFS: computed when the
husband or wife is the only other claimant, will not claim, and the filer is a parent. Still refused (same gates):
spouse also claims; another relative could also claim; filer not a parent by birth or adoption; all non-MFS cases as
before. `tree.json`, `categories.json`: no change.

## 5. Next year (2026)

No operations. The new lines carry by the 2025-plus-operations mechanism. Documents: i1040gi 2026 and Pub 501 2026 are
not archived (awaited); no 2026 difference to write. No existing 2026 operation names a line this lane changed
(grep of `changes/2026/`). `year_changes.py --check`: rc 0. `year_shared_refs.py --year 2026`: 0 references.

## 6. Defects

None new. BUG-0729 fixed (section 2).

## 7. For other lanes and requests

- L1: the rows need `household.married_dec31` asked on MFS (your conflict gate). The `dependent.other_claimant` tick
  label ("Lived over half of 2025 with another relative who could claim them", 12 words, at the limit) cannot carry
  "your husband or wife counts"; only the help does. An MFS parent may pass over the box (who could answer No wrongly:
  the MFS parent living with the other parent). Worth the question review and the owner's walk.
- L5: fixtures M7 and M11 (scout §5) depend on D3: M7's child must answer `other_claimant` false (spouse lived with
  the child under half the year), M11's child `other_claimant` true, `other_only_spouse` true, `spouse_claims` false,
  `filer_parent` true. `engine/src/generate.ts` `Dependent` and `tools/engines/generate_cases.py` know nothing of the
  three new inputs (defaults apply).
- Mutation (not run, per brief): expect operand mutants on the six new chooses. Killed by the six cases, I predict
  [not run]: `tiebreak_unsettled` both arms (spouse_not_claiming / spouse_claims), `tiebreak_settled` both arms
  (the two settled_not_qc cases), `spouse_settles_unclaimed` (not_parent), `other_only_spouse_if_mfs` mfs arm
  (other_relative_too vs spouse_not_claiming), `eic_tiebreak_unsettled` (spouse_not_claiming eic_child true vs
  spouse_claims refusal). Non-mfs arms of `other_only_spouse_if_mfs` that all go to `dependent.no` and the seven
  non-child arms of `filer_parent_if_child` will survive a swap to another `no` arm only as equivalent.

## 8. Verification (this tree; base x1-base is broken as the brief says)

| Command | Result |
|---|---|
| `build` (after copying nx-b1 defaults) | OK (`npm run compile` fails on the base's mutate-worker.ts; dist used) |
| `render`, `render --ny` | OK |
| `test-fixtures` | 1399/2017; all 618 failures are base: 598 `s2.amt_owed` not declared, 74 `sd.qof` unanswered, 1 `s2.mortgage_subsidy`, 1 `sb.partIII`; none names a dependent line. All dependent.json cases and the six new cases ok |
| `test-fixtures --ny` | 142/357; failures base (`s2.amt_owed` 214, `sd.qof`) |
| `interview-coverage --rows dependents.yaml` | 18 old rows and `single_no_spouse_questions` pass; 4 MFS rows refused at base `s3.mfs` (pass with it lifted, see §1) |
| `tick-groups` | passed |
| `interview-rules` | not completed: one run timed out at 25 min on the loaded machine, the second was stopped on the coordinator's deadline instruction; to run at integration |
| `citations.py --strict` | 0 findings |
| `check_consumers.py` | my 2 new pairs ruled; remaining 38 new / 6 stale are base (not dependent-lane, except `dependent.edu_over@i8863:p9`, whose subject is its question, unchanged here) |
| `check_questions.py`, `check_screens.py`, `check_false_no.py` | rc 0 (due-at-release lists include the new inputs and gate) |
| `siblings.py --check`, `check_bug_inventory.py` | rc 1, findings all base pending entries (none this lane's) |
| `check_twins.py` | 0 problems |
| `year_changes.py --check`, `year_shared_refs.py --year 2026` | rc 0 |
| `mutate`, `check_all.sh` | not run (brief) |

## 9. Review debt (round 2)

- `dependent`: transcription (line-scoped: the 12 new lines, `qc_tiebreak_claimant`, `eic_tiebreak`, `us_half`),
  render (same lines), class M (dependent).
- Question review: `dependent.other_only_spouse`, `dependent.spouse_claims`, `dependent.filer_parent` (never
  reviewed), `dependent.other_claimant`, `dependent.us_half` (changed).
- Screen and false-no: `gate:dependent.other_only_spouse_if_mfs` (listed due), and the refusal reached through
  `dependent.spouse_claims` (Yes refuses) under the per-release sample.
- Dry-run estimate not run (no paid tooling run in the lane).

## 10. Walks

Not recorded (coordinator deadline; and the MFS personas (14 to 16) are L1's, and an MFS walk stops at the base `s3.mfs` refusal in this tree).

## 11. Left open, in rank order

1. Rerun the five rows after L1 merges; confirm `household.married_dec31` is asked.
2. Tick label of `dependent.other_claimant` for MFS (question review / owner).
3. Married HOH with the spouse as other claimant (same rule; not extended).
4. Spouse-claims refusal when the spouse is only a stepparent (over-refusal, recorded).

Estimated coverage gain: unmeasured here [I]: MFS parents whose child also lives with the spouse — the scout's
section 0 item 9 says "most MFS parents who live together" would refuse without D3; this lane makes them computable
when the spouse does not claim. Part of the scout's +1.3 to +1.5 points; not separable.
