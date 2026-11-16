# Lane b1-mutB: mutation survivors of lanes F9 and F5, and interview-rules on the merged tree

Model claude-opus-5-5, class judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/b1-mutB`, the final
goal-1 merge (B1, 0c8cd21d). Nothing committed; no paid review, no model call. Lane b1-mutA takes the 71 s2/AMT
survivors of BUG-0656; this lane takes the 12 of lanes F9 (household 7, s3 3) and F5 (scveh 2).

## (1) Mutation survivors

Each fixture below was predicted by hand from the source named in its `evidence_note` before it was run; all six
passed as predicted on their first run (`test-fixtures` 2034/2034). No existing expected value changed; cases were
appended at the end of each file, nothing reformatted. Kills were checked one mutant at a time before the full run
(`/tmp/b1mutB/killcheck.mjs`: the data and the mutant evaluated on the named cases).

| Mutant | Disposition |
|---|---|
| `refusal.household.household.hoh_fails.0` | killed: `b1mutB.household.single_child_hoh_missed` (line 12e refused at `household.hoh_missed` -> $15,750) |
| `operand.household.household.hoh_missed_cost.hoh_missed_person.then0` | killed: `b1mutB.household.single_member_not_test2` |
| `filter.household.household.test2_lived_persons` | killed: `b1mutB.household.single_member_not_test2` |
| `boundary.household.household.hoh_missed_person` | killed: `b1mutB.household.single_member_not_test2` (0 > 0 vs 0 >= 0) |
| `operand.household.household.hoh_missed_person.test2_lived_persons.gt.0` | killed: `b1mutB.household.single_member_not_test2` |
| `operand.household.household.hoh_missed_person.test2_absence_persons.gt.1` | killed: `b1mutB.household.single_child_hoh_missed` (1 > 0 vs 1 > 1) |
| `operand.household.household.hoh_missed_test2.no.then1` | equivalent on every input: pinned argument in `EQUIVALENT_IF` (below) |
| `operand.s3.s3.adoption_if_any.adoption_final_if_adoption.all.0.eq.0` | killed: `b1mutB.s3.adoption_not_final` |
| `operand.s3.s3.prior_amt_if_forms.prior_amt_deferral_if_amt` | killed: `b1mutB.s3.prior_amt_exclusion_items_only` |
| `refusal.s3.s3.line14.6` | killed: `b1mutB.s3.form2439_line14` (the Form 2439 refusal F9 added without a regression case) |
| `operand.scveh.scveh.part3_reached.part2_reached.all.0.eq.0` | killed: `b1mutB.veh.part3_reached` |
| `operand.scveh.scveh.part3_reached.line11.all.1.any.1.lt.1` | killed: `b1mutB.veh.part3_reached` |

The new cases:
- `fixtures/2025/household.json`: `b1mutB.household.single_child_hoh_missed` (single, never married, a 4-year-old
  child all year, home cost paid: refused at `household.hoh_missed`, i1040gi p. 14 Test 2);
  `b1mutB.household.single_member_not_test2` (the same with an unrelated household member as the only dependent:
  not a Test 2 person, p501 Table 4; single stands, line 12e $15,750).
- `fixtures/2025/s3.json`: `b1mutB.s3.adoption_not_final` (2025 expenses, adoption not final: no 2025 credit, i8839
  p. 3; line 7 $0), `b1mutB.s3.prior_amt_exclusion_items_only` (2024 AMT from exclusion items only: no Form 8801
  credit, i8801 p. 1; line 7 $0), `b1mutB.s3.form2439_line14` (Form 2439: line 14 and 15 refused at
  `sd.f2439_if_dividends`, Schedule 3 line 13a).
- `fixtures/2025/scveh.json`: `b1mutB.veh.part3_reached` (a $30,000 passenger car placed in 2025, no section 179, no
  special allowance: Part II and Part III of the p946 worksheet reached; line 11 $12,200, line 16 $0).

The argument (`engine/src/mutate.ts`, after the `hoh_community_property` arguments):
`operand.household.household.hoh_missed_test2.no.then1`. `dependents_any` is a known false only on a known empty
roster (it counts `dependent.one`, the parameter 1, with no filter); there both Test 2 counts are 0 and
`hoh_missed_person` is false, `household.no`'s value. Where `dependents_any` is unknown (roster not given), both
alternatives are ways and neither refuses, so the line is that guard's unknown on both routes (spec 4.7.3). Digest
pinned with `premiseDigest` on this build (`cd28e80f5ed1cd7e`); `holds` true.

Refund mutant (`operand.refund.refund.worksheet.no.then0`): the integrator's argument is gone from `EQUIVALENT_IF`,
and the added expectation `refund.received_if_worksheet` $0 in `g1f4.refuse.refund.two_itemized` kills it
(data $0, mutant $2,000, by killcheck); the full run's result is below.

Full run (`MUTATE_WORKERS=8 node engine/dist/main.js mutate`, about 1 h 55 min under load average 110 to 250):
7758 mutants, 431 surviving (was 443): 353 equivalent on every input, 7 on answered inputs only, **71 unexplained,
all lane b1-mutA's** (60 s2, 6 person.amt_dep, 5 amt parameters); none of this lane's 12 remains, and the refund
mutant is no longer a survivor (killed). 0 stale arguments; every self-test 0 problems; sampled check: 113 keyed
arguments, 300 generated returns and 2034 fixture cases at 4 rates, 0 problems; the new argument `holds` on all sets
(9336 sets, 6307 reaching, 5714 exercising). Exit 1 only on b1-mutA's 71.

## (2) interview-rules

`node engine/dist/main.js interview-rules` (defaults) on this tree, with the integrator's baseline: **0 problems**
(293 walks, 995 random traversals, 269 complete returns classed; 2 early-completion, 11 out-of-order and 4
asked-and-unread templates, all held). So the integrator's pending rerun is confirmed. Each of the eight B1 findings
was reproduced on its witness (the run's own random seeds, `SEED * 1000 + walk index + s * 100003`, recomputed by
`/tmp/b1mutB/probe_exact.mjs`) and traced. None is fixed here; each is kept in `tools/interview_rules_baseline.json`
with its traced cause replacing "cause not traced at B1" (keys unchanged).

| Finding | Cause | Lane |
|---|---|---|
| `dependent.disabled` early completion (generated.375, dep_c: household member, 15) | read by the age branches of the qualifying-child test (`qc_age_younger`, `qc_age_19`, `qc_age_student`); a random order completes while they still read it; either answer changes nothing (T2's probe). | none: lines unchanged since g1-base; witnessed because the merged generator and data moved the seeded sample (T2 already saw it on its own sweep) |
| `eic.legally_separated`, `eic.same_home` out of bank order (generated.327, hoh) | `eic.step3_married` is an any-test; on hoh, `eic.married_rules` reads `household.married`, and while `married_dec31` is unanswered the any reads its later operands. | none (as above; T2 saw `legally_separated`) |
| `ny_it201.ask.moved_out` out of bank order (ny.generated.933) | `ny_it201.moved` is any[moved_in, moved_out]; a Yes to moved_in makes moved_out moot, and a random order can ask moved_out first. A seq change cannot fix an order the check draws at random. | none (lines identical at g1-base) |
| `dependent.born_died`, `placed` (ny.generated.1130), `kidnapped`, `months` (ny.generated.1379) asked and unread | lane **g1-f9**'s T-304 (1) chain: on a single return with a dependent and `household.home_cost` Yes, `household.hoh_missed_person` counts `household.test2_lived_persons`, whose filter reads `dependent.hoh_test2_lived`; its two all-tests read on past an unknown `dependent.claimed` / `qualifying_child` into `dependent.hoh_lived_half` (months and kidnapped via `lived_half`; born_died then placed via `hoh_part_year`). The person then turns out neither claimed nor a qualifying child. With `home_cost` false on the same inputs none of the four is asked (checked on both witnesses). Before the round `hoh_test2_lived` was read only on the head of household path. | **g1-f9** |

Why not fixed: none of the eight yields to a question order/seq change (the out-of-order and early-completion ones
are drawn in random orders; the F9 four are read ahead by expressions). The gating corrections that would fix them
are expression changes: for the F9 four, new choose lines in `forms/2025/dependent.yaml` so that
`dependent.hoh_lived_half` is read only once `dependent.claimed` (first branch) or `dependent.qualifying_child`
(second branch) is known true; for eic, `same_home` asked only after `married_rules` is known true; for New York,
`moved_out` asked only after a No to `moved_in`. Each adds mutants (another mutation run), and needs class M and render
review of the form; FOR THE COORDINATOR. The F9 one is the one worth doing: it asks up to four needless questions of a
single filer with a non-qualifying dependent who paid the home's cost.

## Files changed

- `fixtures/2025/household.json`, `fixtures/2025/s3.json`, `fixtures/2025/scveh.json` (cases appended)
- `engine/src/mutate.ts` (one argument added)
- `reports/2025/mutation.md` (regenerated by the run)
- `tools/interview_rules_baseline.json` (reasons of the eight B1 entries; keys unchanged)
- `docs/provisional/lanes/b1-mutB.md` (this file)

## Verification

- `npm run build`: OK. `test-fixtures`: 2034/2034 (2028 + 6 new).
- `mutate` (federal): above. `mutate --ny` not run (no New York data or fixture changed).
- `interview-rules`: 0 problems before and after the baseline reason edit (two full default runs).
- Not run: check_all (per brief), `test-fixtures --ny`, other checks (no form, question or tool changed).
- Probe scripts (not in the tree): `/tmp/b1mutB/killcheck.mjs`, `digest.mjs`, `probe_exact.mjs`, `probe_override.mjs`.

## Reviews for round 2

None: no form, expression, question or interview text changed by the mutation half; fixtures added only.
