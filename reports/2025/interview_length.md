# Interview length: what question order could save

Written by `node engine/dist/main.js interview-length --write` (engine/src/interview-length.ts; deterministic, no model calls).
Every return is walked in three orders, and each order must give the same status and values (it does; a difference fails the run):

- **static**: today's order (bank order, then key).
- **floor**: the least any order can ask, knowing the answers: the inputs the complete return's evaluation reads. An order that
  asks only those (the oracle walk) is run and asks exactly that many on every return, so the floor is attained, not just bounded.
- **expected**: an order that does not know the answers: at each step it asks the open question whose closed answer (false, 0,
  none) would make the most other open questions unreachable, weighted by the share answering no from `interview/2025/gate_frequencies.yaml`
  (0.5 where the file names no share), ties in bank order. It probes the evaluator; it never answers for the filer.

Only the evaluator's reachability hides a question, so these are the only savings open to order. A question asked in every order and
answered no or 0 is one only a missing gate (a formal-model change) could hide. **Closed** answers are false, 0 or an empty list.
The returns are synthetic (fixtures, generated returns, minimal returns), not real filers.

## Summary

Means are per complete return; refused returns are counted but not measured beyond static. *Saved* is the share of all static
questions in the group that the order does not ask.

| Returns | Complete | Refused | Not walkable | Static asked (mean) | Static max | Closed answers (mean, share) | Floor (mean) | Expected order (mean) | Saved at floor | Saved by expected |
|---|---|---|---|---|---|---|---|---|---|---|
| Stage 5 whole returns | 9 | 2 | 0 | 138.8 | 167 | 119.2 (86%) | 138.8 | 138.8 | 0% | 0% |
| generated returns | 2 | 10 | 0 | 217.5 | 251 | 173.5 (80%) | 217.5 | 217.5 | 0% | 0% |
| minimal returns | 62 | 0 | 0 | 117.6 | 133 | 114.0 (97%) | 117.6 | 117.6 | 0% | 0% |
| social-security profile fixtures | 15 | 6 | 0 | 13.2 | 15 | 8.4 (64%) | 13.2 | 13.2 | 0% | 0% |
| sales profile fixtures | 58 | 14 | 0 | 100.4 | 151 | 89.0 (89%) | 100.4 | 100.4 | 0% | 0% |
| stage4 profile fixtures | 69 | 64 | 0 | 126.5 | 158 | 114.9 (91%) | 126.4 | 126.5 | 0% | 0% |
| **full profile, Stage 5 and generated** | 11 | 12 | 0 | 153.1 | 251 | 129.1 (84%) | 153.1 | 153.1 | 0% | 0% |
| **all** | 215 | 96 | 0 | 110.3 | 251 | 101.0 (92%) | 110.3 | 110.3 | 0% | 0% |

## Closed answers no order avoids (missing-gate candidates)

Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the 11 complete
Stage 5 and generated returns ask them closed (count of 62 complete minimal returns beside). *Kind*: `gate guard` is read by a gate's guard
(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a
new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all
returns in `gate_frequencies.yaml` where the file names the template (- where it does not).

101 templates are asked and answered closed on every one of the 11 returns; 30 of them have a recorded share
yes below the rare-situation cut (0.05).

| Template | Kind | Share yes | Stage 5 and generated | Minimal |
|---|---|---|---|---|
| `$dependent` | ungated | 0.2937 | 11 | 62 |
| `$oi8z` | ungated | 0.0485 | 11 | 62 |
| `$retirement` | ungated | 0.2357 | 11 | 62 |
| `f2441.care` | ungated | 0.045 | 11 | 62 |
| `f8863.paid` | ungated | 0.09 | 11 | 62 |
| `f8959.territory_w2` | ungated | 0.006 | 11 | 62 |
| `household.community_property` | ungated | 0.2335 | 11 | 62 |
| `person.blind` | ungated | 0.004 | 11 | 62 |
| `person.inherited_account` | ungated | - | 11 | 62 |
| `person.rrta` | ungated | 0.0015 | 11 | 62 |
| `person.x_archer_excess` | ungated | - | 11 | 62 |
| `qbi.coop_patron` | ungated | - | 11 | 62 |
| `refund.any` | ungated | - | 11 | 62 |
| `s1.cod_any` | ungated | 0.006 | 11 | 62 |
| `s1.digital_income` | ungated | - | 11 | 62 |
| `s1.inmate_wages` | ungated | - | 11 | 62 |
| `s1.ltc_payout` | ungated | - | 11 | 62 |
| `s1a.carloan` | ungated | 0.03 | 11 | 62 |
| `s1a.overtime` | ungated | 0.1471 | 11 | 62 |
| `s1a.tips` | ungated | 0.0195 | 11 | 62 |
| `s2.amt_owed` | ungated | 0.0009 | 11 | 62 |
| `s2.credit_recapture` | ungated | - | 11 | 62 |
| `s2.hsa_testing` | ungated | - | 11 | 62 |
| `s2.iso_vested` | ungated | - | 11 | 62 |
| `s2.other_tax` | ungated | - | 11 | 62 |
| `s3.credit_bond` | ungated | 0.012 | 11 | 62 |
| `s3.disability_retired` | ungated | - | 11 | 62 |
| `s3.line10` | ungated | 0.0153 | 11 | 62 |
| `s3.repaid_income` | ungated | 0.002 | 11 | 62 |
| `sa.bond_premium` | ungated | - | 11 | 62 |
| `sa.debt_instrument_loss` | ungated | - | 11 | 62 |
| `sa.dependent` | ungated | 0.0469 | 11 | 62 |
| `sa.elect_itemize` | ungated | - | 11 | 62 |
| `sa.estate_tax_income` | ungated | - | 11 | 62 |
| `sa.excluded_income` | ungated | 0.004 | 11 | 62 |
| `sa.impairment_work` | ungated | - | 11 | 62 |
| `sa.pension_unrecovered` | ungated | - | 11 | 62 |
| `sa.sales_tax_wish` | ungated | - | 11 | 62 |
| `sb.account_any` | ungated | - | 11 | 62 |
| `sb.asset_any` | ungated | - | 11 | 62 |
| `sb.company_any` | ungated | - | 11 | 62 |
| `sb.territory_any` | ungated | - | 11 | 62 |
| `sb.trust_any` | ungated | - | 11 | 62 |
| `scope.archer_msa` | ungated | - | 11 | 62 |
| `scope.attorney_fees` | ungated | - | 11 | 62 |
| `scope.chapter11` | ungated | - | 11 | 62 |
| `scope.disaster_distribution` | ungated | - | 11 | 62 |
| `scope.education_recapture` | ungated | - | 11 | 62 |
| `scope.f8814` | ungated | - | 11 | 62 |
| `scope.farm` | ungated | - | 11 | 62 |
| `scope.k1` | ungated | - | 11 | 62 |
| `scope.medicaid_waiver` | ungated | - | 11 | 62 |
| `scope.nol` | ungated | - | 11 | 62 |
| `scope.pay_no_w2` | ungated | - | 11 | 62 |
| `scope.recovery` | ungated | - | 11 | 62 |
| `scope.reforestation` | ungated | - | 11 | 62 |
| `scope.rental` | ungated | - | 11 | 62 |
| `sd.carryover` | ungated | 0.045 | 11 | 62 |
| `sd.casualty` | ungated | 0.025 | 11 | 62 |
| `sd.condemned` | ungated | 0.025 | 11 | 62 |
| `sd.sec1256` | ungated | 0.025 | 11 | 62 |
| `sd.small_business_stock` | ungated | 0.025 | 11 | 62 |
| `sd.trader_election` | ungated | 0.025 | 11 | 62 |
| `f1040.withheld_other_any` | gate guard | - | 11 | 61 |
| `f2441.benefits` | gate guard | 0.012 | 11 | 61 |
| `f5695.any` | gate guard | 0.0252 | 11 | 61 |
| `person.eligible_educator` | gate guard | - | 11 | 61 |
| `person.ira_owner` | gate guard | - | 11 | 61 |
| `person.x_edu_account` | gate guard | - | 11 | 61 |
| `qbi.prior_form` | gate guard | - | 11 | 61 |
| `s1.alaska_any` | gate guard | - | 11 | 61 |
| `s1.alimony_any` | gate guard | - | 11 | 61 |
| `s1.hobby_any` | gate guard | - | 11 | 61 |
| `s1.jury_any` | gate guard | - | 11 | 61 |
| `s1.scholarship_any` | gate guard | - | 11 | 61 |
| `s1.uc_any` | gate guard | - | 11 | 61 |
| `s1.winnings_any` | gate guard | - | 11 | 61 |
| `s2.household_help` | gate guard | - | 11 | 61 |
| `s2.options_any` | gate guard | - | 11 | 61 |
| `s3.adoption_any` | gate guard | 0.012 | 11 | 61 |
| `s3.ev` | gate guard | 0.012 | 11 | 61 |
| `s3.farmland` | gate guard | 0.002 | 11 | 61 |
| `s3.foreign_any` | gate guard | 0.002 | 11 | 61 |
| `s3.kerosene` | gate guard | 0.0019 | 11 | 61 |
| `s3.prior_other_forms` | gate guard | 0.012 | 11 | 61 |
| `sa.personal_property_tax_any` | gate guard | - | 11 | 61 |
| `sa.state_tax_other_any` | gate guard | - | 11 | 61 |
| `scope.armed_forces` | gate guard | - | 11 | 61 |
| `scope.business_before` | gate guard | - | 11 | 61 |
| `scope.foreign_shares` | gate guard | - | 11 | 61 |
| `scope.noncitizen` | gate guard | - | 11 | 61 |
| `scope.religious_work` | gate guard | - | 11 | 61 |
| `sd.sold_other` | gate guard | 0.025 | 11 | 61 |
| `ssb.any` | gate guard | - | 11 | 61 |
| `household.married_dec31` | behind a gate | 0.3656 | 11 | 0 |
| `household.spouse_died_this_year` | behind a gate | 0.006 | 11 | 0 |
| `s1.nqdc_pension` | behind a gate | - | 11 | 0 |
| `s2.w2_marks` | behind a gate | - | 11 | 0 |
| `scope.artist_official` | behind a gate | - | 11 | 0 |
| `scope.excess_deferral` | behind a gate | - | 11 | 0 |
| `scope.w2_marks` | behind a gate | - | 11 | 0 |
| `$f1095a` | ungated | 0.085 | 10 | 62 |
| `$sc` | ungated | 0.1898 | 10 | 62 |
| `sli.any` | gate guard | - | 10 | 61 |
| `$f8889` | ungated | 0.11 | 9 | 62 |
| `$sales` | ungated | 0.13 | 8 | 62 |
| `sa.medical_any` | ungated | - | 8 | 62 |
| `sa.medical_premiums` | ungated | - | 8 | 62 |
| `f4952.has_interest` | gate guard | 0.01 | 8 | 61 |
| `sa.home_other` | ungated | - | 7 | 62 |
| `sa.home_owner` | ungated | - | 7 | 62 |
| `div.any` | gate guard | - | 7 | 61 |
| `sa.gift_carryover` | ungated | - | 7 | 61 |
| `sa.gifts` | gate guard | 0.4 | 7 | 61 |
| `sa.state_tax_any` | gate guard | - | 7 | 61 |
| `$interest` | ungated | 0.3441 | 6 | 62 |

## Questions order could avoid

Templates asked in static order and not read by the complete return, by number of complete returns (all groups): the questions a
better order (or a nested `choose`) would not ask. On the full profile these are the templates interview-rules holds under
`walked_unused`; the slice profiles are not in its reach check.

| Template | Returns |
|---|---|
| `person.blind` | 4 |

## Per return

### Stage 5 whole returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| stage5.return.owed | complete | 147 | 125 | 147 | 147 |
| stage5.return.refund | complete | 128 | 116 | 128 | 128 |
| stage5.return.itemized | complete | 167 | 126 | 167 | 167 |
| stage5.refuse.screens | refused | 84 | 79 | - | - |
| stage5.refuse.other_income | refused | 112 | 106 | - | - |
| stage5.return.refund_f4952_screens_unused | complete | 128 | 116 | 128 | 128 |
| stage5.return.refund_f8960_unsupported_unused | complete | 128 | 116 | 128 | 128 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 128 | 116 | 128 | 128 |
| stage5.return.refund_f8960_refund_unused | complete | 128 | 116 | 128 | 128 |
| stage5.return.refund_combat_pay_no_children | complete | 128 | 116 | 128 | 128 |
| stage5.return.itemized_f8960_allocation_unused | complete | 167 | 126 | 167 | 167 |

### generated returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| generated.0 | complete | 251 | 203 | 251 | 251 |
| generated.1 | refused | 195 | 147 | - | - |
| generated.2 | refused | 140 | 102 | - | - |
| generated.3 | refused | 161 | 130 | - | - |
| generated.4 | complete | 184 | 144 | 184 | 184 |
| generated.5 | refused | 154 | 103 | - | - |
| generated.6 | refused | 153 | 134 | - | - |
| generated.7 | refused | 135 | 99 | - | - |
| generated.8 | refused | 217 | 160 | - | - |
| generated.9 | refused | 241 | 167 | - | - |
| generated.10 | refused | 234 | 185 | - | - |
| generated.11 | refused | 195 | 147 | - | - |

### minimal returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| every gate closed | complete | 116 | 113 | 116 | 116 |
| asset.industry = true alone | complete | 116 | 113 | 116 | 116 |
| asset.listed = true alone | complete | 116 | 113 | 116 | 116 |
| asset.software = true alone | complete | 116 | 113 | 116 | 116 |
| dependent.ever_married = true alone | complete | 116 | 113 | 116 | 116 |
| dependent.lived_all_year = true alone | complete | 116 | 113 | 116 | 116 |
| dependent.ptc_files = true alone | complete | 116 | 113 | 116 | 116 |
| div.any = true alone | complete | 121 | 117 | 121 | 121 |
| eic.lived_with_relative = true alone | complete | 116 | 113 | 116 | 116 |
| f1040.estimated_any = true alone | complete | 117 | 113 | 117 | 117 |
| f1040.withheld_other_any = true alone | complete | 118 | 114 | 118 | 118 |
| f2441.benefits = true alone | complete | 127 | 123 | 127 | 127 |
| f4952.has_interest = true alone | complete | 119 | 115 | 119 | 119 |
| f5695.any = true alone | complete | 133 | 129 | 133 | 133 |
| f5695.line17b = true alone | complete | 116 | 113 | 116 | 116 |
| f5695.line21a = true alone | complete | 116 | 113 | 116 | 116 |
| f8889.coverage_year = "family" alone | complete | 116 | 113 | 116 | 116 |
| f8889.coverage_year = "changed" alone | complete | 116 | 113 | 116 | 116 |
| f8962.other_coverage = true alone | complete | 116 | 113 | 116 | 116 |
| ny_it201.ask.city_resident = true alone | complete | 116 | 113 | 116 | 116 |
| ny_it201.ask.est_any = true alone | complete | 116 | 113 | 116 | 116 |
| ny_it201.ask.owes_use_tax = true alone | complete | 116 | 113 | 116 | 116 |
| person.eligible_educator = true alone | complete | 117 | 113 | 117 | 117 |
| person.ira_owner = true alone | complete | 118 | 114 | 118 | 118 |
| person.x_edu_account = true alone | complete | 118 | 114 | 118 | 118 |
| qbi.prior_form = true alone | complete | 118 | 114 | 118 | 118 |
| retirement.rollover_any = true alone | complete | 116 | 113 | 116 | 116 |
| s1.alaska_any = true alone | complete | 117 | 113 | 117 | 117 |
| s1.alimony_any = true alone | complete | 117 | 113 | 117 | 117 |
| s1.hobby_any = true alone | complete | 117 | 113 | 117 | 117 |
| s1.jury_any = true alone | complete | 117 | 113 | 117 | 117 |
| s1.scholarship_any = true alone | complete | 117 | 113 | 117 | 117 |
| s1.uc_any = true alone | complete | 117 | 113 | 117 | 117 |
| s1.winnings_any = true alone | complete | 119 | 115 | 119 | 119 |
| s2.household_help = true alone | complete | 117 | 113 | 117 | 117 |
| s2.options_any = true alone | complete | 118 | 114 | 118 | 118 |
| s3.adoption_any = true alone | complete | 119 | 115 | 119 | 119 |
| s3.ev = true alone | complete | 119 | 115 | 119 | 119 |
| s3.farmland = true alone | complete | 117 | 113 | 117 | 117 |
| s3.foreign_any = true alone | complete | 121 | 117 | 121 | 121 |
| s3.kerosene = true alone | complete | 117 | 113 | 117 | 117 |
| s3.prior_other_forms = true alone | complete | 120 | 116 | 120 | 120 |
| sa.gifts = true alone | complete | 118 | 114 | 118 | 118 |
| sa.personal_property_tax_any = true alone | complete | 117 | 113 | 117 | 117 |
| sa.state_tax_any = true alone | complete | 117 | 113 | 117 | 117 |
| sa.state_tax_other_any = true alone | complete | 117 | 113 | 117 | 117 |
| sc.employees = true alone | complete | 116 | 113 | 116 | 116 |
| sc.goods = true alone | complete | 116 | 113 | 116 | 116 |
| sc.travel_meals = true alone | complete | 116 | 113 | 116 | 116 |
| scope.armed_forces = true alone | complete | 119 | 115 | 119 | 119 |
| scope.business_before = true alone | complete | 119 | 115 | 119 | 119 |
| scope.foreign_shares = true alone | complete | 118 | 114 | 118 | 118 |
| scope.noncitizen = true alone | complete | 117 | 113 | 117 | 117 |
| scope.religious_work = true alone | complete | 118 | 114 | 118 | 118 |
| scveh.others_use = true alone | complete | 116 | 113 | 116 | 116 |
| scveh.smr_always = true alone | complete | 116 | 113 | 116 | 116 |
| sd.route_each = true alone | complete | 116 | 113 | 116 | 116 |
| sd.sold_other = true alone | complete | 119 | 115 | 119 | 119 |
| sli.any = true alone | complete | 119 | 115 | 119 | 119 |
| ssb.any = true alone | complete | 117 | 113 | 117 | 117 |
| ssb.prior_year_pay = true alone | complete | 116 | 113 | 116 | 116 |
| tipjob.listed = true alone | complete | 116 | 113 | 116 | 116 |

### social-security profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| ss.multi | complete | 15 | 9 | 15 | 15 |
| ss.base.below | complete | 15 | 9 | 15 | 15 |
| ss.base.exact | complete | 15 | 9 | 15 | 15 |
| ss.base.above | complete | 15 | 9 | 15 | 15 |
| ss.withheld.below | complete | 15 | 9 | 15 | 15 |
| ss.withheld.exact | complete | 15 | 9 | 15 | 15 |
| ss.withheld.above | complete | 15 | 9 | 15 | 15 |
| ss.single.exact | complete | 10 | 7 | 10 | 10 |
| ss.single.below | complete | 10 | 7 | 10 | 10 |
| ss.single.over | refused | 6 | 3 | - | - |
| ss.multi.over | refused | 8 | 4 | - | - |
| ss.tips | complete | 15 | 8 | 15 | 15 |
| ss.none | complete | 9 | 8 | 9 | 9 |
| ss.mfj | complete | 9 | 8 | 9 | 9 |
| ss.mfs | refused | 3 | 2 | - | - |
| ss.rrta | refused | 4 | 2 | - | - |
| ss.hoh | complete | 15 | 9 | 15 | 15 |
| ss.qss | complete | 15 | 9 | 15 | 15 |
| ss.other.components | refused | 13 | 4 | - | - |
| ss.person.separation | complete | 10 | 7 | 10 | 10 |
| ss.early.refusal | refused | 8 | 5 | - | - |

### sales profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| sales.carryover.short_term | complete | 103 | 88 | 103 | 103 |
| sales.official.gain | complete | 97 | 87 | 97 | 97 |
| sales.official.loss | complete | 97 | 87 | 97 | 97 |
| sales.official.adjustment | complete | 98 | 87 | 98 | 98 |
| sales.official.basis | complete | 98 | 87 | 98 | 98 |
| sales.adjust.A.B | complete | 98 | 87 | 98 | 98 |
| sales.adjust.A.W | complete | 98 | 87 | 98 | 98 |
| sales.adjust.A.BW | complete | 99 | 87 | 99 | 99 |
| sales.adjust.B.B | complete | 97 | 87 | 97 | 97 |
| sales.adjust.B.W | complete | 98 | 87 | 98 | 98 |
| sales.adjust.B.BW | complete | 98 | 87 | 98 | 98 |
| sales.adjust.D.B | complete | 98 | 87 | 98 | 98 |
| sales.adjust.D.W | complete | 98 | 87 | 98 | 98 |
| sales.adjust.D.BW | complete | 99 | 87 | 99 | 99 |
| sales.adjust.E.B | complete | 97 | 87 | 97 | 97 |
| sales.adjust.E.W | complete | 98 | 87 | 98 | 98 |
| sales.adjust.E.BW | complete | 98 | 87 | 98 | 98 |
| sales.refuse.wash_over_loss | refused | 93 | 82 | - | - |
| sales.adjust.A.W.equal_loss | complete | 98 | 87 | 98 | 98 |
| sales.adjust.D.BW.wash_within_corrected_loss | complete | 99 | 87 | 99 | 99 |
| sales.official.aggregate | complete | 98 | 87 | 98 | 98 |
| sales.official.two_aggregate | complete | 105 | 88 | 105 | 105 |
| sales.box.A | complete | 97 | 87 | 97 | 97 |
| sales.box.B | complete | 97 | 87 | 97 | 97 |
| sales.box.C | complete | 97 | 87 | 97 | 97 |
| sales.box.D | complete | 97 | 87 | 97 | 97 |
| sales.box.E | complete | 97 | 87 | 97 | 97 |
| sales.box.F | complete | 97 | 87 | 97 | 97 |
| sales.loss.single.0 | complete | 97 | 89 | 97 | 97 |
| sales.loss.mfs.0 | complete | 96 | 89 | 96 | 96 |
| sales.loss.single.1 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.1 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.149999 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.149999 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.150000 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.150000 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.150001 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.150001 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.299999 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.299999 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.300000 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.300000 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.300001 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.300001 | complete | 96 | 88 | 96 | 96 |
| sales.loss.single.700000 | complete | 97 | 88 | 97 | 97 |
| sales.loss.mfs.700000 | complete | 96 | 88 | 96 | 96 |
| sales.cents | complete | 103 | 90 | 103 | 103 |
| sales.no_sales | complete | 95 | 90 | 95 | 95 |
| sales.distribution | complete | 101 | 94 | 101 | 101 |
| sales.refuse.digital.G | refused | 87 | 81 | - | - |
| sales.refuse.digital.H | refused | 87 | 81 | - | - |
| sales.refuse.digital.I | refused | 87 | 81 | - | - |
| sales.refuse.digital.J | refused | 87 | 81 | - | - |
| sales.refuse.digital.K | refused | 87 | 81 | - | - |
| sales.refuse.digital.L | refused | 87 | 81 | - | - |
| sales.refuse.special | refused | 92 | 83 | - | - |
| sales.refuse.code | refused | 92 | 84 | - | - |
| sales.refuse.no_report_B | refused | 92 | 84 | - | - |
| sales.refuse.aggregate.eligibility | refused | 93 | 85 | - | - |
| sales.refuse.aggregate.basis | refused | 90 | 82 | - | - |
| sales.refuse.aggregate.adjustment | refused | 93 | 85 | - | - |
| sales.refuse.forms | refused | 82 | 78 | - | - |
| sales.select.sdtw.28pct | complete | 116 | 100 | 116 | 116 |
| sales.select.sdtw.1250 | complete | 116 | 100 | 116 | 116 |
| sales.select.zero_taxable | complete | 116 | 100 | 116 | 116 |
| sales.select.4952_zero | complete | 107 | 93 | 107 | 107 |
| sales.select.short_only | complete | 102 | 90 | 102 | 102 |
| sales.select.loss_dividend | complete | 110 | 96 | 110 | 110 |
| sales.select.loss_no_dividend | complete | 102 | 91 | 102 | 102 |
| sales.netting | complete | 108 | 92 | 108 | 108 |
| sales.mixed_columns | complete | 151 | 97 | 151 | 151 |
| sales.select.sdtw.election | complete | 107 | 93 | 107 | 107 |

### stage4 profile fixtures

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| stage4.mut.div_box3_basis_reconciled | complete | 126 | 116 | 126 | 126 |
| stage4.refuse.div.section1202 | refused | 122 | 112 | - | - |
| stage4.refuse.div.amt | refused | 122 | 113 | - | - |
| stage4.refuse.div.special | refused | 120 | 111 | - | - |
| stage4.refuse.div.inconsistent | refused | 122 | 112 | - | - |
| stage4.refuse.div.components | refused | 122 | 113 | - | - |
| stage4.refuse.div.overlapping | refused | 123 | 112 | - | - |
| stage4.refuse.div.basis | refused | 123 | 114 | - | - |
| stage4.interest.limited | complete | 130 | 119 | 130 | 130 |
| stage4.interest.exception | complete | 130 | 119 | 130 | 130 |
| stage4.interest.election | complete | 130 | 117 | 130 | 130 |
| stage4.4952.carryover_no_income | complete | 122 | 112 | 122 | 122 |
| stage4.f4952.line4a_taxable_interest_and_dividends | complete | 132 | 118 | 132 | 132 |
| stage4.refuse.4952.unsupported | refused | 118 | 108 | - | - |
| stage4.refuse.4952.alternative_allocation | refused | 119 | 109 | - | - |
| stage4.refuse.4952.election | refused | 119 | 110 | - | - |
| stage4.refuse.4952.bad_dividends | refused | 126 | 115 | - | - |
| stage4.refuse.4952.unsupported_with_carryover | refused | 119 | 109 | - | - |
| stage4.interest.short_term | complete | 123 | 110 | 123 | 123 |
| stage4.f4952.unused_unsupported | complete | 116 | 109 | 116 | 116 |
| stage4.f4952.unused_alternative_allocation | complete | 116 | 109 | 116 | 116 |
| stage4.base | complete | 116 | 109 | 116 | 116 |
| stage4.medicare.single.-1 | complete | 116 | 109 | 116 | 116 |
| stage4.medicare.single.0 | complete | 116 | 109 | 116 | 116 |
| stage4.medicare.single.100000 | complete | 116 | 109 | 116 | 116 |
| stage4.medicare.hoh.-1 | complete | 137 | 118 | 137 | 137 |
| stage4.medicare.hoh.0 | complete | 137 | 118 | 137 | 137 |
| stage4.medicare.hoh.100000 | complete | 137 | 118 | 137 | 137 |
| stage4.medicare.qss.-1 | complete | 114 | 107 | 114 | 114 |
| stage4.medicare.qss.0 | complete | 114 | 107 | 114 | 114 |
| stage4.medicare.qss.100000 | complete | 114 | 107 | 114 | 114 |
| stage4.medicare.mfs.-1 | refused | 104 | 98 | - | - |
| stage4.medicare.mfs.0 | refused | 104 | 98 | - | - |
| stage4.medicare.mfs.100000 | refused | 104 | 98 | - | - |
| stage4.medicare.mfj.-1 | refused | 85 | 79 | - | - |
| stage4.medicare.mfj.0 | refused | 85 | 79 | - | - |
| stage4.medicare.mfj.100000 | refused | 85 | 79 | - | - |
| stage4.medicare.withholding | complete | 116 | 109 | 116 | 116 |
| stage4.medicare.withholding_floor | complete | 116 | 109 | 116 | 116 |
| stage4.refuse.8959 | refused | 116 | 110 | - | - |
| stage4.niit.allocated | complete | 143 | 120 | 142 | 143 |
| stage4.niit.single.0 | complete | 125 | 116 | 125 | 125 |
| stage4.niit.single.100000 | complete | 127 | 118 | 127 | 127 |
| stage4.niit.hoh.0 | complete | 146 | 125 | 146 | 146 |
| stage4.niit.hoh.100000 | complete | 148 | 127 | 148 | 148 |
| stage4.niit.qss.0 | complete | 123 | 114 | 123 | 123 |
| stage4.niit.qss.100000 | complete | 125 | 116 | 125 | 125 |
| stage4.niit.mfj.0 | refused | 92 | 84 | - | - |
| stage4.niit.mfj.100000 | refused | 92 | 84 | - | - |
| stage4.niit.mfs.0 | refused | 113 | 105 | - | - |
| stage4.niit.mfs.100000 | refused | 115 | 107 | - | - |
| stage4.niit.standard_no_deduction | complete | 133 | 120 | 133 | 133 |
| stage4.refuse.8960.unsupported | refused | 117 | 109 | - | - |
| stage4.refuse.8960.refund | refused | 118 | 110 | - | - |
| stage4.niit.loss_floor | complete | 125 | 112 | 125 | 125 |
| stage4.refuse.niit.allocation | refused | 119 | 110 | - | - |
| stage4.refuse.8960.unsupported.simultaneous | refused | 117 | 109 | - | - |
| stage4.additional_taxes.combined | complete | 143 | 120 | 142 | 143 |
| stage4.official.medicare_example5 | refused | 85 | 79 | - | - |
| stage4.ftc.29999 | complete | 127 | 114 | 127 | 127 |
| stage4.ftc.30000 | complete | 127 | 114 | 127 | 127 |
| stage4.ftc.regular_limit | complete | 127 | 114 | 127 | 127 |
| stage4.refuse.ftc.limit | refused | 122 | 113 | - | - |
| stage4.refuse.ftc.passive | refused | 124 | 115 | - | - |
| stage4.refuse.ftc.statements | refused | 125 | 115 | - | - |
| stage4.refuse.ftc.eligible | refused | 126 | 115 | - | - |
| stage4.refuse.ftc.election | refused | 127 | 115 | - | - |
| stage4.mut.savers_claimed_dependent | refused | 95 | 87 | - | - |
| stage4.qbi.below | complete | 127 | 117 | 127 | 127 |
| stage4.qbi.exact | complete | 127 | 117 | 127 | 127 |
| stage4.qbi.above | complete | 127 | 117 | 127 | 127 |
| stage4.qbi.income_limit | complete | 125 | 115 | 125 | 125 |
| stage4.qbi.capital_limit | complete | 125 | 114 | 125 | 125 |
| stage4.refuse.qbi | refused | 116 | 108 | - | - |
| stage4.qbi.zero_income | complete | 116 | 110 | 116 | 116 |
| stage4.refuse.s2.amt | refused | 115 | 107 | - | - |
| s2.reg.iso_vested_2025 | refused | 108 | 100 | - | - |
| stage4.refuse.s2.other | refused | 116 | 108 | - | - |
| stage4.refuse.s2.amt.simultaneous | refused | 115 | 107 | - | - |
| stage4.refuse.gift.sectionB | refused | 119 | 109 | - | - |
| stage4.salt.below | complete | 120 | 111 | 120 | 120 |
| stage4.salt.exact | complete | 120 | 111 | 120 | 120 |
| stage4.salt.phase | complete | 120 | 111 | 120 | 120 |
| stage4.salt.floor | complete | 119 | 110 | 119 | 119 |
| stage4.salt.above | complete | 119 | 110 | 119 | 119 |
| stage4.salt.mfs | refused | 107 | 99 | - | - |
| stage4.salt.mfs_floor | refused | 107 | 99 | - | - |
| stage4.salt.low_paid | complete | 119 | 110 | 119 | 119 |
| stage4.medical.below | complete | 116 | 107 | 116 | 116 |
| stage4.medical.above | complete | 116 | 107 | 116 | 116 |
| stage4.standard.single | complete | 117 | 108 | 117 | 117 |
| stage4.standard.hoh | complete | 138 | 117 | 138 | 138 |
| stage4.standard.qss | complete | 115 | 106 | 115 | 115 |
| stage4.standard.mfj | refused | 86 | 78 | - | - |
| stage4.standard.mfs | refused | 104 | 97 | - | - |
| stage4.standard.spouse_itemizes | refused | 102 | 95 | - | - |
| stage4.standard.itemized | complete | 123 | 114 | 123 | 123 |
| stage4.standard.elected | complete | 116 | 108 | 115 | 116 |
| stage4.gift.50000.false | complete | 120 | 110 | 120 | 120 |
| stage4.gift.500000.false | complete | 120 | 110 | 120 | 120 |
| stage4.gift.500001.true | complete | 121 | 110 | 121 | 121 |
| stage4.refuse.sa.unsupported | refused | 113 | 105 | - | - |
| stage4.refuse.sa.charity_limited | refused | 101 | 92 | - | - |
| stage4.refuse.sa.excluded_income | refused | 108 | 100 | - | - |
| stage4.refuse.standard.dependent | refused | 95 | 87 | - | - |
| stage4.refuse.dependent_itemizes | refused | 95 | 87 | - | - |
| stage4.refuse.standard.spouse_extra | refused | 103 | 96 | - | - |
| stage4.refuse.gift.special | refused | 118 | 108 | - | - |
| stage4.refuse.sa.unsupported.simultaneous | refused | 107 | 98 | - | - |
| stage4.deductions.combined | complete | 139 | 115 | 139 | 139 |
| audit.sa.negative_agi_medical | complete | 158 | 144 | 158 | 158 |
| audit.sa.negative_agi_medical_paid | complete | 158 | 142 | 158 | 158 |
| stage4.refuse.sb.unsupported | refused | 114 | 104 | - | - |
| stage4.refuse.sb.fbar_required | refused | 113 | 105 | - | - |
| stage4.refuse.sb.form8938 | refused | 114 | 106 | - | - |
| stage4.refuse.sb.line8 | refused | 115 | 106 | - | - |
| stage4.sb.foreign_no_filing | complete | 116 | 109 | 116 | 116 |
| stage4.refuse.sb.unsupported.simultaneous | refused | 114 | 104 | - | - |
| stage4.refuse.scope.schedule1 | refused | 74 | 67 | - | - |
| scope.reg.nol_casualty_no_business | refused | 107 | 100 | - | - |
| stage4.refuse.scope.credits | refused | 112 | 103 | - | - |
| stage4.refuse.scope.other_income | refused | 93 | 85 | - | - |
| stage4.refuse.scope.other_line16 | refused | 108 | 100 | - | - |
| stage4.refuse.married | refused | 104 | 98 | - | - |
| stage4.sdtw.special_rates | complete | 133 | 121 | 133 | 133 |
| stage4.sdtw.skip22 | complete | 133 | 120 | 132 | 133 |
| stage4.sdtw.skip32 | complete | 123 | 114 | 123 | 123 |
| stage4.sdtw.twenty_percent | complete | 133 | 121 | 133 | 133 |
| stage4.sdtw.lower_bracket | complete | 131 | 119 | 131 | 131 |
| stage4.sdtw.line12_takes_line9 | complete | 142 | 125 | 142 | 142 |
| stage4.mut.sdtw_28pct_no_1250 | complete | 133 | 122 | 133 | 133 |
| stage4.mut.sdtw_1250_line32_is_line1 | complete | 131 | 121 | 131 | 131 |
| stage4.feeders.shortloss | complete | 138 | 120 | 138 | 138 |

<!-- Hand-written findings below this line are kept when the tool rewrites the report. -->











## Findings (hand-written; tax year 2025, from the tables above as first written)

**What the numbers show (observation).**

- Today's order is at, or within 3 questions of, the floor on all 161 complete returns. On the full profile, the 12 complete Stage 5
  and generated returns ask a mean of 111.2 questions against a floor of 110.9. The only gap is generated.4: it asks 264 where the floor
  is 261, and the three extra questions are the Form 8962 templates interview-rules already holds under `walked_unused` (BUG-0487).
  On the slice profiles, 10 stage4 fixtures ask one question their slice targets do not read (`dependent.parent_home_paid`,
  `person.blind`). Across all returns, the floor is 0% below static (0.1% before rounding).
- The expected-pruning order, which does not know the answers, saves nothing on any return. In the one case where order matters
  (BUG-0487), the deciding value is Form 8962 line 5, a computed amount: no closed answer to a single question removes the three
  questions, so a one-step probe cannot see the saving.
- Most of the length is closed answers that are read. The complete returns answer 86% of their questions false, 0 or none (Stage 5
  82%; minimal returns 96%; the minimal "nothing at all" return asks about 80). On the full profile, 60 templates are asked and
  answered closed on every one of the 12 complete returns, and the evaluation reads every one of them. Of those 60,
  `gate_frequencies.yaml` puts 37 below the 5% rare-situation cut.

**What this suggests (interpretation; moderate credence).** Answer-dependent ordering (T-251) is not worth building to shorten
the federal interview as the model now stands. This is about as strong as a measurement here gets, because the floor is a bound,
not a sample: no order can ask fewer questions than the answered inputs the complete return reads, and the oracle order attains that
floor on every return. The reason is structural. Because conjunctions were rewritten as nested `choose`, the questions that
stay reachable are ones the evaluation reads. That leaves nothing for order to prune. The owner's "142 of 165 answered no" is real,
and it reproduces here at the same ratio (about 77 to 96% closed). It is a breadth problem: flat top-level screens, each read, each
asked of everyone. Fewer questions would take new umbrella gates in the formal model (for example, one "any of these rare
situations?" input whose no makes the rows below it unreachable), which is a model change under the gates design. It is not an
interview-layer change. Grouping those rows on rare-situation grids, as the design already proposes, would cut screens, but each row
would still be an answer.

**Limits.** These are synthetic returns, not real filers. The Stage 5 fixtures are hand-written scenarios, and 9 of the 12 generated
returns end refused, so only 3 complete generated returns are measured. Refused returns (92 of 253) are not measured beyond
static order. The no-order-can-avoid count is exact for these returns. How it generalizes to real filers rests on how well the
fixtures represent them, and that is not measured. The expected order is one heuristic among many. A smarter one cannot beat the
floor, which static order already reaches, so its absence does not change the conclusion.
