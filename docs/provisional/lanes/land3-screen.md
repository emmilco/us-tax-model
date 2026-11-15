# Lane land3-screen: duplicate `(screen)` sections in transcription records

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/land3-screen`, not committed.

## Cause

There was a key collision between *different* computed `(screen)` lines. It was not one line duplicated and not a fault in how the log is merged. `transcribe.marker_keys` left `(screen)` unqualified on purpose, so every computed `(screen)` line of a form got the log key `(screen)`. Until the redraft, each form had at most one computed `(screen)` line. Now three forms have two each:
ira (`ira.special`, `ira.reservist_repaid`), person (`person.sav_excess`, `person.ira_excess`) and
scveh (`scveh.smr_ok`, `scveh.screen`). asset has one; sc has none. The other `(screen)` lines are inputs.

For those three forms, `line_keys` listed `(screen)` twice in `key_order`. In the comparison, `second_by_printed` and
`write_scoped`'s `fresh` (both dicts keyed by that key) kept only the last line. So `merge_log` wrote the
same section twice, and `ingest` stored a record with two parts named `section (screen)`. `view_of`
then failed in `parse_record`. That is why the two ira sections are identical: both are
`ira.reservist_repaid`'s verdict, and `ira.special` was never judged. A whole-form review of these forms would have collided in the same way.

## Fix

- `tools/transcription/transcribe.py`
  - `marker_keys`: `(screen)` is qualified as `(screen) (<id>)` only where two or more computed lines
    carry it. Screening inputs, and a form's single computed `(screen)` line, keep the bare marker.
  - New `prompt_marker`: the request still shows `(screen)` bare (`build_prompt`), so prompts are
    byte-for-byte unchanged. I checked this: the dry-run prompts for ira, scveh and person equal the saved
    `.lines-2a11f3e11a13`, `.lines-094185db5197` and `.lines-388530d2aca3` prompts.
  - New `second_keys`, used by `compare`: a reply's `(screen)` line with a project id takes the project's key.
    The reply echoes the bare marker, and in a line-scoped pass it may hold only one such line.
  - `line_keys` raises if two compared lines share a log key. A future collision would therefore stop before the
    model call, not after it.
- `tools/transcription/triage.py` `pairs_for`: uses `second_keys`, as `compare` does.
- `tools/transcription/review_store.py` `write_record`: refuses parts that share a name, so no such record
  can be stored again.

## Effect on other forms' logs

None. `check_logs.py` (federal and `--jurisdiction ny`) gives the same output before and after the change
(diffed). `review_store.py check` passes. Every form's `line_keys` is unique (62 forms checked).
Only ira, person and scveh get new keys, and none of their stored logs has a `(screen)` section yet: these lines
were never reviewed, and they are already listed as stale.

## The three records and the logs

`25acd583ae9d…` (scveh), `ef8ec7cd2b8b…` (person) and `dcced19e34c9…` (ira) were orphans. `ingest` wrote them and
then failed before writing the index, so no index names them. I deleted them. The indexes and views of
ira, scveh and person are unchanged from before the failed passes.

I did not recompute them from the saved responses. The prompts are identical, but the receipt name
`<form>.lines-<tag>` hashes the scope's log keys, which now differ (ira `0aab07e26b1b`, scveh
`4175e68469b4`, person `5bb5b3947bc6`). So `--from-response` finds no saved prompt under the new name and
refuses (it makes no call). `rerun_all.py --resume` would then fall back to a paid call. I ran neither.
An offline `compare` of the saved replies, with no writes, gives distinct sections and no extras: ira 6, scveh 23,
person 37 lines.

Coordinator's choice: (a) rerun paid; or (b) reuse the three saved replies at no cost by
filing their receipt files under the new tags and running `transcribe.py --form F --lines auto --from-response`.
I did not do (b), because it means copying `.transcription/` files by hand.

## Paid rerun estimate

`rerun_all.py --dry-run --kinds transcription --forms ira,scveh,person --model claude-opus-5-5`:
ira $0.55, person $1.79, scveh $0.97; total $3.30. That is above the $3.00 gate, so it needs `--approve-cost`.

## Tests

- New class `ScreenLineKeys` in `tools/transcription/test_review_tools.py` (4 tests): key qualification and
  `second_keys`; a stored line-scoped pass over both ira `(screen)` lines (two sections, the store reads
  back, `check()` passes); a pass over one of them, given bare; a refused record with duplicate part names.
  With the old `marker_keys`, 3 of the 4 tests fail.
- Full suite `unittest discover -s tools/transcription`: 315 tests, 313 pass. The 2 failures are in
  `test_rerun_all.UsageLimitBreaker` and come from `test_review_tools.py` line 40, which sets
  `REVIEW_INACTIVE_FAMILY` when the module is imported. `test_rerun_all` passes alone (14/14). That leak was already there.

## Not addressed

References *to* screening inputs still expand to the bare `(screen)` in compared expressions. Two
different screening inputs therefore compare as the same operand. Changing that would change the compared expressions of
many forms, so it is left for a separate decision.
