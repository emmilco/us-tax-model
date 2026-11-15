# Lane O3a: Form 5695 becomes carryforward-only (C-CRED-01 to C-CRED-08)

Model claude-opus-5-5, judgment class; year 2026, jurisdiction us. Worktree `.claude/worktrees/ty26-o3a` on
`refs/scratch/ty26-w2` (ty26-base + R3 + P1R4 + R1). Not committed. check-all was not run, at the coordinator's
instruction.

## What changed

- `changes/2026/f5695.yaml` (new): 8 entries, 335 operations. A script (`/tmp/ty26-o3a-work/gen.py`) read every
  `from` value from `forms/2025/f5695.yaml`, `interview/2025/questions.yaml` and `ambiguities/2025.yaml`; only the
  `to` values were written by hand.
  - C-CRED-01: `set_form` title ("Form 5695 — Carryforward of Residential Energy Credit") and note.
  - Kinds: 217 `remove_line`, 69 `remove_question`, 36 `set`, 4 `remove_ambiguity`, 4 `set_ambiguity`, 2
    `set_form`, 2 `set_question`, 1 `add_line`.
  - C-CRED-02, -06, -07, -08: the removals (with `line13` in C-CRED-03 and `line13_positive` in C-CRED-05), each
    input's `remove_question`, and `remove_ambiguity` for
    `amb.2025.f5695_battery_second_home`, `_17abc_section_a`, `_category_cap` and `_section_b_residence`. That is
    all of Part I lines 1 to 11 and Part II, the opening question `f5695.any` with every kind-of-property question
    and gate, the QMID attestations, and the business-use, construction, joint-occupancy, separate-homes and condo
    questions.
  - C-CRED-03: the carryforward tail is renumbered with its ids kept. `line12` prints 1, `line15` prints 3 (reads
    `line12_if_carry` and `line14`), and `line16` prints 4 (line 1 less line 3). The 2025 line 13 is removed: line
    1 is now the only source. `part1_any` is kept because `s3.line5a` reads it; it is now a `copy` of
    `carry_if_prior`. The labels, prompts, help and cites of `carry`, `carry_if_prior` and `line12` move to 2025/2027.
  - C-CRED-04: `line14` prints 2. `rce_ws2` drops `s3.line5b` from its sum, and its note goes. Cites move to the
    2026 worksheet for line 2 (i5695 p. 2).
  - C-CRED-05: new `f5695.carry_positive` (line 1 > 0). `claiming_part1` (id kept for `s8812.clwb_complete`) now
    tests it in place of the removed `line13_positive`. Four `set_ambiguity` on `amb.2025.clwb_claiming_part1`:
    text, readings and reason re-read for lines 1/3, and the cite moved to p. 5. The chosen reading is unchanged.
- No `scope.f5695.yaml`. The change map's `scope.credits` no longer exists, and no scope line or interview scope
  text names Form 5695 or energy credits (checked by grep). The plan's split file has nothing to hold.
- `bug_pending/ty26-o3a-01.md` (BUG-0650), below.

## Decisions

- Removal, not zero lines: the 2026 form prints only lines 1 to 4.
- `f5695.line15`, `f5695.claiming_part1` and `f5695.part1_any` keep their ids (O3b's `s3.line5a`, `s8812.clwb_15`
  and `s8812.clwb_complete` read them).
- `claiming_part1` tests line 1 (the credit before the tax limit), as 2025 tested line 13. Testing line 3 would
  be circular: line 3 reads Credit Limit Worksheet B through the line 2 worksheet.
- The four `amb.2025.f5695_*` entries are removed rather than given an `unlinked` reason, because no 2026 line can
  raise them.

## Status of the check

- **Fails in this worktree alone.** The failures are of two kinds:
  - **Interview files (79 failures).** No operation kind can edit `interview/2025/full.yaml` (target
    `f5695.line32b`), `gate_frequencies.yaml` (`refs: f5695.any` in `home_energy`, `clean_energy_part1` and
    `home_improvement_part2`), `personas/10_homeowner_solar_heat_pump.yaml`, or 20 `l8b.energy_*` rows of
    `coverage/education_energy.yaml` (BUG-0650).
  - **Dangling reads (2 failures).** `s3.line5b` still reads `f5695.part2_any` and `f5695.line32`. These clear with
    O3b's `s3.yaml`, so O3b must merge before or with O3a.
- **With O3b's `s3.yaml` and `s8812.yaml` added (scratch `/tmp/ty26-o3a-scratch`).** 34 entries and 458 operations
  apply except for the 79 interview-file failures. With only f5695, s3 and s8812 in `changes/2026` and the
  interview files edited in the scratch copy (persona deleted, energy rows other than the two carryforward rows
  dropped, target dropped, gate-frequency refs changed), the result is "17 entries, 367 operations: all apply". All
  evidence quotes are printed on their pages.

## Scratch build

`year_changes.write(2025, changes_year=2026)` in the scratch copy touched 37 lines, removed 217, removed 4
register entries and changed 1. Every written file parses. `node engine/dist/main.js build` then failed only on:

- O3b's `i1062` cites not in the 2025 manifest (expected when built as 2025; patched in scratch);
- `group energy_power / energy_shell / energy_heating: no question names it`. The bank's `groups` list cannot be
  edited by operations (part of BUG-0650);
- 69 defaults of removed inputs in `fixtures/2025/defaults.json` (adoption's `fixtures_year.py` drops them).

I then made the three edits in the scratch copy as adoption would (the `i1062` manifest entry, the three empty
groups dropped, the 69 defaults dropped) and rebuilt. Result: "build OK". That run covered references, types,
cycles, guards, gates, interview stages 2 and 3, and canonical output. Not run on the scratch tree: test-fixtures,
render, and the property, mutation and classm suites.

## Shared files naming removed ids (not fixed; BUG-0644 class)

- `tools/coverage/tree.json` lines 269-282: `f5695.line7a`, `business_use`, `construction_later`,
  `joint_occupancy`, `separate_homes_joint`, `sec_a_new_home`, `sec_b_new_home`, and the seven `*_no_qmid` gates.
- `tools/engines/generate_cases.py` lines 71, 576-609, 852-859: 53 removed ids (Part I costs, every Part II input,
  `f5695.any`, `part2_any`, the QMIDs).
- `engine/src/generate.ts` lines 87-90, 125, 523-529, 578-580 (22 ids). `engine/src/mutate.ts` lines 2046-2049 (39
  ids, including `kinds_answered`, `part1_some` and `line13_positive`).
- `tools/engines/run_engines.py`, `ustaxes_adapter.py`, `ots_adapter.py` and `compare.py` read `f5695.line13`,
  `line30`, `line31` and `line32`.
- `fixtures/2025`: 695 cases mention a removed id (mostly classm 265, mutation 244, f5695 52, classm.deepseek
  112). This is a key-or-string match, so expected outputs are included. The 2026 fixture carry marks them "not
  evaluated".
- Parameters `f5695.rce_rate`, `eehi_rate`, `insulation_max`, the door, window and item maxima, `audit_max`,
  `annual_max` and `heat_pump_max` are read by nothing once this applies (C-CRED-09, lane P2).

## Waiting on unpublished documents

- **2026 i1040gi.** The joint-return cite (p. 13, Married Filing Jointly) in `f5695.carry`, `carry_if_prior`,
  `line12` and `line12_if_carry` stays the 2025 edition.
- **Finals of f5695, i5695 and i1040s8812.** All 8 entries are `verified: draft`.
- **Fact Sheet 2025-05** (named by the 2026 i5695) is not archived. It is a pointer only and encodes nothing.

## For other lanes

- **O3b.** Merge before O3a. Once this applies, nothing reads `s3.line5b`, so it may be removed or kept as the
  printed "Reserved" line.
- **Coordinator or owner.** Under BUG-0650, the check cannot pass with these removals until the
  interview files can be edited by an operation, or the rule is relaxed. Replacing the energy persona and coverage
  rows falls under the interview construction protocol.
- **Year literal outside scope.** `s3.prior_other_forms` (the gate of the carryforward question) still says "2024
  return"; adoption's literal list covers it.
