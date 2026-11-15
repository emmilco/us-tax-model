# The interview's asking order, measured

Written by `node engine/dist/main.js interview-order --write` (engine/src/interview-order.ts; deterministic, no model calls). Returns walked: the whole-return fixtures, the generated returns and the minimal returns, in the `full` profile.

Each return is walked in the interview's own order to completion or refusal. A *re-entry* is a place where an order number
(or a form) is left and later entered again. A *delayed child* is a gated question not asked directly after the yes/no question
that opened it (a question that is no descendant of that parent was asked between them). Causes: **sorting**, the question was
already reachable and the bank's order put another first, or a topic was left for a child that the bank places in another
topic; **late**, a question became reachable only part-way (the one that re-enters, or an earlier-sorted one the topic was left
for), and the entry names the answer it was waiting on. A question's order number is the first thing the interview sorts by,
so an order number is re-entered for the late cause, or for a child with a lower order number than its parent.

## Totals

| returns | walks | questions (mean) | order re-entries: sorting | late | form re-entries: sorting | late | delayed children: sorting | late |
|---|---|---|---|---|---|---|---|---|
| whole-return fixtures | 11 | 115.8 | 0.0 | 0.0 | 22.5 | 5.4 | 2.5 | 0.0 |
| generated returns | 12 | 84.3 | 0.0 | 0.3 | 10.8 | 5.0 | 5.1 | 0.1 |
| minimal returns | 55 | 116.6 | 0.0 | 0.0 | 24.2 | 4.0 | 0.9 | 0.0 |

The counts are means per walk.

## What the late questions waited on

Every late finding, by the question that became reachable part-way and the answer it waited on, with the number of walks showing it
and what it caused (an order number re-entered, a form re-entered, a child delayed).

| question | waited on | its parent or roster? | caused | walks |
|---|---|---|---|---|
| `person.blind` | `sa.dependent` | no | form | 74 |
| `household.ever_married` | `f1040.status` | no | form | 64 |
| `person.eic_ssn` | `scope.attorney_fees` | no | form | 57 |
| `scope.w2_marks` | `$w2` | no | form | 13 |
| `sd.distributions` | `div.any` | yes | form | 6 |
| `s2.mortgage_subsidy` | `sa.mortgage_interest` | no | form | 5 |
| `s3.mcc` | `sa.mortgage_interest` | no | form | 5 |
| `f1040.line3a` | `sb.ordinary_dividends` | no | form | 4 |
| `person.x_hsa_prior_excess` | `$f8889` | no | form | 4 |
| `qbi.prior_form` | `scope.attorney_fees` | no | form | 4 |
| `sd.route_each` | `$sales` | no | form | 4 |
| `sa.foreign_tax_deduct` | `ftc.taxes` | no | form | 3 |
| `f1040.tax_exempt_interest` | `person.eic_ssn` | no | form | 2 |
| `person.plan` | `$sc` | no | form | 2 |
| `s2.lookback` | `$sc` | no | form | 2 |
| `div.box12` | `person.eic_ssn` | no | child, form, order | 1 |
| `f5695.carry` | `s3.prior_other_forms` | yes | form | 1 |
| `ftc.carryover` | `s3.prior_other_forms` | yes | order | 1 |
| `household.home_cost` | `dependent.tin` | no | form | 1 |
| `household.home_cost` | `dependent.parent_home_paid` | no | form | 1 |
| `household.married_dec31` | `$person` | no | form | 1 |
| `person.sav_claimed` | `sli.assisted_any` | no | form | 1 |
| `person.x_ira_prior_excess` | `person.x_archer_excess` | no | child | 1 |
| `sc.at_risk` | `scope.business_before` | no | form, order | 1 |
| `w2.box3` | `$sc` | no | form, order | 1 |

## Delayed children for the sorting cause

By child and parent, with the number of walks.

| child | place | parent | place | walks |
|---|---|---|---|---|
| `sa.charity_limited` | order 200 seq 40 | `sa.gifts` | order 200 seq 5 | 7 |
| `sa.line11` | order 200 seq 41 | `sa.gifts` | order 200 seq 5 | 7 |
| `sa.line5a` | order 200 seq 30 | `sa.state_tax_any` | order 200 seq 2 | 7 |
| `sa.line5b` | order 200 seq 26 | `sa.home_owner` | order 200 seq 1 | 6 |
| `sa.mortgage_interest` | order 200 seq 20 | `sa.home_owner` | order 200 seq 1 | 6 |
| `sa.mortgage_unreported` | order 200 seq 21 | `sa.home_owner` | order 200 seq 1 | 6 |
| `sa.property_tax_other_any` | order 200 seq 27 | `sa.home_owner` | order 200 seq 1 | 6 |
| `sa.line1` | order 200 seq 50 | `sa.medical_any` | order 200 seq 6 | 5 |
| `div.other_boxes` | order 272 seq 7 | `div.any` | order 272 seq 1 | 4 |
| `sd.distributions` | order 272 seq 4 | `div.any` | order 272 seq 1 | 4 |
| `sd.f2439` | order 272 seq 18 | `div.any` | order 272 seq 1 | 4 |
| `sales.route` | order 274 seq 11 | `sd.route_each` | order 274 seq 2 | 2 |
| `sc.line14` | order 252 seq 26 | `sc.employees` | order 252 seq 17 | 2 |
| `sc.line19` | order 252 seq 27 | `sc.employees` | order 252 seq 17 | 2 |
| `sc.line24a` | order 252 seq 21 | `sc.travel_meals` | order 252 seq 16 | 2 |
| `sc.line26` | order 252 seq 25 | `sc.employees` | order 252 seq 17 | 2 |
| `sc.line35` | order 252 seq 28 | `sc.goods` | order 252 seq 18 | 2 |
| `sc.line36` | order 252 seq 29 | `sc.goods` | order 252 seq 18 | 2 |
| `sc.line37` | order 252 seq 30 | `sc.goods` | order 252 seq 18 | 2 |
| `sc.line38` | order 252 seq 31 | `sc.goods` | order 252 seq 18 | 2 |
| `sc.line39` | order 252 seq 32 | `sc.goods` | order 252 seq 18 | 2 |
| `sc.line41` | order 252 seq 33 | `sc.goods` | order 252 seq 18 | 2 |
| `sc.meals_100` | order 252 seq 24 | `sc.travel_meals` | order 252 seq 16 | 2 |
| `sc.meals_50` | order 252 seq 22 | `sc.travel_meals` | order 252 seq 16 | 2 |
| `sc.meals_80` | order 252 seq 23 | `sc.travel_meals` | order 252 seq 16 | 2 |
| `scope.nonresident` | order 113 seq 10 | `scope.noncitizen` | order 113 seq 1 | 2 |
| `f1040.line25b` | order 300 seq 3 | `f1040.withheld_other_any` | order 300 seq 1 | 1 |
| `f1040.line25c_other` | order 300 seq 4 | `f1040.withheld_other_any` | order 300 seq 1 | 1 |
| `f5695.audit` | order 230 seq 12 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.biomass` | order 230 seq 18 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.central_ac` | order 230 seq 15 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.doors` | order 230 seq 9 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.furnace` | order 230 seq 17 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.geothermal` | order 230 seq 5 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.heat_pump` | order 230 seq 13 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.hp_water_heater` | order 230 seq 14 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.insulation` | order 230 seq 8 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.line5a` | order 230 seq 6 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.panel` | order 230 seq 11 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.solar` | order 230 seq 2 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.solar_water` | order 230 seq 3 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.water_heater` | order 230 seq 16 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.wind` | order 230 seq 4 | `f5695.any` | order 220 seq 4 | 1 |
| `f5695.windows` | order 230 seq 10 | `f5695.any` | order 220 seq 4 | 1 |
| `person.sav_trad` | order 180 seq 10 | `person.ira_owner` | order 180 seq 1 | 1 |
| `s1.alaska_dividend` | order 160 seq 20 | `s1.alaska_any` | order 160 seq 5 | 1 |
| `s1.alimony` | order 161 seq 10 | `s1.alimony_any` | order 161 seq 1 | 1 |
| `s1.gambling_winnings` | order 160 seq 13 | `s1.winnings_any` | order 160 seq 2 | 1 |
| `s1.jury_pay` | order 160 seq 18 | `s1.jury_any` | order 160 seq 4 | 1 |
| `s1.olympic` | order 160 seq 16 | `s1.winnings_any` | order 160 seq 2 | 1 |
| `s1.prizes` | order 160 seq 15 | `s1.winnings_any` | order 160 seq 2 | 1 |
| `s1.scholarship_taxable` | order 160 seq 17 | `s1.scholarship_any` | order 160 seq 3 | 1 |
| `s1.uc_paid` | order 160 seq 10 | `s1.uc_any` | order 160 seq 1 | 1 |
| `s3.adoption` | order 126 seq 3 | `s3.adoption_any` | order 126 seq 1 | 1 |
| `s3.adoption_earlier` | order 126 seq 4 | `s3.adoption_any` | order 126 seq 1 | 1 |
| `s3.ev_bought` | order 225 seq 3 | `s3.ev` | order 220 seq 2 | 1 |
| `s3.ev_dealer` | order 225 seq 2 | `s3.ev` | order 220 seq 2 | 1 |
| `s3.ev_equipment` | order 225 seq 5 | `s3.ev` | order 220 seq 2 | 1 |
| `s3.farmland_deferral` | order 290 seq 4 | `s3.farmland` | order 290 seq 2 | 1 |
| `s3.kerosene_credit` | order 225 seq 7 | `s3.kerosene` | order 220 seq 3 | 1 |
| `sa.line5c` | order 200 seq 32 | `sa.personal_property_tax_any` | order 200 seq 4 | 1 |
| `sa.state_tax_other` | order 200 seq 31 | `sa.state_tax_other_any` | order 200 seq 3 | 1 |
| `scope.adoption_benefits` | order 126 seq 6 | `s3.adoption_any` | order 126 seq 1 | 1 |
| `scope.church_exempt_wages` | order 146 seq 11 | `scope.religious_work` | order 146 seq 3 | 1 |
| `scope.clergy` | order 146 seq 10 | `scope.religious_work` | order 146 seq 3 | 1 |
| `scope.military_move` | order 113 seq 14 | `scope.armed_forces` | order 113 seq 3 | 1 |
| `scope.reservist_expenses` | order 113 seq 13 | `scope.armed_forces` | order 113 seq 3 | 1 |
| `scope.reservist_repaid` | order 113 seq 15 | `scope.armed_forces` | order 113 seq 3 | 1 |
| `scope.unearned_2700` | order 113 seq 11 | `scope.under24` | order 113 seq 2 | 1 |
| `sd.business_property` | order 274 seq 26 | `sd.sold_other` | order 274 seq 20 | 1 |
| `sd.installment` | order 274 seq 27 | `sd.sold_other` | order 274 seq 20 | 1 |
| `sd.like_kind` | order 274 seq 28 | `sd.sold_other` | order 274 seq 20 | 1 |

## What the bank states

Read from the built question bank alone. A question that states no `seq` is asked after those of its order number that do, by id.

| order | questions | state a seq | forms |
|---|---|---|---|
| 100 | 2 | 2 | f1040, person |
| 101 | 3 | 3 | household |
| 102 | 3 | 3 | household |
| 103 | 3 | 3 | household |
| 110 | 4 | 4 | person |
| 111 | 1 | 1 | sa |
| 112 | 1 | 1 | person |
| 113 | 11 | 11 | sa, scope |
| 118 | 1 | 1 | s3 |
| 120 | 36 | 36 | dependent |
| 126 | 6 | 6 | s3, scope |
| 130 | 3 | 3 | scope |
| 140 | 11 | 11 | person, w2 |
| 145 | 6 | 6 | s1, s2, scope |
| 146 | 9 | 9 | f8959, s1, s2, scope |
| 150 | 3 | 3 | person, s1a |
| 151 | 6 | 6 | tipjob |
| 153 | 5 | 5 | otjob |
| 155 | 12 | 12 | f2441, s2, w2 |
| 156 | 6 | 6 | f2441 |
| 157 | 9 | 9 | dcprov, dependent |
| 158 | 2 | 2 | s8812, scope |
| 160 | 18 | 18 | s1 |
| 161 | 12 | 12 | s1, scope |
| 165 | 18 | 18 | refund |
| 170 | 50 | 50 | retirement |
| 180 | 24 | 24 | ira, person |
| 185 | 8 | 8 | ssb |
| 190 | 32 | 32 | f8889, person |
| 192 | 1 | 1 | person |
| 193 | 4 | 4 | s2, scope |
| 195 | 1 | 1 | f1095a |
| 196 | 18 | 18 | f8962 |
| 197 | 45 | 45 | f1095a |
| 198 | 2 | 2 | f8962 |
| 199 | 4 | 4 | dependent, f8962 |
| 200 | 39 | 39 | gift, s2, s3, sa, sd |
| 220 | 6 | 6 | f5695, f8863, s1a, s3, sli |
| 221 | 12 | 12 | carloan |
| 225 | 5 | 5 | s3 |
| 230 | 68 | 68 | f5695 |
| 241 | 29 | 29 | dependent, person |
| 242 | 1 | 1 | f8863 |
| 243 | 3 | 3 | person |
| 244 | 5 | 5 | sli |
| 250 | 5 | 5 | sc |
| 251 | 7 | 7 | sc |
| 252 | 40 | 40 | sc |
| 255 | 45 | 45 | scveh |
| 257 | 32 | 32 | asset |
| 258 | 7 | 7 | s179, scope |
| 259 | 3 | 3 | ltc |
| 260 | 8 | 8 | person |
| 261 | 1 | 1 | person |
| 263 | 1 | 1 | ira |
| 265 | 2 | 2 | scope |
| 267 | 1 | 1 | s2 |
| 270 | 3 | 3 | interest |
| 271 | 1 | 1 | f1040 |
| 272 | 18 | 18 | div, f1040, qbi, sb, sd |
| 273 | 3 | 3 | sb |
| 274 | 19 | 19 | sales, sd |
| 276 | 16 | 16 | clcw, clcw26, f4952, f8960, sd |
| 278 | 3 | 3 | f8960 |
| 279 | 5 | 5 | ftc, s3 |
| 280 | 5 | 5 | ftc |
| 284 | 1 | 1 | sa |
| 285 | 13 | 13 | sb, scope |
| 290 | 9 | 9 | f5695, s3 |
| 291 | 3 | 3 | s2 |
| 294 | 3 | 3 | oi8z |
| 295 | 2 | 2 | scope |
| 296 | 5 | 5 | qbi |
| 300 | 5 | 5 | f1040 |
| 301 | 2 | 2 | f1040 |
| 305 | 1 | 1 | s3 |
| 310 | 2 | 2 | household, s8812 |
| 311 | 2 | 2 | person |
| 313 | 6 | 6 | eic |
| 314 | 2 | 2 | dependent |
| 315 | 5 | 5 | person |
| 316 | 13 | 13 | w2 |
| 317 | 3 | 3 | retirement |
| 318 | 1 | 1 | s3 |

Gated questions the bank does not place directly after their parent: 139.

| child | parent | why |
|---|---|---|
| `household.considered_unmarried` | `household.married_dec31` | the parent is in order 101 and the child in order 102 |
| `household.cp_married` | `household.ever_married` | the parent is in order 101 and the child in order 103 |
| `person.died_at_64` | `person.born_jan1` | 1 question that the parent does not open stand between them (the first: `person.under16_at_year_end`) |
| `scope.nonresident` | `scope.noncitizen` | 4 questions that the parent does not open stand between them (the first: `scope.under24`) |
| `scope.unearned_2700` | `scope.under24` | 4 questions that the parent does not open stand between them (the first: `scope.armed_forces`) |
| `scope.reservist_expenses` | `scope.armed_forces` | 5 questions that the parent does not open stand between them (the first: `sa.excluded_income`) |
| `scope.military_move` | `scope.armed_forces` | 5 questions that the parent does not open stand between them (the first: `sa.excluded_income`) |
| `scope.reservist_repaid` | `scope.armed_forces` | 5 questions that the parent does not open stand between them (the first: `sa.excluded_income`) |
| `dependent.joint_return` | `dependent.ever_married` | 4 questions that the parent does not open stand between them (the first: `dependent.own_money`) |
| `s3.adoption` | `s3.adoption_any` | 1 question that the parent does not open stand between them (the first: `scope.f8814`) |
| `s3.adoption_earlier` | `s3.adoption_any` | 1 question that the parent does not open stand between them (the first: `scope.f8814`) |
| `scope.adoption_benefits` | `s3.adoption_any` | 1 question that the parent does not open stand between them (the first: `scope.f8814`) |
| `scope.performer_expenses` | `scope.artist_official` | 1 question that the parent does not open stand between them (the first: `scope.excess_deferral`) |
| `scope.clergy` | `scope.religious_work` | 2 questions that the parent does not open stand between them (the first: `f8959.territory_w2`) |
| `scope.church_exempt_wages` | `scope.religious_work` | 2 questions that the parent does not open stand between them (the first: `f8959.territory_w2`) |
| `s2.iso` | `s2.options_any` | 2 questions that the parent does not open stand between them (the first: `scope.clergy`) |
| `s1.stock_options` | `s2.options_any` | 2 questions that the parent does not open stand between them (the first: `scope.clergy`) |
| `f2441.nondependent` | `f2441.care_other` | 4 questions that the parent does not open stand between them (the first: `f2441.prior_year`) |
| `s1.uc_paid` | `s1.uc_any` | 5 questions that the parent does not open stand between them (the first: `s1.winnings_any`) |
| `s1.gambling_winnings` | `s1.winnings_any` | 7 questions that the parent does not open stand between them (the first: `s1.scholarship_any`) |
| `s1.prizes` | `s1.winnings_any` | 8 questions that the parent does not open stand between them (the first: `s1.scholarship_any`) |
| `s1.olympic` | `s1.winnings_any` | 8 questions that the parent does not open stand between them (the first: `s1.scholarship_any`) |
| `s1.scholarship_taxable` | `s1.scholarship_any` | 10 questions that the parent does not open stand between them (the first: `s1.jury_any`) |
| `s1.jury_pay` | `s1.jury_any` | 10 questions that the parent does not open stand between them (the first: `s1.alaska_any`) |
| `s1.alaska_dividend` | `s1.alaska_any` | 11 questions that the parent does not open stand between them (the first: `s1.hobby_any`) |
| `s1.hobby_income` | `s1.hobby_any` | 11 questions that the parent does not open stand between them (the first: `s1.uc_paid`) |
| `s1.alimony` | `s1.alimony_any` | 5 questions that the parent does not open stand between them (the first: `s1.cod_any`) |
| `retirement.dis_early` | `retirement.disability` | 2 questions that the parent does not open stand between them (the first: `retirement.pso_exclusion`) |
| `retirement.dis_terror` | `retirement.disability` | 2 questions that the parent does not open stand between them (the first: `retirement.pso_exclusion`) |
| `retirement.dis_military` | `retirement.disability` | 2 questions that the parent does not open stand between them (the first: `retirement.pso_exclusion`) |
| `retirement.lump_sum` | `retirement.born_1936` | 3 questions that the parent does not open stand between them (the first: `retirement.dis_early`) |
| `person.sav_trad` | `person.ira_owner` | 3 questions that the parent does not open stand between them (the first: `person.inherited_account`) |
| `person.sav_roth` | `person.ira_owner` | 4 questions that the parent does not open stand between them (the first: `person.inherited_account`) |
| `person.x_ira_prior_excess` | `person.ira_owner` | 8 questions that the parent does not open stand between them (the first: `person.inherited_account`) |
| `person.rmd_missed` | `person.inherited_account` | 13 questions that the parent does not open stand between them (the first: `person.x_edu_account`) |
| `person.x_edu_taxable` | `person.x_edu_account` | 13 questions that the parent does not open stand between them (the first: `person.x_archer_excess`) |
| `person.x_edu_excess` | `person.x_edu_account` | 13 questions that the parent does not open stand between them (the first: `person.x_archer_excess`) |
| `sa.mortgage_interest` | `sa.home_other` | 3 questions that the parent does not open stand between them (the first: `sa.gift_carryover`) |
| `sa.mortgage_unreported` | `sa.home_other` | 3 questions that the parent does not open stand between them (the first: `sa.gift_carryover`) |
| `sa.line5b` | `sa.home_other` | 7 questions that the parent does not open stand between them (the first: `sa.gift_carryover`) |
| `sa.property_tax_other_any` | `sa.home_other` | 7 questions that the parent does not open stand between them (the first: `sa.gift_carryover`) |
| `sa.line5a` | `sa.state_tax_any` | 17 questions that the parent does not open stand between them (the first: `sa.state_tax_other_any`) |
| `sa.state_tax_other` | `sa.state_tax_other_any` | 17 questions that the parent does not open stand between them (the first: `sa.personal_property_tax_any`) |
| `sa.line5c` | `sa.personal_property_tax_any` | 17 questions that the parent does not open stand between them (the first: `sa.gifts`) |
| `sa.charity_limited` | `sa.gifts` | 17 questions that the parent does not open stand between them (the first: `sa.medical_any`) |
| `sa.line11` | `sa.gifts` | 17 questions that the parent does not open stand between them (the first: `sa.medical_any`) |
| `sa.line1` | `sa.medical_premiums` | 19 questions that the parent does not open stand between them (the first: `sd.casualty`) |
| `s3.ev_dealer` | `s3.ev` | the parent is in order 220 and the child in order 225 |
| `s3.ev_bought` | `s3.ev` | the parent is in order 220 and the child in order 225 |
| `s3.ev_equipment` | `s3.ev` | the parent is in order 220 and the child in order 225 |
| `s3.kerosene_credit` | `s3.kerosene` | the parent is in order 220 and the child in order 225 |
| `f5695.solar` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.solar_water` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.wind` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.geothermal` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.line5a` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.insulation` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.doors` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.windows` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.panel` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.audit` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.heat_pump` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.hp_water_heater` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.central_ac` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.water_heater` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.furnace` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.biomass` | `f5695.any` | the parent is in order 220 and the child in order 230 |
| `f5695.line1` | `f5695.solar` | 20 questions that the parent does not open stand between them (the first: `f5695.solar_water`) |
| `f5695.line2` | `f5695.solar_water` | 20 questions that the parent does not open stand between them (the first: `f5695.wind`) |
| `f5695.line3` | `f5695.wind` | 20 questions that the parent does not open stand between them (the first: `f5695.geothermal`) |
| `f5695.line4` | `f5695.geothermal` | 20 questions that the parent does not open stand between them (the first: `f5695.line5a`) |
| `f5695.line18a` | `f5695.insulation` | 23 questions that the parent does not open stand between them (the first: `f5695.doors`) |
| `f5695.line19a` | `f5695.doors` | 23 questions that the parent does not open stand between them (the first: `f5695.windows`) |
| `f5695.line19d_i` | `f5695.doors` | 23 questions that the parent does not open stand between them (the first: `f5695.windows`) |
| `f5695.line19d_ii` | `f5695.doors` | 23 questions that the parent does not open stand between them (the first: `f5695.windows`) |
| `f5695.line19e` | `f5695.doors` | 23 questions that the parent does not open stand between them (the first: `f5695.windows`) |
| `f5695.line20a_i` | `f5695.windows` | 27 questions that the parent does not open stand between them (the first: `f5695.panel`) |
| `f5695.line20a_ii` | `f5695.windows` | 27 questions that the parent does not open stand between them (the first: `f5695.panel`) |
| `f5695.line20a_iii` | `f5695.windows` | 27 questions that the parent does not open stand between them (the first: `f5695.panel`) |
| `f5695.line20a_iv` | `f5695.windows` | 27 questions that the parent does not open stand between them (the first: `f5695.panel`) |
| `f5695.line20b` | `f5695.windows` | 27 questions that the parent does not open stand between them (the first: `f5695.panel`) |
| `f5695.line29a` | `f5695.heat_pump` | 33 questions that the parent does not open stand between them (the first: `f5695.hp_water_heater`) |
| `f5695.line29b` | `f5695.heat_pump` | 33 questions that the parent does not open stand between them (the first: `f5695.hp_water_heater`) |
| `f5695.line29c` | `f5695.hp_water_heater` | 34 questions that the parent does not open stand between them (the first: `f5695.central_ac`) |
| `f5695.line29d` | `f5695.hp_water_heater` | 34 questions that the parent does not open stand between them (the first: `f5695.central_ac`) |
| `f5695.line29e` | `f5695.biomass` | 32 questions that the parent does not open stand between them (the first: `f5695.business_use`) |
| `f5695.line29f` | `f5695.biomass` | 32 questions that the parent does not open stand between them (the first: `f5695.business_use`) |
| `f5695.line22a` | `f5695.central_ac` | 38 questions that the parent does not open stand between them (the first: `f5695.water_heater`) |
| `f5695.line22b` | `f5695.central_ac` | 38 questions that the parent does not open stand between them (the first: `f5695.water_heater`) |
| `f5695.line23a_i` | `f5695.water_heater` | 40 questions that the parent does not open stand between them (the first: `f5695.furnace`) |
| `f5695.line23a_ii` | `f5695.water_heater` | 40 questions that the parent does not open stand between them (the first: `f5695.furnace`) |
| `f5695.line23b` | `f5695.water_heater` | 40 questions that the parent does not open stand between them (the first: `f5695.furnace`) |
| `f5695.line24a` | `f5695.furnace` | 43 questions that the parent does not open stand between them (the first: `f5695.biomass`) |
| `f5695.line24b` | `f5695.furnace` | 43 questions that the parent does not open stand between them (the first: `f5695.biomass`) |
| `f5695.line25a` | `f5695.panel` | 52 questions that the parent does not open stand between them (the first: `f5695.audit`) |
| `f5695.line26a` | `f5695.audit` | 54 questions that the parent does not open stand between them (the first: `f5695.heat_pump`) |
| `sli.interest` | `sli.any` | the parent is in order 220 and the child in order 244 |
| `sli.unqualified_any` | `sli.any` | the parent is in order 220 and the child in order 244 |
| `sli.assisted_any` | `sli.any` | the parent is in order 220 and the child in order 244 |
| `sc.line24a` | `sc.travel_meals` | 4 questions that the parent does not open stand between them (the first: `sc.employees`) |
| `sc.meals_50` | `sc.travel_meals` | 4 questions that the parent does not open stand between them (the first: `sc.employees`) |
| `sc.meals_80` | `sc.travel_meals` | 4 questions that the parent does not open stand between them (the first: `sc.employees`) |
| `sc.meals_100` | `sc.travel_meals` | 4 questions that the parent does not open stand between them (the first: `sc.employees`) |
| `sc.line26` | `sc.employees` | 7 questions that the parent does not open stand between them (the first: `sc.goods`) |
| `sc.line14` | `sc.employees` | 7 questions that the parent does not open stand between them (the first: `sc.goods`) |
| `sc.line19` | `sc.employees` | 7 questions that the parent does not open stand between them (the first: `sc.goods`) |
| `sc.line35` | `sc.goods` | 9 questions that the parent does not open stand between them (the first: `sc.ho_uses`) |
| `sc.line36` | `sc.goods` | 9 questions that the parent does not open stand between them (the first: `sc.ho_uses`) |
| `sc.line37` | `sc.goods` | 9 questions that the parent does not open stand between them (the first: `sc.ho_uses`) |
| `sc.line38` | `sc.goods` | 9 questions that the parent does not open stand between them (the first: `sc.ho_uses`) |
| `sc.line39` | `sc.goods` | 9 questions that the parent does not open stand between them (the first: `sc.ho_uses`) |
| `sc.line41` | `sc.goods` | 9 questions that the parent does not open stand between them (the first: `sc.ho_uses`) |
| `scveh.leasing` | `scveh.others_use` | 1 question that the parent does not open stand between them (the first: `scveh.method_other`) |
| `scveh.exempt_use` | `scveh.others_use` | 1 question that the parent does not open stand between them (the first: `scveh.method_other`) |
| `scveh.qbu_low` | `scveh.others_use` | 1 question that the parent does not open stand between them (the first: `scveh.method_other`) |
| `asset.software_spread` | `asset.software` | 2 questions that the parent does not open stand between them (the first: `asset.industry`) |
| `asset.industry_item` | `asset.industry` | 2 questions that the parent does not open stand between them (the first: `asset.long_production`) |
| `sd.distributions` | `div.any` | 1 question that the parent does not open stand between them (the first: `f1040.line3a`) |
| `div.box12` | `div.any` | 2 questions that the parent does not open stand between them (the first: `f1040.line3a`) |
| `div.other_boxes` | `div.any` | 2 questions that the parent does not open stand between them (the first: `f1040.line3a`) |
| `sd.f2439` | `div.any` | 3 questions that the parent does not open stand between them (the first: `f1040.line3a`) |
| `sales.route` | `sd.route_each` | 7 questions that the parent does not open stand between them (the first: `sales.box`) |
| `sd.business_property` | `sd.sold_other` | 4 questions that the parent does not open stand between them (the first: `sd.sec1256`) |
| `sd.installment` | `sd.sold_other` | 4 questions that the parent does not open stand between them (the first: `sd.sec1256`) |
| `sd.like_kind` | `sd.sold_other` | 4 questions that the parent does not open stand between them (the first: `sd.sec1256`) |
| `ftc.carryover` | `s3.prior_other_forms` | the parent is in order 290 and the child in order 279 |
| `ftc.taxes` | `s3.foreign_any` | the parent is in order 279 and the child in order 280 |
| `sb.fbar_required` | `sb.territory_any` | 1 question that the parent does not open stand between them (the first: `scope.foreign_shares`) |
| `sb.form8938` | `sb.territory_any` | 1 question that the parent does not open stand between them (the first: `scope.foreign_shares`) |
| `sb.line8` | `sb.territory_any` | 1 question that the parent does not open stand between them (the first: `scope.foreign_shares`) |
| `sb.form5471` | `sb.territory_any` | 1 question that the parent does not open stand between them (the first: `scope.foreign_shares`) |
| `scope.pfic` | `scope.foreign_shares` | 5 questions that the parent does not open stand between them (the first: `sb.fbar_required`) |
| `scope.cfc` | `scope.foreign_shares` | 5 questions that the parent does not open stand between them (the first: `sb.fbar_required`) |
| `s3.farmland_deferral` | `s3.farmland` | 1 question that the parent does not open stand between them (the first: `s3.repaid_income`) |
| `f1040.line25b` | `f1040.withheld_other_any` | 1 question that the parent does not open stand between them (the first: `f1040.estimated_any`) |
| `f1040.line25c_other` | `f1040.withheld_other_any` | 1 question that the parent does not open stand between them (the first: `f1040.estimated_any`) |
| `f1040.line26` | `f1040.estimated_any` | 2 questions that the parent does not open stand between them (the first: `f1040.line25b`) |
| `household.credit_disallowed` | `eic.qc_of_another` | the parent is in order 313 and the child in order 310 |
| `s3.elderly_credit` | `s3.disability_retired` | the parent is in order 118 and the child in order 318 |

## Each walk

A walk's line of runs reads `order:form×questions`. For a minimal return with one gate opened, only the findings the
every-gate-closed return does not also have are listed.

### whole-return fixtures

**stage5.return.owed**: 146 questions, complete; order re-entries 0, form re-entries 29 sorting and 7 late, delayed children 3 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×15 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 272:sd×1 · 273:sb×2 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 280:ftc×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×2 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 41 by `scope.w2_marks` (order 145 seq 3), left after step 21, 19 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 48 by `s2.options_any` (order 146 seq 5), left after step 39, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 53 by `s2.household_help` (order 155 seq 3), left after step 48, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 54 by `s1.uc_any` (order 160 seq 1), left after step 40, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 65 by `scope.recovery` (order 161 seq 6), left after step 46, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 68 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 44 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 74 by `scope.disaster_distribution` (order 193 seq 1), left after step 65, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 76 by `s2.hsa_testing` (order 193 seq 3), left after step 53, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 77 by `scope.education_recapture` (order 193 seq 4), left after step 75, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 79 by `sa.home_owner` (order 200 seq 1), left after step 13, 65 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 89 by `sa.estate_tax_income` (order 200 seq 70), left after step 87, 1 between. Sorting: it was reachable (since step 84), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 96 by `s1a.carloan` (order 220 seq 1), left after step 50, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 97 by `s3.ev` (order 220 seq 2), left after step 17, 79 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 103 by `scope.business_before` (order 258 seq 1), left after step 77, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 109 by `f1040.line3a` (order 272 seq 3), left after step 2, 106 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 108), which its gate does not read.
- form sd re-entered at step 110 by `sd.distributions` (order 272 seq 4), left after step 88, 21 between. Late: reachable only after the answer to `div.any` (step 107), its parent or roster.
- form div re-entered at step 112 by `div.other_boxes` (order 272 seq 7), left after step 107, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 113 by `sd.f2439` (order 272 seq 18), left after step 110, 2 between. Sorting: it was reachable (since step 108), and `qbi.dividends` was asked instead (within order 272, the block's entry and seq order put it first).
- form sb re-entered at step 114 by `sb.nominee` (order 273 seq 1), left after step 108, 5 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 108), which its gate does not read.
- form sd re-entered at step 117 by `sd.sold_other` (order 274 seq 20), left after step 113, 3 between. Sorting: it was reachable (since step 1), and `sb.nominee` was asked instead (the bank puts order 273 seq 1 first).
- form s3 re-entered at step 124 by `s3.foreign_any` (order 279 seq 1), left after step 98, 25 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form sb re-entered at step 126 by `sb.account_any` (order 285 seq 1), left after step 115, 10 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 131 by `scope.foreign_shares` (order 285 seq 6), left after step 103, 27 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 132 by `s3.credit_bond` (order 290 seq 1), left after step 124, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 136 by `s2.credit_recapture` (order 291 seq 1), left after step 76, 59 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 140 by `scope.reforestation` (order 295 seq 1), left after step 131, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 142 by `qbi.prior_form` (order 296 seq 1), left after step 111, 30 between. Late: reachable only after the answer to `scope.attorney_fees` (step 141), which its gate does not read.
- form f1040 re-entered at step 144 by `f1040.withheld_other_any` (order 300 seq 1), left after step 109, 34 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 146 by `s3.line10` (order 305 seq 1), left after step 135, 10 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sd.distributions` (order 272 seq 4), step 110: child of `div.any` (step 107), 1 other question between. Sorting: it was reachable (since step 108), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 112: child of `div.any` (step 107), 2 other questions between. Sorting: it was reachable (since step 108), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sd.f2439` (order 272 seq 18), step 113: child of `div.any` (step 107), 2 other questions between. Sorting: it was reachable (since step 108), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).

**stage5.return.refund**: 127 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×3 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 80 by `sa.estate_tax_income` (order 200 seq 70), left after step 78, 1 between. Sorting: it was reachable (since step 75), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 87 by `s1a.carloan` (order 220 seq 1), left after step 41, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 88 by `s3.ev` (order 220 seq 2), left after step 17, 70 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 94 by `scope.business_before` (order 258 seq 1), left after step 68, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 79, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 89, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 285 seq 6), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 124 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 121 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 127 by `s3.line10` (order 305 seq 1), left after step 115, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.itemized**: 166 questions, complete; order re-entries 0, form re-entries 31 sorting and 12 late, delayed children 12 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×6 · 200:sd×1 · 200:sa×4 · 200:s3×1 · 200:s2×1 · 200:sa×5 · 200:gift×3 · 200:sa×8 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 272:sd×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×6 · 274:sd×5 · 276:sd×1 · 276:f4952×6 · 279:s3×1 · 280:ftc×5 · 284:sa×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×2 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 77 by `sa.mortgage_interest` (order 200 seq 20), left after step 75, 1 between. Sorting: it was reachable (since step 71), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s3 re-entered at step 81 by `s3.mcc` (order 200 seq 24), left after step 17, 63 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 77), which its gate does not read.
- form s2 re-entered at step 82 by `s2.mortgage_subsidy` (order 200 seq 25), left after step 67, 14 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 77), which its gate does not read.
- form sa re-entered at step 83 by `sa.line5b` (order 200 seq 26), left after step 80, 2 between. Sorting: it was reachable (since step 71), and `s3.mcc` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 91 by `sa.line1` (order 200 seq 50), left after step 87, 3 between. Sorting: it was reachable (since step 76), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 99 by `s1a.carloan` (order 220 seq 1), left after step 41, 57 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 100 by `s3.ev` (order 220 seq 2), left after step 81, 18 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 200 seq 25 first).
- form scope re-entered at step 106 by `scope.business_before` (order 258 seq 1), left after step 68, 37 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 112 by `f1040.line3a` (order 272 seq 3), left after step 2, 109 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 113 by `sd.distributions` (order 272 seq 4), left after step 76, 36 between. Late: reachable only after the answer to `div.any` (step 110), its parent or roster.
- form div re-entered at step 115 by `div.other_boxes` (order 272 seq 7), left after step 110, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 116 by `sd.f2439` (order 272 seq 18), left after step 113, 2 between. Sorting: it was reachable (since step 111), and `qbi.dividends` was asked instead (within order 272, the block's entry and seq order put it first).
- form sb re-entered at step 117 by `sb.nominee` (order 273 seq 1), left after step 111, 5 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 120 by `sd.route_each` (order 274 seq 2), left after step 116, 3 between. Late: reachable only after the answer to `$sales` (step 119), which its gate does not read.
- form sales re-entered at step 121 by `sales[s1].box` (order 274 seq 4), left after step 119, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 119), which its gate does not read.
- form sd re-entered at step 127 by `sd.sold_other` (order 274 seq 20), left after step 120, 6 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 139 by `s3.foreign_any` (order 279 seq 1), left after step 101, 37 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form sa re-entered at step 145 by `sa.foreign_tax_deduct` (order 284 seq 1), left after step 98, 46 between. Late: reachable only after the answer to `ftc.taxes` (step 140), which its gate does not read.
- form sb re-entered at step 146 by `sb.account_any` (order 285 seq 1), left after step 118, 27 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 151 by `scope.foreign_shares` (order 285 seq 6), left after step 106, 44 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 152 by `s3.credit_bond` (order 290 seq 1), left after step 139, 12 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 156 by `s2.credit_recapture` (order 291 seq 1), left after step 82, 73 between. Sorting: it was reachable (since step 1), and `sa.line5b` was asked instead (the bank puts order 200 seq 26 first).
- form scope re-entered at step 160 by `scope.reforestation` (order 295 seq 1), left after step 151, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 162 by `qbi.prior_form` (order 296 seq 1), left after step 114, 47 between. Late: reachable only after the answer to `scope.attorney_fees` (step 161), which its gate does not read.
- form f1040 re-entered at step 164 by `f1040.withheld_other_any` (order 300 seq 1), left after step 112, 51 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 166 by `s3.line10` (order 305 seq 1), left after step 155, 10 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sa.mortgage_interest` (order 200 seq 20), step 77: child of `sa.home_owner` (step 70), 6 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.mortgage_unreported` (order 200 seq 21), step 78: child of `sa.home_owner` (step 70), 6 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5b` (order 200 seq 26), step 83: child of `sa.home_owner` (step 70), 10 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.property_tax_other_any` (order 200 seq 27), step 84: child of `sa.home_owner` (step 70), 10 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5a` (order 200 seq 30), step 85: child of `sa.state_tax_any` (step 71), 13 other questions between. Sorting: it was reachable (since step 72), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.charity_limited` (order 200 seq 40), step 86: child of `sa.gifts` (step 74), 11 other questions between. Sorting: it was reachable (since step 75), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 87: child of `sa.gifts` (step 74), 11 other questions between. Sorting: it was reachable (since step 75), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line1` (order 200 seq 50), step 91: child of `sa.medical_any` (step 75), 15 other questions between. Sorting: it was reachable (since step 76), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- `sd.distributions` (order 272 seq 4), step 113: child of `div.any` (step 110), 1 other question between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 115: child of `div.any` (step 110), 2 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sd.f2439` (order 272 seq 18), step 116: child of `div.any` (step 110), 2 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sales[s1].route` (order 274 seq 11), step 124: child of `sd.route_each` (step 120), 3 other questions between. Sorting: it was reachable (since step 121), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).

**stage5.refuse.screens**: 19 questions, refused; order re-entries 0, form re-entries 4 sorting and 2 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).

**stage5.refuse.other_income**: 15 questions, refused; order re-entries 0, form re-entries 2 sorting and 2 late, delayed children 1 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×2

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- `scope.nonresident` (order 113 seq 10), step 15: child of `scope.noncitizen` (step 10), 4 other questions between. Sorting: it was reachable (since step 11), and `scope.under24` was asked instead (within order 113, the block's entry and seq order put it first).

**stage5.return.refund_f4952_screens_unused**: 127 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×3 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 80 by `sa.estate_tax_income` (order 200 seq 70), left after step 78, 1 between. Sorting: it was reachable (since step 75), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 87 by `s1a.carloan` (order 220 seq 1), left after step 41, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 88 by `s3.ev` (order 220 seq 2), left after step 17, 70 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 94 by `scope.business_before` (order 258 seq 1), left after step 68, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 79, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 89, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 285 seq 6), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 124 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 121 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 127 by `s3.line10` (order 305 seq 1), left after step 115, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.refund_f8960_unsupported_unused**: 127 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×3 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 80 by `sa.estate_tax_income` (order 200 seq 70), left after step 78, 1 between. Sorting: it was reachable (since step 75), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 87 by `s1a.carloan` (order 220 seq 1), left after step 41, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 88 by `s3.ev` (order 220 seq 2), left after step 17, 70 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 94 by `scope.business_before` (order 258 seq 1), left after step 68, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 79, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 89, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 285 seq 6), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 124 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 121 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 127 by `s3.line10` (order 305 seq 1), left after step 115, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.f8960_unsupported_agi_at_threshold**: 127 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×3 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 80 by `sa.estate_tax_income` (order 200 seq 70), left after step 78, 1 between. Sorting: it was reachable (since step 75), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 87 by `s1a.carloan` (order 220 seq 1), left after step 41, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 88 by `s3.ev` (order 220 seq 2), left after step 17, 70 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 94 by `scope.business_before` (order 258 seq 1), left after step 68, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 79, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 89, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 285 seq 6), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 124 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 121 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 127 by `s3.line10` (order 305 seq 1), left after step 115, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.refund_f8960_refund_unused**: 127 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×3 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 80 by `sa.estate_tax_income` (order 200 seq 70), left after step 78, 1 between. Sorting: it was reachable (since step 75), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 87 by `s1a.carloan` (order 220 seq 1), left after step 41, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 88 by `s3.ev` (order 220 seq 2), left after step 17, 70 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 94 by `scope.business_before` (order 258 seq 1), left after step 68, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 79, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 89, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 285 seq 6), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 124 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 121 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 127 by `s3.line10` (order 305 seq 1), left after step 115, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.refund_combat_pay_no_children**: 127 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×3 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 80 by `sa.estate_tax_income` (order 200 seq 70), left after step 78, 1 between. Sorting: it was reachable (since step 75), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 87 by `s1a.carloan` (order 220 seq 1), left after step 41, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 88 by `s3.ev` (order 220 seq 2), left after step 17, 70 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 94 by `scope.business_before` (order 258 seq 1), left after step 68, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 79, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 89, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 285 seq 6), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 124 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 121 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 127 by `s3.line10` (order 305 seq 1), left after step 115, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.itemized_f8960_allocation_unused**: 166 questions, complete; order re-entries 0, form re-entries 31 sorting and 12 late, delayed children 12 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×6 · 200:sd×1 · 200:sa×4 · 200:s3×1 · 200:s2×1 · 200:sa×5 · 200:gift×3 · 200:sa×8 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 272:sd×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×6 · 274:sd×5 · 276:sd×1 · 276:f4952×6 · 279:s3×1 · 280:ftc×5 · 284:sa×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×2 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 65 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 68 by `scope.education_recapture` (order 193 seq 4), left after step 66, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.home_owner` (order 200 seq 1), left after step 13, 56 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 77 by `sa.mortgage_interest` (order 200 seq 20), left after step 75, 1 between. Sorting: it was reachable (since step 71), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s3 re-entered at step 81 by `s3.mcc` (order 200 seq 24), left after step 17, 63 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 77), which its gate does not read.
- form s2 re-entered at step 82 by `s2.mortgage_subsidy` (order 200 seq 25), left after step 67, 14 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 77), which its gate does not read.
- form sa re-entered at step 83 by `sa.line5b` (order 200 seq 26), left after step 80, 2 between. Sorting: it was reachable (since step 71), and `s3.mcc` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 91 by `sa.line1` (order 200 seq 50), left after step 87, 3 between. Sorting: it was reachable (since step 76), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 99 by `s1a.carloan` (order 220 seq 1), left after step 41, 57 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 100 by `s3.ev` (order 220 seq 2), left after step 81, 18 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 200 seq 25 first).
- form scope re-entered at step 106 by `scope.business_before` (order 258 seq 1), left after step 68, 37 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 112 by `f1040.line3a` (order 272 seq 3), left after step 2, 109 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 113 by `sd.distributions` (order 272 seq 4), left after step 76, 36 between. Late: reachable only after the answer to `div.any` (step 110), its parent or roster.
- form div re-entered at step 115 by `div.other_boxes` (order 272 seq 7), left after step 110, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 116 by `sd.f2439` (order 272 seq 18), left after step 113, 2 between. Sorting: it was reachable (since step 111), and `qbi.dividends` was asked instead (within order 272, the block's entry and seq order put it first).
- form sb re-entered at step 117 by `sb.nominee` (order 273 seq 1), left after step 111, 5 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 120 by `sd.route_each` (order 274 seq 2), left after step 116, 3 between. Late: reachable only after the answer to `$sales` (step 119), which its gate does not read.
- form sales re-entered at step 121 by `sales[s1].box` (order 274 seq 4), left after step 119, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 119), which its gate does not read.
- form sd re-entered at step 127 by `sd.sold_other` (order 274 seq 20), left after step 120, 6 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 139 by `s3.foreign_any` (order 279 seq 1), left after step 101, 37 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form sa re-entered at step 145 by `sa.foreign_tax_deduct` (order 284 seq 1), left after step 98, 46 between. Late: reachable only after the answer to `ftc.taxes` (step 140), which its gate does not read.
- form sb re-entered at step 146 by `sb.account_any` (order 285 seq 1), left after step 118, 27 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 151 by `scope.foreign_shares` (order 285 seq 6), left after step 106, 44 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 152 by `s3.credit_bond` (order 290 seq 1), left after step 139, 12 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 156 by `s2.credit_recapture` (order 291 seq 1), left after step 82, 73 between. Sorting: it was reachable (since step 1), and `sa.line5b` was asked instead (the bank puts order 200 seq 26 first).
- form scope re-entered at step 160 by `scope.reforestation` (order 295 seq 1), left after step 151, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 162 by `qbi.prior_form` (order 296 seq 1), left after step 114, 47 between. Late: reachable only after the answer to `scope.attorney_fees` (step 161), which its gate does not read.
- form f1040 re-entered at step 164 by `f1040.withheld_other_any` (order 300 seq 1), left after step 112, 51 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 166 by `s3.line10` (order 305 seq 1), left after step 155, 10 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sa.mortgage_interest` (order 200 seq 20), step 77: child of `sa.home_owner` (step 70), 6 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.mortgage_unreported` (order 200 seq 21), step 78: child of `sa.home_owner` (step 70), 6 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5b` (order 200 seq 26), step 83: child of `sa.home_owner` (step 70), 10 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.property_tax_other_any` (order 200 seq 27), step 84: child of `sa.home_owner` (step 70), 10 other questions between. Sorting: it was reachable (since step 71), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5a` (order 200 seq 30), step 85: child of `sa.state_tax_any` (step 71), 13 other questions between. Sorting: it was reachable (since step 72), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.charity_limited` (order 200 seq 40), step 86: child of `sa.gifts` (step 74), 11 other questions between. Sorting: it was reachable (since step 75), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 87: child of `sa.gifts` (step 74), 11 other questions between. Sorting: it was reachable (since step 75), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line1` (order 200 seq 50), step 91: child of `sa.medical_any` (step 75), 15 other questions between. Sorting: it was reachable (since step 76), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- `sd.distributions` (order 272 seq 4), step 113: child of `div.any` (step 110), 1 other question between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 115: child of `div.any` (step 110), 2 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sd.f2439` (order 272 seq 18), step 116: child of `div.any` (step 110), 2 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sales[s1].route` (order 274 seq 11), step 124: child of `sd.route_each` (step 120), 3 other questions between. Sorting: it was reachable (since step 121), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).

### generated returns

**generated.0**: 228 questions, complete; order re-entries 2, form re-entries 29 sorting and 11 late, delayed children 20 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×13 · 192:person×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×7 · 200:sd×1 · 200:sa×4 · 200:s3×1 · 200:s2×1 · 200:sa×5 · 200:gift×5 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 140:w2×2 · 250:sc×4 · 251:sc×7 · 252:sc×34 · 255:scveh×11 · 257:asset×1 · 258:scope×1 · 260:person×1 · 261:person×1 · 265:scope×2 · 267:s2×1 · 270:interest×3 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×6 · 279:s3×1 · 280:ftc×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×3 · 300:f1040×2 · 305:s3×1

- order 140 re-entered at step 121 by `person[taxpayer].w2[emp_a].box3` (order 140 seq 7), left after step 29, 91 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- order 250 re-entered at step 123 by `person[taxpayer].sc[biz_a].line1` (order 250 seq 2), left after step 120, 2 between. Late: left for `person[taxpayer].w2[emp_a].box3` (order 140 seq 7), which sorts earlier and was reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form person re-entered at step 77 by `person[taxpayer].x_hsa_prior_excess` (order 192 seq 1), left after step 62, 14 between. Late: reachable only after the answer to `$f8889@person[taxpayer]` (step 64), which its gate does not read.
- form scope re-entered at step 78 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 21 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 80 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 35 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 81 by `scope.education_recapture` (order 193 seq 4), left after step 79, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 83 by `sa.home_owner` (order 200 seq 1), left after step 13, 69 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 91 by `sa.mortgage_interest` (order 200 seq 20), left after step 89, 1 between. Sorting: it was reachable (since step 84), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s3 re-entered at step 95 by `s3.mcc` (order 200 seq 24), left after step 17, 77 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 91), which its gate does not read.
- form s2 re-entered at step 96 by `s2.mortgage_subsidy` (order 200 seq 25), left after step 80, 15 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 91), which its gate does not read.
- form sa re-entered at step 97 by `sa.line5b` (order 200 seq 26), left after step 94, 2 between. Sorting: it was reachable (since step 84), and `s3.mcc` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 107 by `sa.estate_tax_income` (order 200 seq 70), left after step 101, 5 between. Sorting: it was reachable (since step 101), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 114 by `s1a.carloan` (order 220 seq 1), left after step 41, 72 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 115 by `s3.ev` (order 220 seq 2), left after step 95, 19 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 200 seq 25 first).
- form w2 re-entered at step 121 by `person[taxpayer].w2[emp_a].box3` (order 140 seq 7), left after step 29, 91 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form sc re-entered at step 123 by `person[taxpayer].sc[biz_a].line1` (order 250 seq 2), left after step 120, 2 between. Late: left for `person[taxpayer].w2[emp_a].box3` (order 140 seq 7), which sorts earlier and was reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form scope re-entered at step 180 by `scope.business_before` (order 258 seq 1), left after step 81, 98 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form person re-entered at step 181 by `person[taxpayer].plan` (order 260 seq 1), left after step 77, 103 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form scope re-entered at step 183 by `scope.se_plan_other` (order 265 seq 1), left after step 180, 2 between. Sorting: it was reachable (since step 121), and `person[taxpayer].plan` was asked instead (the bank puts order 260 seq 1 first).
- form s2 re-entered at step 185 by `s2.lookback` (order 267 seq 1), left after step 96, 88 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form sd re-entered at step 193 by `sd.sold_other` (order 274 seq 20), left after step 90, 102 between. Sorting: it was reachable (since step 1), and `sa.mortgage_interest` was asked instead (the bank puts order 200 seq 20 first).
- form s3 re-entered at step 205 by `s3.foreign_any` (order 279 seq 1), left after step 116, 88 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form sb re-entered at step 207 by `sb.account_any` (order 285 seq 1), left after step 191, 15 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 212 by `scope.foreign_shares` (order 285 seq 6), left after step 184, 27 between. Sorting: it was reachable (since step 1), and `s2.lookback` was asked instead (the bank puts order 267 seq 1 first).
- form s3 re-entered at step 213 by `s3.credit_bond` (order 290 seq 1), left after step 205, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 217 by `s2.credit_recapture` (order 291 seq 1), left after step 185, 31 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form scope re-entered at step 221 by `scope.reforestation` (order 295 seq 1), left after step 212, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 226 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 223 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 228 by `s3.line10` (order 305 seq 1), left after step 216, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sa.mortgage_interest` (order 200 seq 20), step 91: child of `sa.home_owner` (step 83), 7 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.mortgage_unreported` (order 200 seq 21), step 92: child of `sa.home_owner` (step 83), 7 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5b` (order 200 seq 26), step 97: child of `sa.home_owner` (step 83), 11 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.property_tax_other_any` (order 200 seq 27), step 98: child of `sa.home_owner` (step 83), 11 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5a` (order 200 seq 30), step 99: child of `sa.state_tax_any` (step 84), 14 other questions between. Sorting: it was reachable (since step 85), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.charity_limited` (order 200 seq 40), step 100: child of `sa.gifts` (step 87), 12 other questions between. Sorting: it was reachable (since step 88), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 101: child of `sa.gifts` (step 87), 12 other questions between. Sorting: it was reachable (since step 88), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line24a` (order 252 seq 21), step 154: child of `person[taxpayer].sc[biz_a].travel_meals` (step 149), 4 other questions between. Sorting: it was reachable (since step 150), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].meals_50` (order 252 seq 22), step 155: child of `person[taxpayer].sc[biz_a].travel_meals` (step 149), 4 other questions between. Sorting: it was reachable (since step 150), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].meals_80` (order 252 seq 23), step 156: child of `person[taxpayer].sc[biz_a].travel_meals` (step 149), 4 other questions between. Sorting: it was reachable (since step 150), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].meals_100` (order 252 seq 24), step 157: child of `person[taxpayer].sc[biz_a].travel_meals` (step 149), 4 other questions between. Sorting: it was reachable (since step 150), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line26` (order 252 seq 25), step 158: child of `person[taxpayer].sc[biz_a].employees` (step 150), 7 other questions between. Sorting: it was reachable (since step 151), and `person[taxpayer].sc[biz_a].goods` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line14` (order 252 seq 26), step 159: child of `person[taxpayer].sc[biz_a].employees` (step 150), 7 other questions between. Sorting: it was reachable (since step 151), and `person[taxpayer].sc[biz_a].goods` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line19` (order 252 seq 27), step 160: child of `person[taxpayer].sc[biz_a].employees` (step 150), 7 other questions between. Sorting: it was reachable (since step 151), and `person[taxpayer].sc[biz_a].goods` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line35` (order 252 seq 28), step 161: child of `person[taxpayer].sc[biz_a].goods` (step 151), 9 other questions between. Sorting: it was reachable (since step 152), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line36` (order 252 seq 29), step 162: child of `person[taxpayer].sc[biz_a].goods` (step 151), 9 other questions between. Sorting: it was reachable (since step 152), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line37` (order 252 seq 30), step 163: child of `person[taxpayer].sc[biz_a].goods` (step 151), 9 other questions between. Sorting: it was reachable (since step 152), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line38` (order 252 seq 31), step 164: child of `person[taxpayer].sc[biz_a].goods` (step 151), 9 other questions between. Sorting: it was reachable (since step 152), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line39` (order 252 seq 32), step 165: child of `person[taxpayer].sc[biz_a].goods` (step 151), 9 other questions between. Sorting: it was reachable (since step 152), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line41` (order 252 seq 33), step 166: child of `person[taxpayer].sc[biz_a].goods` (step 151), 9 other questions between. Sorting: it was reachable (since step 152), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).

**generated.1**: 59 questions, refused; order re-entries 0, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×43 · 102:household×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form household re-entered at step 59 by `household.home_cost` (order 102 seq 2), left after step 6, 52 between. Late: reachable only after the answer to `dependent[dep_c].tin` (step 58), which its gate does not read.

**generated.2**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1

**generated.3**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1

**generated.4**: 183 questions, complete; order re-entries 0, form re-entries 30 sorting and 12 late, delayed children 11 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×13 · 192:person×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×6 · 200:sd×1 · 200:sa×7 · 200:gift×3 · 200:sa×8 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 244:sli×3 · 241:person×1 · 250:sc×1 · 258:scope×1 · 270:interest×5 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 272:sd×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×13 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 280:ftc×5 · 284:sa×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×2 · 305:s3×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form person re-entered at step 77 by `person[taxpayer].x_hsa_prior_excess` (order 192 seq 1), left after step 62, 14 between. Late: reachable only after the answer to `$f8889@person[taxpayer]` (step 64), which its gate does not read.
- form scope re-entered at step 78 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 21 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 80 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 35 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 81 by `scope.education_recapture` (order 193 seq 4), left after step 79, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 83 by `sa.home_owner` (order 200 seq 1), left after step 13, 69 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 90 by `sa.mortgage_interest` (order 200 seq 20), left after step 88, 1 between. Sorting: it was reachable (since step 84), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 100 by `sa.line1` (order 200 seq 50), left after step 96, 3 between. Sorting: it was reachable (since step 89), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 108 by `s1a.carloan` (order 220 seq 1), left after step 41, 66 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 109 by `s3.ev` (order 220 seq 2), left after step 17, 91 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form person re-entered at step 117 by `person[taxpayer].sav_claimed` (order 241 seq 5), left after step 77, 39 between. Late: reachable only after the answer to `sli.assisted_any` (step 116), which its gate does not read.
- form scope re-entered at step 119 by `scope.business_before` (order 258 seq 1), left after step 81, 37 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 127 by `f1040.line3a` (order 272 seq 3), left after step 2, 124 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 126), which its gate does not read.
- form sd re-entered at step 128 by `sd.distributions` (order 272 seq 4), left after step 89, 38 between. Late: reachable only after the answer to `div.any` (step 125), its parent or roster.
- form div re-entered at step 130 by `div.other_boxes` (order 272 seq 7), left after step 125, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 131 by `sd.f2439` (order 272 seq 18), left after step 128, 2 between. Sorting: it was reachable (since step 126), and `qbi.dividends` was asked instead (within order 272, the block's entry and seq order put it first).
- form sb re-entered at step 132 by `sb.nominee` (order 273 seq 1), left after step 126, 5 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 126), which its gate does not read.
- form sd re-entered at step 135 by `sd.route_each` (order 274 seq 2), left after step 131, 3 between. Late: reachable only after the answer to `$sales` (step 134), which its gate does not read.
- form sales re-entered at step 136 by `sales[s1].box` (order 274 seq 4), left after step 134, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 134), which its gate does not read.
- form sd re-entered at step 149 by `sd.sold_other` (order 274 seq 20), left after step 135, 13 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 156 by `s3.foreign_any` (order 279 seq 1), left after step 110, 45 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form sa re-entered at step 162 by `sa.foreign_tax_deduct` (order 284 seq 1), left after step 107, 54 between. Late: reachable only after the answer to `ftc.taxes` (step 157), which its gate does not read.
- form sb re-entered at step 163 by `sb.account_any` (order 285 seq 1), left after step 133, 29 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 168 by `scope.foreign_shares` (order 285 seq 6), left after step 119, 48 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 169 by `s3.credit_bond` (order 290 seq 1), left after step 156, 12 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 173 by `s2.credit_recapture` (order 291 seq 1), left after step 80, 92 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 177 by `scope.reforestation` (order 295 seq 1), left after step 168, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 179 by `qbi.prior_form` (order 296 seq 1), left after step 129, 49 between. Late: reachable only after the answer to `scope.attorney_fees` (step 178), which its gate does not read.
- form f1040 re-entered at step 181 by `f1040.withheld_other_any` (order 300 seq 1), left after step 127, 53 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 183 by `s3.line10` (order 305 seq 1), left after step 172, 10 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sa.mortgage_interest` (order 200 seq 20), step 90: child of `sa.home_owner` (step 83), 6 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.mortgage_unreported` (order 200 seq 21), step 91: child of `sa.home_owner` (step 83), 6 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5b` (order 200 seq 26), step 92: child of `sa.home_owner` (step 83), 6 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.property_tax_other_any` (order 200 seq 27), step 93: child of `sa.home_owner` (step 83), 6 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5a` (order 200 seq 30), step 94: child of `sa.state_tax_any` (step 84), 9 other questions between. Sorting: it was reachable (since step 85), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.charity_limited` (order 200 seq 40), step 95: child of `sa.gifts` (step 87), 7 other questions between. Sorting: it was reachable (since step 88), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 96: child of `sa.gifts` (step 87), 7 other questions between. Sorting: it was reachable (since step 88), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line1` (order 200 seq 50), step 100: child of `sa.medical_any` (step 88), 11 other questions between. Sorting: it was reachable (since step 89), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- `sd.distributions` (order 272 seq 4), step 128: child of `div.any` (step 125), 1 other question between. Sorting: it was reachable (since step 126), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 130: child of `div.any` (step 125), 2 other questions between. Sorting: it was reachable (since step 126), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sd.f2439` (order 272 seq 18), step 131: child of `div.any` (step 125), 2 other questions between. Sorting: it was reachable (since step 126), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).

**generated.5**: 8 questions, refused; order re-entries 0, form re-entries 1 sorting and 0 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).

**generated.6**: 160 questions, complete; order re-entries 0, form re-entries 27 sorting and 9 late, delayed children 8 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×6 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×13 · 192:person×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×6 · 200:sd×1 · 200:sa×4 · 200:s3×1 · 200:s2×1 · 200:sa×5 · 200:gift×1 · 200:sa×8 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×6 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×2 · 305:s3×1 · 311:person×1 · 271:f1040×1 · 313:eic×3 · 158:s8812×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 126 seq 2), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 32 by `scope.w2_marks` (order 145 seq 3), left after step 21, 10 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 24), which its gate does not read.
- form s2 re-entered at step 39 by `s2.options_any` (order 146 seq 5), left after step 30, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 44 by `s2.household_help` (order 155 seq 3), left after step 39, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 45 by `s1.uc_any` (order 160 seq 1), left after step 31, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 56 by `scope.recovery` (order 161 seq 6), left after step 37, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 59 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 23, 35 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form person re-entered at step 77 by `person[taxpayer].x_hsa_prior_excess` (order 192 seq 1), left after step 62, 14 between. Late: reachable only after the answer to `$f8889@person[taxpayer]` (step 64), which its gate does not read.
- form scope re-entered at step 78 by `scope.disaster_distribution` (order 193 seq 1), left after step 56, 21 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 80 by `s2.hsa_testing` (order 193 seq 3), left after step 44, 35 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 81 by `scope.education_recapture` (order 193 seq 4), left after step 79, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 83 by `sa.home_owner` (order 200 seq 1), left after step 13, 69 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 90 by `sa.mortgage_interest` (order 200 seq 20), left after step 88, 1 between. Sorting: it was reachable (since step 84), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s3 re-entered at step 94 by `s3.mcc` (order 200 seq 24), left after step 17, 76 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 90), which its gate does not read.
- form s2 re-entered at step 95 by `s2.mortgage_subsidy` (order 200 seq 25), left after step 80, 14 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 90), which its gate does not read.
- form sa re-entered at step 96 by `sa.line5b` (order 200 seq 26), left after step 93, 2 between. Sorting: it was reachable (since step 84), and `s3.mcc` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 102 by `sa.line1` (order 200 seq 50), left after step 100, 1 between. Sorting: it was reachable (since step 89), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 110 by `s1a.carloan` (order 220 seq 1), left after step 41, 68 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 111 by `s3.ev` (order 220 seq 2), left after step 94, 16 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 200 seq 25 first).
- form scope re-entered at step 117 by `scope.business_before` (order 258 seq 1), left after step 81, 35 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 121 by `sd.sold_other` (order 274 seq 20), left after step 89, 31 between. Sorting: it was reachable (since step 1), and `sa.mortgage_interest` was asked instead (the bank puts order 200 seq 20 first).
- form s3 re-entered at step 133 by `s3.foreign_any` (order 279 seq 1), left after step 112, 20 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 139 by `scope.foreign_shares` (order 285 seq 6), left after step 117, 21 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 140 by `s3.credit_bond` (order 290 seq 1), left after step 133, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 144 by `s2.credit_recapture` (order 291 seq 1), left after step 95, 48 between. Sorting: it was reachable (since step 1), and `sa.line5b` was asked instead (the bank puts order 200 seq 26 first).
- form scope re-entered at step 148 by `scope.reforestation` (order 295 seq 1), left after step 139, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 152 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 149 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 154 by `s3.line10` (order 305 seq 1), left after step 143, 10 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 155 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 77, 77 between. Late: reachable only after the answer to `scope.attorney_fees` (step 149), which its gate does not read.
- form f1040 re-entered at step 156 by `f1040.tax_exempt_interest` (order 271 seq 1), left after step 153, 2 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 155), which its gate does not read.
- `sa.mortgage_interest` (order 200 seq 20), step 90: child of `sa.home_owner` (step 83), 6 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.mortgage_unreported` (order 200 seq 21), step 91: child of `sa.home_owner` (step 83), 6 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5b` (order 200 seq 26), step 96: child of `sa.home_owner` (step 83), 10 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.property_tax_other_any` (order 200 seq 27), step 97: child of `sa.home_owner` (step 83), 10 other questions between. Sorting: it was reachable (since step 84), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5a` (order 200 seq 30), step 98: child of `sa.state_tax_any` (step 84), 13 other questions between. Sorting: it was reachable (since step 85), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.charity_limited` (order 200 seq 40), step 99: child of `sa.gifts` (step 87), 11 other questions between. Sorting: it was reachable (since step 88), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 100: child of `sa.gifts` (step 87), 11 other questions between. Sorting: it was reachable (since step 88), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line1` (order 200 seq 50), step 102: child of `sa.medical_any` (step 88), 13 other questions between. Sorting: it was reachable (since step 89), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).

**generated.7**: 18 questions, refused; order re-entries 0, form re-entries 3 sorting and 3 late, delayed children 0 sorting and 0 late.

100:person×1 · 101:household×1 · 110:person×2 · 111:sa×1 · 112:person×2 · 113:scope×2 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3

- form person re-entered at step 3 by `person[spouse].birth_year` (order 110 seq 1), left after step 1, 1 between. Late: left for `household.married_dec31` (order 101 seq 2), which sorts earlier and was reachable only after the answer to `$person` (step 1), which its gate does not read.
- form person re-entered at step 6 by `person[spouse].blind` (order 112 seq 1), left after step 4, 1 between. Late: reachable only after the answer to `sa.dependent` (step 5), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 113 seq 4), left after step 5, 4 between. Late: left for `person[spouse].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 5), which its gate does not read.
- form scope re-entered at step 11 by `scope.chapter11` (order 113 seq 5), left after step 9, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 14 by `s3.adoption_any` (order 126 seq 1), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 15 by `scope.f8814` (order 126 seq 2), left after step 11, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).

**generated.8**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1

**generated.9**: 31 questions, refused; order re-entries 0, form re-entries 4 sorting and 2 late, delayed children 1 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×2 · 118:s3×1 · 120:dependent×12 · 126:s3×1 · 126:scope×1 · 130:scope×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 29 by `s3.adoption_any` (order 126 seq 1), left after step 16, 12 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 30 by `scope.f8814` (order 126 seq 2), left after step 15, 14 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- `scope.unearned_2700` (order 113 seq 11), step 15: child of `scope.under24` (step 11), 3 other questions between. Sorting: it was reachable (since step 12), and `scope.armed_forces` was asked instead (within order 113, the block's entry and seq order put it first).

**generated.10**: 290 questions, complete; order re-entries 2, form re-entries 31 sorting and 17 late, delayed children 21 sorting and 1 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×14 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×15 · 145:s2×1 · 145:s1×1 · 145:scope×3 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×13 · 192:person×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×6 · 200:sd×1 · 200:sa×4 · 200:s3×1 · 200:s2×1 · 200:sa×5 · 200:gift×5 · 200:sa×8 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×5 · 251:sc×7 · 252:sc×36 · 255:scveh×6 · 257:asset×22 · 258:scope×1 · 252:sc×1 · 259:ltc×3 · 260:person×1 · 261:person×1 · 265:scope×2 · 267:s2×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:sd×1 · 272:div×1 · 272:sd×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×17 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 280:ftc×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×3 · 300:f1040×2 · 305:s3×1 · 311:person×1 · 271:f1040×1 · 272:div×1

- order 252 re-entered at step 219 by `person[taxpayer].sc[biz_a].at_risk` (order 252 seq 38), left after step 189, 29 between. Late: reachable only after the answer to `scope.business_before` (step 218), which its gate does not read.
- order 272 re-entered at step 290 by `div.box12` (order 272 seq 6), left after step 235, 54 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 288), which its gate does not read.
- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 30 by `s3.adoption_any` (order 126 seq 1), left after step 15, 14 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 31 by `scope.f8814` (order 126 seq 2), left after step 14, 16 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 35 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 25 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 54 by `scope.w2_marks` (order 145 seq 3), left after step 34, 19 between. Late: reachable only after the answer to `$w2@person[taxpayer]` (step 37), which its gate does not read.
- form s2 re-entered at step 61 by `s2.options_any` (order 146 seq 5), left after step 52, 8 between. Sorting: it was reachable (since step 1), and `s1.nqdc_pension` was asked instead (the bank puts order 145 seq 2 first).
- form s2 re-entered at step 66 by `s2.household_help` (order 155 seq 3), left after step 61, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form s1 re-entered at step 67 by `s1.uc_any` (order 160 seq 1), left after step 53, 13 between. Sorting: it was reachable (since step 1), and `scope.w2_marks` was asked instead (the bank puts order 145 seq 3 first).
- form scope re-entered at step 78 by `scope.recovery` (order 161 seq 6), left after step 59, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 81 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 36, 44 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form person re-entered at step 99 by `person[taxpayer].x_hsa_prior_excess` (order 192 seq 1), left after step 84, 14 between. Late: reachable only after the answer to `$f8889@person[taxpayer]` (step 86), which its gate does not read.
- form scope re-entered at step 100 by `scope.disaster_distribution` (order 193 seq 1), left after step 78, 21 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 102 by `s2.hsa_testing` (order 193 seq 3), left after step 66, 35 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 103 by `scope.education_recapture` (order 193 seq 4), left after step 101, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 105 by `sa.home_owner` (order 200 seq 1), left after step 13, 91 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 112 by `sa.mortgage_interest` (order 200 seq 20), left after step 110, 1 between. Sorting: it was reachable (since step 106), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s3 re-entered at step 116 by `s3.mcc` (order 200 seq 24), left after step 30, 85 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 112), which its gate does not read.
- form s2 re-entered at step 117 by `s2.mortgage_subsidy` (order 200 seq 25), left after step 102, 14 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 112), which its gate does not read.
- form sa re-entered at step 118 by `sa.line5b` (order 200 seq 26), left after step 115, 2 between. Sorting: it was reachable (since step 106), and `s3.mcc` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 128 by `sa.line1` (order 200 seq 50), left after step 122, 5 between. Sorting: it was reachable (since step 111), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 136 by `s1a.carloan` (order 220 seq 1), left after step 63, 72 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 137 by `s3.ev` (order 220 seq 2), left after step 116, 20 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 200 seq 25 first).
- form scope re-entered at step 218 by `scope.business_before` (order 258 seq 1), left after step 103, 114 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sc re-entered at step 219 by `person[taxpayer].sc[biz_a].at_risk` (order 252 seq 38), left after step 189, 29 between. Late: reachable only after the answer to `scope.business_before` (step 218), which its gate does not read.
- form person re-entered at step 223 by `person[taxpayer].plan` (order 260 seq 1), left after step 99, 123 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 142), which its gate does not read.
- form scope re-entered at step 225 by `scope.se_plan_other` (order 265 seq 1), left after step 218, 6 between. Late: left for `person[taxpayer].sc[biz_a].at_risk` (order 252 seq 38), which sorts earlier and was reachable only after the answer to `scope.business_before` (step 218), which its gate does not read.
- form s2 re-entered at step 227 by `s2.lookback` (order 267 seq 1), left after step 117, 109 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 142), which its gate does not read.
- form sd re-entered at step 233 by `sd.distributions` (order 272 seq 4), left after step 111, 121 between. Late: reachable only after the answer to `div.any` (step 231), its parent or roster.
- form div re-entered at step 234 by `div.other_boxes` (order 272 seq 7), left after step 231, 2 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 235 by `sd.f2439` (order 272 seq 18), left after step 233, 1 between. Sorting: it was reachable (since step 232), and `div.other_boxes` was asked instead (within order 272, the block's entry and seq order put it first).
- form sb re-entered at step 236 by `sb.nominee` (order 273 seq 1), left after step 232, 3 between. Sorting: it was reachable (since step 230), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form sd re-entered at step 239 by `sd.route_each` (order 274 seq 2), left after step 235, 3 between. Late: reachable only after the answer to `$sales` (step 238), which its gate does not read.
- form sales re-entered at step 240 by `sales[s1].box` (order 274 seq 4), left after step 238, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 238), which its gate does not read.
- form sd re-entered at step 257 by `sd.sold_other` (order 274 seq 20), left after step 239, 17 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 264 by `s3.foreign_any` (order 279 seq 1), left after step 138, 125 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form sb re-entered at step 266 by `sb.account_any` (order 285 seq 1), left after step 237, 28 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 271 by `scope.foreign_shares` (order 285 seq 6), left after step 226, 44 between. Sorting: it was reachable (since step 1), and `s2.lookback` was asked instead (the bank puts order 267 seq 1 first).
- form s3 re-entered at step 272 by `s3.credit_bond` (order 290 seq 1), left after step 264, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 276 by `s2.credit_recapture` (order 291 seq 1), left after step 227, 48 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form scope re-entered at step 280 by `scope.reforestation` (order 295 seq 1), left after step 271, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 285 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 282 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 287 by `s3.line10` (order 305 seq 1), left after step 275, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 288 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 224, 63 between. Late: reachable only after the answer to `scope.attorney_fees` (step 281), which its gate does not read.
- form f1040 re-entered at step 289 by `f1040.tax_exempt_interest` (order 271 seq 1), left after step 286, 2 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 288), which its gate does not read.
- form div re-entered at step 290 by `div.box12` (order 272 seq 6), left after step 234, 55 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 288), which its gate does not read.
- `sa.mortgage_interest` (order 200 seq 20), step 112: child of `sa.home_owner` (step 105), 6 other questions between. Sorting: it was reachable (since step 106), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.mortgage_unreported` (order 200 seq 21), step 113: child of `sa.home_owner` (step 105), 6 other questions between. Sorting: it was reachable (since step 106), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5b` (order 200 seq 26), step 118: child of `sa.home_owner` (step 105), 10 other questions between. Sorting: it was reachable (since step 106), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.property_tax_other_any` (order 200 seq 27), step 119: child of `sa.home_owner` (step 105), 10 other questions between. Sorting: it was reachable (since step 106), and `sa.state_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line5a` (order 200 seq 30), step 120: child of `sa.state_tax_any` (step 106), 13 other questions between. Sorting: it was reachable (since step 107), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.charity_limited` (order 200 seq 40), step 121: child of `sa.gifts` (step 109), 11 other questions between. Sorting: it was reachable (since step 110), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 122: child of `sa.gifts` (step 109), 11 other questions between. Sorting: it was reachable (since step 110), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line1` (order 200 seq 50), step 128: child of `sa.medical_any` (step 110), 17 other questions between. Sorting: it was reachable (since step 111), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line24a` (order 252 seq 21), step 174: child of `person[taxpayer].sc[biz_a].travel_meals` (step 169), 4 other questions between. Sorting: it was reachable (since step 170), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].meals_50` (order 252 seq 22), step 175: child of `person[taxpayer].sc[biz_a].travel_meals` (step 169), 4 other questions between. Sorting: it was reachable (since step 170), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].meals_80` (order 252 seq 23), step 176: child of `person[taxpayer].sc[biz_a].travel_meals` (step 169), 4 other questions between. Sorting: it was reachable (since step 170), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].meals_100` (order 252 seq 24), step 177: child of `person[taxpayer].sc[biz_a].travel_meals` (step 169), 4 other questions between. Sorting: it was reachable (since step 170), and `person[taxpayer].sc[biz_a].employees` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line26` (order 252 seq 25), step 178: child of `person[taxpayer].sc[biz_a].employees` (step 170), 7 other questions between. Sorting: it was reachable (since step 171), and `person[taxpayer].sc[biz_a].goods` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line14` (order 252 seq 26), step 179: child of `person[taxpayer].sc[biz_a].employees` (step 170), 7 other questions between. Sorting: it was reachable (since step 171), and `person[taxpayer].sc[biz_a].goods` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line19` (order 252 seq 27), step 180: child of `person[taxpayer].sc[biz_a].employees` (step 170), 7 other questions between. Sorting: it was reachable (since step 171), and `person[taxpayer].sc[biz_a].goods` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line35` (order 252 seq 28), step 181: child of `person[taxpayer].sc[biz_a].goods` (step 171), 9 other questions between. Sorting: it was reachable (since step 172), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line36` (order 252 seq 29), step 182: child of `person[taxpayer].sc[biz_a].goods` (step 171), 9 other questions between. Sorting: it was reachable (since step 172), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line37` (order 252 seq 30), step 183: child of `person[taxpayer].sc[biz_a].goods` (step 171), 9 other questions between. Sorting: it was reachable (since step 172), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line38` (order 252 seq 31), step 184: child of `person[taxpayer].sc[biz_a].goods` (step 171), 9 other questions between. Sorting: it was reachable (since step 172), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line39` (order 252 seq 32), step 185: child of `person[taxpayer].sc[biz_a].goods` (step 171), 9 other questions between. Sorting: it was reachable (since step 172), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `person[taxpayer].sc[biz_a].line41` (order 252 seq 33), step 186: child of `person[taxpayer].sc[biz_a].goods` (step 171), 9 other questions between. Sorting: it was reachable (since step 172), and `person[taxpayer].sc[biz_a].ho_uses` was asked instead (within order 252, the block's entry and seq order put it first).
- `div.box12` (order 272 seq 6), step 290: child of `div.any` (step 231), 53 other questions between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 288), which its gate does not read.

**generated.11**: 29 questions, refused; order re-entries 0, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×3 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×13 · 102:household×1

- form person re-entered at step 7 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 5 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 112 seq 1), left after step 7, 1 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 13 by `sa.excluded_income` (order 113 seq 4), left after step 8, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form scope re-entered at step 14 by `scope.chapter11` (order 113 seq 5), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form household re-entered at step 29 by `household.home_cost` (order 102 seq 2), left after step 6, 22 between. Late: reachable only after the answer to `dependent[dep_a].parent_home_paid` (step 28), which its gate does not read.

### minimal returns

**every gate closed**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

100:person×1 · 100:f1040×1 · 101:household×1 · 103:household×1 · 110:person×1 · 111:sa×1 · 112:person×1 · 113:scope×3 · 113:sa×1 · 113:scope×1 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 126:scope×1 · 130:scope×3 · 140:person×2 · 140:w2×1 · 146:scope×3 · 146:f8959×1 · 146:s2×1 · 150:s1a×2 · 155:f2441×2 · 155:s2×1 · 160:s1×6 · 161:s1×5 · 161:scope×1 · 165:refund×1 · 170:retirement×1 · 180:person×4 · 185:ssb×1 · 190:f8889×1 · 193:scope×2 · 193:s2×1 · 193:scope×1 · 195:f1095a×1 · 200:sa×9 · 200:sd×1 · 200:sa×7 · 220:s1a×1 · 220:s3×2 · 220:f5695×1 · 220:f8863×1 · 220:sli×1 · 250:sc×1 · 258:scope×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 276:f4952×1 · 279:s3×1 · 285:sb×5 · 285:scope×1 · 290:s3×4 · 291:s2×3 · 294:oi8z×1 · 295:scope×2 · 296:qbi×2 · 300:f1040×2 · 305:s3×1 · 311:person×1

- form person re-entered at step 5 by `person[taxpayer].birth_year` (order 110 seq 1), left after step 1, 3 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 100 seq 2 first).
- form person re-entered at step 7 by `person[taxpayer].blind` (order 112 seq 1), left after step 5, 1 between. Late: reachable only after the answer to `sa.dependent` (step 6), which its gate does not read.
- form sa re-entered at step 11 by `sa.excluded_income` (order 113 seq 4), left after step 6, 4 between. Late: left for `person[taxpayer].blind` (order 112 seq 1), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 6), which its gate does not read.
- form scope re-entered at step 12 by `scope.chapter11` (order 113 seq 5), left after step 10, 1 between. Sorting: it was reachable (since step 1), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- form s3 re-entered at step 15 by `s3.adoption_any` (order 126 seq 1), left after step 13, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 16 by `scope.f8814` (order 126 seq 2), left after step 12, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 20 by `person[taxpayer].rrta` (order 140 seq 1), left after step 7, 12 between. Sorting: it was reachable (since step 2), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form scope re-entered at step 23 by `scope.pay_no_w2` (order 146 seq 1), left after step 19, 3 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 32 by `s2.household_help` (order 155 seq 3), left after step 27, 4 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 44 by `scope.recovery` (order 161 seq 6), left after step 25, 18 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 146 seq 4 first).
- form person re-entered at step 47 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 21, 25 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 4 first).
- form scope re-entered at step 53 by `scope.disaster_distribution` (order 193 seq 1), left after step 44, 8 between. Sorting: it was reachable (since step 1), and `refund.any` was asked instead (the bank puts order 165 seq 1 first).
- form s2 re-entered at step 55 by `s2.hsa_testing` (order 193 seq 3), left after step 32, 22 between. Sorting: it was reachable (since step 1), and `s1.uc_any` was asked instead (the bank puts order 160 seq 1 first).
- form scope re-entered at step 56 by `scope.education_recapture` (order 193 seq 4), left after step 54, 1 between. Sorting: it was reachable (since step 1), and `s2.hsa_testing` was asked instead (within order 193, the block's entry and seq order put it first).
- form sa re-entered at step 58 by `sa.home_owner` (order 200 seq 1), left after step 11, 46 between. Sorting: it was reachable (since step 1), and `scope.chapter11` was asked instead (the bank puts order 113 seq 5 first).
- form sa re-entered at step 68 by `sa.estate_tax_income` (order 200 seq 70), left after step 66, 1 between. Sorting: it was reachable (since step 63), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form s1a re-entered at step 75 by `s1a.carloan` (order 220 seq 1), left after step 29, 45 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 76 by `s3.ev` (order 220 seq 2), left after step 15, 60 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 126 seq 2 first).
- form scope re-entered at step 82 by `scope.business_before` (order 258 seq 1), left after step 56, 25 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 86 by `sd.sold_other` (order 274 seq 20), left after step 67, 18 between. Sorting: it was reachable (since step 1), and `sa.estate_tax_income` was asked instead (the bank puts order 200 seq 70 first).
- form s3 re-entered at step 93 by `s3.foreign_any` (order 279 seq 1), left after step 77, 15 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form scope re-entered at step 99 by `scope.foreign_shares` (order 285 seq 6), left after step 82, 16 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 100 by `s3.credit_bond` (order 290 seq 1), left after step 93, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 104 by `s2.credit_recapture` (order 291 seq 1), left after step 55, 48 between. Sorting: it was reachable (since step 1), and `scope.education_recapture` was asked instead (the bank puts order 193 seq 4 first).
- form scope re-entered at step 108 by `scope.reforestation` (order 295 seq 1), left after step 99, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 112 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 109 between. Late: left for `household.ever_married` (order 101 seq 1), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 114 by `s3.line10` (order 305 seq 1), left after step 103, 10 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 115 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 50, 64 between. Late: reachable only after the answer to `scope.attorney_fees` (step 109), which its gate does not read.

**asset.industry = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**asset.listed = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**asset.software = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**dependent.ever_married = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**dependent.lived_all_year = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**div.any = true alone**: 120 questions, complete; order re-entries 0, form re-entries 27 sorting and 5 late, delayed children 0 sorting and 0 late.

- form sd re-entered at step 86 by `sd.distributions` (order 272 seq 4), left after step 67, 18 between. Late: reachable only after the answer to `div.any` (step 84), its parent or roster.
- form div re-entered at step 87 by `div.other_boxes` (order 272 seq 7), left after step 84, 2 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 88 by `sd.f2439` (order 272 seq 18), left after step 86, 1 between. Sorting: it was reachable (since step 85), and `div.other_boxes` was asked instead (within order 272, the block's entry and seq order put it first).
- form sd re-entered at step 90 by `sd.sold_other` (order 274 seq 20), left after step 88, 1 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (within order 274, the block's entry and seq order put it first).
- form sb re-entered at step 99 by `sb.account_any` (order 285 seq 1), left after step 85, 13 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 105 by `s3.credit_bond` (order 290 seq 1), left after step 97, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).

**eic.lived_with_relative = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**f1040.estimated_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**f1040.withheld_other_any = true alone**: 117 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 2 sorting and 0 late.

- `f1040.line25b` (order 300 seq 3), step 114: child of `f1040.withheld_other_any` (step 112), 1 other question between. Sorting: it was reachable (since step 113), and `f1040.estimated_any` was asked instead (within order 300, the block's entry and seq order put it first).
- `f1040.line25c_other` (order 300 seq 4), step 115: child of `f1040.withheld_other_any` (step 112), 1 other question between. Sorting: it was reachable (since step 113), and `f1040.estimated_any` was asked instead (within order 300, the block's entry and seq order put it first).

**f4952.has_interest = true alone**: 118 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**f5695.any = true alone**: 132 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 16 sorting and 0 late.

- form f5695 re-entered at step 81 by `f5695.solar` (order 230 seq 2), left after step 78, 2 between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.solar` (order 230 seq 2), step 81: child of `f5695.any` (step 78), 2 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.solar_water` (order 230 seq 3), step 82: child of `f5695.any` (step 78), 2 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.wind` (order 230 seq 4), step 83: child of `f5695.any` (step 78), 2 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.geothermal` (order 230 seq 5), step 84: child of `f5695.any` (step 78), 2 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.line5a` (order 230 seq 6), step 85: child of `f5695.any` (step 78), 2 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.insulation` (order 230 seq 8), step 87: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.doors` (order 230 seq 9), step 88: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.windows` (order 230 seq 10), step 89: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.panel` (order 230 seq 11), step 90: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.audit` (order 230 seq 12), step 91: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.heat_pump` (order 230 seq 13), step 92: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.hp_water_heater` (order 230 seq 14), step 93: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.central_ac` (order 230 seq 15), step 94: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.water_heater` (order 230 seq 16), step 95: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.furnace` (order 230 seq 17), step 96: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).
- `f5695.biomass` (order 230 seq 18), step 97: child of `f5695.any` (step 78), 3 other questions between. Sorting: it was reachable (since step 79), and `f8863.paid` was asked instead (the bank puts order 220 seq 5 first).

**f8889.coverage_year = "family" alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**f8889.coverage_year = "changed" alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**f8962.other_coverage = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**person.eligible_educator = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**person.ira_owner = true alone**: 117 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 1 late.

- `person[taxpayer].sav_trad` (order 180 seq 10), step 51: child of `person[taxpayer].ira_owner` (step 47), 3 other questions between. Sorting: it was reachable (since step 48), and `person[taxpayer].inherited_account` was asked instead (within order 180, the block's entry and seq order put it first).
- `person[taxpayer].x_ira_prior_excess` (order 180 seq 17), step 52: child of `person[taxpayer].ira_owner` (step 47), 3 other questions between. Late: reachable only after the answer to `person[taxpayer].x_archer_excess` (step 50), which its gate does not read.

**person.x_edu_account = true alone**: 117 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**qbi.prior_form = true alone**: 117 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**retirement.rollover_any = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**s1.alaska_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- `s1.alaska_dividend` (order 160 seq 20), step 39: child of `s1.alaska_any` (step 37), 1 other question between. Sorting: it was reachable (since step 38), and `s1.hobby_any` was asked instead (within order 160, the block's entry and seq order put it first).

**s1.alimony_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 1 sorting and 0 late.

- form s1 re-entered at step 45 by `s1.alimony` (order 161 seq 10), left after step 43, 1 between. Sorting: it was reachable (since step 40), and `scope.recovery` was asked instead (within order 161, the block's entry and seq order put it first).
- form scope re-entered at step 54 by `scope.disaster_distribution` (order 193 seq 1), left after step 44, 9 between. Sorting: it was reachable (since step 1), and `s1.alimony` was asked instead (the bank puts order 161 seq 10 first).
- `s1.alimony` (order 161 seq 10), step 45: child of `s1.alimony_any` (step 39), 5 other questions between. Sorting: it was reachable (since step 40), and `s1.cod_any` was asked instead (within order 161, the block's entry and seq order put it first).

**s1.hobby_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**s1.jury_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- `s1.jury_pay` (order 160 seq 18), step 39: child of `s1.jury_any` (step 36), 2 other questions between. Sorting: it was reachable (since step 37), and `s1.alaska_any` was asked instead (within order 160, the block's entry and seq order put it first).

**s1.scholarship_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- `s1.scholarship_taxable` (order 160 seq 17), step 39: child of `s1.scholarship_any` (step 35), 3 other questions between. Sorting: it was reachable (since step 36), and `s1.jury_any` was asked instead (within order 160, the block's entry and seq order put it first).

**s1.uc_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- `s1.uc_paid` (order 160 seq 10), step 39: child of `s1.uc_any` (step 33), 5 other questions between. Sorting: it was reachable (since step 34), and `s1.winnings_any` was asked instead (within order 160, the block's entry and seq order put it first).

**s1.winnings_any = true alone**: 118 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 3 sorting and 0 late.

- `s1.gambling_winnings` (order 160 seq 13), step 39: child of `s1.winnings_any` (step 34), 4 other questions between. Sorting: it was reachable (since step 35), and `s1.scholarship_any` was asked instead (within order 160, the block's entry and seq order put it first).
- `s1.prizes` (order 160 seq 15), step 40: child of `s1.winnings_any` (step 34), 4 other questions between. Sorting: it was reachable (since step 35), and `s1.scholarship_any` was asked instead (within order 160, the block's entry and seq order put it first).
- `s1.olympic` (order 160 seq 16), step 41: child of `s1.winnings_any` (step 34), 4 other questions between. Sorting: it was reachable (since step 35), and `s1.scholarship_any` was asked instead (within order 160, the block's entry and seq order put it first).

**s2.household_help = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**s2.options_any = true alone**: 117 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 0 sorting and 0 late.

- form s2 re-entered at step 34 by `s2.household_help` (order 155 seq 3), left after step 28, 5 between. Sorting: it was reachable (since step 1), and `s1.stock_options` was asked instead (the bank puts order 146 seq 13 first).
- form s1 re-entered at step 35 by `s1.uc_any` (order 160 seq 1), left after step 29, 5 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).

**s3.adoption_any = true alone**: 118 questions, complete; order re-entries 0, form re-entries 26 sorting and 4 late, delayed children 3 sorting and 0 late.

- form s3 re-entered at step 17 by `s3.adoption` (order 126 seq 3), left after step 15, 1 between. Sorting: it was reachable (since step 16), and `scope.f8814` was asked instead (within order 126, the block's entry and seq order put it first).
- form scope re-entered at step 19 by `scope.adoption_benefits` (order 126 seq 6), left after step 16, 2 between. Sorting: it was reachable (since step 16), and `s3.adoption` was asked instead (within order 126, the block's entry and seq order put it first).
- form s3 re-entered at step 79 by `s3.ev` (order 220 seq 2), left after step 18, 60 between. Sorting: it was reachable (since step 1), and `scope.adoption_benefits` was asked instead (the bank puts order 126 seq 6 first).
- `s3.adoption` (order 126 seq 3), step 17: child of `s3.adoption_any` (step 15), 1 other question between. Sorting: it was reachable (since step 16), and `scope.f8814` was asked instead (within order 126, the block's entry and seq order put it first).
- `s3.adoption_earlier` (order 126 seq 4), step 18: child of `s3.adoption_any` (step 15), 1 other question between. Sorting: it was reachable (since step 16), and `scope.f8814` was asked instead (within order 126, the block's entry and seq order put it first).
- `scope.adoption_benefits` (order 126 seq 6), step 19: child of `s3.adoption_any` (step 15), 1 other question between. Sorting: it was reachable (since step 16), and `scope.f8814` was asked instead (within order 126, the block's entry and seq order put it first).

**s3.ev = true alone**: 118 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 3 sorting and 0 late.

- form s3 re-entered at step 81 by `s3.ev_dealer` (order 225 seq 2), left after step 77, 3 between. Sorting: it was reachable (since step 77), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form s3 re-entered at step 96 by `s3.foreign_any` (order 279 seq 1), left after step 83, 12 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- `s3.ev_dealer` (order 225 seq 2), step 81: child of `s3.ev` (step 76), 4 other questions between. Sorting: it was reachable (since step 77), and `s3.kerosene` was asked instead (the bank puts order 220 seq 3 first).
- `s3.ev_bought` (order 225 seq 3), step 82: child of `s3.ev` (step 76), 4 other questions between. Sorting: it was reachable (since step 77), and `s3.kerosene` was asked instead (the bank puts order 220 seq 3 first).
- `s3.ev_equipment` (order 225 seq 5), step 83: child of `s3.ev` (step 76), 4 other questions between. Sorting: it was reachable (since step 77), and `s3.kerosene` was asked instead (the bank puts order 220 seq 3 first).

**s3.farmland = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- `s3.farmland_deferral` (order 290 seq 4), step 103: child of `s3.farmland` (step 101), 1 other question between. Sorting: it was reachable (since step 102), and `s3.repaid_income` was asked instead (within order 290, the block's entry and seq order put it first).

**s3.foreign_any = true alone**: 120 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

- form s3 re-entered at step 105 by `s3.credit_bond` (order 290 seq 1), left after step 96, 8 between. Sorting: it was reachable (since step 1), and `ftc.carryover` was asked instead (the bank puts order 279 seq 5 first).

**s3.kerosene = true alone**: 116 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 1 sorting and 0 late.

- form s3 re-entered at step 81 by `s3.kerosene_credit` (order 225 seq 7), left after step 77, 3 between. Sorting: it was reachable (since step 78), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).
- form s3 re-entered at step 94 by `s3.foreign_any` (order 279 seq 1), left after step 81, 12 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- `s3.kerosene_credit` (order 225 seq 7), step 81: child of `s3.kerosene` (step 77), 3 other questions between. Sorting: it was reachable (since step 78), and `f5695.any` was asked instead (the bank puts order 220 seq 4 first).

**s3.prior_other_forms = true alone**: 119 questions, complete; order re-entries 2, form re-entries 25 sorting and 5 late, delayed children 0 sorting and 0 late.

- order 279 re-entered at step 104 by `ftc.carryover` (order 279 seq 5), left after step 93, 10 between. Late: reachable only after the answer to `s3.prior_other_forms` (step 103), its parent or roster.
- order 290 re-entered at step 105 by `s3.prior_amt` (order 290 seq 6), left after step 103, 1 between. Sorting: left for `ftc.carryover` (order 279 seq 5), a child of the question before it, which the bank places in another order number.
- form s3 re-entered at step 105 by `s3.prior_amt` (order 290 seq 6), left after step 103, 1 between. Sorting: left for `ftc.carryover` (order 279 seq 5), a child of the question before it, which the bank places in another form.
- form f5695 re-entered at step 107 by `f5695.carry` (order 290 seq 8), left after step 78, 28 between. Late: reachable only after the answer to `s3.prior_other_forms` (step 103), its parent or roster.
- form s3 re-entered at step 118 by `s3.line10` (order 305 seq 1), left after step 106, 11 between. Sorting: it was reachable (since step 1), and `f5695.carry` was asked instead (the bank puts order 290 seq 8 first).

**sa.gifts = true alone**: 117 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 2 sorting and 0 late.

- form sa re-entered at step 67 by `sa.charity_limited` (order 200 seq 40), left after step 65, 1 between. Sorting: it was reachable (since step 63), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form sa re-entered at step 70 by `sa.estate_tax_income` (order 200 seq 70), left after step 68, 1 between. Sorting: it was reachable (since step 68), and `$gift` was asked instead (within order 200, the block's entry and seq order put it first).
- form sd re-entered at step 88 by `sd.sold_other` (order 274 seq 20), left after step 66, 21 between. Sorting: it was reachable (since step 1), and `sa.charity_limited` was asked instead (the bank puts order 200 seq 40 first).
- `sa.charity_limited` (order 200 seq 40), step 67: child of `sa.gifts` (step 62), 4 other questions between. Sorting: it was reachable (since step 63), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).
- `sa.line11` (order 200 seq 41), step 68: child of `sa.gifts` (step 62), 4 other questions between. Sorting: it was reachable (since step 63), and `sa.medical_any` was asked instead (within order 200, the block's entry and seq order put it first).

**sa.personal_property_tax_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- form sa re-entered at step 68 by `sa.line5c` (order 200 seq 32), left after step 66, 1 between. Sorting: it was reachable (since step 62), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form sd re-entered at step 87 by `sd.sold_other` (order 274 seq 20), left after step 67, 19 between. Sorting: it was reachable (since step 1), and `sa.line5c` was asked instead (the bank puts order 200 seq 32 first).
- `sa.line5c` (order 200 seq 32), step 68: child of `sa.personal_property_tax_any` (step 61), 6 other questions between. Sorting: it was reachable (since step 62), and `sa.gifts` was asked instead (within order 200, the block's entry and seq order put it first).

**sa.state_tax_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- form sa re-entered at step 68 by `sa.line5a` (order 200 seq 30), left after step 66, 1 between. Sorting: it was reachable (since step 60), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form sd re-entered at step 87 by `sd.sold_other` (order 274 seq 20), left after step 67, 19 between. Sorting: it was reachable (since step 1), and `sa.line5a` was asked instead (the bank puts order 200 seq 30 first).
- `sa.line5a` (order 200 seq 30), step 68: child of `sa.state_tax_any` (step 59), 8 other questions between. Sorting: it was reachable (since step 60), and `sa.state_tax_other_any` was asked instead (within order 200, the block's entry and seq order put it first).

**sa.state_tax_other_any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- form sa re-entered at step 68 by `sa.state_tax_other` (order 200 seq 31), left after step 66, 1 between. Sorting: it was reachable (since step 61), and `sd.casualty` was asked instead (within order 200, the block's entry and seq order put it first).
- form sd re-entered at step 87 by `sd.sold_other` (order 274 seq 20), left after step 67, 19 between. Sorting: it was reachable (since step 1), and `sa.state_tax_other` was asked instead (the bank puts order 200 seq 31 first).
- `sa.state_tax_other` (order 200 seq 31), step 68: child of `sa.state_tax_other_any` (step 60), 7 other questions between. Sorting: it was reachable (since step 61), and `sa.personal_property_tax_any` was asked instead (within order 200, the block's entry and seq order put it first).

**sc.employees = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**sc.goods = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**sc.travel_meals = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**scope.armed_forces = true alone**: 118 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 3 sorting and 0 late.

- `scope.reservist_expenses` (order 113 seq 13), step 13: child of `scope.armed_forces` (step 10), 2 other questions between. Sorting: it was reachable (since step 11), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- `scope.military_move` (order 113 seq 14), step 14: child of `scope.armed_forces` (step 10), 2 other questions between. Sorting: it was reachable (since step 11), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).
- `scope.reservist_repaid` (order 113 seq 15), step 15: child of `scope.armed_forces` (step 10), 2 other questions between. Sorting: it was reachable (since step 11), and `sa.excluded_income` was asked instead (within order 113, the block's entry and seq order put it first).

**scope.business_before = true alone**: 119 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

- form scope re-entered at step 103 by `scope.foreign_shares` (order 285 seq 6), left after step 85, 17 between. Sorting: it was reachable (since step 1), and `s179.prior_form` was asked instead (the bank puts order 258 seq 5 first).

**scope.foreign_shares = true alone**: 117 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**scope.noncitizen = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 1 sorting and 0 late.

- `scope.nonresident` (order 113 seq 10), step 13: child of `scope.noncitizen` (step 8), 4 other questions between. Sorting: it was reachable (since step 9), and `scope.under24` was asked instead (within order 113, the block's entry and seq order put it first).

**scope.religious_work = true alone**: 117 questions, complete; order re-entries 0, form re-entries 25 sorting and 4 late, delayed children 2 sorting and 0 late.

- form scope re-entered at step 28 by `scope.clergy` (order 146 seq 10), left after step 25, 2 between. Sorting: it was reachable (since step 26), and `f8959.territory_w2` was asked instead (within order 146, the block's entry and seq order put it first).
- form s2 re-entered at step 34 by `s2.household_help` (order 155 seq 3), left after step 27, 6 between. Sorting: it was reachable (since step 1), and `scope.clergy` was asked instead (the bank puts order 146 seq 10 first).
- form scope re-entered at step 46 by `scope.recovery` (order 161 seq 6), left after step 29, 16 between. Sorting: it was reachable (since step 1), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- `scope.clergy` (order 146 seq 10), step 28: child of `scope.religious_work` (step 25), 2 other questions between. Sorting: it was reachable (since step 26), and `f8959.territory_w2` was asked instead (within order 146, the block's entry and seq order put it first).
- `scope.church_exempt_wages` (order 146 seq 11), step 29: child of `scope.religious_work` (step 25), 2 other questions between. Sorting: it was reachable (since step 26), and `f8959.territory_w2` was asked instead (within order 146, the block's entry and seq order put it first).

**scveh.others_use = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**scveh.smr_always = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**sd.route_each = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**sd.sold_other = true alone**: 118 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 3 sorting and 0 late.

- `sd.business_property` (order 274 seq 26), step 91: child of `sd.sold_other` (step 86), 4 other questions between. Sorting: it was reachable (since step 87), and `sd.sec1256` was asked instead (within order 274, the block's entry and seq order put it first).
- `sd.installment` (order 274 seq 27), step 92: child of `sd.sold_other` (step 86), 4 other questions between. Sorting: it was reachable (since step 87), and `sd.sec1256` was asked instead (within order 274, the block's entry and seq order put it first).
- `sd.like_kind` (order 274 seq 28), step 93: child of `sd.sold_other` (step 86), 4 other questions between. Sorting: it was reachable (since step 87), and `sd.sec1256` was asked instead (within order 274, the block's entry and seq order put it first).

**sli.any = true alone**: 118 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**ssb.any = true alone**: 116 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**ssb.prior_year_pay = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

**tipjob.listed = true alone**: 115 questions, complete; order re-entries 0, form re-entries 24 sorting and 4 late, delayed children 0 sorting and 0 late.

