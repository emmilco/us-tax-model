# Lane land3-holes: BUG-0642 (NOL gated behind a business) and BUG-0643 (ISO stock vesting in 2025)

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/land3-holes` (detached
snapshot 29ae532a). Not committed. No paid review call and no model call from code.

## Are the defects real

**landing-05: yes, with one caveat about the source.**

- i1040gi p. 91, Line 8a reads in full: "Net operating loss (NOL) deduction. Enter any deduction for an NOL from an
  earlier year. ... See the Instructions for Form 172 for details." It sets no business condition.
- The page does not itself say that a personal casualty or theft loss can create an NOL. That is NOL law (section
  172(d)(4)(C)), and the bank's own help on `scope.nol` already said "Answer Yes too for such a loss that came from a
  casualty or theft". No source in `sources/2025` states it (searched every 2025 source for "net operating loss").
  The reading agent said the same thing (cfindings_C2).
- Before the fix, `scope.schedule1` read `scope.nol_if_business_before`, which is `scope.no` (false) when
  `scope.business_before` is No. A filer who never had a business was never asked `scope.nol` and was not refused.

**landing-08: yes.**

- i6251 p. 4, Line 2i measures the adjustment at the value "when your rights in the acquired stock first become
  transferable or when these rights are no longer subject to a substantial risk of forfeiture". The exception is an
  election, made within 30 days, to include it "upon the transfer to you".
- ISO stock bought (early exercise) before 2025 that vests in 2025 therefore has a 2025 adjustment.
- That filer answers No to `s2.options_any` ("use stock options ... to buy shares, or sell shares bought that way", in
  2025). `s2.iso` (2025 exercise) is never reached and would also be No.
- What the project does for a 2025 exercise-and-hold: refuse on `s2.amt` (Form 6251). The fix sends the vesting case
  to the same refusal.

## The change

The two fixes follow the same rule, N2: a parent that someone could wrongly answer No is fixed with a separate
question, never with a longer parent.

### landing-05 (`forms/2025/scope.yaml`, bank order 258)

Form:

- The gate line `scope.nol_if_business_before` is removed.
- `scope.nol` is ungated. `scope.schedule1` reads it directly, in the same place in its `any`.
- `scope.nol` question, which adds the spouse phrase because a spouse's carryover goes on a joint return: "Are you (or,
  on a joint return, your spouse) carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction?"
- `scope.nol` cite: i1040gi p. 91, Line 8a, "Enter any deduction for an NOL from an earlier year". This replaces the
  generic Form 1040 locator.

Bank:

- New tick group `before_2025`, heading "Before 2025, did you (or, on a joint return, your spouse) have either of
  these?". Its boxes:
  - `scope.business_before` (seq 1), "A business, farm, rental, or share in a partnership or S corporation"
  - `scope.nol` (seq 2), "A loss still being carried into 2025 (a 'net operating loss')"
- New help for `scope.nol`: "A loss bigger than that year's income, carried forward on an earlier return. It can come
  from a business, or from a disaster or theft with no business. A Yes ends the interview here: ..."

Cost and judgment:

- Steps: a filer with no business has one screen where there was one question, so 0 steps more. A filer with a
  business has one step fewer.
- Words: the filer with nothing reads about 12 more.
- Who could wrongly pass over the NOL box: someone whose carryover came from a disaster and who does not know the term.
  The label says "a loss still being carried into 2025", and the help names disaster and theft.
- `scope.passive`, `scope.f8978` and `s179.prior_form` stay beneath `scope.business_before`. Each needs a holding
  before 2025.
- Rejected:
  - widening the parent's wording, because that is two subjects (N1) and a longer parent (N2);
  - a plain ungated question, because it adds a step for every filer.

### landing-08 (`forms/2025/s2.yaml`, bank order 146)

Form:

- New input `s2.iso_vested`: "Did shares that you (or, on a joint return, your spouse) bought before 2025 with
  incentive stock options vest in 2025, that is, first become yours to sell or no longer able to be forfeited?".
  - Cited to i6251 p. 4, Line 2i (the vesting rule and the election) and p. 1, Who Must File.
  - It is asked of every filer.
- `s2.amt` now reads `any(s2.iso_if_options, s2.iso_vested, s2.amt_owed)`, so a Yes refuses Form 6251 on `s2.line2`,
  `s2.line3` and `s2.line21`.

Bank:

- Sixth box of the existing screen `other_pay` (seq 6). This adds no step.
  - Tick: "Shares bought before 2025 with incentive stock options that vested in 2025".
  - Prompt: "Did shares you (or, on a joint return, your spouse) bought before 2025 with incentive stock options (ISOs)
    vest in 2025?".
  - Help: early exercise explained, and a filer who made the 30-day election is told to answer No.

Unchanged:

- `s2.options_any` and `s2.iso` cover the 2025 exercise as before. `s2.iso` gives Yes for stock still unvested at the
  end of 2025, and that only causes a refusal.

Rejected:

- Widening the parent tick to "... or vested". It would draw restricted-stock (RSU) holders into the options branch,
  and it would make the parent longer (N2).

### Other files

- `fixtures/2025/defaults.json`: `s2.iso_vested` false, with the standard "Closed: ..." reason.
- `interview/2025/stage4.yaml`: `s2.iso_vested` listed after `s2.iso`.
- `engine/src/generate.ts`: `s2.iso_vested` added to NOT_DRAWN.
- `tools/engines/generate_cases.py`: `s2.iso_vested` added to SCREENS_NO for `s2.amt`.
- Coverage rows:
  - `scope.nol_casualty_no_business` (`coverage/scope.yaml`): business_before No, nol Yes, refused on `scope.schedule1`.
  - `other.iso_vested_2025` (`coverage/other.yaml`): options_any No, iso_vested Yes, refused on `s2.amt`.
- `reviews/2025/consumers.json`:
  - Removed the stale `consumer:scope.business_before@i1040gi:p91` (the gate is gone) and
    `consumer:scope.nol@i1040gi:p91` (that page is now `scope.nol`'s own).
  - Added eight `scope.nol` pairs that `scope.schedule1` now creates directly (i1040gi pp. 25, 92, 93, 99, 100; i1040se
    p. 1; i1040sf p. 2; i1040sse p. 1). Each was ruled `same` with the reason used for the other screening items: "one
    Yes among the refusal's screening questions".
  - Added `consumer:s2.iso_vested@i1040gi:p112`, ruled `same`.
  - Re-ruled the four `differs` pairs (`s2.iso` and `s2.options_any` at i6251 p. 1 and p. 4) as `same` and dropped
    `fixed_by`. The reason states that the vest case is now asked by `s2.iso_vested`, which `s2.amt` reads beside this
    gate. All phrases are verbatim.
- `bug_pending/landing-05.md` and `landing-08.md`: the Fix, Fix lines, Siblings checked and Regression predictions
  fields are filled in.

### Fixtures (no expected value edited)

- Restated inputs in the class M and mutation files, which take no defaults:
  - `scope.nol` false in 11 cases (`classm.eic.1` to `11`, business_before No);
  - `s2.iso_vested` false in 92 cases (44 in `classm.json`, 40 in `classm.deepseek.json`, 8 in `mutation.json`).
  - No scenario has an NOL or a vesting ISO.
- New `scope.reg.nol_casualty_no_business` (`scope.json`):
  - predicted before running: `scope.ready` refused on `scope.schedule1` with the Schedule 1 remedy;
  - matched.
- New `s2.reg.iso_vested_2025` (`s2.json`):
  - predicted before running: `s2.line2`, `s2.line3` and `s2.line21` refused on `s2.amt`;
  - matched (3 values).
- That both cases would not have been refused before the fix is inferred from the old definitions. They were not run on
  the old tree.

## Verification (this worktree, after the last edit to forms, bank and fixtures)

| Command | Result |
|---|---|
| build + render | build OK; 68 rendered files |
| `test-fixtures` | 1989/1989. The baseline was 1987/1987, and the two new cases are added |
| `test-fixtures --ny` | 357/357 |
| `citations.py --strict` | 0 new (6 in the baseline) |
| `check_consumers.py` | 0 new, 0 stale (452 ruled) |
| `check_questions.py` | 0 new |
| `check_screens.py` | 0 new |
| `check_false_no.py` | 0 new |
| `siblings.py --check` | exit 0 |
| `check_bug_inventory.py` | exit 1. One line each for landing-05 and landing-08: "a committed pending entry was changed or removed". This comes from the snapshot commit, as the brief foresaw. Also eight "landing-04/06/07/09..13 cited but no pending file" lines from the snapshot base, which this lane did not touch |
| `interview-rules` | 0 problems (177 walks) |
| `tick-groups` | passed, 0 problems. Both `before_2025` and `other_pay` were shown whole on the background return (neither is listed as "not checked"). No screen was seen in a browser |
| `check_refusal_reach.mjs` | 465 refusal fixtures checked; 2 listed exceptions (the existing list) |
| `interview-coverage --write` | 0 problems; 498 rows, the two new rows included |
| `year_changes.py --check` | all 90 operations apply |

## Review dry run

`python3 tools/transcription/rerun_all.py --dry-run --kinds transcription,render,classm --forms scope,s2 --model claude-opus-5-5`:

- 5 jobs, total $3.45. This is above the $3.00 gate, so it needs `--approve-cost`:
  - classm s2 (whole), $1.00
  - render s2 (line-scoped), $0.24
  - render scope (line-scoped), $0.78
  - transcription s2 (line-scoped), $0.61
  - transcription scope (line-scoped), $0.83
- No class M job was planned for scope.
- No job was run.

## Left open

- `s2.amt_owed`'s question still says "other than from incentive stock options exercised in 2025". A filer whose stock
  vests may also answer Yes there, which is harmless because both refuse. Its wording was not changed, to avoid a
  re-review for no change in value.
- `.classm/jobs.json` lists `s2.iso` and `scope.nol` (review data). It was not edited by hand.
- The NOL-from-casualty rule rests on section 172(d)(4)(C), not on a source in `sources/2025`. If wanted, add the Form
  172 instructions.
- Reviews due: those in the dry run above. Also:
  - question reviews of `s2.iso_vested` and `scope.nol` (new wording), and of the two new tick labels and the new
    heading;
  - the screen and false-no reviews of the new screen `before_2025` and the new box at the next sample.
- Persona walks were not compared. `draft-walk` is not in this tree. The step count claims above come from the screen
  structure, not from a measured walk.
