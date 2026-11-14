# New York year handling: inventory, changes and a rehearsal (2026-11-14)

Charter section 7 item 5 ("New York gets the same year handling as federal") and the New York part of section 8
item 4. Measured on `main` at `460825d2`, then on this branch. Written by a judgment-class agent
(claude-opus-5-5). No paid call, no model call from code, no network. New York's 2026 forms are not published:
nothing was fetched, and the path to 2026 was rehearsed in a scratch copy outside the repository in which "2026" is
made of the 2025 documents (section 3).

**Labels.** [M] measured, with the command or file. [I] inferred from reading code, not run. [T] testimony from a
project document, not re-measured.

## 1. Inventory: where New York assumed 2025 or could not take `--year`

Lines are those of `460825d2`. "Probe" means the tool was run with `--jurisdiction ny --year 2026` in a scratch copy
of that commit, where New York has no 2026 data and the federal tree has the 2026 drafts catalog
(`tools/sources/2026.json`), so `taxyear.py` accepts the year.

### 1.1 The New York tools

| # | Where | What | Before [M: probe] | Now |
|---|---|---|---|---|
| Y1 | `tools/ny_predict.py:21`; amounts at 33-57, 112-117, 162-168, 194-197, 223, 249, 260, 271-272 | `NYDIR = sources/ny/2025`; every amount transcribed from the 2025 printing; no `--year` | `--self-test --year 2026` ran on 2025 data and passed: silently 2025 | takes `--year` (taxyear) and refuses `--jurisdiction us`; `predict()` exits for any year but `PRINTED` (2025), naming it; the self-test checks the `PRINTED` examples whatever the year |
| Y2 | `tools/ny_fixtures.py:30, 51, 86, 139, 287, 321, 396, 402` | output path, federal cases, `eval` without `--year`, canonical path, `tax_year`, and three notes naming 2024, 2025 and 2026 | silently 2025 [I] | paths, evaluation and `tax_year` by year; notes by `YEAR ± 1`; refuses a year the predictor was not transcribed for |
| Y3 | `tools/engines/ny_policyengine.py:33, 34, 48, 73, 76, 81, 90, 108` | fixtures and report paths, PolicyEngine periods, the evaluation year | silently 2025 [I] | by year; at 2025 the regenerated `reports/ny/2025/engine_differential.md` is byte-identical [M: run, `git status` clean] |
| Y4 | `tools/extract_ny_tax_table.py:180-182`, `:45` | titles, heading and quote fixed to 2025 ("$107,650"); limit fixed at $65,000 (paths were already by year) | traceback (`FileNotFoundError`, manifest) | heading, AGI-limit sentence and both "$65,000 or more" sentences read from the page's hashed text, each required once; refuses a year without New York data |
| Y5 | `tools/fetch_sources.py:239` | the New York catalog read unconditionally | traceback (`FileNotFoundError`, `tools/sources/ny/2026.json`) | refusal naming the missing catalog and the New York years |
| Y6 | `tools/check_extraction.py:326` | the manifest read unconditionally | traceback | refusal naming the missing archive |
| Y7 | `tools/archive_text.py:44` (read by `citations.py`, `year_diff.py`, `citations.py --relocate`) | the manifest read unconditionally | traceback in each of the three | refusal naming the missing `manifest.json` |
| Y8 | `tools/transcription/year_carry.py` (76, 98, 106, 114-118, 349, 362, 387, 415, 421, 434, 480) | federal paths only; no `--jurisdiction` | `unrecognized arguments: --jurisdiction ny` | carries New York's reviews, reading each tree across both jurisdictions (section 2) |
| Y9 | `tools/transcription/year_carry.py:183` | a table's "value" was the hash of its file, `tax_year:` and title included | every line reading a table needs a review at every rollover: 19 transcription, 19 render and 918 class M lines with identical documents [M: rehearsal 1]. Federal tables likewise | the hash of the table's data without title, citation and tax year; two self-test pairs |
| Y10 | `tools/year_diff.py:248-250` | only PDFs compared; a web page "not compared (no PDF text)" | 453 of the 778 New York citations (58%) cite a web page (`ny_it201i-html` 451, `ny_it201_tax_tables` 2) [M: `grep -rhoE "doc: [a-z0-9_-]+"` over `forms/ny`, `params/ny`, `tables/ny`, `ambiguities/ny`, `interview/ny`]: a change there never reached the worklist. The rate schedules, the worksheet amounts and the household tables cite the web edition | web pages compared on their derived text (one page). A planted change ($16,050 to $16,350 in the 2026 copy) put `ny.std_deduction` on the worklist twice, quote and probable value change [M] |
| Y11 | `tools/year_diff.py:512` | `--adopt` printed `reports/<to>/year_literals_…` for New York, which writes `reports/ny/<to>/` | wrong path in the message [M] | the path written |
| Y12 | `tools/jurisdiction.py`, `tools/taxyear.py` | `--year` checked against federal data only | any year with federal data was taken for New York | in New York mode a year needs `forms/ny/<year>/` or `tools/sources/ny/<year>.json` (`require_year`, on import after taxyear) |

### 1.2 Shared tools that work for New York or are year-neutral

| Tool | With `--jurisdiction ny` |
|---|---|
| `fetch_sources.py`, `check_extraction.py` | worked for 2025; now refuse a missing year clearly (Y5, Y6) |
| `citations.py --strict`, `--relocate` | works once the archive exists: 328 segments relocated, all in place; strict 0 findings, 381 input quotes matched [M: rehearsal] |
| `year_diff.py` and `--adopt` | worked for PDFs (owner decision C8 was done); web pages now compared (Y10) |
| `fixtures_year.py` | works: 337 cases kept, 0 re-recorded, 1 official example dropped (`ny.official.tax_table_38275`, listed under "Official examples to find for the new year"), 59 s [M] |
| `check_source_titles.py` | reads both catalogs whatever the flag; works [M] |
| `check_year_ids.py` | reads both jurisdictions' ids from the build; with no build for the year it reads 0 ids and passes (federal too) [M] |
| engine (`engine/src`) | year-clean for New York: every New York path goes through `nyPath`/`YEAR` [M: grep]; a year with no `forms/ny/<year>/` builds without New York, by design [I] |

### 1.3 Check-all

- The 16 New York mirrors were already declared once with `jstep` (commit `24b84f69`): 18 `jstep` lines now, each New
  York run the step `ny_<name>` with the run's year arguments [M: `grep -c "^jstep "`]. No step copied from a federal
  step remains. The New York-only steps are `ny_tax_table` and, new on this branch, `ny_household_tables`; the build
  step renders New York (`render --ny`). Nothing to parameterize further.
- At a year New York has no data for, every New York step now fails with the refusal of Y12 rather than a traceback.
  Whether such a year should skip the New York steps instead is an owner decision (section 5, D1).

### 1.4 Data and documents

| # | What | Measure |
|---|---|---|
| Y13 | Year literals in the New York tree after `--adopt` | 153 lines [M: `reports/ny/2026/year_literals_from_2025.json` in the rehearsal]: 82 references to the seven `amb.ny.2025.*` ids; 71 other lines: 32 in `ny_it201` labels, question sources and remedies ("for all of 2025", "your 2024 New York adjusted gross income"), 7 in the interview's question text and help, 5 in the register's prose, 2 table titles, and 25 comments (tables 20, forms 3, interview 2) |
| Y14 | `amb.ny.2025.*` ids | 7 ids, 487 references in the repository (forms, register, tools, 32 review files) [M: grep]. `check_year_ids.py` does not cover register ids |
| Y15 | The catalog's current-edition addresses | 4 of 34 entries of `tools/sources/ny/2025.json` have no year in their address (`ny_it201i-html`, `ny_st141`, `ny_st141i`, `ny_tax_law_601`); 30 are year-pinned (`/pdf/2025/inc/<form>_2025…`) [M]. Fetched before New York replaces them, they would archive the 2025 edition as 2026; the fetcher's draft flags are IRS-only and New York has no edition check |
| Y16 | Titles naming the year | `ny_it201i-html`'s title is "2025 Form IT-201-I, …", checked verbatim (`check_source_titles.py`) [M] |
| Y17 | Parameters | 217 values in `params/ny/2025.yaml`, all by hand [M]; the rate schedules, worksheet amounts, standard deductions, sales and use tax chart and school tax credit are tables of the web edition |
| Y18 | The statute | Tax Law § 601(d-4), the recapture regime the worksheets follow (`amb.ny.2025.recapture_selection`), is enacted for named taxable years [T: `sources/ny/2025/README.md`]; whether it holds for 2026 must be read again |
| Y19 | UI | `ui/index.html:7, 15, 21` and `ui/app.ts:303` say "2025 return" for both jurisdictions [M] |
| Y20 | `ny_fixtures.py` against the committed fixtures | at 2025 it writes 135 cases; the committed `it201.json` has 142 (7 added since: `ny.gate.*`, `ny.mut.*`), 9 refusal cases with a `line54` expectation it does not write, and every case's inputs relying on `defaults.json` where it writes them in full [M: run in a scratch copy, compared case by case]. It cannot regenerate the file; running it in the repository would discard those cases |

## 2. What now takes a year

Every New York tool takes `--year N` and resolves the default as the federal tools do (`taxyear.py`: the newest year
of `years.json`). `--jurisdiction ny` is taken by the shared tools; the New York-only tools (`ny_predict.py`,
`ny_fixtures.py`, `extract_ny_tax_table.py`, `extract_ny_household_tables.py`, `engines/ny_policyengine.py`) are in
New York mode without it and refuse `--jurisdiction us`. A year with no New York data is refused, naming what is
missing. `tools/README.md`, "New York years", is the reference.

`year_carry.py --jurisdiction ny` reads the old and new trees as the New York review tools do: both jurisdictions'
forms (a New York line names federal lines), both parameter files and table directories, each document's sources and
rendering in its own jurisdiction's directory, and New York's review indexes (`reviews/ny/<year>/`).

## 3. The rehearsal: 2025 adopted as if it were 2026

Scratch copy `/tmp/nyr/reh` (this branch, rsync without `.git` and the large untracked stores); `sources/2026` and
`sources/ny/2026` copies of the 2025 archives with `tax_year` 2026; both 2026 catalogs copies of the 2025 ones. The
2025 tree for the review carry: `/tmp/nyr/base` (`460825d2`). Scripts `/tmp/nyr/scripts/{setup_rehearsal,rehearse,
rehearse2}.sh`, logs `/tmp/nyr/out/reh1`, `reh2`. Each step in order, federal first where New York reads it:

| Step | Command | Result [M] |
|---|---|---|
| 1 | `fetch_sources.py --jurisdiction ny --year 2026` | 34 documents verified offline |
| 2 | `check_extraction.py --jurisdiction ny --year 2026` | 32 PDFs, 1 against HTML, 0 failing |
| 3 | `year_diff.py --from 2025 --to 2026 --adopt` (federal) | 39 s; 13 of 4,079 items on the worklist |
| 4 | `year_diff.py --jurisdiction ny --from 2025 --to 2026 --adopt` | 3 s; copies forms, tables, parameters, register and interview; relocation 328 segments, all in place; 153 year-literal lines (Y13); 0 of 705 items on the worklist (before Y10, the web pages unread) |
| 5 | `citations.py --strict --jurisdiction ny --year 2026` | 0 findings |
| 6 | `extract_ny_tax_table.py --check --year 2026` | **stops**: "expected one heading '2026 New York State Tax Table', found 0". Correct: the copied page prints 2025. On the real page it is the check that the page is the 2026 edition |
| 7 | `extract_ny_household_tables.py --check --year 2026` | **differs** from the adopted copies, which keep "sources/ny/2025/README.md" in their header; regenerating (without `--check`) writes the 2026 files. The data rows were equal |
| 8, 9 | `ny_predict.py`, `ny_fixtures.py --year 2026` | **refuse**: amounts known for 2025 only |
| 10 | `node engine/dist/main.js build --year 2026` | OK (223 s once the fixtures existed, walking the New York interview) |
| 11, 12 | `render --ny --year 2026`, `render --year 2026` | 12 and 68 files |
| 13 | `fixtures_year.py --from 2025 --to 2026` (federal) | **fails** after 118 s: `classm-jobs --year 2026` rejects `person[taxpayer].sc[biz_a].scveh[car_1].placed: invalid Enum(placed_year) input` (a federal defect: a carried vehicle's placed-in-service year is not in the 2026 enum) |
| 14 | `fixtures_year.py --jurisdiction ny --from 2025 --to 2026` | 337 kept, 0 re-recorded, 1 official example dropped; 59 s |
| 15 | `test-fixtures --ny --year 2026` | 337/337 pass |
| 16 | `year_carry.py --jurisdiction ny --year 2026 --from /tmp/nyr/base` | before Y9: transcription 154 carry / 19 review, render 348 / 19, class M 119 / 918, every review line "values changed" on a table. After Y9: see `reh2` below |
| 17 | `check_logs.py`, `check_year_ids.py --year 2026` | **refuse**: "stale build: canonical/ is older than ambiguities/ny/2026.yaml". `build_fresh.py` compares every year's canonical output with every year's sources, so adopting 2026 makes the 2025 build stale too; rebuilding 2025 clears it (federal as well) |
| 18 | `check_operands.py`, `check_consumers.py`, `check_limits.py --jurisdiction ny --year 2026` | **new findings** on unchanged documents: `--adopt` carries `reviews/<year>/citations.json` only, not the source-coverage rulings and baselines (`operands.json`, `consumers.json`, `limits.json`; federally also `instruction_cites.json`, `signs.json`) |

Second pass (`rehearse2.sh`, log `/tmp/nyr/out/reh2`), with Y9 and Y10 in place and both years rebuilt:

| Step | Command | Result [M] |
|---|---|---|
| 19 | `build --year 2026`, then `build` (2025) | both OK, 223 s and 203 s; the stale-build refusal of step 17 is gone |
| 20 | `year_carry.py --jurisdiction ny --year 2026 --from /tmp/nyr/base` | every compared line carries: transcription 173, render 367, class M 1,037; 0 to review |
| 21 | the same with `--write` | 18 indexes written; `review_store.py --jurisdiction ny check`: 18 indexes, 29 records, all present |
| 22 | `check_logs.py --jurisdiction ny --year 2026` | **fails**: for each of the 6 forms, transcription and render, "reviewed an earlier form … outside every compared line; rerun the whole review" (a document's own fields carry only where its cited source moved the year, which the copied documents do not, so this is an artefact of the rehearsal [I]); and 274 "ruling … is in the log but not in `<form>.rulings.json`": `year_carry.py --write` writes the indexes but not the rulings sidecars (federal too) |
| 23 | `citations.py --strict`, `check_instruction_cites.py`, `check_signs.py` | pass |
| 24 | `check_operands.py`, `check_consumers.py`, `check_limits.py` | new findings, as step 18 |
| 25 | `check_screens.py`, `check_false_no.py`, `check_questions.py`, `check_completeness.py` | pass, listing what is due at the next release |
| 26 | `test-fixtures --ny --year 2026` | 337/337 |
| 27 | `properties --ny --year 2026` | **crashes** on the federal defect of step 13 (`Enum(placed_year)` on a generated federal return) |
| 28 | `check_year_ids.py --year 2026` | fails on federal ids only (`scveh.s179_2025_ok` and others: `tools/year_ids.json` lists ids per year and has no 2026 list) |

Where the mechanical part stops, in order: the tax tables' heading (the page must be the new edition), the predictor
(its amounts are one printing, read by hand), the federal fixture carry and properties (steps 13, 27: a federal
defect New York inherits), the build freshness of the other year (step 17, cleared by rebuilding it), the
source-coverage rulings (steps 18, 24) and the rulings sidecars of carried reviews (step 22). Everything else New York
needs ran: archive checks, adoption, relocation, citations, fixtures carried and passing, every review line carried.

## 4. Tables

| Tables | How | Check |
|---|---|---|
| `ny_tax_table`, `ny_city_tax_table` | `extract_ny_tax_table.py`, from the tax-tables web page | `--check` (check-all `ny_tax_table`), with the rate-schedule conjecture |
| `ny_hh_state_t1`, `ny_hh_state_t2_p1` to `_p7`, `ny_hh_city_t4`, `ny_hh_city_t5_p1` to `_p7` (16) | `extract_ny_household_tables.py`, new, from the web edition of IT-201-I | `--check` (check-all `ny_household_tables`): all 16 byte-identical to the committed files [M] |
| `ny_hh_spouse_count` | by hand | none needed: it is the "one for your spouse if married filing joint return" rule by filing status, not a printed table of amounts, and does not change with the year |

So 18 of 19 New York tables are now made by a tool (2 before). The household tables were first transcribed by hand;
that the extractor reproduces them byte for byte is also a check of that transcription: no cell differs from the
archived page.

The parameters are not tables but most are read from tables of the same web edition (Y17). I read the 2025 rate
schedules (State and City, three status groups each), the worksheet recapture and incremental amounts (worksheets 2
to 5, 8 to 10, 13 to 15), the standard deductions, the sales and use tax chart and the school tax credit tables from
the archived page (`/tmp/nyr/scripts/dump_tables.py`) and compared them by eye with `params/ny/2025.yaml`: no
difference found. This was a reading, not a mechanical check.

## 5. Decisions taken here that the owner may want otherwise

- **D1. A year with federal data and no New York data fails the New York steps.** When 2026 is added to `years.json`
  before New York's 2026 forms are archived, every `ny_*` check-all step fails with the refusal of Y12, so the commit
  guard blocks until New York is adopted too. The alternative is to skip the New York steps visibly for such a year
  (a New York list of adopted years in `years.json`, or the absence of `tools/sources/ny/<year>.json`), letting the
  federal year be adopted alone. Not chosen here because it changes what is checked. Today the federal year cannot
  be adopted alone in any case: in a scratch tree with a federal 2026 and no New York 2026
  (`/tmp/nyr/scripts/fedonly.sh`), `build --year 2026` fails, "interview/2026/conflict_checks.yaml:
  ny_it201.gate.line79_over: not a refusal gate (no line's refuses names it)": the federal interview's conflict
  checks name a New York gate [M]. Either the two years are adopted together or that file must allow an absent New
  York tree.
- **D2. The predictor stays one printing.** `ny_predict.py` refuses every year but 2025 rather than holding amounts
  per year; a 2026 transcription can make its constants a per-year table when it is written.
- **D3. The household tables' headers are unchanged**, so the extractor reproduces them, including "transcribed from
  the web edition"; a header naming the extractor would differ from the committed files.
- **D4. `year_carry.py`'s table value excludes the table's title and citation**, not only its year: a moved citation
  of a table with equal data carries.
- **D5. `year_diff.py` compares web pages** for both jurisdictions; a federal year diff will list the federal web
  editions' citations too.

## 6. Not done, and what the day New York publishes its 2026 forms needs

Not done here: the federal fixture carry defect (steps 13, 27), year-scoped build freshness (step 17), carrying the
source-coverage rulings (step 18) and the rulings sidecars of carried reviews (step 22), year-free register ids and question text (Y13, Y14), a mechanical New York
parameter proposal (Y17: the federal parameter lane's tool should be pointed at the web edition's tables), a catalog
edition check (Y15), the UI title (Y19).

The day New York publishes (in order; the federal year should be adopted first, since New York reads its lines):

1. Write `tools/sources/ny/2026.json` from the 2025 catalog: move the year in the 30 year-pinned addresses and in the
   `ny_it201i-html` title; keep the four current-edition addresses but fetch them only once their pages show 2026
   (the IT-201-I web edition's "Updated" date, the tax-tables page's heading). Then `fetch_sources.py --jurisdiction
   ny --year 2026 --fetch` and `check_extraction.py --jurisdiction ny --year 2026`.
2. `year_diff.py --jurisdiction ny --from 2025 --to 2026 --adopt`; work the worklist (now including the web pages),
   the 153 year-literal lines and the relocation report until `citations.py --strict --jurisdiction ny --year 2026`
   passes. Read Tax Law § 601(d-4) again (Y18).
3. Regenerate the tables: `extract_ny_tax_table.py --year 2026` and `extract_ny_household_tables.py --year 2026`
   (both refuse a page that does not print what they expect). Re-read the 217 parameters from the web edition.
4. Transcribe the 2026 amounts into `ny_predict.py` (its `PRINTED` table) and check them against the 2026 tax-table
   examples; add the new class A example in place of the dropped `ny.official.tax_table_38275`.
5. `fixtures_year.py --jurisdiction ny --from 2025 --to 2026`, then `test-fixtures --ny --year 2026`.
6. Rebuild both years (`build_fresh.py`), carry the reviews (`year_carry.py --jurisdiction ny --year 2026 --from <the
   2025 tree> --write`, with its rulings sidecars once that is built) and review the rest; carry or re-rule the
   source-coverage rulings.
7. Then `tools/check_all.sh --year 2026` covers New York.
