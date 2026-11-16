# Lane x2-dep: filers who can be claimed as a dependent (TY2025, federal)

Model: claude-opus-5-5 · Class: judgment · Year: 2025 · Jurisdiction: us (New York: one fixture; no New York form changed)
Worktree: `.claude/worktrees/x2-dep` · Base: `825024d8` (`refs/scratch/x1-base`) · Design: `scout-dependent-filers.md`
No commits, no paid reviews, no model calls from code. `check_all.sh` not run, `mutate` not run (brief, base caution).
`fixtures/2025/defaults.json` was replaced by the copy from `.claude/worktrees/nx-b1` to build (base caution); this lane
adds no input, so it has no defaults patch, and that file is restored to the base before hand-off.

Done: batch D (the dependent standard deduction and its ripple), batch Q (the bound worksheet def, unread until Form
8615). Not done: batch K (Form 8615), not started (the coordinator's deadline); Form 8814 stays refused.

Batch Q verification (run, then the scratch removed): a temporary display line in `qdcg` bound `qdcg_amount` to the
worksheet's own lines 1 to 3 and `f1040.status`. Over every evaluable fixture case outside class M (1,374 of 1,386; 12
rejected by the base's undeclared inputs), it equalled `qdcg.line25` in every case: 1,047 money values (single 680, mfj
182, hoh 141, mfs 31, qss 13; 31 with the 15% band in use, 2 with the 20% band), 275 refusals, 52 unknowns. The
scratch line is not in the hand-off; the def has no reader until Form 8615, so its lines are unobserved by fixtures and
mutation until then.

## 1. What the merge must know

**Stop-and-report: one expected value outside the pre-authorized list.** `fixtures/2025/dependent.json`
`stage8.single.filer_is_dependent` expects the `sa.dependent` refusal on 13 lines. It changes for the same reason as the
scout's list (the refusal became a computation), but the scout's list does not name it, so it is **not edited** and fails
`test-fixtures` in this tree. The values the evaluator now gives, checked against the source (single, wages $120,000,
dependent worksheet capped at $15,750, taxable income $104,250, 2025 single rates: 1,192.50 + 4,386 + 12,072.50 + 24% x
$900 = $17,867; no dependent, so no credit; $12,000 withheld): `f1040.line12e` 15,750; `f1040.line19` 0; `f1040.line34`
0; `f1040.line37` 5,867; `s8812.clw_a1`, `clw_a3`, `clw_a5`, `line13` 17,867; `s8812.earned_covers` true;
`s8812.from_part_iib`, `line14`, `line16a`, `line17` 0. Restate on the coordinator's word.

Shared-file changes (all by id; existing lines changed are listed):

| File | Change |
|---|---|
| `forms/2025/sa.yaml` (mfs-l2 also edits) | **Changed:** `sa.dependent` (label and source: the dual-status clause dropped); `sa.standard` (its false branch reads `sa.standard_amount` for `sa.standardraw`; its refusal `when: sa.dependent` replaced by `when: sa.dep_qss`); `sa.deduction` (its `sa.dependent` refusal removed). **New:** `sa.dep_earned_sum`, `sa.dep_earned`, `sa.dep_add`, `sa.dep_plus`, `sa.dep_min`, `sa.dep_line2`, `sa.dep_line3`, `sa.dep_line4a`, `sa.dep_line4b`, `sa.dep_line4c`, `sa.dep_qss`, `sa.standard_amount` (inserted before `sa.standard`) |
| `forms/2025/eic.yaml` | `eic.step4`: its `refuses: sa.dependent` removed |
| `forms/2025/f8962.yaml` (mfs-l3 owns) | **New:** `f8962.dependent_filer` (after `f8962.any`). **Changed:** `f8962.line24`'s refusal list (`&id003`, which `f8962.line25` shares) gains a first entry `when: f8962.dependent_filer`; first so that the refusal is told on entering a Form 1095-A, before the other Form 8962 questions (N11) |
| `forms/2025/qdcg_amount.yaml` | new def (batch Q) |
| `tables/2025/qdcg_zero_ceiling.yaml`, `qdcg_fifteen_ceiling.yaml` | new hand-written keyed tables |
| `tools/check_qdcg_ceiling.py` | new check, with `--self-test`; **not wired into check-all** (request below) |
| `params/2025.yaml` | `sa.dep_min` 135000, `sa.dep_add` 45000 |
| `ambiguities/2025.yaml` | `amb.2025.sa_dep_earned`, `amb.2025.sa_dep_qss` |
| `interview/2025/questions.yaml` | `sa.dependent` help: "A Yes ends the interview here." removed |
| `interview/2025/coverage/dependent_filers.yaml` | new (3 rows) |
| `interview/2025/personas/14_dependent_student.yaml` | new |
| `tools/coverage/tree.json` | row `sa.dependent` replaced by `sa.dep_qss` (everyone/status); row `f8962.dependent_filer` added (ptc) |
| `reviews/2025/consumers.json` | 7 rulings, all "same": `consumer:sa.dependent@` `i8962:p3` (new pair), `i1040gi:p18`, `p34`, `p35`, `p41`, `p42`, `f8880:p2` (baseline pairs reopened because the question's text changed) |
| `fixtures/2025/classm.json` | `classm.tipjob.1`: input `s2.mortgage_subsidy: false` added (inputs only; the case sets `sa.dependent: true` and now evaluates into the AMT screen; the default's value; its expected values are unchanged and pass) |
| `fixtures/2025/{sa,eic,f2441,f8863,f8880,f8962,sli}.json`, `fixtures/ny/2025/it201.json` | new cases appended (section 8); 3 restated (below) |
| `tools/coverage/categories.json` | not touched: the integrator sets `dependent_filer` `refused: false` and drops `sa.dependent` from its `gates` |

Restated, pre-authorized (D1), each from the source:
- `sa.json` `stage4.refuse.standard.dependent`: `sa.standard` refusal → $15,750 (wages $100,000: line 2 $100,450, line 3
  $15,750, line 4a $15,750); `sa.itemizes` refusal → false (no itemized deductions, no election).
- `sa.json` `stage4.refuse.dependent_itemizes`: `sa.deduction` and `f1040.line12e` refusal → $15,750.
- `f1040.json` `stage9.eic.refuse.dependent_of_another`: `f1040.line27a` refusal → $0 (Step 4 q. 6 "STOP You can't take
  the credit"); `f1040.line27c` refusal → false (that STOP does not say to check 27c; the scout predicted true).
- Coverage rows: no existing row ended on `sa.dependent` (grep), so none restated.
- Class M (scout's list): `classm.json` `eic.9`, `clcw.3`; `classm.deepseek.json` `sa.5`, `f4952.3`, `clcw.3`,
  `f8889.1` pass unchanged; `tipjob.1` needed the one input above.

## 2. What changed

Computed now: a return where someone can claim you (or, on a joint return, your spouse), at single, married filing
jointly and head of household (married filing separately goes with the MFS lanes; line 3 already has its amount):
- The Standard Deduction Worksheet for Dependents (i1040gi p. 35): earned income by the printed formula; line 2 as the
  larger of earned income plus $450 and $1,350 (the same amount as the worksheet's Yes and No; Pub. 501 p. 24 states it
  so); line 3 the basic amount for the status; line 4b the existing age and blindness boxes. Itemizing is open to such a
  filer (no refusal).
- EIC: a claimable filer without a qualifying child gets "no credit" at Step 4 q. 6 (the value was already encoded); one
  with a qualifying child takes Step 3, which asks no dependency question (pinned).
- Downstream paths now reached, each pinned by a fixture: no dependents and no child tax credit for a claimable filer
  (Step 2 q. 4); head of household with a qualifying person the filer cannot claim only because they are claimable (Pub.
  501 HOH note 3); education credits and the saver's credit barred only when claimed (`person.sav_claimed`), allowed when
  only claimable; student loan interest barred when claimed; New York item C Yes and the $3,100 standard deduction.

Still refused (gate, reason):
- `sa.dep_qss`: a qualifying surviving spouse someone can claim; the worksheet gives no amount for the status
  (amb.2025.sa_dep_qss).
- `f8962.dependent_filer`: a claimable filer with a Form 1095-A (i8962 p. 3, "No one can claim you as a dependent").
- `f2441.nondependent_gate` (existing): a claimable parent paying for care is asked the qualifying-person question and
  refused on Yes (pinned by `dep.care_parent_claimable_refused`). This is where most claimable parents with care costs end.
- `scope.unearned_2700` / `scope.f8615` (Form 8615) and `scope.f8814`: unchanged; batch K not built.
- `household.filer_under16`: kept (decision D2).

## 3. Decisions

In `docs/provisional/DECISIONS.md`, "Filers who can be claimed as a dependent (lane x2-dep)". Lane choices, each with the alternative rejected:
- Line 2 as `larger_of(earned + $450, $1,350)` rather than the printed Yes/No `choose` on "more than $900": the two are
  equal at every amount (at $900 both give $1,350); the choose could not prove line 2 non-negative and left an
  equivalent gt/ge mutant.
- Earned income entered as zero when the formula's total is negative (Pub. 501 Table 8 line 1, "If none, enter -0-"),
  rather than signed; line 2 is the same either way; pinned by `dep.earned_below_zero`.
- QSS refused on the worksheet's silence, not as conflicting answers: the scout's premise was wrong. i1040gi, Qualifying
  Surviving Spouse, condition 2c allows a QSS who "could be claimed as a dependent on someone else's return". No
  consistency rule was added.
- The Form 8962 refusal was placed first in line 24's list rather than last, so the filer is told on entering the form.

## 4. Gates replaced and residual refusals

Removed: the `sa.dependent` refusals on `sa.standard` and `sa.deduction`, and on `eic.step4`. `sa.dependent` is no
longer a refusal gate (tree.json row retired). New residual gates: `sa.dep_qss`, `f8962.dependent_filer`, both placed in
tree.json and walked by coverage rows. Not measurable by the estimate (unmeasured list).

## 5. Next year (protocol 7.1)

- Rev. Proc. 2025-32 (archived, final) section 4.14(2): for 2026 the dependent standard deduction "cannot exceed the
  greater of (1) $1,350, or (2) the sum of $450 and the individual's earned income". `sa.dep_min` and `sa.dep_add` are
  unchanged: a "no change" row. The proposed id is `C-X2DEP-SA-01`, for the change map and the README table (the
  coordinator's bookkeeping).
- The 2026 i1040gi is not archived, so the worksheet's locators await it; no `changes/2026` file is written. List
  `sa.dep_min` and `sa.dep_add` for `propose_params.py --from 2025 --to 2026`.
- Q: the two ceiling tables need their 2026 rows at adoption (Rev. Proc. 2025-32 section 4.03, per the scout:
  49,450/98,900/66,200 and 545,500/613,700/306,850/579,600; not re-read by this lane). `check_qdcg_ceiling.py --year
  2026` will hold them equal to the 2026 parameters. List both tables for the adoption step.
- `year_changes.py --check`: passes (no operation touches a changed line).

## 6. Defects

None filed. The base breakages are not this lane's (section 8).

## 7. Requests

- Coordinator: authorize the `stage8.single.filer_is_dependent` restatement (section 1).
- Integrator: wire `tools/check_qdcg_ceiling.py` (and `--self-test`) into check-all, as for the other hand-written
  tables' checks; add the two tables to `docs/ty2026/ADOPTION.md`.
- `person.yaml` owner: gate `person.sav_claimed` on `sa.dependent` (decision D7), which removes a question for every
  non-dependent student and saver (N8).

## 8. Verification

| Command | Result |
|---|---|
| `node engine/dist/main.js build` | OK on the final tree (with the lane's fixtures' interview paths), defaults from nx-b1 |
| `test-fixtures` | an earlier full run (before the coordinator's deadline message): all lane cases and the 3 restated pass; other failures are the base's (598 `s2.amt_owed` undeclared, 18 `sd.qof` unknown, `stage4.sb.foreign_no_filing`) and `stage8.single.filer_is_dependent` (section 1). On the final build, the lane's 23 federal cases (69 values, including the 3 restated and `classm.tipjob.1`) were evaluated directly: all pass |
| `test-fixtures --ny` | `ny.dep.item_c_single` passes; the other 214 failures are the base's `s2.amt_owed` and `sd.qof` |
| `interview-coverage --rows interview/2025/coverage/dependent_filers.yaml` | 0 problems (3 rows) |
| `tick-groups` | 0 problems |
| `citations.py --strict` | exit 0 |
| `check_consumers.py` | no `sa.dependent` finding left; other findings are the base's |
| `check_questions.py`, `check_screens.py`, `check_false_no.py` | exit 0 |
| `tree.py --check` | 7 findings, none for this lane's gates (other lanes' gates not placed) |
| `siblings.py --check`, `check_bug_inventory.py` | findings only for other lanes' pending entries |
| `year_changes.py --check` | exit 0 |
| `check_qdcg_ceiling.py`, `--self-test` | ok; 6/6 |
| `interview-rules` | not run (coordinator: own fixtures and rows only) |
| `mutate`, `ny_compare`, check-all | not run (brief) |

Fixtures added (hand-predicted before running; every prediction matched the evaluator): `sa.json` `dep.pub501_ex1`,
`dep.pub501_ex3_blind`, `dep.pub501_ex4_business_loss` (class A for the deduction, Pub. 501 Examples 1, 3, 4),
`dep.capped_at_basic`, `dep.joint_both_claimable`, `dep.self_employed_se_half`, `dep.scholarship_counts`,
`dep.earned_below_zero`, `dep.qss_refused`, `dep.hoh_claimable_parent`; `eic.json` `dep.eic_no_child_step4_q6`,
`dep.eic_with_child_step3`; `f2441.json` `dep.care_parent_claimable_refused`; `f8863.json` `dep.edu_claimed_no_credit`,
`dep.edu_claimable_not_claimed`; `f8880.json` `dep.saver_claimed_no_credit`, `dep.saver_claimable_not_claimed`;
`sli.json` `dep.sli_claimed_no_deduction`; `f8962.json` `dep.marketplace_refused`; `fixtures/ny/2025/it201.json`
`ny.dep.item_c_single`. Branches: both sides of line 2's `larger_of` (D1/D3), of 4a's `smaller_of` (D3/D4), of the
`sa.standard_amount` choose, of the earned-income floor, and both statuses of `sa.dep_qss`.

Mutation, expected (not run): every arithmetic operand of the new lines is asserted by a case above. External engines:
not mapped (protocol 5.6 lane E); the scout found Tax-Calculator, PolicyEngine and UsTaxes compute this deduction
(UsTaxes from wages only, which would differ on D3, D6 and D7).

## 9. Review debt (round 2; no dry-run estimate made)

- `sa`: transcription (line-scoped: the 12 new lines, `sa.standard`, `sa.deduction`), class M, render (the
  `sa.dependent` label).
- `eic`: transcription (`eic.step4`).
- `f8962`: transcription (`f8962.dependent_filer`, line 24), class M.
- `qdcg_amount` (new def): transcription, class M (whole), once Form 8615 reads it.
- Screen and false-no samples: `gate:sa.dep_qss`, `gate:f8962.dependent_filer`.
- Question review: `sa.dependent` (help changed).

## 10. Walks

Persona 14 (`14_dependent_student`, typical filer, new): completes after 128 questions; `sa.dependent` is asked as
before, and no new question is asked. Personas 01 and 07 (nothing in the area): both complete. Against the committed
after-walks (`docs/provisional/walks/after/`) the only difference from this lane is the `sa.dependent` help (36 → 30
words); the other differences come from the base's lanes. No before-walk was made on this base (a 25-minute build under
load average ~130; the change cannot reach a filer who answers No).

## 11. Left open, in rank order

1. Batch K (Form 8615 and topic 277), which also makes `qdcg_amount` read and testable through a real line.
2. `stage8.single.filer_is_dependent` restatement (section 1).
3. `person.sav_claimed` gate (D7).
4. A joint return where only one spouse is claimable: the worksheet's "your earned income" is read as the return's
   (amb.2025.sa_dep_earned); no archived text settles it.
5. Child AMT (§59(j)) for a dependent child with large unearned income: archive Rev. Proc. 2024-40 (scout R4).
