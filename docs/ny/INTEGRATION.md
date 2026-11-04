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

(Completed at step 8.)
