# Lane x2-k1e: Schedule K-1 (Form 1041), estates and trusts — income only

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/x2-k1e` (detached,
base x1-base `825024d8` plus newly archived sources, review data cloned). No commit, no claims, no paid reviews, no
model calls from code. Not run: `tools/check_all.sh` (brief), mutate (brief), a clean full `test-fixtures` /
`interview-coverage` (base broken; coordinator 14:35: own fixtures and rows only).
Design: `docs/provisional/lanes/scout-k1.md` §3.4 (lane K3); its decisions settled as it recommends, with the
corrections in §3 (recorded in `docs/provisional/DECISIONS.md` §6). Return wiring: `/tmp/k1-wiring-k1e.md`; draft
plan for the whole K-1 return integration: `/tmp/k1-integration-plan.md` (copies of both in `x2-k1e_work/`).

## 1. What the merge must know

- **Nothing on the return reads k1e yet.** `scope.k1` still refuses every K-1 holder through `scope.schedule1`, and
  no return line reads `person.k1e_*`. The k1e questions are therefore unreachable in this tree; they open when the
  integration lane wires the totals and takes `scope.k1` out of `scope.schedule1` (`/tmp/k1-wiring-k1e.md`).
- `person.yaml`: 18 new lines `person.k1e_total_*` / `person.k1e_count_*`, inserted as one block before
  `person.rrta`. Each carries `display:` so the build accepts it unread; **drop `display` from each total the
  integration wires**.
- `fixtures/2025/defaults.json`: the base copy from `nx-b1` (brief) plus 36 k1e defaults inserted in input order
  (no other entry changed). Patch script: `/tmp/x2-k1e/defaults_patch.py` (copy in `x2-k1e_work/`), idempotent;
  rerun it on the merged file.
- `interview/2025/questions.yaml`: 3 groups (`k1e_refused`, `k1e_boxes`, `k1e_codes`) appended to `groups`, 36
  entries at order 266 (seq 1–36) appended at the end of `questions`. No other entry touched.
- `ambiguities/2025.yaml`: 2 entries appended (`amb.2025.k1e_passive_default`, `amb.2025.k1e_portfolio_no_sche`).
- `tools/coverage/tree.json`: 8 gates appended (topic `other_income`; move them if x1-sche adds a Schedule E topic).
- `docs/provisional/DECISIONS.md`: §6 appended.
- Coverage rows and personas are **not** in `interview/2025/` (unreachable here): `x2-k1e_work/coverage_k1e.yaml`
  (11 rows), `persona_18_k1_estate_heir.yaml`, `persona_19_refused_estate_final.yaml`; move them at integration.
  Rows `scope.k1` and `scope.estate_excess_deductions` (scope.yaml) change their ends then (N9, D-K12): the latter to
  `k1e.box11_any`.
- Persona numbers 18 and 19 (the scout gave 15–17 to k1p/k1s).
- No line of sche/f8582/s1/f1040/sd/f8960/qbi was edited.

## 2. What changed

| File | Change |
|---|---|
| `forms/2025/k1e.yaml` (new) | collection `k1e`, parent `person`; 87 lines (generator `/tmp/x2-k1e/gen_form.py`) |
| `forms/2025/person.yaml` | 18 sums over k1e |
| `fixtures/2025/k1e.json` (new) | 19 hand-predicted cases |
| `changes/2026/k1e.yaml` (new) | change C-X2K1E-K1E-01 |
| shared files | §1 |

**Computed now (per K-1, summed per person):** box 1 interest; 2a/2b dividends; 3 and 4a net capital gains; 4b
(28% rate) and 4c (unrecaptured §1250, asked only when 4a > 0); box 5 → Schedule E line 33 (f); boxes 7, 8 →
column (d) (rentals are passive "even if you materially participate", p925 p. 5); box 6 → (d), or (f) when the
beneficiary worked > 500 hours in that business (`k1e.material`, test 1 only); 13 A estimated tax (→ 1040 line 26,
not line 37); 13 B backup withholding; 14 A tax-exempt interest; 14 H positive (→ Form 8960 line 7 and MAGI line 13);
14 I QBI (may be negative) and section 199A dividends; `k1e.sch_e_any` (a portfolio-only K-1 adds no Schedule E row);
`k1e.rre` (box 7, for the Form 8582 rental-exception test, i8582 p. 1).

**Still refused (gate, reason):** `k1e.box9_any` (deductions: Form 8582 / columns (c),(e)); `k1e.box10_any` (Schedule
A line 16); `k1e.box11_any` (final-year deductions, line 24k, carryovers); `k1e.box12_any` (Form 6251); `k1e.loss`
(negative box 6, 7 or 8: beneficiary passive rules not issued); `k1e.other_codes_if_codes` (13 C–ZZ, 14 B foreign
taxes, 14 E, 14 F, others); `k1e.h_negative` (MAGI effect depends on the trust's statement); `k1e.qbi_other_if_14i`
(PTP income, cooperative items). All sit on `k1e.screen`, which every per-K-1 result adds (zero), so a refused K-1
refuses every person sum it enters; the refusal order is the asking order.

**Questions (order 266):** seq 1 `$k1e` ("For this person … — In 2025, did you get a Schedule K-1 (Form 1041) from
an estate or a trust? …"); 2–5 tick group `k1e_refused` "Does any of these boxes of this Schedule K-1 show an
amount?" (boxes 9, 10, 11, 12; refusing, first and alone); 6–11 tick group `k1e_boxes` "Which of these boxes … show an
amount?" (1, 2a, 3 or 4a, 5, 6/7/8, 13 or 14); 12–22 the box amounts in printed order, each only behind its tick;
23 `k1e.material` (only when box 6 > 0); 24–29 tick group `k1e_codes` (13 A, 13 B, 14 A, 14 H, 14 I, any other code —
refusing); 30–36 the code amounts, the code I statement amounts and `k1e.qbi_other`. Full wording: the bank.
Who could answer No wrongly: box 11 on a final K-1 (help names it); `k1e.material` (a beneficiary who runs the trust's
business as trustee — help says own work only; effect limited to column (d)/(f), amb).

## 3. Decisions (alternative rejected)

- D-K9 income only, as the scout (rejected: `s1.line24k` for 11 A). **Correction to the scout:** it put all of boxes
  6–8 behind material participation; rentals (7, 8) are passive regardless (p925 p. 5), so only box 6 is asked.
- 14 H: the scout wired line 7 only; i8960 p. 13 also increases MAGI (line 13). Negative refused (rejected: a second
  question on whether the trust marked a MAGI adjustment).
- Box 12 refused: the scout's "existing `s2.amt` remedy" does not exist in this tree (only `s2.amt_pab`, `amt_boat`,
  `amt_business`).
- 14 E refused with other codes (rejected: accepting it as information unless Form 4952 is used — needs an f4952
  edit outside this lane).
- Box 6–8 and 14 H entered as signed amounts with derived refusals (rejected: a separate "is it a loss?" question).
- No 2b ≤ 2a / 4b+4c ≤ 4a consistency refusal: no archived sentence states it for the 1041 K-1.
- 2026: the scout read the f1041sk1 diff as a 28%-gain line change; it is box 10's Schedule A line 16 → 17e.

## 4. Gates replaced and residual refusals

None replaced in this lane (`scope.k1` stays until integration). New residual gates: the 8 above, placed in
`tree.json`. At integration: `scope.k1` leaves `scope.schedule1`; `categories.json` `estate_trust` → covered with
these residual gates.

## 5. Next year

`changes/2026/k1e.yaml`: C-X2K1E-K1E-01 (draft f1041sk1 p. 3 "Schedule A, line 17e"; i1041sk1 p. 3): box 10 cite and
refusal text. Nothing else the form cites changes (sentence diff of both 2026 drafts read). Change-map entry for
`research/ty2026/changes.md` (Business section), to add in the bookkeeping commit: "C-X2K1E-K1E-01. Estate tax
deduction (K-1 1041 box 10) moves to Schedule A line 17e — Kind: wording; Touches: k1e.box10_any, k1e.screen."
No new parameters. `year_changes.py --check`: all 131 entries apply.

## 6. Defects

None filed.

## 7. Requests

- Integration lane: `/tmp/k1-wiring-k1e.md` (every total, its destination and source, incl. u1250 **line 11** for
  4c, f8960 line 13, f8582.required via `k1e.rre`).
- Round 2 reviews (§9).

## 8. Verification (what was run; what was seen)

Run on this worktree (base x1-base, defaults copied from `nx-b1` + the k1e patch). "Base" = failures that name nothing
of this lane.

| Command | Result |
|---|---|
| `node engine/dist/main.js build` (lane tree) | OK, after two fixes found by it (`k1e.nii_adj`, `k1e.rre` typed Dollars: a sum of a signed box cannot be proved non-negative) |
| `render`, `render --ny` | OK (69 + 12 files) |
| `test-fixtures` | **all 19 `k1e.*` cases pass.** Values matched the hand predictions on the first run; the 8 refusal cases first failed only because their expected `cite` lacked `revision/snapshot/tax_year` (fixture format; gates were right). Whole suite 1412/2030: the 618 failures are base (598 `s2.amt_owed` stale input, rest f4952/f8960/sd/ssb cases with no k1e entry) |
| `python3 tools/citations.py --strict` | 0 findings (final tree, after the scratch was reverted, 16:15) |
| `python3 tools/year_changes.py --check` | all 131 entries apply (incl. `changes/2026/k1e.yaml`) |
| `python3 tools/year_shared_refs.py --year 2026` | 0 references |
| `python3 tools/coverage/tree.py --check` | fails on 6 base gates (household.hoh_missed, refund.two_itemized_if_two, s2.amt_pab_over, s3.business_credit_any, s3.business_fuel_any, sd.f2439_if_dividends); none of the 8 k1e gates |
| `check_consumers.py` | base findings only (sc, scveh, sd, s2, f8863, sa); none k1e/person.k1e |
| `transcription/check_questions.py`, `check_screens.py`, `check_false_no.py` | exit 0; k1e gates/questions not listed (unreachable in this tree) |
| `siblings.py --check`, `check_bug_inventory.py` | base findings only (g1-*, landing, ty26) |
| `interview-rules` | 18 problems, all base (s2.amt_owed walks, dependent/ny reach); none k1e |
| `tick-groups` | passed; the 3 k1e groups "not checked here" (behind an answer the background never gives) |
| `interview-coverage` (year rows) | not completed (stopped at the coordinator's 14:35 instruction) |
| `year_changes.py --check` (final tree) | all apply |
| Coverage rows + personas, **scratch wiring** (applied, built, checked, then reverted: `scope.k1` out of `scope.schedule1`, a throwaway return form `zzk1e` summing the 16 person totals behind `scope.k1`, as `full` targets; `display` stripped) | `interview-coverage --rows x2-k1e_work/coverage_k1e.yaml`: **11 rows, 0 problems** (3 computed rows complete; 8 refusals each told at its own question, on the row's answer). `draft-walk`: persona 18 completes with 0 problems; persona 19 refused at `…k1e[mom_estate].box11_any` (its `end` was then rewritten to the instance id; not re-walked). Found by the scratch: a wired total that keeps `display:` fails the build ("marked display but read"), and a row's `refused` must name the instance gate. The script: `/tmp/x2-k1e/scratch/apply.py`, `revert.sh`. `canonical/` in the worktree is from the scratch build (generated; rebuild before reading it) |
| `mutate`, `check_all.sh` | not run (brief) |


## 9. Review debt (round 2)

- k1e new: transcription, render, class M, run **whole and directly** (`rerun_all.py` plans only forms with a log:
  its dry run listed person only). Class M needs k1e class M cases.
- person: transcription and render line-scoped (dry run: $1.69 + $1.32 = $3.01, above the $3.00 gate); class M person
  request could not be built in this tree (base).
- Screen / false-no samples for the 8 new gates and question reviews for the 36 questions, once reachable.

## 10. Walks

Scratch-wired tree (transcripts in `x2-k1e_work/walks/`). Before (this base): an estate heir is refused at
`scope.schedule1` on the `scope.k1` tick.
- Typical heir (persona 18, W-2 + estate K-1 with boxes 1, 2a/2b, 4a): the k1e topic is **12 questions on 9 screens**
  (roster; refusing screen of 4 boxes; screen of 6 boxes; amounts 1, 2a, 2b, 3, 4a, 4b, 4c). Whole walk 144 questions /
  67 screens vs 127 / 58 for the one-W-2 filer — the other extra steps are the dividend/capital-gain questions the
  income opens elsewhere [I, not itemized].
- Refused heir (persona 19): roster, then the first screen (box 11 ticked) — refused at the topic's second step.
- Filer with nothing: in the scratch the one-W-2 filer was asked `$k1e` (an empty list) although `scope.k1` was No,
  because the scratch target `zzk1e.rows` was not behind `scope.k1`. With the real wiring the roster must be read only
  after `scope.k1` Yes (0 extra steps); the integrator should check this walk.
- Possible saving left: boxes 4b and 4c are two steps for every long-term-gain filer, typically zero.

## 11. Left open (rank order)

1. Wiring (integration lane): totals, `scope.k1`, rows and personas moved, `display` dropped.
2. Mutation of k1e at integration (cases cover both sides of every choose, each `loss` operand, each `sch_e_any`
   operand; not run).
3. 14 E as information when Form 4952 is not used; 11 A via `s1.line24k`; box 12 via Form 6251 — coverage candidates.
4. A statement reporting a disposition of a passive activity (i1041sk1 p. 2) is neither asked nor refused: it can only
   free the filer's own suspended losses (return overstates income, never understates).
5. Estimated gain [E, scout]: +0.2 to +0.3 points of returns (estate/trust 0.4%; final-year K-1s with box 11 are the
   main residual). Unmeasured.
