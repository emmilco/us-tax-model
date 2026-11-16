# Lane A8-k1e: what the estate and trust K-1 lane (Schedule K-1, Form 1041) needs to land

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-16 about 01:15. Read only: nothing
in the repository, its worktrees or .git was changed. No build, engine run, fixture run or model call was made.
Tags: **[C path:line]** checked against that file. Paths are relative to the xint worktree unless they start with
`x2-k1e/` (= `.claude/worktrees/x2-k1e`) or `/tmp`. **[I]** inferred, not checked.
`P/round4/k1int.md` did not exist when this was written (checked at 01:08 and 01:14). Where this plan depends on the
integration lane, it says so.

## Summary

1. **What x2-k1e built** (worktree `x2-k1e`, base `825024d8` x1-base, uncommitted). It adds a new collection form
   `k1e` (Schedule K-1 (Form 1041) per entry, parent `person`, 87 lines). It computes income only: boxes 1 to 8,
   13 A/B and 14 A/H(positive)/I. It refuses boxes 9 to 12, losses in 6 to 8, other codes, negative 14 H, and PTP or
   cooperative items. It also adds 18 `person.k1e_*` sums, which are display-only and read by nothing, 19 hand-predicted
   fixtures, 36 questions at order 266 in 3 tick groups, 2 ambiguities, 8 `tree.json` gates, a 2026 change entry and
   36 defaults. A scratch wiring was applied, checked and reverted. With it, all 11 parked coverage rows passed, and
   persona 18 completed. [C x2-k1e git status; docs/provisional/lanes/x2-k1e.md:11-42,106-128]
2. **Reviews already paid for, held only in the x2-k1e worktree.** These are the whole-form transcription ($1.08) and
   render ($0.27) reviews, adjudicated by xrev-new. They are 2 ledger rows, 5 tracked review files, 2 store files and
   one pending low, `xrevk1e-01`: boxes 4b and 4c are read only when 4a > 0, a reading that is not registered. None of
   this is in xint. The ledger has 0 k1e rows, the inventory has no `xrevk1e`, and xint has no `reviews/2025/*/k1e*`.
   xint's carry-back list left out x2-k1e. [C x2-k1e/.transcription/costs.jsonl (2 rows); grep in xint: 0;
   docs/provisional/lanes/xint.md:222-223]
3. **Why it was deferred.** Class M had no job: "k1e: 0 case(s) cover 0/118 branches … 118 with every answer"
   [C x2-k1e/reviews/2025/transcription/adjudication/k1e.md, class M section]. `check_logs` reported "missing: k1e"
   [C /tmp/xrev-new/k1e.checklogs.txt:79]. The coordinator dropped k1e from xint at 18:45 [C xint.md:207-210].
   **Nuance:** other new forms also had no class M jobs (the f1116 family, rprop, rf4562) and still landed
   [C docs/records/2026-11-15/land3-followups.md:109]. k1p got 10 class M cases with `scope.k1` still refusing
   [C fixtures/2025/classm.json `classm.k1p.1`…`10`]. The visible difference is in the fixtures: **all 19 k1e cases
   state `scope.k1: true`, while none of the k1p or k1s cases does** [C grep counts: k1e.json 19, k1p.json 0,
   k1s.json 0]. `scope.k1: true` refuses the whole return at `scope.schedule1` [C forms/2025/scope.yaml:1188].
   class M takes only cases whose derived values are all computed, with no refusal [C engine/src/classm.ts:540-551].
   So the block is probably the fixture inputs, not k1e itself [I]. Once the wiring lifts `scope.k1`, these same
   cases compute and the block disappears [I].
4. **What has changed in xint since then.**
   - x1-sche has landed (`sche`, `f8582`, `rental`, `royalty` and the rest), so the Schedule E and Form 8582
     targets now exist. Lines 33 to 37 still do not. `sche.line41` = `copy sche.line26` [C sche.yaml:250-258].
     `f8582.required` = deductions ∧ ¬exception [C f8582.yaml:637-651].
   - k1p and k1s have landed, with their own `person.k1p_total_*` and `person.k1s_total_*`. Nothing reads them yet
     [C med-k1sche.md headline 2].
   - A `k1` topic exists in `tree.json`.
   - Personas **18 and 19 are taken** (`18_refused_nft_art`, `19_rental_house`), and so is 20. The next free numbers
     are 23 and up [C ls interview/2025/personas].
   - Order 266 is still free [C grep `order: 266`: none].
   - `f1040.line26` and `line3a` are now gated inputs [C f1040.yaml:265-273, 998-1005].
   - `f8960.line4a` = `s1.line5` [C git diff 825024d8 f8960.yaml].
   - The `scope.k1` help still says "A Yes ends the interview here" [C interview/2025/questions.yaml:1833-1838].
   - The v2 K-1 patches (k1p, k1s) are pending and touch the same shared files (`questions.yaml`, `defaults.json`)
     [C patches/v2/k1.md:9-18].
5. **Landing plan.** Land k1e in the K-1 integration batch, after k1p and k1s are wired, as its own sub-step:
   re-apply, wire, unpark, check, carry the reviews back, then run class M (section 4). The extra paid cost of k1e alone
   is about $2 to $5: class M whole, plus line-scoped reruns if the 4b/4c fix lands. Sampled screen and false-no
   reviews come on top, at about 19 subjects [I estimate].
6. **Owner decisions:**
   - Confirm D-K9, D-K11, D-K12 and D-K13. They were settled under delegation; the decision memo recommends confirming.
   - Choose the xrevk1e-01 fix: (a) register the reading, or (b) widen the screen and refuse.
   - Split `scope.k1` into a partnership/S-corporation question and an estate/trust question, or keep one question.
   - Decide the persona numbers.
   - Decide whether k1e lands in the K-1 integration batch or a later one.

---

## 1. What x2-k1e built (diff against base `825024d8`, read with git status and git diff --stat)

Lane-owned changes [C `git -C x2-k1e status --short`, `git diff --stat 825024d8`]:

| File | Change |
|---|---|
| `forms/2025/k1e.yaml` (new) | 1347 lines of YAML, 87 line ids. Screens `k1e.box9_any`…`box12_any` (refusing tick group); `interest_any`, `dividends_any`, `gains_any`, `other_any`, `business_any`, `codes_any` (box ticks); box amounts each behind a tick (`*_if_any`); `k1e.loss`, `material`/`box6_passive`/`box6_active`; code ticks 13 A/B, 14 A/H/I, `other_codes`; `h_negative`, `qbi_other`; `k1e.screen` (sum of every refusal, added to each output); outputs `interest`, `ord_div`, `qual_div`, `st_gain`, `lt_gain`, `collectibles`, `unrecap_1250`, `col_d`, `col_f`, `rre`, `sch_e_any`, `est_tax`, `backup_wh`, `taxexempt_int`, `nii_adj`, `qbi`, `reit` [C x2-k1e/forms/2025/k1e.yaml line ids 13-1329] |
| `forms/2025/person.yaml` | +221 lines: 18 `person.k1e_total_*` / `k1e_count_*`, each with `display:`, as one block before `person.rrta` [C x2-k1e.md:16-18] |
| `fixtures/2025/k1e.json` (new) | 19 cases, hand-predicted; 11 computed, 8 refusal; every case states `scope.k1: true` [C grep count 19] |
| `interview/2025/questions.yaml` | +164: groups `k1e_refused`, `k1e_boxes`, `k1e_codes`; 36 entries order 266 seq 1–36 [C x2-k1e.md:22-23] |
| `fixtures/2025/defaults.json` | 36 k1e defaults (script `docs/provisional/lanes/x2-k1e_work/defaults_patch.py`, idempotent, sorted insert) [C that file] |
| `ambiguities/2025.yaml` | `amb.2025.k1e_passive_default`, `amb.2025.k1e_portfolio_no_sche` [C git diff] |
| `tools/coverage/tree.json` | 8 gates under `other_income` (xint moved them to topic `k1`) [C xint.md:88] |
| `changes/2026/k1e.yaml` | C-X2K1E-K1E-01: box 10 cite "Schedule A, line 16" → "line 17e", and a `set` of the **whole** `k1e.screen.refuses` list (from/to) [C x2-k1e/changes/2026/k1e.yaml] |
| `docs/provisional/DECISIONS.md` | §6 (D-K9, D-K11, D-K13, D-K14, D-K16 and four lane decisions) [C git diff] |
| Untracked, from xrev-new | `bug_pending/xrevk1e-01.md`; `reviews/2025/{render,transcription}/k1e.{index,rulings}.json`; `reviews/2025/transcription/adjudication/k1e.md`; 2 `reviews/store/{render,transcription}/*.md` [C git status `??`] |
| Generated / not the lane's | `rendered/2025/*`, `reports/2025/*`, `reports/2027/shared_refs_from_2026.*`, `canonical/` (from the scratch build: rebuild before reading it), `sources/` + `tools/sources/*.json` (nx-src's archive, already in xint as a superset) [C x2-k1e.md:127; xint.md:90] |

Parked documents (in xint under `docs/provisional/lanes/x2-k1e_work/`): `coverage_k1e.yaml` (11 rows:
`k1e.portfolio_heir`, `trust_business_passive`, `codes_estimated_tax`, `box9`, `box10`, `box11_final_year`,
`box12_amt`, `rental_loss`, `foreign_taxes`, `nii_negative`, `qbi_ptp`), `persona_18_k1_estate_heir.yaml`,
`persona_19_refused_estate_final.yaml` (end `refused: person[taxpayer].k1e[mom_estate].box11_any`), the three walks,
`k1-wiring-k1e.md` (the contract), `k1-integration-plan.md` (draft for all three K-1 forms) [C ls; file heads].

**Lost or volatile:**
- The scratch wiring scripts (`/tmp/x2-k1e/scratch/apply.py`, `revert.sh`) are gone: `/tmp/x2-k1e` has no `scratch/`.
- The generators (`gen_form.py`, `gen_fixtures.py`, `gen_person.py`, `gen_changes.py`) survive only in `/tmp/x2-k1e`.
  Copy them into `x2-k1e_work/` before /tmp is cleared [C ls /tmp/x2-k1e].

Verification the lane reported (not rerun here; testimony as of 2026-11-15 16:15) [C x2-k1e.md:108-128]:
- The 19 k1e fixtures matched the hand predictions on the first run.
- `citations --strict` gave 0 findings, and `year_changes --check` applied every entry.
- On the scratch wiring, the 11 coverage rows gave 0 problems, and persona 18 completed.
- Mutation and `check_all` were not run.
- xint's check r2, which included k1e, passed: test-fixtures 2158/2158, and 357/357 with --ny [C xint.md:92-93].

## 2. Why it was deferred, and how firm that reason is

- **The stated reason.** "class M cannot build a k1e log before the K-1 wiring" [C xint.md:207]. The review lane found
  no class M job [C x2-k1e/reviews/2025/transcription/adjudication/k1e.md, last section]. `check_logs` reported
  `classm logs [claude]: 55/56 forms logged; missing: k1e` [C /tmp/xrev-new/k1e.checklogs.txt:79].
- **What class M requires.** A case is a candidate only when every value derived for the entry is computed ("a refusal
  anywhere in the entry … puts the case outside the hand-worked scope") and a job can be built from it
  [C engine/src/classm.ts:540-551].
- **Likely cause [I].**
  - Every k1e fixture states `scope.k1: true` [C k1e.json grep: 19 of 19]. That refuses the return at
    `scope.schedule1` [C scope.yaml:1188-1190].
  - k1p and k1s fixtures leave `scope.k1` at its default, and their class M cases were built
    [C classm.json `classm.k1p.1`: no `scope.k1` input].
  - So k1e's block probably comes from its fixture inputs, not from anything the wiring alone can supply.
  - **Not checked:** whether a job built from a k1e case without `scope.k1` would also fail on another refusal, for
    example from a `k1e.screen` operand. This is a free test (`node engine/dist/main.js classm-jobs --docs k1e
    --include-fixtures` on a copy with `scope.k1` removed from `k1e.json`), but it cannot run tonight.
- **Other likely reasons [I].**
  - The release tonight gates on `tools/release_reviews.sh`. With k1e in the tree, at least 6 screen subjects and 13
    gate subjects would have been due and never reviewed [C /tmp/xint/quick-r3.log:147-152, 334-337 and following].
    Dropping k1e also removed that debt from the release.
  - The coordinator chose to "merge with k1p/k1s; rows and personas stay parked" [C xint.md:86].
- **Consequence.** After the wiring, `scope.k1: true` no longer refuses, so the existing k1e fixtures become class M
  candidates without restatement [I]. If the owner wants k1e to land **before** the wiring, as k1p and k1s did, the
  alternative is to restate the 19 cases without `scope.k1` and build class M then. That restatement changes inputs
  only, not expected values. It is a choice, recorded as decision O5.

## 3. What has changed in xint since x2-k1e's base

| Area | Then (x1-base) | Now (xint) | Effect on k1e |
|---|---|---|---|
| Schedule E / Form 8582 | absent | `sche.yaml` 378 lines, `f8582.yaml` 655 [C wc] | Targets exist. Lines 33–37 and `sche.line34a_*` do not: the integration adds Part III [C grep: `sche.line33`, `line37` missing] |
| `sche.line41` | — | `copy sche.line26`, note "Parts II to IV … refused (scope.k1, scope.farm)" [C sche.yaml:250-258] | Integration: `sum(line26, line32, line37)` |
| `sche.any` | — | rental-only choose [C sche.yaml:357-375] | `∨ Σ k1e.count_sche > 0` |
| `sche.nonpassive_net` | — | royalty only [C sche.yaml:298-306] | `+ Σ k1e.col_f` |
| `f8582.required` | — | `deductions ∧ ¬exception`; `exception` tests p5b, p5c, p4c, p4b ≤ $25,000, MAGI ≤ $100,000 [C f8582.yaml:637-680] | **The exception does not yet test "no interest as a beneficiary in rental real estate" or "rental with active participation were the only passive activities"** (i8582 p. 1). The integration adds `Σ k1e.rre > 0` and `Σ k1e.col_d > 0` (with the k1p and k1s passive rows) as failures of the exception. k1e income goes into `f8582.p5a` (line 2a) |
| `f8960.line4a` | `f8960.zero` | `copy s1.line5`, Dollars [C git diff f8960] | Columns (d) and (f) arrive through `s1.line5`. Still to wire: `f8960.line7` (currently `copy f8960.zero`, NonNeg [C f8960.yaml:320-326]) and `line13` |
| `f1040.line26`, `line3a` | inputs, gated | unchanged shape: `gated_by line26_if_estimated` / `line3a_if_ordinary` [C f1040.yaml:265-273, 998-1005] | The plan's "rename the input to `*_entered`" must keep the gates and restate every fixture that sets them (k1-integration-plan.md:56,58) |
| `u1250.line11` | `copy div.box2b_if_capital_gain` | same [C u1250.yaml:154-161] | `+ Σ k1e.unrecap_1250` (line 11, not line 5) |
| k1p, k1s | absent | landed; totals unread [C med-k1sche.md:38-40] | Same integration lane; shared files `person.yaml`, `questions.yaml`, `defaults.json`, `tree.json` |
| `tree.json` | no K-1 topic | topic `k1` (k1p 28, k1s/f7203 23 gates) [C xint.md:51-52,88] | k1e's 8 gates go into `k1` |
| Personas | 18, 19 free | 18 `refused_nft_art`, 19 `rental_house`, 20–22 taken [C ls] | Renumber: 23 and 24, or a range shared with k1p and k1s (their 15–17 are also taken) |
| Bank | order 266 free | still free; 265 and 267 are neighbours [C questions.yaml:1010, 2032] | No collision |
| `scope.k1` help | "A Yes ends the interview here." | same [C questions.yaml:1838] | Must change when lifted (MORNING-REPORT.md:126 lead) |
| `scope.k1` coverage rows | end `refused: scope.schedule1` | same; row `scope.estate_excess_deductions` also [C interview/2025/coverage/scope.yaml:217-223, 342-348] | Ends change (N9, D-K12): `estate_excess_deductions` → `…k1e[…].box11_any` (instance gate) |
| `categories.json` `estate_trust` | gate `scope.schedule1` | same [C tools/coverage/categories.json:323-327] | → k1e residual gates; `refused` stays true while box 11 and the others refuse (section 9.3) |
| Married-at-year-end lint | — | xint dropped `household.married_dec31` from f1040.json `stage13.refuse.joint_without_spouse` because `k1e.two_entries_and_spouse` was the only defaults-taking MFJ case [C xint.md:228-232] | Harmless when k1e returns (two cases then take the default). Run `/tmp/xint/tools/l5_restate.py` on `k1e.json` anyway: it is MFS-scoped and idempotent [C xint.md:115-119]; expect 0 changes [I] |
| NY | — | No NY line reads K-1 items directly. The IT-225 screen names "modifications passed through from … estate or trust" [C forms/ny/2025/ny_it201.yaml:206-208] | The NY fiduciary adjustment (IT-225 EA-901/ES-901 [C sources/ny/2025/ny_it225i.cols.txt:850]) stays behind that screen. NY line 555 copies the federal amount [C ny_it201.yaml:555-558]. No NY work for k1e [I] |
| 2026 | — | `changes/2026/*` now has f8582, rental and other entries | k1e's entry still applies [I: not rerun]. **Caution:** it `set`s all of `k1e.screen.refuses`, so any refusal added for the 4b/4c fix must also go into its `from` and `to` lists |

## 4. Landing plan (after the K-1 integration, or as the last step of it)

Prerequisite: k1p and k1s are wired by the integration lane, and that lane has lifted `scope.k1` from `scope.schedule1`.
If `P/round4/k1int.md` sets a different order, follow it. The steps below are k1e's part.

**Step 1. Re-apply the lane** (mechanical; Sonnet). Use x2-k1e's saved diff, the same way xint's `xfix_delta.sh`
rebuilt lanes from x1-base [C xint.md:211-213]:
- `forms/2025/k1e.yaml`, `fixtures/2025/k1e.json` and `changes/2026/k1e.yaml` as they are.
- The person block before `person.rrta`.
- The bank: 3 groups and 36 entries at order 266.
- The 2 ambiguities and DECISIONS §6.
- The 8 gates, under topic `k1`.
- Defaults by `defaults_patch.py`, run on the merged file.
- The 7 consumer rulings xint wrote and then removed: rule again, or re-take them from xint's history [C xint.md:93-95,
  209]. Pairs `k1e.interest_any`, `dividends_any`, `gains_any`, `other_any`, `business_any` @i1041sk1:p2, `codes_any`
  @p4, `box12_any` @f1041sk1:p2.

**Step 2. Wire** (judgment). Follow `x2-k1e_work/k1-wiring-k1e.md`, every row [C that file:17-38]:
- `sb.line2` ← interest; `sb.line6` ← ord_div; `f1040.line3a` ← qual_div; `sd.line5` and `sd.line12` ← st_gain and
  lt_gain; `g28.line4` ← collectibles; **`u1250.line11`** ← unrecap_1250.
- `sche.line34a_d` and `line34a_f` ← col_d and col_f, then lines 35, 37 and 41. `sche.line34b_*` and `line36` are 0.
- `f8582.line2a` / `p5a` ← col_d (Part V only, never Part IV). The `f8582.exception` failure on `rre > 0` or
  `col_d > 0` (section 3).
- `sche.any` ← count_sche; `sche.nonpassive_net` ← col_f.
- `f1040.line26` ← est_tax (not in line 37); `f1040.line25c` ← backup_wh; `f1040.line2a` ← taxexempt_int.
- **`f8960.line7` and `f8960.line13`** ← nii_adj. No `line4b` term.
- `person.qbi` ← qbi; `qbi.eligible` / `f8995.line6` ← reit.
- `sd.other_forms`: drop the K-1 clause.
- Remove `display:` from every total that is read [C k1-wiring-k1e.md:14-15; x2-k1e.md:127 build fact].
- **The roster must be read only behind `scope.k1` Yes.** In the scratch wiring, a target outside the gate made the
  one-W-2 filer answer an empty `$k1e` [C x2-k1e.md:148-150]. Persona 01's walk must not grow.
- Open item, not read: whether `eic`'s investment-income test needs columns (d) and (f) beyond lines 2a, 2b, 3b and
  Schedule D [C k1-wiring-k1e.md:45-46].
- Lead: `f1116.line3e` may leave out Schedule E and K-1 income [C MORNING-REPORT.md:125]. Decide when f1116 meets
  k1e income [I].

**Step 3. Interview** (judgment; the interview lane, K6). Read `docs/2026-11-13_interview_construction_protocol.md`
first.
- `scope.k1` help: drop "A Yes ends the interview here". Decide on the split (decision O3).
- Recheck the 36 k1e prompts and their help against N1–N12. They were written before tonight's N10 and wording passes
  [I].
- Possible saving: 4b and 4c are two steps for every long-term-gain filer [C x2-k1e.md:151].

**Step 4. Unpark** (mechanical).
- Move `coverage_k1e.yaml` to `interview/2025/coverage/k1e.yaml`.
- Move the personas to `interview/2025/personas/23_k1_estate_heir.yaml` and `24_refused_estate_final.yaml` (or the
  agreed range). Each persona's `end` keeps the instance gate.
- Restate the ends of `scope.k1` and `scope.estate_excess_deductions` (N9, D-K12). Then run
  `interview-coverage --write`.
- Record the before and after walks for 01 (nothing), 23 (typical) and 24 (refused). Before = refused at
  `scope.schedule1`.

**Step 5. Fix or register `xrevk1e-01`** (decision O2). Either change triggers line-scoped transcription and render on
k1e.
- (a) Register `amb.2025.k1e_parts_of_4a`. No arithmetic change.
- (b) Widen `k1e.gains_any` to "box 3, 4a, 4b or 4c". Refuse 4b/4c > 0 when 4a ≤ 0. Add a fixture. Update the
  `changes/2026/k1e.yaml` `from`/`to` lists.
- Recommendation: (b). The defect drops tax silently [C x2-k1e/bug_pending/xrevk1e-01.md: "tax understated if the case
  occurs"], and a refusal fails safe. Owner's call.
- File the entry with `new_bug.py` and get it numbered at the batch merge. It is not in xint's inventory today.

**Step 6. Checks** (in the lane's worktree, fast tier, then full at the batch):
- build; `test-fixtures` (19 k1e cases plus the restated `f1040.line26`/`line3a` cases); `citations --strict`;
  `year_changes --check`; `tree.py --check`; `check_consumers`; `tick-groups` (the three k1e groups become reachable:
  today they are "not checked here" [C /tmp/xint/quick-r3.log]); `interview-rules`; `interview-coverage`.
- **mutate** on k1e: not yet run. The cases cover both sides of every choose, each `loss` operand and each
  `sch_e_any` operand [C x2-k1e.md:156-157].
- Engine differential: say in the note whether any external engine computes Form 1041 K-1 income. Not checked [I].

**Step 7. Review data and reviews.**
- **Carry back first.** Run `tools/worktree_data.py carry-back x2-k1e` (dry run, then real) for the 2 cost rows and the
  `.transcription` triage. Take the 5 tracked review files and the 2 store files with xint's `take_reviews.py` method
  [C xint.md:222-227]. Do not rerun what is already paid for: the logs answer `k1e.yaml` as written at 12:30, and the
  reviews ran at 17:11 [C file times].
- Then run the due reviews in section 6.

## 5. Refusals to keep (k1e residual gates; all on `k1e.screen`, refusal order = asking order)

[C x2-k1e.md:52-57; changes/2026/k1e.yaml `to` list]

| Gate | What it refuses | Why it stays |
|---|---|---|
| `k1e.box9_any` | Box 9 directly apportioned deductions | Form 8582 / Schedule E columns (c) and (e): loss side not built |
| `k1e.box10_any` | Box 10 estate tax deduction (Schedule A line 16; 2026: 17e) | Schedule A other-deduction line not built |
| `k1e.box11_any` | Box 11 final-year deductions (11 A excess deductions → `s1.line24k`; carryovers) | The commonest estate loss (D-K9 note); a later candidate [C decisions.md:240] |
| `k1e.box12_any` | Box 12 AMT items | No Form 6251 route for them exists [C x2-k1e.md:74-75] |
| `k1e.loss` | Negative box 6, 7 or 8 | Passive rules for beneficiaries not issued (i1041sk1 p. 2) |
| `k1e.other_codes_if_codes` | 13 C–ZZ, 14 B (foreign tax), 14 E, 14 F, others | 14 E needs Form 4952; 14 B interacts with the foreign tax credit (D-K14) |
| `k1e.h_negative` | Negative 14 H | MAGI effect depends on the trust's statement (i8960 p. 13) |
| `k1e.qbi_other_if_14i` | PTP income and cooperative items in the 14 I statement | Form 8995-A |

Not asked and not refused, which overstates income and never understates it: a statement reporting a disposition of
a passive activity [C x2-k1e.md:159-160].
Pending defect: 4b/4c with 4a blank (section 4, step 5).

Gates retired at landing: `scope.k1` leaves `scope.schedule1` for the `estate_trust` share. This is the integration's
change, not k1e's alone.

## 6. Fixtures and reviews

**Fixtures.**
- `fixtures/2025/k1e.json`: 19 entry-level cases [C x2-k1e.md:40,115]. They stay as written; the integration plan
  keeps them entry-level [C k1-integration-plan.md:105-106].
- To add:
  - Return-level k1e cases: scout-k1 FK-series rows for estates, and an estate heir through `sb`, `sd`, `u1250`,
    `f8960.line7`/`13` and `f8582` Part V.
  - A 4b/4c case if fix (b) lands.
  - One case where `col_d > 0` breaks the Form 8582 exception when there is a rental loss. This is the only k1e path
    that changes another form's limit [I].
- Class M: `classm.k1e.*` comes from `classm-jobs --docs k1e --include-fixtures` after the wiring. First confirm, free
  of charge, that it builds jobs.

**Reviews** (protocol 6.1 [C docs/2026-11-15_coverage_expansion_protocol.md:229-236]). One per form per round,
after all fixes:

| Subject | Kind | Status |
|---|---|---|
| k1e (new) | transcription, render | **Done** ($1.35), adjudicated (10 representation, 2 ambiguity, findings = xrevk1e-01). Carry back. Rerun line-scoped only if step 5 (b) changes the form |
| k1e (new) | class M | **Due**, whole. No log exists, so run it directly (`rerun_all.py` plans only forms with a log [C x2-k1e.md:133-134]). The x2-k1e note gives no price; about $1–3 [I] |
| person (k1e block) | transcription, render, line-scoped | Due. The lane's dry run priced person transcription plus render at $3.01, over the $3.00 gate [C x2-k1e.md:135-136]. In the integration this falls inside person's single review for the round |
| sb, f1040, sd, g28, u1250, f8960, qbi/f8995, sche, f8582, scope | line-scoped transcription (plus render where wording changes); class M for f8960, f8995, person, sche | The integration lane's debt, shared with k1p and k1s [C k1-integration-plan.md:107-109] |
| 6 k1e screens (`box9_any`…`box12_any`, `other_codes`, `qbi_other`) and ≥ 13 `gate:k1e.*` subjects | screen review, sampled per release | Due before a release that includes k1e [C /tmp/xint/quick-r3.log:147-152, 334-337 and following] |
| `k1e.box11_any` (final K-1), `k1e.material` | false-no | Due. These are the two "answer No wrongly" risks [C x2-k1e.md:65-66] |
| k1e | completeness | Due, sampled |
| 36 k1e questions, `scope.k1` help | question review | Due |

## 7. Owner decisions

- **O1. Confirm D-K9, D-K11, D-K12 and D-K13 as settled for k1e** (income only; order 266; coverage-row ends change;
  a portfolio-only K-1 puts no row on Schedule E). They were settled under delegation [C x2-k1e
  DECISIONS.md §6]. Recommendation: confirm [C decisions.md:240-249]. The lane's own decisions also need confirming:
  - box 6 passive unless the 500-hour test is met;
  - boxes 7 and 8 always passive;
  - 14 H positive goes to line 7 **and** line 13;
  - box 12 and 14 E refused.
- **O2. xrevk1e-01:** (a) register the reading, or (b) widen the screen and refuse. Recommendation: (b), because it
  fails safe.
- **O3. `scope.k1` split.** Either keep one question or split it into "partnership or S corporation" and "estate or
  trust", so that a beneficiary is not asked the 1065 and 1120-S rosters (N8) [C k1-integration-plan.md:88-91]. This
  belongs to the interview lane, but it changes the coverage-row ends for all three K-1 forms.
- **O4. Persona numbers** for k1e (and for k1p/k1s, whose scout numbers 15–17 are also taken). Proposed: 23–24 for
  k1e.
- **O5. Timing.** Either (i) land k1e with the K-1 integration, which is the plan above and matches the coordinator's
  18:45 decision, or (ii) land it earlier, as k1p and k1s did: restate the 19 fixtures without `scope.k1` and build class
  M before the wiring. Recommendation: (i). The block in (ii) is inferred, not tested, and k1e adds nothing to a
  return until it is wired.
- **O6. Spend.** The k1e-only spend is about $2–5, plus its share of the integration's line-scoped reviews and the
  sampled screen, false-no and question reviews [I estimate]. Any single run over $3.00 needs `--approve-cost`.

## 8. What this report did not check

- Whether `classm-jobs` would build k1e jobs from cases without `scope.k1`.
- Whether `year_changes --check` still applies `changes/2026/k1e.yaml` on xint.
- Whether the k1e bank entries still pass `interview-rules` under tonight's N-norm changes.
- The EIC investment-income question.
- Any engine-differential coverage.

All of these need runs or source reading that tonight's rules exclude, or that belong to the integration lane.
