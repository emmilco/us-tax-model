# Completeness review, round 9 (xrel, sampled release reviews): adjudication of the people family

Family `people` (forms `person`, `household`, `dependent`, `s3`). Six claims were unruled at the B1 plus expansion tree
(`.claude/worktrees/xint`), all in `dependent` and `household`; `person` and `s3` had none. The rulings are in the
fragment `/tmp/xrel/frag/people.completeness.json`, keys `unruled:<form>#1.<n>`, each with the record's current
`subject_sha`; the lead merges them into `rulings.json`. `xrel.py merge` (no `--write`) refuses none of them.

Earlier rulings of these forms were leads only: the claim numbers moved between rounds, so each claim was checked
against the current lines (`forms/2025/*.yaml`) and the interview wording (`interview/2025/questions.yaml`), and its
quote against `sources/2025/*.cols.txt`. No new evaluation was needed: no claim turns on an amount the tool computes.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| dependent | 2 | 0 | 1 | 0 | 1 | 0 |
| household | 4 | 0 | 1 | 1 | 2 | 0 |
| **total** | 6 | 0 | 2 | 1 | 3 | 0 |

No real gap, so no bug is filed for this tool.

## dependent (subject 3cc3af70)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | dependent.edu_aoc: the 2- and 10-year bans on the American opportunity credit and the Form 8862 requirement (i8863 pp. 1, 3) | covered | `f8863.ban`, asked when any American opportunity credit is claimed (`f8863.ban_refused`), refuses `f8863.line7`. The reviewer saw the dependent form alone. |
| #1.2 | dependent.claimed: more than four dependents, the checkbox and statement (i1040gi p. 17) | presentation | Every dependent is listed and counted; the box and statement are how the paper form shows rows that do not fit. No amount. |

## household (subject e6820725)

| Claim | Item | Class | Where |
|---|---|---|---|
| #1.1 | household.test1_persons: a parent in a rest home; a parent who died in 2025 (p501 p. 9) | covered | `dependent.parent_home_paid` asks both in its words; `dependent.hoh_test1` reads it. |
| #1.2 | household.test2_persons: born or died, kidnapped child, one qualifier per head of household, tie-breakers (p501 pp. 9-10, i1040gi p. 44) | out of scope (gate `dependent.qc_tiebreak`) | `dependent.hoh_lived_half` (part of the year alive); `dependent.kidnapped` with the refusal `dependent.kidnap_residency`; `dependent.other_claimant` with the refusal `dependent.qc_tiebreak` on `dependent.qualifying_child`. |
| #1.3 | household.hoh_eligible: the unclaimed qualifying child's name in the entry space (i1040gi p. 14, p501 p. 8) | presentation | A notice exists for the spouse's name on a separate return, none for this name. |
| #1.4 | household.qss_eligible: the same for a qualifying surviving spouse (i1040gi p. 15) | presentation | As #1.3. |

## Notes

- **Repeats.** #1.1 of `dependent` repeats the earlier ruling of the same quote, then classed out of scope with the gate
  `f8863.ban_refused`. It is classed covered here because the line that asks the fact, `f8863.ban`, is named. Either class
  holds. The two `household` eligibility claims repeat earlier rulings of the same rules, rechecked against the current lines.
- **MFS.** None of the six claims rests on the removed gate `s3.mfs`.
- **Suggestion, not a defect.** #1.3 and #1.4 could be closed by a notice beside the spouse-name notice in `household.yaml`.
  The tool does not print the filing-status entry spaces, so this is an instruction to the filer.
