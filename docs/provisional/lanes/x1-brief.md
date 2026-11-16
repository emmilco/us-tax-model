# Brief shared by the coverage-expansion wave X1 lanes (Schedule E, Form 1116, digital assets)

Model: claude-opus-5-5. Class: judgment (source reading, encoding, interview design). Year: 2025 (plus the 2026
carry the protocol requires). Jurisdiction: us (New York only where the scout design names an NY ripple).

You are one lane of wave X1 of federal coverage expansion in the tax-formalization project. Your lane id, area and
worktree are in your launch message. Two documents govern your work, both in your worktree under
`docs/provisional/lanes/`:
- `coverage_expansion_protocol.md` — the coverage expansion protocol (draft adopted by the coordinator; owner
  decisions: areas are taken in order of marginal gain, and married filing separately follows this wave). Follow it
  phase by phase (§1 to §10); its definition of done (§10) is your exit, except the paid reviews (below).
- `scout-<area>.md` — the design scout for your area: scope (computed / still refused / gates that narrow), sources,
  encoding plan, interview plan, fixtures. Every "owner decision Dn" in it is settled **as the scout recommends**
  (the owner delegated these to the coordinator); record each in `docs/provisional/DECISIONS.md` (append a section for
  your lane). Treat the scout's claims as testimony: verify against the archived sources and the tree before building
  on them ([V] marks are the scout's own checks, still testimony).

Also normative: project `CLAUDE.md`, and `docs/2026-11-13_interview_construction_protocol.md` for every question.

## Where you work
- Only in your worktree `/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/<lane>`, a detached
  snapshot (`refs/scratch/x1-base`) of the goal-1 integration in progress (12 of 18 fix lanes merged; the rest
  merge in parallel with you, touching other forms). Review data is already cloned. Never cd elsewhere.
- Build first: `npm run compile --silent && node engine/dist/main.js build && node engine/dist/main.js render &&
  node engine/dist/main.js render --ny`.
- Do not commit; do not run `tools/claims.py`; **do not run `tools/check_all.sh`**. Deliverable: your working-tree
  diff plus a report. Verify with targeted checks: `test-fixtures` (+ `--ny`), `interview-rules`, `tick-groups`,
  `interview-coverage --rows <your files>` (and the rows of files you touched), `citations.py --strict`,
  `check_consumers.py`, `check_questions.py`, `check_screens.py`, `check_false_no.py`, `siblings.py --check`,
  `check_bug_inventory.py`, `year_changes.py --check`, self-tests of tools you change, and `mutate` once at the end
  (the machine is quiet now; `MUTATE_WORKERS=6`). Explain or kill every survivor on your lines.
- **No paid reviews and no model calls from code.** Transcription, render and class M of your new forms run in round
  2 after the merge; list exactly what round 2 must run.
- Sources: use only archived documents (`sources/2025/manifest.json`). If a needed document is not archived, the
  scout says so: refuse that part as the scout plans, and list the document for archiving; do not fetch.

## Shared files (merged by id at integration)
`interview/2025/questions.yaml`, `fixtures/2025/defaults.json`, `fixtures/2025/classm.json`, `mutation.json`,
`interview/2025/coverage/*.yaml`, `reviews/2025/consumers.json`, `ambiguities/2025.yaml`, `tools/sources/*.json`,
`forms/2025/scope.yaml`, `f1040.yaml`, `s1.yaml`, `f8960.yaml`. Change only entries your area needs; never
reformat or reorder others. The three X1 lanes may touch the same shared forms (s1, f8960, scope, sd): keep your
edits to distinct lines; where you must change a line another X1 area also names in its scout design, say so in
the report. Use the order/seq slots the scout proposes; report any collision.
Generated files (`canonical/`, `rendered/`, `reports/`, `docs/COVERAGE.md`) are regenerated at integration.

## Rules
- Every new line cites its source with a locator the citation checker accepts; every question follows the
  interview protocol (norms N1–N12) and gets coverage rows.
- No expected value of an existing fixture is edited to make it pass. Where your area turns a refusal into a
  computation the scout marks as an approved end change (N9), restate those expectations from the source and list
  each one; any other changed value: stop and report.
- New behaviour gets hand-predicted fixtures written from the source before running (the scout's fixture list is
  the minimum).
- Defects: `python3 tools/new_bug.py "Title" --pending x1-<area> --field ...`. Do not edit `BUG_INVENTORY.md`,
  `TASKS.md`, `TASKS-DONE.md`.
- 2026: add the `changes/2026/` operations for your new forms the protocol's §7 requires (or record why not), and
  run `year_changes.py --check`.

## Report
Concise: what is computed now and what is still refused (gate, reason); files and line ids; questions added
(text); fixtures; decisions settled; verification commands and outcomes; round-2 review list; merge cautions;
the estimated coverage gain. Write the same to `docs/provisional/lanes/x1-<area>.md`.
