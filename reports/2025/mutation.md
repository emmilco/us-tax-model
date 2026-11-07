# Mutation score — implemented worksheets

Single-atom mutations applied to the canonical data; a mutant is killed if the
build-time checker fails on it or if any fixture case's value changes. Fixture
expectations are the recorded values checked in the previous run (the same values
the fixture test compares).

| Metric | Value |
| --- | --- |
| Mutants | 5156 |
| Killed by the checker | 1015 |
| Killed by fixtures | 3855 (35 only by class M cases) |
| Surviving | 286 (279 provably equivalent on every input; 7 equivalent on answered inputs only) |
| Mutation score (raw) | 94.5% |
| Mutation score (mutants provably equivalent on every input excluded) | 99.9% |
| Mutation score (also excluding those equivalent on answered inputs only) | 100.0% |

## Killed only by class M cases

A class M rerun regenerates its cases, so these kills can be lost. Before replacing a case named here,
keep it (or a stage fixture with the same facts and source-predicted values) among the stage fixtures.

| Mutant | Kind | Location | First class M case killing it |
| --- | --- | --- | --- |
| operand.dependent.dependent.qc_age.younger.any.0.all.1.eq.0 | replace an operand | dependent.dependent.qc_age | classm.f1040.5.deepseek |
| operand.dependent.dependent.dc_child_all_year.qc_dependent.all.0.eq.0 | replace an operand | dependent.dependent.dc_child_all_year | classm.f2441.2.deepseek |
| operand.f1095a.f1095a.b_jan.mo_b.then0 | replace an operand | f1095a.f1095a.b_jan | classm.f1095a.1.deepseek |
| operand.f8863.f8863.ban_refused.line1.all.0.gt.0 | replace an operand | f8863.f8863.ban_refused | classm.f8863.4.deepseek |
| filter.f8880.f8880.line2a | remove collection filter | f8880.f8880.line2a | classm.f8880.2.deepseek |
| boundary.f8880.f8880.clw_room | replace strict greater-than with inclusive | f8880.f8880.clw_room | classm.s3.2.deepseek |
| operand.f8880.f8880.clw_room.clw3.gt.0 | replace an operand | f8880.f8880.clw_room | classm.s3.2.deepseek |
| operand.f8880.f8880.can_take_tax.no.then1 | replace an operand | f8880.f8880.can_take_tax | classm.s3.2.deepseek |
| operand.f8889.f8889.age55_line3.married_family.all.1.eq.0 | replace an operand | f8889.f8889.age55_line3 | classm.f8889.5.deepseek |
| operand.f8962.f8962.alien_branch.line5.all.1.lt.0 | replace an operand | f8962.f8962.alien_branch | classm.s3.2.deepseek |
| operand.household.household.ctc_ssn.id_count.all.1.eq.0 | replace an operand | household.household.ctc_ssn | classm.s3.4.deepseek |
| operand.person.person.sav_simple_plan.zero.then0 | replace an operand | person.person.sav_simple_plan | classm.f8880.2.deepseek |
| operand.s3.s3.line15.line9 | replace an operand | s3.s3.line15 | classm.s3.2.deepseek |
| operand.sales.sales.wash_over.b | replace an operand | sales.sales.wash_over | classm.f1040.6.deepseek |
| operand.sales.sales.wash_bad.wash_loss.all.1.gt.0 | replace an operand | sales.sales.wash_bad | classm.g28.2.deepseek |
| operand.sc.sc.f7206_line7.zero.then1 | replace an operand | sc.sc.f7206_line7 | classm.sc.1 |
| operand.scveh.scveh.line9.line9_actual.then1 | replace an operand | scveh.scveh.line9 | classm.f8960.2.deepseek |
| operand.scveh.scveh.bonus_fullcase.bonus_forty.then1 | replace an operand | scveh.scveh.bonus_fullcase | classm.f1040.4.deepseek |
| operand.scveh.scveh.bonus_2025.bonus_fullcase.then0 | replace an operand | scveh.scveh.bonus_2025 | classm.f1040.4.deepseek |
| operand.scveh.scveh.line19_hy.rate_hy.rate | replace an operand | scveh.scveh.line19_hy | classm.sc.2 |
| operand.scveh.scveh.line19_2025.line19_hy.then0 | replace an operand | scveh.scveh.line19_2025 | classm.sc.2 |
| operand.scveh.scveh.macrs_heavy.line19.then0 | replace an operand | scveh.scveh.macrs_heavy | classm.se.3 |
| operand.scveh.scveh.q4_basis.zero.then1 | replace an operand | scveh.scveh.q4_basis | classm.scveh.3 |
| operand.scveh.scveh.cost179_o.zero.then1 | replace an operand | scveh.scveh.cost179_o | classm.s179.4 |
| operand.sdtw.sdtw.line5.line3 | replace an operand | sdtw.sdtw.line5 | classm.f1040.2.deepseek |
| minmax.sdtw.sdtw.line7 | swap smaller_of/larger_of | sdtw.sdtw.line7 | classm.f1040.2.deepseek |
| operand.sdtw.sdtw.line13.line10 | replace an operand | sdtw.sdtw.line13 | classm.f1040.2.deepseek |
| operand.sli.sli.divisor.divisor_other.then2 | replace an operand | sli.sli.divisor | classm.sli.1 |
| operand.ssb.ssb.line8.base_single.then3 | replace an operand | ssb.ssb.line8 | classm.ssb.4 |
| operand.ssb.ssb.line8.base_single.then4 | replace an operand | ssb.ssb.line8 | classm.ssb.6 |
| operand.ssb.ssb.line10.adjust_single.then3 | replace an operand | ssb.ssb.line10 | classm.ssb.4 |
| operand.ssb.ssb.line10.adjust_single.then4 | replace an operand | ssb.ssb.line10 | classm.ssb.6 |
| boundary.w2.w2.has_box10 | replace strict greater-than with inclusive | w2.w2.has_box10 | classm.f2441.2.deepseek |
| operand.w2.w2.has_box10.box10.gt.0 | replace an operand | w2.w2.has_box10 | classm.f2441.1.deepseek |
| boundary.w2.w2.box10_bad | replace strict greater-than with inclusive | w2.w2.box10_bad | classm.w2.1.deepseek |

## Surviving — equivalent on answered inputs only

Each argument below is proven only on returns where the answers it names are given; with them withheld a
partial return can tell the mutant apart (spec 4.7.3). They are not counted as provably equivalent on every input.

- `operand.dependent.dependent.dc_line2c.dc_incapable.all.1.eq.0` (replace an operand, dependent.dependent.dc_line2c): dc_line2c is all[dc_qp, dc_incapable, age test]; the mutant reads dc_disabled_qp, all[dc_incapable, dc_lived_half], in place of dc_incapable. The second conjunct is reached only when dc_qp is true or unknown (a refusal ends both tests). dc_qp true means its any-test found dc_child_all_year, dc_disabled_qp or dc_child true. dc_child_all_year and dc_child (through dc_age13) each need qc_dependent true, which needs qualifying_child true, an all-test whose last conjunct is lived_half true; lived_half is then a memoized true in the dependent's frame (spec 4.7.6), and dc_lived_half, an any-test whose first disjunct is lived_half true, is true. dc_disabled_qp true needs dc_lived_half true. So wherever dc_qp is true, dc_lived_half is true and dc_disabled_qp is dc_incapable's value (an input with no gates): the conjuncts agree. dc_qp is unknown only with an input it reads unanswered; there the mutant can be false or a refusal (through dc_lived_half) where the base is unknown, so the argument is over answered inputs: dc_qp is read by f2441.qp_count and f2441.paid_total for every dependent, and its inputs are asked on any return that reaches Form 2441. (Premises pinned: dependent.dc_line2c, dependent.dc_incapable, dependent.dc_disabled_qp, dependent.dc_qp, dependent.dc_lived_half, dependent.dc_child_all_year, dependent.dc_child, dependent.dc_age13, dependent.qc_dependent, dependent.qualifying_child, dependent.lived_half; the mutant reads dependent.dc_disabled_qp.) (structural conditions re-checked this run.)
- `operand.eic.eic.step5_income.earned_for_limit.lt.0` (replace an operand, eic.eic.step5_income): step5_income compares earned_for_limit with eic.limit; the mutant compares wsb_4b, sum[earned_income, wsb_se]. earned_for_limit chooses on self_employed (sc_count > 0): earned_income when false, wsb_4b when true. With self_employed true the two are the same value. With it false sc_count is a complete 0 (a lower bound decides gt only true, spec 4.7.5), so each person's sc_count is a complete 0, has_sc is false and eic_se is person.zero ($0); wsb_se sums eic_se over the same roster with no where-test, so it is $0, and wsb_4b is earned_income's value (a sum returns its first operand's refusal at once, and an unknown plus $0 stays unknown). self_employed is never a refusal (its counts sum parameters over rosters, with no gates); it is unknown only with a $person or $sc roster unconfirmed, where the base is unknown and the mutant can be decided (earned_income's refusal), so the argument is over answered inputs: those rosters are asked on every return. (Premises pinned: eic.step5_income, eic.earned_for_limit, eic.wsb_4b, eic.wsb_se, eic.earned_income, eic.self_employed, eic.sc_count, person.sc_count, person.has_sc, person.eic_se, person.zero, param:ss.zero; the mutant reads eic.wsb_4b.) (structural conditions re-checked this run.)
- `operand.f2441.f2441.attrib_gate.line31.all.3.gt.0` (replace an operand, f2441.f2441.attrib_gate): attrib_gate's fourth conjunct compares line31 with $0; the mutant compares line3, a choose with no gates that is line31 when f2441.benefits is true and line3_expenses when it is false. The conjunct is reached only when has_1e (Form 1040 line 1e above $0) was true or unknown. Line 1e is f2441.zero ($0) when benefits is false, so has_1e true means benefits is a memoized true and line3 is line31's value: the comparisons agree. With benefits answered, has_1e is unknown only when it is true and line 26 is unknown, and line3 is again line31. With benefits unanswered line3 is unknown where line31 may be decided, so the argument is over answered inputs: benefits is read by Form 1040 line 1e, which line 1z sums, and is asked on every return. (Premises pinned: f2441.attrib_gate, f2441.line3, f2441.line31, f2441.has_1e, f1040.line1e, f2441.benefits, f2441.zero, param:sales.zero; the mutant reads f2441.line3.) (structural conditions re-checked this run.)
- `operand.household.household.roster_ok.taxpayers.any.1.all.1.eq.0` (replace an operand, household.household.roster_ok): roster_ok's second disjunct is all[status not mfj, taxpayers = 1, spouses = 0]; the mutant reads persons, the count of every person entry, in place of taxpayers, the count of entries whose role is taxpayer. The three counts sum the parameter person.one over the same $person roster, taxpayers and spouses with a where-test on person.role only, and none has gates; person_role has the two values taxpayer and spouse (checked), so with the roster confirmed and every role answered persons is taxpayers plus spouses. Where spouses is 0 the two counts are equal; otherwise the third conjunct is false and both tests are false (neither second conjunct can refuse). With the roster unconfirmed all three counts are unknown and both tests are unknown, or false at the status. Only with a role unanswered can taxpayers be unknown where persons is known, and the mutant then be more decided; the role is asked first for every person entry, and roster_ok gates Form 1040 line 1a through household.roster_bad, so the argument is over answered inputs. (Premises pinned: household.roster_ok, household.taxpayers, household.persons, household.spouses, person.role, person.one, enum:person_role; the mutant reads household.persons.) (structural conditions re-checked this run.)
- `operand.s8812.s8812.line18a.chart_eic.then0` (replace an operand, s8812.s8812.line18a): line18a's taking_eic-true alternative is chart_eic; the mutant reads eiw_7_figured (eiw_3 less eiw_6). It is taken only when Form 1040 line 27a, a copy of eic.credit, is above $0, so eligible is true and line6 is above $0; line6 is line2 or the smaller of line5 and line2, so line2 is above $0, line1_in_table is true and line1 is at least table_start (positive, checked). eligible true makes step1_income and step5_income complete. Line 11b (line 9 less line 10) is complete; line 9 sums line 8, a copy of Schedule 1 line 10, which sums Schedule 1 line 3, and line 10 copies Schedule 1 line 26, which sums Schedule 1 line 15, so both are complete. earned_for_limit is complete, so earned_income (Step 5 line 1, line 1z behind scope.schedule1; less line 2, $0 behind scope.other_income; plus line 4, $0 behind s8812.combat_pay) is complete and those gates are false. Then eiw_1a is line 1z, eiw_1b $0 (the same combat-pay gate), eiw_2b Schedule 1 line 3, eiw_3 eiw_3sum floored at zero, eiw_4 $0 (scope.schedule1) and eiw_5 Schedule 1 line 15: eiw_7_figured is max(line 1z + S1 line 3, 0) less S1 line 15. S1 line 3 sums each person's sc_total and line 15 each person's se_line13. With self_employed false every Schedule C roster is empty, line 3 is $0 and each se_line13 is person.zero; chart_eic is earned_income, line 1z, and so is eiw_7_figured. With it true chart_eic is wsb_4b, line 1z plus the sum of each person's eic_se: person.zero for a person with no Schedule C (whose sc_total and se_line13 are $0), sc_total less se_line13 when files_se, and sc_total otherwise, where files_se false means Schedule SE line 4c is $0, so lines 6, the social security base, 10, 11, 12 and 13 of that person's Schedule SE are $0. So wsb_4b is line 1z + S1 line 3 less S1 line 15; line1 (wsb_6, wsb_4b floored) is above $0, so line 1z + S1 line 3 is above $0, no floor applies, and eiw_7_figured equals chart_eic. Where taking_eic is false or refused the alternative is not evaluated; where it is unknown the alternative is a way (spec 4.7.3) and chart_eic and eiw_7_figured can differ in whether they refuse, so the argument is over answered inputs. A Schedule C roster is empty when self_employed is false because self_employed tests sc_count > 0 and sc_count sums sc.one, a positive parameter (pinned). (Premises pinned: s8812.line18a, s8812.chart_eic, s8812.eiw_7_figured, s8812.taking_eic, f1040.line27a, eic.credit, eic.zero, eic.line6, eic.after_line4, eic.smaller, eic.line2, eic.line1_in_table, eic.line1, eic.wsb_6, eic.eligible, eic.step1_income, eic.step5_income, eic.earned_for_limit, eic.earned_income, eic.step5_line1, eic.step5_line2, eic.step5_line3, eic.step5_line4, eic.wsb_4b, eic.wsb_se, eic.self_employed, eic.sc_count, s8812.eiw_3, s8812.eiw_3sum, s8812.eiw_1a, s8812.eiw_1b, s8812.eiw_2b, s8812.eiw_6, s8812.eiw_4, s8812.eiw_5, s8812.zero, f1040.line11b, f1040.line11a, f1040.line9, f1040.line8, f1040.line10, s1.line10, s1.line26, s1.line3, s1.line15, person.sc_total, person.se_line13, person.se_line4c, person.files_se, person.eic_se, person.eic_se_has, person.eic_part1, person.has_sc, person.sc_count, person.zero, def:se, param:sales.zero, param:ss.zero, sc.one, param:sc.one; the mutant reads s8812.eiw_7_figured.) (structural conditions re-checked this run.)
- `operand.sc.sc.qbi_se.zero.then1` (replace an operand, sc.sc.qbi_se): sc.qbi_se's qbi_has-false alternative: qbi_has is profit_pos more than $0, so known false means profit_pos is a complete $0; then Form 7206 line 4 is $0, f7206_has is false, lines 7 and 9 are $0, lines 8, 10 and 13 are $0, and line 14 is $0 or (hi_uses true) the smaller of line 3 and $0, which is $0 when line 3 is complete and otherwise line 3's own refusal or unknown. qbi_se's only reader is qbi_ded, the sum of qbi_se, qbi_plan ($0 under the same qbi_has) and line 14: sum($0, $0, L14) and sum(L14, $0, L14) are the same value for L14 $0, the same refusal (it is the only refusing operand) or an unknown. Where qbi_has is unknown both alternatives are ways (spec 4.7.3), and line 14 can make the mutant's qbi_se a refusal where the base's $0 leaves it unknown, so the argument is over answered inputs. (Premises pinned: sc.qbi_se, sc.qbi_has, sc.qbi_ded, sc.qbi_plan, sc.f7206_line14, sc.f7206_min, sc.f7206_line13, sc.f7206_line10, sc.f7206_line9, sc.f7206_line8, sc.f7206_line7, sc.f7206_has, sc.f7206_line4, sc.profit_pos, sc.f7206_line3, param:sales.zero; the mutant reads sc.f7206_line14.) (structural conditions re-checked this run.)
- `operand.sdtw.sdtw.line4.zero.then1` (replace an operand, sdtw.sdtw.line4): sdtw.line4's filing4952-false alternative is sdtw.zero ($0); the mutant reads sdtw.line3, a copy of f4952.election through sd.investment_election. filing4952 is f4952.required, all[used, required_test]; it is known false only when used is false (so has_election, a disjunct of used, is false and election is f4952.zero) or required_test is false (an any-test whose first disjunct is election > 0, so election was evaluated complete and not above $0). Either way line3 is $0 wherever the alternative is taken; a refused guard ends the choose before either alternative. Where filing4952 is unknown both alternatives are ways (spec 4.7.3), and line3 can make the mutant a refusal on both where the base's $0 leaves it unknown, so the argument is over answered inputs. (Premises pinned: sdtw.line4, sdtw.line3, sdtw.zero, sd.filing4952, sd.investment_election, f4952.required, f4952.used, f4952.required_test, f4952.election, f4952.has_election, f4952.zero, param:sales.zero; the mutant reads sdtw.line3.) (structural conditions re-checked this run.)

## Surviving — classified equivalent

- `operand.asset.asset.bonus_forty.after179` (replace an operand, asset.asset.bonus_forty): Copy-chain identity: asset.after179 and asset.bonus_full expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.asset.asset.macrs_hy.ub` (replace an operand, asset.asset.macrs_hy): Copy-chain identity: asset.ub and asset.col19c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.asset.asset.bonus_2025.zero.then1` (replace an operand, asset.asset.bonus_2025): Branch settled by its guard: where asset.bonus_2025 takes alternative 1 (guard {
  "eq": [
    "asset.is2025",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.dep_2025 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.s179_2025.zero.then1` (replace an operand, asset.asset.s179_2025): Branch settled by its guard: where asset.s179_2025 takes alternative 1 (guard {
  "eq": [
    "asset.is2025",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.bonus_2025 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.mq_q4.zero.then1` (replace an operand, asset.asset.mq_q4): Branch settled by its guard: where asset.mq_q4 takes alternative 1 (guard {
  "eq": [
    "asset.is2025",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.s179_2025 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither asset.zero nor asset.s179_2025 ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.mq_total.zero.then1` (replace an operand, asset.asset.mq_total): Branch settled by its guard: where asset.mq_total takes alternative 1 (guard {
  "eq": [
    "asset.is2025",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.mq_q4 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.cost179.zero.then1` (replace an operand, asset.asset.cost179): Branch settled by its guard: where asset.cost179 takes alternative 1 (guard {
  "eq": [
    "asset.is2025",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.mq_total make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.dc_lived_half.part_year_home.any.1.all.2.eq.0` (replace an operand, dependent.dependent.dc_lived_half): dc_lived_half is any[lived_half, all[qualifying_child false, born_died, part_year_home]]; the mutant reads hoh_lived_half, any[lived_half, all[qualifying_child false, any[born_died, placed], part_year_home]], in place of part_year_home. The replaced conjunct is reached only after lived_half was neither true nor a refusal (any-test) and the first two conjuncts were true or unknown, so lived_half, qualifying_child and born_died are memoized there (spec 4.7.6) and born_died is not false. With born_died true the inner any is true without reading placed, so hoh_lived_half is any[lived_half, P] where P is the base conjunct list's value; with born_died unknown the inner any is true or unknown (placed is an input with no gates, never a refusal). In every combination the mutant's inner all-test differs from the base's only by a true turned unknown, or a false turned unknown when lived_half is unknown, and the outer any-test, which already remembers lived_half's unknown in that case, gives the same value; a refusal of part_year_home is passed through in both. (Premises pinned: dependent.dc_lived_half, dependent.hoh_lived_half, dependent.lived_half, dependent.qualifying_child, dependent.born_died, dependent.placed, dependent.part_year_home; the mutant reads dependent.hoh_lived_half.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.edu_adj.zero.then1` (replace an operand, dependent.dependent.edu_adj): dependent.edu_adj's edu_student-false alternative: as for person.edu_adj, edu_over_refused is decided false by its first conjunct, and lines 27 to 31 read edu_adj only in alternatives guarded by edu_aoc or edu_llc, all-tests whose first conjunct is edu_student true; where edu_student is unknown edu_adj is that unknown on both routes, its other alternative never refusing (spec 4.7.3). edu_adj is a helper. (Premises pinned: dependent.edu_adj, dependent.edu_student, dependent.edu_over_refused, dependent.edu_aoc, dependent.edu_llc, dependent.edu_line27, dependent.edu_line28, dependent.edu_line29, dependent.edu_line30, dependent.edu_line31, dependent.zero; the mutant reads dependent.dc_line2d.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.edu_aoc.edu_student.all.0.eq.0` (replace an operand, dependent.dependent.edu_aoc): Conjunct prefix: dependent.edu_show26 expands to conjuncts that dependent.edu_aoc reads anyway, in the same first-read order (dependent.edu_student among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.dependent.dependent.edu_aoc.edu_line24.all.2.eq.0` (replace an operand, dependent.dependent.edu_aoc): Conjunct prefix: dependent.edu_show26 expands to conjuncts that dependent.edu_aoc reads anyway, in the same first-read order (dependent.edu_line24 among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.dependent.dependent.edu_line28.zero.then1` (replace an operand, dependent.dependent.edu_line28): Branch settled by its guard: where dependent.edu_line28 takes alternative 1 (guard {
  "eq": [
    "dependent.edu_aoc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.zero and dependent.edu_line27 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.edu_line29.zero.then1` (replace an operand, dependent.dependent.edu_line29): Branch settled by its guard: where dependent.edu_line29 takes alternative 1 (guard {
  "eq": [
    "dependent.edu_aoc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.zero and dependent.edu_line28 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.edu_line30.zero.then1` (replace an operand, dependent.dependent.edu_line30): Branch settled by its guard: where dependent.edu_line30 takes alternative 1 (guard {
  "eq": [
    "dependent.edu_aoc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.zero and dependent.edu_line29 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.eic.eic.show_wsb6.self_employed.all.1.eq.0` (replace an operand, eic.eic.show_wsb6): Conjunct prefix: eic.show_wsb4b expands to conjuncts that eic.show_wsb6 reads anyway, in the same first-read order (eic.self_employed among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.eic.eic.wsb_6.zero` (replace an operand, eic.eic.wsb_6): Gated zero carried earlier: eic.zero is an ungated zero and eic.step5_line4 the same zero behind refusal gates (s8812.combat_pay); eic.wsb_4b, read first, reaches eic.step5_line4 through ungated arithmetic, so whenever eic.step5_line4 refuses or is unknown eic.wsb_4b already is, and is returned first, and otherwise both operands are zero.
- `operand.eic.eic.line1.earned_income.then0` (replace an operand, eic.eic.line1): eic.line1 chooses on self_employed: false takes earned_income, true takes wsb_6 (wsb_4b floored at zero, no gates). The mutant reads earned_for_limit in the false alternative, a choice on the same guards that takes earned_income when self_employed is false and wsb_4b when true. With self_employed known false both are earned_income, the same memoized value. Where self_employed is unknown both lines evaluate both alternatives (spec 4.7.3): earned_for_limit is a refusal exactly when earned_income and wsb_4b both refuse, then earned_income's; wsb_6 refuses exactly when wsb_4b does. So the base line 1 is a refusal exactly when earned_income and wsb_4b refuse, then earned_income's, and so is the mutant (its first way is earned_for_limit, that same refusal); otherwise both are self_employed's unknown. (Premises pinned: eic.line1, eic.earned_for_limit, eic.earned_income, eic.wsb_6, eic.wsb_4b, eic.self_employed, eic.zero; the mutant reads eic.earned_for_limit.) (structural conditions re-checked this run.)
- `operand.eic.eic.line1_in_table.line1.ge.0` (replace an operand, eic.eic.line1_in_table): line1_in_table compares eic.line1 with eic.table_start; the mutant compares eic.earned_for_limit. Both choose on the same guards (self_employed false, then true) and take earned_income on the first; on the second line 1 takes wsb_6, which is wsb_4b floored at zero (subtract_floor0 from wsb_4b of eic.zero, no gates of its own), and earned_for_limit takes wsb_4b. A refused guard is the value of both; with an unknown guard both evaluate both alternatives (spec 4.7.3) and are a refusal exactly when earned_income and wsb_4b both refuse (wsb_6 refuses exactly when wsb_4b does), then earned_income's, the first way's, and otherwise that guard's unknown; an incomplete wsb_4b is wsb_6's value too. For a complete wsb_4b x, max(x, 0) >= start exactly when x >= start, because table_start is positive (checked). (Premises pinned: eic.line1_in_table, eic.line1, eic.earned_for_limit, eic.self_employed, eic.wsb_6, eic.wsb_4b, eic.earned_income, eic.zero, param:eic.table_start; the mutant reads eic.earned_for_limit.) (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table0.line1.key` (replace an operand, eic.eic.line1_table0): eic.line1_table0 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table1.line1.key` (replace an operand, eic.eic.line1_table1): eic.line1_table1 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table2.line1.key` (replace an operand, eic.eic.line1_table2): eic.line1_table2 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table3.line1.key` (replace an operand, eic.eic.line1_table3): eic.line1_table3 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.show5.eligible.all.0.eq.0` (replace an operand, eic.eic.show5): show5 is all[eligible, line4 false, line5_blank false, line2 > 0]; the mutant reads show3, all[eligible, line2 > 0], in place of eligible. With eligible false or a refusal both tests end at their first conjunct with that value. With eligible true, step1_income (line 11b below eic.limit) and step5_income (earned_for_limit below eic.limit) are complete, so eic.limit, a choice on the filing status and then on ssn_count's bands, is complete: the status is supplied and ssn_count is not a refusal. Then line3 (a copy of line 11b) is complete; line1 takes earned_income, or wsb_6 (wsb_4b floored at zero), on the same self_employed guard as earned_for_limit, so it is complete; line4 is a complete comparison; line5_blank compares line3 with line5_threshold, a choice on the status and ssn_count's bands among parameters, so it is complete or unknown; line2 chooses on line1_in_table (complete) between eic.zero and a table lookup keyed on line1 and the status in a table chosen by ssn_count's bands, so it is complete or unknown. None of these lines has a refusal gate, so no conjunct refuses, and show3 is line2 > 0's value V. V false makes both tests false (the base reaches V after line4 and line5_blank, which cannot refuse); V true leaves both the same remaining conjuncts; V unknown makes both unknown unless line4 or line5_blank is false, which makes both false. With eligible unknown, the tests could differ only if line2 refused, and line2 can refuse only through ssn_count, which counts the dependents whose eic_ssn_child (and so eic_child) is true; a refusal there also refuses qc_count, has_qc and step34, which eligible reads, so eligible would be a refusal, not unknown. (Premises pinned: eic.show5, eic.show3, eic.eligible, eic.step1_income, eic.step5_income, eic.limit, eic.limit_other, eic.limit_joint, eic.earned_for_limit, eic.self_employed, eic.line4, eic.line5_blank, eic.line3, eic.line1, eic.wsb_6, eic.zero, eic.line2, eic.line1_in_table, eic.line1_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line5_threshold, eic.threshold_other, eic.threshold_joint, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.ssn_count, dependent.eic_ssn_child, dependent.eic_child, eic.qc_count, eic.has_qc, eic.step34; the mutant reads eic.show3.) (structural conditions re-checked this run.)
- `operand.eic.eic.credit.line6.then0` (replace an operand, eic.eic.credit): eic.credit's eligible alternative reads line6, which is line2 when line4 (line3 equals line1) is true and after_line4 otherwise, so the mutant differs only where line4 is true. eligible true needs step1_income (AGI, which line3 copies, below the limit) and step5_income (earned_for_limit, whose branch value is line1's source, below the limit) complete and true, so line3 and line1 are complete there and line4 is a complete comparison. With line4 true, line5 looks up line3 in the same EIC table (by the same ssn_count choices and filing status) that line2 looks up line1 in, so where line1 is at least table_start line5 equals line2 and after_line4 (line2, or the smaller of line5 and line2) is line2; where line1 is below table_start line2 is $0 and line3, equal to line1, is below every line 5 threshold (all of which exceed table_start), so line5 is blank and after_line4 is line2. eic.credit's refusal gate, household.eic_disallowed_claim (which reads eligible and line6 itself), is evaluated at line entry before the expression, the same on both routes (spec 4.7.1); only the expression's operand changes. (Premises pinned: eic.credit, eic.eligible, eic.line6, eic.after_line4, eic.line4, eic.line3, eic.line1, eic.line2, eic.zero, eic.line1_in_table, eic.line1_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line5, eic.line3_table0, eic.line3_table1, eic.line3_table2, eic.line3_table3, eic.line5_blank, eic.line5_threshold, eic.threshold_other, eic.threshold_joint, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.smaller, eic.step1_income, eic.step5_income, eic.earned_for_limit, eic.wsb_6, eic.wsb_4b, eic.earned_income, param:eic.table_start; the mutant reads eic.after_line4.) (structural conditions re-checked this run.)
- `boundary.eic.eic.wsb_4b_positive` (replace strict greater-than with inclusive, eic.eic.wsb_4b_positive): The inclusive test differs only at Worksheet B line 4b = 0. wsb_4b_positive is read only by the line 5 stop, an all-test that requires self-employment before it and, after it, Step 5 question 3 to be No; for a self-employed filer question 3 compares line 4b with the EIC limit, so at line 4b = 0 it asks whether 0 < limit, which holds for every limit (all are positive). The stop is therefore false on both routes, and question 3 reads only lines the stop has already evaluated without refusal, so no refusal is newly reached. (structural conditions re-checked this run.)
- `operand.f1095a.f1095a.a_feb.mo_a.then0` (replace an operand, f1095a.f1095a.a_feb): Branch settled by its guard: where f1095a.a_feb takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_jan make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_jan ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_mar.mo_a.then0` (replace an operand, f1095a.f1095a.a_mar): Branch settled by its guard: where f1095a.a_mar takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_feb make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_feb ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_apr.mo_a.then0` (replace an operand, f1095a.f1095a.a_apr): Branch settled by its guard: where f1095a.a_apr takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_mar make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_mar ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_may.mo_a.then0` (replace an operand, f1095a.f1095a.a_may): Branch settled by its guard: where f1095a.a_may takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_apr make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_apr ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_jun.mo_a.then0` (replace an operand, f1095a.f1095a.a_jun): Branch settled by its guard: where f1095a.a_jun takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_may make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_may ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_jul.mo_a.then0` (replace an operand, f1095a.f1095a.a_jul): Branch settled by its guard: where f1095a.a_jul takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_jun make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_jun ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_aug.mo_a.then0` (replace an operand, f1095a.f1095a.a_aug): Branch settled by its guard: where f1095a.a_aug takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_jul make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_jul ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_sep.mo_a.then0` (replace an operand, f1095a.f1095a.a_sep): Branch settled by its guard: where f1095a.a_sep takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_aug make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_aug ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_oct.mo_a.then0` (replace an operand, f1095a.f1095a.a_oct): Branch settled by its guard: where f1095a.a_oct takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_sep make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_sep ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_nov.mo_a.then0` (replace an operand, f1095a.f1095a.a_nov): Branch settled by its guard: where f1095a.a_nov takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_oct make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_oct ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.a_dec.mo_a.then0` (replace an operand, f1095a.f1095a.a_dec): Branch settled by its guard: where f1095a.a_dec takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_a and f1095a.a_nov make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_a nor f1095a.a_nov ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_feb.mo_b.then0` (replace an operand, f1095a.f1095a.b_feb): Branch settled by its guard: where f1095a.b_feb takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_jan make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_jan ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_mar.mo_b.then0` (replace an operand, f1095a.f1095a.b_mar): Branch settled by its guard: where f1095a.b_mar takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_feb make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_feb ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_apr.mo_b.then0` (replace an operand, f1095a.f1095a.b_apr): Branch settled by its guard: where f1095a.b_apr takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_mar make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_mar ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_may.mo_b.then0` (replace an operand, f1095a.f1095a.b_may): Branch settled by its guard: where f1095a.b_may takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_apr make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_apr ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_jun.mo_b.then0` (replace an operand, f1095a.f1095a.b_jun): Branch settled by its guard: where f1095a.b_jun takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_may make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_may ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_jul.mo_b.then0` (replace an operand, f1095a.f1095a.b_jul): Branch settled by its guard: where f1095a.b_jul takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_jun make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_jun ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_aug.mo_b.then0` (replace an operand, f1095a.f1095a.b_aug): Branch settled by its guard: where f1095a.b_aug takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_jul make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_jul ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_sep.mo_b.then0` (replace an operand, f1095a.f1095a.b_sep): Branch settled by its guard: where f1095a.b_sep takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_aug make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_aug ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_oct.mo_b.then0` (replace an operand, f1095a.f1095a.b_oct): Branch settled by its guard: where f1095a.b_oct takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_sep make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_sep ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_nov.mo_b.then0` (replace an operand, f1095a.f1095a.b_nov): Branch settled by its guard: where f1095a.b_nov takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_oct make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_oct ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1095a.f1095a.b_dec.mo_b.then0` (replace an operand, f1095a.f1095a.b_dec): Branch settled by its guard: where f1095a.b_dec takes alternative 0 (guard {
  "eq": [
    "f1095a.uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1095a.mo_b and f1095a.b_nov make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1095a.mo_b nor f1095a.b_nov ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f2441.f2441.line11.line10` (replace an operand, f2441.f2441.line11): Copy-chain identity: f2441.line10 and f2441.clw3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f2441.f2441.line13_earned.line20.all.3.gt.1` (replace an operand, f2441.f2441.line13_earned): The fourth conjunct of line13_earned compares line 23 with line 20; the mutant compares it with line 24. Line 22 is f2441.zero (a $0 parameter), so line 24 is the smaller of (the smaller of line 20 and line 21) and $0, and line 23 is line 15 less $0. The fourth conjunct is reached only after line 20 < line 17 and line 20 < line 21 were each true or unknown. Line 20 is line 17, 18 and 19's smallest floored at zero, so line 20 complete means line 17 complete and the second conjunct complete: then line 20 < line 17 <= line 15 = line 23, so both comparisons are true when line 23 is complete, and both are line 23's own unknown or refusal otherwise (it is the left operand, and the right operand is complete in both when line 21 is). Line 21 unknown leaves the third conjunct unknown and line 24 unknown: the base comparison is true or line 23's incompleteness, the mutant's unknown or that refusal, so the test is the same. Line 20 unknown makes line 24 unknown, and both comparisons are line 23's refusal or unknown. A refusal of line 20 or line 21 ends the test at the second or third conjunct. (Premises pinned: f2441.line13_earned, f2441.line24, f2441.line24_20_21, f2441.line22, f2441.zero, f2441.line20, f2441.line20_all, f2441.line20_17_18, f2441.line17, f2441.line15, f2441.line23, f2441.line21, param:sales.zero; the mutant reads f2441.line24.) (structural conditions re-checked this run.)
- `operand.f2441.f2441.line25.line24` (replace an operand, f2441.f2441.line25): Floor-minus-min identity: f2441.line25 is f2441.line24_20_21 less f2441.line24, floored at zero, and one of f2441.line24 and f2441.line22 is the ungated smaller of f2441.line24_20_21 and the other, so f2441.line24_20_21 less either, floored at zero, is the same at every input; f2441.line24_20_21 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.f5329.f5329.l49_base.l48` (replace an operand, f5329.f5329.l49_base): Copy-chain identity: f5329.l48 and f5329.l47 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.line15.line14` (replace an operand, f5695.f5695.line15): Copy-chain identity: f5695.line14 and f5695.rce_ws3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.line16.line15` (replace an operand, f5695.f5695.line16): Floor-minus-min identity: f5695.line16 is f5695.line13 less f5695.line15, floored at zero, and one of f5695.line15 and f5695.line14 is the ungated smaller of f5695.line13 and the other, so f5695.line13 less either, floored at zero, is the same at every input; f5695.line13 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.f5695.f5695.ins_30.eehi_rate.rate` (replace an operand, f5695.f5695.ins_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.door1_30.eehi_rate.rate` (replace an operand, f5695.f5695.door1_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.line19g.eehi_rate.rate` (replace an operand, f5695.f5695.line19g): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.windows_30.eehi_rate.rate` (replace an operand, f5695.f5695.windows_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.ac_30.eehi_rate.rate` (replace an operand, f5695.f5695.ac_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.wh_30.eehi_rate.rate` (replace an operand, f5695.f5695.wh_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.furnace_30.eehi_rate.rate` (replace an operand, f5695.f5695.furnace_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.enabling_30.eehi_rate.rate` (replace an operand, f5695.f5695.enabling_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.audit_30.eehi_rate.rate` (replace an operand, f5695.f5695.audit_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.hp_30.eehi_rate.rate` (replace an operand, f5695.f5695.hp_30): Copy-chain identity: f5695.eehi_rate and f5695.rce_rate expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.eehi_credit.line31` (replace an operand, f5695.f5695.eehi_credit): Copy-chain identity: f5695.line31 and f5695.eehi_ws3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8863.f8863.clw3.clw1` (replace an operand, f8863.f8863.clw3): Copy-chain identity: f8863.clw1 and f8863.line18 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8889.f8889.age55_unmarried.age55.all.0.eq.0` (replace an operand, f8889.f8889.age55_unmarried): age55_unmarried is all[age55, married false]; the mutant reads age55_line3, all[age55, married_family false], in place of age55, and married_family is all[married, any[...]] over inputs (household.married, dec_coverage, last_month, months_family) and use_last_month (a choose on dec_coverage taking last_month or the false parameter no_last_month), none with refusal gates, so married_family is never a refusal. With married false, married_family is false and age55_line3 is age55. With married true the second conjunct is false in both, and the mutant's first conjunct is age55's value or false. With married unknown, married_family is false or unknown, so age55_line3 is age55's value or unknown where age55 is true, and the second conjunct is unknown: both tests are unknown, or false where age55 is false. (Premises pinned: f8889.age55_unmarried, f8889.age55_line3, f8889.married_family, f8889.age55, household.married, f8889.use_last_month, f8889.dec_coverage, f8889.months_family, f8889.last_month, f8889.no_last_month; the mutant reads f8889.age55_line3.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.line3_last_month.line3_changed.then0` (replace an operand, f8889.f8889.line3_last_month): Branch settled by its guard: where f8889.line3_last_month takes alternative 0 (guard {
  "eq": [
    "f8889.changed",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f8889.line3_changed and f8889.line3_all_year make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f8889.line3_changed nor f8889.line3_all_year ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f8889.f8889.family_dec_year.zero.then2` (replace an operand, f8889.f8889.family_dec_year): Unreachable alternative: f8889.family_dec_year is a helper that every printed line reads only through choices whose guards make f8889.use_last_month true, and f8889.use_last_month true makes the guard of alternative 2 ({
  "eq": [
    "f8889.dec_coverage",
    {
      "const": "none"
    }
  ],
  "op": "test"
}
) false; where f8889.family_dec_year's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither f8889.zero nor f8889.line5 ever refuses; spec 4.7.3); so wherever a printed value depends on f8889.family_dec_year that alternative is not taken, and replacing its value changes no printed value.
- `operand.f8889.f8889.self_dec_year.zero.then1` (replace an operand, f8889.f8889.self_dec_year): self_dec_year's self_only alternative is read (through self_in_family, step4_total, step4 and line6_split) only by line6, and only where split is true; with use_last_month true (which self_in_family requires to read self_dec_year) and December coverage self-only, married_family's inner any-test is false (its first disjunct needs December family coverage, its second needs use_last_month false), so married_family, an all-test, is false even past an unknown married answer (spec 4.7.2) or is the same refusal on both routes, and split is false: line6 reads line5, not line6_split. use_last_month is a choose on dec_coverage (asked first) that takes last_month for self-only or family coverage and the false parameter no_last_month for none, with no gates: it is true only with December coverage known and not none and last_month true, and it is never a refusal. (Premises pinned: f8889.self_dec_year, f8889.self_in_family, f8889.self_all, f8889.step4_total, f8889.step4, f8889.line6_split, f8889.line6, f8889.split, f8889.married_family, f8889.use_last_month, f8889.dec_coverage, f8889.self_year, f8889.zero, f8889.last_month, f8889.no_last_month; the mutant reads f8889.self_family_months.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.self_dec_year.zero.then2` (replace an operand, f8889.f8889.self_dec_year): Unreachable alternative: f8889.self_dec_year is a helper that every printed line reads only through choices whose guards make f8889.use_last_month true, and f8889.use_last_month true makes the guard of alternative 2 ({
  "eq": [
    "f8889.dec_coverage",
    {
      "const": "none"
    }
  ],
  "op": "test"
}
) false; where f8889.self_dec_year's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither f8889.zero nor f8889.self_family_months ever refuses; spec 4.7.3); so wherever a printed value depends on f8889.self_dec_year that alternative is not taken, and replacing its value changes no printed value.
- `operand.f8889.f8889.self_in_family.self_dec_year.then0` (replace an operand, f8889.f8889.self_in_family): self_in_family's use_last_month alternative: use_last_month true means December coverage is known and not none (use_last_month is a choose on dec_coverage taking last_month for self-only or family coverage and the false parameter no_last_month for none, with no gates). With family coverage self_dec_year and self_all are both self_year (self_all takes self_year under use_last_month), the same memoized value; with self-only coverage step4_total reaches line6 only through line6_split, which line6 reads only where split is true, and married_family (so split) is then false or the same refusal on both routes, as for self_dec_year's zero alternative. (Premises pinned: f8889.self_dec_year, f8889.self_in_family, f8889.self_all, f8889.step4_total, f8889.step4, f8889.line6_split, f8889.line6, f8889.split, f8889.married_family, f8889.use_last_month, f8889.dec_coverage, f8889.self_year, f8889.zero, f8889.last_month, f8889.no_last_month; the mutant reads f8889.self_all.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.line16.zero.then1` (replace an operand, f8889.f8889.line16): Branch settled by its guard: where f8889.line16 takes alternative 1 (guard {
  "eq": [
    "f8889.has_dist",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f8889.zero and f8889.line15 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f8889.zero nor f8889.line15 ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f8889.f8889.subject.line16.then0` (replace an operand, f8889.f8889.subject): f8889.subject is read only by line17b_figured, which only line17b reads, and only in its has_taxable alternative; has_taxable is line16 more than $0 (sales.zero), so where subject is read line16 is complete and positive, which only line16's has_dist alternative gives (the other is f8889.zero, $0), and that alternative's value is line16_figured. Where has_taxable is false or refused, subject is not read; where it is unknown, line17b evaluates line17b_figured as a way (spec 4.7.3), but line17b's other alternative is f8889.zero, which never refuses, so line17b is that unknown on both routes. (Premises pinned: f8889.subject, f8889.line17b_figured, f8889.line17b, f8889.has_taxable, f8889.line16, f8889.line16_figured, f8889.has_dist, f8889.zero, param:sales.zero; the mutant reads f8889.line16_figured.) (structural conditions re-checked this run.)
- `operand.f8959.f8959.line3.zero` (replace an operand, f8959.f8959.line3): Copy-chain identity: f8959.zero and f8959.line2 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line23.zero` (replace an operand, f8959.f8959.line23): Copy-chain identity: f8959.zero and f8959.line14 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line4.line2` (replace an operand, f8959.f8959.line4): Copy-chain identity: f8959.line2 and f8959.line23 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line4.line3` (replace an operand, f8959.f8959.line4): Copy-chain identity: f8959.line3 and f8959.line23 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line18.line17` (replace an operand, f8959.f8959.line18): Line 17 is 0.9% of line 16, and line 16 is line 14 less line 15 floored at zero, where line 14 is $0 behind its refusal gate and line 15 is not negative; so line 16 and line 17 are both $0, and when line 14 refuses or is unknown both carry its value (line 16 reads line 14 first, and the rate passes it through). (structural conditions re-checked this run.)
- `operand.f8960.f8960.line4a.zero` (replace an operand, f8960.f8960.line4a): Copy-chain identity: f8960.zero and f8960.line3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line4b.zero` (replace an operand, f8960.f8960.line4b): Copy-chain identity: f8960.zero and f8960.line4a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line5b.zero` (replace an operand, f8960.f8960.line5b): Copy-chain identity: f8960.zero and f8960.line4b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line6.zero` (replace an operand, f8960.f8960.line6): Copy-chain identity: f8960.zero and f8960.line5c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line7.zero` (replace an operand, f8960.f8960.line7): Copy-chain identity: f8960.zero and f8960.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line9c.zero` (replace an operand, f8960.f8960.line9c): Copy-chain identity: f8960.zero and f8960.line7 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line9b.zero.then1` (replace an operand, f8960.f8960.line9b): Branch settled by its guard: where f8960.line9b takes alternative 1 (guard {
  "eq": [
    "sa.itemizes",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f8960.zero and f8960.line9a make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f8960.f8960.line9d.line9c` (replace an operand, f8960.f8960.line9d): Line 9c and lines 4a and 4b (the operands of line 4c) are each $0 behind the same refusal entries, word for word; so line 4c, their sum, is $0 when no entry fires and otherwise carries the same refusal (or unknown) that line 9c does. (structural conditions re-checked this run.)
- `operand.f8962.f8962.filing.applicable.all.1.any.0.eq.0` (replace an operand, f8962.f8962.filing): filing is all[any, any[applicable, aptc]]; the mutant reads show_applicable, all[any, applicable], in place of applicable. The inner any-test is reached only when f8962.any is true or unknown. With any true, show_applicable is applicable's (memoized) value. f8962.any is forms > 0, and forms counts the Form 1095-A roster with a parameter field, so any is unknown only when that roster is unconfirmed; then aptc (aptc_total, a sum over the same roster) is unknown, never a refusal (spec 4.7.5: an unconfirmed roster evaluates nothing), and show_applicable differs from applicable only by a true turned unknown, which the outer all-test, already holding any's unknown, cannot see: both are unknown, or the same refusal of applicable. (Premises pinned: f8962.filing, f8962.show_applicable, f8962.applicable, f8962.any, f8962.forms, f8962.aptc, f8962.aptc_total, f1095a.one, param:sales.one; the mutant reads f8962.show_applicable.) (structural conditions re-checked this run.)
- `operand.f8995.f8995.line9.line8` (replace an operand, f8995.f8995.line9): Copy-chain identity: f8995.line8 and f8995.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8995a.f8995a.line31.line30` (replace an operand, f8995a.f8995a.line31): Copy-chain identity: f8995a.line30 and f8995a.line28 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ira.ira.cov_gate.any_trad.all.1.eq.0` (replace an operand, ira.ira.cov_gate): Conjunct prefix: ira.lines2to6 expands to conjuncts that ira.cov_gate reads anyway, in the same first-read order (ira.any_trad among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.ira.ira.cov_gate.anyone_covered.all.2.eq.0` (replace an operand, ira.ira.cov_gate): Conjunct prefix: ira.lines2to6 expands to conjuncts that ira.cov_gate reads anyway, in the same first-read order (ira.anyone_covered among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.ira.ira.line2b.zero.then1` (replace an operand, ira.ira.line2b): Branch settled by its guard: where ira.line2b takes alternative 1 (guard {
  "eq": [
    "ira.lines2to6",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that ira.zero and ira.line2a make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither ira.zero nor ira.line2a ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.ira.ira.line6b.zero.then1` (replace an operand, ira.ira.line6b): Branch settled by its guard: where ira.line6b takes alternative 1 (guard {
  "eq": [
    "ira.lines2to6",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that ira.zero and ira.line6a make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.ira.ira.line7b.zero.then1` (replace an operand, ira.ira.line7b): Branch settled by its guard: where ira.line7b takes alternative 1 (guard {
  "eq": [
    "ira.any_trad",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that ira.zero and ira.line7a make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.educator_deduction.zero.then1` (replace an operand, person.person.educator_deduction): Branch equal under a case split: where person.educator_deduction takes alternative 1 (guard {
  "eq": [
    "person.has_educator_expenses",
    {
      "const": false
    }
  ],
  "op": "test"
}
), person.zero and person.educator_limited have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.person.person.se_line6.zero.then1` (replace an operand, person.person.se_line6): person.se_line6's has_sc-false alternative is person.zero; the mutant reads person.s179_listed, a sum of sc.f29 over the person's Schedule C entries. With has_sc known false the roster is confirmed and empty, so s179_listed is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; se_line6's own gate, se_rrta, is then unknown, so se_line6 is that unknown at line entry and its expression, the only part the mutant changes, is not evaluated (spec 4.7.1). (Premises pinned: person.se_line6, person.s179_listed, person.has_sc, person.sc_count, person.se_rrta, person.sc_rrta_count, person.zero, sc.one, param:sc.one; the mutant reads person.s179_listed.) (structural conditions re-checked this run.)
- `operand.person.person.se_line12.zero.then1` (replace an operand, person.person.se_line12): Branch settled by its guard: where person.se_line12 takes alternative 1 (guard {
  "eq": [
    "person.has_sc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.se_line6 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.se_line13.zero.then1` (replace an operand, person.person.se_line13): Branch settled by its guard: where person.se_line13 takes alternative 1 (guard {
  "eq": [
    "person.has_sc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.se_line12 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.se_line4c.zero.then1` (replace an operand, person.person.se_line4c): Branch settled by its guard: where person.se_line4c takes alternative 1 (guard {
  "eq": [
    "person.has_sc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.se_line13 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.sep_s1.sc_total` (replace an operand, person.person.sep_s1): Copy-chain identity: person.sc_total and person.se_line2 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.person.person.simple_catchup.simple_regular` (replace an operand, person.person.simple_catchup): Floor-minus-min identity: person.simple_catchup is person.simple_deferral less person.simple_regular, floored at zero, and one of person.simple_regular and person.simple_cap is the ungated smaller of person.simple_deferral and the other, so person.simple_deferral less either, floored at zero, is the same at every input; person.simple_deferral is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.person.person.eic_se.zero.then1` (replace an operand, person.person.eic_se): person.eic_se's has_sc-false alternative is person.zero; the mutant reads person.eic_part1, sc_total less se_line13. With has_sc known false the roster is confirmed and empty, sc_total is $0 and se_line13 takes person.zero, so eic_part1 is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; sc_total, a sum over that roster, is unknown, and se_line13's gate se_rrta is unknown, so se_line13 is unknown at line entry; eic_part1 is then unknown, never a refusal, as the base's person.zero is not, and eic_se is has_sc's unknown on both routes (spec 4.7.3). (Premises pinned: person.eic_se, person.eic_part1, person.sc_total, person.se_line13, person.has_sc, person.sc_count, person.se_rrta, person.sc_rrta_count, person.zero, sc.one, param:sc.one; the mutant reads person.eic_part1.) (structural conditions re-checked this run.)
- `operand.person.person.dc_earned.eic_se` (replace an operand, person.person.dc_earned): person.eic_se is person.eic_se_has when the person has a Schedule C and $0 otherwise. With no Schedule C every sum over the person's Schedule C entries is $0, so the Schedule SE railroad gate is false, line 4c is $0, files_se is false and eic_se_has is the empty Schedule C total, $0; with the roster unanswered both routes are unknown. The replacement changes no value. (structural conditions re-checked this run.)
- `operand.person.person.ira_8606_line2.zero.then1` (replace an operand, person.person.ira_8606_line2): Branch settled by its guard: where person.ira_8606_line2 takes alternative 1 (guard {
  "eq": [
    "person.ira_files_8606",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.ira_nondeductible make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.ira_se.zero.then1` (replace an operand, person.person.ira_se): person.ira_se's has_sc-false alternative is person.zero; the mutant reads person.ira_se_take, the sum of se_line13 and s16. With has_sc known false both take person.zero, so the sum is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; se_line13's gate se_rrta is unknown, so se_line13 is unknown at line entry, and s16 is a choice on has_sc with a person.zero alternative, so it is unknown (spec 4.7.3); ira_se_take is then unknown, never a refusal, and ira_se is has_sc's unknown on both routes. (Premises pinned: person.ira_se, person.ira_se_take, person.se_line13, person.s16, person.has_sc, person.sc_count, person.se_rrta, person.sc_rrta_count, person.zero, sc.one, param:sc.one; the mutant reads person.ira_se_take.) (structural conditions re-checked this run.)
- `operand.person.person.edu_adj.zero.then1` (replace an operand, person.person.edu_adj): edu_adj's edu_student-false alternative: edu_student is then known false (memoized). edu_over_refused is an all-test whose first conjunct, edu_student true, decides it false before edu_adj is read; lines 27 to 30 read edu_adj only in the alternative guarded by edu_aoc and line 31 only in the one guarded by edu_llc, both all-tests whose first conjunct is edu_student true, so both are false and those alternatives (and their bindings) are not evaluated (spec 4.7.3, 4.7.4). Where edu_student is unknown, edu_adj's other alternative never refuses, so edu_adj is that unknown on both routes (spec 4.7.3). edu_adj is a helper. (Premises pinned: person.edu_adj, person.edu_student, person.edu_over_refused, person.edu_aoc, person.edu_llc, person.edu_line27, person.edu_line28, person.edu_line29, person.edu_line30, person.edu_line31, person.zero; the mutant reads person.ira_se.) (structural conditions re-checked this run.)
- `operand.person.person.edu_aoc.edu_student.all.0.eq.0` (replace an operand, person.person.edu_aoc): Conjunct prefix: person.edu_show26 expands to conjuncts that person.edu_aoc reads anyway, in the same first-read order (person.edu_student among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.person.person.edu_aoc.edu_line24.all.2.eq.0` (replace an operand, person.person.edu_aoc): Conjunct prefix: person.edu_show26 expands to conjuncts that person.edu_aoc reads anyway, in the same first-read order (person.edu_line24 among them), so the all-test meets the same first refusal or false, or ends unknown or true, at every input.
- `operand.person.person.edu_line28.zero.then1` (replace an operand, person.person.edu_line28): Branch settled by its guard: where person.edu_line28 takes alternative 1 (guard {
  "eq": [
    "person.edu_aoc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.edu_line27 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.edu_line29.zero.then1` (replace an operand, person.person.edu_line29): Branch settled by its guard: where person.edu_line29 takes alternative 1 (guard {
  "eq": [
    "person.edu_aoc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.edu_line28 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.edu_line30.zero.then1` (replace an operand, person.person.edu_line30): Branch settled by its guard: where person.edu_line30 takes alternative 1 (guard {
  "eq": [
    "person.edu_aoc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.edu_line29 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.qdcg.qdcg.line8.line7` (replace an operand, qdcg.qdcg.line8): qdcg.line8 is min(qdcg.line5, qdcg.line7) and qdcg.line7 is the ungated min(qdcg.line1, qdcg.line6); qdcg.line5 is qdcg.line1 less a non-negative amount, floored at zero, with qdcg.line1 not negative, so qdcg.line5 <= qdcg.line1 and min(qdcg.line5, min(qdcg.line1, qdcg.line6)) = min(qdcg.line5, qdcg.line6) at every input; qdcg.line5 is read first on both routes. (structural conditions re-checked this run.)
- `operand.qdcg.qdcg.line12.line11` (replace an operand, qdcg.qdcg.line12): Copy-chain identity: qdcg.line11 and qdcg.line9 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.retirement.retirement.smw4_table1.smw4_t1_210.then3` (replace an operand, retirement.retirement.smw4_table1): Branch equal under a case split: where retirement.smw4_table1 takes alternative 3 (guard {
  "all": [
    {
      "ge": [
        "retirement.age",
        {
          "const": 66,
          "type": "Count"
        }
      ],
      "op": "test"
    },
    {
      "lt": [
        "retirement.age",
        {
          "const": 71,
          "type": "Count"
        }
      ],
      "op": "test"
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "retirement.joint_life",
    {
      "const": false
    }
  ],
  "op": "test"
}
, {
  "eq": [
    "retirement.used_last_year",
    {
      "const": false
    }
  ],
  "op": "test"
}
 on its one reader path), retirement.smw4_t1_210 and retirement.smw4_t2_210 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.retirement.retirement.exc_capped.taxable` (replace an operand, retirement.retirement.exc_capped): Guarded figure: retirement.l1 is retirement.taxable wherever retirement.early holds, and every printed line reads retirement.exc_capped (a helper) only through choices whose guards make retirement.early true, which, where a guard is unknown, are that unknown whatever retirement.exc_capped is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where retirement.early does not hold only retirement.exc_capped's own, unprinted value can differ.
- `operand.retirement.retirement.l2_e05.l2.then0` (replace an operand, retirement.retirement.l2_e05): Branch equal under a case split: where retirement.l2_e05 takes alternative 0 (guard {
  "eq": [
    "retirement.is_e05",
    {
      "const": true
    }
  ],
  "op": "test"
}
), retirement.l2 and retirement.exc_capped have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.retirement.retirement.l2_s.zero.then1` (replace an operand, retirement.retirement.l2_s): Branch settled by its guard: where retirement.l2_s takes alternative 1 (guard {
  "eq": [
    "retirement.is_s",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that retirement.zero and retirement.l1_s make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1.s1.line2b_notice.line2a.gt.0` (replace an operand, s1.s1.line2b_notice): Guarded figure: s1.line2a is s1.alimony_refused wherever s1.alimony holds, and every printed line reads s1.line2b_notice (a helper) only through choices whose guards make s1.alimony true, which, where a guard is unknown, are that unknown whatever s1.line2b_notice is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1.alimony does not hold only s1.line2b_notice's own, unprinted value can differ.
- `operand.s1.s1.line19b_notice.line19a.gt.0` (replace an operand, s1.s1.line19b_notice): Guarded figure: s1.line19a is s1.paid_refused wherever s1.alimony holds, and every printed line reads s1.line19b_notice (a helper) only through choices whose guards make s1.alimony true, which, where a guard is unknown, are that unknown whatever s1.line19b_notice is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1.alimony does not hold only s1.line19b_notice's own, unprinted value can differ.
- `operand.s1.s1.line19c_notice.line19a.gt.0` (replace an operand, s1.s1.line19c_notice): Guarded figure: s1.line19a is s1.paid_refused wherever s1.alimony holds, and every printed line reads s1.line19c_notice (a helper) only through choices whose guards make s1.alimony true, which, where a guard is unknown, are that unknown whatever s1.line19c_notice is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1.alimony does not hold only s1.line19c_notice's own, unprinted value can differ.
- `operand.s1.s1.line26.line25` (replace an operand, s1.s1.line26): Copy-chain identity: s1.line25 and s1.line24a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s179.s179.line13.line12` (replace an operand, s179.s179.line13): Floor-minus-min identity: s179.line13 is s179.line9_10 less s179.line12, floored at zero, and one of s179.line12 and s179.line11 is the ungated smaller of s179.line9_10 and the other, so s179.line9_10 less either, floored at zero, is the same at every input; s179.line9_10 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.s1a.s1a.line2e.line2b` (replace an operand, s1a.s1a.line2e): Copy-chain identity: s1a.line2b and s1a.zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.line2e.line2c` (replace an operand, s1a.s1a.line2e): Copy-chain identity: s1a.line2c and s1a.zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.line2e.line2d` (replace an operand, s1a.s1a.line2e): Copy-chain identity: s1a.line2d and s1a.zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.line4b.zero.then0` (replace an operand, s1a.s1a.line4b): Branch settled by its guard: where s1a.line4b takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line4a make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line4c_one.line4b` (replace an operand, s1a.s1a.line4c_one): Guarded figure: s1a.line4b is s1a.line4b_calc wherever s1a.part2 holds, and every printed line reads s1a.line4c_one (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line4c_one is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line4c_one's own, unprinted value can differ.
- `operand.s1a.s1a.line4c.zero.then0` (replace an operand, s1a.s1a.line4c): Branch settled by its guard: where s1a.line4c takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line4c_one make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line5.zero.then0` (replace an operand, s1a.s1a.line5): Branch settled by its guard: where s1a.line5 takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line4c make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line6_calc.line5` (replace an operand, s1a.s1a.line6_calc): Guarded figure: s1a.line5 is s1a.line5_calc wherever s1a.part2 holds, and every printed line reads s1a.line6_calc (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line6_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line6_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line6.zero.then0` (replace an operand, s1a.s1a.line6): Branch settled by its guard: where s1a.line6 takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line5 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line7_calc.line6` (replace an operand, s1a.s1a.line7_calc): Guarded figure: s1a.line6 is s1a.line6_calc wherever s1a.part2 holds, and every printed line reads s1a.line7_calc (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line7_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line7_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line7.zero.then0` (replace an operand, s1a.s1a.line7): Branch settled by its guard: where s1a.line7 takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line6 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line8.line8_calc.then1` (replace an operand, s1a.s1a.line8): Copy-chain identity: s1a.line8_calc and s1a.line3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.line9_calc.base_other.then2` (replace an operand, s1a.s1a.line9_calc): Unreachable alternative: s1a.line9_calc is a helper that every printed line reads only through choices whose guards make s1a.part2 true, and s1a.part2 true makes the guard of alternative 2 ({
  "eq": [
    "f1040.status",
    {
      "const": "mfs"
    }
  ],
  "op": "test"
}
) false; where s1a.line9_calc's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither s1a.base_other nor s1a.tips_max ever refuses; spec 4.7.3); so wherever a printed value depends on s1a.line9_calc that alternative is not taken, and replacing its value changes no printed value.
- `operand.s1a.s1a.line10_calc.line8` (replace an operand, s1a.s1a.line10_calc): Guarded figure: s1a.line8 is s1a.line8_calc wherever s1a.part2 holds, and every printed line reads s1a.line10_calc (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line10_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line10_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line10.zero.then0` (replace an operand, s1a.s1a.line10): Branch settled by its guard: where s1a.line10 takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line8 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.line10_over` (replace strict greater-than with inclusive, s1a.s1a.line10_over): The test 's1a.line8 more than s1a.line9' made inclusive adds only s1a.line8 = s1a.line9; there s1a.line10_pos is zero, the reduction s1a.line12 is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.line13_figured (s1a.line7 less s1a.line12) equals s1a.line7, the value the other branch gives. The test is read only by s1a.line13_amount. (structural conditions re-checked this run.)
- `operand.s1a.s1a.line10_over.line9.gt.1` (replace an operand, s1a.s1a.line10_over): Guarded figure: s1a.line9 is s1a.line9_calc wherever s1a.part2 holds, and every printed line reads s1a.line10_over (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line10_over is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line10_over's own, unprinted value can differ.
- `operand.s1a.s1a.line10_pos.line9` (replace an operand, s1a.s1a.line10_pos): Guarded figure: s1a.line9 is s1a.line9_calc wherever s1a.part2 holds, and every printed line reads s1a.line10_pos (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line10_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line10_pos's own, unprinted value can differ.
- `operand.s1a.s1a.line12.zero.then0` (replace an operand, s1a.s1a.line12): Branch settled by its guard: where s1a.line12 takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line11_thousands make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line13_figured.line12` (replace an operand, s1a.s1a.line13_figured): Guarded figure: s1a.line12 is s1a.line12_calc wherever s1a.part2 holds, and every printed line reads s1a.line13_figured (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.line13_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.line13_figured's own, unprinted value can differ.
- `operand.s1a.s1a.line13_ssn.zero.then0` (replace an operand, s1a.s1a.line13_ssn): s1a.line13_ssn's s1a.tip_ssn-false alternative is s1a.zero; the mutant reads s1a.line13_figured, s1a.line7 less s1a.line12, floored at zero. With s1a.tip_ssn known false, s1a.part2 (all[s1a.tips true, status not mfs, s1a.tip_ssn true]) is false, so s1a.line7 and s1a.line12 take s1a.zero and s1a.line13_figured is $0. Where s1a.tip_ssn is unknown, s1a.part2 is false or unknown (s1a.tips and the status are inputs), so s1a.line7 and s1a.line12, each a choice on s1a.part2 with an s1a.zero alternative, are $0 or that unknown, never a refusal (spec 4.7.3), and so is s1a.line13_figured; the base's s1a.zero is not a refusal either, so s1a.line13_ssn is s1a.tip_ssn's unknown on both routes. (Premises pinned: s1a.line13_ssn, s1a.line13_figured, s1a.line7, s1a.line12, s1a.part2, s1a.tip_ssn, s1a.tips, s1a.tip_ssn_count, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line13_figured.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line13_claim.line13_ssn.then0` (replace an operand, s1a.s1a.line13_claim): s1a.line13_claim's single alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.line13, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.line13 (spec 4.7.3), but s1a.line13's other alternative, s1a.zero, never refuses, so s1a.line13 is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is single, s1a.part2 is all[s1a.tips true, status not mfs, s1a.tip_ssn true], so it has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9 take s1a.zero, s1a.line10_over (is s1a.line8 more than s1a.line9) is false and s1a.line13_amount is s1a.line7, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line13_claim, s1a.line13, s1a.line13_ssn, s1a.line13_amount, s1a.line13_figured, s1a.line7, s1a.line12, s1a.line8, s1a.line9, s1a.line10_over, s1a.part2, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line13_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line13_claim.line13_ssn.then1` (replace an operand, s1a.s1a.line13_claim): s1a.line13_claim's mfj alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.line13, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.line13 (spec 4.7.3), but s1a.line13's other alternative, s1a.zero, never refuses, so s1a.line13 is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is mfj, s1a.part2 is all[s1a.tips true, status not mfs, s1a.tip_ssn true], so it has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9 take s1a.zero, s1a.line10_over (is s1a.line8 more than s1a.line9) is false and s1a.line13_amount is s1a.line7, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line13_claim, s1a.line13, s1a.line13_ssn, s1a.line13_amount, s1a.line13_figured, s1a.line7, s1a.line12, s1a.line8, s1a.line9, s1a.line10_over, s1a.part2, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line13_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line13_claim.zero.then2` (replace an operand, s1a.s1a.line13_claim): s1a.line13_claim's married-filing-separately alternative is s1a.zero ($0); the mutant reads s1a.line13_amount. s1a.line13_claim is read only by s1a.line13, in its s1a.tips-true alternative. With the status known to be mfs, s1a.part2 (all[s1a.tips true, status not mfs, s1a.tip_ssn true]) is false, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9 each take s1a.zero, s1a.line10_over is false and s1a.line13_amount is s1a.line7, $0: the two values agree. Where the status is unknown both are ways (spec 4.7.3). s1a.tip_ssn is any[all[status not mfj, household.taxpayer_work_ssn], all[status mfj, s1a.tip_ssn_count > 0]]; each all-test then meets the unknown status first, so it is false or unknown, never true, and never a refusal (s1a.tip_ssn_count and household.taxpayer_work_ssn are counts over the person roster with no refusal gates); so s1a.tip_ssn is false or unknown and s1a.line13_ssn is $0 or unknown, never a refusal, on the other four ways. The claim line is then the status's unknown on both routes. (Premises pinned: s1a.line13_claim, s1a.line13, s1a.line13_ssn, s1a.line13_amount, s1a.line13_figured, s1a.line7, s1a.line12, s1a.line8, s1a.line9, s1a.line10_over, s1a.part2, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line13_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line13_claim.line13_ssn.then3` (replace an operand, s1a.s1a.line13_claim): s1a.line13_claim's hoh alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.line13, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.line13 (spec 4.7.3), but s1a.line13's other alternative, s1a.zero, never refuses, so s1a.line13 is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is hoh, s1a.part2 is all[s1a.tips true, status not mfs, s1a.tip_ssn true], so it has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9 take s1a.zero, s1a.line10_over (is s1a.line8 more than s1a.line9) is false and s1a.line13_amount is s1a.line7, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line13_claim, s1a.line13, s1a.line13_ssn, s1a.line13_amount, s1a.line13_figured, s1a.line7, s1a.line12, s1a.line8, s1a.line9, s1a.line10_over, s1a.part2, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line13_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line13_claim.line13_ssn.then4` (replace an operand, s1a.s1a.line13_claim): s1a.line13_claim's qss alternative is s1a.line13_ssn; the mutant reads s1a.line13_amount. s1a.line13_claim's only reader is s1a.line13, a choice on s1a.tips (false: s1a.zero; true: s1a.line13_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.line13 (spec 4.7.3), but s1a.line13's other alternative, s1a.zero, never refuses, so s1a.line13 is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is qss, s1a.part2 is all[s1a.tips true, status not mfs, s1a.tip_ssn true], so it has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.line13_ssn take s1a.line13_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9 take s1a.zero, s1a.line10_over (is s1a.line8 more than s1a.line9) is false and s1a.line13_amount is s1a.line7, $0, which is s1a.line13_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.line7, s1a.line12, s1a.line8 and s1a.line9, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.line10_over is unknown and s1a.line13_amount, whose two alternatives are then unknown, is unknown; s1a.line13_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line13_claim, s1a.line13, s1a.line13_ssn, s1a.line13_amount, s1a.line13_figured, s1a.line7, s1a.line12, s1a.line8, s1a.line9, s1a.line10_over, s1a.part2, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line13_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line14b.zero.then0` (replace an operand, s1a.s1a.line14b): Branch settled by its guard: where s1a.line14b takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line14a make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line14c_calc.line14b` (replace an operand, s1a.s1a.line14c_calc): Guarded figure: s1a.line14b is s1a.line14b_calc wherever s1a.part3 holds, and every printed line reads s1a.line14c_calc (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.line14c_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.line14c_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line14c.zero.then0` (replace an operand, s1a.s1a.line14c): Branch settled by its guard: where s1a.line14c takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line14b make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.ot_max.ot_max_other.then2` (replace an operand, s1a.s1a.ot_max): Unreachable alternative: s1a.ot_max is a helper that every printed line reads only through choices whose guards make s1a.part3 true, and s1a.part3 true makes the guard of alternative 2 ({
  "eq": [
    "f1040.status",
    {
      "const": "mfs"
    }
  ],
  "op": "test"
}
) false; where s1a.ot_max's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (the values compared, or another alternative still possible, cannot refuse while the guard is unknown; spec 4.7.3); so wherever a printed value depends on s1a.ot_max that alternative is not taken, and replacing its value changes no printed value.
- `operand.s1a.s1a.line17_calc.base_other.then2` (replace an operand, s1a.s1a.line17_calc): Unreachable alternative: s1a.line17_calc is a helper that every printed line reads only through choices whose guards make s1a.part3 true, and s1a.part3 true makes the guard of alternative 2 ({
  "eq": [
    "f1040.status",
    {
      "const": "mfs"
    }
  ],
  "op": "test"
}
) false; where s1a.line17_calc's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (the values compared, or another alternative still possible, cannot refuse while the guard is unknown; spec 4.7.3); so wherever a printed value depends on s1a.line17_calc that alternative is not taken, and replacing its value changes no printed value.
- `operand.s1a.s1a.line17.zero.then0` (replace an operand, s1a.s1a.line17): Branch settled by its guard: where s1a.line17 takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line15 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line18_calc.line16` (replace an operand, s1a.s1a.line18_calc): Guarded figure: s1a.line16 is s1a.line16_calc wherever s1a.part3 holds, and every printed line reads s1a.line18_calc (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.line18_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.line18_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line18.zero.then0` (replace an operand, s1a.s1a.line18): Branch settled by its guard: where s1a.line18 takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line16 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.line18_over` (replace strict greater-than with inclusive, s1a.s1a.line18_over): The test 's1a.line16 more than s1a.line17' made inclusive adds only s1a.line16 = s1a.line17; there s1a.line18_pos is zero, the reduction s1a.line20 is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.line21_figured (s1a.line15 less s1a.line20) equals s1a.line15, the value the other branch gives. The test is read only by s1a.line21_amount. (structural conditions re-checked this run.)
- `operand.s1a.s1a.line18_over.line17.gt.1` (replace an operand, s1a.s1a.line18_over): Guarded figure: s1a.line17 is s1a.line17_calc wherever s1a.part3 holds, and every printed line reads s1a.line18_over (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.line18_over is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.line18_over's own, unprinted value can differ.
- `operand.s1a.s1a.line18_pos.line17` (replace an operand, s1a.s1a.line18_pos): Guarded figure: s1a.line17 is s1a.line17_calc wherever s1a.part3 holds, and every printed line reads s1a.line18_pos (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.line18_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.line18_pos's own, unprinted value can differ.
- `operand.s1a.s1a.line20.zero.then0` (replace an operand, s1a.s1a.line20): Branch settled by its guard: where s1a.line20 takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line19_thousands make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line21_figured.line20` (replace an operand, s1a.s1a.line21_figured): Guarded figure: s1a.line20 is s1a.line20_calc wherever s1a.part3 holds, and every printed line reads s1a.line21_figured (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.line21_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.line21_figured's own, unprinted value can differ.
- `operand.s1a.s1a.line21_ssn.zero.then0` (replace an operand, s1a.s1a.line21_ssn): s1a.line21_ssn's s1a.ot_ssn-false alternative is s1a.zero; the mutant reads s1a.line21_figured, s1a.line15 less s1a.line20, floored at zero. With s1a.ot_ssn known false, s1a.part3 (all[s1a.overtime true, status not mfs, s1a.ot_ssn true]) is false, so s1a.line15 and s1a.line20 take s1a.zero and s1a.line21_figured is $0. Where s1a.ot_ssn is unknown, s1a.part3 is false or unknown (s1a.overtime and the status are inputs), so s1a.line15 and s1a.line20, each a choice on s1a.part3 with an s1a.zero alternative, are $0 or that unknown, never a refusal (spec 4.7.3), and so is s1a.line21_figured; the base's s1a.zero is not a refusal either, so s1a.line21_ssn is s1a.ot_ssn's unknown on both routes. (Premises pinned: s1a.line21_ssn, s1a.line21_figured, s1a.line15, s1a.line20, s1a.part3, s1a.ot_ssn, s1a.overtime, s1a.ot_ssn_count, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line21_figured.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line21_claim.line21_ssn.then0` (replace an operand, s1a.s1a.line21_claim): s1a.line21_claim's single alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.line21, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.line21 (spec 4.7.3), but s1a.line21's other alternative, s1a.zero, never refuses, so s1a.line21 is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is single, s1a.part3 is all[s1a.overtime true, status not mfs, s1a.ot_ssn true], so it has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17 take s1a.zero, s1a.line18_over (is s1a.line16 more than s1a.line17) is false and s1a.line21_amount is s1a.line15, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line21_claim, s1a.line21, s1a.line21_ssn, s1a.line21_amount, s1a.line21_figured, s1a.line15, s1a.line20, s1a.line16, s1a.line17, s1a.line18_over, s1a.part3, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line21_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line21_claim.line21_ssn.then1` (replace an operand, s1a.s1a.line21_claim): s1a.line21_claim's mfj alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.line21, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.line21 (spec 4.7.3), but s1a.line21's other alternative, s1a.zero, never refuses, so s1a.line21 is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is mfj, s1a.part3 is all[s1a.overtime true, status not mfs, s1a.ot_ssn true], so it has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17 take s1a.zero, s1a.line18_over (is s1a.line16 more than s1a.line17) is false and s1a.line21_amount is s1a.line15, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line21_claim, s1a.line21, s1a.line21_ssn, s1a.line21_amount, s1a.line21_figured, s1a.line15, s1a.line20, s1a.line16, s1a.line17, s1a.line18_over, s1a.part3, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line21_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line21_claim.zero.then2` (replace an operand, s1a.s1a.line21_claim): s1a.line21_claim's married-filing-separately alternative is s1a.zero ($0); the mutant reads s1a.line21_amount. s1a.line21_claim is read only by s1a.line21, in its s1a.overtime-true alternative. With the status known to be mfs, s1a.part3 (all[s1a.overtime true, status not mfs, s1a.ot_ssn true]) is false, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17 each take s1a.zero, s1a.line18_over is false and s1a.line21_amount is s1a.line15, $0: the two values agree. Where the status is unknown both are ways (spec 4.7.3). s1a.ot_ssn is any[all[status not mfj, household.taxpayer_work_ssn], all[status mfj, s1a.ot_ssn_count > 0]]; each all-test then meets the unknown status first, so it is false or unknown, never true, and never a refusal (s1a.ot_ssn_count and household.taxpayer_work_ssn are counts over the person roster with no refusal gates); so s1a.ot_ssn is false or unknown and s1a.line21_ssn is $0 or unknown, never a refusal, on the other four ways. The claim line is then the status's unknown on both routes. (Premises pinned: s1a.line21_claim, s1a.line21, s1a.line21_ssn, s1a.line21_amount, s1a.line21_figured, s1a.line15, s1a.line20, s1a.line16, s1a.line17, s1a.line18_over, s1a.part3, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line21_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line21_claim.line21_ssn.then3` (replace an operand, s1a.s1a.line21_claim): s1a.line21_claim's hoh alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.line21, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.line21 (spec 4.7.3), but s1a.line21's other alternative, s1a.zero, never refuses, so s1a.line21 is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is hoh, s1a.part3 is all[s1a.overtime true, status not mfs, s1a.ot_ssn true], so it has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17 take s1a.zero, s1a.line18_over (is s1a.line16 more than s1a.line17) is false and s1a.line21_amount is s1a.line15, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line21_claim, s1a.line21, s1a.line21_ssn, s1a.line21_amount, s1a.line21_figured, s1a.line15, s1a.line20, s1a.line16, s1a.line17, s1a.line18_over, s1a.part3, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line21_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line21_claim.line21_ssn.then4` (replace an operand, s1a.s1a.line21_claim): s1a.line21_claim's qss alternative is s1a.line21_ssn; the mutant reads s1a.line21_amount. s1a.line21_claim's only reader is s1a.line21, a choice on s1a.overtime (false: s1a.zero; true: s1a.line21_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.line21 (spec 4.7.3), but s1a.line21's other alternative, s1a.zero, never refuses, so s1a.line21 is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is qss, s1a.part3 is all[s1a.overtime true, status not mfs, s1a.ot_ssn true], so it has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.line21_ssn take s1a.line21_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17 take s1a.zero, s1a.line18_over (is s1a.line16 more than s1a.line17) is false and s1a.line21_amount is s1a.line15, $0, which is s1a.line21_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.line15, s1a.line20, s1a.line16 and s1a.line17, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.line18_over is unknown and s1a.line21_amount, whose two alternatives are then unknown, is unknown; s1a.line21_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.line21_claim, s1a.line21, s1a.line21_ssn, s1a.line21_amount, s1a.line21_figured, s1a.line15, s1a.line20, s1a.line16, s1a.line17, s1a.line18_over, s1a.part3, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.line21_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line24_calc.line23` (replace an operand, s1a.s1a.line24_calc): Guarded figure: s1a.line23 is s1a.line23_total wherever s1a.carloan holds, and every printed line reads s1a.line24_calc (a helper) only through choices whose guards make s1a.carloan true, which, where a guard is unknown, are that unknown whatever s1a.line24_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.carloan does not hold only s1a.line24_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line27_calc.line25` (replace an operand, s1a.s1a.line27_calc): Guarded figure: s1a.line25 is s1a.line25_calc wherever s1a.part4 holds, and every printed line reads s1a.line27_calc (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.line27_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.line27_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line27.zero.then0` (replace an operand, s1a.s1a.line27): Branch settled by its guard: where s1a.line27 takes alternative 0 (guard {
  "eq": [
    "s1a.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line25 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.line27_over` (replace strict greater-than with inclusive, s1a.s1a.line27_over): The test 's1a.line25 more than s1a.line26' made inclusive adds only s1a.line25 = s1a.line26; there s1a.line27_pos is zero, the reduction s1a.line29 is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.line30_figured (s1a.line24 less s1a.line29) equals s1a.line24, the value the other branch gives. The test is read only by s1a.line30_amount. (structural conditions re-checked this run.)
- `operand.s1a.s1a.line27_over.line26.gt.1` (replace an operand, s1a.s1a.line27_over): Guarded figure: s1a.line26 is s1a.line26_calc wherever s1a.part4 holds, and every printed line reads s1a.line27_over (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.line27_over is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.line27_over's own, unprinted value can differ.
- `operand.s1a.s1a.line27_pos.line26` (replace an operand, s1a.s1a.line27_pos): Guarded figure: s1a.line26 is s1a.line26_calc wherever s1a.part4 holds, and every printed line reads s1a.line27_pos (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.line27_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.line27_pos's own, unprinted value can differ.
- `operand.s1a.s1a.line29.zero.then0` (replace an operand, s1a.s1a.line29): Branch settled by its guard: where s1a.line29 takes alternative 0 (guard {
  "eq": [
    "s1a.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line28_thousands make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line30_figured.line29` (replace an operand, s1a.s1a.line30_figured): Guarded figure: s1a.line29 is s1a.line29_calc wherever s1a.part4 holds, and every printed line reads s1a.line30_figured (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.line30_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.line30_figured's own, unprinted value can differ.
- `operand.s1a.s1a.line30.zero.then0` (replace an operand, s1a.s1a.line30): s1a.line30's carloan-false alternative is s1a.zero; the mutant reads s1a.line30_figured, line24 less line29, floored at zero, both choices on s1a.part4 (carloan true) between s1a.zero and their figures. With carloan known false, part4 is false and both are $0, so line30_figured is $0. Where carloan is unknown, part4 is that unknown, line24 and line29 are $0 or unknown, never a refusal (spec 4.7.3), and so is line30_figured; s1a.line30 is then carloan's unknown on both routes. (Premises pinned: s1a.line30, s1a.line30_figured, s1a.line24, s1a.line29, s1a.part4, s1a.carloan, s1a.zero; the mutant reads s1a.line30_figured.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.line32_calc.senior_base_other.then2` (replace an operand, s1a.s1a.line32_calc): Unreachable alternative: s1a.line32_calc is a helper that every printed line reads only through choices whose guards make s1a.part5 true, and s1a.part5 true makes the guard of alternative 2 ({
  "eq": [
    "f1040.status",
    {
      "const": "mfs"
    }
  ],
  "op": "test"
}
) false; where s1a.line32_calc's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (the values compared, or another alternative still possible, cannot refuse while the guard is unknown; spec 4.7.3); so wherever a printed value depends on s1a.line32_calc that alternative is not taken, and replacing its value changes no printed value.
- `operand.s1a.s1a.line33_calc.line31` (replace an operand, s1a.s1a.line33_calc): Guarded figure: s1a.line31 is s1a.line31_calc wherever s1a.part5 holds, and every printed line reads s1a.line33_calc (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.line33_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.line33_calc's own, unprinted value can differ.
- `operand.s1a.s1a.line33.zero.then0` (replace an operand, s1a.s1a.line33): Branch settled by its guard: where s1a.line33 takes alternative 0 (guard {
  "eq": [
    "s1a.part5",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line31 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.line33_over` (replace strict greater-than with inclusive, s1a.s1a.line33_over): The test 's1a.line31 more than s1a.line32' made inclusive adds only s1a.line31 = s1a.line32; there s1a.line33_pos is zero, the reduction s1a.line34 is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.line35_figured (s1a.senior_amount less s1a.line34) equals s1a.senior_amount, the value the other branch gives. The test is read only by s1a.line35_calc. (structural conditions re-checked this run.)
- `operand.s1a.s1a.line33_over.line32.gt.1` (replace an operand, s1a.s1a.line33_over): Guarded figure: s1a.line32 is s1a.line32_calc wherever s1a.part5 holds, and every printed line reads s1a.line33_over (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.line33_over is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.line33_over's own, unprinted value can differ.
- `operand.s1a.s1a.line33_pos.line32` (replace an operand, s1a.s1a.line33_pos): Guarded figure: s1a.line32 is s1a.line32_calc wherever s1a.part5 holds, and every printed line reads s1a.line33_pos (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.line33_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.line33_pos's own, unprinted value can differ.
- `operand.s1a.s1a.line34.zero.then0` (replace an operand, s1a.s1a.line34): Branch settled by its guard: where s1a.line34 takes alternative 0 (guard {
  "eq": [
    "s1a.part5",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line33_pos make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line35_figured.line34` (replace an operand, s1a.s1a.line35_figured): Guarded figure: s1a.line34 is s1a.line34_calc wherever s1a.part5 holds, and every printed line reads s1a.line35_figured (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.line35_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.line35_figured's own, unprinted value can differ.
- `operand.s1a.s1a.line35.line35_calc.then1` (replace an operand, s1a.s1a.line35): Branch equal under a case split: where s1a.line35 takes alternative 1 (guard {
  "eq": [
    "s1a.part5",
    {
      "const": true
    }
  ],
  "op": "test"
}
), s1a.line35_calc and s1a.line35_figured have the same value in every case of s1a.line33_over (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged), through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.s1a.s1a.line36a_claim.zero.then2` (replace an operand, s1a.s1a.line36a_claim): s1a.line36a_claim's married-filing-separately alternative is s1a.zero; the mutant reads s1a.line35, a choice on s1a.part5 (all[senior_any, status not mfs]) between s1a.zero and line35_calc. With the status known to be mfs, part5 is false and line35 is s1a.zero: the two values agree. Where the status is unknown both are ways (spec 4.7.3): part5 is false or unknown (senior_any compares s1a.senior_count, a count over the person roster with no refusal gates, with 0), so line35 is $0 or that unknown, never a refusal, as the base's s1a.zero is; the claim line is then the status's unknown on both routes. (Premises pinned: s1a.line36a_claim, s1a.line35, s1a.part5, s1a.senior_any, s1a.senior_count, s1a.zero; the mutant reads s1a.line35.) (structural conditions re-checked this run.)
- `operand.s2.s2.line3.line1z` (replace an operand, s2.s2.line3): Copy-chain identity: s2.line1z and s2.line1a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s2.s2.line21.line18` (replace an operand, s2.s2.line21): Copy-chain identity: s2.line18 and s2.line17c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2b.zero` (replace an operand, s8812.s8812.line2b): Copy-chain identity: s8812.zero and s8812.line2a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2c.zero` (replace an operand, s8812.s8812.line2c): Copy-chain identity: s8812.zero and s8812.line2b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2d.line2a` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2a and s8812.line2b, s8812.line2c are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line2d.line2b` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2b and s8812.line2a, s8812.line2c are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line2d.line2c` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2c and s8812.line2a, s8812.line2b are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line14.line13` (replace an operand, s8812.s8812.line14): Copy-chain identity: s8812.line13 and s8812.clw_a5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.eiw_3.zero` (replace an operand, s8812.s8812.eiw_3): Gated zero carried earlier: s8812.zero is an ungated zero and s8812.eiw_1b the same zero behind refusal gates (s8812.combat_pay); s8812.eiw_3sum, read first, reaches s8812.eiw_1b through ungated arithmetic, so whenever s8812.eiw_1b refuses or is unknown s8812.eiw_3sum already is, and is returned first, and otherwise both operands are zero.
- `operand.sa.sa.line3.line2` (replace an operand, sa.sa.line3): Copy-chain identity: sa.line2 and sa.agi_floor expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line8b.zero` (replace an operand, sa.sa.line8b): Copy-chain identity: sa.zero and sa.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line8c.zero` (replace an operand, sa.sa.line8c): Copy-chain identity: sa.zero and sa.line8b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line13.zero` (replace an operand, sa.sa.line13): Copy-chain identity: sa.zero and sa.line8c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line15.zero` (replace an operand, sa.sa.line15): Copy-chain identity: sa.zero and sa.line13 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line16.zero.then1` (replace an operand, sa.sa.line16): Copy-chain identity: sa.zero and sa.line15 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.standard.zero.then0` (replace an operand, sa.sa.standard): sa.standard's mfs_spouse_itemizes-true alternative: standard is a helper read only by sa.itemizes and sa.deduction. In itemizes the mfs_spouse_itemizes disjunct is true and decides the any-test before its last disjunct, the only one that reads standard (an earlier unknown is outranked by the deciding true; an earlier refusal ends the test before standard is read); so itemizes is not false, and deduction reads standard only where itemizes is false or, as a way, unknown (spec 4.7.3). Where itemizes is unknown, mfs_spouse_itemizes is not true (a true disjunct decides the any-test), so the mutated alternative is not taken; where mfs_spouse_itemizes is unknown, standard's other alternative, standardraw, never refuses, so standard is that unknown on both routes. (Premises pinned: sa.standard, sa.deduction, sa.itemizes, sa.standardraw, sa.mfs_spouse_itemizes, sa.extra_blind, sa.elect_itemize; the mutant reads sa.extra_blind.) (structural conditions re-checked this run.)
- `operand.sa.sa.deduction.standard.then1` (replace an operand, sa.sa.deduction): sa.deduction's itemizes-false alternative: an any-test is known false only when every disjunct was evaluated and false with no unknown remembered (spec 4.7.2), so mfs_spouse_itemizes is known false and the comparison of line 17 with sa.standard read standard as a known value; a known standard passed its gates and took its mfs_spouse_itemizes-false alternative, whose value is standardraw, the same memoized value. Where itemizes is unknown both alternatives are ways (spec 4.7.3): every disjunct was then evaluated with no true one and no refusal, so line 17, the itemized alternative and the comparison's operand, is not a refusal, and deduction is that unknown on both routes. (Premises pinned: sa.standard, sa.deduction, sa.itemizes, sa.standardraw, sa.mfs_spouse_itemizes, sa.extra_blind, sa.elect_itemize; the mutant reads sa.standardraw.) (structural conditions re-checked this run.)
- `boundary.sc.sc.ho_over` (replace strict greater-than with inclusive, sc.sc.ho_over): The home office test 'square feet more than the cap' made inclusive adds only square feet equal to the cap, where the rate times the square feet and the rate times the cap are the same amount. The test is read only by line 4. (structural conditions re-checked this run.)
- `operand.sc.sc.ho_both.zero` (replace an operand, sc.sc.ho_both): sc.ho_both is a helper whose only reader is sc.ho_line5_lim, in its ho_no179-false alternative; ho_line5_lim is a helper whose only reader is sc.ho_line5, in its ho_unlimited-false alternative. A printed line therefore reads ho_both only after ho_unlimited and ho_no179 were found known false in the frame (spec 4.7.3, 4.7.6), and then ho_both's gate ho_both_limits, the all-test of those two being false, is true, so ho_both is its refusal at line entry and its expression, the only part the mutant changes, is not evaluated (4.7.1). Where ho_unlimited or ho_no179 is unknown those choices evaluate ho_line5_lim and ho_both as ways (4.7.3); the gate is then unknown, which leaves ho_both that unknown on both routes, or false, which needs the other flag true, so the reading choice takes its other alternative. With the gate false (ho_both or ho_line5_lim evaluated as a target) only those two helpers' own values differ. (Premises pinned: sc.ho_both, sc.ho_both_limits, sc.ho_line5_lim, sc.ho_line5, sc.ho_unlimited, sc.ho_no179, sc.ho_pre179_floor, sc.zero; the mutant reads sc.ho_pre179_floor.) (structural conditions re-checked this run.)
- `operand.sc.sc.f7206_line9.zero.then1` (replace an operand, sc.sc.f7206_line9): sc.f7206_line9's f7206_has-false alternative is sc.zero; the mutant reads sc.f7206_line8, line 4 less line 7, floored at zero. f7206_has is line 4 (profit_pos, sc.result floored at zero) more than sc.zero. With it known false line 4 is $0 and line 7 takes sc.zero, so line 8 is $0. Where f7206_has is unknown, line 4 is unknown (a refused line 4 refuses the guard and both routes alike), and line 7, a choice on f7206_has with an sc.zero alternative, is unknown (spec 4.7.3); line 8 is then unknown, never a refusal, and line 9 is f7206_has's unknown on both routes. (Premises pinned: sc.f7206_line9, sc.f7206_line8, sc.f7206_line4, sc.f7206_line7, sc.f7206_has, sc.profit_pos, sc.zero; the mutant reads sc.f7206_line8.) (structural conditions re-checked this run.)
- `operand.sc.sc.f7206_min.f7206_line13` (replace an operand, sc.sc.f7206_min): Copy-chain identity: sc.f7206_line13 and sc.f7206_line10 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sc.sc.qbi_plan.zero.then1` (replace an operand, sc.sc.qbi_plan): Branch settled by its guard: where sc.qbi_plan takes alternative 1 (guard {
  "eq": [
    "sc.qbi_has",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sc.zero and sc.qbi_se make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.scveh.scveh.bonus_forty.line15` (replace an operand, scveh.scveh.bonus_forty): Copy-chain identity: scveh.line15 and scveh.bonus_full expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.scveh.scveh.line17.line16` (replace an operand, scveh.scveh.line17): Floor-minus-min identity: scveh.line17 is scveh.line11 less scveh.line16, floored at zero, and one of scveh.line16 and scveh.bonus_allowed is the ungated smaller of scveh.line11 and the other, so scveh.line11 less either, floored at zero, is the same at every input; scveh.line11 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.scveh.scveh.l5.k5` (replace an operand, scveh.scveh.l5): scveh.l5 looks up the vehicle's year-5 limit; the mutant looks up year 4. Only a 2019 vehicle's scveh.l5 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.is2019, so scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on is2019 taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.d5.l5` (replace an operand, scveh.scveh.d5): scveh.d5 is min(l5, t5); the mutant reads d4 = min(l4, t4) in place of l5, and min(min(l4, t4), t5) = min(l5, t5) when l4 = l5 and t4 >= t5. Only a 2019 vehicle's scveh.d5 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.is2019, so scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on is2019 taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.l6.k6` (replace an operand, scveh.scveh.l6): scveh.l6 looks up the vehicle's year-6 limit; the mutant looks up year 5. Only a 2019 vehicle's scveh.l6 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.is2019, so scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on is2019 taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.d6.l6` (replace an operand, scveh.scveh.d6): scveh.d6 is min(l6, t6); the mutant reads d5 = min(l5, t5) in place of l6, and min(min(l5, t5), t6) = min(l6, t6) when l5 = l6 and t5 >= t6. Only a 2019 vehicle's scveh.d6 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.is2019, so scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on is2019 taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.macrs.zero.then1` (replace an operand, scveh.scveh.macrs): Branch settled by its guard: where scveh.macrs takes alternative 1 (guard {
  "eq": [
    "scveh.is_actual_owned",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that scveh.zero and scveh.bonus make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.scveh.scveh.s179_2025.zero.then1` (replace an operand, scveh.scveh.s179_2025): Branch settled by its guard: where scveh.s179_2025 takes alternative 1 (guard {
  "eq": [
    "scveh.is_actual_owned",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that scveh.zero and scveh.macrs make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.scveh.scveh.mq_q4.zero.then1` (replace an operand, scveh.scveh.mq_q4): Branch settled by its guard: where scveh.mq_q4 takes alternative 1 (guard {
  "eq": [
    "scveh.is_actual_owned",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that scveh.zero and scveh.s179_2025 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.scveh.scveh.mq_total.zero.then1` (replace an operand, scveh.scveh.mq_total): Branch settled by its guard: where scveh.mq_total takes alternative 1 (guard {
  "eq": [
    "scveh.is_actual_owned",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that scveh.zero and scveh.mq_q4 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.scveh.scveh.cost179.zero.then1` (replace an operand, scveh.scveh.cost179): Branch settled by its guard: where scveh.cost179 takes alternative 1 (guard {
  "eq": [
    "scveh.is_actual_owned",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that scveh.zero and scveh.mq_total make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.scveh.scveh.mq_q4_o.mq_q4_a2.then0` (replace an operand, scveh.scveh.mq_q4_o): Copy-chain identity: scveh.mq_q4_a2 and scveh.q4_basis expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line19.zero.then1` (replace an operand, sd.sd.line19): Branch settled by its guard: where sd.line19 takes alternative 1 (guard {
  "eq": [
    "sd.line17",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sd.zero and sd.line18 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sd.sd.line5.zero` (replace an operand, sd.sd.line5): Copy-chain identity: sd.zero and sd.line4 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line6.zero.then1` (replace an operand, sd.sd.line6): Copy-chain identity: sd.zero and sd.line5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line12.zero` (replace an operand, sd.sd.line12): Copy-chain identity: sd.zero and sd.line11 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line14.zero.then1` (replace an operand, sd.sd.line14): Copy-chain identity: sd.zero and sd.line12 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.to1040.line21.then0` (replace an operand, sd.sd.to1040): sd.to1040's has_loss-true alternative is sd.line21, a choice on the same has_loss taking limited_loss (the larger of line 16 and the loss-limit parameter) or sd.zero; the mutant reads limited_loss. With has_loss known true line 21 is limited_loss, the same memoized value. has_loss compares line 16 with 0, so where it is unknown line 16 is unknown (a refused line 16 refuses the guard and both routes alike): limited_loss is then unknown, line 21 is unknown (spec 4.7.3) and so is the other alternative, line 16; neither route is a refusal on every way, and to1040 is has_loss's unknown on both. (Premises pinned: sd.to1040, sd.line21, sd.limited_loss, sd.line16, sd.has_loss, sd.zero; the mutant reads sd.limited_loss.) (structural conditions re-checked this run.)
- `operand.sdtw.sdtw.line17.line16` (replace an operand, sdtw.sdtw.line17): Line 17 is min(line 14, line 16) and line 16 is min(line 1, line 15). Line 13 is line 10 less min(line 9, line 11), and line 10 is line 6 plus line 9 with both floored at zero, so line 13 is not negative and line 14 (line 1 less line 13, floored) is at most line 1, which is not negative. Then min(line 14, min(line 1, line 15)) = min(line 14, line 15); and line 14 reads line 1 first, so a refusal or unknown in line 1 reaches line 17 through line 14 on both routes. (structural conditions re-checked this run.)
- `operand.sdtw.sdtw.line24.zero.then1` (replace an operand, sdtw.sdtw.line24): Branch settled by its guard: where sdtw.line24 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line23 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.line26.zero.then1` (replace an operand, sdtw.sdtw.line26): Branch settled by its guard: where sdtw.line26 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line25 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw27.line26` (replace an operand, sdtw.sdtw.raw27): Guarded figure: sdtw.line26 is sdtw.raw26 wherever sdtw.after22 holds, and every printed line reads sdtw.raw27 (a helper) only through choices whose guards make sdtw.after22 true, which, where a guard is unknown, are that unknown whatever sdtw.raw27 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after22 does not hold only sdtw.raw27's own, unprinted value can differ.
- `operand.sdtw.sdtw.line27.zero.then1` (replace an operand, sdtw.sdtw.line27): Branch settled by its guard: where sdtw.line27 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line26 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw28.line22` (replace an operand, sdtw.sdtw.raw28): Guarded figure: sdtw.line24 is sdtw.line22 wherever sdtw.after22 holds, and every printed line reads sdtw.raw28 (a helper) only through choices whose guards make sdtw.after22 true, which, where a guard is unknown, are that unknown whatever sdtw.raw28 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after22 does not hold only sdtw.raw28's own, unprinted value can differ.
- `operand.sdtw.sdtw.line28.zero.then1` (replace an operand, sdtw.sdtw.line28): Branch settled by its guard: where sdtw.line28 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line24 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw29.line27` (replace an operand, sdtw.sdtw.raw29): Guarded figure: sdtw.line27 is sdtw.raw27 wherever sdtw.after22 holds, and every printed line reads sdtw.raw29 (a helper) only through choices whose guards make sdtw.after22 true, which, where a guard is unknown, are that unknown whatever sdtw.raw29 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after22 does not hold only sdtw.raw29's own, unprinted value can differ.
- `operand.sdtw.sdtw.line29.zero.then1` (replace an operand, sdtw.sdtw.line29): Branch settled by its guard: where sdtw.line29 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line27 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw30.line29` (replace an operand, sdtw.sdtw.raw30): Guarded figure: sdtw.line29 is sdtw.raw29 wherever sdtw.after22 holds, and every printed line reads sdtw.raw30 (a helper) only through choices whose guards make sdtw.after22 true, which, where a guard is unknown, are that unknown whatever sdtw.raw30 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after22 does not hold only sdtw.raw30's own, unprinted value can differ.
- `operand.sdtw.sdtw.line30.zero.then1` (replace an operand, sdtw.sdtw.line30): Branch settled by its guard: where sdtw.line30 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line29 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw31.line30` (replace an operand, sdtw.sdtw.raw31): Guarded figure: sdtw.line30 is sdtw.raw30 wherever sdtw.after22 holds, and every printed line reads sdtw.raw31 (a helper) only through choices whose guards make sdtw.after22 true, which, where a guard is unknown, are that unknown whatever sdtw.raw31 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after22 does not hold only sdtw.raw31's own, unprinted value can differ.
- `operand.sdtw.sdtw.line31.zero.then1` (replace an operand, sdtw.sdtw.line31): Branch settled by its guard: where sdtw.line31 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line30 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.line32.zero.then1` (replace an operand, sdtw.sdtw.line32): Branch settled by its guard: where sdtw.line32 takes alternative 1 (guard {
  "eq": [
    "sdtw.after22",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line28 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw33.line32` (replace an operand, sdtw.sdtw.raw33): Guarded figure: sdtw.line32 is sdtw.raw32 wherever sdtw.after22 holds, and every printed line reads sdtw.raw33 (a helper) only through choices whose guards make sdtw.after22 true, which, where a guard is unknown, are that unknown whatever sdtw.raw33 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after22 does not hold only sdtw.raw33's own, unprinted value can differ.
- `operand.sdtw.sdtw.raw34.line33` (replace an operand, sdtw.sdtw.raw34): Guarded figure: sdtw.line33 is sdtw.raw33 wherever sdtw.after32 holds, and every printed line reads sdtw.raw34 (a helper) only through choices whose guards make sdtw.after32 true, which, where a guard is unknown, are that unknown whatever sdtw.raw34 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.after32 does not hold only sdtw.raw34's own, unprinted value can differ.
- `operand.sdtw.sdtw.line34.zero.then1` (replace an operand, sdtw.sdtw.line34): Branch settled by its guard: where sdtw.line34 takes alternative 1 (guard {
  "eq": [
    "sdtw.after32",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line33 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.line36.zero.then1` (replace an operand, sdtw.sdtw.line36): Branch settled by its guard: where sdtw.line36 takes alternative 1 (guard {
  "eq": [
    "sdtw.use1250",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line35 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.line37.zero.then1` (replace an operand, sdtw.sdtw.line37): Branch settled by its guard: where sdtw.line37 takes alternative 1 (guard {
  "eq": [
    "sdtw.use1250",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line36 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw38.line37` (replace an operand, sdtw.sdtw.raw38): Guarded figure: sdtw.line37 is sdtw.raw37 wherever sdtw.use1250 holds, and every printed line reads sdtw.raw38 (a helper) only through choices whose guards make sdtw.use1250 true, which, where a guard is unknown, are that unknown whatever sdtw.raw38 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.use1250 does not hold only sdtw.raw38's own, unprinted value can differ.
- `operand.sdtw.sdtw.line38.zero.then1` (replace an operand, sdtw.sdtw.line38): Branch settled by its guard: where sdtw.line38 takes alternative 1 (guard {
  "eq": [
    "sdtw.use1250",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line37 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw39.line38` (replace an operand, sdtw.sdtw.raw39): Guarded figure: sdtw.line38 is sdtw.raw38 wherever sdtw.use1250 holds, and every printed line reads sdtw.raw39 (a helper) only through choices whose guards make sdtw.use1250 true, which, where a guard is unknown, are that unknown whatever sdtw.raw39 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.use1250 does not hold only sdtw.raw39's own, unprinted value can differ.
- `operand.sdtw.sdtw.line39.zero.then1` (replace an operand, sdtw.sdtw.line39): Branch settled by its guard: where sdtw.line39 takes alternative 1 (guard {
  "eq": [
    "sdtw.use1250",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line38 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw40.line39` (replace an operand, sdtw.sdtw.raw40): Guarded figure: sdtw.line39 is sdtw.raw39 wherever sdtw.use1250 holds, and every printed line reads sdtw.raw40 (a helper) only through choices whose guards make sdtw.use1250 true, which, where a guard is unknown, are that unknown whatever sdtw.raw40 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.use1250 does not hold only sdtw.raw40's own, unprinted value can differ.
- `operand.sdtw.sdtw.line40.zero.then1` (replace an operand, sdtw.sdtw.line40): Branch settled by its guard: where sdtw.line40 takes alternative 1 (guard {
  "eq": [
    "sdtw.use1250",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line39 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw42.line41` (replace an operand, sdtw.sdtw.raw42): Guarded figure: sdtw.line41 is sdtw.raw41 wherever sdtw.use28 holds, and every printed line reads sdtw.raw42 (a helper) only through choices whose guards make sdtw.use28 true, which, where a guard is unknown, are that unknown whatever sdtw.raw42 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.use28 does not hold only sdtw.raw42's own, unprinted value can differ.
- `operand.sdtw.sdtw.line42.zero.then1` (replace an operand, sdtw.sdtw.line42): Branch settled by its guard: where sdtw.line42 takes alternative 1 (guard {
  "eq": [
    "sdtw.use28",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line41 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.raw43.line42` (replace an operand, sdtw.sdtw.raw43): Guarded figure: sdtw.line42 is sdtw.raw42 wherever sdtw.use28 holds, and every printed line reads sdtw.raw43 (a helper) only through choices whose guards make sdtw.use28 true, which, where a guard is unknown, are that unknown whatever sdtw.raw43 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sdtw.use28 does not hold only sdtw.raw43's own, unprinted value can differ.
- `operand.sdtw.sdtw.line43.zero.then1` (replace an operand, sdtw.sdtw.line43): Branch settled by its guard: where sdtw.line43 takes alternative 1 (guard {
  "eq": [
    "sdtw.use28",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sdtw.zero and sdtw.line42 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.sdtw.sdtw.line45.line43` (replace an operand, sdtw.sdtw.line45): Line 43 is its helper (28% of line 42) when sdtw.use28 holds and $0 otherwise, and line 42 is $0 under the same gate; so when the gate is false the helper is 28% of $0, and when it is unknown or refused line 42 and line 43 return the gate's value, which the rate passes through. Line 45 reads the same value either way. (structural conditions re-checked this run.)
- `boundary.sli.sli.over` (replace strict greater-than with inclusive, sli.sli.over): The test 'line 4 more than line 5' made inclusive adds only the case line 4 = line 5; there line 6 (line 4 less line 5) is zero or negative, the prorate ratio is kept at 0, and the prorated amount equals the skip branch's zero. The test is read only by line 8. (structural conditions re-checked this run.)
- `operand.sli.sli.line9.line8` (replace an operand, sli.sli.line9): Reading the prorated line directly instead of line 8 differs only when line 4 is not more than line 5; there line 6 (line 4 less line 5) is zero or negative, the prorate ratio is kept at 0, and the prorated amount equals the skip branch's zero. The test is read only by line 8. (structural conditions re-checked this run.)
- `operand.ssb.ssb.show16_18.mfs_together.all.1.any.0.eq.0` (replace an operand, ssb.ssb.show16_18): show16_18 is all[past7, any[mfs_together, past9]]; the mutant reads show10_15 (all[show8_9, past9], show8_9 being all[lines8_to_15, past7] and lines8_to_15 being mfs_together false) in place of mfs_together. With mfs_together true, line 8 is mfs_base with lived_apart false, that is ssb.zero, so line 9 (line 7 less line 8, floored) is line 7 and past9 is past7, true where the any-test is reached: both are true. With mfs_together false, show10_15 is past9 (past7 is already true), so the any-tests agree. mfs_together is unknown only when the status or lived_apart is unknown; then line 8 is unknown and line 9 is unknown or line 7's refusal (subtract evaluates both), so past9 is unknown or that refusal, which past7 has already returned: both any-tests are unknown. With past7 unknown (line 7 unknown, the outer test continuing past it), line 9 is unknown or line 8's refusal, so past9 is unknown or that refusal; show8_9 is false (mfs_together true) or unknown, and show10_15 is false or past9's value. With mfs_together true the base any-test is true and the mutant's is past9's unknown (line 8 is then $0); otherwise both any-tests are past9's value. The outer test, holding past7's unknown, is unknown on both routes, or the same refusal. (Premises pinned: ssb.show16_18, ssb.mfs_together, ssb.show10_15, ssb.show8_9, ssb.lines8_to_15, ssb.past7, ssb.past9, ssb.line9, ssb.line8, ssb.mfs_base, ssb.line7, ssb.zero, ssb.lived_apart; the mutant reads ssb.show10_15.) (structural conditions re-checked this run.)
- `operand.ssb.ssb.show16_18.past9.all.1.any.1.eq.0` (replace an operand, ssb.ssb.show16_18): show16_18 is all[past7, any[mfs_together, past9]]; the mutant reads show10_15, all[all[mfs_together false, past7], past9], in place of past9. The second disjunct is reached only when mfs_together was not true. With mfs_together false and past7 true (the outer test's first conjunct), show10_15 is past9. mfs_together is unknown only when the status or lived_apart is unknown; then line 8 is unknown, so past9 is unknown or line 7's refusal (already returned by past7): show10_15 is then unknown too, and both any-tests are unknown. With past7 unknown (line 7 unknown, the outer test continuing past it), past9 is unknown or line 8's refusal, and show10_15, all[show8_9 (unknown, since lines8_to_15 is true or unknown there and past7 is unknown), past9], is past9's value; the second disjuncts agree, and the outer test, holding past7's unknown, is unknown on both routes or the same refusal. (Premises pinned: ssb.show16_18, ssb.mfs_together, ssb.show10_15, ssb.show8_9, ssb.lines8_to_15, ssb.past7, ssb.past9, ssb.line9, ssb.line8, ssb.mfs_base, ssb.line7, ssb.zero, ssb.lived_apart; the mutant reads ssb.show10_15.) (structural conditions re-checked this run.)
- `operand.ssb.ssb.line16.line16_together.then0` (replace an operand, ssb.ssb.line16): ssb.line16's mfs_together-true alternative is line16_together, line 7 times 85%; the mutant reads line 15, line 11 times 85%, line 11 being line 9 less line 10 and line 9 line 7 less line 8, each floored at zero. mfs_together is all[status mfs, lived_apart false]; then line 8 and line 10 take mfs_base and mfs_adjust with lived_apart false, ssb.zero, so line 11 is line 7 and the two values agree. Lines 8 and 10 choose on the status, and mfs_base and mfs_adjust on lived_apart, among parameters only, so they are never refusals; line 15 is therefore a refusal exactly when line 7 is, with line 7's refusal, as line16_together is. Where mfs_together is unknown both alternatives are ways (spec 4.7.3): the first way refuses on both routes alike, and the other, line16_sum, is the same line, so line 16 is the same on both. (Premises pinned: ssb.line16, ssb.line16_together, ssb.line15, ssb.line11, ssb.line9, ssb.line10, ssb.line8, ssb.mfs_base, ssb.mfs_adjust, ssb.line7, ssb.mfs_together, ssb.lived_apart, ssb.zero; the mutant reads ssb.line15.) (structural conditions re-checked this run.)
- `operand.ssb.ssb.line18.zero.then1` (replace an operand, ssb.ssb.line18): Branch settled by its guard: where ssb.line18 takes alternative 1 (guard {
  "eq": [
    "ssb.has_benefits",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that ssb.zero and ssb.line17 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither ssb.zero nor ssb.line17 ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.u1250.u1250.line13.line9` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line9 and u1250.line8 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line10` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line10 and u1250.line8 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line12` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line12 and u1250.line8 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.w2.w2.g_gov_part.zero.then1` (replace an operand, w2.w2.g_gov_part): Copy-chain identity: w2.zero and w2.dc_zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.w2.w2.g_counted.zero.then1` (replace an operand, w2.w2.g_counted): Copy-chain identity: w2.zero and w2.dc_zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `boundary.se.positive` (replace strict greater-than with inclusive, se.positive): The test 'line 3 more than zero' made inclusive adds only line 3 = $0, where line 4a's two branches agree: line 3 itself, and 92.35% of line 3 floored at zero, both $0. The test is read only by line 4a. (structural conditions re-checked this run.)
- `param.eic.earned_amount0.$1` (shift a money parameter (+$1), eic.earned_amount0): Unread parameter: no line of any form or definition reads eic.earned_amount0; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.earned_amount1.$1` (shift a money parameter (+$1), eic.earned_amount1): Unread parameter: no line of any form or definition reads eic.earned_amount1; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.earned_amount2.$1` (shift a money parameter (+$1), eic.earned_amount2): Unread parameter: no line of any form or definition reads eic.earned_amount2; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.earned_amount3.$1` (shift a money parameter (+$1), eic.earned_amount3): Unread parameter: no line of any form or definition reads eic.earned_amount3; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum0.$1` (shift a money parameter (+$1), eic.maximum0): Unread parameter: no line of any form or definition reads eic.maximum0; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum1.$1` (shift a money parameter (+$1), eic.maximum1): Unread parameter: no line of any form or definition reads eic.maximum1; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum2.$1` (shift a money parameter (+$1), eic.maximum2): Unread parameter: no line of any form or definition reads eic.maximum2; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum3.$1` (shift a money parameter (+$1), eic.maximum3): Unread parameter: no line of any form or definition reads eic.maximum3; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.ws_threshold0.joint.$1` (shift a money parameter (+$1), eic.ws_threshold0.joint): Line 5 amount eic.ws_threshold0.joint: in eic_0 the bands covering [eic.ws_threshold0.joint, eic.ws_threshold0.joint + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way (only whether line 5 is shown can differ). (structural conditions re-checked this run.)
- `param.eic.ws_threshold0.other.$1` (shift a money parameter (+$1), eic.ws_threshold0.other): Line 5 amount eic.ws_threshold0.other: in eic_0 the bands covering [eic.ws_threshold0.other, eic.ws_threshold0.other + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way (only whether line 5 is shown can differ). (structural conditions re-checked this run.)
- `param.eic.ws_threshold1.joint.$1` (shift a money parameter (+$1), eic.ws_threshold1.joint): Line 5 amount eic.ws_threshold1.joint: in eic_1, eic_2, eic_3 the bands covering [eic.ws_threshold1.joint, eic.ws_threshold1.joint + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way (only whether line 5 is shown can differ). (structural conditions re-checked this run.)
