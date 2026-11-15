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
| whole-return fixtures | 11 | 116.4 | 0.0 | 4.5 | 22.8 | 5.8 | 1.0 | 0.4 |
| generated returns | 12 | 85.4 | 0.0 | 3.1 | 10.6 | 4.8 | 0.4 | 0.8 |
| minimal returns | 56 | 119.6 | 0.0 | 5.1 | 25.1 | 6.1 | 0.3 | 0.1 |

The counts are means per walk.

## What the late questions waited on

Every late finding, by the question that became reachable part-way and the answer it waited on, with the number of walks showing it
and what it caused (an order number re-entered, a form re-entered, a child delayed).

| question | waited on | its parent or roster? | caused | walks |
|---|---|---|---|---|
| `person.blind` | `sa.dependent` | no | form, order | 75 |
| `s1.inmate_wages` | `s1.nqdc_pension` | no | order | 69 |
| `sa.state_tax_any` | `sa.elect_itemize` | no | order | 69 |
| `s1.nqdc_pension` | `s1.ltc_payout` | no | order | 67 |
| `household.ever_married` | `f1040.status` | no | form | 64 |
| `s2.hsa_testing` | `sa.home_other` | no | form | 63 |
| `person.eic_ssn` | `scope.business_before` | no | form | 57 |
| `sa.line5b` | `sa.elect_itemize` | no | child, order | 6 |
| `sa.property_tax_other_any` | `sa.elect_itemize` | no | child | 6 |
| `sd.distributions` | `div.any` | yes | form | 6 |
| `s2.mortgage_subsidy` | `sa.mortgage_interest` | no | form | 5 |
| `s3.mcc` | `sa.mortgage_interest` | no | form | 5 |
| `f1040.line3a` | `sb.ordinary_dividends` | no | form | 4 |
| `sd.route_each` | `$sales` | no | form | 4 |
| `f1040.tax_exempt_interest` | `person.eic_ssn` | no | form | 3 |
| `qbi.prior_form` | `scope.business_before` | no | form | 3 |
| `sa.foreign_tax_deduct` | `ftc.taxes` | no | form | 3 |
| `div.box12` | `person.eic_ssn` | no | child, form, order | 2 |
| `person.plan` | `$sc` | no | form | 2 |
| `sc.at_risk` | `s179.prior_form` | no | form, order | 2 |
| `scope.se_plan_other` | `$sc` | no | form | 2 |
| `w2.box3` | `$sc` | no | form, order | 2 |
| `f5695.carry` | `s3.prior_other_forms` | yes | form | 1 |
| `household.home_cost` | `dependent.tin` | no | form | 1 |
| `household.home_cost` | `dependent.parent_home_paid` | no | form | 1 |
| `household.married_dec31` | `$person` | no | form | 1 |
| `person.eic_ssn` | `scope.passive` | no | form | 1 |
| `person.x_ira_prior_excess` | `person.x_archer_excess` | no | child, order | 1 |
| `qbi.prior_form` | `person.sav_claimed` | no | form | 1 |
| `qbi.prior_form` | `scope.passive` | no | form, order | 1 |
| `s1.nqdc_pension` | `s1.olympic` | no | order | 1 |
| `s1.nqdc_pension` | `s1.stock_options` | no | order | 1 |
| `s1.olympic` | `s1.ltc_payout` | no | child, order | 1 |
| `s1.stock_options` | `s1.ltc_payout` | no | child, order | 1 |
| `s2.hsa_testing` | `sa.mortgage_interest` | no | form, order | 1 |

## Delayed children for the sorting cause

By child and parent, with the number of walks.

| child | place | parent | place | walks |
|---|---|---|---|---|
| `sd.f2439` | order 274 seq 28 | `div.any` | order 272 seq 1 | 6 |
| `div.other_boxes` | order 272 seq 7 | `div.any` | order 272 seq 1 | 4 |
| `sd.distributions` | order 272 seq 4 | `div.any` | order 272 seq 1 | 4 |
| `sales.route` | order 274 seq 11 | `sd.route_each` | order 274 seq 2 | 2 |
| `f5695.audit` | order 230 seq 12 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.biomass` | order 230 seq 18 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.central_ac` | order 230 seq 15 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.doors` | order 230 seq 9 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.furnace` | order 230 seq 17 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.heat_pump` | order 230 seq 13 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.hp_water_heater` | order 230 seq 14 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.insulation` | order 230 seq 8 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.panel` | order 230 seq 11 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.water_heater` | order 230 seq 16 | `f5695.any` | order 230 seq 1 | 1 |
| `f5695.windows` | order 230 seq 10 | `f5695.any` | order 230 seq 1 | 1 |
| `sa.mortgage_unreported` | order 200 seq 4 | `sa.home_owner` | order 200 seq 1 | 1 |
| `scope.adoption_benefits` | order 127 seq 2 | `s3.adoption_any` | order 126 seq 1 | 1 |
| `scope.f8978` | order 295 seq 6 | `scope.business_before` | order 295 seq 3 | 1 |

## What the bank states

Read from the built question bank alone. A question that states no `seq` is asked after those of its order number that do, by id.

| order | questions | state a seq | forms |
|---|---|---|---|
| 0 | 2 | 0 | f1040, person |
| 2 | 6 | 0 | household, person |
| 10 | 2 | 0 | ftc, person |
| 102 | 3 | 3 | household |
| 103 | 3 | 3 | household |
| 110 | 1 | 1 | person |
| 111 | 2 | 2 | sa |
| 113 | 10 | 10 | scope |
| 118 | 1 | 1 | s3 |
| 120 | 36 | 36 | dependent |
| 126 | 4 | 4 | s3 |
| 127 | 2 | 2 | scope |
| 130 | 3 | 3 | scope |
| 140 | 9 | 9 | person, w2 |
| 144 | 2 | 2 | person |
| 145 | 5 | 5 | scope |
| 146 | 3 | 3 | scope |
| 148 | 3 | 3 | f8959, s1, s2 |
| 149 | 3 | 3 | s1, s2 |
| 150 | 1 | 1 | s1a |
| 151 | 6 | 6 | tipjob |
| 152 | 1 | 1 | s1a |
| 153 | 5 | 5 | otjob |
| 155 | 10 | 10 | f2441, w2 |
| 156 | 6 | 6 | f2441 |
| 157 | 9 | 9 | dcprov, dependent |
| 158 | 1 | 1 | scope |
| 159 | 2 | 2 | s2 |
| 160 | 22 | 22 | s1 |
| 161 | 7 | 7 | s1 |
| 165 | 18 | 18 | refund |
| 168 | 1 | 1 | scope |
| 170 | 50 | 50 | retirement |
| 175 | 1 | 1 | scope |
| 177 | 4 | 4 | person |
| 178 | 7 | 7 | ssb |
| 179 | 1 | 1 | ssb |
| 180 | 12 | 12 | person |
| 181 | 5 | 5 | ira |
| 187 | 1 | 1 | scope |
| 190 | 32 | 32 | f8889, person |
| 191 | 1 | 1 | scope |
| 192 | 2 | 2 | person |
| 193 | 1 | 1 | s2 |
| 195 | 1 | 1 | f1095a |
| 196 | 18 | 18 | f8962 |
| 197 | 45 | 45 | f1095a |
| 198 | 2 | 2 | f8962 |
| 199 | 4 | 4 | dependent, f8962 |
| 200 | 9 | 9 | sa |
| 201 | 7 | 7 | sa |
| 202 | 8 | 8 | gift, sa |
| 203 | 3 | 3 | sa |
| 204 | 9 | 9 | sa |
| 215 | 2 | 2 | s2, s3 |
| 216 | 1 | 1 | sd |
| 220 | 1 | 1 | s1a |
| 221 | 12 | 12 | carloan |
| 225 | 7 | 7 | s3 |
| 230 | 69 | 69 | f5695 |
| 239 | 2 | 2 | f5695 |
| 240 | 1 | 1 | f8863 |
| 241 | 27 | 27 | dependent, person |
| 242 | 1 | 1 | f8863 |
| 243 | 3 | 3 | person |
| 244 | 6 | 6 | sli |
| 247 | 3 | 3 | person |
| 248 | 1 | 1 | scope |
| 250 | 5 | 5 | sc |
| 251 | 7 | 7 | sc |
| 252 | 24 | 24 | sc |
| 253 | 8 | 8 | sc |
| 254 | 5 | 5 | sc |
| 255 | 45 | 45 | scveh |
| 257 | 32 | 32 | asset |
| 258 | 3 | 3 | s179 |
| 259 | 6 | 6 | ltc, sc |
| 260 | 8 | 8 | person |
| 261 | 1 | 1 | person |
| 262 | 5 | 5 | qbi |
| 263 | 1 | 1 | ira |
| 265 | 2 | 2 | scope |
| 267 | 1 | 1 | s2 |
| 270 | 3 | 3 | interest |
| 271 | 1 | 1 | f1040 |
| 272 | 17 | 17 | div, f1040, qbi, sb, sd |
| 273 | 3 | 3 | sb |
| 274 | 20 | 20 | sales, sd |
| 276 | 9 | 9 | clcw, clcw26, f8960, sd |
| 277 | 7 | 7 | f4952 |
| 278 | 3 | 3 | f8960 |
| 279 | 4 | 4 | s3 |
| 280 | 5 | 5 | ftc |
| 284 | 1 | 1 | sa |
| 285 | 10 | 10 | sb |
| 287 | 3 | 3 | scope |
| 290 | 7 | 7 | s3 |
| 291 | 1 | 1 | s2 |
| 292 | 1 | 1 | s2 |
| 293 | 1 | 1 | s2 |
| 294 | 3 | 3 | oi8z |
| 295 | 6 | 6 | scope |
| 300 | 5 | 5 | f1040 |
| 301 | 2 | 2 | f1040 |
| 305 | 1 | 1 | s3 |
| 310 | 3 | 3 | household, s8812 |
| 311 | 4 | 4 | person |
| 313 | 6 | 6 | eic |
| 314 | 2 | 2 | dependent |
| 315 | 7 | 7 | person |
| 316 | 13 | 13 | w2 |
| 317 | 3 | 3 | retirement |
| 318 | 1 | 1 | s3 |

Gated questions the bank does not place directly after their parent: 65.

| child | parent | why |
|---|---|---|
| `ftc.carryover` | `s3.prior_other_forms` | the parent is in order 290 and the child in order 10 |
| `person.died_at_64` | `person.born_jan1` | the parent is in order 2 and the child in order 10 |
| `household.considered_unmarried` | `household.married_dec31` | the parent is in order 2 and the child in order 102 |
| `household.cp_married` | `household.ever_married` | the parent is in order 2 and the child in order 103 |
| `dependent.joint_return` | `dependent.ever_married` | 4 questions that the parent does not open stand between them (the first: `dependent.own_money`) |
| `scope.adoption_benefits` | `s3.adoption_any` | the parent is in order 126 and the child in order 127 |
| `s1.prizes` | `s1.winnings_any` | 1 question that the parent does not open stand between them (the first: `s1.gambling_pro`) |
| `s1.olympic` | `s1.winnings_any` | 1 question that the parent does not open stand between them (the first: `s1.gambling_pro`) |
| `person.sav_roth` | `person.ira_owner` | 1 question that the parent does not open stand between them (the first: `person.ira_trad`) |
| `person.x_ira_prior_excess` | `person.ira_owner` | 5 questions that the parent does not open stand between them (the first: `person.ira_trad`) |
| `sa.line5b` | `sa.home_other` | 2 questions that the parent does not open stand between them (the first: `sa.mortgage_over_limit`) |
| `sa.property_tax_other_any` | `sa.home_other` | 2 questions that the parent does not open stand between them (the first: `sa.mortgage_over_limit`) |
| `sa.charity_limited` | `sa.gifts` | 1 question that the parent does not open stand between them (the first: `sa.gift_carryover`) |
| `sa.line11` | `sa.gifts` | 1 question that the parent does not open stand between them (the first: `sa.gift_carryover`) |
| `f5695.insulation` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.doors` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.windows` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.panel` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.audit` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.heat_pump` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.hp_water_heater` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.central_ac` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.water_heater` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.furnace` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
| `f5695.biomass` | `f5695.any` | 1 question that the parent does not open stand between them (the first: `f5695.line7a`) |
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
| `f5695.carry` | `s3.prior_other_forms` | the parent is in order 290 and the child in order 239 |
| `f5695.line12` | `s3.prior_other_forms` | the parent is in order 290 and the child in order 239 |
| `sd.distributions` | `div.any` | 1 question that the parent does not open stand between them (the first: `f1040.line3a`) |
| `div.box12` | `div.any` | 2 questions that the parent does not open stand between them (the first: `f1040.line3a`) |
| `div.other_boxes` | `div.any` | 2 questions that the parent does not open stand between them (the first: `f1040.line3a`) |
| `sales.route` | `sd.route_each` | 7 questions that the parent does not open stand between them (the first: `sales.box`) |
| `sd.f2439` | `div.any` | the parent is in order 272 and the child in order 274 |
| `f4952.line4g` | `f4952.has_interest` | 1 question that the parent does not open stand between them (the first: `f4952.prior_7`) |
| `ftc.taxes` | `s3.foreign_any` | the parent is in order 279 and the child in order 280 |
| `household.credit_disallowed` | `eic.qc_of_another` | the parent is in order 313 and the child in order 310 |
| `s3.elderly_credit` | `s3.disability_retired` | the parent is in order 118 and the child in order 318 |

## Each walk

A walk's line of runs reads `order:form×questions`. For a minimal return with one gate opened, only the findings the
every-gate-closed return does not also have are listed.

### whole-return fixtures

**stage5.return.owed**: 147 questions, complete; order re-entries 5, form re-entries 29 sorting and 8 late, delayed children 3 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×15 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×6 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 280:ftc×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×2 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 61 by `s1.nqdc_pension` (order 148 seq 2), left after step 45, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 60), which its gate does not read.
- order 161 re-entered at step 62 by `s1.inmate_wages` (order 161 seq 6), left after step 60, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 61), which its gate does not read.
- order 201 re-entered at step 79 by `sa.state_tax_any` (order 201 seq 1), left after step 77, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 78), which its gate does not read.
- order 204 re-entered at step 86 by `sa.estate_tax_income` (order 204 seq 2), left after step 78, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 78), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 38 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 15 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 39 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 17 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 46 by `s2.options_any` (order 149 seq 1), left after step 44, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 51 by `s2.household_help` (order 159 seq 1), left after step 46, 4 between. Sorting: it was reachable (since step 45), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 65 by `scope.recovery` (order 168 seq 1), left after step 43, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 67 by `scope.disaster_distribution` (order 175 seq 1), left after step 65, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 69 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 38, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 70 by `scope.excess_deferral` (order 187 seq 1), left after step 67, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 72 by `scope.archer_msa` (order 191 seq 1), left after step 70, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 74 by `sa.home_owner` (order 200 seq 1), left after step 10, 63 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 76 by `s2.hsa_testing` (order 193 seq 1), left after step 51, 24 between. Late: reachable only after the answer to `sa.home_other` (step 75), which its gate does not read.
- form sa re-entered at step 77 by `sa.sales_tax_wish` (order 201 seq 7), left after step 75, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 75), which its gate does not read.
- form s1a re-entered at step 92 by `s1a.carloan` (order 220 seq 1), left after step 48, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 93 by `s3.ev` (order 225 seq 1), left after step 17, 75 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 98 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 69, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 101 by `scope.education_recapture` (order 248 seq 1), left after step 72, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 109 by `f1040.line3a` (order 272 seq 3), left after step 2, 106 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 108), which its gate does not read.
- form sd re-entered at step 110 by `sd.distributions` (order 272 seq 4), left after step 91, 18 between. Late: reachable only after the answer to `div.any` (step 107), its parent or roster.
- form div re-entered at step 112 by `div.other_boxes` (order 272 seq 7), left after step 107, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sb re-entered at step 113 by `sb.nominee` (order 273 seq 1), left after step 108, 4 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 108), which its gate does not read.
- form sd re-entered at step 116 by `sd.sold_other` (order 274 seq 20), left after step 110, 5 between. Sorting: it was reachable (since step 1), and `qbi.dividends` was asked instead (the bank puts order 272 seq 5 first).
- form s3 re-entered at step 124 by `s3.foreign_any` (order 279 seq 1), left after step 94, 29 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form sb re-entered at step 126 by `sb.account_any` (order 285 seq 1), left after step 114, 11 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 131 by `scope.foreign_shares` (order 287 seq 1), left after step 101, 29 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 132 by `s3.credit_bond` (order 290 seq 1), left after step 124, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 136 by `s2.credit_recapture` (order 291 seq 1), left after step 76, 59 between. Sorting: it was reachable (since step 77), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 140 by `scope.reforestation` (order 295 seq 1), left after step 131, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 143 by `qbi.prior_form` (order 262 seq 1), left after step 111, 31 between. Late: reachable only after the answer to `scope.business_before` (step 142), which its gate does not read.
- form f1040 re-entered at step 145 by `f1040.withheld_other_any` (order 300 seq 1), left after step 109, 35 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 147 by `s3.line10` (order 305 seq 1), left after step 135, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sd.distributions` (order 272 seq 4), step 110: child of `div.any` (step 107), 1 other question between. Sorting: it was reachable (since step 108), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 112: child of `div.any` (step 107), 2 other questions between. Sorting: it was reachable (since step 108), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sd.f2439` (order 274 seq 28), step 121: child of `div.any` (step 107), 10 other questions between. Sorting: it was reachable (since step 108), and `f1040.line3a` was asked instead (the bank puts order 272 seq 3 first).

**stage5.return.refund**: 128 questions, complete; order re-entries 5, form re-entries 26 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×3 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 201 re-entered at step 70 by `sa.state_tax_any` (order 201 seq 1), left after step 68, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- order 204 re-entered at step 77 by `sa.estate_tax_income` (order 204 seq 2), left after step 69, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 24 between. Late: reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form sa re-entered at step 68 by `sa.sales_tax_wish` (order 201 seq 7), left after step 66, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form s1a re-entered at step 83 by `s1a.carloan` (order 220 seq 1), left after step 39, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 84 by `s3.ev` (order 225 seq 1), left after step 17, 66 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 89 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 92 by `scope.education_recapture` (order 248 seq 1), left after step 63, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 82, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 85, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 287 seq 1), left after step 92, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 68), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 125 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 122 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 128 by `s3.line10` (order 305 seq 1), left after step 115, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.itemized**: 167 questions, complete; order re-entries 6, form re-entries 30 sorting and 11 late, delayed children 4 sorting and 2 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×5 · 201:sa×1 · 204:sa×1 · 200:sa×2 · 201:sa×4 · 202:sa×3 · 202:gift×3 · 203:sa×2 · 204:sa×5 · 215:s3×1 · 215:s2×1 · 193:s2×1 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×6 · 274:sd×6 · 276:sd×1 · 277:f4952×6 · 279:s3×1 · 280:ftc×5 · 284:sa×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×2 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 200 re-entered at step 72 by `sa.line5b` (order 200 seq 7), left after step 69, 2 between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- order 201 re-entered at step 74 by `sa.state_tax_any` (order 201 seq 1), left after step 70, 3 between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- order 204 re-entered at step 86 by `sa.estate_tax_income` (order 204 seq 2), left after step 71, 14 between. Late: left for `sa.line5b` (order 200 seq 7), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form sa re-entered at step 84 by `sa.medical_any` (order 203 seq 1), left after step 80, 3 between. Sorting: it was reachable (since step 72), and `$gift` was asked instead (the bank puts order 202 seq 5 first).
- form s3 re-entered at step 91 by `s3.mcc` (order 215 seq 1), left after step 17, 73 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 66), which its gate does not read.
- form s2 re-entered at step 92 by `s2.mortgage_subsidy` (order 215 seq 2), left after step 42, 49 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 66), which its gate does not read.
- form s1a re-entered at step 95 by `s1a.carloan` (order 220 seq 1), left after step 39, 55 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 96 by `s3.ev` (order 225 seq 1), left after step 91, 4 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 215 seq 2 first).
- form person re-entered at step 101 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 40 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 104 by `scope.education_recapture` (order 248 seq 1), left after step 63, 40 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 112 by `f1040.line3a` (order 272 seq 3), left after step 2, 109 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 113 by `sd.distributions` (order 272 seq 4), left after step 94, 18 between. Late: reachable only after the answer to `div.any` (step 110), its parent or roster.
- form div re-entered at step 115 by `div.other_boxes` (order 272 seq 7), left after step 110, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sb re-entered at step 116 by `sb.nominee` (order 273 seq 1), left after step 111, 4 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 119 by `sd.route_each` (order 274 seq 2), left after step 113, 5 between. Late: reachable only after the answer to `$sales` (step 118), which its gate does not read.
- form sales re-entered at step 120 by `sales[s1].box` (order 274 seq 4), left after step 118, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 118), which its gate does not read.
- form sd re-entered at step 126 by `sd.sold_other` (order 274 seq 20), left after step 119, 6 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 139 by `s3.foreign_any` (order 279 seq 1), left after step 97, 41 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form sa re-entered at step 145 by `sa.foreign_tax_deduct` (order 284 seq 1), left after step 90, 54 between. Late: reachable only after the answer to `ftc.taxes` (step 140), which its gate does not read.
- form sb re-entered at step 146 by `sb.account_any` (order 285 seq 1), left after step 117, 28 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 151 by `scope.foreign_shares` (order 287 seq 1), left after step 104, 46 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 152 by `s3.credit_bond` (order 290 seq 1), left after step 139, 12 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 156 by `s2.credit_recapture` (order 291 seq 1), left after step 93, 62 between. Sorting: it was reachable (since step 94), and `sd.casualty` was asked instead (the bank puts order 216 seq 1 first).
- form scope re-entered at step 160 by `scope.reforestation` (order 295 seq 1), left after step 151, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 163 by `qbi.prior_form` (order 262 seq 1), left after step 114, 48 between. Late: reachable only after the answer to `scope.business_before` (step 162), which its gate does not read.
- form f1040 re-entered at step 165 by `f1040.withheld_other_any` (order 300 seq 1), left after step 112, 52 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 167 by `s3.line10` (order 305 seq 1), left after step 155, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sa.line5b` (order 200 seq 7), step 72: child of `sa.home_owner` (step 65), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- `sa.property_tax_other_any` (order 200 seq 8), step 73: child of `sa.home_owner` (step 65), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- `sd.distributions` (order 272 seq 4), step 113: child of `div.any` (step 110), 1 other question between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 115: child of `div.any` (step 110), 2 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sales[s1].route` (order 274 seq 11), step 123: child of `sd.route_each` (step 119), 3 other questions between. Sorting: it was reachable (since step 120), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- `sd.f2439` (order 274 seq 28), step 131: child of `div.any` (step 110), 17 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (the bank puts order 272 seq 3 first).

**stage5.refuse.screens**: 19 questions, refused; order re-entries 1, form re-entries 4 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).

**stage5.refuse.other_income**: 12 questions, refused; order re-entries 1, form re-entries 2 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×2

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.

**stage5.return.refund_f4952_screens_unused**: 128 questions, complete; order re-entries 5, form re-entries 26 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×3 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 201 re-entered at step 70 by `sa.state_tax_any` (order 201 seq 1), left after step 68, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- order 204 re-entered at step 77 by `sa.estate_tax_income` (order 204 seq 2), left after step 69, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 24 between. Late: reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form sa re-entered at step 68 by `sa.sales_tax_wish` (order 201 seq 7), left after step 66, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form s1a re-entered at step 83 by `s1a.carloan` (order 220 seq 1), left after step 39, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 84 by `s3.ev` (order 225 seq 1), left after step 17, 66 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 89 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 92 by `scope.education_recapture` (order 248 seq 1), left after step 63, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 82, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 85, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 287 seq 1), left after step 92, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 68), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 125 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 122 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 128 by `s3.line10` (order 305 seq 1), left after step 115, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.refund_f8960_unsupported_unused**: 128 questions, complete; order re-entries 5, form re-entries 26 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×3 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 201 re-entered at step 70 by `sa.state_tax_any` (order 201 seq 1), left after step 68, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- order 204 re-entered at step 77 by `sa.estate_tax_income` (order 204 seq 2), left after step 69, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 24 between. Late: reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form sa re-entered at step 68 by `sa.sales_tax_wish` (order 201 seq 7), left after step 66, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form s1a re-entered at step 83 by `s1a.carloan` (order 220 seq 1), left after step 39, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 84 by `s3.ev` (order 225 seq 1), left after step 17, 66 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 89 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 92 by `scope.education_recapture` (order 248 seq 1), left after step 63, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 82, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 85, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 287 seq 1), left after step 92, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 68), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 125 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 122 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 128 by `s3.line10` (order 305 seq 1), left after step 115, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.f8960_unsupported_agi_at_threshold**: 128 questions, complete; order re-entries 5, form re-entries 26 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×3 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 201 re-entered at step 70 by `sa.state_tax_any` (order 201 seq 1), left after step 68, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- order 204 re-entered at step 77 by `sa.estate_tax_income` (order 204 seq 2), left after step 69, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 24 between. Late: reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form sa re-entered at step 68 by `sa.sales_tax_wish` (order 201 seq 7), left after step 66, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form s1a re-entered at step 83 by `s1a.carloan` (order 220 seq 1), left after step 39, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 84 by `s3.ev` (order 225 seq 1), left after step 17, 66 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 89 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 92 by `scope.education_recapture` (order 248 seq 1), left after step 63, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 82, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 85, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 287 seq 1), left after step 92, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 68), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 125 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 122 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 128 by `s3.line10` (order 305 seq 1), left after step 115, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.refund_f8960_refund_unused**: 128 questions, complete; order re-entries 5, form re-entries 26 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×3 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 201 re-entered at step 70 by `sa.state_tax_any` (order 201 seq 1), left after step 68, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- order 204 re-entered at step 77 by `sa.estate_tax_income` (order 204 seq 2), left after step 69, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 24 between. Late: reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form sa re-entered at step 68 by `sa.sales_tax_wish` (order 201 seq 7), left after step 66, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form s1a re-entered at step 83 by `s1a.carloan` (order 220 seq 1), left after step 39, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 84 by `s3.ev` (order 225 seq 1), left after step 17, 66 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 89 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 92 by `scope.education_recapture` (order 248 seq 1), left after step 63, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 82, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 85, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 287 seq 1), left after step 92, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 68), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 125 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 122 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 128 by `s3.line10` (order 305 seq 1), left after step 115, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.refund_combat_pay_no_children**: 128 questions, complete; order re-entries 5, form re-entries 26 sorting and 5 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×3 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 201 re-entered at step 70 by `sa.state_tax_any` (order 201 seq 1), left after step 68, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- order 204 re-entered at step 77 by `sa.estate_tax_income` (order 204 seq 2), left after step 69, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 69), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 67 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 24 between. Late: reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form sa re-entered at step 68 by `sa.sales_tax_wish` (order 201 seq 7), left after step 66, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 66), which its gate does not read.
- form s1a re-entered at step 83 by `s1a.carloan` (order 220 seq 1), left after step 39, 43 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 84 by `s3.ev` (order 225 seq 1), left after step 17, 66 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 89 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 28 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 92 by `scope.education_recapture` (order 248 seq 1), left after step 63, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 98 by `sd.sold_other` (order 274 seq 20), left after step 82, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 105 by `s3.foreign_any` (order 279 seq 1), left after step 85, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 111 by `scope.foreign_shares` (order 287 seq 1), left after step 92, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 112 by `s3.credit_bond` (order 290 seq 1), left after step 105, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 116 by `s2.credit_recapture` (order 291 seq 1), left after step 67, 48 between. Sorting: it was reachable (since step 68), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 120 by `scope.reforestation` (order 295 seq 1), left after step 111, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 125 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 122 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 128 by `s3.line10` (order 305 seq 1), left after step 115, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).

**stage5.return.itemized_f8960_allocation_unused**: 167 questions, complete; order re-entries 6, form re-entries 30 sorting and 11 late, delayed children 4 sorting and 2 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×5 · 201:sa×1 · 204:sa×1 · 200:sa×2 · 201:sa×4 · 202:sa×3 · 202:gift×3 · 203:sa×2 · 204:sa×5 · 215:s3×1 · 215:s2×1 · 193:s2×1 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×6 · 274:sd×6 · 276:sd×1 · 277:f4952×6 · 279:s3×1 · 280:ftc×5 · 284:sa×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×2 · 305:s3×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 200 re-entered at step 72 by `sa.line5b` (order 200 seq 7), left after step 69, 2 between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- order 201 re-entered at step 74 by `sa.state_tax_any` (order 201 seq 1), left after step 70, 3 between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- order 204 re-entered at step 86 by `sa.estate_tax_income` (order 204 seq 2), left after step 71, 14 between. Late: left for `sa.line5b` (order 200 seq 7), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 63 by `scope.archer_msa` (order 191 seq 1), left after step 61, 1 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 65 by `sa.home_owner` (order 200 seq 1), left after step 10, 54 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form sa re-entered at step 84 by `sa.medical_any` (order 203 seq 1), left after step 80, 3 between. Sorting: it was reachable (since step 72), and `$gift` was asked instead (the bank puts order 202 seq 5 first).
- form s3 re-entered at step 91 by `s3.mcc` (order 215 seq 1), left after step 17, 73 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 66), which its gate does not read.
- form s2 re-entered at step 92 by `s2.mortgage_subsidy` (order 215 seq 2), left after step 42, 49 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 66), which its gate does not read.
- form s1a re-entered at step 95 by `s1a.carloan` (order 220 seq 1), left after step 39, 55 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 96 by `s3.ev` (order 225 seq 1), left after step 91, 4 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 215 seq 2 first).
- form person re-entered at step 101 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 40 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 104 by `scope.education_recapture` (order 248 seq 1), left after step 63, 40 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form f1040 re-entered at step 112 by `f1040.line3a` (order 272 seq 3), left after step 2, 109 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 113 by `sd.distributions` (order 272 seq 4), left after step 94, 18 between. Late: reachable only after the answer to `div.any` (step 110), its parent or roster.
- form div re-entered at step 115 by `div.other_boxes` (order 272 seq 7), left after step 110, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sb re-entered at step 116 by `sb.nominee` (order 273 seq 1), left after step 111, 4 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 111), which its gate does not read.
- form sd re-entered at step 119 by `sd.route_each` (order 274 seq 2), left after step 113, 5 between. Late: reachable only after the answer to `$sales` (step 118), which its gate does not read.
- form sales re-entered at step 120 by `sales[s1].box` (order 274 seq 4), left after step 118, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 118), which its gate does not read.
- form sd re-entered at step 126 by `sd.sold_other` (order 274 seq 20), left after step 119, 6 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 139 by `s3.foreign_any` (order 279 seq 1), left after step 97, 41 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form sa re-entered at step 145 by `sa.foreign_tax_deduct` (order 284 seq 1), left after step 90, 54 between. Late: reachable only after the answer to `ftc.taxes` (step 140), which its gate does not read.
- form sb re-entered at step 146 by `sb.account_any` (order 285 seq 1), left after step 117, 28 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 151 by `scope.foreign_shares` (order 287 seq 1), left after step 104, 46 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 152 by `s3.credit_bond` (order 290 seq 1), left after step 139, 12 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 156 by `s2.credit_recapture` (order 291 seq 1), left after step 93, 62 between. Sorting: it was reachable (since step 94), and `sd.casualty` was asked instead (the bank puts order 216 seq 1 first).
- form scope re-entered at step 160 by `scope.reforestation` (order 295 seq 1), left after step 151, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form qbi re-entered at step 163 by `qbi.prior_form` (order 262 seq 1), left after step 114, 48 between. Late: reachable only after the answer to `scope.business_before` (step 162), which its gate does not read.
- form f1040 re-entered at step 165 by `f1040.withheld_other_any` (order 300 seq 1), left after step 112, 52 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 167 by `s3.line10` (order 305 seq 1), left after step 155, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- `sa.line5b` (order 200 seq 7), step 72: child of `sa.home_owner` (step 65), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- `sa.property_tax_other_any` (order 200 seq 8), step 73: child of `sa.home_owner` (step 65), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 71), which its gate does not read.
- `sd.distributions` (order 272 seq 4), step 113: child of `div.any` (step 110), 1 other question between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 115: child of `div.any` (step 110), 2 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sales[s1].route` (order 274 seq 11), step 123: child of `sd.route_each` (step 119), 3 other questions between. Sorting: it was reachable (since step 120), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- `sd.f2439` (order 274 seq 28), step 131: child of `div.any` (step 110), 17 other questions between. Sorting: it was reachable (since step 111), and `f1040.line3a` was asked instead (the bank puts order 272 seq 3 first).

### generated returns

**generated.0**: 239 questions, refused; order re-entries 9, form re-entries 27 sorting and 9 late, delayed children 0 sorting and 2 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×13 · 191:scope×1 · 195:f1095a×1 · 200:sa×5 · 201:sa×1 · 204:sa×1 · 200:sa×2 · 201:sa×4 · 202:sa×3 · 202:gift×5 · 203:sa×2 · 204:sa×5 · 215:s3×1 · 215:s2×1 · 193:s2×1 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×2 · 177:person×1 · 248:scope×1 · 250:sc×1 · 140:w2×2 · 250:sc×4 · 251:sc×7 · 252:sc×24 · 253:sc×8 · 254:sc×1 · 255:scveh×1 · 257:asset×22 · 258:s179×1 · 254:sc×1 · 259:sc×3 · 259:ltc×1 · 260:person×1 · 261:person×1 · 265:scope×2 · 270:interest×3 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×6 · 279:s3×1 · 280:ftc×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 267:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×2 · 295:scope×3

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 200 re-entered at step 84 by `sa.line5b` (order 200 seq 7), left after step 81, 2 between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- order 201 re-entered at step 86 by `sa.state_tax_any` (order 201 seq 1), left after step 82, 3 between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- order 204 re-entered at step 100 by `sa.estate_tax_income` (order 204 seq 2), left after step 83, 16 between. Late: left for `sa.line5b` (order 200 seq 7), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- order 140 re-entered at step 121 by `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), left after step 28, 92 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- order 250 re-entered at step 123 by `person[taxpayer].sc[biz_a].line1` (order 250 seq 2), left after step 120, 2 between. Late: left for `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), which sorts earlier and was reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- order 254 re-entered at step 191 by `person[taxpayer].sc[biz_a].at_risk` (order 254 seq 5), left after step 166, 24 between. Late: reachable only after the answer to `s179.prior_form` (step 190), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 75 by `scope.archer_msa` (order 191 seq 1), left after step 61, 13 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 77 by `sa.home_owner` (order 200 seq 1), left after step 10, 66 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form sa re-entered at step 98 by `sa.medical_any` (order 203 seq 1), left after step 92, 5 between. Sorting: it was reachable (since step 84), and `$gift` was asked instead (the bank puts order 202 seq 5 first).
- form s3 re-entered at step 105 by `s3.mcc` (order 215 seq 1), left after step 17, 87 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- form s2 re-entered at step 106 by `s2.mortgage_subsidy` (order 215 seq 2), left after step 42, 63 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- form s1a re-entered at step 109 by `s1a.carloan` (order 220 seq 1), left after step 39, 69 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 110 by `s3.ev` (order 225 seq 1), left after step 105, 4 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 215 seq 2 first).
- form person re-entered at step 115 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 54 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 119 by `scope.education_recapture` (order 248 seq 1), left after step 75, 43 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form w2 re-entered at step 121 by `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), left after step 28, 92 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form sc re-entered at step 123 by `person[taxpayer].sc[biz_a].line1` (order 250 seq 2), left after step 120, 2 between. Late: left for `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), which sorts earlier and was reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form sc re-entered at step 191 by `person[taxpayer].sc[biz_a].at_risk` (order 254 seq 5), left after step 166, 24 between. Late: reachable only after the answer to `s179.prior_form` (step 190), which its gate does not read.
- form person re-entered at step 196 by `person[taxpayer].plan` (order 260 seq 1), left after step 118, 77 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form scope re-entered at step 198 by `scope.se_plan_other` (order 265 seq 1), left after step 119, 78 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 120), which its gate does not read.
- form sd re-entered at step 207 by `sd.sold_other` (order 274 seq 20), left after step 108, 98 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 219 by `s3.foreign_any` (order 279 seq 1), left after step 111, 107 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form sb re-entered at step 221 by `sb.account_any` (order 285 seq 1), left after step 205, 15 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 226 by `scope.foreign_shares` (order 287 seq 1), left after step 199, 26 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 227 by `s3.credit_bond` (order 290 seq 1), left after step 219, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 231 by `s2.credit_recapture` (order 291 seq 1), left after step 107, 123 between. Sorting: it was reachable (since step 108), and `sd.casualty` was asked instead (the bank puts order 216 seq 1 first).
- form scope re-entered at step 237 by `scope.reforestation` (order 295 seq 1), left after step 226, 10 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- `sa.line5b` (order 200 seq 7), step 84: child of `sa.home_owner` (step 77), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- `sa.property_tax_other_any` (order 200 seq 8), step 85: child of `sa.home_owner` (step 77), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.

**generated.1**: 58 questions, refused; order re-entries 1, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×2 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×43 · 102:household×1

- order 111 re-entered at step 9 by `sa.excluded_income` (order 111 seq 2), left after step 7, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 7), which its gate does not read.
- form person re-entered at step 5 by `person[taxpayer].birth_year` (order 2), left after step 1, 3 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 6 by `household.community_property` (order 103 seq 1), left after step 4, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 8 by `person[taxpayer].blind` (order 110 seq 4), left after step 5, 2 between. Late: reachable only after the answer to `sa.dependent` (step 7), which its gate does not read.
- form sa re-entered at step 9 by `sa.excluded_income` (order 111 seq 2), left after step 7, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 7), which its gate does not read.
- form household re-entered at step 58 by `household.home_cost` (order 102 seq 2), left after step 6, 51 between. Late: reachable only after the answer to `dependent[dep_c].tin` (step 57), which its gate does not read.

**generated.2**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.3**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.4**: 271 questions, complete; order re-entries 11, form re-entries 31 sorting and 19 late, delayed children 4 sorting and 3 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×13 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 200:sa×1 · 201:sa×1 · 204:sa×1 · 200:sa×2 · 201:sa×4 · 202:sa×3 · 202:gift×3 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×4 · 247:person×1 · 192:person×2 · 177:person×1 · 248:scope×1 · 250:sc×1 · 140:w2×2 · 250:sc×4 · 251:sc×7 · 252:sc×24 · 253:sc×8 · 254:sc×1 · 255:scveh×1 · 257:asset×22 · 258:s179×1 · 254:sc×1 · 259:sc×3 · 259:ltc×3 · 260:person×1 · 261:person×1 · 265:scope×2 · 270:interest×5 · 272:div×1 · 272:sb×1 · 272:f1040×1 · 272:sd×1 · 272:qbi×1 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×13 · 274:sd×6 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 280:ftc×5 · 284:sa×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 267:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×3 · 295:scope×3 · 300:f1040×2 · 305:s3×1 · 315:person×1 · 262:qbi×3 · 311:person×1 · 271:f1040×1 · 272:div×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 200 re-entered at step 80 by `sa.mortgage_unreported` (order 200 seq 4), left after step 78, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- order 200 re-entered at step 83 by `sa.line5b` (order 200 seq 7), left after step 80, 2 between. Late: reachable only after the answer to `sa.elect_itemize` (step 82), which its gate does not read.
- order 201 re-entered at step 85 by `sa.state_tax_any` (order 201 seq 1), left after step 81, 3 between. Late: reachable only after the answer to `sa.elect_itemize` (step 82), which its gate does not read.
- order 204 re-entered at step 97 by `sa.estate_tax_income` (order 204 seq 2), left after step 82, 14 between. Late: left for `sa.line5b` (order 200 seq 7), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 82), which its gate does not read.
- order 140 re-entered at step 118 by `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), left after step 28, 89 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 117), which its gate does not read.
- order 250 re-entered at step 120 by `person[taxpayer].sc[biz_a].line1` (order 250 seq 2), left after step 117, 2 between. Late: left for `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), which sorts earlier and was reachable only after the answer to `$sc@person[taxpayer]` (step 117), which its gate does not read.
- order 254 re-entered at step 188 by `person[taxpayer].sc[biz_a].at_risk` (order 254 seq 5), left after step 163, 24 between. Late: reachable only after the answer to `s179.prior_form` (step 187), which its gate does not read.
- order 272 re-entered at step 271 by `div.box12` (order 272 seq 6), left after step 209, 61 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 269), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 75 by `scope.archer_msa` (order 191 seq 1), left after step 61, 13 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 77 by `sa.home_owner` (order 200 seq 1), left after step 10, 66 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 79 by `s2.hsa_testing` (order 193 seq 1), left after step 42, 36 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- form sa re-entered at step 80 by `sa.mortgage_unreported` (order 200 seq 4), left after step 78, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- form sa re-entered at step 95 by `sa.medical_any` (order 203 seq 1), left after step 91, 3 between. Sorting: it was reachable (since step 83), and `$gift` was asked instead (the bank puts order 202 seq 5 first).
- form s1a re-entered at step 103 by `s1a.carloan` (order 220 seq 1), left after step 39, 63 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 104 by `s3.ev` (order 225 seq 1), left after step 17, 86 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 112 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 51 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 116 by `scope.education_recapture` (order 248 seq 1), left after step 75, 40 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form w2 re-entered at step 118 by `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), left after step 28, 89 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 117), which its gate does not read.
- form sc re-entered at step 120 by `person[taxpayer].sc[biz_a].line1` (order 250 seq 2), left after step 117, 2 between. Late: left for `person[taxpayer].w2[emp_a].box3` (order 140 seq 5), which sorts earlier and was reachable only after the answer to `$sc@person[taxpayer]` (step 117), which its gate does not read.
- form sc re-entered at step 188 by `person[taxpayer].sc[biz_a].at_risk` (order 254 seq 5), left after step 163, 24 between. Late: reachable only after the answer to `s179.prior_form` (step 187), which its gate does not read.
- form person re-entered at step 195 by `person[taxpayer].plan` (order 260 seq 1), left after step 115, 79 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 117), which its gate does not read.
- form scope re-entered at step 197 by `scope.se_plan_other` (order 265 seq 1), left after step 116, 80 between. Late: reachable only after the answer to `$sc@person[taxpayer]` (step 117), which its gate does not read.
- form f1040 re-entered at step 206 by `f1040.line3a` (order 272 seq 3), left after step 2, 203 between. Late: reachable only after the answer to `sb.ordinary_dividends` (step 205), which its gate does not read.
- form sd re-entered at step 207 by `sd.distributions` (order 272 seq 4), left after step 102, 104 between. Late: reachable only after the answer to `div.any` (step 204), its parent or roster.
- form div re-entered at step 209 by `div.other_boxes` (order 272 seq 7), left after step 204, 4 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sb re-entered at step 210 by `sb.nominee` (order 273 seq 1), left after step 205, 4 between. Late: left for `f1040.line3a` (order 272 seq 3), which sorts earlier and was reachable only after the answer to `sb.ordinary_dividends` (step 205), which its gate does not read.
- form sd re-entered at step 213 by `sd.route_each` (order 274 seq 2), left after step 207, 5 between. Late: reachable only after the answer to `$sales` (step 212), which its gate does not read.
- form sales re-entered at step 214 by `sales[s1].box` (order 274 seq 4), left after step 212, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 212), which its gate does not read.
- form sd re-entered at step 227 by `sd.sold_other` (order 274 seq 20), left after step 213, 13 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 235 by `s3.foreign_any` (order 279 seq 1), left after step 105, 129 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form sa re-entered at step 241 by `sa.foreign_tax_deduct` (order 284 seq 1), left after step 101, 139 between. Late: reachable only after the answer to `ftc.taxes` (step 236), which its gate does not read.
- form sb re-entered at step 242 by `sb.account_any` (order 285 seq 1), left after step 211, 30 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 247 by `scope.foreign_shares` (order 287 seq 1), left after step 198, 48 between. Sorting: it was reachable (since step 1), and `$interest` was asked instead (the bank puts order 270 seq 1 first).
- form s3 re-entered at step 248 by `s3.credit_bond` (order 290 seq 1), left after step 235, 12 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 252 by `s2.credit_recapture` (order 291 seq 1), left after step 79, 172 between. Sorting: it was reachable (since step 80), and `sa.mortgage_unreported` was asked instead (the bank puts order 200 seq 4 first).
- form scope re-entered at step 259 by `scope.reforestation` (order 295 seq 1), left after step 247, 11 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 262 by `f1040.withheld_other_any` (order 300 seq 1), left after step 206, 55 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 264 by `s3.line10` (order 305 seq 1), left after step 251, 12 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 265 by `person[taxpayer].sav_claimed` (order 315 seq 2), left after step 196, 68 between. Sorting: it was reachable (since step 112), and `scope.se_plan_other` was asked instead (the bank puts order 265 seq 1 first).
- form qbi re-entered at step 266 by `qbi.prior_form` (order 262 seq 1), left after step 208, 57 between. Late: reachable only after the answer to `person[taxpayer].sav_claimed` (step 265), which its gate does not read.
- form person re-entered at step 269 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 265, 3 between. Late: left for `qbi.prior_form` (order 262 seq 1), which sorts earlier and was reachable only after the answer to `person[taxpayer].sav_claimed` (step 265), which its gate does not read.
- form f1040 re-entered at step 270 by `f1040.tax_exempt_interest` (order 271 seq 1), left after step 263, 6 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 269), which its gate does not read.
- form div re-entered at step 271 by `div.box12` (order 272 seq 6), left after step 209, 61 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 269), which its gate does not read.
- `sa.mortgage_unreported` (order 200 seq 4), step 80: child of `sa.home_owner` (step 77), 1 other question between. Sorting: it was reachable (since step 78), and `s2.hsa_testing` was asked instead (the bank puts order 193 seq 1 first).
- `sa.line5b` (order 200 seq 7), step 83: child of `sa.home_owner` (step 77), 3 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 82), which its gate does not read.
- `sa.property_tax_other_any` (order 200 seq 8), step 84: child of `sa.home_owner` (step 77), 3 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 82), which its gate does not read.
- `sd.distributions` (order 272 seq 4), step 207: child of `div.any` (step 204), 1 other question between. Sorting: it was reachable (since step 205), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `div.other_boxes` (order 272 seq 7), step 209: child of `div.any` (step 204), 2 other questions between. Sorting: it was reachable (since step 205), and `f1040.line3a` was asked instead (within order 272, the block's entry and seq order put it first).
- `sd.f2439` (order 274 seq 28), step 232: child of `div.any` (step 204), 24 other questions between. Sorting: it was reachable (since step 205), and `f1040.line3a` was asked instead (the bank puts order 272 seq 3 first).
- `div.box12` (order 272 seq 6), step 271: child of `div.any` (step 204), 61 other questions between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 269), which its gate does not read.

**generated.5**: 7 questions, refused; order re-entries 0, form re-entries 2 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×2 · 2:person×1 · 103:household×1 · 111:sa×1

- form person re-entered at step 5 by `person[taxpayer].birth_year` (order 2), left after step 1, 3 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 6 by `household.community_property` (order 103 seq 1), left after step 4, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).

**generated.6**: 161 questions, complete; order re-entries 6, form re-entries 27 sorting and 7 late, delayed children 0 sorting and 2 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×6 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×13 · 191:scope×1 · 195:f1095a×1 · 200:sa×5 · 201:sa×1 · 204:sa×1 · 200:sa×2 · 201:sa×4 · 202:sa×3 · 202:gift×1 · 203:sa×2 · 204:sa×5 · 215:s3×1 · 215:s2×1 · 193:s2×1 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×2 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×6 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×2 · 305:s3×1 · 311:person×1 · 271:f1040×1 · 313:eic×3 · 310:s8812×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 52 by `s1.nqdc_pension` (order 148 seq 2), left after step 36, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 51), which its gate does not read.
- order 161 re-entered at step 53 by `s1.inmate_wages` (order 161 seq 6), left after step 51, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 52), which its gate does not read.
- order 200 re-entered at step 84 by `sa.line5b` (order 200 seq 7), left after step 81, 2 between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- order 201 re-entered at step 86 by `sa.state_tax_any` (order 201 seq 1), left after step 82, 3 between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- order 204 re-entered at step 96 by `sa.estate_tax_income` (order 204 seq 2), left after step 83, 12 between. Late: left for `sa.line5b` (order 200 seq 7), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 17 by `s3.adoption_any` (order 126 seq 1), left after step 15, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 18 by `scope.f8814` (order 127 seq 1), left after step 14, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 22 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 29 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 22, 6 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 30 by `scope.pay_no_w2` (order 145 seq 1), left after step 21, 8 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 37 by `s2.options_any` (order 149 seq 1), left after step 35, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 42 by `s2.household_help` (order 159 seq 1), left after step 37, 4 between. Sorting: it was reachable (since step 36), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 56 by `scope.recovery` (order 168 seq 1), left after step 34, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 58 by `scope.disaster_distribution` (order 175 seq 1), left after step 56, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 60 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 29, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 61 by `scope.excess_deferral` (order 187 seq 1), left after step 58, 2 between. Sorting: it was reachable (since step 24), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 75 by `scope.archer_msa` (order 191 seq 1), left after step 61, 13 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 77 by `sa.home_owner` (order 200 seq 1), left after step 10, 66 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form sa re-entered at step 94 by `sa.medical_any` (order 203 seq 1), left after step 92, 1 between. Sorting: it was reachable (since step 84), and `$gift` was asked instead (the bank puts order 202 seq 5 first).
- form s3 re-entered at step 101 by `s3.mcc` (order 215 seq 1), left after step 17, 83 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- form s2 re-entered at step 102 by `s2.mortgage_subsidy` (order 215 seq 2), left after step 42, 59 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 78), which its gate does not read.
- form s1a re-entered at step 105 by `s1a.carloan` (order 220 seq 1), left after step 39, 65 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 106 by `s3.ev` (order 225 seq 1), left after step 101, 4 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 215 seq 2 first).
- form person re-entered at step 111 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 60, 50 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 115 by `scope.education_recapture` (order 248 seq 1), left after step 75, 39 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 121 by `sd.sold_other` (order 274 seq 20), left after step 104, 16 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 133 by `s3.foreign_any` (order 279 seq 1), left after step 107, 25 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 139 by `scope.foreign_shares` (order 287 seq 1), left after step 115, 23 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 140 by `s3.credit_bond` (order 290 seq 1), left after step 133, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 144 by `s2.credit_recapture` (order 291 seq 1), left after step 103, 40 between. Sorting: it was reachable (since step 104), and `sd.casualty` was asked instead (the bank puts order 216 seq 1 first).
- form scope re-entered at step 148 by `scope.reforestation` (order 295 seq 1), left after step 139, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 153 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 150 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 155 by `s3.line10` (order 305 seq 1), left after step 143, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 156 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 114, 41 between. Late: reachable only after the answer to `scope.business_before` (step 150), which its gate does not read.
- form f1040 re-entered at step 157 by `f1040.tax_exempt_interest` (order 271 seq 1), left after step 154, 2 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 156), which its gate does not read.
- `sa.line5b` (order 200 seq 7), step 84: child of `sa.home_owner` (step 77), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.
- `sa.property_tax_other_any` (order 200 seq 8), step 85: child of `sa.home_owner` (step 77), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 83), which its gate does not read.

**generated.7**: 18 questions, refused; order re-entries 1, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 2:household×1 · 2:person×2 · 111:sa×1 · 110:person×2 · 111:sa×1 · 113:scope×3 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3

- order 111 re-entered at step 8 by `sa.excluded_income` (order 111 seq 2), left after step 5, 2 between. Late: left for `person[spouse].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 5), which its gate does not read.
- form person re-entered at step 3 by `person[spouse].birth_year` (order 2), left after step 1, 1 between. Late: left for `household.married_dec31` (order 2), which sorts earlier and was reachable only after the answer to `$person` (step 1), which its gate does not read.
- form person re-entered at step 6 by `person[spouse].blind` (order 110 seq 4), left after step 4, 1 between. Late: reachable only after the answer to `sa.dependent` (step 5), which its gate does not read.
- form sa re-entered at step 8 by `sa.excluded_income` (order 111 seq 2), left after step 5, 2 between. Late: left for `person[spouse].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 5), which its gate does not read.
- form s3 re-entered at step 14 by `s3.adoption_any` (order 126 seq 1), left after step 12, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 15 by `scope.f8814` (order 127 seq 1), left after step 11, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).

**generated.8**: 2 questions, refused; order re-entries 0, form re-entries 0 sorting and 0 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1

**generated.9**: 31 questions, refused; order re-entries 1, form re-entries 4 sorting and 2 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×5 · 118:s3×1 · 120:dependent×12 · 126:s3×1 · 127:scope×1 · 130:scope×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 29 by `s3.adoption_any` (order 126 seq 1), left after step 16, 12 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 30 by `scope.f8814` (order 127 seq 1), left after step 15, 14 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).

**generated.10**: 206 questions, complete; order re-entries 7, form re-entries 30 sorting and 11 late, delayed children 1 sorting and 3 late.

0:person×1 · 0:f1040×1 · 2:household×3 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×14 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×15 · 144:person×1 · 145:scope×3 · 146:scope×2 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 187:scope×1 · 190:f8889×13 · 191:scope×1 · 195:f1095a×1 · 200:sa×5 · 201:sa×1 · 204:sa×1 · 200:sa×2 · 201:sa×4 · 202:sa×3 · 202:gift×5 · 203:sa×2 · 204:sa×5 · 215:s3×1 · 215:s2×1 · 193:s2×1 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×2 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×3 · 272:div×1 · 272:sb×1 · 272:sd×1 · 272:div×1 · 273:sb×2 · 274:sales×1 · 274:sd×1 · 274:sales×17 · 274:sd×6 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 280:ftc×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×2 · 305:s3×1 · 311:person×1 · 271:f1040×1 · 272:div×1

- order 111 re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- order 148 re-entered at step 74 by `s1.nqdc_pension` (order 148 seq 2), left after step 58, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 73), which its gate does not read.
- order 161 re-entered at step 75 by `s1.inmate_wages` (order 161 seq 6), left after step 73, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 74), which its gate does not read.
- order 200 re-entered at step 106 by `sa.line5b` (order 200 seq 7), left after step 103, 2 between. Late: reachable only after the answer to `sa.elect_itemize` (step 105), which its gate does not read.
- order 201 re-entered at step 108 by `sa.state_tax_any` (order 201 seq 1), left after step 104, 3 between. Late: reachable only after the answer to `sa.elect_itemize` (step 105), which its gate does not read.
- order 204 re-entered at step 122 by `sa.estate_tax_income` (order 204 seq 2), left after step 105, 16 between. Late: left for `sa.line5b` (order 200 seq 7), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 105), which its gate does not read.
- order 272 re-entered at step 206 by `div.box12` (order 272 seq 6), left after step 150, 55 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 204), which its gate does not read.
- form person re-entered at step 6 by `person[taxpayer].birth_year` (order 2), left after step 1, 4 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 7 by `household.community_property` (order 103 seq 1), left after step 5, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 9 by `person[taxpayer].blind` (order 110 seq 4), left after step 6, 2 between. Late: reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form sa re-entered at step 10 by `sa.excluded_income` (order 111 seq 2), left after step 8, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 8), which its gate does not read.
- form s3 re-entered at step 30 by `s3.adoption_any` (order 126 seq 1), left after step 15, 14 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 31 by `scope.f8814` (order 127 seq 1), left after step 14, 16 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 35 by `person[taxpayer].rrta` (order 140 seq 1), left after step 9, 25 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 51 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 35, 15 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 52 by `scope.pay_no_w2` (order 145 seq 1), left after step 34, 17 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 59 by `s2.options_any` (order 149 seq 1), left after step 57, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 64 by `s2.household_help` (order 159 seq 1), left after step 59, 4 between. Sorting: it was reachable (since step 58), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 78 by `scope.recovery` (order 168 seq 1), left after step 56, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 80 by `scope.disaster_distribution` (order 175 seq 1), left after step 78, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 82 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 51, 30 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 83 by `scope.excess_deferral` (order 187 seq 1), left after step 80, 2 between. Sorting: it was reachable (since step 37), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form scope re-entered at step 97 by `scope.archer_msa` (order 191 seq 1), left after step 83, 13 between. Sorting: it was reachable (since step 1), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form sa re-entered at step 99 by `sa.home_owner` (order 200 seq 1), left after step 10, 88 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form sa re-entered at step 120 by `sa.medical_any` (order 203 seq 1), left after step 114, 5 between. Sorting: it was reachable (since step 106), and `$gift` was asked instead (the bank puts order 202 seq 5 first).
- form s3 re-entered at step 127 by `s3.mcc` (order 215 seq 1), left after step 30, 96 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 100), which its gate does not read.
- form s2 re-entered at step 128 by `s2.mortgage_subsidy` (order 215 seq 2), left after step 64, 63 between. Late: reachable only after the answer to `sa.mortgage_interest` (step 100), which its gate does not read.
- form s1a re-entered at step 131 by `s1a.carloan` (order 220 seq 1), left after step 61, 69 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 132 by `s3.ev` (order 225 seq 1), left after step 127, 4 between. Sorting: it was reachable (since step 1), and `s2.mortgage_subsidy` was asked instead (the bank puts order 215 seq 2 first).
- form person re-entered at step 137 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 82, 54 between. Sorting: it was reachable (since step 2), and `scope.excess_deferral` was asked instead (the bank puts order 187 seq 1 first).
- form scope re-entered at step 141 by `scope.education_recapture` (order 248 seq 1), left after step 97, 43 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 149 by `sd.distributions` (order 272 seq 4), left after step 130, 18 between. Late: reachable only after the answer to `div.any` (step 147), its parent or roster.
- form div re-entered at step 150 by `div.other_boxes` (order 272 seq 7), left after step 147, 2 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sb re-entered at step 151 by `sb.nominee` (order 273 seq 1), left after step 148, 2 between. Sorting: it was reachable (since step 146), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form sd re-entered at step 154 by `sd.route_each` (order 274 seq 2), left after step 149, 4 between. Late: reachable only after the answer to `$sales` (step 153), which its gate does not read.
- form sales re-entered at step 155 by `sales[s1].box` (order 274 seq 4), left after step 153, 1 between. Late: left for `sd.route_each` (order 274 seq 2), which sorts earlier and was reachable only after the answer to `$sales` (step 153), which its gate does not read.
- form sd re-entered at step 172 by `sd.sold_other` (order 274 seq 20), left after step 154, 17 between. Sorting: it was reachable (since step 1), and `sales[s1].box` was asked instead (within order 274, the block's entry and seq order put it first).
- form s3 re-entered at step 180 by `s3.foreign_any` (order 279 seq 1), left after step 133, 46 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form sb re-entered at step 182 by `sb.account_any` (order 285 seq 1), left after step 152, 29 between. Sorting: it was reachable (since step 1), and `$sales` was asked instead (the bank puts order 274 seq 1 first).
- form scope re-entered at step 187 by `scope.foreign_shares` (order 287 seq 1), left after step 141, 45 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 188 by `s3.credit_bond` (order 290 seq 1), left after step 180, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- form s2 re-entered at step 192 by `s2.credit_recapture` (order 291 seq 1), left after step 129, 62 between. Sorting: it was reachable (since step 130), and `sd.casualty` was asked instead (the bank puts order 216 seq 1 first).
- form scope re-entered at step 196 by `scope.reforestation` (order 295 seq 1), left after step 187, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 201 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 198 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 203 by `s3.line10` (order 305 seq 1), left after step 191, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 204 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 140, 63 between. Late: reachable only after the answer to `scope.business_before` (step 198), which its gate does not read.
- form f1040 re-entered at step 205 by `f1040.tax_exempt_interest` (order 271 seq 1), left after step 202, 2 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 204), which its gate does not read.
- form div re-entered at step 206 by `div.box12` (order 272 seq 6), left after step 150, 55 between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 204), which its gate does not read.
- `sa.line5b` (order 200 seq 7), step 106: child of `sa.home_owner` (step 99), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 105), which its gate does not read.
- `sa.property_tax_other_any` (order 200 seq 8), step 107: child of `sa.home_owner` (step 99), 4 other questions between. Late: reachable only after the answer to `sa.elect_itemize` (step 105), which its gate does not read.
- `sd.f2439` (order 274 seq 28), step 177: child of `div.any` (step 147), 26 other questions between. Sorting: it was reachable (since step 148), and `sb.nominee` was asked instead (the bank puts order 273 seq 1 first).
- `div.box12` (order 272 seq 6), step 206: child of `div.any` (step 147), 53 other questions between. Late: reachable only after the answer to `person[taxpayer].eic_ssn` (step 204), which its gate does not read.

**generated.11**: 28 questions, refused; order re-entries 1, form re-entries 2 sorting and 3 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×2 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×13 · 102:household×1

- order 111 re-entered at step 9 by `sa.excluded_income` (order 111 seq 2), left after step 7, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 7), which its gate does not read.
- form person re-entered at step 5 by `person[taxpayer].birth_year` (order 2), left after step 1, 3 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 6 by `household.community_property` (order 103 seq 1), left after step 4, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 8 by `person[taxpayer].blind` (order 110 seq 4), left after step 5, 2 between. Late: reachable only after the answer to `sa.dependent` (step 7), which its gate does not read.
- form sa re-entered at step 9 by `sa.excluded_income` (order 111 seq 2), left after step 7, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 7), which its gate does not read.
- form household re-entered at step 28 by `household.home_cost` (order 102 seq 2), left after step 6, 21 between. Late: reachable only after the answer to `dependent[dep_a].parent_home_paid` (step 27), which its gate does not read.

### minimal returns

**every gate closed**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

0:person×1 · 0:f1040×1 · 2:household×1 · 2:person×1 · 103:household×1 · 111:sa×1 · 110:person×1 · 111:sa×1 · 113:scope×4 · 118:s3×1 · 120:dependent×1 · 126:s3×1 · 127:scope×1 · 130:scope×3 · 140:person×1 · 140:w2×1 · 144:person×1 · 145:scope×3 · 148:s2×1 · 148:f8959×1 · 149:s2×1 · 150:s1a×1 · 152:s1a×1 · 155:f2441×2 · 159:s2×1 · 160:s1×6 · 161:s1×3 · 148:s1×1 · 161:s1×2 · 165:refund×1 · 168:scope×1 · 170:retirement×1 · 175:scope×1 · 178:ssb×1 · 180:person×1 · 190:f8889×1 · 191:scope×1 · 195:f1095a×1 · 200:sa×2 · 193:s2×1 · 201:sa×1 · 204:sa×1 · 201:sa×3 · 202:sa×2 · 203:sa×2 · 204:sa×5 · 216:sd×1 · 220:s1a×1 · 225:s3×2 · 230:f5695×1 · 240:f8863×1 · 244:sli×1 · 247:person×1 · 192:person×1 · 177:person×1 · 248:scope×1 · 250:sc×1 · 258:s179×1 · 270:interest×1 · 272:div×1 · 274:sales×1 · 274:sd×5 · 276:sd×1 · 277:f4952×1 · 279:s3×1 · 285:sb×5 · 287:scope×1 · 290:s3×4 · 291:s2×1 · 292:s2×1 · 293:s2×1 · 294:oi8z×1 · 295:scope×3 · 262:qbi×2 · 300:f1040×2 · 305:s3×1 · 311:person×1

- order 111 re-entered at step 8 by `sa.excluded_income` (order 111 seq 2), left after step 6, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 6), which its gate does not read.
- order 148 re-entered at step 43 by `s1.nqdc_pension` (order 148 seq 2), left after step 27, 15 between. Late: reachable only after the answer to `s1.ltc_payout` (step 42), which its gate does not read.
- order 161 re-entered at step 44 by `s1.inmate_wages` (order 161 seq 6), left after step 42, 1 between. Late: reachable only after the answer to `s1.nqdc_pension` (step 43), which its gate does not read.
- order 201 re-entered at step 60 by `sa.state_tax_any` (order 201 seq 1), left after step 58, 1 between. Late: reachable only after the answer to `sa.elect_itemize` (step 59), which its gate does not read.
- order 204 re-entered at step 67 by `sa.estate_tax_income` (order 204 seq 2), left after step 59, 7 between. Late: left for `sa.state_tax_any` (order 201 seq 1), which sorts earlier and was reachable only after the answer to `sa.elect_itemize` (step 59), which its gate does not read.
- form person re-entered at step 4 by `person[taxpayer].birth_year` (order 2), left after step 1, 2 between. Sorting: it was reachable (since step 2), and `f1040.status` was asked instead (the bank puts order 0 first).
- form household re-entered at step 5 by `household.community_property` (order 103 seq 1), left after step 3, 1 between. Sorting: it was reachable (since step 3), and `person[taxpayer].birth_year` was asked instead (the bank puts order 2 first).
- form person re-entered at step 7 by `person[taxpayer].blind` (order 110 seq 4), left after step 4, 2 between. Late: reachable only after the answer to `sa.dependent` (step 6), which its gate does not read.
- form sa re-entered at step 8 by `sa.excluded_income` (order 111 seq 2), left after step 6, 1 between. Late: left for `person[taxpayer].blind` (order 110 seq 4), which sorts earlier and was reachable only after the answer to `sa.dependent` (step 6), which its gate does not read.
- form s3 re-entered at step 15 by `s3.adoption_any` (order 126 seq 1), left after step 13, 1 between. Sorting: it was reachable (since step 1), and `$dependent` was asked instead (the bank puts order 120 seq 1 first).
- form scope re-entered at step 16 by `scope.f8814` (order 127 seq 1), left after step 12, 3 between. Sorting: it was reachable (since step 1), and `s3.disability_retired` was asked instead (the bank puts order 118 seq 1 first).
- form person re-entered at step 20 by `person[taxpayer].rrta` (order 140 seq 1), left after step 7, 12 between. Sorting: it was reachable (since step 2), and `sa.excluded_income` was asked instead (the bank puts order 111 seq 2 first).
- form person re-entered at step 22 by `person[taxpayer].eligible_educator` (order 144 seq 1), left after step 20, 1 between. Sorting: it was reachable (since step 2), and `$w2@person[taxpayer]` was asked instead (the bank puts order 140 seq 2 first).
- form scope re-entered at step 23 by `scope.pay_no_w2` (order 145 seq 1), left after step 19, 3 between. Sorting: it was reachable (since step 1), and `person[taxpayer].rrta` was asked instead (the bank puts order 140 seq 1 first).
- form s2 re-entered at step 28 by `s2.options_any` (order 149 seq 1), left after step 26, 1 between. Sorting: it was reachable (since step 1), and `f8959.territory_w2` was asked instead (the bank puts order 148 seq 3 first).
- form s2 re-entered at step 33 by `s2.household_help` (order 159 seq 1), left after step 28, 4 between. Sorting: it was reachable (since step 27), and `s1a.tips` was asked instead (the bank puts order 150 seq 1 first).
- form scope re-entered at step 47 by `scope.recovery` (order 168 seq 1), left after step 25, 21 between. Sorting: it was reachable (since step 1), and `s2.w2_marks` was asked instead (the bank puts order 148 seq 1 first).
- form scope re-entered at step 49 by `scope.disaster_distribution` (order 175 seq 1), left after step 47, 1 between. Sorting: it was reachable (since step 1), and `$retirement@person[taxpayer]` was asked instead (the bank puts order 170 seq 1 first).
- form person re-entered at step 51 by `person[taxpayer].ira_owner` (order 180 seq 1), left after step 22, 28 between. Sorting: it was reachable (since step 2), and `scope.pay_no_w2` was asked instead (the bank puts order 145 seq 1 first).
- form scope re-entered at step 53 by `scope.archer_msa` (order 191 seq 1), left after step 49, 3 between. Sorting: it was reachable (since step 1), and `ssb.any` was asked instead (the bank puts order 178 seq 1 first).
- form sa re-entered at step 55 by `sa.home_owner` (order 200 seq 1), left after step 8, 46 between. Sorting: it was reachable (since step 1), and `scope.noncitizen` was asked instead (the bank puts order 113 seq 1 first).
- form s2 re-entered at step 57 by `s2.hsa_testing` (order 193 seq 1), left after step 33, 23 between. Late: reachable only after the answer to `sa.home_other` (step 56), which its gate does not read.
- form sa re-entered at step 58 by `sa.sales_tax_wish` (order 201 seq 7), left after step 56, 1 between. Late: left for `s2.hsa_testing` (order 193 seq 1), which sorts earlier and was reachable only after the answer to `sa.home_other` (step 56), which its gate does not read.
- form s1a re-entered at step 73 by `s1a.carloan` (order 220 seq 1), left after step 30, 42 between. Sorting: it was reachable (since step 1), and `f2441.care` was asked instead (the bank puts order 155 seq 1 first).
- form s3 re-entered at step 74 by `s3.ev` (order 225 seq 1), left after step 15, 58 between. Sorting: it was reachable (since step 1), and `scope.f8814` was asked instead (the bank puts order 127 seq 1 first).
- form person re-entered at step 79 by `person[taxpayer].x_edu_account` (order 247 seq 1), left after step 51, 27 between. Sorting: it was reachable (since step 2), and `$f8889@person[taxpayer]` was asked instead (the bank puts order 190 seq 1 first).
- form scope re-entered at step 82 by `scope.education_recapture` (order 248 seq 1), left after step 53, 28 between. Sorting: it was reachable (since step 1), and `$f1095a` was asked instead (the bank puts order 195 seq 1 first).
- form sd re-entered at step 88 by `sd.sold_other` (order 274 seq 20), left after step 72, 15 between. Sorting: it was reachable (since step 1), and `s1a.carloan` was asked instead (the bank puts order 220 seq 1 first).
- form s3 re-entered at step 95 by `s3.foreign_any` (order 279 seq 1), left after step 75, 19 between. Sorting: it was reachable (since step 1), and `f5695.any` was asked instead (the bank puts order 230 seq 1 first).
- form scope re-entered at step 101 by `scope.foreign_shares` (order 287 seq 1), left after step 82, 18 between. Sorting: it was reachable (since step 1), and `$sc@person[taxpayer]` was asked instead (the bank puts order 250 seq 1 first).
- form s3 re-entered at step 102 by `s3.credit_bond` (order 290 seq 1), left after step 95, 6 between. Sorting: it was reachable (since step 1), and `sb.account_any` was asked instead (the bank puts order 285 seq 1 first).
- form s2 re-entered at step 106 by `s2.credit_recapture` (order 291 seq 1), left after step 57, 48 between. Sorting: it was reachable (since step 58), and `sa.sales_tax_wish` was asked instead (the bank puts order 201 seq 7 first).
- form scope re-entered at step 110 by `scope.reforestation` (order 295 seq 1), left after step 101, 8 between. Sorting: it was reachable (since step 1), and `s3.credit_bond` was asked instead (the bank puts order 290 seq 1 first).
- form f1040 re-entered at step 115 by `f1040.withheld_other_any` (order 300 seq 1), left after step 2, 112 between. Late: left for `household.ever_married` (order 2), which sorts earlier and was reachable only after the answer to `f1040.status` (step 2), which its gate does not read.
- form s3 re-entered at step 117 by `s3.line10` (order 305 seq 1), left after step 105, 11 between. Sorting: it was reachable (since step 1), and `s2.credit_recapture` was asked instead (the bank puts order 291 seq 1 first).
- form person re-entered at step 118 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 81, 36 between. Late: reachable only after the answer to `scope.business_before` (step 112), which its gate does not read.

**asset.industry = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**asset.listed = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**asset.software = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**dependent.ever_married = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**dependent.lived_all_year = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**div.any = true alone**: 123 questions, complete; order re-entries 5, form re-entries 27 sorting and 7 late, delayed children 1 sorting and 0 late.

- form sd re-entered at step 88 by `sd.distributions` (order 272 seq 4), left after step 72, 15 between. Late: reachable only after the answer to `div.any` (step 86), its parent or roster.
- form div re-entered at step 89 by `div.other_boxes` (order 272 seq 7), left after step 86, 2 between. Sorting: left for `sb.ordinary_dividends` (order 272 seq 2), a child of the question before it, which the bank places in another form.
- form sd re-entered at step 91 by `sd.sold_other` (order 274 seq 20), left after step 88, 2 between. Sorting: it was reachable (since step 1), and `div.other_boxes` was asked instead (the bank puts order 272 seq 7 first).
- form sb re-entered at step 101 by `sb.account_any` (order 285 seq 1), left after step 87, 13 between. Sorting: it was reachable (since step 1), and `sd.distributions` was asked instead (the bank puts order 272 seq 4 first).
- form s3 re-entered at step 107 by `s3.credit_bond` (order 290 seq 1), left after step 99, 7 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).
- `sd.f2439` (order 274 seq 28), step 96: child of `div.any` (step 86), 6 other questions between. Sorting: it was reachable (since step 87), and `$sales` was asked instead (within order 274, the block's entry and seq order put it first).

**eic.lived_with_relative = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**f1040.estimated_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**f1040.withheld_other_any = true alone**: 120 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**f4952.has_interest = true alone**: 121 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**f5695.any = true alone**: 135 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 11 sorting and 0 late.

- `f5695.insulation` (order 230 seq 8), step 83: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.doors` (order 230 seq 9), step 84: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.windows` (order 230 seq 10), step 85: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.panel` (order 230 seq 11), step 86: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.audit` (order 230 seq 12), step 87: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.heat_pump` (order 230 seq 13), step 88: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.hp_water_heater` (order 230 seq 14), step 89: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.central_ac` (order 230 seq 15), step 90: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.water_heater` (order 230 seq 16), step 91: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.furnace` (order 230 seq 17), step 92: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).
- `f5695.biomass` (order 230 seq 18), step 93: child of `f5695.any` (step 76), 1 other question between. Sorting: it was reachable (since step 77), and `f5695.line7a` was asked instead (within order 230, the block's entry and seq order put it first).

**f8889.coverage_year = "family" alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**f8889.coverage_year = "changed" alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**f8962.other_coverage = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**person.eligible_educator = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**person.ira_owner = true alone**: 120 questions, complete; order re-entries 6, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 1 late.

- order 180 re-entered at step 82 by `person[taxpayer].x_ira_prior_excess` (order 180 seq 9), left after step 52, 29 between. Late: reachable only after the answer to `person[taxpayer].x_archer_excess` (step 81), which its gate does not read.
- `person[taxpayer].x_ira_prior_excess` (order 180 seq 9), step 82: child of `person[taxpayer].ira_owner` (step 51), 29 other questions between. Late: reachable only after the answer to `person[taxpayer].x_archer_excess` (step 81), which its gate does not read.

**person.x_edu_account = true alone**: 120 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**qbi.prior_form = true alone**: 120 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**retirement.rollover_any = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.alaska_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.alimony_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.hobby_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.jury_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.scholarship_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.uc_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s1.winnings_any = true alone**: 121 questions, complete; order re-entries 6, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 1 late.

- order 160 re-entered at step 45 by `s1.olympic` (order 160 seq 17), left after step 41, 3 between. Late: reachable only after the answer to `s1.ltc_payout` (step 44), which its gate does not read.
- order 148 re-entered at step 46 by `s1.nqdc_pension` (order 148 seq 2), left after step 27, 18 between. Late: reachable only after the answer to `s1.olympic` (step 45), which its gate does not read.
- `s1.olympic` (order 160 seq 17), step 45: child of `s1.winnings_any` (step 37), 5 other questions between. Late: reachable only after the answer to `s1.ltc_payout` (step 44), which its gate does not read.

**s179.prior_form = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s2.household_help = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s2.options_any = true alone**: 120 questions, complete; order re-entries 6, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 1 late.

- order 149 re-entered at step 44 by `s1.stock_options` (order 149 seq 3), left after step 29, 14 between. Late: reachable only after the answer to `s1.ltc_payout` (step 43), which its gate does not read.
- order 148 re-entered at step 45 by `s1.nqdc_pension` (order 148 seq 2), left after step 27, 17 between. Late: reachable only after the answer to `s1.stock_options` (step 44), which its gate does not read.
- `s1.stock_options` (order 149 seq 3), step 44: child of `s2.options_any` (step 28), 14 other questions between. Late: reachable only after the answer to `s1.ltc_payout` (step 43), which its gate does not read.

**s3.adoption_any = true alone**: 121 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 1 sorting and 0 late.

- `scope.adoption_benefits` (order 127 seq 2), step 19: child of `s3.adoption_any` (step 15), 1 other question between. Sorting: it was reachable (since step 16), and `scope.f8814` was asked instead (within order 127, the block's entry and seq order put it first).

**s3.ev = true alone**: 121 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s3.farmland = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s3.foreign_any = true alone**: 123 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

- form s3 re-entered at step 107 by `s3.credit_bond` (order 290 seq 1), left after step 98, 8 between. Sorting: it was reachable (since step 1), and `ftc.taxes` was asked instead (the bank puts order 280 seq 1 first).

**s3.kerosene = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**s3.prior_other_forms = true alone**: 122 questions, complete; order re-entries 6, form re-entries 26 sorting and 7 late, delayed children 0 sorting and 0 late.

- order 290 re-entered at step 108 by `s3.prior_amt` (order 290 seq 6), left after step 105, 2 between. Sorting: left for `ftc.carryover` (order 10), a child of the question before it, which the bank places in another order number.
- form f5695 re-entered at step 107 by `f5695.carry` (order 239 seq 1), left after step 76, 30 between. Late: reachable only after the answer to `s3.prior_other_forms` (step 105), its parent or roster.
- form s3 re-entered at step 108 by `s3.prior_amt` (order 290 seq 6), left after step 105, 2 between. Sorting: left for `ftc.carryover` (order 10), a child of the question before it, which the bank places in another form.

**sa.gifts = true alone**: 120 questions, complete; order re-entries 5, form re-entries 26 sorting and 6 late, delayed children 0 sorting and 0 late.

- form sa re-entered at step 67 by `sa.medical_any` (order 203 seq 1), left after step 65, 1 between. Sorting: it was reachable (since step 60), and `$gift` was asked instead (the bank puts order 202 seq 5 first).

**sa.personal_property_tax_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sa.state_tax_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sa.state_tax_other_any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sc.employees = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sc.goods = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sc.travel_meals = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**scope.armed_forces = true alone**: 121 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**scope.business_before = true alone**: 121 questions, complete; order re-entries 6, form re-entries 25 sorting and 7 late, delayed children 1 sorting and 0 late.

- order 295 re-entered at step 117 by `scope.f8978` (order 295 seq 6), left after step 114, 2 between. Late: left for `qbi.prior_form` (order 262 seq 1), which sorts earlier and was reachable only after the answer to `scope.passive` (step 114), which its gate does not read.
- form scope re-entered at step 117 by `scope.f8978` (order 295 seq 6), left after step 114, 2 between. Late: left for `qbi.prior_form` (order 262 seq 1), which sorts earlier and was reachable only after the answer to `scope.passive` (step 114), which its gate does not read.
- form person re-entered at step 121 by `person[taxpayer].eic_ssn` (order 311 seq 4), left after step 81, 39 between. Late: reachable only after the answer to `scope.passive` (step 114), which its gate does not read.
- `scope.f8978` (order 295 seq 6), step 117: child of `scope.business_before` (step 112), 2 other questions between. Sorting: it was reachable (since step 113), and `qbi.prior_form` was asked instead (the bank puts order 262 seq 1 first).

**scope.foreign_shares = true alone**: 120 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**scope.noncitizen = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**scope.religious_work = true alone**: 120 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**scveh.others_use = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**scveh.smr_always = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sd.route_each = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sd.sold_other = true alone**: 121 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**sli.any = true alone**: 121 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**ssb.any = true alone**: 119 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**ssb.prior_year_pay = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

**tipjob.listed = true alone**: 118 questions, complete; order re-entries 5, form re-entries 25 sorting and 6 late, delayed children 0 sorting and 0 late.

