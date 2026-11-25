# Mutation score — implemented worksheets

Single-atom mutations applied to the canonical data; a mutant is killed if the
build-time checker fails on it or if any fixture case's value changes. Fixture
expectations are the recorded values checked in the previous run (the same values
the fixture test compares).

| Metric | Value |
| --- | --- |
| Mutants | 10536 |
| Killed by the checker | 3952 |
| Killed by fixtures | 6116 (77 only by class M cases) |
| Surviving | 468 (450 provably equivalent on every input; 10 equivalent on answered inputs only) |
| Surviving on unobserved lines (among the provably equivalent) | 0 |
| Mutation score (raw) | 95.6% |
| Mutation score (mutants provably equivalent on every input excluded) | 99.8% |
| Mutation score (also excluding those equivalent on answered inputs only) | 99.9% |

## Killed only by class M cases

A class M rerun regenerates its cases, so these kills can be lost. Before replacing a case named here,
keep it (or a stage fixture with the same facts and source-predicted values) among the stage fixtures.

| Mutant | Kind | Location | First class M case killing it |
| --- | --- | --- | --- |
| operand.dependent.dependent.lived_half.lived_all_year.then0 | replace an operand | dependent.dependent.lived_half | classm.f5695.8.deepseek |
| operand.dependent.dependent.qr_relationship.qr_listed_relative.then1 | replace an operand | dependent.dependent.qr_relationship | classm.s8812.4.deepseek |
| operand.dependent.dependent.dc_child_all_year.qc_dependent.all.0.eq.0 | replace an operand | dependent.dependent.dc_child_all_year | classm.f2441.2.deepseek |
| boundary.dependent.dependent.edu_has_adj | replace strict greater-than with inclusive | dependent.dependent.edu_has_adj | classm.f8863.2.deepseek |
| operand.eic.eic.check_27c.has_qc.any.2.all.1.eq.0 | replace an operand | eic.eic.check_27c | classm.f1040.1.deepseek |
| operand.f1095a.f1095a.b_jan.mo_b.then0 | replace an operand | f1095a.f1095a.b_jan | classm.f1095a.1.deepseek |
| operand.f2441.f2441.mfs_married.line_a.all.1.eq.0 | replace an operand | f2441.f2441.mfs_married | classm.f2441.11 |
| operand.f5695.f5695.sec_a_claimed.no.then1 | replace an operand | f5695.f5695.sec_a_claimed | classm.f5695.2.deepseek |
| filter.f8582.f8582.prior_count | remove collection filter | f8582.f8582.prior_count | classm.f8582.4.deepseek |
| boundary.f8582.f8582.has_prior | replace strict greater-than with inclusive | f8582.f8582.has_prior | classm.f8582.4.deepseek |
| boundary.f8853c.f8853c.has_periodic | replace strict greater-than with inclusive | f8853c.f8853c.has_periodic | classm.f8853c.2 |
| operand.f8853c.f8853c.line21.zero.then1 | replace an operand | f8853c.f8853c.line21 | classm.f8853c.2 |
| operand.f8853c.f8853c.line23.line21 | replace an operand | f8853c.f8853c.line23 | classm.f8853c.2 |
| boundary.f8853c.f8853c.has_line24 | replace strict greater-than with inclusive | f8853c.f8853c.has_line24 | classm.s1.12.deepseek |
| operand.f8853c.f8853c.has_line24.line24_if_periodic.gt.0 | replace an operand | f8853c.f8853c.has_line24 | classm.s1.12.deepseek |
| filter.f8880.f8880.line2a | remove collection filter | f8880.f8880.line2a | classm.f8880.2.deepseek |
| operand.f8880.f8880.line3a_counted.line3a.then0 | replace an operand | f8880.f8880.line3a_counted | classm.f1040.6.deepseek |
| operand.f8880.f8880.line3b_counted.line3b.then0 | replace an operand | f8880.f8880.line3b_counted | classm.f8880.3.deepseek |
| operand.f8880.f8880.contrib_counted.line3a_counted | replace an operand | f8880.f8880.contrib_counted | classm.f1040.6.deepseek |
| operand.f8880.f8880.contrib_counted.line3b_counted | replace an operand | f8880.f8880.contrib_counted | classm.f1040.6.deepseek |
| boundary.f8880.f8880.has_contrib | replace strict greater-than with inclusive | f8880.f8880.has_contrib | classm.f1040.6.deepseek |
| operand.f8880.f8880.can_take_contrib.no.then1 | replace an operand | f8880.f8880.can_take_contrib | classm.f1040.6.deepseek |
| operand.f8889.f8889.fsf_possible.no.then0 | replace an operand | f8889.f8889.fsf_possible | classm.f8889.11 |
| operand.f8889.f8889.ask_former_spouse_family.fsf_eligible.then0 | replace an operand | f8889.f8889.ask_former_spouse_family | classm.f8889.7 |
| operand.f8889.f8889.covered_12.yes.then0 | replace an operand | f8889.f8889.covered_12 | classm.f8889.3.deepseek |
| operand.f8889.f8889.covered_12.yes.then1 | replace an operand | f8889.f8889.covered_12 | classm.f8889.2 |
| boundary.f8960.f8960.allocation_over_5e | replace strict greater-than with inclusive | f8960.f8960.allocation_over_5e | classm.f8960.1.deepseek |
| operand.f8962.f8962.show_applicable.applicable.all.1.eq.0 | replace an operand | f8962.f8962.show_applicable | classm.s2.5.deepseek |
| boundary.household.household.dependents_any | replace strict greater-than with inclusive | household.household.dependents_any | classm.s2.1.deepseek |
| operand.household.household.cp_marriage_ended.cp_not_joint.then3 | replace an operand | household.household.cp_marriage_ended | classm.f2441.4.deepseek |
| operand.household.household.cp_marriage_ended.cp_not_joint.then4 | replace an operand | household.household.cp_marriage_ended | classm.f8960.2.deepseek |
| operand.ira.ira.roth_reduced.roth_start_joint.any.0.all.1.ge.1 | replace an operand | ira.ira.roth_reduced | classm.f1040.7.deepseek |
| operand.k1p.k1p.under500.hours500_if_work.all.1.eq.0 | replace an operand | k1p.k1p.under500 | classm.k1p.2.deepseek |
| operand.k1p.k1p.p5_b2_income.zero.then0 | replace an operand | k1p.k1p.p5_b2_income | classm.k1p.1.deepseek |
| operand.k1s.k1s.other_ask.work_if_b1.all.0.eq.0 | replace an operand | k1s.k1s.other_ask | classm.k1s.2.deepseek |
| boundary.k1s.k1s.has_loss | replace strict greater-than with inclusive | k1s.k1s.has_loss | classm.k1s.2.deepseek |
| operand.k1s.k1s.b1_np.zero.then1 | replace an operand | k1s.k1s.b1_np | classm.k1s.5.deepseek |
| boundary.person.person.f8919_any | replace strict greater-than with inclusive | person.person.f8919_any | classm.s2.4.deepseek |
| boundary.person.person.edu_has_adj | replace strict greater-than with inclusive | person.person.edu_has_adj | classm.f8863.2.deepseek |
| operand.person.person.spouse_senior_work_ssn.no.then0 | replace an operand | person.person.spouse_senior_work_ssn | classm.tcw.1 |
| operand.rec.rec.line8.line7 | replace an operand | rec.rec.line8 | classm.rec.1 |
| operand.refund.refund.taxable_1040.zero.then0 | replace an operand | refund.refund.taxable_1040 | classm.f1040.3.deepseek |
| operand.refund.refund.taxable.taxable_1040.then1 | replace an operand | refund.refund.taxable | classm.f1040.3.deepseek |
| operand.rental.rental.personal_c.zero.then1 | replace an operand | rental.rental.personal_c | classm.f8582.1.deepseek |
| operand.rental.rental.line20.line18 | replace an operand | rental.rental.line20 | classm.f8582.1.deepseek |
| operand.rental.rental.line3.rents.then1 | replace an operand | rental.rental.line3 | classm.rental.1.deepseek |
| operand.rental.rental.p6_loss.overall_loss.then0 | replace an operand | rental.rental.p6_loss | classm.rental.3.deepseek |
| operand.rental.rental.p7_listed.p7a.gt.0 | replace an operand | rental.rental.p7_listed | classm.rental.1.deepseek |
| operand.retirement.retirement.ira_put_back.direct.all.1.eq.0 | replace an operand | retirement.retirement.ira_put_back | classm.tcw.4 |
| operand.retirement.retirement.l2.l2_exc.then1 | replace an operand | retirement.retirement.l2 | classm.s2.8.deepseek |
| operand.s1.s1.line20_box.no.then1 | replace an operand | s1.s1.line20_box | classm.s1.2.deepseek |
| boundary.s1.s1.has_jury_pay | replace strict greater-than with inclusive | s1.s1.has_jury_pay | classm.f8960.1.deepseek |
| boundary.s2.s2.amt_could | replace strict greater-than with inclusive | s2.s2.amt_could | classm.s2.3.deepseek |
| operand.s2.s2.amt_owed.amt_boat_if_could.any.0.eq.0 | replace an operand | s2.s2.amt_owed | classm.s2.1.deepseek |
| operand.s2.s2.amt_owed.amt_business_if_sc.any.1.eq.0 | replace an operand | s2.s2.amt_owed | classm.s2.1.deepseek |
| operand.s3.s3.business_credit_any.rental_credit_if_rentals.any.1.eq.0 | replace an operand | s3.s3.business_credit_any | classm.s3.1.deepseek |
| operand.s3.s3.line15.line9 | replace an operand | s3.s3.line15 | classm.s3.2.deepseek |
| boundary.sa.sa.e05_claimed | replace strict greater-than with inclusive | sa.sa.e05_claimed | classm.f8960.2.deepseek |
| operand.sa.sa.mortgage_interest_not_mfs.mfs.all.1.eq.0 | replace an operand | sa.sa.mortgage_interest_not_mfs | classm.sa.5.deepseek |
| operand.sa.sa.gift_property_limit.agi_floor | replace an operand | sa.sa.gift_property_limit | classm.s3.2.deepseek |
| operand.sales.sales.wash_bad.wash_loss.all.1.gt.0 | replace an operand | sales.sales.wash_bad | classm.g28.2.deepseek |
| operand.sc.sc.line20a.rent_equipment | replace an operand | sc.sc.line20a | classm.clcw_next_year.1.deepseek |
| operand.sc.sc.f7206_line7.zero.then1 | replace an operand | sc.sc.f7206_line7 | classm.sc.1 |
| operand.sc.sc.qbi_has.zero.gt.1 | replace an operand | sc.sc.qbi_has | classm.sc.2 |
| filter.sche.sche.line23c | remove collection filter | sche.sche.line23c | classm.sche.2.deepseek |
| filter.sche.sche.rent_exp | remove collection filter | sche.sche.rent_exp | classm.sche.2.deepseek |
| operand.sche.sche.line23e.rent_exp | replace an operand | sche.sche.line23e | classm.sche.1.deepseek |
| operand.scveh.scveh.line9.line9_actual.then1 | replace an operand | scveh.scveh.line9 | classm.clcw_next_year.1.deepseek |
| operand.scveh.scveh.line19_hy.rate_hy.rate | replace an operand | scveh.scveh.line19_hy | classm.s8812.1.deepseek |
| operand.scveh.scveh.line19_this_year.line19_hy.then0 | replace an operand | scveh.scveh.line19_this_year | classm.s8812.1.deepseek |
| operand.sdtw.sdtw.line5.line3 | replace an operand | sdtw.sdtw.line5 | classm.f1040.2.deepseek |
| minmax.sdtw.sdtw.line7 | swap smaller_of/larger_of | sdtw.sdtw.line7 | classm.f1040.2.deepseek |
| operand.ssb.ssb.line8.base_single.then4 | replace an operand | ssb.ssb.line8 | classm.ssb.6 |
| operand.ssb.ssb.line10.adjust_single.then3 | replace an operand | ssb.ssb.line10 | classm.tcw.13 |
| operand.ssb.ssb.line10.adjust_single.then4 | replace an operand | ssb.ssb.line10 | classm.ssb.6 |
| boundary.w2.w2.has_box10 | replace strict greater-than with inclusive | w2.w2.has_box10 | classm.f2441.2.deepseek |
| boundary.w2.w2.box10_bad | replace strict greater-than with inclusive | w2.w2.box10_bad | classm.w2.1.deepseek |

## Surviving — equivalent on answered inputs only

Each argument below is proven only on returns where the answers it names are given; with them withheld a
partial return can tell the mutant apart (spec 4.7.3). They are not counted as provably equivalent on every input.

- `operand.dependent.dependent.dc_line2c.dc_incapable.all.1.eq.0` (replace an operand, dependent.dependent.dc_line2c): dc_line2c is all[dc_qp, dc_incapable, age test]; the mutant reads dc_disabled_qp, all[dc_incapable, dc_lived_half], in place of dc_incapable. The second conjunct is reached only when dc_qp is true or unknown (a refusal ends both tests). dc_qp true means its any-test found dc_child_all_year, dc_disabled_qp or dc_child true. dc_child_all_year and dc_child (through dc_age13) each need qc_dependent true, a choice on qualifying_child whose false alternative is dependent.no (the parameter household.no, false), so it needs qualifying_child true: qc_tests true, a chain of choices (qc_relationship, then qc_age, then self_support_if_own_money false, then joint_return_if_ever_married false) whose every other alternative is dependent.no and whose last is lived_half; lived_half is then a memoized true in the dependent's frame (spec 4.7.6), and dc_lived_half, an any-test whose first disjunct is lived_half true, is true. dc_disabled_qp true needs dc_lived_half true. So wherever dc_qp is true, dc_lived_half is true and dc_disabled_qp is dc_incapable's value (an input with no gates): the conjuncts agree. dc_qp is unknown only with an input it reads unanswered; there the mutant can be false or a refusal (through dc_lived_half) where the base is unknown, so the argument is over answered inputs: dc_qp is read by f2441.qp_count and f2441.paid_total for every dependent, and its inputs are asked on any return that reaches Form 2441. (Premises pinned: dependent.dc_line2c, dependent.dc_incapable, dependent.dc_disabled_qp, dependent.dc_qp, dependent.dc_lived_half, dependent.dc_child_all_year, dependent.dc_child, dependent.dc_age13, dependent.qc_dependent, dependent.qualifying_child, dependent.qc_tests, dependent.qc_from_age, dependent.qc_from_support, dependent.qc_from_joint, dependent.no, param:household.no, dependent.lived_half; the mutant reads dependent.dc_disabled_qp.) (structural conditions re-checked this run.)
- `operand.eic.eic.step5_income.earned_for_limit.lt.0` (replace an operand, eic.eic.step5_income): step5_income compares earned_for_limit with eic.limit; the mutant compares wsb_4b, sum[earned_income, wsb_se]. earned_for_limit chooses on self_employed (sc_count > 0): earned_income when false, wsb_4b when true. With self_employed true the two are the same value. With it false sc_count is a complete 0 (a lower bound decides gt only true, spec 4.7.5), so each person's sc_count is a complete 0, has_sc is false and eic_se is person.zero ($0); wsb_se sums eic_se over the same roster with no where-test, so it is $0, and wsb_4b is earned_income's value (a sum returns its first operand's refusal at once, and an unknown plus $0 stays unknown). self_employed is never a refusal (its counts sum parameters over rosters, with no gates); it is unknown only with a $person or $sc roster unconfirmed, where the base is unknown and the mutant can be decided (earned_income's refusal), so the argument is over answered inputs: those rosters are asked on every return. (Premises pinned: eic.step5_income, eic.earned_for_limit, eic.wsb_4b, eic.wsb_se, eic.earned_income, eic.self_employed, eic.sc_count, person.sc_count, person.has_sc, person.eic_se, person.zero, param:ss.zero; the mutant reads eic.wsb_4b.) (structural conditions re-checked this run.)
- `operand.eic.eic.check_27c.has_qc.any.3.all.1.eq.0` (replace an operand, eic.eic.check_27c): eic.check_27c is an any-test of six all-tests, taken in order (a refusal ends it, a true ends it); the mutant's fourth disjunct (D3: reached_step3, has_qc = false, married_rules = false, age_range, us_home = true, status not mfj, qc_of_another_if_lived = true) tests eic.show5 = false in place of eic.has_qc = false. show5 is all[eligible = true, line4 = false, line5_blank = false, line2 > 0]. With the answers given: (a) has_qc true: the base D3 is false; if show5 is false and the other conjuncts of D3 hold, the second disjunct (D1: reached_step3, has_qc, step3_married, status not mfj, qc_of_another_if_lived) holds too, since married_rules false makes step3_married true, and D1 is taken first, so check_27c is true on both routes. (b) has_qc false: show5 true needs eligible true, which (eligible a choice on reached_step5, reached_step5 on reached_step3 then step34, step34 on has_qc false taking step4) needs married_rules false, age_range, us_home true and step4_dependent, that is status mfj or qc_of_another_if_lived false; either makes D3's last two conjuncts fail, so D3 is false on both routes; show5 false gives the base's conjunct. (c) Where show5 refuses: eligible's refusal is met again by D4 (worksheet_a_stop, a choice on eligible) in the base, as the same memoized value (spec 4.7.6); with eligible true, line4 and line5_blank read line3 (Form 1040 line 11b, read first by D0's below_top, whose refusal ends both tests at D0) and line1, and line1 and line2 are read again by D4 through line2_zero (line2 on line1_in_table on line1), so the base refuses with the same refusal; and D3 true in the base means qc_of_another_if_lived true, step4_dependent false and eligible false, so show5 is false, not a refusal. Where eligible or has_qc is unknown (an answer withheld) the two routes can leave different pending values or refusals, so the argument is over answered inputs. (Premises pinned: eic.check_27c, eic.has_qc, eic.show5, eic.eligible, eic.reached_step5, eic.reached_step3, eic.step34, eic.step4, eic.step4_age, eic.step4_home, eic.step4_dependent, eic.married_rules, eic.step3_married, eic.qc_of_another_if_lived, eic.age_range, eic.us_home, eic.worksheet_a_stop, eic.line2_zero, eic.line2, eic.line4, eic.line5_blank, eic.line3, eic.line1, eic.below_top, eic.no, param:household.no; the mutant reads eic.show5.) (structural conditions re-checked this run.)
- `operand.f8880.f8880.line3a_counted.zero.then1` (replace an operand, f8880.f8880.line3a_counted): line3a_counted's elig_a-false alternative is f8880.zero ($0); the mutant reads line11, a copy of clw3. line3a_counted is read only by contrib_counted, which only has_contrib reads, which only can_take_contrib reads (has_contrib true takes past7, false takes no, the false parameter savers.no_credit), which only can_take_tax reads where clw_room (clw3 more than $0) is true, or as a way where it is unknown (spec 4.7.3). With clw_room unknown can_take_tax's other way, no, never refuses, so can_take_tax is clw_room's unknown on both routes. With clw_room true clw3 is complete and positive, so with elig_a false the mutant's contrib_counted is that amount plus line3b_counted: both routes are line3b_counted's refusal or unknown alike, and otherwise has_contrib is true on the mutant's route. Where the base's has_contrib is true too both take past7; where it is false line3b_counted is $0, the base takes no (false) and the mutant past7, line7 more than $0. line7 is line6a plus line6b; line6a is $0 (elig_a false); line6b is $0 when elig_b is false, and otherwise line3b is $0 and line6b is the smaller of the cap and line5b, line3b less line4b floored at zero, which is $0 when line4b is complete. So past7 is false wherever line4b is answered. With elig_a unknown the mutant's ways line3a and line11 cannot both refuse under clw_room true (line11 is complete). Where line4b's distribution answers are withheld, line5b and so past7 are unknown and the mutant can be unknown where the base is false, so the argument is over answered inputs. (Premises pinned: f8880.line3a_counted, f8880.line3a, f8880.line11, f8880.clw3, f8880.clw_room, f8880.contrib_counted, f8880.line3b_counted, f8880.has_contrib, f8880.can_take_contrib, f8880.can_take_tax, f8880.past7, f8880.no, f8880.line7, f8880.line6a, f8880.line6b, f8880.line6b_figured, f8880.line5b, f8880.line3b, f8880.line4b, f8880.elig_a, f8880.elig_b, f8880.cap, f8880.zero, param:savers.no_credit, param:sales.zero; the mutant reads f8880.line11.) (structural conditions re-checked this run.)
- `operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0` (replace an operand, ira.ira.mfs_cov_matters_trad): ira.mfs_cov_matters_trad is all[household.mfs = true, ira.cov_you = 0, household.mfs_apart_all_year = false]; the mutant tests ira.cov_count in place of ira.cov_you. Both sum person.one over the person entries whose person.ira_cov is true; cov_you counts only those whose person.role is taxpayer (enum person_role: taxpayer or spouse). So they differ only on an entry whose role is spouse, or unknown. The second conjunct is reached only where household.mfs is true or unknown (a known false first conjunct ends both tests). A return that is not joint has one person entry, the taxpayer's, and its role is recorded with the roster answer. Every entry is then the taxpayer's and the two counts are equal. A roster that lists a spouse on such a return fails household.roster_ok and is refused at line 1a (household.roster_bad); it is not an answer the interview gives. Where a role is withheld, cov_you is unknown and cov_count is known, so the mutant can be a known false where the base is unknown (mfs.ira.apart_covered with answers withheld). The argument is over answered inputs. (Premises pinned: ira.mfs_cov_matters_trad, ira.cov_you, ira.cov_count, household.mfs, household.mfs_apart_all_year, ira.mfs_cov_matters, person.role, person.ira_cov, enum:person_role, household.roster_ok, household.roster_bad; the mutant reads ira.cov_count.) (structural conditions re-checked this run.)
- `operand.person.person.f4137_line6.zero.then1` (replace an operand, person.person.f4137_line6): person.f4137_line6 is a choice on person.f4137_filed (person.f4137_col_c more than $0): true takes person.f4137_line6_figured, false takes person.zero (the parameter ss.zero, $0); the mutant takes person.f4137_line4, the sum of f4137.line4 over the person's Form 4137 roster, in the false alternative. f4137.line4 is subtract_floor0 from line 2 (a copy of person.f4137_col_c) take line 3 (a copy of person.f4137_col_d). f4137_filed is a known false only where col_c is a known $0 (it is NonNegDollars). col_c and col_d are choices on the same scope.tips_unreported_if_pay: false gives person.zero to both; true gives the sums over the f4137row roster of the inputs f4137row.col_c and f4137row.col_d, which have no refusal gate. Where col_d is known, every entry's line 4 is max(0, $0 - col_d) = $0, and the sum over any roster is $0, the data's value, so the only reader, f8959.line2 (the sum of person.f4137_line6 over persons), is the same. Where a row's col_d answer is withheld, the mutant's line 4 is unknown where the data's alternative is $0; and where f4137_filed is unknown both alternatives are ways (spec 4.7.3), and the mutant's way can be unknown or another amount where the data's is $0. So the argument is over answered inputs. (Premises pinned: person.f4137_line6, person.f4137_filed, person.f4137_col_c, person.f4137_col_d, person.f4137_rows_c, person.f4137_rows_d, f4137row.col_c, f4137row.col_d, person.f4137_line4, f4137.line2, f4137.line3, f4137.line4, person.zero, param:ss.zero, param:sales.zero, f8959.line2; the mutant reads person.f4137_line4.) (structural conditions re-checked this run.)
- `operand.rec.rec.to_line1.zero.then1` (replace an operand, rec.rec.to_line1): rec.to_line1 is a choice on rec.path: true takes rec.line_b, false takes rec.zero (the parameter sales.zero, $0); the mutant takes rec.line_c in place of rec.zero. to_line1's only reader is refund.taxable, a choice on the same rec.path that takes to_line1 only when rec.path is true, and to_line1 then meets the same known true (memoized in the frame, spec 4.7.6) and takes line_b on both routes; where rec.path is a known false, refund.taxable takes refund.taxable_1040 and does not read to_line1. Where rec.path is unknown (scope.recovery or refund.itemized not answered), both alternatives of refund.taxable and of to_line1 are ways (spec 4.7.3), and the mutant's line_c way can refuse (through rec.line11) where rec.zero cannot, so a return with those answers withheld can tell the routes apart; the argument is over answered inputs. (Premises pinned: rec.to_line1, rec.path, refund.taxable, rec.line_b, rec.line_c, rec.zero, param:sales.zero, refund.taxable_1040; the mutant reads rec.line_c.) (structural conditions re-checked this run.)
- `operand.rental.rental.home.home_pers10_if_any.all.1.gt.0` (replace an operand, rental.rental.home): rental.home is all[rental.personal_c more than the parameter rental.home_days, rental.home_pers10_if_any more than rental.home_rent_c]; the mutant compares rental.home_pers10 (ten times days_personal, as cents) in place of home_pers10_if_any. personal_c and home_pers10_if_any are both choices on rental.personal_any: true takes personal_raw and home_pers10, false takes rental.zero (the parameter sales.zero, $0); none of these lines has a refusal gate. Where personal_any is a known true, home_pers10_if_any is home_pers10's value, so the second tests agree. Where it is a known false, personal_c is $0, not more than 14, so the first conjunct is a known false and both all-tests end false before the second. Where personal_any is unknown, personal_c and home_pers10_if_any have both alternatives as ways (spec 4.7.3), while home_pers10 reads days_personal directly, so a return that answers days_personal but not personal_any can tell the routes apart; the interview asks days_personal only after personal_any is yes, so the argument is over answered inputs. (Premises pinned: rental.home, rental.home_pers10_if_any, rental.home_pers10, rental.personal_any, rental.personal_c, rental.personal_raw, rental.zero, param:sales.zero, param:rental.home_days; the mutant reads rental.home_pers10.) (structural conditions re-checked this run.)
- `operand.s8812.s8812.line18a.chart_eic.then0` (replace an operand, s8812.s8812.line18a): line18a's taking_eic-true alternative is chart_eic; the mutant reads eiw_7_figured (eiw_3 less eiw_6). It is taken only when Form 1040 line 27a, a copy of eic.credit, is above $0, so eligible is true and line6 is above $0; line6 is line2 or the smaller of line5 and line2, so line2 is above $0, line1_in_table is true and line1 is at least table_start (positive, checked). eligible true makes step1_income and step5_income complete. Line 11b (line 9 less line 10) is complete; line 9 sums line 8, a copy of Schedule 1 line 10, which sums s1.line10_ex5 (a sum that includes Schedule 1 line 3) and Schedule 1 line 5, and line 10 copies Schedule 1 line 26, which sums Schedule 1 line 15, so both are complete. earned_for_limit is complete, so earned_income (Step 5 line 1, line 1z behind scope.schedule1; less line 2, M, the sum of person.mw_not_earned over the person roster; plus line 4, $0 behind s8812.combat_pay) is complete, so M is a complete amount, at least $0, and those gates are false. Then eiw_1a is line 1z, eiw_1b $0 (the same combat-pay gate), eiw_2b Schedule 1 line 3, eiw_3 eiw_3sum floored at zero, eiw_4 M (the same sum over the same field, behind scope.schedule1) and eiw_5 Schedule 1 line 15: eiw_7_figured is max(line 1z + S1 line 3, 0) less (M + S1 line 15). S1 line 3 sums each person's sc_total and line 15 each person's se_line13. With self_employed false every Schedule C roster is empty, line 3 is $0 and each se_line13 is person.zero; chart_eic is earned_income, line 1z less M, and so is eiw_7_figured (line 1z is NonNegDollars, so the floor does not apply). With it true chart_eic is wsb_4b, line 1z plus the sum of each person's eic_se: person.zero for a person with no Schedule C (whose sc_total and se_line13 are $0), sc_total less se_line13 when files_se, and sc_total otherwise, where files_se false means Schedule SE line 4c is $0, so lines 6, the social security base, 10, 11, 12 and 13 of that person's Schedule SE are $0. So wsb_4b is line 1z + S1 line 3 less (M + S1 line 15); line1 (wsb_6, wsb_4b floored) is above $0, so line 1z + S1 line 3 is above M + S1 line 15, itself at least $0, no floor applies, and eiw_7_figured equals chart_eic. Where taking_eic is false or refused the alternative is not evaluated; where it is unknown the alternative is a way (spec 4.7.3) and chart_eic and eiw_7_figured can differ in whether they refuse, so the argument is over answered inputs. A Schedule C roster is empty when self_employed is false because self_employed tests sc_count > 0 and sc_count sums sc.one, a positive parameter (pinned). (Premises pinned: s8812.line18a, s8812.chart_eic, s8812.eiw_7_figured, s8812.taking_eic, f1040.line27a, eic.credit, eic.zero, eic.line6, eic.after_line4, eic.smaller, eic.line2, eic.line1_in_table, eic.line1, eic.wsb_6, eic.eligible, eic.step1_income, eic.step5_income, eic.earned_for_limit, eic.earned_income, eic.step5_line1, eic.step5_line2, eic.step5_line3, eic.step5_line4, eic.wsb_4b, eic.wsb_se, eic.self_employed, eic.sc_count, s8812.eiw_3, s8812.eiw_3sum, s8812.eiw_1a, s8812.eiw_1b, s8812.eiw_2b, s8812.eiw_6, s8812.eiw_4, s8812.eiw_5, s8812.zero, f1040.line11b, f1040.line11a, f1040.line9, f1040.line8, f1040.line10, s1.line10, s1.line10_ex5, s1.line26, s1.line3, s1.line15, person.sc_total, person.se_line13, person.se_line4c, person.files_se, person.eic_se, person.eic_se_has, person.eic_part1, person.has_sc, person.sc_count, person.zero, def:se, param:sales.zero, param:ss.zero, sc.one, param:sc.one; the mutant reads s8812.eiw_7_figured.) (structural conditions re-checked this run.)
- `operand.sdtw.sdtw.line4.zero.then1` (replace an operand, sdtw.sdtw.line4): sdtw.line4's filing4952-false alternative is sdtw.zero ($0); the mutant reads sdtw.line3, a copy of f4952.election through sd.investment_election. filing4952 is f4952.required, a choice on used: true takes required_test, false takes f4952.no (the parameter f4952.no, false); it is known false only when used is false (so has_election, a disjunct of used, is false and election is f4952.zero) or used is true and required_test is false (an any-test whose first disjunct is election > 0, so election was evaluated complete and not above $0). Either way line3 is $0 wherever the alternative is taken; a refused guard ends the choose before either alternative. Where filing4952 is unknown both alternatives are ways (spec 4.7.3), and line3 can make the mutant a refusal on both where the base's $0 leaves it unknown, so the argument is over answered inputs. (Premises pinned: sdtw.line4, sdtw.line3, sdtw.zero, sd.filing4952, sd.investment_election, f4952.required, f4952.used, f4952.required_test, f4952.election, f4952.has_election, f4952.zero, f4952.no, param:f4952.no, param:sales.zero; the mutant reads sdtw.line3.) (structural conditions re-checked this run.)

## Surviving — classified equivalent

- `operand.asset.asset.bonus_forty.after179` (replace an operand, asset.asset.bonus_forty): Copy-chain identity: asset.after179 and asset.bonus_full expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.asset.asset.macrs_hy.ub` (replace an operand, asset.asset.macrs_hy): Copy-chain identity: asset.ub and asset.col19c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.asset.asset.bonus_this_year.zero.then1` (replace an operand, asset.asset.bonus_this_year): Branch settled by its guard: where asset.bonus_this_year takes alternative 1 (guard {
  "eq": [
    "asset.placed_this_year",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.dep_this_year make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.s179_this_year.zero.then1` (replace an operand, asset.asset.s179_this_year): Branch settled by its guard: where asset.s179_this_year takes alternative 1 (guard {
  "eq": [
    "asset.placed_this_year",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.bonus_this_year make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.mq_q4.zero.then1` (replace an operand, asset.asset.mq_q4): Branch settled by its guard: where asset.mq_q4 takes alternative 1 (guard {
  "eq": [
    "asset.placed_this_year",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.s179_this_year make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither asset.zero nor asset.s179_this_year ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.mq_total.zero.then1` (replace an operand, asset.asset.mq_total): Branch settled by its guard: where asset.mq_total takes alternative 1 (guard {
  "eq": [
    "asset.placed_this_year",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.mq_q4 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.cost179.zero.then1` (replace an operand, asset.asset.cost179): Branch settled by its guard: where asset.cost179 takes alternative 1 (guard {
  "eq": [
    "asset.placed_this_year",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that asset.zero and asset.mq_total make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.asset.asset.s179_bad_test2.s179_bad_test2_test1.then0` (replace an operand, asset.asset.s179_bad_test2): Branch equal under a case split: where asset.s179_bad_test2 takes alternative 0 (guard {
  "eq": [
    "asset.s179_bad_test2_test1",
    {
      "const": true
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "asset.s179_bad_test1",
    {
      "const": true
    }
  ],
  "op": "test"
}
 on its one reader path), asset.s179_bad_test2_test1 and asset.s179_bad_test1 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.asset.asset.s179_bad_test2_test2.over_half.eq.0` (replace an operand, asset.asset.s179_bad_test2_test2): asset.s179_bad_test2_test2 is the test 'over_half eq false'; the mutant tests 's179_bad_test2_test1 eq false' (section 179 not more than the basis). Its only reader is asset.s179_bad_test2_from2, in the alternative whose guard is 'over_half eq false'; from2's only reader is asset.s179_bad_test2, in the alternative whose guard is 's179_bad_test2_test1 eq false', and s179_bad_test2's other alternative is test1 itself. Where both guards hold (taken in the frame, spec 4.7.6), test1 is a known false and over_half a known false, so both tests are true. Where test1 is a refusal, s179_bad_test2 is that refusal on both routes; where it is unknown, its alternative test1 is a way that is unknown, not a refusal, so s179_bad_test2 is test1's unknown on both routes whatever from2 is (spec 4.7.3). So s179_bad_test2, and every line reading it, has the same value on both routes; only the helpers from2 and test2_test2, evaluated as targets of their own, can differ. (Premises pinned: asset.s179_bad_test2_test2, asset.s179_bad_test2_from2, asset.s179_bad_test2, asset.s179_bad_test2_test1, asset.over_half, asset.not179; the mutant reads asset.s179_bad_test2_test1.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.qc_age_younger.younger.then0` (replace an operand, dependent.dependent.qc_age_younger): qc_age_younger is a choice on the input younger: true takes younger (true), false takes disabled; the mutant reads under_24 (age below the parameter qc.student_age_limit, 24) in place of younger in the true alternative. qc_age_younger is read by qc_age, in its under_19-true alternative, and by qc_age_student, in its student-true alternative; qc_age_student is read only by qc_age_19, in its under_24-true alternative. Through qc_age, under_19 (age below the parameter qc.age_limit, 19) is a known true, so age is known and below 19 and under_24 is true. Through qc_age_student, under_24 is a memoized true (spec 4.7.6). Either way the mutant's alternative is true, the base's value. Where under_19, student or under_24 is unknown the alternative is a way (spec 4.7.3), and every way of those choices (younger, disabled, under_24, qc_age_19, qc_age_student) reads only inputs and parameters with no refusal gates, so none refuses and each line is its guard's unknown on both routes. The two age parameters are pinned (19 and 24). (Premises pinned: dependent.qc_age_younger, dependent.younger, dependent.disabled, dependent.under_24, dependent.qc_age, dependent.under_19, dependent.qc_age_student, dependent.student, dependent.qc_age_19, dependent.age, param:qc.age_limit, param:qc.student_age_limit; the mutant reads dependent.under_24.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.qr_other_relation.qr_other_lawful.then0` (replace an operand, dependent.dependent.qr_other_relation): Branch equal under a case split: where dependent.qr_other_relation takes alternative 0 (guard {
  "eq": [
    "dependent.qr_other_lawful",
    {
      "const": true
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "all": [
    {
      "ne": [
        "dependent.relationship",
        {
          "const": "child"
        }
      ],
      "op": "test"
    },
    {
      "ne": [
        "dependent.relationship",
        {
          "const": "sibling"
        }
      ],
      "op": "test"
    },
    {
      "ne": [
        "dependent.relationship",
        {
          "const": "parent"
        }
      ],
      "op": "test"
    },
    {
      "ne": [
        "dependent.relationship",
        {
          "const": "parent_relative"
        }
      ],
      "op": "test"
    },
    {
      "ne": [
        "dependent.relationship",
        {
          "const": "in_law"
        }
      ],
      "op": "test"
    },
    {
      "ne": [
        "dependent.relationship",
        {
          "const": "household_member"
        }
      ],
      "op": "test"
    }
  ],
  "op": "test"
}
 on its one reader path), dependent.qr_other_lawful and dependent.qr_household_member have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.dependent.dependent.spouse_relative_joint.no.then0` (replace an operand, dependent.dependent.spouse_relative_joint): spouse_relative_joint is a choice on the filing status: mfj takes spouse_relative, every other status takes dependent.no (the parameter household.no, false); the mutant reads qr_other_lawful in place of dependent.no for single. spouse_relative_joint is read by two lines only. qr_other_relation reads it only as the way of the guard 'qr_other_lawful is false', so wherever that alternative is taken qr_other_lawful is a memoized false in the same frame (spec 4.7.6), the value of dependent.no. qr_household_member reads it only as the way of the guard 'household_all_year is false'; qr_other_lawful is a choice on household_all_year whose false alternative is dependent.no, so there too it is false. Where the reader's guard is unknown both alternatives are ways (spec 4.7.3): qr_other_lawful is then that unknown or false (its ways are the input lawful and dependent.no, neither with a refusal gate), never a refusal, as dependent.no never is, so the reader is the guard's unknown on both routes; a refused guard ends the choose with its refusal on both routes. Where the status is unknown the mutant's way is again qr_other_lawful's false or unknown in each reading frame, never a refusal, and the mfj way spouse_relative is the same on both routes. (Premises pinned: dependent.spouse_relative_joint, dependent.qr_other_relation, dependent.qr_household_member, dependent.qr_other_lawful, dependent.household_all_year, dependent.lawful, dependent.no, param:household.no; the mutant reads dependent.qr_other_lawful.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.spouse_relative_joint.no.then2` (replace an operand, dependent.dependent.spouse_relative_joint): spouse_relative_joint is a choice on the filing status: mfj takes spouse_relative, every other status takes dependent.no (the parameter household.no, false); the mutant reads qr_other_lawful in place of dependent.no for mfs. spouse_relative_joint is read by two lines only. qr_other_relation reads it only as the way of the guard 'qr_other_lawful is false', so wherever that alternative is taken qr_other_lawful is a memoized false in the same frame (spec 4.7.6), the value of dependent.no. qr_household_member reads it only as the way of the guard 'household_all_year is false'; qr_other_lawful is a choice on household_all_year whose false alternative is dependent.no, so there too it is false. Where the reader's guard is unknown both alternatives are ways (spec 4.7.3): qr_other_lawful is then that unknown or false (its ways are the input lawful and dependent.no, neither with a refusal gate), never a refusal, as dependent.no never is, so the reader is the guard's unknown on both routes; a refused guard ends the choose with its refusal on both routes. Where the status is unknown the mutant's way is again qr_other_lawful's false or unknown in each reading frame, never a refusal, and the mfj way spouse_relative is the same on both routes. (Premises pinned: dependent.spouse_relative_joint, dependent.qr_other_relation, dependent.qr_household_member, dependent.qr_other_lawful, dependent.household_all_year, dependent.lawful, dependent.no, param:household.no; the mutant reads dependent.qr_other_lawful.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.spouse_relative_joint.no.then3` (replace an operand, dependent.dependent.spouse_relative_joint): spouse_relative_joint is a choice on the filing status: mfj takes spouse_relative, every other status takes dependent.no (the parameter household.no, false); the mutant reads qr_other_lawful in place of dependent.no for hoh. spouse_relative_joint is read by two lines only. qr_other_relation reads it only as the way of the guard 'qr_other_lawful is false', so wherever that alternative is taken qr_other_lawful is a memoized false in the same frame (spec 4.7.6), the value of dependent.no. qr_household_member reads it only as the way of the guard 'household_all_year is false'; qr_other_lawful is a choice on household_all_year whose false alternative is dependent.no, so there too it is false. Where the reader's guard is unknown both alternatives are ways (spec 4.7.3): qr_other_lawful is then that unknown or false (its ways are the input lawful and dependent.no, neither with a refusal gate), never a refusal, as dependent.no never is, so the reader is the guard's unknown on both routes; a refused guard ends the choose with its refusal on both routes. Where the status is unknown the mutant's way is again qr_other_lawful's false or unknown in each reading frame, never a refusal, and the mfj way spouse_relative is the same on both routes. (Premises pinned: dependent.spouse_relative_joint, dependent.qr_other_relation, dependent.qr_household_member, dependent.qr_other_lawful, dependent.household_all_year, dependent.lawful, dependent.no, param:household.no; the mutant reads dependent.qr_other_lawful.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.spouse_relative_joint.no.then4` (replace an operand, dependent.dependent.spouse_relative_joint): spouse_relative_joint is a choice on the filing status: mfj takes spouse_relative, every other status takes dependent.no (the parameter household.no, false); the mutant reads qr_other_lawful in place of dependent.no for qss. spouse_relative_joint is read by two lines only. qr_other_relation reads it only as the way of the guard 'qr_other_lawful is false', so wherever that alternative is taken qr_other_lawful is a memoized false in the same frame (spec 4.7.6), the value of dependent.no. qr_household_member reads it only as the way of the guard 'household_all_year is false'; qr_other_lawful is a choice on household_all_year whose false alternative is dependent.no, so there too it is false. Where the reader's guard is unknown both alternatives are ways (spec 4.7.3): qr_other_lawful is then that unknown or false (its ways are the input lawful and dependent.no, neither with a refusal gate), never a refusal, as dependent.no never is, so the reader is the guard's unknown on both routes; a refused guard ends the choose with its refusal on both routes. Where the status is unknown the mutant's way is again qr_other_lawful's false or unknown in each reading frame, never a refusal, and the mfj way spouse_relative is the same on both routes. (Premises pinned: dependent.spouse_relative_joint, dependent.qr_other_relation, dependent.qr_household_member, dependent.qr_other_lawful, dependent.household_all_year, dependent.lawful, dependent.no, param:household.no; the mutant reads dependent.qr_other_lawful.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.qualifying_relative.no.then1` (replace an operand, dependent.dependent.qualifying_relative): qualifying_relative is a choice on qr_relationship: true takes qr_from_child, false takes dependent.no (the parameter household.no, false); the mutant reads qr_kidnapped in place of dependent.no. qr_kidnapped is qualifying_relative's own fourth and last refusal gate, and a line's gates are evaluated at entry before its expression (spec 4.7.1): the choice is evaluated only when every gate was a known false, so wherever it is evaluated qr_kidnapped is a memoized false in the dependent's frame (spec 4.7.6), the value of dependent.no, whether the false alternative is taken or is one of the ways past an unknown qr_relationship (spec 4.7.3). A refused guard ends the choose with its refusal on both routes. (Premises pinned: dependent.qualifying_relative, dependent.qr_kidnapped, dependent.no, param:household.no; the mutant reads dependent.qr_kidnapped.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.qr_dependent.no.then1` (replace an operand, dependent.dependent.qr_dependent): qr_dependent is a choice on qualifying_relative: true takes qr_dependent_resident, false takes dependent.no (the parameter household.no, false); the mutant reads qr_kidnapped in place of dependent.no. qr_kidnapped is a refusal gate of qualifying_relative (its fourth), and a line's gates are evaluated at entry before its expression (spec 4.7.1): qualifying_relative is a known false only when every gate was a known false, so wherever the false alternative is taken qr_kidnapped is a memoized false in the dependent's frame (spec 4.7.6), the value of dependent.no. A refused guard ends the choose with its refusal on both routes. Where qualifying_relative is unknown both alternatives are ways (spec 4.7.3); neither dependent.no (a parameter) nor qr_kidnapped (a choice on under_19_kidnap, a comparison of the input age, between kidnapped_if_part_year, a choice on the input lived_all_year between dependent.no and the input kidnapped, and dependent.no, with no refusal gates) refuses, so qr_dependent is that unknown on both routes. (Premises pinned: dependent.qr_dependent, dependent.qualifying_relative, dependent.qr_kidnapped, dependent.under_19_kidnap, dependent.age, dependent.kidnapped_if_part_year, dependent.lived_all_year, dependent.kidnapped, dependent.no, param:household.no; the mutant reads dependent.qr_kidnapped.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.odc_person.no.then1` (replace an operand, dependent.dependent.odc_person): odc_person is a choice on claimed: true takes odc_from_tin, false takes dependent.no (the parameter household.no, false); the mutant reads ctc_child in place of dependent.no. claimed copies meets_tests behind the refusal gate claimed_no_tin, and meets_tests is a choice on qc_dependent: true takes qc_dependent itself, false takes qr_dependent. So claimed is a known false only through meets_tests's false alternative: qc_dependent is then a memoized false in the dependent's frame (spec 4.7.6), and ctc_child, a choice on qc_dependent whose false alternative is dependent.no, has no refusal gate and is false, the value of dependent.no. A refused guard ends the choose with its refusal on both routes. Where claimed is unknown both alternatives are ways (spec 4.7.3) and the base is that unknown, dependent.no being no refusal; the mutant differs only if odc_from_tin and ctc_child both refuse. ctc_child refuses only where qc_dependent refuses, or is true with ctc_from_tin refusing (an unknown qc_dependent leaves dependent.no a way). In both cases meets_tests is that refusal or true, so claimed is unknown only through its gate: claimed_no_tin is a choice on tin_known (no gates; tin_known is a choice on the input citizen_ssn between citizen_ssn itself and the input tin) between meets_tests (tin_known false) and dependent.no (tin_known true), so with tin_known true claimed is meets_tests's refusal or true, with tin_known false the gate is that refusal or true and claimed refuses, and claimed is unknown only with tin_known unknown. odc_from_tin is a choice on tin_known whose false alternative is dependent.no, so with tin_known unknown it is unknown, not a refusal, and odc_person is claimed's unknown on both routes. (Premises pinned: dependent.odc_person, dependent.claimed, dependent.claimed_no_tin, dependent.meets_tests, dependent.qc_dependent, dependent.ctc_child, dependent.ctc_from_tin, dependent.odc_from_tin, dependent.tin_known, dependent.citizen_ssn, dependent.tin, dependent.no, param:household.no; the mutant reads dependent.ctc_child.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.eic_ssn_child.no.then1` (replace an operand, dependent.dependent.eic_ssn_child): eic_ssn_child is a choice on eic_child: true takes eic_ssn_known, false takes dependent.no (the parameter household.no, false); the mutant reads kidnap_eic in place of dependent.no. kidnap_eic is eic_child's first refusal gate, evaluated at entry before the expression (spec 4.7.1): eic_child is a known false only when every gate was a known false, so wherever the false alternative is taken kidnap_eic is a memoized false in the dependent's frame (spec 4.7.6), the value of dependent.no. A refused guard ends the choose with its refusal on both routes. Where eic_child is unknown both alternatives are ways (spec 4.7.3); neither dependent.no nor kidnap_eic refuses (kidnap_eic is a choice on qc_relationship between kidnap_eic_kidnapped, a choice on kidnapped_if_part_year (a choice on the input lived_all_year between dependent.no and the input kidnapped) between not_us_half and dependent.no, and dependent.no; qc_relationship and not_us_half compare inputs; none has a refusal gate), so eic_ssn_child is that unknown on both routes. (Premises pinned: dependent.eic_ssn_child, dependent.eic_child, dependent.eic_ssn_known, dependent.kidnap_eic, dependent.kidnap_eic_kidnapped, dependent.qc_relationship, dependent.not_us_half, dependent.us_half, dependent.kidnapped_if_part_year, dependent.lived_all_year, dependent.kidnapped, dependent.relationship, dependent.no, param:household.no; the mutant reads dependent.kidnap_eic.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.edu_adj.zero.then1` (replace an operand, dependent.dependent.edu_adj): dependent.edu_adj's edu_student-false alternative: as for person.edu_adj, edu_has_adj is read only by edu_over_if_adj, which only edu_over_refused reads, in its edu_student-true alternative, and edu_over_refused is a choice on edu_student whose false alternative is edu_no (the year parameter edu.no, false); lines 27 to 30 read edu_adj only where edu_aoc is true, and edu_aoc is all[edu_aoc_rules true, f8863.ban_if_aoc false] with edu_aoc_rules a choice on edu_student whose false alternative is edu_no; line 31 reads it only where edu_llc is true, an all-test whose first conjunct is edu_student true. Where edu_student is unknown edu_adj is that unknown on both routes, its other alternative, edu_adj_sum (a sum of three inputs with no refusal gates), never refusing (spec 4.7.3). edu_adj, edu_has_adj and edu_over_if_adj are helpers. (Premises pinned: dependent.edu_adj, dependent.edu_adj_sum, dependent.edu_student, dependent.edu_has_adj, dependent.edu_over_if_adj, dependent.edu_over_refused, dependent.edu_aoc, dependent.edu_aoc_rules, dependent.edu_no, dependent.edu_llc, dependent.edu_line27, dependent.edu_line28, dependent.edu_line29, dependent.edu_line30, dependent.edu_line31, dependent.zero, param:edu.no; the mutant reads dependent.dc_line2d.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.edu_has_adj.edu_adj.gt.0` (replace an operand, dependent.dependent.edu_has_adj): Guarded figure: dependent.edu_adj is dependent.edu_adj_sum wherever dependent.edu_student holds, and every printed line reads dependent.edu_has_adj (a helper) only through choices whose guards make dependent.edu_student true, which, where a guard is unknown, are that unknown whatever dependent.edu_has_adj is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where dependent.edu_student does not hold only dependent.edu_has_adj's own, unprinted value can differ.
- `operand.dependent.dependent.edu_over_refused.edu_no.then1` (replace an operand, dependent.dependent.edu_over_refused): dependent.edu_over_refused is a choice on edu_student: true takes edu_over_if_adj, false takes edu_no (the year parameter edu.no, false); the mutant reads edu_has_adj (edu_adj more than $0) in place of edu_no. edu_adj is a choice on the same edu_student whose false alternative is dependent.zero (the parameter sales.zero, $0), so with edu_student a known false (memoized, spec 4.7.6) edu_adj is $0 and edu_has_adj is false, the value of edu_no. A refused guard ends the choose with its refusal on both routes. Where edu_student is unknown both alternatives are ways (spec 4.7.3); edu_no is a parameter and edu_has_adj cannot refuse (edu_adj's alternatives are edu_adj_sum, a sum of three inputs with no refusal gates, and dependent.zero, so edu_adj is never a refusal), so edu_over_refused is that unknown on both routes. (Premises pinned: dependent.edu_over_refused, dependent.edu_student, dependent.edu_over_if_adj, dependent.edu_has_adj, dependent.edu_adj, dependent.edu_adj_sum, dependent.zero, dependent.edu_no, param:edu.no, param:sales.zero; the mutant reads dependent.edu_has_adj.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.edu_aoc_rules.edu_no.then1` (replace an operand, dependent.dependent.edu_aoc_rules): Branch equal under a case split: where dependent.edu_aoc_rules takes alternative 1 (guard {
  "eq": [
    "dependent.edu_student",
    {
      "const": false
    }
  ],
  "op": "test"
}
), dependent.edu_no and dependent.edu_show26 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
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
- `operand.dependent.dependent.odc_from_tin.no.then1` (replace an operand, dependent.dependent.odc_from_tin): odc_from_tin is a choice on tin_known (a choice on the input citizen_ssn between citizen_ssn itself and the input tin, with no gates): true takes odc_from_citizen, false takes dependent.no (the parameter household.no, false); the mutant reads meets_tests in place of dependent.no. odc_from_tin is read only by odc_person, as the alternative its choice on claimed takes when claimed is true. claimed copies meets_tests behind the refusal gate claimed_no_tin, a choice on tin_known: false takes meets_tests, true takes dependent.no. claimed is a known true only when that gate was a known false (spec 4.7.1), which with tin_known false would need meets_tests false and so claimed false, and with tin_known unknown is unknown: so wherever claimed is true tin_known is a memoized true (spec 4.7.6) and odc_from_tin takes odc_from_citizen on both routes. Where claimed is false or a refusal odc_from_tin is not read. Where claimed is unknown both alternatives of odc_person are ways (spec 4.7.3) and its false alternative, dependent.no, is no refusal, so odc_person is claimed's unknown on both routes whatever odc_from_tin is. (Premises pinned: dependent.odc_from_tin, dependent.odc_person, dependent.claimed, dependent.claimed_no_tin, dependent.meets_tests, dependent.tin_known, dependent.citizen_ssn, dependent.tin, dependent.no, param:household.no; the mutant reads dependent.meets_tests.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.child_all_year.no.then1` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 1 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "sibling"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.child_all_year.no.then2` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 2 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "sibling_descendant"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.child_all_year.no.then3` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 3 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "parent"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.child_all_year.no.then4` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 4 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "parent_relative"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.child_all_year.no.then5` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 5 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "in_law"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.child_all_year.no.then6` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 6 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "household_member"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.child_all_year.no.then7` (replace an operand, dependent.dependent.child_all_year): Branch settled by its guard: where dependent.child_all_year takes alternative 7 (guard {
  "eq": [
    "dependent.relationship",
    {
      "const": "other"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.own_child_if_qss make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.no nor dependent.own_child_if_qss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.married_screen_qr.no` (replace an operand, dependent.dependent.married_screen_qr): married_screen_qr is a copy of dependent.no (the parameter household.no, false) behind its refusal gate dependent.married; the mutant reads married_if_ever_married_qc in place of dependent.no. married_screen_qr is read only by married_if_ever_married_qr, a choice on the input ever_married whose true alternative is married_screen_qr and whose false alternative is dependent.no. The copy is evaluated only where married was a known false (spec 4.7.1), memoized in the dependent's frame (spec 4.7.6). Through the reader ever_married is a known true, so married_if_ever_married_qc takes its own ever_married-true alternative, married_screen_qc, a copy of dependent.no behind the same gate dependent.married, a known false: false, the value of dependent.no. Where ever_married is unknown both alternatives of married_if_ever_married_qr are ways (spec 4.7.3) and dependent.no is no refusal, so the reader is that unknown on both routes; where it is false or a refusal the reader does not read married_screen_qr. married_screen_qr's own value differs only where ever_married is unknown and married false, where nothing reads it. (Premises pinned: dependent.married_screen_qr, dependent.married_if_ever_married_qr, dependent.married_if_ever_married_qc, dependent.married_screen_qc, dependent.married, dependent.ever_married, dependent.no, param:household.no; the mutant reads dependent.married_if_ever_married_qc.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.married_if_ever_married_qr.married_screen_qr.then0` (replace an operand, dependent.dependent.married_if_ever_married_qr): Branch settled by its guard: where dependent.married_if_ever_married_qr takes alternative 0 (guard {
  "eq": [
    "dependent.ever_married",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.married_screen_qr and dependent.married_if_ever_married_qc make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.married_if_ever_married_qr.no.then1` (replace an operand, dependent.dependent.married_if_ever_married_qr): Branch settled by its guard: where dependent.married_if_ever_married_qr takes alternative 1 (guard {
  "eq": [
    "dependent.ever_married",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.married_if_ever_married_qc make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.married_screen_eic.no` (replace an operand, dependent.dependent.married_screen_eic): married_screen_eic is a copy of dependent.no (the parameter household.no, false) behind its refusal gate dependent.married; the mutant reads married_if_ever_married_qr in place of dependent.no. married_screen_eic is read only by married_if_ever_married_eic, a choice on the input ever_married whose true alternative is married_screen_eic and whose false alternative is dependent.no. The copy is evaluated only where married was a known false (spec 4.7.1), memoized in the dependent's frame (spec 4.7.6). Through the reader ever_married is a known true, so married_if_ever_married_qr takes its own ever_married-true alternative, married_screen_qr, a copy of dependent.no behind the same gate dependent.married, a known false: false, the value of dependent.no. Where ever_married is unknown both alternatives of married_if_ever_married_eic are ways (spec 4.7.3) and dependent.no is no refusal, so the reader is that unknown on both routes; where it is false or a refusal the reader does not read married_screen_eic. married_screen_eic's own value differs only where ever_married is unknown and married false, where nothing reads it. (Premises pinned: dependent.married_screen_eic, dependent.married_if_ever_married_eic, dependent.married_if_ever_married_qr, dependent.married_screen_qr, dependent.married, dependent.ever_married, dependent.no, param:household.no; the mutant reads dependent.married_if_ever_married_qr.) (structural conditions re-checked this run.)
- `operand.dependent.dependent.married_if_ever_married_eic.no.then1` (replace an operand, dependent.dependent.married_if_ever_married_eic): Branch settled by its guard: where dependent.married_if_ever_married_eic takes alternative 1 (guard {
  "eq": [
    "dependent.ever_married",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.married_if_ever_married_qr make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.qc_tiebreak_not_child.no.then1` (replace an operand, dependent.dependent.qc_tiebreak_not_child): Branch settled by its guard: where dependent.qc_tiebreak_not_child takes alternative 1 (guard {
  "eq": [
    "dependent.other_claimant",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.no and dependent.qc_tiebreak_claimant make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.tin_known.citizen_ssn.then0` (replace an operand, dependent.dependent.tin_known): Branch settled by its guard: where dependent.tin_known takes alternative 0 (guard {
  "eq": [
    "dependent.citizen_ssn",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.citizen_ssn and dependent.citizen_known make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.citizen_ssn nor dependent.citizen_known ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.work_ssn_known.citizen_ssn.then0` (replace an operand, dependent.dependent.work_ssn_known): Branch settled by its guard: where dependent.work_ssn_known takes alternative 0 (guard {
  "eq": [
    "dependent.citizen_ssn",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.citizen_ssn and dependent.tin_known make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.citizen_ssn nor dependent.tin_known ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.dependent.dependent.eic_ssn_known.citizen_ssn.then0` (replace an operand, dependent.dependent.eic_ssn_known): Branch settled by its guard: where dependent.eic_ssn_known takes alternative 0 (guard {
  "eq": [
    "dependent.citizen_ssn",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that dependent.citizen_ssn and dependent.work_ssn_known make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither dependent.citizen_ssn nor dependent.work_ssn_known ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.eic.eic.step3_not_joint.no.then1` (replace an operand, eic.eic.step3_not_joint): Branch equal under a case split: where eic.step3_not_joint takes alternative 1 (guard {
  "eq": [
    "eic.step3_married",
    {
      "const": false
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "all": [
    {
      "ne": [
        "f1040.status",
        {
          "const": "mfj"
        }
      ],
      "op": "test"
    }
  ],
  "op": "test"
}
 on its one reader path), eic.no and eic.status_mfj have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.eic.eic.step3.step3_not_joint.then0` (replace an operand, eic.eic.step3): Branch settled by its guard: where eic.step3 takes alternative 0 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "single"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that eic.step3_not_joint and eic.not_qc_of_another make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither eic.step3_not_joint nor eic.not_qc_of_another ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.eic.eic.step3.step3_not_joint.then4` (replace an operand, eic.eic.step3): Branch settled by its guard: where eic.step3 takes alternative 4 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "qss"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that eic.step3_not_joint and eic.not_qc_of_another make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither eic.step3_not_joint nor eic.not_qc_of_another ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.eic.eic.show_wsb6.self_employed.all.1.eq.0` (replace an operand, eic.eic.show_wsb6): show_wsb6 is all[eligible, self_employed]; the mutant reads show_wsb4b, all[reached_step5, self_employed], in place of self_employed. eligible is a choice on reached_step5: true takes step5_income, false takes eic.no (the parameter household.no, false); none of these lines has a refusal gate. The second conjunct is reached only when eligible is true or unknown (a false or refused first conjunct ends both tests). eligible is true only through its first alternative, so reached_step5 is then a known true, memoized in the same frame (spec 4.7.6), and show_wsb4b is self_employed's value. Where eligible is unknown, reached_step5 is true or unknown (a false one makes eligible false, a refused one makes it that refusal): if true, show_wsb4b is self_employed's value; if unknown, show_wsb4b is false where self_employed is false, self_employed's refusal where it refuses, and unknown otherwise, which is what the base all-test, already holding eligible's unknown, gives with self_employed in that place. (Premises pinned: eic.show_wsb6, eic.show_wsb4b, eic.eligible, eic.reached_step5, eic.step5_income, eic.self_employed, eic.no, param:household.no; the mutant reads eic.show_wsb4b.) (structural conditions re-checked this run.)
- `operand.eic.eic.wsb_6.zero` (replace an operand, eic.eic.wsb_6): Gated zero carried earlier: eic.zero is an ungated zero and eic.step5_line4 the same zero behind refusal gates (s8812.combat_pay); eic.wsb_4b, read first, reaches eic.step5_line4 through ungated arithmetic, so whenever eic.step5_line4 refuses or is unknown eic.wsb_4b already is, and is returned first, and otherwise both operands are zero.
- `operand.eic.eic.line1.earned_income.then0` (replace an operand, eic.eic.line1): eic.line1 chooses on self_employed: false takes earned_income, true takes wsb_6 (wsb_4b floored at zero, no gates). The mutant reads earned_for_limit in the false alternative, a choice on the same guards that takes earned_income when self_employed is false and wsb_4b when true. With self_employed known false both are earned_income, the same memoized value. Where self_employed is unknown both lines evaluate both alternatives (spec 4.7.3): earned_for_limit is a refusal exactly when earned_income and wsb_4b both refuse, then earned_income's; wsb_6 refuses exactly when wsb_4b does. So the base line 1 is a refusal exactly when earned_income and wsb_4b refuse, then earned_income's, and so is the mutant (its first way is earned_for_limit, that same refusal); otherwise both are self_employed's unknown. (Premises pinned: eic.line1, eic.earned_for_limit, eic.earned_income, eic.wsb_6, eic.wsb_4b, eic.self_employed, eic.zero; the mutant reads eic.earned_for_limit.) (structural conditions re-checked this run.)
- `operand.eic.eic.line1_in_table.line1.ge.0` (replace an operand, eic.eic.line1_in_table): line1_in_table compares eic.line1 with eic.table_start; the mutant compares eic.earned_for_limit. Both choose on the same guards (self_employed false, then true) and take earned_income on the first; on the second line 1 takes wsb_6, which is wsb_4b floored at zero (subtract_floor0 from wsb_4b of eic.zero, no gates of its own), and earned_for_limit takes wsb_4b. A refused guard is the value of both; with an unknown guard both evaluate both alternatives (spec 4.7.3) and are a refusal exactly when earned_income and wsb_4b both refuse (wsb_6 refuses exactly when wsb_4b does), then earned_income's, the first way's, and otherwise that guard's unknown; an incomplete wsb_4b is wsb_6's value too. For a complete wsb_4b x, max(x, 0) >= start exactly when x >= start, because table_start is positive (checked). (Premises pinned: eic.line1_in_table, eic.line1, eic.earned_for_limit, eic.self_employed, eic.wsb_6, eic.wsb_4b, eic.earned_income, eic.zero, param:eic.table_start; the mutant reads eic.earned_for_limit.) (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table0.line1.key` (replace an operand, eic.eic.line1_table0): eic.line1_table0 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table1.line1.key` (replace an operand, eic.eic.line1_table1): eic.line1_table1 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table2.line1.key` (replace an operand, eic.eic.line1_table2): eic.line1_table2 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.line1_table3.line1.key` (replace an operand, eic.eic.line1_table3): eic.line1_table3 is read only by eic.line1_table, which only eic.line2 reads, and only in the alternative taken when eic.line1 is at least eic.table_start (a positive amount). eic.line1 and eic.earned_for_limit choose on eic.self_employed between eic.earned_income (not self-employed) and eic.wsb_6 or eic.wsb_4b (self-employed), and eic.wsb_6 is eic.wsb_4b floored at zero; so wherever the lookup is read, eic.line1 is positive and complete, eic.self_employed and the branch taken are complete, and the two keys are the same amount. The lookup lines and eic.line1_table are helpers: only their own, unprinted values can differ, where eic.line2 does not read them. (structural conditions re-checked this run.)
- `operand.eic.eic.credit.line6.then0` (replace an operand, eic.eic.credit): eic.credit's eligible alternative reads line6, which is line2 when line4 (line3 equals line1) is true and after_line4 otherwise, so the mutant differs only where line4 is true. eligible true needs step1_income (AGI, which line3 copies, below the limit) and step5_income (earned_for_limit, whose branch value is line1's source, below the limit) complete and true, so line3 and line1 are complete there and line4 is a complete comparison. With line4 true, line5 looks up line3 in the same EIC table (by the same ssn_count choices and filing status) that line2 looks up line1 in, so where line1 is at least table_start line5 equals line2 and after_line4 (line2, or the smaller of line5 and line2) is line2; where line1 is below table_start line2 is $0 and line3, equal to line1, is below every line 5 threshold (all of which exceed table_start), so line5 is blank and after_line4 is line2. eic.credit's refusal gate, household.eic_disallowed_claim (which reads eligible and line6 itself, through household.eic_claimed and household.eic_above_zero), is evaluated at line entry before the expression, the same on both routes (spec 4.7.1); only the expression's operand changes. (Premises pinned: eic.credit, eic.eligible, eic.line6, eic.after_line4, eic.line4, eic.line3, eic.line1, eic.line2, eic.zero, eic.line1_in_table, eic.line1_table, eic.line1_table0, eic.line1_table1, eic.line1_table2, eic.line1_table3, eic.line5, eic.line3_table0, eic.line3_table1, eic.line3_table2, eic.line3_table3, eic.line5_blank, eic.line5_threshold, eic.threshold_other, eic.threshold_joint, eic.threshold0_other, eic.threshold1_other, eic.threshold0_joint, eic.threshold1_joint, eic.smaller, eic.step1_income, eic.step5_income, eic.earned_for_limit, eic.wsb_6, eic.wsb_4b, eic.earned_income, param:eic.table_start; the mutant reads eic.after_line4.) (structural conditions re-checked this run.)
- `boundary.eic.eic.wsb_4b_positive` (replace strict greater-than with inclusive, eic.eic.wsb_4b_positive): The inclusive test differs only at Worksheet B line 4b = 0. wsb_4b_positive is read only by the line 5 stop, an all-test that requires self-employment before it and, after it, Step 5 question 3 to be No; for a self-employed filer question 3 compares line 4b with the EIC limit, so at line 4b = 0 it asks whether 0 < limit, which holds for every limit (all are positive). The stop is therefore false on both routes, and question 3 reads only lines the stop has already evaluated without refusal, so no refusal is newly reached. (structural conditions re-checked this run.)
- `operand.eic.eic.from_step1_income.no.then1` (replace an operand, eic.eic.from_step1_income): from_step1_income is a choice on step1_income: true takes from_step1_ssn, false takes eic.no (the parameter household.no, false); the mutant reads eic.clergy in place of eic.no. clergy is scope.schedule1 = true behind its own refusal gate scope.schedule1, so it is false where scope.schedule1 is a known false, that gate's refusal where it is true, unknown where it is unknown, and its refusal where it is a refusal (scope.schedule1 is an any-test over the scope items and their gate lines). step1_income compares Form 1040 line 11b with eic.limit; line 11b copies line 11a, line 9 less line 10, and line 10 has the refusal gate scope.schedule1, so wherever scope.schedule1 is true or a refusal line 10, line 11a and line 11b are refusals and so is step1_income (a subtraction and a comparison return their operands' first refusal, a refusal outranking an unknown, spec 4.7.2). So where the false alternative is taken step1_income is a known false, line 11b is complete, scope.schedule1 is a known false memoized in the same frame (spec 4.7.6), and clergy is false, the value of eic.no. A refused guard ends the choose with its refusal on both routes. Where step1_income is unknown both alternatives are ways (spec 4.7.3); scope.schedule1 is then neither true nor a refusal, so clergy is false or unknown, never a refusal, as eic.no is not, and from_step1_income is that unknown on both routes. (Premises pinned: eic.from_step1_income, eic.step1_income, eic.clergy, eic.no, eic.limit, f1040.line11b, f1040.line11a, f1040.line10, f1040.line9, scope.schedule1, param:household.no; the mutant reads eic.clergy.) (structural conditions re-checked this run.)
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
- `operand.f1116.f1116.line13.zero` (replace an operand, f1116.f1116.line13): Copy-chain identity: f1116.zero and f1116.line12 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f1116.f1116.line16.zero` (replace an operand, f1116.f1116.line16): Copy-chain identity: f1116.zero and f1116.line13 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f1116.f1116.line18_shown.line17.gt.0` (replace an operand, f1116.f1116.line18_shown): f1116.line18_shown tests line 17 more than $0; the mutant tests line 15. Line 17 is the sum of line 15 and line 16, and line 16 is a copy of f1116.zero, the parameter sales.zero ($0), with no refusal gates, so line 16 is always the amount $0. A sum takes its first refusal, else its first unknown, else the total (spec 4.7.4): where line 15 is an amount, line 17 is that amount plus $0, the same amount; where line 15 is a refusal, line 17 is that refusal; where it is unknown, line 17 is an unknown (the known $0 adds no mark), which compares equal to line 15's. Neither line 17 nor line 15 has refusal gates, so the test compares the same operand value with $0 on both routes, and line18_shown, read only by line 18's display condition, has the same value on every input. (Premises pinned: f1116.line18_shown, f1116.line17, f1116.line15, f1116.line16, f1116.zero, param:sales.zero; the mutant reads f1116.line15.) (structural conditions re-checked this run.)
- `operand.f1116.f1116.line18.zero` (replace an operand, f1116.f1116.line18): Copy-chain identity: f1116.zero and f1116.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f1116.f1116.line24.line23` (replace an operand, f1116.f1116.line24): f1116.line24 is the smaller of line 14 and line 23; the mutant reads line 21 in place of line 23. Line 23 is the sum of line 21 and line 22, and line 22 is a copy of f1116.zero, the parameter sales.zero ($0), with no refusal gates, so line 22 is always the amount $0. A sum takes its first refusal, else its first unknown, else the total (spec 4.7.4): where line 21 is an amount, line 23 is that amount plus $0, the same amount; where line 21 is a refusal, line 23 is that refusal; where it is unknown, line 23 is an unknown (the known $0 adds no mark), which compares equal to line 21's. Neither line 23 nor line 21 has refusal gates, so line 24 compares the same operand values on both routes and no value of line 24 changes. (Premises pinned: f1116.line24, f1116.line23, f1116.line21, f1116.line22, f1116.zero, param:sales.zero; the mutant reads f1116.line21.) (structural conditions re-checked this run.)
- `operand.f1116.f1116.line32.line27` (replace an operand, f1116.f1116.line32): Copy-chain identity: f1116.line27 and f1116.line24 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f1116.f1116.line33.line32` (replace an operand, f1116.f1116.line33): Copy-chain identity: f1116.line32 and f1116.line27 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f1116.f1116.line34.zero` (replace an operand, f1116.f1116.line34): Copy-chain identity: f1116.zero and f1116.line22 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f1116col.f1116col.div_tax_hi.zero.then1` (replace an operand, f1116col.f1116col.div_tax_hi): Branch settled by its guard: where f1116col.div_tax_hi takes alternative 1 (guard {
  "eq": [
    "f1116col.div_hi",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1116col.zero and f1116col.div_gross_hi make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1116col.zero nor f1116col.div_gross_hi ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1116col.f1116col.div_tax_lo.zero.then1` (replace an operand, f1116col.f1116col.div_tax_lo): Branch settled by its guard: where f1116col.div_tax_lo takes alternative 1 (guard {
  "eq": [
    "f1116col.div_lo",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1116col.zero and f1116col.div_gross_lo make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1116col.zero nor f1116col.div_gross_lo ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1116col.f1116col.int_tax_hi.zero.then1` (replace an operand, f1116col.f1116col.int_tax_hi): Branch settled by its guard: where f1116col.int_tax_hi takes alternative 1 (guard {
  "eq": [
    "f1116col.int_hi",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1116col.zero and f1116col.int_gross_hi make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1116col.zero nor f1116col.int_gross_hi ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f1116col.f1116col.int_tax_lo.zero.then1` (replace an operand, f1116col.f1116col.int_tax_lo): Branch settled by its guard: where f1116col.int_tax_lo takes alternative 1 (guard {
  "eq": [
    "f1116col.int_lo",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f1116col.zero and f1116col.int_gross_lo make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f1116col.zero nor f1116col.int_gross_lo ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f2441.f2441.statement_notice.no.then1` (replace an operand, f2441.f2441.statement_notice): Branch settled by its guard: where f2441.statement_notice takes alternative 1 (guard {
  "eq": [
    "f2441.filing",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f2441.no and f2441.line1_box make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f2441.no nor f2441.line1_box ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f2441.f2441.household_notice.no.then1` (replace an operand, f2441.f2441.household_notice): Branch settled by its guard: where f2441.household_notice takes alternative 1 (guard {
  "eq": [
    "f2441.filing",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f2441.no and f2441.statement_notice make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f2441.no nor f2441.statement_notice ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f2441.f2441.line11_figured.line10` (replace an operand, f2441.f2441.line11_figured): Copy-chain identity: f2441.line10 and f2441.clw3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f2441.f2441.line13_earned.line20.all.3.gt.1` (replace an operand, f2441.f2441.line13_earned): The fourth conjunct of line13_earned compares line 23 with line 20; the mutant compares it with line 24. Line 22 is f2441.zero (a $0 parameter), so line 24 is the smaller of (the smaller of line 20 and line 21) and $0, and line 23 is line 15 less $0. The fourth conjunct is reached only after line 20 < line 17 and line 20 < line 21 were each true or unknown. Line 20 is line 17, 18 and 19's smallest floored at zero, so line 20 complete means line 17 complete and the second conjunct complete: then line 20 < line 17 <= line 15 = line 23, so both comparisons are true when line 23 is complete, and both are line 23's own unknown or refusal otherwise (it is the left operand, and the right operand is complete in both when line 21 is). Line 21 unknown leaves the third conjunct unknown and line 24 unknown: the base comparison is true or line 23's incompleteness, the mutant's unknown or that refusal, so the test is the same. Line 20 unknown makes line 24 unknown, and both comparisons are line 23's refusal or unknown. A refusal of line 20 or line 21 ends the test at the second or third conjunct. (Premises pinned: f2441.line13_earned, f2441.line24, f2441.line24_20_21, f2441.line22, f2441.zero, f2441.line20, f2441.line20_all, f2441.line20_17_18, f2441.line17, f2441.line15, f2441.line23, f2441.line21, param:sales.zero; the mutant reads f2441.line24.) (structural conditions re-checked this run.)
- `operand.f2441.f2441.line25.line24` (replace an operand, f2441.f2441.line25): Floor-minus-min identity: f2441.line25 is f2441.line24_20_21 less f2441.line24, floored at zero, and one of f2441.line24 and f2441.line22 is the ungated smaller of f2441.line24_20_21 and the other, so f2441.line24_20_21 less either, floored at zero, is the same at every input; f2441.line24_20_21 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.f5329.f5329.l49_base.l48` (replace an operand, f5329.f5329.l49_base): Copy-chain identity: f5329.l48 and f5329.l47 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.line7a_if_any.no.then1` (replace an operand, f5695.f5695.line7a_if_any): Branch settled by its guard: where f5695.line7a_if_any takes alternative 1 (guard {
  "eq": [
    "f5695.any",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f5695.no and f5695.biomass_if_any make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f5695.no nor f5695.biomass_if_any ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f5695.f5695.part1_any.no.then1` (replace an operand, f5695.f5695.part1_any): f5695.part1_any is a choice on f5695.kinds_answered: true takes f5695.part1_some, false takes f5695.no (the parameter household.no, false); the mutant takes f5695.sec_b_kinds in place of f5695.no. f5695.kinds_answered is an all-test whose every conjunct is any(K eq true, K eq false) over one kind line K (each a Bool choice on f5695.any between the kind's input and f5695.no, with no refusal gate), so each conjunct is true, unknown or a refusal and the all-test is never a known false (spec 4.7.2); the guard 'kinds_answered eq false' is never true. No line among the kind lines, f5695.carry_if_prior (a choice on the input s3.prior_other_forms between the input f5695.carry and f5695.no), f5695.part1_some and f5695.sec_b_kinds (any-tests of those lines) has a refusal gate, so none of them is ever a refusal. Where kinds_answered is true both routes take part1_some; where it is a refusal the choice is that refusal on both. Where it is unknown both alternatives are ways (spec 4.7.3); neither way refuses on either route (f5695.no, part1_some and sec_b_kinds are never refusals), so part1_any is kinds_answered's unknown on both routes. No value of part1_any changes. (Premises pinned: f5695.part1_any, f5695.kinds_answered, f5695.part1_some, f5695.sec_b_kinds, f5695.carry_if_prior, f5695.carry, s3.prior_other_forms, f5695.any, f5695.no, param:household.no, f5695.solar_if_any, f5695.solar, f5695.solar_water_if_any, f5695.solar_water, f5695.wind_if_any, f5695.wind, f5695.geothermal_if_any, f5695.geothermal, f5695.line5a_if_any, f5695.line5a, f5695.line7a_if_any, f5695.line7a, f5695.insulation_if_any, f5695.insulation, f5695.doors_if_any, f5695.doors, f5695.windows_if_any, f5695.windows, f5695.panel_if_any, f5695.panel, f5695.audit_if_any, f5695.audit, f5695.heat_pump_if_any, f5695.heat_pump, f5695.hp_water_heater_if_any, f5695.hp_water_heater, f5695.central_ac_if_any, f5695.central_ac, f5695.water_heater_if_any, f5695.water_heater, f5695.furnace_if_any, f5695.furnace, f5695.biomass_if_any, f5695.biomass; the mutant reads f5695.sec_b_kinds.) (structural conditions re-checked this run.)
- `operand.f5695.f5695.part2_any.no.then1` (replace an operand, f5695.f5695.part2_any): Branch settled by its guard: where f5695.part2_any takes alternative 1 (guard {
  "eq": [
    "f5695.kinds_answered",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f5695.no and f5695.part1_any make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f5695.no nor f5695.part1_any ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f5695.f5695.line11_if_any.zero.then1` (replace an operand, f5695.f5695.line11_if_any): Branch settled by its guard: where f5695.line11_if_any takes alternative 1 (guard {
  "eq": [
    "f5695.any",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f5695.zero and f5695.line6b_if_any make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f5695.f5695.claiming_part1.no.then1` (replace an operand, f5695.f5695.claiming_part1): f5695.claiming_part1 is a choice on f5695.part1_any: true takes f5695.line13_positive, false takes f5695.no (the parameter household.no, false); the mutant takes f5695.line5a_if_any in place of f5695.no. part1_any is a choice on f5695.kinds_answered (true: f5695.part1_some; false: f5695.no). f5695.kinds_answered is an all-test whose every conjunct is any(K eq true, K eq false) over one kind line K (each a Bool choice on f5695.any between the kind's input and f5695.no, with no refusal gate), so each conjunct is true, unknown or a refusal and the all-test is never a known false (spec 4.7.2); the guard 'kinds_answered eq false' is never true. No line among the kind lines, f5695.carry_if_prior (a choice on the input s3.prior_other_forms between the input f5695.carry and f5695.no), f5695.part1_some and f5695.sec_b_kinds (any-tests of those lines) has a refusal gate, so none of them is ever a refusal. So part1_any is a known false only as part1_some known false, an any-test of which one disjunct is 'line5a_if_any eq true'; that disjunct is then a known false, so the Bool line5a_if_any is false, the value f5695.no gives. Where part1_any is true both routes take line13_positive; where it is a refusal the choice is that refusal on both. Where it is unknown both alternatives are ways (spec 4.7.3), and neither f5695.no nor line5a_if_any (a choice on f5695.any between the input f5695.line5a and f5695.no, no refusal gate) ever refuses, so claiming_part1 is part1_any's unknown on both routes. No value of claiming_part1 changes. (Premises pinned: f5695.claiming_part1, f5695.line13_positive, f5695.part1_any, f5695.kinds_answered, f5695.part1_some, f5695.sec_b_kinds, f5695.carry_if_prior, f5695.carry, s3.prior_other_forms, f5695.any, f5695.no, param:household.no, f5695.solar_if_any, f5695.solar, f5695.solar_water_if_any, f5695.solar_water, f5695.wind_if_any, f5695.wind, f5695.geothermal_if_any, f5695.geothermal, f5695.line5a_if_any, f5695.line5a, f5695.line7a_if_any, f5695.line7a, f5695.insulation_if_any, f5695.insulation, f5695.doors_if_any, f5695.doors, f5695.windows_if_any, f5695.windows, f5695.panel_if_any, f5695.panel, f5695.audit_if_any, f5695.audit, f5695.heat_pump_if_any, f5695.heat_pump, f5695.hp_water_heater_if_any, f5695.hp_water_heater, f5695.central_ac_if_any, f5695.central_ac, f5695.water_heater_if_any, f5695.water_heater, f5695.furnace_if_any, f5695.furnace, f5695.biomass_if_any, f5695.biomass; the mutant reads f5695.line5a_if_any.) (structural conditions re-checked this run.)
- `operand.f5695.f5695.rce_credit.rce_limit` (replace an operand, f5695.f5695.rce_credit): Copy-chain identity: f5695.rce_limit and f5695.rce_ws3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f5695.f5695.carry_out.rce_credit` (replace an operand, f5695.f5695.carry_out): Floor-minus-min identity: f5695.carry_out is f5695.line13 less f5695.rce_credit, floored at zero, and one of f5695.rce_credit and f5695.rce_limit is the ungated smaller of f5695.line13 and the other, so f5695.line13 less either, floored at zero, is the same at every input; f5695.line13 is read first on both routes and the other operand second, so the same refusal or unknown wins.
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
- `operand.f7203.f7203.l3i.zero` (replace an operand, f7203.f7203.l3i): Copy-chain identity: f7203.zero and f7203.l3h expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f7203.f7203.l3j.zero` (replace an operand, f7203.f7203.l3j): Copy-chain identity: f7203.zero and f7203.l3i expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f7203.f7203.l3m.zero` (replace an operand, f7203.f7203.l3m): Copy-chain identity: f7203.zero and f7203.l3l expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f7203.f7203.l8c.zero` (replace an operand, f7203.f7203.l8c): Copy-chain identity: f7203.zero and f7203.l8b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f7203.f7203.room36.c35` (replace an operand, f7203.f7203.room36): Guarded figure: f7203.c35 is f7203.c35_k wherever f7203.has_loss holds, and every printed line reads f7203.room36 (a helper) only through choices whose guards make f7203.has_loss true, which, where a guard is unknown, are that unknown whatever f7203.room36 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where f7203.has_loss does not hold only f7203.room36's own, unprinted value can differ.
- `operand.f7203.f7203.room37.c36` (replace an operand, f7203.f7203.room37): Guarded figure: f7203.c36 is f7203.c36_k wherever f7203.has_loss holds, and every printed line reads f7203.room37 (a helper) only through choices whose guards make f7203.has_loss true, which, where a guard is unknown, are that unknown whatever f7203.room37 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where f7203.has_loss does not hold only f7203.room37's own, unprinted value can differ.
- `operand.f7203.f7203.room38.c37` (replace an operand, f7203.f7203.room38): Guarded figure: f7203.c37 is f7203.c37_k wherever f7203.has_loss holds, and every printed line reads f7203.room38 (a helper) only through choices whose guards make f7203.has_loss true, which, where a guard is unknown, are that unknown whatever f7203.room38 is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where f7203.has_loss does not hold only f7203.room38's own, unprinted value can differ.
- `operand.f7203.f7203.line13.zero` (replace an operand, f7203.f7203.line13): Copy-chain identity: f7203.zero and f7203.line12 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f7203.f7203.line14.line11` (replace an operand, f7203.f7203.line14): f7203.line14 is the sum of f7203.line11, f7203.line12 and f7203.line13 (the last two copies of f7203.zero, the parameter sales.zero, $0); the mutant reads f7203.c47 for f7203.line11, which is smaller_of f7203.c47 and f7203.line10. f7203.line14's only reader is f7203.line15, subtract_floor0 from f7203.line10 take f7203.line14. Where f7203.line10 is unknown or a refusal, f7203.line15 is that value on both routes (its from operand is evaluated first, spec 4.7.4). Where f7203.line10 is a known amount L: f7203.c47 is the sum of f7203.c35 to f7203.c38, each a choice on f7203.has_loss between its _k helper and f7203.zero. With has_loss false each is $0, so c47 is $0 and line 11 is min(0, L) = 0. With has_loss true, c35_k is at most L, room36 is L less c35 (not below zero), c36_k at most room36, room37 is room36 less c36, c37_k at most room37, room38 is room37 less c37, and c38_k at most room38, so c35 + c36 + c37 + c38 is at most L and line 11 is c47. Where c47 or has_loss is unknown or a refusal and L is known, smaller_of's only incomplete operand is c47, so line 11 is c47's value. So f7203.line14 is the same on both routes wherever f7203.line15 reads it, and f7203.line15 is the same everywhere; only f7203.line14's own value can differ, where f7203.line10 is incomplete. None of these lines carries a refusal gate. (Premises pinned: f7203.line14, f7203.line11, f7203.line12, f7203.line13, f7203.line15, f7203.line10, f7203.c47, f7203.c35, f7203.c36, f7203.c37, f7203.c38, f7203.c35_k, f7203.c36_k, f7203.c37_k, f7203.c38_k, f7203.room36, f7203.room37, f7203.room38, f7203.has_loss, f7203.zero, param:sales.zero; the mutant reads f7203.c47.) (structural conditions re-checked this run.)
- `operand.f8853c.f8853c.line20.line18` (replace an operand, f8853c.f8853c.line20): Copy-chain identity: f8853c.line18 and f8853c.line17_if_periodic expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8863.f8863.clw3.clw1` (replace an operand, f8863.f8863.clw3): Copy-chain identity: f8863.clw1 and f8863.line18 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8880.f8880.clw_room.clw3.gt.0` (replace an operand, f8880.f8880.clw_room): Copy-chain identity: f8880.clw3 and f8880.line11 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8880.f8880.line3b_counted.zero.then1` (replace an operand, f8880.f8880.line3b_counted): line3b_counted's elig_b-false alternative is f8880.zero ($0); the mutant reads line3a_counted. line3b_counted is read only by contrib_counted, sum[line3a_counted, line3b_counted], which only has_contrib reads, as contrib_counted more than $0 (sales.zero). Where the alternative is taken contrib_counted is line3a_counted plus $0 on the base route and line3a_counted twice on the mutant's: a sum returns its first operand's refusal at once (spec 4.7.4), an unknown first operand leaves both unknown, and a complete, non-negative x and 2x are both more than $0 or both $0. With elig_b unknown the mutant's line3b_counted can be a refusal where the base's is unknown only if line3a_counted refuses, and contrib_counted is then line3a_counted's refusal on both routes. (Premises pinned: f8880.line3b_counted, f8880.line3a_counted, f8880.contrib_counted, f8880.has_contrib, f8880.zero, param:sales.zero; the mutant reads f8880.line3a_counted.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.bad_months.counts_hold.then0` (replace an operand, f8889.f8889.bad_months): bad_months's self_only alternative is counts_hold (the parameter hsa.year_counts_hold, false); the mutant reads mfs. bad_months is read only by line13_figured, as a refusal gate after mfs, the first of its gates: a later gate is evaluated only when mfs is a known false (spec 4.7.1), and mfs is then a memoized false in the same frame (spec 4.7.6), so the mutant's alternative is false, counts_hold's value. Where the coverage used (f8889.coverage) is unknown the alternatives are ways (spec 4.7.3) and the mutant's way is that same false. Only bad_months's own value changes, where mfs is true or unknown, and no line reads it there. (Premises pinned: f8889.bad_months, f8889.line13_figured, f8889.mfs, f8889.counts_hold, param:hsa.year_counts_hold, f8889.coverage; the mutant reads f8889.mfs.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.bad_months.counts_hold.then1` (replace an operand, f8889.f8889.bad_months): bad_months's family alternative is counts_hold (the parameter hsa.year_counts_hold, false); the mutant reads mfs. bad_months is read only by line13_figured, as a refusal gate after mfs, the first of its gates: a later gate is evaluated only when mfs is a known false (spec 4.7.1), and mfs is then a memoized false in the same frame (spec 4.7.6), so the mutant's alternative is false, counts_hold's value. Where the coverage used (f8889.coverage) is unknown the alternatives are ways (spec 4.7.3) and the mutant's way is that same false. Only bad_months's own value changes, where mfs is true or unknown, and no line reads it there. (Premises pinned: f8889.bad_months, f8889.line13_figured, f8889.mfs, f8889.counts_hold, param:hsa.year_counts_hold, f8889.coverage; the mutant reads f8889.mfs.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.no_fsa.yes.then1` (replace an operand, f8889.f8889.no_fsa): Branch equal under a case split: where f8889.no_fsa takes alternative 1 (guard {
  "eq": [
    "f8889.fsa_if_clear",
    {
      "const": false
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "f8889.clear_if_uniform",
    {
      "const": true
    }
  ],
  "op": "test"
}
 on its one reader path), f8889.yes and f8889.clear_if_uniform have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.f8889.f8889.eligible_all.no.then1` (replace an operand, f8889.f8889.eligible_all): Branch settled by its guard: where f8889.eligible_all takes alternative 1 (guard {
  "eq": [
    "f8889.clear_if_uniform",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f8889.no and f8889.fsa_if_clear make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f8889.no nor f8889.fsa_if_clear ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f8889.f8889.sf_married.yes.then0` (replace an operand, f8889.f8889.sf_married): Branch equal under a case split: where f8889.sf_married takes alternative 0 (guard {
  "eq": [
    "household.married",
    {
      "const": true
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "f8889.eligible_all",
    {
      "const": true
    }
  ],
  "op": "test"
}
, {
  "eq": [
    "f8889.year_self_answered",
    {
      "const": true
    }
  ],
  "op": "test"
}
 on its one reader path), f8889.yes and f8889.eligible_all have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.f8889.f8889.fsf_eligible.no.then1` (replace an operand, f8889.f8889.fsf_eligible): Branch equal under a case split: where f8889.fsf_eligible takes alternative 1 (guard {
  "eq": [
    "f8889.eligible_all",
    {
      "const": false
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "f8889.coverage_year",
    {
      "const": "self_only"
    }
  ],
  "op": "test"
}
 on its one reader path), f8889.no and f8889.spouse_family_if_asked have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.f8889.f8889.coverage_family.cov_changed.then1` (replace an operand, f8889.f8889.coverage_family): Branch settled by its guard: where f8889.coverage_family takes alternative 1 (guard {
  "eq": [
    "f8889.eligible_all",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f8889.cov_changed and f8889.coverage_self make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither f8889.cov_changed nor f8889.coverage_self ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f8889.f8889.age55_unmarried.age55.all.0.eq.0` (replace an operand, f8889.f8889.age55_unmarried): age55_unmarried is all[age55, household.married false]; the mutant reads age55_line3, all[age55, married_family false], in place of age55. married_family is a choose on household.married (family_any_time where true, f8889.no where false), and family_any_time is a choose on full_year (dec_family or some_family_months) over inputs and parameters with no refusal gates (coverage_year and the checks beneath it, dec_coverage, last_month, months_family, and the parameters behind year_same, year_self_only, year_family and no_last_month); household.married and age55 are derived with no refusal gates on the way (household.married a choice on marriage_possible (a choice on the input f1040.status taking the input ever_married or status_states_marriage, a test of the status) taking the input married_dec31 or household.no, the parameter household.no (false); age55 a test of the input person.birth_year against the parameter age.cut_55 and of age55_at_year_end_if_open_year, a choice on age55_open_year (a test of birth_year) taking the input age55_at_year_end or person.no). So none of these lines is a refusal. With married false, married_family is false and age55_line3 is age55. With married true the second conjunct is false on both routes, and the mutant's first conjunct is age55's value or false, never a refusal. With married unknown, married_family is unknown, so age55_line3 is false where age55 is false and otherwise age55's value or unknown, and the second conjunct is unknown: both tests are false where age55 is false and unknown otherwise. (Premises pinned: f8889.age55_unmarried, f8889.age55_line3, f8889.married_family, f8889.age55, household.married, f8889.family_any_time, f8889.dec_family, f8889.some_family_months, f8889.full_year, f8889.year_same, f8889.use_last_month, f8889.dec_coverage_if_changed, f8889.coverage_year, f8889.dec_coverage, f8889.last_month, f8889.no_last_month, f8889.year_self_only, f8889.year_family, f8889.months_family, f8889.coverage, f8889.coverage_self, f8889.coverage_self_spouse, f8889.coverage_family, f8889.eligible_all, f8889.no_fsa, f8889.clear_if_uniform, f8889.fsa_if_clear, f8889.spouse_family_if_asked, f8889.ask_spouse_family, f8889.year_self_answered, f8889.sf_eligible, f8889.sf_married, f8889.clear_all_year, f8889.fsa, f8889.spouse_family, f8889.cov_self_only, f8889.cov_family, f8889.cov_changed, f8889.no, f8889.yes, param:hsa.no, param:hsa.yes, param:hsa.cov_self_only, param:hsa.cov_family, param:hsa.cov_changed, household.marriage_possible, household.married_dec31, household.ever_married, household.status_states_marriage, household.no, param:household.no, person.age55_at_year_end_if_open_year, person.age55_open_year, person.age55_at_year_end, person.no, param:age.cut_55; the mutant reads f8889.age55_line3.) (structural conditions re-checked this run.)
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
- `operand.f8889.f8889.family_dec_year.zero.then2` (replace an operand, f8889.f8889.family_dec_year): family_dec_year's none alternative (no December 1 coverage) is f8889.zero; the mutant reads line5. family_dec_year is read only by step1_total, which takes it where full_year is true. full_year is a choose on coverage (the coverage used: the coverage_year answer, turned to changed by the checks beneath it, clear_all_year, fsa and spouse_family, all inputs with no gates): year_same (a parameter) for self_only and family, use_last_month for changed; use_last_month takes no_last_month (the parameter hsa.no_last_month, false) where dec_coverage_if_changed is none; and dec_coverage_if_changed is year_self_only or year_family (the parameters hsa.year_self_only, self_only, and hsa.year_family, family) for those two coverage values and dec_coverage for changed. So full_year true never meets December coverage none, and the changed alternative is not taken there. full_year reads only inputs and parameters with no gates, so it is never a refusal; where it is unknown step1_total's other way, family_counted (the parameter line family_under55 times the input months_family), never refuses, so step1_total is full_year's unknown on both routes (spec 4.7.3). (Premises pinned: f8889.family_dec_year, f8889.step1_total, f8889.full_year, f8889.year_same, f8889.use_last_month, f8889.no_last_month, f8889.last_month, f8889.dec_coverage_if_changed, f8889.coverage_year, f8889.dec_coverage, f8889.year_self_only, f8889.year_family, f8889.family_counted, f8889.family_under55, f8889.months_family, f8889.zero, param:hsa.no_last_month, param:hsa.year_self_only, param:hsa.year_family, f8889.coverage, f8889.coverage_self, f8889.coverage_self_spouse, f8889.coverage_family, f8889.eligible_all, f8889.no_fsa, f8889.clear_if_uniform, f8889.fsa_if_clear, f8889.spouse_family_if_asked, f8889.ask_spouse_family, f8889.year_self_answered, f8889.sf_eligible, f8889.sf_married, f8889.clear_all_year, f8889.fsa, f8889.spouse_family, f8889.cov_self_only, f8889.cov_family, f8889.cov_changed, f8889.no, f8889.yes, param:hsa.no, param:hsa.yes, param:hsa.cov_self_only, param:hsa.cov_family, param:hsa.cov_changed; the mutant reads f8889.line5.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.self_dec_year.zero.then2` (replace an operand, f8889.f8889.self_dec_year): self_dec_year's none alternative (no December 1 coverage) is f8889.zero; the mutant reads self_family_months. self_dec_year is read only by self_in_family, which takes it where full_year is true. full_year is a choose on coverage (the coverage used: the coverage_year answer, turned to changed by the checks beneath it, clear_all_year, fsa and spouse_family, all inputs with no gates): year_same (a parameter) for self_only and family, use_last_month for changed; use_last_month takes no_last_month (the parameter hsa.no_last_month, false) where dec_coverage_if_changed is none; and dec_coverage_if_changed is year_self_only or year_family (the parameters hsa.year_self_only, self_only, and hsa.year_family, family) for those two coverage values and dec_coverage for changed. So full_year true never meets December coverage none, and the changed alternative is not taken there. full_year reads only inputs and parameters with no gates, so it is never a refusal; where it is unknown self_in_family's other way, self_family_months (self_amount times the input months_family, reading only inputs and parameters with no refusal gates), never refuses, so self_in_family is full_year's unknown on both routes (spec 4.7.3). (Premises pinned: f8889.self_dec_year, f8889.self_in_family, f8889.full_year, f8889.year_same, f8889.use_last_month, f8889.no_last_month, f8889.last_month, f8889.dec_coverage_if_changed, f8889.coverage_year, f8889.dec_coverage, f8889.year_self_only, f8889.year_family, f8889.self_family_months, f8889.self_amount, f8889.self_55, f8889.self_under55, f8889.age55_line3, f8889.age55, f8889.married_family, household.married, f8889.family_any_time, f8889.dec_family, f8889.some_family_months, f8889.months_family, f8889.zero, param:hsa.no_last_month, param:hsa.year_self_only, param:hsa.year_family, f8889.coverage, f8889.coverage_self, f8889.coverage_self_spouse, f8889.coverage_family, f8889.eligible_all, f8889.no_fsa, f8889.clear_if_uniform, f8889.fsa_if_clear, f8889.spouse_family_if_asked, f8889.ask_spouse_family, f8889.year_self_answered, f8889.sf_eligible, f8889.sf_married, f8889.clear_all_year, f8889.fsa, f8889.spouse_family, f8889.cov_self_only, f8889.cov_family, f8889.cov_changed, f8889.no, f8889.yes, param:hsa.no, param:hsa.yes, param:hsa.cov_self_only, param:hsa.cov_family, param:hsa.cov_changed, household.marriage_possible, household.married_dec31, household.ever_married, household.status_states_marriage, household.no, param:household.no, person.age55_at_year_end_if_open_year, person.age55_open_year, person.age55_at_year_end, person.no, param:age.cut_55; the mutant reads f8889.self_family_months.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.testing_failed_figured.no.then1` (replace an operand, f8889.f8889.testing_failed_figured): testing_failed_figured's alternative for testing_if_asked false is f8889.no (the parameter hsa.no, false); the mutant reads testing_prior_if_asked. testing_if_asked is any[ira_failed true, testing_prior_if_asked true], a known false only where both disjuncts are known false, so where the false alternative is taken testing_prior_if_asked is false, f8889.no's value. Nothing testing_if_asked reads has a refusal gate (ira_failed, testing_prior_if_asked, ask_last_month_prior, ask_testing, not_covered_12 and the coverage lines beneath them read only inputs and parameters with no refusal gates), so it is never a refusal; where it is unknown both alternatives are ways (spec 4.7.3), neither route's ways (not_covered_12 with f8889.no, or with testing_prior_if_asked) refuse, and testing_failed_figured is that unknown on both routes. (Premises pinned: f8889.testing_failed_figured, f8889.testing_if_asked, f8889.not_covered_12, f8889.ira_failed, f8889.testing_prior_if_asked, f8889.covered_12, f8889.no, f8889.yes, f8889.ira_gap_if_prior, f8889.ask_last_month_prior, f8889.testing_prior, f8889.coverage, f8889.all_year, f8889.ira_prior_if_asked, f8889.ira_gap, f8889.ask_testing, f8889.coverage_year, f8889.coverage_self, f8889.coverage_family, f8889.cov_changed, f8889.months_eligible, f8889.ira_prior, f8889.any, f8889.eligible_all, f8889.coverage_self_spouse, f8889.cov_family, f8889.line2, sales.zero, f8889.line9, f8889.clear_if_uniform, f8889.no_fsa, f8889.spouse_family_if_asked, f8889.cov_self_only, f8889.clear_all_year, f8889.fsa_if_clear, f8889.ask_spouse_family, f8889.year_self_answered, f8889.spouse_family, f8889.fsa, f8889.sf_eligible, f8889.sf_married, household.married, household.marriage_possible, household.married_dec31, household.no, f1040.status, household.ever_married, household.status_states_marriage, param:hsa.no, param:hsa.yes, param:hsa.cov_changed, param:hsa.cov_family, param:sales.zero, param:hsa.cov_self_only, param:household.no; the mutant reads f8889.testing_prior_if_asked.) (structural conditions re-checked this run.)
- `operand.f8889.f8889.line16_figured.line15` (replace an operand, f8889.f8889.line16_figured): Guarded figure: f8889.line15 is f8889.line15_dist wherever f8889.has_dist holds, and every printed line reads f8889.line16_figured (a helper) only through choices whose guards make f8889.has_dist true, which, where a guard is unknown, are that unknown whatever f8889.line16_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where f8889.has_dist does not hold only f8889.line16_figured's own, unprinted value can differ.
- `operand.f8889.f8889.line16.zero.then1` (replace an operand, f8889.f8889.line16): Branch settled by its guard: where f8889.line16 takes alternative 1 (guard {
  "eq": [
    "f8889.has_dist",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that f8889.zero and f8889.line15 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.f8889.f8889.subject.line16.then0` (replace an operand, f8889.f8889.subject): f8889.subject is read only by line17b_figured, which only line17b reads, and only in its has_taxable alternative; has_taxable is line16 more than $0 (sales.zero), so where subject is read line16 is complete and positive, which only line16's has_dist alternative gives (the other is f8889.zero, $0), and that alternative's value is line16_figured. Where has_taxable is false or refused, subject is not read; where it is unknown, line17b evaluates line17b_figured as a way (spec 4.7.3), but line17b's other alternative is f8889.zero, which never refuses, so line17b is that unknown on both routes. (Premises pinned: f8889.subject, f8889.line17b_figured, f8889.line17b, f8889.has_taxable, f8889.line16, f8889.line16_figured, f8889.has_dist, f8889.zero, param:sales.zero; the mutant reads f8889.line16_figured.) (structural conditions re-checked this run.)
- `operand.f8959.f8959.line23.zero` (replace an operand, f8959.f8959.line23): Copy-chain identity: f8959.zero and f8959.rrta_comp expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.total_tax.rrta_tax` (replace an operand, f8959.f8959.total_tax): Line 17 is 0.9% of line 16, and line 16 is line 14 less line 15 floored at zero, where line 14 is $0 behind its refusal gate and line 15 is not negative; so line 16 and line 17 are both $0, and when line 14 refuses or is unknown both carry its value (line 16 reads line 14 first, and the rate passes it through). (structural conditions re-checked this run.)
- `operand.f8960.f8960.line4b.zero` (replace an operand, f8960.f8960.line4b): Copy-chain identity: f8960.zero and f8960.line3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line5b.zero` (replace an operand, f8960.f8960.line5b): Copy-chain identity: f8960.zero and f8960.line4b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line6.zero` (replace an operand, f8960.f8960.line6): Copy-chain identity: f8960.zero and f8960.line5c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line7.zero` (replace an operand, f8960.f8960.line7): Copy-chain identity: f8960.zero and f8960.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
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
- `operand.f8962.f8962.marriage.no.then1` (replace an operand, f8962.f8962.marriage): marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for single. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates. (Premises pinned: f8962.marriage, f8962.alloc, f8962.line9, f8962.line24, f8962.line25, f8962.no, f1040.status, param:household.no; the mutant reads f8962.alloc.) (structural conditions re-checked this run.)
- `operand.f8962.f8962.marriage.no.then2` (replace an operand, f8962.f8962.marriage): marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for mfs. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates. (Premises pinned: f8962.marriage, f8962.alloc, f8962.line9, f8962.line24, f8962.line25, f8962.no, f1040.status, param:household.no; the mutant reads f8962.alloc.) (structural conditions re-checked this run.)
- `operand.f8962.f8962.marriage.no.then3` (replace an operand, f8962.f8962.marriage): marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for hoh. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates. (Premises pinned: f8962.marriage, f8962.alloc, f8962.line9, f8962.line24, f8962.line25, f8962.no, f1040.status, param:household.no; the mutant reads f8962.alloc.) (structural conditions re-checked this run.)
- `operand.f8962.f8962.marriage.no.then4` (replace an operand, f8962.f8962.marriage): marriage is a choice on the filing status: mfj takes the input married_this_year and every other status takes f8962.no (the parameter household.no, false); the mutant reads alloc in place of f8962.no for qss. marriage is read by line9, any[alloc, marriage], and by line24 and line25, in each as the third refusal gate, after alloc (the second). In line9 the second disjunct is reached only where alloc is false or unknown (a true one ends the test, a refused one refuses it): with alloc false the mutant reads false, the value of f8962.no; with alloc unknown the base's second disjunct is false and the mutant's unknown, and the any-test returns the unknown it met first, alloc's, on both routes. In line24 and line25 gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so marriage is read only where alloc is a memoized false in the frame (spec 4.7.6), the value of f8962.no. Where the status is unknown every alternative is a way (spec 4.7.3) and the other non-joint alternatives take f8962.no, which never refuses, so marriage is the status's unknown on both routes. The status is an input with no refusal gates. (Premises pinned: f8962.marriage, f8962.alloc, f8962.line9, f8962.line24, f8962.line25, f8962.no, f1040.status, param:household.no; the mutant reads f8962.alloc.) (structural conditions re-checked this run.)
- `operand.f8962.f8962.filing.applicable.all.1.any.0.eq.0` (replace an operand, f8962.f8962.filing): filing is all[any, any[applicable, aptc]]; the mutant reads show_applicable, all[any, applicable], in place of applicable. The inner any-test is reached only when f8962.any is true or unknown. With any true, show_applicable is applicable's (memoized) value. f8962.any is forms > 0, and forms counts the Form 1095-A roster with a parameter field, so any is unknown only when that roster is unconfirmed; then aptc (aptc_total, a sum over the same roster) is unknown, never a refusal (spec 4.7.5: an unconfirmed roster evaluates nothing), and show_applicable differs from applicable only by a true turned unknown, which the outer all-test, already holding any's unknown, cannot see: both are unknown, or the same refusal of applicable. (Premises pinned: f8962.filing, f8962.show_applicable, f8962.applicable, f8962.any, f8962.forms, f8962.aptc, f8962.aptc_total, f1095a.one, param:sales.one; the mutant reads f8962.show_applicable.) (structural conditions re-checked this run.)
- `operand.f8962.f8962.alien_branch.no.then1` (replace an operand, f8962.f8962.alien_branch): alien_branch is a choice on f8962.any: true takes alien_not_barred, false takes f8962.no (the parameter household.no, false); the mutant reads filing in place of f8962.no. filing is all[any, any[applicable, aptc]], so wherever f8962.any is a known false filing is false at its first conjunct (spec 4.7.2), the value of f8962.no. f8962.any is forms > 0, and forms counts the Form 1095-A roster with a parameter field and no filter, so any is never a refusal and is unknown only when that roster is unconfirmed. alien_branch is read only by line24 and line25, in each as the seventh refusal gate, after void_form (the sixth); gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1). void_form is void_forms > 0, a count over the same roster, which is unknown with no lower bound when the roster is unconfirmed (spec 4.7.5: an unconfirmed roster evaluates nothing). So alien_branch is read only where the roster is confirmed and f8962.any is known, and there the two routes agree. alien_branch's own value does differ where nothing reads it: with the roster unconfirmed and line 5 a refusal, filing refuses and alien_not_barred can (through alien_from_income), so every way of the mutant can refuse (spec 4.7.3) and it can be that refusal where the base is the unknown of f8962.any. A reader that reached alien_branch with the roster unconfirmed (anywhere but behind void_form or another line unknown on an unconfirmed roster) would see that difference; alien_branch, line24 and line25 are premises, so a new reader of alien_branch, or a change to the gate lists of line24 or line25, lapses this argument. (Premises pinned: f8962.alien_branch, f8962.line24, f8962.line25, f8962.void_form, f8962.void_forms, f8962.any, f8962.forms, f8962.filing, f8962.no, f1095a.one, param:sales.one, param:household.no; the mutant reads f8962.filing.) (structural conditions re-checked this run.)
- `operand.f8995.f8995.line9.line8` (replace an operand, f8995.f8995.line9): Copy-chain identity: f8995.line8 and f8995.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8995a.f8995a.line31.line30` (replace an operand, f8995a.f8995a.line31): Copy-chain identity: f8995a.line30 and f8995a.line28 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ftc.ftc.elect_if_tax.no.then1` (replace an operand, ftc.ftc.elect_if_tax): Branch settled by its guard: where ftc.elect_if_tax takes alternative 1 (guard {
  "eq": [
    "ftc.has_tax",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that ftc.no and ftc.eligible_if_tax make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither ftc.no nor ftc.eligible_if_tax ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.household.household.cp_spouse_or_retirement.spouse_cp_domicile_if_asked.then0` (replace an operand, household.household.cp_spouse_or_retirement): Branch equal under a case split: where household.cp_spouse_or_retirement takes alternative 0 (guard {
  "eq": [
    "household.spouse_cp_domicile_if_asked",
    {
      "const": true
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "household.community_property",
    {
      "const": false
    }
  ],
  "op": "test"
}
 on its one reader path), household.spouse_cp_domicile_if_asked and household.ask_spouse_cp_domicile have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.household.household.hoh_community_property.no.then1` (replace an operand, household.household.hoh_community_property): hoh_community_property is a choice on the filing status: hoh takes hoh_cp_married and every other status takes household.no (the parameter household.no, false); the mutant reads household.cp_any in place of household.no for mfj. hoh_community_property is read only by hoh_eligible, as its second refusal gate, and hoh_eligible only by hoh_fails, all[status hoh, hoh_eligible false], whose first conjunct is false wherever the status is mfj (an all-test stops at a false conjunct), so hoh_eligible is not read there and the mutated alternative changes no line that reads it. Where the status is unknown every alternative is a way (spec 4.7.3): the other alternatives that take household.no never refuse, so hoh_community_property is the status's unknown on both routes whatever household.cp_any is; where the status is hoh both routes take hoh_cp_married. The status is an input with no refusal gates. (Premises pinned: household.hoh_community_property, household.hoh_eligible, household.hoh_fails, household.hoh_cp_married, household.cp_any, household.no, f1040.status, param:household.no; the mutant reads household.cp_any.) (structural conditions re-checked this run.)
- `operand.household.household.hoh_community_property.no.then2` (replace an operand, household.household.hoh_community_property): hoh_community_property is a choice on the filing status: hoh takes hoh_cp_married and every other status takes household.no (the parameter household.no, false); the mutant reads household.cp_any in place of household.no for mfs. hoh_community_property is read only by hoh_eligible, as its second refusal gate, and hoh_eligible only by hoh_fails, all[status hoh, hoh_eligible false], whose first conjunct is false wherever the status is mfs (an all-test stops at a false conjunct), so hoh_eligible is not read there and the mutated alternative changes no line that reads it. Where the status is unknown every alternative is a way (spec 4.7.3): the other alternatives that take household.no never refuse, so hoh_community_property is the status's unknown on both routes whatever household.cp_any is; where the status is hoh both routes take hoh_cp_married. The status is an input with no refusal gates. (Premises pinned: household.hoh_community_property, household.hoh_eligible, household.hoh_fails, household.hoh_cp_married, household.cp_any, household.no, f1040.status, param:household.no; the mutant reads household.cp_any.) (structural conditions re-checked this run.)
- `operand.household.household.hoh_community_property.no.then4` (replace an operand, household.household.hoh_community_property): hoh_community_property is a choice on the filing status: hoh takes hoh_cp_married and every other status takes household.no (the parameter household.no, false); the mutant reads household.cp_any in place of household.no for qss. hoh_community_property is read only by hoh_eligible, as its second refusal gate, and hoh_eligible only by hoh_fails, all[status hoh, hoh_eligible false], whose first conjunct is false wherever the status is qss (an all-test stops at a false conjunct), so hoh_eligible is not read there and the mutated alternative changes no line that reads it. Where the status is unknown every alternative is a way (spec 4.7.3): the other alternatives that take household.no never refuse, so hoh_community_property is the status's unknown on both routes whatever household.cp_any is; where the status is hoh both routes take hoh_cp_married. The status is an input with no refusal gates. (Premises pinned: household.hoh_community_property, household.hoh_eligible, household.hoh_fails, household.hoh_cp_married, household.cp_any, household.no, f1040.status, param:household.no; the mutant reads household.cp_any.) (structural conditions re-checked this run.)
- `operand.household.household.hoh_missed_test2.no.then1` (replace an operand, household.household.hoh_missed_test2): hoh_missed_test2 is a choice on household.dependents_any: true takes hoh_missed_cost, false takes household.no (the parameter household.no, false); the mutant reads hoh_missed_person in place of household.no. dependents_any is dependents_listed more than 0, and dependents_listed sums dependent.one (the parameter dependent.one, 1) over the dependent roster with no filter, so dependents_any is a known false only where the roster is known to be empty. There test2_lived_persons and test2_absence_persons, sums of dependent.one over the same empty roster, are both 0, and hoh_missed_person (test2_lived_persons more than test2_absence_persons) is false, household.no's value. dependents_listed reads only the roster and a parameter and has no refusal gate, so dependents_any is never a refusal. Where it is unknown (the roster not given) both alternatives are ways (spec 4.7.3), and a choose is a refusal only when every way is: household.no never refuses, and hoh_missed_person, two sums over a roster not given, is an unknown and no refusal, so on both routes hoh_missed_test2 is dependents_any's unknown, unchanged. So hoh_missed_test2 has the same value on both routes wherever it is evaluated, and its readers, the gate hoh_missed and hoh_missed_mfs_test2 (a choice on it), receive that value on both. (Premises pinned: household.hoh_missed_test2, household.hoh_missed, household.hoh_missed_mfs_test2, household.dependents_any, household.dependents_listed, dependent.one, param:dependent.one, household.hoh_missed_cost, household.hoh_missed_person, household.test2_lived_persons, household.test2_absence_persons, household.no, param:household.no; the mutant reads household.hoh_missed_person.) (structural conditions re-checked this run.)
- `operand.household.household.hoh_missed_mfs.no.then1` (replace an operand, household.household.hoh_missed_mfs): hoh_missed_mfs is a choice on household.mfs (the filing status equal to mfs; the status is an input with no refusal gates, so mfs is never a refusal): true takes hoh_missed_mfs_listed, false takes household.no (the parameter household.no, false); the mutant reads household.hoh_missed in place of household.no. hoh_missed_mfs is read only by household.hoh_fails, as the second of its two refusal gates; the first is hoh_missed. A line's gates are evaluated at entry in order, and a gate that is true, a refusal or unknown ends them (spec 4.7.1), so hoh_missed_mfs is evaluated only where hoh_missed is a known false, memoized in the same frame (spec 4.7.6): with mfs false the mutant's alternative is false, the value of household.no. A refused guard ends the choose with its refusal on both routes. Where mfs is unknown both alternatives are ways (spec 4.7.3); neither household.no nor hoh_missed (a known false) refuses, so hoh_missed_mfs is that unknown on both routes. The interview's reach pass also evaluates the gates after an unanswered first gate, but only a later gate that is true or a refusal changes what it does; there hoh_missed is unknown, so the base's false and the mutant's alternative (hoh_missed's unknown, or with mfs unknown hoh_missed_mfs's unknown on both routes) are neither, and no new input is read (hoh_missed is memoized). (Premises pinned: household.hoh_missed_mfs, household.hoh_fails, household.hoh_missed, household.mfs, f1040.status, household.no, param:household.no; the mutant reads household.hoh_missed.) (structural conditions re-checked this run.)
- `operand.household.household.qss_no_child_notice.qss_no_child.then0` (replace an operand, household.household.qss_no_child_notice): Unreachable alternative: household.qss_no_child_notice is a helper that every printed line reads only through choices whose guards make household.ask_spouse_cp_domicile true, and household.ask_spouse_cp_domicile true makes the guard of alternative 0 ({
  "eq": [
    "household.qss_claimed",
    {
      "const": true
    }
  ],
  "op": "test"
}
) false; where household.qss_no_child_notice's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither household.qss_no_child nor household.qss ever refuses; spec 4.7.3); so wherever a printed value depends on household.qss_no_child_notice that alternative is not taken, and replacing its value changes no printed value.
- `operand.household.household.qss_no_child_notice.no.then1` (replace an operand, household.household.qss_no_child_notice): Unreachable alternative: household.qss_no_child_notice is a helper that every printed line reads only through choices whose guards make household.qss_claimed true, and household.qss_claimed true makes the guard of alternative 1 ({
  "eq": [
    "household.qss_claimed",
    {
      "const": false
    }
  ],
  "op": "test"
}
) false; where household.qss_no_child_notice's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither household.no nor household.qss ever refuses; spec 4.7.3); so wherever a printed value depends on household.qss_no_child_notice that alternative is not taken, and replacing its value changes no printed value.
- `operand.household.household.mfs_community_property.no.then0` (replace an operand, household.household.mfs_community_property): Branch equal under a case split: where household.mfs_community_property takes alternative 0 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "single"
    }
  ],
  "op": "test"
}
), household.no and household.mfs_apart_last6 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.household.household.mfs_community_property.no.then1` (replace an operand, household.household.mfs_community_property): Branch equal under a case split: where household.mfs_community_property takes alternative 1 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "mfj"
    }
  ],
  "op": "test"
}
), household.no and household.mfs_apart_last6 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.household.household.mfs_community_property.no.then3` (replace an operand, household.household.mfs_community_property): Branch equal under a case split: where household.mfs_community_property takes alternative 3 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "hoh"
    }
  ],
  "op": "test"
}
), household.no and household.mfs_apart_last6 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.household.household.mfs_community_property.no.then4` (replace an operand, household.household.mfs_community_property): Branch equal under a case split: where household.mfs_community_property takes alternative 4 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "qss"
    }
  ],
  "op": "test"
}
), household.no and household.mfs_apart_last6 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
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
- `operand.ira.ira.roth_reduced.roth_magi.any.0.all.1.ge.0` (replace an operand, ira.ira.roth_reduced): Copy-chain identity: ira.roth_magi and ira.line5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ira.ira.roth_reduced.roth_magi.any.1.all.1.ge.0` (replace an operand, ira.ira.roth_reduced): Copy-chain identity: ira.roth_magi and ira.line5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ira.ira.roth_reduced.roth_magi.any.2.all.2.gt.0` (replace an operand, ira.ira.roth_reduced): Copy-chain identity: ira.roth_magi and ira.line5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ira.ira.combat_gate.no.then1` (replace an operand, ira.ira.combat_gate): Branch equal under a case split: where ira.combat_gate takes alternative 1 (guard {
  "eq": [
    "ira.any_trad",
    {
      "const": false
    }
  ],
  "op": "test"
}
), ira.no and ira.special_gate have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.k1p.k1p.active.decisions_if_asked.all.0.eq.0` (replace an operand, k1p.k1p.active): k1p.active is all[k1p.decisions_if_asked = true, k1p.tenth_if_decisions = true]; the mutant tests k1p.ask_active in place of decisions_if_asked. decisions_if_asked is a choice on ask_active (true: the input k1p.decisions; false: k1p.no, the parameter household.no, false), and tenth_if_decisions is a choice on decisions_if_asked (true: the input k1p.tenth; false: k1p.no). Where decisions_if_asked is true, ask_active is true, so both conjunctions are tenth_if_decisions's value. Where it is false (ask_active false, or decisions answered No), tenth_if_decisions is false and both are false. Where it is unknown, either ask_active is that unknown (has_b2 or general unanswered) and the mutant's first conjunct is the same unknown, or ask_active is true and decisions is unanswered, and in both cases tenth_if_decisions is the unknown of its guard (its other way, k1p.no, never refuses, spec 4.7.3), so both conjunctions are unknown with no conjunct false. None of these lines carries a refusal gate. (Premises pinned: k1p.active, k1p.decisions_if_asked, k1p.tenth_if_decisions, k1p.ask_active, k1p.decisions, k1p.tenth, k1p.no, param:household.no, k1p.has_b2, k1p.general; the mutant reads k1p.ask_active.) (structural conditions re-checked this run.)
- `operand.k1p.k1p.b1_neg.zero` (replace an operand, k1p.k1p.b1_neg): k1p.b1_neg is subtract_floor0 from k1p.zero take k1p.box1_if_any, max(0, 0 - B) where B is k1p.box1_if_any; the mutant takes k1p.b1_pos for k1p.zero, and k1p.b1_pos is subtract_floor0 from k1p.box1_if_any take k1p.zero, max(B, 0), with k1p.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1p.box1_if_any nor k1p.b1_pos carries a refusal gate and k1p.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1p.b1_pos passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1p.b1_neg, k1p.b1_pos, k1p.box1_if_any, k1p.zero, param:sales.zero; the mutant reads k1p.b1_pos.) (structural conditions re-checked this run.)
- `operand.k1p.k1p.b2_neg.zero` (replace an operand, k1p.k1p.b2_neg): k1p.b2_neg is subtract_floor0 from k1p.zero take k1p.box2_if_any, max(0, 0 - B) where B is k1p.box2_if_any; the mutant takes k1p.b2_pos for k1p.zero, and k1p.b2_pos is subtract_floor0 from k1p.box2_if_any take k1p.zero, max(B, 0), with k1p.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1p.box2_if_any nor k1p.b2_pos carries a refusal gate and k1p.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1p.b2_pos passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1p.b2_neg, k1p.b2_pos, k1p.box2_if_any, k1p.zero, param:sales.zero; the mutant reads k1p.b2_pos.) (structural conditions re-checked this run.)
- `operand.k1p.k1p.b3_neg.zero` (replace an operand, k1p.k1p.b3_neg): k1p.b3_neg is subtract_floor0 from k1p.zero take k1p.box3_if_any, max(0, 0 - B) where B is k1p.box3_if_any; the mutant takes k1p.b3_pos for k1p.zero, and k1p.b3_pos is subtract_floor0 from k1p.box3_if_any take k1p.zero, max(B, 0), with k1p.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1p.box3_if_any nor k1p.b3_pos carries a refusal gate and k1p.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1p.b3_pos passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1p.b3_neg, k1p.b3_pos, k1p.box3_if_any, k1p.zero, param:sales.zero; the mutant reads k1p.b3_pos.) (structural conditions re-checked this run.)
- `operand.k1p.k1p.b1_net_loss.zero.then1` (replace an operand, k1p.k1p.b1_net_loss): Branch settled by its guard: where k1p.b1_net_loss takes alternative 1 (guard {
  "eq": [
    "k1p.b1_passive",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1p.zero and k1p.b1_net_income make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1p.zero nor k1p.b1_net_income ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1p.k1p.p4_loss.zero.then1` (replace an operand, k1p.k1p.p4_loss): Branch settled by its guard: where k1p.p4_loss takes alternative 1 (guard {
  "eq": [
    "k1p.active",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1p.zero and k1p.p4_income make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1p.zero nor k1p.p4_income ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1p.k1p.p4_prior.zero.then1` (replace an operand, k1p.k1p.p4_prior): Branch settled by its guard: where k1p.p4_prior takes alternative 1 (guard {
  "eq": [
    "k1p.active",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1p.zero and k1p.p4_loss make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1p.zero nor k1p.p4_loss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1p.k1p.p6_loss.zero.then1` (replace an operand, k1p.k1p.p6_loss): Branch settled by its guard: where k1p.p6_loss takes alternative 1 (guard {
  "eq": [
    "k1p.active",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1p.zero and k1p.p4_prior make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1p.zero nor k1p.p4_prior ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1p.k1p.p5_b2_loss.zero.then0` (replace an operand, k1p.k1p.p5_b2_loss): Branch settled by its guard: where k1p.p5_b2_loss takes alternative 0 (guard {
  "eq": [
    "k1p.active",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1p.zero and k1p.p5_b2_income make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1p.zero nor k1p.p5_b2_income ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1p.k1p.p5_b2_prior.zero.then0` (replace an operand, k1p.k1p.p5_b2_prior): Branch settled by its guard: where k1p.p5_b2_prior takes alternative 0 (guard {
  "eq": [
    "k1p.active",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1p.zero and k1p.p5_b2_loss make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1p.zero nor k1p.p5_b2_loss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1p.k1p.se_pos.zero` (replace an operand, k1p.k1p.se_pos): Guarded figure: k1p.col_i is k1p.zero wherever k1p.b1_passive holds, and every printed line reads k1p.se_pos (a helper) only through choices whose guards make k1p.b1_passive true, which, where a guard is unknown, are that unknown whatever k1p.se_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where k1p.b1_passive does not hold only k1p.se_pos's own, unprinted value can differ.
- `operand.k1s.k1s.ask_prior_active.tenth_if_active.all.1.eq.0` (replace an operand, k1s.k1s.ask_prior_active): k1s.ask_prior_active is all[k1s.b2_prior_if_any > 0, k1s.tenth_if_active = true]; the mutant tests k1s.part4 in place of k1s.tenth_if_active. k1s.part4 is all[k1s.active_if_b2 = true, k1s.tenth_if_active = true], and k1s.tenth_if_active is a choice on k1s.active_if_b2 (true: the input k1s.tenth; false: k1s.no, the parameter s3.no, false). Where active_if_b2 is true, part4 is the test of tenth_if_active, so the two are the same value (true, false or the unknown of an unanswered k1s.tenth). Where it is false, tenth_if_active is false and part4 is false. Where it is unknown (k1s.box2_any or k1s.active unanswered), tenth_if_active is the unknown of its guard, since its other way, k1s.no, never refuses (spec 4.7.3), and part4 is unknown with no conjunct false. Where it is a refusal, tenth_if_active and part4 are that refusal. So part4 and tenth_if_active have the same value on every input and both conjunctions agree. None of these lines carries a refusal gate. (Premises pinned: k1s.ask_prior_active, k1s.part4, k1s.tenth_if_active, k1s.active_if_b2, k1s.tenth, k1s.no, param:s3.no, k1s.box2_any, k1s.active; the mutant reads k1s.part4.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.loss1.zero` (replace an operand, k1s.k1s.loss1): k1s.loss1 is subtract_floor0 from k1s.zero take k1s.box1_if_any, max(0, 0 - B) where B is k1s.box1_if_any; the mutant takes k1s.gain1 for k1s.zero, and k1s.gain1 is subtract_floor0 from k1s.box1_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box1_if_any nor k1s.gain1 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain1 passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1s.loss1, k1s.gain1, k1s.box1_if_any, k1s.zero, param:sales.zero; the mutant reads k1s.gain1.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.loss2.zero` (replace an operand, k1s.k1s.loss2): k1s.loss2 is subtract_floor0 from k1s.zero take k1s.box2_if_any, max(0, 0 - B) where B is k1s.box2_if_any; the mutant takes k1s.gain2 for k1s.zero, and k1s.gain2 is subtract_floor0 from k1s.box2_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box2_if_any nor k1s.gain2 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain2 passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1s.loss2, k1s.gain2, k1s.box2_if_any, k1s.zero, param:sales.zero; the mutant reads k1s.gain2.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.loss3.zero` (replace an operand, k1s.k1s.loss3): k1s.loss3 is subtract_floor0 from k1s.zero take k1s.box3_if_any, max(0, 0 - B) where B is k1s.box3_if_any; the mutant takes k1s.gain3 for k1s.zero, and k1s.gain3 is subtract_floor0 from k1s.box3_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box3_if_any nor k1s.gain3 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain3 passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1s.loss3, k1s.gain3, k1s.box3_if_any, k1s.zero, param:sales.zero; the mutant reads k1s.gain3.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.loss7.zero` (replace an operand, k1s.k1s.loss7): k1s.loss7 is subtract_floor0 from k1s.zero take k1s.box7_if_any, max(0, 0 - B) where B is k1s.box7_if_any; the mutant takes k1s.gain7 for k1s.zero, and k1s.gain7 is subtract_floor0 from k1s.box7_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box7_if_any nor k1s.gain7 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain7 passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1s.loss7, k1s.gain7, k1s.box7_if_any, k1s.zero, param:sales.zero; the mutant reads k1s.gain7.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.loss8.zero` (replace an operand, k1s.k1s.loss8): k1s.loss8 is subtract_floor0 from k1s.zero take k1s.box8a_if_any, max(0, 0 - B) where B is k1s.box8a_if_any; the mutant takes k1s.gain8 for k1s.zero, and k1s.gain8 is subtract_floor0 from k1s.box8a_if_any take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.box8a_if_any nor k1s.gain8 carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.gain8 passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1s.loss8, k1s.gain8, k1s.box8a_if_any, k1s.zero, param:sales.zero; the mutant reads k1s.gain8.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.np_loss.zero` (replace an operand, k1s.k1s.np_loss): k1s.np_loss is subtract_floor0 from k1s.zero take k1s.b1_np, max(0, 0 - B) where B is k1s.b1_np; the mutant takes k1s.np_income for k1s.zero, and k1s.np_income is subtract_floor0 from k1s.b1_np take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Neither k1s.b1_np nor k1s.np_income carries a refusal gate and k1s.zero is a parameter, so neither route can refuse; where B is unknown both routes are that unknown (k1s.np_income passes it on and the first unknown operand wins, spec 4.7.4). (Premises pinned: k1s.np_loss, k1s.np_income, k1s.b1_np, k1s.zero, param:sales.zero; the mutant reads k1s.np_income.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.p1_income.zero` (replace an operand, k1s.k1s.p1_income): k1s.p1_income is subtract_floor0 from k1s.b1_passive take k1s.zero (the parameter sales.zero, $0); the mutant takes k1s.col_i, a choice on k1s.ok (true: k1s.np_loss; false: k1s.zero). b1_passive and k1s.b1_np are complementary choices on k1s.material (b1_passive takes k1s.b1_net where material is false and k1s.zero where it is true; b1_np takes b1_net where material is true and zero where it is false), and np_loss is subtract_floor0 from zero take b1_np. Where ok is true: material false makes b1_np $0, so col_i is $0 and the routes agree; material true makes b1_passive $0, and max(0, 0 - col_i) = 0 = max(0, 0 - 0) since col_i is never negative; material unknown makes b1_passive that unknown, the first operand on both routes. Where ok is false col_i is zero and the routes agree. Where ok is a refusal or unknown the two p1_income values can differ, but p1_income is read only by k1s.passive_income and k1s.p5_income_raw, which are read only by k1s.col_h and k1s.p5_income, choices on ok (true: those lines; false: k1s.zero): a refusing guard ends each choice with ok's refusal, and an unknown guard leaves each the unknown of ok, since the other way, zero, never refuses (spec 4.7.3). So every reader agrees. (Premises pinned: k1s.p1_income, k1s.col_i, k1s.b1_passive, k1s.np_loss, k1s.b1_np, k1s.material, k1s.zero, param:sales.zero, k1s.ok, k1s.passive_income, k1s.col_h, k1s.p5_income_raw, k1s.p5_income; the mutant reads k1s.col_i.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.p1_loss.zero` (replace an operand, k1s.k1s.p1_loss): k1s.p1_loss is subtract_floor0 from k1s.zero take k1s.b1_passive, max(0, 0 - B) where B is k1s.b1_passive; the mutant takes k1s.p1_income for k1s.zero, and k1s.p1_income is subtract_floor0 from k1s.b1_passive take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Where B is a refusal or unknown, k1s.p1_income is that same refusal or unknown and is the first operand that is not known on the mutant's route, while B is the only such operand on the data's, so both routes carry B's own refusal or unknown (spec 4.7.4); k1s.p1_income and k1s.zero carry no refusal gate of their own. (Premises pinned: k1s.p1_loss, k1s.p1_income, k1s.b1_passive, k1s.zero, param:sales.zero; the mutant reads k1s.p1_income.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.p2_loss.zero` (replace an operand, k1s.k1s.p2_loss): k1s.p2_loss is subtract_floor0 from k1s.zero take k1s.b2_net, max(0, 0 - B) where B is k1s.b2_net; the mutant takes k1s.p2_income for k1s.zero, and k1s.p2_income is subtract_floor0 from k1s.b2_net take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Where B is a refusal or unknown, k1s.p2_income is that same refusal or unknown and is the first operand that is not known on the mutant's route, while B is the only such operand on the data's, so both routes carry B's own refusal or unknown (spec 4.7.4); k1s.p2_income and k1s.zero carry no refusal gate of their own. (Premises pinned: k1s.p2_loss, k1s.p2_income, k1s.b2_net, k1s.zero, param:sales.zero; the mutant reads k1s.p2_income.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.p3_loss.zero` (replace an operand, k1s.k1s.p3_loss): k1s.p3_loss is subtract_floor0 from k1s.zero take k1s.b3_net, max(0, 0 - B) where B is k1s.b3_net; the mutant takes k1s.p3_income for k1s.zero, and k1s.p3_income is subtract_floor0 from k1s.b3_net take k1s.zero, max(B, 0), with k1s.zero the parameter sales.zero ($0). max(B, 0) - B is max(0, -B), never negative, so max(0, max(B, 0) - B) = max(0, -B) for every amount B: the two values agree. Where B is a refusal or unknown, k1s.p3_income is that same refusal or unknown and is the first operand that is not known on the mutant's route, while B is the only such operand on the data's, so both routes carry B's own refusal or unknown (spec 4.7.4); k1s.p3_income and k1s.zero carry no refusal gate of their own. (Premises pinned: k1s.p3_loss, k1s.p3_income, k1s.b3_net, k1s.zero, param:sales.zero; the mutant reads k1s.p3_income.) (structural conditions re-checked this run.)
- `operand.k1s.k1s.p4_loss_raw.zero.then1` (replace an operand, k1s.k1s.p4_loss_raw): Branch settled by its guard: where k1s.p4_loss_raw takes alternative 1 (guard {
  "eq": [
    "k1s.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p4_income_raw make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1s.zero nor k1s.p4_income_raw ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p4_prior_raw.zero.then1` (replace an operand, k1s.k1s.p4_prior_raw): Branch settled by its guard: where k1s.p4_prior_raw takes alternative 1 (guard {
  "eq": [
    "k1s.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p4_loss_raw make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1s.zero nor k1s.p4_loss_raw ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p5_b2_loss.zero.then1` (replace an operand, k1s.k1s.p5_b2_loss): Branch settled by its guard: where k1s.p5_b2_loss takes alternative 1 (guard {
  "eq": [
    "k1s.part4",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p5_b2_income make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1s.zero nor k1s.p5_b2_income ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p5_b2_prior.b2_prior_if_any.then0` (replace an operand, k1s.k1s.p5_b2_prior): Unreachable alternative: k1s.p5_b2_prior is a helper that every printed line reads only through choices whose guards make k1s.tenth_if_active true, and k1s.tenth_if_active true makes the guard of alternative 0 ({
  "eq": [
    "k1s.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
) false; where k1s.p5_b2_prior's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither k1s.b2_prior_if_any nor k1s.p5_b2_loss ever refuses; spec 4.7.3); so wherever a printed value depends on k1s.p5_b2_prior that alternative is not taken, and replacing its value changes no printed value.
- `operand.k1s.k1s.p5_b2_prior.zero.then1` (replace an operand, k1s.k1s.p5_b2_prior): Branch settled by its guard: where k1s.p5_b2_prior takes alternative 1 (guard {
  "eq": [
    "k1s.part4",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p5_b2_loss make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither k1s.zero nor k1s.p5_b2_loss ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p4_income.zero.then1` (replace an operand, k1s.k1s.p4_income): Guarded figure: k1s.p5_b2_prior is k1s.zero wherever k1s.part4 holds, and every printed line reads k1s.p4_income (a helper) only through choices whose guards make k1s.part4 true, which, where a guard is unknown, are that unknown whatever k1s.p4_income is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where k1s.part4 does not hold only k1s.p4_income's own, unprinted value can differ.
- `operand.k1s.k1s.p4_loss.zero.then1` (replace an operand, k1s.k1s.p4_loss): Branch settled by its guard: where k1s.p4_loss takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p4_income make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p4_prior.zero.then1` (replace an operand, k1s.k1s.p4_prior): Branch settled by its guard: where k1s.p4_prior takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p4_loss make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p1_prior_passive.zero.then1` (replace an operand, k1s.k1s.p1_prior_passive): Unreachable alternative: k1s.p1_prior_passive is a helper that every printed line reads only through choices whose guards make k1s.other_ask true, and k1s.other_ask true makes the guard of alternative 1 ({
  "eq": [
    "k1s.material",
    {
      "const": true
    }
  ],
  "op": "test"
}
) false; where k1s.p1_prior_passive's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither k1s.zero nor k1s.p5_loss_raw ever refuses; spec 4.7.3); so wherever a printed value depends on k1s.p1_prior_passive that alternative is not taken, and replacing its value changes no printed value.
- `operand.k1s.k1s.p5_loss.zero.then1` (replace an operand, k1s.k1s.p5_loss): Branch settled by its guard: where k1s.p5_loss takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p5_income make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.p5_prior.zero.then1` (replace an operand, k1s.k1s.p5_prior): Branch settled by its guard: where k1s.p5_prior takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p5_loss make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.int.zero.then1` (replace an operand, k1s.k1s.int): Branch settled by its guard: where k1s.int takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.p5_prior make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.ord_div.zero.then1` (replace an operand, k1s.k1s.ord_div): Branch settled by its guard: where k1s.ord_div takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.int make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.qual_div.zero.then1` (replace an operand, k1s.k1s.qual_div): Branch settled by its guard: where k1s.qual_div takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.ord_div make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.st.zero.then1` (replace an operand, k1s.k1s.st): Guarded figure: k1s.b1_passive is k1s.zero wherever k1s.material holds, and every printed line reads k1s.st (a helper) only through choices whose guards make k1s.material true, which, where a guard is unknown, are that unknown whatever k1s.st is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where k1s.material does not hold only k1s.st's own, unprinted value can differ.
- `operand.k1s.k1s.lt.zero.then1` (replace an operand, k1s.k1s.lt): Branch settled by its guard: where k1s.lt takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.st make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.g28.zero.then1` (replace an operand, k1s.k1s.g28): Branch settled by its guard: where k1s.g28 takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.lt make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.u1250.zero.then1` (replace an operand, k1s.k1s.u1250): Branch settled by its guard: where k1s.u1250 takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.qual_div make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.backup.zero.then1` (replace an operand, k1s.k1s.backup): Branch settled by its guard: where k1s.backup takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.u1250 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.taxexempt.zero.then1` (replace an operand, k1s.k1s.taxexempt): Branch settled by its guard: where k1s.taxexempt takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.backup make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.nonpassive.zero.then1` (replace an operand, k1s.k1s.nonpassive): Branch settled by its guard: where k1s.nonpassive takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.g28 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.k1s.k1s.qbi.zero.then1` (replace an operand, k1s.k1s.qbi): Branch settled by its guard: where k1s.qbi takes alternative 1 (guard {
  "eq": [
    "k1s.ok",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that k1s.zero and k1s.nonpassive make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.work_ssn_or_tin.tin.then0` (replace an operand, person.person.work_ssn_or_tin): Branch settled by its guard: where person.work_ssn_or_tin takes alternative 0 (guard {
  "eq": [
    "person.tin",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.tin and person.tin_or_itin_applied make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither person.tin nor person.tin_or_itin_applied ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.person.person.has_educator_expenses` (replace strict greater-than with inclusive, person.person.has_educator_expenses): has_educator_expenses is educator_expenses_if_educator more than $0, read only by educator_deduction, a choice on it (true: educator_eligible_amount; false: person.zero). The educator lines read only the inputs eligible_educator and educator_expenses and the parameters s1.educator_max ($300), ss.zero and sales.zero ($0), and none has a refusal gate, so no route refuses; educator_expenses_if_educator is a choice on eligible_educator (true: educator_expenses; false: person.zero), so it is known only where eligible_educator is (a choice past an unknown guard is that guard's unknown, spec 4.7.3). The inclusive test differs only where educator_expenses_if_educator is a known $0, so where eligible_educator is known: the base takes person.zero ($0); the mutant takes educator_eligible_amount, a choice on the same eligible_educator whose true alternative is educator_limited, the smaller of educator_expenses_if_educator ($0) and educator_max ($300), $0, and whose false alternative is person.zero, $0. educator_deduction is $0 on both routes. (Premises pinned: person.educator_deduction, person.has_educator_expenses, person.educator_eligible_amount, person.educator_expenses_if_educator, person.educator_limited, person.educator_max, person.eligible_educator, person.educator_expenses, person.zero, param:s1.educator_max, param:ss.zero, param:sales.zero.) (structural conditions re-checked this run.)
- `operand.person.person.has_educator_expenses.educator_expenses_if_educator.gt.0` (replace an operand, person.person.has_educator_expenses): has_educator_expenses is educator_expenses_if_educator more than $0, read only by educator_deduction, a choice on it (true: educator_eligible_amount; false: person.zero); the mutant tests educator_max ($300) more than $0, always true, so its educator_deduction is always educator_eligible_amount. The educator lines read only the inputs eligible_educator and educator_expenses and the parameters s1.educator_max ($300), ss.zero and sales.zero ($0), and none has a refusal gate, so no route refuses; educator_expenses_if_educator is a choice on eligible_educator (true: educator_expenses; false: person.zero), so it is known only where eligible_educator is (a choice past an unknown guard is that guard's unknown, spec 4.7.3). Where the base test is true both routes take educator_eligible_amount. Where it is false educator_expenses_if_educator is a known $0 and eligible_educator is known: the base takes person.zero ($0), and educator_eligible_amount is educator_limited, the smaller of $0 and $300, or person.zero, $0 either way. Where it is unknown, educator_expenses_if_educator is unknown and the base's educator_deduction is that unknown (no way refuses); on the mutant's route educator_eligible_amount is unknown too: with eligible_educator unknown it is that guard's unknown, and with eligible_educator true it is educator_limited, the smaller of an unknown and $300, unknown (spec 4.7.4). (Premises pinned: person.educator_deduction, person.has_educator_expenses, person.educator_eligible_amount, person.educator_expenses_if_educator, person.educator_limited, person.educator_max, person.eligible_educator, person.educator_expenses, person.zero, param:s1.educator_max, param:ss.zero, param:sales.zero; the mutant reads person.educator_max.) (structural conditions re-checked this run.)
- `operand.person.person.educator_eligible_amount.zero.then1` (replace an operand, person.person.educator_eligible_amount): educator_eligible_amount's eligible_educator-false alternative is person.zero; the mutant reads educator_max ($300). educator_eligible_amount is read only by educator_deduction, in its has_educator_expenses-true alternative. The educator lines read only the inputs eligible_educator and educator_expenses and the parameters s1.educator_max ($300), ss.zero and sales.zero ($0), and none has a refusal gate, so no route refuses; educator_expenses_if_educator is a choice on eligible_educator (true: educator_expenses; false: person.zero), so it is known only where eligible_educator is (a choice past an unknown guard is that guard's unknown, spec 4.7.3). With eligible_educator a known false (memoized, spec 4.7.6) educator_expenses_if_educator is person.zero, $0, so has_educator_expenses (educator_expenses_if_educator more than $0) is false and educator_deduction takes person.zero without reading educator_eligible_amount. The mutated alternative is otherwise a way only with eligible_educator unknown; educator_expenses_if_educator is then unknown, so has_educator_expenses is unknown and educator_deduction is that unknown on both routes, no way refusing. (Premises pinned: person.educator_deduction, person.has_educator_expenses, person.educator_eligible_amount, person.educator_expenses_if_educator, person.educator_limited, person.educator_max, person.eligible_educator, person.educator_expenses, person.zero, param:s1.educator_max, param:ss.zero, param:sales.zero; the mutant reads person.educator_max.) (structural conditions re-checked this run.)
- `operand.person.person.educator_deduction.educator_eligible_amount.then0` (replace an operand, person.person.educator_deduction): Branch equal under a case split: where person.educator_deduction takes alternative 0 (guard {
  "eq": [
    "person.has_educator_expenses",
    {
      "const": true
    }
  ],
  "op": "test"
}
), person.educator_eligible_amount and person.educator_limited have the same value in every case of person.eligible_educator (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged), through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
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
- `operand.person.person.f8919_ss8.no.then1` (replace an operand, person.person.f8919_ss8): Unreachable alternative: person.f8919_ss8 is a helper that every printed line reads only through choices whose guards make person.f8919_ss8 true, and person.f8919_ss8 true makes the guard of alternative 1 ({
  "eq": [
    "scope.contractor_pay_if_pay",
    {
      "const": false
    }
  ],
  "op": "test"
}
) false; where person.f8919_ss8's guards or its readers' are unknown, the choice is that unknown whatever the alternative's value (neither person.no nor person.f8919_any ever refuses; spec 4.7.3); so wherever a printed value depends on person.f8919_ss8 that alternative is not taken, and replacing its value changes no printed value.
- `operand.person.person.f8919_line10.zero.then1` (replace an operand, person.person.f8919_line10): Branch settled by its guard: where person.f8919_line10 takes alternative 1 (guard {
  "eq": [
    "person.f8919_any",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.f8919_wages make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither person.zero nor person.f8919_wages ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.f8919_tax.zero.then1` (replace an operand, person.person.f8919_tax): Branch settled by its guard: where person.f8919_tax takes alternative 1 (guard {
  "eq": [
    "person.f8919_any",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.f8919_line10 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.f4137_col_d.zero.then1` (replace an operand, person.person.f4137_col_d): Branch settled by its guard: where person.f4137_col_d takes alternative 1 (guard {
  "eq": [
    "scope.tips_unreported_if_pay",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.f4137_col_c make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither person.zero nor person.f4137_col_c ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.f4137_line10.zero.then1` (replace an operand, person.person.f4137_line10): Branch settled by its guard: where person.f4137_line10 takes alternative 1 (guard {
  "eq": [
    "person.f4137_filed",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.f4137_line6 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.f4137_tax.zero.then1` (replace an operand, person.person.f4137_tax): Branch settled by its guard: where person.f4137_tax takes alternative 1 (guard {
  "eq": [
    "person.f4137_filed",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.zero and person.f4137_line10 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
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
- `operand.person.person.simple_age_50_59_years.simple_age_if_open_year.then0` (replace an operand, person.person.simple_age_50_59_years): Branch settled by its guard: where person.simple_age_50_59_years takes alternative 0 (guard {
  "eq": [
    "person.simple_open_year",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.simple_age_if_open_year and person.simple_age_60_63_years make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither person.simple_age_if_open_year nor person.simple_age_60_63_years ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.simple_age_from_age50.catchup_age50.then0` (replace an operand, person.person.simple_age_from_age50): Branch settled by its guard: where person.simple_age_from_age50 takes alternative 0 (guard {
  "eq": [
    "person.age50_at_year_end_if_open_year",
    {
      "const": true
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.catchup_age50 and person.simple_age_if_open_year make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither person.catchup_age50 nor person.simple_age_if_open_year ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.simple_catchup.simple_regular` (replace an operand, person.person.simple_catchup): Floor-minus-min identity: person.simple_catchup is person.simple_deferral less person.simple_regular, floored at zero, and one of person.simple_regular and person.simple_cap is the ungated smaller of person.simple_deferral and the other, so person.simple_deferral less either, floored at zero, is the same at every input; person.simple_deferral is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.person.person.eic_se.zero.then1` (replace an operand, person.person.eic_se): person.eic_se's has_sc-false alternative is person.zero; the mutant reads person.eic_part1, sc_total less se_line13. With has_sc known false the roster is confirmed and empty, sc_total is $0 and se_line13 takes person.zero, so eic_part1 is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; sc_total, a sum over that roster, is unknown, and se_line13's gate se_rrta is unknown, so se_line13 is unknown at line entry; eic_part1 is then unknown, never a refusal, as the base's person.zero is not, and eic_se is has_sc's unknown on both routes (spec 4.7.3). (Premises pinned: person.eic_se, person.eic_part1, person.sc_total, person.se_line13, person.has_sc, person.sc_count, person.se_rrta, person.sc_rrta_count, person.zero, sc.one, param:sc.one; the mutant reads person.eic_part1.) (structural conditions re-checked this run.)
- `operand.person.person.dc_earned.eic_se` (replace an operand, person.person.dc_earned): person.eic_se is person.eic_se_has when the person has a Schedule C and $0 otherwise. With no Schedule C every sum over the person's Schedule C entries is $0, so the Schedule SE railroad gate is false, line 4c is $0, files_se is false and eic_se_has is the empty Schedule C total, $0; with the roster unanswered both routes are unknown. The replacement changes no value. (structural conditions re-checked this run.)
- `operand.person.person.ira_excess_gate.no.then1` (replace an operand, person.person.ira_excess_gate): Branch equal under a case split: where person.ira_excess_gate takes alternative 1 (guard {
  "eq": [
    "person.ira_any_contrib",
    {
      "const": false
    }
  ],
  "op": "test"
}
), person.no and person.ira_has have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.person.person.ira_roth_income.no.then1` (replace an operand, person.person.ira_roth_income): Branch settled by its guard: where person.ira_roth_income takes alternative 1 (guard {
  "eq": [
    "person.ira_roth_has",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that person.no and person.ira_roth_over make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.person.person.ira_dist_gate.no.then1` (replace an operand, person.person.ira_dist_gate): ira_dist_gate is a choice on ira_has (ira_contrib more than $0): true takes ira_dist_if_files, false takes person.no (the parameter household.no, false); the mutant reads ira_basis_gate, all[ira_files_8606, ira_basis_adjusted], in place of person.no. ira_contrib reads inputs with no refusal gates (ira_trad, and sav_trad through the gate sav_trad_if_ira_owner, a choice on the input ira_owner whose other alternative is person.no), so ira_has is never a refusal. With ira_has a known false (memoized, spec 4.7.6), ira_nondeductible, a choice on ira_has whose false alternative is person.zero, is $0, ira_files_8606 (ira_nondeductible more than $0) is false, and ira_basis_gate, an all-test whose first conjunct is ira_files_8606 true, is false, the value of person.no. Where ira_has is unknown both alternatives are ways (spec 4.7.3): ira_nondeductible is then unknown (its person.zero way never refuses), ira_files_8606 is unknown, and ira_basis_gate is false or unknown (ira_basis_adjusted is an input with no refusal gates), never a refusal, so ira_dist_gate is that unknown on both routes. (Premises pinned: person.ira_dist_gate, person.ira_has, person.ira_contrib, person.ira_dist_if_files, person.ira_basis_gate, person.ira_files_8606, person.ira_nondeductible, person.ira_basis_adjusted, person.zero, person.no, param:household.no, person.sav_trad_if_ira_owner, person.ira_owner, person.sav_trad, person.ira_trad; the mutant reads person.ira_basis_gate.) (structural conditions re-checked this run.)
- `operand.person.person.ira_se.zero.then1` (replace an operand, person.person.ira_se): person.ira_se's has_sc-false alternative is person.zero; the mutant reads person.ira_se_take, the sum of se_line13 and s16. With has_sc known false both take person.zero, so the sum is $0. Where has_sc is unknown: has_sc is sc_count more than 0, sc_count a sum of sc.one (a parameter) over the person's Schedule C entries with no filter, so it is complete wherever that roster is confirmed and unknown, without a lower bound, only where it is not; person.se_rrta sums sc.one over the same roster (where sc.rrta), so it is unknown there too; se_line13's gate se_rrta is unknown, so se_line13 is unknown at line entry, and s16 is a choice on has_sc with a person.zero alternative, so it is unknown (spec 4.7.3); ira_se_take is then unknown, never a refusal, and ira_se is has_sc's unknown on both routes. (Premises pinned: person.ira_se, person.ira_se_take, person.se_line13, person.s16, person.has_sc, person.sc_count, person.se_rrta, person.sc_rrta_count, person.zero, sc.one, param:sc.one; the mutant reads person.ira_se_take.) (structural conditions re-checked this run.)
- `operand.person.person.edu_adj.zero.then1` (replace an operand, person.person.edu_adj): edu_adj's edu_student-false alternative: edu_student is then known false (memoized). edu_adj's other reader, edu_has_adj (edu_adj more than $0), is read only by edu_over_if_adj, which only edu_over_refused reads, in its edu_student-true alternative; edu_over_refused is a choice on edu_student whose false alternative is edu_no, the year parameter edu.no (false), so it is false without reading edu_adj. Lines 27 to 30 read edu_adj only in the alternative guarded by edu_aoc true; edu_aoc is all[edu_aoc_rules true, f8863.ban_if_aoc false] and edu_aoc_rules is a choice on edu_student whose false alternative is edu_no, so edu_aoc is false (an all-test stops at a known false conjunct). Line 31 reads it only in the alternative guarded by edu_llc true, an all-test whose first conjunct is edu_student true, so edu_llc is false. Those alternatives (and their bindings) are not evaluated (spec 4.7.3, 4.7.4). Where edu_student is unknown, edu_adj's other alternative, edu_adj_sum (a sum of three inputs with no refusal gates, edu_a_this_year, edu_a_next_year and edu_refunds), never refuses, so edu_adj is that unknown on both routes (spec 4.7.3). edu_adj, edu_has_adj and edu_over_if_adj are helpers. (Premises pinned: person.edu_adj, person.edu_adj_sum, person.edu_student, person.edu_has_adj, person.edu_over_if_adj, person.edu_over_refused, person.edu_aoc, person.edu_aoc_rules, person.edu_no, person.edu_llc, person.edu_line27, person.edu_line28, person.edu_line29, person.edu_line30, person.edu_line31, person.zero, param:edu.no, person.edu_a_this_year, person.edu_a_next_year, person.edu_refunds; the mutant reads person.ira_se.) (structural conditions re-checked this run.)
- `operand.person.person.edu_has_adj.edu_adj.gt.0` (replace an operand, person.person.edu_has_adj): Guarded figure: person.edu_adj is person.edu_adj_sum wherever person.edu_student holds, and every printed line reads person.edu_has_adj (a helper) only through choices whose guards make person.edu_student true, which, where a guard is unknown, are that unknown whatever person.edu_has_adj is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where person.edu_student does not hold only person.edu_has_adj's own, unprinted value can differ.
- `operand.person.person.edu_over_refused.edu_no.then1` (replace an operand, person.person.edu_over_refused): Branch equal under a case split: where person.edu_over_refused takes alternative 1 (guard {
  "eq": [
    "person.edu_student",
    {
      "const": false
    }
  ],
  "op": "test"
}
), person.edu_no and person.edu_has_adj have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.person.person.edu_aoc_rules.edu_no.then1` (replace an operand, person.person.edu_aoc_rules): Branch equal under a case split: where person.edu_aoc_rules takes alternative 1 (guard {
  "eq": [
    "person.edu_student",
    {
      "const": false
    }
  ],
  "op": "test"
}
), person.edu_no and person.edu_show26 have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
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
- `operand.qbi.qbi.coop_patron_if_amount.no.then1` (replace an operand, qbi.qbi.coop_patron_if_amount): Branch equal under a case split: where qbi.coop_patron_if_amount takes alternative 1 (guard {
  "eq": [
    "qbi.has_amount",
    {
      "const": false
    }
  ],
  "op": "test"
}
), qbi.no and qbi.suspended_if_business have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.qdcg.qdcg.line8.line7` (replace an operand, qdcg.qdcg.line8): qdcg.line8 is min(qdcg.line5, qdcg.line7) and qdcg.line7 is the ungated min(qdcg.line1, qdcg.line6); qdcg.line5 is qdcg.line1 less a non-negative amount, floored at zero, with qdcg.line1 not negative, so qdcg.line5 <= qdcg.line1 and min(qdcg.line5, min(qdcg.line1, qdcg.line6)) = min(qdcg.line5, qdcg.line6) at every input; qdcg.line5 is read first on both routes. (structural conditions re-checked this run.)
- `operand.qdcg.qdcg.line12.line11` (replace an operand, qdcg.qdcg.line12): Copy-chain identity: qdcg.line11 and qdcg.line9 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.rec.rec.path.no.then0` (replace an operand, rec.rec.path): Branch settled by its guard: where rec.path takes alternative 0 (guard {
  "eq": [
    "scope.recovery",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that rec.no and rec.two_returns_if_joint make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither rec.no nor rec.two_returns_if_joint ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.rec.rec.w2a_line5_more` (replace strict greater-than with inclusive, rec.rec.w2a_line5_more): rec.w2a_line5_more (rec.w2a_line3 gt rec.w2a_line4) is read only by rec.w2a_line7_capped and rec.w2a_line8_capped (true: the share, rec.w2a_line7_share or rec.w2a_line8_share; false: rec.zero), and they only by rec.w2a_line7 and rec.w2a_line8, in their rec.w2a_cap-true alternative. Made inclusive, the test changes only where lines 3 and 4 are known and equal; with either unknown or refused, both tests are that unknown or refusal. The shares are prorate(rec.w2a_line5, line 1 or line 2, rec.w2a_line6), and rec.w2a_line5 is subtract_floor0 from line 3 take line 4, $0 when they are equal. With rec.w2a_cap known true, line 4 is refund.line2, 5d less 5e floored, positive since 5d is more than 5e; line 3 equals it, so rec.w2a_line6 (line 1 plus line 2, of which line 3 is the smaller with 5d) is positive and known: each share is $0, as the data's rec.zero. With rec.w2a_cap known false the capped lines are not read. With rec.w2a_cap unknown, line 4 is unknown (a choice on it) or, where both its ways refuse, a refusal, so the test is the same on both routes. (Premises pinned: rec.w2a_line5_more, rec.w2a_line7_capped, rec.w2a_line8_capped, rec.w2a_line7_share, rec.w2a_line8_share, rec.w2a_line5, rec.w2a_line3, rec.w2a_line4, rec.w2a_line6, rec.w2a_line1, rec.w2a_line2, rec.w2a_cap, refund.line2, rec.w2a_line7, rec.w2a_line8, rec.zero, param:sales.zero.) (structural conditions re-checked this run.)
- `operand.rec.rec.w2a_line5_more.w2a_line3.gt.0` (replace an operand, rec.rec.w2a_line5_more): rec.w2a_line5_more tests rec.w2a_line3 gt rec.w2a_line4; the mutant tests rec.w2a_line6 gt rec.w2a_line4. rec.w2a_line3 is smaller_of(rec.w2a_line6, refund.line5d_prior_year): not more than line 6, the same refusal where line 6 refuses (line 6 is its first operand), and unknown where line 6 or 5d is unknown. The test is read only by rec.w2a_line7_capped and rec.w2a_line8_capped (true: the share, prorate(rec.w2a_line5, line 1 or line 2, rec.w2a_line6); false: rec.zero), and they only in rec.w2a_cap's true alternative. The routes differ only where line 3 is not more than line 4 and line 6 is more: there rec.w2a_line5 (line 3 less line 4, floored) is $0 and line 6 is positive, so each share is $0, as rec.zero. Where 5d is unknown, line 4 is unknown too (rec.w2a_cap or refund.line2 reads 5d), so both tests are unknown. (Premises pinned: rec.w2a_line5_more, rec.w2a_line7_capped, rec.w2a_line8_capped, rec.w2a_line7_share, rec.w2a_line8_share, rec.w2a_line5, rec.w2a_line3, rec.w2a_line4, rec.w2a_line6, rec.w2a_line1, rec.w2a_line2, rec.w2a_cap, refund.line2, rec.w2a_line7, rec.w2a_line8, rec.zero, param:sales.zero; the mutant reads rec.w2a_line6.) (structural conditions re-checked this run.)
- `operand.rec.rec.w2a_line7_capped.zero.then1` (replace an operand, rec.rec.w2a_line7_capped): rec.w2a_line7_capped's rec.w2a_line5_more-false alternative is rec.zero ($0); the mutant reads rec.w2a_line5, subtract_floor0 from rec.w2a_line3 take rec.w2a_line4. That alternative is taken only where rec.w2a_line5_more (line 3 gt line 4) is known false, so lines 3 and 4 are known with line 3 not more than line 4 and line 5 is $0. Where the test is unknown, both routes are unknown: neither rec.zero nor rec.w2a_line5 can refuse without the test refusing first (line 5 refuses only where line 3 or line 4 does). (Premises pinned: rec.w2a_line7_capped, rec.w2a_line5_more, rec.w2a_line5, rec.w2a_line3, rec.w2a_line4, rec.zero, param:sales.zero; the mutant reads rec.w2a_line5.) (structural conditions re-checked this run.)
- `operand.rec.rec.w2a_line8_capped.zero.then1` (replace an operand, rec.rec.w2a_line8_capped): rec.w2a_line8_capped's rec.w2a_line5_more-false alternative is rec.zero ($0); the mutant reads rec.w2a_line7. rec.w2a_line8_capped is read only by rec.w2a_line8, in its rec.w2a_cap-true alternative. With cap true and rec.w2a_line5_more false, rec.w2a_line7 is its cap-true alternative rec.w2a_line7_capped, whose line5_more-false alternative is rec.zero: $0 on both routes. With cap unknown, rec.w2a_line8 is unknown unless every way refuses; the mutant's alternative rec.w2a_line7 is then a choice whose way rec.w2a_line7_capped is $0, so it does not refuse, as rec.zero does not. Where rec.w2a_line5_more is unknown both routes are unknown; it is never unknown where rec.w2a_line1 refuses (line 6, line 3 and the test refuse first). (Premises pinned: rec.w2a_line8_capped, rec.w2a_line8, rec.w2a_line7, rec.w2a_line7_capped, rec.w2a_line5_more, rec.w2a_line8_share, rec.w2a_line7_share, rec.w2a_line5, rec.w2a_line3, rec.w2a_line4, rec.w2a_line6, rec.w2a_line1, rec.w2a_line2, rec.w2a_cap, rec.zero, param:sales.zero; the mutant reads rec.w2a_line7.) (structural conditions re-checked this run.)
- `operand.rec.rec.line3.line1b` (replace an operand, rec.rec.line3): Copy-chain identity: rec.line1b and rec.w2a_line8 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.rec.rec.to_line8z.zero.then1` (replace an operand, rec.rec.to_line8z): Branch settled by its guard: where rec.to_line8z takes alternative 1 (guard {
  "eq": [
    "rec.path",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that rec.zero and rec.to_line1 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.rental.rental.overlap_c.zero.then1` (replace an operand, rental.rental.overlap_c): Branch settled by its guard: where rental.overlap_c takes alternative 1 (guard {
  "eq": [
    "rental.personal_any",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that rental.zero and rental.personal_c make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither rental.zero nor rental.personal_c ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.rental.rental.total_c.overlap_c` (replace an operand, rental.rental.total_c): Guarded figure: rental.overlap_c is rental.overlap_raw wherever rental.personal_any holds, and every printed line reads rental.total_c (a helper) only through choices whose guards make rental.personal_any true, which, where a guard is unknown, are that unknown whatever rental.total_c is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where rental.personal_any does not hold only rental.total_c's own, unprinted value can differ.
- `operand.rental.rental.home_pers10_if_any.zero.then1` (replace an operand, rental.rental.home_pers10_if_any): rental.home_pers10_if_any's rental.personal_any-false alternative is rental.zero; the mutant reads rental.home_rent_c. Its only reader is rental.home, all(rental.personal_c gt the parameter rental.home_days (14), rental.home_pers10_if_any gt rental.home_rent_c), evaluated in order and false at the first false conjunct. Where rental.personal_any is false, rental.personal_c is its false alternative rental.zero ($0), and 0 gt 14 is false, so rental.home is false before the second conjunct is read. Where personal_any is unknown, rental.home_pers10_if_any is unknown on both routes (neither rental.home_pers10, rental.zero nor rental.home_rent_c refuses), and where it is true both take rental.home_pers10. (Premises pinned: rental.home_pers10_if_any, rental.home, rental.personal_c, rental.personal_any, rental.zero, param:sales.zero, param:rental.home_days, rental.home_rent_c, rental.home_pers10; the mutant reads rental.home_rent_c.) (structural conditions re-checked this run.)
- `operand.rental.rental.net_loss.zero` (replace an operand, rental.rental.net_loss): rental.net_loss is subtract_floor0 from rental.zero ($0, the parameter sales.zero) take rental.line21; the mutant takes rental.line21 from rental.net_income, which is subtract_floor0 from rental.line21 take rental.zero, that is max(line21, 0). For a known line 21: max(max(line21, 0) - line21, 0) = max(-line21, 0). Where line 21 is unknown or a refusal, rental.net_income is that same value: both routes give line 21's refusal, or unknown. (Premises pinned: rental.net_loss, rental.net_income, rental.line21, rental.zero, param:sales.zero; the mutant reads rental.net_income.) (structural conditions re-checked this run.)
- `operand.rental.rental.prior_loss.zero.then1` (replace an operand, rental.rental.prior_loss): Branch equal under a case split: where rental.prior_loss takes alternative 1 (guard {
  "eq": [
    "rental.reported",
    {
      "const": false
    }
  ],
  "op": "test"
}
), rental.zero and rental.net_loss have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
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
), retirement.l2 and retirement.l2_exc have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
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
- `operand.royalty.royalty.loss_abs.zero` (replace an operand, royalty.royalty.loss_abs): royalty.loss_abs is subtract_floor0 from royalty.zero ($0, the parameter sales.zero) take royalty.line21; the mutant takes royalty.line21 from royalty.income, which is subtract_floor0 from royalty.line21 take royalty.zero, that is max(line21, 0). For a known line 21: max(max(line21, 0) - line21, 0) = max(-line21, 0) = max(0 - line21, 0). Where line 21 is unknown or a refusal, royalty.income is that same value, and subtract_floor0 gives the first refusal among its operands, else unknown: both routes give line 21's refusal, or unknown. loss_abs's own refusal gate (royalty.not_at_risk) is evaluated at entry, before the expression, the same on both routes (spec 4.7.1). (Premises pinned: royalty.loss_abs, royalty.income, royalty.line21, royalty.zero, param:sales.zero; the mutant reads royalty.income.) (structural conditions re-checked this run.)
- `operand.s1.s1.line7.zero.then1` (replace an operand, s1.s1.line7): Branch settled by its guard: where s1.line7 takes alternative 1 (guard {
  "eq": [
    "s1.has_uc",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1.zero and s1.uc_paid_if_any make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither s1.zero nor s1.uc_paid_if_any ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1.s1.line2b_notice.line2a.gt.0` (replace an operand, s1.s1.line2b_notice): Guarded figure: s1.line2a is s1.alimony_refused wherever s1.alimony_if_any holds, and every printed line reads s1.line2b_notice (a helper) only through choices whose guards make s1.alimony_if_any true, which, where a guard is unknown, are that unknown whatever s1.line2b_notice is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1.alimony_if_any does not hold only s1.line2b_notice's own, unprinted value can differ.
- `operand.s1.s1.nol_limit.no.then1` (replace an operand, s1.s1.nol_limit): Branch equal under a case split: where s1.nol_limit takes alternative 1 (guard {
  "eq": [
    "scope.nol",
    {
      "const": false
    }
  ],
  "op": "test"
}
), s1.no and s1.nol_marital have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.s1.s1.line19b_notice.line19a.gt.0` (replace an operand, s1.s1.line19b_notice): Guarded figure: s1.line19a is s1.paid_refused wherever s1.alimony_if_any holds, and every printed line reads s1.line19b_notice (a helper) only through choices whose guards make s1.alimony_if_any true, which, where a guard is unknown, are that unknown whatever s1.line19b_notice is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1.alimony_if_any does not hold only s1.line19b_notice's own, unprinted value can differ.
- `operand.s1.s1.line19c_notice.line19a.gt.0` (replace an operand, s1.s1.line19c_notice): Guarded figure: s1.line19a is s1.paid_refused wherever s1.alimony_if_any holds, and every printed line reads s1.line19c_notice (a helper) only through choices whose guards make s1.alimony_if_any true, which, where a guard is unknown, are that unknown whatever s1.line19c_notice is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1.alimony_if_any does not hold only s1.line19c_notice's own, unprinted value can differ.
- `operand.s1.s1.line26.line25` (replace an operand, s1.s1.line26): Copy-chain identity: s1.line25 and s1.line24a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s179.s179.line13.line12` (replace an operand, s179.s179.line13): Floor-minus-min identity: s179.line13 is s179.line9_10 less s179.line12, floored at zero, and one of s179.line12 and s179.line11 is the ungated smaller of s179.line9_10 and the other, so s179.line9_10 less either, floored at zero, is the same at every input; s179.line9_10 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.s1a.s1a.line2e.line2b` (replace an operand, s1a.s1a.line2e): Copy-chain identity: s1a.line2b and s1a.zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.line2e.line2c` (replace an operand, s1a.s1a.line2e): Copy-chain identity: s1a.line2c and s1a.zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.line2e.line2d` (replace an operand, s1a.s1a.line2e): Copy-chain identity: s1a.line2d and s1a.zero expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.tips_employee_one.line4b` (replace an operand, s1a.s1a.tips_employee_one): Guarded figure: s1a.line4b is s1a.line4b_calc wherever s1a.part2 holds, and every printed line reads s1a.tips_employee_one (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.tips_employee_one is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.tips_employee_one's own, unprinted value can differ.
- `operand.s1a.s1a.tips_employee.zero.then0` (replace an operand, s1a.s1a.tips_employee): Branch settled by its guard: where s1a.tips_employee takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.tips_employee_one make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.tips_business.zero.then0` (replace an operand, s1a.s1a.tips_business): Branch settled by its guard: where s1a.tips_business takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.tips_employee make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.tips_total_calc.tips_business` (replace an operand, s1a.s1a.tips_total_calc): Guarded figure: s1a.tips_business is s1a.tips_business_calc wherever s1a.part2 holds, and every printed line reads s1a.tips_total_calc (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.tips_total_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.tips_total_calc's own, unprinted value can differ.
- `operand.s1a.s1a.tips_total.zero.then0` (replace an operand, s1a.s1a.tips_total): Branch settled by its guard: where s1a.tips_total takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.tips_business make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.tips_capped_calc.tips_total` (replace an operand, s1a.s1a.tips_capped_calc): Guarded figure: s1a.tips_total is s1a.tips_total_calc wherever s1a.part2 holds, and every printed line reads s1a.tips_capped_calc (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.tips_capped_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.tips_capped_calc's own, unprinted value can differ.
- `operand.s1a.s1a.tips_capped.zero.then0` (replace an operand, s1a.s1a.tips_capped): Branch settled by its guard: where s1a.tips_capped takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.tips_total make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.tips_magi.tips_magi_calc.then1` (replace an operand, s1a.s1a.tips_magi): Copy-chain identity: s1a.tips_magi_calc and s1a.line3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s1a.s1a.tips_over_calc.tips_magi` (replace an operand, s1a.s1a.tips_over_calc): Guarded figure: s1a.tips_magi is s1a.tips_magi_calc wherever s1a.part2 holds, and every printed line reads s1a.tips_over_calc (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.tips_over_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.tips_over_calc's own, unprinted value can differ.
- `operand.s1a.s1a.tips_over.zero.then0` (replace an operand, s1a.s1a.tips_over): Branch settled by its guard: where s1a.tips_over takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.tips_magi make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.tips_magi_over` (replace strict greater-than with inclusive, s1a.s1a.tips_magi_over): The test 's1a.tips_magi more than s1a.tips_threshold' made inclusive adds only s1a.tips_magi = s1a.tips_threshold; there s1a.tips_over_pos is zero, the reduction s1a.tips_reduction is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.tips_deduction_figured (s1a.tips_capped less s1a.tips_reduction) equals s1a.tips_capped, the value the other branch gives. The test is read only by s1a.tips_deduction_amount. (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_magi_over.tips_threshold.gt.1` (replace an operand, s1a.s1a.tips_magi_over): s1a.tips_threshold is a choice on s1a.part2: false takes s1a.zero, true takes s1a.tips_threshold_calc; the mutant reads s1a.tips_threshold_calc in place of s1a.tips_threshold in s1a.tips_magi_over, a helper whose only reader is s1a.tips_deduction_amount. s1a.tips_deduction_amount's only reader is s1a.tips_deduction_ssn, in its s1a.tip_ssn-true alternative; s1a.tips_deduction_ssn's only reader is s1a.tips_deduction_claim, in its single, mfj, hoh and qss alternatives; s1a.tips_deduction_claim's only reader is the printed s1a.tips_deduction, in its s1a.tips-true alternative (s1a.tips_deduction's own refusal gates are evaluated at entry, the same on both routes, spec 4.7.1). s1a.part2 is a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs and s1a.no (false) for mfs. So where those three guards hold (s1a.tips true, a status other than mfs, s1a.tip_ssn true), s1a.part2 is true, s1a.tips_threshold is s1a.tips_threshold_calc's memoized value (spec 4.7.6), and s1a.tips_magi_over is the same on both routes. Where one of them is false the alternative reading s1a.tips_magi_over is not taken, and where one is refused the choose holding it is that refusal on both routes. Where one is unknown, the choose holding it has another alternative still possible that never refuses (s1a.zero, in s1a.tips_deduction, s1a.tips_deduction_claim and s1a.tips_deduction_ssn), so it is that guard's unknown on both routes whatever s1a.tips_magi_over is (spec 4.7.3). No printed value changes; only the helpers between s1a.tips_magi_over and s1a.tips_deduction can differ where s1a.part2 is not true. (Premises pinned: s1a.tips_magi_over, s1a.tips_threshold, s1a.tips_threshold_calc, s1a.tips_deduction_amount, s1a.tips_deduction_ssn, s1a.tips_deduction_claim, s1a.tips_deduction, s1a.part2, s1a.part2_ssn, s1a.tips, s1a.tip_ssn, s1a.no, s1a.zero, f1040.status, param:household.no; the mutant reads s1a.tips_threshold_calc.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_over_pos.tips_threshold` (replace an operand, s1a.s1a.tips_over_pos): Guarded figure: s1a.tips_threshold is s1a.tips_threshold_calc wherever s1a.part2 holds, and every printed line reads s1a.tips_over_pos (a helper) only through choices whose guards make s1a.part2 true, which, where a guard is unknown, are that unknown whatever s1a.tips_over_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part2 does not hold only s1a.tips_over_pos's own, unprinted value can differ.
- `operand.s1a.s1a.tips_reduction.zero.then0` (replace an operand, s1a.s1a.tips_reduction): Branch settled by its guard: where s1a.tips_reduction takes alternative 0 (guard {
  "eq": [
    "s1a.part2",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line11_thousands make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.tips_deduction_figured.tips_reduction` (replace an operand, s1a.s1a.tips_deduction_figured): s1a.tips_reduction is a choice on s1a.part2: false takes s1a.zero, true takes s1a.tips_reduction_calc; the mutant reads s1a.tips_reduction_calc in place of s1a.tips_reduction in s1a.tips_deduction_figured, a helper whose only reader is s1a.tips_deduction_amount. s1a.tips_deduction_amount's only reader is s1a.tips_deduction_ssn, in its s1a.tip_ssn-true alternative; s1a.tips_deduction_ssn's only reader is s1a.tips_deduction_claim, in its single, mfj, hoh and qss alternatives; s1a.tips_deduction_claim's only reader is the printed s1a.tips_deduction, in its s1a.tips-true alternative (s1a.tips_deduction's own refusal gates are evaluated at entry, the same on both routes, spec 4.7.1). s1a.part2 is a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs and s1a.no (false) for mfs. So where those three guards hold (s1a.tips true, a status other than mfs, s1a.tip_ssn true), s1a.part2 is true, s1a.tips_reduction is s1a.tips_reduction_calc's memoized value (spec 4.7.6), and s1a.tips_deduction_figured is the same on both routes. Where one of them is false the alternative reading s1a.tips_deduction_figured is not taken, and where one is refused the choose holding it is that refusal on both routes. Where one is unknown, the choose holding it has another alternative still possible that never refuses (s1a.zero, in s1a.tips_deduction, s1a.tips_deduction_claim and s1a.tips_deduction_ssn), so it is that guard's unknown on both routes whatever s1a.tips_deduction_figured is (spec 4.7.3). No printed value changes; only the helpers between s1a.tips_deduction_figured and s1a.tips_deduction can differ where s1a.part2 is not true. (Premises pinned: s1a.tips_deduction_figured, s1a.tips_reduction, s1a.tips_reduction_calc, s1a.tips_deduction_amount, s1a.tips_deduction_ssn, s1a.tips_deduction_claim, s1a.tips_deduction, s1a.part2, s1a.part2_ssn, s1a.tips, s1a.tip_ssn, s1a.no, s1a.zero, f1040.status, param:household.no; the mutant reads s1a.tips_reduction_calc.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_deduction_ssn.zero.then0` (replace an operand, s1a.s1a.tips_deduction_ssn): s1a.tips_deduction_ssn's s1a.tip_ssn-false alternative is s1a.zero; the mutant reads s1a.tips_deduction_figured, s1a.tips_capped less s1a.tips_reduction, floored at zero. s1a.tips_deduction_ssn is read only by s1a.tips_deduction_claim, and s1a.tips_deduction_claim only by s1a.tips_deduction, in its s1a.tips-true alternative; where s1a.tips is unknown s1a.tips_deduction is a choice whose other way, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever s1a.tips_deduction_ssn is (spec 4.7.3). Where s1a.tips is true, s1a.part2 is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs and s1a.no (false) for mfs. With s1a.tip_ssn known false and the status known, s1a.part2 is false, so s1a.tips_capped and s1a.tips_reduction take s1a.zero and s1a.tips_deduction_figured is $0. With s1a.tip_ssn known false and the status unknown, s1a.part2 is that unknown, never a refusal, and so are s1a.tips_capped, s1a.tips_reduction and s1a.tips_deduction_figured (each a choice on s1a.part2 with an s1a.zero alternative, or their difference); s1a.tips_deduction_claim is then a choice on the unknown status whose mfs alternative, s1a.zero, never refuses, so it is the status's unknown on both routes. Where s1a.tip_ssn is unknown, s1a.part2 is false or unknown (s1a.tips and the status are inputs, s1a.no a parameter), so s1a.tips_capped and s1a.tips_reduction are $0 or that unknown, never a refusal, and so is s1a.tips_deduction_figured; the base's s1a.zero is not a refusal either, so s1a.tips_deduction_ssn is s1a.tip_ssn's unknown on both routes. (Premises pinned: s1a.tips_deduction_ssn, s1a.tips_deduction_claim, s1a.tips_deduction, s1a.tips_deduction_figured, s1a.tips_capped, s1a.tips_reduction, s1a.part2, s1a.part2_ssn, s1a.no, param:household.no, s1a.tip_ssn, s1a.tips, s1a.tip_ssn_count, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.tips_deduction_figured.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then0` (replace an operand, s1a.s1a.tips_deduction_claim): s1a.tips_deduction_claim's single alternative is s1a.tips_deduction_ssn; the mutant reads s1a.tips_deduction_amount. s1a.tips_deduction_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.tips_deduction_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is single, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.tips_deduction_ssn take s1a.tips_deduction_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.tips_magi_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.tips_deduction_amount is s1a.tips_capped, $0, which is s1a.tips_deduction_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.tips_magi_over is unknown and s1a.tips_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.tips_deduction_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.tips_deduction_claim, s1a.tips_deduction, s1a.tips_deduction_ssn, s1a.tips_deduction_amount, s1a.tips_deduction_figured, s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi, s1a.tips_threshold, s1a.tips_magi_over, s1a.part2, s1a.part2_ssn, s1a.no, param:household.no, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.tips_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then1` (replace an operand, s1a.s1a.tips_deduction_claim): s1a.tips_deduction_claim's mfj alternative is s1a.tips_deduction_ssn; the mutant reads s1a.tips_deduction_amount. s1a.tips_deduction_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.tips_deduction_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is mfj, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.tips_deduction_ssn take s1a.tips_deduction_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.tips_magi_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.tips_deduction_amount is s1a.tips_capped, $0, which is s1a.tips_deduction_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.tips_magi_over is unknown and s1a.tips_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.tips_deduction_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.tips_deduction_claim, s1a.tips_deduction, s1a.tips_deduction_ssn, s1a.tips_deduction_amount, s1a.tips_deduction_figured, s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi, s1a.tips_threshold, s1a.tips_magi_over, s1a.part2, s1a.part2_ssn, s1a.no, param:household.no, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.tips_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_deduction_claim.zero.then2` (replace an operand, s1a.s1a.tips_deduction_claim): s1a.tips_deduction_claim's married-filing-separately alternative is s1a.zero ($0); the mutant reads s1a.tips_deduction_amount. s1a.tips_deduction_claim is read only by s1a.tips_deduction, in its s1a.tips-true alternative. Where s1a.tips is unknown the claim line is a way of its reader (spec 4.7.3), whose other alternative, s1a.zero, never refuses, so that reader is s1a.tips's unknown on both routes whatever the claim line is. With s1a.tips true and the status known to be mfs, s1a.part2 (s1a.part2_ssn, whose mfs alternative is s1a.no, false) is false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold each take s1a.zero, s1a.tips_magi_over is false and s1a.tips_deduction_amount is s1a.tips_capped, $0: the two values agree. Where the status is unknown both are ways (spec 4.7.3). s1a.tip_ssn is any[all[status not mfj, household.taxpayer_work_ssn], all[status mfj, s1a.tip_ssn_count > 0]]; each all-test then meets the unknown status first, so it is false or unknown, never true, and never a refusal (s1a.tip_ssn_count and household.taxpayer_work_ssn are counts over the person roster with no refusal gates); so s1a.tip_ssn is false or unknown and s1a.tips_deduction_ssn is $0 or unknown, never a refusal, on the other four ways. The claim line is then the status's unknown on both routes. (Premises pinned: s1a.tips_deduction_claim, s1a.tips_deduction, s1a.tips_deduction_ssn, s1a.tips_deduction_amount, s1a.tips_deduction_figured, s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi, s1a.tips_threshold, s1a.tips_magi_over, s1a.part2, s1a.part2_ssn, s1a.no, param:household.no, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.tips_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then3` (replace an operand, s1a.s1a.tips_deduction_claim): s1a.tips_deduction_claim's hoh alternative is s1a.tips_deduction_ssn; the mutant reads s1a.tips_deduction_amount. s1a.tips_deduction_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.tips_deduction_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is hoh, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.tips_deduction_ssn take s1a.tips_deduction_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.tips_magi_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.tips_deduction_amount is s1a.tips_capped, $0, which is s1a.tips_deduction_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.tips_magi_over is unknown and s1a.tips_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.tips_deduction_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.tips_deduction_claim, s1a.tips_deduction, s1a.tips_deduction_ssn, s1a.tips_deduction_amount, s1a.tips_deduction_figured, s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi, s1a.tips_threshold, s1a.tips_magi_over, s1a.part2, s1a.part2_ssn, s1a.no, param:household.no, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.tips_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then4` (replace an operand, s1a.s1a.tips_deduction_claim): s1a.tips_deduction_claim's qss alternative is s1a.tips_deduction_ssn; the mutant reads s1a.tips_deduction_amount. s1a.tips_deduction_claim's only reader is s1a.tips_deduction, a choice on s1a.tips (false: s1a.zero; true: s1a.tips_deduction_claim). Where s1a.tips is false the claim line is not read. Where s1a.tips is unknown the claim line is a way of s1a.tips_deduction (spec 4.7.3), but s1a.tips_deduction's other alternative, s1a.zero, never refuses, so s1a.tips_deduction is s1a.tips's unknown on both routes whatever the claim line is. Where s1a.tips is true and the status is qss, s1a.part2, a choice on s1a.tips whose true alternative is s1a.part2_ssn, a choice on the status that takes s1a.tip_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.tip_ssn's value: s1a.tip_ssn true makes s1a.tips_deduction_ssn take s1a.tips_deduction_amount, the same memoized line; s1a.tip_ssn false makes s1a.part2 false, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold take s1a.zero, s1a.tips_magi_over (is s1a.tips_magi more than s1a.tips_threshold) is false and s1a.tips_deduction_amount is s1a.tips_capped, $0, which is s1a.tips_deduction_ssn's s1a.zero; s1a.tip_ssn unknown makes s1a.part2 that unknown, so s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi and s1a.tips_threshold, each a choice on s1a.part2 with an s1a.zero alternative, are unknown, s1a.tips_magi_over is unknown and s1a.tips_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.tips_deduction_ssn, a choice on s1a.tip_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.tip_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.tip_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.tips_deduction_claim, s1a.tips_deduction, s1a.tips_deduction_ssn, s1a.tips_deduction_amount, s1a.tips_deduction_figured, s1a.tips_capped, s1a.tips_reduction, s1a.tips_magi, s1a.tips_threshold, s1a.tips_magi_over, s1a.part2, s1a.part2_ssn, s1a.no, param:household.no, s1a.tip_ssn, s1a.tip_ssn_count, s1a.tips, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.tips_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_1099.zero.then0` (replace an operand, s1a.s1a.ot_1099): Branch settled by its guard: where s1a.ot_1099 takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.ot_w2 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.ot_total_calc.ot_1099` (replace an operand, s1a.s1a.ot_total_calc): Guarded figure: s1a.ot_1099 is s1a.ot_1099_calc wherever s1a.part3 holds, and every printed line reads s1a.ot_total_calc (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.ot_total_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.ot_total_calc's own, unprinted value can differ.
- `operand.s1a.s1a.ot_total.zero.then0` (replace an operand, s1a.s1a.ot_total): Branch settled by its guard: where s1a.ot_total takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.ot_1099 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.ot_threshold.zero.then0` (replace an operand, s1a.s1a.ot_threshold): Branch settled by its guard: where s1a.ot_threshold takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.ot_capped make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.ot_over_calc.ot_magi` (replace an operand, s1a.s1a.ot_over_calc): Guarded figure: s1a.ot_magi is s1a.ot_magi_calc wherever s1a.part3 holds, and every printed line reads s1a.ot_over_calc (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.ot_over_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.ot_over_calc's own, unprinted value can differ.
- `operand.s1a.s1a.ot_over.zero.then0` (replace an operand, s1a.s1a.ot_over): Branch settled by its guard: where s1a.ot_over takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.ot_magi make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.ot_magi_over` (replace strict greater-than with inclusive, s1a.s1a.ot_magi_over): The test 's1a.ot_magi more than s1a.ot_threshold' made inclusive adds only s1a.ot_magi = s1a.ot_threshold; there s1a.ot_over_pos is zero, the reduction s1a.ot_reduction is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.ot_deduction_figured (s1a.ot_capped less s1a.ot_reduction) equals s1a.ot_capped, the value the other branch gives. The test is read only by s1a.ot_deduction_amount. (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_magi_over.ot_threshold.gt.1` (replace an operand, s1a.s1a.ot_magi_over): s1a.ot_threshold is a choice on s1a.part3: false takes s1a.zero, true takes s1a.ot_threshold_calc; the mutant reads s1a.ot_threshold_calc in place of s1a.ot_threshold in s1a.ot_magi_over, a helper whose only reader is s1a.ot_deduction_amount. s1a.ot_deduction_amount's only reader is s1a.ot_deduction_ssn, in its s1a.ot_ssn-true alternative; s1a.ot_deduction_ssn's only reader is s1a.ot_deduction_claim, in its single, mfj, hoh and qss alternatives; s1a.ot_deduction_claim's only reader is the printed s1a.ot_deduction, in its s1a.overtime-true alternative (s1a.ot_deduction's own refusal gates are evaluated at entry, the same on both routes, spec 4.7.1). s1a.part3 is a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs and s1a.no (false) for mfs. So where those three guards hold (s1a.overtime true, a status other than mfs, s1a.ot_ssn true), s1a.part3 is true, s1a.ot_threshold is s1a.ot_threshold_calc's memoized value (spec 4.7.6), and s1a.ot_magi_over is the same on both routes. Where one of them is false the alternative reading s1a.ot_magi_over is not taken, and where one is refused the choose holding it is that refusal on both routes. Where one is unknown, the choose holding it has another alternative still possible that never refuses (s1a.zero, in s1a.ot_deduction, s1a.ot_deduction_claim and s1a.ot_deduction_ssn), so it is that guard's unknown on both routes whatever s1a.ot_magi_over is (spec 4.7.3). No printed value changes; only the helpers between s1a.ot_magi_over and s1a.ot_deduction can differ where s1a.part3 is not true. (Premises pinned: s1a.ot_magi_over, s1a.ot_threshold, s1a.ot_threshold_calc, s1a.ot_deduction_amount, s1a.ot_deduction_ssn, s1a.ot_deduction_claim, s1a.ot_deduction, s1a.part3, s1a.part3_ssn, s1a.overtime, s1a.ot_ssn, s1a.no, s1a.zero, f1040.status, param:household.no; the mutant reads s1a.ot_threshold_calc.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_over_pos.ot_threshold` (replace an operand, s1a.s1a.ot_over_pos): Guarded figure: s1a.ot_threshold is s1a.ot_threshold_calc wherever s1a.part3 holds, and every printed line reads s1a.ot_over_pos (a helper) only through choices whose guards make s1a.part3 true, which, where a guard is unknown, are that unknown whatever s1a.ot_over_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part3 does not hold only s1a.ot_over_pos's own, unprinted value can differ.
- `operand.s1a.s1a.ot_reduction.zero.then0` (replace an operand, s1a.s1a.ot_reduction): Branch settled by its guard: where s1a.ot_reduction takes alternative 0 (guard {
  "eq": [
    "s1a.part3",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line19_thousands make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.ot_deduction_figured.ot_reduction` (replace an operand, s1a.s1a.ot_deduction_figured): s1a.ot_reduction is a choice on s1a.part3: false takes s1a.zero, true takes s1a.ot_reduction_calc; the mutant reads s1a.ot_reduction_calc in place of s1a.ot_reduction in s1a.ot_deduction_figured, a helper whose only reader is s1a.ot_deduction_amount. s1a.ot_deduction_amount's only reader is s1a.ot_deduction_ssn, in its s1a.ot_ssn-true alternative; s1a.ot_deduction_ssn's only reader is s1a.ot_deduction_claim, in its single, mfj, hoh and qss alternatives; s1a.ot_deduction_claim's only reader is the printed s1a.ot_deduction, in its s1a.overtime-true alternative (s1a.ot_deduction's own refusal gates are evaluated at entry, the same on both routes, spec 4.7.1). s1a.part3 is a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs and s1a.no (false) for mfs. So where those three guards hold (s1a.overtime true, a status other than mfs, s1a.ot_ssn true), s1a.part3 is true, s1a.ot_reduction is s1a.ot_reduction_calc's memoized value (spec 4.7.6), and s1a.ot_deduction_figured is the same on both routes. Where one of them is false the alternative reading s1a.ot_deduction_figured is not taken, and where one is refused the choose holding it is that refusal on both routes. Where one is unknown, the choose holding it has another alternative still possible that never refuses (s1a.zero, in s1a.ot_deduction, s1a.ot_deduction_claim and s1a.ot_deduction_ssn), so it is that guard's unknown on both routes whatever s1a.ot_deduction_figured is (spec 4.7.3). No printed value changes; only the helpers between s1a.ot_deduction_figured and s1a.ot_deduction can differ where s1a.part3 is not true. (Premises pinned: s1a.ot_deduction_figured, s1a.ot_reduction, s1a.ot_reduction_calc, s1a.ot_deduction_amount, s1a.ot_deduction_ssn, s1a.ot_deduction_claim, s1a.ot_deduction, s1a.part3, s1a.part3_ssn, s1a.overtime, s1a.ot_ssn, s1a.no, s1a.zero, f1040.status, param:household.no; the mutant reads s1a.ot_reduction_calc.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_deduction_ssn.zero.then0` (replace an operand, s1a.s1a.ot_deduction_ssn): s1a.ot_deduction_ssn's s1a.ot_ssn-false alternative is s1a.zero; the mutant reads s1a.ot_deduction_figured, s1a.ot_capped less s1a.ot_reduction, floored at zero. s1a.ot_deduction_ssn is read only by s1a.ot_deduction_claim, and s1a.ot_deduction_claim only by s1a.ot_deduction, in its s1a.overtime-true alternative; where s1a.overtime is unknown s1a.ot_deduction is a choice whose other way, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever s1a.ot_deduction_ssn is (spec 4.7.3). Where s1a.overtime is true, s1a.part3 is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs and s1a.no (false) for mfs. With s1a.ot_ssn known false and the status known, s1a.part3 is false, so s1a.ot_capped and s1a.ot_reduction take s1a.zero and s1a.ot_deduction_figured is $0. With s1a.ot_ssn known false and the status unknown, s1a.part3 is that unknown, never a refusal, and so are s1a.ot_capped, s1a.ot_reduction and s1a.ot_deduction_figured (each a choice on s1a.part3 with an s1a.zero alternative, or their difference); s1a.ot_deduction_claim is then a choice on the unknown status whose mfs alternative, s1a.zero, never refuses, so it is the status's unknown on both routes. Where s1a.ot_ssn is unknown, s1a.part3 is false or unknown (s1a.overtime and the status are inputs, s1a.no a parameter), so s1a.ot_capped and s1a.ot_reduction are $0 or that unknown, never a refusal, and so is s1a.ot_deduction_figured; the base's s1a.zero is not a refusal either, so s1a.ot_deduction_ssn is s1a.ot_ssn's unknown on both routes. (Premises pinned: s1a.ot_deduction_ssn, s1a.ot_deduction_claim, s1a.ot_deduction, s1a.ot_deduction_figured, s1a.ot_capped, s1a.ot_reduction, s1a.part3, s1a.part3_ssn, s1a.no, param:household.no, s1a.ot_ssn, s1a.overtime, s1a.ot_ssn_count, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.ot_deduction_figured.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then0` (replace an operand, s1a.s1a.ot_deduction_claim): s1a.ot_deduction_claim's single alternative is s1a.ot_deduction_ssn; the mutant reads s1a.ot_deduction_amount. s1a.ot_deduction_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.ot_deduction_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is single, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.ot_deduction_ssn take s1a.ot_deduction_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.ot_magi_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.ot_deduction_amount is s1a.ot_capped, $0, which is s1a.ot_deduction_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.ot_magi_over is unknown and s1a.ot_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.ot_deduction_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.ot_deduction_claim, s1a.ot_deduction, s1a.ot_deduction_ssn, s1a.ot_deduction_amount, s1a.ot_deduction_figured, s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi, s1a.ot_threshold, s1a.ot_magi_over, s1a.part3, s1a.part3_ssn, s1a.no, param:household.no, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.ot_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then1` (replace an operand, s1a.s1a.ot_deduction_claim): s1a.ot_deduction_claim's mfj alternative is s1a.ot_deduction_ssn; the mutant reads s1a.ot_deduction_amount. s1a.ot_deduction_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.ot_deduction_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is mfj, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.ot_deduction_ssn take s1a.ot_deduction_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.ot_magi_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.ot_deduction_amount is s1a.ot_capped, $0, which is s1a.ot_deduction_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.ot_magi_over is unknown and s1a.ot_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.ot_deduction_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.ot_deduction_claim, s1a.ot_deduction, s1a.ot_deduction_ssn, s1a.ot_deduction_amount, s1a.ot_deduction_figured, s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi, s1a.ot_threshold, s1a.ot_magi_over, s1a.part3, s1a.part3_ssn, s1a.no, param:household.no, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.ot_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_deduction_claim.zero.then2` (replace an operand, s1a.s1a.ot_deduction_claim): s1a.ot_deduction_claim's married-filing-separately alternative is s1a.zero ($0); the mutant reads s1a.ot_deduction_amount. s1a.ot_deduction_claim is read only by s1a.ot_deduction, in its s1a.overtime-true alternative. Where s1a.overtime is unknown the claim line is a way of its reader (spec 4.7.3), whose other alternative, s1a.zero, never refuses, so that reader is s1a.overtime's unknown on both routes whatever the claim line is. With s1a.overtime true and the status known to be mfs, s1a.part3 (s1a.part3_ssn, whose mfs alternative is s1a.no, false) is false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold each take s1a.zero, s1a.ot_magi_over is false and s1a.ot_deduction_amount is s1a.ot_capped, $0: the two values agree. Where the status is unknown both are ways (spec 4.7.3). s1a.ot_ssn is any[all[status not mfj, household.taxpayer_work_ssn], all[status mfj, s1a.ot_ssn_count > 0]]; each all-test then meets the unknown status first, so it is false or unknown, never true, and never a refusal (s1a.ot_ssn_count and household.taxpayer_work_ssn are counts over the person roster with no refusal gates); so s1a.ot_ssn is false or unknown and s1a.ot_deduction_ssn is $0 or unknown, never a refusal, on the other four ways. The claim line is then the status's unknown on both routes. (Premises pinned: s1a.ot_deduction_claim, s1a.ot_deduction, s1a.ot_deduction_ssn, s1a.ot_deduction_amount, s1a.ot_deduction_figured, s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi, s1a.ot_threshold, s1a.ot_magi_over, s1a.part3, s1a.part3_ssn, s1a.no, param:household.no, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.ot_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then3` (replace an operand, s1a.s1a.ot_deduction_claim): s1a.ot_deduction_claim's hoh alternative is s1a.ot_deduction_ssn; the mutant reads s1a.ot_deduction_amount. s1a.ot_deduction_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.ot_deduction_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is hoh, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.ot_deduction_ssn take s1a.ot_deduction_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.ot_magi_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.ot_deduction_amount is s1a.ot_capped, $0, which is s1a.ot_deduction_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.ot_magi_over is unknown and s1a.ot_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.ot_deduction_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.ot_deduction_claim, s1a.ot_deduction, s1a.ot_deduction_ssn, s1a.ot_deduction_amount, s1a.ot_deduction_figured, s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi, s1a.ot_threshold, s1a.ot_magi_over, s1a.part3, s1a.part3_ssn, s1a.no, param:household.no, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.ot_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then4` (replace an operand, s1a.s1a.ot_deduction_claim): s1a.ot_deduction_claim's qss alternative is s1a.ot_deduction_ssn; the mutant reads s1a.ot_deduction_amount. s1a.ot_deduction_claim's only reader is s1a.ot_deduction, a choice on s1a.overtime (false: s1a.zero; true: s1a.ot_deduction_claim). Where s1a.overtime is false the claim line is not read. Where s1a.overtime is unknown the claim line is a way of s1a.ot_deduction (spec 4.7.3), but s1a.ot_deduction's other alternative, s1a.zero, never refuses, so s1a.ot_deduction is s1a.overtime's unknown on both routes whatever the claim line is. Where s1a.overtime is true and the status is qss, s1a.part3, a choice on s1a.overtime whose true alternative is s1a.part3_ssn, a choice on the status that takes s1a.ot_ssn for every status but mfs (s1a.no, false, for mfs), has s1a.ot_ssn's value: s1a.ot_ssn true makes s1a.ot_deduction_ssn take s1a.ot_deduction_amount, the same memoized line; s1a.ot_ssn false makes s1a.part3 false, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold take s1a.zero, s1a.ot_magi_over (is s1a.ot_magi more than s1a.ot_threshold) is false and s1a.ot_deduction_amount is s1a.ot_capped, $0, which is s1a.ot_deduction_ssn's s1a.zero; s1a.ot_ssn unknown makes s1a.part3 that unknown, so s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi and s1a.ot_threshold, each a choice on s1a.part3 with an s1a.zero alternative, are unknown, s1a.ot_magi_over is unknown and s1a.ot_deduction_amount, whose two alternatives are then unknown, is unknown; s1a.ot_deduction_ssn, a choice on s1a.ot_ssn with an s1a.zero alternative, is unknown too (spec 4.7.3), and unknowns are one value to the mutation run. s1a.ot_ssn is never a refusal: it reads only the status, household.taxpayer_work_ssn and s1a.ot_ssn_count, counts over the person roster with no refusal gates. Where the status is unknown, the claim line's married-filing-separately alternative, s1a.zero, is a way that never refuses, so the claim line is the status's unknown on both routes (spec 4.7.3). (Premises pinned: s1a.ot_deduction_claim, s1a.ot_deduction, s1a.ot_deduction_ssn, s1a.ot_deduction_amount, s1a.ot_deduction_figured, s1a.ot_capped, s1a.ot_reduction, s1a.ot_magi, s1a.ot_threshold, s1a.ot_magi_over, s1a.part3, s1a.part3_ssn, s1a.no, param:household.no, s1a.ot_ssn, s1a.ot_ssn_count, s1a.overtime, household.taxpayer_work_ssn, household.taxpayer_work_ssn_count, s1a.zero; the mutant reads s1a.ot_deduction_amount.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.vli_capped_calc.vli_total` (replace an operand, s1a.s1a.vli_capped_calc): Guarded figure: s1a.vli_total is s1a.vli_total_all wherever s1a.carloan holds, and every printed line reads s1a.vli_capped_calc (a helper) only through choices whose guards make s1a.carloan true, which, where a guard is unknown, are that unknown whatever s1a.vli_capped_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.carloan does not hold only s1a.vli_capped_calc's own, unprinted value can differ.
- `operand.s1a.s1a.vli_over_calc.vli_magi` (replace an operand, s1a.s1a.vli_over_calc): Guarded figure: s1a.vli_magi is s1a.vli_magi_calc wherever s1a.part4 holds, and every printed line reads s1a.vli_over_calc (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.vli_over_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.vli_over_calc's own, unprinted value can differ.
- `operand.s1a.s1a.vli_over.zero.then0` (replace an operand, s1a.s1a.vli_over): Branch settled by its guard: where s1a.vli_over takes alternative 0 (guard {
  "eq": [
    "s1a.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.vli_magi make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.vli_magi_over` (replace strict greater-than with inclusive, s1a.s1a.vli_magi_over): The test 's1a.vli_magi more than s1a.vli_threshold' made inclusive adds only s1a.vli_magi = s1a.vli_threshold; there s1a.vli_over_pos is zero, the reduction s1a.vli_reduction is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.vli_deduction_figured (s1a.vli_capped less s1a.vli_reduction) equals s1a.vli_capped, the value the other branch gives. The test is read only by s1a.vli_deduction_amount. (structural conditions re-checked this run.)
- `operand.s1a.s1a.vli_magi_over.vli_threshold.gt.1` (replace an operand, s1a.s1a.vli_magi_over): Guarded figure: s1a.vli_threshold is s1a.vli_threshold_calc wherever s1a.part4 holds, and every printed line reads s1a.vli_magi_over (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.vli_magi_over is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.vli_magi_over's own, unprinted value can differ.
- `operand.s1a.s1a.vli_over_pos.vli_threshold` (replace an operand, s1a.s1a.vli_over_pos): Guarded figure: s1a.vli_threshold is s1a.vli_threshold_calc wherever s1a.part4 holds, and every printed line reads s1a.vli_over_pos (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.vli_over_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.vli_over_pos's own, unprinted value can differ.
- `operand.s1a.s1a.vli_reduction.zero.then0` (replace an operand, s1a.s1a.vli_reduction): Branch settled by its guard: where s1a.vli_reduction takes alternative 0 (guard {
  "eq": [
    "s1a.part4",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.line28_thousands make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.vli_deduction_figured.vli_reduction` (replace an operand, s1a.s1a.vli_deduction_figured): Guarded figure: s1a.vli_reduction is s1a.vli_reduction_calc wherever s1a.part4 holds, and every printed line reads s1a.vli_deduction_figured (a helper) only through choices whose guards make s1a.part4 true, which, where a guard is unknown, are that unknown whatever s1a.vli_deduction_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part4 does not hold only s1a.vli_deduction_figured's own, unprinted value can differ.
- `operand.s1a.s1a.vli_deduction.zero.then0` (replace an operand, s1a.s1a.vli_deduction): s1a.vli_deduction's carloan-false alternative is s1a.zero; the mutant reads s1a.vli_deduction_figured, line24 less line29, floored at zero, both choices on s1a.part4 (carloan true) between s1a.zero and their figures. With carloan known false, part4 is false and both are $0, so s1a.vli_deduction_figured is $0. Where carloan is unknown, part4 is that unknown, line24 and line29 are $0 or unknown, never a refusal (spec 4.7.3), and so is s1a.vli_deduction_figured; s1a.vli_deduction is then carloan's unknown on both routes. (Premises pinned: s1a.vli_deduction, s1a.vli_deduction_figured, s1a.vli_capped, s1a.vli_reduction, s1a.part4, s1a.carloan, s1a.zero; the mutant reads s1a.vli_deduction_figured.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.senior_over_calc.senior_magi` (replace an operand, s1a.s1a.senior_over_calc): Guarded figure: s1a.senior_magi is s1a.senior_magi_calc wherever s1a.part5 holds, and every printed line reads s1a.senior_over_calc (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.senior_over_calc is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.senior_over_calc's own, unprinted value can differ.
- `operand.s1a.s1a.senior_over.zero.then0` (replace an operand, s1a.s1a.senior_over): Branch settled by its guard: where s1a.senior_over takes alternative 0 (guard {
  "eq": [
    "s1a.part5",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.senior_magi make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `boundary.s1a.s1a.senior_magi_over` (replace strict greater-than with inclusive, s1a.s1a.senior_magi_over): The test 's1a.senior_magi more than s1a.senior_threshold' made inclusive adds only s1a.senior_magi = s1a.senior_threshold; there s1a.senior_over_pos is zero, the reduction s1a.senior_reduction is zero (zero in whole $1,000 steps, or 6% of zero), and s1a.senior_phased_figured (s1a.senior_amount less s1a.senior_reduction) equals s1a.senior_amount, the value the other branch gives. The test is read only by s1a.senior_phased_calc. (structural conditions re-checked this run.)
- `operand.s1a.s1a.senior_magi_over.senior_threshold.gt.1` (replace an operand, s1a.s1a.senior_magi_over): Guarded figure: s1a.senior_threshold is s1a.senior_threshold_calc wherever s1a.part5 holds, and every printed line reads s1a.senior_magi_over (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.senior_magi_over is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.senior_magi_over's own, unprinted value can differ.
- `operand.s1a.s1a.senior_over_pos.senior_threshold` (replace an operand, s1a.s1a.senior_over_pos): Guarded figure: s1a.senior_threshold is s1a.senior_threshold_calc wherever s1a.part5 holds, and every printed line reads s1a.senior_over_pos (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.senior_over_pos is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.senior_over_pos's own, unprinted value can differ.
- `operand.s1a.s1a.senior_reduction.zero.then0` (replace an operand, s1a.s1a.senior_reduction): Branch settled by its guard: where s1a.senior_reduction takes alternative 0 (guard {
  "eq": [
    "s1a.part5",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.zero and s1a.senior_over_pos make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.senior_phased_figured.senior_reduction` (replace an operand, s1a.s1a.senior_phased_figured): Guarded figure: s1a.senior_reduction is s1a.senior_reduction_calc wherever s1a.part5 holds, and every printed line reads s1a.senior_phased_figured (a helper) only through choices whose guards make s1a.part5 true, which, where a guard is unknown, are that unknown whatever s1a.senior_phased_figured is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where s1a.part5 does not hold only s1a.senior_phased_figured's own, unprinted value can differ.
- `operand.s1a.s1a.senior_phased.senior_phased_calc.then1` (replace an operand, s1a.s1a.senior_phased): Branch equal under a case split: where s1a.senior_phased takes alternative 1 (guard {
  "eq": [
    "s1a.part5",
    {
      "const": true
    }
  ],
  "op": "test"
}
), s1a.senior_phased_calc and s1a.senior_phased_figured have the same value in every case of s1a.senior_magi_over (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged), through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.s1a.s1a.senior_you_claim.zero.then2` (replace an operand, s1a.s1a.senior_you_claim): s1a.senior_you_claim's married-filing-separately alternative is s1a.zero; the mutant reads s1a.senior_phased, a choice on s1a.part5 (all[senior_any, status not mfs]) between s1a.zero and s1a.senior_phased_calc. With the status known to be mfs, part5 is false and line35 is s1a.zero: the two values agree. Where the status is unknown both are ways (spec 4.7.3): part5 is false or unknown (senior_any compares s1a.senior_count with 0, and senior_count counts the person entries whose person.senior_work_ssn is true, a choice on person.age65 between the input work_ssn and person.no (a parameter); age65 is an any-test on the input birth_year and born_jan1_if_cut_year, a choice on birth_cut_year (tests of birth_year) between the input born_jan1 and person.no; none has a refusal gate), so line35 is $0 or that unknown, never a refusal, as the base's s1a.zero is; the claim line is then the status's unknown on both routes. (Premises pinned: s1a.senior_you_claim, s1a.senior_phased, s1a.part5, s1a.senior_any, s1a.senior_count, person.senior_work_ssn, person.work_ssn, person.age65, person.birth_year, person.born_jan1_if_cut_year, person.birth_cut_year, person.born_jan1, person.no, s1a.zero; the mutant reads s1a.senior_phased.) (structural conditions re-checked this run.)
- `operand.s1a.s1a.part3_ssn.ot_ssn.then0` (replace an operand, s1a.s1a.part3_ssn): Branch equal under a case split: where s1a.part3_ssn takes alternative 0 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "single"
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "s1a.overtime",
    {
      "const": true
    }
  ],
  "op": "test"
}
 on its one reader path), s1a.ot_ssn and s1a.part2_ssn have the same value in every case of household.taxpayer_work_ssn (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged), through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.s1a.s1a.part3_ssn.no.then2` (replace an operand, s1a.s1a.part3_ssn): Branch settled by its guard: where s1a.part3_ssn takes alternative 2 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "mfs"
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that s1a.no and s1a.part2_ssn make, and both reduce to the same value (through settled choices, copies, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since neither s1a.no nor s1a.part2_ssn ever refuses (spec 4.7.3); so the mutated line is unchanged at every input.
- `operand.s1a.s1a.part3_ssn.ot_ssn.then3` (replace an operand, s1a.s1a.part3_ssn): Branch equal under a case split: where s1a.part3_ssn takes alternative 3 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "hoh"
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "s1a.overtime",
    {
      "const": true
    }
  ],
  "op": "test"
}
 on its one reader path), s1a.ot_ssn and s1a.part2_ssn have the same value in every case of household.taxpayer_work_ssn (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged), through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.s1a.s1a.part3_ssn.ot_ssn.then4` (replace an operand, s1a.s1a.part3_ssn): Branch equal under a case split: where s1a.part3_ssn takes alternative 4 (guard {
  "eq": [
    "f1040.status",
    {
      "const": "qss"
    }
  ],
  "op": "test"
}
) and its value can reach a printed line (guards {
  "eq": [
    "s1a.overtime",
    {
      "const": true
    }
  ],
  "op": "test"
}
 on its one reader path), s1a.ot_ssn and s1a.part2_ssn have the same value in every case of household.taxpayer_work_ssn (each value, and unanswered or refused, which the choices and comparisons that read it pass on unchanged), through settled choices, copies, comparisons of complete values and arithmetic of zeros, so no printed value changes.
- `operand.s2.s2.amt_rel.zero.then1` (replace an operand, s2.s2.amt_rel): s2.amt_rel is a choice on s2.amt_dep_any (eq true, then eq false; exhaustive for a Bool): true takes s2.amt_rel_items, false takes s2.zero (the parameter sales.zero, $0); the mutant reads s2.amt_dep in place of s2.zero. amt_dep_any is the test amt_dep > 0. Where it is a known false, amt_dep is a known NonNegDollars amount not more than 0, so $0, the value s2.zero gives. Where it is true both routes take amt_rel_items; where it is a refusal (a comparison passes its operand's refusal, spec 4.7.2) the first guard ends both routes with it. Where it is unknown, amt_dep is not a refusal (the test would be that refusal), so neither second way refuses, no route has every way a refusal, and amt_rel is amt_dep_any's unknown on both routes (spec 4.7.3). No value of amt_rel changes. (Premises pinned: s2.amt_rel, s2.amt_dep_any, s2.amt_dep, s2.zero, param:sales.zero; the mutant reads s2.amt_dep.) (structural conditions re-checked this run.)
- `operand.s2.s2.amt_l15.amt_l13.then1` (replace an operand, s2.s2.amt_l15): s2.amt_l15 is a choice on f1040.gate.sdtw (eq true, then eq false; exhaustive for a Bool): true takes s2.amt_l15_sdtw, false takes s2.amt_l13; the mutant reads s2.amt_l13_14, the sum of s2.amt_l13 and s2.amt_l14, in place of amt_l13. amt_l14 is a choice on the same guard, false taking s2.zero (the parameter sales.zero, $0). Where sdtw is a known false, amt_l14 is $0, so the sum is amt_l13 when amt_l13 is an amount, and amt_l13's own refusal or unknown otherwise (a sum takes its first refusal, else its first unknown, spec 4.7.4; the known $0 adds no mark). Where sdtw is true both routes take amt_l15_sdtw; where it is a refusal it ends both. Where it is unknown, amt_l14's ways are sd.line19 and the never-refusing s2.zero, so amt_l14 is an unknown, never a refusal, and amt_l13_14 is a refusal exactly where amt_l13 is: the second way refuses on one route exactly where it does on the other, so amt_l15 is the first way's refusal (amt_l15_sdtw's) on both routes or sdtw's unknown on both (spec 4.7.3). No value of amt_l15 changes. (Premises pinned: s2.amt_l15, s2.amt_l13_14, s2.amt_l14, s2.zero, param:sales.zero; the mutant reads s2.amt_l13_14.) (structural conditions re-checked this run.)
- `operand.s2.s2.line21.other_additional_total` (replace an operand, s2.s2.line21): Copy-chain identity: s2.other_additional_total and s2.hsa_distribution_tax expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2b.zero` (replace an operand, s8812.s8812.line2b): Copy-chain identity: s8812.zero and s8812.line2a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2c.zero` (replace an operand, s8812.s8812.line2c): Copy-chain identity: s8812.zero and s8812.line2b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2d.line2a` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2a and s8812.line2b, s8812.line2c are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line2d.line2b` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2b and s8812.line2a, s8812.line2c are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line2d.line2c` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2c and s8812.line2a, s8812.line2b are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line14.line13` (replace an operand, s8812.s8812.line14): Copy-chain identity: s8812.line13 and s8812.clw_a5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.eiw_3.zero` (replace an operand, s8812.s8812.eiw_3): Gated zero carried earlier: s8812.zero is an ungated zero and s8812.eiw_1b the same zero behind refusal gates (s8812.combat_pay); s8812.eiw_3sum, read first, reaches s8812.eiw_1b through ungated arithmetic, so whenever s8812.eiw_1b refuses or is unknown s8812.eiw_3sum already is, and is returned first, and otherwise both operands are zero.
- `operand.sa.sa.medical_premiums_if_not_large.no.then1` (replace an operand, sa.sa.medical_premiums_if_not_large): sa.medical_premiums_if_not_large is a choice on sa.medical_any: false takes the premiums answer sa.medical_premiums, true takes sa.no (the parameter household.no, false); the mutant reads sa.age65 in place of sa.no. Its only reader is sa.medical_asked, any[medical_any is true, medical_premiums_if_not_large is true, e05_claimed is true], evaluated in order: where sa.medical_any is true the first disjunct decides the any-test and the line is not read (an any-test returns at its first true disjunct). Where sa.medical_any is a refusal the guard refuses and both routes are that refusal. Where it is unknown both alternatives are ways (spec 4.7.3); the first way, the input sa.medical_premiums, is never a refusal, so the line is sa.medical_any's unknown on both routes. (Premises pinned: sa.medical_premiums_if_not_large, sa.medical_asked, sa.medical_any, sa.medical_premiums, sa.no, param:household.no; the mutant reads sa.age65.) (structural conditions re-checked this run.)
- `operand.sa.sa.home_other_if_not_owner.no.then1` (replace an operand, sa.sa.home_other_if_not_owner): sa.home_other_if_not_owner is a choice on sa.home_owner: false takes the answer sa.home_other, true takes sa.no (the parameter household.no, false); the mutant reads sa.e05_claimed in place of sa.no. Its only reader is sa.home_asked, any[home_owner is true, home_other_if_not_owner is true], evaluated in order: where sa.home_owner is true the first disjunct decides the any-test and the line is not read. Where sa.home_owner is a refusal the guard refuses and both routes are that refusal. Where it is unknown both alternatives are ways (spec 4.7.3); the first way, the input sa.home_other, is never a refusal, so the line is sa.home_owner's unknown on both routes. (Premises pinned: sa.home_other_if_not_owner, sa.home_asked, sa.home_owner, sa.home_other, sa.no, param:household.no; the mutant reads sa.e05_claimed.) (structural conditions re-checked this run.)
- `operand.sa.sa.line3.line2` (replace an operand, sa.sa.line3): Copy-chain identity: sa.line2 and sa.agi_floor expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line8b.zero` (replace an operand, sa.sa.line8b): Copy-chain identity: sa.zero and sa.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line8c.zero` (replace an operand, sa.sa.line8c): Copy-chain identity: sa.zero and sa.line8b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.gift_carryover_amount.zero` (replace an operand, sa.sa.gift_carryover_amount): Copy-chain identity: sa.zero and sa.line8c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.other_itemized.zero.then1` (replace an operand, sa.sa.other_itemized): Copy-chain identity: sa.zero and sa.casualty_loss expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.deduction.standard.then1` (replace an operand, sa.sa.deduction): sa.deduction's itemizes-false alternative: the mutant changes only deduction's own expression, so its refusal gates, mfs_joint_paid_if_itemizing and charity_over_if_itemizing, evaluated before its alternatives, are the same on both routes. An any-test is known false only when every disjunct was evaluated and false with no unknown remembered (spec 4.7.2), so mfs_spouse_itemizes is known false and the comparison of total_itemized (line 17) with sa.standard read standard as a known value; a known standard passed its gates and took its mfs_spouse_itemizes-false alternative, whose value is standard_amount, the same memoized value. Where itemizes is unknown both alternatives are ways (spec 4.7.3): every disjunct was then evaluated with no true one and no refusal, so total_itemized, the itemized alternative and the comparison's operand, is not a refusal, and deduction is that unknown on both routes. (Premises pinned: sa.standard, sa.deduction, sa.itemizes, sa.standard_amount, sa.mfs_spouse_itemizes, sa.elect_itemize, sa.total_itemized; the mutant reads sa.standard_amount.) (structural conditions re-checked this run.)
- `operand.sales.sales.bad_aggregate.no.then1` (replace an operand, sales.sales.bad_aggregate): bad_aggregate is a choice on the route gate line route_if_chosen (an Enum(sales_route)): aggregate takes aggregate_fails, detail takes sales.no (the parameter household.no, false); the mutant reads bad_code in place of sales.no. bad_aggregate is read only by sales.one, as its third refusal gate, after bad_code (the second); gates are evaluated in order and a gate that is not a known false ends the list (spec 4.7.1), so bad_aggregate is read only where bad_code is a memoized false in the sale's frame (spec 4.7.6), the value of sales.no. Where route_if_chosen is a refusal, the first guard refuses and bad_aggregate is that refusal on both routes. Where it is unknown both alternatives are ways (spec 4.7.3), and aggregate_fails's way is not the only one: sales.no and the memoized bad_code are not refusals, so bad_aggregate is the route's unknown on both routes. (Premises pinned: sales.bad_aggregate, sales.one, sales.bad_code, sales.route_if_chosen, sales.aggregate_fails, sales.digital, sales.special, sales.no, param:household.no, enum:sales_route; the mutant reads sales.bad_code.) (structural conditions re-checked this run.)
- `boundary.sc.sc.ho_over` (replace strict greater-than with inclusive, sc.sc.ho_over): The home office test 'square feet more than the cap' made inclusive adds only square feet equal to the cap, where the rate times the square feet and the rate times the cap are the same amount. The test is read only by line 4. (structural conditions re-checked this run.)
- `operand.sc.sc.f7206_line9.zero.then1` (replace an operand, sc.sc.f7206_line9): sc.f7206_line9's f7206_has-false alternative is sc.zero; the mutant reads sc.f7206_line8, line 4 less line 7, floored at zero. f7206_has is line 4 (profit_pos, sc.result floored at zero) more than sc.zero. With it known false line 4 is $0 and line 7 takes sc.zero, so line 8 is $0. Where f7206_has is unknown, line 4 is unknown (a refused line 4 refuses the guard and both routes alike), and line 7, a choice on f7206_has with an sc.zero alternative, is unknown (spec 4.7.3); line 8 is then unknown, never a refusal, and line 9 is f7206_has's unknown on both routes. (Premises pinned: sc.f7206_line9, sc.f7206_line8, sc.f7206_line4, sc.f7206_line7, sc.f7206_has, sc.profit_pos, sc.zero; the mutant reads sc.f7206_line8.) (structural conditions re-checked this run.)
- `operand.sc.sc.f7206_min.f7206_line13` (replace an operand, sc.sc.f7206_min): Copy-chain identity: sc.f7206_line13 and sc.f7206_line10 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sc.sc.f7206_unused.f7206_line14` (replace an operand, sc.sc.f7206_unused): Guarded figure: sc.f7206_line14 is sc.f7206_min wherever sc.hi_uses holds, and every printed line reads sc.f7206_unused (a helper) only through choices whose guards make sc.hi_uses true, which, where a guard is unknown, are that unknown whatever sc.f7206_unused is (another alternative still possible never refuses, or neither operand ever refuses; spec 4.7.3), so the replacement changes no printed value; where sc.hi_uses does not hold only sc.f7206_unused's own, unprinted value can differ.
- `operand.sc.sc.f7206_unused_if_uses.zero.then1` (replace an operand, sc.sc.f7206_unused_if_uses): Branch settled by its guard: where sc.f7206_unused_if_uses takes alternative 1 (guard {
  "eq": [
    "sc.hi_uses",
    {
      "const": false
    }
  ],
  "op": "test"
}
), the lines that guard compares are complete and fix the choices that sc.zero and sc.f7206_line14 make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
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
- `filter.sche.sche.rents` (remove collection filter, sche.sche.rents): sche.rents sums rental.line3 over the rentals where rental.reported (rental.excluded eq false); the mutant sums every rental. rental.line3 is a choice on rental.excluded: true takes rental.zero ($0), false takes rental.rents (an input). A rental with excluded known true adds $0 on the mutant's route and is skipped on the data's; one with excluded false is summed on both. One with excluded unknown makes the data's sum unknown (its where-test is unknown) and makes rental.line3 unknown on the mutant's (spec 4.7.3: rental.zero never refuses, so not every way refuses), so the sum is unknown on both. rental.excluded is a test on inputs and lines with no refusal gate, and rental.line3 has none, so neither route meets a refusal the other does not. (Premises pinned: sche.rents, rental.line3, rental.reported, rental.excluded, rental.rents, rental.zero, param:sales.zero.) (structural conditions re-checked this run.)
- `filter.sche.sche.rent_income` (remove collection filter, sche.sche.rent_income): sche.rent_income sums rental.net_income (subtract_floor0 from rental.line21 take rental.zero) over the rentals where rental.reported (rental.excluded eq false); the mutant sums every rental. rental.line21 is a choice on rental.excluded whose first alternative, excluded true, is rental.zero ($0): an excluded rental's net income is $0 on the mutant's route and skipped on the data's. With excluded unknown, the data's where-test is unknown and rental.line21 is unknown (its way rental.zero never refuses, spec 4.7.3), so both sums are unknown. With excluded false both sum the same value, refusals included, in the same roster order. (Premises pinned: sche.rent_income, rental.net_income, rental.line21, rental.reported, rental.excluded, rental.zero, param:sales.zero.) (structural conditions re-checked this run.)
- `filter.sche.sche.rent_netloss` (remove collection filter, sche.sche.rent_netloss): sche.rent_netloss sums rental.net_loss (subtract_floor0 from rental.zero take rental.line21) over the rentals where rental.reported (rental.excluded eq false); the mutant sums every rental. rental.line21 is a choice on rental.excluded whose first alternative, excluded true, is rental.zero ($0), so an excluded rental's net loss is $0 on the mutant's route and skipped on the data's. With excluded unknown, the data's where-test is unknown and rental.line21 is unknown (its way rental.zero never refuses, spec 4.7.3), so both sums are unknown. With excluded false both sum the same value, refusals included, in the same roster order. (Premises pinned: sche.rent_netloss, rental.net_loss, rental.line21, rental.reported, rental.excluded, rental.zero, param:sales.zero.) (structural conditions re-checked this run.)
- `operand.scveh.scveh.is_actual_leased.no.then1` (replace an operand, scveh.scveh.is_actual_leased): Branch equal under a case split: where scveh.is_actual_leased takes alternative 1 (guard {
  "eq": [
    "scveh.is_actual_leased_test1",
    {
      "const": false
    }
  ],
  "op": "test"
}
), scveh.no and scveh.on_auto_limits have the same value, through settled choices, copies, comparisons of complete values and arithmetic of zeros, so the mutated line is unchanged at every input.
- `operand.scveh.scveh.claims_bonus_this_year.no.then1` (replace an operand, scveh.scveh.claims_bonus_this_year): scveh.claims_bonus_this_year is a choice on scveh.placed_this_year: true takes scveh.claims_bonus, false takes scveh.no (the parameter household.no, false); the mutant takes scveh.low_use (over_half false) in place of scveh.no. placed_this_year is the test 'scveh.year eq 1', and scveh.year is a keyed lookup of the recovery_year table on the input scveh.placed, whose one refusal gate is scveh.low_use. A gate that is not a known false stops the line at entry with the gate's refusal or unknown (spec 4.7.1), so placed, year and placed_this_year are known only where low_use is a known false: where placed_this_year is false, low_use is false, the value scveh.no gives. Where placed_this_year is true both routes take claims_bonus; where it is a refusal the choice is that refusal on both. Where it is unknown both alternatives are ways (spec 4.7.3); scveh.no and low_use (a test of bm_c against nonbusiness_c, products and a sum of inputs and the parameter sc.one_cent, with no refusal gate) never refuse, so the choice is placed_this_year's unknown on both routes. (Premises pinned: scveh.claims_bonus_this_year, scveh.placed_this_year, scveh.year, scveh.placed, scveh.low_use, scveh.over_half, scveh.bm_c, scveh.nonbusiness_c, scveh.cm_c, scveh.om_c, scveh.cent, scveh.miles_business, scveh.miles_commuting, scveh.miles_other, scveh.no, param:household.no, param:sc.one_cent, table:recovery_year; the mutant reads scveh.low_use.) (structural conditions re-checked this run.)
- `operand.scveh.scveh.bonus_forty.line15` (replace an operand, scveh.scveh.bonus_forty): Copy-chain identity: scveh.line15 and scveh.bonus_full expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.scveh.scveh.line17.line16` (replace an operand, scveh.scveh.line17): Floor-minus-min identity: scveh.line17 is scveh.line11 less scveh.line16, floored at zero, and one of scveh.line16 and scveh.bonus_allowed is the ungated smaller of scveh.line11 and the other, so scveh.line11 less either, floored at zero, is the same at every input; scveh.line11 is read first on both routes and the other operand second, so the same refusal or unknown wins.
- `operand.scveh.scveh.l5.k5` (replace an operand, scveh.scveh.l5): scveh.l5 looks up the vehicle's year-5 limit; the mutant looks up year 4. Only a 2019 vehicle's scveh.l5 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.first_year_after_recovery, so scveh.year and scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on first_year_after_recovery taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.d5.l5` (replace an operand, scveh.scveh.d5): scveh.d5 is min(l5, t5); the mutant reads d4 = min(l4, t4) in place of l5, and min(min(l4, t4), t5) = min(l5, t5) when l4 = l5 and t4 >= t5. Only a 2019 vehicle's scveh.d5 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.first_year_after_recovery, so scveh.year and scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on first_year_after_recovery taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.l6.k6` (replace an operand, scveh.scveh.l6): scveh.l6 looks up the vehicle's year-6 limit; the mutant looks up year 5. Only a 2019 vehicle's scveh.l6 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.first_year_after_recovery, so scveh.year and scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on first_year_after_recovery taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
- `operand.scveh.scveh.d6.l6` (replace an operand, scveh.scveh.d6): scveh.d6 is min(l6, t6); the mutant reads d5 = min(l5, t5) in place of l6, and min(min(l5, t5), t6) = min(l6, t6) when l5 = l6 and t5 >= t6. Only a 2019 vehicle's scveh.d6 reaches a printed line (every reader path passes a choice taken only for a 2019 vehicle), and for it the auto_limit rows for years 4, 5 and 6 hold one limit and every 5-year GDS column's rates do not increase from year 4 to year 6. Where that choice's guard (scveh.first_year_after_recovery, so scveh.year and scveh.placed) is unknown it evaluates the alternative as a way (spec 4.7.3), and its value matters there only through its refusals. Those are the same on both routes: the line and the mutant read only ungated lookups keyed on scveh.placed and parameters (and, for d5 and d6, the basis scveh.b100, in the same operand order), so they refuse at the same inputs with the same refusal; and every reader from the line to the choice passes refusals on unchanged and makes none of its own: d5 or d6 (smaller_of), d_total (sum), unrecovered (subtract_floor0), post_amount (smaller_of) and post (prorate), all without refusal gates, each returning the first refusal among its operands, then macrs_pass, a choice on first_year_after_recovery taking post only as a line-valued alternative. The mutation tool checks that chain (readerSteps' transparent steps) before it applies the argument. (structural conditions re-checked this run.)
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
- `operand.scveh.scveh.s179_this_year.zero.then1` (replace an operand, scveh.scveh.s179_this_year): Branch settled by its guard: where scveh.s179_this_year takes alternative 1 (guard {
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
), the lines that guard compares are complete and fix the choices that scveh.zero and scveh.s179_this_year make, and both reduce to the zero (through settled choices, copies and arithmetic of zeros, with refusal gates only among the line's own, already false); where its guards are unknown the line is that unknown on both routes, since the values compared, or another alternative still possible, cannot refuse while the guard is unknown (spec 4.7.3); so the mutated line is unchanged at every input.
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
- `operand.ssb.ssb.has_benefits.line1.gt.0` (replace an operand, ssb.ssb.has_benefits): Copy-chain identity: ssb.line1 and ssb.benefits_if_any expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ssb.ssb.line2.line1` (replace an operand, ssb.ssb.line2): Copy-chain identity: ssb.line1 and ssb.benefits_if_any expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.ssb.ssb.show16_18.mfs_together.all.1.any.0.eq.0` (replace an operand, ssb.ssb.show16_18): show16_18 is all[past7, any[mfs_together, past9]]; the mutant reads show10_15 (all[show8_9, past9], show8_9 being all[lines8_to_15, past7] and lines8_to_15 being mfs_together false) in place of mfs_together. With mfs_together true, line 8 is mfs_base with lived_apart false, that is ssb.zero, so line 9 (line 7 less line 8, floored) is line 7 and past9 is past7, true where the any-test is reached: both are true. With mfs_together false, show10_15 is past9 (past7 is already true), so the any-tests agree. mfs_together is unknown only when the status or lived_apart is unknown; then line 8 is unknown and line 9 is unknown or line 7's refusal (subtract evaluates both), so past9 is unknown or that refusal, which past7 has already returned: both any-tests are unknown. With past7 unknown (line 7 unknown, the outer test continuing past it), line 9 is unknown or line 8's refusal, so past9 is unknown or that refusal; show8_9 is false (mfs_together true) or unknown, and show10_15 is false or past9's value. With mfs_together true the base any-test is true and the mutant's is past9's unknown (line 8 is then $0); otherwise both any-tests are past9's value. The outer test, holding past7's unknown, is unknown on both routes, or the same refusal. (Premises pinned: ssb.show16_18, ssb.mfs_together, ssb.show10_15, ssb.show8_9, ssb.lines8_to_15, ssb.past7, ssb.past9, ssb.line9, ssb.line8, ssb.mfs_base, ssb.line7, ssb.zero, ssb.lived_apart; the mutant reads ssb.show10_15.) (structural conditions re-checked this run.)
- `operand.ssb.ssb.show16_18.past9.all.1.any.1.eq.0` (replace an operand, ssb.ssb.show16_18): show16_18 is all[past7, any[mfs_together, past9]]; the mutant reads show10_15, all[all[mfs_together false, past7], past9], in place of past9. The second disjunct is reached only when mfs_together was not true. With mfs_together false and past7 true (the outer test's first conjunct), show10_15 is past9. mfs_together is unknown only when the status or lived_apart is unknown; then line 8 is unknown, so past9 is unknown or line 7's refusal (already returned by past7): show10_15 is then unknown too, and both any-tests are unknown. With past7 unknown (line 7 unknown, the outer test continuing past it), past9 is unknown or line 8's refusal, and show10_15, all[show8_9 (unknown, since lines8_to_15 is true or unknown there and past7 is unknown), past9], is past9's value; the second disjuncts agree, and the outer test, holding past7's unknown, is unknown on both routes or the same refusal. (Premises pinned: ssb.show16_18, ssb.mfs_together, ssb.show10_15, ssb.show8_9, ssb.lines8_to_15, ssb.past7, ssb.past9, ssb.line9, ssb.line8, ssb.mfs_base, ssb.line7, ssb.zero, ssb.lived_apart; the mutant reads ssb.show10_15.) (structural conditions re-checked this run.)
- `operand.ssb.ssb.line16.line16_together.then0` (replace an operand, ssb.ssb.line16): ssb.line16's mfs_together-true alternative is line16_together, line 7 times 85%; the mutant reads line 15, line 11 times 85%, line 11 being line 9 less line 10 and line 9 line 7 less line 8, each floored at zero. mfs_together is all[status mfs, lived_apart false]; then line 8 and line 10 take mfs_base and mfs_adjust with lived_apart false, ssb.zero, so line 11 is line 7 and the two values agree. Lines 8 and 10 choose on the status, and mfs_base and mfs_adjust on lived_apart, among parameters only, so they are never refusals; line 15 is therefore a refusal exactly when line 7 is, with line 7's refusal, as line16_together is. Where mfs_together is unknown both alternatives are ways (spec 4.7.3): the first way refuses on both routes alike, and the other, line16_sum, is the same line, so line 16 is the same on both. (Premises pinned: ssb.line16, ssb.line16_together, ssb.line15, ssb.line11, ssb.line9, ssb.line10, ssb.line8, ssb.mfs_base, ssb.mfs_adjust, ssb.line7, ssb.mfs_together, ssb.lived_apart, ssb.zero; the mutant reads ssb.line15.) (structural conditions re-checked this run.)
- `operand.ssb.ssb.line18.zero.then1` (replace an operand, ssb.ssb.line18): ssb.line18 is a choice on has_benefits, the test 'line 1 more than sales.zero ($0)': true takes line18_figured, false takes ssb.zero (the parameter sales.zero, $0); the mutant takes line 17, line 1 times 85% (ssb.rate85), in place of ssb.zero. has_benefits is a known false only where line 1 is a known value not more than $0; line 1 is NonNegDollars, so it is $0, and $0 times 85% is $0, the value ssb.zero gives. Line 1 copies benefits_if_any and has no refusal gate, nor has line 17; where line 1 is unknown or a refusal, so is the guard: a refusal ends the choose on both routes; an unknown leaves both alternatives as ways (spec 4.7.3), and neither ssb.zero nor line 17 (then unknown, not a refusal) refuses, so line 18 is the guard's unknown on both routes. (Premises pinned: ssb.line18, ssb.line18_figured, ssb.has_benefits, ssb.line1, ssb.line17, ssb.zero, param:sales.zero, param:ssb.rate85; the mutant reads ssb.line17.) (structural conditions re-checked this run.)
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

## Keyed arguments, checked on a sample

Each keyed argument above is also checked by execution: the mutant and the data are evaluated on 300 generated
returns and the inputs of every fixture case, each as given and with answers withheld at rates 0.1, 0.3, 0.6;
every line on a value sheet that reads the mutated line must agree. A set reaches the mutant where the line it changes reads other
operands or has another value than under the data, and exercises it where a value it can change differs.
An argument over answered inputs only is held to the sets as given.
Known-killed controls (one fixture-killed mutant per line): 90 of 101 rejected by the same check.

| Argument | Held to | Sets | Reaching it | Exercising it | Result |
| --- | --- | --- | --- | --- | --- |
| operand.asset.asset.s179_bad_test2_test2.over_half.eq.0 | all sets | 661 | 661 | 661 | holds |
| operand.dependent.dependent.qc_age_younger.younger.then0 | all sets | 3135 | 3043 | 2324 | holds |
| operand.dependent.dependent.spouse_relative_joint.no.then0 | all sets | 3135 | 1370 | 643 | holds |
| operand.dependent.dependent.spouse_relative_joint.no.then2 | all sets | 3135 | 1039 | 312 | holds |
| operand.dependent.dependent.spouse_relative_joint.no.then3 | all sets | 3135 | 1603 | 876 | holds |
| operand.dependent.dependent.spouse_relative_joint.no.then4 | all sets | 3135 | 917 | 190 | holds |
| operand.dependent.dependent.qualifying_relative.no.then1 | all sets | 3135 | 208 | 0 | holds |
| operand.dependent.dependent.qr_dependent.no.then1 | all sets | 3135 | 2881 | 0 | holds |
| operand.dependent.dependent.odc_person.no.then1 | all sets | 3135 | 2420 | 218 | holds |
| operand.dependent.dependent.eic_ssn_child.no.then1 | all sets | 3135 | 2605 | 0 | holds |
| operand.dependent.dependent.dc_line2c.dc_incapable.all.1.eq.0 | answered returns | 485 | 95 | 86 | holds |
| operand.dependent.dependent.edu_adj.zero.then1 | all sets | 3135 | 3098 | 2152 | holds |
| operand.dependent.dependent.edu_over_refused.edu_no.then1 | all sets | 3135 | 3098 | 2152 | holds |
| operand.dependent.dependent.odc_from_tin.no.then1 | all sets | 3135 | 1365 | 88 | holds |
| operand.dependent.dependent.married_screen_qr.no | all sets | 3135 | 2448 | 2448 | holds |
| operand.dependent.dependent.married_screen_eic.no | all sets | 3135 | 2448 | 2448 | holds |
| operand.eic.eic.show_wsb6.self_employed.all.1.eq.0 | all sets | 12496 | 9465 | 9465 | holds |
| operand.eic.eic.step5_income.earned_for_limit.lt.0 | answered returns | 2383 | 2383 | 2130 | holds |
| operand.eic.eic.line1.earned_income.then0 | all sets | 12496 | 11027 | 9491 | holds |
| operand.eic.eic.line1_in_table.line1.ge.0 | all sets | 12496 | 12496 | 12496 | holds |
| operand.eic.eic.line1_table0.line1.key | all sets | 12496 | 12496 | 12496 | holds |
| operand.eic.eic.line1_table1.line1.key | all sets | 12496 | 12496 | 12496 | holds |
| operand.eic.eic.line1_table2.line1.key | all sets | 12496 | 12496 | 12496 | holds |
| operand.eic.eic.line1_table3.line1.key | all sets | 12496 | 12496 | 12496 | holds |
| operand.eic.eic.credit.line6.then0 | all sets | 12496 | 518 | 333 | holds |
| operand.eic.eic.check_27c.has_qc.any.3.all.1.eq.0 | answered returns | 2383 | 504 | 504 | holds; on a partial return: generated return 156 (seed 20261115), answers withheld at rate 0.6: f1040.line27c is unknown with the data and { "cite": { "doc": "i1040gi", "locator": "p. 42, Step 5, worksheet line 4; p. 43, Combat pay, nontaxable", "revision": "2025; printed date 2026-02-25", "snapsho... with the mutant |
| boundary.eic.eic.wsb_4b_positive | all sets | 12496 | 360 | 360 | holds |
| operand.eic.eic.from_step1_income.no.then1 | all sets | 12496 | 10586 | 1636 | holds |
| operand.f1116.f1116.line18_shown.line17.gt.0 | all sets | 12496 | 12496 | 0 | holds |
| operand.f1116.f1116.line24.line23 | all sets | 12496 | 12496 | 0 | holds |
| operand.f2441.f2441.line13_earned.line20.all.3.gt.1 | all sets | 12496 | 5032 | 5032 | holds |
| operand.f5695.f5695.part1_any.no.then1 | all sets | 12496 | 3431 | 0 | holds |
| operand.f5695.f5695.claiming_part1.no.then1 | all sets | 12496 | 12424 | 0 | holds |
| operand.f7203.f7203.line14.line11 | all sets | 277 | 277 | 9 | holds |
| operand.f8880.f8880.line3a_counted.zero.then1 | answered returns | 2383 | 308 | 16 | holds |
| operand.f8880.f8880.line3b_counted.zero.then1 | all sets | 12496 | 3451 | 17 | holds |
| operand.f8889.f8889.bad_months.counts_hold.then0 | all sets | 2645 | 1045 | 103 | holds |
| operand.f8889.f8889.bad_months.counts_hold.then1 | all sets | 2645 | 977 | 40 | holds |
| operand.f8889.f8889.age55_unmarried.age55.all.0.eq.0 | all sets | 2645 | 2645 | 2645 | holds |
| operand.f8889.f8889.family_dec_year.zero.then2 | all sets | 2645 | 2262 | 1023 | holds |
| operand.f8889.f8889.self_dec_year.zero.then2 | all sets | 2645 | 2262 | 1023 | holds |
| operand.f8889.f8889.testing_failed_figured.no.then1 | all sets | 2645 | 2631 | 0 | holds |
| operand.f8889.f8889.subject.line16.then0 | all sets | 2645 | 2623 | 1518 | holds |
| operand.f8959.f8959.total_tax.rrta_tax | all sets | 12496 | 12270 | 0 | holds |
| operand.f8962.f8962.marriage.no.then1 | all sets | 12496 | 9258 | 6138 | holds |
| operand.f8962.f8962.marriage.no.then2 | all sets | 12496 | 3860 | 740 | holds |
| operand.f8962.f8962.marriage.no.then3 | all sets | 12496 | 4064 | 944 | holds |
| operand.f8962.f8962.marriage.no.then4 | all sets | 12496 | 3466 | 346 | holds |
| operand.f8962.f8962.filing.applicable.all.1.any.0.eq.0 | all sets | 12496 | 1487 | 1487 | holds |
| operand.f8962.f8962.alien_branch.no.then1 | all sets | 12496 | 11794 | 11028 | holds |
| operand.household.household.hoh_community_property.no.then1 | all sets | 12496 | 4328 | 1208 | holds |
| operand.household.household.hoh_community_property.no.then2 | all sets | 12496 | 3860 | 740 | holds |
| operand.household.household.hoh_community_property.no.then4 | all sets | 12496 | 3466 | 346 | holds |
| operand.household.household.hoh_missed_test2.no.then1 | all sets | 12496 | 9361 | 8577 | holds |
| operand.household.household.hoh_missed_mfs.no.then1 | all sets | 12496 | 11756 | 8636 | holds |
| operand.ira.ira.mfs_cov_matters_trad.cov_you.all.1.eq.0 | answered returns | 2383 | 135 | 135 | holds |
| operand.k1p.k1p.active.decisions_if_asked.all.0.eq.0 | all sets | 349 | 349 | 0 | holds |
| operand.k1p.k1p.b1_neg.zero | all sets | 349 | 349 | 349 | holds |
| operand.k1p.k1p.b2_neg.zero | all sets | 349 | 349 | 349 | holds |
| operand.k1p.k1p.b3_neg.zero | all sets | 349 | 349 | 349 | holds |
| operand.k1s.k1s.ask_prior_active.tenth_if_active.all.1.eq.0 | all sets | 277 | 83 | 83 | holds |
| operand.k1s.k1s.loss1.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.loss2.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.loss3.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.loss7.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.loss8.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.np_loss.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.p1_income.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.p1_loss.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.p2_loss.zero | all sets | 277 | 277 | 277 | holds |
| operand.k1s.k1s.p3_loss.zero | all sets | 277 | 277 | 277 | holds |
| boundary.person.person.has_educator_expenses | all sets | 11665 | 9087 | 9087 | holds |
| operand.person.person.has_educator_expenses.educator_expenses_if_educator.gt.0 | all sets | 11665 | 11665 | 11665 | holds |
| operand.person.person.educator_eligible_amount.zero.then1 | all sets | 11665 | 11592 | 9028 | holds |
| operand.person.person.f4137_line6.zero.then1 | answered returns | 2383 | 2366 | 2366 | holds |
| operand.person.person.se_line6.zero.then1 | all sets | 11665 | 9711 | 9642 | holds |
| operand.person.person.eic_se.zero.then1 | all sets | 11665 | 10330 | 9711 | holds |
| operand.person.person.dc_earned.eic_se | all sets | 11665 | 11631 | 10296 | holds |
| operand.person.person.ira_dist_gate.no.then1 | all sets | 11665 | 11548 | 8810 | holds |
| operand.person.person.ira_se.zero.then1 | all sets | 11665 | 10330 | 9711 | holds |
| operand.person.person.edu_adj.zero.then1 | all sets | 11665 | 11530 | 8553 | holds |
| operand.qdcg.qdcg.line8.line7 | all sets | 12496 | 10987 | 0 | holds |
| boundary.rec.rec.w2a_line5_more | all sets | 12496 | 4678 | 4678 | holds |
| operand.rec.rec.w2a_line5_more.w2a_line3.gt.0 | all sets | 12496 | 12496 | 4 | holds |
| operand.rec.rec.w2a_line7_capped.zero.then1 | all sets | 12496 | 12490 | 4685 | holds |
| operand.rec.rec.w2a_line8_capped.zero.then1 | all sets | 12496 | 12490 | 4685 | holds |
| operand.rec.rec.to_line1.zero.then1 | answered returns | 2383 | 2358 | 2358 | holds |
| operand.rental.rental.home_pers10_if_any.zero.then1 | all sets | 410 | 359 | 276 | holds |
| operand.rental.rental.home.home_pers10_if_any.all.1.gt.0 | answered returns | 101 | 11 | 0 | holds |
| operand.rental.rental.net_loss.zero | all sets | 410 | 410 | 410 | holds |
| operand.royalty.royalty.loss_abs.zero | all sets | 64 | 43 | 43 | holds |
| boundary.s1a.s1a.tips_magi_over | all sets | 12496 | 9010 | 9010 | holds |
| operand.s1a.s1a.tips_magi_over.tips_threshold.gt.1 | all sets | 12496 | 12496 | 12381 | holds |
| operand.s1a.s1a.tips_deduction_figured.tips_reduction | all sets | 12496 | 12496 | 12381 | holds |
| operand.s1a.s1a.tips_deduction_ssn.zero.then0 | all sets | 12496 | 7543 | 902 | holds |
| operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then0 | all sets | 12496 | 9258 | 2447 | holds |
| operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then1 | all sets | 12496 | 4328 | 1180 | holds |
| operand.s1a.s1a.tips_deduction_claim.zero.then2 | all sets | 12496 | 3860 | 740 | holds |
| operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then3 | all sets | 12496 | 4064 | 303 | holds |
| operand.s1a.s1a.tips_deduction_claim.tips_deduction_ssn.then4 | all sets | 12496 | 3466 | 151 | holds |
| boundary.s1a.s1a.ot_magi_over | all sets | 12496 | 9062 | 9062 | holds |
| operand.s1a.s1a.ot_magi_over.ot_threshold.gt.1 | all sets | 12496 | 12496 | 12385 | holds |
| operand.s1a.s1a.ot_deduction_figured.ot_reduction | all sets | 12496 | 12496 | 12385 | holds |
| operand.s1a.s1a.ot_deduction_ssn.zero.then0 | all sets | 12496 | 7555 | 901 | holds |
| operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then0 | all sets | 12496 | 9258 | 2447 | holds |
| operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then1 | all sets | 12496 | 4328 | 1192 | holds |
| operand.s1a.s1a.ot_deduction_claim.zero.then2 | all sets | 12496 | 3860 | 740 | holds |
| operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then3 | all sets | 12496 | 4064 | 303 | holds |
| operand.s1a.s1a.ot_deduction_claim.ot_deduction_ssn.then4 | all sets | 12496 | 3466 | 151 | holds |
| boundary.s1a.s1a.vli_magi_over | all sets | 12496 | 8989 | 8989 | holds |
| operand.s1a.s1a.vli_deduction.zero.then0 | all sets | 12496 | 12349 | 8989 | holds |
| boundary.s1a.s1a.senior_magi_over | all sets | 12496 | 8572 | 8572 | holds |
| operand.s1a.s1a.senior_you_claim.zero.then2 | all sets | 12496 | 3860 | 740 | holds |
| operand.s2.s2.amt_rel.zero.then1 | all sets | 12496 | 12314 | 0 | holds |
| operand.s2.s2.amt_l15.amt_l13.then1 | all sets | 12496 | 10921 | 3126 | holds |
| operand.s8812.s8812.line18a.chart_eic.then0 | answered returns | 2383 | 226 | 226 | holds; on a partial return: generated return 99 (seed 20261115), answers withheld at rate 0.1: s8812.line19 is { "cite": { "doc": "i4562", "locator": "p. 14, Lines 26 and 27; p. 15, Column (f)", "revision": "2025", "snapshot": "5c1c95b78d557130f2afa0bd192bef352ef65e42ae6... with the data and unknown with the mutant |
| operand.sa.sa.medical_premiums_if_not_large.no.then1 | all sets | 12496 | 4467 | 1316 | holds |
| operand.sa.sa.home_other_if_not_owner.no.then1 | all sets | 12496 | 4863 | 1711 | holds |
| operand.sa.sa.deduction.standard.then1 | all sets | 12496 | 1971 | 0 | holds |
| operand.sales.sales.bad_aggregate.no.then1 | all sets | 1677 | 1645 | 1153 | holds |
| boundary.sc.sc.ho_over | all sets | 1469 | 9 | 9 | holds |
| operand.sc.sc.f7206_line9.zero.then1 | all sets | 1469 | 1148 | 89 | holds |
| filter.sche.sche.rents | all sets | 12496 | 410 | 81 | holds |
| filter.sche.sche.rent_income | all sets | 12496 | 410 | 81 | holds |
| filter.sche.sche.rent_netloss | all sets | 12496 | 410 | 81 | holds |
| operand.scveh.scveh.claims_bonus_this_year.no.then1 | all sets | 586 | 492 | 0 | holds |
| operand.scveh.scveh.l5.k5 | all sets | 586 | 550 | 550 | holds |
| operand.scveh.scveh.d5.l5 | all sets | 586 | 586 | 586 | holds |
| operand.scveh.scveh.l6.k6 | all sets | 586 | 550 | 550 | holds |
| operand.scveh.scveh.d6.l6 | all sets | 586 | 586 | 586 | holds |
| operand.sd.sd.to1040.line21.then0 | all sets | 12496 | 8416 | 0 | holds |
| operand.sdtw.sdtw.line4.zero.then1 | answered returns | 2383 | 2260 | 2260 | holds |
| operand.sdtw.sdtw.line17.line16 | all sets | 12496 | 10964 | 0 | holds |
| operand.sdtw.sdtw.line45.line43 | all sets | 12496 | 10986 | 10365 | holds |
| boundary.sli.sli.over | all sets | 12496 | 7 | 7 | holds |
| operand.sli.sli.line9.line8 | all sets | 12496 | 12496 | 11771 | holds |
| operand.ssb.ssb.show16_18.mfs_together.all.1.any.0.eq.0 | all sets | 12496 | 11087 | 11087 | holds |
| operand.ssb.ssb.show16_18.past9.all.1.any.1.eq.0 | all sets | 12496 | 10650 | 10650 | holds |
| operand.ssb.ssb.line16.line16_together.then0 | all sets | 12496 | 3826 | 668 | holds |
| operand.ssb.ssb.line18.zero.then1 | all sets | 12496 | 12254 | 9012 | holds |
| boundary.se.positive | all sets | 11665 | 3 | 3 | holds |
| param.eic.ws_threshold0.joint.$1 | all sets | 12496 | 12496 | 12496 | holds |
| param.eic.ws_threshold0.other.$1 | all sets | 12496 | 12496 | 12496 | holds |
| param.eic.ws_threshold1.joint.$1 | all sets | 12496 | 12496 | 12496 | holds |

- Controls the sample did not reject (its readers never differ on these sets; the kill is on the line itself or rests on a fixture's own answers): operand.dependent.dependent.dc_line2c.dc_qp.all.0.eq.0 (line:dependent.dependent.dc_line2c), operand.eic.eic.show_wsb6.eligible.all.0.eq.0 (line:eic.eic.show_wsb6), operand.eic.eic.wsb_4b_positive.wsb_4b.gt.0 (line:eic.eic.wsb_4b_positive), boundary.f1116.f1116.line18_shown (line:f1116.f1116.line18_shown), operand.f8962.f8962.filing.any.all.0.eq.0 (line:f8962.f8962.filing), operand.household.household.hoh_community_property.no.then0 (line:household.household.hoh_community_property), operand.k1s.k1s.p1_loss.b1_passive (line:k1s.k1s.p1_loss), operand.k1s.k1s.p2_loss.b2_net (line:k1s.k1s.p2_loss), operand.k1s.k1s.p3_loss.b3_net (line:k1s.k1s.p3_loss), operand.s2.s2.amt_l15.amt_l15_sdtw.then0 (line:s2.s2.amt_l15), operand.ssb.ssb.show16_18.past7.all.0.eq.0 (line:ssb.ssb.show16_18)

## Surviving — explained by an open defect

- `operand.k1s.k1s.col_k.zero.then1` (replace an operand, k1s.k1s.col_k): BUG-0928
- `operand.k1s.k1s.col_i.zero.then1` (replace an operand, k1s.k1s.col_i): BUG-0928
- `operand.k1s.k1s.col_h.zero.then1` (replace an operand, k1s.k1s.col_h): BUG-0928
- `operand.k1s.k1s.p5_income.zero.then1` (replace an operand, k1s.k1s.p5_income): BUG-0928
- `operand.person.person.f8919_line10.f8919_line10_figured.then0` (replace an operand, person.person.f8919_line10): BUG-0928
- `operand.s2.s2.amt_l16.amt_l15` (replace an operand, s2.s2.amt_l16): BUG-0764
- `operand.s2.s2.amt_l7.amt_l39.then1` (replace an operand, s2.s2.amt_l7): BUG-0764
- `operand.s2.s2.amt_tmt_over.amt_l7.gt.0` (replace an operand, s2.s2.amt_tmt_over): BUG-0764
