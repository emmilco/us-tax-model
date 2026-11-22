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
| Stage 5 whole returns | 9 | 3 | 0 | 140.8 | 169 | 121.4 (86%) | 140.8 | 140.8 | 0% | 0% |
| generated returns | 2 | 8 | 2 | 238.5 | 299 | 190.5 (80%) | 238.5 | 238.5 | 0% | 0% |
| minimal returns | 116 | 0 | 0 | 119.0 | 135 | 115.7 (97%) | 119.0 | 119.0 | 0% | 0% |
| **full profile, Stage 5 and generated** | 11 | 11 | 2 | 158.5 | 299 | 134.0 (85%) | 158.5 | 158.5 | 0% | 0% |
| **all** | 127 | 11 | 2 | 122.5 | 299 | 117.3 (96%) | 122.5 | 122.5 | 0% | 0% |

## Closed answers no order avoids (missing-gate candidates)

Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the 11 complete
Stage 5 and generated returns ask them closed (count of 116 complete minimal returns beside). *Kind*: `gate guard` is read by a gate's guard
(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a
new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all
returns in `gate_frequencies.yaml` where the file names the template (- where it does not).

104 templates are asked and answered closed on every one of the 11 returns; 29 of them have a recorded share
yes below the rare-situation cut (0.05).

| Template | Kind | Share yes | Stage 5 and generated | Minimal |
|---|---|---|---|---|
| `$dependent` | ungated | 0.2937 | 11 | 116 |
| `$f1095a` | ungated | 0.085 | 11 | 116 |
| `$oi8z` | ungated | 0.0485 | 11 | 116 |
| `$retirement` | ungated | 0.2357 | 11 | 116 |
| `f2441.care` | ungated | 0.045 | 11 | 116 |
| `f8959.territory_w2` | ungated | 0.006 | 11 | 116 |
| `household.community_property` | ungated | 0.2335 | 11 | 116 |
| `person.blind` | ungated | 0.004 | 11 | 116 |
| `person.inherited_account` | ungated | - | 11 | 116 |
| `person.rrta` | ungated | 0.0015 | 11 | 116 |
| `person.x_archer_excess` | ungated | - | 11 | 116 |
| `qbi.coop_patron` | ungated | - | 11 | 116 |
| `refund.any` | ungated | - | 11 | 116 |
| `s1.cod_any` | ungated | 0.006 | 11 | 116 |
| `s1.inmate_wages` | ungated | - | 11 | 116 |
| `s1.ltc_payout` | ungated | - | 11 | 116 |
| `s1a.carloan` | ungated | 0.03 | 11 | 116 |
| `s1a.overtime` | ungated | 0.1471 | 11 | 116 |
| `s1a.tips` | ungated | 0.0195 | 11 | 116 |
| `s2.credit_recapture` | ungated | - | 11 | 116 |
| `s2.hsa_testing` | ungated | - | 11 | 116 |
| `s2.iso_vested` | ungated | - | 11 | 116 |
| `s2.other_tax` | ungated | - | 11 | 116 |
| `s3.credit_bond` | ungated | 0.012 | 11 | 116 |
| `s3.disability_retired` | ungated | - | 11 | 116 |
| `s3.line10` | ungated | 0.0153 | 11 | 116 |
| `s3.repaid_income` | ungated | 0.002 | 11 | 116 |
| `sa.bond_premium` | ungated | - | 11 | 116 |
| `sa.debt_instrument_loss` | ungated | - | 11 | 116 |
| `sa.dependent` | ungated | 0.0469 | 11 | 116 |
| `sa.elect_itemize` | ungated | - | 11 | 116 |
| `sa.estate_tax_income` | ungated | - | 11 | 116 |
| `sa.excluded_income` | ungated | 0.004 | 11 | 116 |
| `sa.gift_carryover` | ungated | - | 11 | 116 |
| `sa.impairment_work` | ungated | - | 11 | 116 |
| `sa.pension_unrecovered` | ungated | - | 11 | 116 |
| `sa.sales_tax_wish` | ungated | - | 11 | 116 |
| `sb.account_any` | ungated | - | 11 | 116 |
| `sb.asset_any` | ungated | - | 11 | 116 |
| `sb.company_any` | ungated | - | 11 | 116 |
| `sb.territory_any` | ungated | - | 11 | 116 |
| `sb.trust_any` | ungated | - | 11 | 116 |
| `scope.archer_msa` | ungated | - | 11 | 116 |
| `scope.attorney_fees` | ungated | - | 11 | 116 |
| `scope.chapter11` | ungated | - | 11 | 116 |
| `scope.disaster_distribution` | ungated | - | 11 | 116 |
| `scope.education_recapture` | ungated | - | 11 | 116 |
| `scope.f8814` | ungated | - | 11 | 116 |
| `scope.farm` | ungated | - | 11 | 116 |
| `scope.k1` | ungated | - | 11 | 116 |
| `scope.reforestation` | ungated | - | 11 | 116 |
| `scope.treaty` | ungated | - | 11 | 116 |
| `sd.carryover` | ungated | 0.045 | 11 | 116 |
| `sd.casualty` | ungated | 0.025 | 11 | 116 |
| `sd.condemned` | ungated | 0.025 | 11 | 116 |
| `sd.qof` | ungated | - | 11 | 116 |
| `sd.sec1256` | ungated | 0.025 | 11 | 116 |
| `sd.small_business_stock` | ungated | 0.025 | 11 | 116 |
| `sd.trader_election` | ungated | 0.025 | 11 | 116 |
| `f1040.digital_assets` | gate guard | - | 11 | 115 |
| `f1040.tax_exempt_any` | gate guard | - | 11 | 115 |
| `f1040.withheld_other_any` | gate guard | - | 11 | 115 |
| `f2441.benefits` | gate guard | 0.012 | 11 | 115 |
| `f5695.any` | gate guard | 0.0252 | 11 | 115 |
| `person.eligible_educator` | gate guard | - | 11 | 115 |
| `person.ira_owner` | gate guard | - | 11 | 115 |
| `person.x_edu_account` | gate guard | - | 11 | 115 |
| `qbi.prior_form` | gate guard | - | 11 | 115 |
| `s1.alaska_any` | gate guard | - | 11 | 115 |
| `s1.alimony_any` | gate guard | - | 11 | 115 |
| `s1.hobby_any` | gate guard | - | 11 | 115 |
| `s1.jury_any` | gate guard | - | 11 | 115 |
| `s1.scholarship_any` | gate guard | - | 11 | 115 |
| `s1.uc_any` | gate guard | - | 11 | 115 |
| `s1.winnings_any` | gate guard | - | 11 | 115 |
| `s2.household_help` | gate guard | - | 11 | 115 |
| `s2.options_any` | gate guard | - | 11 | 115 |
| `s3.adoption_any` | gate guard | 0.012 | 11 | 115 |
| `s3.ev` | gate guard | 0.012 | 11 | 115 |
| `s3.farmland` | gate guard | 0.002 | 11 | 115 |
| `s3.foreign_any` | gate guard | 0.002 | 11 | 115 |
| `s3.kerosene` | gate guard | 0.0019 | 11 | 115 |
| `s3.prior_other_forms` | gate guard | 0.012 | 11 | 115 |
| `sa.personal_property_tax_any` | gate guard | - | 11 | 115 |
| `sa.state_tax_other_any` | gate guard | - | 11 | 115 |
| `scope.armed_forces` | gate guard | - | 11 | 115 |
| `scope.business_before` | gate guard | - | 11 | 115 |
| `scope.foreign_shares` | gate guard | - | 11 | 115 |
| `scope.medicaid_waiver` | gate guard | - | 11 | 115 |
| `scope.nol` | gate guard | - | 11 | 115 |
| `scope.noncitizen` | gate guard | - | 11 | 115 |
| `scope.pay_no_w2` | gate guard | - | 11 | 115 |
| `scope.recovery` | gate guard | - | 11 | 115 |
| `scope.religious_work` | gate guard | - | 11 | 115 |
| `scope.rental` | gate guard | - | 11 | 115 |
| `sd.sold_other` | gate guard | 0.025 | 11 | 115 |
| `ssb.any` | gate guard | - | 11 | 115 |
| `household.married_dec31` | behind a gate | 0.3656 | 11 | 0 |
| `household.spouse_died_this_year` | behind a gate | 0.006 | 11 | 0 |
| `s1.nqdc_pension` | behind a gate | - | 11 | 0 |
| `s2.w2_marks` | behind a gate | - | 11 | 0 |
| `scope.artist_official` | behind a gate | - | 11 | 0 |
| `scope.excess_deferral` | behind a gate | - | 11 | 0 |
| `scope.w2_marks` | behind a gate | - | 11 | 0 |
| `$sc` | ungated | 0.1898 | 10 | 116 |
| `f8863.paid` | ungated | 0.09 | 10 | 116 |
| `sli.any` | ungated | - | 10 | 116 |
| `$f8889` | ungated | 0.11 | 9 | 116 |
| `$sales` | ungated | 0.13 | 8 | 116 |
| `f4952.has_interest` | gate guard | 0.01 | 8 | 115 |
| `$interest` | ungated | 0.3441 | 7 | 116 |
| `sa.home_other` | ungated | - | 7 | 116 |
| `sa.home_owner` | ungated | - | 7 | 116 |
| `sa.medical_any` | ungated | - | 7 | 116 |
| `sa.medical_premiums` | ungated | - | 7 | 116 |
| `div.any` | gate guard | - | 7 | 115 |
| `sa.gifts` | gate guard | 0.4 | 7 | 115 |
| `sa.state_tax_any` | gate guard | - | 7 | 115 |

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
| f1116.mint_line33_refused_line20_zero_line18 | refused | 161 | 134 | - | - |
| stage5.return.owed | complete | 149 | 127 | 149 | 149 |
| stage5.return.refund | complete | 130 | 118 | 130 | 130 |
| stage5.return.itemized | complete | 169 | 129 | 169 | 169 |
| stage5.refuse.screens | refused | 99 | 93 | - | - |
| stage5.refuse.other_income | refused | 116 | 110 | - | - |
| stage5.return.refund_f4952_screens_unused | complete | 130 | 118 | 130 | 130 |
| stage5.return.refund_f8960_unsupported_unused | complete | 130 | 118 | 130 | 130 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 130 | 118 | 130 | 130 |
| stage5.return.refund_f8960_refund_unused | complete | 130 | 118 | 130 | 130 |
| stage5.return.refund_combat_pay_no_children | complete | 130 | 118 | 130 | 130 |
| stage5.return.itemized_f8960_allocation_unused | complete | 169 | 129 | 169 | 169 |

### generated returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| generated.0 | refused | 165 | 144 | - | - |
| generated.1 | refused | 344 | 249 | - | - |
| generated.2 | refused | 145 | 113 | - | - |
| generated.3 | refused | 184 | 146 | - | - |
| generated.4 | complete | 299 | 229 | 299 | 299 |
| generated.6 | complete | 178 | 152 | 178 | 178 |
| generated.7 | refused | 253 | 188 | - | - |
| generated.8 | refused | 197 | 150 | - | - |
| generated.9 | refused | 243 | 177 | - | - |
| generated.11 | refused | 214 | 159 | - | - |

### minimal returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| every gate closed | complete | 118 | 115 | 118 | 118 |
| asset.listed = true alone | complete | 118 | 115 | 118 | 118 |
| asset.software = true alone | complete | 118 | 115 | 118 | 118 |
| dependent.ever_married = true alone | complete | 118 | 115 | 118 | 118 |
| dependent.lived_all_year = true alone | complete | 118 | 115 | 118 | 118 |
| dependent.own_money = true alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "sibling" alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "sibling_descendant" alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "parent" alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "parent_relative" alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "in_law" alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "household_member" alone | complete | 118 | 115 | 118 | 118 |
| dependent.relationship = "other" alone | complete | 118 | 115 | 118 | 118 |
| div.any = true alone | complete | 123 | 119 | 123 | 123 |
| eic.lived_with_relative = true alone | complete | 118 | 115 | 118 | 118 |
| f1040.digital_assets = true alone | complete | 119 | 115 | 119 | 119 |
| f1040.estimated_any = true alone | complete | 119 | 115 | 119 | 119 |
| f1040.tax_exempt_any = true alone | complete | 119 | 115 | 119 | 119 |
| f1040.withheld_other_any = true alone | complete | 120 | 116 | 120 | 120 |
| f2441.benefits = true alone | complete | 129 | 125 | 129 | 129 |
| f4952.has_interest = true alone | complete | 121 | 117 | 121 | 121 |
| f5695.any = true alone | complete | 135 | 131 | 135 | 135 |
| f5695.line17b = true alone | complete | 118 | 115 | 118 | 118 |
| f5695.line21a = true alone | complete | 118 | 115 | 118 | 118 |
| f8853c.periodic = true alone | complete | 118 | 115 | 118 | 118 |
| f8889.coverage_year = "family" alone | complete | 118 | 115 | 118 | 118 |
| f8889.coverage_year = "changed" alone | complete | 118 | 115 | 118 | 118 |
| f8889.inherited_any = true alone | complete | 118 | 115 | 118 | 118 |
| f8962.other_coverage = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b1 = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b14a = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b15o = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b18a = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b19 = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b2 = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b20z = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b3 = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b4a = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b5 = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b6a = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b8 = true alone | complete | 118 | 115 | 118 | 118 |
| k1p.has_b9a = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box13o_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box16_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box17_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box1_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box2_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box3_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box4_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box5_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box7_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.box8_any = true alone | complete | 118 | 115 | 118 | 118 |
| k1s.prior_any = true alone | complete | 118 | 115 | 118 | 118 |
| ny_it201.ask.bought_untaxed = true alone | complete | 118 | 115 | 118 | 118 |
| ny_it201.ask.city_resident = true alone | complete | 118 | 115 | 118 | 118 |
| ny_it201.ask.est_any = true alone | complete | 118 | 115 | 118 | 118 |
| person.eligible_educator = true alone | complete | 119 | 115 | 119 | 119 |
| person.ira_owner = true alone | complete | 120 | 116 | 120 | 120 |
| person.x_edu_account = true alone | complete | 120 | 116 | 120 | 120 |
| qbi.prior_form = true alone | complete | 120 | 116 | 120 | 120 |
| rental.has_advertising = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_cleaning = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_commissions = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_insurance = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_legal = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_management = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_mortgage = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_other = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_other_interest = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_repairs = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_supplies = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_taxes = true alone | complete | 118 | 115 | 118 | 118 |
| rental.has_utilities = true alone | complete | 118 | 115 | 118 | 118 |
| rental.prior_any = true alone | complete | 118 | 115 | 118 | 118 |
| rental.short_stays = true alone | complete | 118 | 115 | 118 | 118 |
| retirement.rollover_any = true alone | complete | 118 | 115 | 118 | 118 |
| royalty.expenses_any = true alone | complete | 118 | 115 | 118 | 118 |
| s1.alaska_any = true alone | complete | 119 | 115 | 119 | 119 |
| s1.alimony_any = true alone | complete | 119 | 115 | 119 | 119 |
| s1.hobby_any = true alone | complete | 119 | 115 | 119 | 119 |
| s1.jury_any = true alone | complete | 119 | 115 | 119 | 119 |
| s1.scholarship_any = true alone | complete | 119 | 115 | 119 | 119 |
| s1.uc_any = true alone | complete | 119 | 115 | 119 | 119 |
| s1.winnings_any = true alone | complete | 121 | 117 | 121 | 121 |
| s2.household_help = true alone | complete | 119 | 115 | 119 | 119 |
| s2.options_any = true alone | complete | 120 | 116 | 120 | 120 |
| s3.adoption_any = true alone | complete | 121 | 117 | 121 | 121 |
| s3.ev = true alone | complete | 121 | 117 | 121 | 121 |
| s3.farmland = true alone | complete | 119 | 115 | 119 | 119 |
| s3.foreign_any = true alone | complete | 123 | 119 | 123 | 123 |
| s3.kerosene = true alone | complete | 119 | 115 | 119 | 119 |
| s3.prior_other_forms = true alone | complete | 122 | 118 | 122 | 122 |
| sa.gifts = true alone | complete | 121 | 117 | 121 | 121 |
| sa.personal_property_tax_any = true alone | complete | 119 | 115 | 119 | 119 |
| sa.state_tax_any = true alone | complete | 119 | 115 | 119 | 119 |
| sa.state_tax_other_any = true alone | complete | 119 | 115 | 119 | 119 |
| sc.employees = true alone | complete | 118 | 115 | 118 | 118 |
| sc.goods = true alone | complete | 118 | 115 | 118 | 118 |
| sc.travel_meals = true alone | complete | 118 | 115 | 118 | 118 |
| scope.armed_forces = true alone | complete | 121 | 117 | 121 | 121 |
| scope.business_before = true alone | complete | 121 | 117 | 121 | 121 |
| scope.foreign_shares = true alone | complete | 120 | 116 | 120 | 120 |
| scope.medicaid_waiver = true alone | complete | 120 | 116 | 120 | 120 |
| scope.nol = true alone | complete | 122 | 118 | 122 | 122 |
| scope.noncitizen = true alone | complete | 119 | 115 | 119 | 119 |
| scope.pay_no_w2 = true alone | complete | 123 | 119 | 123 | 123 |
| scope.recovery = true alone | complete | 122 | 118 | 122 | 122 |
| scope.religious_work = true alone | complete | 120 | 116 | 120 | 120 |
| scope.rental = true alone | complete | 125 | 121 | 125 | 125 |
| scveh.others_use = true alone | complete | 118 | 115 | 118 | 118 |
| scveh.smr_always = true alone | complete | 118 | 115 | 118 | 118 |
| sd.route_each = true alone | complete | 118 | 115 | 118 | 118 |
| sd.sold_other = true alone | complete | 121 | 117 | 121 | 121 |
| ssb.any = true alone | complete | 119 | 115 | 119 | 119 |
| ssb.prior_year_pay = true alone | complete | 118 | 115 | 118 | 118 |
| tipjob.listed = true alone | complete | 118 | 115 | 118 | 118 |

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
