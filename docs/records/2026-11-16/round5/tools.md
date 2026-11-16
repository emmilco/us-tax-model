# Round 5, lane D4-tools: T-337 (release_prep.sh) and T-338 (renames cover collection-indexed keys)

Lane D4-tools. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Proposals only; nothing applied
to xint.

## Summary

- **Patches.** `P/patches/v4/t337.patch` (7 files) and `P/patches/v4/t338.patch` (10 files). Each is one atomic
  unit. **Apply them in order: t337, then t338.** t338 is cut on top of t337: both touch `check_all_steps.sh`,
  `self_tests.py` and `README.md`, and t338 adds its step to `release_prep.sh`.
  - `git apply --check t337.patch` passes on xint as it stands (checked).
  - In a scratch copy of xint's files, t337 was applied, then `git apply --check t338.patch`, then t338. The result
    matches the b/ copies byte for byte (checked: `scratch/round5-D4-tools/check/seq`).
- **T-337.** The new `tools/release_prep.sh` takes no command from anywhere but `check_all_steps.sh`. It gets
  them from a new `--print-steps` mode of that script. In that mode the real `step`/`jstep` declarations print
  `name<TAB>command` (quoted with `%q`) and run nothing. So the two scripts cannot drift. If a listed step is not
  declared, release_prep stops with exit 2.
  - `release_reviews.sh` now runs all six sampled-review checks and lists each failure. A build failure exits 2.
  - release_prep prints each step's time and ends with one `release-prep: PASS` or `release-prep: FAIL: ...` line.
  - It has a stub-based self-test, `tools/test_release_prep.sh`.
- **T-338.** The new `tools/rename_ids.py` (`apply` / `check`) is the committed rename step. It renames and finds
  an old id in three forms: the whole id; the collection-indexed form, alone or nested
  (`person[taxpayer].f8853c[c].pre1996`); and a renamed document's name. It works in these places:
  - fixtures, defaults included;
  - coverage rows;
  - personas;
  - the triage witnesses of the rulings sidecars.

  `rename_carry.py` now uses the same substitution. Its old one missed collection keys nested in a path.
  `check` runs as a new check-all step for both jurisdictions (`renamed_ids`, `ny_renamed_ids`) and as a
  release_prep step. A unit test was added (`tools/test_rename_ids.py`).
- **Landing condition for T-338 (checked against xint data).** On xint now, `check` with the standing map finds
  **26 old ids**, all in triage witnesses of default-family rulings sidecars:
  - `clcw_next_year.rulings.json`: 13, all instance `@clcw26`;
  - `f8962.rulings.json`: 4;
  - `rec.rulings.json`: 4;
  - `refund.rulings.json`: 5.

  It finds none in fixtures, coverage rows or personas, in either jurisdiction. The landing commit must therefore
  include the output of a one-time `python3 tools/rename_ids.py apply` (and `--jurisdiction ny`, which changes
  nothing). Otherwise the new step fails.
- **Nothing was run** but `bash -n`, shellcheck, Python `ast.parse`, two read-only `--print-steps` listings, an
  in-memory exercise of the substitution functions, and a read-only `check` scan of xint. Neither self-test has
  been run (round rules: no test suites).

---

## T-337: `tools/release_prep.sh`

### Hunks

| File | Change |
|---|---|
| `tools/check_all_steps.sh` | New `--print-steps`. It is parsed with `--tier`, and is documented in the header. In print mode: no `: > check-all-times`, no `mktemp`, no `finish` trap, and `times=/dev/null`, so a printed `self_tests.py --times` writes nowhere. `step()` is redefined after the function definitions to print `name\t %q...`, or `name\tskip\t<reason>` for a New York step the year skips. `wave()` becomes a no-op. The two New York skip messages are suppressed. Run mode is unchanged. |
| `tools/release_reviews.sh` | Compile, build and render first: a failure prints a message and exits 2. Then all six checks run (`check_completeness`, `check_screens`, `check_false_no`; us and ny), each under `== <check> (<n> s)[: FAILED (exit k)]`. Afterwards: exit 1 with the list of failed checks, or `release reviews: complete`. `release.sh` only tests for nonzero, so it is unaffected. It now reports every due item instead of stopping at the first. |
| `tools/release_prep.sh` (new) | `[--fail-fast]`; any other argument exits 2. Takes a check-all slot (`check_slot.py --tier release-prep`), like check_all.sh. Reads `check_all_steps.sh --print-steps --tier full` and refuses (exit 2) a `PREP_STEPS` name not declared. Runs `release_reviews.sh` first; its exit 2 (no build) ends the run. Then runs each `PREP_STEPS` command in sequence, cheapest first by the recorded check-all times, with `eval` in a subshell. Logs go to `$(git rev-parse --git-path release-prep)/<step>.log`. A step that passes is then checked with `tools/step_output.py --logs`, as check-all's `wave` does. A failing step's log is printed. The run ends with a per-step table (PASS/FAIL/SKIP, seconds) and `release-prep: PASS` (0) or `release-prep: FAIL: <steps>` (1). |
| `tools/test_release_prep.sh` (new) | Temporary repository with the real release_prep, release_reviews, check_all_steps, step_output, taxyear and jurisdiction. Every other `tools/` path those scripts name, plus `node` and `npm`, is one stub that logs its call and fails when `FAIL` names part of it. Seven cases follow this table. |
| `tools/self_tests.py` | Row `release_prep_self_test` (code group). |
| `tools/release.sh` | Header: release_prep.sh is the recommended first step. |
| `tools/README.md` | New paragraph after the release.sh paragraph (Commit guard section). |

Cases in `test_release_prep.sh`:

1. All pass. Every expected call is made with its declared command, and none of mutate, interview-length,
   evidence, review packets, engines, integration, compare, properties, twins or interview-coverage runs.
   23 PASS lines appear, the steps run after the reviews, and check-all's times file is untouched.
2. Failures are collected. A review check and `ny_limits` fail, yet later review checks and later steps still run,
   and the summary names both.
3. `--fail-fast` stops at the first failure.
4. A failed compile stops the run before any check.
5. `NO_TIER_LINE` makes `bookkeeping_self_tests` fail through `step_output.py`.
6. With `ny_adopted: []`, New York steps show as SKIP.
7. Drift: removing `jstep limits` from the steps script gives exit 2, with nothing run.

### `PREP_STEPS` (order)

`check_bug_inventory bug_status check_agent_runs doc_figures limits ny_limits consumers ny_consumers year_changes
ny_year_changes citations ny_citations check_extraction ny_check_extraction check_logs ny_check_logs
bookkeeping_self_tests ny_test_fixtures test_fixtures coverage interview_rules self_tests`

T-338 adds `renamed_ids ny_renamed_ids` after `ny_consumers`.

Mapping from the brief: "check_limits" is the jstep `limits`, "check_consumers" is the jstep `consumers`,
"test-fixtures us and --ny" is `test_fixtures`/`ny_test_fixtures`, "citations --strict" is the jstep `citations`
(both jurisdictions). All are checked in the printed listing (see Verification).

### Design decisions (each is a choice the coordinator may reverse)

1. **"Source or parse": a print mode, not a parser.** Sourcing `check_all_steps.sh` would run it, and a parser
   would have to re-implement `jstep`, `"${node[@]}"`, `"$@"` and the New York skip. The print mode reuses the
   script's own `step`/`jstep`/`in_tier`/`ny_skip`. Steps whose command is a function of the script
   (`build_and_render`, `lean_build`, `review_packets`) print by name and are not in `PREP_STEPS`.
2. **Run every step, `--fail-fast` optional.** The brief asks for one PASS/FAIL summary and for every due item to
   be collected. The draft TASKS row in `coordinator/protocol-8.10-additions.md:50-53` says "stops at the first
   failure". I chose run-all as the default because the whole selection takes minutes and one run then shows
   every defect. **The TASKS row text should be changed** to "runs every step (or stops at the first failure
   with --fail-fast), printing each step's time and one PASS or FAIL".
3. **"Quick self-tests" means both `bookkeeping_self_tests` and `self_tests` (code group).** The code group takes
   115 to 275 s in recorded parallel check-all runs: the `.git/worktrees/agent-*/check-all-times` files, read for
   this lane. Four of five broken self-tests surfaced on 2026-11-16 (`morning-report-notes.md:22`). If "quick"
   meant only the bookkeeping group, delete `self_tests` from `PREP_STEPS`. That is a one-word change, and the
   self-test count changes from 23 to 22.
4. **Sequential, cheapest first, not parallel.** This gives clean per-step times and leaves the CPU to whatever
   else holds a slot. Inferred cost: 10 to 15 min end to end. That is the sum of the recorded parallel step times
   (about 1,000 to 1,300 s, inflated by contention) plus the release-reviews build.
5. **No `--year`.** A release is the default year, and `release_reviews.sh` builds only the default year.
6. **Reports.** release_prep regenerates none of its own. `coverage` rewrites `reports/<year>/coverage.md` as it
   does in check-all (`engine/src/fixtures.ts` `coverageReport`, which writes `reportPath("coverage.md")`;
   checked). `doc_figures --check` then checks against the committed reports, since evidence, mutation and the
   engine differential are rewritten only by later waves. A figure that changes only after those waves is not
   caught here. The README says a pass is not a promise about the full check.

### Check tier and verification

- **Tier: fast.** None of the paths is in `tools/full_paths.txt` (checked), and `tools/*.sh` are not docs paths.
- Before landing, run:
  1. `bash tools/test_release_prep.sh`, which must end `release-prep self-test OK`;
  2. `python3 tools/step_output.py --self-test`;
  3. `bash tools/test_check_all_ny_skip.sh`, since the print mode touches the same script;
  4. `python3 tools/tier_paths.py --self-test`;
  5. then the fast-tier check-all.
- Smoke test on a real tree: `tools/release_prep.sh --fail-fast` in a worktree with cloned review data.
- **Already verified.**
  - `bash -n` on all four scripts and `shellcheck -S warning` on the three new or rewritten ones: clean.
  - `check_all_steps.sh --print-steps --tier full` (b/ copy, run read-only) printed 81 steps.
  - The commands match the brief, for example `limits\t python3 tools/check_limits.py`,
    `ny_test_fixtures\t node engine/dist/main.js test-fixtures --ny` and
    `self_tests\t python3 tools/self_tests.py --group code --times /dev/null`.
  - `interview_length` is absent without `CHECK_ALL_RELEASE`.
  - `.git/check-all-times` was unchanged (same size and mtime before and after).
- **Unverified.** The self-test has not been run. These assumptions are inferred and the self-test would show
  them:
  - bash exports a variable assigned in a function call's prefix to that function's children
    (`FAIL=... run ...`);
  - `jurisdiction.py` accepts `ny_adopted: []` (from reading `jurisdiction.py:89-108`).
- **Reviews it makes due: none.** No form content is touched.

---

## T-338: renames cover collection-indexed keys

### What was found (checked)

- No committed tool applies a rename to the data. `rename_carry.py` carries review verdicts and rewrites no
  fixture, row or persona; it rewrites only class M case ids when a document moves
  (`tools/transcription/rename_carry.py:943-950`).
- The only rename-apply script is the working record `docs/provisional/lanes/rename_work/rename.py`. It does cover
  `doc[key].local` (lines 30-31). The tool that made the 9 renames of 2026-11-16 (`/tmp/xint/rename_map.json`)
  is not recorded. The `].` exclusion named in `protocol-8.10-additions.md:39-42` came from that unrecorded step.
- `rename_carry.substituter` had a real gap of its own. Its collection pattern `(?<![A-Za-z0-9_.])(ID+)(\[..\])\.(ID+)`
  consumes `person[taxpayer].f8853c` first, so a collection key nested in a path (as coverage rows and personas
  write them, e.g. `interview/2025/coverage/hsa.yaml:10`) was never put back in its scratch tree. Inferred
  consequence: such units would be refused as "not current at the old names".
- The places hold these forms: fixture keys and refusal gates (`fixtures/2025/f8853c.json:384,389`,
  `classm.json:116156`), defaults (`fixtures/<year>/defaults.json`, field `input`), coverage rows and personas
  (`person[taxpayer].<doc>[<entry>].<local>`), and the rulings sidecars' triage witnesses
  (`partial:<case>-<doc>[<e>].<local>@<instance>`, `reviews/2025/transcription/f8853c.rulings.json:150-161`).
- Triage stamps are not validated by any check (`rulings.py:325-335`, `rulings.check`). They are compared only by
  `carry.py:536-550`, which matches a ruling to the current triage stamp. So an old name in a witness does not
  fail a check, but it stops a mechanical carry of that ruling. Renaming the witnesses restores the match.

### Hunks

| File | Change |
|---|---|
| `tools/rename_ids.py` (new) | `load_map` reads `year_free_names.json` (with document entries) or rename_carry's two shapes. `substituter(mapping, documents)` renames, in this order: (1) per-document collection patterns `LEAD doc [entry] . local (?!ID)`, where LEAD is `(?<=\]\.)` or `(?<![A-Za-z0-9_.])`, so a path step matches and a dotted id does not; only renames that keep the document are rewritten; (2) the whole id, with rename_carry's existing boundaries; (3) document names. `finder` reports all three, including cross-document collection forms, which `apply` cannot rewrite. `places()` lists fixtures `**/*.json`, `interview/<year>/{coverage,personas}/**/*.y*ml`, and default-family `reviews/<year>/{transcription,render,classm}/*.rulings.json`, through `jurisdiction.ypath`/`interview_dir`. In fixtures, lines of `id`, `description` and `evidence_note` are skipped (rename.py's rule). In rulings, only the witness input and instance parts are touched, never case ids or ruling texts, and by exact JSON-string replacement so the format is preserved. `apply [FILE...]` also rewrites whole files given. `check` exits 1 listing file and line (or ruling and witness) and the old ids. |
| `tools/test_rename_ids.py` (new) | unittest. Forms: whole; collection; the 2026-11-16 case (`f8853c[p0].pre1996` and its `_if_reimbursed` gate); `[*]`/`[]`; path step; dotted-id and other-document negatives; document names; cross-document reported but not rewritten; finder after sub is empty; witness rewrite keeps the case id. `load_map` in three shapes. Temporary tree: check lists exactly the 5 files; apply changes 5; check is then empty; skipped fixture fields, ruling text, second-family sidecar, forms file and the New York fixture are untouched; a second apply changes nothing. New York, FILE args and a moved document are also tested. `main()` prints `rename ids self-test: ok (N tests)`. |
| `tools/transcription/rename_carry.py` | `substituter` delegates to `rename_ids.substituter`, so the carry's put-back and the rename use one substitution. Docstrings name the path-step form. The scratch tree is a copy of `tools/`, so `rename_ids.py` is present there (`test_rename_carry.py:97` copies all of `tools/`). |
| `tools/transcription/test_rename_carry.py` | One added expectation: `p[q].x[k].a_2025` becomes `p[q].x[k].a_now`, and `y.x[k].a_2025` is unchanged. The existing expectation still holds (checked in memory). |
| `tools/check_all_steps.sh` | Wave 1, after `year_ids`: `jstep renamed_ids "--jurisdiction ny" python3 tools/rename_ids.py check`. |
| `tools/self_tests.py` | Row `rename_ids_self_test` (code group). |
| `tools/tier_paths.py` | `WALKERS` entry for `rename_ids.py`'s `.rglob(`, which `WALK_RE` flags. |
| `tools/release_prep.sh`, `tools/test_release_prep.sh` | `renamed_ids ny_renamed_ids` added to `PREP_STEPS`. Self-test: expected call `tools/rename_ids.py check --jurisdiction ny`, and the PASS count goes from 23 to 25. |
| `tools/README.md` | New subsection "Renaming the ids in the data, and checking that none is left" under the rename-carry section, with the order of a rename. `renamed_ids` added to the release_prep paragraph. |

### Landing (data migration in the same commit)

1. Apply t338 after t337.
2. Run `python3 tools/rename_ids.py apply` and `python3 tools/rename_ids.py apply --jurisdiction ny`.
   - Expected: 4 files change, 26 witness strings in total. `clcw_next_year.rulings.json`: 13, all `@clcw26` to
     `@clcw_next_year`. `f8962.rulings.json`: 4 `f8962.married_in_2025`. `rec.rulings.json`: 4 `rec.not_2024`.
     `refund.rulings.json`: 5 (`refund.not_2024`, `refund.line17_2024`). New York: 0. These counts come from a
     read-only scan of xint with this code (`scratch/round5-D4-tools/drive_check.py`).
   - xint is still moving; rerun `check` first and expect the same list or a subset.
3. Run `python3 tools/rename_ids.py check` and the same with `--jurisdiction ny`. Both should print
   `no old id left`.
4. Commit the tool together with the 4 sidecars.
   - Inferred: no review falls due. Sidecar triage stamps are not part of any subject.
   - Unverified: whether `tools/claims.py` wants claims for the forms whose sidecars change (clcw_next_year, f8962,
     rec, refund).

### Check tier and verification

- **Tier: fast.** No `full_paths.txt` path, and the sidecar changes are not docs paths.
- Before landing, run:
  1. `python3 tools/test_rename_ids.py`;
  2. `python3 tools/transcription/test_rename_carry.py`, which is a few minutes and builds a small tree;
  3. `python3 tools/tier_paths.py --self-test`;
  4. `bash tools/test_release_prep.sh`;
  5. `bash tools/test_check_all_ny_skip.sh`, which picks up `tools/rename_ids.py` as a stub automatically;
  6. the landing steps above, then the fast-tier check-all.
- **Already verified.**
  - `ast.parse` on all Python files, and `bash -n` and shellcheck on the scripts.
  - `--print-steps` lists `renamed_ids\t python3 tools/rename_ids.py check` and its ny twin.
  - Every substitution and finder expectation of `test_rename_ids.Forms`, and the rename_carry test's old and new
    expectations, give the asserted strings when run in memory against the b/ code.
  - The read-only check on xint is as above.
- **Unverified.** The `Tree` cases of the unit test, because they write a temporary tree, and the full
  `test_rename_carry.py`.
- **Not covered, by design.**
  - Ruling texts and keys (`printed` keeps old ids, e.g. `asset.rulings.json`). These are the reviewer's record,
    and rename_carry re-keys what it proves.
  - Second-family sidecars, which are historical.
  - Case ids, which are labels.
  - Prose in fixtures (`description`, `evidence_note`).
  - Collection-indexed renames that move a document: `check` reports them and they must be renamed by hand.
  - `apply` does not rename `forms/`, the bank or code unless they are passed as FILE. The README gives the order
    of a whole rename.
- **Reviews it makes due: none** (inferred).

## Open questions for the coordinator

1. **Run-all or stop-at-first-failure as the default** (T-337 decision 2). The draft TASKS row says
   stop-at-first; this draft runs everything and offers `--fail-fast`. Which should the TASKS row and the script
   say?
2. **What "quick self-tests" means** (T-337 decision 3). Both groups (this draft), or only
   `bookkeeping_self_tests`? The second drops about 2 to 4 min from the run.
3. **Land T-338's one-time witness migration in the same commit?** The 4 sidecars and 26 witnesses above are
   names only. If not, the new `renamed_ids` step must stay out of `check_all_steps.sh` until it is done.
