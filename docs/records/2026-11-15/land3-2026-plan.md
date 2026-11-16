# TY2026 preparation: lane plan (after the interview redraft lands)

Written 2026-11-14 by a judgment-class planning agent (claude-opus-5-5, year 2026, jurisdiction us). Read-only: no
file in any checkout was changed. Base read: the landing tree `.claude/worktrees/landing` (uncommitted over
`83c7d1c0`).

Labels: **[V]** verified here (command or file named); **[T]** testimony from a project doc, not re-measured;
**[I]** inferred.

## 0. Where things stand

- `years.json` is `{"adopted": [2025]}` [V]. No `forms/2026`, `params/2026.yaml` or `tables/2026` exists [T: rollover
  measurement, not re-listed].
- **Operations.** `python3 tools/year_changes.py --check` on the landing tree: "17 entries, 90 operations ... all
  apply"; notes: five parameters undefined (`sa.gambling_rate`, `sa.gift_floor_rate`, `sa.limit_screen`,
  `sc.mileage_rate_h1`, `_h2`), seven new inputs needing defaults (`f1040.form1062`, `s3a.wants_benefit`,
  `sa.mortgage_insurance`, `scveh.miles_business_h1`, `_h2`, `w2.box12_tp`, `w2.box12_tt`), 16 of 17 entries on drafts,
  `s3a.line4` awaits `s2.line20` (C-SCHED-10) [V]. 66 change-map entries that need operations are unwritten [V: the
  `changes/2026/README.md` table, rows without "yes" and with an operation kind].
- **Sources.** `tools/sources/2026.json` has 91 entries, all archived in `sources/2026/` [V]; 55 drafts [T: archive
  refresh]. 198 ids of the 2025 catalog have no 2026 entry [V], among them the documents that gate work:
  `i1040gi` (+`-html`), `i1040sca`, `i1040sd`, `i8949`, `i8995a`, `i4562`, `i8962`, `i8582`, `p946`, `p463`, `p970`,
  `p590a`, `p501`, `p526`, `p560` [V]. As of 2026-11-04 none of those had a posted 2026 edition, draft or final [T:
  `reports/2026/archive_refresh_2026-11-04.md` section 7]; whether any posted since is unchecked [I: due].
- **New York.** No 2026 NY source exists or is published [T: `docs/ny/2026-11-14_ny_year_handling.md`].

## 1. What the landing tree changes in the T-29x rows

| Row | Finding | Status |
|---|---|---|
| T-296 | "Mend the three operations the redraft makes stale" is **done in the landing tree**: `changes/2026/f1040.yaml`, `sa.yaml` and the README are modified; the check passes with 90 operations (was 86; `sa.yaml` 29 to 33) and adds the new input `sa.mortgage_insurance` [V]. The row's counts (86 operations, five proposals) are stale. | close that item at the landing's bookkeeping |
| T-261 | The year-free renames are **applied in the landing tree**: `tools/year_free_names.json` (54 renames, more than the 35 + 1 of the row), `tools/year_ids.json` 2025 list emptied, `forms/2025/clcw26.yaml` deleted (now `clcw_next_year`) [V]. No operation in `changes/2026/` names an old id (the check passes) [V]. The change map `research/ty2026/changes.md` still names old ids in its "Touches" (e.g. `f8880.dist_2025`, `f2441.paid_2026` under C-CRED-16/-12) [V for C-CRED-16]; ops lanes must re-base on current ids (the check's "gone" names the closest). | T-261 closes at the landing (after the carry); change map is testimony as of 11-04 |
| T-295 | Rehearsal step 28 (`check_year_ids --year 2026` fails on `scveh.s179_2025_ok` etc.) is **obsoleted** by the renames [I]. Every other item still holds: `interview/2025/conflict_checks.yaml:92` names `ny_it201.gate.line79_over` [V]; `placed_year` is `y2005..y2025` with no year extension in `fixtures_year.py`/`year_diff.py` [V: grep]; `year_carry.py` writes indexes, no sidecars [I: grep]; contract banks exist only under `input_contracts/2025`, `adapter_contracts/2025` [V]; `check_year_ids.py` only gained an empty-list message [V: diff]. `tools/ny_fixtures.py` is modified by the landing (new f2441 gate inputs) but its overwrite defect stands [V: diff]. | open, as written minus step 28 |
| T-297 | **Stale count.** The landing adds 18 parameters to `params/2025.yaml` (14 `age.*` birth-year cut-offs, `sales.detail`, `ret.catchup_under50`, `_age50`, `_age60_63`) and an enum `dependent_support_view` [V: diff]. The 292-parameter proposal predates them; the 14 `age.*` cite `i1040gi` (no 2026 edition), so `propose_params.py` would decline them although the file's own comment says "Each moves by one with the tax year" [V]. | rerun after landing; needs the offset rule (D7) |
| T-298 | Its trigger ("next change to `params/2025.yaml`") is **met by the landing**, which changes that file without the fix: `tables/2025/rate_schedule.yaml:15` still reads "section 3.01", `params/2025.yaml` lines 866 and 956 "section 3.06" [V]. | due now: lane P1 |

## 2. Decisions this plan makes on the owner's behalf

| # | Decision | Recommendation | Reason |
|---|---|---|---|
| D1 | Federal 2026 adoptable without NY 2026 (ny doc D1) | **Yes, decouple**: `years.json` gains a per-jurisdiction list (`"ny_adopted": [2025]`); check-all skips the `ny_*` steps visibly for a year NY has not adopted; `build` skips (with a note) conflict checks naming a NY gate when `forms/ny/<year>` is absent | NY publishes after the IRS; coupled, NY's date becomes the federal critical path. The check reduced is only NY-for-a-year-NY-lacks |
| D2 | Adopt a draft `forms/2026` on main early? | **No.** Preparation stays as operations (`changes/2026/`) plus staged parameters and tables; adoption runs on main only when the gating finals exist (charter 1.4). Drafts are adopted only in scratch rehearsals | Operations are checked on every commit and cannot decay; an adopted copy would decay and double every 2025 fix |
| D3 | Shared forms (`person`, `dependent`, `f1040`, `carloan`, ...) touched by several lanes | **Split files** `changes/2026/<form>.<topic>.yaml`, each with `form: <form>`; one lane owns each file | `load_changes` reads every `*.yaml` and keys on the `form:` field, in sorted file order, and flags collisions across files [V: `tools/year_changes.py:134-165`]. Avoids serializing lanes on one file. Needs a one-line note in `tools/README.md` and `changes/2026/README.md` |
| D4 | Ambiguity register entries (C-PRI-15, C-SCHED-28, C-CRED-02, C-CRED-05) | **Operations** `add_ambiguity` / `set_ambiguity` in `year_changes.py` (design doc section 7 left this open) | Otherwise the four entries live as prose and decay as the proposals did |
| D5 | New-input defaults and ripple at adoption | Each `add_question` carries `default` and `reason`; `fixtures_year.py` writes them to `fixtures/<to>/defaults.json`; `--adopt` copies the contract banks to `<to>/` | Removes the serial `inputs`-claim step at adoption (T-296, T-295) |
| D6 | `placed_year` and its table keys | `--adopt` extends enums declared `extends_with_year: true` (and `recovery_year`'s keys) by `y<to>` | The rehearsal's fixture/property failure is mechanical, not a judgment |
| D7 | Year-moving parameters | Declare `moves_with_year: 1` on the 14 `age.*` params; `propose_params.py` fills them by offset, marked `derived` | They move by definition; a 2026 i1040gi would only confirm |
| D8 | Read a value from a second document (T-297) | **Yes** for the Tax Computation Worksheet rows from Rev. Proc. 2025-32's rate tables, marked `derived`, re-verified when the 2026 i1040gi posts | `extract_printed_tables.py` already checks TCW parameters against the rate-schedule rows; raises the mechanical share now |
| D9 | Draft-to-final flip | **Per document, as each final posts**, not all at once | Spreads work over Dec to Jan; `year_changes.py --check` already lists entries whose documents are all final [T: tools/README] |
| D10 | Paid reviews during preparation | **None.** Reviews run once, line-scoped, on the adopted finals | Drafts change; a draft-based review is spent twice |
| D11 | Wording-only change entries | One **Sonnet** lane (W1) in split `<form>.wording.yaml` files, in parallel with the Opus lanes | Mechanical: quote the change map's 2026 text; the evidence check verifies each quote |
| D12 | 2025 tree after 2026 adoption (T-261's open question) | Defect fixes only; a fix that applies to both years lands in 2026 and is ported to 2025 only if it changes a 2025 return | Bounds double maintenance in filing season |
| D13 | Source refresh before finals | A Sonnet lane (S1) re-checks irs.gov draft/final pages now and then weekly, archiving new 2026 drafts/finals per ADOPTION.md step 1 | Network fetch; the gating documents' arrival dates are unknown |
| D14 | Claims for operation lanes | Each lane claims the forms it alone writes operations for (`python3 tools/claims.py claim s2 f8959 --reason "2026 operations, lane O1"`); shared forms (`person`, `dependent`, `household`, `f1040`, `carloan`, `scveh`) are not claimed; a 2025 lane editing them reruns `year_changes.py --check` and mends | Claims only fire on `forms/<year>/` edits [V: `tools/claims.py` docstring], which ops lanes do not make; the claim protects their operations from a 2025 edit that would stale them |

## 3. Lanes

Every brief states Model, Class, Year 2026, Jurisdiction (`us` unless noted); every lane works in a worktree
(`tools/worktree_data.py clone`; results via `carry-back`), records defects as `bug_pending/` entries, does not edit
`BUG_INVENTORY.md`, `TASKS.md` or the `changes/2026/README.md` table (the coordinator's bookkeeping commit does),
and verifies with `tools/check_all.sh` in its own worktree (fast tier for changes-only commits [I: the design doc
puts `year_changes` in the fast tier]). Paid reviews: none in any preparation lane (D10).

### Wave 1: start immediately after the landing (all independent)

| Lane | Model / class | Scope (files; claims) | Inputs | Deliverable and verification |
|---|---|---|---|---|
| **P1** T-298 + BUG-0627 | Sonnet / mechanical | `tables/2025/rate_schedule.yaml`, the eight `eic.*` and `s1.ebl_threshold` cites in `params/2025.yaml`, the ruling in `reviews/2025/citations.json`, `engine/src/conjecture.ts` text; the two qss thresholds in `research/ty2026/params-2026.proposed.yaml` (`ctc.threshold` qss 200,000; `s1.ebl_threshold` qss = single) | BUG-0626, BUG-0627; `sources/2025` Rev. Proc. 2024-40 | `citations.py --strict` passes; check-all. Merge first (it touches `params/2025.yaml`, as P2 does). Review: none expected (cite locators only) [I] |
| **R1** NY decoupling (D1) | Opus / judgment; jurisdiction ny | `years.json`, `tools/taxyear.py`, `tools/jurisdiction.py`, `tools/check_all_steps.sh`, `engine/src/build.ts` (conflict checks); `tools/check_year_ids.py` refuses a year with no build | ny doc D1, `fedonly.sh` repro | In a scratch tree with federal 2026 = 2025 copied and no NY 2026: `build --year 2026` passes, `check_all.sh --year 2026` lists NY steps as skipped; with NY 2026 present, unchanged. Self-tests |
| **R2** Carry what adoption drops | Opus / judgment | `tools/year_diff.py --adopt` carries `operands.json`, `consumers.json`, `limits.json`, `instruction_cites.json`, `signs.json` and both contract banks (`tools/transcription/{input,adapter}_contracts/<year>/`); `tools/transcription/year_carry.py --write` writes rulings sidecars | ny doc rehearsal steps 18, 22, 24 | Rerun those steps in a scratch rehearsal: no new findings on unchanged documents; `check_logs.py` no "not in rulings.json"; self-tests |
| **R3** Operation kinds and adoption rules (D4, D5, D6) | Opus / judgment | `tools/year_changes.py` (`add_ambiguity`, `set_ambiguity`; `default`/`reason` on `add_question`), `tools/fixtures_year.py` (write new defaults), `tools/year_diff.py` (enum `extends_with_year`, `recovery_year` keys), `params/2025.yaml` flag on `placed_year` only; `tools/README.md` sections | design doc sections 2, 7; T-296 | `--self-test` plants each new kind's failures; the seven listed new inputs get `default`s in their existing ops (touches `changes/2026/{f1040,sa,s3a,scveh,w2}.yaml`: R3 owns them until merged). Merge early: O3a and O7 need it |
| **R4** Small year defects | Sonnet / mechanical | `tools/build_fresh.py` scoped to a year; `tools/ny_fixtures.py` refuses to overwrite committed fixtures (writes `--out`); NY catalog edition check for the 4 year-free addresses (Y15); `tax_year` in the server state and page title (`engine/src/serve.ts`, `ui/`) | T-295, T-297 last item, ny doc Y15/Y19 | Self-tests; scratch: adopting 2026 no longer makes 2025 stale |
| **P2** Parameters and tables, draft pass | Opus / judgment | `tools/propose_params.py` (D7 offset, D8 second document), `moves_with_year` on the 14 `age.*` in `params/2025.yaml` (after P1 merges); staged outputs only: `reports/2026/params_proposal_from_2025.{md,yaml}`, `research/ty2026/params-2026.proposed.yaml` (merged with the mechanical result, defining the five params the ops read and `ret.catchup_*` from `n-25-67`), `extract_printed_tables.py --write --year 2026 --out research/ty2026/tables-2026`, `layouts.py --propose --from 2025 --to 2026 --partial` (staged) | landed `params/2025.yaml`; `sources/2026` | `propose_params.py --compare` report; `year_changes.py --check` param note answered by the staged file; list of params still waiting, by document |
| **S1** Source refresh (D13) | Sonnet / mechanical | `tools/sources/2026.json`, `sources/2026/`, a dated `reports/2026/archive_refresh_<date>.md` | ADOPTION.md step 1; the 2025 catalog | `fetch_sources.py --year 2026` and `check_extraction.py --year 2026` pass; new drafts/finals listed. Repeat weekly; each run is its own small lane |
| **O1** Schedule 2 and Form 8959 (**critical**) | Opus / judgment | `changes/2026/s2.yaml`, `f8959.yaml`; claims `s2 f8959`. C-SCHED-10, -11 (s2 side), -13, -15; s2 sides of C-PEOP-03, -12, C-SCHED-17. Must add `s2.line20` | change map; `sources/2026/f1040s2`, `f8959`, `i8959` | `year_changes.py --check`: the `s2.line20` await clears; new evidence quotes printed. Tip: edit a scratch copy, then `year_changes.py --record` |
| **O2** Retirement, Form 5329, IRA | Opus / judgment | `f5329.yaml`, `retirement.yaml`, `ira.yaml`, `person.retirement.yaml`; claims `f5329 retirement ira`. C-SCHED-11 (5329 side), C-PEOP-03 to -06, -08, -11 (refused, owner decision 5) | `f5329`, `i5329`, `f1099r`/`i1099r` (final), `p590b`, `n-25-67` | check passes; new inputs (boxes 7a to 7d) carry defaults (after R3, or added at rebase) |
| **O3b** Schedule 3 and Schedule 8812 | Opus / judgment | `s3.yaml`, `s8812.yaml`; claims `s3 s8812`. C-SCHED-12, -16, -18 to -20 (cites with the rest), -23, -26, -39; s3/s8812 sides of C-CRED-05, C-SCHED-17 | `f1040s3`, `f1040s8812`, `i1040s8812` | check passes; reads of new s2 lines use `awaits` until O1 merges |
| **O5** Education and saver's credit | Opus / judgment | `f8863.yaml`, `f8880.yaml`, `person.edu.yaml`, `dependent.edu.yaml`; claims `f8863 f8880`. C-CRED-16, -18, -20, C-PEOP-16, -17, -21 (C-PEOP-24's p970 items wait) | `f8863`, `i8863`, `f8880`, `f1098t`, `i1098et` | check passes |
| **O6** Health coverage and HSA | Opus / judgment | `f8962.yaml`, `f8889.yaml`, `person.hsa.yaml`; claims `f8962 f8889`. C-PEOP-12, -14, -27, C-PRI-20, -22, -23 (C-PEOP-13/i8962 items wait) | `f8962`, `f8889`, `i8889`, `rp-25-25`, `rp-25-19` | check passes |
| **O8** Schedule 1-A and Form 1040 page 1 | Opus / judgment | `s1a.yaml`, `tipjob.yaml`, `otjob.yaml`, `carloan.s1a.yaml`, `s1.s1a.yaml`, `f1040.page1.yaml`; claims `s1a tipjob otjob`. C-SCHED-01 to -06, -08, C-PRI-06 | `f1040s1a`, `fw2`, `iw2w3` | check passes. Largest renumbering; `--record` from an edited copy |
| **O9** Schedule C and depreciation | Opus / judgment | `sc.yaml`, `asset.yaml`, `f4562.yaml`, `scveh.yaml` (existing), `carloan.sc.yaml`; claims `sc asset f4562`. C-BUS-02, -04, -06, -11, -12 (expr only; amounts in P2) | `f1040sc` (final), `i1040sc`, `f4562`; `i4562`, `p946`, `p463` not posted | check passes; items resting on `i4562`/`p946`/`p463` listed as waiting |
| **W1** Wording-only entries (D11) | Sonnet / mechanical | `<form>.wording.yaml` files: C-PRI-11, -21, -29, C-SCHED-07, -29, C-CRED-13, -14 (label), -17, C-PEOP-01, -02, -07, -10, -19, -20, C-BUS-03, -05, -08 | change map quotes | check passes (evidence quotes printed; no collision with O lanes, which do not take these ids) |

### Wave 2: after R3 merges

| Lane | Model / class | Scope | Deliverable |
|---|---|---|---|
| **O3a** Form 5695 carryforward-only | Opus / judgment | `f5695.yaml`, `scope.f5695.yaml`; claim `f5695`. C-CRED-01 to -08 with the register ops of C-CRED-02, -05 | check passes; many `remove_line`/`remove_question`: dangling check clean. Can start in wave 1 and add register ops at rebase |
| **O4** Dependent care | Opus / judgment | `f2441.yaml`, `dcprov.yaml`, `dependent.dc.yaml`; claims `f2441 dcprov`. C-CRED-10 (line 8 by status: reads P2's staged `dc_rate`), -11, -12, C-PEOP-18 | check passes; new params named for P2 |
| **O7** QBI and net investment income tax | Opus / judgment | `f8995.yaml`, `f8995a.yaml`, `qbi.yaml`, `f8960.yaml`, `s1.niit.yaml`, `f1040.qbi.yaml`; claims `f8995 f8995a qbi f8960`. C-SCHED-27, -28 (register op), -31 to -33 | check passes (`i8995a` items wait) |
| **R5** Draft-adoption rehearsal | Opus / judgment | `tools/year_rehearse.sh` (new; scratch copy outside the repo, as the NY rehearsal did) and a dated `docs/<date>_ty2026_draft_adoption_rehearsal.md` | Runs `year_diff.py --adopt`, staged params/tables as `params/2026.yaml`/`tables/2026` in scratch, `build --year 2026`, `fixtures_year.py`, `test-fixtures`, `year_carry.py --from <2025 tree>` (no `--write`), `rerun_all.py` dry-run cost estimate per changed form, and the year-literal list classified. Output: the defect list and the adoption's review estimate. Rerun after each wave and at each batch of finals |

### Wave 3: when the finals post (staggered, D9)

| Lane | Model / class | Trigger | Work |
|---|---|---|---|
| **F1** Finals refetch | Sonnet / mechanical | each S1 run that finds finals | ADOPTION.md step 1 for those documents |
| **F2** Flip to final | Sonnet / mechanical; Opus for any entry whose quote no longer prints | `year_changes.py --check` notes entries with all documents final | set `verified: final`; failing quotes go to the owning O lane's form, as a small Opus lane |
| **P3** Parameters final pass | Opus / judgment | `i1040gi` (and `i8962`, `p946`) archived | `propose_params.py` again; the 117 waiting values; tables and layouts without `--partial`; `check_auto_limits.py` |
| **O10** Waiting entries | Opus / judgment | `i1040gi`, `p970`, `p590a`, `i4562` archived | C-PEOP-23, -24 and every item listed as waiting by O lanes |

### Wave 4: adoption (finals in, R5 clean)

| Lane | Model / class | Work |
|---|---|---|
| **A1** Adopt | Opus / judgment; holds `inputs` | `year_diff.py --from 2025 --to 2026 --adopt`; `params/2026.yaml`, `tables/2026` from staging; relocation report and `citations.py --strict --year 2026`; `fixtures_year.py --from 2025 --to 2026`; predicted cases of `research/ty2026/fixtures-proposed/2026-predicted.json`; `build --year 2026`; `year_carry.py --year 2026 --from <2025 tree> --write` |
| **A2a..n** Reviews by form group | Opus adjudication; reviews are paid calls | After A1 merges, one lane per group of changed forms (claims `forms/2026` ids): `rerun_all.py` line-scoped transcription, render, class M for lines not carried; one review per form per round; `--approve-cost` only where the dry run in R5 named it |
| **A3** Year on | Sonnet / mechanical | `years.json` adds 2026 (federal; NY per D1), `check_all.sh --year 2026`, sampled completeness/screen/false-no reviews for the 2026 release (`release_reviews.sh`) |
| **N1** New York 2026 | Opus / judgment; jurisdiction ny | when NY publishes, after A1: ny doc section 6 steps 1 to 7, as two lanes (catalog, adopt, tables; predictor, fixtures, carry) |

## 4. Dependencies, critical path, merge order

```
landing ─┬─ P1 ─ P2 ──────────────────────────┐
         ├─ R3 ─┬─ O3a, O4, O7 ───────────────┤
         ├─ O1 ─┘ (clears the s2.line20 await)├─ R5 rehearsal ─ [IRS finals: S1/F1/F2/P3/O10] ─ A1 ─ A2 ─ A3
         ├─ R1, R2, R4 ───────────────────────┤                                             └─ N1 (when NY publishes)
         └─ O2, O3b, O5, O6, O8, O9, W1 ───────┘
```

- **Critical path.** Internal: landing, then O1 + R1 + R2 + R3 (one session each, parallel), then R5. Everything else in
  waves 1 and 2 is off the critical path. External, and dominant: the IRS finals, chiefly `i1040gi` (about 129
  parameter citations and 937 worklist items wait on it [T: T-297, ADOPTION.md]); expected December 2026 to January
  2027 [T: ADOPTION.md]. After finals: F1, F2/P3/O10 (parallel), A1, A2 (parallel by form), A3.
- **Shortening it.** (1) O1 first and alone on Schedule 2: it is the only await that makes adoption refuse. (2) D1:
  NY leaves the federal path. (3) R5 rehearses the whole adoption on drafts, so the finals day is refetch, flip and
  re-run, not discovery. (4) D9: flip document by document as finals post. (5) D5/R3: no serial inputs step at
  adoption. (6) A2 runs as parallel form-group lanes against the per-line list `year_carry.py` already produced.
- **Merge order.** P1 first (shares `params/2025.yaml` with P2). Then R3, then O1, in either order but early. Then R1,
  R2, R4 and the wave-1 O lanes and W1 as they finish (file-disjoint by D3; `year_changes.py --check` after each merge
  catches collisions between lanes, resolved in the later lane). Then P2, O3a, O4, O7. R5 last in the wave, and again
  after each later merge batch. After each batch, one coordinator bookkeeping commit: the `changes/2026/README.md`
  table, `TASKS.md` (T-295, T-296, T-297, T-298 rows), pending bug entries assigned.
- **Concurrency.** Wave 1 is 15 lanes; with two machine check slots (`CHECK_ALL_MAX_RUNS=2`) [T: CLAUDE.md], run
  about eight at once (the four on the critical path plus four O/W lanes), then the rest [I].

## 5. Paid reviews

- Preparation (waves 1 to 3): **$0** by D10. The only spend is agent runs (logged in `research/costs/agent_runs.jsonl`).
- Adoption (A2): transcription, render and class M on the lines the operations touch and lines whose cited text
  changed; carried lines are not reviewed. Not measured: R5's `year_carry` dry run and `rerun_all.py` estimate give
  the number. The measurement doc's full-review estimate of $140 to $400 a year [T] is the ceiling; the large
  relayouts (Schedule 2, Schedule 1-A, Form 5695, Form 2441, Form 8995) are the likeliest to exceed the $3.00 gate per
  run [I].
- Release (A3): one sampled completeness, screen and false-no review per changed form, at the 2026 milestone.

## 6. Risks and open points

- The change map is testimony as of 2026-11-04 [T]; ids moved since (redraft, renames). O lanes re-base on current
  ids; the check's "gone" with suggestions catches misses.
- D3 rests on reading `load_changes`; that adoption applies split files in the right order and writes each form once
  is inferred, to be confirmed by R3's self-test (add a split-file case) [I].
- The 66-entry count of unwritten op-needing entries is from the README table; the design doc says 83 need operations
  and 17 are written [T], consistent [V arithmetic].
- Whether any gating 2026 document posted since 11-04 is unchecked: S1's first run answers it.
