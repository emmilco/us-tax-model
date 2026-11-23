# TY2026 draft-adoption rehearsal (2026-11-15)

Plan lane R5 (`docs/provisional/lanes/ty26-plan.md`, wave 2): the whole federal adoption of 2026, run on what is
archived today (IRS drafts and the finals posted so far), in a scratch copy outside the repository, to find what
breaks before the finals arrive and to price the reviews adoption will need. Written by a judgment-class agent
(claude-opus-5-5). No paid review, no model call; New York is not adopted (plan decision D1) and was not rehearsed.

**Labels.** [M] measured in the rehearsal, with the step or file. [I] inferred, not run. [T] testimony from a project
document, not re-measured.

## 1. What was run

`tools/year_rehearse.sh` (new) on the lane tree (the 2025 landing plus 2026 batches A and B: 130 entries, 1,256
operations in `changes/2026/`), copy `/tmp/ty26-r5-reh/tree`, logs `/tmp/ty26-r5-reh/out/` (one per step,
`summary.tsv`). The run that reached the end was
`tools/year_rehearse.sh --dest /tmp/ty26-r5-reh --reuse-build --stand-in-sources`, reusing the 2025 build of the run
before it (that build took 59 minutes: the machine's load average was 90 to 270 throughout, with other lanes'
builds). The last step (the second dry-run estimate) was added after that run and run by hand in the same copy with
the step's own code (`out/20b_estimate_unlogged.log`).

Three stand-ins let the run go past defects; each is in the script's header and shows in the summary as its own step:

- `adopt_standin` (BUG-1033): copies the 38 interview files under `interview/2025/coverage/` and
  `personas/` that `--adopt` leaves out, then applies the operations and writes the shared-refs report.
- `labels_standin` (BUG-1034): adds `y2026: '2026'` to the two `value_labels` of `placed_year`.
- `sources_standin` (`--stand-in-sources`): the 29 documents the 2026 definitions cite that have no 2026 archive
  are copied from `sources/2025/` (manifest entries marked `stand_in`). Everything after the build therefore treats
  those documents as unchanged: the carry and the estimate below are a **lower bound** for the forms that cite them.

## 2. Step by step

| # | Step | rc | Time | Outcome [M] |
|---|---|---|---|---|
| 1 | compile | 0 | 1 s | |
| 2 | build 2025 | 0 | 59 min | (previous run; reused) |
| 3 | `year_diff.py --adopt` | **1** | 53 s | Copies, carries 12 review files, writes the year-literal list, relocates (3,016 segments: 182 in place, 1,637 moved, 1,197 to review; 1 "could not rewrite forms/2026/scope.yaml:657; edit by hand"), then **stops**: 20 interview operations of C-CRED-01 are "gone: no interview file personas/... / coverage/education_energy.yaml" (BUG-1033). The year is left half adopted |
| 4 | `adopt_standin` | 0 | 7 s | 38 files copied; all 1,256 operations apply (521 lines added or changed, 239 removed); 414 shared references |
| 5 | stage parameters | 0 | 1 s | 295 adopted parameters: 15 retired removed; 80 final values changed, 35 final unchanged, 11 draft changed, 60 draft unchanged, 14 derived (age) changed; 95 with no 2026 source keep the 2025 value; 12 new (8 final, 4 draft); enums `retirement_account` +trump, `bonus_choice` -forty, `early_exception` and `placed_year` restated unchanged. No problem reported |
| 6 | stage tables | 0 | 1 s | `dc_rate`, `ltc_limit`, `rate_schedule`, `savers_rate` replace the adopted copies |
| 7 | `citations.py --strict --year 2026` | **1** | 51 s | 857 findings (570 not found, 287 found on another page): i8962 350, rp-25-32 97, i8889 88, i8863 71, i2441 43, p525 28, i1040sc 26, others; by file forms 712, params 134, ambiguities 11. 3,710 segments on documents with no 2026 text. Input quotes: 347 checked, 56 unmatched (55 new, 3 stale) |
| 8 | build 2026 | **1** | 3 s | 6,168 errors: 6,166 follow from documents with no 2026 archive (2,089 `cite doc ... not in sources/2026/manifest.json`, 2,008 each 'citation has no snapshot hash' and 'no revision', 61 schema failures on the snapshot pattern); 2 `value_labels must label every value of the enum` (`scveh.placed`, `asset.placed`; BUG-1034) |
| 9-11 | stand-ins, build 2026 again | 0 | 3 s | **build OK** (no fixtures yet, so no interview walk) |
| 12 | rebuild 2025 | 0 | 46 min | build OK (adopting makes the 2025 build stale for `build_fresh`, as the New York record found) |
| 13 | render 2026 | 0 | 1 s | 69 files |
| 14 | `fixtures_year.py --no-hand-work` | 0 | 6 min | 1,224 carried: 108 kept, 1,116 re-recorded, "3 not evaluated" (the three `bonus_choice: forty` cases), 25 official examples dropped; defaults 9 added, 71 dropped; 754 cases marked "not evaluated in 2026" for stating a removed input (BUG-1036) |
| 15 | `test-fixtures --year 2026` | **1** | 3 min | 1,212 of 1,978 pass. 754 failures are the marked cases (679 `f5695.any`, 49 `miles_business`, 10 `edu_tin_issued`, 6 `bonus_choice`); 12 are re-recorded cases that still expect a removed line (BUG-1036) |
| 16 | `year_carry.py` (no `--write`) | 0 | 29 min | see section 3 |
| 17 | `year_carry.py --write` | 0 | 35 min | same counts; indexes and sidecars written |
| 18 | `review_store.py check --year 2026` | 0 | 1 s | 64 indexes, 115 records, all present |
| 19 | `check_logs.py --year 2026` | **1** | 2.5 min | "rulings: 80 in logs, all in sidecars" (R2's sidecar fix holds). Fails on logs not carried (transcription 27/63, render 30/63, class M 7/56 forms logged) and on 866 snapshot or reading-order rows of carried logs, including logs carried whole (BUG-1037) |
| 20 | `rerun_all.py --year 2026 --dry-run` | 0 | 5 min | 64 jobs planned, only for forms with a 2026 log (BUG-1038); see section 4 |
| 20b | the same over the forms with no 2026 log | 0 | ~2 h | 115 jobs; all 48 class M requests fail to build (BUG-1039); see section 4 |
| 21 | report digest | 0 | | year literals 2,779 lines (from_year 1,781, adjacent 510, year_id 427, other 144, fixed reference 88, birth cutoff 85; 2,216 with a moved candidate; interview subdirectories not scanned, r5-01); shared refs 414 in 8 files (`generate_cases.py` 143, `generate.ts` 138, `mutate.ts` 88, `coverage/tree.json` 16, `run_engines.py` 12, `compare.py` 8, `ots_adapter.py` 5, `ustaxes_adapter.py` 4) |

## 3. The review carry (year_carry, step 16) [M]

| Kind | Lines carry | Lines to review | Forms carried whole | Forms reviewed every line | In part |
|---|---|---|---|---|---|
| Transcription | 190 | 1,137 | 2 | 34 | 26 |
| Render | 260 | 1,310 | 3 | 32 | 27 |
| Class M | 250 | 5,307 | 7 | 48 | 0 |

Reasons (a line may have several), transcription: cited text changed 937, the line or what it reads changed 267, its
citations changed 257, values changed 164, not compared under the same key 111, cited document not archived 82, no
2025 review 60. Class M: cited text changed 4,967, values changed 4,026, citations changed 3,704. Most of the change is
the drafts' new text and the pages relocation moved; the 29 stood-in documents count as unchanged, so i1040gi,
i4562, p946, i1040sd and the rest will add to these numbers when they post [I].

Two transcription forms (`dependent`, `f8889`) cannot be planned at all: their input-contract banks were carried with
the 2025 source snapshot and are refused as stale, as designed (lane R2): their cases are to be reviewed against the
2026 text first.

## 4. The adoption's review estimate

Priced by `rerun_all.py --dry-run` (request size x the ledger's recent cost per prompt character, Claude family), on
the rehearsal's text: drafts where posted, 2025 text for the 29 stood-in documents. One round, no reruns.

| Kind | Jobs priced | Line-scoped | Whole | Dollars | Not priced |
|---|---|---|---|---|---|
| Transcription | 58 | 23 | 35 | $48.03 | `dependent`, `f8889` (stale input banks); `clcw`, `tax_on_amount` current |
| Render | 59 | 22 | 37 | $40.42 | `clcw`, `sales`, `tax_on_amount` current |
| Class M | 0 | | | **not priced** | 7 forms current; 48 forms' requests could not be built (BUG-1039) |
| **Total priced** | 117 | | | **$88.45** | |

- Class M [I]: the 48 forms with no carried line have 258 class M cases, all marked "not evaluated in 2026"
  (they are whole returns and state `f5695.any`). At the 2025 mean of $0.286 per Claude class M call
  (`.transcription/costs.jsonl`, 660 calls), one round is about **$74**. So the adoption's first round is about
  **$160** [I], inside the $140 to $400 a year the measurement doc gives as the ceiling [T].
- Largest jobs: render Form 1040 $3.02 (the only job over the $3.00 gate on its own), render s8812 $2.59, transcription
  person $2.39, render f8995 $2.12, render s2 $2.08. Every A2 run that groups more than a few forms will need
  `--approve-cost`.
- The 64 + 115 split is the defect of BUG-1038: run as the plan says (`rerun_all.py` per form group), A2
  would get only the first 64 jobs ($36.68) and never review the forms that changed most (f8962, f2441, f5695, f8863,
  f8889, s2, s8812 ...).
- Lower bound: the stand-ins make every line citing i1040gi, i4562, p946, i1040sd, p560 and the other 24 stood-in
  documents look unchanged; when those post, their lines move from "carry" to "review" [I].

## 5. Defects

New, each a pending entry (`bug_pending/ty26-r5-NN.md`):

| Id | Defect | Blocks | Owner (suggested) |
|---|---|---|---|
| BUG-1033 | `--adopt` copies only top-level `interview/<year>/*.yaml`; operations on `personas/` and `coverage/` fail and adoption stops half done | adoption | `year_diff.py` (R3/R6 code) |
| BUG-1034 | an enum extended with the year (`placed_year`) leaves the questions' `value_labels` behind; build refuses | the 2026 build | `extend_year_enums` (R3) |
| BUG-1035 | 97 rp-25-32 anchors "section 4.NN" are not printed text (the staged parameters and the tcw operation) | `citations.py --strict` | P2 / citations |
| BUG-1036 | 754 fixture cases "not evaluated in 2026" (563 of them only for a default No to `f5695.any`); test-fixtures fails them; 12 re-recorded cases keep expectations on removed lines; the carry's summary says 3 | test-fixtures | `fixtures_year.py`, engine fixtures |
| BUG-1037 | check_logs fails year-carried logs on their 2025 snapshot rows, even when carried whole | check_logs | check_logs / review store |
| BUG-1038 | rerun_all plans no review for a form where no line carried | A2 reviews, the estimate | `rerun_all.py` |
| BUG-1039 | `classm-jobs --include-fixtures` crashes on the marked cases; no class M request can be built | class M reviews | engine `classm.ts` |

Seen, and covered by existing rows or by design:

- 414 shared references (BUG-0644, lane R6's list): each shared file still needs its two-year decision.
- 2,779 year-literal lines (BUG-0645, BUG-0646): the worklist R6 built; nothing moves them yet.
- Three `bonus_choice: forty` fixture cases (C-BUS-04, lane O9) and 49 `miles_business` cases (C-BUS-01; lane R3's
  note leaves the move to its owner): listed by the carry as designed.
- Stale input banks for `dependent` and `f8889` (lane R2's design: reviewed against the new text first).
- Render logs run whole for `f4562`, `interest`, `mq`, `se`, `tcw` (no line subjects and a changed source) and
  transcription `tipjob` (changed outside every compared line): the tool's stated rule, not a defect.
- `forms/2026/s1.yaml` keeps one cite of `rp-2024-40` (`s1.ebl_threshold`), whose 2025 catalog names `rp-25-32`; the
  year-diff worklist covers a document with no edition in one year.
- Relocation could not rewrite one segment (`forms/2026/scope.yaml:657`, p525): the tool's "edit by hand".

## 6. What waits on unpublished or unarchived documents

The 2026 build fails on 29 cited documents with no 2026 archive. Status per `reports/2026/archive_refresh_2026-11-14.md`
[T] (S1's refresh): "not posted" means only the 2025 edition is on irs.gov.

| Document | Build errors | Status |
|---|---|---|
| i1040gi | 1,174 | not posted; also 42 parameters with no 2026 value (lane P2) and the Tax Table, EIC table and layout pages |
| i4562 | 257 | not posted |
| i1040sd | 202 | not posted |
| p946 (+ html) | 145 | not posted; Pub. 946 tables and `auto_limit` |
| p560 | 67 | not posted |
| i1040sca | 47 | not posted |
| p501 | 36 | not posted |
| i8949 | 28 | not posted |
| i8995a | 1 | not posted |
| p550, p969, p974, p504 | 23 | not posted (2025 or earlier only) |
| p463 | 1 | not posted |
| i3800, i8801, i8839, i8936, f8396 | 44 | 2026 drafts posted (i3800 2026-11-13), not yet archived: S1's next run |
| fr-2025-24154, n-25-69, rp-2024-40 | 27 | guidance with no 2026 entry in the catalog: to be catalogued for 2026 (continuous use), and rp-2024-40 replaced by rp-25-32 |
| i8615, i6251, i4136, i8911, i8912, i1040sr | 37 | not in the 11-14 refresh report; to check |

Beyond these, 57 of the 96 documents archived for 2026 are drafts, and 122 of the 130 change entries rest on drafts
[M: manifest; `year_changes.py --check`]: every count in sections 3 and 4 is to be remeasured at the finals.

## 7. Rerunning it

`tools/year_rehearse.sh --dest /tmp/ty26-r5-reh --force --stand-in-sources` (a full run takes about three hours on
a loaded machine, two builds of 2025 being most of it), or with `--reuse-build` on an existing copy whose 2025
definitions have not changed. As the defects close, their stand-in steps stop appearing in `summary.tsv`. The plan
asks for a rerun after each wave and at each batch of finals.

## 8. Rerun after the fixes (lane R7)

Lane R7 fixed r5-01 to r5-07 (tools and data) and removed the stand-ins for r5-01 and r5-02 and the second dry run
from the script. It reran the rehearsal in full (`/tmp/ty26-r7-reh`). Results [M]: adoption passes on its own;
citations 760 findings, none on rp-25-32; check_logs has no snapshot findings; `rerun_all` plans 179 jobs in one
run ($88.45 priced). Class M still cannot be priced: the random corpus in `engine/src/generate.ts` draws Form 5695
inputs that 2026 removes (BUG-0644). 369 fixture cases remain marked not evaluated. Before and after, step by step:
`docs/provisional/lanes/ty26-r7.md`.
