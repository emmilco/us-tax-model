# Lane b1-adj-ny — adjudication, New York ny_it201 and ny_it2 (goal-1 round, B1)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction ny. Worktree `.claude/worktrees/nx-b1`. Touched only
the Claude transcription and render logs and sidecars of ny_it201 and ny_it2 (through `rule.py --jurisdiction ny`),
their adjudication summaries (`reviews/2025/transcription/adjudication/ny_it201.md`, new `ny_it2.md`), two pending bug
files and this note. No form, tool, build, render or paid review. `carry.py` (dry run) would have ruled nothing.

## Rulings

| form | kind | line | class |
| --- | --- | --- | --- |
| ny_it201 | transcription | 1 | ambiguity (amb.ny.2025.whole_dollars, C4) |
| ny_it201 | transcription | (81) safe_harbor_100 | ambiguity (C4) |
| ny_it201 | transcription | (81) safe_harbor_110 | ambiguity (C4) |
| ny_it201 | render | 48 | finding, low (BUG-0762) |
| ny_it2 | transcription | 17a (whole dollars) | finding, low (BUG-0763) |
| ny_it2 | transcription | 19 (whole dollars) | finding, low (BUG-0763) |

Counts: ny_it201 transcription ambiguity 3; ny_it201 render finding 1; ny_it2 transcription finding 2. None left open.

## Findings

- **BUG-0762 (low; amount-affecting, rare).** Household credit, married filing separately: tables 3
  and 6 key on federal AGI "total from both returns", but `ny_it201.gate.hh_city_mfs` / `gate.hh_state_mfs` refuse
  only when this return's line 19 is within the rows, and MFS is otherwise zero. A spouse's negative AGI can bring
  the total within the rows: lines 48 and 40 are then $0 without a refusal. Fix: add `ny_it201.ask.spouse_agi_negative`
  (asked for MFS with item C No) and make each gate `all[status = mfs, any[<in_range>, ask.spouse_agi_negative],
  item_c = false]`; or drop the in-range test from both gates. Line 40's render was MATCH; it is the sibling.
- **BUG-0763 (low; presentation).** IT-2 boxes 17a and NYC 19 (whole dollars) have no `shown_when` and
  print $0 when there is no withholding, where IT-2 p. 2 says to leave them blank. Fix: helpers
  `ny_it2.h_state_shown` / `h_city_shown` = withheld > 0 and `shown_when` on `ny_it2.state_whole` / `city_whole`
  (no box 16a wages input exists; the owner may instead rule $0 shown by choice). This reverses the reasoning of the
  2026-11-04 model-error rulings on these lines (a record is required for every W-2; its boxes are not).

## Verification

`check_logs.py --jurisdiction ny`: no "open ruling(s)" line for ny_it201 or ny_it2 after the rulings.
