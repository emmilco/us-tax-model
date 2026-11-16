# Lane xadj-a: round-2 adjudication, household / dependent / eic / s8812

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.
Worktree: `.claude/worktrees/xint` (coverage-expansion merge, uncommitted). Fork of lane xadj. No form edits, no paid
review run by this lane, no commit. Rulings files in `/tmp/xadj/a/`; summaries appended to
`reviews/2025/transcription/adjudication/<form>.md`, section "Goal-1 coverage-expansion round (2026-11-15)".

## Counts (Claude family)

| form | kind | result of the review | ruled |
|---|---|---|---|
| household | transcription | 1 agree, 4 disagree | model error 1, representation 3 |
| household | render | 10 match, 1 mismatch | scope 1 |
| dependent | transcription | 1 agree, 23 disagree (whole: partial-input cases) | model error 22, representation 1 |
| dependent | render | 6 match | none to rule |
| dependent | class M | 10 agree, 0 disagree | none to rule |
| eic | transcription | 0 agree, 17 disagree | model error 15, representation 1, scope 1 |
| eic | render | 2 match | none to rule |
| s8812 | transcription | 0 agree, 2 disagree | model error 1, scope 1 |
| s8812 | render | 1 match, 1 mismatch | scope 1 |
| eic | class M | 80 agree, 0 disagree | none to rule |
| s8812 | class M | see "For the coordinator" | |

Findings (medium/high/low): none. Pending bugs: none.

## What was decided on the source (new this round)

- household.filing_status_conflict: the reply refuses every separate filer not married on Dec 31, which also refuses a
  2025 widow; p501 p. 6 ("considered married for the whole year") supports the project's household.joint_unmarried.
- dependent (claimed, ctc/odc/actc, hoh lines, eic_child): the reply's husband-or-wife tiebreak settles a child the
  spouse does not claim for any filer; p501 p. 15 lets a non-parent claim only with AGI above the parents'. The
  project requires dependent.filer_parent (mfs-l4); the project is right.
- eic.credit / eic.separated_box: on a separate return the reply answers Step 3 q. 4 from the eic.same_home input
  rather than household.mfs_living, and allows the credit on two MFS fixtures whose spouse lived with the filer in
  the last 6 months (stage9.mut.eic_mfs_child_same_home $3,261; stage15.refuse.f2441.mfs_benefits $65). Step 3 q. 4
  Yes / q. 5 No is STOP; the project's $0 is right (amb.2025.mfs_lived_apart).

## For the coordinator

- **Tool/data issue (not fixed):** `triage.py --form household` refuses the household log: "cannot triage these
  sections, whose line-scoped pass reply cannot be found ... household.all_tin (pass 7073fcafb61a: its scope names
  lines the form no longer compares: household.widowed_2025)". So rerun_all's triage step on household produced no
  record, and carry could not rule mechanically. The four household lines were ruled by reading the expressions.
- **Latent gap for the K-1 wiring:** Schedule 8812 Earned Income Worksheet line 2b (i1040s8812 p. 7) adds partnership
  K-1 box 14 code A; `s8812.eiw_*` / CLW B line 3 omit it. Unreachable now (scope.k1 and person.se_screen refuse every
  such return), so ruled scope, not a finding; the lane that lifts scope.k1 must add it (and check eic Worksheet B).
- eic triage records one reply-side error: the reply's helper eic.h_age_count cites `person.born_after_1960`, which
  does not exist (model error, no project consequence).
- **s8812 class M:** not yet run when this lane handed back (21:42; queue order s1, s2, s3, then s8812). Its log is
  unruled; whoever picks it up runs nothing new, only rules `/tmp/xadj/classm-s8812.txt`'s result if it exits 3.
- **check_logs could not verify:** at 21:08 `check_logs.py` stopped with "stale build: canonical/2025/ is older than
  forms/2025/s2.yaml" (s2.yaml edited after the build, not by this lane). The rule.py runs reported "open rulings
  remaining: 0" for every log ruled here; the check_logs confirmation is still owed after a rebuild.
