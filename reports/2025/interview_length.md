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
| Stage 5 whole returns | 9 | 3 | 0 | 142.0 | 171 | 122.7 (86%) | 142.0 | 142.0 | 0% | 0% |
| generated returns | 3 | 8 | 1 | 184.0 | 218 | 156.0 (85%) | 184.0 | 184.0 | 0% | 0% |
| minimal returns | 118 | 0 | 0 | 120.0 | 136 | 116.7 (97%) | 120.0 | 120.0 | 0% | 0% |
| **full profile, Stage 5 and generated** | 12 | 11 | 1 | 152.5 | 218 | 131.0 (86%) | 152.5 | 152.5 | 0% | 0% |
| **all** | 130 | 11 | 1 | 123.0 | 218 | 118.0 (96%) | 123.0 | 123.0 | 0% | 0% |

## Closed answers no order avoids (missing-gate candidates)

Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the 12 complete
Stage 5 and generated returns ask them closed (count of 118 complete minimal returns beside). *Kind*: `gate guard` is read by a gate's guard
(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a
new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all
returns in `gate_frequencies.yaml` where the file names the template (- where it does not).

106 templates are asked and answered closed on every one of the 12 returns; 29 of them have a recorded share
yes below the rare-situation cut (0.05).

| Template | Kind | Share yes | Stage 5 and generated | Minimal |
|---|---|---|---|---|
| `$dependent` | ungated | 0.2937 | 12 | 118 |
| `$oi8z` | ungated | 0.0485 | 12 | 118 |
| `$retirement` | ungated | 0.2357 | 12 | 118 |
| `$sc` | ungated | 0.1898 | 12 | 118 |
| `f2441.care` | ungated | 0.045 | 12 | 118 |
| `f8863.paid` | ungated | 0.09 | 12 | 118 |
| `f8959.territory_w2` | ungated | 0.006 | 12 | 118 |
| `household.community_property` | ungated | 0.2335 | 12 | 118 |
| `person.blind` | ungated | 0.004 | 12 | 118 |
| `person.inherited_account` | ungated | - | 12 | 118 |
| `person.rrta` | ungated | 0.0015 | 12 | 118 |
| `person.x_archer_excess` | ungated | - | 12 | 118 |
| `refund.any` | ungated | - | 12 | 118 |
| `s1.cod_any` | ungated | 0.006 | 12 | 118 |
| `s1.inmate_wages` | ungated | - | 12 | 118 |
| `s1.ltc_payout` | ungated | - | 12 | 118 |
| `s1a.carloan` | ungated | 0.03 | 12 | 118 |
| `s1a.overtime` | ungated | 0.1471 | 12 | 118 |
| `s1a.tips` | ungated | 0.0195 | 12 | 118 |
| `s2.credit_recapture` | ungated | - | 12 | 118 |
| `s2.hsa_testing` | ungated | - | 12 | 118 |
| `s2.iso_vested` | ungated | - | 12 | 118 |
| `s2.other_tax` | ungated | - | 12 | 118 |
| `s3.credit_bond` | ungated | 0.012 | 12 | 118 |
| `s3.disability_retired` | ungated | - | 12 | 118 |
| `s3.line10` | ungated | 0.0153 | 12 | 118 |
| `s3.repaid_income` | ungated | 0.002 | 12 | 118 |
| `sa.bond_premium` | ungated | - | 12 | 118 |
| `sa.debt_instrument_loss` | ungated | - | 12 | 118 |
| `sa.dependent` | ungated | 0.0469 | 12 | 118 |
| `sa.elect_itemize` | ungated | - | 12 | 118 |
| `sa.estate_tax_income` | ungated | - | 12 | 118 |
| `sa.excluded_income` | ungated | 0.004 | 12 | 118 |
| `sa.gift_carryover` | ungated | - | 12 | 118 |
| `sa.impairment_work` | ungated | - | 12 | 118 |
| `sa.pension_unrecovered` | ungated | - | 12 | 118 |
| `sa.sales_tax_wish` | ungated | - | 12 | 118 |
| `sb.account_any` | ungated | - | 12 | 118 |
| `sb.asset_any` | ungated | - | 12 | 118 |
| `sb.company_any` | ungated | - | 12 | 118 |
| `sb.territory_any` | ungated | - | 12 | 118 |
| `sb.trust_any` | ungated | - | 12 | 118 |
| `scope.archer_msa` | ungated | - | 12 | 118 |
| `scope.attorney_fees` | ungated | - | 12 | 118 |
| `scope.chapter11` | ungated | - | 12 | 118 |
| `scope.disaster_distribution` | ungated | - | 12 | 118 |
| `scope.education_recapture` | ungated | - | 12 | 118 |
| `scope.f8814` | ungated | - | 12 | 118 |
| `scope.farm` | ungated | - | 12 | 118 |
| `scope.k1` | ungated | - | 12 | 118 |
| `scope.reforestation` | ungated | - | 12 | 118 |
| `scope.remic` | ungated | - | 12 | 118 |
| `scope.trade_act_repaid` | ungated | - | 12 | 118 |
| `scope.treaty` | ungated | - | 12 | 118 |
| `sd.carryover` | ungated | 0.045 | 12 | 118 |
| `sd.casualty` | ungated | 0.025 | 12 | 118 |
| `sd.condemned` | ungated | 0.025 | 12 | 118 |
| `sd.qof` | ungated | - | 12 | 118 |
| `sd.sec1256` | ungated | 0.025 | 12 | 118 |
| `sd.small_business_stock` | ungated | 0.025 | 12 | 118 |
| `sd.trader_election` | ungated | 0.025 | 12 | 118 |
| `f1040.digital_assets` | gate guard | - | 12 | 117 |
| `f1040.tax_exempt_any` | gate guard | - | 12 | 117 |
| `f1040.withheld_other_any` | gate guard | - | 12 | 117 |
| `f2441.benefits` | gate guard | 0.012 | 12 | 117 |
| `f5695.any` | gate guard | 0.0252 | 12 | 117 |
| `person.eligible_educator` | gate guard | - | 12 | 117 |
| `person.ira_owner` | gate guard | - | 12 | 117 |
| `person.x_edu_account` | gate guard | - | 12 | 117 |
| `qbi.prior_form` | gate guard | - | 12 | 117 |
| `s1.alaska_any` | gate guard | - | 12 | 117 |
| `s1.alimony_any` | gate guard | - | 12 | 117 |
| `s1.hobby_any` | gate guard | - | 12 | 117 |
| `s1.jury_any` | gate guard | - | 12 | 117 |
| `s1.scholarship_any` | gate guard | - | 12 | 117 |
| `s1.uc_any` | gate guard | - | 12 | 117 |
| `s1.winnings_any` | gate guard | - | 12 | 117 |
| `s2.household_help` | gate guard | - | 12 | 117 |
| `s2.options_any` | gate guard | - | 12 | 117 |
| `s3.adoption_any` | gate guard | 0.012 | 12 | 117 |
| `s3.ev` | gate guard | 0.012 | 12 | 117 |
| `s3.farmland` | gate guard | 0.002 | 12 | 117 |
| `s3.foreign_any` | gate guard | 0.002 | 12 | 117 |
| `s3.kerosene` | gate guard | 0.0019 | 12 | 117 |
| `s3.prior_other_forms` | gate guard | 0.012 | 12 | 117 |
| `sa.personal_property_tax_any` | gate guard | - | 12 | 117 |
| `sa.state_tax_other_any` | gate guard | - | 12 | 117 |
| `scope.armed_forces` | gate guard | - | 12 | 117 |
| `scope.business_before` | gate guard | - | 12 | 117 |
| `scope.foreign_shares` | gate guard | - | 12 | 117 |
| `scope.medicaid_waiver` | gate guard | - | 12 | 117 |
| `scope.nol` | gate guard | - | 12 | 117 |
| `scope.noncitizen` | gate guard | - | 12 | 117 |
| `scope.pay_no_w2` | gate guard | - | 12 | 117 |
| `scope.recovery` | gate guard | - | 12 | 117 |
| `scope.religious_work` | gate guard | - | 12 | 117 |
| `scope.rental` | gate guard | - | 12 | 117 |
| `sd.sold_other` | gate guard | 0.025 | 12 | 117 |
| `ssb.any` | gate guard | - | 12 | 117 |
| `household.married_dec31` | behind a gate | 0.3656 | 12 | 0 |
| `household.spouse_died_this_year` | behind a gate | 0.006 | 12 | 0 |
| `s1.nqdc_pension` | behind a gate | - | 12 | 0 |
| `s2.w2_marks` | behind a gate | - | 12 | 0 |
| `scope.artist_official` | behind a gate | - | 12 | 0 |
| `scope.excess_deferral` | behind a gate | - | 12 | 0 |
| `scope.w2_marks` | behind a gate | - | 12 | 0 |
| `$f1095a` | ungated | 0.085 | 11 | 118 |
| `sli.any` | ungated | - | 11 | 118 |
| `$f8889` | ungated | 0.11 | 9 | 118 |
| `$sales` | ungated | 0.13 | 9 | 118 |
| `sa.medical_any` | ungated | - | 8 | 118 |
| `sa.medical_premiums` | ungated | - | 8 | 118 |
| `div.any` | gate guard | - | 8 | 117 |
| `f4952.has_interest` | gate guard | 0.01 | 8 | 117 |
| `sa.gifts` | gate guard | 0.4 | 8 | 117 |
| `$interest` | ungated | 0.3441 | 7 | 118 |
| `sa.home_other` | ungated | - | 7 | 118 |
| `sa.home_owner` | ungated | - | 7 | 118 |
| `sa.state_tax_any` | gate guard | - | 7 | 117 |
| `f1040.estimated_any` | gate guard | - | 6 | 117 |

## Questions order could avoid

Templates asked in static order and not read by the complete return, by number of complete returns (all groups): the questions a
better order (or a nested `choose`) would not ask. On the full profile these are the templates interview-rules holds under
`walked_unused`.

| Template | Returns |
|---|---|

## Per return

### Stage 5 whole returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| f1116.mint_line33_refused_line20_zero_line18 | refused | 162 | 135 | - | - |
| stage5.return.owed | complete | 150 | 128 | 150 | 150 |
| stage5.return.refund | complete | 131 | 119 | 131 | 131 |
| stage5.return.itemized | complete | 171 | 131 | 171 | 171 |
| stage5.refuse.screens | refused | 99 | 93 | - | - |
| stage5.refuse.other_income | refused | 118 | 112 | - | - |
| stage5.return.refund_f4952_screens_unused | complete | 131 | 119 | 131 | 131 |
| stage5.return.refund_f8960_unsupported_unused | complete | 131 | 119 | 131 | 131 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 131 | 119 | 131 | 131 |
| stage5.return.refund_f8960_refund_unused | complete | 131 | 119 | 131 | 131 |
| stage5.return.refund_combat_pay_no_children | complete | 131 | 119 | 131 | 131 |
| stage5.return.itemized_f8960_allocation_unused | complete | 171 | 131 | 171 | 171 |

### generated returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| generated.0 | complete | 173 | 152 | 173 | 173 |
| generated.1 | refused | 273 | 204 | - | - |
| generated.2 | refused | 131 | 101 | - | - |
| generated.3 | refused | 198 | 155 | - | - |
| generated.4 | complete | 218 | 172 | 218 | 218 |
| generated.5 | refused | 177 | 125 | - | - |
| generated.6 | complete | 161 | 144 | 161 | 161 |
| generated.7 | refused | 193 | 138 | - | - |
| generated.8 | refused | 207 | 159 | - | - |
| generated.9 | refused | 170 | 131 | - | - |
| generated.11 | refused | 200 | 151 | - | - |

### minimal returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| every gate closed | complete | 119 | 116 | 119 | 119 |
| asset.listed = true alone | complete | 119 | 116 | 119 | 119 |
| asset.software = true alone | complete | 119 | 116 | 119 | 119 |
| dependent.ever_married = true alone | complete | 119 | 116 | 119 | 119 |
| dependent.lived_all_year = true alone | complete | 119 | 116 | 119 | 119 |
| dependent.own_money = true alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "sibling" alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "sibling_descendant" alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "parent" alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "parent_relative" alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "in_law" alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "household_member" alone | complete | 119 | 116 | 119 | 119 |
| dependent.relationship = "other" alone | complete | 119 | 116 | 119 | 119 |
| div.any = true alone | complete | 124 | 120 | 124 | 124 |
| eic.lived_with_relative = true alone | complete | 119 | 116 | 119 | 119 |
| f1040.digital_assets = true alone | complete | 120 | 116 | 120 | 120 |
| f1040.estimated_any = true alone | complete | 120 | 116 | 120 | 120 |
| f1040.tax_exempt_any = true alone | complete | 120 | 116 | 120 | 120 |
| f1040.withheld_other_any = true alone | complete | 121 | 117 | 121 | 121 |
| f2441.benefits = true alone | complete | 130 | 126 | 130 | 130 |
| f4952.has_interest = true alone | complete | 122 | 118 | 122 | 122 |
| f5695.any = true alone | complete | 136 | 132 | 136 | 136 |
| f5695.line17b = true alone | complete | 119 | 116 | 119 | 119 |
| f5695.line21a = true alone | complete | 119 | 116 | 119 | 119 |
| f8853c.periodic = true alone | complete | 119 | 116 | 119 | 119 |
| f8889.coverage_year = "family" alone | complete | 119 | 116 | 119 | 119 |
| f8889.coverage_year = "changed" alone | complete | 119 | 116 | 119 | 119 |
| f8889.inherited_any = true alone | complete | 119 | 116 | 119 | 119 |
| f8962.other_coverage = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b1 = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b14a = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b15o = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b18a = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b19 = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b2 = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b20z = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b3 = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b4a = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b5 = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b6a = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b8 = true alone | complete | 119 | 116 | 119 | 119 |
| k1p.has_b9a = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box13o_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box16_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box17_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box1_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box2_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box3_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box4_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box5_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box7_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.box8_any = true alone | complete | 119 | 116 | 119 | 119 |
| k1s.prior_any = true alone | complete | 119 | 116 | 119 | 119 |
| ny_it201.ask.bought_untaxed = true alone | complete | 119 | 116 | 119 | 119 |
| ny_it201.ask.city_resident = true alone | complete | 119 | 116 | 119 | 119 |
| ny_it201.ask.est_any = true alone | complete | 119 | 116 | 119 | 119 |
| person.eligible_educator = true alone | complete | 120 | 116 | 120 | 120 |
| person.ira_owner = true alone | complete | 121 | 117 | 121 | 121 |
| person.x_edu_account = true alone | complete | 121 | 117 | 121 | 121 |
| qbi.prior_form = true alone | complete | 121 | 117 | 121 | 121 |
| rental.has_advertising = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_cleaning = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_commissions = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_insurance = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_legal = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_management = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_mortgage = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_other = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_other_interest = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_repairs = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_supplies = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_taxes = true alone | complete | 119 | 116 | 119 | 119 |
| rental.has_utilities = true alone | complete | 119 | 116 | 119 | 119 |
| rental.prior_any = true alone | complete | 119 | 116 | 119 | 119 |
| rental.short_stays = true alone | complete | 119 | 116 | 119 | 119 |
| retirement.rollover_any = true alone | complete | 119 | 116 | 119 | 119 |
| royalty.expenses_any = true alone | complete | 119 | 116 | 119 | 119 |
| rprop.kind = "nonresidential" alone | complete | 119 | 116 | 119 | 119 |
| rprop.kind = "personal" alone | complete | 119 | 116 | 119 | 119 |
| s1.alaska_any = true alone | complete | 120 | 116 | 120 | 120 |
| s1.alimony_any = true alone | complete | 120 | 116 | 120 | 120 |
| s1.hobby_any = true alone | complete | 120 | 116 | 120 | 120 |
| s1.jury_any = true alone | complete | 120 | 116 | 120 | 120 |
| s1.scholarship_any = true alone | complete | 120 | 116 | 120 | 120 |
| s1.uc_any = true alone | complete | 120 | 116 | 120 | 120 |
| s1.winnings_any = true alone | complete | 122 | 118 | 122 | 122 |
| s2.household_help = true alone | complete | 120 | 116 | 120 | 120 |
| s2.options_any = true alone | complete | 121 | 117 | 121 | 121 |
| s3.adoption_any = true alone | complete | 122 | 118 | 122 | 122 |
| s3.ev = true alone | complete | 122 | 118 | 122 | 122 |
| s3.farmland = true alone | complete | 120 | 116 | 120 | 120 |
| s3.foreign_any = true alone | complete | 124 | 120 | 124 | 124 |
| s3.kerosene = true alone | complete | 120 | 116 | 120 | 120 |
| s3.prior_other_forms = true alone | complete | 123 | 119 | 123 | 123 |
| sa.gifts = true alone | complete | 122 | 118 | 122 | 122 |
| sa.personal_property_tax_any = true alone | complete | 120 | 116 | 120 | 120 |
| sa.state_tax_any = true alone | complete | 120 | 116 | 120 | 120 |
| sa.state_tax_other_any = true alone | complete | 120 | 116 | 120 | 120 |
| sc.employees = true alone | complete | 119 | 116 | 119 | 119 |
| sc.goods = true alone | complete | 119 | 116 | 119 | 119 |
| sc.travel_meals = true alone | complete | 119 | 116 | 119 | 119 |
| scope.armed_forces = true alone | complete | 122 | 118 | 122 | 122 |
| scope.business_before = true alone | complete | 122 | 118 | 122 | 122 |
| scope.foreign_shares = true alone | complete | 121 | 117 | 121 | 121 |
| scope.medicaid_waiver = true alone | complete | 121 | 117 | 121 | 121 |
| scope.nol = true alone | complete | 123 | 119 | 123 | 123 |
| scope.noncitizen = true alone | complete | 120 | 116 | 120 | 120 |
| scope.pay_no_w2 = true alone | complete | 124 | 120 | 124 | 124 |
| scope.recovery = true alone | complete | 123 | 119 | 123 | 123 |
| scope.religious_work = true alone | complete | 121 | 117 | 121 | 121 |
| scope.rental = true alone | complete | 126 | 122 | 126 | 126 |
| scveh.others_use = true alone | complete | 119 | 116 | 119 | 119 |
| scveh.smr_always = true alone | complete | 119 | 116 | 119 | 119 |
| sd.route_each = true alone | complete | 119 | 116 | 119 | 119 |
| sd.sold_other = true alone | complete | 123 | 119 | 123 | 123 |
| ssb.any = true alone | complete | 122 | 118 | 122 | 122 |
| ssb.prior_year_pay = true alone | complete | 119 | 116 | 119 | 119 |
| tipjob.listed = true alone | complete | 119 | 116 | 119 | 119 |

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
