# T-169 (Schedule A definition details, BUG-0302): report

Branch `claude/A-backlog`, from `main` at the time of branching. Rows: T-169. Forms: sa.

T-169 is **partly done**: the line 1, 5a, 5b (and 5c) parts are fixed by wording. The line 12 and blindness parts
are not done; their questions are in other forms (Owner questions 1 and 2). Proposed bug entries are in
`PROPOSED_BUGS.md` (PENDING-1 to PENDING-4).

## Premise check

Inspected: `forms/2025/sa.yaml`, `gift.yaml`, `person.yaml`, `ftc.yaml`, `ltc.yaml`; the sa entry of
`reviews/2025/completeness/completeness.json` (six claims); `sources/2025/i1040sca.cols.txt`, `i1040gi.cols.txt`,
`p969.cols.txt` (page found by form-feed split).

| Part | Premise in BUG-0302 / the claim | Holds? |
| --- | --- | --- |
| `sa.line1` | free-entry amount with none of the seven medical adjustments | Holds. The question was "Unreimbursed eligible medical and dental expenses" and nothing else. Page detail: the long-term care chart and the $50-a-night limit are on i1040sca p. 2, not p. 1 as the claim cites. |
| `sa.line5a` territory taxes | territory taxes belong on 5a; nothing says so | Holds, but too narrow. The rule (i1040sca p. 3, "U.S. territory taxes") covers lines 5a, 5b **and 5c**. The p. 7 sentence the claim quotes sits under **Line 6** (foreign taxes): "this line" is line 6. |
| `sa.line5b` prepaid 2026 tax | no question or refusal | Holds. The sentence is on p. 6 under Line 5b (the cols text repeats it on p. 7). |
| `sa.line12` | no question on good used condition, its $500 appraisal exception, or the $250 acknowledgment | **Partly does not hold.** `sa.line12` has no question of its own; it sums `gift.allowed`. `gift.special` already asks about "a clothing or household item over $500 not in good used condition" and refuses it. Checked by evaluation (below). The remaining gaps are an item of $500 or less not in good used condition (not deductible) and the $250 acknowledgment. Both belong in `gift.deduction`, form `gift`. |
| `sa.boxes_blind` | blindness is counted with no definition | Holds, but the question is `person.blind` in `person.yaml` ("Are you blind under the standard-deduction instructions?"). That is outside FORMS. |
| `sa.mfs` (sixth claim) | refused by s3.mfs per BUG-0302 | Not part of T-169; not checked further. |

Claimed protections, checked by evaluation (`node engine/dist/main.js eval`, inputs from `stage5.return.itemized`
with `gift[books].deduction` = $600):
- `gift[books].special` = true: `gift[books].allowed`, `sa.line12`, `sa.line14`, `sa.line17`, `sa.deduction` and
  `f1040.line12e` are refusals with gate `gift[books].special`.
- `gift[books].special` = false: `sa.line12` = $600 and `f1040.line12e` = $27,100.
- `sa.excluded_income` (the exception for territory taxes allocable to excluded income): the existing fixture
  `stage4.refuse.sa.excluded_income` refuses `sa.line17` on that gate, and it passes.

## What changed (commit `8f1365a`)

Wording and citations only, in `forms/2025/sa.yaml`, plus regenerated `rendered/2025/sa.md` and
`reports/2025/citations.md`. No expression, gate, refusal or input id changed. No new inputs, so there is no sibling
ripple and no tree.json gate.

- `sa.line1` question: leave out amounts equal to tax-free HSA or Archer MSA distributions (p969 pp. 9, 13);
  premiums paid by pretax pay reduction; a retired public safety officer's premiums paid with a tax-free plan
  distribution; the housework part of mixed nursing and housework pay; meals while away from home for medical care,
  except hospital care (which includes meals and lodging), with other lodging at no more than $50 a night per
  person. Long-term care premiums are included only up to the age limit, with the five chart amounts. On a final
  return, include estate-paid expenses "that Pub. 502 allows". The cite moves from the generic
  `f1040sa "Schedule A (2025), lines 1–18"` to i1040sca pp. 1–2 and p969 pp. 9 and 13, with the quotes.
- `sa.line5a`: include territory income taxes (not as foreign taxes), except those allocable to excluded income and
  those taken as a credit instead.
- `sa.line5b`: only taxes paid in 2025 and assessed before 2026 (assessment by state or local law, generally when
  the filer becomes liable), so a prepayment of 2026 tax not yet assessed is left out. Territory real estate taxes
  are included, except those allocable to excluded income.
- `sa.line5c`: territory personal property taxes are included, except those allocable to excluded income. This
  goes slightly beyond the row's wording ("line 5a"), because the source sentence names 5a, 5b and 5c.

Inference, not sourced text: the "taken as a credit instead" exception is on 5a only. The foreign tax credit
applies to income taxes; i1040sca p. 3 says only "You may want to take a credit for U.S. territory tax instead of a
deduction". The Pub. 969 rule is stated as "amounts equal to tax-free distributions". That is how p969 words it;
i1040sca only says "see Pub. 969".

## Regression and prediction

No behavior changed, so no regression fixture was added. The prediction, written before running, was: every
fixture value unchanged, with only the rendered sa page and the citation-count report changing. The result matched:
1437/1437 fixtures passed after the change, as before it, and git shows only those files changed.

## Over-refusals accepted

None added. Remaining under-coverage, recorded but not fixed:
- The estate-paid expense rule is stated only by reference to Pub. 502. **Pub. 502 is not in `sources/2025`**, so
  its conditions (when estate payments count as paid by the decedent) cannot be cited or quoted.
- The age chart amounts are written into the question text, not taken from `tables/` (`ltc_limit`, used by
  `ltc.limit`). If the table changes, the question will not follow it.

## Owner questions

1. **Line 12 (form `gift`).** Should `gift.deduction` say that a clothing or household item of $500 or less not in
   good used condition is not deductible, and that a property gift of $250 or more needs a contemporaneous written
   acknowledgment (i1040sca p. 11)? Or should a gate refuse a gift lacking the acknowledgment? The over-$500 case
   is already refused by `gift.special` (verified above). PENDING-2.
2. **Blindness (form `person`).** Should `person.blind` state the partial-blindness test (20/200 in the better eye
   with correction, or a field of 20 degrees or less) and the certified eye-doctor statement (i1040gi p. 33)?
   PENDING-3.
3. **Line 1 and computed amounts (outside T-169).** i1040sca says to reduce premiums by the Schedule 1 line 17
   self-employed health insurance deduction and to complete Form 8962 before line 1. The project computes both, and
   `sa.line1` asks for one supplied amount. Should this be wording, or a separate premiums input less `s1.line17`?
   That is a scope choice; I recorded it as PENDING-4 and did not touch it.
4. **Pub. 502.** Should it be archived in `sources/2025` so that the estate-paid and lodging rules can be cited
   directly?

## Rows not done

- T-169 line 12 and blindness parts (Owner questions 1 and 2). The row's "rerun the sa reviews and completeness"
  is left to the integrator, as instructed: no paid reviews were run.

## Checks run

After `npm ci`, `npm run build` and `npm run render`, on the final tree:

| Check | Result |
| --- | --- |
| `node engine/dist/main.js test-fixtures` | 1437/1437 passed (also 1437/1437 on the baseline before the edit) |
| `tools/check_consumers.py` | exit 0; 0 new, 0 stale |
| `tools/check_instruction_cites.py` | exit 0; 0 new, 0 stale |
| `tools/citations.py --strict` | exit 0; 0 findings; quotes 2816 → 2838 (the new locator quotes verify) |
| `tools/coverage/tree.py --check` | exit 0; 191 gates |
| `tools/check_limits.py` | exit 0; 0 new |
| `tools/transcription/check_completeness.py` | exit 1: one new finding, `stale: sa`, which is expected (rerun `completeness_review.py --forms sa`) |
| `tools/transcription/check_logs.py` | exit 1: sa transcription and render logs are stale under both families, which is expected. It also prints "human reading pending" notes (optional under the validation policy) and many `[deepseek, optional]` eligibility notes that cite missing `.transcription/*.prompt.txt`. These are absent in this cloud checkout and do not come from this change. I did not run it on the baseline, so that last point is an inference. |

Not run: `check-all`/mutation, `check_operands.py`, `check_signs.py`, `check_screens.py`, the Lean comparison, and all
paid reviews. **I do not claim a green suite.** No guard or hook blocked anything.

Baseline timing caveat: in the baseline run, `citations.py --strict` started after the sa.yaml edit had been written
to disk (`canonical/` was still the old build), so its baseline count is not a clean pre-edit count. Fixtures,
consumers and instruction-cites in that run used the pre-edit build.

## Inspected vs inferred

- Inspected: all source quotes (exact-match against the cols text), the page of each, the current questions, and
  the gift.special and excluded-income refusals (by evaluation and fixture).
- Inferred: credit exception limited to 5a; the residual check_logs notes predate this change; Guam, CNMI and USVI
  exclusions do not need a gate beyond `sa.excluded_income` (unchecked).
