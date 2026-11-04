# New York: integration notes for the owner's machine (Phase 4)

Written at the end of Phase 3 (`docs/ny/2026-11-04_ny_cloud_brief.md`, steps 1 to 8) on branch `ny/2025-foundation`.
What the cloud session built, what it changed in shared code (with the evidence that federal results are unchanged),
what it could not run here, and what the owner's machine must run before this branch is integrated.

## What exists

| Path | What |
| --- | --- |
| `sources/ny/2025/` | the New York archive (Phase 1) |
| `params/ny/2025.yaml` | New York parameters (`ny.*`) |
| `tables/ny/2025/` | the State and City Tax Tables (extracted, `tools/extract_ny_tax_table.py --check`), the household credit tables |
| `forms/ny/2025/` | `ny_it201` (Form IT-201), `ny_it2` (one record per W-2), `ny_rs`, `ny_city_rs` (rate schedules), `ny_tcw`, `ny_tcw_first` (the tax computation worksheets) |
| `ambiguities/ny/2025.yaml` | New York readings (`amb.ny.2025.*`) |
| `interview/ny/` | the New York question bank and profile (`--profile ny`) |
| `fixtures/ny/2025/` | New York fixtures (`test-fixtures --ny`) |
| `reviews/ny/2025/`, `reports/ny/2025/` | rulings and reports of the checks in New York mode |
| `research/audits/ny/2025-phase3-review.md` | the in-session independent review (step 7) |

## Shared code changed, and the federal evidence

Every change keeps federal results as they were; each step's commit says so with its evidence.

- `engine/src/build.ts`, `canonical.ts`, `year.ts`: the build reads the New York tree and writes New York files of
  its own (`ny_*.json`, `tables/ny_*.json`, `params-ny.json`, `register-ny.json`, `interview-ny.json`); the loaders
  merge them. Evidence: after every step, `diff -r` of `canonical/2025/` against the branch's starting point, excluding
  only those New York files, is empty.
- `engine/src/interview.ts`, `interview-check.ts`: the `ny` profile; the New York fixtures' interview paths are
  walked at build. Federal profiles: `interview*.json` byte-identical ("all" in a profile still means the federal bank).
- `engine/src/fixtures.ts`, `mutate.ts`, `compare.ts`: `--ny` selects the New York fixtures and writes to
  `reports/ny/2025/`; without it they read exactly the federal fixtures and write the federal reports.
- `lean/Main.lean`: merges `params-ny.json` into the parameters. **Untested here** (no Lean toolchain could be
  installed: GitHub is not reachable from this environment). Run `lake build` and `node engine/dist/main.js compare`.
- `tools/jurisdiction.py` (new), `tools/citations.py`, `baseline_check.py`, the five source-coverage checks,
  `year_diff.py`, `fixtures_year.py`: `--jurisdiction ny`. Federal reports unchanged (`git status reports/2025` clean
  after running each in federal mode).
- `tools/fetch_sources.py`, `tools/check_extraction.py`: `--jurisdiction ny` (Phase 1).

## To run on the owner's machine

1. `npm ci && npm run compile && node engine/dist/main.js build` (the build walks the New York interview over every
   New York fixture as well as the federal paths; expect it to take longer).
2. `node engine/dist/main.js test-fixtures` (federal, must stay 1637/1637) and `node engine/dist/main.js test-fixtures --ny`.
3. Lean: `cd lean && lake build`, then `node engine/dist/main.js compare` and `node engine/dist/main.js compare --ny`
   (the `lean/Main.lean` change that merges `params-ny.json` is untested; this environment could not install Lean).
4. `tools/check_all.sh`. It was not run here: it needs data not in the repository and the macOS PDFKit reader. The
   New York checks are not yet steps of it; add them (or run them by hand):
   - `python3 tools/fetch_sources.py --jurisdiction ny` (archive verifies offline);
   - `python3 tools/check_extraction.py --jurisdiction ny` (with PDFKit on macOS);
   - `python3 tools/citations.py --strict --jurisdiction ny`;
   - the five source-coverage checks with `--jurisdiction ny` (17 findings, all ruled in `reviews/ny/2025/`);
   - `python3 tools/extract_ny_tax_table.py --check`;
   - `python3 tools/ny_predict.py --self-test`;
   - `node engine/dist/main.js mutate --ny`.
5. The project's review tools (paid model calls; not run in the cloud by the brief) on the New York documents
   `ny_it201`, `ny_it2`, `ny_rs`, `ny_city_rs`, `ny_tcw`, `ny_tcw_first`: transcription, render comparison, class M,
   the completeness review and the screen review. The review tools read `sources/<year>/` and the federal input
   contracts; they need the same `--jurisdiction ny` treatment (the source pages are in `sources/ny/2025/`), which
   was not built here.
6. `tools/year_diff.py` and `tools/fixtures_year.py` with `--jurisdiction ny` at the 2026 adoption (Phase 5).

## Open items

- **Recapture worksheet selection.** PolicyEngine-US selects the recapture of the tax table benefit by New York AGI
  alone; IT-201-I's worksheets also test taxable income ("your taxable income (line 38) is $215,400 or less" for
  worksheet 7). Where New York AGI is above a worksheet's taxable-income limit and taxable income is not, the two differ
  by up to a few hundred dollars (`reports/ny/2025/engine_differential.md`, the cases at $215,400 and $161,550 of
  taxable income). The encoding follows the printed instructions. Tax Law § 601(d) is not archived; reading it would
  settle whether the instructions' conditions match the statute.
- **Line 25** (`amb.ny.2025.line25`, decision B1): revisit with the 2026 instructions.
- **Married filing separately**: the federal encoding refuses it (line 37), so the New York profile refuses it too;
  the New York lines compute it (fixtures `ny.status.mfs.*`), the household credit tables 3 and 6 are refused.
- **Household credit columns 3 to 7** are reachable only with two or more dependents who are not qualifying children
  for the earned income credit (fixtures `ny.household.hoh.parents*`); with a qualifying child, the earned income
  credit screen (decision B9) refuses first.
- **Lows of the in-session review** (`research/audits/ny/2025-phase3-review.md`) are listed, not fixed.
- **The federal W-2 entries and the New York W-2 records** are keyed alike by convention only; nothing checks that
  every federal W-2 has a New York record (IT-2 requires one per W-2).
- `forms/ny/2025/*.yaml` were generated from a script kept out of the repository; edit the YAML directly.
