# Source archiving (Stage 0)

Run `python3 tools/fetch_sources.py --fetch` deliberately to retrieve the public
IRS PDFs listed in `tools/sources/2025.json`. Python 3, curl and Poppler's
`pdftotext` must already be installed. No packages are downloaded by the script.
Use `--only ID ...` to retrieve a subset. No return data is accepted or sent.

Run `python3 tools/fetch_sources.py` to verify archived PDF and extracted-text
hashes offline and report missing catalog entries. This is an archive integrity
check, not the later implementation's CLI or a tax correctness check.

The manifest records requested and resolved URLs, actual UTC retrieval time,
SHA-256 hashes, and revision review status. Current IRS URLs can change: a
download is **not** automatically considered a TY2025 source. Inspect its printed
year/revision and record that finding in the manifest before citing it for
encoding. Reusable forms may have an older printed revision. Existing snapshots
are preserved; replacing a revision requires a deliberate catalog/archive change.
Extracted text retains page breaks; PDF page numbers can be located by splitting
on form-feed characters. Layout extraction does not replace visual review where
columns or checkboxes matter.

Source PDFs are IRS publications. Script code is Apache-2.0 as required by the
project specification; the source catalog and archive metadata are CC0-1.0.

## Toolchain inspected

The Stage 0 check found Node v24.11.1, npm 11.6.2, Lean 4.29.1 through elan,
Lake 5.0.0 (the installed Lean build), and pdftotext 26.01.0. Python 3 and curl
are also present. No installation was needed. Elan's remote `stable` query
failed in the sandbox but the installed Lean toolchain ran successfully.
No project toolchain is pinned yet; engine/proof configuration belongs to Stage 1.

## Commit guard

`npm run check-all` runs `tools/check_all.sh`, which runs the suite
(`tools/check_all_steps.sh`, for the default year or the one given with
`npm run check-all -- --year N`) and, when it passes, writes the hash of the tested
working tree to its tier's marker and list of green trees (the last 50 of the clone):
`.git/check-all-green` and `.git/check-all-green-trees` for the full tier,
`check-all-green-fast` and `check-all-green-fast-trees` for fast, and the same with
`docs`. The run counts as green only if nothing outside the suite's own outputs
(`reports/`, `rendered/`) changed while it ran. It refuses to start when a git-ignored
raw review file the review logs reference (`.transcription/`, `.classm/`) is missing
(`python3 tools/worktree_data.py check`; `check --list` prints every reference): a
linked worktree has none of them, and the review checks would otherwise pass on what
little it has.

A linked worktree (an agent's) gets its git-ignored data from the main worktree with
`python3 tools/worktree_data.py clone <worktree>`: complete copy-on-write clones
(`cp -cR`, never links) of the review data (`.transcription/`, `.classm/`,
`.human-review/`, `.extraction-review/`, `.direct-file/`) and the installs
(`node_modules/`, `.engines/`, `lean/.lake/`), and a record of the clone's base (the
hash of every untracked review file, each ledger's length and hash) in the worktree's
git directory. Reviews run there write their raw files and cost rows into the
worktree's copies; `python3 tools/worktree_data.py carry-back <worktree>` (`--dry-run`
first) brings them back: it appends to the main `costs.jsonl` exactly the rows the
worktree appended since the clone (refusing if either ledger no longer begins with the
cloned one), and copies each raw file the worktree changed since the base where the
main copy is unchanged, refusing everything if any file changed on both sides. Naming
such a non-ledger file after `--prefer-worktree PATH...` (repo-relative; shell globs are fine)
copies the worktree's version over main's instead, with one report line per file; a ledger
name is an error, a named file not in conflict is reported and handled as usual, every other
conflict still refuses, and `--dry-run` writes nothing. Files git
tracks are left to the worktree's commits. A worktree cloned some other way has no base
and is refused; carry it back by hand. `python3 tools/worktree_data.py fill <worktree>`
(`--dry-run` first; run from the main checkout) copies into the worktree each untracked
review file main has and the worktree lacks, for a worktree whose uncommitted tracked review
files make `clone` refuse. It never overwrites or deletes a worktree file and never touches
a ledger; each filled file enters the base at the hash of main's copy, so carry-back brings
it back only if the worktree later edits it. `--self-test` runs in check-all.

The suite has three tiers, chosen with `--tier` (`tools/check_all.sh --tier fast`):

- **full** (the default): every step, about 38 minutes. A release needs it.
- **fast**: every step except `mutate`, `ny_mutate`, `engine_differential`, `lean_build`,
  `compare`, `ny_compare` and `human_review` (the human-review tooling's test: human packets
  are optional), about 10 minutes. It does not check mutation adequacy or agreement
  with the independent evaluators, and leaves `mutation.md`, `evaluator_agreement.md`
  and `engine_differential.{md,json}` as the last full run wrote them; `evidence.md`
  then says that its E column dates from the latest release.
- **docs**: compile, the build, and the checks that read the bookkeeping paths in
  `tools/docs_paths.txt` (`check_bug_inventory`, `check_agent_runs`, `siblings_check`,
  `coverage_tree`, and `bookkeeping_self_tests`: the self-tests of the agent-run, siblings,
  bookkeeping and green-record tools),
  about 3 minutes, nearly all of it the build.

A full-green tree is also fast- and docs-green, and a fast-green tree is docs-green.
Which tier a commit needs is decided from the paths it changes against its parent
(`tools/tier_paths.py`): **full** if it changes a path in `tools/full_paths.txt` (the
mutation tool and its equivalence and pinned lists, the Lean evaluator and its
comparison, the engine differential, the human-review tooling's code and data but not its README), **docs** if every changed path is in
`tools/docs_paths.txt`, **fast** otherwise; a merge needs at least fast, a commit with
no parent full. The lists are read from the parent, so a commit cannot widen the list
it is judged by. `tools/tier_paths.py --self-test` (run by `hooks/test_green.sh`) checks
that every reference to a docs-tier path in the code check-all runs is listed with the
steps that read it, and that those steps are in the docs tier.

`npm run check-all-bg` (`tools/check_all_bg.sh`) runs the same suite on a snapshot of
the working tree in `.git/check-all-worktree`, detached, so the main tree can be
edited while it runs (`--wait` runs it in the foreground; `--tier` as above; `--status`
lists the running runs, the check-all slots and the latest finished run, and `--status <tree>`
shows the record of the latest run of that snapshot tree). Each run keeps its own record and
log in `.git/check-all-bg/runs/<snapshot-tree>-<timestamp>/` (`status`, `log`, the newest 50
kept); `.git/check-all-bg/last` is a copy of the latest finished run's status and
`.git/check-all-bg/log` a link to the latest started run's log, so a run that finishes just
before another starts loses nothing. The snapshot is the tree
`git add -A` would commit; the worktree is the script's own and is reset before each
run; ignored data the suite reads is copied in as copy-on-write clones, and the build
outputs are rebuilt from the snapshot. One background run at a time per clone. It runs from the
main worktree or a linked one: the snapshot and the review data come from the worktree
it is run in (which must hold the review data in full), and the installs
(`node_modules`, `.engines`, `lean/.lake`) from the main worktree when that one has
none. When it is green,
`tools/commit_tested.sh -F <file>` commits exactly that tree, leaving edits made since
the snapshot uncommitted (it reads `last`; `COMMIT_TESTED_TREE=<tree>` names another run's
snapshot tree instead); it refuses if another worktree started the run, if the run's
tier is below the one the commit needs, if HEAD has moved since the snapshot or if anything is staged, and writes the
regenerated `reports/` and `rendered/` files into the working tree where it still holds
the snapshot's version.

`tools/release.sh` makes a release: on the clean tip of `main` it runs
`tools/check_all_bg.sh --wait --tier full`, and when the run is green it commits the
reports the run rewrote (if any, with `tools/commit_tested.sh`; `-F <file>` gives the
message) and puts the annotated tag `r<YYYY>.<MM>.<DD>.<n>` on the tested commit. It
pushes the tag only with `--push`. A red run tags nothing.

A run for a year other than the default passes or fails as usual but writes no
marker.

At most `CHECK_ALL_MAX_RUNS` (default 2) check-all runs execute at once on the machine, in
any worktree, foreground (`tools/check_all.sh`) or background (`tools/check_all_bg.sh`), of
any tier; further runs print that they are waiting, and on which runs, and start in arrival
order as slots free (`tools/check_slot.py`, with `--status` to list the holders and waiters).
A slot is an `flock` on a file in `.git/check-all-slots/` (the clone's common git dir),
held by the run and its children and released when the last of them exits, however it ends,
so a killed run leaves no stale slot; a waiter's place is a ticket named by arrival time and
pid, dropped when its pid is dead. A background run waits for its slot before it checks out
its snapshot. The worker pools size themselves to the limit: by default the smaller of
the core count less six and `floor((cores - 2) / CHECK_ALL_MAX_RUNS)`
(`defaultWorkers()` in `engine/src/pool.ts`, used by the test commands, interview-rules
and mutate); `TEST_WORKERS` and `MUTATE_WORKERS` still override. `check_slot.py --self-test`
and `hooks/test_check_bg.sh` (per-run records, pruning, a background run waiting for a
slot) are check-all steps.

After compiling and building, the steps run in three waves of side-by-side steps
(see the head of `tools/check_all_steps.sh`); a step that reads what another writes runs
in a later wave than its writer (`human_review` and `evidence` after
`engine_differential`), a rule no check enforces, so a new
step must be placed by it. A check that runs for both jurisdictions is declared once
(`jstep`), and its New York run is the step `ny_<name>`. The tools' self-tests and test
suites run as two steps, `bookkeeping_self_tests` and `self_tests`
(`tools/self_tests.py --list` names each test and its command), side by side in a worker
pool, each failing test named. A step's output is printed when its wave ends, and
each step's wall time is in `.git/check-all-times`, with each self-test's as
`self_tests/<name>`. Mutation spreads its mutants
over worker threads (`MUTATE_WORKERS`, default `defaultWorkers()` of `engine/src/pool.ts`);
`MUTATE_WORKERS=1` runs it on one.

`tools/hooks/pre-commit` refuses any commit whose tree is not exactly a tree a green
run of the tier the commit needs tested (a marker, or one of the recorded green
trees): no green run, a run of too low a tier, a tree changed since the run, or a
partial stage. Git runs no pre-commit hook on a merge, so `tools/hooks/pre-push`
checks every commit of the pushed range by the same rule, against its own parents,
which catches a merge made by `git pull`; it also refuses a release tag (`refs/tags/r*`)
whose commit's tree is not full-green. Enable both once per clone:

    git config core.hooksPath tools/hooks

`--no-verify` bypasses either hook; that is a deliberate act, not a routine.

## Review rerun guards

`tools/transcription/rerun_all.py` plans every job before it makes any paid call, and
enforces these rules (self-tests: `tools/transcription/test_rerun_all.py`):

- **Once per form per round.** A job (form, review kind, model family) whose log already
  answers the current subject (`subjects.log_state` finds nothing it judged changed, the same
  test `check_logs.py` applies) is not run. `--force-rerun REASON` runs it; the reason goes
  into the run summary (`.transcription/rerun_summary.json`, `"forced"`) and, through the
  `REVIEW_RERUN_REASON` environment variable, into each paid call's row of the cost ledger
  (`.transcription/costs.jsonl`, `"rerun_reason"`).
- **Line-scoped by default.** Transcription and render run with `--lines auto` (only the
  lines whose subject changed). A job runs whole when the tool refuses line scoping (no log
  or no line subjects to merge into, a change outside every compared line, a form with
  partial-input cases), when `--whole` is given, or for a forced rerun of a current log
  without `--lines`. Class M has no line scope. `--lines L` names the lines explicitly.
- **Cost estimate.** Each job is first run with its tool's `--dry-run`, which builds the
  request it would send; its prompt size is priced at the average cost per prompt character
  of the last `PRICE_SAMPLE` (30) successful priced calls of the same tool and model family in
  the ledger. The estimate is printed per job and in total before anything is called. A
  saved response that `--resume` would reuse is still counted. `--dry-run` prints the plan
  and estimate and stops.
- **Owner gate.** A run whose estimate exceeds `COST_GATE_USD` ($3.00), or which includes
  calls the ledger cannot price (no recent call of that tool and family), is refused (exit 2)
  unless `--approve-cost DOLLARS` is at least the estimate.

## EIC Table

`python3 tools/extract_eic_table.py` reads the 2025 Earned Income Credit Table
(i1040gi pp. 49-60) from word boxes and writes `tables/2025/eic_0.yaml` to
`eic_3.yaml`, one table per number of qualifying children with valid SSNs. It
refuses to write unless the rows tile $1 to $68,700 in $50 steps and every
starred cell's footnote (read from the page text, matched by order) fits the row
and the column. `node engine/dist/main.js conjecture` checks every cell against
the credit formula built from Rev. Proc. 2024-40 section 3.06(1); see
`reports/2025/eic_table_conjecture.md`.

## Sampled completeness, screen, false-no and question reviews

`completeness_review.py` and `check_completeness.py`, `screen_review.py` and `check_screens.py`,
`false_no_review.py` and `check_false_no.py`, and `question_review.py` and `check_questions.py` keep sampled reviews (`tools/transcription/samples.py`). A form's (or screen's) subject is the hash of its review prompt without the
reviewer's system prompt; its record holds the samples run on that subject, and the union of their findings is ruled
once. Screen, false-no and question rulings are per sample (`unruled:<unit>#<k>`); a sample carries a ruling only when its
verdict and findings equal a ruled sample's. A claim equal to a ruled claim of the same form and
subject (item and normalised quote) carries that ruling. Between releases a form whose subject changed is due:
listed by check-all, not failed. `--release` of the completeness, screen and false-no checks is the release gate
(`tools/release_reviews.sh`): it fails while any subject is due or short of `SAMPLES_PER_MILESTONE` samples.
`check_questions.py` lists due questions (a count on the console, the list in `reports/<year>/question_currency.md`)
and fails on unruled samples and orphans; its `--release` mode joins the release gate once the first full pass is
ruled (owner decision 2026-11-10). A question's subject is its line, interview wording and help, and its direct
readers' lines and English (`question_review.subject`); a screen's subject leaves out the help its prompt shows. A record marked `grandfathered` holds one review made before
sampling and satisfies the milestone until its subject changes. Runs are guarded: samples beyond the milestone need
`--force-rerun REASON`, and an estimate above the owner's $3.00 gate needs `--approve-cost` (`spend.py`, shared with
`rerun_all.py`).

## Process hooks

- **Fresh build** (`tools/build_fresh.py`): the completeness, screen, false-no and question checks and triage refuse to run when
  canonical/ is older than a model source or engine/dist older than engine/src (rebuild first).
- **Bug inventory in merges** (`tools/check_bug_inventory.py --merge`, from pre-commit): a merge may not create or
  renumber a BUG entry; colliding ids are renumbered in a commit on the branch before merging.
- **Docs conventions** (`tools/check_docs_conventions.py`, docs tier): docs/ files are dated unless living, and
  HANDOFF-NEXT-SESSION.md keeps two entries.
- **Form claims** (`tools/claims.py`): two lanes never edit the same form at once. `tools/hooks/pre-commit` refuses a
  commit that changes a form another branch holds, or adds an input id while another branch holds `inputs`; a commit on
  a lane's branch claims what it changes, and `tools/hooks/post-commit` releases a branch's claims when it is merged.
  `tools/claims.py claim <form> --reason TEXT` claims before work starts; `list` shows the claims.
- **Claude Code hooks** (`tools/claude_hooks/`): `bash_guard.py` refuses `pgrep -f` waits and hand copies into review data; `agents.py` refuses an agent
  launch without an explicit model or without `Class:`, `Year:` and `Jurisdiction:` in its brief (mechanical on Sonnet,
  judgment on Opus), and writes and completes the run's row in `research/costs/agent_runs.jsonl`. They are enabled per
  clone by `.claude/settings.json` (git-excluded), which holds the following. Each command ends in `|| true`: a deny is
  printed as JSON, and a missing or broken script (python exits 2, which a PreToolUse hook reads as a block) must not
  stop every call.

      {"hooks": {
        "PreToolUse": [
          {"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/tools/claude_hooks/bash_guard.py || true"}]},
          {"matcher": "Agent|Task", "hooks": [{"type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/tools/claude_hooks/agents.py || true"}]}],
        "PostToolUse": [{"matcher": "Agent|Task", "hooks": [{"type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/tools/claude_hooks/agents.py || true"}]}],
        "SubagentStop": [{"hooks": [{"type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/tools/claude_hooks/agents.py || true"}]}]}}

## Scripts run by hand

These scripts are not run by check-all; each is run deliberately, and its own header says how. Every other script
under `tools/` is named by check-all or by another tool's code (a reference search, not a trace of every call). The table extractors are the yearly ones: at a year's adoption each writes
that year's table from its archived source, and the check-all step named beside it checks the result.

| Script | What it is for |
|---|---|
| `extract_tax_table.py` | The Tax Table from `i1040gi.pdf` into `tables/<year>/tax_table.yaml` (yearly) |
| `extract_macrs_tables.py` | The MACRS tables of Pub. 946 into `tables/<year>/macrs_gds.yaml` (yearly; checked by `check_macrs_tables.py`) |
| `extract_class_lives.py` | Pub. 946 Appendix B into `tables/<year>/class_lives.yaml` and its enum file (yearly) |
| `extract_eic_table.py` | The EIC Table (section above) |
| `engines/ny_policyengine.py` | The New York differential against PolicyEngine-US, under the engines interpreter (`engines/setup.sh`) |
| `coverage/estimate.py` | The coverage estimate (spec 2.4), under the engines interpreter with the microdata `coverage/fetch_microdata.sh` downloads once |
| `coverage/roadmap.py` | `reports/roadmap.html` from the coverage estimate and the open rows of `TASKS.md` |
| `ny_fixtures.py` | Writes the New York fixtures from `ny_predict.py`'s predictions |
| `new_bug.py`, `task_row.py` | Append a `BUG_INVENTORY.md` entry; add or update a `TASKS.md` row (tested by `test_bookkeeping_tools.py`) |
| `ocr_audit.py` | An image-grounded audit of the archived text layers (Tesseract), for a person to adjudicate; not a gate |
| `extraction/page_review.py` | Local HTML pages of each archived page beside the project's reading of it, for a person to judge |
| `transcription/question_review.py` | The question review (section "Sampled completeness, screen, false-no and question reviews"); also prices every question's prompt without a call (`--measure`) and lists which existing reviews judge each input's wording (`--coverage`) |
| `transcription/migrate_line_subjects.py` | Rewrites transcription logs' line-subject tables (`transcription/README.md`; tested by `test_review_tools.py`) |
| `human_review/test_browser.mjs`, `../ui/test_browser.mjs` | Browser smoke tests of the review packet and the web UI, against a separately launched headless Chrome |
