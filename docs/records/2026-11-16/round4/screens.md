# Lane A10-screens (claude-opus-5-5, judgment, 2025, us): interview wording in screen reviews

Round 4, read-only. Nothing in the repository or xint was edited. No builds, test runs or model calls were made.
"Checked" means read at path:line in xint, or measured by a read-only script (`scratch/round4-screens/measure.py`,
`verify.py`) that loads the patched modules from scratch against xint's data and writes nothing in the repository.
"Inferred" means not checked directly.

Outputs:
- `patches/v3/screens.patch`: the change and the one-time migration. `git apply --check` passes against xint's working tree (checked).
- `patches/v3/screens-joint.patch`: optional, separate. It fixes a stale joint-return instruction in the screen
  prompt (see D). Read D before landing it.

## Summary

1. **What the patch does.** Screen-review prompts now show the question as the filer sees it, and the screen's
   subject includes that wording:
   - for a screen asked on its own, the interview prompt;
   - for a box on a tick-box screen, the group's heading, the label beside the box, and the prompt behind
     "What this asks". 61 of the 149 federal screens are boxes on tick-box screens.
   The help is still shown, and still left out of the subject, as the current rule says. A rewording of the prompt,
   the tick label or the group heading now makes a screen due.
2. **Gate and false-no subjects do not change.** `gates.wording()` is untouched. The new display goes through a
   separate function, `gates.shown()`. (checked: gates.subject reads only wording())
3. **Migration ($0).** `migrate_screen_subjects.py` moves each record that is current on the YAML-text subject to
   the new subject, and moves its per-sample rulings and baseline entries with it. Simulated in memory on xint's data
   (checked):

   | | Federal | NY |
   | --- | --- | --- |
   | Records moved | 141 | 12 |
   | Unchanged (subject identical under the new definition) | 8 | 0 |
   | Rulings moved | 129 | 11 |
   | Baseline entries moved | 0 | 0 |
   | Due units afterwards | 0 | 0 |
   | Accepted rulings on current screens, before and after | 136 and 136 | 11 and 11 |

   A second run moves nothing. So `check_screens --release` does not block the next release on these screens.
   - **Why 141, not 134:** the 15 screens whose interview prompt equals the YAML text still change subject if they
     are tick-box members or their prompt formatting changes. Only 8 are truly unchanged.
4. **Pilot: 10 federal screens, estimated $0.93** at the code's own estimate (`spend.estimate`, using the ledger
   fit of fixed $0.0305 + $1.361e-6 per prompt character). That is under the $3.00 gate, so no `--approve-cost` is
   needed. Run it after the migration as second samples (`--samples 1 --force-rerun REASON`). Sample 1 then
   (old YAML wording) and sample 2 (interview wording) sit in the same record.
   - **Full alternatives, estimated:** rerun all 141 moved federal screens for **$18.79**, and the 12 NY screens for
     **$0.94**. The audit's $14.50 used a mean that included gate samples. The recorded screen-only mean is $0.172
     per sample (checked).
5. **New finding (D): the screen prompt tells the reviewer to ignore joint-return gaps.** It says "married filing
   statuses are refused elsewhere" (screen_review.py:155-156 in xint). The gate prompt (:188-189) and the false-no
   prompt (false_no_review.py:93) both say a joint return is in scope (checked). The question wording itself names
   the spouse in many screens.
   - The instruction text is part of `screen_subject`, so fixing it makes every screen due again. That makes it a
     re-review decision, not a wording edit. **Owner decision.**
6. **Minor (checked):** screen_review.json in xint holds 36 records for screens that no longer exist
   (e.g. `scope.schedule1`, `s2.amt`). check_screens reports orphans only for gates (check_screens.py:83-85), so
   these never show. This is not part of this patch.

## A. The change (screens.patch), hunk by hunk

**tools/transcription/gates.py**
- New `ticks()` builds `{input: {"heading", "tick"}}` for questions that have a `group` in the built profiles
  (interview-full.json, then interview-ny.json, last wins, as `questions()` does).
  - The label is `tick`, or the prompt's first line if there is no `tick`. This mirrors ui/app.ts:583
    `q.tick ?? firstLine(q.prompt)` (checked).
  - The heading is the group's `heading`. This mirrors ui/app.ts:624 (checked).
- New `shown(line)` returns `wording(line)` plus `asked`, and `heading`/`tick` for a tick-box box.
- `wording()` and `questions()` are unchanged, so `gates.subject` is unchanged (checked by reading :101-112).

**tools/transcription/screen_review.py**
- New `question_text(sline)`, the text placed after "Input `<id>`: ":
  - **Asked on its own:** the interview prompt (`indent_rest`).
  - **Tick-box box:** "a box on a tick-box screen. The filer ticks it for YES, and leaves it unticked or chooses
    "None of these" for NO.", followed by `Screen heading:`, `Label beside the box:`, and `Question shown under the
    box's "What this asks":`.
  - **Not asked by any profile:** the YAML text plus "(No interview profile asks this input; this is the form's own
    question text.)". The silent fallback is now visible. All 149 screens are asked (measured), so this is a guard.
- `build_prompt` takes `question` in place of reading `sline['expr']['source']`. The template is otherwise
  byte-identical, which lets the migration recompute the old subject exactly.
- `prompt_for(..., question=None)` uses `question_text` by default. The migration passes the YAML source.
- `screen_subject` keeps its definition: the prompt without the gate and the help. Its docstring now says the
  wording is the interview's.
- `run_one`: the record's `question` field is `question_text(sline)`.
- `main`: when new samples are appended to a record, `subject_migrated` is dropped, because the record has now been
  judged on the interview wording.
- Module docstring updated.

Example of the new block for `person.rrta` (checked, printed from the patched code on xint data):
```
Input `person.rrta`: a box on a tick-box screen. The filer ticks it for YES, and leaves it unticked or chooses "None of these" for NO.
  Screen heading: For this person (you, or your spouse on a joint return) — Did either of these describe your work in 2025?
  Label beside the box: Worked for a railroad
  Question shown under the box's "What this asks": For this person (you, or your spouse on a joint return) — Did you work for a railroad in 2025?
Help shown with it: Yes also if box 14 of a W-2 shows railroad retirement (RRTA) pay or tax, ...
```
Before the patch, the same screen showed the YAML text: "Do any wage statements report railroad retirement compensation
or taxes (W-2 box 14), or d…".

**tools/transcription/check_screens.py**
- The docstring states the new subject and the `subject_migrated` mark.
- `findings()` counts current records that carry `subject_migrated` and prints one console line. It does not fail
  and adds nothing to the report.

**tools/transcription/migrate_screen_subjects.py** (new; modelled on migrate_line_subjects.py)
- `source_subject`: the subject with `question=expr.source`, which is exactly the old definition (checked: with the
  old wording, all 149 federal and 12 NY records match it today).
- `plan` sorts each record into one of four outcomes:
  - **move:** the record matches the old subject.
  - **left, "already":** the record matches the new subject.
  - **left, "due":** the record matches neither. It is not laundered.
  - **left, "never reviewed":** there is no record.
- `apply` moves the following:
  - `subject_sha` changes, and `subject_migrated: {"from", "date"}` is added;
  - `unruled:<screen>#k` rulings whose `subject_sha` is the old subject;
  - baseline entries equal to `baseline_check.subject_hash({"subject": old})`.
- Gate records are untouched.
- Output keeps the files' current serialization (checked): screen_review.json is `indent=1, ensure_ascii=False`
  plus a trailing newline; rulings.json is `indent=1` (ASCII) plus a trailing newline.
- Options: `--dry-run`, and `--jurisdiction ny`. It calls `build_fresh.require(rendered=True)`.
- Note: the patch creates the file as mode 644. migrate_line_subjects.py is also 644 (checked).

**tools/transcription/test_review_tools.py**
- `GatedScreens.setUp` also patches `G._TICKS` to `{}`, so the tests never read canonical/.
- `test_the_prompt_shows_the_help_and_the_subject_ignores_it` now takes `before` with the same asked prompt and no
  help. Without that change it would fail, because "not asked" now adds the fallback note.
- New class `ScreenWording` with five tests:
  - rewording the interview prompt changes the subject;
  - a tick box shows its heading and label, and changing either changes the subject;
  - the fallback is marked;
  - the migration moves the record, its ruling and its baseline entry, leaves a gate ruling alone, and is idempotent;
  - a record on another subject is left due.
- **Unverified: the tests were not run** (round 4 rule). The other existing screen tests were checked by reading:
  - :3518-3530 still hold, because "Outside scope?" is still in the gated prompt and both subjects fall back
    identically;
  - :3540-3555 still hold, because a reworded YAML source with no profile still makes the screen due.

**tools/README.md**
- Updates the sentence on screen subjects in "Sampled completeness, screen, false-no and question reviews".
- Adds a row for the new script to the tools table.

### How to verify (after the release check, in a lane worktree)
1. `python3 tools/transcription/test_review_tools.py GatedScreens ScreenWording GateUnits` (or the file's
   normal runner), then `tools/check_all.sh` in that worktree.
2. `python3 tools/transcription/migrate_screen_subjects.py --dry-run`, and again with `--jurisdiction ny`.
   Expected: 141 moved, 129 rulings, 8 left "already"; NY 12 moved, 11 rulings. If wording changes before this
   runs, these numbers change.
3. Run the migration for real in both jurisdictions, then `python3 tools/transcription/check_screens.py --release`
   (and `--jurisdiction ny`). Expected: no `due` for screens, and the console line
   "141 screen(s) current on samples shown the form's question text…".

### Ordering constraints
- Land the code and the migration's output in **one commit**, made after `build_fresh` and before any further
  wording change.
  - Any wording change made between landing the code and running the migration would be absorbed and never
    reviewed.
  - A YAML-text or gated-line change made before the migration correctly leaves the record "due".
- Do **not** land before tonight's release (tooling.md A, point 8). With the migration in the same commit it would
  not block the release, but the release is already gated on a tree.
- `rename_carry.py:333` calls `S.screen_subject` and picks up the new definition automatically (inferred from
  reading; not exercised).

### What it makes due (under the project's rules)
- With the migration: nothing.
- Without the migration: 141 federal and 12 NY screens.
- Gates and false-no: unchanged.
- Docs:
  - docs/2026-11-10_question_review_design.md:40 and :81 are dated testimony. Leave them, and record the change in
    the decision record (tooling.md B.4).
  - The bug-inventory text, if any, goes in the inventory and not in the patch. None was written.

## B. The cost the migration accepts

Each moved record was judged against the YAML text, not against what the filer reads.
- For 134 federal screens those differ (tooling.md B.1, measured there; reproduced here: 134 prompts differ, 0 not
  asked, 61 tick-box members).
- Typical gaps:
  - `sa.charity_limited`: YAML "Are any charitable deductions reduced by income limits…" versus interview "Were
    your gifts to charity so large that the law limits what you can deduct for 2025…".
  - The 61 tick-box members, whose label (at most 12 words) is all a filer must read.
- The rulings that move with the records were made on findings about the YAML text. They stay accepted until each
  screen's next change.
- The mark `subject_migrated` keeps that debt countable (check_screens prints the count). It disappears at a screen's
  next sample or subject change.

## C. Pilot plan (10 federal screens)

**Purpose.** To measure whether showing the interview wording changes what the review finds, before choosing between
leaving the migrated records to work off at their next change and rerunning all 141 ($18.79).
- The project rule allows a global re-review only "if a measured defect calls for it" (CLAUDE.md, inference cost).
- The pilot is the measurement.

**Selection** (data from screen_review.json and canonical/2025/interview-full.json in xint; checked):

| # | Screen | Why | Previous verdict | Tick-box? | Est. |
| --- | --- | --- | --- | --- | --- |
| 1 | `sa.charity_limited` | Largest YAML/interview divergence (ratio 0.02); 8 gated lines | NARROW | no | $0.079 |
| 2 | `gift.special` | Second largest (0.03) | UNCLEAR | no | $0.072 |
| 3 | `s1.alimony_unsupported` | Third largest (0.06); interview narrows to "that alimony" | WIDE | no | $0.072 |
| 4 | `dependent.married` | Audit's example: interview adds "or on a joint tax return"; a COVERS can turn NARROW/WIDE | COVERS | no | $0.057 |
| 5 | `person.rrta` | Tick box (`work_kind`), label "Worked for a railroad" vs YAML about W-2 box 14 | COVERS | yes | $0.133 |
| 6 | `rec.nonitemized` | Tick box (`rec_rare`), long label | NARROW | yes | $0.089 |
| 7 | `f5695.line7a` | Tick box (`energy_power`), "A fuel cell at your main home" | WIDE | yes | $0.075 |
| 8 | `k1p.r_b12` | Tick box (`k1p_boxes_10`), terse "Box 12: section 179 deduction" | COVERS | yes | $0.184 |
| 9 | `f2441.prior_year` | Tick box (`care_facts`), per-person group | WIDE | yes | $0.061 |
| 10 | `refund.two_itemized` | **Control:** wording identical and subject unchanged; measures sampling noise alone | COVERS | no | $0.108 |
| | **Total** | | | | **$0.93** |

The mix covers 4 high-divergence single questions, 5 tick-box members, and 1 control. The earlier verdicts cover all
four kinds: 2 NARROW, 1 UNCLEAR, 3 WIDE, 4 COVERS.

**Cost, computed from the code without running it.**
- `plan()` (screen_review.py:341-361) prices each job with `spend.estimate(len(prompt_for(...)), "screen_review.py",
  model, spend.prices())`.
- I evaluated exactly that with the patched `prompt_for` on xint's data and the current ledger fit, which is
  (screen_review.py, claude): fixed $0.03045 + $1.3612e-6/char.
- Prompt sizes run from 19,277 characters (`dependent.married`) to 112,448 (`k1p.r_b12`).
- Total $0.93, under the $3.00 gate.
- The fit uses the last 30 ledger rows, so the figure at run time may differ slightly.
- Recorded actual costs for these screens were about 10 to 20% above the estimate (e.g. `sa.charity_limited` $0.096
  vs $0.079). So budget about $1.10, the same as the audit's figure.
- Separately, adjudication of the non-COVERS samples is an Opus judgment agent run, logged in agent_runs.jsonl. The
  code does not price it.

**Commands** (after the migration has been landed):
```
python3 tools/transcription/screen_review.py --screens sa.charity_limited,gift.special,s1.alimony_unsupported,dependent.married,person.rrta,rec.nonitemized,f5695.line7a,k1p.r_b12,f2441.prior_year,refund.two_itemized --samples 1 --force-rerun "pilot: interview wording in screen prompts" --dry-run
```
- Expected dry-run output: each line reads `1 sample(s) from #2 ~$0.0x`, then "10 sample(s), estimated $0.93; gate
  $3.00", with no refusal.
- Then the same command without `--dry-run`.
- If the pilot is run *before* the migration instead, `--samples`/`--force-rerun` are not needed for 1-9 (they are
  due). But each new sample then replaces the old record (screen_review.py:412-413), so the comparison needs the old
  record from git. Migrate first.

**Reading the result** (decide the rule before looking):
- For each of screens 1-9, adjudicate sample #2 as usual, and also classify each finding as:
  - (i) the same as a sample #1 finding;
  - (ii) new and caused by the interview wording or tick label, quoting text that is only in the interview;
  - (iii) new but not wording-caused (sampling variation).
- The control (10) shows the base rate of (iii).
- **Rerun all ($18.79 + $0.94 NY, `--approve-cost`):** if two or more of screens 1-9 have a (ii) finding
  adjudicated as a real defect (a NARROW or UNCLEAR the earlier sample could not have seen).
- **Keep the migration and let the debt work off at each screen's next change:** if there are none.
- **Owner's call:** if there is exactly one.
- n=10 with one sample each is weak evidence either way. The rule is a decision threshold, not a measurement of the
  defect rate.
- New non-COVERS samples are `unruled:<screen>#2` and fail check-all until ruled, so the adjudication must land
  with the pilot.

## D. The joint-return instruction (screens-joint.patch, optional)

- The screen prompt says "Do not report differences that arise only on a joint return (married filing statuses are
  refused elsewhere)" (screen_review.py:155-156 in xint; text from 2026-10-17, commit 362e08ec).
- Joint returns are in scope. The gate prompt says so (:188-189), and so does the false-no prompt
  (false_no_review.py:93). Many screen questions themselves say "(or, on a joint return, your spouse)" (checked:
  e.g. `rec.nonitemized`, `f5695.line7a`, `f2441.prior_year`).
- So every screen sample to date was told to skip spouse-only gaps. This is a measured defect in the review
  prompt; its effect on verdicts is not measured.
- The patch replaces the sentence with "Do not report situations another listed refusal already covers. A joint
  return is in scope: on a joint return the question must cover the spouse's situations too."

**Interaction with the migration (important).**
- The instruction text is inside `screen_subject`, because the subject is the whole prompt minus the gate and help.
- If the joint patch lands **before** the migration runs, `source_subject` no longer reproduces the old subjects
  and the migration moves nothing.
- If it lands **after**, every screen (149 + 12) becomes due again.
- So the joint patch is effectively the decision to re-review all screens: about $19.62 federal plus $0.94 NY at
  today's fit, with `--approve-cost`.
- Options for the owner:
  - (a) Land screens.patch and the migration; run the pilot on the final prompt by applying screens-joint.patch
    in the pilot worktree only; decide from the pilot both whether to re-review and whether to land the joint fix.
  - (b) Land both and re-review everything (no migration needed).
  - (c) A follow-up redesign. Make `screen_subject` hash the reviewed content (`question_text`, the gated items,
    the excerpt) rather than the whole prompt. Instruction changes would then apply prospectively, as the project
    rule requires for other reviews and as gates.subject already does. It would need the same kind of one-time
    migration. Not drafted.

## Provenance

- **Inspected:**
  - screen_review.py, gates.py, check_screens.py, samples.py, spend.py, baseline_check.py:40-110,
    rename_carry.py:320-345 and :755-830, question_review.py:283-292 and :400-430, the test fixtures
    test_review_tools.py:3283-3557, ui/app.ts:20-31, :59 and :576-629, and tools/README.md:521-537 — all in xint;
  - xint's reviews/2025/screens and reviews/ny/2025/screens JSON, and canonical/2025/interview-full.json and
    interview-ny.json;
  - the patched modules, loaded from scratch and run read-only (plan, apply in memory, prompt text, estimates);
  - `git apply --check` of screens.patch against xint.
- **Inferred (unverified):**
  - that the new and changed tests pass (not run);
  - that `build_fresh.require` passes at landing time;
  - that rename_carry needs no change;
  - that ticking a box records YES (taken from ui/app.ts:576-578 comments, not exercised in a browser);
  - the run-time cost (the ledger fit moves).
- **Plausible gap:** xint is uncommitted and changing. If any interview wording or YAML text changes before
  landing, the move counts above change. The migration's logic handles that correctly, but the numbers here will
  not match.
