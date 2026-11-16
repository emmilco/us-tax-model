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
| Stage 5 whole returns | 9 | 3 | 0 | 139.6 | 167 | 120.2 (86%) | 139.6 | 139.6 | 0% | 0% |
| generated returns | 4 | 8 | 0 | 181.3 | 209 | 150.3 (83%) | 181.3 | 181.3 | 0% | 0% |
| minimal returns | 116 | 0 | 0 | 118.0 | 134 | 114.6 (97%) | 118.0 | 118.0 | 0% | 0% |
| **full profile, Stage 5 and generated** | 13 | 11 | 0 | 152.4 | 209 | 129.5 (85%) | 152.4 | 152.4 | 0% | 0% |
| **all** | 129 | 11 | 0 | 121.5 | 209 | 116.1 (96%) | 121.5 | 121.5 | 0% | 0% |

## Closed answers no order avoids (missing-gate candidates)

Templates asked, read by the complete return and answered closed, on the full profile, listed when at least half of the 13 complete
Stage 5 and generated returns ask them closed (count of 116 complete minimal returns beside). *Kind*: `gate guard` is read by a gate's guard
(asking it is the gate working); `behind a gate` is already gated and its gate was open; `ungated` has no gate line above it, so only a
new gate in the formal model (one question whose no makes it unreachable) could hide it. *Share yes* is the situation's share of all
returns in `gate_frequencies.yaml` where the file names the template (- where it does not).

102 templates are asked and answered closed on every one of the 13 returns; 28 of them have a recorded share
yes below the rare-situation cut (0.05).

| Template | Kind | Share yes | Stage 5 and generated | Minimal |
|---|---|---|---|---|
| `$f1095a` | ungated | 0.085 | 13 | 116 |
| `$retirement` | ungated | 0.2357 | 13 | 116 |
| `$sc` | ungated | 0.1898 | 13 | 116 |
| `f1040.tax_exempt_interest` | ungated | - | 13 | 116 |
| `f2441.care` | ungated | 0.045 | 13 | 116 |
| `f8863.paid` | ungated | 0.09 | 13 | 116 |
| `f8959.territory_w2` | ungated | 0.006 | 13 | 116 |
| `household.community_property` | ungated | 0.2335 | 13 | 116 |
| `person.blind` | ungated | 0.004 | 13 | 116 |
| `person.inherited_account` | ungated | - | 13 | 116 |
| `person.rrta` | ungated | 0.0015 | 13 | 116 |
| `person.x_archer_excess` | ungated | - | 13 | 116 |
| `qbi.coop_patron` | ungated | - | 13 | 116 |
| `refund.any` | ungated | - | 13 | 116 |
| `s1.cod_any` | ungated | 0.006 | 13 | 116 |
| `s1.inmate_wages` | ungated | - | 13 | 116 |
| `s1.ltc_payout` | ungated | - | 13 | 116 |
| `s1a.carloan` | ungated | 0.03 | 13 | 116 |
| `s1a.overtime` | ungated | 0.1471 | 13 | 116 |
| `s1a.tips` | ungated | 0.0195 | 13 | 116 |
| `s2.credit_recapture` | ungated | - | 13 | 116 |
| `s2.hsa_testing` | ungated | - | 13 | 116 |
| `s2.iso_vested` | ungated | - | 13 | 116 |
| `s2.other_tax` | ungated | - | 13 | 116 |
| `s3.credit_bond` | ungated | 0.012 | 13 | 116 |
| `s3.disability_retired` | ungated | - | 13 | 116 |
| `s3.line10` | ungated | 0.0153 | 13 | 116 |
| `s3.repaid_income` | ungated | 0.002 | 13 | 116 |
| `sa.bond_premium` | ungated | - | 13 | 116 |
| `sa.debt_instrument_loss` | ungated | - | 13 | 116 |
| `sa.dependent` | ungated | 0.0469 | 13 | 116 |
| `sa.elect_itemize` | ungated | - | 13 | 116 |
| `sa.estate_tax_income` | ungated | - | 13 | 116 |
| `sa.excluded_income` | ungated | 0.004 | 13 | 116 |
| `sa.impairment_work` | ungated | - | 13 | 116 |
| `sa.pension_unrecovered` | ungated | - | 13 | 116 |
| `sa.sales_tax_wish` | ungated | - | 13 | 116 |
| `sb.account_any` | ungated | - | 13 | 116 |
| `sb.asset_any` | ungated | - | 13 | 116 |
| `sb.company_any` | ungated | - | 13 | 116 |
| `sb.territory_any` | ungated | - | 13 | 116 |
| `sb.trust_any` | ungated | - | 13 | 116 |
| `scope.archer_msa` | ungated | - | 13 | 116 |
| `scope.attorney_fees` | ungated | - | 13 | 116 |
| `scope.chapter11` | ungated | - | 13 | 116 |
| `scope.disaster_distribution` | ungated | - | 13 | 116 |
| `scope.education_recapture` | ungated | - | 13 | 116 |
| `scope.f8814` | ungated | - | 13 | 116 |
| `scope.farm` | ungated | - | 13 | 116 |
| `scope.k1` | ungated | - | 13 | 116 |
| `scope.reforestation` | ungated | - | 13 | 116 |
| `sd.carryover` | ungated | 0.045 | 13 | 116 |
| `sd.casualty` | ungated | 0.025 | 13 | 116 |
| `sd.condemned` | ungated | 0.025 | 13 | 116 |
| `sd.qof` | ungated | - | 13 | 116 |
| `sd.sec1256` | ungated | 0.025 | 13 | 116 |
| `sd.small_business_stock` | ungated | 0.025 | 13 | 116 |
| `sd.trader_election` | ungated | 0.025 | 13 | 116 |
| `f1040.digital_assets` | gate guard | - | 13 | 115 |
| `f1040.withheld_other_any` | gate guard | - | 13 | 115 |
| `f2441.benefits` | gate guard | 0.012 | 13 | 115 |
| `f5695.any` | gate guard | 0.0252 | 13 | 115 |
| `person.eligible_educator` | gate guard | - | 13 | 115 |
| `person.ira_owner` | gate guard | - | 13 | 115 |
| `person.x_edu_account` | gate guard | - | 13 | 115 |
| `qbi.prior_form` | gate guard | - | 13 | 115 |
| `s1.alaska_any` | gate guard | - | 13 | 115 |
| `s1.alimony_any` | gate guard | - | 13 | 115 |
| `s1.hobby_any` | gate guard | - | 13 | 115 |
| `s1.jury_any` | gate guard | - | 13 | 115 |
| `s1.scholarship_any` | gate guard | - | 13 | 115 |
| `s1.uc_any` | gate guard | - | 13 | 115 |
| `s1.winnings_any` | gate guard | - | 13 | 115 |
| `s2.household_help` | gate guard | - | 13 | 115 |
| `s2.options_any` | gate guard | - | 13 | 115 |
| `s3.adoption_any` | gate guard | 0.012 | 13 | 115 |
| `s3.ev` | gate guard | 0.012 | 13 | 115 |
| `s3.farmland` | gate guard | 0.002 | 13 | 115 |
| `s3.foreign_any` | gate guard | 0.002 | 13 | 115 |
| `s3.kerosene` | gate guard | 0.0019 | 13 | 115 |
| `s3.prior_other_forms` | gate guard | 0.012 | 13 | 115 |
| `sa.personal_property_tax_any` | gate guard | - | 13 | 115 |
| `sa.state_tax_other_any` | gate guard | - | 13 | 115 |
| `scope.armed_forces` | gate guard | - | 13 | 115 |
| `scope.business_before` | gate guard | - | 13 | 115 |
| `scope.foreign_shares` | gate guard | - | 13 | 115 |
| `scope.medicaid_waiver` | gate guard | - | 13 | 115 |
| `scope.nol` | gate guard | - | 13 | 115 |
| `scope.noncitizen` | gate guard | - | 13 | 115 |
| `scope.pay_no_w2` | gate guard | - | 13 | 115 |
| `scope.recovery` | gate guard | - | 13 | 115 |
| `scope.religious_work` | gate guard | - | 13 | 115 |
| `scope.rental` | gate guard | - | 13 | 115 |
| `sd.sold_other` | gate guard | 0.025 | 13 | 115 |
| `ssb.any` | gate guard | - | 13 | 115 |
| `household.married_dec31` | behind a gate | 0.3656 | 13 | 0 |
| `household.spouse_died_this_year` | behind a gate | 0.006 | 13 | 0 |
| `s1.nqdc_pension` | behind a gate | - | 13 | 0 |
| `s2.w2_marks` | behind a gate | - | 13 | 0 |
| `scope.artist_official` | behind a gate | - | 13 | 0 |
| `scope.excess_deferral` | behind a gate | - | 13 | 0 |
| `scope.w2_marks` | behind a gate | - | 13 | 0 |
| `$dependent` | ungated | 0.2937 | 12 | 116 |
| `$oi8z` | ungated | 0.0485 | 12 | 116 |
| `sli.any` | ungated | - | 12 | 116 |
| `$f8889` | ungated | 0.11 | 9 | 116 |
| `$sales` | ungated | 0.13 | 9 | 116 |
| `f4952.has_interest` | gate guard | 0.01 | 9 | 115 |
| `sa.medical_any` | ungated | - | 8 | 116 |
| `sa.medical_premiums` | ungated | - | 8 | 116 |
| `div.any` | gate guard | - | 8 | 115 |
| `$interest` | ungated | 0.3441 | 7 | 116 |
| `sa.home_other` | ungated | - | 7 | 116 |
| `sa.home_owner` | ungated | - | 7 | 116 |
| `f1040.estimated_any` | gate guard | - | 7 | 115 |
| `sa.gift_carryover` | ungated | - | 7 | 115 |
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
| f1116.mint_line33_refused_line20_zero_line18 | refused | 160 | 133 | - | - |
| stage5.return.owed | complete | 148 | 126 | 148 | 148 |
| stage5.return.refund | complete | 129 | 117 | 129 | 129 |
| stage5.return.itemized | complete | 167 | 127 | 167 | 167 |
| stage5.refuse.screens | refused | 97 | 91 | - | - |
| stage5.refuse.other_income | refused | 115 | 109 | - | - |
| stage5.return.refund_f4952_screens_unused | complete | 129 | 117 | 129 | 129 |
| stage5.return.refund_f8960_unsupported_unused | complete | 129 | 117 | 129 | 129 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 129 | 117 | 129 | 129 |
| stage5.return.refund_f8960_refund_unused | complete | 129 | 117 | 129 | 129 |
| stage5.return.refund_combat_pay_no_children | complete | 129 | 117 | 129 | 129 |
| stage5.return.itemized_f8960_allocation_unused | complete | 167 | 127 | 167 | 167 |

### generated returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| generated.0 | complete | 170 | 149 | 170 | 170 |
| generated.1 | refused | 345 | 248 | - | - |
| generated.2 | refused | 148 | 119 | - | - |
| generated.3 | refused | 171 | 138 | - | - |
| generated.4 | complete | 185 | 146 | 185 | 185 |
| generated.5 | refused | 173 | 121 | - | - |
| generated.6 | complete | 161 | 142 | 161 | 161 |
| generated.7 | refused | 206 | 151 | - | - |
| generated.8 | refused | 194 | 147 | - | - |
| generated.9 | refused | 254 | 185 | - | - |
| generated.10 | complete | 209 | 164 | 209 | 209 |
| generated.11 | refused | 198 | 149 | - | - |

### minimal returns

| Return | Status | Static | Closed | Floor | Expected |
|---|---|---|---|---|---|
| every gate closed | complete | 117 | 114 | 117 | 117 |
| asset.industry = true alone | complete | 117 | 114 | 117 | 117 |
| asset.listed = true alone | complete | 117 | 114 | 117 | 117 |
| asset.software = true alone | complete | 117 | 114 | 117 | 117 |
| dependent.ever_married = true alone | complete | 117 | 114 | 117 | 117 |
| dependent.lived_all_year = true alone | complete | 117 | 114 | 117 | 117 |
| dependent.ptc_files = true alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "sibling" alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "sibling_descendant" alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "parent" alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "parent_relative" alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "in_law" alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "household_member" alone | complete | 117 | 114 | 117 | 117 |
| dependent.relationship = "other" alone | complete | 117 | 114 | 117 | 117 |
| div.any = true alone | complete | 122 | 118 | 122 | 122 |
| eic.lived_with_relative = true alone | complete | 117 | 114 | 117 | 117 |
| f1040.digital_assets = true alone | complete | 118 | 114 | 118 | 118 |
| f1040.estimated_any = true alone | complete | 118 | 114 | 118 | 118 |
| f1040.withheld_other_any = true alone | complete | 119 | 115 | 119 | 119 |
| f2441.benefits = true alone | complete | 128 | 124 | 128 | 128 |
| f4952.has_interest = true alone | complete | 120 | 116 | 120 | 120 |
| f5695.any = true alone | complete | 134 | 130 | 134 | 134 |
| f5695.line17b = true alone | complete | 117 | 114 | 117 | 117 |
| f5695.line21a = true alone | complete | 117 | 114 | 117 | 117 |
| f8853c.periodic = true alone | complete | 117 | 114 | 117 | 117 |
| f8889.coverage_year = "family" alone | complete | 117 | 114 | 117 | 117 |
| f8889.coverage_year = "changed" alone | complete | 117 | 114 | 117 | 117 |
| f8889.inherited_any = true alone | complete | 117 | 114 | 117 | 117 |
| f8962.other_coverage = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b1 = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b14a = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b15o = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b18a = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b19 = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b2 = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b20z = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b3 = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b4a = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b5 = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b6a = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b8 = true alone | complete | 117 | 114 | 117 | 117 |
| k1p.has_b9a = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box13o_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box16_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box17_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box1_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box2_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box3_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box4_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box5_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box7_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.box8_any = true alone | complete | 117 | 114 | 117 | 117 |
| k1s.prior_any = true alone | complete | 117 | 114 | 117 | 117 |
| ny_it201.ask.city_resident = true alone | complete | 117 | 114 | 117 | 117 |
| ny_it201.ask.est_any = true alone | complete | 117 | 114 | 117 | 117 |
| ny_it201.ask.owes_use_tax = true alone | complete | 117 | 114 | 117 | 117 |
| person.eligible_educator = true alone | complete | 118 | 114 | 118 | 118 |
| person.ira_owner = true alone | complete | 119 | 115 | 119 | 119 |
| person.x_edu_account = true alone | complete | 119 | 115 | 119 | 119 |
| qbi.prior_form = true alone | complete | 119 | 115 | 119 | 119 |
| rental.has_advertising = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_cleaning = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_commissions = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_insurance = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_legal = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_management = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_mortgage = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_other = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_other_interest = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_repairs = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_supplies = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_taxes = true alone | complete | 117 | 114 | 117 | 117 |
| rental.has_utilities = true alone | complete | 117 | 114 | 117 | 117 |
| rental.prior_any = true alone | complete | 117 | 114 | 117 | 117 |
| rental.short_stays = true alone | complete | 117 | 114 | 117 | 117 |
| retirement.rollover_any = true alone | complete | 117 | 114 | 117 | 117 |
| royalty.expenses_any = true alone | complete | 117 | 114 | 117 | 117 |
| s1.alaska_any = true alone | complete | 118 | 114 | 118 | 118 |
| s1.alimony_any = true alone | complete | 118 | 114 | 118 | 118 |
| s1.hobby_any = true alone | complete | 118 | 114 | 118 | 118 |
| s1.jury_any = true alone | complete | 118 | 114 | 118 | 118 |
| s1.scholarship_any = true alone | complete | 118 | 114 | 118 | 118 |
| s1.uc_any = true alone | complete | 118 | 114 | 118 | 118 |
| s1.winnings_any = true alone | complete | 120 | 116 | 120 | 120 |
| s2.household_help = true alone | complete | 118 | 114 | 118 | 118 |
| s2.options_any = true alone | complete | 119 | 115 | 119 | 119 |
| s3.adoption_any = true alone | complete | 120 | 116 | 120 | 120 |
| s3.ev = true alone | complete | 120 | 116 | 120 | 120 |
| s3.farmland = true alone | complete | 118 | 114 | 118 | 118 |
| s3.foreign_any = true alone | complete | 122 | 118 | 122 | 122 |
| s3.kerosene = true alone | complete | 118 | 114 | 118 | 118 |
| s3.prior_other_forms = true alone | complete | 121 | 117 | 121 | 121 |
| sa.gifts = true alone | complete | 119 | 115 | 119 | 119 |
| sa.personal_property_tax_any = true alone | complete | 118 | 114 | 118 | 118 |
| sa.state_tax_any = true alone | complete | 118 | 114 | 118 | 118 |
| sa.state_tax_other_any = true alone | complete | 118 | 114 | 118 | 118 |
| sc.employees = true alone | complete | 117 | 114 | 117 | 117 |
| sc.goods = true alone | complete | 117 | 114 | 117 | 117 |
| sc.travel_meals = true alone | complete | 117 | 114 | 117 | 117 |
| scope.armed_forces = true alone | complete | 120 | 116 | 120 | 120 |
| scope.business_before = true alone | complete | 120 | 116 | 120 | 120 |
| scope.foreign_shares = true alone | complete | 119 | 115 | 119 | 119 |
| scope.medicaid_waiver = true alone | complete | 119 | 115 | 119 | 119 |
| scope.nol = true alone | complete | 121 | 117 | 121 | 121 |
| scope.noncitizen = true alone | complete | 118 | 114 | 118 | 118 |
| scope.pay_no_w2 = true alone | complete | 122 | 118 | 122 | 122 |
| scope.recovery = true alone | complete | 121 | 117 | 121 | 121 |
| scope.religious_work = true alone | complete | 119 | 115 | 119 | 119 |
| scope.rental = true alone | complete | 123 | 119 | 123 | 123 |
| scveh.others_use = true alone | complete | 117 | 114 | 117 | 117 |
| scveh.smr_always = true alone | complete | 117 | 114 | 117 | 117 |
| sd.route_each = true alone | complete | 117 | 114 | 117 | 117 |
| sd.sold_other = true alone | complete | 120 | 116 | 120 | 120 |
| ssb.any = true alone | complete | 118 | 114 | 118 | 118 |
| ssb.prior_year_pay = true alone | complete | 117 | 114 | 117 | 117 |
| tipjob.listed = true alone | complete | 117 | 114 | 117 | 117 |

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
