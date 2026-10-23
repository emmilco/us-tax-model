# Data-level properties

Properties of spec 6.3 checked over 400 generated returns (fast-check, seed 7, every filing status). "Applicable" counts the cases where the property's premise held and its values were computed; a refusal or an unknown makes a case inapplicable. A failure is reported with the smallest counterexample fast-check found.

| Property | Statement | Cases | Applicable | Result |
| --- | --- | --- | --- | --- |
| sdtw_skip_rule | Computing lines 23–43 of the Schedule D Tax Worksheet unconditionally gives the same lines 45, 47 and Form 1040 line 16 as skipping them, and every skipped component of line 41 and line 45 is zero when computed anyway. | 400 | 133 | holds |
| tax_bounds | Form 1040 line 16 is non-negative, at most the top rate (37/100) on taxable income plus one Tax Table band ($50), and at most the tax on all taxable income from the Tax Table or Tax Computation Worksheet. | 400 | 133 | holds |
| deduction_choice | With no election to itemize and no spouse itemizing, Form 1040 line 16 under the project's standard-or-itemized choice is at most line 16 under either deduction forced. | 400 | 132 | holds |
| refusal_propagates | No line computes a value from an operand that is a refusal; every line evaluated from a refused operand is a refusal. | 400 | 346 | holds |
| refusal_outranks_unknown | On generated returns with up to eight answers removed, every line evaluated from a refused operand is a refusal, whatever its other operands are; in particular an unknown operand does not hide a refused one. | 400 | 326 | holds |
| tax_monotone | Raising W-2 box 1 of the first employer, all else fixed, never lowers Form 1040 line 16. | 400 | 132 | holds |
| tax_monotone_by_method | Raising W-2 box 1 of the first employer, all else fixed, never lowers the Qualified Dividends and Capital Gain Tax Worksheet line 25 or the Schedule D Tax Worksheet line 47, each where it is computed on both returns. | 400 | 132 | holds |
| screens_respected | No generated return answers a screen No while an amount asked only after a Yes is nonzero (the generator's screens: Form 5695 Parts I and II, Sections A and B and lines 5a, 25a and 26a; Form 2441 care and benefits; Form W-2 box 12; the Simplified Method; owned vehicles; Form 7206). | 400 | 87 | holds |

## sdtw_skip_rule

- Rewritten lines (skip rule removed in the variant): 21 — 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43.
- Cases where Form 1040 line 16 came from this worksheet: 133. Cases with lines 1 and 16 equal (lines 23–43 skipped): 80; lines 1 and 32 equal with lines 1 and 16 different (lines 33–43 skipped): 9; Schedule D line 19 zero after line 32 (lines 35–40 skipped): 37; lines 41–43 skipped after line 32: 6.

## deduction_choice

- Cases where total tax (line 24) under the project's choice exceeded the better alternative: 0.

## refusal_outranks_unknown

- Cases with a refused operand somewhere: 326; cases with a line that has both a refused and an unknown operand (the order this property guards): 251.

## tax_monotone

- Cases where total tax (line 24) fell as wages rose: 0.

## tax_monotone_by_method

- Cases compared: QDCG worksheet line 25 132, Schedule D Tax Worksheet line 47 132.

## screens_respected

- Amounts found behind each screen answered No: f2441.benefits: f2441.line13, f2441.line14, f2441.paid_2026, f2441.plan_max, person[].w2[].box10; f2441.care: dependent[].dc_paid; f5695.line25a: f5695.line25c; f5695.line26a: f5695.line26b; f5695.line5a: f5695.battery_cost; f5695.part1_any: f5695.battery_cost, f5695.line1, f5695.line12, f5695.line2, f5695.line3, f5695.line4; f5695.part2_any: f5695.line18a, f5695.line19a, f5695.line19d_i, f5695.line19d_ii, f5695.line19e, f5695.line20a_i, f5695.line20a_ii, f5695.line20a_iii, f5695.line20a_iv, f5695.line20b, f5695.line22a, f5695.line22b, f5695.line23a_i, f5695.line23a_ii, f5695.line23b, f5695.line24a, f5695.line24b, f5695.line25c, f5695.line26b, f5695.line29a, f5695.line29b, f5695.line29c, f5695.line29d, f5695.line29e, f5695.line29f; person[].sc[].hi_uses: person[].sc[].f7206_line1; person[].sc[].scveh[].owned: person[].sc[].scveh[].cost, person[].sc[].scveh[].prior_179; person[].w2[].box12_any: person[].w2[].box12_aa, person[].w2[].box12_bb, person[].w2[].box12_d, person[].w2[].box12_e, person[].w2[].box12_ee, person[].w2[].box12_f, person[].w2[].box12_g, person[].w2[].box12_h, person[].w2[].box12_s; retirement[].annuity: retirement[].cost, retirement[].recovered.

## Branch coverage of the generated corpus

1943 of 2195 branches (choose guards, Bool lines both ways, floor and positive sides of subtract_floor0, left and right of smaller_of and larger_of) reached by the 400 generated returns. Unreached:

- asset.outside:true
- asset.screen:true
- asset.screened:true
- asset.pct_bad:true
- asset.listed_low:true
- asset.s179_bad:true
- asset.bonus_same:false
- asset.bonus_mixed:true
- carloan.mixed_qualifying:floor
- dcprov.household:true
- dcprov.related:true
- dcprov.see_statement:true
- dependent.dc_under13:false
- dependent.dc_no_tin:true
- dependent.dc_line2c:true
- eic.step1_foreign:false
- eic.step1_resident:false
- eic.step2_other:false
- eic.step3_married:false
- eic.wsb_line5_stop:true
- eic.clergy:true
- f1040.line27b:true
- f2441.nondependent_gate:true
- f2441.provider_ineligible:true
- f2441.line1_box:true
- f2441.statement_notice:true
- f2441.household_notice:true
- f2441.line2_box:true
- f2441.two_or_more:true
- f2441.limit#0
- f2441.line3_expenses:right
- f2441.attrib_gate:true
- f2441.line6:positive
- f2441.line11:right
- f2441.line14_bad:true
- f2441.employer_care_gate:true
- f2441.line21:left
- f2441.line24:right
- f2441.line25:positive
- f2441.line29:floor
- f2441.line31:left
- f5695.line15:right
- f5695.line16:positive
- f5695.doors_no_qmid:true
- f5695.windows_no_qmid:true
- f5695.ac_no_qmid:true
- f5695.wh_no_qmid:true
- f5695.enabling_no_qmid:true
- f5695.enabling_capped:right
- f5695.audit_capped:right
- f5695.line32:right
- f5695.line32b:true
- f8606.files:true
- f8606.dist:true
- f8889.bad_months:true
- f8889.line13_figured:right
- f8889.has_dist:true
- f8889.rollover_bad:true
- f8889.line14b#0
- f8889.line14c:positive
- f8889.line15#0
- f8889.line16_figured:positive
- f8889.line16#0
- f8889.has_taxable:true
- f8889.line17a:true
- f8889.subject_bad:true
- f8889.subject#1
- f8889.line17b#0
- f8959.line16:positive
- f8960.bad_allocation:true
- household.roster_ok:false
- household.roster_bad:true
- ira.any_trad:true
- ira.lines2to6:true
- ira.cov_gate:true
- ira.line1a:true
- ira.line1b:true
- ira.line2a#0
- ira.line2b#0
- ira.line6a#0
- ira.line6b#0
- ira.line7a#0
- ira.line7b#0
- ira.kbh_amount#1
- ira.kbh_amount#2
- ira.kbh_short:true
- ira.both_kinds:true
- ira.over_comp:true
- ira.special:true
- ira.se_capital:true
- ira.se_capital_gate:true
- ira.special_gate:true
- ira.combat_gate:true
- ira.excl_gate:true
- ira.deduct_less:true
- ira.less_gate:true
- oi8z.additional_tax:true
- otjob.flsa:false
- otjob.special_rule:true
- otjob.figured#0
- otjob.figured#2
- otjob.figured#4
- otjob.figured#5
- otjob.col_b#0
- person.itin_applied:true
- person.hsa_repeated:true
- person.sep_s7:right
- person.sep_s21:right
- person.simple_regular:right
- person.simple_catchup:positive
- person.ne_comp:right
- person.ira_has:true
- person.ira_excess:true
- person.ira_excess_gate:true
- person.ira_age50:true
- person.ira_work_plan:true
- person.ira_limit#0
- person.ira_prod_wide#0
- person.ira_prod_joint#0
- person.ira_over_limit:true
- person.ira_deduction#0
- person.ira_nd_figured:positive
- person.ira_nondeductible#0
- person.ira_files_8606:true
- person.ira_basis_adjusted:true
- person.ira_basis_gate:true
- person.ira_8606_line2#0
- person.ira_dist:true
- person.ira_dist_gate:true
- person.ira_ssb#0
- refund.has:true
- refund.box8:true
- refund.not_2024:true
- refund.itemized:true
- refund.sales:true
- refund.worksheet:true
- refund.exc_tax:true
- refund.exc_who:true
- refund.line5e_bad:true
- refund.line1:right
- refund.line2_more:true
- refund.line2:positive
- refund.line3_more:true
- refund.line3:positive
- refund.mfs_spouse_itemized:true
- refund.line5#1
- refund.line5#2
- refund.line5#3
- refund.line5#4
- refund.per_box#1
- refund.per_box#2
- refund.per_box#3
- refund.per_box#4
- refund.you_born:true
- refund.you_blind:true
- refund.spouse_born:true
- refund.spouse_blind:true
- refund.spouse_boxes:true
- refund.amt_you_born#0
- refund.amt_you_blind#0
- refund.amt_spouse_born#1
- refund.amt_spouse_born_checked#0
- refund.amt_spouse_blind#1
- refund.amt_spouse_blind_checked#0
- refund.line8_figured:positive
- refund.line8#1
- refund.line8#2
- refund.line8#3
- refund.line8#4
- refund.line8_mfs#0
- refund.line9_figured:right
- refund.line9#1
- refund.taxable#1
- retirement.sav_404k:true
- s1.line1#1
- s1.ebl:true
- s1.sc_1a:true
- s1.line8_other:true
- s1.has_gambling:true
- s1.gambling_pro:true
- s1.gambling_business:true
- s1.alimony:true
- s1.alimony_unsupported:true
- s1.line2a#0
- s1.line2b_notice:true
- s1.cod_any:true
- s1.has_cod:true
- s1.cod_unsupported:true
- s1.cod_figured#0
- s1.line8c#0
- s1.line19a#0
- s1.line19b_notice:true
- s1.line19c_notice:true
- s1.jury_over:true
- s179.line4:positive
- s179.line5_full:floor
- s179.line9:left
- s179.line11:right
- s1a.line4c_one:right
- s1a.line10_over:true
- s1a.line10_pos:positive
- s1a.line13_amount#1
- s1a.line18_over:true
- s1a.line18_pos:positive
- s1a.line21_figured:positive
- s1a.line21_amount#1
- s8812.few_children:false
- s8812.line27#1
- s8812.clwb_three:true
- s8812.clwb_11#0
- s8812.clwb_12:right
- sa.line16_gambling:right
- sa.line16#0
- sales.special:true
- sc.statutory:true
- sc.passive:false
- sc.spouse_owned:true
- sc.method_other:true
- sc.special:true
- sc.screened:true
- sc.ho_other:true
- sc.ho_screened:true
- sc.at_risk:false
- sc.not_at_risk:true
- sc.inventory_other:true
- sc.hi_screen:true
- sc.hi_screened:true
- sc.tips_ot:true
- scope.ready:false
- scveh.no_miles:true
- scveh.smr_ok:false
- scveh.smr_bad:true
- scveh.screen:true
- scveh.screened:true
- scveh.suv:true
- scveh.s179_bad:true
- scveh.bonus_same:false
- scveh.bonus_mixed:true
- scveh.s179_line10:right
- scveh.line11:floor
- scveh.d6:left
- scveh.too_old:true
- sd.screen:true
- tipjob.col_d:right
- w2.box10_bad:true
- w2.box12_userra:true
- w2.has_g:true
- w2.g_governmental:true
- w2.g_bad:true
- w2.g_gov_part#0
- w2.g_counted#0
- w2.code_h:true
