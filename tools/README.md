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

`compare` and `ny_compare` (`engine/src/compare.ts`) run the TypeScript and the Lean evaluator
over every fixture case and over generated whole returns, and fail on any line value that
differs. The generated returns come from the general generator (`engine/src/generate.ts`:
`sampleReturns`, and `nyReturnArbitrary` for `--ny`) and are the corpus of the `properties`
step: both commands take the returns, the seed and the size from one definition
(`corpusReturns`, `CORPUS_SEED`, `CORPUS_SIZE`), so they follow the declared inputs and their
branch coverage is the one `properties.md` lists. `PROPERTY_RUNS=<n>` sets the size for a run of
either command (400 without it; check-all sets none); each report states the seed and the number of
returns it used, so two reports written under different sizes say so themselves. The self-test
`compare --corpus-self-test` (`compare_corpus_self_test`) fails unless the returns the comparison
compares are the returns the properties report's coverage is of, for both jurisdictions, unless a
return with New York answers carries every answer of the federal return of its index, and unless both
commands follow `PROPERTY_RUNS`.

What each run covers. Both evaluators read the whole canonical build, so each run compares
the lines of every document, federal and New York. `compare` runs on the federal fixture cases
and the federal generated returns, none of which gives a New York answer: there most New York
lines are unknown (compared by kind only) and the rest have values that need no New York answer
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
pool, each failing test named. A step's output is printed when its wave ends, under its `== <step>` line.

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
`MUTATE_WORKERS=1` runs it on one.

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

## EIC Table

`python3 tools/extract_eic_table.py` reads the 2025 Earned Income Credit Table
(i1040gi pp. 49-60) from word boxes and writes `tables/2025/eic_0.yaml` to
`eic_3.yaml`, one table per number of qualifying children with valid SSNs. It
refuses to write unless the rows tile $1 to $68,700 in $50 steps and every
starred cell's footnote (read from the page text, matched by order) fits the row
and the column. `node engine/dist/main.js conjecture` checks every cell against
the credit formula built from Rev. Proc. 2024-40 section 3.06(1); see
`reports/2025/eic_table_conjecture.md`.

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
(`tools/release_reviews.sh`): it fails while any subject is due or short of `SAMPLES_PER_MILESTONE` samples.
`check_questions.py` lists due questions (a count on the console, the list in `reports/<year>/question_currency.md`)
and fails on unruled samples and orphans; its `--release` mode joins the release gate once the first full pass is
ruled (owner decision 2026-11-10). A question's subject is its line, interview wording and help, and its direct
readers' lines and English (`question_review.subject`); a screen's subject leaves out the help its prompt shows. A record marked `grandfathered` holds one review made before
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
{ "input": "household.married", "value": false, "reason": "...",
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
conditions and rules, less the open entries of cases it drops.

## Process hooks

- **Fresh build** (`tools/build_fresh.py`): the completeness, screen, false-no and question checks and triage refuse to run when
  canonical/ is older than a model source or engine/dist older than engine/src (rebuild first).
- **Fresh rendered text** (`tools/build_fresh.py`, `require(rendered=True)` or `--rendered`): `npm run build` writes
  `canonical/` and not the tracked `rendered/` files; `npm run render` (and `node engine/dist/main.js render --ny`
  for New York) and check-all write those. Every tool that reads `rendered/` for a review refuses to run, dry
  runs included, unless the build is fresh and each rendered file is what the canonical data renders to: the render
  review and its planner (`render_compare.py`, `rerun_all.py` with render jobs), the log check (`check_logs.py`: a
  render log's subject is the hash of its rendered file), and the screen, false-no and question reviews and
  their checks (their prompts and subjects quote each line's rendered English). The comparison is by content
  (`node engine/dist/main.js render --check`, which renders in memory and writes nothing; about half a second for
  both jurisdictions), and the refusal names the files that differ and the command that regenerates them. The
  transcription review reads the form's YAML, class M builds the canonical data and its jobs itself, and the
  completeness review reads `canonical/`; none of them reads `rendered/`.
- **Bug inventory in merges** (`tools/check_bug_inventory.py --merge`, from pre-commit): a merge may not create or
  renumber a BUG entry; colliding ids are renumbered in a commit on the branch before merging.
- **Docs conventions** (`tools/check_docs_conventions.py`, docs tier): docs/ files are dated unless living, and
  HANDOFF-NEXT-SESSION.md keeps two entries.
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
- **Twin lines** (`tools/check_twins.py`, check-all step `twins`, fast and full tiers): Form 8863 Part III is stated twice
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
  judgment on Opus; Fable is allowed for either class), and writes and completes the run's row in `research/costs/agent_runs.jsonl`. They are enabled per
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
| `extract_printed_tables.py --write` | The small printed tables of a year (section "Printed tables"; `--check` is in check-all) |
| `propose_params.py` | A year's parameter values read from its archived documents at the places the prior year's citations name (section "Proposing a year's parameters") |
| `engines/ny_policyengine.py` | The New York differential against PolicyEngine-US, under the engines interpreter (`engines/setup.sh`) |
| `coverage/estimate.py` | The coverage estimate (spec 2.4), under the engines interpreter with the microdata `coverage/fetch_microdata.sh` downloads once |
| `coverage/roadmap.py` | `reports/roadmap.html` from the coverage estimate and the open rows of `TASKS.md` |
| `ny_fixtures.py` | Writes the New York fixtures from `ny_predict.py`'s predictions |
| `new_bug.py`, `task_row.py` | Append a `BUG_INVENTORY.md` entry; add or update a `TASKS.md` row (tested by `test_bookkeeping_tools.py`) |
| `ocr_audit.py` | An image-grounded audit of the archived text layers (Tesseract), for a person to adjudicate; not a gate |
| `extraction/page_review.py` | Local HTML pages of each archived page beside the project's reading of it, for a person to judge |
| `transcription/question_review.py` | The question review (section "Sampled completeness, screen, false-no and question reviews"); also prices every question's prompt without a call (`--measure`) and lists which existing reviews judge each input's wording (`--coverage`) |
| `transcription/migrate_line_subjects.py` | Rewrites transcription logs' line-subject tables (`transcription/README.md`; tested by `test_review_tools.py`) |
| `human_review/test_browser.mjs`, `../ui/test_browser.mjs` | Browser smoke tests of the review packet and the web UI (the interview page and the vetting page), against a separately launched headless Chrome |
