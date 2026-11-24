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
The Lean toolchain has since been pinned (`lean/lean-toolchain`, v4.29.1); Node is not pinned.

## Commit guard

`npm run check-all` runs `tools/check_all.sh`, which runs the suite
(`tools/check_all_steps.sh`, for the default year or the one given with
`npm run check-all -- --year N`; with more than one year in `years.json` `adopted`, its last stage
builds every other adopted year with the run's engine and runs that year's fixtures, federal and, where New York
has adopted the year, New York's, and in the full tier its Lean comparison: the engine and tools are shared by
every year, so a change to them is checked against each; a change confined to one year's directories needs only
that year's run) and, when it passes, writes the hash of the tested
working tree to its tier's marker and list of green trees (the last 50 of the clone):
`.git/check-all-green` and `.git/check-all-green-trees` for the full tier,
`check-all-green-light` and `check-all-green-light-trees` for light, and the same with
`docs`. The run counts as green only if nothing outside the suite's own outputs
(`reports/`, `rendered/`, and the figure blocks of the last wave, below) changed while it ran. It refuses to start when a git-ignored
raw review file the review logs reference (`.transcription/`, `.classm/`) is missing
(`python3 tools/worktree_data.py check`; `check --list` prints every reference): a
linked worktree has none of them, and the review checks would otherwise pass on what
little it has.

The agent-run ledger, `research/costs/agent_runs.jsonl`, is tracked, but no hook writes it: the Claude Code hook
(`tools/claude_hooks/agents.py`, under "Process hooks") writes each agent run's row to the untracked pending file
`<git common dir>/agent-runs/pending.jsonl`, shared by every worktree of the clone, and totals the row when the agent
stops. `python3 tools/agent_runs_fold.py` (`--dry-run` first if you like) moves the finished rows (those with
`tool_uses`) to the end of the ledger, skipping any `agent_id` the ledger already holds, and leaves unfinished rows
pending. It refuses unless run on the branch `next` (any worktree) or in the main worktree on `main`, so a lane
branch never gains ledger rows to conflict on merge. `tools/check_all.sh` and `tools/check_all_bg.sh`, run there, fold first,
before taking the tree they test, so the folded rows are part of the tested tree and of the commit that follows;
elsewhere they skip the fold, and `AGENT_RUNS_FOLD=0` skips it anywhere. Agents starting and stopping therefore
leave the working tree as it is. The `check_agent_runs` step checks the ledger and warns, without failing, when the
pending file holds finished rows dated before yesterday. `--self-test` runs in check-all.

A linked worktree (an agent's) gets its git-ignored data from the main worktree with
`python3 tools/worktree_data.py clone <worktree>`: complete copy-on-write clones
(`cp -cR`, never links) of the review data (`.transcription/`, `.classm/`,
`.extraction-review/`, `.direct-file/`) and the installs
(`node_modules/`, `.engines/`, `lean/.lake/`), and a record of the clone's base (the
hash of every untracked review file, each ledger's length and hash, and the hash of each
row of main's ledger) in the worktree's
git directory. Reviews run there write their raw files and cost rows into the
worktree's copies; `python3 tools/worktree_data.py carry-back <worktree>` (`--dry-run`
first) brings them back: it appends to the main `costs.jsonl` the rows the
worktree appended since the clone, less any row main already holds as the same line (one
carried back first through another worktree). It refuses if the worktree's ledger no longer
begins with the ledger as cloned or last carried, or if main's ledger has lost or reordered
any row it held then; rows other worktrees added between those rows are accepted, and
nothing in main's ledger is rewritten or dropped. It copies each raw file the worktree changed since the base where the
main copy is unchanged, refusing everything if any file changed on both sides. Naming
such a non-ledger file after `--prefer-worktree PATH...` (repo-relative; shell globs are fine)
copies the worktree's version over main's instead, with one report line per file; a ledger
name is an error, a named file not in conflict is reported and handled as usual, every other
conflict still refuses, and `--dry-run` writes nothing. `--keep-main PATH...` is its counterpart:
each named both-changed file is left as main has it, nothing copied, and recorded in the base as
carried, so a later carry-back raises it again only if the worktree changes it; a path named in
both lists is an error. Files git
tracks are left to the worktree's commits. A worktree cloned some other way has no base
and is refused; carry it back by hand. `python3 tools/worktree_data.py fill <worktree>`
(`--dry-run` first; run from the main checkout) copies into the worktree each untracked
review file main has and the worktree lacks, for a worktree whose uncommitted tracked review
files make `clone` refuse. It never overwrites or deletes a worktree file and never touches
a ledger; each filled file enters the base at the hash of main's copy, so carry-back brings
it back only if the worktree later edits it. `--self-test` runs in check-all.

`python3 tools/worktree_gc.py` sorts the linked worktrees: `keep` (locked with a reason starting "keep",
`git worktree lock --reason "keep: <why>" <path>`), `removable` (clean, HEAD on `main`, nothing for carry-back to
bring), `active` (used in the last 7 days) and `stale` (the rest). `remove` removes the removable ones; `archive
NAME...` saves a worktree's uncommitted diff, untracked files and uncarried review files under
`.claude/worktree-archive/<date>/<name>/`, then removes it. A lane's worktree is removed or archived in the unit
that integrates it. check-all prints `worktree_gc.py check`; `tools/release.sh` and `tools/release_prep.sh` fail
while any worktree is removable or stale. `--self-test` runs in check-all.

**Branches and releases (owner decision 2026-11-22).** Work is committed on the branch `next` and on lane branches,
never on `main`. `main` moves only when `tools/release.sh` fast-forwards it to a commit whose exact tree passed a
green full run in release mode, and the release tag is on that commit; so every commit `main` holds was released or
is an ancestor of a release.

**Preflight.** `tools/check_all.sh` and `tools/check_all_bg.sh` first run `tools/preflight.sh` in the worktree being
tested (`check_all_bg.sh` before it takes its snapshot, so what it writes is in the snapshot) and stop when it fails
(`CHECK_ALL_PREFLIGHT=done` skips it). It rebuilds when the build is stale (`tools/build_fresh.py`), regenerates the
derived files the steps compare with what they would write (`reports/bug_status.md`, `docs/COVERAGE.md` and the
README's coverage table, `reports/<year>/gate_frequencies.md`, `reports/<year>/person_wording.md`, the interview
coverage report when the run will compare it, and last the figure blocks of `tools/doc_figures.py`), then runs the
bookkeeping checks that fail in seconds (`check_bug_inventory`, `check_agent_runs`, `check_docs_conventions`,
`bug_status --check`, `doc_figures --check`), stopping at the first failure. A run therefore never fails because a
generated file was not regenerated.

The run's own regenerated reports are consistent by construction. Steps of the run rewrite reports under `reports/`
(evidence, coverage, citations, and in a full run mutation, the evaluator agreement, the engine differential and the
interview length), and the figure blocks of the handoff, `README.md` and `docs/TRUST.md` quote some of them. The last
wave's step `doc_figures` therefore writes the blocks from the reports the run itself wrote and then checks them;
`check_all.sh` accepts that change to those three files when `tools/doc_figures.py --blocks-changed <tree before the
run>` names them, that is, when their text differs from the tree before the run only between figure markers. A
green run's tree holds reports and figures that agree, and `tools/commit_tested.sh` commits both.

The suite has three tiers, chosen with `--tier` (`tools/check_all.sh --tier full`):

- **light** (the default; what a commit on `next` or a lane branch needs): compile, build and render, the engine
  self-check, the federal and New York fixtures, the bookkeeping checks (`check_bug_inventory`, `bug_status`,
  `check_agent_runs`, `check_docs_conventions`, `siblings_check`, `bookkeeping_self_tests`), the checks of generated
  reports (`gate_frequencies`, `person_wording`, `coverage_tree`, `doc_figures`), the year-label lint
  (`label_year`, "Year-label lint" below), four checks of seconds that would otherwise fail only at a release
  (`hermetic_env`, `twins`, `refusal_reach`, and `engine_cases`: a sample of the engine differential's generated
  returns evaluated by the build, `generate_cases.py --check-project`), the static guards below, and the interview
  checks `interview_rules`, `interview_coverage`, `tick_groups` and `spouse_phrase` scoped to the forms the change
  touches.
  The static guards read the tree and the build and evaluate no return: `year_changes` and `ny_year_changes` (the next
  year's operations still apply, "Year changes as operations"; about 8 s), `renamed_ids` and `ny_renamed_ids` (no old
  id of `tools/year_free_names.json` left, the code included, "Renaming the ids in the data"; about 11 s),
  `mutate_arguments` and `ny_mutate_arguments` (the keyed mutation arguments on the build, below; under 1 s) and
  `unread_params` (every parameter read, below; about 8 s). They run side by side in the first wave after the build.
  `tools/change_scope.py` computes the scope from the paths that differ from HEAD: `all` when a path can change any
  walk (the engine, the profiles, the schema, parameters, tables, an unlisted path), `none` when the interview checks
  read no changed path (tools, bookkeeping, reports, reviews, sources, the Lean evaluator, the web UI), else the form
  ids of the changed form files and of the input keys on the changed lines of fixtures, coverage rows and the
  question bank. With a list, each check gets `--forms <ids>` (`engine/src/form-scope.ts`: a walk, row or tick group
  is checked when one of its input keys names one of the forms); with `none` the four steps are listed as skipped;
  with `all` they run unscoped. A scoped run does not judge what needs every walk (a baseline entry no longer seen,
  the pruning report, the interview coverage report, a coverage set no row uses).
- **full** (the release's tier): every step. In release mode (`CHECK_ALL_RELEASE=1`, which `tools/release.sh` sets)
  it also runs `release_steps`: `interview_length` and the release checks of the sampled reviews
  (`release_completeness`, `release_screens`, `release_false_no`, each with its `ny_` step: the `--release` checks of
  `tools/release_reviews.sh`). Only a release runs it; never run it to commit. The recorded green full runs
  (`.git/check-all-bg/runs/*/times`) took 13 to 32 minutes on an idle machine, median 17; most of the spread is the
  machine's other load. `engine_differential` reuses the outside engines' stored records while their inputs are
  unchanged (`tools/engines/README.md`, "Stored engine records").
- **docs**: compile, the build, and the checks that read the bookkeeping paths in
  `tools/docs_paths.txt` (`check_bug_inventory`, `bug_status`, `check_agent_runs`, `siblings_check`,
  `coverage_tree`, `doc_figures`, and `bookkeeping_self_tests`: the self-tests of the agent-run, siblings,
  bookkeeping and green-record tools), nearly all of it the build.

Between releases, the reports only the full tier rewrites (`mutation.md`, `evaluator_agreement.md`,
`engine_differential.{md,json}`, `interview_length.md`, `evidence.md`, `properties.md`) can be older than `next`'s
tree; the release run rewrites them, and `main` holds only their released versions.

`compare` and `ny_compare` (`engine/src/compare.ts`) run the TypeScript and the Lean evaluator
over every fixture case and over generated whole returns, and fail on any line value that
differs. The generated returns come from the general generator (`engine/src/generate.ts`:
`sampleReturns`, and `nyReturnArbitrary` for `--ny`) and are the corpus of the `properties`
step: both commands take the returns, the seed and the size from one definition
(`corpusReturns`, `CORPUS_SEED`, `CORPUS_SIZE`), so they follow the declared inputs and their
branch coverage is the one `properties.md` lists. `PROPERTY_RUNS=<n>` sets the size for a run of
either command (400 without it; check-all refuses to start while it, or another variable that changes what
a step checks, is set: `SIZING_ENV` in `tools/green.sh`); each report states the seed and the number of
returns it used, so two reports written under different sizes say so themselves. The self-test
`compare --corpus-self-test` (`compare_corpus_self_test`) fails unless the returns the comparison
compares are the returns the properties report's coverage is of, for both jurisdictions, unless a
return with New York answers carries every answer of the federal return of its index, and unless both
commands follow `PROPERTY_RUNS`.

What each run covers. Both evaluators read the whole canonical build, so each run compares
the lines of every document, federal and New York. `compare` runs on the federal fixture cases
and the federal generated returns, none of which gives a New York answer: there most New York
lines are unknown (compared on the missing input each names, a partial count's lower bound and the
gate-pending mark, not on the reason) and the rest have values that need no New York answer
(constants, figures from federal lines, refusals). `ny_compare` runs on the New York fixture
cases and on the same generated returns with New York answers added, and so compares the New
York lines with answers and the federal lines again. The New York lines stay in the federal run:
the federal fixture cases are in no other run, so their New York values would be compared nowhere.
The New York documents take about a fifth of the federal run's evaluation time. Each report states its run's
cases and counts the New York documents' lines apart, by kind.

How the Lean evaluator is run. `taxeval` (`lean/Main.lean`) reads the canonical build once, then reads
cases from standard input, one JSON line each (`{"id": ..., "inputs": {...}}`), and answers one line each,
in the order read: the case's values (`{"id": ..., "values": {...}}`) or the reason it has none
(`{"id": ..., "failed": ...}`: a line ran out of the step budget). A case's answer is a pure function of
the build, the budget and the case (`answerCase`; the memo and the cycle markers begin empty in
`evaluateCase`), so neither the order of the cases nor how they are grouped can change a value. The
comparison sends its cases in batches of 50 (`BATCH_SIZE`), one process at a time. It accepts a batch's
answer only when it is one line per case, in the cases' order, each naming its case (`readAnswers`); for
any other answer every case of the batch counts as a case the Lean evaluator gave no values for. A process
that ends with an error is charged to the first case it left unanswered: the answers before it stand,
that case has no values, and the cases after it go to a new process. A process that has not ended after
20 minutes (`BATCH_LIMIT_MINUTES`; a batch takes seconds, and the whole comparison takes less than that on
a machine with many times more runnable work than cores) is stopped and charged in the same way, and no
process is started after it: every later case counts as one the Lean evaluator gave no values for, so the
step fails within the limit where it would otherwise wait for ever. To evaluate one case by hand:
`echo '{"id":"x","inputs":{}}' | lean/.lake/build/bin/taxeval --canonical canonical/<year>`.

The step first plants answers that are not the cases sent (a case not answered, answered twice or out of
turn, an answer for a case that was not sent, a line that is no answer) and stops unless each leaves every
case of its batch without values. It puts in the Lean evaluator's place a process that does not answer,
with a limit of a second, and stops unless that process is stopped, its cases are left without values
and no process is started after it. It then plants differences on generated returns and stops unless each
is reported on its line with the planted values: for each kind of value (money, count, rate,
Bool, enum, refusal, unknown) a differing Lean value on a computed line of that kind, one per
field the comparison reads (a refusal's gate, form, remedy and citation); a line the Lean
evaluator ran out of steps on, where the TypeScript value is an amount and where it is unknown;
a line removed from the Lean values and a line only they have; and an answer changed for the
Lean evaluator only. `evaluator_agreement.md` counts the compared
values by kind, fixtures apart from generated returns, and what was not compared, by reason:
a case the Lean evaluator gave no values for, a line only one evaluator gave, a line the Lean
evaluator ran out of steps on. Each of those fails the step.

A full-green tree is also light- and docs-green, and a light-green tree is docs-green.
Which tier a commit needs is decided from the paths it changes against its parent
(`tools/tier_paths.py`): **docs** if every changed path is in `tools/docs_paths.txt`,
**light** otherwise; a merge needs at least light, a commit with no parent full. No path
makes a commit need the full tier: its other steps are the release's. The list is read
from the parent, so a commit cannot widen the list it is judged by. `tools/tier_paths.py --self-test` (run by `hooks/test_green.sh`) checks
that every reference to a docs-tier path in the code check-all runs is listed with the
steps that read it, and that those steps are in the docs tier.

`npm run check-all-bg` (`tools/check_all_bg.sh`) runs the same suite on a snapshot of
the working tree in `.git/check-all-worktree`, detached, so the main tree can be
edited while it runs (`--wait` runs it in the foreground; `--tier` as above; `--status`
lists the running runs, the check-all slots and the latest finished run, and `--status <tree>`
shows the record of the latest run of that snapshot tree). Each run keeps its own record and
log in `.git/check-all-bg/runs/<snapshot-tree>-<timestamp>/` (`status`, `log`, and the steps' wall
times, `times`, with their summary, `times.txt`, which `status` names; the newest 50
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

`tools/release.sh [--push] [--allow-open-bugs] [-F <file>] [<commit>]` makes a release: it promotes a commit of `next` (its tip by
default) to `main`. HEAD must be that commit, with a clean working tree (on `next`, or detached at an earlier commit of
`next`), and `main` must be its ancestor. When the commit's exact tree is already release-green (a green full run in
release mode, `CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify tools/check_all_bg.sh --wait --tier full`, in the snapshot
worktree, recorded in the release list of `tools/green.sh`), that run is not repeated, but `tools/release_reviews.sh`
still runs. Otherwise it runs `tools/release_reviews.sh` (fail fast), then that release-mode run. A sampled-review
ruling that confirms an open bug of medium or high severity (or none recorded) promotes nothing unless
`--allow-open-bugs` is given; it is passed to `tools/release_reviews.sh` and, as `CHECK_ALL_ALLOW_OPEN_BUGS=1`, to the
run's release steps, and the tag message lists each allowed ruling and bug. When the run rewrote files (it rewrites the reports the light tier does not),
`tools/commit_tested.sh` commits the tested tree on HEAD (`-F <file>` gives the message) and that commit is promoted.
It then fast-forwards `main` to the commit (`git merge --ff-only` in the worktree holding `main`, or by moving the ref
when none does), tags it `r<YYYY>.<MM>.<DD>.<n>`, records the tree as release-ready, and with `--push` pushes `main`
and the tag. A red run, a sampled-review gap, a removable or stale worktree, or a `main` that is not an ancestor
promotes nothing. A release does not fold agent-run rows (it runs with `AGENT_RUNS_FOLD=0`): it tests
the commit as committed, and agents may run meanwhile, since their rows go to the untracked pending file.

`tools/release_prep.sh [--fail-fast]` is the recommended first step of a release: run it on the candidate tree as
soon as its content is final, before the release-mode full check. A defect the full check would report only when
its wave ends (about 13 minutes for wave 1, longer for wave 2) shows here in minutes. It runs:

1. `tools/release_reviews.sh`, which builds and renders the tree and then runs every release check of the sampled
   reviews (completeness, screens, false-no; both jurisdictions), each separately, so one run lists every due item
   (the reviews to run while the rest proceeds). A failed build stops the run there (`release_reviews.sh` exits 2).
2. The check-all steps of its `PREP_STEPS`, one after another, cheapest first: `check_bug_inventory`, `bug_status`,
   `check_agent_runs`, `doc_figures`, `limits`, `consumers`, `renamed_ids`, `year_changes`, `citations`,
   `check_extraction`, `check_logs` (each with its `ny_` step), `bookkeeping_self_tests`, `test_fixtures` and
   `ny_test_fixtures`,
   `coverage`, `interview_rules` and `self_tests`. Each runs the command `tools/check_all_steps.sh --print-steps
   --tier full` declares for it, so the two cannot drift; a listed name the steps script does not declare stops the
   run (exit 2). A step that exits 0 without a line `tools/step_output.py` requires of it fails, as in check-all.

Every step runs, unless `--fail-fast` stops at the first failure. Each step's output goes to
`<git dir>/release-prep/<step>.log`; a failing step's output is printed. It ends with each step's status and time
and one line, `release-prep: PASS` (exit 0) or `release-prep: FAIL: <steps>` (exit 1). It rewrites nothing but
what its steps write in check-all (`coverage.md`, and the figure blocks `doc_figures` writes before it checks them);
the reports only the later waves or a release rewrite are left as they are, so the figures are those of the committed
reports. A pass does not mean the full check will pass.
It takes one of the check-all slots. `tools/test_release_prep.sh` (check-all `self_tests`) runs it in a temporary
repository with stub tools.

A run for a year other than the default passes or fails as usual but writes no
marker.

At most `CHECK_ALL_MAX_RUNS` check-all runs execute at once on the machine, in
any worktree, foreground (`tools/check_all.sh`) or background (`tools/check_all_bg.sh`), of
any tier. Unset, two runs always may, and a further run (up to as many as the cores and memory hold
at a light run's measured demand, `RUN_CORES` and `RUN_MEM` in `tools/check_slot.py`) starts only
while the one-minute load average and the memory available leave room for it. Further runs print
that they are waiting, on which runs and, beyond the two, why there is no room, and start in arrival
order as slots free (`tools/check_slot.py`, with `--status` to list the holders and waiters).
A slot is an `flock` on a file in `.git/check-all-slots/` (the clone's common git dir),
held by the run and its children and released when the last of them exits, however it ends,
so a killed run leaves no stale slot; a waiter's place is a ticket named by arrival time and
pid, dropped when its pid is dead. A background run waits for its slot before it checks out
its snapshot. The worker pools size themselves to the limit (unset: to the runs holding slots
when the run started, at least two): by default the smaller of
the core count less six and `floor((cores - 2) / CHECK_ALL_MAX_RUNS)`
(`defaultWorkers()` in `engine/src/pool.ts`, used by the test commands, interview-rules,
mutate, interview-length and interview-coverage); `TEST_WORKERS`, `MUTATE_WORKERS` and
`INTERVIEW_WORKERS` still override. `check_slot.py --self-test`
and `hooks/test_check_bg.sh` (per-run records, pruning, a background run waiting for a
slot) are check-all steps.

The engine commands that load the machine take the same slots when they start outside a check-all run
(`SLOT_COMMANDS` in `engine/src/slot.ts`: build, test-fixtures, test-integration, test-serve, interview-rules,
interview-length, interview-coverage, tick-groups, mutate, properties and compare), so that a build or test run
started by hand or by an agent in a worktree waits its turn beside the checks instead of overloading the machine.
Such a command waits for a slot before any work (it prints the same waiting lines), holds it until it exits
(`tools/check_slot.py --for-pid`: a holder process frees the slot when the command's process ends, however it ends),
and passes `CHECK_ALL_SLOT` and `CHECK_ALL_MAX_RUNS` to its children, so a command it starts does not wait again
and its pools are sized as in a run. Where `CHECK_ALL_SLOT` is already set (inside a check-all run, release-prep or
a command that holds a slot) nothing waits, so a run never waits for a second slot while it holds one. A
`--self-test` of these commands runs at once, as do the commands not listed (eval, interview, serve, render and the
rest). `npm run build` takes a slot through the build. `tools/check_slot.py --status` names each holder (`node build`
for a build). On an idle machine the wait is one call of `check_slot.py`, a fraction of a second.

The build (`node engine/dist/main.js build`) walks the fixtures' interview paths on `BUILD_WORKERS` worker threads
(default `defaultWorkers()`; the errors are the same for every count, `interview-paths --self-test`), and reuses a
passing build whose every read is unchanged (`engine/src/build-cache.ts`): the build records what it reads (file bytes,
directory listings, existence), its code (engine/dist, node_modules) and its environment, and a later build in the same
worktree whose reads all give what they gave then prints that build's output and leaves its `canonical/<year>/`
instead of building again, so the preflight's build and the step's are one. `BUILD_CACHE=off` always builds;
`BUILD_CACHE=verify` (the default with `ENGINE_CACHE=verify`, as a release runs) always builds and fails when a stored
build of the same reads gave other output. `build-cache --self-test` is a check-all self-test.
The check steps that are engine commands and write nothing (`STEP_COMMANDS` in `engine/src/build-cache.ts`:
interview-coverage, tick-groups, spouse-wording, check-self-test, interview-rules) are reused the same way: a run is
traced with its worker threads and node child processes (they load the tracer through `NODE_OPTIONS=--import`), and a
passing run that read nothing untraceably (a python or shell child, `fs.promises`, a module outside the hashed code) and
wrote only in its own temporary folders is stored with its output; a later run of the same command line, code and
environment whose every read is unchanged prints that output and a `step cache:` line instead of running. The
preflight's `interview-coverage --write` stands for the step's `interview-coverage` (`WRITE_CHECK`). test-fixtures
starts python and is never reused. `BUILD_CACHE` governs the steps as the build (`verify` runs every step and says so
when one fails where a passing run of the same reads was stored); `step-cache --self-test` is a check-all self-test.

After compiling and building, the steps run in three waves of side-by-side steps
(see the head of `tools/check_all_steps.sh`); a step that reads what another writes runs
in a later wave than its writer (`evidence` after `engine_differential`), a rule no check enforces, so a new
step must be placed by it. A check that runs for both jurisdictions is declared once
(`jstep`), and its New York run is the step `ny_<name>`. The tools' self-tests and test
suites run as two steps, `bookkeeping_self_tests` and `self_tests`
(`tools/self_tests.py --list` names each test and its command), side by side in a worker
pool, each failing test named. A self-test behaves inside a run as when run alone: `tools/self_tests.py` gives each
test its environment without the run settings (`STRIP` in `tools/hermetic_env.py`: release mode, the preflight's
`CHECK_ALL_PREFLIGHT=done`, `AGENT_RUNS_FOLD=0`, the cache modes, the sizing variables and the rest), and each shell
self-test (`tools/test_*.sh`, `tools/hooks/test_*.sh`) unsets them on its first lines, so one run by hand from a
polluted shell behaves the same. Worker counts, `CHECK_ALL_MAX_RUNS` and `CHECK_ALL_SLOT` are passed on.
`hermetic_env.py --self-test` (the light-tier step `hermetic_env`) fails when a tool reads an environment variable that none of its
lists classifies, or when a shell self-test does not unset the run settings: a new run setting goes in `STRIP`. A step's output is printed when its wave ends, under its `== <step>` line.

Some self-tests have no row in `tools/self_tests.py`: a step runs them inside itself, and with the
call removed the step would print one line less and still pass. `tools/step_output.py` lists, per
step, the line each of them prints when it ran and found no problem, and a step that exits 0
without one of its lines fails, with what is missing printed under its `== <step>` line. The steps
and their lines: `compare` and `ny_compare`, the Bool-and-enum choose self-test, the planted answers, the time limit and
the planted differences; `mutate` and `ny_mutate`, the six self-tests of the equivalence reasoning (retargeting,
whole-dollar parameters, unknown-guard side condition, guarded-figure dominance, premise digest,
Bool and enum choose); `engine_differential`, the UsTaxes line cache self-test that
`tools/engines/run.sh` runs (or the line saying that it, or the whole step, was skipped for want of
the engines); `bookkeeping_self_tests`, the tier path rule's self-test that `hooks/test_green.sh`
runs. A self-test added inside a step needs a row there. `step_output.py --self-test` (a check-all
step) checks the matching on constructed logs, that every step with required lines is declared in
`tools/check_all_steps.sh`, and that its `wave` runs the check.

Wall times, in whole seconds, are written to `.git/check-all-times` (the worktree's git directory; rewritten by
each run): each step's as `<seconds> <step>`, each self-test's as `<seconds> self_tests/<name>`, each stage's
(`compile`, `build`, `wave1`, `wave2`, `wave3`) as `<seconds> stage:<label> <its steps>`, and the run's as
`<seconds> run:<tier>`. When the steps end, passed or failed, the run prints their summary
(`tools/check_times.py`, after the last step's output and before the green line): one row per stage with its wall
time, its share of the run, and its slowest and next slowest step; then every step by wall time with its stage,
the slowest of each stage marked with the most that shortening it alone can save; then the self-tests. Stages run
one after another and the steps of a stage side by side, so a stage lasts as long as its slowest step and the times
of its steps do not add up. `python3 tools/check_times.py [FILE] [--top N]` prints the summary of the last run
of this worktree, or of a run's `times` file. Mutation spreads its mutants
over worker threads (`MUTATE_WORKERS`, default `defaultWorkers()` of `engine/src/pool.ts`);
`MUTATE_WORKERS=1` runs it on one. `interview_length` spreads its returns, and `interview_coverage` the walks of
its rows, over worker threads (`INTERVIEW_WORKERS`, default `defaultWorkers()`, as for mutate). Each worker builds
the same list of returns or receives the row, and the results are taken back in list order, so the report, the problems and the exit code are the same for every count; `INTERVIEW_WORKERS=1` runs
both on one thread. Each self-test checks this on a small set (the first five generated returns; the
planted rows and the smallest row file), on one thread and on two workers. Within a thread, both keep what they
compute by state: interview-length the status and reachable inputs of each state its walks and probes meet, and
interview-coverage each answer applied, by the answers given before it, since walks that have answered alike so far
(the minimal returns; every row's background answers) meet the same states. Both are functions of the built data,
the bank and the state, so what is kept is what would be computed again.

A surviving mutant must be explained, by a structural rule checked against the data or by
a hand-written equivalence argument keyed by the mutant's id (`EQUIVALENT_IF` in
`engine/src/mutate.ts`). A hand-written argument names its premises and is pinned to a
digest of them (`premiseDigest`); when a premise changes the digest moves, the survivor is
listed as not yet explained and the step fails until someone re-reads the argument and
records the new digest. The digest covers what the two routes' values can depend on:

- for a premise line: its expression (operator, operands in order, constants, parameter
  and table references, guards, collection and field), its refusal gates in order with
  each gate's line, `when_known`, form, remedy and citation (a refusal value carries all
  of them, spec 4.7), its type, its printed marker, its display condition, and the list of
  lines that read it;
- for a `param:` premise the parameter's type and value, for `enum:` the value names, for
  `table:` the table without its title, citation and column notes, and for `def:` the
  def's id, kind, parameters, collection keys and each line's facts as above.

It does not cover an input's question text, a line's label, citation or note, or a
parameter's, enum's or table's citation: rewording a question or correcting a citation
leaves every argument pinned, and needs no re-reading. An argument that reasons from what
a question says, rather than from the expressions, would need the wording pinned too;
no argument does, and one that did would have to add it to its own `holds`. The step runs
two self-tests of the pins: `premiseDigestSelfTest` (on a synthetic form, each wording or
citation edit leaves the digest and each edit to an expression, type, gate, marker,
display condition, reader, parameter, enum, table or def moves it; on the real data,
rewording every question, label and line citation leaves every pinned argument holding,
and changing any one premise line's type or premise parameter's value un-pins it) and
`retargetSelfTest` (an argument is not taken by a mutant that now reads another line).

The keyed arguments are also checked without a mutation run, in the light tier: `node engine/dist/main.js
mutate-arguments [--ny]` (steps `mutate_arguments`, `ny_mutate_arguments`) takes every generated mutant of the
jurisdiction as surviving and reports each argument whose mutant is no longer generated, reads another line than the
argument names, or no longer holds on the build, and each `ANSWERED_ONLY` id with no argument (`argumentProblems` in
`engine/src/mutate.ts`, the same test as the run's stale-argument check, less whether the mutant is killed). An
argument that a recorded open bug covers is listed in `tools/mutation_arguments_open.json` (`{"open": {argument id:
bug id}}`): it is printed as known and does not fail the step; a listed argument of the jurisdiction with no problem
fails it until it is removed from the list, so the list only shrinks. A change that moves an argument's premises
therefore fails the commit that makes it: re-read the argument and record the new digest, or file the bug and list
the argument. `--self-test` checks the comparison with the list (check-all `self_tests`).

One structural rule explains survivors on unobserved lines (`unobservedLine`): the mutated line is a `(helper)` of a
form with no refusal gate, and it and every line that names it, transitively (in an expression, a collection filter, a
refusal gate, a display condition or a gate), are such helpers, none reading a definition instance and none named by an
interview target, an interview file of the year (federal or New York) or the product's code (evaluator, values sheet,
interview, server, client). Such a mutant changes only those helpers' own values. Any other marker, a `display`
mark (a helper kept to be shown on the values sheet), a refusal anywhere on the chain, or a definition line counts as
observed. The rule is computed from the data on every run, so it lapses
for a chain once an observed line reads it; mutation.md lists these survivors in their own section with the chain ends
(helpers nothing reads, candidates for cleanup), and `unobservedLineSelfTest` plants each way of being observed on a
synthetic chain and checks that the rule then does not apply.

`tools/hooks/pre-commit` refuses any commit made on `main`, and any other commit whose tree is not exactly a tree
a green run of the tier the commit needs tested (a marker, or one of the recorded green
trees): no green run, a run of too low a tier, a tree changed since the run, or a
partial stage; `tools/hooks/pre-merge-commit` refuses a merge commit on `main` (a fast-forward makes no commit).
Git runs no pre-commit hook on a merge that needs no editing, so `tools/hooks/pre-push`
checks every commit of the pushed range by the same rule, against its own parents,
which catches a merge made by `git pull`; it refuses to push `main` to a commit whose tree is not in the release
list, and a release tag (`refs/tags/r*`) whose commit's tree is not full-green and release-ready. Enable the hooks
once per clone:

    git config core.hooksPath tools/hooks

The path is relative: git resolves it against the root of the worktree a command runs in, so each linked worktree
runs its own tree's hooks (an absolute path would make every worktree run one checkout's hooks);
`tools/worktree_gc.py check` needs action, and so fails a release, while it is absolute.

`--no-verify` bypasses either hook; that is a deliberate act, not a routine.

**No ceremonial reruns (owner rule, 2026-11-15; advisory, no tool enforces it).** A check is rerun only where the
tree changed in what that check verifies; a release of a release-green tree reruns nothing. The commit guard still
requires a green light-tier record of the exact tree, so where
a rerun would be purely ceremonial (the tree differs from a green one only in what no check reads) the owner decides
whether to commit with `--no-verify`, as on 2026-11-15 for three commits.

## Review rerun guards

`tools/transcription/rerun_all.py` plans every job before it makes any paid call, and
enforces these rules (self-tests: `tools/transcription/test_rerun_all.py`):

- **Fresh rendered text.** A run that includes render jobs is refused (exit 2), `--dry-run` included, when the
  build is stale or `rendered/` is not what it renders to (`tools/build_fresh.py`, "Process hooks" below): a
  render log's state and request are read from `rendered/`, so on a rendering from before an edit the plan
  would call the log current and price nothing. `render_compare.py` refuses the same way when run directly.
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
- **Mechanical rulings after a review.** A review that leaves open disagreements is followed,
  unless `--no-carry`, by `carry.py`; a transcription review first by `triage.py` on the new reply.
  `carry.py` rules, in order: a reply that fails the host's validation on the line (model error on
  the declaration); a repeat of an earlier settled ruling on an unchanged line (carried over, naming
  its source): the same disagreement content, or, for transcription, a new reply that differs from the
  line exactly as an earlier ruled reply did (the same triage verdict, kinds of difference and witness
  inputs, from the ruling's triage stamp in the sidecar, with the line subject it was ruled on); and a
  disagreement whose triage record, for that very reply and the current form,
  shows the project's line and the reply's agreeing on every input run (no value different, missing
  or invalid; compared on fixture cases and on at least 500 generated returns; no evaluation
  failure; every alternative of every choose line where the two sides differ, that either side reached,
  taken on some compared input, as the record's `branches` counts it, so that agreement on a sample that
  never took the differing branch rules nothing): "representation; equivalent on executable triage,
  ruled mechanically", with the counts.
  One in ten of those (`AUDIT_EVERY`), chosen by a hash of the disagreement's identity, so a rerun
  holds the same ones, is left open and printed as held for adjudication; an agent rules it, so a
  broken rule shows. A disagreement an earlier finding, defect or unsettled ruling answered is never
  ruled by triage. Self-tests: `test_review_tools.py` (`CarryOver`, `TriageRulings`).

## Carrying review verdicts across a rename of line ids

`tools/transcription/rename_carry.py` carries the review verdicts of lines whose ids were renamed, where
the rename is proven to change nothing but the names (owner decision: such a carry is acceptable
evidence). Run it in the renamed tree after its build and rendering:

    python3 tools/transcription/rename_carry.py --map MAP.json --from <commit before the rename> [--report PATH]
    python3 tools/transcription/rename_carry.py --map MAP.json --from <commit> --write --report PATH

`MAP.json` is `{"old id": "new id", ...}` (or `{"renames": [{"old": ..., "new": ...}]}`); `--from` may also
name a directory holding the tree before the rename. Without `--write` it only reports.

- **Stale map.** It refuses the map whole (exit 2, nothing written) when an old id is not a line at
  `--from` or is still a line, a new id was already a line at `--from` or is not one now, an id has no
  document prefix, or two entries share an id.
- **Proof.** For each review unit the rename moves (a compared line of a transcription or render log,
  a whole-form class M subject, a question, screen, gate or completeness record): (A) the subject the
  review recorded equals the subject the tool's own code computes on a copy-on-write scratch copy of
  the tree with every new id put back to its old id (in `forms/`, `rendered/`, `canonical/`,
  `interview/`, `ambiguities/`); and (B) for transcription, render and class M, the year-carry parts
  (`year_carry.parts`: subject with foreign interfaces, values read, cited anchor sections) are equal at
  `--from` and in the scratch tree, and the review policies at `--from` are the current ones. A unit
  that fails either is listed with the reason, nothing of it is carried, and it falls due as usual.
- **What it writes.** Index lines get the current subject and a `carried` marker (`by: rename`, the map
  entries the subject names, `from`, the subject it was proven against); a line whose log key is a
  renamed id is shown from its record's old section under the new key (`section`), and its rulings
  sidecar is re-keyed; class M (and a log without line subjects) gets `subject_carried`; sampled
  records, their per-sample rulings and baseline entries are re-keyed to the new id with the current
  `subject_sha` and a `carried` marker; a completeness ruling's `line` and `gate` are renamed; a
  `consumers.json` ruling or baseline entry of a renamed input is re-keyed when the input's question is
  unchanged. Records,
  verdict and ruling texts and raw replies keep the old names. `check_logs.py`, `review_store.py check`,
  `rulings.py --check` and the sampled checks then accept the carried entries and fail as before on
  anything whose proof did not hold. A later review of the form drops a line's marker only when the
  line's verdict comes from a new record.
- **A renamed document.** The `document` entries of `tools/year_free_names.json` (`--documents FILE`, `none` to skip)
  also move the document's review files to its new name: logs, rulings sidecars and second-family variants,
  adjudication, the per-form questions and false-no files, the top-level raw replies in `.transcription/` and
  `.classm/`, and the class M case ids (`classm.<old>.<n>`) of the fixtures and logs (shown from their old
  sections, with a rename marker; sidecar contexts re-stamped where they were current). Records keep the old
  document name; `review_store.py check` accepts it for a renamed document. Lines whose proof holds are carried;
  the rest stay stale.
- **Not covered.** A second family's transcription and render logs (line carries load the Claude index only;
  class M rulings and a renamed document's variants do move), definition lines' local ids, and the seeded
  generated returns (which move with input ids: rulings citing them
  rest on the earlier sample). It takes several minutes on the whole tree (it computes every subject twice).
- Self-test: `tools/transcription/test_rename_carry.py` (a small tree of its own; check-all `self_tests`).

### Renaming the ids in the data, and checking that none is left

The data that names lines and inputs by path is renamed with `tools/rename_ids.py`, which uses the same
substitution as the carry above:

    python3 tools/rename_ids.py apply [--map MAP.json] [FILE...]   (and again with --jurisdiction ny)
    python3 tools/rename_ids.py check [--map MAP.json]

The map is `tools/year_free_names.json` unless `--map` names another (either shape above). An old id is
renamed, and found by `check`, in three forms: the whole id (`f8853c.pre1996`, not inside a longer id); the
collection-indexed form, alone or as a step of a path (`f8853c[p0].pre1996`, `person[taxpayer].f8853c[c].pre1996`);
and a renamed document's name wherever it stands as a name (`$clcw26`, `clcw26[x]`). It covers, for the year and
jurisdiction: every `.json` under `fixtures/<year>/` (`defaults.json` included), except the lines of the fields
`id`, `description` and `evidence_note`; every line of `interview/<year>/coverage/` and `interview/<year>/personas/`;
and, in the default family's rulings sidecars, the witnesses of each triage stamp (their input and instance, not the
case id), so that a ruling's stamp still matches the triage that `carry.py` compares it with. Ruling texts and keys
are not touched. `apply` also rewrites whole each FILE given (the forms, the question bank and other files the
rename names). A collection-indexed id whose rename moves it to another document is not rewritten; `check` reports
it. The order of a rename: rename the definitions and the files that name them, `rename_ids.py apply` (both
jurisdictions), build and render, `rename_carry.py --write`, then test-fixtures and coverage at once. `check` runs in
check-all for both jurisdictions (steps `renamed_ids`, `ny_renamed_ids`) and fails on any old id of
`year_free_names.json` left in those places. The federal `check` also reads the code (every `.ts`, `.tsx`, `.mjs`,
`.js`, `.py`, `.sh` and `.lean` file under `engine/src`, `ui`, `tools` and `lean`, build output, dependencies and
`tools/test_rename_ids.py` left out), where a line is often named by its bare local name: it reports a quoted bare name `"L"` (or `'L'`, or
backquoted) where the map renamed `doc.L`, `doc` has no line `L` now, and the name stands beside its document: `doc`
is named as a document (`doc.`, `doc[`, quoted) within three lines, or the line quotes at least three names and `doc`
has the most of them among its current lines (a list such as `["line8", "line16a", "line16b"]` of Schedule C
inputs). A line holding `rename_ids: not an id` is not read. Ids built from pieces (`s2\.line(8|21)` in a
pattern) are not found. Tests: `tools/test_rename_ids.py` (check-all `self_tests`).

## Unread parameters

`python3 tools/check_unread_params.py [--year N]` (light-tier step `unread_params`) fails on a parameter of
`params/<year>.yaml` or `params/ny/<year>.yaml` whose key no reader names as a whole name (not inside a longer id).
The readers: `forms/<year>/`, `forms/ny/<year>/`, `interview/<year>/`, `interview/ny/<year>/`, the next year's
operations (`changes/<year+1>/`, `changes/ny/<year+1>/`) and the code and data files under `engine/src`, `tools`,
`ui` and `lean`; a mention in a comment counts. A parameter that code reads only by a name it builds
(`eic.earned_amount${k}`) is listed in `tools/unread_params_allow.json` with the prefix, the files that build the
name and the reason; the check fails on an entry whose key is gone, is read by name, or whose files no longer build a
name from the prefix. A parameter nothing reads is removed, with its staged next-year value
(`research/ty<year+1>/params-<year+1>.proposed.yaml`, `params_auto.json`), rather than listed. Tests:
`tools/test_check_unread_params.py` (check-all `self_tests`).

## EIC Table

`python3 tools/extract_eic_table.py` reads the 2025 Earned Income Credit Table
(i1040gi pp. 49-60) from word boxes and writes `tables/2025/eic_0.yaml` to
`eic_3.yaml`, one table per number of qualifying children with valid SSNs. It
refuses to write unless the rows tile $1 to $68,700 in $50 steps and every
starred cell's footnote (read from the page text, matched by order) fits the row
and the column. `node engine/dist/main.js conjecture` checks every cell against
the credit formula built from Rev. Proc. 2024-40 section 2.06(1); see
`reports/2025/eic_table_conjecture.md`.

## New York years

The New York tools take the tax year the way the federal ones do: `--year N`, else the newest year in `years.json`
(`taxyear.py`). New York publishes a year's forms after the IRS does, so a year can have federal data and none for
New York. In New York mode (`--jurisdiction ny`, `jurisdiction.py`) a year qualifies only if it has New York
definitions (`forms/ny/<year>/`) or a New York catalog (`tools/sources/ny/<year>.json`); for any other year the tool
exits naming both and the New York years that exist. `fetch_sources.py` and `check_extraction.py`, which parse the
flag themselves, refuse the same way; a tool reading an archive that has no `manifest.json` exits naming it
(`archive_text.py`).

A federal year can be adopted before New York's. `years.json` lists New York's adopted years apart
(`ny_adopted`), each of which needs its `forms/ny/<year>/`; `jurisdiction.py --ny-status [--year N]` says whether
check-all checks New York for a year. For a year not listed, check-all skips every `ny_*` step, listing each in its
wave as skipped with the reason and counting them at the run's start and end, and the New York render runs only
when `forms/ny/<year>/` exists. Without `forms/ny/<year>/` the build skips, with a note in its output, every
conflict check (`interview/<year>/conflict_checks.yaml`) that names a New York gate. Adopting New York for a year
is adding it to `ny_adopted`.

- The New York-only tools (`ny_predict.py`, `ny_fixtures.py`, `extract_ny_tax_table.py`,
  `extract_ny_household_tables.py`, `engines/ny_policyengine.py`) are in New York mode without the flag and refuse
  `--jurisdiction us`.
- `ny_predict.py` holds the amounts of one printing (`PRINTED`): `predict()` exits for any other year, so
  `ny_fixtures.py` does too, until the year's amounts are read from its IT-201-I and tax tables and added. Its
  `--self-test` checks the `PRINTED` examples whatever the year.
- `ny_fixtures.py` writes the file named by `--out PATH` whole, and refuses to overwrite a file git tracks or the
  default `fixtures/ny/<year>/it201.json` when it exists (`--self-test`). It reproduces neither the cases added to that file
  by hand since it was generated nor the files' reliance on `defaults.json`; carry New York fixtures to a new year with
  `fixtures_year.py --jurisdiction ny`, not with this script.
- The year tools work for New York with `--jurisdiction ny`: `year_diff.py` (and `--adopt`, which copies
  `forms/ny`, `tables/ny`, `params/ny`, `ambiguities/ny` and `interview/ny` and relocates their citations with
  `citations.py --relocate`), `fixtures_year.py`, `citations.py`, `fetch_sources.py`, `check_extraction.py`, and
  `transcription/year_carry.py`, which carries New York's reviews (`reviews/ny/<year>/`) reading each tree across
  both jurisdictions (a New York line names federal lines).
- The New York tables are extracted, each year, from the archived web pages: the State and City Tax Tables by
  `extract_ny_tax_table.py` (the page's heading, its New York AGI limit and its $65,000 limit read from the page) and
  the household credit tables 1, 2, 4 and 5 by `extract_ny_household_tables.py` (the captions, the header cells the
  citations quote and Notes 1 to 3 checked as printed). Both write `tables/ny/<year>/` and, with `--check`, compare a
  fresh extraction with the committed files byte for byte (check-all steps `ny_tax_table`, `ny_household_tables`).
  `ny_hh_spouse_count` (one for your spouse on a joint return) has no printed amounts and stays by hand.

## Proposing a year's parameters

`python3 tools/propose_params.py --from 2025 --to 2026 --write` reads every parameter of
`params/2025.yaml` from the 2026 edition of the document its citation names, at the place the
citation names, and writes `reports/2026/params_proposal_from_2025.yaml` (per parameter: status
`unchanged`, `changed` or `not found`, the 2025 and proposed values, and the evidence: how the
place was found, the 2026 document and pages, the 2025 text and the 2026 text read) and `.md`
(counts, the declined by reason, the changed values). A value read from an IRS draft is marked
`draft: true`. The tool never fills a parameter whose text it cannot place: the reasons it
declines are listed in its header (a text reworded or gone, printed with different figures in
several places, no edition archived, no text naming the value alone, a value that is not a
printed figure). How a place is read: the citation's quote that prints the value, or the
narrowest window of printed words around it that names the value alone in the 2025 edition,
confirmed by the next wider window; line and item numbers are free, years move with the tax
year, and a text printed the same number of times in both editions is read in order.

Two kinds of parameter are derived by a rule, and their records carry `derived` (the rule). A Count
declared `moves_with_year: N` in the parameter file (the `age.*` years of birth) is the prior value plus
N a year; a reading of its citation, where the next edition can be read, must agree. The Tax
Computation Worksheet rows (`tcw.<status>.b<k>.upper`, `.rate`, `.subtract`) are the next year's
rate-table row at the row's rate (read by `extract_printed_tables.rate_schedule` from the revenue
procedure): its upper limit, its rate, and the rate on its lower limit less its base. The rule is
checked on the prior year first, and a schedule with a different number of rows over the Tax Table
boundary is noted on each of that status's records (the worksheet section needs a row the form lacks).

`--compare FILE` scores a proposal against a parameter file taken as the truth. Two runs check
the reader: `--from 2025 --to 2025 --compare params/2025.yaml` (how many 2025 values it reads
back from their own citations) and `--from 2026 --to 2025 --params
research/ty2026/params-2026.proposed.yaml --compare params/2025.yaml` (the hand-read 2026
citations read in the 2025 archive, against the adopted 2025 values). `--self-test` (in
check-all) plants two editions of a few documents and checks each kind of reading and of
refusal.

## Printed tables

`python3 tools/extract_printed_tables.py --check` (check-all) reads the small printed tables again
from the year's archive and compares them, cell by cell, with the committed `tables/<year>/` files:
`dc_rate` (Form 2441 line 8, or the phaseout schedule of its instructions when the form refers to
it), `ltc_limit` (Form 7206 line 2(b), against the Instructions for Form 7206 and the revenue
procedure), `savers_rate` (Form 8880 line 9, against section 25B(b)(2)'s 3/4 and 1/2 thresholds and
the parameter `savers.agi_limit`), `rate_schedule` (the revenue procedure's Tables 1 to 4, each base
against the previous row and the Tax Computation Worksheet parameters against their rows) and the
passenger automobile limits (`auto_limit`, `auto_limit_first_nobonus`, from Pub. 946, checked against
three printings by `check_auto_limits.py`). Tables are found by the words printed with them, not by
page. `--write [--table ID] [--out DIR]` writes a year's tables (refusing one that is not well formed
or that its second printing or formula contradicts); `--out` writes outside `tables/` for a year not
yet adopted.

Written by hand: `quarter_convention` (the mid-quarter fractions, fixed by the regulations, not a
yearly printing), `macrs_last_year` (each recovery period plus one; checked against `macrs_gds` by
`check_macrs_tables.py`), `recovery_year` (the year less the year placed in service, plus one: figured,
not printed; its keys are the `placed_year` enumeration, renamed with the year) and `simple_catchup`
(three amounts printed in the running text of Pub. 560 and the year's retirement plan notice; the
2026 Pub. 560 is not archived).

## Page layouts

The tools that read an archived document by page (the Tax Table, EIC Table, Form 8962 and Pub. 946 class-life
extractors, the second transcription of the Pub. 946 tables, and the instruction-section check's page ranges of
Form 1040 and Schedules 1 to 3 in i1040gi) take the pages from `tools/layouts/<year>.json`, read through
`tools/layouts.py`. Each page range names the words printed on its first page (`first`), its last page (`last`),
the page after it (`last_before`) or the lowest pages of a list of words (`each`); `fields` hold a layout's other
values for the year (the EIC Table's column edges and last row, the HHS guidelines the Form 8962 tables reprint). A
year with no file, or no entry, stops the tool that needs it, naming the file.

`python3 tools/layouts.py --check` (check-all) fails when a range's pages are not where its words are printed in
the year's archive. `python3 tools/layouts.py --propose --from 2025 --to 2026` writes the next year's file: every
range placed again by its words in the new archive (years in the words moved), the fields carried and listed for
review; a layout whose document has no edition archived, or whose words are not printed, is listed and the file is
not written unless `--partial`. `--self-test` (in check-all) plants an edition with a page inserted.

## Sampled completeness, screen, false-no and question reviews

`completeness_review.py` and `check_completeness.py`, `screen_review.py` and `check_screens.py`,
`false_no_review.py` and `check_false_no.py`, and `question_review.py` and `check_questions.py` keep sampled reviews (`tools/transcription/samples.py`). A form's (or screen's) subject is the hash of its review prompt without the
reviewer's system prompt; its record holds the samples run on that subject, and the union of their findings is ruled
once. Screen, false-no and question rulings are per sample (`unruled:<unit>#<k>`); a sample carries a ruling only when its
verdict and findings equal a ruled sample's. A claim equal to a ruled claim of the same form and
subject (item and normalised quote) carries that ruling. Between releases a form whose subject changed is due:
listed by check-all, not failed. `--release` of the completeness, screen and false-no checks is the release gate
(`tools/release_reviews.sh`): it fails while any subject is due or short of `SAMPLES_PER_MILESTONE` samples, and while an
accepted or carried ruling confirms an open bug of medium or high severity (or of none recorded) in `BUG_INVENTORY.md`
(`samples.open_defects`: the ruling's `bug` or `bugs`, the ids its class names when the class is a defect or a real
gap, "low defect: ..." included, or a finding it classes so; "no gate defect; ... (BUG-NNNN)" confirms nothing),
unless the release is made with `--allow-open-bugs` (`tools/release.sh`, `release_prep.sh` and `release_reviews.sh`
pass it on), which lists each such ruling and bug in the tag message.
`check_questions.py` lists due questions (a count on the console, the list in `reports/<year>/question_currency.md`)
and fails on unruled samples and orphans; its `--release` mode joins the release gate once the first full pass is
ruled (owner decision 2026-11-10). A question's subject is its line, interview wording and help, and its direct
readers' lines and English (`question_review.subject`); a screen's subject holds its question as the interview shows it
(`screen_review.question_text`: the prompt, and for a box of a tick-box group the group's heading and the box's label),
so a rewording makes the screen due, and leaves out the help its prompt shows. A screen record marked `subject_migrated`
(`migrate_screen_subjects.py`) is current on samples shown the form's own question text until its next change or sample. A record marked `grandfathered` holds one review made before
sampling and satisfies the milestone until its subject changes. Runs are guarded: samples beyond the milestone need
`--force-rerun REASON`, and an estimate above the owner's $3.00 gate needs `--approve-cost` (`spend.py`, shared with
`rerun_all.py`).

## Interview coverage rows

`node engine/dist/main.js interview-coverage` (the check-all step `interview_coverage`, beside
`interview_rules`) walks every row of `interview/<year>/coverage/*.yaml` through the built interview and
fails, naming the row, when the walk does not end where the row says; it calls no model. It also fails when
`reports/<year>/interview_coverage.md` is not what the rows produce: `--write` writes the report (after a
change to the rows, or to the wording of a question or refusal a row meets). `--rows FILE` (repeatable) checks
other row files instead, without the report, and `--schema FILE` names another schema file holding
`coverageFile`. The row format, the background return that answers the questions a row leaves out, and what a
row cannot say are in `interview/README.md`, "Coverage rows". Its `--self-test` is a row of
`tools/self_tests.py`.

## Test-data defaults

A hand-authored fixture case states only the answers that make its scenario. `fixtures/<year>/defaults.json` (and,
for the New York cases, also `fixtures/ny/<year>/defaults.json`) gives every other input and every roster one value
with its reason. `engine/src/fixture-inputs.ts` (`resolveInputs`) is the only place the defaults are applied; Python
tools read cases through `tools/fixture_inputs.py`, which calls that resolver (`main.js fixture-inputs`), so every
tool evaluates a case on the same inputs. The evaluator, the command-line program and the interview never read the
defaults, and the class M and mutation files take none.

A default is sound when it is what a filer in the case's situation would truthfully answer. Where it is not, the
project's own line usually does not read it, but a model's transcription of the form may, and its value then differs
from the project's on every case that takes the default.

**Resolution order.** (1) Parameter-relative inputs become amounts. (2) Every input the case does not state takes its
default, entry by entry for the collections the case lists. (3) A default with a withholding condition is left out
where the condition holds; every condition is read on the inputs as they stand after step 2. (4) An input the case
states as `null` is left out. An input left out is unknown to the evaluator.

**Conditional withholding.** A default that is untruthful in a situation another answer identifies says so beside
its value:

```json
{ "input": "household.married_dec31", "value": false, "reason": "...",
  "withheld": { "when": [{ "input": "f1040.status", "in": ["mfj", "mfs"] }],
                "reason": "A filer who files jointly or separately is married, ..." } }
```

`when` is a list of tests that must all hold. A test reads one answer, stated or defaulted, and compares it with
constants: `{"input": <input>, "is": <value>}`, `"in": [<values>]` or `"not": <value>`, or
`{"count": "$<collection>", ...}` for the number of entries a roster lists. For a default of a collection's input, a
test reads a top-level form's input or an input of the same entry (or of an entry enclosing it), and a count reads a
top-level roster or the roster the entry is in. A test on an answer the case leaves unknown does not hold, and a
condition never removes an answer the case states. A condition reads only inputs whose own default is unconditional,
so the order in which conditions are read cannot matter. The build refuses a condition that names an unknown input
or roster, compares with a value the answer cannot take, tests one answer twice, reads an entry it cannot be read
beside, reads its own input or an input whose default is conditional, or holds in no case.

**Consistency rules.** `consistency` in a defaults file lists answers that one filer cannot give together, each with
its reason, in the same tests:

```json
{ "never": [{ "input": "f4952.has_interest", "is": false }, { "input": "f4952.line4g", "not": 0 }],
  "reason": "The election on Form 4952 line 4g is made by a filer with investment interest expense." }
```

The build refuses a case in which every test of a rule holds and at least one of the answers read is a default the
case took (a case that states all of them is a scenario, and is not refused), and it refuses defaults that break a
rule by themselves. A rule on a collection's inputs is read entry by entry. `open` on a rule lists what is known to
break it and stays, each with its reason: a case id, or `(defaults)` for the defaults themselves, in which case an
entry that takes every answer the rule reads from the defaults is not reported again. An open entry that no longer
breaks its rule is refused. The rules state only what cannot be true of one filer; they do not re-derive the forms.

**State, withhold or leave.**

- Leave the default where it is the truthful answer in the case's situation.
- State the answer where the scenario means one, including an answer equal to the default that the case's result
  rests on: a case whose student's number was only applied for states that no.
- Withhold in the case (`null`) where the scenario is that the question is unanswered.
- Withhold in the defaults (a condition) where the default is untruthful for every case in a situation another
  answer identifies; a case in that situation that needs the answer states it.
- Do not withhold a default only because the project does not read it there. A review's transcription may read it,
  and an unknown in its place hides a real disagreement (`docs/2026-11-11_test_data_defaults_audit.md`).

**Guards.** The build checks every input and roster has exactly one default of a value it accepts, every condition
and rule is well formed, and no case breaks a rule (`defaultsProblems`, `consistencyProblems`); `check-self-test`
plants each malformed condition and each kind of violation. A commit that changes an existing default's value or
its withholding condition needs one line per default in its message, `Fixture-default-changed: <input> (<n> cases)`,
with the number of cases whose inputs change as `tools/defaults_guard.mjs` counts them (`tools/hooks/commit-msg`); a
default for a new input needs none. `tools/fixtures_year.py` carries the defaults file to a new year with its
conditions and rules, less the open entries of cases it drops, with the defaults the year's operations give new
inputs added and those of removed inputs dropped ("Year changes as operations").

## Year changes as operations

A change prepared for the next tax year is kept as operations keyed by line id in `changes/<year>/<form>.yaml`
(`changes/ny/<year>/` for New York), not as a copy of a form: `tools/year_changes.py` applies the operations of year
N+1 to the forms, question bank and profiles of year N. Design and the classification of the TY2026 change map:
`docs/2026-11-14_year_change_operations.md`; the TY2026 entries: `changes/2026/README.md`.

```yaml
changes:
  tax_year: 2026
  form: f1040
  entries:
  - change: C-PRI-02                       # the change-map entry
    evidence:                              # printed where it says, in sources/2026
    - {doc: f1040, page: 3, quote: "13a Additional deductions from Schedule 1-A, line 44"}
    verified: draft                        # draft, or final once checked against a final edition
    operations:
    - set: {line: f1040.s1a_deductions, field: printed, from: 13b, to: 13a}
```

Operations: `add_line {after, line}`, `remove_line {line}`, `set {line, field, from, to}` (`field` a path of keys such
as `expr.take` or `cite.locator`; `from: null` is absent, `to: null` removes), `add_form {form}`, `set_form {field,
from, to}`, `add_question {input, like | after, entry, profiles, default, reason}` (`like` lends its order number and
its place in the profiles, never its wording), `remove_question {input}`, `set_question {input, field, from, to}`,
and on the ambiguity register (`ambiguities/<year>.yaml`, by entry id) `add_ambiguity {entry, after}` (`entry` a whole
register entry; appended, or placed after the entry `after`), `set_ambiguity {id, field, from, to}` and
`remove_ambiguity {id}`. An entry may list the lines it `awaits` (`{line, change}`), lines another change not yet
written is to add, and a free-text `note`.

**Split files.** Several lanes may write operations on one form: besides `changes/<year>/<form>.yaml`, a file
`changes/<year>/<form>.<topic>.yaml` holds its own entries, with `form: <form>` (the loader keys on that field, not
the name). Files apply grouped by the name's form part, the form's own file before its split files (sorted), so a
split file may build on lines the form's own file adds; collisions are found across files.

**New inputs' defaults.** An `add_question` for an input line carries the input's test-data `default` (a value its
type accepts: a Bool, an integer, non-negative unless `Dollars`, or a value of its enum) and a one-line `reason`, as
`fixtures/<year>/defaults.json` holds them ("Test-data defaults"). The check fails a new input without them;
`fixtures_year.py` writes them into the new year's `defaults.json`, after the default of the question the new one is
placed after, drops the defaults of inputs the operations remove, resolves the cases against the result, drops a
case's answer to a removed input where it equals that input's unconditional from-year default (it says what the
default said), marks "not evaluated in <year>" (and lists) the cases that still state a removed input, and drops (and
lists) an expectation on a removed line. A case of a file that takes no defaults (class M, mutation) is given the
new inputs' defaults as stated answers where it does not answer them, so a value it asserts does not become unknown
for want of an input the year adds; the report lists those answers, and any expectation the carry still moves from a
known value to unknown. The engine's fixture loader leaves the marked cases out (`classm-jobs`,
`mutate` and the other commands that evaluate every case see none of them), and `test-fixtures` names them and fails
while any remain.

**The register.** After the operations, every line's `ambiguity` names a register entry, an added entry is linked by
a line or says why not (`unlinked`), an entry whose last linking line goes is removed or given an `unlinked` reason,
and no line or interview file names a removed entry (the build's rules, `engine/src/check.ts`). Adoption writes the
register entry by entry, as it writes lines.

**Interview files.** The other files of `interview/<year>/` (profiles' targets, coverage rows and sets, personas,
gate frequencies, the bank's tick-box `groups`) are changed by file and path: `set_interview {file, field, from, to}`
(`field` a path of keys; with `list` and `item`, a field of the list entry with that id),
`add_interview_item {file, list, item, after}` and `remove_interview_item {file, list, item}` (`list` a path to a
list; `item` an entry with an `id`, named by its id, or a plain value such as a target), `add_interview_file {file,
data}` and `remove_interview_file {file}`. They fail as the line operations do (gone, stale, already applied,
collision); a profile's `questions` and the bank's questions stay with the question operations, and profiles and the
bank are not removed. After them, what an interview operation writes must name lines that exist, an entry id or key
it removes must not still be named in its file, every group must be named by a question and every question's group
declared. Adoption writes these files block by block (an entry of an id-keyed list, the item lines of a plain list),
keeping comments, and refuses if the written text does not load as the applied data.

**Year-valued enums.** An enum whose values are years declares `extends_with_year: true` in the parameters
(`placed_year`); `year_diff.py --adopt` adds `y<to-year>` to it, labels it first in the `value_labels` of every
question whose input has that enum type (refusing, before it writes anything, labels that are not each year labelled
by itself, newest first), and re-derives the `recovery_year` table (each row
the to-year less the year placed in service, plus 1, after checking every from-year row follows that rule; a row for
`y<to-year>`). Tables keyed by such an enum whose cells are printed amounts (`auto_limit`,
`auto_limit_first_nobonus`) get their new rows from the new year's Pub. 946, not by rule.

- `year_changes.py --check` (check-all step `year_changes`, with `ny_year_changes`) fails, naming the file, change,
  position, kind and line, when an operation's line, form or anchor is gone (the closest ids suggested), the value it
  expects is not there (stale), it is already applied, two operations collide, a reference is left dangling, a gated
  input is read outside its gate, a new input has no question or a question outlives its input, a new input has no
  valid default, a new question takes another's order and seq, the register is left inconsistent with the lines'
  `ambiguity` links, or the evidence is not printed on its page (or is marked final on a draft). It notes the
  parameters the operations read that the year does not define, awaited lines, and entries whose documents are all
  final now. `--against DIR` checks another tree's `forms/`, `interview/` and `params/` read-only (an exported branch).
  It also notes how many references in year-shared files name a line the operations remove, or a refusal gate no
  refusal uses after them (below). When every operation applies, it runs the engine's static checks
  (`engine/src/check.ts` through `main.js check`: references, cycles, types, guard tiling, gates, citations, tables)
  on the tree the operations produce, federally and on this checkout (`--no-static` skips them): the applied forms
  and register, the year's parameters with the staged values of `research/ty<N+1>/params-<N+1>.proposed.yaml` laid
  over them (a value staged as none keeps the year's; retired parameters removed; changed enumerations replaced), the
  year's tables with the staged ones of `research/ty<N+1>/tables-<N+1>/` in their place, and every citation filled
  from the new year's archive; a citation of a document not yet archived for the new year gets an all-zero snapshot,
  so its snapshot check is skipped and the document is named in a note. A static error fails the step, naming the
  line, except an id that names another number than the line prints (`lineIdProblems`), which `--check` counts in a
  note (renaming them is T-353) and `year_diff.py --adopt`, which runs the same checks, refuses. It is not the build:
  schema validation, the interview and refusal-note checks, display rules and test-data defaults still wait for
  adoption. `--self-test` plants a type error, a self-reading line and an id that names another printed number in the
  applied tree, and checks that id drift is a note under `--check` and a failure in adoption.
- `year_shared_refs.py [--year N]` lists those references: code and tool data kept for every year (under `tools/`
  and `engine/src/`, not under a year directory) that name such an id: the id itself (also inside a key such as a
  mutation pin's), an instance id (`dependent[{k}].x`), the local name as a quoted string in a file that builds the
  form's ids from names (`f"f5695.{k}"`: a weaker match), and a coverage-tree `"gate"` placement of a retired gate.
  It changes nothing: each shared file serves the old year too, so whether it branches by year, skips or drops the
  id is the adoption lane's judgment. `--adopt` writes the list to `reports/<to>/shared_refs_from_<from>.{json,md}`.
  `--self-test` (in check-all) plants each kind of reference and each non-reference.
- `year_changes.py --record EDITED.yaml` prints the operations that turn the year's form into an edited copy of it,
  as an entry to complete with its change and evidence.
- `year_diff.py --adopt` refuses to adopt when an operation does not apply or an awaited line is missing, then
  applies the operations to the relocated copy, block by block: every line, bank entry and profile line no operation
  touches keeps the copy's text. It lists, in `reports/<to>/year_literals_from_<from>.json` (and in the year-diff
  report), every line of the copy that names a year outside a citation (a `locator:` or `quote:` scalar, its
  continuation lines included), each year classed: `from_year`; `year_id` (an id or constant bearing a year,
  `amb.2025.x` included); `birth_cutoff` (a year of birth, in a scalar that speaks of birth, equal to a year-moving
  age parameter's value or the year before it: the parameter is named); `adjacent_year` (three years before to two
  after: prior returns, carryovers, the next year; moves when relative to the tax year, stays when a statutory
  date); `fixed_reference` (a document number such as Notice 2025-69); `other_year`. A line whose moving years (the
  from-year, the adjacent years and the years of birth) can be moved carries the moved text as a candidate; nothing
  is edited. A year-moving age parameter declares `moves_with_year: N`; an `age.*` Count without it counts as moving
  by 1.
- `year_diff.py --adopt` also carries, never over an existing file, the from-year's review files adoption keeps:
  the citation rulings (marked "carried from <year>", to be reviewed again), the rulings and baselines of the
  source-coverage checks (`operands`, `consumers`, `limits`, `instruction_cites`, `signs`: copied byte for byte) and of
  the input-quote check (`input_quotes`, with the year in a parameter's key moved), the twin declarations
  (`twins.json`, byte for byte: a declared difference the year's operations changed is reported by `check_twins.py`,
  to be restated), and the input and adapter contract banks (`transcription/{input,adapter}_contracts/<year>/`, with `tax_year` moved; an input bank
  keeps its source snapshot, so a new edition whose text differs is refused as stale until the cases are reviewed).
  A bank required in one year is required in every later year. A ruling is keyed by its finding; a baseline entry
  holds while its subject hashes as recorded, or as recorded once the two marks adoption moves (a citation's
  `tax_year`, a "(<year>)" edition) are moved back one year (`baseline_check.year_back`), so a carried entry comes
  due where the new year changed anything else.
- `--self-test` (in check-all) plants each failure in a synthetic tree, and checks that writing equals applying in
  memory and keeps untouched blocks byte for byte.
- `year_rehearse.sh [--from 2025] [--to 2026] [--dest DIR] [--stand-in-sources] [--reuse-build]` rehearses the
  whole adoption on what is archived today, in a scratch copy outside the repository (default
  `/tmp/year-rehearse-<to>`), and writes nothing in the repository. In order: build the from-year,
  `year_diff.py --adopt`, the staged parameters (`research/ty<to>/params-<to>.proposed.yaml`, in the
  `params/<from>.yaml` format: staged values with their cites, the from-year value where no to-year source prints one,
  `retired` removed, `enums.changed` applied) and tables (`research/ty<to>/tables-<to>/`), `citations.py --strict`,
  build and render the to-year (and rebuild the from-year), `fixtures_year.py --no-hand-work`, `test-fixtures`,
  `year_carry.py` without and with `--write`, `review_store.py check`, `check_logs.py`, `rerun_all.py --dry-run`
  (which also plans, whole, the forms the carry left with no to-year log), and a digest of the reports adoption
  writes. Logs go to `DIR/out/` (one per step, `summary.tsv`). `--stand-in-sources` retries a to-year build that
  fails only on unarchived documents with their from-year editions, so the carry and the estimate are a lower bound
  for the forms that cite them. No model is called. A run takes hours on a loaded machine (each build of 2025 walks
  the interview); `--reuse-build` keeps an earlier copy's from-year build.

### Year-label lint

`check_label_year.py` (the light tier's `label_year`) finds a line's label, or a question's prompt or help, that
prints this year's amount of a dollar parameter the line reads (a question: the parameters of its input's line and of
the lines that read the input directly), when the next year's staged value
(`research/ty<year+1>/params-<year+1>.proposed.yaml`) differs and no operation of `changes/<year+1>/` rewrites that
text (`set` of `label`, `set_question` of `prompt` or `help`, `set` of `expr.source`, or a removal). Labels hold
literal text (no form renders a parameter into a label), so the fix is an operation printing the staged amount:
`changes/<year+1>/<form>.labels.yaml` holds those of lines no other operation relabels. A parameter staged with no
value (`value: null`, the prior-year `refund.*` amounts until the next year's Form 1040 instructions) is printed as a
note and checked once a value is staged, so the relabel goes in with the staging. A hit may instead be held in
`tools/label_year_baseline.json` with the reason the amount stays right; a held id no longer a hit fails.
`--self-test` (in check-all) plants each case.

## Process hooks

- **Fresh build** (`tools/build_fresh.py`): the completeness, screen, false-no and question checks and triage refuse to run when
  canonical/<year>/ is older than a model source of that year (the year's forms, tables, params and ambiguities, and
  the schema; another year's files do not count) or engine/dist older than engine/src (rebuild first).
- **Fresh rendered text** (`tools/build_fresh.py`, `require(rendered=True)` or `--rendered`): `npm run build` writes
  `canonical/` and not the tracked `rendered/` files; `npm run render` (and `node engine/dist/main.js render --ny`
  for New York) and check-all write those. Every tool that reads `rendered/` for a review refuses to run, dry
  runs included, unless the build is fresh and each rendered file is what the canonical data renders to: the render
  review and its planner (`render_compare.py`, `rerun_all.py` with render jobs), the log check (`check_logs.py`: a
  render log's subject is the hash of its rendered file), and the screen, false-no and question reviews and
  their checks (their prompts and subjects quote each line's rendered English). The comparison is by content
  (`node engine/dist/main.js render --check`, which renders in memory and writes nothing; about half a second for
  both jurisdictions), and the refusal names the files that differ and the command that regenerates them. The
  transcription review reads the form's YAML, class M builds the canonical data (when `build_fresh.py` finds it
  stale) and its jobs itself, and the
  completeness review reads `canonical/`; none of them reads `rendered/`.
- **Bug inventory and pending entries** (`tools/check_bug_inventory.py`, step `check_bug_inventory`; `--merge`
  from pre-commit). The rule a branch follows: a branch that runs alongside others does not write
  `BUG_INVENTORY.md`. It records each defect as a pending entry, `python3 tools/new_bug.py "Title" --pending
  [PREFIX] --field ...`, which writes `bug_pending/<PREFIX>-<NN>.md` (one entry, headed
  `## BUG-NEW-<PREFIX>-<NN> — <title>`; the prefix defaults to the branch's name, so two branches never
  choose the same file) and prints the placeholder, `BUG-NEW-<PREFIX>-<NN>`, which the branch cites
  wherever it would cite an id: other entries, commit messages, docs, code. A committed pending entry is
  never changed or deleted on the branch (a correction is another pending entry that cites it). Ids are
  given in the merge that brings the entries onto main, by whoever merges: `git merge --no-ff --no-commit
  <branch>`, then `python3 tools/new_bug.py --assign`, which appends every pending entry in the tree to the
  inventory in name order (numbers compared as numbers) with the next ids, rewrites each placeholder to its
  id in every tracked file, deletes the pending files and prints `BUG-NEW-<name> -> BUG-NNNN` per entry for
  the merge's commit message; then `git add -A`, a check-all run of that tree, and `git commit` (pre-commit
  refuses a tree no green run tested, and runs the merge check; `tools/commit_tested.sh` refuses a staged
  index, so it does not conclude a merge). Many findings at one landing go
  the same way: written as pending entries on the branch (one `--pending` call each, in the order they are
  to be numbered), numbered together by one `--assign`. A single session on main may still append directly
  with `new_bug.py` (no `--pending`).
  Placeholders in `docs/records/` (records kept verbatim) are neither checked nor rewritten by `--assign`.
  A fix proposed and not made (owner decision 2026-11-15) is labelled `- **Proposed fix:**`, with
  `- **Proposed fix lines:**` for the lines it would change; `- **Fix:**` means a fix that was made, and
  `tools/siblings.py --check` requires such an entry to have `- **Fix lines:**` and `- **Siblings checked:**`.
  What the checks hold: on every tree, the inventory extends HEAD's byte for byte with ids gapless from
  BUG-0001; every pending file is one well-formed entry under its own name; every pending file committed at
  HEAD is present and unchanged; every placeholder in a tracked file names a pending file. On a merge
  (pre-commit, which runs on a merge concluded with `git commit`, so a merge that assigns must be made with
  `--no-commit`): every parent's inventory is a prefix of the merge's, so no entry is rewritten, dropped or
  renumbered and no id is reused; what the merge appends after the longest parent's inventory is exactly
  what `--assign` appends for the parents' pending entries the merge removes; a pending file the merge
  keeps is a parent's, changed only by the rewriting of assigned placeholders. `tools/siblings.py --check`
  reads pending entries too, measured from the commit that added the file, and an assigned entry from the
  merge that assigned it. Its review-refresh test (a sibling form's review log changed) applies only to the
  entries the tree under test adds or changes over HEAD, measured from HEAD; a committed entry keeps the
  verdict of the commit that added it, so a later change to another form does not make its siblings due again.
- **Bug status** (`tools/bug_status.py`, step `bug_status`, docs tier). The inventory is append-only, so an
  entry's status is derived, never edited in: from its own fields (`Status`, `Disposition`, a fix field), then
  from later entries that close it (a `Closes:` field, or the title conventions older entries used, such as
  "BUG-x is fixed: ..."), with the rules in the tool's docstring. To close an entry, record a closure entry:
  `python3 tools/new_bug.py "Closure: BUG-x is fixed" --pending PREFIX --field "Closes=BUG-x"
  --field "Closure=fixed" --field "Evidence=..."` (`Closure` is `fixed`, `won't fix`, `superseded`,
  `duplicate`, `not a defect` or `disposed`; "in part" after the ids leaves the entry open; a `Reopens:` field
  reopens). `reports/bug_status.md` lists every open entry with the `TASKS.md` rows that cover it (a row naming
  the entry, or a task id named in the entry's status or fix), in two tables: covered by a row and covered by
  none. `--check` fails when a closure names no entry or an unknown kind, or when the report is not current;
  regenerate it with `--write` after changing the inventory, `bug_pending/` or the task registers. Assigning ids
  keeps it current, since the report lists pending entries last, in the order `--assign` numbers them.
- **Docs conventions** (`tools/check_docs_conventions.py`, docs tier): docs/ files are dated unless living, and
  HANDOFF-NEXT-SESSION.md keeps two entries.
- **Generated figures** (`tools/doc_figures.py`, step `doc_figures`, docs tier, in the last wave): the State figures of
  HANDOFF-NEXT-SESSION.md and the headline figures of README.md and docs/TRUST.md (bug inventory, task register,
  scoreboard, filer coverage, citations, `opaque` count, ambiguity register) are written between
  `<!-- figures:NAME -->` and `<!-- /figures:NAME -->` from the registers and reports that hold them; prose stays
  outside the markers. `--check` names each stale block; run the tool to rewrite them. The last release is the newest
  `r*` tag reachable from HEAD, so the first commit after a release refreshes the block. `--self-test`
  (`doc_figures_self_test`) plants a stale block, a missing marker and a release tagged after its commit.
- **Year-free ids** (`tools/check_year_ids.py`, step `year_ids`; spec 4.3): reads every document, line, parameter,
  enum and table id of the year's canonical build, both jurisdictions, and fails on an id that carries a year unless
  `tools/year_ids.json` lists it for that tax year. An id carries a year when it holds four digits from 1900 to 2099
  with no digit beside them (`died_2025`, `is2025`, `edu_a2026`, `born_before_2001`) or, for an id with no dot, ends
  in the two digits of the tax year or a year next to it (`clcw26`). Not a year, by rule: a number outside that range
  or of another length (Form 2441, Form 1040, an amount of 5000), four digits written as a reference after `f`, `form`,
  `line`, `section` or `pub` (`line2025`), and two digits in a dotted id (`line25`, `rate25`). A line id is examined
  after its document's id, so a document is listed once and its lines are not. Each listed id has its `kind` and its
  `class` (what the year means: `this_year`, `next_year`, `prior_year`, `offset`, `misnomer`), which the check
  compares with the build; a listed id that is gone or carries no year fails until its entry is removed, so the list
  only shrinks. A tax year with no list refuses every such id. An id the rules take for a year whose number is not
  one is recorded under `look_alikes` with what the number is. The list holds no replacement names. `--self-test`
  (`year_ids_self_test`) plants ids of each shape and the look-alikes.
- **Form claims** (`tools/claims.py`): two lanes never edit the same form at once. `tools/hooks/pre-commit` refuses a
  commit that changes a form another branch holds, or adds an input id while another branch holds `inputs`; a commit on
  a lane's branch claims what it changes, and `tools/hooks/post-commit` releases a branch's claims when it is merged.
  `tools/claims.py claim <form> --reason TEXT` claims before work starts; `list` shows the claims.
- **Twin lines** (`tools/check_twins.py`, check-all step `twins`, full tier: a release runs it, a commit does not): Form 8863 Part III is stated twice
  in the form data, for a person on the return (`person.edu*` in `person.yaml`) and for a dependent (`dependent.edu*` in
  `dependent.yaml`), because no line can range over both collections. The check pairs the two blocks by local id and
  compares each pair field by field (the form line: printed marker, label, type, `shown_when`, the whole expression with
  its operands and question wording, citation, refusals and their gates; the question bank entry; the test-data
  default), after normalizing only a reference to the side's own document and, for the Form 8863 lines that sum each
  block (`readers`), the collection summed. `reviews/<year>/twins.json` declares the blocks, the reader pairs, every
  field that differs on purpose (`differences`: pair, field, both sides' values or `{"pattern": REGEX}`, `null` for a
  field one side lacks, a reason and its source) and every id with no twin (`one_sided`, with reason and source). The
  check fails, naming the pair, the field and both texts, on an undeclared difference, on a declared difference that
  is gone or whose values changed, on an id without a twin that is not declared, and on a declared one-sided id that
  is gone or has gained a twin. So a change to a twin line is made on both sides in the same commit, or declared with
  its reason; a lane that edits one side claims both forms (`tools/claims.py claim person dependent`).
  `check_twins.py --sync-from person` (or `dependent`) shows, for each undeclared difference, the change that copies
  that side's field to the other, and `--write` makes it (`--pair NAME` limits it); it copies whole top-level fields
  as text, never a field that holds a declared difference, never a whole line or a test-data default, and writes
  nothing unless the result parses and differs from the data only in the copied fields. A new id matching the blocks'
  pattern is covered at once; a Part III line named outside the pattern (`local` in the file) is not seen.
  `tools/siblings.py` lists a line's twin among its fix-siblings from the same file. `--self-test` plants each kind of
  drift on a copy of the year's data.
- **Claude Code hooks** (`tools/claude_hooks/`): `bash_guard.py` refuses `pgrep -f` waits and hand copies into review data; `agents.py` refuses an agent
  launch without an explicit model or without `Class:`, `Year:` and `Jurisdiction:` in its brief (mechanical on Sonnet,
  judgment on Opus; Fable is allowed for either class), and writes and completes the run's row in the untracked pending file `<git common dir>/agent-runs/pending.jsonl`,
  from which `tools/agent_runs_fold.py` moves finished rows into `research/costs/agent_runs.jsonl` (under "Commit
  guard"). They are enabled per
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
| `extract_realty_tables.py` | Tables A-6 and A-7a of Pub. 946 (mid-month straight line, real property) into `tables/<year>/macrs_mm.yaml` (yearly; `--check` in check-all compares a fresh extraction and checks every month column totals 100%) |
| `extract_class_lives.py` | Pub. 946 Appendix B into `tables/<year>/class_lives.yaml` and its enum file (yearly) |
| `extract_eic_table.py` | The EIC Table (section above) |
| `extract_printed_tables.py --write` | The small printed tables of a year (section "Printed tables"; `--check` is in check-all) |
| `merge_classm.py BASE THEIRS OURS OUT` | Three-way merge of `fixtures/<year>/classm.json` by case id when integrating lanes (coverage expansion protocol 8.4); `--self-test` runs in the bookkeeping group |
| `propose_params.py` | A year's parameter values read from its archived documents at the places the prior year's citations name (section "Proposing a year's parameters") |
| `engines/ny_policyengine.py` | The New York differential against PolicyEngine-US, under the engines interpreter (`engines/setup.sh`) |
| `coverage/estimate.py` | The coverage estimate (spec 2.4), under the engines interpreter with the microdata `coverage/fetch_microdata.sh` downloads once |
| `coverage/roadmap.py` | `reports/roadmap.html` from the coverage estimate and the open rows of `TASKS.md` |
| `ny_fixtures.py` | Writes the New York fixtures from `ny_predict.py`'s predictions, for the year the predictor was transcribed for (section "New York years") |
| `new_bug.py`, `task_row.py` | Append a `BUG_INVENTORY.md` entry, record a pending one (`--pending`) or number the pending ones at a merge (`--assign`); add or update a `TASKS.md` row (tested by `test_bookkeeping_tools.py`) |
| `bug_status.py` | Each bug entry's status (open, fixed, closed by a later entry, a closure record) and the open entries' task rows; writes `reports/bug_status.md` (`--write`); check-all step `bug_status` (`--check`) (section "Bug inventory and pending entries") |
| `ocr_audit.py` | An image-grounded audit of the archived text layers (Tesseract), for a person to adjudicate; not a gate |
| `extraction/page_review.py` | Local HTML pages of each archived page beside the project's reading of it, for a person to judge |
| `transcription/question_review.py` | The question review (section "Sampled completeness, screen, false-no and question reviews"); also prices every question's prompt without a call (`--measure`) and lists which existing reviews judge each input's wording (`--coverage`) |
| `transcription/migrate_line_subjects.py` | Rewrites transcription logs' line-subject tables (`transcription/README.md`; tested by `test_review_tools.py`) |
| `transcription/migrate_screen_subjects.py` | Moves screen review records current on the form's question text to the subject with the interview's wording, with their rulings (section "Sampled completeness, screen, false-no and question reviews"; tested by `test_review_tools.py`) |
| `../ui/test_browser.mjs` | Browser smoke test of the web UI (the interview page and the vetting page), against a separately launched headless Chrome |
