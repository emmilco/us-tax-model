# land3-clcw: logs of `clcw26` carried to `clcw_next_year`

Mechanical lane (claude-sonnet-5-5, class mechanical, tax year 2025, jurisdiction us). Worktree `land3-clcw`, not committed.

## What was done

`rename_carry.py` did not move a renamed document's logs. It now does (the `document` entries of
`tools/year_free_names.json`, option `--documents`), keeping the proof that the rename changes only names. Run from
`d6e7c1e6` with the flat map (54 line ids and the 28 `clcw26.*` lines, 82 ids, derived in `/tmp/land3clcw/map.json`):
23 units carried (transcription 11 lines, render 11 lines, class M whole form), 168 not carried. For `clcw_next_year`,
4 lines (8 and 13, transcription and render) are not carried: "cited text changed: i1040gi Form 8862". The rest of the
document (outside the compared lines) is not carried: the redraft changed the document outside every line.

## Files

Tracked, changed: `tools/transcription/rename_carry.py` (document moves, class M case re-keying, context re-stamp,
part B reads the document at `--from` under its old name), `tools/transcription/review_store.py` (a record may name
the document's former name: `former_document`), `tools/transcription/test_rename_carry.py` (self-test of the move),
`tools/README.md`, `fixtures/2025/classm.json` and `classm.deepseek.json` (case ids `classm.clcw26.N` to
`classm.clcw_next_year.N`).

Tracked, moved (13 `clcw26` files deleted, 13 `clcw_next_year` files added), under `reviews/2025/`: transcription
(index, rulings, deepseek index and rulings, adjudication md), render (index, rulings, deepseek index), classm (index,
deepseek index and rulings), questions and false_no (`clcw_next_year.json`). The carried lines, and the
class M cases, carry a `carried` marker (`by: rename`).

Untracked (git-ignored), moved: `.transcription/clcw26.*` to `clcw_next_year.*` (18 files), `.classm/classm.clcw26.*`
to `classm.clcw_next_year.*` (28 files). Per-unit raw replies (questions, false-no, screens, completeness, triage,
archive) keep their names: records name them.

Also modified by the build, not by the lane: `rendered/2025/asset.md`, `rendered/2025/index.md` (regenerated from the
tree's forms; they differ from the snapshot's committed copies).

## Verification

- `python3 tools/transcription/check_logs.py`: `clcw_next_year` no longer missing; it lists only "the transcription
  log reviewed an earlier form ... outside every compared line" and the same for render (stale, for the review round).
  The command still fails for other forms (expected).
- `python3 tools/transcription/audit_skipped.py` (step `classm_skipped`): exit 0 (was a FileNotFoundError on
  `forms/2025/clcw26.yaml`).
- `python3 tools/transcription/review_store.py check`: every record present and named by its hash.
- `python3 tools/siblings.py --check`: exit 0.
- `python3 tools/transcription/test_rename_carry.py`: ok.
- Dry run `rerun_all.py --kinds transcription,render,classm --forms clcw_next_year --model claude-opus-5-5 --dry-run`:
  render whole $0.12 (23,691 chars), transcription whole $1.87 (445,664 chars), class M not run (its log answers the
  current subject); total $1.99 for 2 jobs (gate $3.00). No model was called.

Inferred, not checked: the full `tools/check_all.sh` was not run; `rulings.py` checks and the sampled-review checks
were not run after the move.
