# Lane mexist (round 7): unexplained survivors on changed existing lines

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/mexist` (detached at
6649c637). Patch: `round7/mexist.patch` (fixtures only; no change to `engine/src/mutate.ts`). Scratch tools and specs:
`scratch/round7-mexist/` (`genspec.py` holds every case with its note; `check.mjs` is the kill check).

## Summary

- Family: 47 survivors (the "not yet explained" rows of reports/2025/mutation.md outside f1116/ftc, K-1/7203 and
  rental/sche/royalty/rprop).
- **32 killed** by 24 new fixture cases in 13 form files, each value predicted by hand from the archived sources
  before the evaluator ran. All 42 expectations agree with the engine; no engine defect found, no pending bug drafted.
- **15 open**: 2 witnessed mutants whose only witness was an incomplete input set (they look equivalent on answered
  inputs), and 13 of the 15 "equivalence candidates" (the other 2 were killed by hand-built cases). Drafted reasoning is below. **No keyed argument was added**: the
  ones I could argue are equivalent only on answered inputs or only on inputs the interview can produce, and I could not
  run the sampled check that would hold them (no full mutate allowed), so I left them for the integrator rather than
  risk a failing argument.
- No survivor of mine is flagged "no reader on any value sheet" in the worklist, so none was skipped on that ground.
  `boundary.f8919.f8919.files` comes close: its only difference is a helper read only by display conditions (see
  below). The structural "no observable reader" rule may cover it.
- Lane MW's addendum (`witness/existing.addendum.md`) had not appeared when I finished. I checked once at the end.

### Verification (what was checked, and how)

- Checked: `scratch/round7-mexist/check.mjs` loads the fixtures as the engine does (`loadFixtureCases`). For each new
  case it evaluates the expected keys on the data and on each mutant (`mutations(data)`, `m.apply`), and compares them
  with the fixtures' comparison (`normal`, as in mutate.ts and mutant_witness.mjs). Result: 42/42 expectations OK, and
  32/32 mutants change an expected value. `node engine/dist/main.js test-fixtures` in the worktree: 2410/2410 passed, including all 24 mexist cases.
- Not checked (inferred): the full `mutate` step on the merged tree (the coordinator forbade a full mutate). I did not
  use `mutant_witness.mjs --only` for the kills, because it searches for witnesses, not expectations.
  Kill-by-expectation is what check.mjs measures. I infer that the integrator's mutate run will count these 32 as
  killed by fixtures. Mutate's comparison could differ from my reimplementation, which I have not observed.
- Diff is additions only (`git diff --numstat`: 0 deletions in every file).

## Killed (fixture case, expected keys, evidence)

| Mutant | Case (file) | Expected keys | Kind of kill |
| --- | --- | --- | --- |
| operand.person.person.earned_not_w2.{household_wages_if_pay, line1c, line1d, f8919_wages, line1h} (5) | mexist.person.earned_not_w2.mw_in_box1 (person.json) | f2441.line4/5/18/19 = $4,000 | value ($8,000 under each mutant) |
| operand.person.person.dc_earned.earned_not_w2 | mexist.person.dc_earned.se_only (person.json) | f2441.line4/5 = $45,910 | value |
| operand.person.person.f4137_line10.f4137_line10_figured.then0 | mexist.person.f4137_line10.gov_tips (person.json) | f8919[form].line8 = refusal (gate tips_gov_if_rows) | refusal vs $32,700 |
| operand.person.person.f4137_filed.f4137_col_c.gt.0 | mexist.person.f4137_filed.noncash_only (person.json) | person.f4137_filed = false | value (gate line) |
| refusal.person.person.line1d.0 | mexist.person.line1d.mw_1099_over (person.json) | f1040.line1d = refusal (mw_1099_over) | refusal vs $2,000 |
| operand.s1a.s1a.line4b.zero.then0 | mexist.s1a.line4b.no_part2_with_f4137 (s1a.json) | s1a.line4b = $0 | value |
| operand.s1a.s1a.line13_ssn.line13_amount.then1 | mexist.s1a.line13.schedule1_refused (s1a.json) | s1a.line13 = Schedule 1 refusal | **refusal detail only** (mutant gives the line 5 refusal) |
| operand.f8959.f8959.line4.line2 | mexist.f8959.line4.f4137_tips (f8959.json) | f8959.line2 $4,700, line4 $32,700 | value |
| operand.f8959.f8959.line4.line3 | mexist.f8959.line4.f8919_wages (f8959.json) | f8959.line3 $10,000, line4 $180,000 | value |
| operand.f8962.f8962.alloc.divorced_enrolled.any.1.eq.0; refusal.f8962.f8962.line25.0 | mexist.f8962.dependent_filer.no_allocation (f8962.json) | alloc false, line9 false, line25 refusal (dependent_filer) | value; refusal vs $0 |
| operand.ssb.ssb.line8.base_single.then3 | mexist.ssb.line8.hoh (ssb.json) | ssb.line8 $25,000 | value |
| boundary.f4137.f4137.line5_over | mexist.f4137.line5_equals_line4 (f4137.json) | line5_over false, line6 $0, line12 $0 | value/refusal |
| operand.f4137.f4137.line5_over.line5.gt.0 | mexist.f4137.reported_over_unreported (f4137.json) | line5_over false, line6 $2,700, line13 $206.55 | value/refusal |
| refusal.f4137.f4137.line8.0 | mexist.f4137.line8_rrta (f4137.json) | line8 refusal (rrta), line12 $68.15 | refusal vs $28,000 |
| operand.eic.eic.check_27c.married_rules.any.2.all.2.eq.0 | mexist.eic.check_27c.mfs_no_us_home (eic.json) | f1040.line27c false | value |
| operand.eic.eic.check_27c.married_rules.any.3.all.2.eq.0 | mexist.eic.check_27c.mfs_qc_of_another (eic.json) | f1040.line27c false | value |
| operand.retirement...dis_split.dis_early_if_disability...; ...dis_wages... (2) | mexist.retirement.dis_split.after_min_age (retirement.json) | retirement[p].dis_split false | value (gate line) |
| filter.f2441.f2441.mfs_qp_count; boundary.f2441.f2441.mfs_qp_home | mexist.f2441.line_a.mfs_apart_no_qp (f2441.json) | f2441.line_a false | value |
| operand.f2441.f2441.line20_all.line19 | mexist.f2441.line20.mfs_spouse_deemed (f2441.json) | f2441.line20 refusal (mfs_spouse_deemed) | refusal vs $5,000 |
| operand.sa.sa.itemizes.standard.any.2.gt.1 | mexist.sa.itemizes.qss_dependent (sa.json) | f8960.line9a refusal (sa.dep_qss) | refusal vs $0 |
| operand.f4952...exception.line4c...; ...line1_if_interest... (2) | mexist.f4952.exception.filing_4952 (f4952.json) | f4952.line3 $2,520, sd.line20 false | **unknown only** (mutants read lines the base leaves unanswered) |
| operand.scveh.scveh.macrs_heavy.line19.then0 | mexist.scveh.macrs_heavy.suv_q1 (scveh.json) | f4562 line21/26h/28 $7,740 | value |
| operand.f8960.f8960.line5d.line5c | mexist.f8960.line5d.no_gains (f8960.json) | f8960.line5d $0 | **unknown only** (base intentionally leaves Schedule 1 unanswered) |
| operand.f8960.f8960.line9c.zero | mexist.f8960.line9c.digital_nii (f8960.json) | line9c, 9d, 11 $0 | refusal vs $0 |

Each case's evidence_note gives the derivation and page cites. Where an expectation is a refusal, the note predicts
which gate refuses. The refusal object was copied from the evaluator after it matched that gate.

Hand-built inputs (not witness sets as given). I checked each against the bank's gates with `inputsAhead` (no
unanswered input reached), and give a plausibility note:
- eic.check_27c cases: the witness base had eic.us_home unanswered. A married-filing-separately return never asks it,
  because Step 4 question 1 stops first. The cases answer it (false; or true with lived_with_relative and
  qc_of_another) so the mutants yield a value, not unknown. **These answers are ones the interview does not ask on an
  MFS return.** The expectation (box not checked) holds whatever they are (i1040gi p. 41), which is the point of the
  fixture. The integrator should decide whether answers the interview never asks are acceptable in a stage fixture.
- f2441.line_a: the witness base was incomplete. Mine is MFS, lived apart the last 6 months, paid home cost, and has a
  15-year-old dependent (not a qualifying person), with no care. Plausible.
- dis_split: the witness toggled disability without the follow-up. I answered dis_early = false (paid after the
  minimum retirement age). Plausible.
- f4137 line 8: rrta true together with W-2 tips. This is the exact situation the gate refuses. Plausible.
- f4137 reported_over_unreported: col_d raised to $6,000 while W-2 box 7 stays $4,000. Slightly inconsistent but
  harmless to the lines expected.
- line1d: an inconsistent pair of answers (1099 amount more than the pay not in box 1). The refusal exists to catch it.

Weak kills, flagged: s1a.line13_ssn (refusal detail), both f4952.exception mutants and f8960.line5d (unknown only).
They count under mutate's definition, but they rest on which refusal comes first or on an unanswered input. The f4952
`line1_if_interest` mutant is in fact equivalent on answered inputs: with line5 = 0 and no carryover, line8 =
min(line1, line6) and line6 = line4h ≥ line4c (4e ≤ 4d makes 4f ≥ 0). So `4c > line8` ⇔ `4c > line1`. Only the unknown
differs. `line4c → line4h` is genuinely non-equivalent: a short-term gain makes 4f > 0 with 4c ≤ line1 < 4h. A value
fixture for it needs a return with a short-term sale and investment interest, which I did not build.

## Open (15)

| Mutant | Status | Analysis (inferred unless marked) |
| --- | --- | --- |
| operand.eic.eic.check_27c.has_qc.any.3.all.1.eq.0 | open (likely answered-only equivalent) | Witness W8 differs only unknown vs refusal. Disjunct 4 with has_qc → show5. If QC is true, disjunct 2 (R ∧ QC ∧ step3_married ∧ ¬mfj ∧ Q) is true on both routes, because ¬married_rules makes step3_married true. If QC is false and the other conjuncts hold, Step 4 Q5 stops, so eligible is false and show5 is false, which matches ¬QC. Checked: a complete combat-pay variant gives the same value on both routes (true). Needs an ANSWERED_ONLY argument; not written. |
| operand.f8962.f8962.show_applicable.any.all.0.eq.0 | open (answered-only equivalent, checked on one case) | The mutant equals `applicable` (applicable ⇒ applicable_figured), so it differs from `any ∧ applicable` only with no Form 1095-A. Then b_zero_month (lines 12a-23a > 0) is false, so b_zero and two_counted are unchanged. Display of lines 7, 8a and 8b moves. Checked on a complete no-1095-A copy of W2: two_counted false on both routes. The witness differed only through unanswered fpl_table and ptc_files. |
| refusal.eic.eic.step2_other.1 | open | Reaches 180 inputs; the worklist says no reader differs. Not analysed further. |
| operand.household.household.joint_unmarried.no.then0 | open | Reads rdp_community_property (status ≠ mfj ∧ community property ∧ RDP) on the married branch. Not analysed further. |
| operand.household.household.mfs_apart_last6.mfs_living_if_mfs.any.1.eq.0 | open | The second disjunct reads mfs_living_else (the together_late parameter), so it is never apart_all_year. The mutant drops "apart all year". Readers (eic.yaml:701, f2441 line A) appear to absorb it: no reader differed on 260 inputs. A candidate kill is MFS apart all year with a qualifying person and care (f2441 line A). Not tried for lack of time. |
| operand.household.household.cp_marriage_ended.cp_not_joint.then2 | open | For MFS, cp_not_joint vs cp_unmarried differ only when community_property is false and cp_unmarried is true. cp_unmarried needs married false, which an MFS return seems to rule out (married_dec31 asked). Not proven. |
| operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0 | open | Not analysed. |
| operand.f8853c.f8853c.has_line17.line17_if_periodic.gt.0 | open | Not analysed. |
| operand.person.person.f8919_line10.f8919_line10_figured.then0 | open (likely equivalent) | Read only as Schedule SE line 8c. With X = 8a + 8b equal to Form 8919 line 8, floor0(W − X − min(L6, floor0(W − X))) = floor0(W − X − L6), so SE line 9 agrees on values. Checked on x2pay.f8919.w3: only the helper differs. Refusal paths (rrta: Form 8919 line 8 refuses, SE's own rrta handling) not traced. |
| operand.person.person.f4137_line6.zero.then1 | open (answered-only equivalent) | In the filed = false branch, col_c is a known 0, so the implicit Form 4137's line 4 = floor0(0 − col_d) = 0 = person.zero. It differs only if col_d is unknown. Read by f8959.line2. |
| operand.person.person.mw_has_1099.mw_1099_if_not_box1.gt.0 | open (equivalent on interview-producible inputs) | It only decides whether mw_business (gated_by mw_business_if_1099) is read. With pay not in box 1 but no 1099, the mutant reads mw_business, which the interview never asks there. Checked: with it unanswered, only the helper differs. With an answer the interview cannot produce (true), line 1d would refuse. |
| operand.sa.sa.mortgage_interest_not_mfs.has_mortgage_interest.all.0.eq.0 | open | Not analysed (time cut in the search). |
| operand.f8863.f8863.show_after4.eligible.all.0.eq.0 | open (same class as mw_has_1099) | It differs only on MFS with f8863.paid true. The interview does not ask paid on MFS (mfs.f8863.no_credit note), so it is false there. Checked on that case: no difference. |
| operand.s1.s1.nol_limit_test.nol_amount_if_nol.all.0.lt.1 | open | Not analysed. |
| boundary.f8919.f8919.files | open (display only) | Checked on x2pay.f4137.noncash_only: only f8919[form].files (a helper) differs. All 8 of its readers are shown_when display conditions. A candidate for the structural no-observable-reader rule. |

Count: killed 30 of the 32 witnessed + 2 former candidates = 32; open 2 + 13 = 15; 32 + 15 = 47.

## Notes for the integrator

- No `// ---- lane mexist begin/end ----` block was added to EQUIVALENT_IF (no argument met the bar).
- An observation, not filed as a bug: f2441's "considered unmarried" test (mfs_qp_count) counts only dc_qp, which
  requires care expenses (f2441.care). i2441's qualifying person does not require expenses. This matters only when
  there are no care expenses, and then no credit is claimed. I see no wrong amount.
