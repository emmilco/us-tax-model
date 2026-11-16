# MFS lane L3: credits on a married filing separately return (Forms 2441, 8863, 8962, 8889)

Model: claude-opus-5-5. Class: judgment. Year: 2025 (with the 2026 operations). Jurisdiction: us.
Worktree `.claude/worktrees/mfs-l3`, base `825024d8` (x1-base). No paid reviews and no model calls. Not run, by the
brief: check-all and mutate (mutate runs at integration). Generated files (`rendered/`, `reports/`, `canonical/`) are
not part of the diff.

## 1. What the merge must know

- **L1 stubs in this tree, to drop at the merge.** The tail of `forms/2025/household.yaml` (household.mfs,
  household.mfs_living, household.mfs_living_else, household.mfs_living_if_mfs, household.mfs_apart_all_year,
  household.mfs_apart_last6). In `params/2025.yaml`: enum `mfs_living`, `household.mfs_living_else`,
  `dc.exclusion_max_mfs`. In the bank: the entry `household.mfs_living` (order 102, seq 9). All were written by
  `/tmp/mfs-l3/l1_stubs.py` under the keys L1 declared in `/tmp/mfs-declared-ids.md`; L1's definitions replace them.
  This lane reads only `household.mfs`, `household.mfs_apart_last6` and `dc.exclusion_max_mfs`.
- **defaults.json.** This tree holds the nx-b1 copy (base caution) plus `/tmp/mfs-l3/defaults_patch.py`: own defaults
  `f2441.mfs_spouse_earned` 0, `f2441.mfs_spouse_deemed` false, `f8962.mfs_exception` false,
  `f8962.mfs_three_years` false, `f8889.mfs_spouse_hsa` false. The `household.mfs_living` (together_late) default
  there is a stub of L1's.
- **Shared files** (this lane's entries only): `interview/2025/questions.yaml` (5 new entries);
  `ambiguities/2025.yaml` (`amb.2025.f2441_mfs_no_credit`); `reviews/2025/consumers.json` (5 rulings);
  `docs/provisional/DECISIONS.md` (one section); new file `interview/2025/coverage/mfs_credits.yaml` (rows kept
  apart from L1's `mfs.yaml`).
- **Restated existing cases** (approved end changes, D2): `stage15.refuse.f2441.mfs`,
  `stage15.refuse.f2441.mfs_benefits` (f2441.json) and `stage11.refuse.hsa_married` (f1040.json). The last case
  gains the input `household.married_dec31: true` (see 2).
- **2026 operations of other changes, mended** because the 2025 lines they name moved:
  - C-CRED-11 (`changes/2026/f2441.yaml`): its two `refuses` ops on f2441.line11 and line26 are removed (the
    refusals are gone).
  - C-PEOP-14 (`changes/2026/f8962.yaml`): its `expr.alternatives` and `label` ops now target
    `f8962.applicable_figured`, where the 2025 body of `applicable` moved.
  - C-CRED-18 (`changes/2026/f8863.yaml`): likewise retargeted to `f8863.eligible_figured`.
  - The f8962 `set_form note` op now quotes the new 2025 note.
- **Forms of other lanes.** None edited. f8889: lane F1's diff (`nx-f1`) is already in this base, byte-identical
  (`diff` of the file is empty). This lane changes the note's first sentence and its refusal list, the `f8889.mfs`
  block, and the first refusal entry of `f8889.line13_figured`. F1's lines (`fsf_*`, `former_spouse_*`,
  `inherited_*`, testing period) are untouched. Both lanes edit the form note's paragraph, a textual neighbour.

## 2. What changed

**Form 2441** (`forms/2025/f2441.yaml`)
- New lines:
  - `f2441.line_a` (printed A): considered unmarried, from `household.mfs_apart_last6`, then `f2441.line_a_home`.
  - `f2441.line_a_home`: a qualifying person's main home for over half of 2025 (`f2441.mfs_qp_count` /
    `mfs_qp_home`, from `dependent.dc_qp` ∧ `dependent.dc_lived_half`), and `household.home_cost`.
  - `f2441.mfs_married`: MFS ∧ ¬line A.
  - Line 11: `f2441.line11_figured` (the old smaller-of); line 11 is zero when `mfs_married`
    (amb.2025.f2441_mfs_no_credit).
  - Line 19: `f2441.line19_other`, with the spouse's earned income input `f2441.mfs_spouse_earned` (gate
    `_if_married`), and the guard `f2441.mfs_spouse_deemed` (gate `_if_married`, refusing on line 19).
  - Line 21: `f2441.exclusion_cap` and `f2441.exclusion_max_mfs` ($2,500).
- Removed: both `s3.mfs` refusals (line 11 and line 26, YAML anchor `&mfs`).

**Form 8863**: `f8863.eligible` chooses on `household.mfs` first (MFS → no). The old body is now
`f8863.eligible_figured`. Every reader of `f8863.paid` is reached only through `eligible` (s3.line3, f1040.line29),
so the education question is never asked on an MFS return (row `mfs.no_education`). No change to person.yaml or
dependent.yaml was needed; the scout's `paid_if_not_mfs` gate is not built.

**Form 8962**
- New lines:
  - `f8962.mfs_ask`.
  - Inputs `f8962.mfs_exception` and `f8962.mfs_three_years`, with their gates.
  - `f8962.line_a` (printed A).
  - `f8962.mfs_barred`.
  - `f8962.applicable_figured` (the old body of `applicable`). `applicable` now returns no when barred.
  - `f8962.alien_not_barred`: `alien_branch` no longer asks the lawfully-present-alien question of a barred filer.
- The existing not-applicable path (D7(a)) then repays the advance payments up to Table 5. Table 5 uses the "other
  statuses" column for MFS, as `params` already had it.
- Source of `f8962.shared_policy` now names "your husband or wife if you file separately".

**Form 8889**
- `f8889.mfs` (gate id kept) is now MFS ∧ treated as family coverage at some time (`f8889.married_family`) ∧ the
  spouse has an HSA of their own. New lines: `f8889.mfs_ask`, input `f8889.mfs_spouse_hsa`, gate
  `f8889.mfs_spouse_hsa_if_asked`.
- The remedy and cite of the refusal (i8889 p. 7, Line 6) are rewritten, and the note is updated.

**Questions added** (bank, text as the filer sees it)
- `f2441.mfs_spouse_deemed` (156/7): "In 2025, was your husband or wife a full-time student, or at some time unable
  to care for themselves because of a physical or mental condition?" Help: student defined; "A Yes ends the
  interview here."
- `f2441.mfs_spouse_earned` (156/8): "How much did your husband or wife earn from work in 2025? Count wages and net
  earnings from self-employment, but not the dependent care benefits in box 10 of their W-2s. Zero if none, or if
  they had a loss."
- `f8962.mfs_exception` (196/8): "Do you live apart from your husband or wife now, and are you unable to file a joint
  return with them because they abused you or abandoned you?" Help defines abuse and abandonment, and says to keep
  records and not send them.
- `f8962.mfs_three_years` (196/9): "Did you take the premium tax credit on a separate return under this exception for
  each of 2022, 2023 and 2024?"
- `f8889.mfs_spouse_hsa` (190/37): "Does your husband or wife have a health savings account (HSA) of their own?"
  Help: "Count an HSA in their name even if nothing was put into it for 2025. A Yes ends the interview here."
- Who could answer No wrongly, and the guard:
  - A filer whose spouse was a student with no pay would enter 0 earnings. Guard: the deemed question, asked first.
  - A spouse with an empty HSA. Guard: the help.
  - A filer unsure whether "abuse" covers emotional abuse. Guard: the help.

## 3. Decisions (alternative rejected)

Owner decisions settled as the scout recommends (recorded in DECISIONS.md):
- **D5.** Narrowed to "family coverage and a spouse with their own HSA". This is narrower than the scout's "own HSA
  or own HDHP": a spouse's own HDHP is already handled by the existing family-coverage questions, as on a joint return
  with one Form 8889, and the line 6 division applies only to "spouses who have separate HSAs" (i8889 p. 7). If the
  coordinator wants the scout's broader wording, add the HDHP to the question; nothing else changes.
- **D6.** Ask Exception 2.
- **D2.** Restate the three cases.

Lane choices:
- **Spouse student/disabled guard.** A new refusing question, `f2441.mfs_spouse_deemed`. Rejected: rewording the
  shared `f2441.student`/`unable` questions to cover a separate-return spouse, which would change joint-return
  wording and existing reviews. Not placed in the `care_facts` tick group, whose heading asks what is "true of you".
- **f8863.** No input gate (see 2). Rejected: switching readers in person.yaml and dependent.yaml (other lanes'
  files); lazy evaluation already keeps the question unasked.
- **f8962.** A barred MFS filer still answers the other-coverage and premium screens on `f8962.line24`. Those
  refusals are listed before the not-applicable result, as for the existing below-100% path. Over-asking, not a
  wrong value.

## 4. Gates replaced and residual refusals

- Removed: `s3.mfs` at `f2441.line11` and `f2441.line26` (L1 removes it at scope and s3.line11).
- Narrowed: `f8889.mfs` (MFS with Form 8889 → MFS with family coverage and a spouse's HSA).
- New: `f2441.mfs_spouse_deemed_if_married`, the refusal on line 19 for a student or disabled spouse with
  benefits.
- Unchanged residuals touching MFS: `f8962.alloc` (a policy shared with the spouse's tax family), `f8962.marriage`
  (joint only).
- `tools/coverage/tree.json` placement for the new gate, and the `categories.json` mapping: requests for the
  integrator (9.3); not edited here.

## 5. Next year (7.1)

- New entries:
  - `C-MFS-F2441-01`: line A label (2026 points to "Line A"; the 2026 line A also covers a line 9b-only credit,
    which stays refused), and the $3,750 labels and cites.
  - `C-MFS-F8962-01`: the 3-year example years move to 2023 to 2025 (label, source, prompt).
- Mends as in 1. `year_changes.py --check`: all 132 entries and 1,260 operations apply.
- New parameter for `propose_params`: `dc.exclusion_max_mfs` 2026 = 375000 (i2441 2026 p. 7).
- f8863 and f8889: no 2026 difference in the MFS rules (i8863 2026 item 2 unchanged; i8889 2026 Line 6 not
  re-read: recorded as a check for adoption).
- Change-map rows for `research/ty2026/changes.md` (coordinator): C-MFS-F2441-01, C-MFS-F8962-01.

## 6. Defects

None filed. Base defects seen and not this lane's:
- 598 federal and 214 NY fixture crashes on `s2.amt_owed`.
- 18 + 5 `sd.qof` unknowns.
- `stage4.sb.foreign_no_filing`.
- `check_bug_inventory` and `siblings --check` failures naming g1/ty26/land3 entries.

## 7. For other lanes and requests

- **L1:**
  - keep `household.mfs_apart_last6` as declared (the Form 2441 line A living test);
  - `dc.exclusion_max_mfs` 250000 in params;
  - the MFS default for `household.married_dec31` (`stage11.refuse.hsa_married` needed it stated).
- **L5:**
  - fixtures M11, M12 and M12b are covered here as `mfs.f2441.benefits_no_credit`, `mfs.f8962.not_applicable` and
    `mfs.f8962.exception`;
  - the generator: add MFS branches for 2441 benefits and 8962.
- **Integrator:** `tree.json` placement for `f2441.mfs_spouse_deemed_if_married`.
- **NY (D8):** Federal Form 2441 line 11/26, 8962 and 8889 values now reach NY on MFS returns; not checked here.

## 8. Verification (this tree; run and seen)

| Command | Result |
|---|---|
| `node engine/dist/main.js build` (with L1 stubs) | build OK |
| `test-fixtures` (own cases) | all 14 pass: 11 new (`mfs.f2441.*` ×4, `mfs.f8962.*` ×3, `mfs.hsa.*` ×3, `mfs.f8863.no_credit`) and 3 restated. Every value of the 11 new cases matched the hand prediction on the first run; the 2 refusal cases needed only the full refusal object (form/remedy/cite) written in. |
| `test-fixtures` (whole) | 1404/2022; all other failures are base: 598 crash on `s2.amt_owed`, ~20 on missing `sd.qof`, 1 Schedule B case. No failure names a line of my forms. The coordinator has since said not to run it again. |
| `test-fixtures --ny` | 142/357; failures only `s2.amt_owed` (214) and `sd.qof` (5), base |
| `interview-rules` | 17 problems, none naming my lines (9 `s2.amt_owed`, dependent/carloan reach, the pruning report). The generator emits no MFS returns, so this check does not exercise the MFS branches. |
| `tick-groups` | passed |
| `interview-coverage --rows interview/2025/coverage/mfs_credits.yaml` | 0 problems, 6 rows. Run with L1's declared removal of the `s3.mfs` refusals applied as a verification-only stub (`/tmp/mfs-l3/l1_scope_stub.py`, reverted after). Without it, every MFS row stops at `s3.mfs`. |
| `citations.py --strict` | 0 findings |
| `year_changes.py --check` | all 132 entries, 1,260 operations apply |
| `check_consumers.py` | my 5 pairs ruled; remaining findings are other lanes' and the base's |
| `check_questions.py`, `check_screens.py`, `check_false_no.py` | exit 0; new subjects due at the release (9) |
| `check_bug_inventory.py`, `siblings.py --check` | fail on base entries (g1, ty26, land3); none of this lane |
| mutate, check-all, `interview-coverage` over the other coverage files, walks | not run (brief; coordinator's deadline) |

**Merge caution found while verifying (for L1 and NY, scout D8).** Once `s3.mfs` stops refusing at
`scope.ready_credits`, the build fails on 5 NY interview fixtures (`ny.status.mfs.40000`, `.70000`, `.120000`,
`.300000`, `ny.refuse.hh_mfs` in `fixtures/ny/2025/it201.json`). They withhold `person[taxpayer].w2[a].box2`
(`null`), which the walk used never to reach. Removing the withholding let the build pass; an input restatement for
the NY lane.

## 9. Review debt (round 2; no paid calls made)

- Transcription + render + class M (line-scoped): f2441, f8962, f8889, f8863. f1040 is touched only through the
  restated fixture.
- Screen review: `f2441.mfs_spouse_deemed`, `gate:f2441.mfs_married`, `gate:f8889.mfs_ask`, `gate:f8962.mfs_ask`,
  `gate:f8962.mfs_exception_if_mfs`.
- False-no review: `gate:f2441.mfs_married`, `gate:f8889.mfs_ask`, `gate:f8962.mfs_ask`,
  `gate:f8962.mfs_exception_if_mfs`.
- Question review: the 5 new questions.

## 10. Walks

Persona walks were not recorded (deadline). The coverage rows stand in as path evidence:
- On a separate return, `f8863.paid` is never asked (`mfs.no_education`).
- The Form 2441 spouse questions come after the Part III facts, and `f2441.prior_year` is not asked of a filer who
  cannot take the credit.
- Line A's questions follow the Marketplace people screen (`mfs.ptc_exception`).
- The HSA spouse question comes at seq 37, after the distribution questions. Seq 27 was taken, and every number from
  1 to 36 was used, so it could not sit next to the coverage questions. The refusal is therefore told late in the
  HSA topic (N11 cost; a renumbering for the next round).

## 11. Left open, in rank order

1. Mutation survivors on the new lines (mutate not run, by the brief).
2. A barred MFS Marketplace filer still answers the coverage screens (3).
3. The line A count uses `dependent.dc_lived_half`, which is the same test the qualifying person already passes;
   a qualifying person under the divorced/separated special rule is refused anyway (`f2441.nondependent_gate`).
